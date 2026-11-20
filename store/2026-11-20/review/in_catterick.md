# Card review packet: Catterick, 2026-11-20

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
{"meeting": "catterick", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 12:00 Catterick | race_id rac_32304911587 | Racing To School Reaches 25 Years Juvenile Hurdle Race (GBB Race)
Hurdle | Class 4 | 1m7f156y | going Good | Turf | 10 runners | rating band - | age 3yo
DATA pace: Lone leader - Poetry of Time is the only habitual front-runner and may be allowed an easy lead.
- Sacre Chef (hrs_17393580848) | 3yo G | 154lb | OR 117 | draw 0 | jockey Harry Atkins(5) | trainer Dan Skelton (14d 16/78) | headgear - | last run 21 days | form 33 | MARKET 53.0% | 09:00 median 1.50 | Matchbook 1.74
    comment: Sacre Chef bids to build on a third last time out and a third two starts back, and he returns after 21 days having run over today's trip and going before.
    DATA: model 25.2% | style Held up (led 5% of runs) | runs in data 2 | last 3: 10 Oct Chepstow Hurdle 16.1f Good To Soft 3/11; 30 Oct Wetherby Hurdle 16f Good 3/8 fig 102
    DATA for: Best recent form figure 102, 10 lb above field average; Trainer 21% wins (16/78), last 14 days; Good recent finishing positions
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Magical Merlot (hrs_55851362) | 3yo G | 154lb | OR - | draw 0 | jockey Brian Hughes | trainer Jonjo & A.J. O'Neill (14d 6/31) | headgear - | last run 66 days | form - | MARKET 17.4% | 09:00 median 4.50 | Matchbook 5.50
    comment: Magical Merlot is effectively unexposed, with no recorded form to lean on, so improvement is firmly possible. He returns after 66 days off and carries 154 lb, which is a notable burden for a horse with so little on his record.
    DATA: model 14.9% | style Held up (led 3% of runs) | runs in data 7 | last 3: 13 Aug Windsor Flat 8.1f Good To Firm 4/8; 26 Aug Newbury Flat 10f Good To Firm 1/7; 15 Sep Redcar Flat 10f Good 3/7
    DATA for: Good recent finishing positions
    DATA against: First run over hurdles in our data
- Poetry of Time (hrs_50434748) | 3yo G | 154lb | OR - | draw 0 | jockey James Best | trainer Syd Hosie (14d 1/8) | headgear - | last run 25 days | form 3 | MARKET 13.1% | 09:00 median 5.50 | Matchbook 7.60
    comment: The main risk is that he's yet to win in recent form and carries 154 lb.
    DATA: model 15.8% | style Leader (led 38% of runs) | runs in data 3 | last 3: 3 May Salisbury Flat 7f Good To Firm 1/7; 6 Jun Chepstow Flat 7.1f Soft 1/7; 26 Oct Hereford Hurdle 16f Good To Firm 3/9 fig 91
    DATA for: Last-run finishing speed +2.8% vs that field (finished strongly); Good recent finishing positions; Pace: may get an uncontested lead
- See Blue (hrs_56873768) | 3yo G | 154lb | OR - | draw 0 | jockey Gavin Sheehan | trainer Max Comley (14d 1/9) | headgear h | last run 26 days | form P | MARKET 8.2% | 09:00 median 9.00 | Matchbook 12.50
    comment: Lightly raced and unexposed, See Blue pulled up last time out 26 days ago, so there's little to go on, though he's yet to win and may have scope to improve. He carries 154 lb.
    DATA: model 8.5% | style Midfield (led 5% of runs) | runs in data 4 | last 3: 25 Apr Haydock Flat 8.2f Good To Firm 2/8; 19 Jun Goodwood Flat 8f Good 8/10; 25 Oct Market Rasen Hurdle 16.5f Good To Soft PU/7
    DATA against: Pulled up in 1 of its last 1 jumps runs
- Elm Creek (hrs_57255142) | 3yo G | 154lb | OR - | draw 0 | jockey Shane Fitzgerald | trainer Rebecca Menzies (14d 1/9) | headgear p | last run 26 days | form 3 | MARKET 3.1% | 09:00 median 19.00 | Matchbook 44.00
    comment: The risk is that he is yet to win in his recent form and carries a hefty 154 lb.
    DATA: model 7.5% | style Midfield (led 4% of runs) | runs in data 4 | last 3: 30 Mar Navan Flat 10f Heavy 3/13; 10 Apr Dundalk Flat 10.7f Standard 5/6; 25 Oct Market Rasen Hurdle 16.5f Good To Soft 3/7 fig 83
    DATA for: Good recent finishing positions
    DATA against: Best recent form figure 83, 9 lb below field average
- Positive Thoughts (hrs_56961681) | 3yo F | 147lb | OR - | draw 0 | jockey Danny McMenamin | trainer John & Sean Quinn (14d 1/6) | headgear - | last run 42 days | form - | MARKET 2.0% | 09:00 median 41.00 | Matchbook 65.00
    comment: Positive Thoughts is lightly raced and unexposed, with no recorded form to go on, so she may have more to offer. She returns after 42 days off and carries 147 lb.
    DATA: model 11.0% | style Midfield (led 3% of runs) | runs in data 9 | last 3: 25 Aug Musselburgh Flat 8.9f Good 6/8; 19 Sep Newcastle Flat 8f Standard 4/10; 9 Oct Kempton Flat 8f Standard To Slow 3/13
    DATA for: Last-run finishing speed +2.6% vs that field (finished strongly)
    DATA against: First run over hurdles in our data
- Al Khawaaneej (hrs_58316300) | 3yo C | 154lb | OR - | draw 0 | jockey Peter Kavanagh | trainer Donald McCain (14d 3/26) | headgear - | last run 52 days | form 4 | MARKET 1.5% | 09:00 median 41.00 | Matchbook 90.00
    comment: The one risk is that he is yet to win in his last start's form line, so that long absence could blunt his edge.
    DATA: model 4.6% | style Held up (led 8% of runs) | runs in data 1 | last 3: 29 Sep Sedgefield Hurdle 16.8f Good 4/7
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Risk Averse Rebel (hrs_55634173) | 3yo G | 154lb | OR - | draw 0 | jockey Benjamin Macey(5) | trainer Gary Hanmer (14d 0/5) | headgear - | last run 17 days | form 7 | MARKET 0.7% | 09:00 median 126.00 | Matchbook 220.00
    comment: Risk Averse Rebel is unexposed after just one recent outing, a seventh last time out 17 days ago, so he looks open to improvement. He is yet to win in that limited form and carries 154 lb.
    DATA: model 5.6% | style Midfield (led 5% of runs) | runs in data 11 | last 3: 11 Sep Chester Flat 10.3f Good To Soft 3/11; 19 Sep Chester Flat 14.4f Heavy 7/10; 3 Nov Warwick Hurdle 16f Good 7/7
    DATA against: Last-run finishing speed -6.4% vs that field (faded)
- Cospicua (hrs_57008434) | 3yo F | 147lb | OR - | draw 0 | jockey Sean Quinlan | trainer Barry Murtagh (14d 0/0) | headgear - | last run 86 days | form - | MARKET 0.6% | 09:00 median 126.00 | Matchbook 260.00
    comment: Cospicua is unexposed with no recorded form to lean on, so she remains open to improvement. She returns after 86 days off and carries 147 lb, which is a notable burden for one so lightly raced.
    DATA: model 4.1% | style Unknown | runs in data 8 | last 3: 11 Jun Yarmouth Flat 11.5f Soft 6/8; 8 Aug Lingfield Flat 13f Standard 5/7; 26 Aug Kempton Flat 12f Standard To Slow 10/11
    DATA against: First run over hurdles in our data
- Retro Rocket (hrs_65225328) | 3yo G | 154lb | OR - | draw 0 | jockey Beau Morgan(5) | trainer Martin Keighley (14d 3/13) | headgear - | last run 81 days | form - | MARKET 0.5% | 09:00 median 201.00 | Matchbook 250.00
    comment: Retro Rocket is unexposed and open to improvement, with no recorded form to go on, so this gelding is one to learn about. He returns after 81 days off and carries 154 lb.
    DATA: model 3.0% | style Held up (led 4% of runs) | runs in data 5 | last 3: 4 Jul Leicester Flat 6f Good To Firm 6/6; 6 Aug Southwell Flat 8.1f Standard 8/10; 31 Aug Ripon Flat 9.8f Soft 8/10
    DATA for: Trainer 23% wins (3/13), last 14 days
    DATA against: Poor recent finishing positions; First run over hurdles in our data

## 12:33 Catterick | race_id rac_32304913524 | Jumps Look Better On Racing TV Novices' Hurdle Race (GBB Race)
Hurdle | Class 4 | 2m3f66y | going Good | Turf | 8 runners | rating band - | age 4yo+
DATA pace: Strong pace - 3 habitual front-runners (Nightflyer, I've Got A Friend, Little John). A contested lead should set things up for horses coming from behind.
- I've Got A Friend (hrs_17391213238) | 5yo G | 154lb | OR - | draw 0 | jockey Brian Hughes | trainer Gary Hanmer (14d 0/5) | headgear - | last run 21 days | form U2-112 | MARKET 45.7% | 09:00 median 1.83 | Matchbook 2.00
    DATA: model 19.1% | style Leader (led 79% of runs) | runs in data 3 | last 3: 23 Aug Worcester NH Flat 16f Good 1/10; 10 Oct Hexham NH Flat 16.2f Good 1/6; 30 Oct Wetherby Hurdle 19.5f Good 2/5 fig 114
    DATA for: Last-run finishing speed +4.8% vs that field (finished strongly); Good recent finishing positions
    DATA against: Pace: likely to be taken on for the lead
- Nightflyer (hrs_60394999) | 4yo G | 160lb | OR 112 | draw 0 | jockey Richie McLernon | trainer Jonjo & A.J. O'Neill (14d 6/31) | headgear p | last run 17 days | form -52122 | MARKET 25.9% | 09:00 median 3.12 | Matchbook 3.65
    DATA: model 37.6% | style Leader (led 43% of runs) | runs in data 9 | last 3: 15 Sep Uttoxeter Hurdle 19.9f Good 1/9; 15 Oct Fontwell Hurdle 19f Good To Soft 2/7 fig 98; 3 Nov Warwick Hurdle 19f Good 2/6 fig 116
    DATA for: Last-run finishing speed +3.9% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Pace: likely to be taken on for the lead
- Seeyasunday (hrs_17395400883) | 5yo G | 154lb | OR - | draw 0 | jockey Charlie Maggs | trainer Oliver Greenall & Josh Guerriero (14d 1/12) | headgear - | last run 325 days | form 3- | MARKET 11.0% | 09:00 median 7.50 | Matchbook 8.80
    DATA: model 8.2% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 325-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Little John (hrs_52055927) | 5yo G | 154lb | OR - | draw 0 | jockey Nathan Moscrop | trainer Joanne Foster (14d 0/0) | headgear t | last run 194 days | form F476-4 | MARKET 5.4% | 09:00 median 13.00 | Matchbook 21.00
    DATA: model 4.2% | style Leader (led 29% of runs) | runs in data 3 | last 3: 2 Apr Clonmel NH Flat 19.5f Soft 7/9; 14 Apr Clonmel Hurdle 19.8f Yielding 6/17; 10 May Cork Hurdle 24.4f Good 4/8
    DATA against: Returns from a 194-day break; Pace: likely to be taken on for the lead
- Largy Silver (hrs_17395664762) | 5yo G | 154lb | OR - | draw 0 | jockey Conor Rabbitt(3) | trainer Jessica Bedi (14d 0/6) | headgear t (1st time) | last run 300 days | form 1- | MARKET 4.7% | 09:00 median 17.00 | Matchbook 22.00
    DATA: model 8.2% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: First-time headgear
    DATA against: Returns from a 300-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Lipati (hrs_17394663482) | 4yo G | 153lb | OR - | draw 0 | jockey Sean Quinlan | trainer Tim Easterby (14d 1/10) | headgear - | last run 14 days | form 3-4 | MARKET 3.0% | 09:00 median 26.00 | Matchbook 40.00
    DATA: model 8.1% | style Held up (led 8% of runs) | runs in data 1 | last 3: 6 Nov Hexham Hurdle 20f Good 4/9
    DATA for: Pace: a contested lead should suit its hold-up style
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Jet To London (hrs_17395003500) | 5yo G | 154lb | OR - | draw 0 | jockey Jamie Hamilton | trainer Mark Walford (14d 2/9) | headgear - | last run 14 days | form /541-6 | MARKET 2.9% | 09:00 median 21.00 | Matchbook 65.00
    DATA: model 8.1% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 6 Nov Hexham Hurdle 20f Good 6/9
    DATA for: Trainer 22% wins (2/9), last 14 days
    DATA against: Last-run finishing speed -2.0% vs that field (faded); Lightly raced: 1 run in our data, so the model has little to go on
- Get On Son (hrs_60090191) | 5yo G | 154lb | OR - | draw 0 | jockey Peter Kavanagh | trainer Joel Parkinson & Sue Smith (14d 1/12) | headgear p (1st time) | last run 7 days | form 0-6P | MARKET 1.3% | 09:00 median 67.00 | Matchbook 90.00
    DATA: model 6.5% | style Held up (led 5% of runs) | runs in data 2 | last 3: 10 Oct Hexham Hurdle 16.2f Good 6/9; 13 Nov Sedgefield Hurdle 17f Good PU/7
    DATA for: First-time headgear; Pace: a contested lead should suit its hold-up style
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Pulled up in 1 of its last 2 jumps runs

## 1:08 Catterick | race_id rac_32304915461 | Weatherbys & Birdie Calendars Handicap Steeple Chase (Go North Monet's Garden Series Qualifier) (GBB Race)
Chase | Class 4 | 2m3f51y | going Good | Turf | 6 runners | rating band 0-120 | age 4yo+
DATA pace: Even - Two likely leaders (Gaelic Rambler, Singapore Trip). A fair, even gallop is most likely.
- Legendary Luke (hrs_51124024) | 6yo G | 170lb | OR 122 | draw 0 | jockey Gavin Sheehan | trainer Jamie Snowden (14d 6/22) | headgear - | last run 29 days | form 1143-7 | MARKET 31.2% | 09:00 median 2.88 | Matchbook 3.05
    comment: Legendary Luke won twice in his last five starts, a winner four and five starts back, and has run over today's trip and on the going before, with a trainer in form at 6/22 over the last fortnight.
    DATA: model 17.4% | style Midfield (led 4% of runs) | runs in data 4 | last 3: 14 Feb Haydock Hurdle 24.3f Good To Soft 4/9; 15 Apr Haydock Hurdle 21.2f Good 3/4; 22 Oct Ffos Las Chase 24f Soft 7/7
    DATA for: Official rating 122, 8 lb above field average; Trainer 27% wins (6/22), last 14 days; Has won at this trip or further
    DATA against: Last-run finishing speed -9.7% vs that field (faded); Carries 8 lb more than average
- Inedit d'Amour (hrs_50188040) | 5yo G | 155lb | OR 107 | draw 0 | jockey Peter Kavanagh | trainer Donald McCain (14d 3/26) | headgear - | last run 24 days | form 540-22 | MARKET 22.3% | 09:00 median 4.00 | Matchbook 4.30
    comment: The main risk is that he remains without a win in his last five starts, with 155 lb to carry.
    DATA: model 13.7% | style Midfield (led 4% of runs) | runs in data 6 | last 3: 4 Apr Haydock Hurdle 15.7f Good 10/11; 4 Oct Uttoxeter Chase 16f Good 2/9; 27 Oct Bangor-on-Dee Chase 17.5f Good To Soft 2/9 fig 107
    DATA for: Last-run finishing speed +2.1% vs that field (finished strongly); Good recent finishing positions; Carries 7 lb less than average
    DATA against: Official rating 107, 7 lb below field average
- Gaelic Rambler (hrs_39568438) | 6yo G | 164lb | OR 116 | draw 0 | jockey Richie McLernon | trainer Jonjo & A.J. O'Neill (14d 6/31) | headgear tb | last run 50 days | form -3V613 | MARKET 16.8% | 09:00 median 5.00 | Matchbook 6.00
    comment: The main risk is a 50-day absence, which could leave him short of peak fitness.
    DATA: model 23.2% | style Leader (led 23% of runs) | runs in data 9 | last 3: 23 Aug Worcester Chase 23f Good 6/8; 15 Sep Uttoxeter Chase 20f Good 1/8; 1 Oct Southwell Hurdle 20.4f Good 3/5
    DATA for: Has won at this trip or further; Good recent finishing positions
- Sign Again (hrs_41052431) | 6yo G | 160lb | OR 112 | draw 0 | jockey Brian Hughes | trainer Charlie Longsdon (14d 2/13) | headgear tp (1st time) | last run 24 days | form 063U-P | MARKET 13.5% | 09:00 median 6.00 | Matchbook 7.80
    comment: The risk is obvious: pulled up last time and an unseated rider before that, with 160 lb to carry.
    DATA: model 9.8% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 27 Feb Doncaster Chase 19.1f Good To Soft UR/4; 27 Oct Bangor-on-Dee Chase 20.5f Good To Soft PU/13
    DATA for: First-time headgear
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Fell or unseated in 1 of its last 2 jumps runs; Pulled up in 1 of its last 2 jumps runs
- Singapore Trip (hrs_24434403) | 8yo G | 156lb | OR 108 | draw 0 | jockey Alice Stevens(3) | trainer Micky Hammond (14d 1/16) | headgear t | last run 19 days | form 11-145 | MARKET 9.7% | 09:00 median 9.50 | Matchbook 9.80
    comment: Three wins in his last five starts catch the eye, but he has since been a fourth and a fifth last time out, and he carries 156 lb off 108 here.
    DATA: model 14.2% | style Leader (led 23% of runs) | runs in data 8 | last 3: 6 May Kelso Chase 17.1f Good 1/7; 14 Oct Wetherby Chase 15f Good To Firm 4/4 fig 102; 1 Nov Huntingdon Chase 16.5f Good 5/8 fig 97
    DATA for: Has won at this trip or further; Carries 6 lb less than average
    DATA against: Recent figures 6 lb below its current mark (looks high in the weights); Official rating 108, 6 lb below field average; Last-run finishing speed -2.1% vs that field (faded)
- Jet of Dreams (hrs_29012809) | 8yo G | 167lb | OR 119 | draw 0 | jockey Danny McMenamin | trainer Warren Greatrex (14d 4/16) | headgear tp | last run 19 days | form -F4117 | MARKET 6.6% | 09:00 median 13.00 | Matchbook 15.50
    comment: In his favour, he won two and three starts back and has run over today's trip and going.
    DATA: model 21.6% | style Held up (led 3% of runs) | runs in data 6 | last 3: 29 Sep Sedgefield Chase 16.4f Good 1/5; 7 Oct Sedgefield Chase 16.4f Good 1/4; 1 Nov Huntingdon Chase 16.5f Good 7/8 fig 103
    DATA for: Official rating 119, 5 lb above field average; Trainer 25% wins (4/16), last 14 days; Good recent finishing positions
    DATA against: Recent figures 16 lb below its current mark (looks high in the weights); Last-run finishing speed -2.5% vs that field (faded); Carries 5 lb more than average; Fell or unseated in 1 of its last 5 jumps runs

## 1:43 Catterick | race_id rac_32304917398 | Support The Injured Jockeys Fund Handicap Hurdle Race (Go North Brindisi Breeze Series Qualifier)
Hurdle | Class 4 | 3m1f71y | going Good | Turf | 9 runners | rating band 0-120 | age 4yo+
DATA pace: Even - Two likely leaders (Quercus Robur, Noonetellsmenothin). A fair, even gallop is most likely.
- Jeteye (hrs_32780258) | 9yo G | 155lb | OR 100 | draw 0 | jockey Rebecca Hitchen(7) | trainer Sam England (14d 3/24) | headgear tb | last run 7 days | form 121511 | MARKET 21.3% | 09:00 median 4.00 | Matchbook 4.50 | CHECK (skip line 3.80)
    comment: Jeteye has won four of his last six, including last time out and two starts back, and he's quick back after seven days, with experience over today's trip and going.
    DATA: model 17.8% | style Prominent (led 23% of runs) | runs in data 11 | last 3: 10 Oct Hexham Chase 24.2f Good 5/9; 3 Nov Sedgefield Chase 26.5f Good 1/4 fig 99; 13 Nov Sedgefield Hurdle 27f Good 1/5 fig 100
    DATA for: Last-run finishing speed +4.4% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
- Noonetellsmenothin (hrs_51185988) | 5yo G | 161lb | OR 106 | draw 0 | jockey Richie McLernon | trainer Jonjo & A.J. O'Neill (14d 6/31) | headgear b | last run 21 days | form P43-32 | MARKET 16.9% | 09:00 median 5.00 | Matchbook 5.80
    comment: Noonetellsmenothin arrives in cracking nick, a second last time out following two thirds, and he has run on today's going after a 21-day break.
    DATA: model 12.9% | style Leader (led 23% of runs) | runs in data 6 | last 3: 22 Apr Ludlow Hurdle 23.8f Good 3/6; 14 Oct Wetherby Hurdle 19.5f Good To Firm 3/7 fig 103; 30 Oct Wetherby Hurdle 21.5f Good 2/11 fig 105
    DATA for: Last-run finishing speed +3.0% vs that field (finished strongly); Good recent finishing positions
    DATA against: Race comments mention jumping mistakes in 3 of its last 5 runs; Pulled up in 1 of its last 5 jumps runs
- Crafty Gael (hrs_32795385) | 7yo G | 157lb | OR 102 | draw 0 | jockey Sean Quinlan | trainer Lizzie Quinlan (14d 1/9) | headgear tp | last run 7 days | form 321121 | MARKET 13.5% | 09:00 median 6.00 | Matchbook 7.40
    comment: Crafty Gael arrives in cracking form, a winner last time out and again four starts back, with a second two starts back, and he has run on today's going.
    DATA: model 15.1% | style Held up (led 4% of runs) | runs in data 9 | last 3: 1 Oct Southwell Hurdle 24.3f Good 1/8; 6 Nov Hexham Hurdle 23.5f Good 2/10 fig 100; 13 Nov Southwell Hurdle 24.5f Good 1/6 fig 100
    DATA for: Good recent finishing positions
- Speed Davis (hrs_33165202) | 8yo G | 168lb | OR 113 | draw 0 | jockey Harry Brown(7) | trainer Donald McCain (14d 3/26) | headgear - | last run 24 days | form 1-5633 | MARKET 12.2% | 09:00 median 7.00 | Matchbook 7.80
    comment: Speed Davis arrives in decent shape, third last time out and a third two starts back after a win five starts back, and he has run on today's going before. Carrying 168 lb is the main risk, though a 24-day break keeps him fresh.
    DATA: model 9.2% | style Held up (led 3% of runs) | runs in data 5 | last 3: 12 Jul Perth Hurdle 23.9f Good 6/7; 4 Sep Bangor-on-Dee Hurdle 23.1f Good 3/5; 27 Oct Bangor-on-Dee Hurdle 23f Good 3/9 fig 113
    DATA for: Best recent form figure 113, 9 lb above field average; Official rating 113, 8 lb above field average; Last-run finishing speed +3.9% vs that field (finished strongly); Good recent finishing positions
    DATA against: Carries 8 lb more than average
- Sunset Hill (hrs_40647103) | 7yo M | 167lb | OR 112 | draw 0 | jockey Nathan Moscrop | trainer Susan Corbett (14d 1/9) | headgear p | last run 14 days | form 4-2364 | MARKET 10.6% | 09:00 median 8.50 | Matchbook 8.60
    comment: Sunset Hill is a consistent mare, finishing a fourth last time out and a second four starts back, and she's fresh from a 14-day break with experience of both today's trip and the going.
    DATA: model 9.7% | style Prominent (led 23% of runs) | runs in data 7 | last 3: 19 May Hexham Hurdle 20.1f Good 3/10; 13 Jun Hexham Hurdle 20.1f Good 6/8; 6 Nov Hexham Hurdle 20f Good 4/9 fig 112
    DATA for: Best recent form figure 112, 8 lb above field average; Official rating 112, 7 lb above field average; Last-run finishing speed +2.3% vs that field (finished strongly)
    DATA against: Carries 7 lb more than average
- Vanilla Dancer (hrs_35596610) | 7yo M | 157lb | OR 102 | draw 0 | jockey Danny McMenamin | trainer Chris Grant (14d 1/3) | headgear - | last run 29 days | form 2-4961 | MARKET 7.6% | 09:00 median 11.00 | Matchbook 13.50
    DATA: model 7.7% | style Prominent (led 23% of runs) | runs in data 8 | last 3: 24 May Kelso Hurdle 20.9f Good 9/12; 29 Sep Sedgefield Hurdle 19.9f Good 6/8; 22 Oct Carlisle Hurdle 20f Good 1/13 fig 99
    DATA against: Best recent form figure 99, 5 lb below field average
- Loulou Madrik (hrs_50433061) | 5yo G | 159lb | OR 104 | draw 0 | jockey Jamie Hamilton | trainer Mark Walford (14d 2/9) | headgear tp | last run 24 days | form 452-75 | MARKET 7.3% | 09:00 median 12.00 | Matchbook 13.00
    comment: The main risk is a weight of 159 lb after a fifth last time out.
    DATA: model 7.9% | style Midfield (led 3% of runs) | runs in data 7 | last 3: 4 Apr Carlisle Chase 24.5f Good 2/6; 10 Oct Hexham Chase 24.2f Good 7/9; 27 Oct Newcastle Chase 20f Good 5/6 fig 96
    DATA for: Trainer 22% wins (2/9), last 14 days
    DATA against: Best recent form figure 96, 8 lb below field average; Recent figures 8 lb below its current mark (looks high in the weights); Last-run finishing speed -2.7% vs that field (faded)
- East Eagle (hrs_40687493) | 6yo G | 151lb | OR 96 | draw 0 | jockey Charlie Maggs | trainer Mike Sowersby (14d 0/4) | headgear t | last run 38 days | form 56P132 | MARKET 5.7% | 09:00 median 15.00 | Matchbook 17.00
    comment: East Eagle arrives in decent heart, a second last time out and a third before that, with a win three starts back, and he has run over today's trip and going.
    DATA: model 9.9% | style Midfield (led 3% of runs) | runs in data 11 | last 3: 19 Jul Stratford Hurdle 26.4f Good To Firm 1/4; 9 Sep Sedgefield Hurdle 27f Good 3/5; 13 Oct Southwell Hurdle 24.3f Good 2/6
    DATA for: Has won at this trip or further; Good recent finishing positions; Carries 9 lb less than average
    DATA against: Official rating 96, 9 lb below field average; Pulled up in 1 of its last 5 jumps runs
- Quercus Robur (hrs_28446908) | 7yo G | 162lb | OR 107 | draw 0 | jockey Ryan Mania | trainer Adam Nicol (14d 1/5) | headgear - | last run 16 days | form 429- | MARKET 5.0% | 09:00 median 15.00 | Matchbook 23.00
    comment: Quercus Robur arrives 16 days after a ninth last time out, though a second two starts back shows he can go close, and he is yet to win in his last three.
    DATA: model 9.7% | style Leader (led 38% of runs) | runs in data 2 | last 3: 20 Mar Musselburgh Hurdle 17.4f Good To Soft 9/10; 4 Nov Musselburgh Flat 16f Soft 4/11 fig 54
    DATA for: Trainer 20% wins (1/5), last 14 days
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on

## 2:18 Catterick | race_id rac_32304919335 | Jodie Standing's Point-To-Point Recruits Handicap Steeple Chase (Challenger Staying Chase Series Qualifier) (GBB Race)
Chase | Class 3 | 3m1f54y | going Good | Turf | 5 runners | rating band 0-125 | age 4yo+
DATA pace: Strong pace - 3 habitual front-runners (Some Scope, Move With The Beat, Paddy O'Mahler). A contested lead should set things up for horses coming from behind.
- Paddy O'Mahler (hrs_34045081) | 8yo G | 158lb | OR 110 | draw 0 | jockey Danny McMenamin | trainer Joel Parkinson & Sue Smith (14d 1/12) | headgear p | last run 20 days | form 112F-4 | MARKET 34.8% | 09:00 median 2.63 | Matchbook 2.80
    comment: In his favour, he won twice in his last five starts, has run over today's trip and going, and is fit after 20 days.
    DATA: model 18.6% | style Leader (led 29% of runs) | runs in data 3 | last 3: 24 Feb Catterick Chase 25.2f Good To Soft 2/6; 22 Mar Carlisle Chase 24.5f Good To Soft F/12; 31 Oct Wetherby Chase 24f Good 4/4 fig 103
    DATA against: Recent figures 7 lb below its current mark (looks high in the weights); Fell or unseated in 1 of its last 3 jumps runs; Pace: likely to be taken on for the lead
- Some Scope (hrs_30208612) | 8yo G | 167lb | OR 119 | draw 0 | jockey Brian Hughes | trainer Richard Hobson (14d 0/4) | headgear tp | last run 19 days | form 022P-7 | MARKET 24.4% | 09:00 median 3.75 | Matchbook 3.90
    comment: Winless in his last five, Some Scope still brings a pair of seconds three and four starts back, and he has run over today's trip and going before.
    DATA: model 16.5% | style Leader (led 83% of runs) | runs in data 5 | last 3: 21 Mar Newbury Chase 23.4f Good To Soft 2/7; 15 Apr Haydock Chase 28.4f Good PU/11; 1 Nov Worcester Chase 20f Good To Soft 7/13 fig 108
    DATA for: Official rating 119, 6 lb above field average
    DATA against: Recent figures 11 lb below its current mark (looks high in the weights); Last-run finishing speed -4.0% vs that field (faded); Carries 6 lb more than average; Pulled up in 1 of its last 5 jumps runs; Pace: likely to be taken on for the lead
- Finn Lough (hrs_34457276) | 7yo G | 156lb | OR 108 | draw 0 | jockey Charlie Maggs | trainer Oliver Greenall & Josh Guerriero (14d 1/12) | headgear t | last run 24 days | form 572F-8 | MARKET 19.9% | 09:00 median 4.50 | Matchbook 5.00
    comment: Finn Lough is yet to win in his last five, but a second three starts back shows his ability, and he has run over today's trip and going before after 24 days off.
    DATA: model 14.0% | style Midfield (led 5% of runs) | runs in data 3 | last 3: 15 Feb Musselburgh Chase 23.6f Soft 2/7; 14 Mar Newcastle Chase 23.4f Good To Soft F/4; 27 Oct Bangor-on-Dee Chase 24f Good To Soft 8/13 fig 101
    DATA for: Carries 5 lb less than average
    DATA against: Best recent form figure 101, 4 lb below field average; Recent figures 7 lb below its current mark (looks high in the weights); Official rating 108, 5 lb below field average; Fell or unseated in 1 of its last 3 jumps runs
- Melton Mossy (hrs_37381631) | 7yo G | 160lb | OR 112 | draw 0 | jockey Conor Ring | trainer Mrs C. Williams (14d 1/25) | headgear - | last run 15 days | form 1-5412 | MARKET 13.2% | 09:00 median 6.00 | Matchbook 8.60
    comment: Second last time out and a winner two starts back, Melton Mossy arrives fresh after 15 days and has run over today's trip and going before, making him a serious threat. The main risk is a stable struggling for form, with just one winner from 25 in the last 14 days.
    DATA: model 22.9% | style Held up (led 4% of runs) | runs in data 6 | last 3: 7 Sep Newton Abbot Chase 16.3f Good 4/5; 5 Oct Stratford Chase 22.6f Good To Firm 1/9; 5 Nov Plumpton Chase 25.5f Good 2/4 fig 110
    DATA for: Best recent form figure 110, 4 lb above field average; Good recent finishing positions; Pace: a contested lead should suit its hold-up style
- Move With The Beat (hrs_34745928) | 7yo G | 164lb | OR 116 | draw 0 | jockey Sean Quinlan | trainer Lizzie Quinlan (14d 1/9) | headgear t | last run 48 days | form 411-15 | MARKET 7.7% | 09:00 median 11.00 | Matchbook 13.50
    comment: The risk is a 48-day absence and 164 lb on his back.
    DATA: model 28.0% | style Leader (led 43% of runs) | runs in data 6 | last 3: 23 Apr Warwick Chase 20f Good 1/6; 13 May Newton Abbot Chase 21f Good 1/4; 3 Oct Fontwell Chase 19.5f Good 5/6
    DATA for: Good recent finishing positions
    DATA against: Pace: likely to be taken on for the lead

## 2:53 Catterick | race_id rac_32304921272 | racingtv.com/freetrial Female Jockeys' Handicap Steeple Chase (Female Professional Jockeys And Amateur Riders' Race)
Chase | Class 5 | 3m1f54y | going Good | Turf | 9 runners | rating band 0-100 | age 4yo+
DATA pace: Strong pace - 5 habitual front-runners (Jo Lescribaa, Anytrixwilldo, Illogical Logic, Aill Dubh, Unspeakable). A contested lead should set things up for horses coming from behind.
- I See The Sea (hrs_35336091) | 7yo G | 161lb | OR 93 | draw 0 | jockey Miss Ellie Callwood(7) | trainer Christopher Kellett (14d 1/1) | headgear b | last run 221 days | form 2P375- | MARKET 18.5% | 09:00 median 4.33 | Matchbook 5.30 | CHECK (skip line 4.11)
    DATA: model 9.7% | style Prominent (led 3% of runs) | runs in data 5 | last 3: 13 Mar Doncaster Chase 26f Good To Soft 3/4; 31 Mar Bangor-on-Dee Chase 24.1f Good 7/10; 13 Apr Hexham Chase 24.2f Good 5/14
    DATA for: Official rating 93, 6 lb above field average
    DATA against: Carries 6 lb more than average; Returns from a 221-day break; Race comments mention jumping mistakes in 2 of its last 5 runs; Pulled up in 1 of its last 5 jumps runs
- Hardy Buck (hrs_28824754) | 8yo G | 142lb | OR 74 | draw 0 | jockey Fern O'Brien(5) | trainer Max Comley (14d 1/9) | headgear tv | last run 30 days | form P-6233 | MARKET 17.0% | 09:00 median 5.00 | Matchbook 5.50
    comment: Hardy Buck has been placed in each of his last three starts, a third last time out, a third two starts back and a second three starts back, but he is still winless in that spell.
    DATA: model 8.6% | style Midfield (led 29% of runs) | runs in data 6 | last 3: 22 Aug Newton Abbot Chase 25.8f Good To Firm 2/6; 26 Sep Market Rasen Chase 23.9f Good 3/7; 21 Oct Fontwell Chase 26f Soft 3/8
    DATA for: Good recent finishing positions; Carries 13 lb less than average
    DATA against: Official rating 74, 13 lb below field average; Race comments mention jumping mistakes in 2 of its last 5 runs; Pulled up in 1 of its last 5 jumps runs
- Anytrixwilldo (hrs_34003578) | 8yo G | 166lb | OR 98 | draw 0 | jockey Miss Gina Andrews | trainer Jonjo & A.J. O'Neill (14d 6/31) | headgear b | last run 23 days | form 4-6631 | MARKET 13.6% | 09:00 median 6.00 | Matchbook 7.20
    comment: Anytrixwilldo won last time out and was third two starts back, so he arrives in good heart after 23 days off, with experience of today's trip and going. The main risk is the 166 lb he must carry off an official mark of 98.
    DATA: model 18.0% | style Leader (led 63% of runs) | runs in data 7 | last 3: 9 Jun Southwell Chase 24.3f Good 6/7; 17 Oct Newton Abbot Chase 26f Good 3/5 fig 92; 28 Oct Huntingdon Chase 23.5f Good 1/6 fig 95
    DATA for: Best recent form figure 95, 15 lb above field average; Official rating 98, 11 lb above field average; Good recent finishing positions
    DATA against: Carries 11 lb more than average; Pace: likely to be taken on for the lead
- Jo Lescribaa (hrs_37890426) | 7yo G | 168lb | OR 100 | draw 0 | jockey Harriet Tucker(7) | trainer Oliver Greenall & Josh Guerriero (14d 1/12) | headgear - | wind surgery | last run 237 days | form 13/6P- | MARKET 13.3% | 09:00 median 6.00 | Matchbook 7.40
    comment: The main risk is a 237-day absence after being pulled up last time out.
    DATA: model 11.2% | style Leader (led 57% of runs) | runs in data 1 | last 3: 28 Mar Uttoxeter Chase 24f Good To Soft PU/10
    DATA for: Official rating 100, 13 lb above field average
    DATA against: Carries 13 lb more than average; Returns from a 237-day break; Lightly raced: 1 run in our data, so the model has little to go on; Pulled up in 1 of its last 1 jumps runs; Pace: likely to be taken on for the lead
- Unspeakable (hrs_29326864) | 8yo G | 142lb | OR 73 | draw 0 | jockey Alice Stevens(3) | trainer David Thompson (14d 0/0) | headgear tp | last run 63 days | form 6-4644 | MARKET 10.9% | 09:00 median 8.00 | Matchbook 8.60
    comment: Unspeakable is winless in his last five, finishing fourth last time out, a fourth two starts back and a sixth three starts back, and he returns after 63 days off carrying 142 lb.
    DATA: model 7.0% | style Leader (led 23% of runs) | runs in data 5 | last 3: 23 Jun Newton Abbot Chase 25.8f Good 6/9; 6 Sep Fontwell Chase 26f Good 4/6; 18 Sep Newton Abbot Chase 25.8f Good 4/7
    DATA for: Carries 13 lb less than average
    DATA against: Official rating 73, 14 lb below field average; Pace: likely to be taken on for the lead
- Illogical Logic (hrs_32982299) | 8yo G | 153lb | OR 85 | draw 0 | jockey Tabitha Worsley | trainer David Thompson (14d 0/0) | headgear p | last run 15 days | form 521144 | MARKET 10.2% | 09:00 median 8.50 | Matchbook 9.20
    comment: Illogical Logic arrives fit after 15 days, a fourth last time out and another fourth two starts back, following back-to-back wins three and four starts back, and he has run over today's trip and going.
    DATA: model 17.7% | style Leader (led 54% of runs) | runs in data 11 | last 3: 2 Oct Hexham Chase 20.1f Good 1/5; 18 Oct Sedgefield Chase 21f Good 4/7 fig 80; 5 Nov Newcastle Chase 20f Good 4/9 fig 82
    DATA against: Pace: likely to be taken on for the lead
- Halfway House Lad (hrs_33644408) | 7yo G | 153lb | OR 85 | draw 0 | jockey Leah Noreci(7) | trainer James Moffatt (14d 0/4) | headgear - | wind surgery | last run 83 days | form -11PP8 | MARKET 7.5% | 09:00 median 12.00 | Matchbook 12.50
    comment: Two wins in his last five starts, but he was eighth last time out and pulled up in the two runs before that, and he returns after 83 days off. He has run over today's trip and going, yet 153 lb on an official mark of 85 leaves plenty to prove.
    DATA: model 10.4% | style Prominent (led 23% of runs) | runs in data 8 | last 3: 28 Jun Cartmel Chase 25.5f Good PU/8; 18 Jul Cartmel Chase 25.5f Good PU/10; 29 Aug Cartmel Chase 21.2f Good 8/11
    DATA for: Has won at this trip or further
    DATA against: Poor recent finishing positions; Race comments mention jumping mistakes in 2 of its last 5 runs; Pulled up in 2 of its last 5 jumps runs
- Aill Dubh (hrs_29829191) | 9yo G | 142lb | OR 74 | draw 0 | jockey Miss Natasha Cookson(7) | trainer Micky Hammond (14d 1/16) | headgear p | last run 14 days | form 415363 | MARKET 6.6% | 09:00 median 13.00 | Matchbook 14.50
    comment: Aill Dubh is a hard sell, with just one win in his last six and a sixth two starts back, though a third last time out, only 14 days ago, shows he is in decent order. He has run over today's trip and going, but carrying 142 lb he looks up against it.
    DATA: model 7.9% | style Leader (led 43% of runs) | runs in data 10 | last 3: 14 Sep Sedgefield Chase 26.3f Good 3/5; 27 Oct Newcastle Chase 20f Good 6/6; 6 Nov Hexham Chase 24f Good 3/7 fig 62
    DATA for: Good recent finishing positions; Carries 13 lb less than average
    DATA against: Best recent form figure 62, 18 lb below field average; Recent figures 12 lb below its current mark (looks high in the weights); Official rating 74, 13 lb below field average; Last-run finishing speed -5.2% vs that field (faded); Pace: likely to be taken on for the lead
- Balkardy (hrs_23241449) | 9yo G | 166lb | OR 98 | draw 0 | jockey Miss Eleanor Williams(7) | trainer Mrs C. Williams (14d 1/25) | headgear p | last run 39 days | form U7P247 | MARKET 2.4% | 09:00 median 34.00 | Matchbook 48.00
    comment: He is yet to win in his last six and the yard is quiet, but 98 officially looks workable.
    DATA: model 9.5% | style Midfield (led 29% of runs) | runs in data 6 | last 3: 13 Jul Newton Abbot Chase 25.8f Good To Firm 2/5; 22 Sep Fontwell Chase 26f Good 4/4; 12 Oct Worcester Chase 23f Good 7/9
    DATA for: Official rating 98, 11 lb above field average
    DATA against: Last-run finishing speed -7.0% vs that field (faded); Carries 11 lb more than average; Pulled up in 1 of its last 5 jumps runs

## 3:28 Catterick | race_id rac_32304923209 | Racing Again 2nd December Open National Hunt Flat Race (Category 2 Elimination) (GBB Race)
NH Flat | Class 5 | 1m7f156y | going Good | Turf | 7 runners | rating band - | age 4-5yo
DATA pace: Lone leader - La Dame Ecarlate is the only habitual front-runner and may be allowed an easy lead.
- La Dame Ecarlate (hrs_64590505) | 4yo F | 149lb | OR - | draw 0 | jockey Gavin Sheehan | trainer Jamie Snowden (14d 6/22) | headgear - | last run 180 days | form 2 | MARKET 29.4% | 09:00 median 2.88 | Matchbook 3.25
    comment: The one concern is a 180-day absence, so fitness is the question.
    DATA: model 37.5% | style Leader (led 57% of runs) | runs in data 1 | last 3: 24 May Fontwell NH Flat 17.7f Good 2/6
    DATA for: Trainer 27% wins (6/22), last 14 days; Pace: may get an uncontested lead
    DATA against: Returns from a 180-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Rescheduled (hrs_17391758727) | 4yo G | 156lb | OR - | draw 0 | jockey Brian Hughes | trainer Donald McCain (14d 3/26) | headgear - | last run 52 days | form 2 | MARKET 25.1% | 09:00 median 3.50 | Matchbook 3.70
    comment: The one concern is a 52-day absence, and he remains yet to win in recent form under a hefty 156 lb.
    DATA: model 8.0% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 29 Sep Sedgefield NH Flat 16.8f Good 2/3
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Batchelor's Lad (hrs_62516552) | 4yo G | 156lb | OR - | draw 0 | jockey Joe Williamson | trainer Philip Kirby (14d 0/10) | headgear - | last run 24 days | form 2-4 | MARKET 18.9% | 09:00 median 4.50 | Matchbook 5.10
    comment: Batchelor's Lad comes here in solid shape, a fourth last time out, and a second two starts back, with a 24-day break and previous experience on today's going, while he is yet to win in his last two starts.
    DATA: model 17.8% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 13 Mar Doncaster NH Flat 16.6f Good To Soft 2/6; 27 Oct Newcastle NH Flat 17f Good 4/9 fig 107
    DATA for: Last-run finishing speed +4.7% vs that field (finished strongly)
    DATA against: Trainer 0 wins from 10 runs, last 14 days; Lightly raced: 2 runs in our data, so the model has little to go on
- Billey Shiftit (hrs_61975410) | 4yo F | 149lb | OR - | draw 0 | jockey James Best | trainer Syd Hosie (14d 1/8) | headgear - | last run 225 days | form 60- | MARKET 12.6% | 09:00 median 7.00 | Matchbook 7.80
    comment: The main risk is fitness, as she's unplaced last time and returns after 225 days off.
    DATA: model 6.6% | style Held up (led 5% of runs) | runs in data 2 | last 3: 25 Feb Wincanton NH Flat 15.2f Good To Soft 6/14; 9 Apr Aintree NH Flat 16.9f Good To Soft 14/20
    DATA against: Last-run finishing speed -2.3% vs that field (faded); Returns from a 225-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- Slainte Mo Chara (hrs_17395667891) | 4yo F | 149lb | OR - | draw 0 | jockey Danny McMenamin | trainer Chris Grant (14d 1/3) | headgear - | last run - days | form - | MARKET 8.2% | 09:00 median 10.00 | Matchbook 13.00
    comment: Slainte Mo Chara is an unraced filly with no recorded form to go on, so she is totally unexposed and open to improvement. She carries 149 lb on what looks a debut, and any market for her would be guesswork.
    DATA: model 11.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Thecaptainsmissus (hrs_17395633472) | 4yo F | 149lb | OR - | draw 0 | jockey Richie McLernon | trainer Laura Horsfall (14d 0/5) | headgear - | last run - days | form - | MARKET 3.8% | 09:00 median 21.00 | Matchbook 32.00
    comment: Thecaptainsmissus is unexposed on her debut with no form to assess, so she is open to improvement. She carries 149 lb, and it's a clean slate for a filly who has plenty to prove.
    DATA: model 11.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Pluto Star (hrs_61750150) | 4yo G | 156lb | OR - | draw 0 | jockey Benjamin Macey(5) | trainer Gary Hanmer (14d 0/5) | headgear - | last run 216 days | form 80- | MARKET 2.3% | 09:00 median 41.00 | Matchbook 50.00
    comment: Pluto Star is hard to fancy: unplaced last time out, an eighth two starts back and now returning after 216 days off, while carrying 156 lb.
    DATA: model 7.2% | style Held up (led 5% of runs) | runs in data 2 | last 3: 18 Feb Southwell NH Flat 15.8f Soft 8/11; 18 Apr Bangor-on-Dee NH Flat 16.7f Good 10/11
    DATA against: Last-run finishing speed -2.3% vs that field (faded); Returns from a 216-day break; Lightly raced: 2 runs in our data, so the model has little to go on
