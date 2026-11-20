# Card review packet: Chepstow, 2026-11-20

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
{"meeting": "chepstow", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 11:20 Chepstow | race_id rac_32305357097 | Why Bet Elsewhere, David Lucas Bookmakers Maiden Hurdle Race (GBB Race)
Hurdle | Class 4 | 2m3f100y | going Soft | Turf | 12 runners | rating band - | age 4yo+
DATA pace: Even - Two likely leaders (Moments In Time, Rine Yeats). A fair, even gallop is most likely.
- Bande Organisee (hrs_51558206) | 5yo G | 158lb | OR - | draw 0 | jockey Jamie Brace(5) | trainer Rebecca Curtis (14d 2/6) | headgear - | last run 272 days | form FF/31- | MARKET 31.9% | 09:00 median 2.69 | Matchbook 2.90
    DATA: model 22.0% | style Unknown | runs in data 1 | last 3: 21 Feb Chepstow NH Flat 16.1f Soft 1/8
    DATA for: Trainer 33% wins (2/6), last 14 days; Last-run finishing speed +9.3% vs that field (finished strongly)
    DATA against: Returns from a 272-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Moments In Time (hrs_50433096) | 5yo G | 158lb | OR - | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 16/78) | headgear - | wind surgery | last run 273 days | form 1/44- | MARKET 14.8% | 09:00 median 5.50 | Matchbook 6.60
    DATA: model 8.2% | style Leader (led 57% of runs) | runs in data 1 | last 3: 20 Feb Exeter NH Flat 16.7f Heavy 4/6
    DATA for: Trainer 21% wins (16/78), last 14 days
    DATA against: Returns from a 273-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Exciting Ride (hrs_17395016016) | 5yo G | 158lb | OR - | draw 0 | jockey Sam Twiston-Davies | trainer Paul Nicholls (14d 2/17) | headgear - | last run 257 days | form F42- | MARKET 13.8% | 09:00 median 6.00 | Matchbook 7.00
    DATA: model 6.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 257-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- All About Trev (hrs_61842039) | 5yo G | 158lb | OR - | draw 0 | jockey Lorcan Williams | trainer Jeremy Scott (14d 0/7) | headgear - | last run 273 days | form 1- | MARKET 13.7% | 09:00 median 6.45 | Matchbook 6.80
    DATA: model 15.8% | style Held up (led 8% of runs) | runs in data 1 | last 3: 20 Feb Exeter NH Flat 16.7f Heavy 1/6
    DATA for: Last-run finishing speed +5.3% vs that field (finished strongly)
    DATA against: Returns from a 273-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Kimai (hrs_17394618633) | 5yo M | 151lb | OR - | draw 0 | jockey Harry Cobden | trainer Tom Ellis (14d 1/10) | headgear - | last run 22 days | form 3/1-4 | MARKET 6.8% | 09:00 median 12.00 | Matchbook 14.50
    DATA: model 8.7% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 29 Oct Ffos Las Hurdle 16f Heavy 4/9 fig 104
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Mybluesuedeshoes (hrs_17395541688) | 5yo G | 158lb | OR - | draw 0 | jockey Tom Bellamy | trainer Kim Bailey & Mat Nicholls (14d 1/11) | headgear - | last run 278 days | form P1- | MARKET 6.3% | 09:00 median 12.00 | Matchbook 16.50
    DATA: model 6.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 278-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Noble Charge (hrs_17395677278) | 5yo G | 158lb | OR - | draw 0 | jockey Sean Bowen | trainer Olly Murphy (14d 9/56) | headgear - | last run 572 days | form 5/ | MARKET 5.3% | 09:00 median 15.00 | Matchbook 18.50
    DATA: model 6.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 572-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Rine Yeats (hrs_49974470) | 6yo G | 158lb | OR - | draw 0 | jockey Charlie Deutsch | trainer Venetia Williams (14d 0/5) | headgear - | last run 251 days | form P/13- | MARKET 3.0% | 09:00 median 21.00 | Matchbook 44.00
    DATA: model 4.9% | style Leader (led 57% of runs) | runs in data 1 | last 3: 14 Mar Fontwell NH Flat 17.7f Soft 3/5
    DATA against: Returns from a 251-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Music Song (hrs_62101571) | 4yo G | 157lb | OR - | draw 0 | jockey Harry Kimber | trainer Robert Walford (14d 0/2) | headgear - | last run 241 days | form 42- | MARKET 1.9% | 09:00 median 34.00 | Matchbook 70.00
    DATA: model 7.8% | style Unknown | runs in data 2 | last 3: 28 Feb Doncaster NH Flat 16.6f Soft 4/8; 24 Mar Southwell NH Flat 15.8f Good 2/7
    DATA for: Last-run finishing speed +7.3% vs that field (finished strongly)
    DATA against: Returns from a 241-day break; Lightly raced: 2 runs in our data, so the model has little to go on; First run over hurdles in our data
- Back To Bratton (hrs_17395674149) | 4yo G | 157lb | OR - | draw 0 | jockey Bryan Carver | trainer Dean Summersby (14d 1/3) | headgear - | last run 222 days | form P3- | MARKET 1.0% | 09:00 median 67.00 | Matchbook 130.00
    DATA: model 6.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 222-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- JPR Two (hrs_58535113) | 5yo G | 158lb | OR - | draw 0 | jockey Lorcan Murtagh | trainer Paul Nicholls (14d 2/17) | headgear - | wind surgery | last run 23 days | form 86-3 | MARKET 1.0% | 09:00 median 81.00 | Matchbook 120.00
    DATA: model 4.5% | style Midfield (led 8% of runs) | runs in data 2 | last 3: 4 Apr Newton Abbot Hurdle 18.5f Good 6/11; 28 Oct Newton Abbot Hurdle 21.5f Good To Soft 3/4
    DATA against: Last-run finishing speed -4.9% vs that field (faded); Lightly raced: 2 runs in our data, so the model has little to go on
- Delilah's Boy (hrs_17393900006) | 5yo G | 158lb | OR - | draw 0 | jockey Ned Fox(3) | trainer Samuel Drinkwater (14d 1/7) | headgear - | last run 15 days | form 59 | MARKET 0.4% | 09:00 median 170.50 | Matchbook 400.00
    DATA: model 2.2% | style Held up (led 5% of runs) | runs in data 2 | last 3: 17 Oct Newton Abbot NH Flat 17f Good 5/7 fig 97; 5 Nov Newbury Hurdle 19f Good To Soft 9/10
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on

## 11:50 Chepstow | race_id rac_32304940642 | Guaranteed Odds At David Lucas Bookmakers Novices' Hurdle Race (Div I) (GBB Race)
Hurdle | Class 4 | 2m16y | going Soft | Turf | 14 runners | rating band - | age 4yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Sea The Day (hrs_57653547) | 5yo G | 154lb | OR - | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 16/78) | headgear - | last run 336 days | form 17- | MARKET 32.4% | 09:00 median 2.50 | Matchbook 2.82
    DATA: model 5.8% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 21% wins (16/78), last 14 days
    DATA against: Returns from a 336-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Common Sense (hrs_17394105477) | 5yo G | 154lb | OR - | draw 0 | jockey Sean Bowen | trainer Rebecca Curtis (14d 2/6) | headgear - | last run 29 days | form 21-3 | MARKET 25.6% | 09:00 median 3.25 | Matchbook 3.50
    DATA: model 11.7% | style Unknown | runs in data 1 | last 3: 22 Oct Ffos Las Hurdle 16f Soft 3/10 fig 114
    DATA for: Best recent form figure 114, 4 lb above field average; Trainer 33% wins (2/6), last 14 days
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Herbies Sock (hrs_17393500537) | 4yo G | 154lb | OR - | draw 0 | jockey Stan Sheppard | trainer Tom Lacey (14d 3/12) | headgear - | last run 42 days | form 31-2 | MARKET 12.0% | 09:00 median 6.50 | Matchbook 8.00
    DATA: model 9.4% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 9 Oct Chepstow Hurdle 16.1f Good To Soft 2/10
    DATA for: Trainer 25% wins (3/12), last 14 days; Last-run finishing speed +7.5% vs that field (finished strongly)
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Passage Guenot (hrs_17394619676) | 4yo G | 154lb | OR - | draw 0 | jockey Harry Cobden | trainer Philip Hobbs & Johnson White (14d 2/12) | headgear - | last run 22 days | form 2-2 | MARKET 9.5% | 09:00 median 8.00 | Matchbook 10.00
    DATA: model 12.9% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 29 Oct Ffos Las Hurdle 16f Heavy 2/9 fig 116
    DATA for: Best recent form figure 116, 6 lb above field average; Last-run finishing speed +2.1% vs that field (finished strongly)
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Littlebobbydazzler (hrs_61910695) | 4yo G | 154lb | OR - | draw 0 | jockey Charlie Deutsch | trainer Mel Rowley (14d 1/10) | headgear h | last run 27 days | form 31-5 | MARKET 6.0% | 09:00 median 12.00 | Matchbook 17.00
    DATA: model 9.7% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 22 Feb Hereford NH Flat 16.2f Soft 3/10; 18 Apr Bangor-on-Dee NH Flat 16.7f Good 1/11; 24 Oct Cheltenham NH Flat 16.5f Good To Soft 5/10 fig 105
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Best recent form figure 105, 5 lb below field average; First run over hurdles in our data
- What's Your Game (hrs_46077962) | 4yo G | 161lb | OR - | draw 0 | jockey Sam Twiston-Davies | trainer Georgina Nicholls (14d 0/2) | headgear - | last run 23 days | form 1 | MARKET 4.5% | 09:00 median 17.00 | Matchbook 21.00
    DATA: model 4.0% | style Prominent (led 4% of runs) | runs in data 4 | last 3: 30 Mar Navan Flat 14f Heavy 11/11; 28 Jun Curragh Flat 12f Good 11/13; 28 Oct Huntingdon Hurdle 19.5f Good 1/6 fig 115
    DATA for: Best recent form figure 115, 5 lb above field average; Last-run finishing speed +2.9% vs that field (finished strongly); Has won at this trip or further
- Sears Crossing (hrs_52087609) | 4yo G | 154lb | OR - | draw 0 | jockey Robert Dunne | trainer Olly Murphy (14d 9/56) | headgear - | last run 36 days | form 2-6 | MARKET 2.2% | 09:00 median 34.00 | Matchbook 48.00
    DATA: model 5.7% | style Held up (led 5% of runs) | runs in data 2 | last 3: 24 Apr Perth Hurdle 16.2f Good 2/8; 15 Oct Perth Hurdle 16f Soft 6/9 fig 107
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Clonagoose (hrs_17394732320) | 5yo G | 154lb | OR - | draw 0 | jockey Bryan Carver | trainer Dean Summersby (14d 1/3) | headgear - | last run 19 days | form 1-1117 | MARKET 1.4% | 09:00 median 51.00 | Matchbook 90.00
    DATA: model 5.1% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 1 Nov Worcester Hurdle 16f Good To Soft 7/16 fig 102
    DATA against: Best recent form figure 102, 8 lb below field average; Lightly raced: 1 run in our data, so the model has little to go on
- Debrave Soldier (hrs_17394921103) | 5yo G | 154lb | OR - | draw 0 | jockey Lewis Stones(3) | trainer Olly Murphy (14d 9/56) | headgear - | last run 12 days | form 2-5 | MARKET 1.4% | 09:00 median 41.00 | Matchbook 140.00
    DATA: model 11.6% | style Unknown | runs in data 1 | last 3: 8 Nov Ffos Las Hurdle 20f Soft 5/9
    DATA against: Last-run finishing speed -4.8% vs that field (faded); Lightly raced: 1 run in our data, so the model has little to go on
- Barrow Hill Lad (hrs_50339849) | 5yo G | 154lb | OR - | draw 0 | jockey David Noonan | trainer Ben Clarke (14d 0/7) | headgear t (1st time) | last run 22 days | form 109-P | MARKET 1.2% | 09:00 median 51.00 | Matchbook 130.00
    DATA: model 4.7% | style Prominent (led 8% of runs) | runs in data 2 | last 3: 27 Jan Chepstow NH Flat 16.1f Soft 9/10; 29 Oct Ffos Las Hurdle 20f Heavy PU/11
    DATA for: First-time headgear
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Pulled up in 1 of its last 1 jumps runs
- Beau Merle (hrs_63171675) | 5yo G | 154lb | OR - | draw 0 | jockey J. P. O'Neill(10) | trainer Faye Bramley (14d 1/17) | headgear - | last run 233 days | form 4- | MARKET 1.1% | 09:00 median 51.00 | Matchbook 160.00
    DATA: model 6.3% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 1 Apr Wincanton NH Flat 15.2f Good 4/8
    DATA against: Returns from a 233-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Lingering Glance (hrs_60722585) | 5yo G | 154lb | OR - | draw 0 | jockey Lorcan Williams | trainer Jeremy Scott (14d 0/7) | headgear - | last run 248 days | form 87- | MARKET 1.0% | 09:00 median 81.00 | Matchbook 170.00
    DATA: model 5.0% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 15 Jan Wincanton NH Flat 15.2f Heavy 8/10; 17 Mar Exeter NH Flat 16.7f Good To Soft 7/10
    DATA against: Returns from a 248-day break; Lightly raced: 2 runs in our data, so the model has little to go on; First run over hurdles in our data
- Commander King (hrs_17395680407) | 7yo G | 154lb | OR - | draw 0 | jockey Rian Corcoran(5) | trainer Gordon Treacy (14d 0/2) | headgear - | last run 201 days | form 31442- | MARKET 0.9% | 09:00 median 81.00 | Matchbook 170.00
    DATA: model 5.8% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 201-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- The Sky At Night (hrs_17394616547) | 5yo G | 154lb | OR - | draw 0 | jockey Adam Wedge | trainer Clive Boultbee-Brooks (14d 0/6) | headgear - | last run 16 days | form 2/0 | MARKET 0.8% | 09:00 median 101.00 | Matchbook 180.00
    DATA: model 2.3% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 4 Nov Chepstow Hurdle 16f Good To Soft 11/12
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on

## 12:22 Chepstow | race_id rac_32304942579 | McCarthy Construction Novices' Hurdle Race (Div II) (GBB Race)
Hurdle | Class 4 | 2m16y | going Soft | Turf | 13 runners | rating band - | age 4yo+
DATA pace: Unclear - Running styles known for only 6 of 13 runners.
- Hidden Mountain (hrs_52056529) | 5yo G | 161lb | OR - | draw 0 | jockey Tom Bellamy | trainer Kim Bailey & Mat Nicholls (14d 1/11) | headgear - | last run 19 days | form 21-1 | MARKET 35.5% | 09:00 median 2.25 | Matchbook 2.58
    DATA: model 26.1% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 1 Mar Huntingdon NH Flat 15.8f Good To Soft 1/12; 1 Nov Worcester Hurdle 16f Good To Soft 1/16 fig 121
    DATA for: Best recent form figure 121, 11 lb above field average; Last-run finishing speed +5.7% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Old Habits (hrs_52236506) | 5yo G | 154lb | OR - | draw 0 | jockey Sean Bowen | trainer Olly Murphy (14d 9/56) | headgear - | last run 36 days | form 3/12-3 | MARKET 32.9% | 09:00 median 2.50 | Matchbook 2.72
    DATA: model 11.0% | style Midfield (led 8% of runs) | runs in data 2 | last 3: 18 Apr Ayr NH Flat 16f Heavy 2/9; 15 Oct Perth Hurdle 16f Soft 3/9 fig 111
    DATA for: Good recent finishing positions
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Moltezuma (hrs_17394932576) | 5yo G | 154lb | OR - | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 16/78) | headgear - | last run 299 days | form 1- | MARKET 13.5% | 09:00 median 5.50 | Matchbook 7.40
    DATA: model 6.1% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 21% wins (16/78), last 14 days
    DATA against: Returns from a 299-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Justoneglance (hrs_17395676235) | 5yo G | 154lb | OR - | draw 0 | jockey Kielan Woods | trainer Fergal O'Brien (14d 3/30) | headgear - | last run - days | form - | MARKET 4.3% | 09:00 median 19.25 | Matchbook 23.00
    DATA: model 6.1% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Soviet Sailor (hrs_17394320335) | 5yo G | 154lb | OR - | draw 0 | jockey Daniel Sansom(3) | trainer Seamus Mullins (14d 3/13) | headgear - | last run 26 days | form 1 | MARKET 3.5% | 09:00 median 21.00 | Matchbook 30.00
    DATA: model 7.8% | style Held up (led 8% of runs) | runs in data 1 | last 3: 25 Oct Market Rasen NH Flat 16.5f Good To Soft 1/4 fig 98
    DATA for: Trainer 23% wins (3/13), last 14 days; Has won at this trip or further
    DATA against: Best recent form figure 98, 12 lb below field average; Lightly raced: 1 run in our data, so the model has little to go on
- Irishcoffee Has (hrs_17395417571) | 4yo G | 154lb | OR - | draw 0 | jockey Harry Cobden | trainer Nick Gifford (14d 1/6) | headgear - | last run 292 days | form F- | MARKET 3.1% | 09:00 median 26.00 | Matchbook 34.00
    DATA: model 6.1% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 292-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Berkshire Woody (hrs_58534805) | 4yo G | 154lb | OR - | draw 0 | jockey Jamie Brace(5) | trainer Rebecca Curtis (14d 2/6) | headgear - | last run 216 days | form 3057- | MARKET 2.2% | 09:00 median 41.00 | Matchbook 44.00
    DATA: model 5.3% | style Leader (led 29% of runs) | runs in data 3 | last 3: 1 Jan Cheltenham NH Flat 16.8f Good 15/16; 22 Feb Hereford NH Flat 16.2f Soft 5/10; 18 Apr Bangor-on-Dee NH Flat 16.7f Good 7/11
    DATA for: Trainer 33% wins (2/6), last 14 days
    DATA against: Returns from a 216-day break; First run over hurdles in our data
- Mistral des Bordes (hrs_56559503) | 4yo G | 154lb | OR - | draw 0 | jockey Adam Wedge | trainer Mrs C. Williams (14d 1/25) | headgear - | last run - days | form - | MARKET 1.2% | 09:00 median 51.00 | Matchbook 140.00
    DATA: model 6.1% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Requiem (hrs_45759511) | 4yo G | 154lb | OR - | draw 0 | jockey Harry Kimber | trainer Robert Walford (14d 0/2) | headgear - | last run 484 days | form - | MARKET 1.0% | 09:00 median 67.00 | Matchbook 180.00
    DATA: model 6.1% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 484-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Topsham Tide (hrs_59335787) | 5yo M | 147lb | OR - | draw 0 | jockey Lorcan Williams | trainer Jeremy Scott (14d 0/7) | headgear - | last run 16 days | form 02-7 | MARKET 1.0% | 09:00 median 81.00 | Matchbook 140.00
    DATA: model 4.6% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 2 Apr Chepstow NH Flat 16.1f Good To Soft 2/11; 4 Nov Chepstow Hurdle 16f Good To Soft 7/12
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Victoria Line (hrs_25238836) | 8yo G | 154lb | OR - | draw 0 | jockey Callum Pritchard | trainer Philip Hobbs & Johnson White (14d 2/12) | headgear - | last run 898 days | form 3/ | MARKET 0.9% | 09:00 median 101.00 | Matchbook 160.00
    DATA: model 6.1% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 898-day break; Lightly raced: 0 runs in our data, so the model has little to go on; Aged 8, older than most of this field
- Blazing Force (hrs_17395679364) | 7yo G | 154lb | OR - | draw 0 | jockey Ben Godfrey | trainer Nigel Hawke (14d 1/5) | headgear - | last run 916 days | form 6/ | MARKET 0.7% | 09:00 median 81.00 | Matchbook 200.00
    DATA: model 6.1% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 20% wins (1/5), last 14 days
    DATA against: Returns from a 916-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Riseandcall (hrs_17394615504) | 5yo G | 154lb | OR - | draw 0 | jockey David Noonan | trainer Ben Clarke (14d 0/7) | headgear - | last run 5 days | form 432-05 | MARKET 0.4% | 09:00 median 201.00 | Matchbook 310.00
    DATA: model 2.6% | style Midfield (led 8% of runs) | runs in data 2 | last 3: 4 Nov Chepstow Hurdle 19.5f Good To Soft 11/14; 15 Nov Fontwell Hurdle 17.5f Soft 5/13
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on

## 12:57 Chepstow | race_id rac_32304944516 | Treble Odds L15s At David Lucas Handicap Steeple Chase (GBB Race)
Chase | Class 3 | 2m3f98y | going Good | Turf | 11 runners | rating band 0-125 | age 4yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Ben Solo (hrs_34166496) | 7yo G | 169lb | OR 126 | draw 0 | jockey Jamie Brace(5) | trainer Rebecca Curtis (14d 2/6) | headgear - | wind surgery | last run 37 days | form 2UP2-3 | MARKET 20.2% | 09:00 median 4.33 | Matchbook 4.50 | CHECK (skip line 4.11)
    comment: The risk is a 169 lb burden, plus a pulled up and an unseated in his last five.
    DATA: model 8.4% | style Prominent (led 38% of runs) | runs in data 3 | last 3: 12 Mar Cheltenham Chase 20.6f Good PU/18; 2 Apr Chepstow Chase 19.4f Good To Soft 2/6; 14 Oct Ffos Las Chase 24f Soft 3/6 fig 116
    DATA for: Official rating 126, 6 lb above field average; Trainer 33% wins (2/6), last 14 days
    DATA against: Recent figures 10 lb below its current mark (looks high in the weights); Carries 6 lb more than average; Pulled up in 1 of its last 3 jumps runs
- Wilstar (hrs_50401764) | 6yo G | 168lb | OR 125 | draw 0 | jockey Sean Bowen | trainer Olly Murphy (14d 9/56) | headgear t | last run 257 days | form /8211- | MARKET 18.2% | 09:00 median 4.50 | Matchbook 5.30
    DATA: model 19.5% | style Unknown | runs in data 3 | last 3: 2 Jan Ayr Hurdle 16f Soft 2/13; 2 Feb Southwell Hurdle 15.8f Good To Soft 1/10; 8 Mar Warwick Hurdle 16f Good To Soft 1/11
    DATA for: Last-run finishing speed +6.5% vs that field (finished strongly); Good recent finishing positions
    DATA against: Returns from a 257-day break; First run over fences in our data
- Largy Go (hrs_51123758) | 5yo G | 158lb | OR 115 | draw 0 | jockey Harry Cobden | trainer Jonjo & A.J. O'Neill (14d 6/31) | headgear - | last run 230 days | form 1/231- | MARKET 15.8% | 09:00 median 5.50 | Matchbook 5.80
    comment: Largy Go has strong recent form, winning last time out and finishing third and second before that, but a 230-day absence is a concern and he carries 158 lb.
    DATA: model 15.0% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 5 Feb Lingfield Hurdle 16f Heavy 2/10; 6 Mar Ayr Hurdle 16f Soft 3/12; 4 Apr Haydock Hurdle 24.3f Good 1/8
    DATA for: Last-run finishing speed +4.6% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions; Carries 5 lb less than average
    DATA against: Official rating 115, 5 lb below field average; Returns from a 230-day break; First run over fences in our data
- Quay Item (hrs_41052228) | 6yo G | 167lb | OR 124 | draw 0 | jockey Freddie Gordon | trainer Nicky Henderson (14d 3/14) | headgear - | last run 266 days | form 2/312- | MARKET 8.4% | 09:00 median 10.00 | Matchbook 11.50
    comment: Quay Item looks solid on recent form, with a second last time out, a win two starts back and a third before that, but he returns after 266 days off and carries 167 lb.
    DATA: model 11.8% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 26 Jan Plumpton Hurdle 20.5f Soft 1/8; 27 Feb Doncaster Hurdle 24.4f Good To Soft 2/4
    DATA for: Trainer 21% wins (3/14), last 14 days; Has won at this trip or further; Good recent finishing positions
    DATA against: Returns from a 266-day break; Lightly raced: 2 runs in our data, so the model has little to go on; First run over fences in our data
- Sogna In Grande (hrs_50402205) | 6yo G | 168lb | OR 125 | draw 0 | jockey Tom Bellamy | trainer Kim Bailey & Mat Nicholls (14d 1/11) | headgear - | last run 27 days | form /114-6 | MARKET 8.0% | 09:00 median 10.00 | Matchbook 12.50
    comment: Sogna In Grande won twice in his last four starts, including a win four starts back and another three starts back, and he returns fresh after 27 days having run over today's trip. The risk is a sixth last time out and 168 lb on his back.
    DATA: model 4.0% | style Unknown | runs in data 3 | last 3: 1 Apr Wincanton Hurdle 21.4f Good 1/5; 22 Apr Perth Hurdle 23.9f Good 4/4; 24 Oct Cheltenham Chase 20f Good 6/9 fig 118
    DATA for: Has won at this trip or further
    DATA against: Recent figures 7 lb below its current mark (looks high in the weights)
- Minella Missile (hrs_34961850) | 8yo G | 160lb | OR 117 | draw 0 | jockey Adam Wedge | trainer Mrs C. Williams (14d 1/25) | headgear - | wind surgery | last run 29 days | form 5P75-2 | MARKET 7.9% | 09:00 median 10.00 | Matchbook 13.00
    comment: The risk is a yard out of form at 1/25 over the last 14 days, with 160 lb to carry and yet to win in recent starts.
    DATA: model 5.2% | style Held up (led 3% of runs) | runs in data 6 | last 3: 14 Mar Uttoxeter Hurdle 19.9f Soft 7/14; 17 Apr Ayr Hurdle 21.4f Soft 5/11; 22 Oct Ffos Las Chase 16f Soft 2/6 fig 117
    DATA for: Last-run finishing speed +2.2% vs that field (finished strongly)
    DATA against: Pulled up in 1 of its last 5 jumps runs; Pace: steady gallop likely, hard to come from off the pace
- Authentic Legacy (hrs_38792516) | 6yo G | 169lb | OR 126 | draw 0 | jockey Freddie Mitchell(3) | trainer Jamie Moore & Josh Moore (14d 1/19) | headgear - | last run 232 days | form 12/61- | MARKET 7.3% | 09:00 median 10.00 | Matchbook 15.00
    comment: Won last time out and again four starts back, with a second three starts back, but a 232-day layoff raises fitness questions, and he has run over today's trip, carrying 169 lb off a mark of 126.
    DATA: model 7.6% | style Held up (led 8% of runs) | runs in data 2 | last 3: 28 Feb Newbury Chase 19.9f Good To Soft 6/8; 2 Apr Chepstow Hurdle 19.5f Good To Soft 1/12
    DATA for: Official rating 126, 6 lb above field average; Last-run finishing speed +4.9% vs that field (finished strongly); Has won at this trip or further
    DATA against: Carries 6 lb more than average; Returns from a 232-day break; Lightly raced: 2 runs in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Pepe Le Moko (hrs_28781592) | 8yo G | 151lb | OR 108 | draw 0 | jockey Miss Heidi Palin(5) | trainer Mrs Jane Williams (14d 2/8) | headgear p | last run 23 days | form 23P-04 | MARKET 4.0% | 09:00 median 19.00 | Matchbook 27.00
    comment: Fourth last time out and fresh enough after 23 days, but Pepe Le Moko is winless in his last five and was pulled up three starts back, so consistency is a question.
    DATA: model 3.2% | style Midfield (led 23% of runs) | runs in data 4 | last 3: 4 Feb Ludlow Chase 20.1f Soft PU/7; 9 Oct Chepstow Hurdle 19.5f Good To Soft 12/15; 28 Oct Newton Abbot Chase 21f Good To Soft 4/6 fig 105
    DATA for: Trainer 25% wins (2/8), last 14 days; Carries 12 lb less than average
    DATA against: Best recent form figure 105, 10 lb below field average; Official rating 108, 12 lb below field average; Pulled up in 1 of its last 4 jumps runs
- Plains Drifter (hrs_46697273) | 6yo G | 160lb | OR 117 | draw 0 | jockey Liam Harrison | trainer Fergal O'Brien (14d 3/30) | headgear - | last run 220 days | form 52321- | MARKET 3.9% | 09:00 median 19.00 | Matchbook 29.00
    comment: Plains Drifter won last time out and has been in the first three in four of his last five, but 220 days off the track is a big concern, and he carries 160 lb.
    DATA: model 14.7% | style Prominent (led 5% of runs) | runs in data 3 | last 3: 15 Jan Ludlow Hurdle 21.2f Good To Soft 3/11; 15 Mar Market Rasen Hurdle 20.6f Good To Soft 2/8; 14 Apr Market Rasen Hurdle 20.6f Good 1/6
    DATA for: Last-run finishing speed +2.4% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Returns from a 220-day break; First run over fences in our data
- Hardy du Seuil (hrs_21659876) | 9yo G | 167lb | OR 124 | draw 0 | jockey Isabelle Ryder(5) | trainer Jamie Snowden (14d 6/22) | headgear p | last run 34 days | form 4235-2 | MARKET 3.2% | 09:00 median 26.00 | Matchbook 34.00
    comment: Hardy du Seuil arrives on a consistent run, second last time out and in the frame in three of his last five, while he has run over today's trip before and is fresh after 34 days off.
    DATA: model 5.2% | style Prominent (led 23% of runs) | runs in data 5 | last 3: 27 Feb Newbury Chase 16.4f Good To Soft 3/4; 4 Apr Newton Abbot Chase 21f Good 5/6; 17 Oct Market Rasen Chase 21.5f Good 2/5 fig 115
    DATA for: Trainer 27% wins (6/22), last 14 days; Good recent finishing positions
    DATA against: Recent figures 9 lb below its current mark (looks high in the weights)
- Opening Bid (hrs_2993004) | 11yo G | 161lb | OR 118 | draw 0 | jockey Bryan Carver | trainer Joe Tizzard (14d 2/18) | headgear tp | last run 23 days | form /21-43 | MARKET 3.1% | 09:00 median 29.00 | Matchbook 34.00
    comment: Opening Bid arrives fit enough after 23 days, a third last time out, a fourth two starts back, and a winner three starts back, and he has run over today's trip.
    DATA: model 5.4% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 9 Oct Chepstow Hurdle 16.1f Good To Soft 4/15; 28 Oct Newton Abbot Chase 16.5f Good To Soft 3/5 fig 116
    DATA for: Last-run finishing speed +3.1% vs that field (finished strongly)
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Aged 11, older than most of this field

## 1:32 Chepstow | race_id rac_32304946453 | Albert Bartlett Triple Crown Series Handicap Hurdle Race (Qualifier)
Hurdle | Class 4 | 2m3f100y | going Soft | Turf | 12 runners | rating band 0-110 | age 3yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Lejo du Seuil (hrs_60492432) | 5yo G | 158lb | OR 107 | draw 0 | jockey Sean Bowen | trainer Ian Williams (14d 1/8) | headgear - | last run 15 days | form 2952-4 | MARKET 20.7% | 09:00 median 4.00 | Matchbook 4.50 | CHECK (skip line 3.80)
    comment: Yet to win in his last five, he must prove it carrying 158 lb.
    DATA: model 8.6% | style Midfield (led 4% of runs) | runs in data 4 | last 3: 4 Feb Ludlow Hurdle 15.8f Soft 5/11; 19 Feb Huntingdon Hurdle 15.8f Heavy 2/9; 5 Nov Newbury Hurdle 16.5f Good To Soft 4/16 fig 109
    DATA for: Best recent form figure 109, 4 lb above field average
- Majeur Allen (hrs_59335836) | 4yo G | 158lb | OR 108 | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 16/78) | headgear - | last run 301 days | form 32- | MARKET 17.3% | 09:00 median 4.33 | Matchbook 5.70
    comment: Majeur Allen filled the places in his last two starts, a second last time out and a third two starts back, but he is yet to win in that spell, and 301 days off makes him hard to fancy carrying 158 lb off an official mark of 108.
    DATA: model 9.0% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 23 Jan Warwick Hurdle 16f Good To Soft 2/7
    DATA for: Trainer 21% wins (16/78), last 14 days; Last-run finishing speed +2.8% vs that field (finished strongly)
    DATA against: Returns from a 301-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Crystal Orchard (hrs_58165338) | 5yo G | 156lb | OR 105 | draw 0 | jockey Harry Cobden | trainer Joe Tizzard (14d 2/18) | headgear - | last run 23 days | form 8553-2 | MARKET 14.4% | 09:00 median 5.50 | Matchbook 6.60
    comment: Crystal Orchard is yet to win in his last five starts but is trending the right way, a second last time out and a third two starts back, and he returns after 23 days.
    DATA: model 9.7% | style Prominent (led 5% of runs) | runs in data 3 | last 3: 9 Jan Exeter NH Flat 16.7f Good To Soft 5/11; 6 Mar Exeter Hurdle 16.7f Good To Soft 3/16; 28 Oct Newton Abbot Hurdle 21.5f Good To Soft 2/4 fig 107
    DATA for: Last-run finishing speed +3.7% vs that field (finished strongly); Good recent finishing positions
- Lully du Houx (hrs_58745428) | 5yo G | 157lb | OR 106 | draw 0 | jockey Tom Bellamy | trainer Kim Bailey & Mat Nicholls (14d 1/11) | headgear - | last run 22 days | form 459-01 | MARKET 11.9% | 09:00 median 7.00 | Matchbook 7.80
    comment: Fit enough after 22 days, he shoulders 157 lb off an official mark of 106.
    DATA: model 11.0% | style Midfield (led 23% of runs) | runs in data 4 | last 3: 17 Feb Newbury Hurdle 16.3f Soft 9/11; 9 Oct Chepstow Hurdle 16.1f Good To Soft 11/15; 29 Oct Ffos Las Hurdle 16f Heavy 1/7 fig 98
    DATA for: Last-run finishing speed +6.3% vs that field (finished strongly)
    DATA against: Best recent form figure 98, 7 lb below field average; Recent figures 8 lb below its current mark (looks high in the weights)
- Mulinas (hrs_37890601) | 7yo G | 159lb | OR 108 | draw 0 | jockey Sam Twiston-Davies | trainer Paul Nicholls (14d 2/17) | headgear - | last run 266 days | form 3/P63- | MARKET 7.8% | 09:00 median 10.00 | Matchbook 12.50
    comment: Mulinas was third last time out, and a third four starts back shows he can reach the frame, but he is yet to win in his last four starts and was pulled up three starts back.
    DATA: model 5.0% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 23 Jan Doncaster Hurdle 19.4f Soft PU/13; 17 Feb Newbury Hurdle 16.3f Soft 6/11; 27 Feb Newbury Hurdle 20.5f Good To Soft 3/6
    DATA for: Last-run finishing speed +2.7% vs that field (finished strongly)
    DATA against: Returns from a 266-day break; Pulled up in 1 of its last 3 jumps runs
- Can You Hear Me (hrs_49389200) | 5yo G | 156lb | OR 105 | draw 0 | jockey Sean Houlihan | trainer Philip Hobbs & Johnson White (14d 2/12) | headgear h | last run 21 days | form 2692-7 | MARKET 6.5% | 09:00 median 11.00 | Matchbook 16.00
    comment: Yet to win in his last five, Can You Hear Me was only seventh last time out and has a ninth and a sixth in that run, so he is hard to fancy at 156 lb.
    DATA: model 6.9% | style Held up (led 5% of runs) | runs in data 3 | last 3: 25 Feb Wincanton Hurdle 19.8f Good To Soft 9/15; 26 Mar Chepstow Hurdle 19.5f Good To Soft 2/10; 30 Oct Uttoxeter Hurdle 20f Good 7/15 fig 104
    DATA for: Last-run finishing speed +2.2% vs that field (finished strongly)
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Laurier des Obeaux (hrs_51866437) | 5yo G | 156lb | OR 105 | draw 0 | jockey Freddie Mitchell(3) | trainer Jamie Moore & Josh Moore (14d 1/19) | headgear - | last run 266 days | form 4/354- | MARKET 4.4% | 09:00 median 15.00 | Matchbook 27.00
    comment: Fourth last time out and a third three starts back show Laurier des Obeaux is consistent, and he has run over today's trip, but he is winless in his last four and returns after 266 days off.
    DATA: model 4.7% | style Unknown | runs in data 1 | last 3: 27 Feb Newbury Hurdle 20.5f Good To Soft 4/6
    DATA against: Returns from a 266-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Lipstick (hrs_44975140) | 5yo G | 157lb | OR 106 | draw 0 | jockey Adam Wedge | trainer Mrs C. Williams (14d 1/25) | headgear - | last run 272 days | form 834- | MARKET 4.0% | 09:00 median 17.00 | Matchbook 29.00
    comment: Lipstick was fourth last time out and third the start before, so the form is respectable, but he's yet to win in his last three and returns after 272 days off.
    DATA: model 11.1% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 21 Feb Chepstow Hurdle 16.1f Soft 4/9
    DATA against: Returns from a 272-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Lets Go To Vegas (hrs_29226106) | 8yo M | 161lb | OR 110 | draw 0 | jockey Jack Hogan | trainer Alastair Ralph (14d 0/6) | headgear - | last run 288 days | form 2/142- | MARKET 3.8% | 09:00 median 19.00 | Matchbook 28.00
    comment: The main risk is a 288-day absence, and she also carries 161 lb.
    DATA: model 14.3% | style Held up (led 8% of runs) | runs in data 2 | last 3: 1 Jan Windsor Hurdle 20f Good 4/8; 5 Feb Doncaster Hurdle 19.4f Soft 2/6
    DATA for: Last-run finishing speed +3.5% vs that field (finished strongly)
    DATA against: Returns from a 288-day break; Lightly raced: 2 runs in our data, so the model has little to go on; Aged 8, older than most of this field; Pace: steady gallop likely, hard to come from off the pace
- Fils de Roi (hrs_31892448) | 7yo G | 161lb | OR 110 | draw 0 | jockey Tom Broughton(3) | trainer Fergal O'Brien (14d 3/30) | headgear - | last run 28 days | form 26/9-0 | MARKET 3.8% | 09:00 median 19.00 | Matchbook 27.00
    comment: Fils de Roi arrives fresh after 28 days off and has run over today's trip, with a second four starts back his best recent effort, though he's yet to win in that spell.
    DATA: model 3.8% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 23 Oct Cheltenham Hurdle 16.5f Good To Soft 10/11 fig 105
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- King of The Road (hrs_37702259) | 7yo G | 156lb | OR 105 | draw 0 | jockey Callum Pritchard | trainer Ben Pauling (14d 5/25) | headgear v (1st time) | last run 50 days | form 290-47 | MARKET 3.3% | 09:00 median 27.00 | Matchbook 29.00
    DATA: model 6.2% | style Prominent (led 29% of runs) | runs in data 4 | last 3: 27 Mar Wetherby Hurdle 21.3f Good 15/16; 20 May Warwick Hurdle 21f Good 4/7; 1 Oct Southwell Hurdle 15.8f Good 7/8
    DATA for: Trainer 20% wins (5/25), last 14 days; First-time headgear
    DATA against: Last-run finishing speed -5.1% vs that field (faded)
- King Sacre (hrs_50123472) | 6yo G | 159lb | OR 108 | draw 0 | jockey Bryan Carver | trainer Nigel Hawke (14d 1/5) | headgear h | last run 117 days | form 52-10P | MARKET 2.1% | 09:00 median 34.00 | Matchbook 55.00
    comment: King Sacre was pulled up last time out and unplaced the run before, so the recent trend is poor, and he returns after 117 days off while carrying 159 lb.
    DATA: model 9.8% | style Prominent (led 38% of runs) | runs in data 6 | last 3: 9 May Hexham Hurdle 16.2f Good To Soft 1/9; 7 Jun Perth Hurdle 16.2f Good 10/12; 26 Jul Uttoxeter Hurdle 15.8f Good PU/6
    DATA for: Trainer 20% wins (1/5), last 14 days
    DATA against: Returns from a 117-day break; Pulled up in 1 of its last 5 jumps runs

## 2:07 Chepstow | race_id rac_32304948390 | Happy 80th Birthday Pamela Hall Handicap Steeple Chase (GBB Race)
Chase | Class 4 | 2m7f136y | going Good | Turf | 11 runners | rating band 0-110 | age 4yo+
DATA pace: Lone leader - Patriotik is the only habitual front-runner and may be allowed an easy lead.
- Gingerbred (hrs_29212561) | 8yo G | 158lb | OR 105 | draw 0 | jockey Will Featherstone(7) | trainer Joe Tizzard (14d 2/18) | headgear - | last run 16 days | form 346-11 | MARKET 25.4% | 09:00 median 3.25 | Matchbook 3.50 | CHECK (skip line 3.09)
    comment: Carrying 158 lb off 105, he has run over today's trip, but the weight looks a stiff ask.
    DATA: model 16.8% | style Midfield (led 29% of runs) | runs in data 6 | last 3: 26 Mar Chepstow Chase 30.6f Good To Soft 6/9; 14 Oct Ffos Las Chase 28f Soft 1/7 fig 90; 4 Nov Chepstow Chase 23.5f Good 1/5 fig 95
    DATA for: Last-run finishing speed +3.9% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Best recent form figure 95, 6 lb below field average; Recent figures 10 lb below its current mark (looks high in the weights)
- Better Off Alone (hrs_34859818) | 7yo G | 161lb | OR 108 | draw 0 | jockey Sean Bowen | trainer Martin Keighley (14d 3/13) | headgear v | last run 28 days | form 4P-312 | MARKET 20.5% | 09:00 median 4.00 | Matchbook 4.50
    comment: Better Off Alone arrives in good heart, a second last time out and a winner two starts back, and he has run over today's trip before after 28 days off. The one risk is his 161 lb burden, a hefty weight to carry.
    DATA: model 12.7% | style Prominent (led 23% of runs) | runs in data 5 | last 3: 4 Sep Worcester Chase 23f Good 3/6; 4 Oct Uttoxeter Chase 24f Good 1/7; 23 Oct Cheltenham Chase 25f Good To Soft 2/11 fig 106
    DATA for: Best recent form figure 106, 5 lb above field average; Trainer 23% wins (3/13), last 14 days; Has won at this trip or further; Good recent finishing positions
    DATA against: Race comments mention jumping mistakes in 2 of its last 5 runs; Pulled up in 1 of its last 5 jumps runs
- Patriotik (hrs_35335790) | 7yo G | 158lb | OR 105 | draw 0 | jockey Adam Wedge | trainer Mrs C. Williams (14d 1/25) | headgear - | last run 22 days | form 065P-5 | MARKET 11.2% | 09:00 median 7.00 | Matchbook 8.40
    DATA: model 4.6% | style Prominent (led 54% of runs) | runs in data 4 | last 3: 26 Jan Plumpton Hurdle 20.5f Soft 5/7; 17 Apr Ayr Hurdle 24.3f Soft PU/15; 29 Oct Ffos Las Chase 19.5f Good 5/6 fig 102
    DATA against: Pulled up in 1 of its last 4 jumps runs
- Jongleur d'Etoiles (hrs_35416801) | 7yo G | 160lb | OR 107 | draw 0 | jockey Harry Cobden | trainer Neil Mulholland (14d 3/19) | headgear tp | last run 119 days | form FP2-81 | MARKET 11.1% | 09:00 median 6.50 | Matchbook 9.40
    comment: Won last time out, but that came after an eighth two starts back and a pulled up and a fall further back, and a 119-day break is a concern.
    DATA: model 12.7% | style Prominent (led 3% of runs) | runs in data 5 | last 3: 13 Mar Doncaster Chase 26f Good To Soft 2/4; 6 Jun Worcester Chase 23f Good 8/11; 24 Jul Uttoxeter Chase 24f Good 1/14
    DATA for: Last-run finishing speed +4.6% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Returns from a 119-day break; Race comments mention jumping mistakes in 3 of its last 5 runs; Fell or unseated in 1 of its last 5 jumps runs; Pulled up in 1 of its last 5 jumps runs
- Jukebox King (hrs_48644533) | 6yo G | 161lb | OR 108 | draw 0 | jockey Tom Bellamy | trainer Kim Bailey & Mat Nicholls (14d 1/11) | headgear t | wind surgery | last run 19 days | form 4442-0 | MARKET 9.2% | 09:00 median 9.00 | Matchbook 10.00
    comment: Jukebox King was beaten last time out but finished second two starts back, and he's been fourth in three of his last five, so he's consistent without a win in that spell.
    DATA: model 10.5% | style Midfield (led 4% of runs) | runs in data 4 | last 3: 8 Mar Warwick Hurdle 21f Good To Soft 4/9; 1 Apr Wincanton Hurdle 21.4f Good 2/8; 1 Nov Worcester Chase 20f Good To Soft 12/15
    DATA against: Last-run finishing speed -5.8% vs that field (faded)
- Tommys Charm (hrs_37701461) | 8yo G | 156lb | OR 103 | draw 0 | jockey Conor O'Farrell | trainer Kerry Lee (14d 1/5) | headgear tp | last run 213 days | form PP654- | MARKET 5.8% | 09:00 median 13.00 | Matchbook 17.00
    comment: Fourth last time out, and a fifth two starts back, suggest Tommys Charm is heading in the right direction, and he has run over today's trip.
    DATA: model 4.5% | style Prominent (led 23% of runs) | runs in data 4 | last 3: 26 Feb Ludlow Chase 23.8f Good To Soft 6/7; 15 Mar Chepstow Chase 19.4f Soft 5/5; 21 Apr Ffos Las Chase 23.8f Good 4/9
    DATA for: Trainer 20% wins (1/5), last 14 days
    DATA against: Returns from a 213-day break; Race comments mention jumping mistakes in 3 of its last 4 runs; Pulled up in 1 of its last 4 jumps runs
- The Long Point (hrs_38089289) | 7yo G | 162lb | OR 109 | draw 0 | jockey Jack Hogan | trainer Emma Lavelle (14d 3/19) | headgear - | last run 237 days | form 4511P- | MARKET 4.8% | 09:00 median 15.00 | Matchbook 22.00
    comment: The Long Point won two starts back and three starts back, but he was pulled up last time out and returns after 237 days off, so fitness is the question.
    DATA: model 10.1% | style Prominent (led 8% of runs) | runs in data 3 | last 3: 23 Jan Doncaster Chase 24f Soft 1/4; 25 Feb Wincanton Chase 25.1f Good To Soft 1/5; 28 Mar Uttoxeter Chase 24f Good To Soft PU/10
    DATA for: Has won at this trip or further
    DATA against: Returns from a 237-day break; Pulled up in 1 of its last 3 jumps runs
- No Tackle (hrs_29592997) | 9yo G | 163lb | OR 110 | draw 0 | jockey Liam Harrison | trainer Robbie Llewellyn (14d 0/3) | headgear v | last run 30 days | form 2223-9 | MARKET 4.1% | 09:00 median 19.00 | Matchbook 27.00
    comment: The risk is that flop last time, which must be forgotten after 30 days off.
    DATA: model 5.7% | style Midfield (led 8% of runs) | runs in data 4 | last 3: 12 Feb Leicester Chase 20.1f Heavy 2/5; 21 Mar Bangor-on-Dee Chase 24.1f Good 3/5; 21 Oct Worcester Chase 16.5f Good To Soft 9/9
    DATA for: Good recent finishing positions
    DATA against: Last-run finishing speed -5.2% vs that field (faded)
- Vanderflier (hrs_41052144) | 6yo G | 162lb | OR 109 | draw 0 | jockey Kevin Brogan | trainer Jonjo & A.J. O'Neill (14d 6/31) | headgear p | wind surgery | last run 211 days | form 1/554- | MARKET 3.4% | 09:00 median 21.00 | Matchbook 32.00
    comment: Vanderflier is hard to fancy after 211 days off, having finished fourth last time out, then a fifth, a fifth and a winner four starts back, and he carries a hefty 162 lb.
    DATA: model 5.0% | style Midfield (led 5% of runs) | runs in data 3 | last 3: 7 Feb Warwick Hurdle 19f Heavy 5/7; 15 Mar Chepstow Hurdle 23.6f Soft 5/7; 23 Apr Warwick Hurdle 19f Good 4/10
    DATA for: Last-run finishing speed +2.9% vs that field (finished strongly)
    DATA against: Returns from a 211-day break; First run over fences in our data
- Esperti (hrs_25427703) | 9yo G | 159lb | OR 106 | draw 0 | jockey Jay Tidball(5) | trainer David Rees (14d 0/2) | headgear - | last run 174 days | form 211-23 | MARKET 2.7% | 09:00 median 26.00 | Matchbook 42.00
    DATA: model 10.6% | style Held up (led 8% of runs) | runs in data 7 | last 3: 21 Apr Ffos Las Chase 23.8f Good 1/9; 4 May Fakenham Chase 29.1f Good 2/10; 30 May Stratford Chase 27.5f Good To Firm 3/5
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Returns from a 174-day break
- Gold Clermont (hrs_21267190) | 10yo M | 160lb | OR 107 | draw 0 | jockey Chad Bament(5) | trainer Andy Irvine (14d 0/2) | headgear - | last run 195 days | form 9P31-P | MARKET 1.6% | 09:00 median 34.00 | Matchbook 120.00
    comment: Gold Clermont won two starts back and was third the run before, but she was pulled up last time out and returns after 195 days off, while carrying 160 lb.
    DATA: model 6.7% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 14 Mar Fontwell Hurdle 25.8f Soft 3/6; 24 Apr Fontwell Chase 26f Good 1/5; 9 May Hexham Chase 24.2f Good To Soft PU/8
    DATA for: Has won at this trip or further
    DATA against: Returns from a 195-day break; Pulled up in 2 of its last 5 jumps runs; Aged 10, older than most of this field

## 2:42 Chepstow | race_id rac_32304950327 | David Lucas Best Prices Welsh Sport Handicap Hurdle Race
Hurdle | Class 5 | 2m16y | going Soft | Turf | 12 runners | rating band 0-105 | age 3yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Northwest Passage (hrs_46109371) | 4yo G | 166lb | OR 96 | draw 0 | jockey William Shanahan(5) | trainer Ivan Furtado (14d 1/7) | headgear - | last run 7 days | form 75-31 | MARKET 36.7% | 09:00 median 2.25 | Matchbook 2.42
    comment: The main risk is the hefty 166 lb he must carry.
    DATA: model 13.3% | style Midfield (led 3% of runs) | runs in data 10 | last 3: 17 Sep Ayr Flat 13.1f Soft 3/11; 10 Oct York Flat 13.9f Good To Soft 3/12; 13 Nov Southwell Hurdle 16f Good 1/11 fig 107
    DATA for: Best recent form figure 107, 14 lb above field average; Recent figures 11 lb above its current mark (looks well handicapped); Has won at this trip or further; Good recent finishing positions
- Jollie Dame (hrs_51273306) | 5yo M | 166lb | OR 103 | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 16/78) | headgear - | last run 44 days | form 3334-1 | MARKET 15.8% | 09:00 median 4.50 | Matchbook 6.40
    comment: Jollie Dame won last time out, and she's been placed in three of her other four recent starts, though 44 days off is a fair break and 166 lb is a hefty burden.
    DATA: model 13.7% | style Midfield (led 3% of runs) | runs in data 6 | last 3: 31 Mar Bangor-on-Dee Hurdle 16.7f Good 3/7; 11 Apr Chepstow Hurdle 16.1f Good To Soft 4/9; 7 Oct Worcester Hurdle 16f Good 1/10
    DATA for: Trainer 21% wins (16/78), last 14 days; Last-run finishing speed +3.7% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
- Best Trump (hrs_49974407) | 5yo G | 158lb | OR 95 | draw 0 | jockey Harry Cobden | trainer Jonjo & A.J. O'Neill (14d 6/31) | headgear - | last run 16 days | form 1/05-4 | MARKET 10.3% | 09:00 median 7.50 | Matchbook 9.20
    comment: Best Trump was a fourth last time out and a fifth two starts back, having won four starts back, so he's been running respectably after just 16 days off.
    DATA: model 8.2% | style Prominent (led 4% of runs) | runs in data 3 | last 3: 9 Jan Exeter Hurdle 16.7f Good To Soft 11/14; 23 Mar Wincanton Hurdle 15.2f Good 5/12; 4 Nov Chepstow Hurdle 16f Good To Soft 4/12 fig 92
    DATA for: Carries 6 lb less than average
- Bouquet de Paris (hrs_50401638) | 4yo G | 156lb | OR 93 | draw 0 | jockey Sean Bowen | trainer Rebecca Curtis (14d 2/6) | headgear h | wind surgery | last run 196 days | form 5546-4 | MARKET 9.1% | 09:00 median 9.00 | Matchbook 10.00
    comment: Winless in his last five, with finishes of fourth last time out, a sixth, a fourth, then two fifths, and 196 days off the track is a big ask at 156 lb.
    DATA: model 9.4% | style Prominent (led 29% of runs) | runs in data 3 | last 3: 1 Mar Ffos Las Hurdle 15.8f Heavy 4/6; 6 Apr Hereford Hurdle 16.2f Good 6/10; 8 May Market Rasen Hurdle 16.6f Good 4/9
    DATA for: Trainer 33% wins (2/6), last 14 days; Carries 8 lb less than average
    DATA against: Official rating 93, 7 lb below field average; Returns from a 196-day break
- In Limbo (hrs_29622061) | 8yo G | 168lb | OR 105 | draw 0 | jockey Bryan Carver | trainer Chris Honour (14d 0/5) | headgear - | last run 23 days | form 4351/7 | MARKET 5.5% | 09:00 median 13.00 | Matchbook 19.00
    comment: The main risk is a seventh last time out, and he carries 168 lb off an official mark of 105.
    DATA: model 6.0% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 28 Oct Newton Abbot Hurdle 17f Good To Soft 7/8 fig 100
    DATA for: Best recent form figure 100, 6 lb above field average; Official rating 105, 5 lb above field average
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Both of Us (hrs_53181632) | 4yo G | 156lb | OR 93 | draw 0 | jockey Sam Twiston-Davies | trainer Kerry Lee (14d 1/5) | headgear tb | last run 6 days | form 33-477 | MARKET 5.0% | 09:00 median 15.00 | Matchbook 19.50
    DATA: model 6.3% | style Held up (led 4% of runs) | runs in data 6 | last 3: 17 Jun Worcester Hurdle 16f Good 4/8; 1 Jul Worcester Hurdle 16f Good 7/9; 14 Nov Uttoxeter Hurdle 16f Good 7/12 fig 75
    DATA for: Trainer 20% wins (1/5), last 14 days; Carries 8 lb less than average
    DATA against: Best recent form figure 75, 18 lb below field average; Recent figures 18 lb below its current mark (looks high in the weights); Official rating 93, 7 lb below field average; Pace: steady gallop likely, hard to come from off the pace
- Mistral St Georges (hrs_61910646) | 4yo G | 167lb | OR 104 | draw 0 | jockey Lorcan Murtagh | trainer Georgina Nicholls (14d 0/2) | headgear - | last run 223 days | form FU2- | MARKET 4.7% | 09:00 median 15.00 | Matchbook 23.00
    comment: Mistral St Georges was second last time out, but he unseated two starts back and fell three starts back, and returns after 223 days off.
    DATA: model 6.3% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 27 Feb Newbury Hurdle 16.3f Good To Soft F/9; 31 Mar Bangor-on-Dee Hurdle 16.7f Good UR/7; 11 Apr Chepstow Hurdle 16.1f Good To Soft 2/7
    DATA for: Last-run finishing speed +2.7% vs that field (finished strongly)
    DATA against: Returns from a 223-day break; Fell or unseated in 2 of its last 3 jumps runs
- Activist (hrs_30764545) | 7yo G | 168lb | OR 105 | draw 0 | jockey Rian Corcoran(5) | trainer David Pipe (14d 2/11) | headgear v | wind surgery | last run 266 days | form 54P28- | MARKET 4.7% | 09:00 median 17.00 | Matchbook 19.50
    comment: The risk is a 266-day absence, with an eighth last time out and 168 lb to carry.
    DATA: model 11.6% | style Held up (led 4% of runs) | runs in data 3 | last 3: 11 Jan Fontwell Hurdle 19.1f Soft PU/14; 9 Feb Plumpton Hurdle 20.5f Soft 2/6; 27 Feb Newbury Hurdle 20.5f Good To Soft 8/13
    DATA for: Official rating 105, 5 lb above field average
    DATA against: Last-run finishing speed -3.3% vs that field (faded); Returns from a 266-day break; Pulled up in 1 of its last 3 jumps runs; Pace: steady gallop likely, hard to come from off the pace
- Red N Yellow (hrs_46974830) | 5yo G | 166lb | OR 103 | draw 0 | jockey Callum Pritchard | trainer Philip Hobbs & Johnson White (14d 2/12) | headgear - | last run 620 days | form 222/ | MARKET 2.6% | 09:00 median 26.00 | Matchbook 44.00
    comment: Red N Yellow returns after 620 days off, which is the obvious hurdle, though he was second last time out, a second two starts back and another second three starts back, so he is yet to win in that sequence.
    DATA: model 7.0% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 620-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Mount Washington (hrs_34470681) | 7yo G | 159lb | OR 96 | draw 0 | jockey Adam Wedge | trainer Mrs C. Williams (14d 1/25) | headgear t | last run 593 days | form 61411/ | MARKET 2.3% | 09:00 median 26.00 | Matchbook 60.00
    comment: Mount Washington won last time out and two starts back, but he returns after 593 days off, carries 159 lb and has a yard struggling at one winner from 25.
    DATA: model 6.2% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 593-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Zambezi Fix (hrs_18504556) | 11yo G | 165lb | OR 102 | draw 0 | jockey Sean Houlihan | trainer Bernard Llewellyn (14d 0/2) | headgear p | last run 170 days | form 4066-2 | MARKET 2.1% | 09:00 median 29.00 | Matchbook 70.00
    comment: The 165 lb burden and 170 days off are the reservations, though he is yet to win in recent starts.
    DATA: model 7.9% | style Held up (led 4% of runs) | runs in data 3 | last 3: 30 Jan Ffos Las Hurdle 15.8f Heavy 6/7; 11 Apr Chepstow Hurdle 16.1f Good To Soft 6/9; 3 Jun Newton Abbot Hurdle 16.8f Good To Soft 2/12
    DATA against: Returns from a 170-day break; Aged 11, older than most of this field; Pace: steady gallop likely, hard to come from off the pace
- Golden Wings (hrs_58315971) | 5yo M | 167lb | OR 104 | draw 0 | jockey Joe Anderson(3) | trainer Grace Harris (14d 1/6) | headgear - | last run 50 days | form P-0708 | MARKET 1.1% | 09:00 median 51.00 | Matchbook 140.00
    comment: Golden Wings is winless in her last five, with an eighth last time out and a seventh three starts back leaving her some way off the pace, though she has run over today's trip.
    DATA: model 4.2% | style Midfield (led 3% of runs) | runs in data 6 | last 3: 3 Aug Cork Hurdle 17f Good 7/18; 28 Aug Down Royal Hurdle 17.4f Good 11/14; 1 Oct Clonmel Hurdle 19.7f Good 8/11
    DATA against: Poor recent finishing positions; Pulled up in 1 of its last 5 jumps runs

## 3:17 Chepstow | race_id rac_32304952264 | Free £5 Bet At David Lucas Open National Hunt Flat Race (Category 1 Elimination) (GBB Race)
NH Flat | Class 5 | 2m16y | going Good | Turf | 11 runners | rating band - | age 4-5yo
DATA pace: Unclear - Running styles known for only 2 of 11 runners.
- Hurricane Mick (hrs_17395687708) | 4yo G | 156lb | OR - | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 16/78) | headgear - | last run 215 days | form 1- | MARKET 38.6% | 09:00 median 2.25 | Matchbook 2.26
    comment: Hurricane Mick won last time out in his only recent start, but he returns after 215 days off and carries 156 lb. He is unexposed and open to improvement, though the long absence raises a fitness question.
    DATA: model 8.9% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 21% wins (16/78), last 14 days
    DATA against: Returns from a 215-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Lord Max (hrs_17395689794) | 4yo G | 156lb | OR - | draw 0 | jockey Callum Pritchard | trainer Philip Hobbs & Johnson White (14d 2/12) | headgear - | last run - days | form - | MARKET 13.0% | 09:00 median 6.00 | Matchbook 7.60
    comment: Lord Max is an unraced gelding with no recorded form, so he is totally unexposed and open to improvement on debut. He carries 156 lb, and there is nothing yet to show how he will handle the task.
    DATA: model 8.9% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Top Magneto (hrs_17395672063) | 4yo G | 156lb | OR - | draw 0 | jockey Sean Bowen | trainer Rebecca Curtis (14d 2/6) | headgear - | last run - days | form - | MARKET 12.3% | 09:00 median 6.50 | Matchbook 7.60
    comment: Top Magneto is an unraced gelding with no recorded form, so he's an unexposed sort who could well improve. He carries 156 lb on debut, and he's yet to win, so there's little to go on beyond that.
    DATA: model 8.9% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 33% wins (2/6), last 14 days
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Killygowan (hrs_52055262) | 5yo G | 156lb | OR - | draw 0 | jockey Toby Wynne | trainer Mel Rowley (14d 1/10) | headgear - | last run 190 days | form 2 | MARKET 8.0% | 09:00 median 10.00 | Matchbook 12.50
    comment: The reservation is a 190-day break, and he is yet to win in recent form while carrying 156 lb.
    DATA: model 14.0% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 14 May Perth NH Flat 16.2f Good To Soft 2/8
    DATA against: Returns from a 190-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Noble Calling (hrs_17394112778) | 5yo G | 156lb | OR - | draw 0 | jockey Nick Slatter(3) | trainer David Killahena & Graeme McPherson (14d 3/8) | headgear - | last run - days | form - | MARKET 7.3% | 09:00 median 11.00 | Matchbook 13.00
    comment: Unraced and unexposed, Noble Calling has no recorded form to go on, so he remains open to improvement on debut. He carries 156 lb, and his first run should reveal plenty about what he can do.
    DATA: model 8.9% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 38% wins (3/8), last 14 days
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Ceebeegeebee (hrs_17395682493) | 4yo G | 156lb | OR - | draw 0 | jockey Kielan Woods | trainer Fergal O'Brien (14d 3/30) | headgear - | last run - days | form - | MARKET 7.0% | 09:00 median 12.00 | Matchbook 13.50
    comment: Ceebeegeebee is an unexposed debutant with no recorded form to go on, so he is open to any amount of improvement.
    DATA: model 8.9% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Eddie The Gray (hrs_17395683536) | 4yo G | 156lb | OR - | draw 0 | jockey Charlie Deutsch | trainer Venetia Williams (14d 0/5) | headgear - | last run - days | form - | MARKET 3.8% | 09:00 median 26.00 | Matchbook 26.00
    comment: Eddie The Gray is unexposed with no recorded form to go on, so this gelding's debut is a leap into the unknown and he looks open to plenty of improvement. He carries 156 lb, and the lack of a previous run leaves him with scope to progress.
    DATA: model 8.9% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Hotter Than Dubai (hrs_60250106) | 5yo M | 149lb | OR - | draw 0 | jockey Bryan Carver | trainer Chris Honour (14d 0/5) | headgear - | last run 273 days | form 63- | MARKET 2.8% | 09:00 median 26.00 | Matchbook 40.00
    comment: The main risk is a 273-day absence, so fitness is the question.
    DATA: model 6.3% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 29 Jan Wincanton NH Flat 15.2f Heavy 6/10; 20 Feb Exeter NH Flat 16.7f Heavy 3/6
    DATA against: Returns from a 273-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- Cappanapeasta (hrs_17395681450) | 5yo M | 149lb | OR - | draw 0 | jockey Tom Bellamy | trainer David Killahena & Graeme McPherson (14d 3/8) | headgear - | last run - days | form - | MARKET 2.6% | 09:00 median 29.00 | Matchbook 46.00
    comment: Cappanapeasta is unraced, so this is a clean slate with no form to go on, and she remains wholly unexposed and open to improvement. She carries 149 lb on debut, and any step forward would be pure upside.
    DATA: model 8.1% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 38% wins (3/8), last 14 days
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Intense Appeal (hrs_17394497645) | 5yo G | 156lb | OR - | draw 0 | jockey Sam Twiston-Davies | trainer Oliver Signy (14d 0/3) | headgear t (1st time) | last run 196 days | form PU5R-7 | MARKET 2.3% | 09:00 median 34.00 | Matchbook 48.00
    comment: Lightly raced and unexposed, Intense Appeal returns after 196 days off, having finished seventh last time out and a fifth three starts back, so he is yet to win and could still improve, though his jumping record is patchy. He carries 156 lb.
    DATA: model 8.9% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: First-time headgear
    DATA against: Returns from a 196-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Moonlight Maverick (hrs_17395691880) | 4yo G | 156lb | OR - | draw 0 | jockey Kevin Brogan | trainer Jonjo & A.J. O'Neill (14d 6/31) | headgear - | last run - days | form - | MARKET 2.3% | 09:00 median 34.00 | Matchbook 55.00
    comment: Moonlight Maverick is an unexposed debutant with no form to go on, so he's open to any amount of improvement. He carries 156 lb on his first outing, and what he shows first time will be the telling part.
    DATA: model 8.9% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
