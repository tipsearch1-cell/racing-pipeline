"""Exploratory candidate X1 (NOT part of the confirmatory test): the hybrid form refitted on the previous-evening (21:00, E)
market: softmax(w1 log m_E + w2 sC + w3 log f). Fitted once on Mar-Oct 2026 replay data (all previously examined), frozen.
python3 freeze_x1.py -> models/x1_evening_2026-11-19.json"""
import hashlib, json, os, sys
import numpy as np, pandas as pd
HERE = os.path.dirname(os.path.abspath(__file__))
P4 = os.path.join(HERE, "..", "..", "model_reconstruction", "phase4")
sys.path.insert(0, P4)
import p4_models as P
EPS = 1e-9
P_ = pd.read_pickle(os.path.join(P4, "work", "preds.pkl"))
e = P_[P_.m_E.notna() & P_.sC.notna() & P_.f.notna() & ~P_.month.str.startswith("H3")].copy()
e = e[e.groupby("race_id").m_E.transform(lambda s: s.notna().all())].sort_values("race_id", kind="mergesort")
e["lmE"] = np.log(e.m_E.clip(EPS)); e["lf"] = np.log((e.f / e.groupby("race_id").f.transform("sum")).clip(EPS))
w = P.clogit_fit(e[["lmE", "sC", "lf"]].to_numpy(), e.y.values, e.race_id.values, l2=0.0, w0=np.array([1.0, 0.0, 0.0]))
rec = dict(name="X1 evening hybrid (exploratory)", weights=[float(x) for x in w], inputs=["log m_E (21:00 composite)", "sC (frozen C score)", "log f (production)"],
           fitted_on=f"{e.date.min()}..{e.date.max()} ({e.race_id.nunique()} races, replay S3)", uses_frozen_C_sha256="56179d9cf676d7d02a2ceb4e0cb484896057a4e0a9fbf8fcb5333bcc87178b52",
           status="EXPLORATORY ONLY - cannot affect the confirmatory D2/E test")
os.makedirs(os.path.join(HERE, "models"), exist_ok=True)
p = os.path.join(HERE, "models", "x1_evening_2026-11-19.json")
json.dump(rec, open(p, "w"), indent=1)
print(rec, hashlib.sha256(open(p, "rb").read()).hexdigest())
