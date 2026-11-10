# Card review packet: Lingfield (AW), 2026-11-10

You are a racing form reviewer. Use ONLY this packet. For every race:

1. Start from each runner's MARKET chance (the sharp-weighted 09:00 price, in %).
2. Change a runner's chance ONLY where the card below gives a specific reason: recent form figures, a comment
   or spotlight line, official rating (OR) vs today's weight, days since last run, trainer's 14-day record,
   headgear or wind surgery first time, draw, trip/going/course clues in the comment. Give a one-line reason
   that names the card fact. No reason on the card = no change. Do not use outside knowledge of the horses.
3. Keep changes moderate: normally within 0.67x to 1.5x of the market chance; never beyond 0.33x to 3x.
   Totals do not need to add to 100; they are rescaled afterwards.
4. Runners marked CHECK need a verdict, BET or SKIP:
   BET only if (a) your chance x best exchange price >= 1.05 AND (b) best exchange price >= the skip line
   shown (0.95 x 09:00 median), and the card supports your chance. Otherwise SKIP. Give a one-line reason.

Write valid JSON to the out path you were given, exactly this shape (use the exact race_id and horse_id values):
{"meeting": "lingfield_aw", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 1:20 Lingfield (AW) | race_id rac_32304375038 | Sky Sports Racing Sky 415 Open National Hunt Flat Race (Category 2 Elimination) (AWT) (GBB Race)
NH Flat | Class 5 | 2m | going Standard / Slow | AW | 4 runners | rating band - | age 4-5yo
- Got To Be Real (hrs_17394529978) | 4yo G | 156lb | OR - | draw 0 | jockey Sean Bowen | trainer Olly Murphy (14d 7/37) | headgear - | last run 247 days | form 1- | MARKET 61.5% | 09:00 median 1.50 | best exchange 1.58
    comment: Winner last time out in his only recent start, Got To Be Real is unexposed and open to improvement, though he returns after 247 days off and carries 156 lb.
- Bombus Pascuorum (hrs_17391211152) | 4yo G | 163lb | OR - | draw 0 | jockey Harry Brown(7) | trainer Donald McCain (14d 0/23) | headgear - | wind surgery | last run 28 days | form 41 | MARKET 25.9% | 09:00 median 3.50 | best exchange 3.80
    comment: Bombus Pascuorum arrives a last-time-out winner, with a fourth two starts back, and has run over today's trip before, so he looks the one to beat after 28 days off. Our rating has him top of the four, with the stable's cold run (0/23) the one reservation.
- Allez Jacqueline (hrs_17395126574) | 4yo F | 149lb | OR - | draw 0 | jockey Gavin Sheehan | trainer Katy Price (14d 0/3) | headgear - | last run 191 days | form 52- | MARKET 9.6% | 09:00 median 9.50 | best exchange 10.50
    comment: Lightly raced and unexposed, Allez Jacqueline finished second last time out after a fifth the start before, so there should be more to come. She returns from 191 days off, yet remains yet to win and carries 149 lb.
- Ezenli (hrs_17394289045) | 4yo G | 156lb | OR - | draw 0 | jockey Miss Brodie Hampson | trainer Archie Watson (14d 1/6) | headgear p (1st time) | last run 16 days | form 4 | MARKET 3.0% | 09:00 median 26.00 | best exchange 40.00
    comment: Ezenli is unexposed and open to improvement, having finished fourth last time out just 16 days ago, so he should be fit enough. He is yet to win in his short recent form and carries 156 lb today.
