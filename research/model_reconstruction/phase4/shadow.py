"""Phase 4 prospective shadow test (research only; never feeds the bot).

  python3 shadow.py freeze                 # fit and freeze D2 + E on all data before 19 Nov 2026 (run once)
  python3 shadow.py predict DAY [--dry]    # after the 08:35 build is published: frozen D2/E chances for DAY's sealed card
  python3 shadow.py score                  # paired log-loss vs the 09:00 market over all settled shadow days

Predictions are written once (write-once + chained manifest) into the forward archive
research/market_intelligence/phase3/archive/archive_data/<DAY>/shadow_phase4.json.gz and should be committed to git
before the first off; the commit time is the provenance. Spec: prereg/MODEL_RECON_PHASE4_SPEC_2026-11-19.md (+ Amendment 1).
"""
import datetime as dt, glob, gzip, hashlib, json, os, pickle, subprocess, sys
import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "pipeline"))
sys.path.insert(0, os.path.join(ROOT, "research", "harville"))
sys.path.insert(0, os.path.join(ROOT, "research", "market_intelligence", "phase3", "archive"))
import p4_models as P  # noqa: E402

FROZEN = os.path.join(HERE, "models", "frozen_2026-11-19.pkl")
FREEZE_CUTOFF = "2026-11-19"
EPS = 1e-9


def freeze():
    from p4_run import load, Xof, CFG
    F, E, feats = load()
    F = F[F.date < FREEZE_CUTOFF]
    cols = feats + ["jumps_f"]
    tr = F[F.trainable].sort_values("race_key", kind="mergesort")
    fp, va = tr[tr.date < "2026-10-19"], tr[tr.date >= "2026-10-19"]
    C = P.ListwiseGBM(**CFG["C"], seed=CFG["seed"], max_features=CFG["max_features"]).fit(
        Xof(fp, cols), fp.y.values, fp.race_key.values, Xv=Xof(va, cols), yv=va.y.values, racev=va.race_key.values, patience=CFG["patience"])
    preds = pd.read_pickle(os.path.join(HERE, "work", "preds.pkl"))
    ev = preds[preds.close.notna() | ~preds.month.str.startswith("H3")].sort_values("race_id", kind="mergesort")
    ev = ev[ev.month >= "2026-03"]
    ev["lm"] = np.log(ev.m_M.clip(EPS)); ev["lf"] = np.log(ev.f.clip(EPS))
    a, v = ev[ev.date < "2026-10-19"], ev[ev.date >= "2026-10-19"]
    D2 = P.ListwiseGBM(**CFG["D2"], seed=CFG["seed"], max_features=CFG["max_features"]).fit(
        Xof(a, cols), a.y.values, a.race_id.values, offset=a.lm.values, Xv=Xof(v, cols), yv=v.y.values, racev=v.race_id.values, offv=v.lm.values, patience=CFG["patience"])
    e = ev[ev.sC.notna()]
    wE = P.clogit_fit(e[["lm", "sC", "lf"]].to_numpy(), e.y.values, e.race_id.values, l2=0.0, w0=np.array([1.0, 0.0, 0.0]))
    os.makedirs(os.path.dirname(FROZEN), exist_ok=True)
    meta = dict(frozen_at_utc=dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"), training_cutoff=f"history before {FREEZE_CUTOFF}",
                features=feats, C_trees=len(C.trees), D2_trees=len(D2.trees), E_weights=wE.tolist(), cfg=CFG)
    pickle.dump(dict(C=C, D2=D2, wE=wE, meta=meta), open(FROZEN, "wb"))
    h = hashlib.sha256(open(FROZEN, "rb").read()).hexdigest()
    json.dump(dict(meta, sha256=h), open(FROZEN.replace(".pkl", ".json"), "w"), indent=1, default=str)
    print("frozen", h, meta["C_trees"], meta["D2_trees"], np.round(wE, 3).tolist())


def claim(jockey):
    """Card weights are before the jockey's claim; results (training) weights are after it. '(3)' -> 3 lb."""
    import re
    m = re.search(r"\((\d+)\)\s*$", str(jockey or ""))
    return float(m.group(1)) if m else 0.0


def card_rows(day):
    from common import load_json, race_market
    from data import norm
    card = load_json(os.path.join(ROOT, "store", day, "sealed_card.json.gz"))
    races = card["racecards"] if isinstance(card, dict) else card
    rows, mkt = [], {}
    for r in races:
        for hid, x in race_market(r).items():
            mkt[(r["race_id"], hid)] = (x.get("mkt") or np.nan) / 100
        typ = r.get("type") or ""
        for h in r["runners"]:
            rows.append(dict(date=day, race_key=r["race_id"], race_id=r["race_id"], course=r["course"], type="Flat" if typ == "Flat" else (typ or "Hurdle"),
                             n=len(r["runners"]), horse=h["horse"], hkey=norm(h["horse"]), horse_id=h["horse_id"], pos=None, bsp=None, fig=None, spd=None,
                             comment=None, btn=None, ovr_btn=None, sp=None, src="card", race_name=r.get("race_name"),
                             **{"or": pd.to_numeric(h.get("ofr"), errors="coerce")}, lbs=pd.to_numeric(h.get("lbs"), errors="coerce") - claim(h.get("jockey")),
                             dist_f=pd.to_numeric(str(r.get("distance_f") or "").rstrip("f"), errors="coerce"), going=r.get("going"), cls=r.get("race_class"),
                             surface=r.get("surface"), trainer=h.get("trainer"), jockey=h.get("jockey")))
    return pd.DataFrame(rows), mkt


def predict(day, dry=False, out_dir=None):
    import collector as COL
    from p4_features import build
    fz = pickle.load(open(FROZEN, "rb"))
    sha = hashlib.sha256(open(FROZEN, "rb").read()).hexdigest()
    extra, mkt = card_rows(day)
    T, groups = build(extra=extra, upto=day)
    feats = fz["meta"]["features"]
    T[feats] = T[feats].astype(float).fillna(0.0)
    T["jumps_f"] = T.type.isin(["Hurdle", "Chase", "NH Flat"]).astype(float) if "type" in T else 0.0
    mp = json.load(open(os.path.join(ROOT, "store", day, "model.json")))
    T["f"] = [mp["races"].get(r, {}).get("runners", {}).get(h, {}).get("p", np.nan) for r, h in zip(T.race_id, T.horse_id)]
    T["m"] = [mkt.get((r, h), np.nan) for r, h in zip(T.race_id, T.horse_id)]
    T = T[T.groupby("race_id").m.transform(lambda s: s.notna().all()) & T.groupby("race_id").f.transform(lambda s: s.notna().all())]
    T = T.sort_values("race_id", kind="mergesort").reset_index(drop=True)
    st, g = P.groups(T.race_id.values)
    m = T.m.values / np.add.reduceat(T.m.values, st)[g]; f = T.f.values / np.add.reduceat(T.f.values, st)[g]
    lm, lf = np.log(np.clip(m, EPS, 1)), np.log(np.clip(f, EPS, 1))
    X = T[feats + ["jumps_f"]].to_numpy(float)
    pD2 = P.softmax_g(fz["D2"].score(X, offset=lm), st, g)
    sC = fz["C"].score(X)
    pE = P.softmax_g(np.c_[lm, sC, lf] @ fz["wE"], st, g)
    rows = [dict(race_id=r, horse_id=h, m_0900=round(float(a), 6), p_existing=round(float(b), 6), p_D2=round(float(c), 6), p_E=round(float(d), 6))
            for r, h, a, b, c, d in zip(T.race_id, T.horse_id, m, f, pD2, pE)]
    rec = dict(day=day, created_utc=dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"), frozen_model_sha256=sha,
               training_cutoff=fz["meta"]["training_cutoff"], spec="prereg/MODEL_RECON_PHASE4_SPEC_2026-11-19.md (+Amendment 1)",
               market="09:00 composite from store/DAY/sealed_card.json.gz", races=int(T.race_id.nunique()), rows=rows, dry_run=bool(dry))
    cfg = COL.load_config(os.path.join(ROOT, "research", "market_intelligence", "phase3", "archive", "config.json"))
    if out_dir:
        cfg["out_dir"] = out_dir
    ok = COL.write_once(cfg, day, "shadow_phase4.json.gz" if not dry else "shadow_phase4_DRYRUN.json.gz", rec, rec["created_utc"])
    print(f"shadow {day}: {rec['races']} races, {len(rows)} runners; written={ok}; frozen {sha[:12]}")
    return rec


def score():
    from common import load_json
    out = []
    for fp in sorted(glob.glob(os.path.join(ROOT, "research", "market_intelligence", "phase3", "archive", "archive_data", "*", "shadow_phase4.json.gz"))):
        rec = json.loads(gzip.decompress(open(fp, "rb").read()))
        rp = os.path.join(ROOT, "store", rec["day"], "results_all.json.gz")
        if not os.path.exists(rp):
            continue
        win = {(r["race_id"], h["horse_id"]) for r in load_json(rp)["results"] for h in r["runners"] if str(h.get("position")) == "1"}
        d = pd.DataFrame(rec["rows"]); d["y"] = [(r, h) in win for r, h in zip(d.race_id, d.horse_id)]
        d = d[d.groupby("race_id").y.transform("sum") == 1]
        d["day"] = rec["day"]; out.append(d)
    if not out:
        print("no settled shadow days yet"); return
    d = pd.concat(out); w = d[d.y]
    for col in ("p_D2", "p_E", "p_existing"):
        x = np.log(w[col].clip(EPS)) - np.log(w.m_0900.clip(EPS))
        print(f"{col}: {w.race_id.nunique()} races, mean log-loss gain vs 09:00 market {x.mean():+.4f}")


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "freeze":
        freeze()
    elif cmd == "predict":
        predict(sys.argv[2], dry="--dry" in sys.argv)
    elif cmd == "score":
        score()
