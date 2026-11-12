# Bookmaker multiples - rebuilt (registered 12 Nov 2026 10:50 Budapest, user-approved; applies from 13 Nov)

Old pipeline (26 Oct - 7 Nov, files in store/): legs were Flat races (turf, AW, Irish Flat), 6+ runners, 09:00 median
3.0-7.0, 89% favourites, 94% handicaps; grouped by bookmaker (William Hill / Betfred / Bet Victor) into Lucky 15 /
Trixie / Double / single at 0.50 a line. 44 settled bets, stake 201.50, P/L +15.66 (+7.8%); legs won 26/81 at avg 4.35.
Its exact leg filter is lost (it took 85 of 153 qualifying Flat favourites), so this is an approximation.

Rule (code pipeline/multiples.py, unchanged during the test):
- Legs: sealed CHECK BETs (rule as amended 12 Nov), not excluded, in Flat handicaps with 6+ runners and median 3.0-7.0.
- Bookmaker: one covering a leg at >= its median and >= 0.95 x best of the three; greedy - the bookmaker covering most
  remaining legs takes them all (tie: higher total price, then alphabetical). Uncovered legs dropped.
- Per bookmaker, in off-time order, groups of 4: 4 = Lucky 15 (15 lines), 3 = Trixie (4), 2 = Double (1), 1 = single.
  Stake 0.50 a line. Published to McCoy as daily/multiples_DAY.csv and multiples_latest.csv (same columns as before).
- Settle: win-only lines at the bookmaker's 09:00 price; a non-runner leg counts as void (price 1.0).
Review after 60 settled bets or at the user's request. Report P/L daily, separately from the bot file.
