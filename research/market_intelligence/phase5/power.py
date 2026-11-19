"""Phase 5 power analysis from historical (development / re-used) paired differences. Uses no forward outcome.
python3 power.py  -> out/power.json, out/power_table.csv"""
import json, os
import numpy as np, pandas as pd
from scipy.stats import norm
HERE = os.path.dirname(os.path.abspath(__file__))
PREDS = os.path.join(HERE, "..", "..", "model_reconstruction", "phase4", "work", "preds.pkl")
EPS = 1e-9
ALPHA1 = 0.0125          # one-sided per model = lower bound of a two-sided 97.5% interval (Bonferroni over E and D2)
POWER = 0.80
RNG = np.random.default_rng(20261120)


def race_diffs(P):
    w = P[P.y == 1].copy()
    out = pd.DataFrame({"date": w.date.values, "race_id": w.race_id.values, "month": w.month.values})
    for c in ("pE", "pD2"):
        out[c] = np.log(w[c].clip(EPS).values) - np.log(w.m_M.clip(EPS).values)
    return out


def summarise(d, col):
    x = d[col].to_numpy(); n = len(x); sd = x.std(ddof=1)
    g = d.groupby("date")[col].agg(["sum", "size"])
    k = g["size"].mean()
    # design effect = var(day mean-weighted) / iid var: var of day sums / (mean races per day * per-race var)
    deff = g["sum"].var(ddof=1) / (g["size"].mean() * sd ** 2)
    return dict(n_races=n, n_days=len(g), races_per_day=round(k, 1), mean=round(x.mean(), 5), sd=round(sd, 4), deff=round(deff, 3))


def n_required(sd, deff, delta, z_crit):
    return int(np.ceil(((z_crit + norm.ppf(POWER)) * sd * np.sqrt(deff) / delta) ** 2))


def obf_boundaries(fracs, sims=2_000_000):
    """Lan-DeMets O'Brien-Fleming alpha spending (one-sided ALPHA1) at information fractions fracs (last = 1).
    Returns critical z per look, found sequentially by Monte Carlo on the canonical joint normal."""
    fr = np.asarray(fracs, float)
    spend = 2 * (1 - norm.cdf(norm.ppf(1 - ALPHA1 / 2) / np.sqrt(fr)))
    inc = np.diff(np.r_[0, fr])
    W = np.cumsum(RNG.standard_normal((sims, len(fr))) * np.sqrt(inc), axis=1)
    Z = W / np.sqrt(fr)
    alive = np.ones(sims, bool); crit = []
    for k in range(len(fr)):
        target = spend[k] - (spend[k - 1] if k else 0.0)
        zk = Z[alive, k]
        need = target * sims
        if need < 1:
            c = np.inf
        else:
            c = float(np.sort(zk)[::-1][int(need) - 1]) if need <= len(zk) else -np.inf
        crit.append(c); alive[alive] = ~(zk > c)
    return crit, spend.tolist()


def obf_two_look(info1):
    """Lan-DeMets O'Brien-Fleming spending, one-sided ALPHA1, looks at information fractions info1 and 1. Returns (c1, c2)."""
    a1 = 2 * (1 - norm.cdf(norm.ppf(1 - ALPHA1 / 2) / np.sqrt(info1)))
    c1 = norm.ppf(1 - a1)
    rho = np.sqrt(info1)
    z = RNG.standard_normal((2_000_000, 2)); z1 = z[:, 0]; z2 = rho * z1 + np.sqrt(1 - rho ** 2) * z[:, 1]
    lo, hi = 1.5, 4.0
    for _ in range(60):
        c2 = (lo + hi) / 2
        p = np.mean((z1 > c1) | (z2 > c2))
        lo, hi = (c2, hi) if p > ALPHA1 else (lo, c2)
    return float(c1), float(c2), float(a1)


def sim_power(d, col, n_races, delta, c, info1=None, c1=None, reps=2000):
    """Day-block resampling simulation: shift the historical per-race differences to mean=delta, draw whole days."""
    days = [g[col].to_numpy() - d[col].mean() + delta for _, g in d.groupby("date")]
    sizes = np.array([len(x) for x in days])
    hits = 0
    for _ in range(reps):
        tot, s, ss_days, idx = 0, [], [], []
        while tot < n_races:
            j = RNG.integers(len(days)); s.append(days[j]); tot += len(days[j])
        allx = np.concatenate(s); sums = np.array([x.sum() for x in s]); m = np.array([len(x) for x in s])
        def z_at(k):  # first k days
            mu = sums[:k].sum() / m[:k].sum()
            r = sums[:k] - mu * m[:k]
            se = np.sqrt(k / (k - 1) * (r ** 2).sum()) / m[:k].sum()   # cluster-robust SE of a ratio mean
            return mu / se
        ok = False
        if info1:
            k1 = int(np.searchsorted(np.cumsum(m), info1 * n_races)) + 1
            ok = z_at(min(k1, len(s))) > c1
        ok = ok or z_at(len(s)) > c
        hits += ok
    return hits / reps


def sim_power_looks(d, col, looks, crit, delta, reps=1000):
    days = [g[col].to_numpy() - d[col].mean() + delta for _, g in d.groupby("date")]
    hits = 0
    for _ in range(reps):
        s, tot = [], 0
        while tot < looks[-1]:
            j = RNG.integers(len(days)); s.append(days[j]); tot += len(days[j])
        sums = np.array([x.sum() for x in s]); m = np.array([len(x) for x in s]); cm = np.cumsum(m)
        for L, c in zip(looks, crit):
            k = min(int(np.searchsorted(cm, L)) + 1, len(s))
            mu = sums[:k].sum() / m[:k].sum(); r = sums[:k] - mu * m[:k]
            se = np.sqrt(k / (k - 1) * (r ** 2).sum()) / m[:k].sum()
            if mu / se > c:
                hits += 1; break
    return hits / reps


def main():
    P = pd.read_pickle(PREDS)
    P = P[P.pE.notna() & P.pD2.notna() & P.m_M.notna()]
    d = race_diffs(P)
    d = d[d.groupby("race_id").race_id.transform("size") == 1]
    per = {"development May-Aug": d[d.month.between("2026-05", "2026-08")],
           "re-used Sep-Oct": d[d.month.isin(["2026-09", "2026-10"])],
           "re-used H3 (sealed-card market)": d[d.month.str.startswith("H3")]}
    summ = {k: {c: summarise(v, c) for c in ("pE", "pD2")} for k, v in per.items()}
    pool = pd.concat(per.values())
    sd_plan = max(summarise(pool, "pE")["sd"], summarise(pool, "pD2")["sd"])
    deff_plan = max(s[c]["deff"] for s in summ.values() for c in s)
    z1 = norm.ppf(1 - ALPHA1)
    rows = []
    for delta in (0.002, 0.003, 0.005):
        n = n_required(sd_plan, deff_plan, delta, z1)
        rows.append(dict(delta=delta, n_races_fixed=n, approx_days_at_30=int(np.ceil(n / 30)),
                         power_at_1000=round(float(norm.cdf(delta / (sd_plan * np.sqrt(deff_plan) / np.sqrt(1000)) - z1)), 3)))
    tab = pd.DataFrame(rows)
    n_final = int(max(1000, np.ceil(tab.loc[tab.delta == 0.003, "n_races_fixed"].iloc[0] * 1.03 / 100) * 100))
    looks = [1000] + [int(n_final * q) for q in (0.25, 0.5, 0.75, 1.0)]
    fracs = [x / n_final for x in looks]
    crit, spend = obf_boundaries(fracs)
    simE = {str(dl): sim_power_looks(pool, "pE", looks, crit, dl) for dl in (0.0, 0.002, 0.003, 0.005)}
    simD2 = {str(dl): sim_power_looks(pool, "pD2", looks, crit, dl) for dl in (0.0, 0.002, 0.003)}
    res = dict(alpha_one_sided_per_model=ALPHA1, target_power=POWER, sd_per_race_plan=sd_plan, design_effect_plan=deff_plan,
               periods=summ, fixed_sample=rows, n_final=n_final, looks_races=looks,
               obf_critical_z=[None if not np.isfinite(c) else round(c, 3) for c in crit], cumulative_alpha_spent=[float(f"{x:.3g}") for x in spend],
               simulated_power_E=simE, simulated_power_D2=simD2)
    os.makedirs(os.path.join(HERE, "out"), exist_ok=True)
    json.dump(res, open(os.path.join(HERE, "out", "power.json"), "w"), indent=1)
    tab.to_csv(os.path.join(HERE, "out", "power_table.csv"), index=False)
    print(json.dumps(res, indent=1))


if __name__ == "__main__":
    main()
