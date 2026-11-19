# Phase 3 run log

- params 2026-05: a=[0.947] w_M=[1.089 0.112] (se [0.044 0.055]) w_H=[1.073 0.061] w_T10=[1.06  0.045] w_L=[1.072 0.022]
- params 2026-06: a=[0.92] w_M=[1.101 0.053] (se [0.033 0.042]) w_H=[ 1.085 -0.003] w_T10=[ 1.068 -0.018] w_L=[ 1.074 -0.033]
- params 2026-07: a=[0.976] w_M=[1.082 0.1  ] (se [0.029 0.036]) w_H=[1.077 0.036] w_T10=[1.059 0.022] w_L=[1.06  0.013]
- params 2026-08: a=[0.982] w_M=[1.085 0.101] (se [0.026 0.032]) w_H=[1.08  0.029] w_T10=[1.065 0.014] w_L=[1.065 0.006]
- params 2026-09: a=[0.987] w_M=[1.079 0.108] (se [0.024 0.029]) w_H=[1.077 0.038] w_T10=[1.064 0.02 ] w_L=[1.063 0.011]
- params 2026-10: a=[0.993] w_M=[1.08  0.099] (se [0.022 0.027]) w_H=[1.083 0.031] w_T10=[1.068 0.014] w_L=[1.062 0.006]
- params final: a=[0.992] w_M=[1.084 0.094] (se [0.021 0.026]) w_H=[1.089 0.027] w_T10=[1.072 0.011] w_L=[1.067 0.002]

## Win calibration
       set               prob      ll   brier     ece   slope  intercept  concordance  top_win  races  runners      lo      hi
0      dev                  f  1.9694  0.0909  0.0039  0.9967    -0.0062       0.6699   0.2661   4758  43370.0     NaN     NaN
1      dev              f_cal  1.9700  0.0909  0.0040  1.0254     0.0479       0.6699   0.2661   4758  43370.0     NaN     NaN
2      dev                m_M  1.8023  0.0856  0.0060  1.0930     0.1638       0.7366   0.3342   4758  43370.0     NaN     NaN
3      dev                b_M  1.7985  0.0855  0.0045  0.9909    -0.0158       0.7362   0.3321   4758  43370.0     NaN     NaN
4      dev                m_H  1.7708  0.0848  0.0051  1.0693     0.1193       0.7454   0.3438   4758  43370.0     NaN     NaN
5      dev              m_T10  1.7625  0.0846  0.0039  1.0543     0.0927       0.7485   0.3445   4758  43370.0     NaN     NaN
6      dev                m_L  1.7573  0.0845  0.0054  1.0479     0.0815       0.7499   0.3428   4758  43370.0     NaN     NaN
7      dev              close  1.7468  0.0843  0.0029  0.9757    -0.0405       0.7526   0.3480   4758  43370.0     NaN     NaN
8      dev      gain_vs_m_M:f -0.1671     NaN     NaN     NaN        NaN          NaN      NaN   4758      NaN -0.1835 -0.1498
9      dev  gain_vs_m_M:f_cal -0.1677     NaN     NaN     NaN        NaN          NaN      NaN   4758      NaN -0.1836 -0.1512
10     dev    gain_vs_m_M:b_M  0.0038     NaN     NaN     NaN        NaN          NaN      NaN   4758      NaN  0.0012  0.0065
11     dev  gain_vs_m_M:close  0.0555     NaN     NaN     NaN        NaN          NaN      NaN   4758      NaN  0.0457  0.0653
12  reused                  f  2.0222  0.0862  0.0032  1.0039     0.0077       0.6713   0.2582   1623  15719.0     NaN     NaN
13  reused              f_cal  2.0223  0.0862  0.0037  1.0118     0.0230       0.6713   0.2582   1623  15719.0     NaN     NaN
14  reused                m_M  1.8345  0.0806  0.0071  1.0968     0.1742       0.7343   0.3309   1623  15719.0     NaN     NaN
15  reused                b_M  1.8315  0.0804  0.0038  0.9946    -0.0096       0.7344   0.3290   1623  15719.0     NaN     NaN
16  reused                m_H  1.7955  0.0797  0.0058  1.1026     0.1810       0.7465   0.3339   1623  15719.0     NaN     NaN
17  reused              m_T10  1.7865  0.0794  0.0059  1.0765     0.1339       0.7509   0.3469   1623  15719.0     NaN     NaN
18  reused                m_L  1.7744  0.0790  0.0071  1.0583     0.1009       0.7569   0.3518   1623  15719.0     NaN     NaN
19  reused              close  1.7649  0.0787  0.0070  1.0051     0.0087       0.7589   0.3530   1623  15719.0     NaN     NaN
20  reused      gain_vs_m_M:f -0.1878     NaN     NaN     NaN        NaN          NaN      NaN   1623      NaN -0.2131 -0.1629
21  reused  gain_vs_m_M:f_cal -0.1878     NaN     NaN     NaN        NaN          NaN      NaN   1623      NaN -0.2114 -0.1641
22  reused    gain_vs_m_M:b_M  0.0030     NaN     NaN     NaN        NaN          NaN      NaN   1623      NaN -0.0022  0.0076
23  reused  gain_vs_m_M:close  0.0696     NaN     NaN     NaN        NaN          NaN      NaN   1623      NaN  0.0508  0.0880
24      H3                  f  2.0128  0.0879  0.0063  1.0123     0.0238       0.6735   0.2626    674   6429.0     NaN     NaN
25      H3              f_cal  2.0129  0.0879  0.0063  1.0179     0.0345       0.6735   0.2626    674   6429.0     NaN     NaN
26      H3                m_M  1.7741  0.0802  0.0103  1.1161     0.2033       0.7606   0.3546    674   6429.0     NaN     NaN
27      H3                b_M  1.7694  0.0801  0.0080  1.0158     0.0272       0.7626   0.3576    674   6429.0     NaN     NaN
28      H3              close  1.7239  0.0788  0.0044  1.0111     0.0186       0.7710   0.3635    674   6429.0     NaN     NaN
29      H3      gain_vs_m_M:f -0.2387     NaN     NaN     NaN        NaN          NaN      NaN    674      NaN -0.2850 -0.1912
30      H3  gain_vs_m_M:f_cal -0.2388     NaN     NaN     NaN        NaN          NaN      NaN    674      NaN -0.2872 -0.1884
31      H3    gain_vs_m_M:b_M  0.0047     NaN     NaN     NaN        NaN          NaN      NaN    674      NaN -0.0025  0.0106
32      H3  gain_vs_m_M:close  0.0502     NaN     NaN     NaN        NaN          NaN      NaN    674      NaN  0.0217  0.0792
33       A                  f  2.0322  0.0868  0.0140  0.9808    -0.0374       0.6825   0.2398    221   2161.0     NaN     NaN
34       A              f_cal  2.0322  0.0868  0.0140  0.9861    -0.0270       0.6825   0.2398    221   2161.0     NaN     NaN
35       A                m_M  1.8383  0.0811  0.0171  0.9963    -0.0066       0.7503   0.3077    221   2161.0     NaN     NaN
36       A                b_M  1.8417  0.0814  0.0169  0.9039    -0.1685       0.7536   0.3167    221   2161.0     NaN     NaN
37       A              close  1.6739  0.0932  0.0230  0.8600    -0.2156       0.7649   0.3455    110    901.0     NaN     NaN
38       A      gain_vs_m_M:f -0.1939     NaN     NaN     NaN        NaN          NaN      NaN    221      NaN -0.2642 -0.1183
39       A  gain_vs_m_M:f_cal -0.1939     NaN     NaN     NaN        NaN          NaN      NaN    221      NaN -0.2626 -0.1177
40       A    gain_vs_m_M:b_M -0.0035     NaN     NaN     NaN        NaN          NaN      NaN    221      NaN -0.0217  0.0148

## Movement
  interval      n  med_abs_pct  share_shorten  share_drift  mean_abs_dprob  rank_change_share
0     M->H  59071       0.2222         0.3738       0.5072          0.0179             0.5150
1   H->T10  59087       0.1000         0.3201       0.4340          0.0084             0.3145
2   T10->L  59096       0.0769         0.3013       0.3797          0.0076             0.2841
3   L->BSP  59089          NaN         0.3342       0.5191          0.0140                NaN
       set                                                   prob      ll                   coef                    se
0      dev                                                    m_M  1.8018                    NaN                   NaN
1      dev                                                    m_H  1.7703                    NaN                   NaN
2      dev                                                  m_T10  1.7620                    NaN                   NaN
3      dev                                                    m_L  1.7568                    NaN                   NaN
4      dev                                                  close  1.7468                    NaN                   NaN
5   reused                                                    m_M  1.8345                    NaN                   NaN
6   reused                                                    m_H  1.7955                    NaN                   NaN
7   reused                                                  m_T10  1.7865                    NaN                   NaN
8   reused                                                    m_L  1.7744                    NaN                   NaN
9   reused                                                  close  1.7649                    NaN                   NaN
10     dev                      clogit win ~ log m_M + move(M->L)     NaN         [1.063, 1.059]        [0.023, 0.054]
11     dev  clogit win ~ log m_M + move(M->L) + (log f - log m_M)     NaN  [1.067, 1.058, 0.007]  [0.03, 0.055, 0.035]

## Disagreement vs movement
        set closer      n   corr     lo     hi
0       dev      H  43380  0.018  0.001  0.036
1       dev    T10  43380 -0.035 -0.054 -0.013
2       dev      L  43380 -0.064 -0.085 -0.042
3       dev    BSP  43370 -0.170 -0.188 -0.154
4   2026-05    BSP  12275 -0.182    NaN    NaN
5   2026-06    BSP  10798 -0.190    NaN    NaN
6   2026-07    BSP  10584 -0.107    NaN    NaN
7   2026-08    BSP   9713 -0.198    NaN    NaN
8    reused      H  15719 -0.054 -0.083 -0.020
9    reused    T10  15719 -0.131 -0.163 -0.095
10   reused      L  15719 -0.172 -0.201 -0.143
11   reused    BSP  15719 -0.273 -0.301 -0.240
12  2026-09    BSP  10825 -0.261    NaN    NaN
13  2026-10    BSP   4894 -0.299    NaN    NaN
14       H3    BSP   6429 -0.335 -0.375 -0.295

## Disagreement models
  market          form                                                                                                                                                coefs                                                                                                                                              ses                           gain_reused                             gain_H3
0    m_M        simple                                                                                                          {"lm": 1.188, "dpos": 0.162, "dneg": 0.077}                                                                                                       {"lm": 0.03, "dpos": 0.075, "dneg": 0.051}  +0.0028 [-0.0021, +0.0074] (n=1,623)  +0.0052 [-0.0026, +0.0112] (n=674)
1    m_M  interactions    {"lm": 1.173, "dpos": 0.013, "dneg": 0.146, "dpos_top3": 0.014, "dneg_top3": -0.081, "dpos_big": -0.066, "dpos_jumps": 0.071, "dpos_hcap": 0.229}  {"lm": 0.035, "dpos": 0.117, "dneg": 0.111, "dpos_top3": 0.141, "dneg_top3": 0.116, "dpos_big": 0.133, "dpos_jumps": 0.129, "dpos_hcap": 0.113}  +0.0015 [-0.0039, +0.0062] (n=1,623)  +0.0051 [-0.0031, +0.0120] (n=674)
2    m_H        simple                                                                                                          {"lm": 1.107, "dpos": 0.024, "dneg": 0.032}                                                                                                       {"lm": 0.03, "dpos": 0.074, "dneg": 0.049}  +0.0034 [+0.0005, +0.0063] (n=1,623)                                 NaN
3    m_H  interactions  {"lm": 1.111, "dpos": -0.039, "dneg": 0.088, "dpos_top3": -0.207, "dneg_top3": -0.039, "dpos_big": -0.182, "dpos_jumps": 0.102, "dpos_hcap": 0.186}  {"lm": 0.035, "dpos": 0.112, "dneg": 0.115, "dpos_top3": 0.149, "dneg_top3": 0.119, "dpos_big": 0.129, "dpos_jumps": 0.121, "dpos_hcap": 0.107}  +0.0023 [-0.0014, +0.0059] (n=1,623)                                 NaN
4  m_T10        simple                                                                                                         {"lm": 1.074, "dpos": -0.013, "dneg": 0.023}                                                                                                      {"lm": 0.031, "dpos": 0.073, "dneg": 0.048}  +0.0022 [+0.0001, +0.0043] (n=1,623)                                 NaN
5  m_T10  interactions   {"lm": 1.076, "dpos": -0.061, "dneg": 0.052, "dpos_top3": -0.139, "dneg_top3": -0.018, "dpos_big": -0.148, "dpos_jumps": 0.066, "dpos_hcap": 0.15}  {"lm": 0.035, "dpos": 0.109, "dneg": 0.114, "dpos_top3": 0.148, "dneg_top3": 0.117, "dpos_big": 0.124, "dpos_jumps": 0.119, "dpos_hcap": 0.105}  +0.0011 [-0.0018, +0.0039] (n=1,623)                                 NaN
6    m_L        simple                                                                                                         {"lm": 1.069, "dpos": 0.026, "dneg": -0.002}                                                                                                      {"lm": 0.031, "dpos": 0.071, "dneg": 0.048}  +0.0010 [-0.0011, +0.0030] (n=1,623)                                 NaN
7    m_L  interactions   {"lm": 1.081, "dpos": -0.003, "dneg": -0.036, "dpos_top3": -0.162, "dneg_top3": 0.056, "dpos_big": -0.162, "dpos_jumps": 0.059, "dpos_hcap": 0.15}  {"lm": 0.035, "dpos": 0.106, "dneg": 0.112, "dpos_top3": 0.147, "dneg_top3": 0.116, "dpos_big": 0.121, "dpos_jumps": 0.116, "dpos_hcap": 0.102}  -0.0003 [-0.0029, +0.0023] (n=1,623)                                 NaN

## CLV
           set                   selection      n  lclv_mean  lclv_lo  lclv_hi  lclv_matched_control  share_shortened  beat_close  clv_mean  clv_lo  clv_hi  clv_median  clv_comm2_mean  pclv_mean  bf_clv_median  matched_control_clv  roi_at_best  roi_at_bsp_c2 value
0          dev                 f_cal EV>=0  23197    -0.3918  -0.4092  -0.3734               -0.4456           0.3370      0.3096   -0.1560 -0.1678 -0.1440     -0.2308         -0.1403    -0.0033        -0.3012              -0.2669      -0.1641        -0.0359   NaN
28         dev                 blend EV>=0   8660    -0.4870  -0.5254  -0.4471               -0.2756           0.3438      0.4436   -0.0122 -0.0329  0.0105     -0.0559          0.0045    -0.0047        -0.3000              -0.2082      -0.0838        -0.1901   NaN
29         dev                     f EV>=0  22947    -0.3884  -0.4073  -0.3698               -0.4561           0.3394      0.3113   -0.1544 -0.1655 -0.1428     -0.2273         -0.1387    -0.0031        -0.2982              -0.2667      -0.1572        -0.0290   NaN
30         dev       all runners (control)  43372    -0.2598  -0.2708  -0.2490                0.0000           0.3931      0.3161   -0.1414 -0.1482 -0.1340     -0.1800         -0.1262     0.0000        -0.2249               0.0000      -0.1508        -0.0296   NaN
31      reused                 f_cal EV>=0   8238    -0.3768  -0.4058  -0.3486               -0.4387           0.3345      0.2752   -0.2013 -0.2170 -0.1837     -0.2814         -0.1864    -0.0020        -0.3235              -0.2977      -0.1830        -0.0512   NaN
57      reused                 blend EV>=0   2001    -0.2168  -0.2740  -0.1569               -0.1737           0.4613      0.4953    0.0527  0.0219  0.0832      0.0000          0.0691     0.0041        -0.0704              -0.1568       0.0800        -0.0407   NaN
58      reused                     f EV>=0   8214    -0.3766  -0.4049  -0.3476               -0.4312           0.3347      0.2753   -0.2018 -0.2180 -0.1855     -0.2812         -0.1870    -0.0020        -0.3235              -0.2894      -0.1834        -0.0499   NaN
59      reused       all runners (control)  15719    -0.2631  -0.2807  -0.2443                0.0000           0.3848      0.2958   -0.1706 -0.1806 -0.1604     -0.2161         -0.1560     0.0000        -0.2343               0.0000      -0.1562        -0.0313   NaN
60          H3                 f_cal EV>=0   3506    -0.3625  -0.4014  -0.3240               -0.3868           0.3071      0.2638   -0.2059 -0.2415 -0.1650     -0.2890         -0.1911    -0.0028        -0.2852              -0.3143      -0.1611         0.2213   NaN
86          H3                 blend EV>=0    765    -0.1516  -0.1958  -0.1050               -0.1803           0.4667      0.5529    0.1659  0.0993  0.2350      0.0417          0.1845     0.0061         0.0213              -0.1740       0.3261         0.2397   NaN
87          H3                     f EV>=0   3497    -0.3620  -0.4013  -0.3231               -0.3867           0.3076      0.2648   -0.2052 -0.2422 -0.1629     -0.2880         -0.1904    -0.0027        -0.2833              -0.3140      -0.1639         0.2161   NaN
88          H3       all runners (control)   6432    -0.2480  -0.2714  -0.2261                0.0000           0.3668      0.2822   -0.1733 -0.1948 -0.1499     -0.2127         -0.1588     0.0000        -0.2000               0.0000      -0.1644         0.0831   NaN
89         dev    blend EV>=0 decided at M   8660    -0.4870      NaN      NaN                   NaN           0.3438      0.4436   -0.0122     NaN     NaN     -0.0559             NaN    -0.0047            NaN                  NaN      -0.0838            NaN   NaN
90         dev    blend EV>=0 decided at H   3160    -0.3586      NaN      NaN                   NaN           0.4047      0.4538   -0.0443     NaN     NaN     -0.0256             NaN     0.0016            NaN                  NaN      -0.1486            NaN   NaN
91         dev  blend EV>=0 decided at T10   2153    -0.0466      NaN      NaN                   NaN           0.5026      0.5518    0.0427     NaN     NaN      0.0286             NaN     0.0056            NaN                  NaN       0.0309            NaN   NaN
92         dev    blend EV>=0 decided at L   2640    -0.0172      NaN      NaN                   NaN           0.5254      0.5837    0.0446     NaN     NaN      0.0345             NaN     0.0038            NaN                  NaN      -0.0106            NaN   NaN
93      reused    blend EV>=0 decided at M   2001    -0.2168      NaN      NaN                   NaN           0.4613      0.4953    0.0527     NaN     NaN      0.0000             NaN     0.0041            NaN                  NaN       0.0800            NaN   NaN
94      reused    blend EV>=0 decided at H    700    -0.0134      NaN      NaN                   NaN           0.5257      0.5471    0.0623     NaN     NaN      0.0263             NaN     0.0096            NaN                  NaN       0.0687            NaN   NaN
95      reused  blend EV>=0 decided at T10    691     0.0252      NaN      NaN                   NaN           0.5760      0.6064    0.0812     NaN     NaN      0.0562             NaN     0.0105            NaN                  NaN       0.0785            NaN   NaN
96      reused    blend EV>=0 decided at L   1641     0.0333      NaN      NaN                   NaN           0.6429      0.6935    0.0836     NaN     NaN      0.0606             NaN     0.0083            NaN                  NaN       0.0185            NaN   NaN
97  A-live-bot           all live bot bets     32        NaN      NaN      NaN                   NaN              NaN      0.5312    0.0421     NaN     NaN      0.0216             NaN        NaN            NaN                  NaN      -0.4662        -0.4233   NaN
98  A-live-bot             favourite check     30        NaN      NaN      NaN                   NaN              NaN      0.5333    0.0600     NaN     NaN      0.0216             NaN        NaN            NaN                  NaN      -0.4306        -0.3848   NaN
99  A-live-bot                  value flag      2        NaN      NaN      NaN                   NaN              NaN      0.5000   -0.2265     NaN     NaN     -0.2265             NaN        NaN            NaN                  NaN      -1.0000        -1.0000   NaN

Chosen on development: E drift cap k=0.3, F disagreement cap u=0.25

## Strategy cells (2% exchange, T=4%)
        set                                                                      strategy           price   bets     roi      lo      hi  clv_mean  beat_close  p_null
1       dev                                                                 A original @M        exchange  17927 -0.2126 -0.2682 -0.1556   -0.1761      0.2928   0.766
2       dev              A original @M | adverse fill (filled only if H quote >= M quote)        exchange  12274 -0.3967 -0.4519 -0.3395   -0.3521      0.1321   0.782
3       dev                                               A original @M | random fill 50%        exchange   8960 -0.2160 -0.2859 -0.1432   -0.1754      0.2948   0.708
4       dev                                               A original @M | random fill 75%        exchange  13432 -0.2273 -0.2855 -0.1625   -0.1765      0.2922   0.849
10      dev                                                                 A original @M  bookmaker best  21797 -0.1587 -0.2149 -0.0999   -0.1567      0.3090   0.474
13      dev                                                               B calibrated @M        exchange  18179 -0.2158 -0.2675 -0.1616   -0.1803      0.2893   0.766
14      dev            B calibrated @M | adverse fill (filled only if H quote >= M quote)        exchange  12507 -0.3972 -0.4518 -0.3383   -0.3556      0.1302   0.753
15      dev                                             B calibrated @M | random fill 50%        exchange   9019 -0.1529 -0.2312 -0.0676   -0.1783      0.2938   0.226
16      dev                                             B calibrated @M | random fill 75%        exchange  13622 -0.2336 -0.2941 -0.1732   -0.1821      0.2900   0.847
22      dev                                                               B calibrated @M  bookmaker best  22055 -0.1655 -0.2213 -0.1087   -0.1584      0.3081   0.521
25      dev                                                                    C blend @M        exchange   2528  0.0595 -0.0438  0.1790    0.1672      0.5596   0.638
26      dev                 C blend @M | adverse fill (filled only if H quote >= M quote)        exchange   1114 -0.2394 -0.4093 -0.0318   -0.0452      0.2857   0.594
27      dev                                                  C blend @M | random fill 50%        exchange   1248 -0.0108 -0.1493  0.1369    0.1712      0.5489   0.839
28      dev                                                  C blend @M | random fill 75%        exchange   1920  0.0538 -0.0696  0.2028    0.1618      0.5583   0.623
34      dev                                                                    C blend @M  bookmaker best   6451 -0.1125 -0.2133  0.0008   -0.0117      0.4435   0.951
37      dev                                                     F disagreement 0..0.25 @M        exchange    416  0.3959  0.1309  0.6999    0.2004      0.5928   0.101
38      dev  F disagreement 0..0.25 @M | adverse fill (filled only if H quote >= M quote)        exchange    168  0.3269 -0.1554  0.9495   -0.0473      0.3114   0.044
39      dev                                   F disagreement 0..0.25 @M | random fill 50%        exchange    214  0.3589 -0.0760  0.8731    0.1307      0.5701   0.135
40      dev                                   F disagreement 0..0.25 @M | random fill 75%        exchange    300  0.3640  0.0430  0.7462    0.2028      0.6100   0.173
46      dev                                                     F disagreement 0..0.25 @M  bookmaker best   1130  0.0513 -0.1658  0.2973    0.0070      0.4681   0.311
49      dev                                                      D market confirmation @H        exchange    428  0.1804 -0.1155  0.5115    0.2368      0.5584   0.170
55      dev                                                      D market confirmation @H  bookmaker best    339  0.2977  0.0474  0.5465    0.2701      0.7198   0.375
58      dev                                                    E drift avoidance k=0.3 @H        exchange   1216 -0.1522 -0.3104  0.0301    0.1033      0.5066   0.781
64      dev                                                    E drift avoidance k=0.3 @H  bookmaker best   1171  0.0103 -0.1979  0.3116    0.0101      0.5261   0.430
67      dev                                                               Timing blend @H        exchange   2509 -0.1793 -0.3297  0.0024    0.0469      0.4404   0.771
73      dev                                                               Timing blend @H  bookmaker best   1681 -0.1900 -0.3637  0.0149   -0.0660      0.4503   0.804
76      dev                                                             Timing blend @T10        exchange   3795 -0.1135 -0.3919  0.2398   -0.0657      0.3264   0.535
82      dev                                                             Timing blend @T10  bookmaker best    830  0.0367 -0.1055  0.1868    0.0986      0.6200   0.668
85      dev                                                               Timing blend @L        exchange   4290  0.0708 -0.2991  0.5146   -0.0031      0.4229   0.315
91      dev                                                               Timing blend @L  bookmaker best   1036  0.0755 -0.0689  0.2381    0.1055      0.6992   0.563
94   reused                                                                 A original @M        exchange   6592 -0.2138 -0.2899 -0.1285   -0.1903      0.2764   0.575
95   reused              A original @M | adverse fill (filled only if H quote >= M quote)        exchange   4669 -0.4507 -0.5399 -0.3545   -0.3678      0.1257   0.892
96   reused                                               A original @M | random fill 50%        exchange   3246 -0.2022 -0.3446 -0.0605   -0.1949      0.2736   0.501
97   reused                                               A original @M | random fill 75%        exchange   4939 -0.2014 -0.3102 -0.0869   -0.1865      0.2770   0.508
103  reused                                                                 A original @M  bookmaker best   7805 -0.1791 -0.2798 -0.0746   -0.2048      0.2738   0.305
106  reused                                                               B calibrated @M        exchange   6617 -0.2172 -0.2947 -0.1316   -0.1924      0.2750   0.593
107  reused            B calibrated @M | adverse fill (filled only if H quote >= M quote)        exchange   4692 -0.4544 -0.5488 -0.3577   -0.3701      0.1247   0.879
108  reused                                             B calibrated @M | random fill 50%        exchange   3233 -0.2162 -0.3079 -0.1265   -0.1923      0.2750   0.552
109  reused                                             B calibrated @M | random fill 75%        exchange   4889 -0.2257 -0.3334 -0.1226   -0.1909      0.2808   0.664
115  reused                                                               B calibrated @M  bookmaker best   7829 -0.1809 -0.2760 -0.0738   -0.2057      0.2731   0.307
118  reused                                                                    C blend @M        exchange   1110  0.0436 -0.0770  0.1532    0.1370      0.5279   0.512
119  reused                 C blend @M | adverse fill (filled only if H quote >= M quote)        exchange    509 -0.2936 -0.4414 -0.1228   -0.0923      0.2574   0.606
120  reused                                                  C blend @M | random fill 50%        exchange    567  0.1165 -0.0823  0.3338    0.1337      0.5291   0.294
121  reused                                                  C blend @M | random fill 75%        exchange    857  0.1059 -0.0213  0.2402    0.1342      0.5216   0.326
127  reused                                                                    C blend @M  bookmaker best   1276  0.1443 -0.0038  0.3108    0.0927      0.5290   0.307
130  reused                                                     F disagreement 0..0.25 @M        exchange    188  0.0179 -0.3150  0.3485    0.1415      0.5798   0.701
131  reused  F disagreement 0..0.25 @M | adverse fill (filled only if H quote >= M quote)        exchange     80 -0.2665 -0.6364  0.1578   -0.1011      0.3250   0.678
132  reused                                   F disagreement 0..0.25 @M | random fill 50%        exchange     98 -0.2362 -0.6250  0.2234    0.1500      0.6122   0.901
133  reused                                   F disagreement 0..0.25 @M | random fill 75%        exchange    144  0.0850 -0.2702  0.4654    0.1539      0.6111   0.585
139  reused                                                     F disagreement 0..0.25 @M  bookmaker best    231  0.1381 -0.1806  0.5130    0.1125      0.5281   0.415
142  reused                                                      D market confirmation @H        exchange    163 -0.0047 -0.4126  0.4296    0.1428      0.5828   0.362
148  reused                                                      D market confirmation @H  bookmaker best    123  0.2467 -0.2307  0.7358    0.1837      0.7317   0.367
151  reused                                                    E drift avoidance k=0.3 @H        exchange    519  0.1374 -0.1642  0.4623    0.0861      0.4952   0.148
157  reused                                                    E drift avoidance k=0.3 @H  bookmaker best    248  0.2185 -0.0091  0.4630    0.1589      0.6613   0.335
160  reused                                                               Timing blend @H        exchange   1264 -0.0918 -0.4252  0.2998   -0.0438      0.3655   0.391
166  reused                                                               Timing blend @H  bookmaker best    292  0.1995  0.0033  0.3983    0.1537      0.6507   0.374
169  reused                                                             Timing blend @T10        exchange   1541 -0.1675 -0.4983  0.1989   -0.0601      0.3121   0.489
175  reused                                                             Timing blend @T10  bookmaker best    242  0.2932 -0.0154  0.6494    0.1546      0.6983   0.194
178  reused                                                               Timing blend @L        exchange   2768  0.0256 -0.1887  0.2565    0.0855      0.5878   0.509
184  reused                                                               Timing blend @L  bookmaker best    708  0.0042 -0.1451  0.1752    0.1445      0.8164   0.925
187      H3                                                                 A original @M        exchange   3088 -0.1410 -0.2866  0.0621   -0.1857      0.2824   0.267
193      H3                                                                 A original @M  bookmaker best   3337 -0.1520 -0.2950  0.0356   -0.2073      0.2631   0.235
196      H3                                                               B calibrated @M        exchange   3084 -0.1428 -0.2889  0.0504   -0.1863      0.2821   0.229
202      H3                                                               B calibrated @M  bookmaker best   3346 -0.1543 -0.2885  0.0222   -0.2070      0.2636   0.259
205      H3                                                                    C blend @M        exchange    575  0.1466 -0.0425  0.3282    0.2156      0.5774   0.430
211      H3                                                                    C blend @M  bookmaker best    518  0.2446 -0.0247  0.5211    0.2288      0.5985   0.395
214      H3                                                     F disagreement 0..0.25 @M        exchange     94  0.3007 -0.3650  0.9987    0.1731      0.5745   0.311
220      H3                                                     F disagreement 0..0.25 @M  bookmaker best     85  0.2274 -0.3456  0.7222    0.1493      0.5412   0.345
