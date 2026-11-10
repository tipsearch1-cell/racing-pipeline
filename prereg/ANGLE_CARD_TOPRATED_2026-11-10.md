# PAPER angle: card's own top-rated runner at Matchbook 8.0+ (registered 10 Nov 2026 16:30 Budapest, before any 11 Nov data)

Why: 26 Oct - 9 Nov back-look (in-sample, exploratory): runners whose card comment calls them top-rated / "the one to beat"
won 57 vs 52.1 expected (A/E 1.09, 95% range 0.85-1.36), +6.5% at BSP; at best exchange 8.0+: 14 won vs 11.1, +12.6% BSP.
Not significant. The reviewer no longer sees these sentences (rule amendment 10 Nov), so this is tracked separately.

Rule (code: pipeline/angle_toprated.py, unchanged during the test):
- Every GB/IRE race on the sealed card. A runner qualifies if its card comment matches the top-rated pattern in the code
  ("one to beat", "top-rated", "tops the/our", "our top", "top of the", or "ranks/ranked ... top/first ... of").
- Selected if its Matchbook 09:00 price >= 8.0. No other filters. Picks written before the first off each day.
Measure: winners vs market expected; level-stake P/L at Matchbook 09:00 (2% commission) and at BSP.
Review: after 300 settled selections. Bet-worthy only if A/E > 1 with the lower 95% bound above 1.0 AND P/L > 0 at
Matchbook 09:00. PAPER ONLY: never in the bot file unless the user decides after that review.
