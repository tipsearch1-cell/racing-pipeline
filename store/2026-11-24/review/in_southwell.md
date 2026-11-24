# Card review packet: Southwell, 2026-11-24

You are a racing form reviewer. Use ONLY this packet. For every race:

1. Start from each runner's MARKET chance (the sharp-weighted 09:00 price, in %).
2. Change a runner's chance ONLY where the card below gives a specific reason: recent form figures, a comment
   or spotlight line, official rating (OR) vs today's weight, days since last run, trainer's 14-day record,
   headgear or wind surgery first time, draw, trip/going/course clues in the comment, and the DATA lines
   (rebuilt form model, last three runs with figures, run style and race pace, finishing speed). Give a one-line reason
   that names the card fact. No reason on the card = no change. Do not use outside knowledge of the horses.
3. Keep changes moderate: normally within 0.67x to 1.5x of the market chance; never beyond 0.33x to 3x.
   Totals do not need to add to 100; they are rescaled afterwards.
   DATA lines come from our own models, not the card: "model" is a form-only win chance (it ignores the market, so
   treat it as one opinion, not the answer); "fig" is a performance figure (higher = better) for that past run - Flat and jumps (Hurdle/Chase/NH Flat)
   figures are on different scales, so only compare figures from the same code as today's race;
   "for"/"against" are derived facts (figures vs field, vs mark, pace fit, jumping errors, finishing speed).
4. Runners marked CHECK are the market favourite. Give a verdict, BET or SKIP, with a one-line reason:
   BET unless the card or the DATA lines give a specific reason to doubt the favourite (then lower its chance and SKIP).
   You do not need to do any price arithmetic; the price check (skip line shown) is applied afterwards.

Write valid JSON to the out path you were given, exactly this shape (use the exact race_id and horse_id values):
{"meeting": "southwell", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 11:56 Southwell | race_id rac_32305388089 | Join The Southwell Racecourse Corporate Club Handicap Steeple Chase
Chase | Class 5 | 2m4f88y | going Good | Turf | 10 runners | rating band 0-100 | age 4yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Imperial Bede (hrs_27982899) | 8yo G | 164lb | OR 94 | draw 0 | jockey Jonjo O'Neill Jr. | trainer Jonjo & A.J. O'Neill (14d 6/36) | headgear p | last run 16 days | form 443683 | MARKET 24.4% | 09:00 median 3.50 | Matchbook 3.80 | CHECK (skip line 3.32)
    comment: Third last time out and only sixteen days ago, Imperial Bede arrives fit and in a rhythm, having run over today's trip and on this going before.
    DATA: model 9.0% | style Prominent (led 3% of runs) | runs in data 11 | last 3: 5 Oct Stratford Chase 22.6f Good To Firm 6/9; 21 Oct Worcester Chase 16.5f Good To Soft 8/9; 8 Nov Ffos Las Chase 16f Good 3/4 fig 80
    DATA for: Official rating 94, 11 lb above field average
    DATA against: Recent figures 14 lb below its current mark (looks high in the weights); Carries 10 lb more than average
- Colby Mayfield (hrs_59551324) | 6yo G | 149lb | OR 79 | draw 0 | jockey Adam Wedge | trainer John & Rhys Flint (14d 0/2) | headgear - | last run 25 days | form 935-U6 | MARKET 16.8% | 09:00 median 5.00 | Matchbook 5.70
    comment: Colby Mayfield is winless in his last five, with a sixth last time out and an unseated two starts back, and a third four starts back is his best finish.
    DATA: model 13.1% | style Midfield (led 4% of runs) | runs in data 6 | last 3: 26 Mar Chepstow Hurdle 23.6f Good To Soft 5/15; 5 May Ffos Las Hurdle 23.9f Good UR/7; 30 Oct Uttoxeter Chase 20f Good 6/11 fig 70
    DATA for: Carries 5 lb less than average
    DATA against: Best recent form figure 70, 8 lb below field average; Recent figures 9 lb below its current mark (looks high in the weights); Fell or unseated in 1 of its last 5 jumps runs
- Grain Trade (hrs_33774671) | 7yo G | 162lb | OR 92 | draw 0 | jockey Robert Dunne | trainer Billy Aprahamian (14d 0/5) | headgear ht | wind surgery | last run 28 days | form 44F-37 | MARKET 10.2% | 09:00 median 8.50 | Matchbook 9.00
    DATA: model 14.2% | style Held up (led 4% of runs) | runs in data 5 | last 3: 14 Apr Market Rasen Chase 17.2f Good F/6; 14 May Fontwell Chase 17.8f Good 3/8; 27 Oct Bangor-on-Dee Chase 17.5f Good To Soft 7/9 fig 77
    DATA for: Official rating 92, 9 lb above field average
    DATA against: Recent figures 15 lb below its current mark (looks high in the weights); Last-run finishing speed -4.1% vs that field (faded); Carries 8 lb more than average; Fell or unseated in 1 of its last 5 jumps runs; Pace: steady gallop likely, hard to come from off the pace
- Doors Breaker (hrs_28191422) | 9yo G | 142lb | OR 64 | draw 0 | jockey Jack Tudor | trainer David Pipe (14d 2/10) | headgear t | wind surgery | last run 1210 days | form P3P0P/ | MARKET 9.6% | 09:00 median 9.00 | Matchbook 9.60
    comment: Doors Breaker is hard to fancy, pulled up last time out and twice more in his last five, with a third four starts back his only bright spot, and he returns after 1210 days off.
    DATA: model 6.3% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 20% wins (2/10), last 14 days; Carries 12 lb less than average
    DATA against: Official rating 64, 19 lb below field average; Returns from a 1210-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Bravethewaves (hrs_27301729) | 9yo G | 152lb | OR 82 | draw 0 | jockey Toby Wynne | trainer Oliver Greenall & Josh Guerriero (14d 2/12) | headgear tb (1st time) | last run 25 days | form 75-03P | MARKET 9.2% | 09:00 median 9.25 | Matchbook 10.00
    comment: Pulled up last time out, Bravethewaves is winless in his last five, though a third two starts back shows he can still run a race, and he has experience of today's trip and going after 25 days off. Carrying 152 lb off 82, he looks a midfield sort.
    DATA: model 9.2% | style Prominent (led 23% of runs) | runs in data 7 | last 3: 29 Aug Cartmel Chase 21.2f Good 11/11; 4 Oct Uttoxeter Chase 24f Good 3/7; 30 Oct Uttoxeter Chase 20f Good PU/11
    DATA for: First-time headgear
    DATA against: Pulled up in 1 of its last 5 jumps runs
- Rap Soul (hrs_46913510) | 7yo G | 168lb | OR 98 | draw 0 | jockey Jack Quinlan | trainer Richard Bandey (14d 0/0) | headgear - | last run 33 days | form 0113-P | MARKET 8.0% | 09:00 median 11.00 | Matchbook 11.50
    comment: Rap Soul counts two wins in his last five starts, a winner three and four starts back, plus a third two starts back, and he has run over today's trip and going before. The risk is that he was pulled up last time out and carries 168 lb off 33 days away.
    DATA: model 19.0% | style Prominent (led 29% of runs) | runs in data 4 | last 3: 9 Mar Plumpton Chase 19.8f Good To Soft 1/4; 8 Apr Fontwell Chase 19.5f Good To Soft 3/7; 22 Oct Ffos Las Chase 19.5f Soft PU/9
    DATA for: Official rating 98, 15 lb above field average
    DATA against: Carries 14 lb more than average; Pulled up in 1 of its last 4 jumps runs
- Four Decades (hrs_56778393) | 5yo M | 149lb | OR 79 | draw 0 | jockey Finn Lambert(3) | trainer Tom Ellis (14d 1/12) | headgear p (1st time) | last run 22 days | form -8863P | MARKET 7.9% | 09:00 median 11.00 | Matchbook 12.00
    comment: The risk is that she was pulled up last time out, so she needs to bounce back.
    DATA: model 7.2% | style Held up (led 3% of runs) | runs in data 9 | last 3: 4 Sep Worcester Chase 16.5f Good 6/6; 29 Sep Sedgefield Chase 21.1f Good 3/4; 2 Nov Southwell Chase 24.5f Good PU/8
    DATA for: Carries 5 lb less than average; First-time headgear
    DATA against: Pulled up in 1 of its last 5 jumps runs; Pace: steady gallop likely, hard to come from off the pace
- Henry Box Brown (hrs_24141278) | 9yo G | 153lb | OR 83 | draw 0 | jockey James Turner(5) | trainer Mrs C. Williams (14d 0/23) | headgear p | last run 48 days | form -U6163 | MARKET 6.5% | 09:00 median 9.25 | Matchbook 21.00
    comment: Third last time out and a winner three starts back, Henry Box Brown has run over today's trip and on this going, but 48 days off and a yard 0/23 in the last fortnight temper enthusiasm, while 153 lb is a notable burden.
    DATA: model 11.2% | style Midfield (led 23% of runs) | runs in data 7 | last 3: 16 Jul Worcester Chase 23f Good 1/8; 7 Sep Newton Abbot Hurdle 26.5f Good 6/7; 7 Oct Sedgefield Chase 26.3f Good 3/3
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Trainer 0 wins from 23 runs, last 14 days; Last-run finishing speed -8.9% vs that field (faded); Race comments mention jumping mistakes in 2 of its last 5 runs; Fell or unseated in 1 of its last 5 jumps runs
- Dynamite Defense (hrs_40819569) | 5yo G | 142lb | OR 72 | draw 0 | jockey James Best | trainer Sarah-Jayne Davies (14d 0/4) | headgear p | last run 23 days | form U3P530 | MARKET 4.6% | 09:00 median 16.00 | Matchbook 24.00
    comment: Winless in his last six, Dynamite Defense was unplaced last time out and has a pulled up and an unseated in that spell, so he is hard to fancy.
    DATA: model 5.4% | style Midfield (led 4% of runs) | runs in data 9 | last 3: 10 Sep Worcester Hurdle 20f Good 5/9; 12 Oct Worcester Chase 16.5f Good To Soft 3/9; 1 Nov Worcester Chase 20f Good To Soft 11/15
    DATA for: Carries 12 lb less than average
    DATA against: Official rating 72, 11 lb below field average; Last-run finishing speed -6.1% vs that field (faded); Pulled up in 1 of its last 5 jumps runs
- The Paddy Pie (hrs_9328690) | 13yo G | 160lb | OR 90 | draw 0 | jockey Oscar Palmer(7) | trainer Joel Parkinson & Sue Smith (14d 1/15) | headgear - | last run 19 days | form 35-437 | MARKET 2.9% | 09:00 median 29.00 | Matchbook 34.00
    DATA: model 5.3% | style Held up (led 8% of runs) | runs in data 2 | last 3: 22 Apr Ludlow Chase 23.8f Good 5/6; 5 Nov Newcastle Chase 20f Good 7/9 fig 85
    DATA for: Best recent form figure 85, 7 lb above field average; Official rating 90, 7 lb above field average
    DATA against: Carries 6 lb more than average; Lightly raced: 2 runs in our data, so the model has little to go on; Aged 13, older than most of this field; Pace: steady gallop likely, hard to come from off the pace

## 12:26 Southwell | race_id rac_32305390026 | Dance Through The Decades Christmas Parties Novices' Handicap Steeple Chase
Chase | Class 5 | 3m60y | going Good | Turf | 9 runners | rating band 0-100 | age 4yo+
DATA pace: Even - Two likely leaders (Vicomte Le Brave, Could Be You). A fair, even gallop is most likely.
- Sledgehammer (hrs_58565304) | 6yo G | 167lb | OR 99 | draw 0 | jockey Oakley Brown(5) | trainer Adrian Keatley (14d 0/6) | headgear - | last run 24 days | form -64F11 | MARKET 27.7% | 09:00 median 3.23 | Matchbook 3.30 | CHECK (skip line 3.06)
    comment: Sledgehammer arrives in cracking form, a winner last time out and again two starts back, and he has run over today's trip and going, but 167 lb is a hefty burden and a fall three starts back is a blemish.
    DATA: model 26.0% | style Held up (led 3% of runs) | runs in data 8 | last 3: 18 Jul Market Rasen Chase 17.2f Good F/8; 10 Oct Hexham Chase 24.2f Good 1/9; 31 Oct Wetherby Chase 24f Good 1/4 fig 92
    DATA for: Best recent form figure 92, 10 lb above field average; Official rating 99, 11 lb above field average; Has won at this trip or further
    DATA against: Recent figures 7 lb below its current mark (looks high in the weights); Carries 10 lb more than average; Race comments mention jumping mistakes in 2 of its last 5 runs; Fell or unseated in 1 of its last 5 jumps runs
- Kastellion (hrs_52055528) | 6yo G | 167lb | OR 99 | draw 0 | jockey Charlie Deutsch | trainer Mel Rowley (14d 0/9) | headgear t | last run 23 days | form 6343-4 | MARKET 17.6% | 09:00 median 5.00 | Matchbook 5.30
    comment: Kastellion has been consistently in the frame, with a fourth last time out, a third two starts back and another third four starts back, and he has run over today's trip and going. Fresh enough after 23 days, but he is yet to win in his last five and a weight of 167 lb is the main risk.
    DATA: model 15.7% | style Held up (led 3% of runs) | runs in data 5 | last 3: 21 Mar Bangor-on-Dee Hurdle 23.1f Good 4/10; 21 Apr Ffos Las Hurdle 23.9f Good 3/12; 1 Nov Worcester Chase 20f Good To Soft 4/15 fig 97
    DATA for: Best recent form figure 97, 16 lb above field average; Official rating 99, 11 lb above field average; Last-run finishing speed +2.2% vs that field (finished strongly)
    DATA against: Trainer 0 wins from 9 runs, last 14 days; Carries 10 lb more than average
- Peckforton Hills (hrs_47064969) | 6yo G | 159lb | OR 91 | draw 0 | jockey Jack Tudor | trainer Oliver Greenall & Josh Guerriero (14d 2/12) | headgear tp | last run 220 days | form 73222- | MARKET 17.6% | 09:00 median 4.50 | Matchbook 5.70
    comment: The one concern is a 220-day absence, and he carries 159 lb.
    DATA: model 17.5% | style Midfield (led 3% of runs) | runs in data 4 | last 3: 27 Feb Doncaster Hurdle 19.4f Good To Soft 2/12; 24 Mar Southwell Hurdle 24.3f Good 2/7; 18 Apr Bangor-on-Dee Chase 24.1f Good 2/14
    DATA for: Last-run finishing speed +4.4% vs that field (finished strongly); Good recent finishing positions
    DATA against: Returns from a 220-day break
- Could Be You (hrs_49974435) | 6yo G | 149lb | OR 81 | draw 0 | jockey Richie McLernon | trainer Neil Mulholland (14d 3/16) | headgear - | last run 22 days | form 9-F851 | MARKET 14.9% | 09:00 median 5.50 | Matchbook 6.80
    comment: Could Be You won last time out, but that sits among a fifth, an eighth, a faller and a ninth in his previous four runs, so consistency is a worry.
    DATA: model 11.4% | style Leader (led 38% of runs) | runs in data 7 | last 3: 10 Sep Worcester Hurdle 23f Good 8/11; 1 Oct Southwell Hurdle 24.3f Good 5/8; 2 Nov Plumpton Chase 25.5f Good 1/4 fig 76
    DATA for: Last-run finishing speed +4.4% vs that field (finished strongly); Has won at this trip or further; Carries 8 lb less than average
    DATA against: Best recent form figure 76, 6 lb below field average; Official rating 81, 7 lb below field average; Race comments mention jumping mistakes in 2 of its last 5 runs; Fell or unseated in 1 of its last 5 jumps runs
- Danger Nap (hrs_46850860) | 5yo G | 167lb | OR 99 | draw 0 | jockey Jonjo O'Neill Jr. | trainer Jonjo & A.J. O'Neill (14d 6/36) | headgear p | last run 168 days | form 6P4-23 | MARKET 8.8% | 09:00 median 10.00 | Matchbook 11.00
    comment: Danger Nap bids to build on a third last time out and a second two starts back, and he has run over today's trip and going before.
    DATA: model 12.2% | style Prominent (led 3% of runs) | runs in data 4 | last 3: 24 Mar Southwell Hurdle 20.4f Good 4/6; 9 May Warwick Hurdle 25f Good 2/6; 9 Jun Southwell Hurdle 24.3f Good 3/12
    DATA for: Official rating 99, 11 lb above field average; Good recent finishing positions
    DATA against: Carries 10 lb more than average; Returns from a 168-day break; Race comments mention jumping mistakes in 2 of its last 4 runs; Pulled up in 1 of its last 4 jumps runs; First run over fences in our data
- Bells of Ufford (hrs_41171725) | 6yo G | 156lb | OR 88 | draw 0 | jockey David Noonan | trainer Mitchell Hunt & Tim Vaughan (14d 1/4) | headgear tp | last run 41 days | form 4-2542 | MARKET 8.0% | 09:00 median 11.00 | Matchbook 12.00
    comment: The main risk is that he is winless in his last five and carries 156 lb after 41 days off.
    DATA: model 8.9% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 10 Jul Worcester Hurdle 20f Good 5/6; 25 Aug Stratford Hurdle 22f Good To Firm 4/8; 14 Oct Ffos Las Chase 23.8f Good To Soft 2/10
- Vicomte Le Brave (hrs_17393689320) | 7yo G | 168lb | OR 100 | draw 0 | jockey Rian Corcoran(5) | trainer Cynthia Woods (14d 0/1) | headgear tp | last run 22 days | form 3-P356 | MARKET 2.1% | 09:00 median 49.50 | Matchbook 48.00
    comment: Lightly raced and open to improvement, Vicomte Le Brave has finished third twice in his last five starts, though he comes here after a sixth last time out and a fifth two starts back. He's yet to win, returns after 22 days and carries 168 lb.
    DATA: model 2.0% | style Leader (led 29% of runs) | runs in data 3 | last 3: 12 Oct Worcester Chase 23f Good To Soft 3/3; 21 Oct Worcester Chase 20f Good To Soft 5/6; 2 Nov Plumpton Hurdle 20.5f Good 6/7
    DATA for: Official rating 100, 12 lb above field average
    DATA against: Last-run finishing speed -7.3% vs that field (faded); Carries 11 lb more than average
- Scoro (hrs_39568473) | 6yo G | 142lb | OR 69 | draw 0 | jockey Harry Reed | trainer L J Morgan (14d 0/4) | headgear tp | last run 11 days | form 664PP7 | MARKET 1.8% | 09:00 median 41.00 | Matchbook 70.00
    comment: Scoro is winless in his last six, with a seventh last time out and back-to-back pulled-up efforts before that, so he is hard to fancy.
    DATA: model 3.8% | style Prominent (led 4% of runs) | runs in data 7 | last 3: 14 Sep Sedgefield Hurdle 16.8f Good PU/10; 2 Nov Southwell Hurdle 20.5f Good PU/11; 13 Nov Southwell Chase 20.5f Good 7/9 fig 61
    DATA for: Carries 15 lb less than average
    DATA against: Best recent form figure 61, 20 lb below field average; Recent figures 8 lb below its current mark (looks high in the weights); Official rating 69, 19 lb below field average; Poor recent finishing positions; Pulled up in 2 of its last 5 jumps runs
- Illico de Montave (hrs_33177291) | 8yo G | 142lb | OR 69 | draw 0 | jockey Ben Poste | trainer Rosemary Gasson (14d 0/0) | headgear p | last run 59 days | form /07-89 | MARKET 1.4% | 09:00 median 51.00 | Matchbook 140.00
    comment: Illico de Montave has been creeping backwards, finishing ninth last time out, an eighth two starts back and a seventh three starts back, and he returns after 59 days off.
    DATA: model 2.6% | style Midfield (led 8% of runs) | runs in data 2 | last 3: 26 Jul Uttoxeter Hurdle 19.9f Good 8/10; 26 Sep Market Rasen Hurdle 23.1f Good 9/10
    DATA for: Carries 15 lb less than average
    DATA against: Official rating 69, 19 lb below field average; Last-run finishing speed -10.4% vs that field (faded); Lightly raced: 2 runs in our data, so the model has little to go on; First run over fences in our data

## 12:56 Southwell | race_id rac_32305391963 | Winter Ladies Night Saturday 28th November Maiden Hurdle Race (Div I) (GBB Race)
Hurdle | Class 4 | 1m7f182y | going Good | Turf | 12 runners | rating band - | age 4yo+
DATA pace: Lone leader - Beau de Maine is the only habitual front-runner and may be allowed an easy lead.
- Beau de Maine (hrs_17394313034) | 4yo G | 158lb | OR - | draw 0 | jockey Sam Twiston-Davies | trainer Nigel & Willy Twiston-Davies (14d 4/26) | headgear - | last run 30 days | form 2 | MARKET 21.6% | 09:00 median 3.50 | Matchbook 4.50 | CHECK (skip line 3.32)
    DATA: model 16.2% | style Leader (led 57% of runs) | runs in data 1 | last 3: 25 Oct Market Rasen NH Flat 16.5f Good To Soft 2/4 fig 103
    DATA for: Pace: may get an uncontested lead
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Uda Man Dan (hrs_17395415485) | 4yo G | 158lb | OR - | draw 0 | jockey Jonathan Burke | trainer Dan Skelton (14d 19/90) | headgear - | last run - days | form - | MARKET 21.1% | 09:00 median 4.00 | Matchbook 4.30
    DATA: model 7.3% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 21% wins (19/90), last 14 days
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Popton Point (hrs_59025540) | 5yo M | 151lb | OR - | draw 0 | jockey Luke Scott(3) | trainer Jennie Candlish (14d 4/27) | headgear - | last run 262 days | form 112- | MARKET 20.2% | 09:00 median 3.88 | Matchbook 4.70
    DATA: model 11.8% | style Midfield (led 8% of runs) | runs in data 2 | last 3: 7 Feb Warwick NH Flat 16f Heavy 1/8; 7 Mar Ayr NH Flat 16f Soft 2/3
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Returns from a 262-day break; Lightly raced: 2 runs in our data, so the model has little to go on; First run over hurdles in our data
- Ballyboy Prince (hrs_17394537279) | 4yo G | 158lb | OR - | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 19/90) | headgear - | last run 21 days | form UU-6 | MARKET 10.3% | 09:00 median 7.75 | Matchbook 9.20
    DATA: model 10.3% | style Unknown | runs in data 1 | last 3: 3 Nov Lingfield Hurdle 16f Good 6/11 fig 101
    DATA for: Trainer 21% wins (19/90), last 14 days
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Grandorado (hrs_17395918211) | 6yo G | 158lb | OR - | draw 0 | jockey Jack Tudor | trainer David Pipe (14d 2/10) | headgear - | last run 268 days | form UP21- | MARKET 10.2% | 09:00 median 8.00 | Matchbook 9.20
    DATA: model 7.3% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 20% wins (2/10), last 14 days
    DATA against: Returns from a 268-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Delusionofgrandeur (hrs_51124339) | 5yo G | 158lb | OR - | draw 0 | jockey Kielan Woods | trainer Fergal O'Brien (14d 3/26) | headgear - | last run 31 days | form P62-28 | MARKET 6.8% | 09:00 median 12.75 | Matchbook 13.00
    DATA: model 12.3% | style Held up (led 5% of runs) | runs in data 2 | last 3: 6 Jun Worcester NH Flat 16f Good 2/9; 24 Oct Cheltenham NH Flat 16.5f Good To Soft 8/10
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; First run over hurdles in our data
- Tandy's Bridge (hrs_54842473) | 5yo G | 158lb | OR - | draw 0 | jockey Finn Lambert(3) | trainer Tom Ellis (14d 1/12) | headgear - | last run 23 days | form 204-0 | MARKET 3.7% | 09:00 median 21.50 | Matchbook 27.00
    DATA: model 9.8% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 24 Mar Southwell NH Flat 15.8f Good 4/7; 1 Nov Worcester Hurdle 16f Good To Soft 10/16 fig 97
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Lady Tara (hrs_17395938028) | 7yo M | 151lb | OR - | draw 0 | jockey Adam Wedge | trainer Richard Phillips (14d 2/3) | headgear - | last run - days | form - | MARKET 1.9% | 09:00 median 34.00 | Matchbook 95.00
    DATA: model 6.6% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Dressforsuccess (hrs_17394068972) | 4yo G | 158lb | OR - | draw 0 | jockey Tristan Durrell | trainer Dan Skelton (14d 19/90) | headgear - | last run 34 days | form 5 | MARKET 1.4% | 09:00 median 41.00 | Matchbook 100.00
    DATA: model 7.1% | style Unknown | runs in data 1 | last 3: 21 Oct Worcester NH Flat 16f Good To Soft 5/6 fig 100
    DATA for: Trainer 21% wins (19/90), last 14 days
    DATA against: Last-run finishing speed -2.0% vs that field (faded); Lightly raced: 1 run in our data, so the model has little to go on
- Who's The Goat (hrs_65642563) | 6yo G | 158lb | OR - | draw 0 | jockey Conor O'Farrell | trainer Micky Hammond & Becky Smith (14d 1/16) | headgear - | last run 11 days | form U | MARKET 1.4% | 09:00 median 51.00 | Matchbook 100.00
    DATA: model 4.9% | style Midfield (led 8% of runs) | runs in data 4 | last 3: 9 Sep Redcar Flat 8f Good 4/9; 26 Sep Ripon Flat 12f Good 6/9; 13 Nov Sedgefield Hurdle 17f Good UR/7
    DATA against: Fell or unseated in 1 of its last 1 jumps runs
- Shah (hrs_17393195981) | 5yo G | 158lb | OR - | draw 0 | jockey Jonathan England | trainer Sam England (14d 5/24) | headgear - | last run 17 days | form 5-2177 | MARKET 0.7% | 09:00 median 126.00 | Matchbook 240.00
    DATA: model 2.8% | style Midfield (led 5% of runs) | runs in data 3 | last 3: 16 May Newmarket Flat 7f Good 11/11; 16 Oct Uttoxeter Hurdle 16f Good 7/10; 7 Nov Uttoxeter Hurdle 16f Good 7/13
    DATA for: Trainer 21% wins (5/24), last 14 days
    DATA against: Poor recent finishing positions
- Imperial Sea (hrs_17394793857) | 5yo G | 158lb | OR - | draw 0 | jockey Robert Dunne | trainer Charles & Adam Pogson (14d 0/1) | headgear - | last run 22 days | form 5-0 | MARKET 0.7% | 09:00 median 176.00 | Matchbook 250.00
    DATA: model 3.5% | style Held up (led 8% of runs) | runs in data 1 | last 3: 2 Nov Southwell Hurdle 16f Good 11/14
    DATA against: Last-run finishing speed -9.7% vs that field (faded); Lightly raced: 1 run in our data, so the model has little to go on

## 1:26 Southwell | race_id rac_32305814229 | Winter Ladies Night Saturday 28th November Maiden Hurdle Race (Div II) (GBB Race)
Hurdle | Class 4 | 1m7f182y | going Good | Turf | 12 runners | rating band - | age 4yo+
DATA pace: Lone leader - Chilly Breeze is the only habitual front-runner and may be allowed an easy lead.
- Made In Reugny (hrs_58099503) | 4yo G | 158lb | OR - | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 19/90) | headgear - | last run 400 days | form 2- | MARKET 64.1% | 09:00 median 1.33 | Matchbook 1.39
    DATA: model 6.1% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 21% wins (19/90), last 14 days
    DATA against: Returns from a 400-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Campfield Flyer (hrs_58412137) | 4yo G | 158lb | OR - | draw 0 | jockey Luke Scott(3) | trainer Dr Richard Newland (14d 1/10) | headgear - | last run 275 days | form 62P- | MARKET 11.1% | 09:00 median 6.50 | Matchbook 9.40
    DATA: model 13.3% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 21 Jan Catterick NH Flat 15.7f Soft 2/9; 22 Feb Hereford Hurdle 16.2f Soft PU/7
    DATA against: Returns from a 275-day break; Lightly raced: 2 runs in our data, so the model has little to go on; Pulled up in 1 of its last 1 jumps runs
- Goodbye Earl (hrs_17394071058) | 4yo G | 158lb | OR - | draw 0 | jockey Rian Corcoran(5) | trainer David Pipe (14d 2/10) | headgear - | last run 26 days | form 31-3 | MARKET 10.9% | 09:00 median 6.00 | Matchbook 10.00
    DATA: model 19.9% | style Held up (led 8% of runs) | runs in data 1 | last 3: 29 Oct Ffos Las NH Flat 16f Heavy 3/6 fig 101
    DATA for: Trainer 20% wins (2/10), last 14 days
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Riptide (hrs_17395124488) | 4yo G | 158lb | OR - | draw 0 | jockey Jack Tudor | trainer David Pipe (14d 2/10) | headgear - | last run 17 days | form 16 | MARKET 5.1% | 09:00 median 13.00 | Matchbook 23.00
    DATA: model 8.5% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 7 Nov Uttoxeter Hurdle 16f Good 6/13
    DATA for: Trainer 20% wins (2/10), last 14 days
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Chilly Breeze (hrs_40687486) | 4yo G | 158lb | OR - | draw 0 | jockey Philip Armson(3) | trainer Michael Chapman (14d 0/0) | headgear h | last run 45 days | form - | MARKET 2.1% | 09:00 median 29.00 | Matchbook 75.00
    DATA: model 12.8% | style Leader (led 29% of runs) | runs in data 8 | last 3: 11 Sep Chester Flat 10.3f Good To Soft 11/11; 29 Sep Bath Flat 8f Good To Firm 1/12; 10 Oct Southwell Flat 8.1f Standard 4/12
    DATA for: Pace: may get an uncontested lead
    DATA against: First run over hurdles in our data
- Dave's Sister (hrs_17395936985) | 7yo M | 151lb | OR - | draw 0 | jockey Daire McConville(7) | trainer D. J. Jeffreys (14d 0/4) | headgear - | last run 184 days | form /2F-32 | MARKET 1.5% | 09:00 median 41.00 | Matchbook 110.00
    DATA: model 5.6% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 184-day break; Lightly raced: 0 runs in our data, so the model has little to go on; Aged 7, older than most of this field
- The Two Four (hrs_17394322421) | 5yo G | 158lb | OR - | draw 0 | jockey Adam Wedge | trainer Christian Williams (14d 1/11) | headgear - | last run 20 days | form 2-P | MARKET 1.1% | 09:00 median 63.00 | Matchbook 190.00
    DATA: model 3.5% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 4 Nov Chepstow Hurdle 16f Good To Soft PU/13
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on; Pulled up in 1 of its last 1 jumps runs
- Yafaarr (hrs_39960508) | 4yo G | 158lb | OR - | draw 0 | jockey Jonathan England | trainer Sam England (14d 5/24) | headgear t | last run 12 days | form 8 | MARKET 1.0% | 09:00 median 67.00 | Matchbook 120.00
    DATA: model 15.6% | style Held up (led 5% of runs) | runs in data 15 | last 3: 16 Oct Newcastle (AW) Flat 10f Standard 4/11 fig 73; 26 Oct Redcar Flat 8f Heavy 6/10 fig 64; 12 Nov Market Rasen Hurdle 16.5f Good To Soft 8/10
    DATA for: Trainer 21% wins (5/24), last 14 days
- Avatar Jet (hrs_36387323) | 5yo G | 158lb | OR - | draw 0 | jockey Oakley Brown(5) | trainer Declan Carroll (14d 0/6) | headgear - | last run 10 days | form P4 | MARKET 1.0% | 09:00 median 101.00 | Matchbook 95.00
    DATA: model 2.5% | style Midfield (led 29% of runs) | runs in data 12 | last 3: 17 Oct Southwell (AW) Flat 8f Standard 11/11 fig 34; 7 Nov Uttoxeter Hurdle 16f Good PU/13; 14 Nov Uttoxeter Hurdle 16f Good 4/7 fig 84
    DATA against: Pulled up in 1 of its last 2 jumps runs
- Thunder Thief (hrs_17393569375) | 4yo G | 158lb | OR - | draw 0 | jockey Charlie Todd | trainer Dan Skelton (14d 19/90) | headgear - | last run 15 days | form P0 | MARKET 0.8% | 09:00 median 81.00 | Matchbook 270.00
    DATA: model 4.3% | style Held up (led 5% of runs) | runs in data 2 | last 3: 22 Oct Ffos Las Hurdle 16f Soft PU/10; 9 Nov Stratford Hurdle 16.5f Good To Soft 11/12
    DATA for: Trainer 21% wins (19/90), last 14 days
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Pulled up in 1 of its last 2 jumps runs
- Gettothebar (hrs_17394925275) | 4yo G | 158lb | OR - | draw 0 | jockey Tristan Durrell | trainer Dan Skelton (14d 19/90) | headgear - | last run 20 days | form 0 | MARKET 0.8% | 09:00 median 126.00 | Matchbook 200.00
    DATA: model 3.9% | style Held up (led 8% of runs) | runs in data 1 | last 3: 4 Nov Chepstow Hurdle 19.5f Good To Soft 10/14
    DATA for: Trainer 21% wins (19/90), last 14 days
    DATA against: Last-run finishing speed -3.4% vs that field (faded); Lightly raced: 1 run in our data, so the model has little to go on
- Look This Way (hrs_62326390) | 4yo F | 151lb | OR - | draw 0 | jockey Charlie Deutsch | trainer Tom Ward (14d 0/3) | headgear - | last run 204 days | form 0-9 | MARKET 0.4% | 09:00 median 151.00 | Matchbook 630.00
    DATA: model 4.0% | style Prominent (led 38% of runs) | runs in data 2 | last 3: 18 Mar Huntingdon NH Flat 15.8f Good 11/14; 4 May Warwick Hurdle 16f Good 9/13
    DATA against: Returns from a 204-day break; Lightly raced: 2 runs in our data, so the model has little to go on

## 1:56 Southwell | race_id rac_32305393900 | Festive Fixtures At Southwell Racecourse Novices' Limited Handicap Hurdle Race
Hurdle | Class 5 | 1m7f182y | going Good | Turf | 14 runners | rating band 0-95 | age 3yo+
DATA pace: Even - Two likely leaders (Dino Bellagio, Little Lady Lucy). A fair, even gallop is most likely.
- Nobody Told Me (hrs_31259193) | 6yo G | 145lb | OR 74 | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 19/90) | headgear - | last run 243 days | form 75543- | MARKET 45.4% | 09:00 median 1.73 | Matchbook 1.96
    comment: Yet to win in his last five, though a third last time out is a step up on the fifth and seventh earlier, and he has run over today's trip and going.
    DATA: model 9.6% | style Held up (led 3% of runs) | runs in data 4 | last 3: 21 Feb Chepstow Hurdle 19.5f Soft 5/12; 7 Mar Hereford Hurdle 19.7f Good 4/11; 26 Mar Chepstow Hurdle 16.1f Good To Soft 3/7
    DATA for: Trainer 21% wins (19/90), last 14 days; Carries 13 lb less than average
    DATA against: Official rating 74, 13 lb below field average; Returns from a 243-day break
- Cheap Sandwiches (hrs_50906093) | 5yo G | 155lb | OR 84 | draw 0 | jockey Freddie Gordon | trainer Chris Gordon (14d 2/6) | headgear - | last run 26 days | form 445-56 | MARKET 11.7% | 09:00 median 6.50 | Matchbook 7.60
    comment: Fourth in two of his last five and fifth twice since, Cheap Sandwiches is consistent if yet to win, and he has run over today's trip and going before, returning fresh after 26 days.
    DATA: model 6.0% | style Midfield (led 4% of runs) | runs in data 5 | last 3: 24 Apr Chepstow Hurdle 16.1f Good 5/12; 9 Oct Chepstow Hurdle 16.1f Good To Soft 5/10; 29 Oct Stratford Hurdle 16.5f Good To Soft 6/9
    DATA for: Trainer 33% wins (2/6), last 14 days
- Yourcardismarked (hrs_59367203) | 5yo G | 161lb | OR 90 | draw 0 | jockey Sean Quinlan | trainer Jennie Candlish (14d 4/27) | headgear t | last run 217 days | form 05805- | MARKET 7.4% | 09:00 median 10.00 | Matchbook 13.00
    comment: Yourcardismarked was fifth last time out and has been winless in his last five, though he has run over today's trip and going before.
    DATA: model 3.8% | style Midfield (led 3% of runs) | runs in data 4 | last 3: 21 Feb Chepstow Hurdle 16.1f Soft 8/9; 14 Mar Fontwell Hurdle 17.7f Soft 10/11; 21 Apr Ffos Las Hurdle 20f Good 5/10
    DATA against: Returns from a 217-day break
- Dino Bellagio (hrs_33036024) | 7yo G | 161lb | OR 90 | draw 0 | jockey Brian Hughes | trainer Donald McCain (14d 4/27) | headgear - | wind surgery | last run 25 days | form 4847/3 | MARKET 7.0% | 09:00 median 10.00 | Matchbook 14.50
    comment: The risk is that he's winless in his last five and carries 161 lb.
    DATA: model 8.2% | style Leader (led 38% of runs) | runs in data 6 | last 3: 22 Aug Chester Flat 15.9f Good To Soft 7/9; 12 Sep Musselburgh Flat 18.1f Good 7/7; 30 Oct Uttoxeter Hurdle 16f Good 3/10 fig 89
- Everest (hrs_41845643) | 7yo M | 159lb | OR 88 | draw 0 | jockey Caoilin Quinn | trainer Jamie Moore & Josh Moore (14d 3/27) | headgear tp | last run 21 days | form 374P-4 | MARKET 5.8% | 09:00 median 13.00 | Matchbook 17.00
    comment: Everest finished fourth last time out, and with 21 days since that run she should be fit, having run over today's trip and going before. Yet to win in her last five and pulled up two starts back, she carries 159 lb off 88, which looks a stiff ask.
    DATA: model 14.6% | style Held up (led 3% of runs) | runs in data 8 | last 3: 22 May Bath Flat 14f Good To Firm 4/10; 13 Jun Bath Flat 17.1f Good 2/8; 3 Nov Lingfield Hurdle 16f Good 4/9 fig 93
    DATA for: Best recent form figure 93, 4 lb above field average; Recent figures 5 lb above its current mark (looks well handicapped); Last-run finishing speed +2.2% vs that field (finished strongly)
- Laplander (hrs_42103796) | 4yo G | 160lb | OR 89 | draw 0 | jockey Sean Bowen | trainer Tom Ward (14d 0/3) | headgear - | last run 241 days | form 6454- | MARKET 5.1% | 09:00 median 15.00 | Matchbook 19.50
    comment: Laplander has been consistent without winning, finishing fourth last time out, a fifth two starts back and a fourth three starts back, and he has run over today's trip.
    DATA: model 7.9% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 7 Feb Newbury Hurdle 16.3f Heavy 4/8; 27 Feb Newbury Hurdle 16.3f Good To Soft 5/9; 28 Mar Uttoxeter Hurdle 15.8f Good To Soft 4/8
    DATA against: Returns from a 241-day break
- Gaelic Glow (hrs_51273285) | 5yo G | 166lb | OR 95 | draw 0 | jockey Jonathan England | trainer Sam England (14d 5/24) | headgear - | last run 15 days | form 565-47 | MARKET 4.8% | 09:00 median 17.00 | Matchbook 18.50
    comment: Fit after 15 days off, Gaelic Glow has run over today's trip and on this going, and his fourth two starts back is the best of a consistent run.
    DATA: model 13.4% | style Held up (led 3% of runs) | runs in data 4 | last 3: 22 Mar Carlisle Hurdle 19.3f Good To Soft 5/10; 16 Oct Uttoxeter Hurdle 16f Good 4/10 fig 97; 9 Nov Carlisle Hurdle 17f Good To Soft 7/14 fig 85
    DATA for: Best recent form figure 97, 8 lb above field average; Official rating 95, 8 lb above field average; Trainer 21% wins (5/24), last 14 days
    DATA against: Carries 8 lb more than average
- Little Lady Lucy (hrs_38018211) | 5yo M | 156lb | OR 85 | draw 0 | jockey Mr Laurie Gallacher(10) | trainer Neil Mulholland (14d 3/16) | headgear p | last run 21 days | form 11-297 | MARKET 2.4% | 09:00 median 26.00 | Matchbook 48.00
    comment: Little Lady Lucy has slipped to a seventh last time out and a ninth before that, a worrying drift after back-to-back wins, and carrying 156 lb makes this hard to fancy. In her favour, she has run over today's trip and going, and a 21-day break is no concern.
    DATA: model 9.5% | style Leader (led 23% of runs) | runs in data 8 | last 3: 30 May Stratford Hurdle 16.3f Good To Firm 2/7; 29 Jun Stratford Hurdle 16.3f Good To Firm 9/14; 3 Nov Lingfield Hurdle 16f Good 7/9 fig 73
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 73, 16 lb below field average; Recent figures 12 lb below its current mark (looks high in the weights); Last-run finishing speed -3.3% vs that field (faded)
- Milady du Breuil (hrs_58196607) | 4yo F | 161lb | OR 90 | draw 0 | jockey Jack Tudor | trainer Christian Williams (14d 1/11) | headgear - | last run 226 days | form 6454F- | MARKET 2.4% | 09:00 median 23.00 | Matchbook 70.00
    comment: The risk is a 226-day absence, and she fell last time out, carrying 161 lb.
    DATA: model 6.1% | style Held up (led 4% of runs) | runs in data 3 | last 3: 27 Jan Chepstow Hurdle 16.1f Soft 5/10; 9 Mar Taunton Hurdle 16.5f Good 4/8; 12 Apr Ffos Las Hurdle 20f Good To Soft F/12
    DATA against: Returns from a 226-day break; Fell or unseated in 1 of its last 3 jumps runs
- Tenadaay (hrs_46384044) | 4yo G | 157lb | OR 86 | draw 0 | jockey Kielan Woods | trainer Fergal O'Brien (14d 3/26) | headgear - | last run 23 days | form 37-9 | MARKET 2.2% | 09:00 median 26.00 | Matchbook 60.00
    comment: Winless in his last three, Tenadaay has gone backwards since a third three starts back, finishing a seventh and then a ninth last time out, and he carries 157 lb off an official mark of 86.
    DATA: model 8.0% | style Prominent (led 23% of runs) | runs in data 5 | last 3: 15 Aug Lingfield Flat 13f Standard 7/9; 18 Sep Wolverhampton Flat 12.2f Standard 2/7; 1 Nov Huntingdon Hurdle 16f Good 9/10
    DATA against: Last-run finishing speed -5.8% vs that field (faded)
- On Subs (hrs_58412109) | 4yo G | 151lb | OR 80 | draw 0 | jockey Adam Wedge | trainer Christian Williams (14d 1/11) | headgear - | last run 28 days | form 8-59 | MARKET 2.0% | 09:00 median 34.00 | Matchbook 60.00
    comment: Lightly raced and yet to win, On Subs has finished ninth last time out, a fifth two starts back and an eighth three starts back, so he remains unexposed and open to improvement. He returns after 28 days off, carrying 151 lb off an official mark of 80.
    DATA: model 1.3% | style Held up (led 8% of runs) | runs in data 2 | last 3: 11 Oct Chepstow Hurdle 16.1f Good To Soft 5/6; 27 Oct Bangor-on-Dee Hurdle 16.5f Good 9/11
    DATA for: Carries 7 lb less than average
    DATA against: Official rating 80, 7 lb below field average; Lightly raced: 2 runs in our data, so the model has little to go on
- Orbys River (hrs_32568592) | 8yo M | 153lb | OR 82 | draw 0 | jockey Toby Wynne | trainer Sam Allwood (14d 1/1) | headgear - | last run 589 days | form 12715/ | MARKET 1.6% | 09:00 median 29.00 | Matchbook 120.00
    comment: Absent for 589 days, Orbys River is hard to fancy, and a fifth last time out followed by a seventh three starts back shows the form is patchy, with 153 lb to carry too. In her favour, she won two starts back and five starts back, and has run over today's trip and going.
    DATA: model 4.9% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 589-day break; Lightly raced: 0 runs in our data, so the model has little to go on; Aged 8, older than most of this field
- Troy Story (hrs_43637076) | 4yo G | 162lb | OR 91 | draw 0 | jockey Lee Edwards | trainer Dave Roberts (14d 0/1) | headgear ht | wind surgery | last run 38 days | form 055 | MARKET 1.3% | 09:00 median 41.00 | Matchbook 140.00
    comment: Troy Story has finished fifth in each of his last two starts, and he has run over today's trip and going before, though he's winless in his last three and returns after 38 days off.
    DATA: model 2.4% | style Held up (led 4% of runs) | runs in data 5 | last 3: 10 Sep Worcester Hurdle 16f Good 11/12; 4 Oct Uttoxeter Hurdle 15.8f Good 5/8; 17 Oct Market Rasen Hurdle 16.5f Good 5/8 fig 92
- Trackman (hrs_32638172) | 6yo G | 162lb | OR 91 | draw 0 | jockey Jack Quinlan | trainer Simon Pearce (14d 1/2) | headgear - | last run 29 days | form 658 | MARKET 0.8% | 09:00 median 78.00 | Matchbook 300.00
    comment: Trackman has finished eighth, fifth and sixth in his last three starts, so he is winless in that spell, though a 29-day break and prior experience over today's trip and going are in his favour.
    DATA: model 4.2% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 17 Jun Worcester Hurdle 16f Good 5/9; 22 Jul Worcester Hurdle 16f Good 8/9; 26 Oct Leicester Flat 10f Soft 14/16

## 2:26 Southwell | race_id rac_32305395837 | Christmas Jumper Day Sunday 13th December Handicap Hurdle Race
Hurdle | Class 4 | 2m4f88y | going Good | Turf | 15 runners | rating band 0-110 | age 3yo+
DATA pace: Even - Two likely leaders (Ballin Bay, Ka Mate du Brivet). A fair, even gallop is most likely.
- In The Purple (hrs_58380224) | 5yo G | 160lb | OR 102 | draw 0 | jockey Sean Bowen | trainer Olly Murphy (14d 10/57) | headgear - | last run 279 days | form 87001- | MARKET 18.5% | 09:00 median 4.50 | Matchbook 4.80 | CHECK (skip line 4.27)
    comment: In The Purple won last time out, but that came after a run of unplaced efforts and a seventh and eighth before it, and he returns after 279 days off.
    DATA: model 10.1% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 18 Feb Southwell Hurdle 20.4f Soft 1/11
    DATA for: Last-run finishing speed +3.5% vs that field (finished strongly); Has won at this trip or further
    DATA against: Returns from a 279-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Typhoon Warrior (hrs_57718752) | 5yo G | 162lb | OR 104 | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 19/90) | headgear - | last run 46 days | form 4366-9 | MARKET 16.3% | 09:00 median 5.00 | Matchbook 5.40
    comment: Typhoon Warrior is winless in his last five, with a ninth last time out following two sixths, though a third four starts back shows he has a bit of ability.
    DATA: model 4.2% | style Held up (led 3% of runs) | runs in data 4 | last 3: 7 Feb Newbury Hurdle 16.3f Heavy 6/8; 8 Mar Warwick Hurdle 16f Good To Soft 6/11; 9 Oct Chepstow Hurdle 16.1f Good To Soft 9/15
    DATA for: Trainer 21% wins (19/90), last 14 days
    DATA against: Last-run finishing speed -2.4% vs that field (faded); Poor recent finishing positions
- The Boss Bear (hrs_51735887) | 6yo G | 165lb | OR 107 | draw 0 | jockey Jonathan Burke | trainer James Owen (14d 4/45) | headgear - | last run 22 days | form 2P88-4 | MARKET 13.9% | 09:00 median 6.00 | Matchbook 6.40
    comment: The risk is a winless run in his last five starts, with two eighths in that spell, and 165 lb to carry.
    DATA: model 7.1% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 21 Mar Newbury Hurdle 18.8f Good To Soft 8/9; 6 Apr Plumpton Hurdle 20.5f Good 8/12; 2 Nov Plumpton Hurdle 20.5f Good 4/7 fig 106
    DATA for: Best recent form figure 106, 6 lb above field average
    DATA against: Race comments mention jumping mistakes in 2 of its last 5 runs; Pulled up in 1 of its last 5 jumps runs
- Presenting Milan (hrs_44264472) | 6yo G | 162lb | OR 104 | draw 0 | jockey Jonjo O'Neill Jr. | trainer Robert Hawker (14d 0/0) | headgear - | last run 34 days | form 62/1-3 | MARKET 10.2% | 09:00 median 7.50 | Matchbook 9.20
    comment: Presenting Milan arrives in solid recent form, third last time out, a winner two starts back, and a second three starts back, and he has run over today's trip and going before.
    DATA: model 9.1% | style Unknown | runs in data 1 | last 3: 21 Oct Worcester Hurdle 20f Good To Soft 3/8 fig 105
    DATA for: Best recent form figure 105, 4 lb above field average; Last-run finishing speed +2.7% vs that field (finished strongly)
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Eternity Rose (hrs_50401694) | 5yo G | 160lb | OR 102 | draw 0 | jockey Liam Harrison | trainer Fergal O'Brien (14d 3/26) | headgear - | last run 197 days | form 3053-4 | MARKET 6.0% | 09:00 median 13.00 | Matchbook 15.50
    comment: Eternity Rose has been consistent without a win, with a fourth last time out, a third two starts back, and another third five starts back, and he has run over today's trip and on the going before.
    DATA: model 7.5% | style Midfield (led 29% of runs) | runs in data 5 | last 3: 23 Mar Kempton Hurdle 16f Good 5/10; 12 Apr Wincanton Hurdle 15.2f Good 3/7; 11 May Southwell Hurdle 20.4f Good 4/10
    DATA against: Returns from a 197-day break; Race comments mention jumping mistakes in 3 of its last 4 runs
- At Mangan Bridge (hrs_47621056) | 8yo G | 166lb | OR 108 | draw 0 | jockey Charlie Hammond | trainer Stuart Edmunds (14d 2/14) | headgear t | last run 25 days | form 3511-0 | MARKET 6.0% | 09:00 median 13.00 | Matchbook 16.00
    comment: At Mangan Bridge won two starts back and three starts back, but was unplaced last time out, and he has run over today's trip and going before.
    DATA: model 5.3% | style Held up (led 8% of runs) | runs in data 1 | last 3: 30 Oct Uttoxeter Hurdle 20f Good 12/15
    DATA against: Last-run finishing speed -2.3% vs that field (faded); Lightly raced: 1 run in our data, so the model has little to go on
- Ka Mate du Brivet (hrs_51123912) | 5yo G | 166lb | OR 108 | draw 0 | jockey Caoilin Quinn | trainer Warren Greatrex (14d 6/24) | headgear - | last run 191 days | form /192-2 | MARKET 5.1% | 09:00 median 13.00 | Matchbook 21.00
    comment: The risk is a 191-day absence, plus 166 lb on his back.
    DATA: model 6.1% | style Leader (led 54% of runs) | runs in data 3 | last 3: 18 Feb Southwell NH Flat 15.8f Soft 9/11; 27 Mar Fontwell Hurdle 21.7f Good To Soft 2/3; 17 May Stratford Hurdle 22f Good To Firm 2/6
    DATA for: Trainer 25% wins (6/24), last 14 days; Last-run finishing speed +4.7% vs that field (finished strongly); Good recent finishing positions
    DATA against: Returns from a 191-day break
- Laysoft (hrs_57686986) | 4yo F | 156lb | OR 99 | draw 0 | jockey Peter Kavanagh | trainer Joel Parkinson & Sue Smith (14d 1/15) | headgear - | last run 28 days | form 3235-3 | MARKET 5.0% | 09:00 median 14.00 | Matchbook 22.00
    comment: Laysoft has been thereabouts, with a third last time out and a second four starts back, but she is winless in her last five and carries 156 lb off an official mark of 99.
    DATA: model 4.0% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 24 Jan Doncaster Hurdle 16.6f Soft 3/5; 26 Feb Wetherby Hurdle 19.7f Soft 5/6; 27 Oct Bangor-on-Dee Hurdle 19.5f Good 3/10 fig 95
    DATA for: Last-run finishing speed +2.1% vs that field (finished strongly); Good recent finishing positions; Carries 6 lb less than average
    DATA against: Best recent form figure 95, 6 lb below field average; Official rating 99, 5 lb below field average
- Smile Back (hrs_41378610) | 6yo M | 158lb | OR 100 | draw 0 | jockey Adam Wedge | trainer Richard Phillips (14d 2/3) | headgear h | last run 217 days | form 22634- | MARKET 4.8% | 09:00 median 17.00 | Matchbook 20.00
    DATA: model 7.6% | style Prominent (led 4% of runs) | runs in data 3 | last 3: 17 Jan Taunton Hurdle 23.9f Good To Soft 6/13; 16 Feb Carlisle Hurdle 25f Good To Soft 3/9; 21 Apr Ffos Las Hurdle 23.9f Good 4/12
    DATA for: Last-run finishing speed +2.7% vs that field (finished strongly)
    DATA against: Returns from a 217-day break
- Blazing Duke (hrs_51766253) | 5yo G | 163lb | OR 105 | draw 0 | jockey Jack Tudor | trainer Oliver Greenall & Josh Guerriero (14d 2/12) | headgear - | last run 238 days | form /57U3- | MARKET 3.4% | 09:00 median 15.00 | Matchbook 55.00
    comment: Blazing Duke is winless in his last four, with an unseated and a seventh in there, and he returns after 238 days off, which makes him hard to fancy under 163 lb.
    DATA: model 8.7% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 17 Mar Wexford Hurdle 16f Soft UR/14; 31 Mar Limerick Hurdle 16f Soft 3/12
    DATA for: Last-run finishing speed +3.2% vs that field (finished strongly)
    DATA against: Returns from a 238-day break; Lightly raced: 2 runs in our data, so the model has little to go on; Race comments mention jumping mistakes in 2 of its last 2 runs; Fell or unseated in 1 of its last 2 jumps runs
- Stroll On By (hrs_27082804) | 9yo G | 159lb | OR 101 | draw 0 | jockey Brian Hughes | trainer Charlie Longsdon (14d 2/16) | headgear - | last run 19 days | form 55FU-4 | MARKET 3.2% | 09:00 median 19.00 | Matchbook 38.00
    DATA: model 3.1% | style Held up (led 8% of runs) | runs in data 1 | last 3: 5 Nov Plumpton Hurdle 16f Good 4/4 fig 96
    DATA against: Best recent form figure 96, 4 lb below field average; Lightly raced: 1 run in our data, so the model has little to go on
- Magical Arthur (hrs_33479873) | 8yo G | 168lb | OR 110 | draw 0 | jockey Sean Quinlan | trainer Jennie Candlish (14d 4/27) | headgear tp | last run 528 days | form 2P/01- | MARKET 2.6% | 09:00 median 21.00 | Matchbook 55.00
    comment: Magical Arthur won last time out and was second four starts back, but he returns after 528 days off and has an unplaced run and a pulled up in between.
    DATA: model 6.0% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Official rating 110, 6 lb above field average
    DATA against: Carries 6 lb more than average; Returns from a 528-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Ithaka (hrs_23836848) | 10yo G | 159lb | OR 101 | draw 0 | jockey Ciaran Gethings | trainer Alastair Ralph (14d 0/6) | headgear t | last run 26 days | form 1PPF-P | MARKET 1.8% | 09:00 median 34.00 | Matchbook 80.00
    comment: Ithaka has failed to complete in his last four outings, pulled up last time out, a faller two starts back, then pulled up twice more, so a win five starts back is the only bright spot.
    DATA: model 3.9% | style Held up (led 5% of runs) | runs in data 5 | last 3: 15 Mar Chepstow Chase 23.6f Soft PU/11; 27 Mar Wetherby Chase 24.2f Good F/9; 29 Oct Stratford Chase 22.5f Good To Soft PU/6
    DATA for: Has won at this trip or further
    DATA against: Poor recent finishing positions; Race comments mention jumping mistakes in 2 of its last 5 runs; Fell or unseated in 1 of its last 5 jumps runs; Pulled up in 3 of its last 5 jumps runs; First run over hurdles in our data; Aged 10, older than most of this field
- Ballin Bay (hrs_33205123) | 8yo G | 166lb | OR 108 | draw 0 | jockey Shane Fitzgerald | trainer Rebecca Menzies (14d 0/10) | headgear - | last run 234 days | form 41117- | MARKET 1.6% | 09:00 median 34.00 | Matchbook 90.00
    comment: Ballin Bay won three on the bounce before a seventh last time out, and he has run over today's trip and going, but a 234-day layoff and 166 lb on his back temper the appeal.
    DATA: model 10.4% | style Leader (led 54% of runs) | runs in data 5 | last 3: 19 Feb Sedgefield Hurdle 27f Soft 1/7; 19 Mar Sedgefield Chase 26.3f Good 1/3; 4 Apr Carlisle Hurdle 25f Good 7/10
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Trainer 0 wins from 10 runs, last 14 days; Last-run finishing speed -3.2% vs that field (faded); Returns from a 234-day break
- Starshine Legend (hrs_37617986) | 5yo G | 163lb | OR 105 | draw 0 | jockey James Best | trainer Sarah-Jayne Davies (14d 0/4) | headgear p | last run 63 days | form 35715 | MARKET 1.6% | 09:00 median 34.00 | Matchbook 120.00
    comment: Starshine Legend was a fifth last time out after a win two starts back, but he's had 63 days off and carries 163 lb, which makes him hard to fancy.
    DATA: model 6.8% | style Midfield (led 4% of runs) | runs in data 7 | last 3: 22 Jul Worcester Hurdle 16f Good 7/9; 19 Aug Worcester Hurdle 20f Good 1/9; 22 Sep Fontwell Hurdle 21.7f Good 5/7
    DATA for: Has won at this trip or further

## 2:56 Southwell | race_id rac_32305397774 | Book The Bistro In Seasons Restaurant Handicap Hurdle Race
Hurdle | Class 5 | 3m60y | going Good | Turf | 9 runners | rating band 0-100 | age 3yo+
DATA pace: Even - Two likely leaders (Has Troke, Innisfree Lass). A fair, even gallop is most likely.
- Gimarias (hrs_50005746) | 6yo G | 166lb | OR 98 | draw 0 | jockey Toby Wynne | trainer Mel Rowley (14d 0/9) | headgear - | last run 20 days | form F753-2 | MARKET 29.1% | 09:00 median 2.88 | Matchbook 3.20
    comment: Gimarias arrives in rising form after a second last time out and a third two starts back, and he has run on today's going before.
    DATA: model 16.5% | style Midfield (led 4% of runs) | runs in data 5 | last 3: 21 Mar Bangor-on-Dee Hurdle 19.6f Good 5/10; 18 Apr Bangor-on-Dee Hurdle 19.6f Good 3/9; 4 Nov Chepstow Hurdle 19.5f Good To Soft 2/16 fig 98
    DATA for: Best recent form figure 98, 6 lb above field average; Official rating 98, 7 lb above field average; Last-run finishing speed +6.0% vs that field (finished strongly); Good recent finishing positions
    DATA against: Trainer 0 wins from 9 runs, last 14 days; Carries 7 lb more than average; Fell or unseated in 1 of its last 5 jumps runs
- The Brave Guy (hrs_40225178) | 6yo G | 161lb | OR 93 | draw 0 | jockey Sean Quinlan | trainer Jennie Candlish (14d 4/27) | headgear - | last run 164 days | form /79-56 | MARKET 17.4% | 09:00 median 5.00 | Matchbook 5.30
    comment: He has run on today's going before and an official 93 gives him some leeway, but 161 lb is a lot to carry.
    DATA: model 14.2% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 2 May Hexham Hurdle 16.2f Good 5/9; 13 Jun Uttoxeter Hurdle 19.9f Good 6/12
    DATA against: Returns from a 164-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- Harrys Hope (hrs_33081034) | 8yo M | 167lb | OR 99 | draw 0 | jockey Jack Quinlan | trainer Matt Crawley (14d 0/2) | headgear - | last run 22 days | form -24243 | MARKET 11.3% | 09:00 median 7.50 | Matchbook 8.40
    comment: Harrys Hope is admirably consistent, finishing third last time out, with a second five starts back, and she has run over today's trip and going before.
    DATA: model 15.2% | style Midfield (led 4% of runs) | runs in data 5 | last 3: 19 Aug Worcester Chase 23f Good 2/6; 4 Sep Bangor-on-Dee Chase 24.1f Good 4/7; 2 Nov Southwell Chase 24.5f Good 3/8 fig 106
    DATA for: Best recent form figure 106, 14 lb above field average; Recent figures 7 lb above its current mark (looks well handicapped); Official rating 99, 8 lb above field average; Good recent finishing positions
    DATA against: Carries 8 lb more than average; First run over hurdles in our data
- Elusive Shine (hrs_40224996) | 6yo G | 152lb | OR 84 | draw 0 | jockey Jonathan England | trainer Sam England (14d 5/24) | headgear t (1st time) | last run 698 days | form 29533/ | MARKET 10.7% | 09:00 median 8.50 | Matchbook 8.60
    comment: Elusive Shine is yet to win in his last five starts, though a third last time out, and a third two starts back, show he has been competitive.
    DATA: model 8.3% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 21% wins (5/24), last 14 days; Carries 7 lb less than average; First-time headgear
    DATA against: Official rating 84, 7 lb below field average; Returns from a 698-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Twp Stori (hrs_32996390) | 8yo G | 149lb | OR 81 | draw 0 | jockey Philip Armson(3) | trainer Samuel Drinkwater (14d 0/5) | headgear - | last run 145 days | form 56-332 | MARKET 8.6% | 09:00 median 8.50 | Matchbook 13.50
    comment: He has run over today's trip and on the going before.
    DATA: model 8.8% | style Held up (led 8% of runs) | runs in data 4 | last 3: 24 May Fontwell Chase 26f Good 3/5; 13 Jun Uttoxeter Chase 24f Good 3/10; 2 Jul Perth Chase 23.8f Good 2/7
    DATA for: Last-run finishing speed +2.4% vs that field (finished strongly); Good recent finishing positions; Carries 10 lb less than average
    DATA against: Official rating 81, 10 lb below field average; Returns from a 145-day break
- Ocean Walz (hrs_39808146) | 6yo G | 153lb | OR 85 | draw 0 | jockey Ben Poste | trainer Rosemary Gasson (14d 0/0) | headgear - | last run 238 days | form 68286- | MARKET 8.3% | 09:00 median 10.00 | Matchbook 12.00
    comment: The big risk is a 238-day absence, with a sixth last time out and 153 lb to carry.
    DATA: model 8.9% | style Midfield (led 4% of runs) | runs in data 4 | last 3: 26 Feb Ludlow Hurdle 21.2f Good To Soft 2/8; 11 Mar Huntingdon Hurdle 20.7f Good 8/14; 31 Mar Bangor-on-Dee Hurdle 23.1f Good 6/8
    DATA for: Carries 6 lb less than average
    DATA against: Official rating 85, 6 lb below field average; Returns from a 238-day break
- Has Troke (hrs_23905735) | 9yo G | 168lb | OR 100 | draw 0 | jockey Kielan Woods | trainer Alex Hales (14d 0/6) | headgear - | last run 280 days | form 1/357- | MARKET 5.6% | 09:00 median 15.00 | Matchbook 17.50
    comment: Has Troke has a win and a third in his last four starts and has run over today's trip, though he has slipped to a fifth and then a seventh since; at 168 lb and 280 days off, rustiness is the one real worry.
    DATA: model 9.5% | style Leader (led 72% of runs) | runs in data 2 | last 3: 23 Jan Warwick Hurdle 25f Good To Soft 5/9; 17 Feb Market Rasen Hurdle 23.1f Soft 7/9
    DATA for: Official rating 100, 9 lb above field average
    DATA against: Last-run finishing speed -6.4% vs that field (faded); Carries 9 lb more than average; Returns from a 280-day break; Lightly raced: 2 runs in our data, so the model has little to go on; Aged 9, older than most of this field
- Innisfree Lass (hrs_30589244) | 8yo M | 164lb | OR 96 | draw 0 | jockey Harry Atkins(5) | trainer Joey Ramsden (14d 0/3) | headgear t | last run 151 days | form 5315-P | MARKET 5.2% | 09:00 median 17.00 | Matchbook 18.00
    comment: The risk is a 151-day absence after she was pulled up last time out.
    DATA: model 12.5% | style Leader (led 54% of runs) | runs in data 5 | last 3: 18 Feb Southwell Hurdle 24.3f Soft 1/6; 14 Mar Fontwell Hurdle 25.8f Soft 5/6; 26 Jun Bangor-on-Dee Hurdle 23.1f Good PU/8
    DATA for: Has won at this trip or further
    DATA against: Returns from a 151-day break; Race comments mention jumping mistakes in 2 of its last 5 runs; Pulled up in 1 of its last 5 jumps runs
- Eyeeye (hrs_30455124) | 6yo G | 154lb | OR 86 | draw 0 | jockey Mr Henry Bailey(7) | trainer Clare Ellam (14d 0/1) | headgear - | last run 18 days | form 950847 | MARKET 3.9% | 09:00 median 17.00 | Matchbook 34.00
    comment: Eyeeye is winless in his last six, with a seventh last time out and a fourth two starts back the best of recent efforts, though he has run on today's going before and returns after 18 days.
    DATA: model 6.1% | style Held up (led 3% of runs) | runs in data 9 | last 3: 4 Sep Bangor-on-Dee Hurdle 19.6f Good 8/11; 13 Oct Southwell Hurdle 20.4f Good 4/11; 6 Nov Fontwell Hurdle 17.5f Good 7/10 fig 73
    DATA for: Carries 5 lb less than average
    DATA against: Best recent form figure 73, 19 lb below field average; Recent figures 13 lb below its current mark (looks high in the weights); Official rating 86, 5 lb below field average

## 3:26 Southwell | race_id rac_32305399711 | Conferences And Events At Southwell Racecourse Handicap Hurdle Race
Hurdle | Class 3 | 1m7f182y | going Good | Turf | 8 runners | rating band 0-130 | age 3yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Wild Goose (hrs_47807235) | 6yo G | 164lb | OR 124 | draw 0 | jockey Aamilah Aswat(7) | trainer Kim Bailey & Mat Nicholls (14d 6/22) | headgear t | last run 32 days | form 21-514 | MARKET 31.5% | 09:00 median 2.88 | Matchbook 2.98
    comment: Wild Goose won two starts back and four starts back, and he has run over today's trip and on the going before, while a yard in form (6 from 22 in the last 14 days) adds weight to his claims. The risk is a fourth last time out after 32 days off, plus 164 lb on his back.
    DATA: model 19.6% | style Prominent (led 8% of runs) | runs in data 6 | last 3: 4 May Warwick Hurdle 16f Good 5/8; 1 Oct Southwell Hurdle 15.8f Good 1/8; 23 Oct Cheltenham Hurdle 16.5f Good To Soft 4/11 fig 124
    DATA for: Best recent form figure 124, 9 lb above field average; Trainer 27% wins (6/22), last 14 days; Has won at this trip or further
- Manuelito (hrs_31518466) | 6yo G | 168lb | OR 128 | draw 0 | jockey Ben Jones | trainer Philip Hobbs & Johnson White (14d 2/15) | headgear - | last run 18 days | form 9/1F-4 | MARKET 24.8% | 09:00 median 3.50 | Matchbook 4.00
    comment: Manuelito signed off with a fourth last time out, 18 days ago, and has a win three starts back, so he arrives fit and with a recent victory on his CV.
    DATA: model 12.7% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 6 Nov Aintree Hurdle 17f Good To Soft 4/7 fig 127
    DATA for: Best recent form figure 127, 12 lb above field average; Official rating 128, 8 lb above field average
    DATA against: Carries 8 lb more than average; Lightly raced: 1 run in our data, so the model has little to go on
- The Cistercian (hrs_53081168) | 6yo G | 164lb | OR 124 | draw 0 | jockey Charlie Hammond | trainer Stuart Edmunds (14d 2/14) | headgear - | wind surgery | last run 244 days | form 3U3U2- | MARKET 14.3% | 09:00 median 6.45 | Matchbook 6.60
    comment: The Cistercian bounced back from an unseating with a second last time out, and he has been placed in two of his other recent runs, so he has a real chance. He has run over today's trip and going, but 244 days off and 164 lb are the main risk.
    DATA: model 18.9% | style Held up (led 3% of runs) | runs in data 4 | last 3: 31 Jan Sandown Hurdle 16f Soft 3/6; 5 Mar Haydock Hurdle 18.9f Good To Soft UR/13; 25 Mar Hexham Hurdle 16.2f Soft 2/9
    DATA for: Last-run finishing speed +3.3% vs that field (finished strongly)
    DATA against: Returns from a 244-day break; Fell or unseated in 2 of its last 4 jumps runs; Pace: steady gallop likely, hard to come from off the pace
- Klitschko (hrs_30315586) | 8yo G | 157lb | OR 117 | draw 0 | jockey Brian Hughes | trainer Lucinda Hughes (14d 0/0) | headgear t | last run 24 days | form U1-422 | MARKET 10.0% | 09:00 median 8.00 | Matchbook 10.50
    DATA: model 14.3% | style Prominent (led 29% of runs) | runs in data 6 | last 3: 4 Oct Kelso Hurdle 20.9f Good To Firm 4/7; 18 Oct Sedgefield Hurdle 17f Good 2/9 fig 118; 31 Oct Wetherby Hurdle 16f Good 2/4 fig 116
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Fell or unseated in 1 of its last 5 jumps runs
- Lawrenny (hrs_38073987) | 7yo G | 163lb | OR 123 | draw 0 | jockey Sean Quinlan | trainer Jennie Candlish (14d 4/27) | headgear p | last run 199 days | form 1/P5-4 | MARKET 5.9% | 09:00 median 15.00 | Matchbook 16.50
    comment: Lawrenny was a fourth last time out and a fifth two starts back, with a win four starts back the highlight of his recent form, and he has run over today's trip.
    DATA: model 10.2% | style Held up (led 5% of runs) | runs in data 2 | last 3: 31 Mar Newcastle Hurdle 20.3f Good To Soft 5/6; 9 May Hexham Hurdle 20.1f Good To Soft 4/12
    DATA against: Returns from a 199-day break; Lightly raced: 2 runs in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Saligo Bay (hrs_22399853) | 8yo G | 155lb | OR 115 | draw 0 | jockey Jonathan England | trainer Sam England (14d 5/24) | headgear - | last run 37 days | form 5-8PP6 | MARKET 4.7% | 09:00 median 15.00 | Matchbook 29.00
    comment: Saligo Bay is yet to win in his last five starts, with two pulled-up efforts in that spell, though a sixth last time out was a step back in the right direction. He has run over today's trip and going, but 155 lb off a mark of 115 looks a stiff task.
    DATA: model 8.9% | style Midfield (led 4% of runs) | runs in data 7 | last 3: 29 Aug Cartmel Hurdle 17.2f Good PU/11; 26 Sep Market Rasen Hurdle 16.6f Good PU/12; 18 Oct Sedgefield Hurdle 17f Good 6/9 fig 109
    DATA for: Trainer 21% wins (5/24), last 14 days
    DATA against: Best recent form figure 109, 6 lb below field average; Recent figures 6 lb below its current mark (looks high in the weights); Poor recent finishing positions; Pulled up in 2 of its last 5 jumps runs
- Mister Cessna (hrs_40605845) | 5yo G | 153lb | OR 113 | draw 0 | jockey Fern O'Brien(5) | trainer Fergal O'Brien (14d 3/26) | headgear p | last run 14 days | form 64-74V | MARKET 4.5% | 09:00 median 15.00 | Matchbook 28.00
    comment: The main risk is a winless run in recent starts, with a best finish of fourth, under 153 lb.
    DATA: model 7.4% | style Prominent (led 23% of runs) | runs in data 4 | last 3: 19 Apr Stratford Chase 17f Good 4/4; 13 May Perth Chase 16f Good To Soft 7/7; 16 Oct Uttoxeter Chase 16f Good 4/5 fig 98
    DATA for: Carries 6 lb less than average
    DATA against: Best recent form figure 98, 17 lb below field average; Recent figures 15 lb below its current mark (looks high in the weights); Official rating 113, 6 lb below field average; Last-run finishing speed -3.1% vs that field (faded); First run over hurdles in our data
- He's A Latchico (hrs_22598401) | 8yo G | 152lb | OR 112 | draw 0 | jockey Caoilin Quinn | trainer Jamie Moore & Josh Moore (14d 3/27) | headgear - | last run 18 days | form 2U3-58 | MARKET 4.3% | 09:00 median 19.00 | Matchbook 24.00
    comment: He has run over today's trip and going, and a third three starts back shows some ability, but 152 lb is a big ask.
    DATA: model 7.9% | style Held up (led 3% of runs) | runs in data 6 | last 3: 24 Apr Fontwell Hurdle 21.7f Good 3/6; 21 Oct Fontwell Hurdle 19f Soft 5/7; 6 Nov Fontwell Hurdle 19f Good 8/8
    DATA for: Carries 8 lb less than average
    DATA against: Official rating 112, 8 lb below field average; Last-run finishing speed -6.4% vs that field (faded); Fell or unseated in 1 of its last 5 jumps runs; Pace: steady gallop likely, hard to come from off the pace
