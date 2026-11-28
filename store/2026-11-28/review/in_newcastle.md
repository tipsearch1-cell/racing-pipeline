# Card review packet: Newcastle, 2026-11-28

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
{"meeting": "newcastle", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 11:40 Newcastle | race_id rac_32305880087 | Dane Architectural Systems Millionaire EBF 'National Hunt' Maiden Hurdle Race (Qualifier) (GBB Race)
Hurdle | Class 4 | 2m0f190y | going Good | Turf | 10 runners | rating band - | age 4-6yo
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Leader Allen (hrs_51491860) | 5yo G | 158lb | OR - | draw 0 | jockey Brian Hayes | trainer W. P. Mullins (14d 16/53) | headgear - | last run 119 days | form 2152/2 | MARKET 50.9% | 09:00 median 1.67 | Matchbook 1.82
    DATA: model 21.3% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 1 Aug Galway Hurdle 16.8f Good To Yielding 2/19
    DATA for: Trainer 30% wins (16/53), last 14 days; Last-run finishing speed +5.3% vs that field (finished strongly)
    DATA against: Returns from a 119-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Nikolavs Otto (hrs_17393777975) | 5yo G | 158lb | OR - | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 27/97) | headgear - | last run 44 days | form 2-5 | MARKET 30.4% | 09:00 median 2.75 | Matchbook 3.10
    DATA: model 15.1% | style Held up (led 8% of runs) | runs in data 1 | last 3: 15 Oct Perth Hurdle 16f Soft 5/9 fig 108
    DATA for: Trainer 28% wins (27/97), last 14 days
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Measure of A Man (hrs_17394321378) | 4yo G | 158lb | OR - | draw 0 | jockey Brian Hughes | trainer Ruth Jefferson (14d 1/4) | headgear - | last run 28 days | form P2-2 | MARKET 10.9% | 09:00 median 7.00 | Matchbook 9.40
    DATA: model 13.1% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 31 Oct Wetherby Hurdle 16f Good 2/6 fig 110
    DATA for: Best recent form figure 110, 6 lb above field average
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Cape Warrior (hrs_63000476) | 4yo G | 158lb | OR - | draw 0 | jockey Danny McMenamin | trainer Micky Hammond & Becky Smith (14d 1/18) | headgear - | last run 19 days | form 22-255 | MARKET 1.8% | 09:00 median 34.00 | Matchbook 85.00
    DATA: model 7.2% | style Midfield (led 4% of runs) | runs in data 5 | last 3: 16 Sep Kelso NH Flat 16.2f Good To Firm 2/5; 24 Oct Kelso Hurdle 16f Good 5/6 fig 92; 9 Nov Carlisle Hurdle 17f Good To Soft 5/14 fig 103
- Beluga Lagoon (hrs_17395001414) | 4yo G | 158lb | OR - | draw 0 | jockey Mr Thomas Easterby(7) | trainer Tim Easterby (14d 2/14) | headgear - | last run 22 days | form U15 | MARKET 1.3% | 09:00 median 41.00 | Matchbook 140.00
    DATA: model 10.8% | style Held up (led 8% of runs) | runs in data 1 | last 3: 6 Nov Hexham Hurdle 20f Good 5/9
    DATA against: Last-run finishing speed -2.2% vs that field (faded); Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Magical Major (hrs_17395163079) | 4yo G | 158lb | OR - | draw 0 | jockey Sean Quinlan | trainer Stuart Coltherd (14d 0/2) | headgear - | last run 19 days | form 2-8 | MARKET 1.3% | 09:00 median 41.00 | Matchbook 140.00
    DATA: model 5.9% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 9 Nov Carlisle Hurdle 17f Good To Soft 8/14
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Rhythm of The Rye (hrs_17394664525) | 5yo G | 158lb | OR - | draw 0 | jockey Jamie Hamilton | trainer Tim Easterby (14d 2/14) | headgear - | last run 23 days | form 2-6 | MARKET 1.2% | 09:00 median 41.00 | Matchbook 180.00
    DATA: model 5.9% | style Held up (led 8% of runs) | runs in data 1 | last 3: 5 Nov Newcastle Hurdle 20.5f Good 6/8
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Dilrisk (hrs_61911346) | 5yo G | 158lb | OR - | draw 0 | jockey Callum Bewley | trainer Nicky Richards (14d 1/9) | headgear - | last run 19 days | form 43-00 | MARKET 0.9% | 09:00 median 67.00 | Matchbook 160.00
    DATA: model 6.6% | style Midfield (led 3% of runs) | runs in data 4 | last 3: 20 Apr Kelso NH Flat 16.2f Good 3/6; 22 Oct Carlisle Hurdle 17f Good 12/13; 9 Nov Carlisle Hurdle 17f Good To Soft 14/14
- Wings of The Glen (hrs_17394666611) | 5yo G | 158lb | OR - | draw 0 | jockey Shane Fitzgerald | trainer Rebecca Menzies (14d 0/17) | headgear - | last run 10 days | form 37 | MARKET 0.9% | 09:00 median 67.00 | Matchbook 220.00
    DATA: model 10.6% | style Held up (led 5% of runs) | runs in data 2 | last 3: 30 Oct Wetherby Hurdle 19.5f Good 3/5 fig 97; 18 Nov Hexham Hurdle 16f Good To Soft 7/9
    DATA against: Best recent form figure 97, 8 lb below field average; Trainer 0 wins from 17 runs, last 14 days; Last-run finishing speed -2.1% vs that field (faded); Lightly raced: 2 runs in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- L'Appel du Large (hrs_59186162) | 5yo G | 158lb | OR - | draw 0 | jockey Bruce Lynn | trainer N. W. Alexander (14d 0/9) | headgear t | wind surgery | last run 198 days | form 90-P | MARKET 0.3% | 09:00 median 201.00 | Matchbook 520.00
    DATA: model 3.5% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 14 Mar Newcastle NH Flat 16.9f Good To Soft 12/12; 14 May Perth Hurdle 16.2f Good To Soft PU/13
    DATA against: Trainer 0 wins from 9 runs, last 14 days; Returns from a 198-day break; Lightly raced: 2 runs in our data, so the model has little to go on; Pulled up in 1 of its last 1 jumps runs

## 12:15 Newcastle | race_id rac_32305882024 | J&D Pierce Steeling The Race Handicap Steeple Chase (GBB Race)
Chase | Class 3 | 3m5f190y | going Good | Turf | 6 runners | rating band 0-130 | age 4yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Red Delta (hrs_34557782) | 7yo G | 159lb | OR 121 | draw 0 | jockey Brian Hughes | trainer Fiona Needham (14d 0/0) | headgear p | last run 41 days | form 1306-4 | MARKET 27.4% | 09:00 median 3.25 | Matchbook 3.60 | CHECK (skip line 3.09)
    comment: The risk is a 41-day layoff and 159 lb, which asks plenty of him after a sixth two starts back.
    DATA: model 10.9% | style Midfield (led 3% of runs) | runs in data 4 | last 3: 22 Mar Carlisle Chase 24.5f Good To Soft 11/12; 15 Apr Haydock Chase 28.4f Good 6/11; 18 Oct Sedgefield Chase 29f Good 4/7 fig 120
- Passengerontheship (hrs_35335776) | 7yo G | 154lb | OR 116 | draw 0 | jockey Harry Skelton | trainer Sam England (14d 6/27) | headgear tp | last run 27 days | form 722211 | MARKET 22.9% | 09:00 median 3.75 | Matchbook 4.50
    comment: Passengerontheship arrives in cracking nick, a winner last time out and again two starts back after three seconds, and he has run over today's trip and going.
    DATA: model 25.0% | style Prominent (led 8% of runs) | runs in data 15 | last 3: 10 Oct Hexham Chase 20.1f Good 2/4; 18 Oct Sedgefield Chase 29f Good 1/7 fig 107; 1 Nov Carlisle Chase 26f Good 1/8 fig 113
    DATA for: Trainer 22% wins (6/27), last 14 days; Good recent finishing positions
    DATA against: Best recent form figure 113, 8 lb below field average
- Impatient (hrs_29829373) | 8yo G | 160lb | OR 122 | draw 0 | jockey Jonjo O'Neill Jr. | trainer Jonjo & A.J. O'Neill (14d 4/33) | headgear t | last run 20 days | form 5124-1 | MARKET 17.9% | 09:00 median 5.00 | Matchbook 5.50
    comment: Impatient arrives in cracking nick, having won last time out and again four starts back, with a second three starts back in the mix, and he's fresh enough after 20 days and has run on today's going before. The main risk is the 160 lb he carries off an official mark of 122.
    DATA: model 18.4% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 1 Feb Market Rasen Chase 23.9f Soft 2/7; 24 Feb Catterick Chase 25.2f Good To Soft 4/6; 8 Nov Ffos Las Chase 24f Good 1/6 fig 119
    DATA for: Good recent finishing positions
- I Wish You (hrs_37987908) | 6yo G | 157lb | OR 119 | draw 0 | jockey Derek Fox | trainer Lucinda Russell & Michael Scudamore (14d 2/24) | headgear p | last run 44 days | form 4313-U | MARKET 17.7% | 09:00 median 5.00 | Matchbook 5.60
    comment: I Wish You unseated last time out and has been off for 44 days, which makes him hard to fancy, though a win three starts back and a third two starts back show he has ability.
    DATA: model 20.3% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 26 Feb Wetherby Chase 24.2f Soft 1/6; 18 Apr Ayr Chase 24.1f Heavy 3/11; 15 Oct Perth Chase 24f Soft UR/6
    DATA against: Fell or unseated in 1 of its last 3 jumps runs
- Ki Woo (hrs_39296628) | 6yo G | 169lb | OR 131 | draw 0 | jockey Lewis Saunders(5) | trainer Oliver Greenall & Josh Guerriero (14d 4/18) | headgear tp | last run 21 days | form 5-12P2 | MARKET 11.7% | 09:00 median 8.00 | Matchbook 8.20
    comment: Ki Woo bounces back from a pulled-up effort with a second last time out, and he has a second three starts back and a win four starts back.
    DATA: model 18.4% | style Prominent (led 3% of runs) | runs in data 7 | last 3: 28 Jun Uttoxeter Chase 24f Good 2/13; 18 Oct Sedgefield Chase 29f Good PU/7; 7 Nov Kelso Chase 23.5f Good 2/4 fig 131
    DATA for: Best recent form figure 131, 10 lb above field average; Official rating 131, 11 lb above field average; Trainer 22% wins (4/18), last 14 days
    DATA against: Carries 11 lb more than average; Pulled up in 1 of its last 5 jumps runs
- Pinot Rouge (hrs_29522815) | 8yo M | 150lb | OR 112 | draw 0 | jockey Kevin Healy(7) | trainer Jessica Bedi (14d 0/8) | headgear tp | last run 10 days | form 3-72P4 | MARKET 2.5% | 09:00 median 41.00 | Matchbook 42.00
    comment: Pinot Rouge is back quickly after 10 days, having finished fourth last time out and a second three starts back, and she has run on today's going before.
    DATA: model 6.9% | style Midfield (led 4% of runs) | runs in data 8 | last 3: 13 Jun Hexham Hurdle 23.3f Good 2/8; 2 Aug Galway Hurdle 24.3f Good PU/18; 18 Nov Hexham Chase 24f Good To Soft 4/4
    DATA for: Carries 8 lb less than average
    DATA against: Official rating 112, 8 lb below field average; Trainer 0 wins from 8 runs, last 14 days; Last-run finishing speed -2.6% vs that field (faded); Pulled up in 1 of its last 5 jumps runs

## 12:50 Newcastle | race_id rac_32305883961 | Weatherbys And Birdie Calendars 'The French Furze' Novices' Hurdle Race (GBB Race)
Hurdle | Class 2 | 2m6f0y | going Good | Turf | 6 runners | rating band - | age 4yo+
DATA pace: Lone leader - Elusive Dreams is the only habitual front-runner and may be allowed an easy lead.
- Old Coast Road (hrs_17393574590) | 5yo G | 159lb | OR - | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 27/97) | headgear - | last run 21 days | form 1-21 | MARKET 37.4% | 09:00 median 2.38 | Matchbook 2.60
    DATA: model 17.2% | style Held up (led 8% of runs) | runs in data 2 | last 3: 11 Oct Chepstow NH Flat 16.1f Good To Soft 2/6; 7 Nov Aintree Hurdle 20f Good To Soft 1/2 fig 112
    DATA for: Trainer 28% wins (27/97), last 14 days; Good recent finishing positions
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Splendid Fellow (hrs_51831577) | 5yo G | 162lb | OR 126 | draw 0 | jockey Brian Hayes | trainer Henry de Bromhead (14d 6/36) | headgear t | last run 23 days | form 26-213 | MARKET 33.8% | 09:00 median 2.75 | Matchbook 2.78
    DATA: model 43.6% | style Prominent (led 3% of runs) | runs in data 4 | last 3: 11 May Killarney Hurdle 20.2f Good To Yielding 2/12; 3 Sep Kilbeggan Hurdle 19f Good To Yielding 1/8; 5 Nov Newbury Hurdle 24.5f Good To Soft 3/16 fig 125
    DATA for: Best recent form figure 125, 11 lb above field average; Good recent finishing positions
- Elusive Dreams (hrs_17395002457) | 6yo G | 159lb | OR - | draw 0 | jockey Danny McMenamin | trainer Ann Hamilton (14d 0/2) | headgear - | last run 22 days | form 1-1 | MARKET 13.6% | 09:00 median 7.00 | Matchbook 7.00
    DATA: model 20.9% | style Leader (led 57% of runs) | runs in data 1 | last 3: 6 Nov Hexham Hurdle 20f Good 1/9 fig 112
    DATA for: Last-run finishing speed +6.4% vs that field (finished strongly); Pace: may get an uncontested lead
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Lauvergnat (hrs_17393557902) | 5yo G | 154lb | OR - | draw 0 | jockey Derek Fox | trainer Lucinda Russell & Michael Scudamore (14d 2/24) | headgear - | last run 27 days | form P1-2 | MARKET 9.3% | 09:00 median 9.00 | Matchbook 11.00
    DATA: model 6.4% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 1 Nov Carlisle Hurdle 20f Good To Soft 2/8 fig 109
    DATA against: Best recent form figure 109, 5 lb below field average; Lightly raced: 1 run in our data, so the model has little to go on
- Dream On Mick (hrs_58565388) | 5yo G | 159lb | OR - | draw 0 | jockey Joe Williamson | trainer Philip Kirby (14d 2/15) | headgear - | last run 213 days | form P11P- | MARKET 3.3% | 09:00 median 26.00 | Matchbook 34.00
    DATA: model 4.8% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 4 Apr Carlisle Hurdle 19.3f Good 1/10; 29 Apr Punchestown Hurdle 23.9f Yielding PU/14
    DATA against: Returns from a 213-day break; Lightly raced: 2 runs in our data, so the model has little to go on; Pulled up in 1 of its last 2 jumps runs
- Bay Runner (hrs_52495443) | 5yo G | 154lb | OR - | draw 0 | jockey Sean Quinlan | trainer Lizzie Quinlan (14d 1/10) | headgear - | last run 28 days | form 32-3 | MARKET 2.6% | 09:00 median 29.00 | Matchbook 46.00
    DATA: model 7.0% | style Held up (led 5% of runs) | runs in data 2 | last 3: 14 Mar Newcastle NH Flat 16.9f Good To Soft 2/12; 31 Oct Ayr Hurdle 16f Good To Soft 3/8 fig 113
    DATA for: Good recent finishing positions
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on

## 1:25 Newcastle | race_id rac_32304615226 | SES Engineering Powering Past The Rehearsal Handicap Steeple Chase (Premier Handicap) (GBB Race)
Chase | Class 1 | 3m0f0y | going Good | Turf | 10 runners | rating band - | age 4yo+
DATA pace: Lone leader - Intense Approach is the only habitual front-runner and may be allowed an easy lead.
- Crest of Fortune (hrs_37096024) | 6yo G | 151lb | OR 135 | draw 0 | jockey Brian Hughes | trainer Anthony Honeyball (14d 1/14) | headgear tp (1st time) | last run 27 days | form 4635-2 | MARKET 18.8% | 09:00 median 4.50 | Matchbook 5.30 | CHECK (skip line 4.27)
    comment: Second last time out and 27 days fresh, Crest of Fortune has run over today's trip and going before, but he is winless in his last five starts and has yet to better that runner-up finish.
    DATA: model 6.9% | style Midfield (led 5% of runs) | runs in data 3 | last 3: 14 Feb Ascot Chase 23.8f Good To Soft 3/3; 10 Apr Aintree Chase 25f Good To Soft 5/8; 1 Nov Worcester Chase 23f Good To Soft 2/7 fig 127
    DATA for: Last-run finishing speed +4.5% vs that field (finished strongly); Good recent finishing positions; First-time headgear
    DATA against: Best recent form figure 127, 7 lb below field average; Recent figures 8 lb below its current mark (looks high in the weights); Race comments mention jumping mistakes in 3 of its last 3 runs
- Jordans Cross (hrs_40494090) | 6yo G | 156lb | OR 140 | draw 0 | jockey Rex Dingle | trainer Anthony Honeyball (14d 1/14) | headgear t | wind surgery | last run 232 days | form F118B- | MARKET 14.9% | 09:00 median 6.00 | Matchbook 6.60
    comment: Jordans Cross won two of his last five, taking a win three starts back and another four starts back, but he was brought down last time out and has been off 232 days.
    DATA: model 11.7% | style Midfield (led 29% of runs) | runs in data 3 | last 3: 24 Jan Cheltenham Chase 20.6f Soft 1/9; 12 Mar Cheltenham Chase 20.6f Good 8/18; 10 Apr Aintree Chase 25f Good To Soft BD/8
    DATA against: Returns from a 232-day break; Fell or unseated in 1 of its last 3 jumps runs
- Il Est Francais (hrs_27821493) | 8yo G | 168lb | OR 152 | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 27/97) | headgear - | last run 45 days | form 3PPP-5 | MARKET 14.8% | 09:00 median 6.00 | Matchbook 6.40
    comment: Fifth last time out after three pulled-up efforts, Il Est Francais has run over today's trip and going and drops back in after 45 days off, with a yard firing at 28% over the last fortnight.
    DATA: model 12.4% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 10 Apr Aintree Chase 21.1f Good To Soft PU/27; 14 Oct Ffos Las Chase 19.5f Soft 5/8 fig 145
    DATA for: Best recent form figure 145, 11 lb above field average; Official rating 152, 15 lb above field average; Trainer 28% wins (27/97), last 14 days
    DATA against: Recent figures 7 lb below its current mark (looks high in the weights); Carries 14 lb more than average; Lightly raced: 2 runs in our data, so the model has little to go on; Pulled up in 1 of its last 2 jumps runs
- Laurens Bay (hrs_34073396) | 7yo G | 151lb | OR 135 | draw 0 | jockey Conor O'Farrell | trainer Jamie Snowden (14d 4/15) | headgear - | last run 314 days | form 1/133- | MARKET 10.6% | 09:00 median 8.50 | Matchbook 9.00
    comment: Laurens Bay arrives with two wins in his last four starts, a third last time out and another third two starts back, and he has run over today's trip and going before.
    DATA: model 7.6% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 18 Jan Windsor Chase 24.3f Soft 3/6
    DATA for: Trainer 27% wins (4/15), last 14 days
    DATA against: Returns from a 314-day break; Lightly raced: 1 run in our data, so the model has little to go on
- First Confession (hrs_38203130) | 7yo G | 155lb | OR 139 | draw 0 | jockey Dylan Johnston | trainer Joe Tizzard (14d 8/31) | headgear - | last run 17 days | form 5F10-1 | MARKET 10.3% | 09:00 median 8.00 | Matchbook 9.80
    DATA: model 9.7% | style Prominent (led 23% of runs) | runs in data 4 | last 3: 3 Feb Carlisle Chase 20.9f Good To Soft 1/4; 10 Mar Cheltenham Chase 29.9f Good To Soft 10/17; 11 Nov Bangor-on-Dee Chase 24f Good 1/5 fig 131
    DATA for: Trainer 26% wins (8/31), last 14 days; Last-run finishing speed +2.3% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Recent figures 8 lb below its current mark (looks high in the weights); Race comments mention jumping mistakes in 2 of its last 4 runs; Fell or unseated in 1 of its last 4 jumps runs
- Apple Away (hrs_29117074) | 9yo M | 152lb | OR 136 | draw 0 | jockey Derek Fox | trainer Lucinda Russell & Michael Scudamore (14d 2/24) | headgear - | last run 27 days | form /31-62 | MARKET 9.0% | 09:00 median 9.00 | Matchbook 11.50
    comment: Apple Away was second last time out and a winner three starts back, and she has run over today's trip and going before, returning fresh after 27 days.
    DATA: model 12.0% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 22 Apr Perth Chase 23.8f Good 1/4; 1 Nov Carlisle Chase 20f Good 2/4 fig 134
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- King Turgeon (hrs_27206879) | 8yo G | 152lb | OR 136 | draw 0 | jockey Rian Corcoran(5) | trainer David Pipe (14d 3/17) | headgear tp | wind surgery | last run 22 days | form /66F-2 | MARKET 7.2% | 09:00 median 12.75 | Matchbook 13.50
    comment: King Turgeon was second last time out and returns after 22 days, though he is yet to win in his last four starts, with a fall and two sixths before that.
    DATA: model 8.8% | style Prominent (led 8% of runs) | runs in data 2 | last 3: 21 Mar Newbury Chase 23.4f Good To Soft F/7; 6 Nov Aintree Chase 25f Good To Soft 2/12 fig 133
    DATA for: Last-run finishing speed +2.4% vs that field (finished strongly)
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Fell or unseated in 1 of its last 2 jumps runs
- Alcedo (hrs_32936512) | 8yo G | 142lb | OR 125 | draw 0 | jockey Murray Dodd(5) | trainer Venetia Williams (14d 0/11) | headgear p | last run 259 days | form 9122P- | MARKET 5.9% | 09:00 median 15.00 | Matchbook 16.50
    comment: Alcedo is hard to fancy after being pulled up last time out and returning from 259 days off, with a long absence to overcome.
    DATA: model 8.0% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 20 Feb Warwick Chase 20f Soft 2/5; 14 Mar Uttoxeter Chase 34f Soft PU/16
    DATA for: Carries 12 lb less than average
    DATA against: Official rating 125, 12 lb below field average; Trainer 0 wins from 11 runs, last 14 days; Returns from a 259-day break; Lightly raced: 2 runs in our data, so the model has little to go on; Pulled up in 1 of its last 2 jumps runs
- Konfusion (hrs_30709889) | 8yo G | 160lb | OR 144 | draw 0 | jockey Callum Bewley | trainer Joel Parkinson & Sue Smith (14d 0/14) | headgear - | last run 7 days | form 3F3-5P | MARKET 5.0% | 09:00 median 17.00 | Matchbook 20.00
    comment: Quick back-out after a pulled up last time, but Konfusion has run over today's trip and going, and was third five starts back and again three starts back, with a fifth two starts back. Carrying 160 lb off 144 is a stiff task, and that's the main risk.
    DATA: model 11.7% | style Prominent (led 3% of runs) | runs in data 5 | last 3: 11 Apr Aintree Chase 25f Good To Soft 3/13; 6 Nov Aintree Chase 25f Good To Soft 5/12 fig 143; 21 Nov Haydock Chase 25.5f Good PU/7
    DATA for: Best recent form figure 143, 9 lb above field average; Official rating 144, 7 lb above field average
    DATA against: Trainer 0 wins from 14 runs, last 14 days; Carries 6 lb more than average; Race comments mention jumping mistakes in 4 of its last 5 runs; Fell or unseated in 1 of its last 5 jumps runs; Pulled up in 1 of its last 5 jumps runs
- Intense Approach (hrs_34373780) | 7yo G | 148lb | OR 132 | draw 0 | jockey Conor Smithers(5) | trainer John McConnell (14d 0/18) | headgear p | last run 28 days | form -06P21 | MARKET 3.4% | 09:00 median 23.00 | Matchbook 32.00
    comment: Intense Approach arrives a last-time-out winner and a second two starts back, but he pulled up three runs ago and was sixth and unplaced before that, so consistency is a worry.
    DATA: model 11.3% | style Leader (led 43% of runs) | runs in data 9 | last 3: 16 Aug Tramore Chase 22f Good To Yielding PU/10; 13 Oct Punchestown Hurdle 23.4f Good 2/5; 31 Oct Down Royal (IRE) Chase 24f Good 1/12 fig 123
    DATA for: Has won at this trip or further; Carries 6 lb less than average; Pace: may get an uncontested lead
    DATA against: Best recent form figure 123, 11 lb below field average; Recent figures 9 lb below its current mark (looks high in the weights); Official rating 132, 5 lb below field average; Trainer 0 wins from 18 runs, last 14 days; Race comments mention jumping mistakes in 3 of its last 5 runs; Pulled up in 1 of its last 5 jumps runs

## 2:00 Newcastle | race_id rac_32304617163 | Bowmer And Kirkland We Build As One Fighting Fifth Hurdle Race (Grade 1) (GBB Race)
Hurdle | Class 1 | 2m0f190y | going Good | Turf | 5 runners | rating band - | age 4yo+
DATA pace: Lone leader - Indemnity is the only habitual front-runner and may be allowed an easy lead.
- Mydaddypaddy (hrs_50401701) | 5yo G | 164lb | OR 153 | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 27/97) | headgear - | last run 263 days | form /1123- | MARKET 41.5% | 09:00 median 2.25 | Matchbook 2.36
    comment: Mydaddypaddy arrives with a strong recent profile, third last time out, a second two starts back, and a winner three starts back and four starts back, and he has run over today's trip, with a yard in form. The main risk is a 263-day absence, carrying 164 lb off an official mark of 153.
    DATA: model 23.7% | style Unknown | runs in data 1 | last 3: 10 Mar Cheltenham Hurdle 16.4f Good To Soft 3/11
    DATA for: Trainer 28% wins (27/97), last 14 days; Last-run finishing speed +2.3% vs that field (finished strongly)
    DATA against: Returns from a 263-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Alexei (hrs_39208155) | 6yo G | 164lb | OR 158 | draw 0 | jockey Jonjo O'Neill Jr. | trainer Joe Tizzard (14d 8/31) | headgear t | last run 21 days | form 3143-1 | MARKET 38.6% | 09:00 median 2.38 | Matchbook 2.60
    comment: Alexei heads the field on form, having won last time out and again four starts back, with a third and a fourth in between, and he's fresh enough after 21 days off. He has run over today's trip and going, and the in-form yard adds support, though 164 lb is a hefty burden.
    DATA: model 25.8% | style Midfield (led 3% of runs) | runs in data 4 | last 3: 10 Mar Cheltenham Hurdle 16.4f Good To Soft 4/9; 9 Apr Aintree Hurdle 20f Good To Soft 3/6; 7 Nov Aintree Hurdle 17f Good To Soft 1/4 fig 157
    DATA for: Best recent form figure 157, 11 lb above field average; Official rating 158, 9 lb above field average; Trainer 26% wins (8/31), last 14 days; Has won at this trip or further; Good recent finishing positions
- Golden Ace (hrs_32996432) | 8yo M | 157lb | OR 150 | draw 0 | jockey Lorcan Williams | trainer Jeremy Scott (14d 0/8) | headgear p | last run 37 days | form 2542-3 | MARKET 14.3% | 09:00 median 6.70 | Matchbook 7.00
    comment: Golden Ace is a consistent sort, third last time out and a second two starts back, and she has run over today's trip and on the going before.
    DATA: model 16.8% | style Prominent (led 23% of runs) | runs in data 4 | last 3: 9 Apr Aintree Hurdle 20f Good To Soft 4/6; 1 May Punchestown Hurdle 16.2f Yielding 2/7; 22 Oct Carlisle Hurdle 17f Good 3/8 fig 138
    DATA for: Good recent finishing positions
    DATA against: Best recent form figure 138, 8 lb below field average; Trainer 0 wins from 8 runs, last 14 days
- Minella Study (hrs_45007368) | 4yo G | 164lb | OR 143 | draw 0 | jockey Ryan Mania | trainer Adam Nicol (14d 1/6) | headgear - | last run 233 days | form 11138- | MARKET 3.7% | 09:00 median 23.00 | Matchbook 29.00
    comment: Eighth last time out and absent for 233 days, Minella Study is hard to fancy after such a long layoff, and carrying 164 lb doesn't help. In his favour, he won three starts in a row before a third prior to that, and has run over today's trip and going.
    DATA: model 21.4% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 13 Mar Cheltenham Hurdle 16.8f Good To Soft 3/20; 9 Apr Aintree Hurdle 16.9f Good To Soft 8/10
    DATA against: Official rating 143, 6 lb below field average; Last-run finishing speed -6.9% vs that field (faded); Returns from a 233-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- Indemnity (hrs_28014434) | 6yo G | 164lb | OR 139 | draw 0 | jockey Brian Hughes | trainer Emma Lavelle (14d 2/19) | headgear - | last run 28 days | form 1-0262 | MARKET 1.9% | 09:00 median 51.00 | Matchbook 55.00
    comment: The main risk is the 164 lb he carries, which leaves little margin off an official mark of 139.
    DATA: model 12.3% | style Leader (led 38% of runs) | runs in data 6 | last 3: 26 Sep Market Rasen Hurdle 16.6f Good 6/12; 21 Oct Kempton (AW) Flat 16f Standard / Slow 13/14 fig 60; 31 Oct Ascot Hurdle 15.5f Good To Firm 2/16 fig 142
    DATA for: Pace: may get an uncontested lead
    DATA against: Official rating 139, 10 lb below field average; Race comments mention jumping mistakes in 2 of its last 5 runs

## 2:35 Newcastle | race_id rac_32305885898 | Ryder & Cundall Designed To Go The Distance Handicap Hurdle Race
Hurdle | Class 3 | 2m4f62y | going Good | Turf | 10 runners | rating band 0-130 | age 3yo+
DATA pace: Lone leader - Kool Raoul is the only habitual front-runner and may be allowed an easy lead.
- Brace For Landing (hrs_50622628) | 5yo G | 159lb | OR 119 | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 27/97) | headgear - | wind surgery | last run 23 days | form 3550-1 | MARKET 22.8% | 09:00 median 3.75 | Matchbook 4.20 | CHECK (skip line 3.56)
    comment: Won last time out after a fifth and an unplaced run before that, and he returns fresh enough after 23 days, having run over today's trip and going before.
    DATA: model 12.9% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 3 Jan Sandown Hurdle 16f Good 5/8; 7 Mar Sandown Hurdle 16f Soft 10/18; 5 Nov Newcastle Hurdle 20.5f Good 1/8 fig 113
    DATA for: Trainer 28% wins (27/97), last 14 days; Has won at this trip or further
    DATA against: Recent figures 6 lb below its current mark (looks high in the weights)
- Cave Bridge (hrs_51831640) | 6yo G | 157lb | OR 117 | draw 0 | jockey Ryan Mania | trainer Harry Derham (14d 1/16) | headgear - | last run 23 days | form /111-6 | MARKET 19.6% | 09:00 median 4.50 | Matchbook 4.80
    DATA: model 9.1% | style Held up (led 8% of runs) | runs in data 1 | last 3: 5 Nov Newbury Hurdle 16.5f Good To Soft 6/16 fig 118
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Las Canals (hrs_47065039) | 5yo G | 159lb | OR 119 | draw 0 | jockey Jonjo O'Neill Jr. | trainer Oliver Greenall & Josh Guerriero (14d 4/18) | headgear - | last run 29 days | form /911-1 | MARKET 17.4% | 09:00 median 5.00 | Matchbook 5.40
    comment: Las Canals arrives bidding for a four-timer after winning last time out, two starts back and three starts back, and has run over today's trip and going before.
    DATA: model 15.2% | style Held up (led 4% of runs) | runs in data 3 | last 3: 10 Mar Sedgefield Hurdle 16.8f Good 1/7; 18 Apr Bangor-on-Dee Hurdle 19.6f Good 1/9; 30 Oct Uttoxeter Hurdle 20f Good 1/15 fig 118
    DATA for: Trainer 22% wins (4/18), last 14 days; Last-run finishing speed +6.1% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
- The Kalooki Kid (hrs_32568396) | 8yo G | 166lb | OR 126 | draw 0 | jockey Danny McMenamin | trainer Nicky Richards (14d 1/9) | headgear - | wind surgery | last run 14 days | form 456P-2 | MARKET 10.4% | 09:00 median 8.00 | Matchbook 9.40
    comment: He is yet to win in his last five, and carries 166 lb, but the recent run was a step forward after being pulled up.
    DATA: model 9.1% | style Prominent (led 23% of runs) | runs in data 4 | last 3: 31 Jan Musselburgh Chase 20.3f Good To Soft 6/8; 30 Mar Ludlow Chase 23.8f Good PU/6; 14 Nov Wetherby Hurdle 21.5f Good 2/6 fig 126
    DATA for: Best recent form figure 126, 10 lb above field average; Official rating 126, 6 lb above field average; Last-run finishing speed +4.3% vs that field (finished strongly)
    DATA against: Carries 6 lb more than average; Pulled up in 1 of its last 4 jumps runs
- Tiddesley Wood (hrs_37096108) | 6yo G | 168lb | OR 128 | draw 0 | jockey Brian Hughes | trainer Adrian Keatley (14d 1/7) | headgear t | last run 49 days | form 1341-4 | MARKET 8.8% | 09:00 median 9.00 | Matchbook 12.00
    comment: Tiddesley Wood has won two of his last five, including two starts back, and was a fourth last time out, though he returns after 49 days off.
    DATA: model 10.7% | style Held up (led 5% of runs) | runs in data 3 | last 3: 5 Feb Huntingdon Hurdle 19.6f Soft 4/6; 14 Mar Kempton Hurdle 21f Good 1/5; 10 Oct Hexham Chase 20.1f Good 4/4
    DATA for: Official rating 128, 8 lb above field average; Has won at this trip or further
    DATA against: Last-run finishing speed -6.7% vs that field (faded); Carries 8 lb more than average; Race comments mention jumping mistakes in 2 of its last 3 runs
- Kool Raoul (hrs_46850825) | 6yo G | 153lb | OR 113 | draw 0 | jockey Derek Fox | trainer Lucinda Russell & Michael Scudamore (14d 2/24) | headgear - | last run 22 days | form 785-11 | MARKET 6.7% | 09:00 median 12.00 | Matchbook 15.50
    comment: Fit enough after 22 days, he has run over today's trip and going.
    DATA: model 16.1% | style Prominent (led 54% of runs) | runs in data 6 | last 3: 13 Apr Hexham Hurdle 20.1f Good 5/9; 20 Oct Hexham Hurdle 20f Good 1/9 fig 105; 6 Nov Hexham Hurdle 20f Good 1/9 fig 108
    DATA for: Has won at this trip or further; Good recent finishing positions; Carries 7 lb less than average
    DATA against: Best recent form figure 108, 8 lb below field average; Official rating 113, 7 lb below field average
- Captain Butler (hrs_32780083) | 8yo G | 159lb | OR 119 | draw 0 | jockey Jamie Hamilton | trainer Ruth Jefferson (14d 1/4) | headgear - | last run 225 days | form 6454P- | MARKET 5.2% | 09:00 median 17.00 | Matchbook 18.00
    comment: The concern is a 225-day absence after he was pulled up last time, under 159 lb.
    DATA: model 10.4% | style Midfield (led 8% of runs) | runs in data 4 | last 3: 17 Jan Haydock Hurdle 15.7f Good To Soft 5/8; 21 Mar Kelso Hurdle 20.9f Good To Soft 4/14; 17 Apr Ayr Hurdle 21.4f Soft PU/11
    DATA against: Returns from a 225-day break; Pulled up in 1 of its last 4 jumps runs
- Tashkhan (hrs_23048564) | 8yo G | 166lb | OR 126 | draw 0 | jockey Sean Quinlan | trainer Brian Ellison (14d 1/9) | headgear - | last run 21 days | form 13534- | MARKET 4.6% | 09:00 median 17.00 | Matchbook 23.00
    comment: The main risk is the hefty 166 lb, with his last win five starts back.
    DATA: model 8.0% | style Held up (led 4% of runs) | runs in data 8 | last 3: 10 Oct Newmarket Flat 18f Good 11/29; 19 Oct Pontefract Flat 18f Heavy 4/9 fig 91; 7 Nov Doncaster Flat 12f Good To Soft 16/23 fig 73
    DATA for: Official rating 126, 6 lb above field average
    DATA against: Carries 6 lb more than average
- Dream's Ka (hrs_59551338) | 4yo G | 156lb | OR 117 | draw 0 | jockey Conor O'Farrell | trainer Katie Scott (14d 0/6) | headgear t | last run 21 days | form 121814 | MARKET 3.1% | 09:00 median 23.00 | Matchbook 40.00
    comment: Dream's Ka has won three of his last six, including a win two starts back, and has run over today's trip and going, but he was only fourth last time out, and he carries 156 lb off an official mark of 117.
    DATA: model 6.2% | style Prominent (led 3% of runs) | runs in data 11 | last 3: 24 Jul Uttoxeter Hurdle 19.9f Good 8/10; 16 Sep Kelso Hurdle 20.9f Good To Firm 1/5; 7 Nov Kelso Hurdle 21f Good 4/11 fig 115
    DATA for: Has won at this trip or further
- Cannock Park (hrs_34456870) | 8yo G | 160lb | OR 120 | draw 0 | jockey Callum Bewley | trainer Ewan Whillans (14d 1/8) | headgear h | last run 168 days | form 45/0-R | MARKET 1.3% | 09:00 median 67.00 | Matchbook 100.00
    comment: The big risk is obvious: he refused last time out and returns after 168 days off.
    DATA: model 2.3% | style Unknown | runs in data 1 | last 3: 13 Jun Hexham Hurdle 20.1f Good RR/8
    DATA against: Returns from a 168-day break; Lightly raced: 1 run in our data, so the model has little to go on

## 3:18 Newcastle | race_id rac_32305887835 | Jodie Standing's Point-To-Point Recruits Handicap Steeple Chase (Go North Monet's Garden Series Qualifier) (GBB Race)
Chase | Class 4 | 2m4f19y | going Good | Turf | 9 runners | rating band 0-120 | age 4yo+
DATA pace: Even - Two likely leaders (Authorized Mission, Looking Splendid). A fair, even gallop is most likely.
- Albie Littlewood (hrs_37520980) | 7yo G | 168lb | OR 120 | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 27/97) | headgear - | last run 38 days | form 6511-1 | MARKET 40.7% | 09:00 median 2.15 | Matchbook 2.30
    comment: Winner last time out, and a winner two and three starts back too, so Albie Littlewood arrives in cracking form and has run over today's trip, with the yard in good nick.
    DATA: model 23.2% | style Held up (led 5% of runs) | runs in data 2 | last 3: 22 Jan Huntingdon Hurdle 20.7f Soft 1/15; 21 Oct Worcester Chase 16.5f Good To Soft 1/9 fig 112
    DATA for: Best recent form figure 112, 8 lb above field average; Official rating 120, 9 lb above field average; Trainer 28% wins (27/97), last 14 days; Last-run finishing speed +4.9% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Recent figures 8 lb below its current mark (looks high in the weights); Carries 9 lb more than average; Lightly raced: 2 runs in our data, so the model has little to go on
- Authorized Mission (hrs_38648869) | 6yo G | 163lb | OR 115 | draw 0 | jockey Danny McMenamin | trainer Nicky Richards (14d 1/9) | headgear - | last run 253 days | form /1295- | MARKET 18.2% | 09:00 median 4.50 | Matchbook 5.40
    comment: The main risk is a 253-day absence, with a fifth last time out and a ninth before that.
    DATA: model 11.8% | style Leader (led 38% of runs) | runs in data 2 | last 3: 2 Jan Ayr Hurdle 24.3f Soft 9/10; 20 Mar Musselburgh Hurdle 23.8f Good To Soft 5/13
    DATA for: Last-run finishing speed +8.0% vs that field (finished strongly)
    DATA against: Returns from a 253-day break; Lightly raced: 2 runs in our data, so the model has little to go on; First run over fences in our data
- Looking Splendid (hrs_32911074) | 8yo G | 163lb | OR 115 | draw 0 | jockey Dylan Johnston | trainer Gary Rutherford (14d 0/2) | headgear - | last run 23 days | form 612-31 | MARKET 10.5% | 09:00 median 7.50 | Matchbook 10.00
    comment: Looking Splendid arrives in cracking form, a winner last time out, with a third two starts back and a second three starts back, and he has run over today's trip and going.
    DATA: model 14.9% | style Leader (led 54% of runs) | runs in data 4 | last 3: 20 Apr Kelso Chase 21.6f Good 2/8; 24 May Kelso Chase 21.6f Good 3/5; 5 Nov Newcastle Chase 20f Good 1/5 fig 108
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Recent figures 7 lb below its current mark (looks high in the weights)
- Diamond Mix (hrs_37633190) | 7yo G | 154lb | OR 106 | draw 0 | jockey Callum Bewley | trainer Ewan Whillans (14d 1/8) | headgear - | last run 22 days | form /13-22 | MARKET 7.2% | 09:00 median 12.50 | Matchbook 13.50
    comment: Diamond Mix has been running well, second last time out and a second two starts back, after a third and a win before that, and he has run over today's trip and going.
    DATA: model 10.0% | style Midfield (led 29% of runs) | runs in data 3 | last 3: 14 Mar Newcastle Chase 16.3f Good To Soft 3/6; 19 May Hexham Chase 15.6f Good 2/5; 6 Nov Hexham Chase 15.5f Good 2/7 fig 106
    DATA for: Good recent finishing positions
- Treaty Boy (hrs_32780251) | 9yo G | 148lb | OR 100 | draw 0 | jockey Sean Quinlan | trainer Stuart Coltherd (14d 0/2) | headgear t | last run 23 days | form 4-41F1 | MARKET 6.6% | 09:00 median 10.00 | Matchbook 19.00
    comment: Carrying 148 lb off an official mark of 100 makes him hard to fancy.
    DATA: model 12.3% | style Midfield (led 4% of runs) | runs in data 7 | last 3: 24 Oct Kelso Chase 17f Good 1/5 fig 86; 3 Nov Sedgefield Chase 16.5f Good F/8; 5 Nov Newcastle Chase 20f Good 1/9 fig 96
    DATA for: Has won at this trip or further; Carries 11 lb less than average
    DATA against: Best recent form figure 96, 8 lb below field average; Official rating 100, 11 lb below field average; Fell or unseated in 1 of its last 5 jumps runs
- Ballyfort (hrs_30122904) | 8yo G | 152lb | OR 104 | draw 0 | jockey Bruce Lynn | trainer N. W. Alexander (14d 0/9) | headgear ht | last run 35 days | form 1622-2 | MARKET 4.9% | 09:00 median 17.00 | Matchbook 20.00
    comment: Ballyfort has finished second in each of his last three starts, which is solid, but he hasn't won since a victory five starts back, and he returns after 35 days carrying 152 lb.
    DATA: model 8.1% | style Held up (led 4% of runs) | runs in data 5 | last 3: 7 Mar Ayr Chase 16.5f Soft 2/5; 17 Apr Ayr Chase 16.5f Soft 2/9; 24 Oct Kelso Chase 17f Good 2/5 fig 96
    DATA for: Last-run finishing speed +3.6% vs that field (finished strongly); Good recent finishing positions; Carries 7 lb less than average
    DATA against: Best recent form figure 96, 8 lb below field average; Recent figures 8 lb below its current mark (looks high in the weights); Official rating 104, 7 lb below field average; Trainer 0 wins from 9 runs, last 14 days
- Glory And Honour (hrs_21212086) | 10yo G | 158lb | OR 110 | draw 0 | jockey Jamie Hamilton | trainer Sam England (14d 6/27) | headgear tb | last run 15 days | form 723632 | MARKET 4.6% | 09:00 median 19.00 | Matchbook 21.00
    comment: Glory And Honour arrives in sound form, second last time out and third two starts back, with only 15 days since that run, and he has run over today's trip and on this going before. He is yet to win in his last six, though, and 158 lb is a hefty burden to carry.
    DATA: model 7.8% | style Prominent (led 29% of runs) | runs in data 10 | last 3: 2 Oct Hexham Hurdle 20.1f Good 6/6; 22 Oct Carlisle Chase 20f Good 3/4 fig 109; 13 Nov Sedgefield Chase 21f Good 2/3 fig 108
    DATA for: Best recent form figure 109, 4 lb above field average; Trainer 22% wins (6/27), last 14 days; Good recent finishing positions
- Genois (hrs_22906905) | 10yo G | 170lb | OR 122 | draw 0 | jockey Jonjo O'Neill Jr. | trainer Jonjo & A.J. O'Neill (14d 4/33) | headgear p | last run 29 days | form 2-P4UP | MARKET 3.8% | 09:00 median 21.00 | Matchbook 27.00
    comment: A second five starts back is his best finish, so the pulled up last time out is the one reservation, though 29 days' rest should help.
    DATA: model 6.6% | style Held up (led 4% of runs) | runs in data 7 | last 3: 19 Jun Market Rasen Chase 21.4f Good 4/6; 14 Oct Wetherby Chase 19.5f Good To Firm UR/4; 30 Oct Wetherby Chase 19.5f Good PU/6
    DATA for: Official rating 122, 11 lb above field average
    DATA against: Carries 11 lb more than average; Fell or unseated in 1 of its last 5 jumps runs; Pulled up in 2 of its last 5 jumps runs
- Heads Or Harps (hrs_27888840) | 9yo G | 154lb | OR 106 | draw 0 | jockey Derek Fox | trainer Lucinda Russell & Michael Scudamore (14d 2/24) | headgear - | last run 44 days | form 2322-7 | MARKET 3.4% | 09:00 median 23.00 | Matchbook 32.00
    comment: Heads Or Harps was placed in four of his last five, finishing second three times and third once before a seventh last time out, and he has run over today's trip and going.
    DATA: model 5.4% | style Held up (led 4% of runs) | runs in data 3 | last 3: 10 Feb Ayr Chase 20.5f Soft 2/4; 6 Mar Ayr Chase 20.5f Soft 2/3; 15 Oct Perth Chase 20f Soft 7/8
    DATA for: Good recent finishing positions
