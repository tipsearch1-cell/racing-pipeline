# Card review packet: Hexham, 2026-11-18

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
   treat it as one opinion, not the answer); "fig" is a performance figure (higher = better) for that past run;
   "for"/"against" are derived facts (figures vs field, vs mark, pace fit, jumping errors, finishing speed).
4. Runners marked CHECK are the market favourite. Give a verdict, BET or SKIP, with a one-line reason:
   BET unless the card or the DATA lines give a specific reason to doubt the favourite (then lower its chance and SKIP).
   You do not need to do any price arithmetic; the price check (skip line shown) is applied afterwards.

Write valid JSON to the out path you were given, exactly this shape (use the exact race_id and horse_id values):
{"meeting": "hexham", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 12:33 Hexham | race_id rac_32304700454 | British Stallion Studs EBF 'National Hunt' Novices' Hurdle Race (Qualifier) (GBB Race)
Hurdle | Class 4 | 2m48y | going Good To Soft | Turf | 9 runners | rating band - | age 4-6yo
DATA pace: Even - Two likely leaders (Koa Beau, Lord du Gouet). A fair, even gallop is most likely.
- Lord du Gouet (hrs_58963065) | 5yo G | 154lb | OR - | draw 0 | jockey Gavin Sheehan | trainer Jamie Snowden (14d 7/22) | headgear - | last run 28 days | form 13-2 | MARKET 59.1% | 09:00 median 1.40 | Matchbook 1.52
    DATA: model 26.8% | style Leader (led 57% of runs) | runs in data 2 | last 3: 26 Mar Chepstow 16.1f Good To Soft 3/10; 21 Oct Fontwell 19f Soft 2/11 fig 115
    DATA for: Best recent form figure 115, 13 lb above field average; Trainer 32% wins (7/22), last 14 days; Last-run finishing speed +6.6% vs that field (finished strongly); Good recent finishing positions
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Eagle Warrior (hrs_51831766) | 5yo G | 154lb | OR - | draw 0 | jockey Patrick Wadge | trainer Sandy Thomson (14d 3/10) | headgear - | last run 27 days | form /155-2 | MARKET 22.2% | 09:00 median 3.25 | Matchbook 4.60
    DATA: model 12.9% | style Prominent (led 29% of runs) | runs in data 3 | last 3: 14 Mar Newcastle 16.9f Good To Soft 5/12; 20 Apr Kelso 16.2f Good 5/6; 22 Oct Carlisle 17f Good 2/13 fig 116
    DATA for: Best recent form figure 116, 14 lb above field average; Trainer 30% wins (3/10), last 14 days
- Loopy Mag (hrs_17394718761) | 5yo G | 154lb | OR - | draw 0 | jockey Danny McMenamin | trainer Joel Parkinson & Sue Smith (14d 1/13) | headgear - | last run 18 days | form P1-3 | MARKET 7.1% | 09:00 median 9.00 | Matchbook 16.00
    DATA: model 9.7% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 31 Oct Wetherby 16f Good 3/6 fig 103
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Order Driven (hrs_62235768) | 4yo G | 154lb | OR - | draw 0 | jockey Jonathan England | trainer Sam England (14d 5/25) | headgear - | last run 223 days | form 672- | MARKET 5.5% | 09:00 median 12.00 | Matchbook 23.00
    DATA: model 8.7% | style Held up (led 5% of runs) | runs in data 3 | last 3: 5 Mar Haydock 15.7f Good To Soft 6/10; 26 Mar Warwick 16f Good 7/11; 9 Apr Taunton 16.5f Good 2/7
    DATA for: Trainer 20% wins (5/25), last 14 days; Last-run finishing speed +8.6% vs that field (finished strongly)
    DATA against: Returns from a 223-day break; First run over hurdles in our data
- Kingsman Mail (hrs_52056543) | 6yo G | 154lb | OR - | draw 0 | jockey Bruce Lynn | trainer N. W. Alexander (14d 1/15) | headgear - | last run 230 days | form 2330- | MARKET 1.5% | 09:00 median 41.00 | Matchbook 85.00
    DATA: model 11.8% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 13 Jan Ayr 16f Heavy 3/8; 23 Feb Ayr 16f Soft 3/4; 2 Apr Kelso 16.2f Good 10/10
    DATA for: Good recent finishing positions
    DATA against: Last-run finishing speed -6.3% vs that field (faded); Returns from a 230-day break
- Ebchester (hrs_64968071) | 5yo G | 154lb | OR - | draw 0 | jockey Nathan Moscrop | trainer Susan Corbett (14d 0/8) | headgear - | last run 47 days | form 445 | MARKET 1.5% | 09:00 median 41.00 | Matchbook 100.00
    DATA: model 8.9% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 24 May Kelso 16.2f Good 4/6; 13 Jun Hexham 16.2f Good 4/8; 2 Oct Hexham 16.2f Good 5/6
    DATA against: Trainer 0 wins from 8 runs, last 14 days; Last-run finishing speed -3.0% vs that field (faded)
- Koa Beau (hrs_64968085) | 5yo G | 154lb | OR - | draw 0 | jockey Craig Nichol | trainer Ewan Whillans (14d 0/14) | headgear h | last run 22 days | form 38 | MARKET 1.2% | 09:00 median 51.00 | Matchbook 120.00
    DATA: model 8.2% | style Leader (led 38% of runs) | runs in data 2 | last 3: 24 May Kelso 16.2f Good 3/6; 27 Oct Newcastle 17f Good 8/9 fig 91
    DATA against: Best recent form figure 91, 11 lb below field average; Trainer 0 wins from 14 runs, last 14 days; Last-run finishing speed -3.3% vs that field (faded); Lightly raced: 2 runs in our data, so the model has little to go on; First run over hurdles in our data
- Wings of The Glen (hrs_17394666611) | 5yo G | 154lb | OR - | draw 0 | jockey Shane Fitzgerald | trainer Rebecca Menzies (14d 1/10) | headgear - | last run 19 days | form 3 | MARKET 1.1% | 09:00 median 51.00 | Matchbook 130.00
    DATA: model 10.5% | style Held up (led 8% of runs) | runs in data 1 | last 3: 30 Oct Wetherby 19.5f Good 3/5 fig 97
    DATA against: Best recent form figure 97, 5 lb below field average; Lightly raced: 1 run in our data, so the model has little to go on
- Cinnamon Storm (hrs_17394125294) | 4yo F | 147lb | OR - | draw 0 | jockey Sean Quinlan | trainer Lizzie Quinlan (14d 2/10) | headgear t | last run 12 days | form 4-04 | MARKET 0.8% | 09:00 median 81.00 | Matchbook 200.00
    DATA: model 2.6% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 22 Oct Carlisle 17f Good 11/13; 6 Nov Hexham 16f Good 4/4 fig 91
    DATA for: Trainer 20% wins (2/10), last 14 days
    DATA against: Best recent form figure 91, 11 lb below field average; Lightly raced: 2 runs in our data, so the model has little to go on

## 1:03 Hexham | race_id rac_32304702391 | Weatherbys And Birdie Calendars 'Chasing Excellence' Beginners' Steeple Chase (GBB Race)
Chase | Class 3 | 3m41y | going Good To Soft | Turf | 4 runners | rating band - | age 4yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Derryhassen Paddy (hrs_38433563) | 7yo G | 159lb | OR 142 | draw 0 | jockey Derek Fox | trainer Lucinda Russell & Michael Scudamore (14d 9/42) | headgear t | last run 25 days | form 13/2-3 | MARKET 48.6% | 09:00 median 1.83 | Matchbook 1.99
    comment: Derryhassen Paddy has finished third, second, third since a win four starts back, and he's fresh enough after 25 days off, having run over today's trip. The main risk is the 159 lb he must carry off a mark of 142.
    DATA: model 31.6% | style Held up (led 8% of runs) | runs in data 1 | last 3: 24 Oct Cheltenham 25f Good To Soft 3/6 fig 112
    DATA for: Official rating 142, 12 lb above field average; Trainer 21% wins (9/42), last 14 days
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Julius des Pictons (hrs_34525736) | 7yo G | 159lb | OR 135 | draw 0 | jockey Gavin Sheehan | trainer Jamie Snowden (14d 7/22) | headgear - | last run 593 days | form 21131/ | MARKET 31.5% | 09:00 median 2.75 | Matchbook 3.15
    comment: Winner last time out and three wins in his last five starts, with a third two starts back and a second five back, Julius des Pictons has strong recent form and has run over today's trip and going before.
    DATA: model 22.1% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Official rating 135, 5 lb above field average; Trainer 32% wins (7/22), last 14 days
    DATA against: Returns from a 593-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Fishery Lane (hrs_34598095) | 7yo G | 159lb | OR 131 | draw 0 | jockey Tristan Durrell | trainer Dan Skelton (14d 19/80) | headgear - | wind surgery | last run 200 days | form 324F2- | MARKET 18.0% | 09:00 median 4.50 | Matchbook 5.80
    comment: Fishery Lane was second last time out and has made the frame in three of his last five, with a fourth and a fall in between, and he has run over today's trip.
    DATA: model 30.1% | style Prominent (led 3% of runs) | runs in data 5 | last 3: 2 Mar Leopardstown 21.5f Soft To Heavy 4/16; 29 Mar Downpatrick 28.5f Yielding To Soft F/15; 2 May Punchestown 31.3f Yielding 2/19
    DATA for: Trainer 24% wins (19/80), last 14 days
    DATA against: Returns from a 200-day break; Race comments mention jumping mistakes in 2 of its last 5 runs; Fell or unseated in 1 of its last 5 jumps runs
- Pinot Rouge (hrs_29522815) | 8yo M | 152lb | OR 112 | draw 0 | jockey Conor Rabbitt(3) | trainer Jessica Bedi (14d 0/5) | headgear tb | last run 108 days | form F3-72P | MARKET 1.9% | 09:00 median 41.00 | Matchbook 65.00
    comment: The main risk is a 108-day absence and a pulled up last time out under 152 lb.
    DATA: model 16.2% | style Midfield (led 3% of runs) | runs in data 7 | last 3: 23 May Cartmel 25.4f Good 7/7; 13 Jun Hexham 23.3f Good 2/8; 2 Aug Galway 24.3f Good PU/18
    DATA against: Official rating 112, 18 lb below field average; Returns from a 108-day break; Fell or unseated in 1 of its last 5 jumps runs; Pulled up in 1 of its last 5 jumps runs

## 1:33 Hexham | race_id rac_32305037492 | Paul Ferguson's Jumpers To Follow Handicap Hurdle Race (Div I)
Hurdle | Class 5 | 2m4f28y | going Good To Soft | Turf | 10 runners | rating band 0-100 | age 3yo+
DATA pace: Strong pace - 3 habitual front-runners (De Deli Counter, Monsieur Le Fuzz, Wind Your Neck In). A contested lead should set things up for horses coming from behind.
- De Deli Counter (hrs_53147948) | 5yo G | 168lb | OR 100 | draw 0 | jockey Jamie Hamilton | trainer Mark Walford (14d 2/14) | headgear p | last run 12 days | form 31-661 | MARKET 25.1% | 09:00 median 3.50 | Matchbook 3.70 | CHECK (skip line 3.32)
    comment: De Deli Counter won last time out just 12 days ago and has won twice in his last five starts, a first and a third among those finishes, so he arrives fit and in form. He has run over today's trip and going before, though 168 lb is a hefty burden.
    DATA: model 15.5% | style Leader (led 79% of runs) | runs in data 8 | last 3: 8 May Market Rasen 20.6f Good 6/7; 18 Oct Sedgefield 20f Good 6/8 fig 90; 6 Nov Hexham 23.5f Good 1/10 fig 98
    DATA for: Best recent form figure 98, 8 lb above field average; Official rating 100, 14 lb above field average; Last-run finishing speed +2.7% vs that field (finished strongly); Has won at this trip or further
    DATA against: Carries 13 lb more than average; Pace: likely to be taken on for the lead
- Takeyoutotheisland (hrs_58596699) | 6yo G | 151lb | OR 83 | draw 0 | jockey Bruce Lynn | trainer N. W. Alexander (14d 1/15) | headgear - | last run 189 days | form 4977-2 | MARKET 14.8% | 09:00 median 5.50 | Matchbook 6.80
    comment: Runner-up last time out, he's otherwise been held in recent starts (seventh twice, a ninth and a fourth), and he's winless in his last five after a 189-day break.
    DATA: model 12.2% | style Midfield (led 3% of runs) | runs in data 4 | last 3: 3 Feb Carlisle 17f Good To Soft 7/12; 4 Apr Carlisle 19.3f Good 7/9; 13 May Perth 20.2f Good To Soft 2/9
    DATA for: Last-run finishing speed +3.9% vs that field (finished strongly)
    DATA against: Returns from a 189-day break
- Monsieur Le Fuzz (hrs_34788817) | 7yo G | 163lb | OR 95 | draw 0 | jockey Charlie Maggs | trainer Rebecca Menzies (14d 1/10) | headgear t | last run 210 days | form 6028P- | MARKET 13.1% | 09:00 median 6.50 | Matchbook 7.20
    DATA: model 12.4% | style Prominent (led 43% of runs) | runs in data 4 | last 3: 24 Feb Catterick 25.3f Good To Soft 2/9; 20 Mar Musselburgh 23.8f Good To Soft 8/13; 22 Apr Perth 23.9f Good PU/10
    DATA for: Official rating 95, 9 lb above field average
    DATA against: Carries 8 lb more than average; Returns from a 210-day break; Pulled up in 1 of its last 4 jumps runs
- Fearless Dragon (hrs_49757603) | 5yo G | 161lb | OR 93 | draw 0 | jockey Brian Hughes | trainer Patrick Neville (14d 1/2) | headgear p | last run 34 days | form 53UP-4 | MARKET 12.9% | 09:00 median 6.50 | Matchbook 7.60
    comment: Fearless Dragon returned a fourth last time out, a better effort after a pulled up and an unseated in the two runs before, though he is winless in his last five and has a third four starts back as his best finish.
    DATA: model 7.6% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 10 Mar Sedgefield 16.8f Good UR/7; 1 Apr Sedgefield 19.9f Good PU/6; 15 Oct Perth 20f Soft 4/8 fig 92
    DATA for: Official rating 93, 7 lb above field average
    DATA against: Carries 6 lb more than average; Fell or unseated in 1 of its last 5 jumps runs; Pulled up in 1 of its last 5 jumps runs
- Wind Your Neck In (hrs_26473223) | 7yo G | 163lb | OR 95 | draw 0 | jockey Jonathan England | trainer Sam England (14d 5/25) | headgear t | last run 20 days | form 2215-6 | MARKET 12.7% | 09:00 median 6.50 | Matchbook 7.60
    comment: The main risk is that he's been beaten in his last two, a fifth then a sixth, and carries 163 lb.
    DATA: model 13.0% | style Leader (led 38% of runs) | runs in data 8 | last 3: 10 Mar Sedgefield 19.9f Good 1/7; 4 Apr Carlisle 19.3f Good 5/7; 29 Oct Stratford 18.5f Good To Soft 6/11 fig 90
    DATA for: Official rating 95, 9 lb above field average; Trainer 20% wins (5/25), last 14 days; Has won at this trip or further
    DATA against: Carries 8 lb more than average; Pace: likely to be taken on for the lead
- Pure Sirloin (hrs_28838222) | 8yo G | 159lb | OR 91 | draw 0 | jockey Harry Reed | trainer Sandy Forster (14d 0/1) | headgear p | last run 238 days | form P3673- | MARKET 9.2% | 09:00 median 9.00 | Matchbook 11.00
    comment: The big risk is 238 days off the track, with 159 lb to carry.
    DATA: model 10.6% | style Held up (led 5% of runs) | runs in data 2 | last 3: 29 Jan Ayr 24.3f Soft 7/13; 25 Mar Hexham 20.1f Soft 3/14
    DATA for: Last-run finishing speed +3.6% vs that field (finished strongly); Pace: a contested lead should suit its hold-up style
    DATA against: Returns from a 238-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- Lewa House (hrs_23558521) | 10yo G | 142lb | OR 69 | draw 0 | jockey Dominic Hislop(7) | trainer Catch Bissett (14d 0/2) | headgear tv | last run 18 days | form 606P-8 | MARKET 5.5% | 09:00 median 13.00 | Matchbook 20.00
    comment: Lewa House is hard to fancy, having finished eighth last time out and pulled up two starts back, and he is winless in his last five outings.
    DATA: model 6.4% | style Midfield (led 3% of runs) | runs in data 4 | last 3: 10 Feb Ayr 20.5f Soft 6/9; 25 Mar Hexham 24.2f Soft PU/10; 31 Oct Ayr 24f Good To Soft 8/11
    DATA for: Carries 13 lb less than average
    DATA against: Official rating 69, 17 lb below field average; Poor recent finishing positions; Pulled up in 1 of its last 4 jumps runs
- Prince Nino (hrs_23952992) | 9yo G | 147lb | OR 79 | draw 0 | jockey Sean Quinlan | trainer Lizzie Quinlan (14d 2/10) | headgear tp | last run 55 days | form /8-18P | MARKET 2.9% | 09:00 median 29.00 | Matchbook 36.00
    comment: Prince Nino was pulled up last time out and was eighth the run before, so he's hard to fancy after 55 days off, though he did win three starts back and has run over today's trip and going.
    DATA: model 7.9% | style Prominent (led 4% of runs) | runs in data 3 | last 3: 13 May Perth 20.2f Good To Soft 1/9; 2 Jul Perth 23.9f Good 8/10; 24 Sep Perth 20.2f Good PU/12
    DATA for: Trainer 20% wins (2/10), last 14 days; Has won at this trip or further; Carries 8 lb less than average
    DATA against: Official rating 79, 7 lb below field average; Pulled up in 1 of its last 3 jumps runs
- Jedhi Knight (hrs_50339793) | 4yo G | 154lb | OR 87 | draw 0 | jockey Tom Midgley(3) | trainer Paul Midgley (14d 0/4) | headgear - | last run 29 days | form 378-9 | MARKET 2.7% | 09:00 median 34.00 | Matchbook 36.00
    comment: Jedhi Knight has slipped from a third four starts back to a ninth last time out, and he is winless in his last four, though 29 days' rest and prior experience on today's going help.
    DATA: model 8.0% | style Held up (led 3% of runs) | runs in data 8 | last 3: 20 Aug Newcastle 12.4f Standard 4/12; 30 Aug Beverley 16.1f Heavy 4/7; 20 Oct Hexham 16f Good 9/10 fig 78
    DATA for: Pace: a contested lead should suit its hold-up style
    DATA against: Best recent form figure 78, 12 lb below field average; Recent figures 9 lb below its current mark (looks high in the weights); Race comments mention jumping mistakes in 2 of its last 3 runs
- Solway Primrose (hrs_23119810) | 12yo M | 142lb | OR 72 | draw 0 | jockey Peter Kavanagh | trainer Lisa Harrison (14d 0/3) | headgear - | wind surgery | last run 343 days | form 5/PPP- | MARKET 1.0% | 09:00 median 81.00 | Matchbook 120.00
    comment: Solway Primrose is hard to fancy, having been pulled up in each of her last three starts, with a fifth four starts back her only completed effort, and she returns after 343 days off.
    DATA: model 6.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Carries 13 lb less than average
    DATA against: Official rating 72, 14 lb below field average; Returns from a 343-day break; Lightly raced: 0 runs in our data, so the model has little to go on; Aged 12, older than most of this field

## 2:08 Hexham | race_id rac_32304704328 | Paul Ferguson's Jumpers To Follow Handicap Hurdle Race (Div II)
Hurdle | Class 5 | 2m4f28y | going Good To Soft | Turf | 10 runners | rating band 0-100 | age 3yo+
DATA pace: Even - Two likely leaders (Wise Move, Dante's Inferno). A fair, even gallop is most likely.
- Ratemenow (hrs_50402429) | 5yo G | 168lb | OR 97 | draw 0 | jockey Nathan Moscrop | trainer Susan Corbett (14d 0/8) | headgear t | wind surgery | last run 41 days | form 4562-2 | MARKET 21.6% | 09:00 median 3.50 | Matchbook 4.70 | CHECK (skip line 3.32)
    comment: Ratemenow arrives bang in form with a second last time out and another second two starts back, and he has run over today's trip and going before. The main risk is that he is yet to win in his last five, and 168 lb is a hefty burden after 41 days off.
    DATA: model 23.3% | style Midfield (led 29% of runs) | runs in data 5 | last 3: 13 Feb Kelso 16.2f Heavy 6/11; 14 Mar Newcastle 20.3f Good To Soft 2/15; 8 Oct Market Rasen 20.6f Good 2/5
    DATA for: Official rating 97, 10 lb above field average; Last-run finishing speed +3.0% vs that field (finished strongly); Good recent finishing positions
    DATA against: Trainer 0 wins from 8 runs, last 14 days; Carries 10 lb more than average
- Je Mr Dawson (hrs_50433208) | 7yo G | 163lb | OR 92 | draw 0 | jockey Ryan Mania | trainer Adam Nicol (14d 1/8) | headgear - | last run 228 days | form /7655- | MARKET 18.6% | 09:00 median 4.33 | Matchbook 5.10
    comment: Fifth last time out and a fifth two starts back suggest Je Mr Dawson is running respectably, and he has run over today's trip, but he is winless in his last four and returns after 228 days off.
    DATA: model 5.6% | style Held up (led 5% of runs) | runs in data 2 | last 3: 22 Jan Wetherby 16f Soft 5/12; 4 Apr Carlisle 19.3f Good 5/9
    DATA for: Official rating 92, 5 lb above field average
    DATA against: Carries 5 lb more than average; Returns from a 228-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- Dante's Inferno (hrs_37505223) | 7yo G | 153lb | OR 82 | draw 0 | jockey David Noonan | trainer Tony Culhane & Stella Barclay (14d 0/5) | headgear p | last run 16 days | form 762UU3 | MARKET 12.4% | 09:00 median 6.50 | Matchbook 7.80
    DATA: model 12.4% | style Leader (led 29% of runs) | runs in data 6 | last 3: 2 Oct Hexham 20.1f Good UR/6; 13 Oct Southwell 20.4f Good UR/11; 2 Nov Southwell 20.5f Good 3/11 fig 80
    DATA for: Last-run finishing speed +2.2% vs that field (finished strongly)
    DATA against: Fell or unseated in 2 of its last 5 jumps runs
- Shadow Chaser (hrs_34860210) | 7yo G | 167lb | OR 96 | draw 0 | jockey Jamie Hamilton | trainer Mark Walford (14d 2/14) | headgear - | last run 288 days | form 27720- | MARKET 11.2% | 09:00 median 7.50 | Matchbook 8.60
    comment: The main risk is that a break that long leaves him short of full fitness after an unplaced latest effort.
    DATA: model 21.4% | style Prominent (led 4% of runs) | runs in data 3 | last 3: 2 Jan Ayr 20.5f Soft 7/19; 15 Jan Newcastle 23.4f Good To Soft 2/11; 3 Feb Carlisle 24.5f Good To Soft 10/14
    DATA for: Official rating 96, 9 lb above field average
    DATA against: Last-run finishing speed -6.5% vs that field (faded); Carries 9 lb more than average; Returns from a 288-day break
- Jeepydoff Meel (hrs_29523151) | 8yo G | 143lb | OR 72 | draw 0 | jockey Oscar Palmer(7) | trainer Lisa Harrison (14d 0/3) | headgear - | last run 19 days | form 849-R4 | MARKET 10.8% | 09:00 median 8.00 | Matchbook 8.60
    comment: Jeepydoff Meel is hard to fancy, winless in his last five with a refusal two starts back and a ninth three starts back, though he was fourth last time out, 19 days ago.
    DATA: model 5.3% | style Midfield (led 8% of runs) | runs in data 2 | last 3: 29 Aug Cartmel 17.2f Good RR/11; 30 Oct Uttoxeter 16f Good 4/10 fig 68
    DATA for: Carries 15 lb less than average
    DATA against: Best recent form figure 68, 10 lb below field average; Official rating 72, 15 lb below field average; Lightly raced: 2 runs in our data, so the model has little to go on
- Pepite de Saphir (hrs_38579338) | 6yo M | 158lb | OR 87 | draw 0 | jockey Shane Fitzgerald | trainer Rebecca Menzies (14d 1/10) | headgear ht (1st time) | last run 16 days | form 2/P4P3 | MARKET 7.5% | 09:00 median 11.50 | Matchbook 13.50
    comment: Pepite de Saphir returned a third last time out just 16 days ago, and she has run over today's trip and going before, though she is yet to win in her last five.
    DATA: model 8.0% | style Midfield (led 29% of runs) | runs in data 4 | last 3: 4 Jun Uttoxeter 19.9f Good 4/7; 28 Aug Sedgefield 19.9f Good PU/9; 2 Nov Southwell 24.5f Good 3/8 fig 85
    DATA for: Best recent form figure 85, 7 lb above field average; First-time headgear
    DATA against: Race comments mention jumping mistakes in 2 of its last 4 runs; Pulled up in 2 of its last 4 jumps runs
- Fourofakind (hrs_27140015) | 7yo G | 164lb | OR 93 | draw 0 | jockey Sean Quinlan | trainer Lizzie Quinlan (14d 2/10) | headgear v | last run 27 days | form 6P7-57 | MARKET 6.8% | 09:00 median 13.00 | Matchbook 13.50
    comment: Fourofakind has been without a win in his last five starts, with a seventh last time out and a fifth two starts back, but he has run over today's trip and going and 27 days off suits.
    DATA: model 10.9% | style Prominent (led 5% of runs) | runs in data 3 | last 3: 22 Mar Carlisle 19.3f Good To Soft 7/10; 20 Jul Cartmel 22.1f Good 5/9; 22 Oct Carlisle 20f Good 7/13
    DATA for: Official rating 93, 6 lb above field average; Trainer 20% wins (2/10), last 14 days
    DATA against: Carries 6 lb more than average
- Wise Move (hrs_30123065) | 8yo G | 157lb | OR 86 | draw 0 | jockey Jonathon Bewley | trainer George Bewley (14d 0/8) | headgear h | last run 12 days | form 54PP-P | MARKET 6.2% | 09:00 median 13.00 | Matchbook 16.00
    comment: Wise Move has been pulled up in each of his last three starts after a fourth and a fifth before that, so form is a worry, though he is back quickly after 12 days and has run over today's trip and going.
    DATA: model 8.9% | style Prominent (led 43% of runs) | runs in data 5 | last 3: 25 Mar Hexham 20.1f Soft PU/13; 13 Apr Hexham 20.1f Good PU/9; 6 Nov Hexham 24f Good PU/7
    DATA against: Trainer 0 wins from 8 runs, last 14 days; Poor recent finishing positions; Pulled up in 3 of its last 5 jumps runs
- Khaleesi Queen (hrs_58535267) | 6yo M | 157lb | OR 86 | draw 0 | jockey Joshua Thompson(5) | trainer Micky Hammond (14d 0/19) | headgear h | last run 246 days | form 09955- | MARKET 3.5% | 09:00 median 23.00 | Matchbook 29.00
    comment: Khaleesi Queen is winless in her recent form, with a fifth last time out, a fifth two starts back and two ninths before that, and she returns after 246 days off.
    DATA: model 2.4% | style Held up (led 5% of runs) | runs in data 4 | last 3: 16 Feb Carlisle 17f Good To Soft 9/10; 3 Mar Newcastle 20.3f Good To Soft 5/12; 17 Mar Wetherby 19.7f Good To Soft 5/6
    DATA against: Trainer 0 wins from 19 runs, last 14 days; Last-run finishing speed -5.2% vs that field (faded); Returns from a 246-day break
- George's Angel (hrs_52496276) | 5yo M | 149lb | OR 78 | draw 0 | jockey Danny McMenamin | trainer R K Watson (14d 0/1) | headgear h (1st time) | last run 44 days | form 077-0P | MARKET 1.4% | 09:00 median 41.00 | Matchbook 120.00
    comment: George's Angel was pulled up last time out and has been without a win in her last five starts, with a seventh three starts back her best recent finish, so she is hard to pin down. Off 44 days and carrying 149 lb, she is lightly raced enough to leave room for improvement.
    DATA: model 1.8% | style Held up (led 5% of runs) | runs in data 2 | last 3: 13 Jun Downpatrick 21.8f Good 11/13; 5 Oct Fairyhouse 16f Good PU/16
    DATA for: Carries 9 lb less than average; First-time headgear
    DATA against: Official rating 78, 9 lb below field average; Lightly raced: 2 runs in our data, so the model has little to go on; Pulled up in 1 of its last 2 jumps runs

## 2:38 Hexham | race_id rac_32304706265 | B K Racing Long Distance Handicap Steeple Chase (Go North Red Rum Series Qualifier) (GBB Race)
Chase | Class 4 | 3m7f199y | going Good To Soft | Turf | 7 runners | rating band 0-120 | age 4yo+
DATA pace: Lone leader - Wal Buck's is the only habitual front-runner and may be allowed an easy lead.
- Wal Buck's (hrs_34253198) | 7yo G | 161lb | OR 113 | draw 0 | jockey Derek Fox | trainer Lucinda Russell & Michael Scudamore (14d 9/42) | headgear v | last run 39 days | form 2144-2 | MARKET 22.8% | 09:00 median 3.75 | Matchbook 4.40 | CHECK (skip line 3.56)
    comment: The main risk is the 161 lb he carries after 39 days off.
    DATA: model 17.6% | style Leader (led 83% of runs) | runs in data 5 | last 3: 5 Mar Haydock 28.4f Good To Soft 4/5; 25 Mar Hexham 31.9f Soft 4/11; 10 Oct Hexham 24.2f Good 2/9
    DATA for: Official rating 113, 10 lb above field average; Trainer 21% wins (9/42), last 14 days; Pace: may get an uncontested lead
    DATA against: Carries 8 lb more than average
- President Scottie (hrs_32598475) | 8yo G | 155lb | OR 107 | draw 0 | jockey Danny McMenamin | trainer Nicky Richards (14d 5/22) | headgear p | last run 13 days | form 6653-6 | MARKET 22.2% | 09:00 median 4.00 | Matchbook 4.20
    comment: Fit after 13 days off, President Scottie has run over today's trip and on this going, and his third two starts back is the pick of a steady recent profile.
    DATA: model 14.8% | style Midfield (led 23% of runs) | runs in data 5 | last 3: 22 Mar Carlisle 24.5f Good To Soft 5/12; 24 Apr Perth 30.6f Good 3/11; 5 Nov Newcastle 24f Good 6/8 fig 102
    DATA for: Best recent form figure 102, 12 lb above field average; Trainer 23% wins (5/22), last 14 days
- Defence Witness (hrs_35321951) | 7yo G | 144lb | OR 96 | draw 0 | jockey Jonathan England | trainer Sam England (14d 5/25) | headgear tp | last run 12 days | form 72-671 | MARKET 19.4% | 09:00 median 4.50 | Matchbook 5.00
    comment: Won last time out just 12 days ago, which is a plus, but that came after a seventh, a sixth and a second in his previous three runs, so consistency is a question.
    DATA: model 13.9% | style Held up (led 3% of runs) | runs in data 8 | last 3: 23 May Cartmel 25.5f Good 6/9; 20 Oct Hexham 24f Good 7/8 fig 86; 6 Nov Hexham 24f Good 1/7 fig 93
    DATA for: Trainer 20% wins (5/25), last 14 days; Last-run finishing speed +2.4% vs that field (finished strongly); Carries 9 lb less than average
    DATA against: Official rating 96, 7 lb below field average; Race comments mention jumping mistakes in 2 of its last 5 runs
- Betterforeveryone (hrs_29257921) | 9yo G | 160lb | OR 112 | draw 0 | jockey Tom Bellamy | trainer Alan King (14d 3/18) | headgear p | last run 193 days | form /14P-3 | MARKET 13.2% | 09:00 median 6.50 | Matchbook 7.60
    DATA: model 17.0% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 25 Feb Bangor-on-Dee 29.6f Soft PU/11; 9 May Hexham 24.2f Good To Soft 3/8
    DATA for: Official rating 112, 9 lb above field average; Last-run finishing speed +2.6% vs that field (finished strongly)
    DATA against: Carries 7 lb more than average; Returns from a 193-day break; Lightly raced: 2 runs in our data, so the model has little to go on; Pulled up in 1 of its last 2 jumps runs
- Rob Roy Macgregor (hrs_32751124) | 8yo G | 142lb | OR 83 | draw 0 | jockey Charlie Maggs | trainer Sandy Thomson (14d 3/10) | headgear p | last run 18 days | form 423-54 | MARKET 11.4% | 09:00 median 8.00 | Matchbook 8.20
    comment: Winless in his last five, Rob Roy Macgregor has been consistent without cracking it, finishing fourth last time out, a fifth before that, and a second four starts back.
    DATA: model 16.8% | style Midfield (led 3% of runs) | runs in data 6 | last 3: 25 Mar Hexham 31.9f Soft 3/11; 2 May Hexham 24.2f Good 5/13; 31 Oct Ayr 24f Good To Soft 4/11 fig 81
    DATA for: Trainer 30% wins (3/10), last 14 days; Carries 11 lb less than average
    DATA against: Best recent form figure 81, 9 lb below field average; Official rating 83, 20 lb below field average
- Torosay (hrs_32415614) | 8yo M | 142lb | OR 93 | draw 0 | jockey Patrick Wadge | trainer Lucinda Russell & Michael Scudamore (14d 9/42) | headgear p | last run 18 days | form 7422-7 | MARKET 9.6% | 09:00 median 9.00 | Matchbook 10.50
    comment: She has run on today's going and returns after 18 days, but 142 lb off 93 is a big ask.
    DATA: model 16.6% | style Held up (led 3% of runs) | runs in data 4 | last 3: 10 Feb Ayr 24.1f Soft 2/11; 6 Mar Ayr 24.1f Soft 2/6; 31 Oct Ayr 24f Good To Soft 7/11 fig 85
    DATA for: Trainer 21% wins (9/42), last 14 days; Good recent finishing positions; Carries 11 lb less than average
    DATA against: Best recent form figure 85, 5 lb below field average; Recent figures 8 lb below its current mark (looks high in the weights); Official rating 93, 10 lb below field average
- Clodders Dream (hrs_29409387) | 8yo G | 165lb | OR 117 | draw 0 | jockey Freddie Mitchell(3) | trainer Max Comley (14d 2/7) | headgear p | wind surgery | last run 17 days | form PPP0-P | MARKET 1.5% | 09:00 median 51.00 | Matchbook 80.00
    comment: Back after 17 days, he has run on today's going before, and his 118 rating sits a pound above his official 117.
    DATA: model 3.3% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 1 Nov Worcester 20f Good To Soft PU/13
    DATA for: Official rating 117, 14 lb above field average; Trainer 29% wins (2/7), last 14 days
    DATA against: Carries 12 lb more than average; Lightly raced: 1 run in our data, so the model has little to go on; Pulled up in 1 of its last 1 jumps runs

## 3:08 Hexham | race_id rac_32304708202 | QuinnBet Handicap Steeple Chase
Chase | Class 5 | 2m4f15y | going Good To Soft | Turf | 12 runners | rating band 0-100 | age 4yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Kinbara Firstdraft (hrs_34373773) | 7yo G | 154lb | OR 86 | draw 0 | jockey Derek Fox | trainer Leonard Kerr (14d 0/3) | headgear tp | last run 7 days | form 952P52 | MARKET 16.9% | 09:00 median 4.50 | Matchbook 5.60 | CHECK (skip line 4.27)
    comment: Kinbara Firstdraft arrives fresh from a second last time out just seven days ago, and he has run over today's trip and going, but he is yet to win in his last six starts. Carrying 154 lb off 86 and pulled up three starts back, he looks more solid than spectacular.
    DATA: model 6.1% | style Held up (led 3% of runs) | runs in data 14 | last 3: 18 Oct Sedgefield 21f Good PU/7; 5 Nov Newcastle 20f Good 5/9 fig 82; 11 Nov Ayr 19.5f Good 2/10 fig 97
    DATA for: Recent figures 11 lb above its current mark (looks well handicapped); Last-run finishing speed +3.4% vs that field (finished strongly)
    DATA against: Pulled up in 1 of its last 5 jumps runs; Pace: steady gallop likely, hard to come from off the pace
- Scairp Dubh (hrs_51618609) | 6yo G | 167lb | OR 99 | draw 0 | jockey Jack Power(5) | trainer Joel Parkinson & Sue Smith (14d 1/13) | headgear p | last run 183 days | form 120-13 | MARKET 13.4% | 09:00 median 6.00 | Matchbook 7.00
    DATA: model 14.1% | style Midfield (led 3% of runs) | runs in data 6 | last 3: 20 Mar Musselburgh 23.8f Good To Soft 11/13; 2 May Hexham 20.1f Good 1/13; 19 May Hexham 20.1f Good 3/6
    DATA for: Official rating 99, 10 lb above field average; Has won at this trip or further; Good recent finishing positions
    DATA against: Carries 10 lb more than average; Returns from a 183-day break
- Drop Kick (hrs_50188397) | 5yo G | 162lb | OR 94 | draw 0 | jockey Jamie Hamilton | trainer Mark Walford (14d 2/14) | headgear - | last run 27 days | form 3238-4 | MARKET 13.0% | 09:00 median 6.00 | Matchbook 7.20
    comment: Fourth last time out and a second and two thirds in his last five, Drop Kick is consistent but yet to win, and he has run over today's trip and going after 27 days off.
    DATA: model 16.6% | style Midfield (led 3% of runs) | runs in data 4 | last 3: 21 Feb Newcastle 20.3f Good To Soft 3/15; 25 Mar Hexham 20.1f Soft 8/14; 22 Oct Carlisle 20f Good 4/13 fig 88
    DATA against: Best recent form figure 88, 6 lb below field average; Recent figures 6 lb below its current mark (looks high in the weights); First run over fences in our data
- King of Cong (hrs_38433437) | 8yo G | 146lb | OR 78 | draw 0 | jockey Charlie Maggs | trainer Patrick Morris (14d 0/8) | headgear p | last run 186 days | form 30PP-P | MARKET 11.6% | 09:00 median 7.10 | Matchbook 8.00
    comment: King of Cong has been pulled up in each of his last three starts and returns after 186 days off, which is a concern, though a third five starts back shows he can run well, and he has run over today's trip and going.
    DATA: model 6.6% | style Prominent (led 4% of runs) | runs in data 3 | last 3: 25 Mar Hexham 24.2f Soft PU/10; 13 Apr Hexham 24.2f Good PU/14; 16 May Uttoxeter 20.9f Good PU/10
    DATA for: Carries 12 lb less than average
    DATA against: Official rating 78, 12 lb below field average; Trainer 0 wins from 8 runs, last 14 days; Poor recent finishing positions; Returns from a 186-day break; Pulled up in 3 of its last 3 jumps runs
- Monochromix (hrs_32653775) | 8yo G | 163lb | OR 95 | draw 0 | jockey Patrick Wadge | trainer Lucinda Russell & Michael Scudamore (14d 9/42) | headgear - | last run 18 days | form 6/54-7 | MARKET 10.2% | 09:00 median 7.50 | Matchbook 9.40
    comment: Monochromix is without a win in his last four, but he has fair efforts in a fourth two starts back and a fifth three starts back, and he's fresh enough after 18 days off.
    DATA: model 7.9% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 31 Oct Ayr 20.5f Good To Soft 7/10 fig 94
    DATA for: Official rating 95, 6 lb above field average; Trainer 21% wins (9/42), last 14 days
    DATA against: Carries 6 lb more than average; Lightly raced: 1 run in our data, so the model has little to go on
- Halpha Soleil (hrs_24616606) | 9yo G | 168lb | OR 100 | draw 0 | jockey Conor O'Farrell | trainer Micky Hammond (14d 0/19) | headgear p | last run 13 days | form 535-22 | MARKET 9.8% | 09:00 median 8.00 | Matchbook 9.60
    comment: Halpha Soleil comes here in good heart, second last time out and again two starts back, and he has run over today's trip and on this going before. Only 13 days since his last run keeps him fit, but he is yet to win in his last five starts and carries 168 lb.
    DATA: model 11.4% | style Midfield (led 5% of runs) | runs in data 4 | last 3: 19 Feb Sedgefield 21.1f Soft 5/5; 6 Jun Hexham 20.1f Good 2/9; 5 Nov Newcastle 20f Good 2/5 fig 96
    DATA for: Official rating 100, 10 lb above field average; Good recent finishing positions
    DATA against: Trainer 0 wins from 19 runs, last 14 days; Carries 10 lb more than average
- Yapper Hill (hrs_35430710) | 7yo G | 151lb | OR 83 | draw 0 | jockey Jonathon Bewley | trainer George Bewley (14d 0/8) | headgear - | last run 228 days | form R7493- | MARKET 6.7% | 09:00 median 11.00 | Matchbook 15.00
    comment: Yapper Hill is winless in his last five and returns after 228 days off, which makes him hard to fancy, though a third last time out and prior experience over today's trip and going offer some hope.
    DATA: model 8.1% | style Midfield (led 5% of runs) | runs in data 3 | last 3: 26 Feb Wetherby 16f Soft 4/8; 25 Mar Hexham 20.1f Soft 9/14; 4 Apr Carlisle 19.3f Good 3/4
    DATA for: Carries 6 lb less than average
    DATA against: Official rating 83, 6 lb below field average; Trainer 0 wins from 8 runs, last 14 days; Returns from a 228-day break; First run over fences in our data
- Colonel Jack (hrs_59367266) | 5yo G | 168lb | OR 100 | draw 0 | jockey Danny McMenamin | trainer Mark Walford (14d 2/14) | headgear t | last run 12 days | form PP4-P | MARKET 4.6% | 09:00 median 17.00 | Matchbook 21.00
    comment: Colonel Jack has been pulled up in three of his last four, which is the clear risk, but he's back quickly after 12 days, has run over today's trip and ran a fourth two starts back.
    DATA: model 4.6% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 15 Jan Newcastle 20.3f Good To Soft PU/16; 25 Mar Hexham 20.1f Soft 4/13; 6 Nov Hexham 20f Good PU/9
    DATA for: Official rating 100, 10 lb above field average
    DATA against: Carries 10 lb more than average; Pulled up in 2 of its last 3 jumps runs; First run over fences in our data
- Dr Shirocco (hrs_21395360) | 11yo G | 143lb | OR 75 | draw 0 | jockey Harry Reed | trainer Sandy Forster (14d 0/1) | headgear - | last run 158 days | form 46-344 | MARKET 4.1% | 09:00 median 15.00 | Matchbook 29.00
    comment: Without a win in his last five and off a 158-day break, Dr Shirocco is hard to fancy, though he's been fourth in his last two and third three starts back, and has run over today's trip and going.
    DATA: model 8.5% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 2 May Hexham 24.2f Good 3/13; 19 May Hexham 24.2f Good 4/6; 13 Jun Hexham 24.2f Good 4/7
    DATA for: Carries 14 lb less than average
    DATA against: Official rating 75, 14 lb below field average; Returns from a 158-day break; Aged 11, older than most of this field
- Order Another One (hrs_50667316) | 5yo M | 148lb | OR 80 | draw 0 | jockey Peter Kavanagh | trainer Dianne Sayer (14d 0/4) | headgear - | last run 27 days | form 175436 | MARKET 3.6% | 09:00 median 21.00 | Matchbook 29.00
    comment: Order Another One has slipped from a third two starts back to a sixth last time out, and her only win in her last six starts came six starts back, so she is hard to fancy at 148 lb.
    DATA: model 7.2% | style Held up (led 3% of runs) | runs in data 5 | last 3: 20 Jul Cartmel 17.2f Good 4/8; 2 Oct Hexham 20.1f Good 3/6; 22 Oct Carlisle 20f Good 6/13
    DATA for: Carries 10 lb less than average
    DATA against: Official rating 80, 10 lb below field average; First run over fences in our data; Pace: steady gallop likely, hard to come from off the pace
- Stretchemout (hrs_40920026) | 6yo M | 162lb | OR 94 | draw 0 | jockey Brian Hughes | trainer R K Watson (14d 0/1) | headgear tp | last run 18 days | form 7P-0P5 | MARKET 3.3% | 09:00 median 19.00 | Matchbook 40.00
    DATA: model 1.4% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 2 Jul Limerick 22.5f Good 14/18; 17 Jul Killarney 23f Good PU/15; 31 Oct Down Royal (IRE) 19.5f Good 5/5 fig 96
    DATA against: Pulled up in 1 of its last 3 jumps runs
- Cowboy Cooper (hrs_27578929) | 10yo G | 158lb | OR 90 | draw 0 | jockey Craig Nichol | trainer Donald Whillans (14d 0/3) | headgear - | last run 230 days | form 31P46- | MARKET 2.8% | 09:00 median 29.00 | Matchbook 34.00
    comment: Cowboy Cooper returns after 230 days off, having finished sixth last time out and pulled up three starts back, so he is hard to fancy under 158 lb. In his favour, he won four starts back and has run over today's trip and on this going before.
    DATA: model 7.4% | style Prominent (led 3% of runs) | runs in data 4 | last 3: 10 Feb Ayr 24.1f Soft PU/11; 3 Mar Newcastle 23.4f Good To Soft 4/8; 2 Apr Kelso 23.4f Good 6/8
    DATA for: Has won at this trip or further
    DATA against: Last-run finishing speed -4.3% vs that field (faded); Returns from a 230-day break; Pulled up in 1 of its last 4 jumps runs

## 3:38 Hexham | race_id rac_32304710139 | QuinnBet Open National Hunt Flat Race (Category 1 Elimination) (GBB Race)
NH Flat | Class 4 | 2m48y | going Good To Soft | Turf | 7 runners | rating band - | age 4-5yo
DATA pace: Unclear - Running styles known for only 3 of 7 runners.
- Max Potential (hrs_17395538559) | 4yo G | 156lb | OR - | draw 0 | jockey Rian Corcoran(5) | trainer David Pipe (14d 0/11) | headgear - | last run 255 days | form F- | MARKET 42.9% | 09:00 median 2.05 | Matchbook 2.16
    comment: Unexposed and lightly raced, Max Potential fell on his only recent start and returns after 255 days off, so there's little form to go on and plenty of scope for improvement. He is yet to win in that limited sample and carries 156 lb.
    DATA: model 13.7% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Trainer 0 wins from 11 runs, last 14 days; Returns from a 255-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Rio Blue (hrs_17395539602) | 4yo G | 156lb | OR - | draw 0 | jockey Tristan Durrell | trainer Dan Skelton (14d 19/80) | headgear - | last run - days | form - | MARKET 24.3% | 09:00 median 3.25 | Matchbook 4.20
    comment: Unraced and unexposed, Rio Blue has no recorded form to go on, so he's an open book with scope to improve. He carries 156 lb on debut, and there's nothing yet to mark him down.
    DATA: model 13.7% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 24% wins (19/80), last 14 days
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Browney Bank (hrs_17395537516) | 4yo C | 156lb | OR - | draw 0 | jockey Danny McMenamin | trainer Ann Hamilton (14d 2/5) | headgear - | last run - days | form - | MARKET 16.0% | 09:00 median 5.00 | Matchbook 6.20
    comment: Browney Bank is an unraced colt with no form to go on, so he's completely unexposed and open to any amount of improvement. He carries 156 lb on debut, and with nothing to judge him on, this is a run to learn from.
    DATA: model 13.7% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 40% wins (2/5), last 14 days
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Jimmy The Jet (hrs_63203462) | 4yo G | 156lb | OR - | draw 0 | jockey Sean Quinlan | trainer Lizzie Quinlan (14d 2/10) | headgear - | last run 230 days | form 3- | MARKET 6.0% | 09:00 median 13.00 | Matchbook 18.00
    comment: The one big risk is a 230-day absence, which leaves fitness a question.
    DATA: model 14.8% | style Held up (led 8% of runs) | runs in data 1 | last 3: 2 Apr Kelso 16.2f Good 3/6
    DATA for: Trainer 20% wins (2/10), last 14 days
    DATA against: Returns from a 230-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Yorgunnarock (hrs_63810110) | 5yo G | 156lb | OR - | draw 0 | jockey Derek Fox | trainer Stuart Coltherd (14d 1/5) | headgear - | last run 212 days | form 4- | MARKET 4.9% | 09:00 median 17.00 | Matchbook 19.50
    DATA: model 11.0% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 20 Apr Kelso 16.2f Good 4/6
    DATA for: Trainer 20% wins (1/5), last 14 days; Last-run finishing speed +2.6% vs that field (finished strongly)
    DATA against: Returns from a 212-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Mortgage Man (hrs_64360905) | 4yo G | 156lb | OR - | draw 0 | jockey Craig Nichol | trainer Ewan Whillans (14d 0/14) | headgear - | last run 196 days | form 4 | MARKET 4.2% | 09:00 median 21.00 | Matchbook 23.00
    comment: The one concern is a 196-day absence, so fitness is the question, along with 156 lb to carry.
    DATA: model 20.6% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 6 May Kelso 16.2f Good 4/10
    DATA for: Last-run finishing speed +5.5% vs that field (finished strongly)
    DATA against: Trainer 0 wins from 14 runs, last 14 days; Returns from a 196-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Angela's Rose (hrs_17395536473) | 4yo F | 149lb | OR - | draw 0 | jockey Nathan Moscrop | trainer Susan Corbett (14d 0/8) | headgear - | last run - days | form - | MARKET 1.8% | 09:00 median 51.00 | Matchbook 65.00
    comment: Angela's Rose is unraced, so she arrives as a blank canvas with plenty of scope to progress, and she carries 149 lb on debut. With no form to go on, she's an unexposed sort who could well find improvement.
    DATA: model 12.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Trainer 0 wins from 8 runs, last 14 days; Lightly raced: 0 runs in our data, so the model has little to go on
