"""Phase 4 ranking diagnostics (hypotheses A-F) on a fixed development split.
  train: history races before 1 Jul 2026; test: Jul-Aug 2026 S3 races (development evidence only).
  python3 research/model_reconstruction/phase4/p4_diag.py -> out/diagnostics.json, out/ablation.csv
"""
import json, os, sys
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import p4_models as P  # noqa: E402
from p4_run import load, Xof  # noqa: E402

OUT = os.path.join(HERE, "out")
EPS = 1e-9


def ll_of(p, y):
    return -np.log(np.clip(p[y == 1], EPS, 1)).mean()


def fit_pred_linear(tr, te, cols, l2=1.0, by_code=True):
    st, g = P.groups(te.race_id.values)
    s = np.zeros(len(te))
    codes = (False, True) if by_code else (None,)
    for jm in codes:
        a = tr if jm is None else tr[tr.jumps == jm]
        sel = np.ones(len(te), bool) if jm is None else (te.jumps_f.values == float(jm))
        w = P.clogit_fit(Xof(a, cols), a.y.values, a.race_key.values, l2=l2)
        s[sel] = Xof(te[sel], cols) @ w
    return P.softmax_g(s, st, g), s


def concordance(df, col):
    c = t = 0
    for _, g in df.groupby("race_id"):
        w = g.loc[g.y == 1, col].to_numpy(); l = g.loc[g.y == 0, col].to_numpy()
        if len(w) == 1:
            c += (l < w[0]).sum() + 0.5 * (l == w[0]).sum(); t += len(l)
    return c / t


def main():
    F, E, feats = load()
    G = json.load(open(os.path.join(HERE, "work", "groups.json")))
    tr = F[F.trainable & (F.date < "2026-07-01")].sort_values("race_key", kind="mergesort")
    te = E[E.month.isin(["2026-07", "2026-08"])].sort_values("race_id", kind="mergesort").reset_index(drop=True)
    y = te.y.values
    st, g = P.groups(te.race_id.values)
    res = {"split": "train history < 2026-07-01; test Jul-Aug 2026 S3 races", "test_races": int(te.race_id.nunique()), "train_races": int(tr.race_key.nunique())}
    res["market_ll"] = ll_of(te.m_M.values, y); res["baseline_ll"] = ll_of(te.f.values, y)
    g0 = G["relative"]["G0"]
    # F compression: production l2 vs none; temperature
    p1, s1 = fit_pred_linear(tr, te, g0, l2=1.0); p0, s0 = fit_pred_linear(tr, te, g0, l2=0.0)
    res["F_compression"] = {"G0_l2_1": ll_of(p1, y), "G0_l2_0": ll_of(p0, y)}
    a = P.temperature_fit(np.log(te.f.clip(EPS).values), y, te.race_id.values)
    res["F_compression"]["baseline_best_temperature_on_test (oracle)"] = a
    res["F_compression"]["baseline_ll_at_oracle_temperature"] = ll_of(P.softmax_g(a * np.log(te.f.clip(EPS).values), st, g), y)
    res["F_compression"]["sum_to_one_max_err"] = float(np.abs(np.add.reduceat(te.f.values, st) - 1).max())
    # entropy check (D) by field size
    ent = []
    for lab, lo, hi in (("<=7", 0, 7), ("8-11", 8, 11), ("12-15", 12, 15), ("16+", 16, 99)):
        sel = te.groupby("race_id").race_id.transform("size").between(lo, hi)
        d = te[sel]
        H = lambda c: float((-(d[c] * np.log(d[c].clip(EPS))).groupby(d.race_id).sum()).mean())  # noqa: E731
        ent.append(dict(field=lab, races=int(d.race_id.nunique()), entropy_model=H("f"), entropy_market=H("m_M"), entropy_bsp=H("close"),
                        ll_model=ll_of(d.f.values, d.y.values), ll_market=ll_of(d.m_M.values, d.y.values)))
    res["D_field_entropy"] = ent
    # D: temperature per field band fitted on TRAIN baseline-equivalent (G0 refit) scores
    trp, trs = fit_pred_linear(tr, tr.assign(race_id=tr.race_key, jumps_f=tr.jumps.astype(float)), g0)
    nb_tr = pd.cut(tr.n, [0, 7, 11, 15, 99], labels=False).values; nb_te = pd.cut(te.groupby("race_id").race_id.transform("size"), [0, 7, 11, 15, 99], labels=False).values
    s_adj = s1.copy()
    for b in range(4):
        m_tr = nb_tr == b
        if m_tr.sum():
            ab = P.temperature_fit(trs[m_tr], tr.y.values[m_tr], tr.race_key.values[m_tr])
            s_adj[nb_te == b] = ab * s1[nb_te == b]
    res["D_field_temperature"] = {"ll_before": ll_of(p1, y), "ll_after": ll_of(P.softmax_g(s_adj, st, g), y)}
    # B objective: runner-level logistic vs race softmax vs pairwise (same G0 features, pooled codes)
    lr = LogisticRegression(C=1.0, max_iter=2000).fit(Xof(tr, g0 + ["jumps_f"]), tr.y.values)
    pr = lr.predict_proba(Xof(te, g0 + ["jumps_f"]))[:, 1]
    pr_n = pr / np.add.reduceat(pr, st)[g]
    pw = P.PairwiseGBM(depth=1, lr=0.2, n_max=120, min_leaf=500, seed=1).fit(Xof(tr, g0), tr.posn.values, tr.race_key.values)
    sp = pw.score(Xof(tr, g0)); at = P.temperature_fit(sp, tr.y.values, tr.race_key.values)
    pp = P.softmax_g(at * pw.score(Xof(te, g0)), st, g)
    pls, _ = fit_pred_linear(tr, te, g0, by_code=False)
    res["B_objective"] = {"runner_logistic_then_normalised": ll_of(pr_n, y), "race_softmax_listwise": ll_of(pls, y), "pairwise_stumps": ll_of(pp, y)}
    # A relative vs absolute features (same groups)
    rel = sum(G["relative"].values(), []); ab = G["relative"]["G0"] + sum(G["absolute"].values(), [])
    abs_cols = [c for c in ab if c not in te.columns and c in F.columns]
    tr2 = tr.copy(); te2 = te.merge(F[["k"] + abs_cols].drop_duplicates("k"), on="k", how="left")
    for c in ab:
        if c not in tr2:
            continue
        med = tr2[c].median(); tr2[c] = tr2[c].fillna(med); te2[c] = te2[c].fillna(med)
    prel, _ = fit_pred_linear(tr, te, rel); pab, _ = fit_pred_linear(tr2, te2, [c for c in ab if c in tr2])
    te["p_rel"] = prel
    bands = pd.qcut(te.m_M.rank(method="first"), 5, labels=False)
    res["A_relative_vs_absolute"] = {"all_relative_features": ll_of(prel, y), "absolute_features": ll_of(pab, y)}
    res["A_concordance"] = {"market": concordance(te, "m_M"), "baseline": concordance(te, "f"), "all_relative": concordance(te, "p_rel"),
                            "within_market_quintile": {str(b): {"market": concordance(te[bands == b], "m_M"), "baseline": concordance(te[bands == b], "f"),
                                                                 "all_relative": concordance(te[bands == b], "p_rel")} for b in range(5)}}
    # E population: last 3 months only vs expanding; pooled vs per code
    tr3 = tr[tr.date >= "2026-04-01"]
    p3m, _ = fit_pred_linear(tr3, te, rel); ppool, _ = fit_pred_linear(tr, te, rel, by_code=False)
    res["E_population"] = {"expanding_Jan_Jun_per_code": ll_of(prel, y), "last3months_Apr_Jun": ll_of(p3m, y), "pooled_codes": ll_of(ppool, y)}
    # C feature ablation (linear race softmax, per code)
    rows = [dict(set="G0 (production features)", ll=ll_of(p1, y))]
    for k in ("G1", "G2", "G3", "G4", "G5", "G6", "G7"):
        pk, _ = fit_pred_linear(tr, te, g0 + G["relative"][k]); rows.append(dict(set=f"G0 + {k}", ll=ll_of(pk, y)))
    rows.append(dict(set="all G0-G7", ll=ll_of(prel, y)))
    for k in ("G0", "G1", "G2", "G3", "G4", "G5", "G6", "G7"):
        cols = [c for c in rel if c not in G["relative"][k]]
        pk, _ = fit_pred_linear(tr, te, cols); rows.append(dict(set=f"all minus {k}", ll=ll_of(pk, y)))
    ab_df = pd.DataFrame(rows); ab_df["gain_vs_G0"] = ab_df.ll.iloc[0] - ab_df.ll; ab_df["gap_to_market"] = ab_df.ll - res["market_ll"]
    ab_df.to_csv(os.path.join(OUT, "ablation.csv"), index=False)
    json.dump(res, open(os.path.join(OUT, "diagnostics.json"), "w"), indent=1, default=float)
    print(json.dumps(res, indent=1, default=float)); print(ab_df.round(4).to_string())


if __name__ == "__main__":
    main()
