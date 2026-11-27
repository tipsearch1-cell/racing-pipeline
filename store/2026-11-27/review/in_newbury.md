# Card review packet: Newbury, 2026-11-27

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
{"meeting": "newbury", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 11:40 Newbury | race_id rac_32306093157 | Coral "Black Friday Price Boosts" 'National Hunt' Maiden Hurdle Race (Div I) (GBB Race)
Hurdle | Class 3 | 2m69y | going Good To Soft | Turf | 12 runners | rating band - | age 4yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Prince Rupert (hrs_62549193) | 4yo G | 158lb | OR - | draw 0 | jockey Nico de Boinville | trainer Nicky Henderson (14d 2/20) | headgear t | wind surgery | last run 258 days | form 1- | MARKET 40.4% | 09:00 median 2.10 | Matchbook 2.32
    DATA: model 19.6% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 14 Mar Kempton NH Flat 16f Good 1/10
    DATA for: Last-run finishing speed +7.8% vs that field (finished strongly); Has won at this trip or further
    DATA against: Returns from a 258-day break; Lightly raced: 1 run in our data, so the model has little to go on
- River Kwai (hrs_62615063) | 5yo G | 158lb | OR - | draw 0 | jockey Sam Twiston-Davies | trainer Paul Nicholls (14d 2/22) | headgear - | last run 255 days | form 1- | MARKET 22.6% | 09:00 median 3.75 | Matchbook 4.20
    DATA: model 19.9% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 17 Mar Exeter NH Flat 16.7f Good To Soft 1/10
    DATA for: Last-run finishing speed +13.1% vs that field (finished strongly); Has won at this trip or further
    DATA against: Returns from a 255-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Lover Desbois (hrs_44975161) | 5yo G | 158lb | OR - | draw 0 | jockey Paul O'Brien | trainer Harry Derham (14d 1/14) | headgear - | last run 251 days | form 414- | MARKET 19.6% | 09:00 median 4.33 | Matchbook 4.80
    DATA: model 14.0% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 2 Feb Kempton NH Flat 16f Good To Soft 1/14; 21 Mar Newbury NH Flat 16.3f Good To Soft 4/20
    DATA for: Last-run finishing speed +3.7% vs that field (finished strongly); Has won at this trip or further
    DATA against: Returns from a 251-day break; Lightly raced: 2 runs in our data, so the model has little to go on; First run over hurdles in our data
- Loughmourne (hrs_51185967) | 5yo G | 158lb | OR - | draw 0 | jockey Bryan Carver | trainer Harry Fry (14d 2/5) | headgear - | last run 285 days | form 1- | MARKET 9.5% | 09:00 median 8.50 | Matchbook 10.50
    DATA: model 6.3% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 40% wins (2/5), last 14 days
    DATA against: Returns from a 285-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Midnight Escape (hrs_56559335) | 5yo G | 158lb | OR - | draw 0 | jockey Jonathan Burke | trainer Ben Case (14d 1/7) | headgear - | last run 26 days | form 4-4 | MARKET 2.2% | 09:00 median 34.00 | Matchbook 50.00
    DATA: model 3.6% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 1 Nov Worcester Hurdle 16f Good To Soft 4/16 fig 111
    DATA for: Best recent form figure 111, 7 lb above field average; Last-run finishing speed +3.6% vs that field (finished strongly)
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Francisco Alvares (hrs_17394316163) | 4yo G | 158lb | OR - | draw 0 | jockey Tristan Durrell | trainer Dan Skelton (14d 23/95) | headgear - | last run 14 days | form 4 | MARKET 1.7% | 09:00 median 34.00 | Matchbook 90.00
    DATA: model 3.8% | style Held up (led 8% of runs) | runs in data 1 | last 3: 13 Nov Southwell NH Flat 16f Good 4/7 fig 101
    DATA for: Trainer 24% wins (23/95), last 14 days
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Lady Kluck (hrs_412693407) | 6yo M | 151lb | OR - | draw 0 | jockey Jack Tudor | trainer David Pipe (14d 2/14) | headgear - | wind surgery | last run 586 days | form 31453/ | MARKET 1.3% | 09:00 median 51.00 | Matchbook 95.00
    DATA: model 5.7% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 586-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Burk Flight (hrs_17394787599) | 4yo G | 158lb | OR - | draw 0 | jockey Sean Bowen | trainer Olly Murphy (14d 9/50) | headgear - | last run 8 days | form 57 | MARKET 0.9% | 09:00 median 51.00 | Matchbook 270.00
    DATA: model 9.8% | style Prominent (led 38% of runs) | runs in data 2 | last 3: 3 Nov Lingfield NH Flat 16f Standard / Slow 5/8 fig 101; 19 Nov Warwick Hurdle 16f Soft 7/14
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Island Getaway (hrs_63202769) | 4yo G | 158lb | OR - | draw 0 | jockey Caoilin Quinn | trainer Warren Greatrex (14d 4/23) | headgear h (1st time) | wind surgery | last run 12 days | form 5-28 | MARKET 0.5% | 09:00 median 126.00 | Matchbook 330.00
    DATA: model 6.3% | style Midfield (led 5% of runs) | runs in data 3 | last 3: 4 Apr Huntingdon NH Flat 15.8f Good 5/8; 7 May Huntingdon NH Flat 15.8f Good 2/3; 15 Nov Cheltenham Hurdle 16.5f Good 8/11
    DATA for: First-time headgear
- Cool Million (hrs_64522955) | 4yo F | 151lb | OR - | draw 0 | jockey Harry Kimber | trainer Faye Bramley (14d 1/14) | headgear - | last run 126 days | form 530 | MARKET 0.5% | 09:00 median 126.00 | Matchbook 460.00
    DATA: model 2.9% | style Held up (led 5% of runs) | runs in data 3 | last 3: 11 May Southwell NH Flat 15.8f Good 5/10; 30 Jun Stratford NH Flat 16.3f Good To Firm 3/7; 24 Jul Uttoxeter Hurdle 15.8f Good 12/13
    DATA against: Last-run finishing speed -10.0% vs that field (faded); Returns from a 126-day break; Pace: steady gallop likely, hard to come from off the pace
- Killarney (hrs_17394598816) | 6yo G | 158lb | OR - | draw 0 | jockey Freddie Gordon | trainer Chris Gordon (14d 3/13) | headgear - | last run 12 days | form 25-7 | MARKET 0.4% | 09:00 median 151.00 | Matchbook 390.00
    DATA: model 4.5% | style Held up (led 8% of runs) | runs in data 2 | last 3: 29 Oct Stratford Hurdle 16.5f Good To Soft 5/10; 15 Nov Fontwell Hurdle 17.5f Soft 7/13
    DATA for: Trainer 23% wins (3/13), last 14 days
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Soldier Poet (hrs_59186295) | 5yo G | 158lb | OR - | draw 0 | jockey Rex Dingle | trainer Nick Gifford (14d 2/7) | headgear h (1st time) | wind surgery | last run 24 days | form 254-0 | MARKET 0.4% | 09:00 median 151.00 | Matchbook 450.00
    DATA: model 3.6% | style Midfield (led 8% of runs) | runs in data 2 | last 3: 16 Mar Plumpton NH Flat 17.8f Good To Soft 4/5; 3 Nov Lingfield Hurdle 16f Good 10/11
    DATA for: Trainer 29% wins (2/7), last 14 days; First-time headgear
    DATA against: Last-run finishing speed -10.1% vs that field (faded); Lightly raced: 2 runs in our data, so the model has little to go on

## 12:10 Newbury | race_id rac_32305727064 | Play Coral "Racing-Super-Series" For Free 'National Hunt' Maiden Hurdle Race (Div II) (GBB Race)
Hurdle | Class 3 | 2m69y | going Good To Soft | Turf | 12 runners | rating band - | age 4yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Stick To The Board (hrs_51831759) | 5yo G | 158lb | OR - | draw 0 | jockey Sam Twiston-Davies | trainer Paul Nicholls (14d 2/22) | headgear - | last run 48 days | form F1-2 | MARKET 48.6% | 09:00 median 1.73 | Matchbook 1.89
    DATA: model 23.5% | style Unknown | runs in data 2 | last 3: 26 Mar Chepstow NH Flat 16.1f Good To Soft 1/10; 10 Oct Chepstow Hurdle 19.5f Good To Soft 2/13
    DATA for: Last-run finishing speed +6.2% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Tally Ho Back (hrs_58099447) | 5yo G | 158lb | OR - | draw 0 | jockey Toby McCain-Mitchell(3) | trainer Nigel & Willy Twiston-Davies (14d 3/19) | headgear - | last run 261 days | form 4260- | MARKET 19.1% | 09:00 median 4.33 | Matchbook 4.90
    DATA: model 5.3% | style Prominent (led 8% of runs) | runs in data 2 | last 3: 18 Jan Windsor NH Flat 16f Soft 6/6; 11 Mar Cheltenham NH Flat 16.4f Good 10/21
    DATA for: Last-run finishing speed +3.6% vs that field (finished strongly)
    DATA against: Returns from a 261-day break; Lightly raced: 2 runs in our data, so the model has little to go on; First run over hurdles in our data
- Octo Gane (hrs_39431707) | 6yo G | 158lb | OR - | draw 0 | jockey Ben Jones | trainer Ben Pauling (14d 8/44) | headgear - | wind surgery | last run 22 days | form 4/6-2 | MARKET 18.6% | 09:00 median 4.33 | Matchbook 5.10
    DATA: model 6.0% | style Held up (led 5% of runs) | runs in data 2 | last 3: 6 Apr Fairyhouse NH Flat 16f Yielding To Soft 6/12; 5 Nov Newbury Hurdle 16.5f Good To Soft 2/9 fig 112
    DATA for: Best recent form figure 112, 9 lb above field average
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Duhallow Storm (hrs_62941116) | 4yo G | 158lb | OR - | draw 0 | jockey Rex Dingle | trainer Anthony Honeyball (14d 1/12) | headgear - | last run 41 days | form 4-1 | MARKET 3.8% | 09:00 median 17.00 | Matchbook 38.00
    DATA: model 14.9% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 14 Apr Newton Abbot NH Flat 16.8f Good 4/8; 17 Oct Newton Abbot NH Flat 17f Good 1/7 fig 108
    DATA for: Best recent form figure 108, 5 lb above field average; Last-run finishing speed +5.3% vs that field (finished strongly); Has won at this trip or further
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; First run over hurdles in our data
- Ashes And Arrows (hrs_52329228) | 5yo G | 158lb | OR - | draw 0 | jockey Tristan Durrell | trainer Dan Skelton (14d 23/95) | headgear - | last run - days | form - | MARKET 2.7% | 09:00 median 26.00 | Matchbook 44.00
    DATA: model 6.7% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 24% wins (23/95), last 14 days
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Jetaway Holiday (hrs_52741850) | 5yo G | 158lb | OR - | draw 0 | jockey Nico de Boinville | trainer Nicky Henderson (14d 2/20) | headgear t | wind surgery | last run 22 days | form 155-6 | MARKET 2.2% | 09:00 median 34.00 | Matchbook 50.00
    DATA: model 8.0% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 8 Mar Warwick NH Flat 16f Good To Soft 5/10; 8 Apr Fontwell Hurdle 19.1f Good To Soft 5/12; 5 Nov Newbury Hurdle 19f Good To Soft 6/10 fig 100
- Plan de Stan (hrs_59862523) | 4yo G | 158lb | OR - | draw 0 | jockey Ben Poste | trainer Tom Symonds (14d 0/3) | headgear - | last run 23 days | form 22-6F | MARKET 1.7% | 09:00 median 41.00 | Matchbook 75.00
    DATA: model 9.3% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 6 Apr Hereford NH Flat 16.2f Good 2/11; 9 May Haydock NH Flat 15.7f Good To Soft 6/9; 4 Nov Chepstow Hurdle 16f Good To Soft F/13
    DATA against: Fell or unseated in 1 of its last 1 jumps runs
- Rock On Ronnie (hrs_60090205) | 5yo G | 158lb | OR - | draw 0 | jockey Sean Bowen | trainer Olly Murphy (14d 9/50) | headgear t (1st time) | last run 8 days | form 73-20 | MARKET 1.1% | 09:00 median 51.00 | Matchbook 160.00
    DATA: model 8.2% | style Midfield (led 5% of runs) | runs in data 3 | last 3: 24 Apr Perth NH Flat 16.2f Good 3/11; 29 Oct Stratford Hurdle 16.5f Good To Soft 2/9 fig 96; 19 Nov Warwick Hurdle 16f Soft 10/14
    DATA for: Good recent finishing positions; First-time headgear
    DATA against: Best recent form figure 96, 7 lb below field average; Last-run finishing speed -4.7% vs that field (faded)
- Jaycee Reidy (hrs_17393185551) | 5yo G | 158lb | OR - | draw 0 | jockey Freddie Gordon | trainer Chris Gordon (14d 3/13) | headgear - | last run 24 days | form F/1-54 | MARKET 1.0% | 09:00 median 67.00 | Matchbook 130.00
    DATA: model 9.2% | style Held up (led 8% of runs) | runs in data 2 | last 3: 3 Oct Fontwell Hurdle 17.7f Good 5/11; 3 Nov Lingfield Hurdle 16f Good 4/11 fig 100
    DATA for: Trainer 23% wins (3/13), last 14 days; Last-run finishing speed +2.5% vs that field (finished strongly)
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Unbelievable Jeff (hrs_17394597773) | 4yo G | 158lb | OR - | draw 0 | jockey Harry Kimber | trainer Faye Bramley (14d 1/14) | headgear - | last run 15 days | form 80 | MARKET 0.5% | 09:00 median 201.00 | Matchbook 220.00
    DATA: model 2.7% | style Midfield (led 8% of runs) | runs in data 2 | last 3: 29 Oct Stratford Hurdle 16.5f Good To Soft 8/10; 12 Nov Hereford Hurdle 16f Good To Firm 10/12
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Days of Joy (hrs_17393184508) | 4yo F | 151lb | OR - | draw 0 | jockey Dylan Johnston | trainer Neil Mulholland (14d 1/12) | headgear - | last run 55 days | form 43-P | MARKET 0.4% | 09:00 median 201.00 | Matchbook 260.00
    DATA: model 3.0% | style Held up (led 8% of runs) | runs in data 1 | last 3: 3 Oct Fontwell Hurdle 17.7f Good PU/11
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on; Pulled up in 1 of its last 1 jumps runs; Pace: steady gallop likely, hard to come from off the pace
- Our Rarest Hour (hrs_17395616784) | 4yo G | 158lb | OR - | draw 0 | jockey David Noonan | trainer Claire Dyson (14d 0/2) | headgear - | last run 8 days | form 530 | MARKET 0.2% | 09:00 median 201.00 | Matchbook 1000.00
    DATA: model 3.3% | style Held up (led 8% of runs) | runs in data 1 | last 3: 19 Nov Warwick Hurdle 16f Soft 14/15
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace

## 12:40 Newbury | race_id rac_32305729001 | Coral Racing Club Novices' Limited Handicap Steeple Chase (For The Fulke Walwyn Trophy) (GBB Race)
Chase | Class 3 | 2m92y | going Good | Turf | 4 runners | rating band - | age 4yo+
DATA pace: Lone leader - Country Mile is the only habitual front-runner and may be allowed an easy lead.
- Klub de Reve (hrs_41189953) | 6yo G | 159lb | OR 132 | draw 0 | jockey Paul O'Brien | trainer Harry Derham (14d 1/14) | headgear - | last run 279 days | form /4211- | MARKET 34.7% | 09:00 median 2.63 | Matchbook 2.84
    comment: Klub de Reve arrives on a roll, a winner last time out and again two starts back, with a second three starts back, and he has run over today's trip before.
    DATA: model 33.0% | style Held up (led 8% of runs) | runs in data 1 | last 3: 21 Feb Kempton Hurdle 16f Good To Soft 1/12
    DATA for: Last-run finishing speed +5.5% vs that field (finished strongly); Has won at this trip or further
    DATA against: Returns from a 279-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Hardly Surprising (hrs_50433131) | 5yo G | 145lb | OR 118 | draw 0 | jockey Harry Cobden | trainer Harry Fry (14d 2/5) | headgear t | last run 233 days | form /5331- | MARKET 25.6% | 09:00 median 3.50 | Matchbook 3.95
    comment: Hardly Surprising won last time out and was third on both starts before that, so he arrives in good heart with a clear case as a threat off 145 lb. The one concern is a 233-day absence, which leaves fitness an open question.
    DATA: model 36.2% | style Prominent (led 8% of runs) | runs in data 2 | last 3: 23 Jan Doncaster Hurdle 19.4f Soft 3/13; 8 Apr Fontwell Hurdle 19.1f Good To Soft 1/12
    DATA for: Trainer 40% wins (2/5), last 14 days; Last-run finishing speed +7.2% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions; Carries 11 lb less than average
    DATA against: Official rating 118, 11 lb below field average; Returns from a 233-day break; Lightly raced: 2 runs in our data, so the model has little to go on; First run over fences in our data
- Masked Man (hrs_52267257) | 5yo G | 157lb | OR 130 | draw 0 | jockey J. J. Slevin | trainer Nigel & Willy Twiston-Davies (14d 3/19) | headgear - | last run 48 days | form 1219-F | MARKET 22.9% | 09:00 median 4.00 | Matchbook 4.30
    comment: Masked Man has two wins in his last five starts, including a victory three starts back and another five starts back, and he has run over today's trip, so he's a solid threat at 157 lb. The risk is a confidence knock after falling last time out, followed by a ninth two starts back, and 48 days off.
    DATA: model 11.2% | style Prominent (led 8% of runs) | runs in data 2 | last 3: 11 Apr Aintree Hurdle 20f Good To Soft 9/12; 10 Oct Chepstow Hurdle 19.5f Good To Soft F/17
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Fell or unseated in 1 of its last 2 jumps runs; First run over fences in our data
- Country Mile (hrs_38417561) | 7yo G | 164lb | OR 137 | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 23/95) | headgear ht | last run 41 days | form /23-1F | MARKET 16.8% | 09:00 median 5.50 | Matchbook 5.90
    DATA: model 19.6% | style Leader (led 38% of runs) | runs in data 2 | last 3: 4 Oct Uttoxeter Chase 16f Good 1/3; 17 Oct Newton Abbot Chase 21f Good F/4
    DATA for: Official rating 137, 8 lb above field average; Trainer 24% wins (23/95), last 14 days; Has won at this trip or further; Pace: may get an uncontested lead
    DATA against: Carries 8 lb more than average; Lightly raced: 2 runs in our data, so the model has little to go on; Fell or unseated in 1 of its last 2 jumps runs

## 1:15 Newbury | race_id rac_32305730938 | Coral "Daily Rewards Shaker" Fillies' Juvenile Hurdle Race (Listed Race) (GBB Race)
Hurdle | Class 1 | 2m69y | going Good To Soft | Turf | 7 runners | rating band - | age 3yo
DATA pace: Even - Two likely leaders (Echo Valley, Koala Rose). A fair, even gallop is most likely.
- Koala Rose (hrs_59367301) | 3yo F | 154lb | OR - | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 23/95) | headgear - | last run 15 days | form 1 | MARKET 48.8% | 09:00 median 1.91 | Matchbook 1.95
    DATA: model 11.1% | style Prominent (led 54% of runs) | runs in data 6 | last 3: 6 Aug Newmarket Flat 16f Good To Firm 3/5; 26 Sep Ripon Flat 12f Good 2/9; 12 Nov Hereford Hurdle 16f Good To Firm 1/3 fig 64
    DATA for: Trainer 24% wins (23/95), last 14 days; Last-run finishing speed +8.1% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Best recent form figure 64, 21 lb below field average
- Nathalie Jolie (hrs_63908810) | 3yo F | 154lb | OR - | draw 0 | jockey Harry Cobden | trainer Nicky Henderson (14d 2/20) | headgear h (1st time) | last run 222 days | form 1- | MARKET 34.0% | 09:00 median 2.63 | Matchbook 2.90
    comment: Nathalie Jolie won her only recent start, but that came 222 days ago, so a long absence is a factor. Unexposed and open to improvement, she shoulders 154 lb here.
    DATA: model 11.3% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: First-time headgear
    DATA against: Returns from a 222-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Espritroyale (hrs_53841046) | 3yo F | 154lb | OR - | draw 0 | jockey Conor Stone-Walsh | trainer Gavin Cromwell (14d 4/41) | headgear h | last run 24 days | form 1 | MARKET 8.5% | 09:00 median 9.50 | Matchbook 13.00
    comment: Espritroyale won last time out and returns after 24 days, a fresh enough gap for a filly who has also run over today's trip.
    DATA: model 23.4% | style Prominent (led 3% of runs) | runs in data 9 | last 3: 21 Sep Listowel Flat 12f Yielding 9/15; 11 Oct Naas Flat 10.7f Soft 5/12; 3 Nov Fairyhouse (IRE) Hurdle 16f Good To Yielding 1/13 fig 102
    DATA for: Best recent form figure 102, 17 lb above field average; Last-run finishing speed +6.2% vs that field (finished strongly); Has won at this trip or further
- Echo Valley (hrs_60818436) | 3yo F | 154lb | OR - | draw 0 | jockey Gavin Sheehan | trainer Tom Symonds (14d 0/3) | headgear - | last run 32 days | form 1 | MARKET 4.8% | 09:00 median 19.00 | Matchbook 21.00
    comment: Echo Valley arrives a winner last time out, and that fresh confidence plus a month's break since that run (32 days) makes her a serious threat, having already run over today's trip.
    DATA: model 23.4% | style Leader (led 29% of runs) | runs in data 9 | last 3: 15 Sep Wolverhampton Flat 14f Standard 4/9; 29 Sep Wolverhampton Flat 16.5f Standard 4/11; 26 Oct Hereford Hurdle 16f Good To Firm 1/9 fig 96
    DATA for: Best recent form figure 96, 11 lb above field average; Last-run finishing speed +5.2% vs that field (finished strongly); Has won at this trip or further
- Hey Stella (hrs_7000000203) | 3yo F | 154lb | OR - | draw 0 | jockey Ben Jones | trainer Faye Bramley (14d 1/14) | headgear - | last run 38 days | form - | MARKET 2.1% | 09:00 median 34.00 | Matchbook 70.00
    comment: Hey Stella is unexposed with no recorded form to go on, so she is open to improvement on her return after 38 days off. She carries 154 lb, and there is little here to hold against her.
    DATA: model 9.2% | style Prominent (led 29% of runs) | runs in data 4 | last 3: 2 Sep Navan Flat 10f Good 11/21; 8 Sep Galway Flat 12f Soft 2/17; 20 Oct Curragh (IRE) Flat 12f Yielding 4/7 fig 59
    DATA against: First run over hurdles in our data
- Red Moon (hrs_58745225) | 3yo F | 154lb | OR - | draw 0 | jockey Kevin Brogan | trainer Richard Bandey (14d 0/1) | headgear - | last run 26 days | form 2 | MARKET 1.1% | 09:00 median 81.00 | Matchbook 140.00
    comment: The main risk is the 154 lb she carries, while she remains yet to win in her recent form.
    DATA: model 14.3% | style Prominent (led 8% of runs) | runs in data 9 | last 3: 13 Sep Bath Flat 8f Good To Soft 5/10; 30 Sep Kempton Flat 8f Standard To Slow 7/11; 1 Nov Worcester Hurdle 16f Good To Soft 2/5 fig 86
- Talka (hrs_64134546) | 3yo F | 154lb | OR - | draw 0 | jockey Jonathan Burke | trainer Donald McCain (14d 2/21) | headgear tb | last run 32 days | form R2 | MARKET 0.7% | 09:00 median 126.00 | Matchbook 150.00
    comment: The risk is the 154 lb burden, plus a refusal two starts back that raises a question over her attitude.
    DATA: model 7.3% | style Prominent (led 29% of runs) | runs in data 3 | last 3: 19 Sep Chester Flat 14.4f Heavy 10/10; 7 Oct Worcester Hurdle 16f Good RO/8; 26 Oct Hereford Hurdle 16f Good To Firm 2/8 fig 79
    DATA for: Last-run finishing speed +3.6% vs that field (finished strongly)
    DATA against: Best recent form figure 79, 6 lb below field average; Fell or unseated in 1 of its last 2 jumps runs

## 1:50 Newbury | race_id rac_32305732875 | Coral John Francome Novices' Steeple Chase(grade 2) (GBB Race)
Chase | Class 1 | 2m3f187y | going Good | Turf | 5 runners | rating band - | age 4yo+
DATA pace: Even - Two likely leaders (Catchintsavo, Tutti Quanti). A fair, even gallop is most likely.
- Taurus Bay (hrs_49757792) | 5yo G | 161lb | OR 142 | draw 0 | jockey Ben Jones | trainer Ben Pauling (14d 8/44) | headgear - | last run 20 days | form 1120-1 | MARKET 37.5% | 09:00 median 2.50 | Matchbook 2.58
    DATA: model 16.9% | style Prominent (led 29% of runs) | runs in data 3 | last 3: 24 Jan Cheltenham Hurdle 20.3f Soft 2/7; 11 Mar Cheltenham Hurdle 21f Good 15/21; 7 Nov Aintree Chase 20f Good To Soft 1/4 fig 145
    DATA for: Best recent form figure 145, 11 lb above field average; Has won at this trip or further; Good recent finishing positions
- Tutti Quanti (hrs_38884678) | 6yo G | 158lb | OR 149 | draw 0 | jockey Sam Twiston-Davies | trainer Paul Nicholls (14d 2/22) | headgear - | last run 44 days | form 118F-2 | MARKET 28.9% | 09:00 median 3.25 | Matchbook 3.35
    DATA: model 20.4% | style Prominent (led 43% of runs) | runs in data 4 | last 3: 10 Mar Cheltenham Hurdle 16.4f Good To Soft 8/9; 18 Apr Ayr Hurdle 16f Heavy F/8; 14 Oct Ffos Las Chase 19.5f Soft 2/4 fig 140
    DATA for: Best recent form figure 140, 6 lb above field average; Official rating 149, 7 lb above field average
    DATA against: Fell or unseated in 1 of its last 4 jumps runs
- Royal Infantry (hrs_34252855) | 7yo G | 158lb | OR 141 | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 23/95) | headgear t | last run 21 days | form 295-11 | MARKET 19.4% | 09:00 median 4.50 | Matchbook 5.30
    DATA: model 30.8% | style Prominent (led 23% of runs) | runs in data 6 | last 3: 15 Apr Haydock Hurdle 21.2f Good 5/11; 20 Oct Hexham Chase 20f Good 1/3 fig 133; 6 Nov Aintree Chase 25f Good To Soft 1/3 fig 130
    DATA for: Trainer 24% wins (23/95), last 14 days; Has won at this trip or further; Good recent finishing positions
- Favour And Fortune (hrs_32733491) | 8yo G | 158lb | OR 140 | draw 0 | jockey Tom Bellamy | trainer Alan King (14d 4/26) | headgear - | last run 20 days | form /635-3 | MARKET 8.5% | 09:00 median 11.00 | Matchbook 11.50
    DATA: model 16.1% | style Held up (led 3% of runs) | runs in data 4 | last 3: 10 Apr Aintree Hurdle 20f Good To Soft 3/22; 25 Apr Sandown Hurdle 19.8f Good 5/10; 7 Nov Aintree Chase 20f Good To Soft 3/4 fig 138
    DATA for: Best recent form figure 138, 4 lb above field average; Good recent finishing positions
- Catchintsavo (hrs_41190121) | 6yo G | 158lb | OR 139 | draw 0 | jockey Rex Dingle | trainer Anthony Honeyball (14d 1/12) | headgear t | last run 34 days | form 1312-4 | MARKET 5.7% | 09:00 median 15.00 | Matchbook 16.50
    DATA: model 15.7% | style Leader (led 63% of runs) | runs in data 5 | last 3: 9 Mar Plumpton Hurdle 20.5f Good To Soft 1/5; 10 Apr Aintree Hurdle 24.7f Good To Soft 2/12; 24 Oct Cheltenham Chase 25f Good To Soft 4/6 fig 112
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Best recent form figure 112, 22 lb below field average

## 2:25 Newbury | race_id rac_32305734812 | Coral "Bet£10 Get£50 Sign Up Offer" Handicap Steeple Chase (GBB Race)
Chase | Class 2 | 2m3f187y | going Good | Turf | 7 runners | rating band 0-150 | age 4yo+
DATA pace: Lone leader - Twinjets is the only habitual front-runner and may be allowed an easy lead.
- Kap Ouest (hrs_37807133) | 7yo G | 143lb | OR 125 | draw 0 | jockey Harry Cobden | trainer Harry Fry (14d 2/5) | headgear h | last run 266 days | form 59/21- | MARKET 35.9% | 09:00 median 2.50 | Matchbook 2.80
    comment: Kap Ouest won last time out and was second two starts back, but he returns after 266 days off, carries 143 lb off 125, and has run over today's trip.
    DATA: model 18.6% | style Held up (led 8% of runs) | runs in data 2 | last 3: 23 Jan Doncaster Chase 19.1f Soft 2/4; 6 Mar Exeter Chase 17.5f Good To Soft 1/4
    DATA for: Trainer 40% wins (2/5), last 14 days; Last-run finishing speed +2.5% vs that field (finished strongly); Good recent finishing positions; Carries 12 lb less than average
    DATA against: Official rating 125, 12 lb below field average; Returns from a 266-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- Twinjets (hrs_28220458) | 9yo G | 169lb | OR 151 | draw 0 | jockey Jay Tidball(5) | trainer Paul Nicholls (14d 2/22) | headgear - | last run 27 days | form UP21-P | MARKET 18.2% | 09:00 median 5.00 | Matchbook 5.30
    DATA: model 22.8% | style Leader (led 79% of runs) | runs in data 5 | last 3: 21 Mar Newbury Chase 19.9f Good To Soft 2/7; 17 Apr Ayr Chase 20.5f Soft 1/9; 31 Oct Wetherby Chase 24f Good PU/6
    DATA for: Official rating 151, 14 lb above field average; Has won at this trip or further; Pace: may get an uncontested lead
    DATA against: Carries 14 lb more than average; Fell or unseated in 1 of its last 5 jumps runs; Pulled up in 2 of its last 5 jumps runs
- Etalon (hrs_27698342) | 9yo G | 158lb | OR 140 | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 23/95) | headgear tp | last run 20 days | form 4-35P4 | MARKET 14.4% | 09:00 median 6.00 | Matchbook 7.20
    comment: The main risk is that he is yet to win in his last five starts, including a pulled up two starts back.
    DATA: model 11.6% | style Held up (led 5% of runs) | runs in data 6 | last 3: 23 Sep Perth Chase 23.8f Good 5/8; 14 Oct Ffos Las Chase 24f Soft PU/6; 7 Nov Aintree Chase 20f Good To Soft 4/11 fig 130
    DATA for: Trainer 24% wins (23/95), last 14 days
    DATA against: Recent figures 10 lb below its current mark (looks high in the weights); Pulled up in 1 of its last 5 jumps runs
- Teddy Blue (hrs_24638887) | 8yo G | 159lb | OR 141 | draw 0 | jockey Paul O'Brien | trainer Harry Derham (14d 1/14) | headgear tb | last run 27 days | form 31P3-8 | MARKET 10.4% | 09:00 median 8.50 | Matchbook 9.60
    comment: The main risk is an eighth last time out, which leaves him with something to prove.
    DATA: model 12.0% | style Prominent (led 5% of runs) | runs in data 6 | last 3: 10 Apr Aintree Chase 21.1f Good To Soft PU/27; 25 Apr Sandown Chase 22.7f Good 3/5; 31 Oct Ascot Chase 17f Good 8/11 fig 138
    DATA for: Has won at this trip or further
    DATA against: Race comments mention jumping mistakes in 2 of its last 5 runs; Pulled up in 1 of its last 5 jumps runs
- Issar d'Airy (hrs_29509004) | 8yo G | 142lb | OR 124 | draw 0 | jockey Caoilin Quinn | trainer Jamie Moore & Josh Moore (14d 3/34) | headgear - | last run 391 days | form 522/8- | MARKET 9.9% | 09:00 median 9.25 | Matchbook 10.00
    comment: Issar d'Airy is hard to fancy after a 391-day absence and an eighth last time out, though he was second two starts back, and a second three starts back, and has run over today's trip.
    DATA: model 9.7% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Carries 13 lb less than average
    DATA against: Official rating 124, 13 lb below field average; Returns from a 391-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Gemirande (hrs_21955059) | 10yo G | 152lb | OR 134 | draw 0 | jockey Ned Fox(3) | trainer Venetia Williams (14d 0/11) | headgear - | last run 602 days | form 16700/ | MARKET 6.6% | 09:00 median 13.00 | Matchbook 15.50
    comment: Gemirande returns after 602 days off, having been unplaced in his last two runs and with a win five starts back his only success in recent form.
    DATA: model 11.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Trainer 0 wins from 11 runs, last 14 days; Returns from a 602-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Le Patron (hrs_30864673) | 8yo G | 164lb | OR 146 | draw 0 | jockey David Noonan | trainer Jamie Moore & Josh Moore (14d 3/34) | headgear - | wind surgery | last run 580 days | form P105P/ | MARKET 4.7% | 09:00 median 21.00 | Matchbook 21.00
    comment: The big risk is a 580-day absence, plus he was pulled up last time out.
    DATA: model 13.9% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Official rating 146, 9 lb above field average
    DATA against: Carries 9 lb more than average; Returns from a 580-day break; Lightly raced: 0 runs in our data, so the model has little to go on

## 3:00 Newbury | race_id rac_32305736749 | Coral Long Distance Hurdle Race (Grade 2) (GBB Race)
Hurdle | Class 1 | 3m57y | going Good To Soft | Turf | 11 runners | rating band - | age 4yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Le Frimeur (hrs_50666882) | 5yo G | 159lb | OR 150 | draw 0 | jockey J. J. Slevin | trainer Harry Derham (14d 1/14) | headgear - | last run 212 days | form 1/111- | MARKET 22.8% | 09:00 median 4.00 | Matchbook 4.10 | CHECK (skip line 3.80)
    comment: Four wins in his last four starts is a formidable record, and he has run over today's trip, but 212 days off the track and 159 lb on his back are real questions to answer.
    DATA: model 14.8% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 20 Mar Newbury Hurdle 20.5f Good To Soft 1/8; 29 Apr Punchestown Hurdle 23.9f Yielding 1/14
    DATA for: Last-run finishing speed +5.5% vs that field (finished strongly); Good recent finishing positions
    DATA against: Returns from a 212-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- Soldier Reeves (hrs_50188446) | 5yo G | 156lb | OR 147 | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 23/95) | headgear t | last run 230 days | form 12342- | MARKET 18.0% | 09:00 median 5.00 | Matchbook 5.10
    comment: Soldier Reeves has been consistent, with a second last time out and a win five starts back, but he returns after 230 days off and carries 156 lb off an official mark of 147.
    DATA: model 6.1% | style Held up (led 8% of runs) | runs in data 3 | last 3: 17 Jan Haydock Hurdle 15.7f Good To Soft 3/6; 11 Mar Cheltenham Hurdle 21f Good 4/21; 11 Apr Aintree Hurdle 20f Good To Soft 2/12
    DATA for: Trainer 24% wins (23/95), last 14 days; Last-run finishing speed +4.5% vs that field (finished strongly); Good recent finishing positions
    DATA against: Returns from a 230-day break; Pace: steady gallop likely, hard to come from off the pace
- Ma Shantou (hrs_38288460) | 7yo G | 160lb | OR 154 | draw 0 | jockey Jonathan Burke | trainer Emma Lavelle (14d 4/23) | headgear - | last run 260 days | form 10118- | MARKET 11.7% | 09:00 median 7.00 | Matchbook 8.60
    comment: Ma Shantou won twice in a row two and three starts back, but he was eighth last time out and now returns after 260 days off, which raises fitness doubts. He has run over today's trip, though 160 lb is a hefty burden on an official 154.
    DATA: model 10.4% | style Prominent (led 4% of runs) | runs in data 3 | last 3: 1 Jan Cheltenham Hurdle 24f Good 1/7; 24 Jan Cheltenham Hurdle 24f Soft 1/6; 12 Mar Cheltenham Hurdle 24f Good 8/10
    DATA for: Official rating 154, 5 lb above field average; Has won at this trip or further; Good recent finishing positions
    DATA against: Last-run finishing speed -11.1% vs that field (faded); Returns from a 260-day break
- Impose Toi (hrs_32538835) | 8yo G | 162lb | OR 157 | draw 0 | jockey Harry Cobden | trainer Nicky Henderson (14d 2/20) | headgear - | last run 230 days | form 112PF- | MARKET 11.6% | 09:00 median 7.50 | Matchbook 8.40
    comment: Back-to-back wins four and five starts back, then a second three starts back, show Impose Toi at his best, and he has run over today's trip, but a fall last time out, a pulled up before that and 230 days off are the concern under 162 lb.
    DATA: model 7.9% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 24 Jan Cheltenham Hurdle 24f Soft 2/6; 12 Mar Cheltenham Hurdle 24f Good PU/10; 11 Apr Aintree Hurdle 24.7f Good To Soft F/11
    DATA for: Official rating 157, 8 lb above field average
    DATA against: Returns from a 230-day break; Fell or unseated in 1 of its last 3 jumps runs; Pulled up in 1 of its last 3 jumps runs
- Wade Out (hrs_35150304) | 7yo G | 156lb | OR 147 | draw 0 | jockey Gavin Sheehan | trainer Olly Murphy (14d 9/50) | headgear p | last run 230 days | form 11461- | MARKET 10.0% | 09:00 median 8.50 | Matchbook 9.80
    comment: Wade Out won last time out and has three wins in his last five starts, though he returns after 230 days off and carries 156 lb.
    DATA: model 10.5% | style Prominent (led 8% of runs) | runs in data 3 | last 3: 18 Jan Windsor Chase 24.3f Soft 4/6; 10 Mar Cheltenham Chase 29.9f Good To Soft 6/17; 11 Apr Aintree Hurdle 24.7f Good To Soft 1/22
    DATA for: Last-run finishing speed +7.1% vs that field (finished strongly); Has won at this trip or further
    DATA against: Returns from a 230-day break
- Strong Leader (hrs_30096829) | 9yo G | 160lb | OR 153 | draw 0 | jockey Sean Bowen | trainer Olly Murphy (14d 9/50) | headgear p | last run 27 days | form 226P-1 | MARKET 9.8% | 09:00 median 8.00 | Matchbook 11.00
    comment: Winner last time out and fresh off a 27-day break, Strong Leader has also finished second twice in his last five starts, and he has run over today's trip before.
    DATA: model 8.8% | style Midfield (led 29% of runs) | runs in data 3 | last 3: 24 Jan Cheltenham Hurdle 24f Soft 6/6; 11 Apr Aintree Hurdle 24.7f Good To Soft PU/11; 31 Oct Wetherby Hurdle 24f Good 1/3 fig 154
    DATA for: Has won at this trip or further
    DATA against: Pulled up in 1 of its last 3 jumps runs
- Caldwell Potter (hrs_29212862) | 8yo G | 156lb | OR 153 | draw 0 | jockey Sam Twiston-Davies | trainer Paul Nicholls (14d 2/22) | headgear - | last run 602 days | form 13211/ | MARKET 5.3% | 09:00 median 15.00 | Matchbook 19.50
    comment: The one big risk is a 602-day absence, which makes fitness the question under 156 lb.
    DATA: model 6.7% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 602-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Lavida Adiva (hrs_35417116) | 7yo M | 149lb | OR 136 | draw 0 | jockey Jack Tudor | trainer Ruth Jefferson (14d 1/3) | headgear - | last run 27 days | form 4327-2 | MARKET 3.8% | 09:00 median 19.00 | Matchbook 30.00
    comment: Winless in her last five, Lavida Adiva was second last time out and has been placed in three of those runs, but a seventh in between and 149 lb on her back make her hard to fancy.
    DATA: model 4.8% | style Midfield (led 5% of runs) | runs in data 5 | last 3: 12 Mar Cheltenham Hurdle 24f Good 2/24; 11 Apr Aintree Hurdle 24.7f Good To Soft 7/11; 31 Oct Wetherby Hurdle 24f Good 2/3 fig 142
    DATA for: Good recent finishing positions
    DATA against: Official rating 136, 13 lb below field average
- Lud'or (hrs_35767767) | 6yo G | 160lb | OR 146 | draw 0 | jockey Caoilin Quinn | trainer Tom Symonds (14d 0/3) | headgear - | last run 286 days | form /1331- | MARKET 3.7% | 09:00 median 23.00 | Matchbook 27.00
    DATA: model 18.6% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 18 Jan Windsor Hurdle 24f Soft 3/15; 14 Feb Haydock Hurdle 24.3f Good To Soft 1/5
    DATA for: Last-run finishing speed +2.6% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Returns from a 286-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- Thomas Mor (hrs_27997151) | 9yo G | 156lb | OR 147 | draw 0 | jockey Callum Pritchard | trainer Philip Hobbs & Johnson White (14d 2/17) | headgear - | last run 261 days | form 0/128- | MARKET 1.9% | 09:00 median 41.00 | Matchbook 60.00
    DATA: model 3.7% | style Held up (led 8% of runs) | runs in data 1 | last 3: 11 Mar Cheltenham Chase 25f Good 9/14
    DATA against: Returns from a 261-day break; Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Supremely West (hrs_29117284) | 8yo G | 156lb | OR 144 | draw 0 | jockey Tristan Durrell | trainer Dan Skelton (14d 23/95) | headgear - | last run 26 days | form 4614-P | MARKET 1.3% | 09:00 median 51.00 | Matchbook 110.00
    comment: Pulled up last time out, Supremely West is hard to fancy after a fourth two starts back, though he did win three starts back and has run over today's trip.
    DATA: model 7.7% | style Held up (led 8% of runs) | runs in data 3 | last 3: 12 Mar Cheltenham Hurdle 24f Good 1/24; 11 Apr Aintree Hurdle 24.7f Good To Soft 4/22; 1 Nov Carlisle Hurdle 20f Good To Soft PU/10
    DATA for: Trainer 24% wins (23/95), last 14 days; Has won at this trip or further
    DATA against: Pulled up in 1 of its last 3 jumps runs; Pace: steady gallop likely, hard to come from off the pace

## 3:35 Newbury | race_id rac_32305738686 | Coral "Pipped-At-The-Post" And Win Handicap Hurdle Race
Hurdle | Class 3 | 3m57y | going Good To Soft | Turf | 15 runners | rating band 0-135 | age 4yo+
DATA pace: Even - Two likely leaders (Isaac des Obeaux, Blizzard of Oz). A fair, even gallop is most likely.
- Harbour Light (hrs_50590421) | 5yo G | 151lb | OR 118 | draw 0 | jockey Toby McCain-Mitchell(3) | trainer Nigel & Willy Twiston-Davies (14d 3/19) | headgear - | last run 20 days | form 211-11 | MARKET 16.7% | 09:00 median 5.00 | Matchbook 5.40 | CHECK (skip line 4.75)
    comment: Harbour Light arrives on a four-race winning streak, a second five starts back the only blemish, and has run over today's trip after 20 days off.
    DATA: model 19.4% | style Midfield (led 5% of runs) | runs in data 7 | last 3: 28 Mar Stratford Hurdle 22f Good 1/9; 11 Oct Chepstow Hurdle 23.6f Good To Soft 1/12; 7 Nov Uttoxeter Hurdle 23.5f Good 1/9 fig 113
    DATA for: Good recent finishing positions; Carries 6 lb less than average
    DATA against: Best recent form figure 113, 6 lb below field average; Official rating 118, 6 lb below field average
- Western Monkey (hrs_38580591) | 7yo G | 157lb | OR 124 | draw 0 | jockey Paul O'Brien | trainer Harry Derham (14d 1/14) | headgear - | last run 22 days | form 11-7 | MARKET 16.2% | 09:00 median 5.00 | Matchbook 5.80
    comment: Western Monkey won two starts back and three starts back, but a seventh last time out tempers the enthusiasm, and he has run over today's trip before.
    DATA: model 6.1% | style Held up (led 8% of runs) | runs in data 1 | last 3: 5 Nov Newbury Hurdle 24.5f Good To Soft 7/16 fig 122
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Alentejo (hrs_37589286) | 7yo G | 159lb | OR 126 | draw 0 | jockey Nico de Boinville | trainer Nicky Henderson (14d 2/20) | headgear t | last run 224 days | form 0/P21- | MARKET 14.8% | 09:00 median 5.50 | Matchbook 6.40
    comment: Alentejo won last time out and was second two starts back, so the form is on the up, and he has run over today's trip before.
    DATA: model 3.3% | style Midfield (led 29% of runs) | runs in data 9 | last 3: 3 Aug Cork Hurdle 18f Good PU/18; 19 Aug Sligo Hurdle 17.7f Good 9/13; 4 Oct Killarney Hurdle 17f Good 14/16
    DATA for: Has won at this trip or further
    DATA against: Poor recent finishing positions; Returns from a 224-day break; Pulled up in 1 of its last 5 jumps runs
- Lihyan (hrs_29226547) | 8yo G | 157lb | OR 124 | draw 0 | jockey Benjamin Macey(5) | trainer Rebecca Menzies (14d 0/10) | headgear h | last run 20 days | form 7-4605 | MARKET 13.8% | 09:00 median 6.45 | Matchbook 6.40
    comment: Lihyan was fifth last time out, 20 days ago, but he is winless in his last five starts and has finished no better than fourth in that spell.
    DATA: model 6.0% | style Held up (led 3% of runs) | runs in data 7 | last 3: 10 Oct Hexham Hurdle 23.3f Good 6/6; 24 Oct Cheltenham Hurdle 24f Good 11/19 fig 118; 7 Nov Aintree Hurdle 24.5f Good To Soft 5/14 fig 121
    DATA for: Has won at this trip or further
    DATA against: Trainer 0 wins from 10 runs, last 14 days
- Geezer Rockstar (hrs_34789769) | 7yo G | 155lb | OR 122 | draw 0 | jockey Bryan Carver | trainer Harry Fry (14d 2/5) | headgear tp | last run 195 days | form /871-1 | MARKET 9.6% | 09:00 median 8.00 | Matchbook 10.50
    comment: Geezer Rockstar won last time out and two starts back, which is the obvious lure, but he returns after 195 days off carrying 155 lb off 122.
    DATA: model 11.2% | style Midfield (led 5% of runs) | runs in data 3 | last 3: 2 Feb Kempton Hurdle 21f Good To Soft 7/11; 1 Apr Wincanton Hurdle 21.4f Good 1/8; 16 May Uttoxeter Hurdle 23.3f Good 1/8
    DATA for: Trainer 40% wins (2/5), last 14 days; Last-run finishing speed +4.6% vs that field (finished strongly); Good recent finishing positions
    DATA against: Returns from a 195-day break
- Deep Cave (hrs_29409646) | 8yo G | 163lb | OR 130 | draw 0 | jockey Adam Wedge | trainer Christian Williams (14d 1/14) | headgear - | last run 20 days | form 0P-679 | MARKET 5.8% | 09:00 median 13.00 | Matchbook 17.00
    DATA: model 6.2% | style Midfield (led 3% of runs) | runs in data 6 | last 3: 9 May Haydock Hurdle 24.3f Good To Soft 6/15; 11 Oct Chepstow Hurdle 23.6f Good To Soft 7/10; 7 Nov Aintree Hurdle 24.5f Good To Soft 9/14 fig 122
    DATA for: Official rating 130, 6 lb above field average
    DATA against: Recent figures 8 lb below its current mark (looks high in the weights); Poor recent finishing positions; Carries 6 lb more than average; Pulled up in 1 of its last 5 jumps runs
- Wonderful Eagle (hrs_30967356) | 7yo G | 161lb | OR 128 | draw 0 | jockey Callum Pritchard | trainer Philip Hobbs & Johnson White (14d 2/17) | headgear p | last run 637 days | form 81331/ | MARKET 5.1% | 09:00 median 16.00 | Matchbook 19.00
    comment: Won last time out and again four starts back, with a pair of thirds in between, but this gelding returns after 637 days off and carries 161 lb.
    DATA: model 5.3% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 637-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Isaac des Obeaux (hrs_32709537) | 8yo G | 169lb | OR 136 | draw 0 | jockey Sam Twiston-Davies | trainer Paul Nicholls (14d 2/22) | headgear - | last run 223 days | form 31214- | MARKET 4.0% | 09:00 median 18.00 | Matchbook 27.00
    comment: Isaac des Obeaux arrives with two wins in his last five starts, a winner two starts back after a second three starts back, and he has run over today's trip. The main risk is a 223-day absence, and he carries 169 lb after a fourth last time out.
    DATA: model 9.8% | style Leader (led 38% of runs) | runs in data 3 | last 3: 15 Jan Wincanton Chase 26.7f Heavy 2/7; 14 Mar Uttoxeter Chase 34f Soft 1/16; 18 Apr Ayr Chase 31.8f Heavy 4/16
    DATA for: Official rating 136, 12 lb above field average; Has won at this trip or further; Good recent finishing positions
    DATA against: Carries 12 lb more than average; Returns from a 223-day break; Race comments mention jumping mistakes in 2 of its last 3 runs; First run over hurdles in our data
- Keable (hrs_29522591) | 9yo G | 164lb | OR 131 | draw 0 | jockey Jack Stenhouse(7) | trainer Philip Hobbs & Johnson White (14d 2/17) | headgear - | last run 258 days | form 13610- | MARKET 4.0% | 09:00 median 19.00 | Matchbook 25.00
    comment: Keable won two starts back and five starts back, but he was unplaced last time out and returns after 258 days off, which raises fitness questions.
    DATA: model 6.7% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 18 Jan Windsor Hurdle 24f Soft 6/15; 21 Feb Chepstow Hurdle 23.6f Soft 1/11; 14 Mar Uttoxeter Hurdle 23.3f Soft 14/17
    DATA for: Official rating 131, 7 lb above field average
    DATA against: Last-run finishing speed -2.7% vs that field (faded); Carries 7 lb more than average; Returns from a 258-day break
- Earth King (hrs_24129364) | 10yo G | 153lb | OR 120 | draw 0 | jockey Jack Tudor | trainer Neil Mulholland (14d 1/12) | headgear p | last run 185 days | form 654-12 | MARKET 2.6% | 09:00 median 26.00 | Matchbook 50.00
    comment: Earth King showed good recent form with a second last time out and a win two starts back, but he returns after 185 days off and carries 153 lb, which is a hard combination to back.
    DATA: model 7.6% | style Held up (led 8% of runs) | runs in data 3 | last 3: 9 Apr Taunton Hurdle 23.9f Good 4/4; 5 May Hereford Hurdle 25.5f Good 1/5; 26 May Plumpton Hurdle 25f Good 2/5
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Returns from a 185-day break
- Inoui Machin (hrs_32709600) | 8yo G | 148lb | OR 115 | draw 0 | jockey Dylan Johnston | trainer Neil Mulholland (14d 1/12) | headgear p | last run 743 days | form 13132/ | MARKET 2.3% | 09:00 median 29.00 | Matchbook 50.00
    comment: Returns after 743 days off, which is a huge hurdle, though Inoui Machin's recent form reads well: a second last time out, a third two starts back, and a winner three starts back.
    DATA: model 4.3% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Carries 9 lb less than average
    DATA against: Official rating 115, 9 lb below field average; Returns from a 743-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Lallygag (hrs_24434564) | 9yo G | 158lb | OR 125 | draw 0 | jockey Jay Tidball(5) | trainer Paul Nicholls (14d 2/22) | headgear tp | wind surgery | last run 30 days | form R112/6 | MARKET 2.0% | 09:00 median 34.00 | Matchbook 60.00
    comment: Lallygag won twice in his last five starts, a first and a first, three and four starts back, then a second two starts back, but he was only sixth last time out, 30 days ago.
    DATA: model 3.5% | style Unknown | runs in data 1 | last 3: 28 Oct Newton Abbot Hurdle 21.5f Good To Soft 6/7
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Moonset (hrs_29522556) | 8yo G | 146lb | OR 113 | draw 0 | jockey Bradley Harris(3) | trainer Neil Mulholland (14d 1/12) | headgear p | last run 36 days | form 1/9P-P | MARKET 1.4% | 09:00 median 41.00 | Matchbook 120.00
    comment: Moonset has been pulled up in his last two starts and was ninth three runs back, so he is hard to fancy, though he did win four starts back and has had 36 days to recover.
    DATA: model 3.2% | style Held up (led 5% of runs) | runs in data 2 | last 3: 26 Feb Wetherby Hurdle 24.1f Soft PU/10; 22 Oct Ffos Las Hurdle 24f Soft PU/8
    DATA for: Carries 11 lb less than average
    DATA against: Official rating 113, 11 lb below field average; Lightly raced: 2 runs in our data, so the model has little to go on; Pulled up in 2 of its last 2 jumps runs
- Blizzard of Oz (hrs_29509879) | 8yo G | 156lb | OR 123 | draw 0 | jockey Harry Kimber | trainer Faye Bramley (14d 1/14) | headgear - | last run 13 days | form P-5800 | MARKET 1.1% | 09:00 median 51.00 | Matchbook 180.00
    comment: The risk is that he carries 156 lb with no recent finish to build on.
    DATA: model 3.0% | style Leader (led 23% of runs) | runs in data 7 | last 3: 28 Jun Uttoxeter Hurdle 23.3f Good 8/10; 24 Oct Cheltenham Hurdle 24f Good 17/19; 14 Nov Cheltenham Hurdle 24f Good 10/10
    DATA against: Last-run finishing speed -6.3% vs that field (faded); Poor recent finishing positions; Pulled up in 1 of its last 5 jumps runs
- Walking On Air (hrs_24194744) | 9yo G | 155lb | OR 122 | draw 0 | jockey Megan Bevan(7) | trainer Gary Brown (14d 0/2) | headgear t | last run 22 days | form 2F-540 | MARKET 0.8% | 09:00 median 81.00 | Matchbook 220.00
    comment: Fit enough after 22 days off, Walking On Air has run over today's trip and was fourth two starts back, with a fifth three starts back, though he was unplaced last time out.
    DATA: model 4.3% | style Prominent (led 4% of runs) | runs in data 7 | last 3: 9 May Haydock Hurdle 24.3f Good To Soft 5/15; 23 May Bangor-on-Dee Chase 24.1f Good 4/7; 5 Nov Newbury Hurdle 24.5f Good To Soft 16/16
    DATA against: Fell or unseated in 1 of its last 5 jumps runs
