# Card review packet: Kempton, 2026-11-23

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
{"meeting": "kempton", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 12:25 Kempton | race_id rac_32305242814 | CopyBet For Champions League Profit Boosts Juvenile Hurdle Race (GBB Race)
Hurdle | Class 4 | 2m0f0y | going Good | Turf | 10 runners | rating band - | age 3yo
DATA pace: Lone leader - Aukus is the only habitual front-runner and may be allowed an easy lead.
- Thisonesforyou (hrs_56094878) | 3yo G | 161lb | OR - | draw 0 | jockey Gavin Sheehan | trainer Olly Murphy (14d 10/50) | headgear - | last run 20 days | form 1 | MARKET 27.1% | 09:00 median 3.00 | Matchbook 3.55 | CHECK (skip line 2.85)
    comment: Thisonesforyou arrives a winner last time out just 20 days ago, and he has run over today's trip and on this going before, so he looks fit and fresh.
    DATA: model 15.3% | style Held up (led 8% of runs) | runs in data 6 | last 3: 21 Aug Salisbury Flat 8f Good 4/8; 10 Sep Lingfield Flat 10f Standard 1/10; 3 Nov Warwick Hurdle 16f Good 1/7 fig 112
    DATA for: Best recent form figure 112, 16 lb above field average; Trainer 20% wins (10/50), last 14 days; Last-run finishing speed +4.0% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
- Barbury Boy (hrs_57504321) | 3yo G | 154lb | OR - | draw 0 | jockey Tom Bellamy | trainer Alan King (14d 2/18) | headgear - | last run 18 days | form 2 | MARKET 18.9% | 09:00 median 4.50 | Matchbook 5.00
    DATA: model 9.6% | style Prominent (led 3% of runs) | runs in data 7 | last 3: 13 Aug Lingfield Flat 10f Standard 2/8; 16 Sep Sandown Flat 9.9f Good 5/9; 5 Nov Plumpton Hurdle 16f Good 2/4 fig 100
    DATA for: Last-run finishing speed +4.2% vs that field (finished strongly); Good recent finishing positions
- Temple (hrs_57406951) | 3yo G | 154lb | OR - | draw 0 | jockey Jonathan Burke | trainer James Owen (14d 3/40) | headgear - | last run 19 days | form - | MARKET 16.5% | 09:00 median 5.00 | Matchbook 5.80
    comment: Temple is unexposed with no recorded form to go on, so he's open to improvement, and his last run 19 days ago keeps him fresh enough. He carries 154 lb, and there's little to judge him on yet.
    DATA: model 9.9% | style Midfield (led 3% of runs) | runs in data 4 | last 3: 19 Jun Newmarket Flat 12f Good 3/6; 1 Jul Thirsk Flat 12f Good To Firm 3/5; 4 Nov Nottingham Flat 14f Soft 7/10 fig 65
    DATA for: Good recent finishing positions
    DATA against: First run over hurdles in our data
- Aukus (hrs_62876352) | 3yo F | 147lb | OR - | draw 0 | jockey Freddie Gordon | trainer Nicky Henderson (14d 3/17) | headgear - | last run 28 days | form 2 | MARKET 13.1% | 09:00 median 6.50 | Matchbook 7.20
    comment: Aukus arrives off a second last time out just 28 days ago, so she should be fit, and she has run over today's trip before.
    DATA: model 5.1% | style Leader (led 38% of runs) | runs in data 6 | last 3: 19 Jun Goodwood Flat 12f Good 6/8; 9 Jul Newbury Flat 13.3f Good To Firm 5/5; 26 Oct Hereford Hurdle 16f Good To Firm 2/9 fig 92
    DATA for: Last-run finishing speed +4.0% vs that field (finished strongly); Pace: may get an uncontested lead
    DATA against: Best recent form figure 92, 4 lb below field average
- James Choice (hrs_55948228) | 3yo G | 154lb | OR - | draw 0 | jockey Sam Twiston-Davies | trainer Warren Greatrex (14d 6/20) | headgear - | last run 72 days | form - | MARKET 10.5% | 09:00 median 8.00 | Matchbook 9.00
    comment: Unexposed gelding with no recorded form to go on, so there's plenty of room for improvement, and he returns after 72 days off carrying 154 lb. His yard is in cracking form, with six landed from 20 in the last fortnight.
    DATA: model 22.6% | style Midfield (led 5% of runs) | runs in data 4 | last 3: 27 Jul Southwell Flat 11.1f Standard 2/14; 17 Aug Wolverhampton Flat 12.2f Standard 2/10; 12 Sep Lingfield Flat 12f Standard 1/9
    DATA for: Trainer 30% wins (6/20), last 14 days; Last-run finishing speed +4.0% vs that field (finished strongly); Good recent finishing positions
    DATA against: First run over hurdles in our data
- Stepanov (hrs_59551359) | 3yo G | 154lb | OR - | draw 0 | jockey Charlie Todd | trainer Emma Lavelle (14d 3/19) | headgear - | last run 28 days | form 4 | MARKET 6.0% | 09:00 median 13.00 | Matchbook 17.50
    comment: The main risk is that he is yet to win in recent form.
    DATA: model 11.2% | style Held up (led 8% of runs) | runs in data 6 | last 3: 4 Jun Wetherby Flat 10f Good To Firm 2/7; 17 Jun Hamilton Flat 11.1f Good 2/7; 26 Oct Hereford Hurdle 16f Good To Firm 4/9 fig 90
    DATA for: Good recent finishing positions
    DATA against: Best recent form figure 90, 6 lb below field average
- Pantile's Gift (hrs_50435119) | 3yo G | 154lb | OR - | draw 0 | jockey Harry Reed | trainer Harry Derham (14d 2/11) | headgear - | last run 18 days | form 3 | MARKET 3.4% | 09:00 median 21.00 | Matchbook 36.00
    comment: Third last time out and only 18 days ago, Pantile's Gift is fit and has run over today's trip and going, but he is yet to win in his recent form and carries a hefty 154 lb.
    DATA: model 7.7% | style Midfield (led 4% of runs) | runs in data 4 | last 3: 13 Apr Newcastle Flat 10.2f Standard 1/7; 21 Apr Yarmouth Flat 10.1f Good To Firm 8/9; 5 Nov Plumpton Hurdle 16f Good 3/4 fig 88
    DATA for: Good recent finishing positions
    DATA against: Best recent form figure 88, 8 lb below field average
- Mathoura (hrs_54304586) | 3yo F | 147lb | OR - | draw 0 | jockey Ben Godfrey | trainer Joe Tickle (14d 1/7) | headgear - | last run 46 days | form - | MARKET 2.3% | 09:00 median 34.00 | Matchbook 50.00
    comment: Mathoura is lightly raced and unexposed, with no recorded form to go on, so she may have more to offer. She returns after 46 days off and carries 147 lb.
    DATA: model 5.1% | style Midfield (led 4% of runs) | runs in data 6 | last 3: 29 Aug Goodwood Flat 9.9f Soft 4/8; 12 Sep Bath Flat 10.2f Good 3/5; 8 Oct Bath Flat 10.2f Good 4/9
    DATA against: First run over hurdles in our data
- John Harrison (hrs_57316462) | 3yo G | 154lb | OR - | draw 0 | jockey Philip Armson(3) | trainer Alan King (14d 2/18) | headgear - | last run 34 days | form - | MARKET 1.4% | 09:00 median 41.00 | Matchbook 140.00
    comment: Unexposed and open to improvement, John Harrison has no recorded form to go on, so he remains a blank page, though a 34-day break since his last run suggests he should be fit enough. He carries 154 lb.
    DATA: model 9.8% | style Midfield (led 4% of runs) | runs in data 6 | last 3: 12 Aug Ffos Las Flat 8f Good 3/5; 21 Sep Wolverhampton Flat 9.5f Standard 9/11; 20 Oct Yarmouth Flat 10f Soft 9/15 fig 57
    DATA against: First run over hurdles in our data
- Kiss For An Angel (hrs_54242657) | 3yo G | 154lb | OR - | draw 0 | jockey Marc Goldstein | trainer Simon Hodgson (14d 0/2) | headgear - | last run 35 days | form - | MARKET 0.9% | 09:00 median 67.00 | Matchbook 220.00
    comment: Kiss For An Angel has no recorded form to lean on, so he is unexposed and open to improvement, and he returns after 35 days off while carrying 154 lb. Plenty to prove, but nothing here says he has reached his ceiling.
    DATA: model 3.6% | style Held up (led 5% of runs) | runs in data 4 | last 3: 22 May Haydock Flat 8f Good To Soft 10/11; 21 Jun Pontefract Flat 8f Good 7/7; 19 Oct Southwell (AW) Flat 8f Standard 13/14 fig 36
    DATA against: Last-run finishing speed -2.6% vs that field (faded); Poor recent finishing positions; First run over hurdles in our data

## 12:55 Kempton | race_id rac_32305244751 | CopyBet Support Safer Gambling/EBF Stallions 'National Hunt' Novices' Hurdle Race (Qualifier) (GBB Race)
Hurdle | Class 4 | 2m0f0y | going Good | Turf | 4 runners | rating band - | age 4-6yo
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Stars Aligning (hrs_62549214) | 4yo G | 154lb | OR - | draw 0 | jockey Tom Bellamy | trainer Alan King (14d 2/18) | headgear h | last run 254 days | form 2- | MARKET 81.1% | 09:00 median 1.17 | Matchbook 1.16
    DATA: model 51.3% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 14 Mar Kempton NH Flat 16f Good 2/10
    DATA for: Last-run finishing speed +7.1% vs that field (finished strongly)
    DATA against: Returns from a 254-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Thatsnotmyname (hrs_63875448) | 5yo M | 147lb | OR - | draw 0 | jockey Gavin Sheehan | trainer Dan Horsford (14d 0/1) | headgear - | last run 28 days | form 0-86F | MARKET 9.2% | 09:00 median 8.00 | Matchbook 13.00
    DATA: model 7.0% | style Held up (led 4% of runs) | runs in data 4 | last 3: 22 May Worcester Hurdle 16f Good 8/10; 6 Jun Worcester Hurdle 16f Good 6/8; 26 Oct Hereford Hurdle 16f Good To Firm F/12
    DATA against: Poor recent finishing positions; Race comments mention jumping mistakes in 2 of its last 3 runs; Fell or unseated in 1 of its last 3 jumps runs; Pace: steady gallop likely, hard to come from off the pace
- Padel Whacker (hrs_63323561) | 4yo G | 154lb | OR - | draw 0 | jockey Caoilin Quinn | trainer Jamie Moore & Josh Moore (14d 1/22) | headgear - | last run 17 days | form 6-57 | MARKET 7.1% | 09:00 median 10.00 | Matchbook 17.50
    DATA: model 18.9% | style Prominent (led 29% of runs) | runs in data 3 | last 3: 4 Apr Huntingdon NH Flat 15.8f Good 6/8; 26 May Plumpton NH Flat 17.8f Good 5/6; 6 Nov Fontwell Hurdle 17.5f Good 7/10
    DATA against: Last-run finishing speed -4.3% vs that field (faded)
- Storm Dudley (hrs_63809494) | 4yo G | 154lb | OR - | draw 0 | jockey Rex Dingle | trainer David Weston (14d 0/2) | headgear - | last run 13 days | form 83 | MARKET 2.6% | 09:00 median 41.00 | Matchbook 38.00
    DATA: model 22.8% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 6 Jun Worcester NH Flat 16f Good 8/9; 10 Nov Lingfield Hurdle 19.5f Good 3/5
    DATA against: Last-run finishing speed -5.0% vs that field (faded); Lightly raced: 2 runs in our data, so the model has little to go on

## 1:25 Kempton | race_id rac_32305246688 | CopyBet Pay First Past The Post Novices' Limited Handicap Steeple Chase (GBB Race)
Chase | Class 3 | 2m2f0y | going Good | Turf | 3 runners | rating band 0-130 | age 4yo+
DATA pace: Lone leader - Bond Broker is the only habitual front-runner and may be allowed an easy lead.
- Dance And Glance (hrs_37096031) | 6yo G | 158lb | OR 126 | draw 0 | jockey Rex Dingle | trainer Anthony Honeyball (14d 2/9) | headgear t | wind surgery | last run 23 days | form 251-33 | MARKET 39.0% | 09:00 median 2.25 | Matchbook 2.58
    DATA: model 31.5% | style Prominent (led 3% of runs) | runs in data 5 | last 3: 4 Apr Haydock Hurdle 15.7f Good 1/11; 9 May Haydock Hurdle 15.7f Good To Soft 3/16; 31 Oct Ascot Chase 19f Good 3/5 fig 123
    DATA for: Trainer 22% wins (2/9), last 14 days; Good recent finishing positions
- Bond Broker (hrs_34153315) | 7yo G | 158lb | OR 126 | draw 0 | jockey Jay Tidball(5) | trainer Paul Nicholls (14d 2/21) | headgear h | last run 18 days | form 4213-1 | MARKET 30.8% | 09:00 median 3.00 | Matchbook 3.15
    comment: Bond Broker arrives fresh from a win last time out, with a third two starts back and another win three starts back, and he has run over today's trip and going before after just 18 days off.
    DATA: model 34.2% | style Leader (led 83% of runs) | runs in data 4 | last 3: 19 Mar Ludlow Chase 20.1f Good 1/6; 19 Apr Stratford Chase 17f Good 3/4; 5 Nov Plumpton Chase 17f Good 1/3 fig 122
    DATA for: Last-run finishing speed +2.8% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions; Pace: may get an uncontested lead
- Cinquenta (hrs_46295844) | 6yo G | 156lb | OR 124 | draw 0 | jockey Gavin Sheehan | trainer Jamie Snowden (14d 5/23) | headgear - | last run 16 days | form 2161-U | MARKET 30.2% | 09:00 median 3.00 | Matchbook 3.25
    comment: Cinquenta won twice in his last five starts, a winner two starts back and again four starts back, and he is back within 16 days with experience of today's trip. The main risk is that he unseated last time out, and he carries 156 lb.
    DATA: model 34.3% | style Prominent (led 29% of runs) | runs in data 4 | last 3: 7 Mar Sandown Hurdle 19.8f Soft 6/17; 12 Apr Ffos Las Hurdle 15.8f Good To Soft 1/12; 7 Nov Uttoxeter Chase 16f Good UR/4
    DATA for: Trainer 22% wins (5/23), last 14 days; Has won at this trip or further
    DATA against: Fell or unseated in 1 of its last 4 jumps runs

## 1:55 Kempton | race_id rac_32305248625 | Pertemps Network Handicap Hurdle Race (Pertemps Hurdle Series Qualifier) (GBB Race)
Hurdle | Class 2 | 3m0f121y | going Good | Turf | 5 runners | rating band - | age 4yo+
DATA pace: Lone leader - Idaho Fire is the only habitual front-runner and may be allowed an easy lead.
- Marsiac (hrs_49757785) | 5yo G | 156lb | OR 125 | draw 0 | jockey Gavin Sheehan | trainer Kim Bailey & Mat Nicholls (14d 4/18) | headgear - | last run 60 days | form 1140-9 | MARKET 32.5% | 09:00 median 2.75 | Matchbook 3.00
    comment: Marsiac has slipped since a winner four starts back and another five starts back, finishing a fourth three starts back, then unplaced, then a ninth last time out, and he returns after 60 days off carrying 156 lb.
    DATA: model 13.7% | style Prominent (led 38% of runs) | runs in data 2 | last 3: 14 Mar Kempton Hurdle 21f Good 10/13; 24 Sep Perth Hurdle 23.9f Good 9/11
    DATA for: Trainer 22% wins (4/18), last 14 days
    DATA against: Last-run finishing speed -3.3% vs that field (faded); Lightly raced: 2 runs in our data, so the model has little to go on
- Road To Wembley (hrs_36696338) | 5yo G | 157lb | OR 126 | draw 0 | jockey Troy Walsh(10) | trainer Olly Murphy (14d 10/50) | headgear t | last run 30 days | form 1-1142 | MARKET 26.2% | 09:00 median 3.50 | Matchbook 3.65
    comment: Road To Wembley arrives with three wins in his last five starts and a second last time out, and he has run over today's trip and going before. The main risk is a 30-day break, while 157 lb is a hefty burden.
    DATA: model 27.9% | style Midfield (led 3% of runs) | runs in data 6 | last 3: 19 Aug Worcester Hurdle 20f Good 1/10; 25 Sep Worcester Hurdle 20f Good 4/15; 24 Oct Cheltenham Hurdle 24f Good 2/6 fig 111
    DATA for: Trainer 20% wins (10/50), last 14 days; Good recent finishing positions
    DATA against: Recent figures 15 lb below its current mark (looks high in the weights)
- Idaho Fire (hrs_51618854) | 5yo G | 150lb | OR 119 | draw 0 | jockey Jonathan Burke | trainer James Owen (14d 3/40) | headgear - | last run 30 days | form P-3116 | MARKET 25.3% | 09:00 median 3.50 | Matchbook 3.90
    comment: Idaho Fire won two starts back and three starts back, but he was only sixth last time out and pulled up five runs ago, so the form is patchy.
    DATA: model 21.3% | style Leader (led 54% of runs) | runs in data 6 | last 3: 10 Jul Worcester Hurdle 20f Good 1/6; 26 Jul Uttoxeter Hurdle 23.3f Good 1/9; 24 Oct Cheltenham Hurdle 24f Good 6/19 fig 115
    DATA for: Good recent finishing positions; Carries 7 lb less than average; Pace: may get an uncontested lead
    DATA against: Official rating 119, 7 lb below field average; Race comments mention jumping mistakes in 2 of its last 5 runs; Pulled up in 1 of its last 5 jumps runs
- Ernest Gray (hrs_23921555) | 9yo G | 157lb | OR 126 | draw 0 | jockey Tom Bellamy | trainer Alan King (14d 2/18) | headgear p | last run 80 days | form 66-421 | MARKET 8.7% | 09:00 median 10.00 | Matchbook 12.00
    comment: The one concern is an 80-day layoff, with 157 lb to carry.
    DATA: model 23.7% | style Prominent (led 3% of runs) | runs in data 4 | last 3: 7 Jul Uttoxeter Hurdle 23.3f Good 4/11; 15 Aug Market Rasen Hurdle 23.1f Good 2/6; 4 Sep Bangor-on-Dee Hurdle 23.1f Good 1/5
    DATA for: Last-run finishing speed +3.7% vs that field (finished strongly); Good recent finishing positions
    DATA against: Aged 9, older than most of this field
- Ikarak (hrs_27751892) | 8yo G | 165lb | OR 134 | draw 0 | jockey H. J. Horgan(10) | trainer Olly Murphy (14d 10/50) | headgear - | last run 226 days | form 13130- | MARKET 7.4% | 09:00 median 12.00 | Matchbook 13.00
    comment: The main risk is a 226-day absence, and he was unplaced last time out.
    DATA: model 13.5% | style Unknown | runs in data 3 | last 3: 2 Jan Ayr Hurdle 24.3f Soft 1/10; 12 Mar Cheltenham Hurdle 24f Good 3/24; 11 Apr Aintree Hurdle 24.7f Good To Soft 13/22
    DATA for: Official rating 134, 8 lb above field average; Trainer 20% wins (10/50), last 14 days; Has won at this trip or further; Good recent finishing positions
    DATA against: Last-run finishing speed -4.0% vs that field (faded); Carries 8 lb more than average; Returns from a 226-day break

## 2:30 Kempton | race_id rac_32305250562 | CopyBet Follow Us On X Lilies Mares' Hurdle Race (Listed Race) (GBB Race)
Hurdle | Class 1 | 2m5f0y | going Good | Turf | 5 runners | rating band - | age 4yo+
DATA pace: Lone leader - Hollygrove Cha Cha is the only habitual front-runner and may be allowed an easy lead.
- Jackie Hobbs (hrs_40352494) | 6yo M | 154lb | OR 130 | draw 0 | jockey Jonathan Burke | trainer Harry Derham (14d 2/11) | headgear - | last run 232 days | form 14156- | MARKET 39.1% | 09:00 median 2.25 | Matchbook 2.52
    comment: Jackie Hobbs won twice in her last five starts, a winner three starts back and again five starts back, and she has run over today's trip and going before. The main risk is a 232-day absence, with a sixth last time out and 154 lb to carry.
    DATA: model 20.2% | style Held up (led 5% of runs) | runs in data 3 | last 3: 23 Jan Warwick Hurdle 19f Good To Soft 1/16; 12 Mar Cheltenham Hurdle 16.8f Good 5/22; 5 Apr Fairyhouse Hurdle 20f Yielding To Soft 6/11
    DATA against: Returns from a 232-day break
- Take No Chances (hrs_29816451) | 8yo M | 154lb | OR 146 | draw 0 | jockey Tristan Durrell | trainer Dan Skelton (14d 15/80) | headgear - | last run 23 days | form 342-03 | MARKET 30.1% | 09:00 median 3.00 | Matchbook 3.20
    comment: Take No Chances arrives in sound order after a third last time out, with a second three starts back and a third five starts back, and she has run over today's trip and going.
    DATA: model 17.6% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 11 Apr Aintree Hurdle 24.7f Good To Soft 2/11; 10 Oct Chepstow Hurdle 19.5f Good To Soft 12/17; 31 Oct Wetherby Hurdle 24f Good 3/3 fig 142
    DATA for: Best recent form figure 142, 15 lb above field average; Official rating 146, 12 lb above field average; Good recent finishing positions
- Hollygrove Cha Cha (hrs_39940726) | 6yo M | 158lb | OR 140 | draw 0 | jockey Gavin Sheehan | trainer Jamie Snowden (14d 5/23) | headgear - | last run 247 days | form 31518- | MARKET 20.2% | 09:00 median 4.50 | Matchbook 4.80
    comment: Hollygrove Cha Cha has two wins in her last five starts, a winner two starts back and again four starts back, and she has run over today's trip and going before; the one concern is a 247-day absence after an eighth last time out, with 158 lb to carry.
    DATA: model 37.2% | style Leader (led 54% of runs) | runs in data 3 | last 3: 16 Jan Windsor Chase 20.2f Soft 5/9; 7 Feb Warwick Hurdle 21f Heavy 1/4; 21 Mar Kelso Hurdle 24.5f Good To Soft 8/9
    DATA for: Official rating 140, 6 lb above field average; Trainer 22% wins (5/23), last 14 days; Has won at this trip or further; Pace: may get an uncontested lead
    DATA against: Last-run finishing speed -17.0% vs that field (faded); Returns from a 247-day break; Race comments mention jumping mistakes in 2 of its last 3 runs
- La Pinsonniere (hrs_37052372) | 6yo M | 154lb | OR 126 | draw 0 | jockey Sam Twiston-Davies | trainer Nicky Henderson (14d 3/17) | headgear b (1st time) | last run 31 days | form 2-9348 | MARKET 6.7% | 09:00 median 13.00 | Matchbook 15.00
    comment: Yet to win in her last five, La Pinsonniere has still hit the frame with a third three starts back and a second five starts back, and she has run over today's trip and going before. Last time's eighth, 31 days ago, is the worry, with 154 lb to carry.
    DATA: model 16.3% | style Midfield (led 3% of runs) | runs in data 7 | last 3: 12 Jun Newton Abbot Chase 25.8f Good 3/4; 15 Jul Uttoxeter Chase 24f Good 4/4; 23 Oct Cheltenham Hurdle 20f Good To Soft 8/11 fig 113
    DATA for: First-time headgear
    DATA against: Best recent form figure 113, 14 lb below field average; Official rating 126, 8 lb below field average
- St Irene (hrs_412694905) | 6yo M | 156lb | OR 127 | draw 0 | jockey Jack Quinlan | trainer Nick Scholfield (14d 1/13) | headgear - | last run 23 days | form 2110-4 | MARKET 3.9% | 09:00 median 23.00 | Matchbook 27.00
    comment: St Irene won twice in her last five starts, but she has been beaten since, a fourth last time out after an unplaced run, and she carries 156 lb off a mark of 127.
    DATA: model 8.7% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 12 Mar Cheltenham Hurdle 16.8f Good 21/22; 31 Oct Wetherby Hurdle 16f Good 4/4 fig 126
    DATA against: Official rating 127, 7 lb below field average; Lightly raced: 2 runs in our data, so the model has little to go on

## 3:05 Kempton | race_id rac_32305252499 | CopyBet Supporting UK Horse Racing Handicap Steeple Chase (Challenger Staying Chase Series Qualifier) (GBB Race)
Chase | Class 3 | 3m0f0y | going Good | Turf | 5 runners | rating band 0-135 | age 4yo+
DATA pace: Lone leader - Tapley is the only habitual front-runner and may be allowed an easy lead.
- King Califet (hrs_38002454) | 7yo G | 148lb | OR 114 | draw 0 | jockey Adam Wedge | trainer Emma Lavelle (14d 3/19) | headgear - | last run 248 days | form 4/841- | MARKET 25.9% | 09:00 median 3.50 | Matchbook 3.75 | CHECK (skip line 3.32)
    comment: King Califet won last time out, but that came 248 days ago and he's had a long absence to shake off, while a fourth and an eighth before that offer little comfort.
    DATA: model 21.7% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 28 Feb Newbury Chase 19.9f Good To Soft 4/8; 20 Mar Newbury Chase 22.4f Good To Soft 1/11
    DATA for: Last-run finishing speed +2.2% vs that field (finished strongly); Carries 12 lb less than average
    DATA against: Official rating 114, 12 lb below field average; Returns from a 248-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- Tapley (hrs_26948047) | 9yo G | 161lb | OR 127 | draw 0 | jockey Caoilin Quinn | trainer Jamie Moore & Josh Moore (14d 1/22) | headgear t | last run 23 days | form 3-4113 | MARKET 25.6% | 09:00 median 3.50 | Matchbook 3.80
    comment: Tapley arrives in cracking recent form, third last time out after back-to-back wins, and he has run over today's trip and going before. A 23-day break looks fine, though a weight of 161 lb and a quiet yard are the only concerns.
    DATA: model 28.6% | style Leader (led 38% of runs) | runs in data 7 | last 3: 22 Sep Fontwell Chase 19.5f Good 1/4; 19 Oct Plumpton Chase 20f Good 1/5 fig 129; 31 Oct Ascot Chase 24f Good 3/10 fig 126
    DATA for: Last-run finishing speed +3.1% vs that field (finished strongly); Good recent finishing positions; Pace: may get an uncontested lead
    DATA against: Race comments mention jumping mistakes in 4 of its last 5 runs
- Glynn Brae (hrs_39941139) | 6yo G | 168lb | OR 134 | draw 0 | jockey Sam Twiston-Davies | trainer Nigel & Willy Twiston-Davies (14d 4/26) | headgear - | last run 23 days | form 441-95 | MARKET 20.9% | 09:00 median 4.00 | Matchbook 4.90
    comment: The main risk is a ninth two starts back and the 168 lb he carries.
    DATA: model 21.5% | style Prominent (led 5% of runs) | runs in data 5 | last 3: 29 Mar Ascot Hurdle 21.7f Good 1/9; 10 Oct Chepstow Hurdle 19.5f Good To Soft 9/17; 31 Oct Ascot Chase 19f Good 5/5 fig 126
    DATA for: Official rating 134, 8 lb above field average
    DATA against: Recent figures 8 lb below its current mark (looks high in the weights); Last-run finishing speed -3.1% vs that field (faded); Carries 8 lb more than average
- Fierce Warrior (hrs_34961402) | 7yo G | 157lb | OR 123 | draw 0 | jockey Freddie Gordon | trainer Nicky Henderson (14d 3/17) | headgear p | wind surgery | last run 222 days | form 21P28- | MARKET 16.5% | 09:00 median 5.50 | Matchbook 5.90
    comment: Fierce Warrior has a win and two seconds in his last five starts, including a second two starts back, and he has run over today's trip and going before. The risk is a 222-day absence, plus an eighth last time out and 157 lb on his back.
    DATA: model 18.1% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 22 Mar Carlisle Chase 24.5f Good To Soft 2/12; 15 Apr Haydock Chase 28.4f Good 8/11
    DATA against: Last-run finishing speed -3.5% vs that field (faded); Returns from a 222-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- El Rio (hrs_28190904) | 9yo G | 164lb | OR 130 | draw 0 | jockey Tom Bellamy | trainer Kim Bailey & Mat Nicholls (14d 4/18) | headgear - | last run 61 days | form 13/3-F | MARKET 11.1% | 09:00 median 8.30 | Matchbook 8.80
    comment: El Rio showed solid consistency before his last-day fall, finishing third twice and winning four starts back, and he has run on today's going before.
    DATA: model 10.1% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 23 Sep Perth Chase 23.8f Good F/8
    DATA for: Trainer 22% wins (4/18), last 14 days
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on; Fell or unseated in 1 of its last 1 jumps runs

## 3:40 Kempton | race_id rac_32305254436 | CopyBet Overnight Best Odds Guaranteed Conditional Jockeys' Handicap Hurdle Race
Hurdle | Class 4 | 2m0f0y | going Good | Turf | 9 runners | rating band 0-110 | age 3yo+
DATA pace: Lone leader - Gordon Grey is the only habitual front-runner and may be allowed an easy lead.
- Woodstock City (hrs_32733463) | 6yo G | 165lb | OR 106 | draw 0 | jockey Troy Walsh(10) | trainer Olly Murphy (14d 10/50) | headgear t | wind surgery | last run 20 days | form F43/31 | MARKET 26.5% | 09:00 median 3.00 | Matchbook 3.75 | CHECK (skip line 2.85)
    comment: Winner last time out and third in each of the two runs before that, Woodstock City arrives fresh enough after 20 days and has run over today's trip and going before.
    DATA: model 23.0% | style Midfield (led 5% of runs) | runs in data 5 | last 3: 18 Jul Nottingham Flat 10.2f Good To Firm 2/6; 26 Sep Market Rasen Hurdle 18.6f Good 3/11; 3 Nov Warwick Hurdle 16f Good 1/11 fig 108
    DATA for: Best recent form figure 108, 4 lb above field average; Trainer 20% wins (10/50), last 14 days; Last-run finishing speed +2.8% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
- Gallivanted (hrs_44721880) | 4yo G | 168lb | OR 109 | draw 0 | jockey Calum Hogan(3) | trainer Harry Derham (14d 2/11) | headgear tp | last run 13 days | form 33-72V | MARKET 21.1% | 09:00 median 3.75 | Matchbook 4.50
    comment: Gallivanted arrives fresh from a run 13 days ago, with a second two starts back and two thirds in his last five, and he has run over today's trip and on this going.
    DATA: model 16.7% | style Midfield (led 3% of runs) | runs in data 9 | last 3: 14 May Salisbury Flat 14.2f Good 8/9; 10 Oct Chepstow Hurdle 16.1f Good To Soft 7/12; 28 Oct Huntingdon Hurdle 16f Good 2/8 fig 108
    DATA for: Best recent form figure 108, 4 lb above field average; Official rating 109, 6 lb above field average; Has won at this trip or further
    DATA against: Carries 6 lb more than average
- Gordon Grey (hrs_32443579) | 6yo G | 160lb | OR 101 | draw 0 | jockey Toby McCain-Mitchell | trainer James Owen (14d 3/40) | headgear t | last run 57 days | form 6U2/1- | MARKET 19.5% | 09:00 median 4.50 | Matchbook 4.70
    comment: Gordon Grey won last time out and was second two starts back, while he has run over today's trip and on this going, but 57 days off and 160 lb on his back make this tougher.
    DATA: model 8.9% | style Leader (led 54% of runs) | runs in data 5 | last 3: 31 Aug Epsom Downs Flat 12f Good To Soft 6/14; 10 Sep Epsom Downs Flat 12f Good To Soft 4/6; 27 Sep Epsom Downs Flat 12f Good 10/13
    DATA for: Pace: may get an uncontested lead
    DATA against: Last-run finishing speed -4.0% vs that field (faded); First run over hurdles in our data
- A Good Yomp (hrs_39488302) | 7yo G | 157lb | OR 98 | draw 0 | jockey Shane Quinlan | trainer Andrew Martin (14d 0/0) | headgear h | last run 20 days | form 334-15 | MARKET 12.5% | 09:00 median 7.00 | Matchbook 7.20
    comment: A Good Yomp was beaten into fifth last time out after winning two starts back, and he has run over today's trip and going before, but carrying 157 lb off an official mark of 98 looks a big ask.
    DATA: model 10.6% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 29 Mar Ascot Hurdle 23.6f Good 4/8; 15 May Aintree Hurdle 16.9f Good 1/10; 3 Nov Warwick Hurdle 16f Good 5/11 fig 95
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 95, 9 lb below field average
- Not At That Price (hrs_51186821) | 6yo G | 162lb | OR 103 | draw 0 | jockey Daire McConville(3) | trainer Charlie Longsdon (14d 2/14) | headgear - | wind surgery | last run 47 days | form 263-2P | MARKET 7.3% | 09:00 median 12.00 | Matchbook 12.50
    comment: The risk is a pulled-up effort last time out, and he returns after 47 days under 162 lb.
    DATA: model 14.6% | style Unknown | runs in data 4 | last 3: 5 Feb Doncaster Hurdle 16.6f Soft 3/12; 2 May Uttoxeter Hurdle 15.8f Good 2/7; 7 Oct Worcester Hurdle 20f Good PU/10
    DATA against: Pulled up in 1 of its last 4 jumps runs
- Dambuster (hrs_37207926) | 5yo G | 167lb | OR 108 | draw 0 | jockey Jude Fernandes(5) | trainer Jamie Moore & Josh Moore (14d 1/22) | headgear - | last run 581 days | form 22/ | MARKET 5.1% | 09:00 median 15.00 | Matchbook 20.00
    comment: Dambuster has finished second in both recent starts and has run over today's trip and going, but he returns after 581 days off and with a stable struggling at 1/22 lately.
    DATA: model 9.0% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Official rating 108, 5 lb above field average
    DATA against: Carries 5 lb more than average; Returns from a 581-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Graffiti (hrs_26473188) | 7yo G | 155lb | OR 96 | draw 0 | jockey Megan Bevan(5) | trainer Gary Brown (14d 0/1) | headgear t | last run 18 days | form 423/10 | MARKET 3.9% | 09:00 median 23.00 | Matchbook 26.00
    DATA: model 9.2% | style Midfield (led 4% of runs) | runs in data 7 | last 3: 7 Jul Brighton Flat 9.9f Good To Firm 1/7; 28 Aug Fontwell Hurdle 17.7f Good 1/9; 5 Nov Newbury Hurdle 16.5f Good To Soft 15/16
    DATA for: Has won at this trip or further; Good recent finishing positions; Carries 7 lb less than average
    DATA against: Official rating 96, 7 lb below field average
- Savant du Mesnil (hrs_40553730) | 6yo G | 155lb | OR 96 | draw 0 | jockey Rian Corcoran | trainer Kayley Woollacott (14d 2/9) | headgear tp (1st time) | last run 33 days | form 7PP1-7 | MARKET 2.0% | 09:00 median 41.00 | Matchbook 55.00
    comment: Savant du Mesnil is hard to fancy after a seventh last time out and two pulled-up efforts in his last five starts, though he did win two starts back and has run over today's trip and going.
    DATA: model 3.0% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 21 Oct Worcester Hurdle 16f Good To Soft 7/7
    DATA for: Trainer 22% wins (2/9), last 14 days; Carries 7 lb less than average; First-time headgear
    DATA against: Official rating 96, 7 lb below field average; Last-run finishing speed -11.2% vs that field (faded); Lightly raced: 1 run in our data, so the model has little to go on
- Royal Approval (hrs_36528219) | 5yo G | 166lb | OR 107 | draw 0 | jockey Paddy Hanlon | trainer Joe Tickle (14d 1/7) | headgear - | last run 25 days | form 65-P | MARKET 1.9% | 09:00 median 51.00 | Matchbook 55.00
    comment: The main risk is a poor recent book: pulled up last time, a fifth two starts back, a sixth three starts back, and he is yet to win in that spell.
    DATA: model 5.1% | style Midfield (led 5% of runs) | runs in data 3 | last 3: 30 May Listowel Hurdle 20.4f Yielding PU/9; 7 Jul Tramore Flat 12f Good 6/6; 29 Oct Bath Flat 10f Soft 10/12 fig 61
    DATA against: Last-run finishing speed -2.3% vs that field (faded); Poor recent finishing positions; Pulled up in 1 of its last 1 jumps runs
