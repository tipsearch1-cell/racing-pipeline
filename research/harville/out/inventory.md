# Harville research - data inventory and provenance

Built 2026-11-19 11:02 UTC by research/harville/data.py. Counts only; no outcome comparisons.

## Track O - 09:00 market archive (genuine pre-race timestamps)
- races 12,991; runners 119,487; dates 2025-10-13 to 2026-10-12 (361 days)
- by code: {'Flat': 7939, 'Jumps': 5052}
- by region: {'GB': 10091, 'IRE': 2900}
- p present: 98.9% of runners
- psp present: 85.5% of runners
- bsp present: 100.0% of runners
- wsp present: 85.5% of runners
- placed_bf present: 11.3% of runners
- runners with a numeric finishing position: 94.1%
- races with a clean 1-2-3 (no dead heat in the first three, 3+ finishers): 98.9%

- races with a 09:00 price for every runner: 96.7%
- non-runners: odds rows without a result row are dropped and the 09:00 chances renormalised over runners

## Track F - Frankie sealed cards (genuine pre-race, 26 Oct 2026 onwards)
- races 1,255; runners 12,636; dates 2026-10-14 to 2026-11-19 (37 days)
- by code: {'Flat': 575, 'Jumps': 680}
- rev present: 20.0% of runners
- mkt present: 99.8% of runners
- p_model present: 100.0% of runners
- psp present: 76.3% of runners
- bsp present: 13.3% of runners
- wsp present: 76.3% of runners
- runners with a numeric finishing position: 86.2%
- races with a clean 1-2-3 (no dead heat in the first three, 3+ finishers): 96.6%

- races with Tote dividends (exacta/trifecta/CSF/tricast): 221

## Track R - RBD GB Flat 2020-2026 (closing prices: diagnostic only)
- races 44,761; runners 403,563; dates 2020-01-01 to 2026-10-09 (2347 days)
- by code: {'Flat': 44761}
- psp present: 99.7% of runners
- bsp present: 99.9% of runners
- fc present: 100.0% of runners
- placed_bf present: 99.7% of runners
- runners with a numeric finishing position: 99.0%
- races with a clean 1-2-3 (no dead heat in the first three, 3+ finishers): 99.4%

- Betfair place-terms rule (5-7: 2, 8-15: 3, 16+ hcap: 4 else 3; by runners that ran) matches RBD 'Placed in Betfair Market' count in 89.1% of 44,434 races (mismatches mostly declared-runner vs ran differences or dead heats)

## Place-price table
- Betfair place SP rows 456,125: {'rbd': 356427, 'rd': 99698}; dates 2020-01-01 to 2026-11-17

## Not available
- Historical bookmaker place / each-way prices with terms: none archived (09:00 win prices only, no EW terms, no Rule 4) -> each-way NOT TESTABLE as an executable price.
- Exchange forecast / exacta prices: none. Tote exacta/trifecta and bookmaker CSF/tricast dividends only in Racing API results saved since 10 Nov 2026 (track F).
- Frankie win probabilities before 26 Oct 2026: none archived; the rebuilt model was trained on Jan-25 Oct 2026 so a replay over that period is in-sample -> Frankie evidence is the genuine forward window only.
- Existing Frankie place probabilities (comparator E): none - Frankie has never produced place probabilities.
