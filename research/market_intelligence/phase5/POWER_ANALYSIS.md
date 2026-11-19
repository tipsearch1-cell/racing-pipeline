# Phase 5 - power analysis (done before any forward outcome)

**The original 1,000-race target is not adequately powered.**
- To detect a true gain of 0.003 log-loss per race (about what E showed historically) with 80% power at the Bonferroni level needs about **12,400 races**. That is roughly 14 months of GB+IRE racing.
- A gain of 0.002 needs about 28,000 races.
- With 1,000 races, power is 5-22% across the three effect sizes.

Script: power.py. Output: out/power.json (sha256 b10626e5…cda067) and out/power_table.csv.

## Planning inputs (historical, previously examined data; no forward outcomes)
| Period | Model | Races | Days | Mean d | SD of d per race | Design effect (day clustering) |
|---|---|---|---|---|---|---|
| Development May-Aug | E | 4,761 | 123 | +0.0034 | 0.093 | 1.07 |
| Development May-Aug | D2 | 4,761 | 123 | +0.0022 | 0.080 | 0.99 |
| Re-used Sep-Oct | E | 1,623 | 42 | +0.0033 | 0.096 | 1.20 |
| Re-used Sep-Oct | D2 | 1,623 | 42 | +0.0003 | 0.052 | 1.18 |
| Re-used H3 (sealed-card market) | E | 776 | 24 | +0.0042 | 0.097 | 1.33 |
| Re-used H3 (sealed-card market) | D2 | 776 | 24 | +0.0015 | 0.029 | 1.13 |

**Planning values (conservative):**
- SD 0.094: the larger of E and D2, pooled.
- Design effect 1.33: the largest observed.
- About 30-39 races per day.

## Fixed-sample requirement (80% power, one-sided α = 0.0125)
| True gain | Races needed | Approx. racing days at 30/day | Power at 1,000 races |
|---|---|---|---|
| 0.002 | 27,909 | 931 | 4.9% |
| 0.003 | 12,404 | 414 | 8.6% |
| 0.005 | 4,466 | 149 | 21.7% |

## Pre-specified extension (sealed)
**Design:**
- Looks at 1,000 (the original Phase 4 point), 3,200, 6,400, 9,600 and 12,800 confirmatory settled races.
- Lan-DeMets O'Brien-Fleming spending of the one-sided 0.0125 per model.
- No futility stopping.

**Boundaries:**

| Look (races) | 1,000 | 3,200 | 6,400 | 9,600 | 12,800 |
|---|---|---|---|---|---|
| Critical z | ∞ (no α spent) | 4.926 | 3.351 | 2.670 | 2.279 |
| Cumulative α | 0 | 5.9e-7 | 4.1e-4 | 0.0039 | 0.0125 |

**Simulated operating characteristics** (1,000 replications resampling whole historical days, shifted to the stated true gain):

| True gain | Power for E | Power for D2 |
|---|---|---|
| 0 (type-I error) | 1.3% | 0.7% |
| 0.002 | 55% | 82% |
| 0.003 | 87% | 99.5% |
| 0.005 | 99.9% | n/a |

D2's paired differences are much less variable (SD 0.03-0.08), so D2 is easier to test than E at the same gain.

## Caveats
- The SD and design effect come from replayed history. Forward variance can differ, and the realised SD is reported at each look.
- Race volume falls in winter, and eligibility attrition (missing 09:00 snapshots, late pushes) lowers the count. The calendar time to 12,800 is therefore an estimate (about 14-16 months).
- Historical gains are subject to selection optimism (winner's curse): E was chosen as the best of five candidates. The true forward gain may be smaller than 0.003, and then even 12,800 races may not detect it. That is why FAIL is always reported together with power.
