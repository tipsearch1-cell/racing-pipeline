# Card review packet: Carlisle, 2026-11-17

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
{"meeting": "carlisle", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 11:50 Carlisle | race_id rac_32304640407 | Margaret Long Memorial Maiden Hurdle Race (GBB Race)
Hurdle | Class 4 | 2m3f218y | going  | Turf | 14 runners | rating band - | age 4yo+
DATA pace: Even - Two likely leaders (Coconut Man, Galatrona). A fair, even gallop is most likely.
- They're Chancers (hrs_47985665) | 6yo G | 158lb | OR - | draw 0 | jockey Danny McMenamin | trainer Nicky Richards (14d 5/18) | headgear - | last run 323 days | form 1/2- | MARKET 23.5% | 09:00 median 3.75 | Matchbook 2.30 | CHECK (skip line 3.56)
    DATA: model 5.1% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 28% wins (5/18), last 14 days
    DATA against: Returns from a 323-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Coconut Man (hrs_51831409) | 5yo G | 158lb | OR - | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 19/78) | headgear - | wind surgery | last run 213 days | form 2/128- | MARKET 18.4% | 09:00 median 4.20 | Matchbook 4.50
    DATA: model 8.5% | style Leader (led 72% of runs) | runs in data 2 | last 3: 13 Jan Ayr 16f Heavy 2/8; 18 Apr Ayr 16f Heavy 8/9
    DATA for: Trainer 24% wins (19/78), last 14 days
    DATA against: Last-run finishing speed -2.6% vs that field (faded); Returns from a 213-day break; Lightly raced: 2 runs in our data, so the model has little to go on; First run over hurdles in our data
- Ar Ais Aris (hrs_58963058) | 5yo G | 158lb | OR - | draw 0 | jockey Derek Fox | trainer Lucinda Russell & Michael Scudamore (14d 9/37) | headgear - | last run 33 days | form 24-2 | MARKET 13.2% | 09:00 median 5.00 | Matchbook 8.60
    DATA: model 12.5% | style Prominent (led 38% of runs) | runs in data 2 | last 3: 24 Apr Perth 16.2f Good 4/11; 15 Oct Perth 20f Soft 2/8 fig 101
    DATA for: Trainer 24% wins (9/37), last 14 days
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Baron du Brizais (hrs_58745533) | 5yo G | 158lb | OR - | draw 0 | jockey Ben Jones | trainer Ben Pauling (14d 3/21) | headgear - | last run 234 days | form 12- | MARKET 13.1% | 09:00 median 6.00 | Matchbook -
    DATA: model 15.1% | style Unknown | runs in data 1 | last 3: 28 Mar Uttoxeter 15.8f Good To Soft 2/7
    DATA for: Last-run finishing speed +3.9% vs that field (finished strongly)
    DATA against: Returns from a 234-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Galatrona (hrs_60787685) | 5yo M | 151lb | OR - | draw 0 | jockey Jonathan Burke | trainer Charlie Longsdon (14d 2/14) | headgear - | last run 246 days | form 211- | MARKET 12.7% | 09:00 median 6.50 | Matchbook 5.40
    DATA: model 17.6% | style Leader (led 57% of runs) | runs in data 1 | last 3: 16 Mar Ffos Las 15.8f Soft 1/5
    DATA for: Last-run finishing speed +7.2% vs that field (finished strongly)
    DATA against: Returns from a 246-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Katagat (hrs_59742102) | 6yo G | 158lb | OR - | draw 0 | jockey Kielan Woods | trainer David Killahena & Graeme McPherson (14d 3/9) | headgear t | wind surgery | last run 292 days | form 33- | MARKET 5.6% | 09:00 median 13.00 | Matchbook 19.00
    DATA: model 8.3% | style Held up (led 8% of runs) | runs in data 1 | last 3: 29 Jan Ayr 16f Soft 3/7
    DATA for: Trainer 33% wins (3/9), last 14 days
    DATA against: Returns from a 292-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Billy Bob Junior (hrs_17394806373) | 5yo G | 158lb | OR - | draw 0 | jockey Mr Oran McGill(5) | trainer Noel C. Kelly (14d 2/7) | headgear - | last run 193 days | form 34-7 | MARKET 4.1% | 09:00 median 13.00 | Matchbook -
    DATA: model 5.1% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 29% wins (2/7), last 14 days
    DATA against: Returns from a 193-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Blofeld (hrs_46265359) | 7yo G | 158lb | OR - | draw 0 | jockey Charlie Maggs | trainer Rebecca Menzies (14d 1/9) | headgear - | last run 319 days | form 1/35- | MARKET 3.9% | 09:00 median 21.00 | Matchbook 18.00
    DATA: model 7.2% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 2 Jan Ayr 20.5f Soft 5/11
    DATA against: Returns from a 319-day break; Lightly raced: 1 run in our data, so the model has little to go on
- A Merry Walk (hrs_58565311) | 6yo G | 158lb | OR - | draw 0 | jockey Sean Quinlan | trainer Jennie Candlish (14d 3/18) | headgear h (1st time) | last run 226 days | form 4FU- | MARKET 1.4% | 09:00 median 67.00 | Matchbook -
    DATA: model 5.1% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: First-time headgear
    DATA against: Returns from a 226-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Absence of Ego (hrs_17394496602) | 5yo G | 158lb | OR - | draw 0 | jockey Patrick Wadge | trainer Lucinda Russell & Michael Scudamore (14d 9/37) | headgear - | last run 21 days | form 2-7 | MARKET 1.3% | 09:00 median 67.00 | Matchbook -
    DATA: model 4.9% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 27 Oct Newcastle 17f Good 7/9 fig 98
    DATA for: Trainer 24% wins (9/37), last 14 days
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Frompillartopost (hrs_17395515613) | 4yo G | 157lb | OR - | draw 0 | jockey Peter Kavanagh | trainer Jane Walton (14d 0/0) | headgear - | last run 192 days | form 54-1 | MARKET 1.0% | 09:00 median 81.00 | Matchbook -
    DATA: model 5.0% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 192-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Gili Island (hrs_61456122) | 4yo G | 157lb | OR - | draw 0 | jockey Tristan Durrell | trainer Dan Skelton (14d 19/78) | headgear - | last run 16 days | form 49-40 | MARKET 0.8% | 09:00 median 101.00 | Matchbook -
    DATA: model 3.2% | style Prominent (led 29% of runs) | runs in data 4 | last 3: 28 Apr Punchestown 16.6f Yielding 9/19; 11 Oct Chepstow 16.1f Good To Soft 4/6; 1 Nov Worcester 16f Good To Soft 14/16
    DATA for: Trainer 24% wins (19/78), last 14 days
    DATA against: Last-run finishing speed -5.0% vs that field (faded)
- Mymatemac (hrs_17395164122) | 4yo G | 157lb | OR - | draw 0 | jockey Ryan Mania | trainer Martin Todhunter (14d 0/5) | headgear - | last run 8 days | form U0 | MARKET 0.6% | 09:00 median 151.00 | Matchbook -
    DATA: model 1.3% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 9 Nov Carlisle 17f Good To Soft 12/14
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Marble Sky (hrs_60090184) | 5yo G | 158lb | OR - | draw 0 | jockey Oscar Palmer(7) | trainer Andrew Crook (14d 1/2) | headgear - | last run 257 days | form 09- | MARKET 0.4% | 09:00 median 201.00 | Matchbook -
    DATA: model 0.9% | style Held up (led 8% of runs) | runs in data 1 | last 3: 5 Mar Haydock 15.7f Good To Soft 9/10
    DATA against: Returns from a 257-day break; Lightly raced: 1 run in our data, so the model has little to go on

## 12:20 Carlisle | race_id rac_32304642344 | Vesta Wealth Galloping Gains 'Chasing Excellence' Novices' Steeple Chase (GBB Race)
Chase | Class 3 | 2m3f210y | going  | Turf | 6 runners | rating band - | age 4yo+
DATA pace: Strong pace - 3 habitual front-runners (Bossman Jack, Swindon Village, Tormund Giantsbane). A contested lead should set things up for horses coming from behind.
- Bossman Jack (hrs_44975007) | 6yo G | 158lb | OR 148 | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 19/78) | headgear - | last run 220 days | form 31161- | MARKET 57.8% | 09:00 median 1.50 | Matchbook 1.42
    DATA: model 20.6% | style Leader (led 57% of runs) | runs in data 4 | last 3: 13 Feb Chepstow 16.1f Soft 1/14; 11 Mar Cheltenham 21f Good 6/21; 11 Apr Aintree 20f Good To Soft 1/12
    DATA for: Official rating 148, 13 lb above field average; Trainer 24% wins (19/78), last 14 days; Last-run finishing speed +5.7% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Returns from a 220-day break; Race comments mention jumping mistakes in 4 of its last 4 runs; First run over fences in our data; Pace: likely to be taken on for the lead
- Kaka's Cousin (hrs_412693491) | 6yo G | 158lb | OR 128 | draw 0 | jockey Jonjo O'Neill Jr. | trainer Jonjo & A.J. O'Neill (14d 6/33) | headgear - | last run 220 days | form 12140- | MARKET 14.1% | 09:00 median 6.00 | Matchbook 5.00
    DATA: model 18.5% | style Prominent (led 5% of runs) | runs in data 4 | last 3: 13 Feb Kelso 16.2f Heavy 1/11; 7 Mar Sandown 19.8f Soft 4/17; 11 Apr Aintree 24.7f Good To Soft 11/22
    DATA against: Official rating 128, 7 lb below field average; Returns from a 220-day break; First run over fences in our data
- A Pai de Nom (hrs_46108132) | 6yo G | 158lb | OR 134 | draw 0 | jockey Tristan Durrell | trainer Dan Skelton (14d 19/78) | headgear - | last run 248 days | form 11312- | MARKET 8.5% | 09:00 median 11.00 | Matchbook 7.00
    DATA: model 26.6% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 10 Jan Kempton 21f Good 3/15; 7 Feb Newbury 24.3f Heavy 1/9; 14 Mar Uttoxeter 23.3f Soft 2/17
    DATA for: Trainer 24% wins (19/78), last 14 days; Last-run finishing speed +5.6% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Returns from a 248-day break; First run over fences in our data
- Kalkbrenner (hrs_47837195) | 6yo G | 158lb | OR 134 | draw 0 | jockey Ben Jones | trainer Ben Pauling (14d 3/21) | headgear - | last run 323 days | form 4/126- | MARKET 8.3% | 09:00 median 12.00 | Matchbook 7.00
    DATA: model 13.2% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 323-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Tormund Giantsbane (hrs_40647334) | 6yo G | 158lb | OR 136 | draw 0 | jockey Charlie Todd | trainer Dan Skelton (14d 19/78) | headgear - | last run 209 days | form /1412- | MARKET 5.8% | 09:00 median 17.00 | Matchbook 12.00
    DATA: model 14.3% | style Leader (led 72% of runs) | runs in data 2 | last 3: 27 Feb Doncaster 24.4f Good To Soft 1/4; 22 Apr Perth 23.9f Good 2/4
    DATA for: Trainer 24% wins (19/78), last 14 days; Last-run finishing speed +2.8% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Returns from a 209-day break; Lightly raced: 2 runs in our data, so the model has little to go on; Race comments mention jumping mistakes in 2 of its last 2 runs; First run over fences in our data; Pace: likely to be taken on for the lead
- Swindon Village (hrs_39568298) | 6yo G | 158lb | OR 132 | draw 0 | jockey David Bass | trainer Charlie Longsdon (14d 2/14) | headgear - | last run 221 days | form 13100- | MARKET 5.5% | 09:00 median 15.00 | Matchbook 20.00
    DATA: model 6.8% | style Leader (led 72% of runs) | runs in data 4 | last 3: 17 Feb Newbury 20.5f Soft 1/6; 13 Mar Cheltenham 24f Good To Soft 11/22; 10 Apr Aintree 20f Good To Soft 18/22
    DATA for: Has won at this trip or further
    DATA against: Last-run finishing speed -3.0% vs that field (faded); Returns from a 221-day break; Race comments mention jumping mistakes in 2 of its last 4 runs; First run over fences in our data; Pace: likely to be taken on for the lead

## 12:50 Carlisle | race_id rac_32304987130 | Crown & Thistle Novices' Hurdle Race (Go North Night Nurse Series Qualifier) (Div I) (GBB Race)
Hurdle | Class 4 | 2m1f33y | going  | Turf | 10 runners | rating band - | age 4yo+
DATA pace: Lone leader - Throatlash is the only habitual front-runner and may be allowed an easy lead.
- Doubly Blessed (hrs_52495310) | 5yo G | 154lb | OR - | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 19/78) | headgear - | last run 229 days | form 12- | MARKET 42.9% | 09:00 median 1.83 | Matchbook 2.18
    DATA: model 15.4% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 2 Apr Kelso 16.2f Good 2/6
    DATA for: Trainer 24% wins (19/78), last 14 days; Last-run finishing speed +5.7% vs that field (finished strongly)
    DATA against: Returns from a 229-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Throatlash (hrs_412693631) | 7yo G | 154lb | OR 117 | draw 0 | jockey Kielan Woods | trainer Donald McCain (14d 3/25) | headgear - | last run 214 days | form 111F6- | MARKET 19.0% | 09:00 median 4.33 | Matchbook 5.00
    DATA: model 26.3% | style Leader (led 29% of runs) | runs in data 3 | last 3: 17 Jan Haydock 19.9f Good To Soft 1/8; 14 Feb Haydock 19.9f Good To Soft F/11; 17 Apr Ayr 16.5f Soft 6/9
    DATA for: Has won at this trip or further; Pace: may get an uncontested lead
    DATA against: Last-run finishing speed -6.2% vs that field (faded); Returns from a 214-day break; Fell or unseated in 1 of its last 3 jumps runs; First run over hurdles in our data
- Hurlyburly (hrs_51800427) | 5yo G | 154lb | OR - | draw 0 | jockey Sean Quinlan | trainer Jedd O'Keeffe (14d 0/4) | headgear - | last run 218 days | form 4623- | MARKET 13.1% | 09:00 median 6.50 | Matchbook -
    DATA: model 10.4% | style Prominent (led 38% of runs) | runs in data 2 | last 3: 5 Mar Haydock 15.7f Good To Soft 2/10; 13 Apr Hexham 16.2f Good 3/11
    DATA for: Last-run finishing speed +5.2% vs that field (finished strongly); Good recent finishing positions
    DATA against: Returns from a 218-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- Abbey Farmer (hrs_17395518742) | 5yo G | 154lb | OR - | draw 0 | jockey Danny McMenamin | trainer Nicky Richards (14d 5/18) | headgear - | last run - days | form - | MARKET 7.9% | 09:00 median 11.00 | Matchbook -
    DATA: model 5.9% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 28% wins (5/18), last 14 days
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Linalene (hrs_46850888) | 5yo G | 154lb | OR 105 | draw 0 | jockey Patrick Wadge | trainer Lucinda Russell & Michael Scudamore (14d 9/37) | headgear - | wind surgery | last run 33 days | form 4722-7 | MARKET 6.8% | 09:00 median 12.00 | Matchbook -
    DATA: model 19.9% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 23 Feb Ayr 16f Soft 2/5; 17 Apr Ayr 16f Soft 2/8; 15 Oct Perth 16f Soft 7/9 fig 87
    DATA for: Trainer 24% wins (9/37), last 14 days; Good recent finishing positions
    DATA against: Race comments mention jumping mistakes in 2 of its last 3 runs
- Aye Over Tee (hrs_17394124251) | 4yo G | 154lb | OR - | draw 0 | jockey Jonjo O'Neill Jr. | trainer Jonjo & A.J. O'Neill (14d 6/33) | headgear - | last run 13 days | form 04 | MARKET 2.9% | 09:00 median 26.00 | Matchbook -
    DATA: model 4.4% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 22 Oct Carlisle 17f Good 10/13; 4 Nov Chepstow 16f Good To Soft 4/13
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Kapoutchino (hrs_17394720847) | 6yo G | 154lb | OR - | draw 0 | jockey Bruce Lynn | trainer N. W. Alexander (14d 1/12) | headgear - | last run 561 days | form 2- | MARKET 2.7% | 09:00 median 34.00 | Matchbook -
    DATA: model 5.9% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 561-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Handball Maradona (hrs_17395262164) | 4yo G | 154lb | OR - | draw 0 | jockey Craig Nichol | trainer Sandy Thomson (14d 3/9) | headgear - | last run 198 days | form 53- | MARKET 2.6% | 09:00 median 34.00 | Matchbook -
    DATA: model 5.9% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 33% wins (3/9), last 14 days
    DATA against: Returns from a 198-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- The Foreman (hrs_30084992) | 8yo G | 154lb | OR - | draw 0 | jockey Peter Kavanagh | trainer Joel Parkinson & Sue Smith (14d 1/11) | headgear - | last run 254 days | form 8/66- | MARKET 1.3% | 09:00 median 67.00 | Matchbook -
    DATA: model 4.6% | style Held up (led 5% of runs) | runs in data 2 | last 3: 16 Feb Carlisle 17f Good To Soft 6/10; 8 Mar Carlisle 17f Good To Soft 6/10
    DATA against: Returns from a 254-day break; Lightly raced: 2 runs in our data, so the model has little to go on; Aged 8, older than most of this field
- Lecanvey Lady (hrs_17393085423) | 5yo M | 147lb | OR - | draw 0 | jockey Callum Bewley | trainer Martin Todhunter (14d 0/5) | headgear - | last run 12 days | form P-6P4 | MARKET 0.9% | 09:00 median 101.00 | Matchbook -
    DATA: model 1.2% | style Held up (led 5% of runs) | runs in data 2 | last 3: 22 Oct Carlisle 17f Good PU/13; 5 Nov Newcastle 20.5f Good 4/8 fig 91
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Pulled up in 1 of its last 2 jumps runs

## 1:25 Carlisle | race_id rac_32304644281 | Crown & Thistle Novices' Hurdle Race (Go North Night Nurse Series Qualifier) (Div II) (GBB Race)
Hurdle | Class 4 | 2m1f33y | going  | Turf | 9 runners | rating band - | age 4yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Turbocharged (hrs_58196558) | 5yo G | 154lb | OR - | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 19/78) | headgear - | wind surgery | last run 257 days | form 31- | MARKET 55.8% | 09:00 median 1.44 | Matchbook 1.48
    DATA: model 27.6% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 5 Mar Haydock 15.7f Good To Soft 1/10
    DATA for: Trainer 24% wins (19/78), last 14 days; Last-run finishing speed +8.1% vs that field (finished strongly)
    DATA against: Returns from a 257-day break; Lightly raced: 1 run in our data, so the model has little to go on
- St Michael's Well (hrs_17394719804) | 6yo G | 154lb | OR - | draw 0 | jockey Danny McMenamin | trainer Joel Parkinson & Sue Smith (14d 1/11) | headgear - | last run 17 days | form 661-4 | MARKET 12.3% | 09:00 median 6.00 | Matchbook 8.80
    DATA: model 4.7% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 31 Oct Wetherby 16f Good 4/6 fig 102
    DATA for: Best recent form figure 102, 12 lb above field average
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Bohemond Antioch (hrs_45856041) | 5yo G | 154lb | OR 113 | draw 0 | jockey Kielan Woods | trainer Donald McCain (14d 3/25) | headgear - | last run 214 days | form /22U7- | MARKET 11.6% | 09:00 median 6.50 | Matchbook 5.00
    DATA: model 13.9% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 17 Apr Ayr 16f Soft 7/8
    DATA against: Last-run finishing speed -6.4% vs that field (faded); Returns from a 214-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Biscuit Billy (hrs_17395260078) | 5yo G | 154lb | OR - | draw 0 | jockey Craig Nichol | trainer Sandy Thomson (14d 3/9) | headgear - | last run - days | form - | MARKET 4.9% | 09:00 median 19.00 | Matchbook -
    DATA: model 7.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 33% wins (3/9), last 14 days
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Onyerbike (hrs_17395519785) | 7yo G | 154lb | OR - | draw 0 | jockey Jack Power(5) | trainer Lucinda Russell & Michael Scudamore (14d 9/37) | headgear - | last run 583 days | form 6P112/ | MARKET 4.8% | 09:00 median 17.00 | Matchbook -
    DATA: model 7.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 24% wins (9/37), last 14 days
    DATA against: Returns from a 583-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Pedro The Poet (hrs_58347534) | 5yo G | 154lb | OR - | draw 0 | jockey Callum Bewley | trainer Nicky Richards (14d 5/18) | headgear - | last run 32 days | form 60- | MARKET 4.8% | 09:00 median 17.00 | Matchbook 22.00
    DATA: model 16.3% | style Held up (led 3% of runs) | runs in data 9 | last 3: 8 Sep Catterick 13.9f Good To Soft 4/6; 23 Sep Redcar 7f Good 2/12; 16 Oct Redcar 10f Good 3/14 fig 70
    DATA for: Trainer 28% wins (5/18), last 14 days; Good recent finishing positions
    DATA against: Best recent form figure 70, 20 lb below field average; First run over hurdles in our data; Pace: steady gallop likely, hard to come from off the pace
- Royal March (hrs_44975168) | 5yo G | 154lb | OR - | draw 0 | jockey Bruce Lynn | trainer N. W. Alexander (14d 1/12) | headgear - | last run 24 days | form 2-4 | MARKET 3.3% | 09:00 median 26.00 | Matchbook -
    DATA: model 11.4% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 14 Apr Market Rasen 16.6f Good 2/8; 24 Oct Kelso 16f Good 4/6 fig 98
    DATA for: Best recent form figure 98, 8 lb above field average
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Rupert The Prince (hrs_50036413) | 4yo G | 154lb | OR - | draw 0 | jockey Shane Fitzgerald | trainer Rebecca Menzies (14d 1/9) | headgear t (1st time) | last run 136 days | form 8-2 | MARKET 1.5% | 09:00 median 67.00 | Matchbook -
    DATA: model 8.9% | style Midfield (led 4% of runs) | runs in data 6 | last 3: 17 May Ripon 16f Good 4/6; 8 Jun Pontefract 17.1f Good 12/12; 4 Jul Carlisle 17.2f Good 5/6
    DATA for: First-time headgear
    DATA against: Last-run finishing speed -5.0% vs that field (faded); Returns from a 136-day break
- Teescomponents Gal (hrs_63810103) | 5yo M | 147lb | OR - | draw 0 | jockey Jamie Hamilton | trainer Gillian Boanas (14d 0/2) | headgear - | last run 195 days | form 6-9 | MARKET 0.8% | 09:00 median 126.00 | Matchbook -
    DATA: model 2.2% | style Held up (led 5% of runs) | runs in data 2 | last 3: 20 Apr Kelso 16.2f Good 6/6; 6 May Kelso 16.2f Good 9/10
    DATA against: Last-run finishing speed -7.0% vs that field (faded); Returns from a 195-day break; Lightly raced: 2 runs in our data, so the model has little to go on; First run over hurdles in our data; Pace: steady gallop likely, hard to come from off the pace

## 1:55 Carlisle | race_id rac_32304646218 | Settle With Claims Care Consultants Handicap Hurdle Race
Hurdle | Class 5 | 3m123y | going  | Turf | 12 runners | rating band 0-100 | age 4yo+
DATA pace: Lone leader - Junior des Mottes is the only habitual front-runner and may be allowed an easy lead.
- King Berry (hrs_44295426) | 5yo G | 155lb | OR 87 | draw 0 | jockey David Bass | trainer Max Comley (14d 2/8) | headgear tp (1st time) | last run 27 days | form 0872-5 | MARKET 20.2% | 09:00 median 3.75 | Matchbook 4.20 | CHECK (skip line 3.56)
    comment: King Berry was a fifth last time out and a second two starts back, though he is winless in his last five and was eighth four starts back.
    DATA: model 10.0% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 21 Mar Newbury 16.3f Good To Soft 7/8; 21 Apr Ffos Las 20f Good 2/10; 21 Oct Worcester 20f Good To Soft 5/10 fig 84
    DATA for: Trainer 25% wins (2/8), last 14 days; Last-run finishing speed +3.5% vs that field (finished strongly); Carries 6 lb less than average; First-time headgear
    DATA against: Official rating 87, 6 lb below field average
- Coventry (hrs_16762907) | 9yo G | 154lb | OR 86 | draw 0 | jockey Peter Kavanagh | trainer Lisa Harrison (14d 0/1) | headgear - | last run 17 days | form 67-171 | MARKET 14.6% | 09:00 median 5.50 | Matchbook -
    comment: Coventry arrives in good heart, a winner last time out and again three starts back, with only 17 days since that run, but the form is patchy, with a seventh in between and a seventh and a sixth before that.
    DATA: model 14.6% | style Held up (led 4% of runs) | runs in data 3 | last 3: 24 Sep Perth 20.2f Good 1/12; 22 Oct Carlisle 20f Good 7/13 fig 78; 31 Oct Ayr 24.5f Good To Soft 1/12 fig 83
    DATA for: Has won at this trip or further; Good recent finishing positions; Carries 7 lb less than average
    DATA against: Best recent form figure 83, 4 lb below field average; Official rating 86, 7 lb below field average
- Junior des Mottes (hrs_34457038) | 7yo G | 154lb | OR 86 | draw 0 | jockey Derek Fox | trainer Leonard Kerr (14d 0/2) | headgear p | last run 17 days | form 1132-3 | MARKET 11.8% | 09:00 median 6.00 | Matchbook 10.00
    DATA: model 9.0% | style Leader (led 54% of runs) | runs in data 6 | last 3: 4 Mar Catterick 25.3f Good 3/8; 14 Mar Fontwell 21.7f Soft 2/5; 31 Oct Ayr 24.5f Good To Soft 3/12 fig 85
    DATA for: Has won at this trip or further; Good recent finishing positions; Carries 7 lb less than average; Pace: may get an uncontested lead
    DATA against: Official rating 86, 7 lb below field average
- Half Track (hrs_23433627) | 10yo G | 156lb | OR 88 | draw 0 | jockey Bruce Lynn | trainer N. W. Alexander (14d 1/12) | headgear - | last run 26 days | form 8U5P-3 | MARKET 11.1% | 09:00 median 7.50 | Matchbook -
    comment: Third last time out suggests Half Track is finding form, though he is winless in his last five and has pulled up and unseated in that spell.
    DATA: model 5.9% | style Prominent (led 38% of runs) | runs in data 2 | last 3: 27 Jan Newcastle 23.7f Soft PU/9; 22 Oct Carlisle 20f Good 3/13 fig 88
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Pulled up in 1 of its last 2 jumps runs
- Ebselysees (hrs_40075602) | 7yo M | 168lb | OR 100 | draw 0 | jockey Nathan Moscrop | trainer Susan Corbett (14d 0/5) | headgear b | last run 24 days | form -15544 | MARKET 9.1% | 09:00 median 9.00 | Matchbook -
    comment: Ebselysees has finished fourth, fourth, fifth and fifth in her last four runs, and her only win came five starts back, so she looks short of a winning edge.
    DATA: model 10.1% | style Prominent (led 3% of runs) | runs in data 7 | last 3: 12 Jul Perth 23.9f Good 5/7; 8 Oct Market Rasen 23.1f Good 4/8; 24 Oct Kelso 22.5f Good 4/9 fig 99
    DATA for: Best recent form figure 99, 12 lb above field average; Official rating 100, 7 lb above field average; Has won at this trip or further
    DATA against: Carries 7 lb more than average
- Wasdell Dundalk (hrs_18602626) | 11yo G | 166lb | OR 98 | draw 0 | jockey Danny McMenamin | trainer Lisa Harrison (14d 0/1) | headgear - | wind surgery | last run 54 days | form 642P46 | MARKET 6.6% | 09:00 median 13.00 | Matchbook -
    DATA: model 5.3% | style Held up (led 3% of runs) | runs in data 6 | last 3: 12 Jul Perth 23.8f Good PU/7; 7 Sep Perth 23.8f Good 4/4; 24 Sep Perth 23.8f Good 6/9
    DATA for: Official rating 98, 5 lb above field average
    DATA against: Carries 5 lb more than average; Race comments mention jumping mistakes in 3 of its last 5 runs; Pulled up in 1 of its last 5 jumps runs
- Hopeless Dancer (hrs_56338324) | 5yo G | 165lb | OR 97 | draw 0 | jockey Harry Reed | trainer Tim Reed (14d 0/1) | headgear - | last run 11 days | form 2232-8 | MARKET 6.2% | 09:00 median 13.00 | Matchbook -
    comment: Hopeless Dancer is a consistent sort, with a second, a third and another second in his three starts before an eighth last time out, and he's back quickly after 11 days.
    DATA: model 4.4% | style Held up (led 8% of runs) | runs in data 1 | last 3: 6 Nov Hexham 20f Good 8/9 fig 83
    DATA against: Best recent form figure 83, 4 lb below field average; Recent figures 14 lb below its current mark (looks high in the weights); Last-run finishing speed -5.5% vs that field (faded); Lightly raced: 1 run in our data, so the model has little to go on
- Shoeshine Boy (hrs_23274181) | 10yo G | 167lb | OR 99 | draw 0 | jockey Craig Nichol | trainer Donald Whillans (14d 0/2) | headgear - | last run 26 days | form 135-P0 | MARKET 5.9% | 09:00 median 13.00 | Matchbook 19.00
    comment: Shoeshine Boy has tailed off since a win five starts back, with a fifth three starts back, then pulled up and unplaced last time, though he has run over today's trip and returns after 26 days.
    DATA: model 5.5% | style Midfield (led 3% of runs) | runs in data 6 | last 3: 17 Apr Ayr 24.3f Soft 5/15; 13 May Perth 26.6f Good To Soft PU/11; 22 Oct Carlisle 20f Good 12/13
    DATA for: Official rating 99, 6 lb above field average; Has won at this trip or further
    DATA against: Carries 6 lb more than average; Pulled up in 1 of its last 5 jumps runs
- Raceview Road (hrs_34166573) | 8yo G | 157lb | OR 89 | draw 0 | jockey Jonathon Bewley | trainer George Bewley (14d 0/6) | headgear - | last run 229 days | form /647P- | MARKET 5.0% | 09:00 median 17.00 | Matchbook -
    comment: Raceview Road was pulled up last time out and returns after 229 days off, with a seventh and a fourth before that leaving him winless in his last four starts.
    DATA: model 9.2% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 2 Jan Ayr 20.5f Soft 4/19; 3 Feb Carlisle 24.5f Good To Soft 7/14; 2 Apr Kelso 23.4f Good PU/8
    DATA against: Returns from a 229-day break; Pulled up in 1 of its last 3 jumps runs
- Kalo Athena (hrs_39431448) | 7yo M | 154lb | OR 86 | draw 0 | jockey Leah Noreci(7) | trainer James Moffatt (14d 0/4) | headgear - | last run 255 days | form 57124- | MARKET 4.0% | 09:00 median 23.00 | Matchbook -
    DATA: model 10.6% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 27 Jan Newcastle 23.7f Soft 2/9; 7 Mar Ayr 24.3f Soft 4/6
    DATA for: Carries 7 lb less than average
    DATA against: Official rating 86, 7 lb below field average; Returns from a 255-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- Shighness (hrs_23500365) | 9yo M | 166lb | OR 98 | draw 0 | jockey Joshua Thompson(5) | trainer Micky Hammond (14d 0/15) | headgear p | last run 182 days | form 663F-U | MARKET 3.6% | 09:00 median 23.00 | Matchbook -
    comment: The main risk is a 182-day absence, with a fall and an unseated rider in her last two outings.
    DATA: model 7.9% | style Midfield (led 4% of runs) | runs in data 4 | last 3: 19 Feb Sedgefield 27f Soft 3/7; 25 Mar Hexham 31.9f Soft F/11; 19 May Hexham 23.3f Good UR/11
    DATA for: Official rating 98, 5 lb above field average
    DATA against: Trainer 0 wins from 15 runs, last 14 days; Carries 5 lb more than average; Returns from a 182-day break; Fell or unseated in 2 of its last 4 jumps runs
- Prince des Fichaux (hrs_29295336) | 9yo G | 167lb | OR 99 | draw 0 | jockey Callum Bewley | trainer Ewan Whillans (14d 0/15) | headgear tp | last run 571 days | form 3P45P/ | MARKET 2.0% | 09:00 median 34.00 | Matchbook 80.00
    comment: He has run over today's trip and finished a fifth two starts back, though 571 days off and a pulled up last time out are the big worry.
    DATA: model 7.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Official rating 99, 6 lb above field average
    DATA against: Trainer 0 wins from 15 runs, last 14 days; Carries 6 lb more than average; Returns from a 571-day break; Lightly raced: 0 runs in our data, so the model has little to go on

## 2:25 Carlisle | race_id rac_32304648155 | DJ Bell Celebration Handicap Hurdle Race (Go North Sea Pigeon Series Qualifier)
Hurdle | Class 4 | 2m1f33y | going  | Turf | 17 runners | rating band 0-120 | age 3yo+
DATA pace: Strong pace - 5 habitual front-runners (Doyen du Bar, Cavalier du Luy, Two Auld Pals, Dark Tide Rising, Travis Wheatley). A contested lead should set things up for horses coming from behind.
- Doyen du Bar (hrs_24277197) | 10yo G | 170lb | OR 122 | draw 0 | jockey Danny McMenamin | trainer Nicky Richards (14d 5/18) | headgear - | last run 262 days | form /3231- | MARKET 28.2% | 09:00 median 2.75 | Matchbook 2.00
    DATA: model 16.2% | style Leader (led 57% of runs) | runs in data 2 | last 3: 16 Jan Market Rasen 21.4f Good To Soft 3/8; 28 Feb Kelso 17.1f Good To Soft 1/8
    DATA for: Official rating 122, 11 lb above field average; Trainer 28% wins (5/18), last 14 days; Last-run finishing speed +3.2% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Carries 11 lb more than average; Returns from a 262-day break; Lightly raced: 2 runs in our data, so the model has little to go on; First run over hurdles in our data; Aged 10, older than most of this field; Pace: likely to be taken on for the lead
- Razors Edge (hrs_49544306) | 6yo G | 161lb | OR 113 | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 19/78) | headgear t | last run 323 days | form 34- | MARKET 18.5% | 09:00 median 4.00 | Matchbook -
    comment: Razors Edge was fourth last time out, and a third two starts back, but he's winless in his last two and returns after 323 days off, which is a big question mark.
    DATA: model 4.6% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 24% wins (19/78), last 14 days
    DATA against: Returns from a 323-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Double Digits (hrs_32682636) | 8yo G | 159lb | OR 111 | draw 0 | jockey Joshua Thompson(5) | trainer Ann Hamilton (14d 2/4) | headgear - | last run 30 days | form 4-2253 | MARKET 9.3% | 09:00 median 8.00 | Matchbook -
    comment: Double Digits is yet to win in his last five starts but has been consistent, finishing third last time out and a second three starts back, and he has run over today's trip.
    DATA: model 9.8% | style Midfield (led 3% of runs) | runs in data 7 | last 3: 24 May Kelso 16.2f Good 2/8; 2 Oct Hexham 16.2f Good 5/7; 18 Oct Sedgefield 17f Good 3/9 fig 111
    DATA for: Best recent form figure 111, 13 lb above field average; Good recent finishing positions
- Dark Tide Rising (hrs_17390790823) | 4yo G | 153lb | OR 105 | draw 0 | jockey Jonathan England | trainer Sam England (14d 5/23) | headgear - | last run 38 days | form -43123 | MARKET 7.2% | 09:00 median 9.50 | Matchbook -
    comment: Dark Tide Rising arrives in cracking nick, with a third last time out, a second two starts back and a win three starts back, and he has run over today's trip before.
    DATA: model 12.9% | style Leader (led 57% of runs) | runs in data 4 | last 3: 4 Sep Worcester 16f Good 1/9; 2 Oct Hexham 16.2f Good 2/6; 10 Oct Hexham 16.2f Good 3/9
    DATA for: Trainer 22% wins (5/23), last 14 days; Last-run finishing speed +3.5% vs that field (finished strongly); Good recent finishing positions; Carries 6 lb less than average
    DATA against: Official rating 105, 6 lb below field average; Pace: likely to be taken on for the lead
- Travis Wheatley (hrs_41346277) | 6yo G | 150lb | OR 102 | draw 0 | jockey Jack Power(5) | trainer Adam Nicol (14d 1/9) | headgear p | last run 24 days | form 813-83 | MARKET 4.7% | 09:00 median 12.00 | Matchbook 26.00
    comment: Travis Wheatley was third last time out, 24 days ago, but a eighth two starts back and another eighth five starts back make him hard to trust, and he carries 150 lb.
    DATA: model 6.5% | style Leader (led 43% of runs) | runs in data 6 | last 3: 17 Apr Ayr 20.5f Soft 3/9; 24 May Kelso 20.9f Good 8/12; 24 Oct Kelso 16f Good 3/6 fig 100
    DATA for: Has won at this trip or further; Good recent finishing positions; Carries 9 lb less than average
    DATA against: Official rating 102, 9 lb below field average; Race comments mention jumping mistakes in 2 of its last 5 runs; Pace: likely to be taken on for the lead
- Cavalier du Luy (hrs_49757806) | 5yo G | 159lb | OR 111 | draw 0 | jockey Bruce Lynn | trainer N. W. Alexander (14d 1/12) | headgear t (1st time) | wind surgery | last run 17 days | form /215-P | MARKET 4.1% | 09:00 median 17.00 | Matchbook -
    comment: Cavalier du Luy won three starts back and was a second four starts back, but he was pulled up last time out and is a fifth two runs ago, so the form has cooled.
    DATA: model 6.4% | style Leader (led 38% of runs) | runs in data 2 | last 3: 29 Jan Ayr 16f Soft 5/8; 31 Oct Ayr 20.5f Good To Soft PU/10
    DATA for: First-time headgear
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Pulled up in 1 of its last 2 jumps runs; Pace: likely to be taken on for the lead
- Chisum (hrs_49757722) | 6yo G | 154lb | OR 106 | draw 0 | jockey William Shanahan(5) | trainer Jennie Candlish (14d 3/18) | headgear - | last run 383 days | form 9/43- | MARKET 3.7% | 09:00 median 21.00 | Matchbook -
    comment: He also carries 154 lb off a mark of 106.
    DATA: model 4.1% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 383-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Two Auld Pals (hrs_26782931) | 8yo G | 154lb | OR 106 | draw 0 | jockey Derek Fox | trainer Lucinda Russell & Michael Scudamore (14d 9/37) | headgear - | last run 24 days | form 8-1436 | MARKET 3.6% | 09:00 median 17.00 | Matchbook -
    comment: Two Auld Pals was sixth last time out and has only the one win in his last five starts, a fourth-start-back success, so he is hard to fancy when carrying 154 lb.
    DATA: model 6.3% | style Leader (led 38% of runs) | runs in data 7 | last 3: 18 Sep Ayr 13.1f Soft 7/10; 2 Oct Hexham 16.2f Good 3/7; 24 Oct Kelso 16f Good 6/6 fig 95
    DATA for: Trainer 24% wins (9/37), last 14 days
    DATA against: Recent figures 11 lb below its current mark (looks high in the weights); Last-run finishing speed -3.1% vs that field (faded); Race comments mention jumping mistakes in 2 of its last 5 runs; Pace: likely to be taken on for the lead
- Maree Verte (hrs_52615290) | 4yo F | 160lb | OR 112 | draw 0 | jockey Kielan Woods | trainer Donald McCain (14d 3/25) | headgear - | wind surgery | last run 563 days | form 1/1- | MARKET 3.5% | 09:00 median 19.00 | Matchbook 29.00
    comment: Unexposed filly who won last time out and again two starts back, though she returns after a 563-day absence, so fitness is the question. Carrying 160 lb off an official mark of 112, she looks open to further improvement.
    DATA: model 4.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 563-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Mick Collins (hrs_40668957) | 5yo G | 170lb | OR 122 | draw 0 | jockey Ryan Mania | trainer Martin Todhunter (14d 0/5) | headgear h | last run 52 days | form 2246-2 | MARKET 3.0% | 09:00 median 23.00 | Matchbook -
    comment: Mick Collins was second last time out and has finished second in three of his last five starts, so he is consistently in the frame, and he has run over today's trip. The one concern is a 52-day absence, plus 170 lb on his back.
    DATA: model 4.9% | style Midfield (led 4% of runs) | runs in data 4 | last 3: 25 Jul Newcastle 12.4f Standard To Slow 7/13; 12 Sep Chester 12.3f Soft 5/11; 26 Sep Haydock 14f Heavy 6/9
    DATA for: Official rating 122, 11 lb above field average
    DATA against: Last-run finishing speed -3.9% vs that field (faded); Carries 11 lb more than average; First run over hurdles in our data
- Rewired (hrs_22488018) | 8yo G | 158lb | OR 110 | draw 0 | jockey Harry Reed | trainer Tristan Davidson (14d 1/5) | headgear - | last run 11 days | form /13-87 | MARKET 2.7% | 09:00 median 21.00 | Matchbook -
    comment: Rewired won four starts back and was third three starts back, but he has since finished an eighth and a seventh last time out, so the form is trending the wrong way. He is fresh enough after 11 days and has run over today's trip, though 158 lb is a hefty burden.
    DATA: model 2.7% | style Held up (led 3% of runs) | runs in data 4 | last 3: 21 Sep Hamilton 12.1f Soft 11/12; 18 Oct Sedgefield 17f Good 8/9 fig 102; 6 Nov Aintree 17f Good To Soft 7/10 fig 104
    DATA for: Best recent form figure 104, 6 lb above field average; Trainer 20% wins (1/5), last 14 days; Pace: a contested lead should suit its hold-up style
    DATA against: Recent figures 6 lb below its current mark (looks high in the weights); Poor recent finishing positions
- Monaco Rules (hrs_40625319) | 6yo G | 158lb | OR 110 | draw 0 | jockey Conor O'Farrell | trainer Micky Hammond (14d 0/15) | headgear - | last run 192 days | form P/42-7 | MARKET 2.6% | 09:00 median 34.00 | Matchbook -
    comment: Monaco Rules showed some promise with a second two starts back, but he was only seventh last time and returns after 192 days off, so fitness is a question.
    DATA: model 4.7% | style Held up (led 8% of runs) | runs in data 1 | last 3: 9 May Hexham 20.1f Good To Soft 7/12
    DATA for: Pace: a contested lead should suit its hold-up style
    DATA against: Trainer 0 wins from 15 runs, last 14 days; Returns from a 192-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Colegram (hrs_41052592) | 6yo M | 153lb | OR 105 | draw 0 | jockey Tristan Durrell | trainer Dan Skelton (14d 19/78) | headgear - | last run 12 days | form 1-3180 | MARKET 2.2% | 09:00 median 34.00 | Matchbook -
    comment: Colegram has won two of her last five, but she was unplaced last time and an eighth two starts back, so the form has cooled, and 153 lb is a big burden.
    DATA: model 4.1% | style Prominent (led 3% of runs) | runs in data 4 | last 3: 26 Jun Bangor-on-Dee 19.6f Good 1/7; 24 Jul Uttoxeter 23.3f Good 8/16; 5 Nov Newbury 16.5f Good To Soft 13/16 fig 93
    DATA for: Trainer 24% wins (19/78), last 14 days; Has won at this trip or further; Carries 6 lb less than average
    DATA against: Best recent form figure 93, 5 lb below field average; Recent figures 12 lb below its current mark (looks high in the weights); Official rating 105, 6 lb below field average
- Dee's Getaway (hrs_40806241) | 6yo M | 151lb | OR 103 | draw 0 | jockey Jonathon Bewley | trainer George Bewley (14d 0/6) | headgear - | last run 17 days | form 0017-9 | MARKET 2.2% | 09:00 median 34.00 | Matchbook -
    comment: She has run over today's trip and is fit after 17 days, but 151 lb is a stiff burden.
    DATA: model 4.0% | style Held up (led 4% of runs) | runs in data 4 | last 3: 25 Mar Hexham 16.2f Soft 1/9; 13 Apr Hexham 16.2f Good 7/8; 31 Oct Ayr 16f Good To Soft 9/9 fig 84
    DATA for: Carries 8 lb less than average; Pace: a contested lead should suit its hold-up style
    DATA against: Best recent form figure 84, 14 lb below field average; Recent figures 19 lb below its current mark (looks high in the weights); Official rating 103, 8 lb below field average; Race comments mention jumping mistakes in 2 of its last 4 runs
- Foster's Fortune (hrs_37889810) | 7yo G | 160lb | OR 112 | draw 0 | jockey Charlie Maggs | trainer Chris Grant (14d 0/3) | headgear - | last run 605 days | form 2123P/ | MARKET 1.8% | 09:00 median 41.00 | Matchbook -
    comment: Pulled up last time out after a third two starts back, a second three starts back and a win four starts back, Foster's Fortune has solid recent form but returns from 605 days off, carrying 160 lb, and has run over today's trip.
    DATA: model 4.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 605-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- How About No (hrs_37613569) | 6yo G | 161lb | OR 113 | draw 0 | jockey Sean Quinlan | trainer Lizzie Quinlan (14d 2/10) | headgear v (1st time) | last run 208 days | form /54PP- | MARKET 1.5% | 09:00 median 51.00 | Matchbook -
    DATA: model 2.8% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 1 Feb Musselburgh 19.8f Good To Soft PU/12; 23 Apr Perth 16.2f Good PU/12
    DATA for: Trainer 20% wins (2/10), last 14 days; First-time headgear
    DATA against: Returns from a 208-day break; Lightly raced: 2 runs in our data, so the model has little to go on; Pulled up in 2 of its last 2 jumps runs
- An Mhi (hrs_27428716) | 9yo G | 168lb | OR 120 | draw 0 | jockey Conor Rabbitt(3) | trainer William Young Jnr (14d 0/1) | headgear - | last run 17 days | form 26/P-F | MARKET 1.1% | 09:00 median 101.00 | Matchbook -
    comment: The main risk is confidence after a fall last time out and a pulled up before that, and he is winless in his last four starts.
    DATA: model 1.1% | style Held up (led 8% of runs) | runs in data 1 | last 3: 31 Oct Ayr 24.5f Good To Soft F/7
    DATA for: Official rating 120, 9 lb above field average; Pace: a contested lead should suit its hold-up style
    DATA against: Carries 9 lb more than average; Lightly raced: 1 run in our data, so the model has little to go on; Fell or unseated in 1 of its last 1 jumps runs

## 3:00 Carlisle | race_id rac_32304650092 | Home Is Where The Heart Is Handicap Hurdle Race
Hurdle | Class 5 | 2m1f33y | going  | Turf | 15 runners | rating band 0-100 | age 3yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Holeheartedly (hrs_59491838) | 5yo G | 157lb | OR 89 | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 19/78) | headgear - | last run 32 days | form 6088-7 | MARKET 22.8% | 09:00 median 4.33 | Matchbook 1.04 | CHECK (skip line 4.11)
    comment: The main risk is a string of finishes outside the first six, including a seventh last time out, while he carries 157 lb.
    DATA: model 3.9% | style Midfield (led 3% of runs) | runs in data 4 | last 3: 13 Feb Chepstow 16.1f Soft 8/14; 14 Mar Uttoxeter 19.9f Soft 8/9; 16 Oct Uttoxeter 16f Good 7/10 fig 71
    DATA for: Trainer 24% wins (19/78), last 14 days
    DATA against: Best recent form figure 71, 14 lb below field average; Recent figures 18 lb below its current mark (looks high in the weights); Last-run finishing speed -3.1% vs that field (faded); Poor recent finishing positions
- Bruce Banner (hrs_44015860) | 4yo G | 168lb | OR 100 | draw 0 | jockey Shane Fitzgerald | trainer Rebecca Menzies (14d 1/9) | headgear - | last run 8 days | form 1P-2 | MARKET 13.7% | 09:00 median 6.00 | Matchbook -
    DATA: model 7.6% | style Prominent (led 23% of runs) | runs in data 12 | last 3: 3 Sep Newcastle 12.4f Standard 4/9; 16 Oct Newcastle (AW) 12.5f Standard 9/12 fig 44; 9 Nov Carlisle 17f Good To Soft 2/14 fig 103
    DATA for: Best recent form figure 103, 18 lb above field average; Official rating 100, 12 lb above field average
    DATA against: Carries 12 lb more than average; Pulled up in 1 of its last 2 jumps runs
- Knockeranna Rose (hrs_51800413) | 6yo G | 148lb | OR 80 | draw 0 | jockey Conor Rabbitt(3) | trainer Susan Corbett (14d 0/5) | headgear - | last run 26 days | form 2-4023 | MARKET 12.2% | 09:00 median 6.00 | Matchbook 5.50
    comment: Knockeranna Rose is yet to win in his last five starts, though a third last time out and a second two starts back show he is rarely far away, and he has run over today's trip.
    DATA: model 10.3% | style Prominent (led 4% of runs) | runs in data 9 | last 3: 21 Jun Hexham 16.2f Good 10/10; 2 Oct Hexham 20.1f Good 2/6; 22 Oct Carlisle 20f Good 3/13 fig 74
    DATA for: Good recent finishing positions; Carries 8 lb less than average
    DATA against: Best recent form figure 74, 11 lb below field average; Recent figures 6 lb below its current mark (looks high in the weights); Official rating 80, 8 lb below field average
- Le Fabuleux Buck's (hrs_57718731) | 5yo G | 168lb | OR 100 | draw 0 | jockey Jonjo O'Neill Jr. | trainer Jonjo & A.J. O'Neill (14d 6/33) | headgear - | last run 236 days | form 05539- | MARKET 9.3% | 09:00 median 7.50 | Matchbook -
    comment: Yet to win in his last five starts, Le Fabuleux Buck's was beaten into ninth last time out after a third two starts back, and he returns from a 236-day break.
    DATA: model 9.8% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 20 Jan Leicester 15.5f Heavy 5/12; 5 Feb Lingfield 16f Heavy 3/10; 26 Mar Chepstow 19.5f Good To Soft 9/10
    DATA for: Official rating 100, 12 lb above field average
    DATA against: Last-run finishing speed -8.5% vs that field (faded); Carries 12 lb more than average; Returns from a 236-day break
- Walk On Son (hrs_45982223) | 6yo G | 155lb | OR 87 | draw 0 | jockey Derek Fox | trainer Lucinda Russell & Michael Scudamore (14d 9/37) | headgear t | last run 28 days | form 8-4PU4 | MARKET 6.4% | 09:00 median 10.00 | Matchbook 16.00
    DATA: model 5.6% | style Midfield (led 4% of runs) | runs in data 7 | last 3: 24 May Kelso 16.2f Good PU/8; 23 Sep Perth 20.1f Good UR/9; 20 Oct Hexham 16f Good 4/10 fig 88
    DATA for: Trainer 24% wins (9/37), last 14 days
    DATA against: Race comments mention jumping mistakes in 2 of its last 5 runs; Fell or unseated in 1 of its last 5 jumps runs; Pulled up in 1 of its last 5 jumps runs
- Raffles Wonder (hrs_27237546) | 9yo G | 166lb | OR 98 | draw 0 | jockey Jonathan England | trainer Sam England (14d 5/23) | headgear ht | last run 182 days | form 6P48-5 | MARKET 5.4% | 09:00 median 9.50 | Matchbook -
    DATA: model 6.7% | style Held up (led 4% of runs) | runs in data 3 | last 3: 4 Feb Sedgefield 16.4f Good To Soft 4/6; 22 Mar Carlisle 15.9f Good To Soft 8/12; 19 May Hexham 15.6f Good 5/5
    DATA for: Official rating 98, 10 lb above field average; Trainer 22% wins (5/23), last 14 days
    DATA against: Last-run finishing speed -3.8% vs that field (faded); Carries 10 lb more than average; Returns from a 182-day break; First run over hurdles in our data; Aged 9, older than most of this field; Pace: steady gallop likely, hard to come from off the pace
- National Question (hrs_29509676) | 6yo G | 153lb | OR 85 | draw 0 | jockey Ryan Mania | trainer Adam Nicol (14d 1/9) | headgear p | last run 21 days | form 516-58 | MARKET 4.2% | 09:00 median 19.00 | Matchbook -
    comment: National Question is hard to fancy, having finished eighth last time out, then a fifth two starts back, and a sixth three starts back, with his only win coming four starts back.
    DATA: model 7.9% | style Held up (led 3% of runs) | runs in data 6 | last 3: 11 Apr Newcastle 20.3f Good 6/12; 13 Jun Hexham 16.2f Good 5/10; 27 Oct Newcastle 17f Good 8/10
    DATA for: Has won at this trip or further
    DATA against: Last-run finishing speed -4.3% vs that field (faded); Pace: steady gallop likely, hard to come from off the pace
- Dilly's Gunner (hrs_47577327) | 5yo M | 161lb | OR 93 | draw 0 | jockey Jamie Hamilton | trainer Michael & David Easterby (14d 1/10) | headgear - | last run 248 days | form /5750- | MARKET 4.1% | 09:00 median 15.00 | Matchbook -
    comment: The main risk is a 248-day absence, with 161 lb to carry on top.
    DATA: model 5.2% | style Held up (led 8% of runs) | runs in data 2 | last 3: 16 Jan Market Rasen 18.6f Good To Soft 5/8; 14 Mar Newcastle 20.3f Good To Soft 11/15
    DATA for: Official rating 93, 5 lb above field average
    DATA against: Returns from a 248-day break; Lightly raced: 2 runs in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Breadalbane Lass (hrs_38417155) | 6yo M | 149lb | OR 81 | draw 0 | jockey Ben Smith(7) | trainer R. Mike Smith (14d 0/7) | headgear tp | last run 163 days | form 641-48 | MARKET 3.9% | 09:00 median 13.00 | Matchbook 40.00
    comment: In her favour, she has run over today's trip and won three starts back, a first in her last five outings.
    DATA: model 11.1% | style Prominent (led 23% of runs) | runs in data 6 | last 3: 23 Apr Perth 16.2f Good 1/14; 9 May Hexham 16.2f Good To Soft 4/8; 7 Jun Perth 16.2f Good 8/12
    DATA for: Carries 7 lb less than average
    DATA against: Official rating 81, 7 lb below field average; Returns from a 163-day break
- Les's Legacy (hrs_23596636) | 9yo G | 160lb | OR 92 | draw 0 | jockey Nathan Moscrop | trainer Susan Corbett (14d 0/5) | headgear tp | last run 10 days | form 4853U3 | MARKET 3.8% | 09:00 median 17.00 | Matchbook -
    comment: Third last time out and only ten days ago, Les's Legacy is fit and in the frame again, though he is winless in his last six and unseated two starts back; he has run over today's trip and carries 160 lb off an official mark of 92.
    DATA: model 9.6% | style Midfield (led 3% of runs) | runs in data 9 | last 3: 2 Oct Hexham 20.1f Good 3/6; 20 Oct Hexham 20f Good UR/9; 7 Nov Kelso 21f Good 3/11 fig 92
    DATA for: Best recent form figure 92, 7 lb above field average
    DATA against: Fell or unseated in 1 of its last 5 jumps runs; Aged 9, older than most of this field
- Action Replay (hrs_17391919349) | 4yo G | 150lb | OR 82 | draw 0 | jockey Richie McLernon | trainer Charlie Longsdon (14d 2/14) | headgear - | last run 23 days | form F-P580 | MARKET 3.6% | 09:00 median 17.00 | Matchbook -
    comment: Unexposed and open to improvement, Action Replay is yet to win in his last five starts, with an eighth two starts back and a fifth three starts back the best of his recent efforts. He returns 23 days after his last run, carrying 150 lb.
    DATA: model 1.3% | style Prominent (led 23% of runs) | runs in data 4 | last 3: 25 Sep Worcester 20f Good 5/9; 7 Oct Worcester 16f Good 8/12; 25 Oct Market Rasen 16.5f Good To Soft 11/11
    DATA for: Carries 6 lb less than average
    DATA against: Official rating 82, 6 lb below field average; Pulled up in 1 of its last 4 jumps runs
- Snapaudaciaheros (hrs_412652912) | 6yo M | 152lb | OR 84 | draw 0 | jockey Charlie Maggs | trainer Rebecca Menzies (14d 1/9) | headgear tp | last run 14 days | form -P1735 | MARKET 2.9% | 09:00 median 29.00 | Matchbook -
    comment: Fifth last time out and just a seventh three starts back leave Snapaudaciaheros short of convincing, and she carries 152 lb from an official mark of 84.
    DATA: model 8.3% | style Prominent (led 4% of runs) | runs in data 9 | last 3: 21 Jun Hexham 16.2f Good 7/10; 20 Oct Hexham 16f Good 3/10 fig 87; 3 Nov Sedgefield 17f Good 5/11 fig 80
    DATA against: Pulled up in 1 of its last 5 jumps runs
- Justus (hrs_20663776) | 8yo G | 158lb | OR 90 | draw 0 | jockey Joshua Thompson(5) | trainer Micky Hammond (14d 0/15) | headgear b | last run 23 days | form 85-245 | MARKET 2.8% | 09:00 median 26.00 | Matchbook -
    comment: Justus arrives fairly fit after 23 days off, with a fifth last time out, a fourth two starts back and a second three starts back showing he's in the mix, and he has run over today's trip.
    DATA: model 8.4% | style Midfield (led 4% of runs) | runs in data 6 | last 3: 19 May Hexham 16.2f Good 2/10; 4 Jun Uttoxeter 15.8f Good 4/5; 25 Oct Market Rasen 16.5f Good To Soft 5/6 fig 79
    DATA against: Best recent form figure 79, 6 lb below field average; Recent figures 11 lb below its current mark (looks high in the weights); Trainer 0 wins from 15 runs, last 14 days
- Bollin Skittle (hrs_50188523) | 6yo M | 154lb | OR 86 | draw 0 | jockey Craig Nichol | trainer Donald Whillans (14d 0/2) | headgear - | last run 241 days | form 5644- | MARKET 2.7% | 09:00 median 34.00 | Matchbook -
    comment: Bollin Skittle has finished fourth in each of her last two starts, then a sixth and a fifth before that, so she is consistent but yet to win in recent form.
    DATA: model 1.9% | style Held up (led 4% of runs) | runs in data 3 | last 3: 3 Feb Carlisle 19.3f Good To Soft 6/7; 28 Feb Kelso 16.2f Good To Soft 4/8; 21 Mar Kelso 20.9f Good To Soft 4/7
    DATA against: Returns from a 241-day break; Pace: steady gallop likely, hard to come from off the pace
- Ribble River (hrs_37289532) | 5yo G | 142lb | OR 71 | draw 0 | jockey Sean Quinlan | trainer Lizzie Quinlan (14d 2/10) | headgear tp | last run 54 days | form 5-5668 | MARKET 2.3% | 09:00 median 41.00 | Matchbook -
    comment: Ribble River is winless in his last five, finishing eighth last time out after a sixth and another sixth before that, and he returns after 54 days off.
    DATA: model 2.6% | style Midfield (led 4% of runs) | runs in data 7 | last 3: 18 Jul Cartmel 17.2f Good 6/8; 3 Sep Haydock 11.6f Soft 10/11; 24 Sep Perth 16.2f Good 8/9
    DATA for: Trainer 20% wins (2/10), last 14 days; Carries 14 lb less than average
    DATA against: Official rating 71, 17 lb below field average; Last-run finishing speed -7.2% vs that field (faded); Poor recent finishing positions

## 3:30 Carlisle | race_id rac_32304652029 | Light Up A Life Conditional Jockeys' Handicap Steeple Chase (Go North One Man Series Qualifier)
Chase | Class 5 | 1m7f207y | going  | Turf | 6 runners | rating band 0-105 | age 4yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Air Apparent (hrs_39528881) | 6yo G | 168lb | OR 105 | draw 0 | jockey Benjamin Macey | trainer Seamus Mullins (14d 3/15) | headgear - | last run 21 days | form 4530-1 | MARKET 30.4% | 09:00 median 2.88 | Matchbook 3.20
    comment: Air Apparent arrives a last-time-out winner after 21 days off, and he has run over today's trip, while a third three starts back shows he can hit the frame.
    DATA: model 24.3% | style Midfield (led 4% of runs) | runs in data 5 | last 3: 7 Mar Hereford 19.7f Good 3/12; 21 Apr Ffos Las 23.9f Good 11/12; 27 Oct Bangor-on-Dee 17.5f Good To Soft 1/9 fig 103
    DATA for: Official rating 105, 9 lb above field average; Trainer 20% wins (3/15), last 14 days; Has won at this trip or further; Good recent finishing positions
    DATA against: Carries 9 lb more than average; Race comments mention jumping mistakes in 2 of its last 5 runs
- Mr Lincoln (hrs_30941071) | 6yo G | 164lb | OR 101 | draw 0 | jockey Charlie Maggs | trainer Iain Jardine (14d 0/9) | headgear p | last run 38 days | form -34271 | MARKET 28.5% | 09:00 median 3.25 | Matchbook 3.20
    comment: Won last time out, but he followed a seventh two starts back and the rest of his recent form is mixed, so carrying 164 lb off 101 looks a tall order.
    DATA: model 27.9% | style Midfield (led 29% of runs) | runs in data 13 | last 3: 8 Aug Ayr 10f Good 8/13; 29 Aug Cartmel 17.2f Good 7/11; 10 Oct Hexham 15.6f Good 1/7
    DATA for: Official rating 101, 5 lb above field average; Has won at this trip or further
    DATA against: Trainer 0 wins from 9 runs, last 14 days; Carries 5 lb more than average
- Cuzco du Mathan (hrs_24263708) | 8yo G | 153lb | OR 90 | draw 0 | jockey Leah Noreci(8) | trainer James Moffatt (14d 0/4) | headgear v | last run 78 days | form 44-783 | MARKET 13.0% | 09:00 median 7.00 | Matchbook -
    DATA: model 12.6% | style Held up (led 3% of runs) | runs in data 6 | last 3: 27 May Cartmel 17.3f Good 7/7; 18 Jul Cartmel 17.3f Good 8/8; 31 Aug Cartmel 17.3f Good To Soft 3/6
    DATA for: Carries 6 lb less than average
    DATA against: Official rating 90, 6 lb below field average; Pace: steady gallop likely, hard to come from off the pace
- Galidam (hrs_40473216) | 6yo G | 159lb | OR 96 | draw 0 | jockey Joshua Thompson(3) | trainer Micky Hammond (14d 0/15) | headgear t | last run 269 days | form /6333- | MARKET 11.8% | 09:00 median 7.00 | Matchbook 11.00
    comment: The one concern is a 269-day absence, plus 159 lb on his back.
    DATA: model 13.1% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 21 Feb Newcastle 16.3f Good To Soft 3/6
    DATA against: Trainer 0 wins from 15 runs, last 14 days; Returns from a 269-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Tommys Law (hrs_34253688) | 7yo G | 165lb | OR 102 | draw 0 | jockey Gregor Walkingshaw(8) | trainer Lucinda Russell & Michael Scudamore (14d 9/37) | headgear t | wind surgery | last run 33 days | form 222P/U | MARKET 11.3% | 09:00 median 8.00 | Matchbook -
    comment: Tommys Law arrives yet to win in his last five, but he was second in three of them, finishing runner-up five starts back, four starts back and three starts back.
    DATA: model 8.9% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 15 Oct Perth 20f Soft UR/8
    DATA for: Official rating 102, 6 lb above field average; Trainer 24% wins (9/37), last 14 days
    DATA against: Carries 6 lb more than average; Lightly raced: 1 run in our data, so the model has little to go on; Fell or unseated in 1 of its last 1 jumps runs
- Divas Doyen (hrs_23796381) | 9yo M | 144lb | OR 81 | draw 0 | jockey Isabelle Ryder | trainer Sandy Forster (14d 0/0) | headgear p | last run 157 days | form 443-P3 | MARKET 5.0% | 09:00 median 19.00 | Matchbook -
    comment: Winless in her last five, Divas Doyen was third last time out but that was 157 days ago, and a pulled up two starts back adds to the doubts under 144 lb.
    DATA: model 13.3% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 2 Apr Kelso 21.6f Good 3/10; 2 May Hexham 20.1f Good PU/13; 13 Jun Hexham 15.6f Good 3/6
    DATA for: Last-run finishing speed +2.2% vs that field (finished strongly); Carries 15 lb less than average
    DATA against: Official rating 81, 15 lb below field average; Returns from a 157-day break; Pulled up in 1 of its last 5 jumps runs
