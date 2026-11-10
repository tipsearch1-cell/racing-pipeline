# Card review packet: Huntingdon, 2026-11-10

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
{"meeting": "huntingdon", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 1:10 Huntingdon | race_id rac_32304055433 | PricedUp Boosts And BOG Veterans' Handicap Steeple Chase
Chase | Class 4 | 2m7f129y | going Good | Turf | 5 runners | rating band 0-120 | age 9yo+
- Charles Ritz (hrs_23274083) | 10yo G | 168lb | OR 120 | draw 0 | jockey Jonathan Burke | trainer Tom George (14d 1/5) | headgear p | last run 200 days | form /1435- | MARKET 26.6% | 09:00 median 3.25 | best exchange 3.70 | CHECK (skip line 3.09)
    comment: Charles Ritz won four starts back and was third two runs ago, and he has run over today's trip and going before, while our rating of 122 ranks him third of five. The main risk is a 200-day absence, with a fifth last time out and 168 lb to carry.
- Sherborne (hrs_21267617) | 10yo G | 167lb | OR 119 | draw 0 | jockey Lorcan Williams | trainer Joe Tizzard (14d 7/25) | headgear t | last run 27 days | form 3114-5 | MARKET 23.3% | 09:00 median 4.00 | best exchange 4.10
    comment: Sherborne arrives with back-to-back wins three and four starts back, followed by a fourth and a fifth last time, and he has run over today's trip and going before, with a yard in form (7/25 in the last 14 days). The main risk is the 167 lb burden, with our rating of 115 below his official 119.
- Fern Hill (hrs_21131054) | 11yo G | 156lb | OR 108 | draw 0 | jockey Ciaran Gethings | trainer Ben Case (14d 0/7) | headgear - | last run 25 days | form 5423-7 | MARKET 17.1% | 09:00 median 5.50 | best exchange 6.20
    comment: Winless in his last five and only seventh last time out, Fern Hill is hard to fancy, though a third and a second two and three starts back show he can get involved. He has run over today's trip and going, but 156 lb is a big burden, and our figures rank him last of five.
- Onemorefortheroad (hrs_18324103) | 11yo G | 166lb | OR 118 | draw 0 | jockey Jack Quinlan | trainer Neil King (14d 0/10) | headgear p | last run 12 days | form 4P/2-6 | MARKET 17.1% | 09:00 median 5.00 | best exchange 5.80
    comment: Onemorefortheroad is fit and fresh after just 12 days, has run over today's trip and going before, and was second two starts back. Our top-rated runner at 130 is the one to beat, though he is yet to win in his last four and carries 166 lb.
- Escaria Ten (hrs_17571050) | 12yo G | 170lb | OR 122 | draw 0 | jockey Freddie Keighley(5) | trainer Martin Keighley (14d 2/10) | headgear v | last run 192 days | form PP343- | MARKET 15.9% | 09:00 median 5.50 | best exchange 6.20
    comment: Third last time out, and a fourth two starts back, Escaria Ten has run over today's trip and going before, while our rating of 129 ranks him second of five. The risk is a 192-day absence, and he carries 170 lb.

## 1:40 Huntingdon | race_id rac_32304047685 | PricedUp Bet Conditional Jockeys' Handicap Hurdle Race
Hurdle | Class 5 | 2m4f145y | going Good | Turf | 5 runners | rating band 0-100 | age 3yo+
- Teorie (hrs_31660727) | 6yo G | 168lb | OR 94 | draw 0 | jockey Toby McCain-Mitchell | trainer James Owen (14d 14/50) | headgear p | last run 24 days | form 6567-6 | MARKET 43.5% | 09:00 median 2.00 | best exchange 2.24
    comment: Teorie has been consistent without a win, finishing sixth last time out and fifth four starts back, and he has run over today's trip and going before. Fresh after 24 days, with a yard landing 14 of 50 lately, he tops our ratings at 92, though 168 lb is a stiff burden.
- Ocean Heights (hrs_24311434) | 9yo G | 166lb | OR 92 | draw 0 | jockey Rian Corcoran(3) | trainer David Pipe (14d 0/14) | headgear tp | last run 22 days | form 332714 | MARKET 20.5% | 09:00 median 4.00 | best exchange 5.00
    comment: Ocean Heights arrives off a fourth last time out, and a winner two starts back, with a 22-day break suggesting he's fit, and he has run on today's going before. The main risk is the 166 lb burden, which looks a hefty ask.
- Bread And Butter (hrs_20387024) | 11yo G | 155lb | OR 81 | draw 0 | jockey Freddie Mitchell | trainer Cynthia Woods (14d 0/3) | headgear t | last run 22 days | form 85-642 | MARKET 13.1% | 09:00 median 7.00 | best exchange 7.20
    comment: Second last time out, his best of his last five runs, Bread And Butter is yet to win in his last five but has run over today's trip and going, comes here fresh after 22 days, and our 87 rating sits six pounds above his 81 mark. The main risk is carrying 155 lb.
- U Asking Me (hrs_29735615) | 9yo G | 153lb | OR 79 | draw 0 | jockey Robbie David | trainer Daisy Hitchins (14d 0/6) | headgear - | last run 41 days | form 7P08F8 | MARKET 12.8% | 09:00 median 7.00 | best exchange 7.60
    comment: U Asking Me is winless in his last six, with an eighth last time out, a fall two starts back and a pulled up five runs ago, so he is hard to fancy. He has run over today's trip and going, and 41 days off is no concern, but 153 lb is a hefty burden for a horse ranked fifth of six on our figures.
- Watchoutitscookie (hrs_29479247) | 8yo G | 147lb | OR 73 | draw 0 | jockey Isabelle Ryder | trainer Nigel Hawke (14d 0/4) | headgear - | last run 38 days | form 70337P | MARKET 10.1% | 09:00 median 9.00 | best exchange 9.40
    comment: Pulled up last time out and without a win in his last six runs, Watchoutitscookie is hard to fancy, though he has run over today's trip and going and was third twice, three and four starts back; 147 lb is a hefty burden, and our rating has him last of six.

## 2:10 Huntingdon | race_id rac_32304049622 | PricedUp Now With Best Odds Guaranteed Mares' Novices' Hurdle Race (Herring Queen Series Qualifier) (GBB Race)
Hurdle | Class 4 | 1m7f171y | going Good | Turf | 7 runners | rating band - | age 4yo+
- Seven Stars (hrs_50841945) | 5yo M | 154lb | OR - | draw 0 | jockey Tom Bellamy | trainer Alan King (14d 1/21) | headgear - | last run 215 days | form 3/316- | MARKET 65.2% | 09:00 median 1.36 | best exchange 1.44
- Dancing Dame (hrs_36123108) | 7yo M | 161lb | OR 105 | draw 0 | jockey Jonathan Burke | trainer James Owen (14d 14/50) | headgear h | last run 35 days | form 86-251 | MARKET 19.8% | 09:00 median 4.33 | best exchange 4.90
- Marvelous Dragones (hrs_60250050) | 4yo F | 154lb | OR - | draw 0 | jockey Brian Hughes | trainer Jamie Snowden (14d 8/21) | headgear t | wind surgery | last run 313 days | form 0230- | MARKET 7.5% | 09:00 median 10.00 | best exchange 15.00
- Potters Angeltiers (hrs_58686866) | 5yo M | 154lb | OR - | draw 0 | jockey Jack Quinlan | trainer Matt Crawley (14d 0/7) | headgear - | last run 298 days | form 0736- | MARKET 4.3% | 09:00 median 17.00 | best exchange 29.00
- Chloe's Courage (hrs_43730729) | 4yo F | 154lb | OR - | draw 0 | jockey David Noonan | trainer John Ryan (14d 0/4) | headgear - | last run 8 days | form 34 | MARKET 1.4% | 09:00 median 51.00 | best exchange 95.00
- Rose of Knocknamoe (hrs_52897040) | 6yo M | 154lb | OR - | draw 0 | jockey Liam Harrison | trainer Fergal O'Brien (14d 3/28) | headgear - | last run 20 days | form 267-F | MARKET 1.0% | 09:00 median 67.00 | best exchange 160.00
- Assured (hrs_41090861) | 5yo M | 154lb | OR - | draw 0 | jockey Lee Edwards | trainer Tom Gretton (14d 1/2) | headgear h (1st time) | last run 22 days | form /- | MARKET 0.9% | 09:00 median 81.00 | best exchange 230.00

## 2:40 Huntingdon | race_id rac_32304051559 | PricedUp Boosted Prices Daily Novices' Handicap Steeple Chase
Chase | Class 5 | 2m3f189y | going Good | Turf | 6 runners | rating band 0-100 | age 4yo+
- Cap Ricochet (hrs_47033077) | 5yo G | 163lb | OR 95 | draw 0 | jockey Brian Hughes | trainer John Dawson (14d 0/3) | headgear - | last run 24 days | form 408-11 | MARKET 49.3% | 09:00 median 1.80 | best exchange 1.94
    comment: Cap Ricochet arrives an in-form threat, having won last time out and again two starts back, and he has run over today's trip and going before after a fresh 24-day break. The risk is the 163 lb he carries off an official mark of 95.
- Helios Allen (hrs_23240721) | 9yo G | 142lb | OR 74 | draw 0 | jockey Jonathan Burke | trainer Ben Case (14d 0/7) | headgear p | last run 7 days | form 5/2234 | MARKET 18.4% | 09:00 median 4.50 | best exchange 5.50
    comment: Winless in his last five, Helios Allen has been in the frame often enough, with a third two starts back and a second three starts back, but he was only fourth last time out and is back within seven days. He has run over today's trip and going, yet our figures rank him fifth of six.
- Walk The Plank (hrs_41410593) | 6yo G | 142lb | OR 74 | draw 0 | jockey Dylan Johnston | trainer Clare Hobson (14d 0/5) | headgear p | last run 8 days | form 1-4583 | MARKET 12.1% | 09:00 median 7.50 | best exchange 7.80
    comment: Walk The Plank is hard to fancy, having won just once in his last five starts, five runs back, with an eighth two starts ago the low point, though a third last time out and a quick eight-day turnaround are positives. He has run on today's going, but carries 142 lb off 74, and our rating of 73 ranks him last of six.
- Eastern Shores (hrs_39959647) | 6yo M | 158lb | OR 90 | draw 0 | jockey Kielan Woods | trainer Fergal O'Brien (14d 3/28) | headgear t | wind surgery | last run 20 days | form 256-7P | MARKET 10.3% | 09:00 median 8.50 | best exchange 9.60
    comment: Eastern Shores has been below her best lately, pulled up last time out and a seventh two starts back, but she was second five starts back and has run over today's trip and going. Fresh enough after 20 days, she's our pick on overall profile, with 158 lb the one reservation.
- Blackijo Dagrostis (hrs_39296446) | 7yo G | 144lb | OR 76 | draw 0 | jockey Stan Sheppard | trainer Matt Sheppard (14d 0/3) | headgear tp | last run 24 days | form 343-6P | MARKET 5.2% | 09:00 median 17.00 | best exchange 19.50
    comment: Blackijo Dagrostis has finished third twice and fourth in his last five, and he has run over today's trip and on this going before, while our rating of 82 sits above his official 76. The risk is the pulled-up effort last time out, and he is yet to win in recent starts under 144 lb.
- Mountain Port (hrs_38002461) | 7yo G | 168lb | OR 100 | draw 0 | jockey Robbie David(5) | trainer Daisy Hitchins (14d 0/6) | headgear t | last run 66 days | form 770-06 | MARKET 4.6% | 09:00 median 19.00 | best exchange 22.00
    comment: Sixth last time out after a 66-day break, Mountain Port has run on today's going and tops our ranking on a 4 lb edge over his official mark of 100, which makes him a genuine threat. The risk is a winless run in his last five starts while carrying 168 lb.

## 3:10 Huntingdon | race_id rac_32304053496 | PricedUp BOG From 10am Selling Handicap Hurdle Race
Hurdle | Class 5 | 1m7f171y | going Good | Turf | 6 runners | rating band - | age 3yo+
- Latin (hrs_35430472) | 5yo G | 164lb | OR 102 | draw 0 | jockey Theo Gillard | trainer Donald McCain (14d 0/23) | headgear t | last run 22 days | form 4-4722 | MARKET 31.1% | 09:00 median 2.75 | best exchange 3.15
    comment: Placed second in each of his last two outings, Latin is bang in form after 22 days off and has run over today's distance and going before, while our rating of 105 ranks him fourth of seven; the risk is a yard without a winner in 23 runners lately, and he's yet to win in his last five.
- Bright Legend (hrs_31300234) | 6yo G | 165lb | OR 103 | draw 0 | jockey J. P. O'Neill(10) | trainer Faye Bramley (14d 1/16) | headgear t | last run 11 days | form -57438 | MARKET 26.7% | 09:00 median 3.25 | best exchange 3.60
    comment: Bright Legend arrives fit after just 11 days, having run over today's trip and going before, and a third two starts back shows he can still go close off 165 lb. Yet to win in his last five, the risk is a laboured eighth last time out.
- Blackwater Lilly (hrs_42912520) | 6yo M | 152lb | OR 90 | draw 0 | jockey Jack Quinlan | trainer Neil King (14d 0/10) | headgear tp | last run 9 days | form 463563 | MARKET 20.6% | 09:00 median 4.33 | best exchange 4.60
    comment: Yet to win in her last six outings, Blackwater Lilly is hard to fancy, with a pair of thirds the best she has managed and three finishes of fifth or worse; she has run over today's trip and going, and a third last time out just nine days ago keeps her ticking over, but 152 lb is a big burden, and our rating of 97 still ranks her sixth of seven.
- Westerton (hrs_31148446) | 6yo G | 156lb | OR 94 | draw 0 | jockey I. J. Power | trainer Jennie Candlish (14d 1/3) | headgear p | last run 27 days | form 82P5P5 | MARKET 13.5% | 09:00 median 6.50 | best exchange 7.20
    comment: Fifth last time out and a second five starts back are the better recent efforts, but Westerton has twice been pulled up and is winless in his last six, so 156 lb off 94 looks a stiff ask. He has run over today's trip and going, and our rating of 100 puts him fifth of seven.
- Stopherandgo (hrs_28824859) | 9yo M | 142lb | OR 70 | draw 0 | jockey Freddie Keighley(5) | trainer David Flood (14d 0/4) | headgear t | last run 9 days | form PP9-85 | MARKET 5.9% | 09:00 median 15.00 | best exchange 17.00
    comment: Winless in her last five, with two pulled up and a ninth and eighth before a fifth last time out, Stopherandgo is hard to fancy, and 142 lb off an official mark of 70 doesn't help. On the plus side, she's back quickly after nine days and has run over this trip and going before.
- Polemon (hrs_32278428) | 7yo G | 168lb | OR 106 | draw 0 | jockey Ellis Collier(5) | trainer Bernard Llewellyn (14d 0/5) | headgear tp | last run 96 days | form P/3B-P | MARKET 2.2% | 09:00 median 34.00 | best exchange 65.00
    comment: Polemon is without a win in his last four, but he was third three starts back and has run over today's trip and going before. Our top-rated runner at 115 against an official 106, he returns after 96 days, with 168 lb the one reservation.

## 3:40 Huntingdon | race_id rac_32304057370 | PricedUp Bet Handicap Hurdle Race (Challenger Two Mile Hurdle Series Qualifier)
Hurdle | Class 4 | 1m7f171y | going Good | Turf | 8 runners | rating band 0-120 | age 3yo+
- Virtual Rock (hrs_27343379) | 7yo G | 168lb | OR 118 | draw 0 | jockey Jonathan Burke | trainer Des Donovan (14d 0/0) | headgear t | last run 27 days | form 1/8112 | MARKET 28.3% | 09:00 median 3.00 | best exchange 3.40 | CHECK (skip line 2.85)
    comment: Virtual Rock arrives in cracking form, a second last time out and a winner two and three starts back, plus he has run over today's trip and going before, but 168 lb is a hefty burden and our ratings place him only fifth of eight, with his official mark of 118 leaving little leeway.
- Gallivanted (hrs_44721880) | 4yo G | 159lb | OR 109 | draw 0 | jockey Paul O'Brien | trainer Harry Derham (14d 5/23) | headgear tp (1st time) | last run 13 days | form 133-72 | MARKET 25.2% | 09:00 median 3.50 | best exchange 3.75
    comment: Gallivanted was second last time out, just 13 days ago, and has run over today's trip and going, though a seventh two starts back and a single win in his last five starts temper the case. Our rating of 114 ranks him sixth of eight, and 159 lb is a hefty burden.
- Blues Singer (hrs_40186391) | 6yo G | 167lb | OR 117 | draw 0 | jockey Tom Bellamy | trainer Alan King (14d 1/21) | headgear - | last run 211 days | form /3914- | MARKET 18.5% | 09:00 median 4.50 | best exchange 5.30
    comment: Blues Singer has a win and a third among his last four runs, including a fourth last time out, and has run over today's trip and going before; our rating of 118 ranks him second of eight. The main risk is a 211-day absence, with a yard out of form (1/21) adding to the concern.
- Cayman Dancer (hrs_50065575) | 4yo G | 167lb | OR 110 | draw 0 | jockey Freddie Mitchell(3) | trainer Jamie Moore & Josh Moore (14d 6/28) | headgear - | last run 8 days | form 526-41 | MARKET 13.8% | 09:00 median 6.50 | best exchange 6.80
    comment: Cayman Dancer won last time out just eight days ago, and he has run over today's trip and on the going before, so he arrives fresh and in form. The risk is a patchy run of finishes before that, with a sixth and a fourth in the previous three outings, and our rating of 114 only ranks him fourth of eight.
- Lewisham Grove (hrs_50188915) | 5yo G | 168lb | OR 118 | draw 0 | jockey William Shanahan(5) | trainer Jennie Candlish (14d 1/3) | headgear - | last run 242 days | form 22152- | MARKET 5.6% | 09:00 median 15.00 | best exchange 18.50
    comment: Second last time out and a winner three starts back, but Lewisham Grove returns after 242 days off and carries 168 lb, which makes him hard to fancy. He has run over today's trip, and our rating of 110 puts him seventh of eight.
- Mister Cessna (hrs_40605845) | 5yo G | 163lb | OR 113 | draw 0 | jockey Fern O'Brien(5) | trainer Fergal O'Brien (14d 3/28) | headgear p (1st time) | last run 25 days | form 264-74 | MARKET 4.5% | 09:00 median 19.00 | best exchange 22.00
    comment: Mister Cessna was a fourth last time out and a second five starts back, and he has run over today's trip and going before, returning after 25 days. Our rating of 121 puts him top of the eight, though he is yet to win in recent starts and carries 163 lb.
- Amalfina (hrs_45921631) | 4yo F | 142lb | OR 92 | draw 0 | jockey Harry Atkins(5) | trainer D. J. Jeffreys (14d 0/4) | headgear - | last run 109 days | form 737 | MARKET 2.5% | 09:00 median 29.00 | best exchange 48.00
    comment: Amalfina is hard to fancy, having finished seventh last time out and returning from a 109-day break, and being yet to win in her last three starts, with a third two starts back her best effort. She has run over today's trip and going, and carries 142 lb, but our rating ranks her last of eight.
- Turn And Finish (hrs_44232769) | 5yo G | 155lb | OR 105 | draw 0 | jockey Charlie Hammond | trainer Steph Hollinshead (14d 0/6) | headgear - | last run 170 days | form 626-8P | MARKET 1.6% | 09:00 median 51.00 | best exchange 75.00
    comment: Turn And Finish has run over today's trip and going before, and his second four starts back shows his ability, while our rating of 115 ranks him third of eight and sits above his official 105. The risk is a 170-day absence and a pulled-up effort last time out, with 155 lb to carry.
