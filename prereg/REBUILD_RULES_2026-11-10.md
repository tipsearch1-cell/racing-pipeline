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
