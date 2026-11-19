# Phase 3 - market movement

**Data:** replay set S3 (development May-Aug, re-used Sep - 12 Oct) with checkpoints:
- M = 09:00;
- H = off minus 60 minutes;
- T10 = off minus 10 minutes;
- L = off minus 1 second;
- BSP.

H3 has only 09:00 and BSP. No 30, 15 or 5 minute snapshots exist in this repo (DATA_AUDIT.md). Market chance at each checkpoint = the production composite (0.6 × exchange + 0.4 × bookmaker median), normalised.

Files: out/movement_intervals.csv, out/movement_predictive.csv, out/disagreement_movement_corr.csv, out/disagreement_movement_within_band.csv.

## How prices move (all S3 runners, May - 12 Oct)
| Interval | Median absolute change in exchange quote | Shortened (> +0.2 pts) | Drifted (< -0.2 pts) | Mean absolute change in probability | Runners changing market rank |
|---|---|---|---|---|---|
| 09:00 -> off-60m | 22% | 37% | 51% | 1.8 pts | 52% |
| off-60m -> off-10m | 10% | 32% | 43% | 0.8 pts | 31% |
| off-10m -> off-1s | 8% | 30% | 38% | 0.8 pts | 28% |
| off-1s -> BSP | n/a | 33% | 52% | 1.4 pts | n/a |

Most of the movement happens between 09:00 and an hour before the off. The last step, to BSP, partly reflects the difference between the composite price and BSP for outsiders, not new information (DATA_AUDIT.md).

## Does later price information predict the result?
Win log-loss by checkpoint (lower is better):

| Set | 09:00 | off-60m | off-10m | off-1s | BSP |
|---|---|---|---|---|---|
| Development | 1.802 | 1.770 | 1.762 | 1.757 | 1.747 |
| Re-used | 1.835 | 1.796 | 1.787 | 1.774 | 1.765 |

Each later checkpoint is more accurate. About 55-60% of the 09:00-to-BSP improvement has already happened an hour before the off.

**Movement beyond the 09:00 price** (conditional logit on development: win ~ log 09:00 chance + move from 09:00 to off-1s):
- the movement coefficient is 1.06 (se 0.05): movement is almost fully informative;
- adding our disagreement (log model - log 09:00) gives a coefficient of 0.007 (se 0.035), essentially zero.

**Once you know how the price moved, our model adds nothing.**

## Verifying the -0.27: do horses we favour drift?
Correlation between disagreement, log(model / 09:00 market), and the later move, log(later market / 09:00 market):

| Set | to off-60m | to off-10m | to off-1s | to BSP |
|---|---|---|---|---|
| Development | +0.018 [+0.001, +0.036] | -0.035 [-0.054, -0.013] | -0.064 [-0.085, -0.042] | -0.170 [-0.188, -0.154] |
| Re-used | -0.054 [-0.083, -0.020] | -0.131 [-0.163, -0.095] | -0.172 [-0.201, -0.143] | **-0.273 [-0.301, -0.240]** |
| H3 untouched | n/a | n/a | n/a | -0.335 [-0.375, -0.295] |

By month (to BSP): May -0.18, Jun -0.19, Jul -0.11, Aug -0.20, Sep -0.26, Oct -0.30.

**The Phase 2 figure reproduces exactly (-0.273),** with day-block 95% intervals.

**But it is mostly an odds-level artefact.**
- Our model is much flatter than the market, so "model above market" mostly means outsider.
- Outsiders lengthen from the 09:00 composite to BSP whatever we think.

Comparing runners within the same 09:00 odds band (20 equal bands; residual correlation):

| Set | Raw correlation | **Within same odds band** | Slope |
|---|---|---|---|
| Development | -0.170 | **+0.138** | +0.161 |
| Re-used | -0.273 | **+0.054** | +0.060 |
| H3 untouched | -0.335 | **+0.050** | +0.047 |

Within band, the to-off-60m, to-off-10m and to-off-1s versions are also positive (+0.07 to +0.18).

**Corrected finding:**
- At the same 09:00 odds, the market tends to move **towards** our model's view. Most of the effect is in the horses we rate *below* the market, which drift (out/disagreement_vs_movement.png).
- The effect is small, was larger in May-Aug than since, and is stable in sign across all three independent periods.
- This is why the blend weight on our model falls from 0.10 at 09:00 to 0.03 an hour before the off, 0.01 at off-10m and 0.002 at the off (TIMING_ANALYSIS.md). **The market absorbs what our model knows before the off.**

We can observe that prices move. **We cannot verify why** (non-runner news, stable confidence, weight of money): no news or order data exists.

Phase 2's statement that "the market moves away from our model" is corrected in research/harville/phase2/ERRATUM_2026-11-19.md.
