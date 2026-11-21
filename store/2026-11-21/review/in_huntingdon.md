# Card review packet: Huntingdon, 2026-11-21

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
{"meeting": "huntingdon", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 12:13 Huntingdon | race_id rac_32305082043 | Podkovan Won By A Czech Head Maiden Hurdle Race (GBB Race)
Hurdle | Class 4 | 1m7f171y | going Good | Turf | 13 runners | rating band - | age 3yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Lastbutnotleased (hrs_17395087983) | 5yo G | 160lb | OR - | draw 0 | jockey Paul O'Brien | trainer Nicky Henderson (14d 2/14) | headgear - | last run 209 days | form 4F1- | MARKET 51.1% | 09:00 median 1.57 | Matchbook 1.75
    DATA: model 5.8% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 209-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Dream On Max (hrs_17395794094) | 4yo G | 160lb | OR - | draw 0 | jockey Stan Sheppard | trainer Henry Daly (14d 2/14) | headgear h (1st time) | last run 201 days | form 2 | MARKET 10.6% | 09:00 median 7.50 | Matchbook 8.80
    DATA: model 5.8% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: First-time headgear
    DATA against: Returns from a 201-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Kaldoun des Rocs (hrs_50556499) | 4yo G | 160lb | OR 117 | draw 0 | jockey Charlie Todd | trainer Dan Skelton (14d 17/80) | headgear ht | wind surgery | last run 27 days | form 2/33-5 | MARKET 10.1% | 09:00 median 7.75 | Matchbook 9.60
    DATA: model 21.5% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 25 Oct Market Rasen Hurdle 16.5f Good To Soft 5/11
    DATA for: Trainer 21% wins (17/80), last 14 days
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Westbrooke Boy (hrs_58931159) | 4yo G | 160lb | OR - | draw 0 | jockey Charlie Hammond | trainer Stuart Edmunds (14d 1/8) | headgear - | last run 19 days | form 172-67 | MARKET 8.6% | 09:00 median 8.50 | Matchbook 12.00
    DATA: model 9.6% | style Midfield (led 4% of runs) | runs in data 4 | last 3: 4 Apr Huntingdon NH Flat 15.8f Good 2/8; 7 Oct Worcester Hurdle 16f Good 6/12; 2 Nov Southwell Hurdle 16f Good 7/14
- Master Roque (hrs_56559475) | 4yo G | 160lb | OR - | draw 0 | jockey Tom Bellamy | trainer Alan King (14d 2/18) | headgear - | last run 193 days | form 0-2 | MARKET 8.1% | 09:00 median 9.50 | Matchbook 12.50
    DATA: model 10.3% | style Midfield (led 8% of runs) | runs in data 2 | last 3: 21 Mar Newbury NH Flat 16.3f Good To Soft 13/20; 12 May Hereford NH Flat 16.2f Good To Firm 2/4
    DATA for: Last-run finishing speed +3.9% vs that field (finished strongly)
    DATA against: Returns from a 193-day break; Lightly raced: 2 runs in our data, so the model has little to go on; First run over hurdles in our data
- Kasgani (hrs_44540734) | 4yo G | 160lb | OR - | draw 0 | jockey Oakley Brown(5) | trainer Declan Carroll (14d 0/5) | headgear - | last run 25 days | form - | MARKET 4.2% | 09:00 median 17.00 | Matchbook 26.00
    DATA: model 10.8% | style Held up (led 3% of runs) | runs in data 4 | last 3: 3 Jun Nottingham Flat 10.2f Good 6/10; 7 Oct Nottingham Flat 10.2f Good To Soft 7/13; 27 Oct Catterick Flat 12f Soft 2/10 fig 68
    DATA against: First run over hurdles in our data; Pace: steady gallop likely, hard to come from off the pace
- Meritocratic (hrs_57103459) | 3yo G | 144lb | OR - | draw 0 | jockey Callum Pritchard | trainer James Owen (14d 3/30) | headgear - | last run 26 days | form P | MARKET 2.5% | 09:00 median 29.00 | Matchbook 46.00
    DATA: model 9.1% | style Held up (led 8% of runs) | runs in data 8 | last 3: 21 Sep Wolverhampton Flat 8.6f Standard 6/10; 13 Oct Wolverhampton Flat 8.6f Standard 3/10; 26 Oct Hereford Hurdle 16f Good To Firm PU/9
    DATA against: Pulled up in 1 of its last 1 jumps runs; Pace: steady gallop likely, hard to come from off the pace
- Mick The Yank (hrs_17393248131) | 4yo G | 160lb | OR - | draw 0 | jockey Lorcan Williams | trainer Stuart Edmunds (14d 1/8) | headgear - | last run 18 days | form 59 | MARKET 1.1% | 09:00 median 51.00 | Matchbook 150.00
    DATA: model 6.5% | style Prominent (led 8% of runs) | runs in data 2 | last 3: 7 Oct Worcester NH Flat 16f Good 5/10; 3 Nov Lingfield Hurdle 16f Good 9/11 fig 88
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Nymphaea (hrs_46384135) | 4yo F | 153lb | OR - | draw 0 | jockey I. J. Power | trainer Jennie Candlish (14d 3/20) | headgear p | last run 28 days | form - | MARKET 1.0% | 09:00 median 67.00 | Matchbook 200.00
    DATA: model 5.8% | style Midfield (led 3% of runs) | runs in data 15 | last 3: 28 Jul Yarmouth Flat 11.5f Good To Firm 4/6; 13 Oct Wolverhampton Flat 12.2f Standard 4/11; 24 Oct Southwell (AW) Flat 12f Standard 11/14
    DATA against: First run over hurdles in our data
- Assured (hrs_41090861) | 5yo M | 153lb | OR - | draw 0 | jockey Lee Edwards | trainer Tom Gretton (14d 0/4) | headgear h | last run 11 days | form 6 | MARKET 0.7% | 09:00 median 101.00 | Matchbook 150.00
    DATA: model 2.2% | style Held up (led 4% of runs) | runs in data 7 | last 3: 1 Oct Nottingham Flat 17.9f Good 9/10; 19 Oct Bath Flat 17f Good To Soft 8/11 fig 31; 10 Nov Huntingdon Hurdle 16f Good 6/7 fig 84
    DATA against: Poor recent finishing positions; Pace: steady gallop likely, hard to come from off the pace
- Military Saint (hrs_52055521) | 6yo G | 160lb | OR - | draw 0 | jockey Adam Wedge | trainer David Dennis (14d 0/1) | headgear - | last run 122 days | form 4P1-P6 | MARKET 0.7% | 09:00 median 96.00 | Matchbook 260.00
    DATA: model 3.1% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 5 Jul Market Rasen Hurdle 20.6f Good PU/7; 22 Jul Worcester Hurdle 16f Good 6/9
    DATA against: Returns from a 122-day break; Lightly raced: 2 runs in our data, so the model has little to go on; Pulled up in 1 of its last 2 jumps runs
- From The Shadows (hrs_17395795137) | 5yo G | 160lb | OR - | draw 0 | jockey David Noonan | trainer Jonathan Barlow (14d 0/1) | headgear - | last run 251 days | form 4PP- | MARKET 0.6% | 09:00 median 101.00 | Matchbook 290.00
    DATA: model 5.8% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 251-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Karios (hrs_56494739) | 3yo G | 144lb | OR - | draw 0 | jockey Jack Quinlan | trainer Matt Crawley (14d 0/2) | headgear h (1st time) | last run 18 days | form 6 | MARKET 0.6% | 09:00 median 126.00 | Matchbook 260.00
    DATA: model 3.6% | style Unknown | runs in data 2 | last 3: 28 Apr Yarmouth Flat 10.1f Good 1/10; 3 Nov Warwick Hurdle 16f Good 6/7
    DATA for: First-time headgear
    DATA against: Last-run finishing speed -2.6% vs that field (faded); Lightly raced: 2 runs in our data, so the model has little to go on

## 12:48 Huntingdon | race_id rac_32305083980 | Podkovan Dancing Through The Dark Handicap Hurdle Race
Hurdle | Class 5 | 3m1f10y | going Good | Turf | 11 runners | rating band 0-100 | age 4yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- U S Marshall (hrs_47345312) | 6yo G | 167lb | OR 97 | draw 0 | jockey Jack Tudor | trainer Oliver Greenall & Josh Guerriero (14d 2/8) | headgear p | last run 30 days | form 9552-6 | MARKET 23.4% | 09:00 median 3.50 | Matchbook 4.00 | CHECK (skip line 3.32)
    comment: The main risk is his 167 lb burden, a hefty load off an official mark of 97.
    DATA: model 17.2% | style Prominent (led 3% of runs) | runs in data 4 | last 3: 14 Mar Newcastle Hurdle 20.3f Good To Soft 5/15; 4 Apr Huntingdon Hurdle 20.7f Good 2/7; 22 Oct Carlisle Hurdle 20f Good 6/13 fig 94
    DATA for: Best recent form figure 94, 8 lb above field average; Official rating 97, 9 lb above field average; Trainer 25% wins (2/8), last 14 days
    DATA against: Carries 9 lb more than average
- Charlie My Boy (hrs_27371862) | 9yo G | 161lb | OR 91 | draw 0 | jockey Jack Quinlan | trainer J. R. Jenkins (14d 0/2) | headgear t | last run 20 days | form -26831 | MARKET 16.1% | 09:00 median 5.00 | Matchbook 6.00
    comment: Fresh from a win last time out, and a third two starts back, Charlie My Boy returns after 20 days having run over today's trip and going before.
    DATA: model 12.6% | style Midfield (led 4% of runs) | runs in data 5 | last 3: 28 Aug Fontwell Hurdle 17.7f Good 8/9; 6 Oct Huntingdon Hurdle 19.6f Good 3/7; 1 Nov Huntingdon Hurdle 25f Good 1/8 fig 87
    DATA for: Last-run finishing speed +2.7% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
- That Is Blue (hrs_60884852) | 5yo M | 167lb | OR 97 | draw 0 | jockey Charlie Bell(10) | trainer Henrietta C Knight (14d 0/7) | headgear - | last run 37 days | form 333-2 | MARKET 15.7% | 09:00 median 5.50 | Matchbook 5.90
    comment: That Is Blue arrives in cracking heart, finishing second last time out and third in each of the three starts before, and she has run on today's going before. The main risk is that she's yet to win in that run and carries 167 lb after 37 days off.
    DATA: model 10.5% | style Midfield (led 3% of runs) | runs in data 4 | last 3: 5 Apr Plumpton Hurdle 20.5f Good 3/5; 24 Apr Fontwell Hurdle 21.7f Good 3/7; 15 Oct Fontwell Hurdle 21.5f Good To Soft 2/6 fig 96
    DATA for: Best recent form figure 96, 10 lb above field average; Official rating 97, 9 lb above field average; Last-run finishing speed +3.2% vs that field (finished strongly); Good recent finishing positions
    DATA against: Carries 9 lb more than average; Race comments mention jumping mistakes in 2 of its last 3 runs
- Carrigmoorna Rowan (hrs_28824621) | 9yo G | 168lb | OR 98 | draw 0 | jockey Ned Fox(3) | trainer Samuel Drinkwater (14d 1/6) | headgear - | last run 31 days | form 552-24 | MARKET 12.6% | 09:00 median 6.50 | Matchbook 7.80
    comment: Carrigmoorna Rowan is consistent, with a fourth last time out, a second two starts back and another second three starts back, and he has run over today's trip and on this going before.
    DATA: model 17.0% | style Prominent (led 5% of runs) | runs in data 7 | last 3: 24 Apr Fontwell Chase 26f Good 2/5; 6 Oct Huntingdon Chase 23.6f Good 2/5; 21 Oct Fontwell Chase 26f Soft 4/8
    DATA for: Official rating 98, 10 lb above field average; Good recent finishing positions
    DATA against: Last-run finishing speed -8.2% vs that field (faded); Carries 10 lb more than average
- Alan Bresil (hrs_50622481) | 6yo G | 164lb | OR 94 | draw 0 | jockey Nathan Andrews(10) | trainer Nick Scholfield (14d 1/14) | headgear b | last run 9 days | form 54633U | MARKET 8.7% | 09:00 median 9.00 | Matchbook 12.00
    comment: Alan Bresil unseated last time but was third in each of the two runs before that, and he's back quickly after nine days, having run over today's trip and going before. He's yet to win in recent form, though, and 164 lb is a stiff burden off 94.
    DATA: model 11.9% | style Midfield (led 3% of runs) | runs in data 12 | last 3: 26 Oct Hereford Hurdle 25.5f Good To Firm 3/8 fig 90; 1 Nov Huntingdon Hurdle 25f Good 3/8 fig 92; 12 Nov Hereford Hurdle 25.5f Good To Firm UR/5
    DATA for: Best recent form figure 92, 6 lb above field average; Official rating 94, 6 lb above field average
    DATA against: Carries 6 lb more than average; Race comments mention jumping mistakes in 2 of its last 5 runs; Fell or unseated in 1 of its last 5 jumps runs
- Daaris (hrs_30314704) | 7yo G | 162lb | OR 92 | draw 0 | jockey David Noonan | trainer Kevin & Lauren Frost (14d 1/4) | headgear b | last run 35 days | form 4/8362 | MARKET 5.5% | 09:00 median 15.00 | Matchbook 17.50
    comment: Daaris is yet to win in his last five starts, but a second last time out and a third three starts back show he's competitive, and he has run over today's trip and going before.
    DATA: model 10.0% | style Held up (led 3% of runs) | runs in data 8 | last 3: 10 Sep Worcester Hurdle 23f Good 3/11; 1 Oct Southwell Hurdle 24.3f Good 6/8; 17 Oct Market Rasen Hurdle 23f Good 2/8 fig 90
    DATA for: Last-run finishing speed +4.5% vs that field (finished strongly); Good recent finishing positions
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Ifyouhaveaplan (hrs_63357049) | 5yo G | 151lb | OR 81 | draw 0 | jockey Tom Cannon | trainer Louise Allan (14d 0/1) | headgear - | last run 51 days | form 256875 | MARKET 4.3% | 09:00 median 19.00 | Matchbook 24.00
    comment: The risk is a winless run in his last six, with five finishes of fifth or worse and a 51-day break.
    DATA: model 1.5% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 15 Aug Market Rasen Hurdle 20.6f Good 8/10; 15 Sep Uttoxeter Hurdle 19.9f Good 7/9; 1 Oct Southwell Hurdle 20.4f Good 5/5
    DATA for: Carries 7 lb less than average
    DATA against: Official rating 81, 7 lb below field average; Last-run finishing speed -9.1% vs that field (faded)
- Moro Rock (hrs_33975718) | 9yo G | 148lb | OR 78 | draw 0 | jockey James Best | trainer Sara Ender (14d 0/0) | headgear - | last run 35 days | form 573-57 | MARKET 4.1% | 09:00 median 21.00 | Matchbook 24.00
    comment: Moro Rock is yet to win in his last five, with a seventh last time out, though a third three starts back shows he can go close, and he has run over today's trip and going.
    DATA: model 6.1% | style Prominent (led 5% of runs) | runs in data 3 | last 3: 10 Apr Sedgefield Hurdle 27f Good 3/5; 19 Jun Market Rasen Hurdle 23.1f Good 5/10; 17 Oct Market Rasen Hurdle 23f Good 7/8
    DATA for: Carries 10 lb less than average
    DATA against: Official rating 78, 10 lb below field average; Last-run finishing speed -7.3% vs that field (faded)
- Footage Detectives (hrs_57504349) | 5yo M | 150lb | OR 80 | draw 0 | jockey Adam Wedge | trainer Henry Oliver (14d 0/5) | headgear - | last run 19 days | form 787-45 | MARKET 3.9% | 09:00 median 21.00 | Matchbook 26.00
    comment: Footage Detectives is winless in her last five, with a fifth last time out, a fourth two starts back and a run of seventh, eighth and seventh before that, so she's hard to fancy. Carrying 150 lb off 80 doesn't help, though she has run on today's going and is only 19 days since her last outing.
    DATA: model 4.5% | style Midfield (led 4% of runs) | runs in data 5 | last 3: 24 Apr Chepstow Hurdle 16.1f Good 7/12; 8 Oct Market Rasen Hurdle 20.6f Good 4/5; 2 Nov Southwell Hurdle 20.5f Good 5/11 fig 71
    DATA for: Carries 8 lb less than average
    DATA against: Best recent form figure 71, 15 lb below field average; Recent figures 9 lb below its current mark (looks high in the weights); Official rating 80, 8 lb below field average; Last-run finishing speed -2.4% vs that field (faded)
- Richardson (hrs_18181709) | 11yo G | 149lb | OR 79 | draw 0 | jockey Lee Edwards | trainer Belinda Clarke (14d 0/0) | headgear - | last run 240 days | form /55P2- | MARKET 3.6% | 09:00 median 23.00 | Matchbook 30.00
    comment: Richardson was second last time out but pulled up two starts back and is yet to win in his last four, while a 240-day absence raises fitness doubts.
    DATA: model 6.0% | style Held up (led 5% of runs) | runs in data 3 | last 3: 24 Jan Uttoxeter Hurdle 19.9f Soft 5/7; 13 Feb Chepstow Hurdle 19.5f Soft PU/11; 26 Mar Chepstow Hurdle 23.6f Good To Soft 2/15
    DATA for: Last-run finishing speed +2.9% vs that field (finished strongly); Carries 9 lb less than average
    DATA against: Official rating 79, 9 lb below field average; Returns from a 240-day break; Pulled up in 1 of its last 3 jumps runs; Aged 11, older than most of this field; Pace: steady gallop likely, hard to come from off the pace
- Credit Union (hrs_59491803) | 5yo G | 149lb | OR 79 | draw 0 | jockey Paul O'Brien | trainer Jessica Bedi (14d 0/6) | headgear h | last run 18 days | form 0-0665 | MARKET 2.0% | 09:00 median 41.00 | Matchbook 48.00
    comment: Credit Union is winless in his last five, finishing a fifth last time out and a sixth two starts back, so he is hard to fancy.
    DATA: model 2.8% | style Held up (led 4% of runs) | runs in data 6 | last 3: 28 Aug Sedgefield Hurdle 19.9f Good 6/8; 2 Oct Hexham Hurdle 16.2f Good 6/6; 3 Nov Sedgefield Hurdle 20f Good 5/11 fig 73
    DATA for: Carries 9 lb less than average
    DATA against: Best recent form figure 73, 13 lb below field average; Recent figures 6 lb below its current mark (looks high in the weights); Official rating 79, 9 lb below field average; Pace: steady gallop likely, hard to come from off the pace

## 1:23 Huntingdon | race_id rac_32305085917 | Moment For The Monastery Mares' Handicap Steeple Chase (Challenger Mares' Chase Qualifer) (GBB Race)
Chase | Class 4 | 2m7f129y | going Good | Turf | 7 runners | rating band 0-120 | age 4yo+
DATA pace: Lone leader - Kilworth is the only habitual front-runner and may be allowed an easy lead.
- Realta Liath (hrs_35335769) | 7yo M | 160lb | OR 111 | draw 0 | jockey Tom Cannon | trainer Warren Greatrex (14d 5/17) | headgear - | wind surgery | last run 212 days | form 13422- | MARKET 21.9% | 09:00 median 4.00 | Matchbook 4.40 | CHECK (skip line 3.80)
    comment: Realta Liath arrives with back-to-back seconds, a third and a fourth before that, and a win five starts back, and she has run over today's trip and going before.
    DATA: model 19.4% | style Held up (led 8% of runs) | runs in data 3 | last 3: 16 Jan Market Rasen Chase 23.9f Soft 4/8; 9 Mar Stratford Chase 22.6f Soft 2/6; 23 Apr Warwick Chase 25.5f Good 2/6
    DATA for: Trainer 29% wins (5/17), last 14 days; Good recent finishing positions
    DATA against: Returns from a 212-day break
- Crazierthandaisy (hrs_39208673) | 7yo M | 164lb | OR 115 | draw 0 | jockey Paul O'Brien | trainer Nicky Henderson (14d 2/14) | headgear - | last run 212 days | form P402P- | MARKET 21.1% | 09:00 median 4.00 | Matchbook 4.60
    comment: The risk is a 212-day absence after being pulled up last time, with 164 lb to carry.
    DATA: model 19.2% | style Held up (led 3% of runs) | runs in data 4 | last 3: 14 Feb Ascot Hurdle 23.6f Good To Soft 14/18; 28 Mar Uttoxeter Hurdle 19.9f Good To Soft 2/7; 23 Apr Warwick Hurdle 21f Good PU/10
    DATA against: Returns from a 212-day break; Pulled up in 1 of its last 4 jumps runs; First run over fences in our data
- Kilworth (hrs_49578186) | 6yo M | 157lb | OR 108 | draw 0 | jockey Liam Harrison | trainer Emma Lavelle (14d 3/17) | headgear - | last run 35 days | form 1P13-4 | MARKET 16.7% | 09:00 median 5.50 | Matchbook 5.50
    comment: Kilworth bears a strong profile, a winner three starts back, then a third and a fourth last time out, with two wins in her last five and experience of today's trip and going.
    DATA: model 14.2% | style Leader (led 29% of runs) | runs in data 5 | last 3: 29 Mar Ascot Hurdle 23.6f Good 1/8; 24 Apr Chepstow Hurdle 23.6f Good 3/4; 17 Oct Stratford Chase 22.5f Good 4/4 fig 101
    DATA for: Has won at this trip or further; Good recent finishing positions; Pace: may get an uncontested lead
    DATA against: Recent figures 7 lb below its current mark (looks high in the weights); Pulled up in 1 of its last 5 jumps runs
- Livingonaprayer (hrs_50187872) | 5yo M | 168lb | OR 119 | draw 0 | jockey Isabelle Ryder(5) | trainer Jamie Snowden (14d 5/20) | headgear - | last run 220 days | form /11P8- | MARKET 13.3% | 09:00 median 6.50 | Matchbook 7.20
    comment: Hard to fancy after 220 days off, with an eighth last time out and a pulled up before that, and she carries 168 lb off 119. On the plus side, she won three and four starts back and has run on today's going before.
    DATA: model 7.4% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 28 Feb Doncaster Hurdle 24.4f Soft PU/8; 15 Apr Haydock Hurdle 21.2f Good 8/8
    DATA for: Official rating 119, 7 lb above field average; Trainer 25% wins (5/20), last 14 days
    DATA against: Last-run finishing speed -11.4% vs that field (faded); Carries 7 lb more than average; Returns from a 220-day break; Lightly raced: 2 runs in our data, so the model has little to go on; Pulled up in 1 of its last 2 jumps runs; First run over fences in our data
- Edith Pelham (hrs_49578263) | 6yo M | 160lb | OR 111 | draw 0 | jockey Jack Quinlan | trainer Fergal O'Brien (14d 3/31) | headgear - | last run 25 days | form 3618-9 | MARKET 10.8% | 09:00 median 8.50 | Matchbook 8.60
    comment: She did win three starts back and has had 25 days to recover, but 160 lb is a hefty burden.
    DATA: model 10.8% | style Prominent (led 23% of runs) | runs in data 5 | last 3: 2 Mar Southwell Hurdle 20.4f Soft 1/6; 21 Mar Newbury Hurdle 20.5f Good To Soft 8/15; 27 Oct Bangor-on-Dee Hurdle 19.5f Good 9/10
    DATA against: Last-run finishing speed -6.6% vs that field (faded); First run over fences in our data
- Regal Renaissance (hrs_30138220) | 8yo M | 168lb | OR 119 | draw 0 | jockey Tom Bellamy | trainer Jack Jones (14d 0/3) | headgear - | last run 57 days | form 11132P | MARKET 10.1% | 09:00 median 8.50 | Matchbook 9.80
    comment: Regal Renaissance won three of her last six, including a winning run from six to four starts back, then added a second and a third before being pulled up last time out.
    DATA: model 19.3% | style Prominent (led 3% of runs) | runs in data 8 | last 3: 22 Jul Worcester Chase 23f Good 3/9; 7 Sep Perth Chase 23.8f Good 2/4; 25 Sep Worcester Chase 20f Good PU/12
    DATA for: Official rating 119, 7 lb above field average; Has won at this trip or further
    DATA against: Carries 7 lb more than average; Pulled up in 1 of its last 5 jumps runs
- Hill In Brazil (hrs_49174237) | 6yo M | 149lb | OR 100 | draw 0 | jockey Luke Scott(3) | trainer Dr Richard Newland (14d 0/0) | headgear - | last run 428 days | form 60/13- | MARKET 6.1% | 09:00 median 13.00 | Matchbook 17.00
    comment: Hill In Brazil arrives with a third last time out and a winner two starts back, and she has run on today's going, but a 428-day absence is a big question mark.
    DATA: model 9.7% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Carries 12 lb less than average
    DATA against: Official rating 100, 12 lb below field average; Returns from a 428-day break; Lightly raced: 0 runs in our data, so the model has little to go on

## 1:58 Huntingdon | race_id rac_32305087854 | Prancing To The Pilsner Handicap Hurdle Race
Hurdle | Class 4 | 1m7f171y | going Good | Turf | 11 runners | rating band 0-120 | age 3yo+
DATA pace: Even - Two likely leaders (Virtual Rock, Takeit Easy). A fair, even gallop is most likely.
- North of Richmond (hrs_41190429) | 6yo G | 166lb | OR 116 | draw 0 | jockey Adam Wedge | trainer Alex Hales (14d 0/4) | headgear - | last run 25 days | form 134P-1 | MARKET 24.5% | 09:00 median 3.50 | Matchbook 3.75 | CHECK (skip line 3.32)
    comment: North of Richmond arrives fresh from a last-time-out win, and that's one of two wins in his last five starts, with a run 25 days ago keeping him fit; he has run over today's trip and going. The main risk is the 166 lb he carries, off an official mark of 116.
    DATA: model 12.4% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 14 Jan Newbury Hurdle 16.3f Good To Soft 4/11; 27 Feb Doncaster Hurdle 16.6f Good To Soft PU/8; 27 Oct Newcastle Hurdle 17f Good 1/6 fig 118
    DATA for: Best recent form figure 118, 10 lb above field average; Last-run finishing speed +4.3% vs that field (finished strongly); Has won at this trip or further
    DATA against: Pulled up in 1 of its last 3 jumps runs
- Bankatary (hrs_57471050) | 4yo G | 162lb | OR 112 | draw 0 | jockey Tom Bellamy | trainer James Owen (14d 3/30) | headgear h | last run 20 days | form 13-41 | MARKET 14.2% | 09:00 median 6.00 | Matchbook 6.60
    comment: Bankatary arrives fresh from a win last time out, with a fourth two starts back, a third three starts back and another win four starts back, and he has run over today's trip and going.
    DATA: model 9.7% | style Prominent (led 4% of runs) | runs in data 6 | last 3: 12 Sep Lingfield Flat 12f Standard 7/9; 19 Oct Plumpton Hurdle 16f Good 4/5 fig 106; 1 Nov Huntingdon Hurdle 16f Good 1/10 fig 106
    DATA for: Last-run finishing speed +3.7% vs that field (finished strongly); Has won at this trip or further
    DATA against: Recent figures 6 lb below its current mark (looks high in the weights); Race comments mention jumping mistakes in 2 of its last 2 runs
- Virtual Rock (hrs_27343379) | 7yo G | 168lb | OR 118 | draw 0 | jockey Jack Tudor | trainer Des Donovan (14d 0/1) | headgear t | last run 11 days | form /8112V | MARKET 14.0% | 09:00 median 6.00 | Matchbook 6.60
    DATA: model 17.2% | style Leader (led 38% of runs) | runs in data 5 | last 3: 15 Sep Uttoxeter Hurdle 19.9f Good 1/12; 22 Sep Fontwell Hurdle 17.7f Good 1/5; 14 Oct Wetherby Hurdle 19.5f Good To Firm 2/5 fig 113
    DATA for: Best recent form figure 113, 5 lb above field average; Official rating 118, 7 lb above field average; Last-run finishing speed +5.1% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Carries 7 lb more than average
- Bluegrass (hrs_25939179) | 7yo G | 166lb | OR 116 | draw 0 | jockey Charlie Hammond | trainer Stuart Edmunds (14d 1/8) | headgear tb | last run 16 days | form 48-720 | MARKET 10.8% | 09:00 median 8.00 | Matchbook 8.60
    comment: Bluegrass ran a second two starts back and is fit after just 16 days off, with experience over today's trip and going, and he is yet to win in his last five.
    DATA: model 8.4% | style Midfield (led 3% of runs) | runs in data 7 | last 3: 2 May Uttoxeter Hurdle 19.9f Good 7/8; 1 Oct Southwell Hurdle 15.8f Good 2/8; 5 Nov Newbury Hurdle 16.5f Good To Soft 12/16 fig 105
    DATA against: Recent figures 11 lb below its current mark (looks high in the weights)
- Caelan (hrs_36696331) | 5yo G | 156lb | OR 106 | draw 0 | jockey Tom Cannon | trainer Sarah Humphrey (14d 0/2) | headgear t | last run 24 days | form 2-4U33 | MARKET 9.6% | 09:00 median 8.50 | Matchbook 10.00
    comment: Caelan has been placed in his last two outings, a third last time out and another third two starts back, and he has run over today's trip and going, but he is yet to win in recent form and an unseated three starts back is a blot.
    DATA: model 6.6% | style Prominent (led 5% of runs) | runs in data 7 | last 3: 18 Jul Nottingham Flat 10.2f Good To Firm 4/6; 17 Oct Market Rasen Hurdle 16.5f Good 3/6 fig 109; 28 Oct Huntingdon Hurdle 16f Good 3/8 fig 105
    DATA for: Good recent finishing positions; Carries 5 lb less than average
    DATA against: Official rating 106, 5 lb below field average; Fell or unseated in 1 of its last 5 jumps runs
- Rock On Pedro (hrs_25455752) | 8yo G | 160lb | OR 110 | draw 0 | jockey Lewis Saunders(5) | trainer Olly Murphy (14d 10/58) | headgear - | last run 25 days | form 38133- | MARKET 9.5% | 09:00 median 9.00 | Matchbook 9.80
    comment: Rock On Pedro arrives in decent heart, third last time out and again two starts back, with a win three starts back, and he has run over today's trip and going.
    DATA: model 11.4% | style Held up (led 8% of runs) | runs in data 1 | last 3: 27 Oct Catterick Flat 16f Soft 3/12 fig 53
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Pergamon (hrs_41091148) | 5yo G | 168lb | OR 118 | draw 0 | jockey William Shanahan(5) | trainer Jennie Candlish (14d 3/20) | headgear tp | last run 35 days | form 1-1115 | MARKET 4.5% | 09:00 median 19.00 | Matchbook 21.00
    comment: Pergamon won four of his last five starts, with a fifth last time out the only blemish, and he has run over today's trip and going before.
    DATA: model 9.2% | style Midfield (led 3% of runs) | runs in data 6 | last 3: 18 Jul Doncaster Flat 16.5f Good To Firm 3/3; 9 Sep Sedgefield Hurdle 16.8f Good 1/3; 17 Oct Market Rasen Hurdle 16.5f Good 5/6
    DATA for: Official rating 118, 7 lb above field average; Has won at this trip or further; Good recent finishing positions
    DATA against: Last-run finishing speed -4.2% vs that field (faded); Carries 7 lb more than average; Race comments mention jumping mistakes in 2 of its last 5 runs
- Rascallion (hrs_40899586) | 7yo G | 160lb | OR 110 | draw 0 | jockey Paul O'Brien | trainer Henrietta C Knight (14d 0/7) | headgear - | last run 13 days | form 12/2-7 | MARKET 4.2% | 09:00 median 15.00 | Matchbook 32.00
    comment: Rascallion was a winner four starts back and filled second spot twice after that, but a seventh last time out tempers the picture; he is quick back after 13 days and has run over this trip and going, though 160 lb is a hefty burden.
    DATA: model 5.4% | style Held up (led 8% of runs) | runs in data 2 | last 3: 29 Sep Bath Flat 10.2f Good To Firm 6/10; 8 Nov Sandown Hurdle 16f Good To Soft 7/7
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Banderas (hrs_32278498) | 6yo G | 161lb | OR 111 | draw 0 | jockey Jonathan England | trainer Sam England (14d 4/23) | headgear t | last run 21 days | form -51764 | MARKET 3.1% | 09:00 median 26.00 | Matchbook 36.00
    comment: Banderas has been slipping since his win four starts back, finishing a fourth last time out after a sixth and a seventh, and he carries a hefty 161 lb.
    DATA: model 3.6% | style Held up (led 4% of runs) | runs in data 6 | last 3: 2 Oct Hexham Hurdle 16.2f Good 7/7; 16 Oct Uttoxeter Hurdle 20f Good 6/6; 31 Oct Wetherby Hurdle 16f Good 4/4 fig 98
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 98, 10 lb below field average; Recent figures 13 lb below its current mark (looks high in the weights); Race comments mention jumping mistakes in 2 of its last 5 runs
- Premier Tenor (hrs_63357329) | 4yo G | 159lb | OR 109 | draw 0 | jockey Charlie Todd | trainer Dan Skelton (14d 17/80) | headgear ht | last run 11 days | form 32PV | MARKET 3.1% | 09:00 median 22.00 | Matchbook 38.00
    DATA: model 12.1% | style Prominent (led 29% of runs) | runs in data 3 | last 3: 22 May Worcester Hurdle 16f Good 3/10; 11 Jun Worcester Hurdle 16f Good 2/9; 25 Sep Worcester Hurdle 20f Good PU/9
    DATA for: Trainer 21% wins (17/80), last 14 days
    DATA against: Race comments mention jumping mistakes in 2 of its last 3 runs; Pulled up in 1 of its last 3 jumps runs
- Takeit Easy (hrs_18160520) | 11yo G | 150lb | OR 100 | draw 0 | jockey Harry Reed | trainer Pam Sly (14d 0/0) | headgear - | last run 24 days | form P24-67 | MARKET 2.5% | 09:00 median 34.00 | Matchbook 38.00
    comment: The risk is a fading run of 4th, 6th and 7th since, plus 150 lb to carry.
    DATA: model 4.0% | style Leader (led 54% of runs) | runs in data 4 | last 3: 23 Mar Kempton Hurdle 16f Good 4/8; 17 Oct Market Rasen Hurdle 16.5f Good 6/6; 28 Oct Huntingdon Hurdle 16f Good 7/8
    DATA for: Carries 11 lb less than average
    DATA against: Official rating 100, 11 lb below field average; Aged 11, older than most of this field

## 2:33 Huntingdon | race_id rac_32305089791 | Podkovan Zero To Hero Handicap Steeple Chase
Chase | Class 5 | 2m3f189y | going Good | Turf | 10 runners | rating band 0-100 | age 4yo+
DATA pace: Even - Two likely leaders (Cloudy Wednesday, Slievehill). A fair, even gallop is most likely.
- Chosen Hero (hrs_30016189) | 8yo M | 154lb | OR 85 | draw 0 | jockey Callum Pritchard | trainer James Owen (14d 3/30) | headgear - | last run 18 days | form 9PPP-1 | MARKET 29.4% | 09:00 median 2.88 | Matchbook 3.15
    comment: The risk is a patchy record, with three pulled-up runs before that victory, plus 154 lb to carry.
    DATA: model 10.2% | style Midfield (led 4% of runs) | runs in data 4 | last 3: 25 Mar Hexham Hurdle 20.1f Soft PU/14; 20 Apr Kelso Hurdle 18.1f Good PU/9; 3 Nov Lingfield Hurdle 16f Good 1/9 fig 86
    DATA for: Last-run finishing speed +2.5% vs that field (finished strongly)
    DATA against: Pulled up in 3 of its last 4 jumps runs; First run over fences in our data
- Helios Allen (hrs_23240721) | 9yo G | 149lb | OR 80 | draw 0 | jockey Jack Quinlan | trainer Ben Case (14d 1/5) | headgear p | last run 11 days | form /22341 | MARKET 18.5% | 09:00 median 4.33 | Matchbook 5.20
    DATA: model 13.7% | style Prominent (led 4% of runs) | runs in data 5 | last 3: 17 Oct Market Rasen Chase 19f Good 3/5 fig 71; 3 Nov Lingfield Chase 20f Good 4/7 fig 74; 10 Nov Huntingdon Chase 20f Good 1/6 fig 82
    DATA for: Trainer 20% wins (1/5), last 14 days; Has won at this trip or further; Good recent finishing positions; Carries 6 lb less than average
    DATA against: Official rating 80, 6 lb below field average
- Kaproyale (hrs_22559229) | 11yo G | 168lb | OR 99 | draw 0 | jockey Tom Bellamy | trainer Charlie Longsdon (14d 2/13) | headgear - | wind surgery | last run 22 days | form /666-3 | MARKET 11.1% | 09:00 median 7.50 | Matchbook 8.60
    comment: Kaproyale arrives in best form of his recent runs, third last time out after three straight sixths, and he has run over today's trip and going before.
    DATA: model 8.7% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 30 Oct Uttoxeter Chase 20f Good 3/11 fig 100
    DATA for: Best recent form figure 100, 16 lb above field average; Official rating 99, 13 lb above field average; Last-run finishing speed +2.9% vs that field (finished strongly)
    DATA against: Carries 13 lb more than average; Lightly raced: 1 run in our data, so the model has little to go on
- Walk The Plank (hrs_41410593) | 6yo G | 142lb | OR 73 | draw 0 | jockey Ben Poste | trainer Clare Hobson (14d 0/2) | headgear p | last run 11 days | form -45832 | MARKET 10.5% | 09:00 median 8.00 | Matchbook 9.00
    comment: Back in just 11 days, he is hard to fancy.
    DATA: model 7.9% | style Held up (led 3% of runs) | runs in data 7 | last 3: 7 Jul Uttoxeter Chase 16f Good 8/10; 2 Nov Southwell Chase 16f Good 3/5 fig 66; 10 Nov Huntingdon Chase 20f Good 2/6 fig 77
    DATA for: Recent figures 4 lb above its current mark (looks well handicapped); Good recent finishing positions; Carries 13 lb less than average
    DATA against: Best recent form figure 77, 6 lb below field average; Official rating 73, 13 lb below field average; Race comments mention jumping mistakes in 2 of its last 5 runs
- Forcetoreckonwith (hrs_38305400) | 7yo M | 156lb | OR 87 | draw 0 | jockey Jack Tudor | trainer Oliver Greenall & Josh Guerriero (14d 2/8) | headgear t | last run 35 days | form 14-F44 | MARKET 7.0% | 09:00 median 12.00 | Matchbook 14.00
    DATA: model 6.5% | style Prominent (led 4% of runs) | runs in data 7 | last 3: 31 Aug Cartmel Chase 17.3f Good To Soft F/6; 25 Sep Worcester Chase 16.5f Good 4/9; 17 Oct Market Rasen Chase 19f Good 4/5 fig 79
    DATA for: Trainer 25% wins (2/8), last 14 days
    DATA against: Best recent form figure 79, 4 lb below field average; Recent figures 8 lb below its current mark (looks high in the weights); Fell or unseated in 1 of its last 5 jumps runs
- Kally des Bruyeres (hrs_37096094) | 6yo G | 162lb | OR 93 | draw 0 | jockey Adam Wedge | trainer David Dennis (14d 0/1) | headgear - | last run 22 days | form 1-F52P | MARKET 6.8% | 09:00 median 13.00 | Matchbook 13.50
    comment: Kally des Bruyeres finished second two starts back and has run over today's trip and going, while 22 days since his last outing keeps him fresh; the risk is that he was pulled up last time out and carries 162 lb.
    DATA: model 14.5% | style Midfield (led 8% of runs) | runs in data 8 | last 3: 25 Sep Worcester Chase 16.5f Good 5/9; 12 Oct Worcester Chase 16.5f Good To Soft 2/9; 30 Oct Uttoxeter Chase 20f Good PU/11
    DATA for: Official rating 93, 7 lb above field average
    DATA against: Carries 7 lb more than average; Race comments mention jumping mistakes in 2 of its last 5 runs; Fell or unseated in 1 of its last 5 jumps runs; Pulled up in 1 of its last 5 jumps runs
- Cloudy Wednesday (hrs_23332568) | 10yo G | 158lb | OR 89 | draw 0 | jockey Isabelle Ryder(5) | trainer Caroline Fryer (14d 0/0) | headgear p | last run 180 days | form 3P-322 | MARKET 5.8% | 09:00 median 13.00 | Matchbook 18.00
    comment: Cloudy Wednesday has been placed in four of his last five, including a second last time out and another second two starts back, but he's yet to win in that spell and returns after 180 days off.
    DATA: model 15.0% | style Leader (led 63% of runs) | runs in data 6 | last 3: 8 May Market Rasen Chase 21.4f Good 3/7; 19 May Huntingdon Chase 19.9f Good To Firm 2/5; 25 May Huntingdon Chase 23.6f Good To Firm 2/4
    DATA for: Good recent finishing positions
    DATA against: Returns from a 180-day break; Pulled up in 1 of its last 5 jumps runs
- McGrath From Clune (hrs_21212513) | 10yo G | 147lb | OR 78 | draw 0 | jockey Lorcan Williams | trainer Tom Gretton (14d 0/4) | headgear tp | last run 27 days | form 2P-0P3 | MARKET 4.6% | 09:00 median 17.00 | Matchbook 24.00
    comment: McGrath From Clune is winless in his last five and has been pulled up twice in that spell, though a third last time out, 27 days ago, hints at some revival.
    DATA: model 2.2% | style Held up (led 5% of runs) | runs in data 4 | last 3: 11 May Southwell Hurdle 15.8f Good 10/13; 16 Jun Stratford Hurdle 18.7f Good PU/10; 25 Oct Market Rasen Chase 19f Good To Soft 3/5 fig 77
    DATA for: Carries 8 lb less than average
    DATA against: Best recent form figure 77, 6 lb below field average; Official rating 78, 8 lb below field average; Pulled up in 2 of its last 4 jumps runs
- Universal Secret (hrs_25040813) | 9yo G | 154lb | OR 85 | draw 0 | jockey Paul O'Brien | trainer Helen Nelmes (14d 0/3) | headgear tp | last run 189 days | form PP12-4 | MARKET 3.7% | 09:00 median 25.00 | Matchbook 25.00
    comment: Universal Secret signed off with a fourth last time out, after a second two starts back and a win three starts back, and he has run over today's trip and going before.
    DATA: model 15.3% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 25 Feb Wincanton Chase 20.2f Good To Soft 1/9; 1 Apr Wincanton Chase 20.2f Good 2/7; 16 May Uttoxeter Chase 20.9f Good 4/10
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Last-run finishing speed -2.7% vs that field (faded); Returns from a 189-day break
- Slievehill (hrs_28903826) | 9yo G | 157lb | OR 88 | draw 0 | jockey Jamie Brace(5) | trainer D. J. Jeffreys (14d 0/3) | headgear - | last run 18 days | form 50P-30 | MARKET 2.5% | 09:00 median 34.00 | Matchbook 44.00
    comment: Slievehill showed he retains ability with a third two starts back, and he returns just 18 days after his last run, having already run over today's trip and going. He is yet to win in his last five, though, and 157 lb is a stiff burden to carry.
    DATA: model 6.0% | style Leader (led 54% of runs) | runs in data 3 | last 3: 22 Jan Wetherby Hurdle 24.1f Soft PU/7; 8 Oct Market Rasen Hurdle 20.6f Good 3/5; 3 Nov Sedgefield Hurdle 20f Good 10/11
    DATA against: Last-run finishing speed -8.5% vs that field (faded); Pulled up in 1 of its last 3 jumps runs; First run over fences in our data

## 3:10 Huntingdon | race_id rac_32305091728 | Podkovans Last Orders "Junior" National Hunt Flat Race (GBB Race)
NH Flat | Class 5 | 1m7f171y | going Good | Turf | 12 runners | rating band - | age 3yo
DATA pace: Unclear - Running styles known for only 2 of 12 runners.
- Nostrae de Cougny (hrs_17393897920) | 3yo G | 163lb | OR - | draw 0 | jockey Charlie Hammond | trainer Stuart Edmunds (14d 1/8) | headgear h | last run 35 days | form 1 | MARKET 32.2% | 09:00 median 2.63 | Matchbook 2.82
    DATA: model 19.5% | style Held up (led 8% of runs) | runs in data 1 | last 3: 17 Oct Market Rasen NH Flat 16.5f Good 1/6 fig 131
    DATA for: Last-run finishing speed +9.0% vs that field (finished strongly); Has won at this trip or further
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Took You Two (hrs_17395092155) | 3yo G | 156lb | OR - | draw 0 | jockey Tom Bellamy | trainer Alan King (14d 2/18) | headgear - | last run - days | form - | MARKET 16.1% | 09:00 median 5.00 | Matchbook 5.90
    comment: Unraced and open to improvement, Took You Two makes his debut with no form to go on, so he's very much an unexposed sort. He carries 156 lb, and it's a case of seeing what he shows first time out.
    DATA: model 7.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Annies Pass (hrs_17393313840) | 3yo F | 149lb | OR - | draw 0 | jockey Paul O'Brien | trainer Charlie Longsdon (14d 2/13) | headgear - | last run 35 days | form 2 | MARKET 13.9% | 09:00 median 6.00 | Matchbook 6.60
    DATA: model 8.3% | style Leader (led 57% of runs) | runs in data 1 | last 3: 17 Oct Market Rasen NH Flat 16.5f Good 2/6 fig 121
    DATA for: Last-run finishing speed +6.0% vs that field (finished strongly)
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Touriga Park (hrs_17395802438) | 3yo G | 156lb | OR - | draw 0 | jockey Charlie Todd | trainer Dan Skelton (14d 17/80) | headgear - | last run - days | form - | MARKET 11.6% | 09:00 median 7.00 | Matchbook 8.40
    comment: Touriga Park is a debutant with no recorded form, so he's an unexposed type with plenty of scope for improvement.
    DATA: model 7.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 21% wins (17/80), last 14 days
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Snicket (hrs_17393321141) | 3yo G | 156lb | OR - | draw 0 | jockey Callum Pritchard | trainer James Owen (14d 3/30) | headgear - | last run 46 days | form 4 | MARKET 10.1% | 09:00 median 8.00 | Matchbook 9.40
    comment: The main risk is the 156 lb on his back, and he is yet to win in his recent form.
    DATA: model 9.2% | style Unknown | runs in data 1 | last 3: 6 Oct Huntingdon NH Flat 15.8f Good 4/8
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Logical Dreamer (hrs_17393319055) | 3yo G | 156lb | OR - | draw 0 | jockey Luke Scott(3) | trainer Dr Richard Newland (14d 0/0) | headgear - | last run - days | form - | MARKET 4.9% | 09:00 median 17.00 | Matchbook 21.00
    comment: Logical Dreamer is unexposed with no recorded form to go on, so this debut is a step into the unknown, and he carries 156 lb. Open to improvement as a newcomer, he is one to learn about rather than judge.
    DATA: model 7.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Nenuphar (hrs_17395800352) | 3yo G | 156lb | OR - | draw 0 | jockey Troy Walsh(7) | trainer Tom Weston (14d 0/0) | headgear - | last run - days | form - | MARKET 3.2% | 09:00 median 23.00 | Matchbook 40.00
    comment: Nenuphar is unraced, so this gelding is a complete unknown and open to plenty of improvement. He carries 156 lb on debut, and with no form to go on, he is one to judge on what he shows.
    DATA: model 7.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Fohlly (hrs_17395798266) | 3yo F | 149lb | OR - | draw 0 | jockey Kevin Brogan | trainer Toby Lawes (14d 0/3) | headgear - | last run - days | form - | MARKET 2.4% | 09:00 median 29.00 | Matchbook 55.00
    comment: Fohlly is an unraced filly with no form to assess, so she's firmly unexposed and open to improvement.
    DATA: model 6.9% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- L'Architect (hrs_17395799309) | 3yo G | 156lb | OR - | draw 0 | jockey Joe Anderson(3) | trainer Martin Dunne (14d 0/2) | headgear - | last run - days | form - | MARKET 1.7% | 09:00 median 41.00 | Matchbook 85.00
    comment: Unraced and making his debut, L'Architect is a blank canvas with no form to go on, so he's unexposed and open to plenty of improvement. He carries 156 lb, and it's a case of waiting to see what he shows first time out.
    DATA: model 7.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Corcordium (hrs_17395797223) | 3yo G | 156lb | OR - | draw 0 | jockey Tom Cannon | trainer Louise Allan (14d 0/1) | headgear - | last run - days | form - | MARKET 1.3% | 09:00 median 51.00 | Matchbook 100.00
    comment: Corcordium is unexposed with no recorded form to go on, so he's an open book at this stage. Carrying 156 lb, the gelding is yet to show what he can do and could well have improvement in him.
    DATA: model 7.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Tilsworth Michael (hrs_17395801395) | 3yo G | 156lb | OR - | draw 0 | jockey Ned Fox(3) | trainer J. R. Jenkins (14d 0/2) | headgear - | last run - days | form - | MARKET 1.3% | 09:00 median 51.00 | Matchbook 130.00
    comment: Tilsworth Michael is unexposed with no recorded runs to go on, so this gelding's debut is a step into the unknown and he looks open to improvement. He carries 156 lb, and there's little to judge him on until he's seen in action.
    DATA: model 7.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Potters Beauden (hrs_17393320098) | 3yo G | 156lb | OR - | draw 0 | jockey Jack Quinlan | trainer Matt Crawley (14d 0/2) | headgear - | last run 46 days | form 8 | MARKET 1.3% | 09:00 median 51.00 | Matchbook 120.00
    comment: The risk is a eighth last time out and 156 lb, a hefty burden for a gelding yet to win in recent form.
    DATA: model 3.5% | style Unknown | runs in data 1 | last 3: 6 Oct Huntingdon NH Flat 15.8f Good 8/8
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
