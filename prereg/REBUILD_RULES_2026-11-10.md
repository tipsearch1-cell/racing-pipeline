# Rebuilt reviewer rules (fixed 2026-11-10, before any rebuilt result is known)
Market chance = 0.6 x 1/(mean exchange price: Betfair Exchange, Matchbook, Smarkets) + 0.4 x 1/(median of all bookmakers), normalised per race.
CHECK runners = market favourite of a race with 5+ runners whose 09:00 median is 3.0-6.0.
CHECK BET: reviewer verdict BET (packet rule: chance x best exchange >= 1.05 and best exchange >= 0.95 x median). MinPrice = 0.95 x median.
Value flag: runner actively raised by the reviewer, final chance >= 1.25 x market and >= 3%, best exchange >= 100/chance. MinPrice = 100/chance.
Excluded from the bot file: bets in races with a runner that has no form and no comment.
Results from the rebuilt pipeline are reported separately from the original pipeline (21 Oct - 9 Nov).

## Decision note 10 Nov 2026 14:36 (Budapest) - no rule change
Reviewed: on 5-9 Nov the old pipeline's value flags went 0/29 (market expected 3.1), CHECK BETs 8/26 (+50% at 09:00 best);
10 Nov had 18 value flags, 0 CHECK BETs, 4 races with 2+ selections. Options offered: value flags paper-only, or
one per race at <= 12.0. User decision: keep the rules as registered; value flags stay in the bot file.
Tracking from 11 Nov: report CHECK BET and value-flag results separately in every settle (count, winners vs expected,
P/L at 09:00 best and BSP). Review point: after 150 settled value flags, or earlier at the user's request.

## Amendment 10 Nov 2026 (decided 16:20 Budapest, before any 11 Nov data) - applies from 11 Nov
Source: independent review of the repo (findings in data/review_2026-11-10.md). User approved these three rule changes:
1. Exclusion: a race is excluded from the bot file if any runner is UNRACED (no form figures). The registered test
   "no form and no comment" never fired because the API writes a comment for every runner.
2. Price: every bet test uses the Matchbook 09:00 price (the exchange the bot bets on): value flag needs
   Matchbook >= 100 / reviewer chance; CHECK BET needs reviewer chance x Matchbook >= 1.05 and Matchbook >= 0.95 x median.
   No Matchbook price = no bet. Settle P/L uses the Matchbook 09:00 price (best exchange for days before 11 Nov).
3. Packet: sentences quoting the card provider's own rating or ranking ("our rating", "one to beat", "ranked", ...)
   are removed from runner comments before the reviewer sees them. Official ratings (OR) stay.
Also from 11 Nov (safety fixes, no rule change): seal re-checks CHECK status and the BET test, ignores verdicts for
non-CHECK runners, excludes races already off at seal time; the final chances are only ever scaled down to 100%.
Unchanged: value-flag thresholds (1.25x market, >= 3%), CHECK definition (fav, 5+ runners, median 3.0-6.0), MinPrices.
Build time moves from 09:05 to 08:35 UK so the bot file is ready before the ~09:30 match.
Dry run on 10 Nov's sealed reviewer output: 18 -> 15 bot bets (Rich Treasure excluded, unraced field; Franciscan Rock and
Hiddenvalley Lake had no Matchbook price). Point 3 cannot be dry-run (it changes what the reviewer reads).

## Implementation note 12 Nov 2026 08:40 UTC (no rule change)
The amendment-3 filter (remove the card's own rating/ranking sentences) missed wordings such as "top of our ranking",
"rated 114 by us, third best of twelve", "leading threat". On 12 Nov the review was sealed twice with leaking packets
(each produced one longshot value flag citing the leaked rating) BEFORE anything was published; the filter was widened
to every sentence in the provider's own voice (our/us/we, ranks/ranked/ranking, rated N, Nth/best of N, leading/main
threat or danger, top-rated, one to beat) and the review re-run once more. Both earlier seals are kept in
store/2026-11-12/review/first_seal_v1 and second_seal_v2. Only the third seal was published.
