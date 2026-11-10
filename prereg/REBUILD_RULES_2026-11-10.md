# Rebuilt reviewer rules (fixed 2026-11-10, before any rebuilt result is known)
Market chance = 0.6 x 1/(mean exchange price: Betfair Exchange, Matchbook, Smarkets) + 0.4 x 1/(median of all bookmakers), normalised per race.
CHECK runners = market favourite of a race with 5+ runners whose 09:00 median is 3.0-6.0.
CHECK BET: reviewer verdict BET (packet rule: chance x best exchange >= 1.05 and best exchange >= 0.95 x median). MinPrice = 0.95 x median.
Value flag: runner actively raised by the reviewer, final chance >= 1.25 x market and >= 3%, best exchange >= 100/chance. MinPrice = 100/chance.
Excluded from the bot file: bets in races with a runner that has no form and no comment.
Results from the rebuilt pipeline are reported separately from the original pipeline (21 Oct - 9 Nov).
