# Card review packet: Musselburgh, 2026-11-27

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
{"meeting": "musselburgh", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 11:50 Musselburgh | race_id rac_32305756119 | Watch On Racing TV Juvenile Maiden Hurdle Race (GBB Race)
Hurdle | Class 4 | 1m7f124y | going Good To Soft | Turf | 7 runners | rating band - | age 3yo
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Guevara (hrs_57717947) | 3yo C | 156lb | OR - | draw 0 | jockey Brian Hughes | trainer Adam Nicol (14d 0/3) | headgear - | last run 145 days | form - | MARKET 41.9% | 09:00 median 2.10 | Matchbook 2.30
    DATA: model 12.1% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 145-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Elm Creek (hrs_57255142) | 3yo G | 156lb | OR - | draw 0 | jockey Shane Fitzgerald | trainer Rebecca Menzies (14d 0/10) | headgear p | last run 7 days | form 33 | MARKET 26.0% | 09:00 median 3.25 | Matchbook 3.90
    DATA: model 10.1% | style Midfield (led 4% of runs) | runs in data 5 | last 3: 10 Apr Dundalk Flat 10.7f Standard 5/6; 25 Oct Market Rasen Hurdle 16.5f Good To Soft 3/7 fig 83; 20 Nov Catterick Hurdle 15.5f Good 3/10 fig 101
    DATA for: Best recent form figure 101, 13 lb above field average; Last-run finishing speed +4.0% vs that field (finished strongly); Good recent finishing positions
    DATA against: Trainer 0 wins from 10 runs, last 14 days
- Shushi (hrs_55634229) | 3yo F | 149lb | OR - | draw 0 | jockey Sean Quinlan | trainer Padraig Roche (14d 0/5) | headgear - | last run 24 days | form 7 | MARKET 19.2% | 09:00 median 4.50 | Matchbook 5.20
    DATA: model 16.0% | style Prominent (led 8% of runs) | runs in data 5 | last 3: 10 Jun Kempton Flat 12f Standard To Slow 6/9; 5 Jul Southwell Flat 14.1f Standard 2/7; 3 Nov Fairyhouse (IRE) Hurdle 16f Good To Yielding 7/13 fig 83
    DATA for: Last-run finishing speed +3.1% vs that field (finished strongly)
    DATA against: Best recent form figure 83, 5 lb below field average
- Northern Man (hrs_60342933) | 3yo G | 156lb | OR - | draw 0 | jockey Bruce Lynn | trainer N. W. Alexander (14d 0/5) | headgear h (1st time) | last run 197 days | form - | MARKET 7.3% | 09:00 median 12.00 | Matchbook 13.50
    DATA: model 12.1% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: First-time headgear
    DATA against: Returns from a 197-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Phantom Shadow (hrs_52709783) | 3yo G | 156lb | OR - | draw 0 | jockey Craig Nichol | trainer Ewan Whillans (14d 0/5) | headgear - | last run 79 days | form - | MARKET 4.1% | 09:00 median 21.00 | Matchbook 25.00
    DATA: model 24.1% | style Midfield (led 4% of runs) | runs in data 8 | last 3: 20 Jul Ayr Flat 10f Good To Firm 1/10; 8 Aug Ayr Flat 10f Good 7/13; 9 Sep Redcar Flat 10f Good 4/9
    DATA against: First run over hurdles in our data
- Royal Baroness (hrs_56873775) | 3yo F | 149lb | OR - | draw 0 | jockey Ben Smith(7) | trainer R. Mike Smith (14d 0/1) | headgear h (1st time) | last run 59 days | form U | MARKET 0.8% | 09:00 median 126.00 | Matchbook 160.00
    DATA: model 19.6% | style Held up (led 8% of runs) | runs in data 3 | last 3: 18 May Carlisle Flat 7.8f Soft 4/10; 5 Jun Musselburgh Flat 8f Good 3/6; 29 Sep Sedgefield Hurdle 16.8f Good UR/7
    DATA for: First-time headgear
    DATA against: Fell or unseated in 1 of its last 1 jumps runs; Pace: steady gallop likely, hard to come from off the pace
- Al Qatem (hrs_57718696) | 3yo G | 156lb | OR - | draw 0 | jockey Lorcan Murtagh | trainer Barry Murtagh (14d 0/2) | headgear - | last run 24 days | form 7 | MARKET 0.7% | 09:00 median 151.00 | Matchbook 260.00
    DATA: model 5.9% | style Held up (led 5% of runs) | runs in data 3 | last 3: 1 Jun Wolverhampton Flat 8.6f Standard 8/9; 30 Jun Salisbury Flat 9.9f Good To Firm 6/7; 3 Nov Sedgefield Hurdle 17f Good 7/8 fig 79
    DATA against: Best recent form figure 79, 9 lb below field average; Poor recent finishing positions; Pace: steady gallop likely, hard to come from off the pace

## 12:20 Musselburgh | race_id rac_32305758056 | Musselburgh Racecourse Premium Annual Membership Handicap Steeple Chase
Chase | Class 5 | 2m4f68y | going Good To Soft | Turf | 6 runners | rating band 0-100 | age 4yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Nevershedatear (hrs_50412649) | 5yo M | 160lb | OR 92 | draw 0 | jockey Charlie Maggs | trainer Oliver Greenall & Josh Guerriero (14d 3/18) | headgear - | last run 28 days | form U25-41 | MARKET 38.9% | 09:00 median 2.25 | Matchbook 2.52
    comment: She has run over today's trip, and 28 days since her last outing is no concern.
    DATA: model 24.9% | style Prominent (led 29% of runs) | runs in data 7 | last 3: 10 Apr Sedgefield Hurdle 16.8f Good 5/5; 16 May Bangor-on-Dee Hurdle 19.6f Good 4/11; 30 Oct Uttoxeter Chase 20f Good 1/11 fig 92
    DATA for: Last-run finishing speed +5.0% vs that field (finished strongly); Has won at this trip or further
    DATA against: Fell or unseated in 1 of its last 5 jumps runs
- Carcaci Castle (hrs_25026316) | 10yo G | 168lb | OR 100 | draw 0 | jockey Oakley Brown(5) | trainer Sandy Thomson (14d 2/5) | headgear p | wind surgery | last run 21 days | form 572P-5 | MARKET 16.6% | 09:00 median 5.50 | Matchbook 5.70
    comment: Carcaci Castle is yet to win in his last five, but a second three starts back shows his ability, and he has run over today's trip and going and returns fresh after 21 days.
    DATA: model 12.4% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 29 Jan Ayr Chase 16.5f Soft PU/11; 6 Nov Hexham Chase 15.5f Good 5/7 fig 97
    DATA for: Best recent form figure 97, 5 lb above field average; Official rating 100, 5 lb above field average; Trainer 40% wins (2/5), last 14 days
    DATA against: Carries 5 lb more than average; Lightly raced: 2 runs in our data, so the model has little to go on; Pulled up in 1 of its last 2 jumps runs
- Flash du Pistolet (hrs_28824551) | 8yo G | 167lb | OR 99 | draw 0 | jockey Sean Quinlan | trainer Stuart Coltherd (14d 0/1) | headgear tp | last run 21 days | form 572-54 | MARKET 15.0% | 09:00 median 6.00 | Matchbook 6.60
    comment: The main risk is that he is yet to win in his last five starts and carries 167 lb off a mark of 99.
    DATA: model 20.8% | style Midfield (led 3% of runs) | runs in data 7 | last 3: 13 Apr Hexham Chase 15.6f Good 2/11; 6 May Kelso Chase 17.1f Good 5/7; 6 Nov Hexham Chase 15.5f Good 4/7 fig 97
    DATA for: Best recent form figure 97, 5 lb above field average
- Huit Reflets (hrs_24555363) | 9yo G | 148lb | OR 80 | draw 0 | jockey Jamie Hamilton | trainer Mark Walford (14d 2/11) | headgear v | last run 24 days | form 426764 | MARKET 12.1% | 09:00 median 7.50 | Matchbook 8.00
    comment: Huit Reflets is winless in his last six, with a fourth last time out following a run of sixth, seventh and sixth, so he is hard to fancy under 148 lb.
    DATA: model 13.4% | style Prominent (led 3% of runs) | runs in data 11 | last 3: 26 Sep Market Rasen Hurdle 18.6f Good 7/11; 20 Oct Hexham Hurdle 16f Good 6/10 fig 83; 3 Nov Sedgefield Chase 16.5f Good 4/8 fig 75
    DATA for: Carries 15 lb less than average
    DATA against: Best recent form figure 83, 9 lb below field average; Official rating 80, 15 lb below field average
- Too Cool Forshrule (hrs_37576770) | 7yo G | 165lb | OR 97 | draw 0 | jockey Brian Hughes | trainer Jackie Stephen (14d 0/0) | headgear - | last run 34 days | form U1PU-P | MARKET 10.9% | 09:00 median 8.00 | Matchbook 9.00
    comment: The main risk is obvious: he has pulled up, unseated and pulled up again in his last three, and carries 165 lb after 34 days off.
    DATA: model 14.8% | style Midfield (led 4% of runs) | runs in data 6 | last 3: 22 Mar Carlisle Chase 15.9f Good To Soft PU/12; 13 Apr Hexham Chase 15.6f Good UR/11; 24 Oct Kelso Chase 17f Good PU/5
    DATA for: Has won at this trip or further
    DATA against: Poor recent finishing positions; Fell or unseated in 2 of its last 5 jumps runs; Pulled up in 2 of its last 5 jumps runs
- Humble Jumble (hrs_46850818) | 6yo G | 168lb | OR 100 | draw 0 | jockey Patrick Wadge | trainer Lucinda Russell & Michael Scudamore (14d 1/19) | headgear - | last run 22 days | form 373P-4 | MARKET 6.4% | 09:00 median 13.00 | Matchbook 16.50
    comment: Humble Jumble arrives fit after 22 days off, with a fourth last time out and a third five starts back, and he has run over today's trip and going before.
    DATA: model 13.7% | style Prominent (led 5% of runs) | runs in data 3 | last 3: 3 Mar Newcastle Hurdle 20.3f Good To Soft 3/12; 24 Apr Perth Hurdle 20.2f Good PU/8; 5 Nov Newcastle Chase 20f Good 4/5
    DATA for: Official rating 100, 5 lb above field average
    DATA against: Carries 5 lb more than average; Race comments mention jumping mistakes in 2 of its last 3 runs; Pulled up in 1 of its last 3 jumps runs

## 12:50 Musselburgh | race_id rac_32305759993 | Protech Network Solutions Ltd Maiden Hurdle Race (Go North Night Nurse Series Qualifier) (GBB Race)
Hurdle | Class 4 | 1m7f124y | going Good To Soft | Turf | 7 runners | rating band - | age 4yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Novak (hrs_52204572) | 4yo G | 158lb | OR 127 | draw 0 | jockey Brian Hughes | trainer Olly Murphy (14d 9/50) | headgear - | last run 181 days | form 3/22-6 | MARKET 69.4% | 09:00 median 1.29 | Matchbook 1.35
    DATA: model 32.0% | style Midfield (led 4% of runs) | runs in data 17 | last 3: 25 Aug Musselburgh Flat 7.1f Good 1/10; 14 Sep Thirsk Flat 7f Good 7/12; 29 Sep Ayr Flat 7.2f Heavy 6/11
    DATA for: Official rating 127, 19 lb above field average
    DATA against: Returns from a 181-day break; First run over hurdles in our data
- Hunters Spring (hrs_40787278) | 5yo M | 151lb | OR 100 | draw 0 | jockey Patrick Wadge | trainer Lucinda Russell & Michael Scudamore (14d 1/19) | headgear - | last run 31 days | form 3U-P34 | MARKET 9.5% | 09:00 median 8.00 | Matchbook 12.00
    DATA: model 12.8% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 13 May Perth Hurdle 20.2f Good To Soft PU/11; 23 Sep Perth Hurdle 16.2f Good 3/10; 27 Oct Newcastle Hurdle 17f Good 4/6 fig 90
    DATA against: Best recent form figure 90, 4 lb below field average; Official rating 100, 8 lb below field average; Race comments mention jumping mistakes in 2 of its last 5 runs; Fell or unseated in 1 of its last 5 jumps runs; Pulled up in 1 of its last 5 jumps runs
- Oor Wish (hrs_51024183) | 6yo M | 151lb | OR 97 | draw 0 | jockey Bruce Lynn | trainer N. W. Alexander (14d 0/5) | headgear - | last run 34 days | form 464-73 | MARKET 7.7% | 09:00 median 11.00 | Matchbook 13.50
    DATA: model 12.5% | style Prominent (led 3% of runs) | runs in data 6 | last 3: 23 Apr Perth Hurdle 20.2f Good 4/7; 13 May Perth Hurdle 20.2f Good To Soft 7/11; 24 Oct Kelso Hurdle 16f Good 3/6 fig 98
    DATA for: Best recent form figure 98, 4 lb above field average
    DATA against: Official rating 97, 11 lb below field average
- Battle of Arsuf (hrs_17394717718) | 4yo G | 158lb | OR - | draw 0 | jockey Toby Wynne | trainer Donald McCain (14d 2/21) | headgear - | last run 27 days | form 4-6 | MARKET 5.1% | 09:00 median 17.00 | Matchbook 19.00
    DATA: model 6.7% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 31 Oct Ayr Hurdle 16f Good To Soft 6/8 fig 94
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Tee Aitch Aye (hrs_51373721) | 5yo G | 158lb | OR - | draw 0 | jockey Sean Quinlan | trainer Iain Jardine (14d 0/13) | headgear - | last run 38 days | form - | MARKET 3.9% | 09:00 median 21.00 | Matchbook 27.00
    DATA: model 14.0% | style Midfield (led 3% of runs) | runs in data 10 | last 3: 20 Sep Hamilton Flat 9.2f Heavy 4/9; 12 Oct Musselburgh Flat 8.9f Good To Soft 5/8; 20 Oct Newcastle (AW) Flat 8f Standard 10/12 fig 58
    DATA against: Trainer 0 wins from 13 runs, last 14 days; First run over hurdles in our data
- Falcon Nine (hrs_30908514) | 6yo G | 158lb | OR - | draw 0 | jockey Jamie Hamilton | trainer Iain Jardine (14d 0/13) | headgear p | last run 31 days | form /- | MARKET 3.9% | 09:00 median 23.00 | Matchbook 30.00
    DATA: model 13.5% | style Held up (led 3% of runs) | runs in data 15 | last 3: 1 Oct Newcastle Flat 8f Standard 2/8; 8 Oct Ayr Flat 10f Heavy 2/12; 27 Oct Catterick Flat 12f Soft 8/10 fig 43
    DATA for: Good recent finishing positions
    DATA against: Trainer 0 wins from 13 runs, last 14 days; First run over hurdles in our data; Pace: steady gallop likely, hard to come from off the pace
- Brand New Man (hrs_17396103865) | 4yo G | 158lb | OR - | draw 0 | jockey Jack Power(5) | trainer Jean McGregor (14d 0/0) | headgear - | last run 48 days | form 7-6 | MARKET 0.5% | 09:00 median 101.00 | Matchbook 340.00
    DATA: model 8.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on

## 1:25 Musselburgh | race_id rac_32305761930 | 100% Racing TV Profits Back To Racing Mares' Handicap Hurdle Race (Challenger Mares' Hurdle Series Qualifier)
Hurdle | Class 4 | 2m3f171y | going Good To Soft | Turf | 4 runners | rating band 0-120 | age 3yo+
DATA pace: Lone leader - Snowrocco is the only habitual front-runner and may be allowed an easy lead.
- Iamyouare (hrs_53181443) | 6yo M | 168lb | OR 114 | draw 0 | jockey Brian Hughes | trainer Donald McCain (14d 2/21) | headgear p | last run 31 days | form 3F2211 | MARKET 40.4% | 09:00 median 2.20 | Matchbook 2.46
    comment: Iamyouare arrives in cracking form, a winner last time out and again two starts back, with a second three starts back before that, and she has run over today's trip and going.
    DATA: model 43.9% | style Prominent (led 23% of runs) | runs in data 9 | last 3: 4 Sep Bangor-on-Dee Hurdle 19.6f Good 2/5; 1 Oct Southwell Hurdle 20.4f Good 1/5; 27 Oct Bangor-on-Dee Hurdle 19.5f Good 1/10 fig 116
    DATA for: Best recent form figure 116, 8 lb above field average; Official rating 114, 6 lb above field average; Last-run finishing speed +4.9% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Carries 6 lb more than average; Fell or unseated in 1 of its last 5 jumps runs
- Gintime (hrs_48006042) | 6yo M | 152lb | OR 98 | draw 0 | jockey Ella McGarry(10) | trainer Nicky Richards (14d 1/10) | headgear - | last run 24 days | form 1958-3 | MARKET 29.2% | 09:00 median 3.25 | Matchbook 3.25
    comment: Gintime arrives fresh from a third last time out, 24 days ago, and has run on today's going before, while a win five starts back shows her ability.
    DATA: model 22.9% | style Prominent (led 5% of runs) | runs in data 4 | last 3: 21 Mar Kelso Hurdle 16.2f Good To Soft 5/15; 13 Apr Hexham Hurdle 16.2f Good 8/8; 3 Nov Sedgefield Hurdle 17f Good 3/11 fig 97
    DATA for: Carries 10 lb less than average
    DATA against: Best recent form figure 97, 10 lb below field average; Official rating 98, 10 lb below field average
- Snowrocco (hrs_34775006) | 7yo M | 165lb | OR 111 | draw 0 | jockey Ryan Mania | trainer Adam Nicol (14d 0/3) | headgear t | last run 21 days | form 1405-2 | MARKET 20.4% | 09:00 median 4.33 | Matchbook 4.90
    comment: Snowrocco comes here on a good note after a second last time out, fresh enough at 21 days, and she has run over today's trip and on this going before. Carrying 165 lb is the main risk, though, with only one win in her last five starts.
    DATA: model 18.3% | style Leader (led 43% of runs) | runs in data 5 | last 3: 20 Mar Musselburgh Hurdle 23.8f Good To Soft 12/13; 31 Mar Newcastle Hurdle 22f Good To Soft 5/8; 6 Nov Hexham Hurdle 20f Good 2/9 fig 110
    DATA for: Has won at this trip or further; Pace: may get an uncontested lead
- A Chara (hrs_50622649) | 5yo M | 162lb | OR 108 | draw 0 | jockey Toby Wynne | trainer Oliver Greenall & Josh Guerriero (14d 3/18) | headgear p (1st time) | last run 20 days | form /42-35 | MARKET 10.0% | 09:00 median 9.00 | Matchbook 10.00
    comment: A Chara arrives in solid, consistent form, a second three starts back and a third two runs ago, and she has run over today's trip and going before. A fifth last time out is the main concern, though she is yet to win in her last four and carries 162 lb.
    DATA: model 14.9% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 4 Oct Uttoxeter Hurdle 23.3f Good 3/4; 7 Nov Uttoxeter Hurdle 23.5f Good 5/9 fig 107
    DATA for: First-time headgear
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on

## 2:00 Musselburgh | race_id rac_32305763867 | Musselburgh Racecourse 2027 Annual Membership Handicap Steeple Chase (Go North One Man Series Qualifier) (GBB Race)
Chase | Class 4 | 1m7f182y | going Good To Soft | Turf | 5 runners | rating band 0-110 | age 4yo+
DATA pace: Lone leader - Scriabin is the only habitual front-runner and may be allowed an easy lead.
- Masterfield (hrs_59367245) | 4yo G | 152lb | OR 101 | draw 0 | jockey Toby Wynne | trainer Oliver Greenall & Josh Guerriero (14d 3/18) | headgear t | last run 31 days | form 53F-33 | MARKET 30.9% | 09:00 median 3.00 | Matchbook 3.10 | CHECK (skip line 2.85)
    comment: Masterfield has finished third in two of his last three outings and is yet to win in his last five, but he has run over today's trip and going before.
    DATA: model 14.2% | style Prominent (led 23% of runs) | runs in data 5 | last 3: 31 Mar Bangor-on-Dee Hurdle 16.7f Good F/7; 16 May Bangor-on-Dee Hurdle 16.7f Good 3/11; 27 Oct Bangor-on-Dee Chase 17.5f Good To Soft 3/9 fig 101
    DATA for: Last-run finishing speed +2.4% vs that field (finished strongly); Carries 9 lb less than average
    DATA against: Race comments mention jumping mistakes in 2 of its last 4 runs; Fell or unseated in 1 of its last 4 jumps runs
- Laristote (hrs_49757890) | 5yo G | 157lb | OR 98 | draw 0 | jockey Brian Hughes | trainer Donald McCain (14d 2/21) | headgear t | last run 31 days | form 3743-5 | MARKET 28.7% | 09:00 median 3.00 | Matchbook 3.50
    comment: Laristote has hit the frame twice in his last five, a third two starts back and another third five starts back, and he returns fresh after 31 days having run over today's trip and going.
    DATA: model 19.4% | style Prominent (led 3% of runs) | runs in data 4 | last 3: 10 Mar Sedgefield Hurdle 16.8f Good 4/7; 18 Apr Bangor-on-Dee Hurdle 16.7f Good 3/13; 27 Oct Bangor-on-Dee Chase 17.5f Good To Soft 5/9 fig 96
    DATA against: Best recent form figure 96, 6 lb below field average; Official rating 98, 5 lb below field average
- Magnolia (hrs_35243250) | 7yo M | 168lb | OR 109 | draw 0 | jockey Craig Nichol | trainer Micky Hammond & Becky Smith (14d 1/18) | headgear t | last run 43 days | form 2-3433 | MARKET 16.6% | 09:00 median 5.50 | Matchbook 5.80
    comment: Magnolia has been consistent, finishing third last time out, third two starts back, and second five starts back, and she has run over today's trip and going before.
    DATA: model 36.9% | style Prominent (led 5% of runs) | runs in data 7 | last 3: 23 May Cartmel Hurdle 17.2f Good 4/10; 23 Sep Perth Hurdle 16.2f Good 3/10; 15 Oct Perth Hurdle 16f Soft 3/9 fig 110
    DATA for: Best recent form figure 110, 8 lb above field average; Official rating 109, 6 lb above field average; Good recent finishing positions
    DATA against: Carries 7 lb more than average; First run over fences in our data
- Scriabin (hrs_37504313) | 6yo G | 166lb | OR 107 | draw 0 | jockey Patrick Wadge | trainer Lucinda Russell & Michael Scudamore (14d 1/19) | headgear t | last run 81 days | form -42185 | MARKET 14.2% | 09:00 median 6.50 | Matchbook 6.80
    comment: The risk is an 81-day absence after a fifth last time out and an eighth two starts back, with 166 lb to carry.
    DATA: model 17.6% | style Leader (led 57% of runs) | runs in data 7 | last 3: 2 Jul Perth Hurdle 16.2f Good 1/9; 15 Aug Perth Hurdle 16.2f Good 8/8; 7 Sep Perth Hurdle 16.2f Good 5/8
    DATA for: Has won at this trip or further; Pace: may get an uncontested lead
    DATA against: Carries 5 lb more than average; First run over fences in our data
- Ask A Sainte (hrs_50339835) | 6yo G | 161lb | OR 102 | draw 0 | jockey Sean Quinlan | trainer Lizzie Quinlan (14d 1/8) | headgear - | last run 21 days | form 2P4733 | MARKET 9.6% | 09:00 median 9.00 | Matchbook 10.50
    comment: Ask A Sainte arrives in fine fettle, third last time out and again two starts back, and he has run over today's trip after a fresh 21 days off. Yet to win in his last six, he must defy 161 lb, which is the main risk.
    DATA: model 11.9% | style Held up (led 5% of runs) | runs in data 9 | last 3: 4 Oct Uttoxeter Chase 16f Good 7/9; 13 Oct Southwell Chase 15.8f Good 3/4; 6 Nov Hexham Chase 15.5f Good 3/7 fig 101
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Pulled up in 1 of its last 5 jumps runs

## 2:32 Musselburgh | race_id rac_32305765804 | Edinburgh Rugby 1872 Cup Handicap Hurdle Race (Go North Sea Pigeon Hurdle Series Qualifier)
Hurdle | Class 4 | 1m7f124y | going Good To Soft | Turf | 6 runners | rating band 0-110 | age 3yo+
DATA pace: Lone leader - Nobotheratall is the only habitual front-runner and may be allowed an easy lead.
- Nobotheratall (hrs_51341444) | 6yo G | 160lb | OR 102 | draw 0 | jockey Harry Reed | trainer Tristan Davidson (14d 0/2) | headgear - | last run 18 days | form 479841 | MARKET 29.2% | 09:00 median 3.00 | Matchbook 3.30 | CHECK (skip line 2.85)
    comment: A weight of 160 lb and a patchy run before that are the only reservations.
    DATA: model 18.8% | style Leader (led 54% of runs) | runs in data 10 | last 3: 16 Oct Uttoxeter Hurdle 16f Good 8/10; 27 Oct Newcastle Hurdle 17f Good 4/10 fig 100; 9 Nov Carlisle Hurdle 17f Good To Soft 1/14 fig 102
    DATA for: Has won at this trip or further; Pace: may get an uncontested lead
    DATA against: Race comments mention jumping mistakes in 3 of its last 5 runs
- Bruce Banner (hrs_44015860) | 4yo G | 160lb | OR 102 | draw 0 | jockey Shane Fitzgerald | trainer Rebecca Menzies (14d 0/10) | headgear - | last run 18 days | form 1P-2 | MARKET 21.0% | 09:00 median 4.00 | Matchbook 4.80
    comment: Bruce Banner arrives in decent shape after a second last time out just 18 days ago, and he has run over today's trip and going before, while a win three starts back shows his upside. The risk is a pulled-up effort two starts back, plus 160 lb on his back.
    DATA: model 9.9% | style Prominent (led 23% of runs) | runs in data 12 | last 3: 3 Sep Newcastle Flat 12.4f Standard 4/9; 16 Oct Newcastle (AW) Flat 12.5f Standard 9/12 fig 44; 9 Nov Carlisle Hurdle 17f Good To Soft 2/14 fig 103
    DATA against: Trainer 0 wins from 10 runs, last 14 days; Pulled up in 1 of its last 2 jumps runs
- Gemini Man (hrs_22523781) | 8yo G | 156lb | OR 98 | draw 0 | jockey Brian Hughes | trainer Iain Jardine (14d 0/13) | headgear - | last run 23 days | form 9326-P | MARKET 18.2% | 09:00 median 5.00 | Matchbook 5.10
    comment: The risk is a pulled-up effort last time out, and he is yet to win in his last five starts, with 156 lb to carry.
    DATA: model 23.1% | style Midfield (led 3% of runs) | runs in data 15 | last 3: 25 Sep Newcastle Flat 10.2f Standard 2/14; 2 Oct Newcastle Flat 10.2f Standard 3/10; 4 Nov Musselburgh Flat 12.5f Soft 2/10 fig 56
    DATA for: Last-run finishing speed +4.7% vs that field (finished strongly); Good recent finishing positions; Carries 6 lb less than average
    DATA against: Official rating 98, 6 lb below field average; Trainer 0 wins from 13 runs, last 14 days; Pulled up in 1 of its last 2 jumps runs
- Scots Poet (hrs_24277260) | 10yo G | 159lb | OR 101 | draw 0 | jockey Craig Nichol | trainer Ewan Whillans (14d 0/5) | headgear tb | last run 34 days | form 1U2541 | MARKET 15.1% | 09:00 median 5.50 | Matchbook 6.80
    comment: Scots Poet won last time out and has two wins in his last six starts, with a fourth and a fifth in between, so the form is decent.
    DATA: model 19.0% | style Held up (led 3% of runs) | runs in data 12 | last 3: 28 Aug Sedgefield Hurdle 16.8f Good 5/6; 16 Sep Kelso Hurdle 18.1f Good To Firm 4/8; 24 Oct Kelso Hurdle 16f Good 1/6 fig 100
    DATA for: Last-run finishing speed +2.1% vs that field (finished strongly); Has won at this trip or further
    DATA against: Best recent form figure 100, 4 lb below field average; Fell or unseated in 1 of its last 5 jumps runs; Aged 10, older than most of this field
- Saint Polo (hrs_40553723) | 6yo G | 169lb | OR 111 | draw 0 | jockey Nathan Moscrop | trainer Susan Corbett (14d 1/10) | headgear tp | last run 41 days | form 111331 | MARKET 14.8% | 09:00 median 6.00 | Matchbook 6.60
    comment: Carrying 169 lb after 41 days off is the main risk.
    DATA: model 26.6% | style Prominent (led 38% of runs) | runs in data 10 | last 3: 7 Sep Newton Abbot Chase 16.3f Good 3/5; 28 Sep Newton Abbot Hurdle 16.8f Good 3/5; 17 Oct Market Rasen Hurdle 16.5f Good 1/6 fig 112
    DATA for: Best recent form figure 112, 8 lb above field average; Official rating 111, 7 lb above field average; Last-run finishing speed +5.2% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Carries 7 lb more than average
- Shooting (hrs_55210701) | 4yo G | 168lb | OR 110 | draw 0 | jockey Bruce Lynn | trainer N. W. Alexander (14d 0/5) | headgear t | last run 43 days | form 9/3P-P | MARKET 1.8% | 09:00 median 51.00 | Matchbook 60.00
    comment: Shooting has pulled up in his last two outings, though he was third three starts back, and he returns after 43 days off carrying 168 lb off an official mark of 110. Yet to win in his last four starts and lightly exposed, he may have more to offer.
    DATA: model 2.5% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 15 Oct Perth Hurdle 16f Soft PU/9
    DATA for: Official rating 110, 6 lb above field average
    DATA against: Carries 6 lb more than average; Lightly raced: 1 run in our data, so the model has little to go on; Pulled up in 1 of its last 1 jumps runs

## 3:07 Musselburgh | race_id rac_32305767741 | Racing TV Conditional Jockeys' Handicap Hurdle Race
Hurdle | Class 5 | 2m3f171y | going Good To Soft | Turf | 8 runners | rating band 0-105 | age 4yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Lillistar (hrs_33302500) | 6yo M | 146lb | OR 82 | draw 0 | jockey Joshua Thompson(3) | trainer Micky Hammond & Becky Smith (14d 1/18) | headgear - | last run 28 days | form P5-331 | MARKET 17.8% | 09:00 median 5.00 | Matchbook 5.30 | CHECK (skip line 4.75)
    comment: She has run over today's trip and going and returns after 28 days.
    DATA: model 23.9% | style Midfield (led 5% of runs) | runs in data 11 | last 3: 28 Aug Sedgefield Hurdle 19.9f Good 3/9; 29 Sep Sedgefield Hurdle 19.9f Good 3/8; 30 Oct Wetherby Hurdle 21.5f Good 1/11 fig 78
    DATA for: Last-run finishing speed +4.5% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions; Carries 6 lb less than average
    DATA against: Best recent form figure 78, 12 lb below field average; Official rating 82, 6 lb below field average; Pulled up in 1 of its last 5 jumps runs
- Lone Star (hrs_28592487) | 9yo M | 149lb | OR 85 | draw 0 | jockey Oscar Palmer(3) | trainer Philip Kirby (14d 1/13) | headgear tp | last run 20 days | form 374647 | MARKET 17.5% | 09:00 median 4.50 | Matchbook 5.70
    comment: The risk is a winless recent run, including a seventh last time out, with 149 lb to carry.
    DATA: model 13.4% | style Prominent (led 3% of runs) | runs in data 10 | last 3: 14 Sep Sedgefield Hurdle 19.9f Good 6/10; 4 Oct Kelso Hurdle 20.9f Good To Firm 4/8; 7 Nov Kelso Hurdle 21f Good 7/11 fig 82
    DATA against: Best recent form figure 82, 8 lb below field average; Aged 9, older than most of this field
- Beat The Retreat (hrs_32751159) | 7yo G | 151lb | OR 87 | draw 0 | jockey Dominic Hislop(8) | trainer N. W. Alexander (14d 0/5) | headgear tv | last run 16 days | form 14-P34 | MARKET 16.7% | 09:00 median 5.00 | Matchbook 5.80
    comment: Fourth last time out and a third two starts back show he's running respectably, and he's fresh enough after 16 days, having run over today's trip and going before. Yet he's won just once in his last five, was pulled up three starts back, and carries 151 lb off 87.
    DATA: model 9.5% | style Prominent (led 3% of runs) | runs in data 5 | last 3: 13 May Perth Hurdle 20.2f Good To Soft PU/8; 24 Sep Perth Hurdle 20.2f Good 3/12; 11 Nov Ayr Hurdle 19.5f Good 4/10 fig 90
    DATA for: Last-run finishing speed +2.0% vs that field (finished strongly); Has won at this trip or further
    DATA against: Pulled up in 1 of its last 5 jumps runs
- Presentandcorrect (hrs_58469222) | 6yo G | 168lb | OR 104 | draw 0 | jockey Charlie Maggs | trainer Rebecca Menzies (14d 0/10) | headgear t | last run 22 days | form 8-3223 | MARKET 14.7% | 09:00 median 6.00 | Matchbook 6.40
    comment: Presentandcorrect has finished in the frame in four of his last five, third last time out, with a second two starts back and another second three starts back, and he has run over today's trip.
    DATA: model 14.0% | style Midfield (led 4% of runs) | runs in data 6 | last 3: 4 Jun Uttoxeter Hurdle 23.3f Good 2/6; 10 Oct Hexham Hurdle 20.1f Good 2/3; 5 Nov Newcastle Hurdle 20.5f Good 3/8 fig 103
    DATA for: Best recent form figure 103, 13 lb above field average; Official rating 104, 16 lb above field average; Good recent finishing positions
    DATA against: Trainer 0 wins from 10 runs, last 14 days; Carries 16 lb more than average; Race comments mention jumping mistakes in 2 of its last 4 runs
- Walk On Son (hrs_45982223) | 6yo G | 151lb | OR 87 | draw 0 | jockey Jack Power | trainer Lucinda Russell & Michael Scudamore (14d 1/19) | headgear t | last run 38 days | form 8-4PU4 | MARKET 14.6% | 09:00 median 6.00 | Matchbook 6.60
    DATA: model 8.8% | style Midfield (led 4% of runs) | runs in data 7 | last 3: 24 May Kelso Hurdle 16.2f Good PU/8; 23 Sep Perth Chase 20.1f Good UR/9; 20 Oct Hexham Hurdle 16f Good 4/10 fig 88
    DATA against: Race comments mention jumping mistakes in 2 of its last 5 runs; Fell or unseated in 1 of its last 5 jumps runs; Pulled up in 1 of its last 5 jumps runs
- Evenwood Sonofagun (hrs_21326921) | 8yo G | 163lb | OR 99 | draw 0 | jockey Alice Stevens | trainer Lizzie Quinlan (14d 1/8) | headgear tp | last run 20 days | form 126784 | MARKET 10.4% | 09:00 median 8.50 | Matchbook 9.00
    comment: The risk is a slide of a seventh and eighth in his previous two outings, plus the 163 lb burden.
    DATA: model 11.8% | style Held up (led 3% of runs) | runs in data 8 | last 3: 18 Jul Cartmel Hurdle 22.1f Good 7/13; 24 Oct Kelso Hurdle 22.5f Good 8/9 fig 92; 7 Nov Kelso Hurdle 21f Good 4/11 fig 99
    DATA for: Best recent form figure 99, 9 lb above field average; Official rating 99, 11 lb above field average; Has won at this trip or further
    DATA against: Carries 11 lb more than average; Pace: steady gallop likely, hard to come from off the pace
- National Question (hrs_29509676) | 6yo G | 149lb | OR 85 | draw 0 | jockey Oakley Brown | trainer Adam Nicol (14d 0/3) | headgear p | last run 31 days | form 516-58 | MARKET 6.7% | 09:00 median 13.00 | Matchbook 14.50
    comment: National Question has won once in his last five, a victory four starts back, but a sixth, a fifth and an eighth since show he's drifted, and he returns after 31 days.
    DATA: model 12.6% | style Held up (led 3% of runs) | runs in data 6 | last 3: 11 Apr Newcastle Hurdle 20.3f Good 6/12; 13 Jun Hexham Hurdle 16.2f Good 5/10; 27 Oct Newcastle Hurdle 17f Good 8/10
    DATA for: Has won at this trip or further
    DATA against: Last-run finishing speed -4.3% vs that field (faded); Pace: steady gallop likely, hard to come from off the pace
- On The Bubble (hrs_36235164) | 5yo M | 142lb | OR 74 | draw 0 | jockey Conor Rabbitt | trainer Gary Rutherford (14d 0/1) | headgear - | last run 20 days | form 8F/5P0 | MARKET 1.7% | 09:00 median 41.00 | Matchbook 80.00
    comment: Winless in her last five, On The Bubble was unplaced last time, pulled up two starts back and fell four starts back, so it is hard to fancy her at 142 lb off an official mark of 74.
    DATA: model 6.1% | style Held up (led 3% of runs) | runs in data 13 | last 3: 16 Sep Kelso Hurdle 18.1f Good To Firm 5/8; 24 Sep Perth Hurdle 20.2f Good PU/12; 7 Nov Kelso Hurdle 21f Good 11/11
    DATA for: Carries 10 lb less than average
    DATA against: Official rating 74, 14 lb below field average; Pulled up in 1 of its last 3 jumps runs; Pace: steady gallop likely, hard to come from off the pace
