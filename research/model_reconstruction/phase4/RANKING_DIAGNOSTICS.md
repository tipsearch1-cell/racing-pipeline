# Phase 4 - why the model ranks badly (hypotheses A-F)

**Fixed development split:** trained on history before 1 Jul 2026 (6,093 races), tested on Jul-Aug 2026 (2,266 races).
- Test log-loss: existing model 1.941; 09:00 market 1.788. Gap = 0.153.
- Files: out/diagnostics.json, out/ablation.csv, out/feature_ablation.png.

| Hypothesis | Controlled test | Result | Contribution to the 0.153 gap | Verdict |
|---|---|---|---|---|
| **A** Weak relative ranking | Concordance overall and within 09:00-market quintiles; all features in relative vs absolute form | Overall concordance: model 0.675, market 0.736. Within the outsider quintile (lowest 09:00 chances): market 0.705, model 0.520 (close to random). Within the favourites quintile: market 0.569, model 0.544. Relative forms did *not* beat absolute forms (log-loss 1.916 vs 1.911). | The symptom, not the cause: the model cannot tell which outsiders are hopeless, so it spreads probability onto them and away from favourites | **Supported as a symptom; "use relative features" rejected as a fix** |
| **B** Wrong objective | The same 13 production features under three objectives: runner-level logistic then normalised, race softmax (current), pairwise | 1.953 / 1.948 / 1.948 | ≈ 0 (the current objective is already listwise and best-equal) | **Rejected** |
| **C** Missing information | Add each feature group to the production set, and remove each from the full set | Trainer and jockey form +0.023; OR & class +0.007; course/distance/going +0.0006; speed figures -0.003; consistency -0.001; pace -0.0005; field strength 0. All groups together: +0.026 | **About 17% of the gap closed; about 83% remains** (information the market has and our data lacks) | **Supported: the main cause** |
| **D** Field-size effects | Entropy vs market and BSP by field size; separate temperature per field band (fitted on training) | The model is more spread out than the market in every band (≤7 runners: 1.55 vs 1.45 nats; 16+: 2.71 vs 2.63). Per-band temperature: 1.9415 -> 1.9413. | ≈ 0 | **Rejected** (too-even probabilities are a symptom of weak information, not a scale error) |
| **E** Training population mismatch | Last 3 months only vs expanding; Flat/Jumps separate vs pooled | 1.9158 / 1.9157 / 1.9154 | ≈ 0 | **Rejected** |
| **F** Compression / post-processing | L2 = 1 vs 0; best temperature on test (oracle); sums to 1 | 1.9415 vs 1.9417; oracle temperature 1.006 (log-loss unchanged); sums exact | ≈ 0 | **Rejected** |

## What it means
- **The favourite / outsider error comes from information, not maths.** The model's probabilities are honest given what it knows: calibration slope 1.0, and no temperature helps. It just knows much less than the market about which horse is strong today.
- The biggest available improvement is **trainer and jockey current form**, which production does not use.
- **Speed figures did not help.** The RaceData dynamic speed ratings, used here through earlier same-code runs only, are noisy and missing for about 31% of runners.
- Even all feature groups together leave the model about 0.13 behind the 09:00 market.

**A side finding (training/prediction mismatch in production):**
- Card weights (`lbs`) are *before* the jockey's claim, but the history (training) weights are *after* it. On 18 Nov, claimers differed by 3-10 lb (mean 1.2 lb across all runners).
- The production lbs_rel feature is therefore slightly inconsistent between training and prediction.
- The Phase 4 shadow script subtracts the claim. Production is unchanged; this is a recommendation only.

Another unavoidable difference: late non-runners after the seal change field-relative features between the card and the result.
