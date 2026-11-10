# What has been tested (as of 14 Oct 2026)

Each line: the idea, the sealed spec in `prereg/`, the result file in `out/`, and the outcome.
Log-loss gains are per race (higher = better); intervals are 95% date-block bootstrap.

## Adopted into the live model
| Idea | Spec | Result | Outcome |
|---|---|---|---|
| v2: carried-weight bands, claimer flag, last finishing speed, long-break flags | MODEL_V2_SPEC | model_v2_test.txt | **PASS**: gain +0.020 [+0.011, +0.030]. Live from 14 Oct |
| v2f: fill missing 12-month form from 6-year RBD history | RBD_FILL_SPEC | rbd_fill_test.txt | **PASS**: A +0.0035 [+0.0002, +0.0067], B +0.026 [+0.014, +0.037]. Live from 14 Oct |

## Worth watching (passed, but not bettable as tested)
| Idea | Spec | Result | Outcome |
|---|---|---|---|
| Lay the place when win-BSP place chance is 15%+ below place-BSP chance (place BSP <= 10) | PLACE_MARKET_SPEC | place_market_test.txt | **PASS (diagnostic)**: 2023-25 +1.15p per £1 liability [+0.06, +2.33], 2026 +1.29p; 6 of 7 years positive. Uses final win BSP, so needs a forward test with prices ~2 min before the off. About +0.4p at 5% commission |
| Each-way Plan B (back e/w at bookmaker, lay win half on exchange) | EACH_WAY_SPEC | data/ew_tracker.csv | Forward test running; primary outcome after 300 bets. 18 bets: -£2.26 vs +£2.40 expected |
| Each-way at standard terms 10 min before off, EV >= 3% | PRICE_HISTORY_SPEC P5 | price_history_test.txt | +6.1% [-4.2%, +16.8%]; did not pass, most profit in Oct-Dec 2025 |

## Failed: model accuracy (no gain over the current model)
| Idea | Spec | Result |
|---|---|---|
| Collateral (head-to-head and common opponents), 12 months | COLLATERAL_SPEC | +0.0001 / +0.0005, both intervals include 0 |
| Collateral over 5 years of RBD | COLLATERAL_5Y_SPEC | A +0.0043 [+0.0013, +0.0074], B +0.0058 [-0.0019, +0.0128]; failed B |
| 6-year RBD form history as extra features | RBD_HISTORY_SPEC | A +0.0029 [-0.0013, +0.0070]; failed A (the fill version passed instead) |
| Own rating (lengths + weight, OR-anchored) | OWN_RATING_SPEC, OWN_RATING_V2_SPEC | A +0.0003 [-0.0032, +0.0036]; failed A. First version drifted badly; v2 fixed drift |
| Full finishing-order training | FULL_ORDER_SPEC | +0.0012 [-0.0017, +0.0039] |
| Trouble-in-running adjustment, comment-based run style (v3a) | TROUBLE_STYLE_SPEC | -0.0002 / +0.0000 |
| Course pace edges (Flat and jumps) | COURSE_PACE_EDGE_SPEC | Flat A -0.0017, jumps -0.0004 |
| Pace shape | PACE_SHAPE_SPEC | Helps vs equal chance (+0.0067) but nothing beyond the forecast or BSP |
| Sectional times | SECTIONALS_SPEC | Front-runner and sectional angles: no gain, no betting edge |
| Statistics ranking (trainer/jockey etc.) | (stat_ranking) | +0.0055 over the forecast, -0.0013 over BSP |

## Failed: betting (no profit at prices you could get)
| Idea | Spec | Result |
|---|---|---|
| Lay favourites the model doubts | LAY_FAV_SPEC | No profit at BSP |
| In-running lays / backs of predicted front-runners | INPLAY_AND_RA_SPEC | Fails; in-running minimum price unusable (adverse selection) |
| Race Advisor ratings | INPLAY_AND_RA_SPEC | No gain beyond BSP |
| Draw and run-style bias | DRAW_PACE_SPEC | Beyond BSP -0.0002; betting +1.9% [-13.5%, +17.3%]. Going split did not repeat across periods |
| Jumps model value bets | JUMPS_MODEL_SPEC | No gain beyond BSP |
| Back-dated card flag patterns | BACKDATED_REVIEW_SPEC | Discovery patterns did not confirm |
| Morning prices (Race Advisor Odds column) + model value | MORNING_PRICE_SPEC | Passed on a small sample (356 bets, +35% [+8%, +63%]) but **not confirmed** by the full bookmaker history below |
| Best bookmaker price vs BSP, all runners and favourites, 5 time points | PRICE_HISTORY_SPEC P1-P2 | Favourites at 10am + BOG -0.04% [-3.6%, +3.7%]; everything else worse. Early prices beat BSP only for horses under 2/1 |
| Model top pick at best price | PRICE_HISTORY_SPEC P3 | -4% to -7%; +BOG -1% to -3% |
| Model + market two-stage value | PRICE_HISTORY_SPEC P3c | -8% to -17%; market gets 90-98% of the weight |
| Steamers (shortened 20%+ by 10am) | PRICE_HISTORY_SPEC P4 | -12% at best price, -6% with BOG; actual/expected vs BSP 1.00 |
| Our form model + place prices | PLACE_MARKET_SPEC B1, B2 | Form adds nothing beyond the place price (log-loss 0.51283 -> 0.51268) |

## What this adds up to
- The model ranks horses well and has improved (v2, v2f), but the win and place markets already price what it knows.
- Ideas that look good against the forecast or bookmaker prices usually vanish against BSP.
- Untested areas that could still be worth sealing a test for: the place-lay rule with near-off prices (needs a
  Betfair feed), lower-grade Irish racing, markets with thin liquidity.
