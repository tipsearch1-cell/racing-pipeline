
### S development May-Aug 2026 (SYNTHETIC replay)

| Model | Races | Win log-loss | Top-2 Brier | Top-3 Brier | Exacta LL | Trifecta LL | P(2nd) slope | P(3rd) slope | Place-prob slope |
|---|---|---|---|---|---|---|---|---|---|
| Original Harville (market) | 4,732 | 1.8078 | 0.14070 | 0.17286 | 3.6022 | 5.3007 | 0.91 | 0.87 | 0.91 |
| Market + discounted Harville | 4,732 | 1.8078 | 0.14064 | 0.17237 | 3.5982 | 5.2818 | 0.99 | 1.05 | 1.02 |
| Our model + discounted Harville | 4,732 | 1.9758 | 0.15239 | 0.18710 | 3.8789 | 5.6311 | 1.00 | 1.02 | 0.99 |
| Blend + discounted Harville | 4,732 | 1.8039 | 0.14070 | 0.17236 | 3.5943 | 5.2770 | 1.00 | 1.05 | 0.98 |
| Enhanced ranking | 4,732 | 1.8039 | 0.14067 | 0.17204 | 3.5959 | 5.2737 | 0.99 | 1.01 | 0.98 |

Paired gains vs market + discounted Harville (A minus model; positive = model better), 95% day-block interval:
- win log-loss: H +0.0000 [+0.0000, +0.0000]; B -0.1679 [-0.1840, -0.1509]; C +0.0039 [+0.0013, +0.0065]; D +0.0039 [+0.0014, +0.0065]
- top-2 Brier (per race): H -0.0006 [-0.0013, +0.0002]; B -0.1075 [-0.1176, -0.0980]; C -0.0006 [-0.0014, +0.0003]; D -0.0003 [-0.0014, +0.0009]
- top-3 Brier (per race): H -0.0045 [-0.0068, -0.0023]; B -0.1348 [-0.1474, -0.1223]; C +0.0001 [-0.0006, +0.0009]; D +0.0031 [+0.0014, +0.0048]
- exacta LL: H -0.0039 [-0.0062, -0.0017]; B -0.2806 [-0.3061, -0.2562]; C +0.0039 [+0.0012, +0.0068]; D +0.0023 [-0.0013, +0.0059]
- trifecta LL: H -0.0189 [-0.0250, -0.0131]; B -0.3493 [-0.3791, -0.3206]; C +0.0048 [+0.0018, +0.0077]; D +0.0081 [+0.0024, +0.0133]

### S holdout 1 Sep-12 Oct 2026 (SYNTHETIC replay)

| Model | Races | Win log-loss | Top-2 Brier | Top-3 Brier | Exacta LL | Trifecta LL | P(2nd) slope | P(3rd) slope | Place-prob slope |
|---|---|---|---|---|---|---|---|---|---|
| Original Harville (market) | 1,616 | 1.8355 | 0.13397 | 0.16755 | 3.6728 | 5.4356 | 0.89 | 0.83 | 0.91 |
| Market + discounted Harville | 1,616 | 1.8355 | 0.13393 | 0.16702 | 3.6692 | 5.4143 | 0.98 | 1.02 | 1.03 |
| Our model + discounted Harville | 1,616 | 2.0259 | 0.14500 | 0.18199 | 3.9717 | 5.8071 | 1.05 | 1.00 | 1.04 |
| Blend + discounted Harville | 1,616 | 1.8321 | 0.13394 | 0.16709 | 3.6649 | 5.4100 | 1.00 | 1.03 | 0.99 |
| Enhanced ranking | 1,616 | 1.8321 | 0.13383 | 0.16683 | 3.6610 | 5.4020 | 0.99 | 1.00 | 0.99 |

Paired gains vs market + discounted Harville (A minus model; positive = model better), 95% day-block interval:
- win log-loss: H +0.0000 [+0.0000, +0.0000]; B -0.1904 [-0.2152, -0.1659]; C +0.0034 [-0.0015, +0.0082]; D +0.0034 [-0.0013, +0.0081]
- top-2 Brier (per race): H -0.0004 [-0.0017, +0.0011]; B -0.1076 [-0.1230, -0.0938]; C -0.0002 [-0.0016, +0.0013]; D +0.0009 [-0.0006, +0.0026]
- top-3 Brier (per race): H -0.0051 [-0.0082, -0.0025]; B -0.1454 [-0.1604, -0.1300]; C -0.0006 [-0.0020, +0.0008]; D +0.0019 [-0.0017, +0.0054]
- exacta LL: H -0.0036 [-0.0072, -0.0001]; B -0.3025 [-0.3375, -0.2707]; C +0.0043 [-0.0006, +0.0091]; D +0.0082 [+0.0029, +0.0135]
- trifecta LL: H -0.0214 [-0.0311, -0.0121]; B -0.3928 [-0.4274, -0.3586]; C +0.0042 [-0.0004, +0.0088]; D +0.0123 [+0.0029, +0.0218]

### G genuine archive 10-18 Nov 2026 (model input)

| Model | Races | Win log-loss | Top-2 Brier | Top-3 Brier | Exacta LL | Trifecta LL | P(2nd) slope | P(3rd) slope | Place-prob slope |
|---|---|---|---|---|---|---|---|---|---|
| Original Harville (market) | 217 | 1.8421 | 0.13055 | 0.16409 | 3.6353 | 5.4237 | 0.95 | 0.86 | 0.89 |
| Market + discounted Harville | 217 | 1.8421 | 0.13042 | 0.16310 | 3.6301 | 5.3751 | 1.04 | 1.07 | 1.00 |
| Our model + discounted Harville | 217 | 2.0406 | 0.14285 | 0.17752 | 3.9698 | 5.7882 | 1.13 | 1.05 | 1.13 |
| Blend + discounted Harville | 217 | 1.8448 | 0.13045 | 0.16305 | 3.6312 | 5.3742 | 1.06 | 1.08 | 0.98 |
| Enhanced ranking | 217 | 1.8448 | 0.12981 | 0.16123 | 3.6214 | 5.3336 | 1.06 | 1.10 | 1.00 |

Paired gains vs market + discounted Harville (A minus model; positive = model better), 95% day-block interval:
- win log-loss: H +0.0000 [+0.0000, +0.0000]; B -0.1985 [-0.2644, -0.1203]; C -0.0027 [-0.0218, +0.0167]; D -0.0027 [-0.0218, +0.0160]
- top-2 Brier (per race): H -0.0013 [-0.0052, +0.0022]; B -0.1228 [-0.1789, -0.0654]; C -0.0004 [-0.0048, +0.0043]; D +0.0060 [+0.0014, +0.0102]
- top-3 Brier (per race): H -0.0098 [-0.0203, +0.0008]; B -0.1424 [-0.2009, -0.0792]; C +0.0005 [-0.0020, +0.0033]; D +0.0185 [+0.0095, +0.0298]
- exacta LL: H -0.0052 [-0.0143, +0.0041]; B -0.3396 [-0.4566, -0.2082]; C -0.0011 [-0.0230, +0.0185]; D +0.0087 [-0.0117, +0.0293]
- trifecta LL: H -0.0485 [-0.0796, -0.0214]; B -0.4131 [-0.5459, -0.2704]; C +0.0009 [-0.0192, +0.0180]; D +0.0415 [+0.0087, +0.0847]

### G genuine archive 10-18 Nov 2026 (reviewer input as B)

| Model | Races | Win log-loss | Top-2 Brier | Top-3 Brier | Exacta LL | Trifecta LL | P(2nd) slope | P(3rd) slope | Place-prob slope |
|---|---|---|---|---|---|---|---|---|---|
| Market + discounted Harville | 217 | 1.8421 | 0.13042 | 0.16310 | 3.6301 | 5.3751 | 1.04 | 1.07 | 1.00 |
| Our model + discounted Harville | 217 | 1.8382 | 0.13101 | 0.16302 | 3.6471 | 5.3857 | 1.09 | 1.11 | 1.07 |
| Blend + discounted Harville | 217 | 1.8464 | 0.13071 | 0.16337 | 3.6358 | 5.3818 | 1.03 | 1.06 | 0.93 |

Paired gains vs market + discounted Harville (A minus model; positive = model better), 95% day-block interval:
- win log-loss: B +0.0039 [-0.0135, +0.0208]; C -0.0043 [-0.0301, +0.0207]
- top-2 Brier (per race): B -0.0059 [-0.0208, +0.0074]; C -0.0028 [-0.0092, +0.0037]
- top-3 Brier (per race): B +0.0008 [-0.0117, +0.0129]; C -0.0026 [-0.0078, +0.0021]
- exacta LL: B -0.0170 [-0.0522, +0.0155]; C -0.0057 [-0.0310, +0.0188]
- trifecta LL: B -0.0105 [-0.0471, +0.0228]; C -0.0066 [-0.0346, +0.0194]
