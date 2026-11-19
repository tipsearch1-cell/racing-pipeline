"""Phase 2 experiments (spec prereg/HARVILLE_PHASE2_SPEC_2026-11-19.md).

  python3 research/harville/phase2/replay.py   # once
  python3 research/harville/phase2/run2.py     # -> phase2/work/*.csv.gz, phase2/out/*.csv, phase2/out/run2_log.md

Walk-forward: for each test month M in May..Oct 2026, every second-stage parameter (discounted-Harville exponents per
input, blend weights, enhanced-model coefficients) is fitted on replayed months Mar..M-1 only. Holdout = Sep-Oct.
G (genuine archive 10-18 Nov) is scored once with parameters fitted on all replayed months.
"""
import json, os, sys, time
import numpy as np
import pandas as pd
from scipy.optimize import minimize

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "research", "harville"))
from harville import clean, position_probs  # noqa: E402
from data import bf_places  # noqa: E402
from run import clogit_nll, hess, se  # noqa: E402  (Phase 1 conditional-logit code, unchanged)

W, OUT = os.path.join(HERE, "work"), os.path.join(HERE, "out")
TEST_MONTHS = ["2026-05", "2026-06", "2026-07", "2026-08", "2026-09", "2026-10"]
HOLDOUT = ("2026-09", "2026-10")
rng = np.random.default_rng(20261119)
EPS = 1e-6


# ------------------------------------------------------------------ races
def build_races(df, mcol, fcol):
    out = []
    for rid, g in df.groupby("race_id", sort=False):
        m = g[mcol].to_numpy(float); f = g[fcol].to_numpy(float)
        if len(g) < 3 or not (np.all(np.isfinite(m)) and np.all(np.isfinite(f))) or m.sum() <= 0 or f.sum() <= 0:
            continue
        pos = g.pos.to_numpy(float)
        fin = pos[np.isfinite(pos)]
        if len(fin) < 3 or (fin == 1).sum() != 1:
            continue
        clean123 = (fin == 1).sum() == 1 and (fin == 2).sum() == 1 and (fin == 3).sum() == 1
        n = len(g)
        hcap = bool(g.hcap.iloc[0])
        nnr = float(g.nnr.iloc[0]) if "nnr" in g else 0.0
        r = dict(race_id=rid, date=g.date.iloc[0], month=g.date.iloc[0][:7], n=n, hcap=hcap, code=g.code.iloc[0] if "code" in g else "?",
                 m=clean(m), f=clean(f), pos=pos, clean=clean123, places=bf_places(int(n + nnr), hcap),
                 psp=g.psp.to_numpy(float) if "psp" in g else np.full(n, np.nan),
                 placed_bf=g.placed_bf.to_numpy(float) if "placed_bf" in g else np.full(n, np.nan),
                 horse=g.horse.to_numpy() if "horse" in g else np.arange(n))
        r["i1"] = int(np.where(pos == 1)[0][0])
        r["i2"] = int(np.where(pos == 2)[0][0]) if (pos == 2).sum() == 1 else None
        r["i3"] = int(np.where(pos == 3)[0][0]) if clean123 else None
        F = {}
        for c in ("f_runs", "f_top3", "f_ps", "f_style", "f_lead", "f_ob", "f_clschg", "f_dist", "f_going"):
            F[c] = g[c].to_numpy(float) if c in g else np.full(n, np.nan)
        r["F"] = F
        out.append(r)
    return out


def blend(r, w):
    if w is None:
        return r["m"]
    lw = w[0] * np.log(r["m"]) + w[1] * np.log(r["f"])
    e = np.exp(lw - lw.max())
    return clean(e / e.sum())


def stage1(r, model, prm):
    return {"A": r["m"], "B": r["f"], "C": blend(r, prm.get("w")), "D": blend(r, prm.get("w")), "H": r["m"]}[model]


def dfeats(r, p, kind):
    lp = np.log(p); n = r["n"]
    ln = np.log(n) - np.log(10)
    if kind == "B5":
        return np.c_[lp, lp * ln]
    rank = np.argsort(np.argsort(-p))
    F = r["F"]
    def z(x, c, fill=0.0):
        return np.where(np.isfinite(x), x - c, fill)
    def na(x):
        return (~np.isfinite(x)).astype(float)
    return np.c_[lp, lp * ln, lp * (1.0 if r["hcap"] else 0.0), (rank == 0).astype(float), ((rank == 1) | (rank == 2)).astype(float),
                 z(F["f_style"], 2.5), na(F["f_style"]), z(F["f_lead"], 0.15),
                 z(F["f_top3"], 0.3), na(F["f_top3"]), np.log1p(np.nan_to_num(F["f_runs"])),
                 z(F["f_ps"], 0.5), z(np.log1p(np.clip(F["f_ob"], 0, 100)), 1.8), na(F["f_ob"]),
                 z(F["f_dist"], 0.5), na(F["f_dist"]), z(F["f_going"], 0.5), na(F["f_going"]), np.clip(np.nan_to_num(F["f_clschg"]), -3, 3)]


D_NAMES = ["lp", "lp*ln(n/10)", "lp*hcap", "fav", "rank2-3", "style", "style_na", "lead", "top3", "top3_na", "log_runs", "posscore",
           "log_btn", "btn_na", "dist_suit", "dist_na", "going_suit", "going_na", "class_change"]


def stage_sets(races, model, prm, kind, stage):
    X, y, gid, k = [], [], [], 0
    for r in races:
        if stage == 2:
            if r["i2"] is None: continue
            keep = np.ones(r["n"], bool); keep[r["i1"]] = False; ch = r["i2"]
        else:
            if r["i3"] is None: continue
            keep = np.ones(r["n"], bool); keep[[r["i1"], r["i2"]]] = False; ch = r["i3"]
        Fm = dfeats(r, stage1(r, model, prm), kind)
        yy = np.zeros(r["n"]); yy[ch] = 1
        X.append(Fm[keep]); y.append(yy[keep]); gid.append(np.full(keep.sum(), k)); k += 1
    return np.vstack(X), np.concatenate(y), np.concatenate(gid), k


def fit_clogit(X, y, gid, ng, l2, x0):
    o = minimize(clogit_nll, x0, args=(X, y, gid, ng, l2), jac=True, method="L-BFGS-B")
    Hm = hess(o.x, X, y, gid, ng)
    if l2:
        Hm = Hm + l2 * np.diag(np.r_[0.0, np.ones(len(o.x) - 1)])
    return o.x, se(Hm)


def fit_blend(races):
    X = np.vstack([np.c_[np.log(r["m"]), np.log(r["f"])] for r in races])
    y = np.concatenate([(np.arange(r["n"]) == r["i1"]).astype(float) for r in races])
    gid = np.concatenate([np.full(r["n"], i) for i, r in enumerate(races)])
    w, s = fit_clogit(X, y, gid, len(races), 0.0, np.array([1.0, 0.0]))
    # secondary: linear mixture lambda by grid
    best = None
    for lam in np.linspace(0, 1, 21):
        ll = sum(np.log(lam * r["f"][r["i1"]] + (1 - lam) * r["m"][r["i1"]]) for r in races)
        if best is None or ll > best[1]:
            best = (lam, ll)
    return w, s, best[0]


def fit_all(train):
    prm = {}
    w, s, lam = fit_blend(train)
    prm["w"], prm["w_se"], prm["lam"] = w, s, lam
    for model in ("A", "B", "C"):
        for st in (2, 3):
            X, y, gid, ng = stage_sets(train, model, prm, "B5", st)
            prm[f"{model}{st}"], _ = fit_clogit(X, y, gid, ng, 0.0, np.array([1.0, 0.0]))
    for st in (2, 3):
        X, y, gid, ng = stage_sets(train, "D", prm, "D", st)
        x0 = np.zeros(X.shape[1]); x0[0] = 1.0
        prm[f"D{st}"], prm[f"D{st}_se"] = fit_clogit(X, y, gid, ng, 1.0, x0)
    return prm


def probs(r, model, prm):
    p = stage1(r, model, prm)
    if model == "H":  # original Harville on market
        return p, p, p
    kind = "D" if model == "D" else "B5"
    Fm = dfeats(r, p, kind)
    l2 = Fm @ prm[f"{model}2"]; l3 = Fm @ prm[f"{model}3"]
    return p, np.exp(l2 - l2.max()), np.exp(l3 - l3.max())


def settle_frac(pos, k):
    frac = np.where(pos < k, 1.0, 0.0)
    eq = pos == k
    if eq.any():
        frac = np.where(eq, 1.0 / eq.sum(), frac)
    return frac


def score(races, prm, models=("H", "A", "B", "C", "D")):
    R, U = [], []
    for r in races:
        pos = r["pos"]; k = r["places"]
        PP = {}
        for mdl in models:
            p, w2, w3 = probs(r, mdl, prm)
            P = position_probs(p, w2, w3, w3, kmax=min(4, r["n"]))
            PP[mdl] = P
            P2 = P[:, :2].sum(1); P3 = P[:, :3].sum(1)
            row = dict(model=mdl, race_id=r["race_id"], date=r["date"], month=r["month"], n=r["n"], code=r["code"], hcap=r["hcap"], nr=r["n"],
                       brier2=np.sum((P2 - (pos <= 2)) ** 2), brier3=np.sum((P3 - (pos <= 3)) ** 2), ll_win=-np.log(p[r["i1"]]))
            if r["i2"] is not None:
                row["ll_ex"] = row["ll_win"] - np.log(w2[r["i2"]] / (w2.sum() - w2[r["i1"]]))
            if r["clean"]:
                row["ll_tri"] = row["ll_ex"] - np.log(w3[r["i3"]] / (w3.sum() - w3[r["i1"]] - w3[r["i2"]]))
            R.append(row)
        rank = np.argsort(np.argsort(-r["m"])) + 1
        frac = settle_frac(np.where(np.isfinite(pos), pos, 99), k) if k else np.zeros(r["n"])
        psp = r["psp"]
        imp = 1 / psp
        impn = imp * k / np.nansum(imp) if k and np.isfinite(imp).all() else np.full(r["n"], np.nan)
        for i in range(r["n"]):
            row = dict(race_id=r["race_id"], date=r["date"], month=r["month"], n=r["n"], code=r["code"], hcap=r["hcap"], places=k, rank=rank[i],
                       m=r["m"][i], f=r["f"][i], pos=pos[i], frac=frac[i], psp=psp[i], imp_psp=impn[i], horse=r["horse"][i])
            for mdl in models:
                P = PP[mdl]
                row[f"P2_{mdl}"] = P[i, 1] if P.shape[1] > 1 else 0
                row[f"P3_{mdl}"] = P[i, 2] if P.shape[1] > 2 else 0
                row[f"Pk_{mdl}"] = P[i, :k].sum() if k else np.nan
                row[f"T3_{mdl}"] = P[i, :3].sum()
            U.append(row)
    return pd.DataFrame(R), pd.DataFrame(U)


def main():
    os.makedirs(OUT, exist_ok=True)
    S = pd.read_pickle(os.path.join(W, "S.pkl"))
    S = S[S.eligible]
    log = ["# Phase 2 run log", ""]
    allR, allU, params = [], [], {}
    races = build_races(S, "p", "pm")
    by_month = {}
    for r in races:
        by_month.setdefault(r["month"], []).append(r)
    log.append(f"S eligible races after result checks: {len(races):,}; by month " + json.dumps({k: len(v) for k, v in sorted(by_month.items())}))
    for M in TEST_MONTHS:
        t0 = time.time()
        train = [r for r in races if r["month"] < M]
        test = by_month.get(M, [])
        prm = fit_all(train)
        params[M] = {k: (v.tolist() if hasattr(v, "tolist") else v) for k, v in prm.items()}
        R, U = score(test, prm)
        allR.append(R); allU.append(U)
        log.append(f"- test {M}: train {len(train):,} races, test {len(test):,}; blend w(market, model) = {np.round(prm['w'], 3).tolist()} "
                   f"(se {np.round(prm['w_se'], 3).tolist()}, z model = {prm['w'][1] / prm['w_se'][1]:.1f}); linear lambda(model) = {prm['lam']:.2f}; "
                   f"B5 A {np.round(prm['A2'], 3).tolist()}/{np.round(prm['A3'], 3).tolist()} B {np.round(prm['B2'], 3).tolist()}/{np.round(prm['B3'], 3).tolist()} ({time.time() - t0:.0f}s)")
    R = pd.concat(allR); U = pd.concat(allU)
    R.to_csv(os.path.join(W, "S_races.csv.gz"), index=False); U.to_csv(os.path.join(W, "S_runners.csv.gz"), index=False)
    # final params on all replayed months -> G
    prmG = fit_all(races)
    params["final_for_G"] = {k: (v.tolist() if hasattr(v, "tolist") else v) for k, v in prmG.items()}
    json.dump(params, open(os.path.join(OUT, "params.json"), "w"), indent=1)
    log.append(f"- final (all replayed months, {len(races):,} races): blend w = {np.round(prmG['w'], 3).tolist()} se {np.round(prmG['w_se'], 3).tolist()}")
    log.append("- D coefficients stage 2: " + ", ".join(f"{n} {v:+.3f} ({s:.3f})" for n, v, s in zip(D_NAMES, prmG["D2"], prmG["D2_se"])))
    log.append("- D coefficients stage 3: " + ", ".join(f"{n} {v:+.3f} ({s:.3f})" for n, v, s in zip(D_NAMES, prmG["D3"], prmG["D3_se"])))
    G = pd.read_pickle(os.path.join(W, "G.pkl"))
    G = G[G.p_model.notna() & G.mkt.notna()].copy()
    G = G[G.groupby("race_id").p_model.transform("size") == G.groupby("race_id").horse_id.transform("size")]
    G["mm"] = G.mkt / G.groupby("race_id").mkt.transform("sum")
    G["code"] = np.where(G.code == "Flat", "Flat", "Jumps")
    G["placed_bf"] = np.nan
    gr = build_races(G, "mm", "p_model")
    RG, UG = score(gr, prmG)
    RG.to_csv(os.path.join(W, "G_races.csv.gz"), index=False); UG.to_csv(os.path.join(W, "G_runners.csv.gz"), index=False)
    # reviewer-as-input variant on G (B uses the sealed reviewer chance)
    G2 = G[G.rev.notna()].copy(); G2["rv"] = G2.rev / G2.groupby("race_id").rev.transform("sum")
    gr2 = build_races(G2, "mm", "rv")
    RG2, UG2 = score(gr2, prmG, models=("A", "B", "C"))
    RG2.to_csv(os.path.join(W, "G_rev_races.csv.gz"), index=False); UG2.to_csv(os.path.join(W, "G_rev_runners.csv.gz"), index=False)
    log.append(f"- G: {len(gr)} races scored (model input); reviewer-input variant {len(gr2)} races")
    open(os.path.join(OUT, "run2_log.md"), "w").write("\n".join(log) + "\n")
    print("\n".join(log))


if __name__ == "__main__":
    main()
