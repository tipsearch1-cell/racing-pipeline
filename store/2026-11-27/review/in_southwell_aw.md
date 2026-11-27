# Card review packet: Southwell (AW), 2026-11-27

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
{"meeting": "southwell_aw", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 2:40 Southwell (AW) | race_id rac_32305740623 | Midnite Golden Rose Stakes (Listed Race)
Flat | Class 1 | 6f16y | going Standard | AW | 8 runners | rating band - | age 3yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Beckford's Folly (hrs_53359635) | 3yo G | 131lb | OR 109 | draw 2 | jockey Billy Loughnane | trainer Charlie Appleby (14d 5/10) | headgear - | last run 209 days | form 161-80 | MARKET 22.8% | 09:00 median 4.00 | Matchbook 4.20 | CHECK (skip line 3.80)
    comment: Beckford's Folly won three starts back and five starts back, but he was unplaced last time and eighth before that, and he returns after 209 days off.
    DATA: model 9.8% | style Unknown | runs in data 2 | last 3: 16 Apr Newmarket Flat 6f Good 8/14; 2 May Newmarket Flat 5f Good To Firm 11/14
    DATA for: Official rating 109, 6 lb above field average; Trainer 50% wins (5/10), last 14 days
    DATA against: Returns from a 209-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- Soldier's Tree (hrs_41013959) | 5yo G | 131lb | OR 107 | draw 6 | jockey Kieran Shoemark | trainer James Owen (14d 4/47) | headgear h | last run 118 days | form 123330 | MARKET 20.9% | 09:00 median 4.00 | Matchbook 4.70
    comment: Soldier's Tree was placed in three straight runs, a third, another third and a third again, before going unplaced last time out, and he has run over today's trip and going.
    DATA: model 18.4% | style Unknown | runs in data 6 | last 3: 20 Jun Ascot Flat 6f Good To Firm 3/27; 18 Jul Newbury Flat 6f Good To Firm 3/7; 1 Aug Goodwood Flat 6f Good To Firm 12/27
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Returns from a 118-day break
- Crestofdistinction (hrs_42943852) | 4yo G | 131lb | OR 107 | draw 5 | jockey George Bass | trainer Jack Channon (14d 0/9) | headgear - | last run 20 days | form -00021 | MARKET 19.1% | 09:00 median 4.50 | Matchbook 4.90
    comment: Crestofdistinction arrives in good heart, a winner last time out and second two starts back, and he returns after a fresh 20 days having run over today's trip.
    DATA: model 16.4% | style Prominent (led 8% of runs) | runs in data 5 | last 3: 13 Sep Doncaster Flat 6.5f Good 11/13; 11 Oct Goodwood Flat 6f Good To Soft 2/13; 7 Nov Doncaster Flat 6f Good To Soft 1/22 fig 113
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Trainer 0 wins from 9 runs, last 14 days
- Montassib (hrs_22372042) | 8yo G | 131lb | OR 104 | draw 4 | jockey Cieren Fallon | trainer William Haggas (14d 4/26) | headgear t | last run 20 days | form 5-4533 | MARKET 16.2% | 09:00 median 5.50 | Matchbook 5.70
    comment: The risk is that he is yet to win in his last five starts, and 131 lb is a big weight to carry.
    DATA: model 17.7% | style Held up (led 8% of runs) | runs in data 4 | last 3: 23 May Curragh Flat 6f Good 5/10; 30 Sep Kempton Flat 6f Standard To Slow 3/6; 7 Nov Doncaster Flat 6f Good To Soft 3/20 fig 113
    DATA for: Good recent finishing positions
    DATA against: Aged 8, older than most of this field; Pace: steady gallop likely, hard to come from off the pace
- Ain't Nobody (hrs_39961502) | 4yo G | 131lb | OR 105 | draw 3 | jockey Kevin Stott | trainer Kevin Ryan (14d 0/3) | headgear p | last run 35 days | form 900732 | MARKET 6.7% | 09:00 median 13.00 | Matchbook 15.00
    comment: Ain't Nobody arrives on an upward curve after a second last time out and a third two starts back, and he has run over today's trip and going, though he is yet to win in his last six and returns after 35 days off.
    DATA: model 12.3% | style Prominent (led 29% of runs) | runs in data 7 | last 3: 30 Aug Beverley Flat 5f Heavy 7/8; 22 Sep Beverley Flat 5f Good 3/6; 23 Oct Dundalk (AW) (IRE) Flat 5f Standard 2/13 fig 106
    DATA for: Good recent finishing positions
- Zen Diva (hrs_54494440) | 3yo F | 126lb | OR 97 | draw 8 | jockey Hector Crouch | trainer Ralph Beckett (14d 3/11) | headgear - | last run 20 days | form 101126 | MARKET 6.4% | 09:00 median 12.00 | Matchbook 17.00
    comment: Zen Diva won three of her last six, and was second two starts back, but a sixth last time out is the latest word and she has to carry 126 lb from draw eight.
    DATA: model 14.4% | style Midfield (led 4% of runs) | runs in data 7 | last 3: 3 Sep Salisbury Flat 6f Good To Soft 1/9; 9 Oct Newmarket Flat 6f Good 2/13; 7 Nov Doncaster Flat 6f Good To Soft 6/20 fig 106
    DATA for: Trainer 27% wins (3/11), last 14 days; Has won at this trip or further; Good recent finishing positions
    DATA against: Official rating 97, 6 lb below field average
- Partisan Hero (hrs_32499964) | 6yo G | 131lb | OR 103 | draw 1 | jockey Callum Shepherd | trainer David Loughnane (14d 4/13) | headgear p | last run 75 days | form 332700 | MARKET 6.4% | 09:00 median 13.00 | Matchbook 16.00
    comment: The main risk is a 75-day absence, with his last two runs unplaced and him yet to win in recent form.
    DATA: model 4.9% | style Prominent (led 5% of runs) | runs in data 8 | last 3: 31 Jul Goodwood Flat 5f Good To Firm 7/15; 21 Aug York Flat 5f Good To Soft 15/18; 13 Sep Curragh Flat 5f Yielding 12/17
    DATA for: Trainer 31% wins (4/13), last 14 days
    DATA against: Poor recent finishing positions
- Hollywood Treasure (hrs_51342284) | 3yo F | 126lb | OR 95 | draw 7 | jockey Rowan Scott | trainer Kevin Philippart de Foy (14d 3/11) | headgear - | last run 49 days | form 17-270 | MARKET 1.4% | 09:00 median 67.00 | Matchbook 75.00
    DATA: model 6.1% | style Unknown | runs in data 3 | last 3: 2 May Goodwood Flat 6f Good 2/9; 23 May Salisbury Flat 6f Good 7/10; 9 Oct Newmarket Flat 6f Good 11/13
    DATA for: Trainer 27% wins (3/11), last 14 days
    DATA against: Official rating 95, 8 lb below field average

## 3:15 Southwell (AW) | race_id rac_32305742560 | Midnite Churchill Stakes (Listed Race)
Flat | Class 1 | 1m3f23y | going Standard | AW | 6 runners | rating band - | age 3yo+
DATA pace: Even - Two likely leaders (Military Order, By The Book). A fair, even gallop is most likely.
- Military Order (hrs_32104240) | 6yo G | 133lb | OR 114 | draw 4 | jockey Billy Loughnane | trainer Charlie Appleby (14d 5/10) | headgear - | last run 14 days | form 223-19 | MARKET 50.0% | 09:00 median 1.83 | Matchbook 1.94
    DATA: model 35.4% | style Leader (led 57% of runs) | runs in data 2 | last 3: 25 Sep Dundalk Flat 10.7f Standard 1/7; 13 Nov Bahrain Flat  Good 9/12
    DATA for: Official rating 114, 9 lb above field average; Trainer 50% wins (5/10), last 14 days; Has won at this trip or further
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Warrant Holder (hrs_49757148) | 4yo G | 130lb | OR 112 | draw 7 | jockey Robert Havlin | trainer John & Thady Gosden (14d 3/25) | headgear t | last run 83 days | form 1-1203 | MARKET 24.0% | 09:00 median 3.75 | Matchbook 4.10
    comment: The one risk is a break of 83 days since his last run, so fitness could count against him from stall 7 under 130 lb.
    DATA: model 23.7% | style Unknown | runs in data 4 | last 3: 19 Jun Ascot Flat 12f Good To Firm 2/17; 11 Jul York Flat 10.3f Good To Firm 10/22; 5 Sep Kempton Flat 12f Standard To Slow 3/5
    DATA for: Official rating 112, 7 lb above field average; Good recent finishing positions
- Spinning Wheel (hrs_52117324) | 4yo G | 130lb | OR 107 | draw 2 | jockey Harry Davies | trainer Simon Crisford (14d 5/10) | headgear - | last run 97 days | form 1-2010 | MARKET 11.3% | 09:00 median 8.00 | Matchbook 8.60
    comment: Spinning Wheel has won twice in his last five starts, a first five starts back and another two starts back, and he has run over today's trip and going before, so he is a strong threat from draw 2. The one concern is a 97-day absence after an unplaced run last time out.
    DATA: model 8.1% | style Midfield (led 5% of runs) | runs in data 4 | last 3: 6 Jun Epsom Downs Flat 12f Soft 12/13; 6 Aug Southwell Flat 11.1f Standard 1/12; 22 Aug York Flat 13.9f Good To Soft 19/22
    DATA for: Trainer 50% wins (5/10), last 14 days; Has won at this trip or further
    DATA against: Returns from a 97-day break
- By The Book (hrs_35828240) | 5yo G | 130lb | OR 106 | draw 5 | jockey Kieran Shoemark | trainer Charlie Appleby (14d 5/10) | headgear p (1st time) | last run 55 days | form 336224 | MARKET 9.3% | 09:00 median 9.50 | Matchbook 11.00
    comment: The main risk is a 55-day break and he is still yet to win in his last six starts.
    DATA: model 20.0% | style Leader (led 57% of runs) | runs in data 3 | last 3: 4 Jul Beverley Flat 12.1f Good To Firm 2/5; 22 Aug Chester Flat 14.4f Good To Soft 2/8; 3 Oct Ascot Flat 12f Good To Firm 4/5
    DATA for: Trainer 50% wins (5/10), last 14 days; Good recent finishing positions; First-time headgear
- Old Harrovian (hrs_26473139) | 7yo G | 130lb | OR 97 | draw 3 | jockey Callum Hutchinson | trainer Andrew Balding (14d 4/39) | headgear t | last run 69 days | form /212-6 | MARKET 3.3% | 09:00 median 26.00 | Matchbook 34.00
    comment: Old Harrovian looks hard to fancy after a sixth last time out and a 69-day absence, though a second two starts back and a win three starts back show some ability.
    DATA: model 5.7% | style Unknown | runs in data 1 | last 3: 19 Sep Newbury Flat 10f Good To Firm 6/11
    DATA against: Official rating 97, 8 lb below field average; Lightly raced: 1 run in our data, so the model has little to go on
- Zgharta (hrs_46515308) | 4yo F | 125lb | OR 93 | draw 6 | jockey P. J. McDonald | trainer Andrew Balding (14d 4/39) | headgear - | last run 20 days | form 047145 | MARKET 2.2% | 09:00 median 34.00 | Matchbook 60.00
    comment: Zgharta was fifth last time out, and a fourth two starts back follows a win three starts back, so the form is patchy with just that one success in her last six.
    DATA: model 7.1% | style Unknown | runs in data 6 | last 3: 31 Jul Goodwood Flat 9.9f Good To Firm 7/7; 3 Sep Salisbury Flat 9.9f Good To Soft 1/7; 7 Nov Doncaster Flat 10f Good To Soft 5/17 fig 94
    DATA against: Official rating 93, 12 lb below field average

## 3:45 Southwell (AW) | race_id rac_32305744497 | All-Weather Championship Is Back Handicap Stakes
Flat | Class 6 | 1m13y | going Standard | AW | 13 runners | rating band 0-60 | age 3yo+
DATA pace: Even - Two likely leaders (Tasever, Double Time). A fair, even gallop is most likely.
- El Fox (hrs_42846776) | 4yo F | 133lb | OR 60 | draw 4 | jockey Luke Morris | trainer Marco Botti (14d 0/14) | headgear - | last run 41 days | form 4-4311 | MARKET 16.8% | 09:00 median 4.50 | Matchbook 5.80 | CHECK (skip line 4.27)
    comment: El Fox arrives on a two-race winning streak, having won last time out and two starts back, and she has run over today's trip and going before.
    DATA: model 19.4% | style Prominent (led 3% of runs) | runs in data 4 | last 3: 28 May Yarmouth Flat 8f Good To Firm 3/9; 10 Oct Southwell Flat 8.1f Standard 1/12; 17 Oct Southwell (AW) Flat 8f Standard 1/11 fig 59
    DATA for: Best recent form figure 59, 5 lb above field average; Has won at this trip or further; Good recent finishing positions
    DATA against: Trainer 0 wins from 14 runs, last 14 days
- Under The Sun (hrs_35767599) | 5yo G | 132lb | OR 59 | draw 12 | jockey Harry Davies | trainer James Owen (14d 4/47) | headgear t | last run 25 days | form 014355 | MARKET 13.4% | 09:00 median 6.00 | Matchbook 7.00
    comment: Under The Sun has been consistent without winning lately, a third three starts back and two fifths since, and he has run over today's trip and going before.
    DATA: model 11.0% | style Midfield (led 4% of runs) | runs in data 7 | last 3: 7 May Windsor Flat 8.1f Good To Firm 3/11; 23 Oct Wolverhampton (AW) Flat 8.5f Standard 5/11 fig 58; 2 Nov Wolverhampton (AW) Flat 9.5f Standard 5/9 fig 56
    DATA for: Best recent form figure 58, 4 lb above field average; Has won at this trip or further
- Boy Named Sioux (hrs_52117331) | 3yo G | 131lb | OR 60 | draw 7 | jockey Oisin Orr | trainer Richard & Peter Fahey (14d 0/14) | headgear - | last run 31 days | form 908793 | MARKET 11.8% | 09:00 median 7.00 | Matchbook 7.80
    comment: Boy Named Sioux bounced back with a third last time out after a run of ninth, seventh and eighth finishes, and he has run over today's trip and going before.
    DATA: model 6.8% | style Unknown | runs in data 8 | last 3: 21 Sep Wolverhampton Flat 9.5f Standard 7/11; 16 Oct Redcar Flat 10f Good 9/14 fig 54; 27 Oct Wolverhampton (AW) Flat 8.5f Standard 3/10 fig 60
    DATA for: Best recent form figure 60, 6 lb above field average
    DATA against: Trainer 0 wins from 14 runs, last 14 days
- Lili Marleen (hrs_46944569) | 4yo F | 131lb | OR 58 | draw 9 | jockey Cieren Fallon | trainer Jack Jones (14d 0/7) | headgear p | last run 27 days | form 889218 | MARKET 11.1% | 09:00 median 7.50 | Matchbook 8.20
    comment: Lili Marleen was eighth last time out and has finished eighth or worse in four of her last six, though she did win two starts back and was second three starts back.
    DATA: model 14.4% | style Prominent (led 5% of runs) | runs in data 9 | last 3: 17 Oct Southwell (AW) Flat 8f Standard 2/11 fig 54; 24 Oct Southwell (AW) Flat 8f Standard 1/13 fig 59; 31 Oct Southwell (AW) Flat 8f Standard 8/14 fig 53
    DATA for: Best recent form figure 59, 5 lb above field average; Has won at this trip or further; Good recent finishing positions
- Beauty Generation (hrs_33789553) | 5yo G | 133lb | OR 60 | draw 5 | jockey Jason Hart | trainer Ross Burdon (14d 1/5) | headgear p | last run 56 days | form 451322 | MARKET 11.0% | 09:00 median 7.00 | Matchbook 8.80
    comment: Beauty Generation arrives in solid recent form, second last time out and second again two starts back, with a win four starts back, though 56 days off the track raises a fitness question.
    DATA: model 10.0% | style Prominent (led 29% of runs) | runs in data 9 | last 3: 21 Jul Nottingham Flat 9f Good To Firm 3/6; 11 Aug Nottingham Flat 10.2f Good To Firm 2/8; 2 Oct Newcastle Flat 8f Standard 2/6
    DATA for: Trainer 20% wins (1/5), last 14 days; Has won at this trip or further; Good recent finishing positions
- Mr Fustic (hrs_25443551) | 8yo G | 130lb | OR 57 | draw 6 | jockey Marco Ghiani | trainer Andi Brown (14d 1/1) | headgear tp | last run 58 days | form 145042 | MARKET 9.0% | 09:00 median 9.00 | Matchbook 10.50
    comment: He has run over today's trip and going, though, and 130 lb from stall six is no outrageous burden.
    DATA: model 7.7% | style Held up (led 4% of runs) | runs in data 7 | last 3: 31 Aug Southwell Flat 8.1f Standard 10/14; 15 Sep Wolverhampton Flat 8.6f Standard 4/12; 30 Sep Kempton Flat 8f Standard To Slow 2/11
    DATA for: Has won at this trip or further
    DATA against: Aged 8, older than most of this field
- Tasever (hrs_30765105) | 6yo G | 133lb | OR 60 | draw 11 | jockey David Nolan | trainer Patrick Morris (14d 0/15) | headgear p | last run 6 days | form 704077 | MARKET 7.7% | 09:00 median 9.50 | Matchbook 13.50
    comment: Tasever is yet to win in his last six starts, with back-to-back seventh-place finishes and a fourth four starts back his best recent effort, though he has run over today's trip and going and is back quickly after six days.
    DATA: model 5.9% | style Leader (led 29% of runs) | runs in data 14 | last 3: 25 Sep Newcastle Flat 7.1f Standard 11/11; 20 Oct Newcastle (AW) Flat 8f Standard 7/12 fig 58; 21 Nov Newcastle (AW) Flat 7f Standard 7/13 fig 54
    DATA for: Best recent form figure 58, 4 lb above field average; Has won at this trip or further
    DATA against: Trainer 0 wins from 15 runs, last 14 days; Poor recent finishing positions
- Fools Rush In (hrs_20977691) | 8yo G | 132lb | OR 59 | draw 2 | jockey James Sullivan | trainer Ruth Carr (14d 3/12) | headgear tv | last run 20 days | form 802309 | MARKET 4.0% | 09:00 median 17.00 | Matchbook 30.00
    comment: Fools Rush In was ninth last time but posted a third three starts back and a second four starts back, and he has run over today's trip and going before.
    DATA: model 4.1% | style Held up (led 8% of runs) | runs in data 12 | last 3: 30 Sep Catterick Flat 7f Good 3/9; 23 Oct Wolverhampton (AW) Flat 8.5f Standard 10/10 fig 45; 7 Nov Southwell (AW) Flat 7f Standard 9/12 fig 52
    DATA for: Trainer 25% wins (3/12), last 14 days; Has won at this trip or further
    DATA against: Recent figures 7 lb below its current mark (looks high in the weights); Aged 8, older than most of this field
- Popeye Doyle (hrs_39961208) | 4yo G | 130lb | OR 57 | draw 10 | jockey Darragh O'Sullivan(7) | trainer Jessica Bedi (14d 0/9) | headgear tb | last run 29 days | form 297658 | MARKET 3.9% | 09:00 median 21.00 | Matchbook 24.00
    comment: Popeye Doyle is hard to fancy, having finished eighth last time out and without a win in his last six starts, with a second six starts back the only real highlight.
    DATA: model 3.1% | style Midfield (led 23% of runs) | runs in data 7 | last 3: 18 Jul Nottingham Flat 8.3f Good To Firm 6/6; 28 Sep Wolverhampton Flat 9.5f Standard 5/10; 29 Oct Southwell (AW) Flat 8f Standard 8/13 fig 53
    DATA against: Trainer 0 wins from 9 runs, last 14 days
- Double Time (hrs_29906261) | 8yo G | 131lb | OR 58 | draw 1 | jockey Callum Hutchinson | trainer Mitchell Hunt & Tim Vaughan (14d 1/5) | headgear ht | wind surgery | last run 44 days | form 6-7008 | MARKET 3.5% | 09:00 median 21.00 | Matchbook 30.00
    comment: The risk is a poor run of finishes after 44 days off.
    DATA: model 3.1% | style Prominent (led 43% of runs) | runs in data 4 | last 3: 23 Jul Sandown Flat 8f Good To Firm 12/12; 20 Aug Lingfield Flat 7f Standard 11/11; 14 Oct Kempton (AW) Flat 8f Standard / Slow 8/9 fig 42
    DATA for: Trainer 20% wins (1/5), last 14 days
    DATA against: Best recent form figure 42, 12 lb below field average; Recent figures 16 lb below its current mark (looks high in the weights); Poor recent finishing positions; Aged 8, older than most of this field
- Bass Player (hrs_29842631) | 7yo G | 130lb | OR 57 | draw 13 | jockey Matthew Lloyd Slater(7) | trainer Kevin & Lauren Frost (14d 1/13) | headgear t | last run 155 days | form 4-9053 | MARKET 3.1% | 09:00 median 21.00 | Matchbook 38.00
    comment: Bass Player showed a return to form when third last time out, and he has run over today's trip and on this going before.
    DATA: model 3.4% | style Prominent (led 23% of runs) | runs in data 4 | last 3: 8 May Ripon Flat 9.8f Good 11/12; 31 May Nottingham Flat 8.3f Good 5/7; 25 Jun Leicester Flat 7f Good To Firm 3/5
    DATA against: Returns from a 155-day break
- Sunshine And Roses (hrs_53420367) | 3yo F | 131lb | OR 60 | draw 14 | jockey P. J. McDonald | trainer John Mackie (14d 0/7) | headgear - | last run 39 days | form 220260 | MARKET 2.6% | 09:00 median 29.00 | Matchbook 42.00
    comment: Winless in her last six, with an unplaced effort last time out and a sixth two starts back, Sunshine And Roses is hard to fancy, though she was second three starts back and has run over today's trip and going.
    DATA: model 6.7% | style Held up (led 8% of runs) | runs in data 9 | last 3: 12 Sep Lingfield Flat 8f Standard 2/4; 23 Sep Kempton Flat 8f Standard To Slow 6/10; 19 Oct Southwell (AW) Flat 8f Standard 10/14 fig 49
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 49, 5 lb below field average; Recent figures 11 lb below its current mark (looks high in the weights)
- Hint of The Jungle (hrs_35596561) | 5yo G | 131lb | OR 58 | draw 3 | jockey Callum Shepherd | trainer Mike Murphy (14d 0/2) | headgear ht | last run 23 days | form 221087 | MARKET 2.1% | 09:00 median 34.00 | Matchbook 60.00
    comment: Hint of The Jungle has tailed off with a seventh last time out and an eighth before that, though he won four starts back and has run over today's trip and going.
    DATA: model 4.4% | style Prominent (led 23% of runs) | runs in data 12 | last 3: 17 Sep Yarmouth Flat 7f Good 10/13; 12 Oct Kempton Flat 6f Standard To Slow 8/10; 4 Nov Kempton (AW) Flat 8f Standard / Slow 7/13 fig 50
    DATA against: Best recent form figure 50, 4 lb below field average; Recent figures 8 lb below its current mark (looks high in the weights); Poor recent finishing positions

## 4:15 Southwell (AW) | race_id rac_32305746434 | AWC Season 14 Has Begun EBF Fillies' Novice Stakes (Div I) (GBB/GBBPlus Race)
Flat | Class 3 | 1m13y | going Standard | AW | 11 runners | rating band - | age 2yo
DATA pace: Unclear - Running styles known for only 2 of 11 runners.
- Southover Gardens (hrs_17396119510) | 2yo F | 128lb | OR - | draw 7 | jockey Robert Havlin | trainer John & Thady Gosden (14d 3/25) | headgear - | last run - days | form - | MARKET 23.6% | 09:00 median 3.65 | Matchbook 3.65 | CHECK (skip line 3.47)
    DATA: model 8.7% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Gracious Gift (hrs_66305820) | 2yo F | 128lb | OR - | draw 6 | jockey Connor Planas | trainer Charlie Appleby (14d 5/10) | headgear - | last run 133 days | form 26 | MARKET 18.7% | 09:00 median 4.00 | Matchbook 5.30
    DATA: model 14.4% | style Unknown | runs in data 2 | last 3: 2 Jul Yarmouth Flat 7f Good To Firm 2/5; 17 Jul Newmarket Flat 7f Good To Firm 6/7
    DATA for: Trainer 50% wins (5/10), last 14 days
    DATA against: Returns from a 133-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- Kalypsa (hrs_17395881706) | 2yo F | 128lb | OR - | draw 2 | jockey Cieren Fallon | trainer William Haggas (14d 4/26) | headgear - | last run - days | form - | MARKET 17.0% | 09:00 median 4.50 | Matchbook 5.40
    DATA: model 8.7% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Signora Fortuna (hrs_17394203519) | 2yo F | 128lb | OR - | draw 4 | jockey Kieran Shoemark | trainer Ed Walker (14d 2/26) | headgear - | last run - days | form - | MARKET 12.1% | 09:00 median 7.00 | Matchbook 7.40
    DATA: model 8.7% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Sassi Lady (hrs_17395703353) | 2yo F | 128lb | OR - | draw 5 | jockey Hector Crouch | trainer Ralph Beckett (14d 3/11) | headgear - | last run - days | form - | MARKET 10.0% | 09:00 median 8.50 | Matchbook 9.00
    DATA: model 8.7% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 27% wins (3/11), last 14 days
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Rose Chimes (hrs_17394558139) | 2yo F | 128lb | OR - | draw 3 | jockey Rowan Scott | trainer Kevin Philippart de Foy (14d 3/11) | headgear - | last run - days | form - | MARKET 5.3% | 09:00 median 15.00 | Matchbook 18.50
    DATA: model 8.7% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 27% wins (3/11), last 14 days
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Camatillo (hrs_17395925512) | 2yo F | 128lb | OR - | draw 10 | jockey Sean Levey | trainer Richard Hannon (14d 2/15) | headgear - | last run - days | form - | MARKET 4.3% | 09:00 median 17.00 | Matchbook 27.00
    DATA: model 8.7% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Ouattara (hrs_17396116381) | 2yo F | 128lb | OR - | draw 11 | jockey Ryan Sexton | trainer Julie Camacho (14d 1/13) | headgear h (1st time) | last run - days | form - | MARKET 3.4% | 09:00 median 26.00 | Matchbook 30.00
    DATA: model 8.7% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: First-time headgear
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Choir of Angels (hrs_17394300518) | 2yo F | 128lb | OR - | draw 1 | jockey Clifford Lee | trainer James Tate (14d 0/6) | headgear - | last run 23 days | form 0 | MARKET 2.7% | 09:00 median 23.00 | Matchbook 46.00
    DATA: model 8.1% | style Held up (led 8% of runs) | runs in data 1 | last 3: 4 Nov Kempton (AW) Flat 8f Standard / Slow 10/13 fig 36
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Jumeirah Pearl (hrs_66527440) | 2yo F | 128lb | OR - | draw 9 | jockey Marco Ghiani | trainer Ismail Mohammed & Jose Santos (14d 1/2) | headgear - | last run 51 days | form 0 | MARKET 1.5% | 09:00 median 51.00 | Matchbook 75.00
    DATA: model 10.2% | style Unknown | runs in data 1 | last 3: 7 Oct Kempton Flat 7f Standard To Slow 12/12
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Final Dash (hrs_17394900243) | 2yo F | 128lb | OR - | draw 8 | jockey George Wood | trainer James Fanshawe (14d 0/14) | headgear - | last run 23 days | form 0 | MARKET 1.4% | 09:00 median 67.00 | Matchbook 80.00
    DATA: model 6.5% | style Held up (led 8% of runs) | runs in data 1 | last 3: 4 Nov Kempton (AW) Flat 8f Standard / Slow 12/13 fig 28
    DATA against: Trainer 0 wins from 14 runs, last 14 days; Lightly raced: 1 run in our data, so the model has little to go on

## 4:45 Southwell (AW) | race_id rac_32305748371 | AWC Season 14 Has Begun EBF Fillies' Novice Stakes (Div II) (GBB/GBBPlus Race)
Flat | Class 3 | 1m13y | going Standard | AW | 11 runners | rating band - | age 2yo
DATA pace: Unclear - Running styles known for only 5 of 11 runners.
- Probing (hrs_17393092724) | 2yo F | 128lb | OR - | draw 4 | jockey Hector Crouch | trainer Ralph Beckett (14d 3/11) | headgear - | last run 48 days | form 2 | MARKET 55.1% | 09:00 median 1.50 | Matchbook 1.60
    DATA: model 26.9% | style Unknown | runs in data 1 | last 3: 10 Oct Newmarket Flat 7f Good 2/6
    DATA for: Trainer 27% wins (3/11), last 14 days; Last-run finishing speed +3.3% vs that field (finished strongly)
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- So This Is Love (hrs_17394744836) | 2yo F | 128lb | OR - | draw 6 | jockey Connor Planas | trainer Charlie Appleby (14d 5/10) | headgear p (1st time) | last run 27 days | form 6 | MARKET 12.3% | 09:00 median 6.50 | Matchbook 7.20
    DATA: model 13.9% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 31 Oct Newmarket Flat 7f Good To Soft 6/11 fig 66
    DATA for: Best recent form figure 66, 21 lb above field average; Trainer 50% wins (5/10), last 14 days; First-time headgear
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Fredegund (hrs_17396113252) | 2yo F | 128lb | OR - | draw 1 | jockey Robert Havlin | trainer John & Thady Gosden (14d 3/25) | headgear - | last run - days | form - | MARKET 7.9% | 09:00 median 9.00 | Matchbook 13.50
    DATA: model 7.3% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Forest Bay (hrs_17392817372) | 2yo F | 128lb | OR - | draw 9 | jockey Rhys Clutterbuck | trainer Ralph Beckett (14d 3/11) | headgear - | last run - days | form - | MARKET 7.2% | 09:00 median 10.00 | Matchbook 14.50
    DATA: model 7.3% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 27% wins (3/11), last 14 days
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Ever Flowing (hrs_17396112209) | 2yo F | 128lb | OR - | draw 10 | jockey Lewis Edmunds | trainer Harry Charlton (14d 0/4) | headgear - | last run - days | form - | MARKET 5.2% | 09:00 median 15.00 | Matchbook 18.50
    DATA: model 7.3% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Evara (hrs_17394899200) | 2yo F | 128lb | OR - | draw 11 | jockey Kieran Shoemark | trainer Ed Walker (14d 2/26) | headgear - | last run - days | form - | MARKET 4.8% | 09:00 median 17.00 | Matchbook 21.00
    DATA: model 7.3% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Lady Bb (hrs_17394557096) | 2yo F | 128lb | OR - | draw 8 | jockey Cieren Fallon | trainer William Haggas (14d 4/26) | headgear - | last run 30 days | form 7 | MARKET 2.3% | 09:00 median 29.00 | Matchbook 50.00
    DATA: model 7.0% | style Held up (led 8% of runs) | runs in data 1 | last 3: 28 Oct Nottingham Flat 8.5f Soft 7/9 fig 28
    DATA against: Best recent form figure 28, 17 lb below field average; Lightly raced: 1 run in our data, so the model has little to go on
- Accoya (hrs_17394299475) | 2yo F | 128lb | OR - | draw 2 | jockey Sean Levey | trainer Richard Hannon (14d 2/15) | headgear - | last run 23 days | form 9 | MARKET 1.7% | 09:00 median 34.00 | Matchbook 100.00
    DATA: model 6.3% | style Held up (led 8% of runs) | runs in data 1 | last 3: 4 Nov Kempton (AW) Flat 8f Standard / Slow 9/12 fig 38
    DATA against: Best recent form figure 38, 7 lb below field average; Lightly raced: 1 run in our data, so the model has little to go on
- Princess Aurelia (hrs_17394903372) | 2yo F | 128lb | OR - | draw 5 | jockey Callum Shepherd | trainer Jonjo & A.J. O'Neill (14d 4/33) | headgear - | last run 23 days | form 6 | MARKET 1.4% | 09:00 median 51.00 | Matchbook 100.00
    DATA: model 4.6% | style Held up (led 8% of runs) | runs in data 1 | last 3: 4 Nov Kempton (AW) Flat 8f Standard / Slow 6/12 fig 52
    DATA for: Best recent form figure 52, 7 lb above field average
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Moon In Matera (hrs_17396115338) | 2yo F | 128lb | OR - | draw 7 | jockey Daniel Muscutt | trainer James Horton (14d 0/8) | headgear - | last run - days | form - | MARKET 1.3% | 09:00 median 51.00 | Matchbook 140.00
    DATA: model 7.3% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Trainer 0 wins from 8 runs, last 14 days; Lightly raced: 0 runs in our data, so the model has little to go on
- Graceful Gracie (hrs_17394842878) | 2yo F | 128lb | OR - | draw 3 | jockey Luke Morris | trainer Mark Loughnane (14d 2/22) | headgear - | last run 11 days | form 66 | MARKET 0.7% | 09:00 median 101.00 | Matchbook 200.00
    DATA: model 4.9% | style Held up (led 8% of runs) | runs in data 2 | last 3: 3 Nov Wolverhampton (AW) Flat 7f Standard 6/11 fig 30; 16 Nov Wolverhampton (AW) Flat 8.5f Standard 6/9 fig 41
    DATA against: Best recent form figure 41, 4 lb below field average; Lightly raced: 2 runs in our data, so the model has little to go on

## 5:15 Southwell (AW) | race_id rac_32305750308 | AWC Finals Day At Newcastle 26th March EBF Novice Stakes (GBB Race)
Flat | Class 3 | 7f14y | going Standard | AW | 9 runners | rating band - | age 2yo
DATA pace: Unclear - Running styles known for only 4 of 9 runners.
- Ezz Al Leith (hrs_17396122639) | 2yo G | 133lb | OR - | draw 4 | jockey Clifford Lee | trainer K. R. Burke (14d 0/11) | headgear - | last run - days | form - | MARKET 26.6% | 09:00 median 3.25 | Matchbook 3.50 | CHECK (skip line 3.09)
    DATA: model 8.1% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Trainer 0 wins from 11 runs, last 14 days; Lightly raced: 0 runs in our data, so the model has little to go on
- Flick of An Eye (hrs_17390534245) | 2yo G | 133lb | OR 81 | draw 1 | jockey Callum Shepherd | trainer Simon Crisford (14d 5/10) | headgear p (1st time) | last run 34 days | form 342 | MARKET 21.1% | 09:00 median 4.00 | Matchbook 4.50
    DATA: model 36.7% | style Held up (led 5% of runs) | runs in data 3 | last 3: 26 Aug Newbury Flat 6.5f Good To Firm 3/10; 15 Sep Yarmouth Flat 6f Good To Soft 4/6; 24 Oct Southwell (AW) Flat 6f Standard 2/7 fig 69
    DATA for: Best recent form figure 69, 17 lb above field average; Trainer 50% wins (5/10), last 14 days; Good recent finishing positions; First-time headgear
- Kite Beach (hrs_17396124725) | 2yo C | 133lb | OR - | draw 6 | jockey Robert Havlin | trainer John & Thady Gosden (14d 3/25) | headgear p (1st time) | last run - days | form - | MARKET 12.7% | 09:00 median 6.50 | Matchbook 7.60
    DATA: model 8.1% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: First-time headgear
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Georges (hrs_17396123682) | 2yo C | 133lb | OR - | draw 9 | jockey Callum Rodriguez | trainer Owen Burrows (14d 2/6) | headgear - | last run - days | form - | MARKET 11.2% | 09:00 median 7.50 | Matchbook 8.80
    DATA: model 8.1% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 33% wins (2/6), last 14 days
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Baysline (hrs_17394654095) | 2yo C | 133lb | OR - | draw 8 | jockey Cieren Fallon | trainer Hugo Palmer (14d 0/3) | headgear - | last run 28 days | form 6 | MARKET 9.4% | 09:00 median 9.00 | Matchbook 10.50
    DATA: model 13.1% | style Held up (led 8% of runs) | runs in data 1 | last 3: 30 Oct Newmarket Flat 7f Good To Soft 6/10 fig 40
    DATA against: Best recent form figure 40, 12 lb below field average; Lightly raced: 1 run in our data, so the model has little to go on
- Barbossa (hrs_17396120553) | 2yo C | 133lb | OR - | draw 3 | jockey Lewis Edmunds | trainer Harry Charlton (14d 0/4) | headgear - | last run - days | form - | MARKET 5.1% | 09:00 median 17.00 | Matchbook 20.00
    DATA: model 8.1% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Turbo Charger (hrs_62168288) | 2yo C | 133lb | OR - | draw 7 | jockey Kieran Shoemark | trainer Charles Hills (14d 0/3) | headgear - | last run 32 days | form 05 | MARKET 5.1% | 09:00 median 17.00 | Matchbook 19.50
    DATA: model 3.7% | style Held up (led 5% of runs) | runs in data 2 | last 3: 1 Oct Salisbury Flat 7f Soft 10/12; 26 Oct Kempton (AW) Flat 7f Standard / Slow 5/9 fig 48
    DATA against: Best recent form figure 48, 4 lb below field average; Lightly raced: 2 runs in our data, so the model has little to go on
- Kokoro (hrs_17395643902) | 2yo C | 133lb | OR - | draw 5 | jockey Oisin Orr | trainer Edward Bethell (14d 0/13) | headgear - | last run - days | form - | MARKET 4.6% | 09:00 median 17.00 | Matchbook 25.00
    DATA: model 8.1% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Trainer 0 wins from 13 runs, last 14 days; Lightly raced: 0 runs in our data, so the model has little to go on
- Cites (hrs_17391375946) | 2yo C | 133lb | OR - | draw 2 | jockey Hector Crouch | trainer Ralph Beckett (14d 3/11) | headgear - | last run 80 days | form 69 | MARKET 4.1% | 09:00 median 23.00 | Matchbook 23.00
    DATA: model 6.1% | style Midfield (led 8% of runs) | runs in data 2 | last 3: 26 Aug Kempton Flat 8f Standard To Slow 6/8; 8 Sep Leicester Flat 7f Good To Soft 9/9
    DATA for: Trainer 27% wins (3/11), last 14 days
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on

## 5:45 Southwell (AW) | race_id rac_32305752245 | Midnite: Built For 2026 Not 2006 Selling Stakes
Flat | Class 4 | 6f16y | going Standard | AW | 6 runners | rating band - | age 3yo+
DATA pace: Lone leader - Blackjack is the only habitual front-runner and may be allowed an easy lead.
- Purosangue (hrs_35828205) | 5yo G | 130lb | OR 85 | draw 6 | jockey Marco Ghiani | trainer Robert Cowell (14d 1/9) | headgear p | last run 3 days | form 589952 | MARKET 53.5% | 09:00 median 1.67 | Matchbook 1.79
    comment: Purosangue arrives in his best form, a second last time out just three days ago, and he has run over today's trip and going before.
    DATA: model 32.7% | style Prominent (led 5% of runs) | runs in data 8 | last 3: 17 Sep Yarmouth Flat 6f Good 9/9; 19 Oct Wolverhampton (AW) Flat 6f Standard 5/12 fig 85; 24 Nov Wolverhampton (AW) Flat 6f Standard 2/9 fig 86
    DATA for: Best recent form figure 86, 12 lb above field average; Official rating 85, 8 lb above field average
- Moving Force (hrs_39960340) | 4yo G | 130lb | OR 80 | draw 5 | jockey Daniel Muscutt | trainer Mark Loughnane (14d 2/22) | headgear - | last run 24 days | form 723365 | MARKET 17.6% | 09:00 median 5.20 | Matchbook 5.50
    DATA: model 21.5% | style Midfield (led 4% of runs) | runs in data 9 | last 3: 5 Oct Kempton Flat 6f Standard To Slow 3/10; 22 Oct Southwell (AW) Flat 6f Standard 6/10 fig 76; 3 Nov Wolverhampton (AW) Flat 6f Standard 5/12 fig 77
    DATA for: Last-run finishing speed +2.3% vs that field (finished strongly)
- Betsen (hrs_35040019) | 5yo G | 133lb | OR 82 | draw 1 | jockey Myla Coppins(5) | trainer Tony Carroll (14d 2/39) | headgear - | last run 11 days | form 853980 | MARKET 11.4% | 09:00 median 7.50 | Matchbook 8.80
    comment: The main risk is a yard struggling, at 2/39 in the last 14 days.
    DATA: model 14.8% | style Midfield (led 3% of runs) | runs in data 14 | last 3: 19 Sep Chester Flat 5.1f Heavy 9/11; 24 Oct Southwell (AW) Flat 5f Standard 8/12 fig 76; 16 Nov Wolverhampton (AW) Flat 5f Standard 11/11 fig 70
    DATA against: Poor recent finishing positions
- Bassenthwaite (hrs_52641386) | 3yo G | 130lb | OR 84 | draw 4 | jockey Callum Shepherd | trainer Mike Murphy (14d 0/2) | headgear - | last run 62 days | form 1-0904 | MARKET 8.5% | 09:00 median 9.50 | Matchbook 13.00
    comment: The main risk is a 62-day absence, with just one win in his last five starts and a victory five starts back.
    DATA: model 14.2% | style Midfield (led 4% of runs) | runs in data 4 | last 3: 22 Jun Windsor Flat 5.1f Good To Firm 9/9; 25 Jul Ascot Flat 5f Good To Firm 10/13; 26 Sep Southwell Flat 5f Standard 4/10
    DATA for: Official rating 84, 7 lb above field average
- Buzz Box (hrs_36416485) | 5yo G | 130lb | OR 73 | draw 2 | jockey Jason Hart | trainer Michael Herrington (14d 0/4) | headgear - | wind surgery | last run 99 days | form 1-4970 | MARKET 6.6% | 09:00 median 13.00 | Matchbook 15.00
    comment: Buzz Box is hard to fancy, unplaced last time out and a seventh and a ninth in the two runs before, with his only win five starts back and 99 days off since.
    DATA: model 6.8% | style Prominent (led 8% of runs) | runs in data 4 | last 3: 5 Jul Southwell Flat 5f Standard 9/9; 30 Jul Wolverhampton Flat 6.1f Standard 7/11; 20 Aug Newcastle Flat 5f Standard 10/13
    DATA against: Poor recent finishing positions; Returns from a 99-day break
- Blackjack (hrs_27794781) | 9yo G | 133lb | OR 59 | draw 3 | jockey Rowan Scott | trainer Alan Brown (14d 0/3) | headgear b | last run 20 days | form 303921 | MARKET 2.3% | 09:00 median 41.00 | Matchbook 48.00
    comment: He has run over today's trip and going, but a ninth three starts back shows his inconsistency, and 133 lb from draw 3 offers little leeway.
    DATA: model 9.9% | style Leader (led 23% of runs) | runs in data 12 | last 3: 17 Sep Southwell Flat 6.1f Standard 9/13; 29 Oct Southwell (AW) Flat 7f Standard 2/13 fig 59; 7 Nov Southwell (AW) Flat 6f Standard 1/11 fig 56
    DATA for: Has won at this trip or further; Good recent finishing positions; Pace: may get an uncontested lead
    DATA against: Best recent form figure 59, 16 lb below field average; Official rating 59, 18 lb below field average; Aged 9, older than most of this field

## 6:15 Southwell (AW) | race_id rac_32305754182 | Midnite Ain't Your Grandad's Bookie Handicap Stakes
Flat | Class 6 | 2m102y | going Standard | AW | 13 runners | rating band 0-60 | age 3yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Saxophonic (hrs_55947675) | 3yo G | 135lb | OR 59 | draw 8 | jockey Rowan Scott | trainer David Simcock (14d 2/13) | headgear - | last run 11 days | form 441314 | MARKET 32.8% | 09:00 median 2.50 | Matchbook 2.64
    comment: Saxophonic arrives fit, just 11 days since a fourth last time out, and he's a winner two starts back and four starts back, so two wins in his last six marks him out.
    DATA: model 26.8% | style Midfield (led 3% of runs) | runs in data 9 | last 3: 3 Oct Southwell Flat 16.5f Standard 3/6; 3 Nov Wolverhampton (AW) Flat 12f Standard 1/11 fig 63; 16 Nov Wolverhampton (AW) Flat 12f Standard 4/11 fig 55
    DATA for: Best recent form figure 63, 17 lb above field average; Recent figures 4 lb above its current mark (looks well handicapped); Official rating 59, 7 lb above field average; Good recent finishing positions
- Zephlyn (hrs_30514841) | 7yo G | 134lb | OR 52 | draw 14 | jockey Jason Hart | trainer Ewan Whillans (14d 0/5) | headgear tp | last run 20 days | form 936567 | MARKET 9.6% | 09:00 median 8.50 | Matchbook 9.00
    comment: Zephlyn is yet to win in his last six, with a seventh last time out and a third five starts back his best finish in that run, though he has run over today's trip and going and is fresh enough after 20 days.
    DATA: model 6.3% | style Prominent (led 5% of runs) | runs in data 11 | last 3: 26 Aug Catterick Flat 13.9f Good 7/8; 24 Sep Perth Hurdle 20.2f Good 6/12; 7 Nov Kelso Hurdle 21f Good 5/11 fig 95
- Charlie Darling (hrs_32277224) | 6yo G | 140lb | OR 58 | draw 1 | jockey Tom Eaves | trainer Alan Brown (14d 0/3) | headgear - | last run 23 days | form 168050 | MARKET 8.9% | 09:00 median 8.50 | Matchbook 11.00
    comment: The risk is a form line that has tailed off since his win six starts back, with nothing better than a fifth since.
    DATA: model 6.3% | style Midfield (led 3% of runs) | runs in data 10 | last 3: 16 Oct Newcastle (AW) Flat 12.5f Standard 10/12 fig 50; 29 Oct Southwell (AW) Flat 14f Standard 5/12 fig 58; 4 Nov Musselburgh Flat 16f Soft 10/11
    DATA for: Best recent form figure 58, 12 lb above field average; Official rating 58, 6 lb above field average; Has won at this trip or further
    DATA against: Carries 7 lb more than average
- Storm On Jura (hrs_42452067) | 4yo F | 136lb | OR 54 | draw 3 | jockey Lauren Young(5) | trainer Jim Goldie (14d 1/17) | headgear - | last run 23 days | form 882215 | MARKET 8.0% | 09:00 median 9.00 | Matchbook 12.00
    comment: Storm On Jura signed off with a fifth last time out, after a win two starts back and seconds three and four starts back, so her recent form is solid, and she has run over today's trip. A weight of 136 lb off a mark of 54 and a 23-day break leave her little margin.
    DATA: model 16.3% | style Held up (led 8% of runs) | runs in data 12 | last 3: 28 Sep Hamilton Flat 12.1f Soft 2/10; 12 Oct Musselburgh Flat 16f Good To Soft 1/8; 4 Nov Musselburgh Flat 16f Soft 5/11 fig 45
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Recent figures 9 lb below its current mark (looks high in the weights); Pace: steady gallop likely, hard to come from off the pace
- Dollar's Dream (hrs_51244340) | 5yo G | 136lb | OR 54 | draw 6 | jockey Kevin Stott | trainer Philip Kirby (14d 1/13) | headgear p | last run 20 days | form 254200 | MARKET 6.8% | 09:00 median 11.00 | Matchbook 15.00
    comment: Dollar's Dream was unplaced in his last two outings but was second three starts back, and he has run over today's trip and going before.
    DATA: model 6.1% | style Prominent (led 23% of runs) | runs in data 7 | last 3: 7 May Southwell Flat 16.5f Standard 2/9; 22 Oct Southwell (AW) Flat 14f Standard 10/12 fig 41; 7 Nov Southwell (AW) Flat 16.5f Standard 10/10 fig 40
    DATA against: Best recent form figure 41, 5 lb below field average; Recent figures 13 lb below its current mark (looks high in the weights)
- Neddies Boy (hrs_28637623) | 8yo G | 129lb | OR 47 | draw 4 | jockey Shane Gray | trainer Daragh Bourke (14d 0/1) | headgear tp | last run 23 days | form 0-8627 | MARKET 6.2% | 09:00 median 13.00 | Matchbook 14.50
    comment: Neddies Boy is winless in his last five, finishing seventh last time out and well beaten in three of the four runs before that, so he is hard to fancy.
    DATA: model 5.7% | style Held up (led 4% of runs) | runs in data 4 | last 3: 3 Sep Newcastle Flat 12.4f Standard 6/9; 30 Sep Catterick Flat 15.9f Good 2/9; 4 Nov Musselburgh Flat 16f Soft 7/11 fig 33
    DATA against: Best recent form figure 33, 13 lb below field average; Recent figures 14 lb below its current mark (looks high in the weights); Official rating 47, 5 lb below field average; Pace: steady gallop likely, hard to come from off the pace
- Choir Boy (hrs_57503887) | 3yo C | 133lb | OR 57 | draw 13 | jockey Cam Hardie | trainer Antony Brittain (14d 2/16) | headgear v | last run 25 days | form 5-4765 | MARKET 5.1% | 09:00 median 15.00 | Matchbook 18.50
    comment: The risk is a winless run, with a fourth four starts back the best of his last five.
    DATA: model 5.1% | style Prominent (led 29% of runs) | runs in data 4 | last 3: 17 Aug Wolverhampton Flat 12.2f Standard 7/10; 3 Sep Southwell Flat 12.1f Standard 6/7; 2 Nov Wolverhampton (AW) Flat 14f Standard 5/9 fig 48
    DATA for: Official rating 57, 5 lb above field average
    DATA against: Recent figures 9 lb below its current mark (looks high in the weights)
- Someone's Wish (hrs_36192471) | 6yo G | 128lb | OR 46 | draw 2 | jockey Paddy Bradley | trainer Patrick Morris (14d 0/15) | headgear p | last run 20 days | form 029464 | MARKET 4.9% | 09:00 median 15.00 | Matchbook 20.00
    comment: Someone's Wish is yet to win in his last six starts but arrives in fair order, fourth last time out and fresh from a 20-day break, having run over today's trip and going.
    DATA: model 3.9% | style Held up (led 4% of runs) | runs in data 10 | last 3: 27 Sep Ffos Las Flat 10f Soft 4/5; 19 Oct Southwell (AW) Flat 11f Standard 6/9 fig 38; 7 Nov Southwell (AW) Flat 12f Standard 4/10 fig 46
    DATA for: Carries 5 lb less than average
    DATA against: Official rating 46, 6 lb below field average; Trainer 0 wins from 15 runs, last 14 days; Pace: steady gallop likely, hard to come from off the pace
- Bodygroove (hrs_32500069) | 6yo G | 130lb | OR 48 | draw 5 | jockey Aiden Brookes | trainer Micky Hammond & Becky Smith (14d 1/18) | headgear p | last run 31 days | form 5686-3 | MARKET 4.5% | 09:00 median 17.00 | Matchbook 21.00
    comment: Bodygroove arrives on an upswing after a third last time out, following a run of sixth, eighth, sixth and fifth, and he has run over today's trip and going.
    DATA: model 5.6% | style Held up (led 4% of runs) | runs in data 5 | last 3: 14 Sep Sedgefield Hurdle 19.9f Good 10/10; 5 Oct Pontefract Flat 18f Good 3/6; 27 Oct Newcastle Hurdle 17f Good 6/10 fig 76
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Star of Jupiter (hrs_45568509) | 5yo G | 127lb | OR 44 | draw 7 | jockey Luke Morris | trainer Mark Loughnane (14d 2/22) | headgear tv | last run 39 days | form 425445 | MARKET 4.5% | 09:00 median 17.00 | Matchbook 23.00
    comment: His one real positive is a second five starts back, and he has run over today's trip and going.
    DATA: model 8.2% | style Held up (led 3% of runs) | runs in data 9 | last 3: 30 Sep Catterick Flat 15.9f Good 4/9; 8 Oct Bath Flat 17.1f Good 4/12; 19 Oct Bath Flat 17f Good To Soft 5/11 fig 37
    DATA for: Last-run finishing speed +2.9% vs that field (finished strongly); Carries 6 lb less than average
    DATA against: Best recent form figure 37, 9 lb below field average; Recent figures 7 lb below its current mark (looks high in the weights); Official rating 44, 8 lb below field average; Pace: steady gallop likely, hard to come from off the pace
- Fashionelle (hrs_33729864) | 7yo M | 134lb | OR 52 | draw 11 | jockey Gina Mangan | trainer Tony Forbes (14d 0/0) | headgear p | last run 213 days | form 23-768 | MARKET 3.1% | 09:00 median 26.00 | Matchbook 32.00
    comment: Fashionelle has been fading lately, with an eighth last time out and a sixth and a seventh before that, and she returns after 213 days off.
    DATA: model 4.9% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 31 Mar Wolverhampton Flat 14f Standard 7/10; 15 Apr Southwell Flat 14.1f Standard 6/8; 28 Apr Southwell Flat 16.5f Standard 8/11
    DATA against: Poor recent finishing positions; Returns from a 213-day break
- Angelardo (hrs_53602024) | 4yo G | 130lb | OR 48 | draw 10 | jockey Billy Garritty | trainer Liam Bailey (14d 0/2) | headgear - | last run 161 days | form 848248 | MARKET 3.1% | 09:00 median 26.00 | Matchbook 32.00
    comment: In his favour, he has run over today's trip and going, and a second three starts back shows he can get involved.
    DATA: model 3.4% | style Midfield (led 3% of runs) | runs in data 9 | last 3: 19 May Newcastle Flat 16.3f Standard 2/7; 8 Jun Pontefract Flat 17.1f Good 4/12; 19 Jun Ayr Flat 15f Soft 8/8
    DATA for: Has won at this trip or further
    DATA against: Last-run finishing speed -10.3% vs that field (faded); Returns from a 161-day break
- Katana (hrs_40553604) | 6yo G | 139lb | OR 57 | draw 9 | jockey William Carson | trainer Robert Stephens (14d 0/4) | headgear - | last run 25 days | form 789 | MARKET 2.4% | 09:00 median 26.00 | Matchbook 50.00
    comment: He has run on today's going before and had a 25-day break, but 139 lb is a lot to carry for a 57-rated gelding.
    DATA: model 1.4% | style Held up (led 4% of runs) | runs in data 5 | last 3: 5 Oct Kempton Flat 12f Standard To Slow 7/7; 26 Oct Kempton (AW) Flat 12f Standard / Slow 8/9 fig 47; 2 Nov Wolverhampton (AW) Flat 9.5f Standard 9/10 fig 36
    DATA for: Official rating 57, 5 lb above field average
    DATA against: Recent figures 10 lb below its current mark (looks high in the weights); Poor recent finishing positions; Carries 6 lb more than average; Pace: steady gallop likely, hard to come from off the pace

## 6:45 Southwell (AW) | race_id rac_32306095094 | Midnite A Next Generation Betting App Amateur Jockeys' Handicap Stakes
Flat | Class 6 | 1m4f14y | going Standard | AW | 14 runners | rating band 0-65 | age 3yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Spec of Light (hrs_47162038) | 4yo G | 153lb | OR 62 | draw 6 | jockey Mr Cameron Hillhouse(5) | trainer Tony Forbes (14d 0/0) | headgear - | last run 39 days | form 884311 | MARKET 14.4% | 09:00 median 5.50 | Matchbook 6.40 | CHECK (skip line 5.22)
    DATA: model 15.3% | style Midfield (led 4% of runs) | runs in data 11 | last 3: 17 Sep Southwell Flat 11.1f Standard 3/9; 6 Oct Southwell Flat 11.1f Standard 1/9; 19 Oct Southwell (AW) Flat 11f Standard 1/9 fig 63
    DATA for: Last-run finishing speed +2.4% vs that field (finished strongly); Good recent finishing positions
- Off Spin (hrs_44199232) | 4yo G | 154lb | OR 63 | draw 8 | jockey Miss Brodie Hampson | trainer Gay Kelleway (14d 0/5) | headgear t | last run 6 days | form 251513 | MARKET 13.8% | 09:00 median 5.50 | Matchbook 6.80
    comment: Off Spin arrives in solid nick, third last time out and a winner two starts back, with two wins in his last six and only six days since his latest run, though he has run over today's trip and going before without that guaranteeing more.
    DATA: model 11.5% | style Held up (led 3% of runs) | runs in data 14 | last 3: 8 Oct Ayr Flat 13.1f Heavy 5/5; 4 Nov Musselburgh Flat 12.5f Soft 1/10 fig 66; 21 Nov Lingfield (AW) Flat 12f Standard 3/12 fig 64
    DATA for: Best recent form figure 66, 7 lb above field average; Last-run finishing speed +2.9% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Urban Road (hrs_28221466) | 7yo G | 153lb | OR 62 | draw 9 | jockey Mr Simon Walker | trainer Alan Brown (14d 0/3) | headgear v | last run 7 days | form 009777 | MARKET 10.4% | 09:00 median 8.00 | Matchbook 8.40
    comment: The risk is plain: he is winless in his last six and carries a hefty 153 lb.
    DATA: model 6.3% | style Held up (led 3% of runs) | runs in data 15 | last 3: 16 Oct Newcastle (AW) Flat 8f Standard 7/9 fig 58; 30 Oct Newcastle (AW) Flat 10f Standard 7/14 fig 58; 20 Nov Wolverhampton (AW) Flat 9.5f Standard 7/12 fig 58
    DATA against: Poor recent finishing positions; Pace: steady gallop likely, hard to come from off the pace
- Deep Sleep (hrs_55484569) | 3yo G | 148lb | OR 62 | draw 11 | jockey Miss Ruby Criscuolo(5) | trainer James Owen (14d 4/47) | headgear - | last run 25 days | form 708531 | MARKET 10.2% | 09:00 median 7.50 | Matchbook 9.20
    comment: He has run on today's going before.
    DATA: model 9.8% | style Prominent (led 5% of runs) | runs in data 9 | last 3: 15 Oct Brighton Flat 10f Good 5/11 fig 58; 23 Oct Wolverhampton (AW) Flat 9.5f Standard 3/10 fig 59; 2 Nov Wolverhampton (AW) Flat 9.5f Standard 1/12 fig 62
    DATA for: Good recent finishing positions
- Five Moons (hrs_59862551) | 3yo F | 147lb | OR 61 | draw 13 | jockey Mr Eireann Cagney | trainer Simon Crisford (14d 5/10) | headgear p | last run 36 days | form 446036 | MARKET 9.7% | 09:00 median 8.00 | Matchbook 9.40
    comment: Winless in her last six, Five Moons was sixth last time out, though she was third two starts back and has run over today's trip and going before.
    DATA: model 4.1% | style Midfield (led 3% of runs) | runs in data 7 | last 3: 27 Jul Southwell Flat 11.1f Standard 13/14; 12 Oct Yarmouth Flat 14.1f Good To Soft 3/11; 22 Oct Southwell (AW) Flat 14f Standard 6/12 fig 60
    DATA for: Trainer 50% wins (5/10), last 14 days; Last-run finishing speed +2.3% vs that field (finished strongly)
- It's A Love Thing (hrs_23264549) | 8yo G | 151lb | OR 56 | draw 3 | jockey Mr Lucas Murphy(3) | trainer Sam England (14d 6/29) | headgear - | last run 11 days | form 083241 | MARKET 7.2% | 09:00 median 11.00 | Matchbook 12.50
    comment: Fresh from a win last time out and just 11 days ago, he's had a fourth two starts back and a second three starts back before that, and has run over today's trip and going before.
    DATA: model 11.0% | style Prominent (led 4% of runs) | runs in data 9 | last 3: 29 Sep Wolverhampton Flat 9.5f Standard 2/13; 23 Oct Wolverhampton (AW) Flat 9.5f Standard 4/10 fig 55; 16 Nov Wolverhampton (AW) Flat 12f Standard 1/11 fig 55
    DATA for: Trainer 21% wins (6/29), last 14 days; Has won at this trip or further; Good recent finishing positions
    DATA against: Best recent form figure 55, 4 lb below field average; Official rating 56, 5 lb below field average
- King Chaos (hrs_44264423) | 5yo G | 152lb | OR 61 | draw 5 | jockey Mr Thomas Easterby(3) | trainer Rebecca Menzies (14d 0/10) | headgear p | last run 7 days | form 178004 | MARKET 6.9% | 09:00 median 11.00 | Matchbook 14.00
    comment: King Chaos was a fourth last time out and has run over today's trip and going, but he's been unplaced in two of the starts before that and his last win came six starts back.
    DATA: model 4.9% | style Held up (led 5% of runs) | runs in data 6 | last 3: 10 Aug Ayr Flat 10f Good To Soft 10/12; 29 Oct Southwell (AW) Flat 11f Standard 10/10 fig 52; 20 Nov Wolverhampton (AW) Flat 9.5f Standard 4/12 fig 60
    DATA for: Last-run finishing speed +2.5% vs that field (finished strongly); Has won at this trip or further
    DATA against: Trainer 0 wins from 10 runs, last 14 days; Pace: steady gallop likely, hard to come from off the pace
- Bint Al Daar (hrs_31550491) | 6yo M | 154lb | OR 63 | draw 12 | jockey Mr Lewis Kent(3) | trainer Kevin & Lauren Frost (14d 1/13) | headgear v | last run 24 days | form 904874 | MARKET 6.6% | 09:00 median 11.00 | Matchbook 15.00
    comment: Bint Al Daar comes here fit after a fourth last time out 24 days ago, and she has run over today's trip and on the going before.
    DATA: model 4.1% | style Held up (led 3% of runs) | runs in data 12 | last 3: 23 Sep Goodwood Flat 14f Good 8/8; 22 Oct Southwell (AW) Flat 11f Standard 7/11 fig 61; 3 Nov Wolverhampton (AW) Flat 12f Standard 4/7 fig 58
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Light Speed (hrs_31451378) | 6yo G | 156lb | OR 65 | draw 14 | jockey Miss Charli Parker(3) | trainer Ruth Carr (14d 3/12) | headgear - | last run 29 days | form 94-605 | MARKET 5.7% | 09:00 median 13.00 | Matchbook 17.50
    comment: The risk is that he is winless in his last five and carries 156 lb.
    DATA: model 4.3% | style Prominent (led 5% of runs) | runs in data 3 | last 3: 22 Sep Beverley Flat 7.3f Good 6/9; 15 Oct Southwell (AW) Flat 8f Standard 10/11 fig 53; 29 Oct Southwell (AW) Flat 11f Standard 5/10 fig 61
    DATA for: Trainer 25% wins (3/12), last 14 days
- No Ordinary Joe (hrs_21229215) | 10yo G | 155lb | OR 64 | draw 7 | jockey Mr Louis Burke(7) | trainer Robert Stephens (14d 0/4) | headgear tp | last run 14 days | form 94442 | MARKET 5.5% | 09:00 median 13.00 | Matchbook 18.50
    comment: Fit after 14 days off, he must carry 155 lb from an official mark of 64.
    DATA: model 5.3% | style Midfield (led 4% of runs) | runs in data 15 | last 3: 11 Oct Chepstow Hurdle 16.1f Good To Soft 5/8; 26 Oct Kempton (AW) Flat 16f Standard / Slow 2/12 fig 62; 13 Nov Cheltenham Hurdle 21f Good 14/18 fig 113
    DATA against: Aged 10, older than most of this field
- Ocean Heights (hrs_24311434) | 9yo G | 148lb | OR 57 | draw 10 | jockey Mr Jack Pipe(7) | trainer David Pipe (14d 2/14) | headgear tp | last run 17 days | form 5-7744 | MARKET 3.6% | 09:00 median 21.00 | Matchbook 29.00
    comment: Back-to-back fourths last time out and two starts back suggest Ocean Heights is edging closer, and he has run over today's trip and going before after a 17-day break.
    DATA: model 7.8% | style Prominent (led 3% of runs) | runs in data 11 | last 3: 18 Sep Newton Abbot Hurdle 16.8f Good 4/11; 19 Oct Bath Flat 17f Good To Soft 4/11 fig 53; 10 Nov Huntingdon Hurdle 20.5f Good 2/5 fig 92
    DATA against: Best recent form figure 53, 6 lb below field average
- Sisterandbrother (hrs_24734906) | 8yo G | 155lb | OR 64 | draw 2 | jockey Miss Stephanie Dorey(5) | trainer Joey Ramsden (14d 0/6) | headgear - | last run 20 days | form 717729 | MARKET 2.4% | 09:00 median 29.00 | Matchbook 44.00
    comment: Sisterandbrother was beaten into ninth last time out, though a second two starts back and a win five starts back show he can still deliver, and he has run over today's trip and going.
    DATA: model 6.3% | style Held up (led 3% of runs) | runs in data 15 | last 3: 6 Aug Southwell Flat 11.1f Standard 7/11; 8 Oct Southwell Flat 14.1f Standard 2/12; 7 Nov Southwell (AW) Flat 16.5f Standard 9/10 fig 50
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 50, 9 lb below field average; Recent figures 14 lb below its current mark (looks high in the weights); Pace: steady gallop likely, hard to come from off the pace
- Flamingo Rose (hrs_22634024) | 9yo M | 149lb | OR 58 | draw 4 | jockey Mr Morgan Tidman(7) | trainer Michael Wigham (14d 0/3) | headgear t | last run 30 days | form 18-538 | MARKET 1.9% | 09:00 median 34.00 | Matchbook 65.00
    comment: Beaten into eighth last time out, Flamingo Rose has a win five starts back but only a third two starts back since, and her 30-day break does little to help.
    DATA: model 5.9% | style Held up (led 4% of runs) | runs in data 3 | last 3: 18 Aug Lingfield Flat 15.8f Standard 5/7; 19 Oct Bath Flat 17f Good To Soft 3/11 fig 60; 28 Oct Nottingham Flat 10f Soft 8/15 fig 52
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Palazzo Persico (hrs_33789826) | 5yo G | 149lb | OR 58 | draw 1 | jockey Mr William Pearman(5) | trainer Tony Carroll (14d 2/39) | headgear - | last run 30 days | form 515360 | MARKET 1.6% | 09:00 median 41.00 | Matchbook 100.00
    comment: Palazzo Persico has been unplaced last time out and a sixth two starts back, with his lone win five starts back now a distant memory, while a stable going 2/39 and a 149 lb burden add to the doubts.
    DATA: model 3.5% | style Held up (led 5% of runs) | runs in data 13 | last 3: 21 Aug Salisbury Flat 8f Good 3/7; 17 Sep Southwell Flat 11.1f Standard 6/9; 28 Oct Nottingham Flat 10f Soft 15/15
    DATA for: Has won at this trip or further
    DATA against: Last-run finishing speed -8.1% vs that field (faded); Pace: steady gallop likely, hard to come from off the pace
