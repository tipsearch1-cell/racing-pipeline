"""How close is the rebuilt pipeline to the old one?  python3 pipeline/compare_old.py 2026-10-26 2026-11-09

Runs the rebuilt models (out-of-sample coefficients, trained to 25 Oct) over the recovered sealed cards and compares
them with the old pipeline's published outputs in report/history_data.json: win-model top pick, chance correlation,
run style, race shape; then scores both models on the actual winners (history table) and BSP.
Writes data/rebuild_vs_old.csv (per runner) and prints a summary.
"""
import json, os, sys
import numpy as np
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import p, load_card  # noqa: E402
from history import load as load_hist, norm  # noqa: E402
from models import run_day, pos_num  # noqa: E402


def main(d0, d1):
    old = json.load(open(p("report", "history_data.json")))
    oldrep = {r["day"]: r for r in old["reports"]}
    H = load_hist()
    res = H[H.src == "api"].assign(hk=H.hkey)
    win = {(r.race_id, r.hk): (pos_num(r.pos) == 1, r.bsp) for r in res.itertuples()}
    rows, races = [], []
    for day in pd.date_range(d0, d1).strftime("%Y-%m-%d"):
        if day not in oldrep or not os.path.exists(p("store", day, "sealed_card.json.gz")):
            continue
        card = load_card(day)
        new = run_day(day, card, oos=True)
        oraces = {r["race_id"]: r for r in oldrep[day]["races"]}
        for r in card:
            o = oraces.get(r["race_id"])
            n = new["races"][r["race_id"]]
            if not o:
                continue
            ob = {norm(x["horse"]): x for x in o["runners"]}
            for h in r["runners"]:
                x = n["runners"][h["horse_id"]]
                y = ob.get(norm(h["horse"]))
                if y is None:
                    continue
                w = win.get((r["race_id"], norm(h["horse"])), (None, None))
                rows.append({"day": day, "race_id": r["race_id"], "code": o.get("code"), "horse": h["horse"], "p_new": x["p"],
                             "p_old": y.get("p"), "mkt": y.get("mkt"), "style_new": x["style"], "lead_new": x["lead"], "sc": x["sc"], "nled": x["nled"], "ncls": x["ncls"], "lead_old": y.get("lead"), "style_old": y.get("style"),
                             "won": w[0], "bsp": w[1]})
            races.append({"day": day, "race_id": r["race_id"], "shape_new": n["shape"]["label"], "shape_old": (o.get("shape") or {}).get("label")})
    d = pd.DataFrame(rows)
    d.to_csv(p("data", "rebuild_vs_old.csv"), index=False)
    R = pd.DataFrame(races)
    d = d[d.p_old.notna()]
    d["p_old_n"] = d.p_old / d.groupby("race_id").p_old.transform("sum")
    d["p_new_n"] = d.p_new / d.groupby("race_id").p_new.transform("sum")
    print(f"Compared {d.race_id.nunique()} races / {len(d)} runners, {d.day.min()} to {d.day.max()}")
    for code in ["All", "Flat", "Jumps"]:
        x = d if code == "All" else d[d.code == code]
        if not len(x):
            continue
        tn = x.loc[x.groupby("race_id").p_new_n.idxmax()]
        to = x.loc[x.groupby("race_id").p_old_n.idxmax()]
        same = (tn.set_index("race_id").horse == to.set_index("race_id").horse).mean()
        print(f"\n{code}: {x.race_id.nunique()} races")
        print(f"  same top pick as old model: {same:.0%}")
        print(f"  correlation of win chances new vs old: {np.corrcoef(x.p_new_n, x.p_old_n)[0, 1]:.2f}  "
              f"(old vs market {np.corrcoef(x.p_old_n, x.mkt.fillna(0))[0, 1]:.2f}, new vs market {np.corrcoef(x.p_new_n, x.mkt.fillna(0))[0, 1]:.2f})")
        s = x[x.won.notna()]
        s = s[s.groupby("race_id").won.transform("sum") == 1]
        if len(s):
            for lab, col in (("old", "p_old_n"), ("new", "p_new_n")):
                t = s.loc[s.groupby("race_id")[col].idxmax()]
                ll = -np.log(s[s.won == True][col].clip(1e-4)).mean()  # noqa: E712
                roi = np.where(t.won == True, (t.bsp - 1) * 0.98, -1)  # noqa: E712
                print(f"  {lab} model: log-loss {ll:.3f}; top pick won {t.won.mean():.0%} of {len(t)}; top pick at BSP {np.nanmean(roi):+.1%}")
            mk = s[s.mkt.notna()]
            mk = mk.assign(m=mk.mkt / mk.groupby("race_id").mkt.transform("sum"))
            print(f"  09:00 market: log-loss {-np.log(mk[mk.won == True].m.clip(1e-4)).mean():.3f}")  # noqa: E712
    k = d[(d.style_old.notna()) & (d.style_old != "Unknown") & (d.style_new != "Unknown")]
    print(f"\nRun style: both known for {len(k)} runners; same label {(k.style_old == k.style_new).mean():.0%}; "
          f"within one step {(abs(k.style_old.map({'Leader': 4, 'Prominent': 3, 'Midfield': 2, 'Held up': 1}) - k.style_new.map({'Leader': 4, 'Prominent': 3, 'Midfield': 2, 'Held up': 1})) <= 1).mean():.0%}")
    print(f"Styles known: old {(d.style_old.fillna('Unknown') != 'Unknown').mean():.0%}, new {(d.style_new != 'Unknown').mean():.0%}")
    print(f"Race shape: same label {(R.shape_new == R.shape_old).mean():.0%} of {len(R)} races")
    print(pd.crosstab(R.shape_old, R.shape_new))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
