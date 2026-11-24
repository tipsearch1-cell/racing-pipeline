# Card review packet: Tramore, 2026-11-24

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
{"meeting": "tramore", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 12:45 Tramore | race_id rac_32305463632 | 2027 Annual Badge At Tramore Racecourse Maiden Hurdle
Hurdle |  | 2m0f50y | going Soft | Turf | 18 runners | rating band - | age 4yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Forty Fifty (hrs_57470973) | 4yo G | 166lb | OR - | draw 0 | jockey Paul Townend | trainer W. P. Mullins (14d 8/45) | headgear - | last run 256 days | form 46- | MARKET 47.2% | 09:00 median 1.40 | Matchbook 1.65
    DATA: model 5.3% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 13 Mar Cheltenham Hurdle 16.8f Good To Soft 6/20
    DATA for: Last-run finishing speed +3.4% vs that field (finished strongly)
    DATA against: Returns from a 256-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Global Submission (hrs_40786466) | 6yo G | 166lb | OR - | draw 0 | jockey  | trainer Henry de Bromhead (14d 9/42) | headgear - | last run 37 days | form 32/2 | MARKET 15.7% | 09:00 median 3.75 | Matchbook 5.60
    DATA: model 21.2% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 18 Oct Limerick (IRE) Hurdle 16.5f Good To Yielding 2/11 fig 112
    DATA for: Best recent form figure 112, 15 lb above field average; Trainer 21% wins (9/42), last 14 days
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Blue Rebel (hrs_17395851459) | 4yo G | 166lb | OR - | draw 0 | jockey  | trainer Gordon Elliott (14d 12/80) | headgear - | last run 269 days | form 1- | MARKET 14.6% | 09:00 median 2.88 | Matchbook 10.00
    DATA: model 4.7% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 269-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Flooring Brandy (hrs_17395146391) | 4yo G | 166lb | OR - | draw 0 | jockey Keith Donoghue | trainer Gavin Cromwell (14d 3/41) | headgear t (1st time) | last run - days | form - | MARKET 4.7% | 09:00 median 10.00 | Matchbook 25.00
    DATA: model 4.7% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: First-time headgear
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- It's Good To Talk (hrs_61684532) | 5yo G | 166lb | OR - | draw 0 | jockey  | trainer Emmet Mullins (14d 3/12) | headgear - | last run 40 days | form 29- | MARKET 2.9% | 09:00 median 23.00 | Matchbook 30.00
    DATA: model 7.8% | style Held up (led 3% of runs) | runs in data 8 | last 3: 5 Sep Navan Flat 10f Good 17/21; 27 Sep Curragh Flat 10f Heavy 8/18; 15 Oct Curragh (IRE) Flat 14f Yielding To Soft 3/21 fig 65
    DATA for: Trainer 25% wins (3/12), last 14 days
    DATA against: First run over hurdles in our data; Pace: steady gallop likely, hard to come from off the pace
- Years Of Guessing (hrs_17395968275) | 4yo G | 166lb | OR - | draw 0 | jockey Philip Byrnes | trainer Robert Tyner (14d 0/4) | headgear - | last run - days | form - | MARKET 1.9% | 09:00 median 30.00 | Matchbook 60.00
    DATA: model 4.7% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Baldilou (hrs_17394332851) | 5yo G | 166lb | OR - | draw 0 | jockey Phillip Enright | trainer Mark Michael McNiff (14d 0/1) | headgear - | last run 32 days | form P23-4 | MARKET 1.9% | 09:00 median 41.00 | Matchbook 42.00
    DATA: model 5.3% | style Unknown | runs in data 1 | last 3: 23 Oct Sligo (IRE) Hurdle 20.5f Yielding 4/9 fig 95
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Kiltinan (hrs_58745701) | 5yo G | 166lb | OR - | draw 0 | jockey Josh Younge(7) | trainer Michael J McDonagh (14d 0/3) | headgear b | last run 12 days | form 4-P86 | MARKET 1.7% | 09:00 median 41.00 | Matchbook 60.00
    DATA: model 2.5% | style Held up (led 4% of runs) | runs in data 3 | last 3: 29 Jul Galway Hurdle 22f Good PU/20; 25 Oct Galway (IRE) Hurdle 21.5f Soft 8/12 fig 94; 12 Nov Thurles (IRE) Hurdle 20f Good 6/11
    DATA for: Last-run finishing speed +2.1% vs that field (finished strongly)
    DATA against: Poor recent finishing positions; Pulled up in 1 of its last 3 jumps runs; Pace: steady gallop likely, hard to come from off the pace
- Irish Chieftain (hrs_59025253) | 5yo G | 166lb | OR - | draw 0 | jockey Sean O'Keeffe | trainer Jonathan Fogarty (14d 0/0) | headgear - | last run - days | form - | MARKET 1.6% | 09:00 median 41.00 | Matchbook 65.00
    DATA: model 4.7% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Well Eliot (hrs_17394416291) | 5yo G | 166lb | OR - | draw 0 | jockey Jordan Canavan(7) | trainer J P Flavin (14d 1/2) | headgear - | last run 237 days | form P43- | MARKET 1.4% | 09:00 median 67.00 | Matchbook 48.00
    DATA: model 4.7% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 237-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Jetson Jane (hrs_17395156821) | 4yo F | 159lb | OR - | draw 0 | jockey Conor Stone-Walsh | trainer Paul Nolan (14d 3/12) | headgear - | last run 16 days | form 0 | MARKET 1.3% | 09:00 median 41.00 | Matchbook 95.00
    DATA: model 5.8% | style Unknown | runs in data 1 | last 3: 8 Nov Naas (IRE) NH Flat 16f Good To Yielding 12/17
    DATA for: Trainer 25% wins (3/12), last 14 days
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Sapphire Jewel (hrs_63171402) | 4yo F | 159lb | OR - | draw 0 | jockey Michael Kenneally(3) | trainer Colin Motherway (14d 0/2) | headgear - | last run 15 days | form 30-66 | MARKET 1.2% | 09:00 median 41.00 | Matchbook 100.00
    DATA: model 4.7% | style Midfield (led 3% of runs) | runs in data 4 | last 3: 29 Apr Punchestown NH Flat 16.6f Yielding 13/16; 2 Oct Gowran Park Hurdle 16.4f Good 6/13; 9 Nov Punchestown (IRE) Hurdle 20.5f Good To Yielding 6/11 fig 90
    DATA against: Best recent form figure 90, 7 lb below field average; Poor recent finishing positions
- Pros And Cons (hrs_61456430) | 5yo G | 166lb | OR - | draw 0 | jockey  | trainer Seamus Neville (14d 0/1) | headgear - | last run 19 days | form 711-27 | MARKET 1.0% | 09:00 median 67.00 | Matchbook 85.00
    DATA: model 3.0% | style Held up (led 5% of runs) | runs in data 2 | last 3: 6 Apr Cork NH Flat 19f Good To Yielding 7/8; 5 Nov Clonmel (IRE) Hurdle 16.5f Good 7/11 fig 93
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Loadstone (hrs_17390606212) | 4yo G | 166lb | OR - | draw 0 | jockey J. J. Slevin | trainer Joseph Patrick O'Brien (14d 5/31) | headgear - | last run 2 days | form 70 | MARKET 0.9% | 09:00 median 67.00 | Matchbook 130.00
    DATA: model 9.4% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 7 Nov Gowran Park (IRE) Hurdle 16f Good To Yielding 7/12; 22 Nov Cork (IRE) Hurdle 17f Soft 13/15
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Lake Isle (hrs_59961405) | 5yo M | 159lb | OR - | draw 0 | jockey Ross Berry(7) | trainer C A Murphy (14d 0/13) | headgear - | last run 316 days | form 5- | MARKET 0.7% | 09:00 median 81.00 | Matchbook 150.00
    DATA: model 3.3% | style Held up (led 8% of runs) | runs in data 1 | last 3: 12 Jan Punchestown NH Flat 16.2f Soft To Heavy 5/13
    DATA for: Last-run finishing speed +4.2% vs that field (finished strongly)
    DATA against: Trainer 0 wins from 13 runs, last 14 days; Returns from a 316-day break; Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Rickety Kate (hrs_17390609341) | 4yo F | 159lb | OR - | draw 0 | jockey John Shinnick | trainer Joseph Patrick O'Brien (14d 5/31) | headgear - | last run 2 days | form 0 | MARKET 0.6% | 09:00 median 101.00 | Matchbook 180.00
    DATA: model 2.7% | style Held up (led 8% of runs) | runs in data 1 | last 3: 22 Nov Cork (IRE) Hurdle 17f Soft 10/15
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Eamon's Dream (hrs_57654471) | 4yo G | 166lb | OR - | draw 0 | jockey Benjamin P Kennedy(7) | trainer Seamus Fahey (14d 0/2) | headgear - | last run 10 days | form 0-0 | MARKET 0.3% | 09:00 median 201.00 | Matchbook 250.00
    DATA: model 3.3% | style Held up (led 8% of runs) | runs in data 2 | last 3: 28 Apr Punchestown NH Flat 16.6f Yielding 12/18; 14 Nov Navan (IRE) Hurdle 20f Good To Yielding 13/22
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Pink Sheet Pony (hrs_58065567) | 4yo F | 159lb | OR - | draw 0 | jockey Patrick M O'Brien(5) | trainer John G Carr (14d 0/2) | headgear - | last run 9 days | form 0 | MARKET 0.2% | 09:00 median 151.00 | Matchbook 1000.00
    DATA: model 2.1% | style Unknown | runs in data 1 | last 3: 15 Nov Navan (IRE) Hurdle 16f Good To Yielding 17/17
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on

## 1:15 Tramore | race_id rac_32305465569 | New Years Day Discount Tickets Online Mares Maiden Hurdle
Hurdle |  | 2m5f0y | going Soft | Turf | 10 runners | rating band - | age 4yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Even Tho (hrs_59428936) | 5yo M | 161lb | OR - | draw 0 | jockey Brian Hayes | trainer W. P. Mullins (14d 8/45) | headgear - | last run 209 days | form F11- | MARKET 76.7% | 09:00 median 1.10 | Matchbook 1.15
    DATA: model 42.4% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 31 Mar Limerick NH Flat 19f Soft 1/11; 29 Apr Punchestown NH Flat 16.6f Yielding 1/16
    DATA for: Last-run finishing speed +13.1% vs that field (finished strongly); Good recent finishing positions
    DATA against: Returns from a 209-day break; Lightly raced: 2 runs in our data, so the model has little to go on; First run over hurdles in our data
- Lucky Valley (hrs_51341773) | 6yo M | 153lb | OR - | draw 0 | jockey Alan O'Sullivan(5) | trainer Michael Barry (14d 0/0) | headgear - | last run 20 days | form 125-53 | MARKET 6.5% | 09:00 median 10.00 | Matchbook 17.50
    DATA: model 4.9% | style Held up (led 4% of runs) | runs in data 3 | last 3: 6 Apr Cork NH Flat 16f Yielding 5/8; 18 Oct Limerick (IRE) Hurdle 16.5f Good To Yielding 5/7 fig 84; 4 Nov Wexford (IRE) Hurdle 16.5f Yielding 3/14 fig 91
    DATA for: Last-run finishing speed +5.5% vs that field (finished strongly)
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Marie D'angos (hrs_17393627783) | 4yo F | 152lb | OR - | draw 0 | jockey Jack Kennedy | trainer Gordon Elliott (14d 12/80) | headgear - | last run 45 days | form 3-8 | MARKET 4.7% | 09:00 median 12.00 | Matchbook 36.00
    DATA: model 10.2% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 10 Oct Fairyhouse Hurdle 16f Good 8/12
    DATA against: Last-run finishing speed -2.5% vs that field (faded); Lightly raced: 1 run in our data, so the model has little to go on
- Whelkeen View (hrs_17393979274) | 4yo F | 152lb | OR - | draw 0 | jockey Sean Flanagan | trainer Paul Nolan (14d 3/12) | headgear - | last run 30 days | form 3 | MARKET 3.2% | 09:00 median 15.00 | Matchbook 70.00
    DATA: model 8.6% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 25 Oct Wexford (IRE) Hurdle 20.5f Soft 3/11 fig 105
    DATA for: Trainer 25% wins (3/12), last 14 days
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Howyasox (hrs_52710462) | 6yo M | 153lb | OR 92 | draw 0 | jockey I. J. Power | trainer John Queally (14d 0/1) | headgear - | last run 54 days | form P-76F5 | MARKET 2.6% | 09:00 median 19.00 | Matchbook 70.00
    DATA: model 10.2% | style Held up (led 3% of runs) | runs in data 4 | last 3: 29 May Tramore Hurdle 21.7f Good 6/10; 10 Jul Cork Hurdle 24f Good F/11; 1 Oct Clonmel Hurdle 19.7f Good 5/11
    DATA against: Fell or unseated in 1 of its last 3 jumps runs; Pace: steady gallop likely, hard to come from off the pace
- Ma Lumiere (hrs_61078556) | 7yo M | 153lb | OR - | draw 0 | jockey Sean O'Keeffe | trainer Martin Paul Fitzgerald (14d 0/1) | headgear - | last run 222 days | form 94- | MARKET 2.6% | 09:00 median 23.00 | Matchbook 65.00
    DATA: model 5.7% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 19 Mar Cork NH Flat 16f Yielding 9/13; 16 Apr Limerick Hurdle 21.5f Soft To Heavy 4/11
    DATA against: Returns from a 222-day break; Lightly raced: 2 runs in our data, so the model has little to go on; Aged 7, older than most of this field
- Rebel Belle (hrs_17395969318) | 4yo F | 152lb | OR - | draw 0 | jockey Carl Millar(5) | trainer David Kenneth Budds (14d 1/2) | headgear - | last run - days | form - | MARKET 1.3% | 09:00 median 51.00 | Matchbook 140.00
    DATA: model 5.8% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Winged Court (hrs_17395970361) | 4yo F | 152lb | OR - | draw 0 | jockey Phillip Enright | trainer Patrick J Duffy (14d 0/0) | headgear - | last run - days | form - | MARKET 1.1% | 09:00 median 51.00 | Matchbook 140.00
    DATA: model 5.8% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Gotawinnerinyou (hrs_64135225) | 4yo F | 152lb | OR - | draw 0 | jockey J. J. Slevin | trainer P A Fahy (14d 0/5) | headgear - | last run 15 days | form 0-9 | MARKET 0.8% | 09:00 median 67.00 | Matchbook 230.00
    DATA: model 4.3% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 28 Apr Punchestown NH Flat 16.6f Yielding 11/18; 9 Nov Punchestown (IRE) Hurdle 20.5f Good To Yielding 9/11
    DATA against: Last-run finishing speed -7.3% vs that field (faded); Lightly raced: 2 runs in our data, so the model has little to go on
- A Chairde Go Leir (hrs_17390250549) | 4yo F | 152lb | OR - | draw 0 | jockey Niall Moore(5) | trainer P A Fahy (14d 0/5) | headgear - | last run 15 days | form 8U | MARKET 0.5% | 09:00 median 126.00 | Matchbook 490.00
    DATA: model 1.9% | style Held up (led 5% of runs) | runs in data 2 | last 3: 16 Aug Tramore NH Flat 16.6f Good To Yielding 8/12; 9 Nov Punchestown (IRE) Hurdle 20.5f Good To Yielding UR/11
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Fell or unseated in 1 of its last 1 jumps runs; Pace: steady gallop likely, hard to come from off the pace

## 1:45 Tramore | race_id rac_32305467506 | Book A Table For New Years Day Mares Handicap Hurdle
Hurdle |  | 2m5f0y | going Soft | Turf | 11 runners | rating band - | age 3yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Mount Shenshan (hrs_33274843) | 8yo M | 150lb | OR 92 | draw 0 | jockey Sean Cleary-Farrell(7) | trainer Thomas Mullins (14d 1/8) | headgear t | last run 10 days | form 606114 | MARKET 25.4% | 09:00 median 3.25 | Matchbook 3.60 | CHECK (skip line 3.09)
    comment: Fourth last time out, after back-to-back wins two and three starts back, shows Mount Shenshan is in good heart, and she's back quickly after ten days with experience of today's trip and going.
    DATA: model 18.5% | style Midfield (led 23% of runs) | runs in data 13 | last 3: 1 Oct Clonmel Hurdle 19.7f Good 1/11; 22 Oct Clonmel (IRE) Chase 21f Good 1/15 fig 89; 14 Nov Navan (IRE) Hurdle 20f Good To Yielding 4/12 fig 90
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Race comments mention jumping mistakes in 2 of its last 5 runs
- Coillte M C G (hrs_41629399) | 6yo M | 150lb | OR 92 | draw 0 | jockey Brian Hayes | trainer S G Carey (14d 2/4) | headgear - | last run 197 days | form 6646-8 | MARKET 14.9% | 09:00 median 5.50 | Matchbook 6.20
    comment: Winless in her last five, Coillte M C G has finished sixth or fourth in four of them before an eighth last time out, and a 197-day absence raises fitness questions.
    DATA: model 8.8% | style Held up (led 4% of runs) | runs in data 3 | last 3: 3 Jan Cork Chase 20f Yielding To Soft 4/11; 5 Mar Thurles Chase 18.1f Soft 6/9; 11 May Killarney Chase 20.5f Good To Yielding 8/14
    DATA against: Last-run finishing speed -2.0% vs that field (faded); Returns from a 197-day break; First run over hurdles in our data; Pace: steady gallop likely, hard to come from off the pace
- Miss Lia (hrs_40352319) | 6yo M | 148lb | OR 90 | draw 0 | jockey Shane O'Callaghan(3) | trainer P. J. Rothwell (14d 0/31) | headgear p | last run 57 days | form 2-0675 | MARKET 13.9% | 09:00 median 6.00 | Matchbook 6.60
    comment: Miss Lia is winless in her last five, with a fifth last time out after a seventh and a sixth, and she returns after 57 days with a yard 0/31 lately. Carrying 148 lb is a hurdle, though she has run over this trip and going before, and a second five starts back shows some ability.
    DATA: model 5.7% | style Midfield (led 3% of runs) | runs in data 6 | last 3: 13 Jun Downpatrick Chase 23.7f Good 6/12; 9 Aug Downpatrick Hurdle 21.8f Good 7/10; 28 Sep Roscommon Chase 21.6f Good To Yielding 5/10
    DATA for: Carries 6 lb less than average
    DATA against: Official rating 90, 6 lb below field average; Trainer 0 wins from 31 runs, last 14 days; Race comments mention jumping mistakes in 3 of its last 5 runs
- Mastertown Miss (hrs_63171717) | 4yo F | 155lb | OR 98 | draw 0 | jockey Cian Quirke | trainer David Harry Kelly (14d 0/5) | headgear h | last run 51 days | form 28-443 | MARKET 9.9% | 09:00 median 8.00 | Matchbook 9.80
    comment: Mastertown Miss was third last time out, with a fourth two starts back and another fourth three starts back, and she has run on today's going before.
    DATA: model 11.0% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 24 Aug Ballinrobe NH Flat 16.2f Good 4/11; 11 Sep Ballinrobe Hurdle 18f Good To Yielding 4/15; 4 Oct Killarney Hurdle 17f Good 3/8
    DATA against: Race comments mention jumping mistakes in 3 of its last 3 runs
- Maxios Prime (hrs_46450201) | 5yo M | 161lb | OR 103 | draw 0 | jockey Harry Sexton(7) | trainer P. J. Rothwell (14d 0/31) | headgear - | last run 197 days | form 7434-P | MARKET 8.3% | 09:00 median 8.50 | Matchbook 13.00
    comment: The main risk is a 197-day absence, plus a stable struggling at 0/31 lately.
    DATA: model 14.4% | style Held up (led 3% of runs) | runs in data 4 | last 3: 3 Mar Leopardstown Hurdle 18.3f Soft 3/13; 21 Mar Navan Hurdle 16f Soft To Heavy 4/12; 11 May Killarney Hurdle 20.2f Good To Yielding PU/12
    DATA for: Official rating 103, 7 lb above field average
    DATA against: Trainer 0 wins from 31 runs, last 14 days; Carries 7 lb more than average; Returns from a 197-day break; Pulled up in 1 of its last 4 jumps runs; Pace: steady gallop likely, hard to come from off the pace
- Onefortheditch (hrs_30122974) | 8yo M | 166lb | OR 108 | draw 0 | jockey Conor Smithers(7) | trainer Eamonn Francis Gallagher (14d 0/1) | headgear - | last run 12 days | form 26-5UU | MARKET 7.8% | 09:00 median 10.00 | Matchbook 13.00
    comment: Onefortheditch is yet to win in her last five, but a second five starts back shows her ability, and she has run over today's trip and going before.
    DATA: model 13.6% | style Prominent (led 3% of runs) | runs in data 7 | last 3: 6 Oct Galway Chase 18.2f Yielding To Soft 5/10; 5 Nov Clonmel (IRE) Chase 17f Good To Yielding UR/15; 12 Nov Thurles (IRE) Chase 21.5f Good UR/15
    DATA for: Official rating 108, 12 lb above field average
    DATA against: Carries 12 lb more than average; Race comments mention jumping mistakes in 3 of its last 5 runs; Fell or unseated in 2 of its last 5 jumps runs
- Dromana Mist (hrs_63810089) | 4yo F | 162lb | OR 105 | draw 0 | jockey Ms A Power(7) | trainer Patrick John Kiely (14d 0/0) | headgear - | last run 30 days | form U-711 | MARKET 6.8% | 09:00 median 11.00 | Matchbook 15.00
    comment: Dromana Mist arrives on a two-race winning run and has run over today's trip and going, but she carries 162 lb and her last-start win came 30 days ago.
    DATA: model 9.8% | style Prominent (led 4% of runs) | runs in data 4 | last 3: 10 May Cork Hurdle 17.3f Good 7/14; 16 May Wexford Hurdle 20f Good To Yielding 1/12; 25 Oct Wexford (IRE) Hurdle 20.5f Soft 1/7 fig 97
    DATA for: Best recent form figure 97, 9 lb above field average; Official rating 105, 9 lb above field average; Has won at this trip or further; Good recent finishing positions
    DATA against: Recent figures 8 lb below its current mark (looks high in the weights); Carries 8 lb more than average; Race comments mention jumping mistakes in 2 of its last 4 runs
- Clash Gold (hrs_48447315) | 7yo M | 148lb | OR 90 | draw 0 | jockey Mike O'Connor | trainer Francis J Flood (14d 0/0) | headgear - | last run 92 days | form 005-25 | MARKET 4.2% | 09:00 median 15.00 | Matchbook 30.00
    comment: Fifth last time out and a second two starts back suggest Clash Gold retains some ability, and she has run on today's going before, but she is yet to win in her last five and returns after 92 days off.
    DATA: model 7.7% | style Prominent (led 29% of runs) | runs in data 5 | last 3: 19 Apr Tramore Hurdle 16f Yielding 5/12; 9 Jun Sligo Hurdle 17.7f Yielding 2/11; 24 Aug Ballinrobe Hurdle 22.3f Good 5/12
    DATA for: Carries 6 lb less than average
    DATA against: Official rating 90, 6 lb below field average; Returns from a 92-day break
- French Adventure (hrs_17393176164) | 5yo M | 150lb | OR 92 | draw 0 | jockey Sean Flanagan | trainer David M O'Brien (14d 0/0) | headgear - | last run 19 days | form 1-P044 | MARKET 3.7% | 09:00 median 21.00 | Matchbook 27.00
    comment: French Adventure has finished fourth in each of her last two starts, but she's winless since a success five starts back and was pulled up four runs ago, so she is hard to fancy.
    DATA: model 3.4% | style Held up (led 5% of runs) | runs in data 3 | last 3: 2 Oct Gowran Park Hurdle 16.4f Good 10/20; 18 Oct Limerick (IRE) Hurdle 16.5f Good To Yielding 4/7 fig 89; 5 Nov Clonmel (IRE) Hurdle 19.5f Good 4/12 fig 81
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Lep Around (hrs_35150479) | 8yo M | 158lb | OR 100 | draw 0 | jockey Mr E P O'Brien(5) | trainer Miss M Harding (14d 0/0) | headgear p (1st time) | last run 37 days | form /03F-0 | MARKET 2.7% | 09:00 median 29.00 | Matchbook 36.00
    comment: The risk is a tough 158 lb and an unplaced effort last time out after a fall before that.
    DATA: model 5.3% | style Midfield (led 5% of runs) | runs in data 4 | last 3: 5 Mar Thurles Chase 18.1f Soft 3/9; 19 Mar Cork Hurdle 24.2f Yielding F/11; 18 Oct Limerick (IRE) Hurdle 19.5f Good To Yielding 10/14
    DATA for: First-time headgear
    DATA against: Fell or unseated in 1 of its last 3 jumps runs
- Leading Rose (hrs_17393307582) | 6yo M | 143lb | OR 85 | draw 0 | jockey Niall Moore(5) | trainer William P Murphy (14d 0/0) | headgear b | last run 14 days | form 4-1956 | MARKET 2.3% | 09:00 median 26.00 | Matchbook 65.00
    comment: Leading Rose has finished sixth and fifth in her last two outings after a ninth, and her only win came four starts back, so the recent trend is hard to like.
    DATA: model 1.7% | style Held up (led 4% of runs) | runs in data 3 | last 3: 5 Oct Fairyhouse Hurdle 20f Good 9/10; 23 Oct Sligo (IRE) Hurdle 25.5f Yielding To Soft 5/5; 10 Nov Fairyhouse (IRE) Hurdle 20.5f Good To Yielding 6/10 fig 77
    DATA for: Carries 11 lb less than average
    DATA against: Best recent form figure 77, 11 lb below field average; Recent figures 8 lb below its current mark (looks high in the weights); Official rating 85, 11 lb below field average; Pace: steady gallop likely, hard to come from off the pace

## 2:15 Tramore | race_id rac_32305469443 | Bill Halley Outstanding Contribution Award 2026 Handicap Hurdle
Hurdle |  | 2m5f0y | going Soft | Turf | 17 runners | rating band 0-100 | age 3yo+
DATA pace: Even - Two likely leaders (Lake Chad, Fairy Meadow). A fair, even gallop is most likely.
- Talas Kera (hrs_55061601) | 5yo M | 160lb | OR 92 | draw 0 | jockey Eoghan Finegan(5) | trainer John G Carr (14d 0/2) | headgear - | last run 17 days | form 540421 | MARKET 14.2% | 09:00 median 4.50 | Matchbook 5.70 | CHECK (skip line 4.27)
    comment: Talas Kera won last time out and was second two starts back, while a fresh 17 days since that run suits her, and she has run over today's trip and going before.
    DATA: model 18.2% | style Midfield (led 3% of runs) | runs in data 9 | last 3: 13 Aug Tramore Hurdle 20.5f Good 4/16; 2 Oct Gowran Park Hurdle 20.2f Good 2/13; 7 Nov Gowran Park (IRE) Hurdle 20f Good To Yielding 1/13 fig 87
    DATA for: Good recent finishing positions
    DATA against: Race comments mention jumping mistakes in 2 of its last 5 runs
- The Ducks Walk (hrs_48853973) | 8yo G | 160lb | OR 92 | draw 0 | jockey Miss Ella Herbison(7) | trainer N Dooly (14d 0/2) | headgear - | last run 15 days | form 460162 | MARKET 14.1% | 09:00 median 5.00 | Matchbook 5.30
    comment: The Ducks Walk comes into this fresh from a second last time out, 15 days ago, and he has run over today's trip, but a sixth two starts back and just one win in his last six hold him back.
    DATA: model 13.4% | style Midfield (led 4% of runs) | runs in data 9 | last 3: 2 Oct Gowran Park Hurdle 20.2f Good 1/13; 30 Oct Down Royal (IRE) Hurdle 24.5f Good To Yielding 6/20 fig 85; 9 Nov Punchestown (IRE) Hurdle 20.5f Good To Yielding 2/22 fig 91
    DATA for: Last-run finishing speed +5.9% vs that field (finished strongly); Good recent finishing positions
- Johnny Cakes (hrs_36970332) | 7yo G | 151lb | OR 83 | draw 0 | jockey Shane O'Callaghan(3) | trainer P. J. Rothwell (14d 0/31) | headgear p | last run 7 days | form 355-43 | MARKET 11.6% | 09:00 median 6.00 | Matchbook 6.60
    comment: Johnny Cakes arrives consistent, finishing third last time out and fourth two starts back, and he has run over today's trip and going before, but he is yet to win in his last five and the yard is 0/31 in the last 14 days.
    DATA: model 8.5% | style Held up (led 3% of runs) | runs in data 5 | last 3: 4 Mar Naas Hurdle 23.8f Soft To Heavy 5/12; 23 Oct Sligo (IRE) Hurdle 25.5f Yielding To Soft 4/9 fig 83; 17 Nov Limerick (IRE) Hurdle 21f Heavy 3/10 fig 73
    DATA for: Carries 5 lb less than average
    DATA against: Best recent form figure 83, 6 lb below field average; Official rating 83, 5 lb below field average; Trainer 0 wins from 31 runs, last 14 days
- Wolfhill (hrs_36416443) | 8yo G | 165lb | OR 97 | draw 0 | jockey Anna McGuinness(7) | trainer David Harry Kelly (14d 0/5) | headgear - | last run 21 days | form 0071/7 | MARKET 8.5% | 09:00 median 7.50 | Matchbook 10.50
    comment: The main risk is a seventh last time out, with 165 lb on his back.
    DATA: model 6.7% | style Unknown | runs in data 1 | last 3: 3 Nov Fairyhouse (IRE) Hurdle 20f Good To Yielding 7/15 fig 95
    DATA for: Best recent form figure 95, 6 lb above field average; Official rating 97, 9 lb above field average
    DATA against: Carries 9 lb more than average; Lightly raced: 1 run in our data, so the model has little to go on
- Le Midnightdancer (hrs_51185925) | 5yo G | 161lb | OR 93 | draw 0 | jockey Keith Donoghue | trainer Gavin Cromwell (14d 3/41) | headgear t (1st time) | last run 252 days | form 087- | MARKET 7.9% | 09:00 median 9.00 | Matchbook 9.60
    comment: Lightly raced and yet to win, Le Midnightdancer was seventh last time out after an eighth two starts back, and returns from 252 days off carrying 161 lb off an official mark of 93, so he looks unexposed with scope to improve.
    DATA: model 2.5% | style Held up (led 5% of runs) | runs in data 2 | last 3: 15 Jan Fairyhouse Hurdle 16f Soft 8/16; 17 Mar Wexford Hurdle 16f Soft 7/14
    DATA for: First-time headgear
    DATA against: Returns from a 252-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- Lake Chad (hrs_17950198) | 11yo G | 168lb | OR 100 | draw 0 | jockey Niall Moore(5) | trainer Philip Fenton (14d 1/2) | headgear - | last run 33 days | form 01-881 | MARKET 7.9% | 09:00 median 8.00 | Matchbook 10.50
    comment: The one concern is a hefty 168 lb after a 33-day break.
    DATA: model 9.1% | style Leader (led 38% of runs) | runs in data 7 | last 3: 30 May Tramore Chase 22f Good To Yielding 8/11; 13 Jun Downpatrick Chase 19.5f Good 8/14; 22 Oct Clonmel (IRE) Hurdle 17f Good To Yielding 1/16 fig 101
    DATA for: Best recent form figure 101, 12 lb above field average; Official rating 100, 12 lb above field average; Last-run finishing speed +3.7% vs that field (finished strongly); Has won at this trip or further
    DATA against: Carries 12 lb more than average; Race comments mention jumping mistakes in 4 of its last 5 runs; Aged 11, older than most of this field
- Ballinaboola Jet (hrs_32982418) | 9yo G | 148lb | OR 80 | draw 0 | jockey J. J. Slevin | trainer R Donohoe (14d 1/4) | headgear - | last run 21 days | form 0140-0 | MARKET 5.9% | 09:00 median 12.00 | Matchbook 13.50
    comment: Ballinaboola Jet has been unplaced in his last two outings and is hard to fancy after that, though a win four starts back and a fourth three starts back show he can perform on his day.
    DATA: model 3.6% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 3 Nov Fairyhouse (IRE) Hurdle 20f Good To Yielding 14/15
    DATA for: Carries 8 lb less than average
    DATA against: Official rating 80, 8 lb below field average; Last-run finishing speed -12.4% vs that field (faded); Lightly raced: 1 run in our data, so the model has little to go on
- Madame Masque (hrs_34253422) | 7yo M | 158lb | OR 90 | draw 0 | jockey  | trainer Henry de Bromhead (14d 9/42) | headgear t | last run 29 days | form 000-05 | MARKET 5.3% | 09:00 median 12.00 | Matchbook 17.50
    comment: Madame Masque is hard to fancy, yet to win in her last five and unplaced in the four runs before a fifth last time out, so she needs a big step forward.
    DATA: model 6.5% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 21 Jul Ballinrobe Hurdle 22.2f Good 11/15; 26 Oct Galway (IRE) Hurdle 24f Heavy 5/19 fig 82
    DATA for: Trainer 21% wins (9/42), last 14 days
    DATA against: Best recent form figure 82, 7 lb below field average; Recent figures 8 lb below its current mark (looks high in the weights); Lightly raced: 2 runs in our data, so the model has little to go on
- Man Down (hrs_17391270603) | 5yo G | 162lb | OR 94 | draw 0 | jockey Conor Smithers(7) | trainer Donncha Duggan (14d 0/4) | headgear - | last run 23 days | form P0679U | MARKET 5.3% | 09:00 median 12.00 | Matchbook 15.50
    comment: Man Down is hard to fancy, having unseated last time out, with a ninth and a seventh before that and nothing better than a sixth in his last six starts. He is yet to win in that spell, and 162 lb is a big burden, though 23 days since his last run at least rules out rustiness.
    DATA: model 4.9% | style Held up (led 3% of runs) | runs in data 5 | last 3: 25 Sep Listowel Hurdle 18.6f Good To Yielding 7/15; 17 Oct Limerick (IRE) Hurdle 19f Good To Yielding 9/18 fig 84; 1 Nov Cork (IRE) Hurdle 20f Good To Yielding UR/14
    DATA for: Official rating 94, 6 lb above field average
    DATA against: Best recent form figure 84, 5 lb below field average; Recent figures 10 lb below its current mark (looks high in the weights); Poor recent finishing positions; Carries 6 lb more than average; Fell or unseated in 1 of its last 5 jumps runs
- Lily Milan (hrs_48289829) | 7yo M | 154lb | OR 86 | draw 0 | jockey I. J. Power | trainer Paul Stephen Kiely (14d 0/0) | headgear p (1st time) | last run 37 days | form 586-93 | MARKET 3.4% | 09:00 median 23.00 | Matchbook 23.00
    comment: Lily Milan bounced back with a third last time out after a ninth two starts back, yet she's winless in her last five and has been beaten in the main otherwise.
    DATA: model 4.2% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 19 Mar Cork NH Flat 16f Yielding 8/13; 5 Apr Cork Hurdle 19f Yielding 6/14; 27 May Wexford Hurdle 24f Good To Yielding 9/14
    DATA for: First-time headgear
    DATA against: Poor recent finishing positions
- Walkmethroughit (hrs_40646921) | 6yo G | 151lb | OR 83 | draw 0 | jockey Sean O'Keeffe | trainer Kieran Callaghan (14d 0/0) | headgear - | last run 67 days | form 7PP-7P | MARKET 3.4% | 09:00 median 17.00 | Matchbook 28.00
    comment: Walkmethroughit is hard to fancy, pulled up in three of his last five starts, including last time out, and without a win in that spell, with a 67-day break to overcome. He has run over today's trip and his 83 official rating looks workable, but 151 lb is a big ask.
    DATA: model 5.0% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 12 Mar Limerick Hurdle 22.8f Heavy PU/15; 24 Jul Kilbeggan Chase 20.4f Good 7/14; 18 Sep Downpatrick Chase 23.5f Good PU/15
    DATA for: Carries 5 lb less than average
    DATA against: Official rating 83, 5 lb below field average; Poor recent finishing positions; Race comments mention jumping mistakes in 5 of its last 5 runs; Pulled up in 3 of its last 5 jumps runs
- Cloonbonniffe (hrs_58596643) | 5yo G | 160lb | OR 92 | draw 0 | jockey Phillip Enright | trainer Mark Michael McNiff (14d 0/1) | headgear t | last run 137 days | form 0-450 | MARKET 3.2% | 09:00 median 23.00 | Matchbook 25.00
    comment: Cloonbonniffe is winless in his last four, with a fifth two starts back and a fourth three starts back his best efforts, and he returns after 137 days off.
    DATA: model 6.1% | style Held up (led 3% of runs) | runs in data 4 | last 3: 12 May Sligo Hurdle 20f Good 4/9; 1 Jun Listowel NH Flat 20f Yielding 5/10; 10 Jul Cork Hurdle 17.3f Good 15/20
    DATA against: Last-run finishing speed -4.7% vs that field (faded); Returns from a 137-day break
- Fizzle Rock (hrs_25427668) | 9yo M | 159lb | OR 91 | draw 0 | jockey Carl Millar(5) | trainer Nigel Thomas Slevin (14d 0/4) | headgear - | last run 32 days | form 4/U9F8 | MARKET 2.3% | 09:00 median 41.00 | Matchbook 29.00
    comment: The reservation is a lack of cover from an eighth last time out and a winless last five starts.
    DATA: model 2.9% | style Held up (led 3% of runs) | runs in data 4 | last 3: 18 Sep Downpatrick Chase 17.8f Good 9/12; 6 Oct Galway Chase 18.2f Yielding To Soft F/10; 23 Oct Sligo (IRE) Hurdle 25.5f Yielding To Soft 8/9
    DATA against: Poor recent finishing positions; Fell or unseated in 2 of its last 4 jumps runs
- Fairy Meadow (hrs_49325780) | 9yo G | 159lb | OR 91 | draw 0 | jockey  | trainer John Joseph Hanlon (14d 0/9) | headgear ht | last run 23 days | form /03800 | MARKET 2.0% | 09:00 median 41.00 | Matchbook 42.00
    comment: Fairy Meadow has been unplaced in two of his last three outings and is yet to win in his last five starts, though a third four starts back shows he can cope at this level.
    DATA: model 1.8% | style Leader (led 38% of runs) | runs in data 5 | last 3: 18 Sep Downpatrick Hurdle 17.8f Good 8/15; 10 Oct Fairyhouse Hurdle 16f Good 13/15; 1 Nov Cork (IRE) Hurdle 16f Good To Yielding 14/21
    DATA against: Trainer 0 wins from 9 runs, last 14 days; Poor recent finishing positions
- Piper Street (hrs_65678249) | 5yo G | 151lb | OR 83 | draw 0 | jockey  | trainer P. J. Rothwell (14d 0/31) | headgear p (1st time) | last run 42 days | form 60000 | MARKET 1.8% | 09:00 median 51.00 | Matchbook 46.00
    comment: Piper Street has been unplaced in his last four starts, with a sixth five runs back his best recent finish, and he returns after 42 days from a yard going 0/31 lately.
    DATA: model 1.5% | style Held up (led 4% of runs) | runs in data 5 | last 3: 18 Sep Downpatrick Hurdle 17.8f Good 12/15; 2 Oct Gowran Park Hurdle 16.4f Good 13/20; 13 Oct Punchestown Hurdle 20f Good 13/15
    DATA for: Carries 5 lb less than average; First-time headgear
    DATA against: Official rating 83, 5 lb below field average; Trainer 0 wins from 31 runs, last 14 days; Poor recent finishing positions
- Carrigeen Ardisia (hrs_48789041) | 6yo M | 145lb | OR 77 | draw 0 | jockey Daniel King | trainer James M Barcoe (14d 2/6) | headgear - | last run 17 days | form 736/09 | MARKET 1.7% | 09:00 median 51.00 | Matchbook 46.00
    comment: Carrigeen Ardisia was beaten into ninth last time out after a sixth three starts back, and she is winless in her last five, though a third four starts back shows she can get involved.
    DATA: model 1.9% | style Held up (led 5% of runs) | runs in data 2 | last 3: 2 Oct Gowran Park Hurdle 16.4f Good 15/20; 7 Nov Gowran Park (IRE) Hurdle 20f Good To Yielding 9/13
    DATA for: Trainer 33% wins (2/6), last 14 days; Carries 11 lb less than average
    DATA against: Official rating 77, 11 lb below field average; Lightly raced: 2 runs in our data, so the model has little to go on
- Renard De Noir (hrs_38002384) | 8yo G | 143lb | OR 75 | draw 0 | jockey Peter Smithers(5) | trainer Ms Helen P Markham (14d 0/2) | headgear - | last run 774 days | form 40009/ | MARKET 1.6% | 09:00 median 67.00 | Matchbook 42.00
    comment: Renard De Noir has been out of sorts, finishing ninth last time out, and he returns from a 774-day absence after a fourth five starts back.
    DATA: model 3.2% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Carries 13 lb less than average
    DATA against: Official rating 75, 13 lb below field average; Returns from a 774-day break; Lightly raced: 0 runs in our data, so the model has little to go on

## 2:45 Tramore | race_id rac_32305471380 | 2027 Group Package Deals Online Beginners Steeplechase
Chase |  | 2m5f100y | going Soft | Turf | 16 runners | rating band - | age 4yo+
DATA pace: Strong pace - 3 habitual front-runners (Sekakarma, I C U In My Dreams, Queen Of The Gales). A contested lead should set things up for horses coming from behind.
- Rebel Reba (hrs_17393304453) | 6yo M | 159lb | OR - | draw 0 | jockey Brian Hayes | trainer W. P. Mullins (14d 8/45) | headgear - | last run 14 days | form /1-672 | MARKET 16.5% | 09:00 median 4.00 | Matchbook 5.00 | CHECK (skip line 3.80)
    comment: Rebel Reba is fresh from a second last time out just 14 days ago, and she has run over today's trip and going, but a seventh and a sixth before that, plus 159 lb on her back, temper enthusiasm.
    DATA: model 6.5% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 5 Oct Fairyhouse Hurdle 20f Good 6/10; 25 Oct Galway (IRE) Hurdle 21.5f Soft 7/12 fig 93; 10 Nov Fairyhouse (IRE) Hurdle 20.5f Good To Yielding 2/10 fig 85
    DATA against: First run over fences in our data
- Kimy (hrs_37789969) | 6yo M | 159lb | OR 98 | draw 0 | jockey Alan O'Sullivan(5) | trainer Thomas Mullins (14d 1/8) | headgear p | last run 6 days | form 93-023 | MARKET 13.7% | 09:00 median 5.00 | Matchbook 5.60
    comment: She is yet to win in her last five, though, and 159 lb is a hefty burden to carry.
    DATA: model 6.1% | style Midfield (led 4% of runs) | runs in data 16 | last 3: 19 Oct Gowran Park (IRE) Flat 12f Soft 5/14 fig 66; 12 Nov Thurles (IRE) Chase 18f Good 3/10 fig 93; 18 Nov Dundalk (AW) (IRE) Flat 12f Standard 7/9 fig 52
- Ersudaly (hrs_46233628) | 6yo M | 159lb | OR - | draw 0 | jockey  | trainer Gordon Elliott (14d 12/80) | headgear p | last run 46 days | form F-7082 | MARKET 9.8% | 09:00 median 6.50 | Matchbook 8.60
    comment: Ersudaly was second last time out, but that came after an eighth, an unplaced run and a seventh, and she is yet to win in her last five.
    DATA: model 3.3% | style Held up (led 3% of runs) | runs in data 6 | last 3: 14 Jul Downpatrick Hurdle 21.8f Good 11/12; 23 Jul Wexford Hurdle 24f Good 8/13; 9 Oct Downpatrick Hurdle 21.8f Good 2/14
    DATA for: Pace: a contested lead should suit its hold-up style
    DATA against: Fell or unseated in 1 of its last 5 jumps runs; First run over fences in our data
- Leni's Law (hrs_59961454) | 7yo G | 166lb | OR 100 | draw 0 | jockey Sean Flanagan | trainer Liz Doyle (14d 0/1) | headgear - | last run 30 days | form 40-745 | MARKET 8.1% | 09:00 median 8.50 | Matchbook 10.00
    DATA: model 8.0% | style Midfield (led 3% of runs) | runs in data 7 | last 3: 15 May Kilbeggan Chase 20.4f Good 7/14; 3 Oct Gowran Park Chase 20f Good To Yielding 4/8; 25 Oct Galway (IRE) Chase 18f Soft To Heavy 5/13 fig 97
    DATA for: Best recent form figure 97, 8 lb above field average
- Let's Go Mans (hrs_51373686) | 5yo G | 166lb | OR - | draw 0 | jockey Keith Donoghue | trainer Gavin Cromwell (14d 3/41) | headgear tp | last run 240 days | form 00218- | MARKET 7.9% | 09:00 median 9.00 | Matchbook 9.80
    comment: Let's Go Mans won two starts back and was second three starts back, but he was eighth last time out and returns after 240 days off, which raises fitness doubts.
    DATA: model 8.3% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 4 Mar Naas Hurdle 23.8f Soft To Heavy 1/12; 29 Mar Downpatrick Hurdle 21.8f Yielding To Soft 8/14
    DATA for: Has won at this trip or further
    DATA against: Returns from a 240-day break; Lightly raced: 2 runs in our data, so the model has little to go on; First run over fences in our data
- Walk In The Clouds (hrs_49325878) | 6yo M | 159lb | OR 96 | draw 0 | jockey Carl Millar(5) | trainer Cian Collins (14d 2/11) | headgear - | last run 238 days | form 08814- | MARKET 6.4% | 09:00 median 10.00 | Matchbook 14.00
    comment: Fourth last time out and a winner two starts back, she has run over today's trip and on this going, but 238 days off is a long layoff and she carries 159 lb.
    DATA: model 10.7% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 4 Feb Punchestown Hurdle 23f Soft To Heavy 8/10; 4 Mar Naas Hurdle 22.1f Soft To Heavy 1/11; 31 Mar Limerick Hurdle 21.3f Soft 4/14
    DATA for: Has won at this trip or further
    DATA against: Returns from a 238-day break; First run over fences in our data
- Joshua Chamberlain (hrs_29735902) | 9yo G | 166lb | OR - | draw 0 | jockey Eoghan Finegan(5) | trainer Gerard Keane (14d 0/6) | headgear - | last run 78 days | form 5/0423 | MARKET 6.4% | 09:00 median 11.00 | Matchbook 12.50
    comment: Joshua Chamberlain arrives in solid form, third last time out and a second two starts back, and he has run over today's distance and going before. The main risk is a 78-day absence, though he is yet to win in his last five and carries 166 lb.
    DATA: model 7.6% | style Midfield (led 3% of runs) | runs in data 4 | last 3: 21 Jul Ballinrobe Hurdle 22.2f Good 4/16; 24 Aug Ballinrobe Hurdle 22.3f Good 2/16; 7 Sep Galway Hurdle 22.4f Yielding 3/19
    DATA for: Good recent finishing positions
    DATA against: Race comments mention jumping mistakes in 2 of its last 4 runs; First run over fences in our data; Aged 9, older than most of this field
- Kanog Bay (hrs_49974239) | 5yo G | 166lb | OR 89 | draw 0 | jockey Mr J Dunne(7) | trainer Ian Patrick Donoghue (14d 0/10) | headgear t | last run 240 days | form 941PP- | MARKET 6.4% | 09:00 median 11.00 | Matchbook 12.00
    comment: Kanog Bay is hard to fancy after back-to-back pulled-up efforts and a 240-day absence, while carrying 166 lb. On the plus side, he won three starts back and has run on today's going before.
    DATA: model 16.3% | style Prominent (led 4% of runs) | runs in data 3 | last 3: 15 Jan Fairyhouse Hurdle 20f Soft 1/16; 5 Feb Thurles Hurdle 22.9f Soft PU/17; 29 Mar Downpatrick Hurdle 21.8f Yielding To Soft PU/10
    DATA against: Official rating 89, 7 lb below field average; Trainer 0 wins from 10 runs, last 14 days; Returns from a 240-day break; Pulled up in 2 of its last 3 jumps runs; First run over fences in our data
- Glenary Prince (hrs_51434236) | 5yo G | 166lb | OR - | draw 0 | jockey Mike O'Connor | trainer Henry de Bromhead (14d 9/42) | headgear - | last run 17 days | form 7-4P5 | MARKET 5.7% | 09:00 median 11.00 | Matchbook 15.00
    comment: Glenary Prince is yet to win in his last four starts, though a fifth last time out, just 17 days ago, shows him in some order after being pulled up two starts back.
    DATA: model 6.4% | style Prominent (led 3% of runs) | runs in data 4 | last 3: 7 Jun Punchestown Hurdle 23.5f Good 4/11; 3 Jul Wexford Hurdle 24.5f Good PU/11; 7 Nov Gowran Park (IRE) Chase 20f Good 5/10 fig 92
    DATA for: Trainer 21% wins (9/42), last 14 days
    DATA against: Race comments mention jumping mistakes in 2 of its last 4 runs; Pulled up in 1 of its last 4 jumps runs
- Jonny Carrol (hrs_51650060) | 5yo G | 166lb | OR - | draw 0 | jockey  | trainer Moses McCabe (14d 0/0) | headgear t | last run 53 days | form P-7840 | MARKET 3.9% | 09:00 median 17.00 | Matchbook 25.00
    comment: Jonny Carrol has run over today's trip and arrives with a fourth two starts back, though he's been unplaced last time out and is winless in his last five.
    DATA: model 3.6% | style Prominent (led 5% of runs) | runs in data 4 | last 3: 23 Jul Wexford Hurdle 20f Good 8/14; 7 Aug Wexford Hurdle 20.2f Good 4/14; 2 Oct Gowran Park Hurdle 20.2f Good 10/13
    DATA against: Race comments mention jumping mistakes in 2 of its last 4 runs; First run over fences in our data
- Harry's Dream (hrs_39208127) | 6yo G | 166lb | OR - | draw 0 | jockey Anna McGuinness(7) | trainer P. J. Rothwell (14d 0/31) | headgear t | last run 12 days | form 4428-0 | MARKET 3.5% | 09:00 median 21.00 | Matchbook 25.00
    comment: Harry's Dream was unplaced last time out and eighth two starts back, though a second three starts back shows he can pay his way, and he's fresh from a 12-day turnaround and has run on today's going.
    DATA: model 3.6% | style Held up (led 3% of runs) | runs in data 4 | last 3: 10 Feb Limerick Hurdle 15.7f Heavy 2/8; 17 Mar Wexford Hurdle 16f Soft 8/10; 12 Nov Thurles (IRE) Chase 18f Good 10/10
    DATA for: Pace: a contested lead should suit its hold-up style
    DATA against: Trainer 0 wins from 31 runs, last 14 days
- Spanish John (hrs_31851477) | 8yo G | 166lb | OR - | draw 0 | jockey Niall Moore(5) | trainer P A Fahy (14d 0/5) | headgear t | last run 15 days | form 20-830 | MARKET 2.8% | 09:00 median 26.00 | Matchbook 30.00
    comment: Fit enough after 15 days off, Spanish John has run over today's trip and going and was third two starts back, but he is winless in his last five and unplaced last time.
    DATA: model 6.4% | style Held up (led 3% of runs) | runs in data 7 | last 3: 30 Sep Bellewstown Flat 12.5f Soft To Heavy 6/12; 23 Oct Sligo (IRE) Hurdle 25.5f Yielding To Soft 3/9 fig 87; 9 Nov Punchestown (IRE) Hurdle 20.5f Good To Yielding 14/22 fig 79
    DATA for: Pace: a contested lead should suit its hold-up style
    DATA against: First run over fences in our data
- Datzdjazz (hrs_58962876) | 4yo F | 150lb | OR - | draw 0 | jockey  | trainer Denis Gerard Hogan (14d 0/12) | headgear - | last run 42 days | form 809-P | MARKET 2.6% | 09:00 median 29.00 | Matchbook 32.00
    comment: Datzdjazz is hard to fancy, pulled up last time out and without a win in her last four starts, with a ninth and an eighth also in that run. A 42-day break and 150 lb give her little to work with, though the freshness might help a little.
    DATA: model 1.0% | style Held up (led 8% of runs) | runs in data 1 | last 3: 13 Oct Punchestown Hurdle 20f Good PU/17
    DATA for: Pace: a contested lead should suit its hold-up style
    DATA against: Trainer 0 wins from 12 runs, last 14 days; Lightly raced: 1 run in our data, so the model has little to go on; Pulled up in 1 of its last 1 jumps runs
- I C U In My Dreams (hrs_46233593) | 6yo M | 159lb | OR - | draw 0 | jockey I. J. Power | trainer Conor Houlihan (14d 0/4) | headgear - | last run 12 days | form 216-69 | MARKET 2.3% | 09:00 median 29.00 | Matchbook 40.00
    comment: Fresh off a run just 12 days ago, she's a winner four starts back and second five starts back, but a ninth last time out and two sixths since leave her needing a bounce-back.
    DATA: model 2.6% | style Leader (led 54% of runs) | runs in data 6 | last 3: 18 Apr Bangor-on-Dee Hurdle 19.6f Good 6/9; 15 May Aintree Hurdle 20f Good 6/8; 12 Nov Thurles (IRE) Chase 18f Good 9/10
    DATA against: Poor recent finishing positions; Pace: likely to be taken on for the lead
- Sekakarma (hrs_35069097) | 9yo G | 166lb | OR - | draw 0 | jockey Harry Sexton(7) | trainer W M Roper (14d 0/0) | headgear - | last run 46 days | form 423170 | MARKET 2.2% | 09:00 median 34.00 | Matchbook 38.00
    comment: Sekakarma has dropped away since winning three starts back, finishing a seventh two starts back and unplaced last time, and he returns after 46 days carrying 166 lb.
    DATA: model 6.1% | style Leader (led 43% of runs) | runs in data 8 | last 3: 28 Aug Wexford Hurdle 20.5f Yielding 1/14; 19 Sep Navan Hurdle 19f Good 7/15; 9 Oct Downpatrick Hurdle 21.8f Good 12/14
    DATA against: First run over fences in our data; Aged 9, older than most of this field; Pace: likely to be taken on for the lead
- Queen Of The Gales (hrs_17391515708) | 6yo M | 159lb | OR - | draw 0 | jockey Mr J P Collins(7) | trainer Colin Motherway (14d 0/2) | headgear - | last run 20 days | form -12908 | MARKET 1.8% | 09:00 median 41.00 | Matchbook 50.00
    comment: Queen Of The Gales has regressed since winning five starts back, with an eighth last time out, an unplaced run before that and a ninth three starts back, so she is hard to fancy carrying 159 lb. A second four starts back and a break of only 20 days are the best points for her.
    DATA: model 3.6% | style Leader (led 29% of runs) | runs in data 3 | last 3: 28 Aug Wexford Hurdle 24.2f Yielding 9/12; 2 Oct Gowran Park Hurdle 20.2f Good 11/17; 4 Nov Wexford (IRE) Hurdle 16.5f Yielding 8/14 fig 73
    DATA against: Best recent form figure 73, 16 lb below field average; Poor recent finishing positions; First run over fences in our data; Pace: likely to be taken on for the lead

## 3:15 Tramore | race_id rac_32305473317 | Ladies Cove Handicap Steeplechase
Chase |  | 2m5f100y | going Soft | Turf | 17 runners | rating band 0-100 | age 4yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Notimelikedpresent (hrs_39959430) | 6yo G | 155lb | OR 86 | draw 0 | jockey Simon Torrens | trainer Robert Tyner (14d 0/4) | headgear t | last run 276 days | form 0/855- | MARKET 14.2% | 09:00 median 5.00 | Matchbook 5.70 | CHECK (skip line 4.75)
    comment: Hard to fancy: Notimelikedpresent is winless in his last four, with a fifth last time out, another fifth two starts back, and a 276-day layoff to overcome under 155 lb. He has run over today's trip and going, which is about the only real positive.
    DATA: model 11.7% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 21 Feb Fairyhouse Chase 23.8f Heavy 5/13
    DATA against: Returns from a 276-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Stily (hrs_39959696) | 6yo G | 145lb | OR 76 | draw 0 | jockey Sean O'Keeffe | trainer Michael J McDonagh (14d 0/3) | headgear b | last run 19 days | form 666433 | MARKET 8.0% | 09:00 median 9.00 | Matchbook 10.00
    comment: Yet to win in his last six, Stily has at least been placed in his last two, a third last time out and another third two starts back, and he returns after 19 days having run over today's trip.
    DATA: model 9.0% | style Prominent (led 3% of runs) | runs in data 7 | last 3: 11 Oct Cork Hurdle 18.9f Good 4/14; 22 Oct Clonmel (IRE) Chase 21f Good 3/15 fig 75; 5 Nov Clonmel (IRE) Chase 17f Good To Yielding 3/15 fig 77
    DATA for: Good recent finishing positions; Carries 9 lb less than average
    DATA against: Best recent form figure 77, 4 lb below field average; Official rating 76, 9 lb below field average
- King Gris (hrs_39568445) | 6yo G | 159lb | OR 90 | draw 0 | jockey Jack Kennedy | trainer Gordon Elliott (14d 12/80) | headgear p | last run 46 days | form 5-5704 | MARKET 8.0% | 09:00 median 8.50 | Matchbook 10.50
    comment: King Gris showed a touch of promise when fourth last time out and has run over today's trip, but he is winless in his last five and returns after 46 days off.
    DATA: model 4.3% | style Midfield (led 4% of runs) | runs in data 6 | last 3: 29 Aug Curragh Flat 12f Yielding 17/19; 18 Sep Downpatrick Chase 17.8f Good 10/12; 9 Oct Downpatrick Chase 23.7f Good 4/14
    DATA against: Carries 5 lb more than average
- Lough Nigara (hrs_29621886) | 9yo G | 168lb | OR 99 | draw 0 | jockey Ricky Doyle | trainer Eoin Griffin (14d 0/1) | headgear - | last run 29 days | form 121R-0 | MARKET 7.5% | 09:00 median 7.50 | Matchbook 13.50
    comment: Lough Nigara won two of his last five starts, a first three starts back and another five back, and he has run over today's trip and going before, while 29 days since his last run suggests he is fresh.
    DATA: model 6.7% | style Prominent (led 38% of runs) | runs in data 6 | last 3: 5 Mar Thurles Hurdle 22.9f Soft 1/13; 29 Mar Downpatrick Hurdle 21.8f Yielding To Soft RR/10; 26 Oct Galway (IRE) Hurdle 22f Heavy 12/12
    DATA for: Official rating 99, 14 lb above field average; Has won at this trip or further
    DATA against: Carries 14 lb more than average; First run over fences in our data
- Roccabaker (hrs_29721972) | 8yo M | 156lb | OR 87 | draw 0 | jockey Cian Quirke | trainer David Harry Kelly (14d 0/5) | headgear tp | last run 33 days | form P77-95 | MARKET 7.4% | 09:00 median 10.00 | Matchbook 11.00
    comment: Roccabaker is winless in her last five, though a fifth last time out is her best finish in that run, and she has run over today's trip and going before.
    DATA: model 7.3% | style Held up (led 3% of runs) | runs in data 7 | last 3: 19 Apr Tramore Hurdle 20.5f Yielding 7/16; 11 Sep Ballinrobe Chase 17.2f Good To Yielding 9/16; 22 Oct Clonmel (IRE) Chase 21f Good 5/15 fig 77
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 77, 4 lb below field average; Recent figures 10 lb below its current mark (looks high in the weights); Pulled up in 1 of its last 5 jumps runs; Pace: steady gallop likely, hard to come from off the pace
- Knockbrack Rambler (hrs_35321769) | 9yo G | 163lb | OR 94 | draw 0 | jockey Phillip Enright | trainer Brendan Maurice Walsh (14d 0/2) | headgear - | last run 176 days | form 858P-1 | MARKET 6.7% | 09:00 median 9.00 | Matchbook 14.00
    comment: Knockbrack Rambler won last time out and has run on today's going, but he was pulled up two starts back, has finished eighth or worse in two of his other recent runs, and returns after 176 days off carrying 163 lb off a mark of 94.
    DATA: model 6.8% | style Midfield (led 23% of runs) | runs in data 5 | last 3: 31 Mar Limerick Chase 19.6f Soft 8/11; 16 Apr Limerick Hurdle 19.3f Soft To Heavy PU/13; 1 Jun Listowel Chase 19f Yielding 1/6
    DATA for: Official rating 94, 9 lb above field average
    DATA against: Carries 9 lb more than average; Returns from a 176-day break; Race comments mention jumping mistakes in 2 of its last 5 runs; Pulled up in 1 of its last 5 jumps runs
- Ray Gun (hrs_46233859) | 4yo G | 145lb | OR 85 | draw 0 | jockey Daniel King | trainer J P Flavin (14d 1/2) | headgear tb | last run 47 days | form -P9692 | MARKET 6.2% | 09:00 median 12.00 | Matchbook 12.50
    comment: Ray Gun bounced back with a second last time out after a run of ninth, sixth and ninth, and he has run over today's trip, but he is yet to win in his last five and returns after 47 days carrying 145 lb off 85.
    DATA: model 5.8% | style Prominent (led 23% of runs) | runs in data 8 | last 3: 14 Aug Tramore Hurdle 21f Good 6/10; 28 Aug Wexford Hurdle 20.5f Yielding 9/14; 8 Oct Tramore Hurdle 20.3f Yielding 2/7
    DATA for: Carries 9 lb less than average
    DATA against: Pulled up in 1 of its last 5 jumps runs; First run over fences in our data
- Revolut Ned (hrs_40225206) | 7yo G | 155lb | OR 86 | draw 0 | jockey Mr B M Coonan(7) | trainer William P Murphy (14d 0/0) | headgear - | last run 14 days | form 137061 | MARKET 5.8% | 09:00 median 12.00 | Matchbook 14.00
    comment: Revolut Ned won last time out and was also a winner six starts back, so he arrives fresh from a 14-day turnaround and has run over today's trip. Against that, he's been inconsistent in between, and 155 lb is a hefty burden off an official mark of 86.
    DATA: model 5.1% | style Midfield (led 4% of runs) | runs in data 5 | last 3: 30 Sep Sligo Chase 25.8f Good 10/12; 14 Oct Punchestown (IRE) Chase 21.5f Good 6/8; 10 Nov Fairyhouse (IRE) Chase 24f Good To Yielding 1/5 fig 81
    DATA for: Has won at this trip or further
- Orlando Spirit (hrs_412672925) | 6yo G | 154lb | OR 85 | draw 0 | jockey  | trainer Paul Power (14d 0/0) | headgear - | last run 195 days | form 0238-4 | MARKET 5.8% | 09:00 median 9.50 | Matchbook 18.50
    comment: Fourth last time out and a second four starts back show Orlando Spirit can get involved, but he is winless in his last five and returns after 195 days off. Carrying 154 lb off an official mark of 85, he looks short of the class to lead this field.
    DATA: model 9.4% | style Held up (led 3% of runs) | runs in data 5 | last 3: 19 Mar Cork Hurdle 17.1f Yielding 3/22; 16 Apr Limerick Hurdle 19.3f Soft To Heavy 8/14; 13 May Punchestown Hurdle 24f Good To Yielding 4/18
    DATA for: Last-run finishing speed +6.8% vs that field (finished strongly)
    DATA against: Returns from a 195-day break; First run over fences in our data; Pace: steady gallop likely, hard to come from off the pace
- Drumadeise (hrs_64036693) | 5yo M | 146lb | OR 77 | draw 0 | jockey  | trainer P Corkery (14d 0/0) | headgear p | last run 50 days | form 00U025 | MARKET 5.3% | 09:00 median 12.00 | Matchbook 19.50
    comment: Drumadeise is winless in her last six, though a second two starts back and a fifth last time out show some life, and she has run over today's trip.
    DATA: model 4.8% | style Prominent (led 3% of runs) | runs in data 8 | last 3: 22 Aug Killarney Hurdle 20.2f Good 14/15; 26 Sep Listowel Hurdle 22f Good 2/17; 5 Oct Fairyhouse Hurdle 24f Good 5/14
    DATA for: Carries 8 lb less than average
    DATA against: Official rating 77, 8 lb below field average; Fell or unseated in 1 of its last 5 jumps runs; First run over fences in our data
- Another Ocana (hrs_27997319) | 9yo G | 150lb | OR 81 | draw 0 | jockey Alan O'Sullivan(5) | trainer L J Archdeacon (14d 0/0) | headgear p | last run 23 days | form 53-378 | MARKET 5.2% | 09:00 median 15.00 | Matchbook 14.50
    comment: Winless in his last five and beaten into eighth last time, Another Ocana is hard to fancy, though two thirds four and three starts back show he can get involved, and he has run over today's trip and going.
    DATA: model 5.3% | style Midfield (led 3% of runs) | runs in data 7 | last 3: 21 May Limerick Chase 22.7f Good 3/11; 17 Oct Limerick (IRE) Hurdle 21.5f Good To Yielding 7/16 fig 74; 1 Nov Cork (IRE) Hurdle 16f Good To Yielding 8/21 fig 69
    DATA against: Best recent form figure 74, 7 lb below field average; Recent figures 7 lb below its current mark (looks high in the weights)
- Moorish Castle (hrs_51373595) | 6yo G | 168lb | OR 99 | draw 0 | jockey  | trainer P A Fahy (14d 0/5) | headgear - | last run 15 days | form FP-010 | MARKET 4.7% | 09:00 median 12.00 | Matchbook 22.00
    comment: Moorish Castle won two starts back and returns just 15 days after his last run, so he should be fit, and he has run on today's going before. Carrying 168 lb off an official mark of 99 is the main risk, along with an unplaced effort last time out.
    DATA: model 6.1% | style Midfield (led 29% of runs) | runs in data 6 | last 3: 2 Oct Gowran Park Hurdle 20.2f Good 17/20; 23 Oct Sligo (IRE) Hurdle 25.5f Yielding To Soft 1/9 fig 96; 9 Nov Punchestown (IRE) Chase 24.5f Good To Yielding 10/12 fig 87
    DATA for: Best recent form figure 96, 15 lb above field average; Official rating 99, 14 lb above field average; Has won at this trip or further
    DATA against: Last-run finishing speed -4.2% vs that field (faded); Carries 14 lb more than average; Fell or unseated in 1 of its last 5 jumps runs; Pulled up in 1 of its last 5 jumps runs
- Without Exception (hrs_37687447) | 7yo G | 149lb | OR 80 | draw 0 | jockey Harry Sexton(7) | trainer P. J. Rothwell (14d 0/31) | headgear p | last run 257 days | form 203P4- | MARKET 4.6% | 09:00 median 15.00 | Matchbook 18.50
    comment: Fourth last time out and a third three starts back suggest he can still run a race, and he has experience of today's trip and going, but a 257-day absence and a yard 0/31 in the last 14 days temper enthusiasm. He's winless in his last five and carries 149 lb off 80.
    DATA: model 5.4% | style Held up (led 5% of runs) | runs in data 2 | last 3: 10 Feb Limerick Hurdle 21f Heavy PU/14; 12 Mar Limerick Hurdle 22.8f Heavy 4/15
    DATA against: Official rating 80, 5 lb below field average; Trainer 0 wins from 31 runs, last 14 days; Returns from a 257-day break; Lightly raced: 2 runs in our data, so the model has little to go on; Pulled up in 1 of its last 2 jumps runs; First run over fences in our data; Pace: steady gallop likely, hard to come from off the pace
- Rockstown Girl (hrs_30865527) | 8yo M | 167lb | OR 98 | draw 0 | jockey James Smith(3) | trainer A. McCann (14d 0/5) | headgear tp | last run 16 days | form 6742P4 | MARKET 3.5% | 09:00 median 21.00 | Matchbook 24.00
    comment: Rockstown Girl arrives fit after 16 days, having finished fourth last time out and second three starts back, and she has run over today's trip and going before.
    DATA: model 2.6% | style Midfield (led 3% of runs) | runs in data 12 | last 3: 9 Oct Downpatrick Chase 19.5f Good 2/8; 22 Oct Clonmel (IRE) Chase 21f Good PU/15; 8 Nov Naas (IRE) Chase 16f Good To Yielding 4/4
    DATA for: Official rating 98, 13 lb above field average
    DATA against: Carries 13 lb more than average; Race comments mention jumping mistakes in 3 of its last 5 runs; Pulled up in 1 of its last 5 jumps runs
- Likable Chancer (hrs_18828502) | 12yo G | 141lb | OR 72 | draw 0 | jockey Shane O'Callaghan(3) | trainer Daniel John Howard (14d 0/0) | headgear tb | last run 38 days | form 3P5-8P | MARKET 3.2% | 09:00 median 19.00 | Matchbook 30.00
    comment: Likable Chancer is hard to fancy after being pulled up last time out and again four starts back, with an eighth and a fifth in between, and he is winless in his last five. He has run over today's trip and going, and a third five runs ago shows some ability off 141 lb.
    DATA: model 3.1% | style Prominent (led 4% of runs) | runs in data 5 | last 3: 20 Apr Tramore Chase 21.7f Good To Yielding 5/12; 21 May Limerick Chase 22.7f Good 8/11; 17 Oct Limerick (IRE) Hurdle 21.5f Good To Yielding PU/18
    DATA for: Carries 13 lb less than average
    DATA against: Official rating 72, 13 lb below field average; Pulled up in 2 of its last 5 jumps runs; Aged 12, older than most of this field
- God Help Us (hrs_23858352) | 10yo G | 155lb | OR 86 | draw 0 | jockey E Walsh | trainer Eamonn Francis Gallagher (14d 0/1) | headgear p | last run 257 days | form /613P- | MARKET 2.7% | 09:00 median 26.00 | Matchbook 34.00
    DATA: model 4.7% | style Held up (led 8% of runs) | runs in data 1 | last 3: 12 Mar Limerick Chase 22.8f Heavy PU/16
    DATA against: Returns from a 257-day break; Lightly raced: 1 run in our data, so the model has little to go on; Pulled up in 1 of its last 1 jumps runs; Pace: steady gallop likely, hard to come from off the pace
- Battle Of Benburb (hrs_21678636) | 9yo G | 141lb | OR 72 | draw 0 | jockey Mr P Verling(7) | trainer Patrick Michael Verling (14d 0/1) | headgear b | last run 12 days | form P-04P9 | MARKET 1.0% | 09:00 median 67.00 | Matchbook 120.00
    comment: The risk is form that reads poorly, with a ninth last time out and a pulled up two starts back.
    DATA: model 1.9% | style Prominent (led 4% of runs) | runs in data 5 | last 3: 22 Aug Killarney Chase 23.4f Good 4/4; 22 Oct Clonmel (IRE) Chase 21f Good PU/15; 12 Nov Thurles (IRE) Chase 21.5f Good 9/15
    DATA for: Carries 13 lb less than average
    DATA against: Official rating 72, 13 lb below field average; Last-run finishing speed -11.5% vs that field (faded); Race comments mention jumping mistakes in 2 of its last 5 runs; Pulled up in 2 of its last 5 jumps runs

## 3:50 Tramore | race_id rac_32305475254 | Irish Stallion Farms EBF Mares (Ladies Pro/Am) Flat Race
NH Flat |  | 2m0f50y | going Soft | Turf | 13 runners | rating band - | age 4yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Lady Aurora (hrs_17395972447) | 5yo M | 165lb | OR - | draw 0 | jockey Miss J Townend | trainer W. P. Mullins (14d 8/45) | headgear - | last run 296 days | form P1- | MARKET 37.6% | 09:00 median 2.20 | Matchbook 2.36
    comment: Unexposed mare who won last time out after being pulled up the start before, so there's little to go on yet and plenty of scope for improvement. She returns after 296 days off and carries 165 lb, so fitness is the question.
    DATA: model 5.9% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 296-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Found It (hrs_61012665) | 5yo M | 165lb | OR - | draw 0 | jockey Miss Charlotte Butler(7) | trainer Gordon Elliott (14d 12/80) | headgear - | last run 206 days | form 217- | MARKET 14.4% | 09:00 median 6.00 | Matchbook 6.00
    comment: Found It won two starts back and was second three starts back, but she was only seventh last time and returns after 206 days off, so fitness is a question.
    DATA: model 17.2% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 2 May Punchestown NH Flat 16f Yielding 7/16
    DATA against: Returns from a 206-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Shuil Solas (hrs_66463446) | 5yo M | 165lb | OR - | draw 0 | jockey Miss H Ross(7) | trainer John E & Thomas Kiely (14d 0/2) | headgear - | last run 9 days | form 59227 | MARKET 12.0% | 09:00 median 6.00 | Matchbook 8.20
    comment: Shuil Solas ran a pair of seconds two and three starts back and is fresh from a run nine days ago, so fitness is no concern, though she was seventh last time and is yet to win in her last five.
    DATA: model 17.3% | style Midfield (led 29% of runs) | runs in data 5 | last 3: 25 Sep Listowel NH Flat 16f Good To Yielding 2/14; 13 Oct Punchestown NH Flat 16.2f Good 2/14; 15 Nov Navan (IRE) NH Flat 16f Good To Yielding 7/8 fig 89
    DATA for: Good recent finishing positions
- Lest Ye Forget (hrs_60343395) | 4yo F | 165lb | OR - | draw 0 | jockey Ms A Power(7) | trainer Patrick John Kiely (14d 0/0) | headgear - | last run 30 days | form 5-3 | MARKET 9.9% | 09:00 median 8.00 | Matchbook 9.20
    comment: Lest Ye Forget arrives in decent order after a third last time out, and a fifth two starts back, and she has run over today's trip and going before, so conditions should not be a concern.
    DATA: model 5.1% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 3 Jan Cork NH Flat 16f Yielding To Soft 5/9; 25 Oct Wexford (IRE) NH Flat 17.5f Soft 3/8 fig 95
    DATA for: Best recent form figure 95, 5 lb above field average
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Miss Kobe (hrs_17392912285) | 5yo M | 165lb | OR - | draw 0 | jockey Ms L A Byrne(7) | trainer John McConnell (14d 0/17) | headgear - | last run 45 days | form 4 | MARKET 6.1% | 09:00 median 13.00 | Matchbook 15.00
    comment: The risk is a 45-day absence, though she is yet to win in her recent form.
    DATA: model 12.1% | style Held up (led 8% of runs) | runs in data 1 | last 3: 10 Oct Fairyhouse NH Flat 16f Good 4/10
    DATA against: Trainer 0 wins from 17 runs, last 14 days; Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Mozart's Song (hrs_66619504) | 4yo F | 165lb | OR - | draw 0 | jockey Ms A T O'Reilly(7) | trainer Eamon Courtney (14d 0/1) | headgear - | last run 30 days | form 33 | MARKET 5.2% | 09:00 median 15.00 | Matchbook 19.00
    DATA: model 5.4% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 7 Sep Galway NH Flat 16.7f Soft 3/18; 25 Oct Galway (IRE) NH Flat 16f Soft 3/6 fig 87
    DATA for: Good recent finishing positions
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Back In Favour (hrs_52709363) | 5yo M | 165lb | OR - | draw 0 | jockey Miss A B O'Connor | trainer A. McCann (14d 0/5) | headgear h | last run 42 days | form 1-8330 | MARKET 4.9% | 09:00 median 15.00 | Matchbook 22.00
    comment: Back In Favour bids to bounce back after an unplaced latest effort, having been third two starts back and third again three starts back, and she has run over today's trip.
    DATA: model 10.9% | style Midfield (led 23% of runs) | runs in data 4 | last 3: 2 Aug Galway NH Flat 16f Good 3/6; 23 Sep Listowel NH Flat 20f Good 3/11; 13 Oct Punchestown NH Flat 16.2f Good 12/14
    DATA for: Good recent finishing positions
- For My Lady (hrs_17392700556) | 5yo M | 165lb | OR - | draw 0 | jockey Miss P Elvin(7) | trainer P. J. Rothwell (14d 0/31) | headgear - | last run 29 days | form 2-F | MARKET 3.7% | 09:00 median 15.00 | Matchbook 46.00
    comment: Lightly raced and unexposed, For My Lady fell last time out but was second two starts back, so there's likely more to come from the mare. She returns after 29 days off, carrying 165 lb, though the yard is 0/31 in the last 14 days.
    DATA: model 2.7% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 26 Oct Galway (IRE) Hurdle 16.5f Soft To Heavy F/10
    DATA against: Trainer 0 wins from 31 runs, last 14 days; Lightly raced: 1 run in our data, so the model has little to go on; Fell or unseated in 1 of its last 1 jumps runs
- She's Trixy (hrs_17393385807) | 4yo F | 165lb | OR - | draw 0 | jockey Anna McGuinness(7) | trainer John McConnell (14d 0/17) | headgear p (1st time) | last run 49 days | form 7 | MARKET 2.2% | 09:00 median 34.00 | Matchbook 65.00
    comment: She's Trixy was only seventh last time out and is yet to win in her recent form, which makes her hard to fancy after 49 days off and with 165 lb to carry.
    DATA: model 4.8% | style Held up (led 8% of runs) | runs in data 1 | last 3: 6 Oct Galway NH Flat 16.6f Yielding To Soft 7/8
    DATA for: First-time headgear
    DATA against: Trainer 0 wins from 17 runs, last 14 days; Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Saint Herblaine (hrs_17394421506) | 4yo F | 165lb | OR - | draw 0 | jockey Miss N Lockhead Anderson(7) | trainer J P Flavin (14d 1/2) | headgear - | last run - days | form - | MARKET 1.7% | 09:00 median 34.00 | Matchbook 100.00
    comment: Unraced and making her debut, Saint Herblaine is a completely unexposed filly with nothing on the formbook to judge her by, so any improvement is there to be found.
    DATA: model 5.9% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Dice In Her Eyes (hrs_17395475979) | 5yo M | 165lb | OR - | draw 0 | jockey Miss Georgie Benson(7) | trainer Tom McGuinness (14d 1/3) | headgear - | last run 30 days | form 3 | MARKET 1.5% | 09:00 median 41.00 | Matchbook 85.00
    comment: Lightly raced and unexposed, Dice In Her Eyes finished third last time out and returns after 30 days off, so she looks open to improvement. She is yet to win in her recent form and carries 165 lb.
    DATA: model 5.9% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Allez Yeats (hrs_66655309) | 7yo M | 165lb | OR - | draw 0 | jockey Miss Ella Herbison(7) | trainer James M Barcoe (14d 2/6) | headgear - | last run 7 days | form P6 | MARKET 0.4% | 09:00 median 151.00 | Matchbook 500.00
    comment: Lightly raced and open to improvement, Allez Yeats was sixth last time out and pulled up two starts back, so she remains unexposed. She turns out again just seven days later and carries 165 lb.
    DATA: model 4.6% | style Prominent (led 8% of runs) | runs in data 2 | last 3: 12 Jul Sligo NH Flat 18.3f Good PU/11; 17 Nov Limerick (IRE) NH Flat 16f Heavy 6/8
    DATA for: Trainer 33% wins (2/6), last 14 days
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Peace Rose (hrs_17392914371) | 4yo F | 165lb | OR - | draw 0 | jockey Mrs Holly Conte | trainer Vincent Conte (14d 0/0) | headgear - | last run 42 days | form 00 | MARKET 0.2% | 09:00 median 201.00 | Matchbook 1000.00
    comment: Peace Rose is unexposed, with just two recent outings and both unplaced, so she's yet to show what she can do. She returns after 42 days off carrying 165 lb, and there should be improvement in her.
    DATA: model 2.3% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 25 Sep Listowel NH Flat 16f Good To Yielding 12/14; 13 Oct Punchestown NH Flat 16.2f Good 14/14
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
