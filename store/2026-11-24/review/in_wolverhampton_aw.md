# Card review packet: Wolverhampton (AW), 2026-11-24

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
{"meeting": "wolverhampton_aw", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 4:30 Wolverhampton (AW) | race_id rac_32305413270 | Midnite It's Actually Pretty Good Apprentice Handicap Stakes
Flat | Class 6 | 6f20y | going Standard | AW | 13 runners | rating band 0-60 | age 3yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Mehmar (hrs_30208255) | 6yo G | 125lb | OR 50 | draw 3 | jockey Harry Vigors | trainer Jack Jones (14d 0/5) | headgear - | last run 31 days | form 857402 | MARKET 39.5% | 09:00 median 2.00 | Matchbook 2.24
    comment: Mehmar was second last time out and has run over today's trip and going, but he is yet to win in his last six starts, with a fourth three starts back his only other finish in the first four.
    DATA: model 10.3% | style Prominent (led 3% of runs) | runs in data 11 | last 3: 16 Jul Leopardstown Flat 7.2f Good 4/14; 22 Jul Naas Flat 8f Good 12/18; 24 Oct Southwell (AW) Flat 6f Standard 2/11 fig 58
    DATA for: Best recent form figure 58, 5 lb above field average; Recent figures 8 lb above its current mark (looks well handicapped)
- Black Missile (hrs_57041565) | 3yo G | 135lb | OR 60 | draw 4 | jockey Shay Farmer | trainer Julie Camacho (14d 1/9) | headgear v | last run 38 days | form 536632 | MARKET 11.3% | 09:00 median 6.50 | Matchbook 8.60
    comment: Black Missile bids to build on a second last time out, with a third five starts back among his better efforts, and he has run over today's trip and going before.
    DATA: model 17.4% | style Midfield (led 3% of runs) | runs in data 7 | last 3: 8 Sep Leicester Flat 5f Good To Soft 6/11; 22 Sep Beverley Flat 5f Good 3/6; 17 Oct Southwell (AW) Flat 6f Standard 2/12 fig 62
    DATA for: Best recent form figure 62, 9 lb above field average; Official rating 60, 7 lb above field average; Good recent finishing positions
    DATA against: Carries 7 lb more than average
- Daytona Lady (hrs_29945083) | 6yo M | 135lb | OR 60 | draw 13 | jockey Olivia Haines(3) | trainer Ruth Carr (14d 2/9) | headgear p | last run 22 days | form 853642 | MARKET 9.7% | 09:00 median 8.00 | Matchbook 9.40
    comment: Yet to win in her last six starts, she carries 135 lb from draw 13, and that lack of a win is the main risk.
    DATA: model 11.5% | style Midfield (led 4% of runs) | runs in data 15 | last 3: 6 Oct Southwell Flat 6.1f Standard 6/10; 19 Oct Southwell (AW) Flat 6f Standard 4/10 fig 63; 2 Nov Wolverhampton (AW) Flat 6f Standard 2/10 fig 60
    DATA for: Best recent form figure 63, 10 lb above field average; Official rating 60, 7 lb above field average; Trainer 22% wins (2/9), last 14 days; Has won at this trip or further
    DATA against: Carries 7 lb more than average
- Knicks (hrs_35730023) | 5yo G | 132lb | OR 57 | draw 8 | jockey Jake Dickson | trainer Michael & David Easterby (14d 1/6) | headgear - | last run 28 days | form 273044 | MARKET 8.2% | 09:00 median 10.00 | Matchbook 11.00
    comment: Knicks has been consistent, finishing fourth last time out and a fourth two starts back, and he has run over today's trip and going before.
    DATA: model 11.5% | style Held up (led 5% of runs) | runs in data 12 | last 3: 17 Sep Ayr Flat 5f Soft 13/20; 5 Oct Pontefract Flat 5f Good 4/12; 27 Oct Catterick Flat 6f Soft 4/10 fig 65
    DATA for: Best recent form figure 65, 12 lb above field average; Recent figures 8 lb above its current mark (looks well handicapped)
    DATA against: Pace: steady gallop likely, hard to come from off the pace; Course: hold-up horses have won 0.7× their fair share at 6f here
- Act of Violence (hrs_36454222) | 5yo G | 135lb | OR 60 | draw 9 | jockey Darragh O'Sullivan(3) | trainer Tony Carroll (14d 1/31) | headgear t | last run 26 days | form 132460 | MARKET 6.7% | 09:00 median 12.00 | Matchbook 13.50
    DATA: model 12.5% | style Prominent (led 4% of runs) | runs in data 8 | last 3: 21 Sep Leicester Flat 6f Good 4/12; 1 Oct Nottingham Flat 6.1f Good 6/15; 29 Oct Bath Flat 5f Soft 13/15 fig 52
    DATA for: Official rating 60, 7 lb above field average; Has won at this trip or further
    DATA against: Recent figures 8 lb below its current mark (looks high in the weights); Carries 7 lb more than average
- Forever Glamorous (hrs_54842711) | 3yo G | 131lb | OR 56 | draw 5 | jockey Alexandra Egan(3) | trainer Christopher Mason (14d 0/1) | headgear p | last run 88 days | form 235135 | MARKET 6.3% | 09:00 median 10.00 | Matchbook 18.00
    comment: On the plus side, he has run over today's trip and won three starts back.
    DATA: model 12.1% | style Held up (led 8% of runs) | runs in data 6 | last 3: 30 Jun Ffos Las Flat 5f Good 1/7; 27 Jul Windsor Flat 6.1f Good To Firm 3/6; 28 Aug Ffos Las Flat 5f Good To Soft 5/6
    DATA for: Good recent finishing positions
    DATA against: Pace: steady gallop likely, hard to come from off the pace; Course: hold-up horses have won 0.7× their fair share at 6f here
- Diligent Henry (hrs_36207647) | 5yo G | 121lb | OR 45 | draw 7 | jockey Molly Keegan-Price(5) | trainer Gemma Tutty (14d 0/4) | headgear b | last run 26 days | form 050567 | MARKET 5.5% | 09:00 median 13.00 | Matchbook 19.00
    comment: Diligent Henry is winless in his last six, finishing seventh last time out, and has not been closer than a fifth in that spell, so he is hard to fancy.
    DATA: model 4.1% | style Prominent (led 5% of runs) | runs in data 8 | last 3: 2 Jun Wolverhampton Flat 7.2f Standard 5/10; 21 Jun Pontefract Flat 6f Good 6/11; 29 Oct Southwell (AW) Flat 7f Standard 7/13 fig 41
    DATA for: Carries 7 lb less than average
    DATA against: Best recent form figure 41, 12 lb below field average; Official rating 45, 8 lb below field average
- Havana Club (hrs_42647878) | 4yo G | 129lb | OR 54 | draw 11 | jockey Donagh Murphy(3) | trainer Adrian Wintle (14d 0/3) | headgear - | last run 42 days | form 413883 | MARKET 3.2% | 09:00 median 19.00 | Matchbook 38.00
    comment: Havana Club was third last time out and has a win five starts back, but two eighths before that show his inconsistency, and 42 days off is a slight query.
    DATA: model 5.8% | style Midfield (led 4% of runs) | runs in data 12 | last 3: 2 Sep Bath Flat 8f Good 8/11; 29 Sep Bath Flat 8f Good To Firm 8/12; 13 Oct Wolverhampton Flat 7.2f Standard 3/9
    DATA for: Has won at this trip or further
- Goldenstateofmind (hrs_50434307) | 3yo G | 135lb | OR 60 | draw 6 | jockey Jude Maher(5) | trainer David Loughnane (14d 2/8) | headgear - | last run 125 days | form 6-7788 | MARKET 2.7% | 09:00 median 23.00 | Matchbook 46.00
    comment: Goldenstateofmind has been beaten in his last five, finishing eighth on each of his last two outings, and returns after 125 days off.
    DATA: model 2.8% | style Midfield (led 4% of runs) | runs in data 4 | last 3: 2 Jun Pontefract Flat 5f Good 7/7; 16 Jun Wolverhampton Flat 6.1f Standard 8/10; 22 Jul Leicester Flat 6f Good To Firm 8/8
    DATA for: Official rating 60, 7 lb above field average; Trainer 25% wins (2/8), last 14 days
    DATA against: Last-run finishing speed -9.0% vs that field (faded); Poor recent finishing positions; Carries 7 lb more than average; Returns from a 125-day break
- Megaphone (hrs_41325445) | 4yo G | 121lb | OR 45 | draw 1 | jockey Mikkel Mortensen | trainer Scott Dixon (14d 0/8) | headgear - | last run 22 days | form 095663 | MARKET 2.6% | 09:00 median 30.50 | Matchbook 44.00
    comment: Megaphone is winless in his last six, though a third last time out, 22 days ago, is a step up on a run of sixth, sixth and fifth before it.
    DATA: model 4.3% | style Prominent (led 23% of runs) | runs in data 10 | last 3: 17 Aug Wolverhampton Flat 5.1f Standard 6/9; 15 Oct Southwell (AW) Flat 7f Standard 6/11 fig 42; 2 Nov Wolverhampton (AW) Flat 6f Standard 3/10 fig 44
    DATA for: Carries 7 lb less than average
    DATA against: Best recent form figure 44, 9 lb below field average; Official rating 45, 8 lb below field average; Trainer 0 wins from 8 runs, last 14 days
- Papa Don't Preach (hrs_25156467) | 7yo G | 124lb | OR 49 | draw 10 | jockey Matthew Lloyd Slater(3) | trainer Kevin & Lauren Frost (14d 1/8) | headgear b | last run 31 days | form 326667 | MARKET 2.2% | 09:00 median 34.00 | Matchbook 50.00
    DATA: model 3.4% | style Held up (led 4% of runs) | runs in data 12 | last 3: 2 Sep Newcastle Flat 5f Standard 6/9; 15 Sep Wolverhampton Flat 6.1f Standard 6/12; 24 Oct Southwell (AW) Flat 6f Standard 7/11 fig 42
    DATA against: Best recent form figure 42, 11 lb below field average; Recent figures 7 lb below its current mark (looks high in the weights); Poor recent finishing positions; Pace: steady gallop likely, hard to come from off the pace; Course: hold-up horses have won 0.7× their fair share at 6f here
- Mister Moet (hrs_52117359) | 3yo G | 124lb | OR 49 | draw 2 | jockey Ethan Tindall | trainer Scott Dixon (14d 0/8) | headgear p | last run 21 days | form 790047 | MARKET 1.3% | 09:00 median 46.00 | Matchbook 120.00
    comment: Mister Moet is winless in his last six, with a seventh last time out and a fourth two starts back the best of a poor recent run, so he is hard to fancy.
    DATA: model 3.2% | style Midfield (led 3% of runs) | runs in data 19 | last 3: 29 Sep Wolverhampton Flat 6.1f Standard 11/11; 26 Oct Southwell (AW) Flat 5f Standard 4/10 fig 51; 3 Nov Wolverhampton (AW) Flat 5f Standard 7/9 fig 39
    DATA for: Has won at this trip or further
    DATA against: Trainer 0 wins from 8 runs, last 14 days
- Devil's Angel (hrs_13998796) | 10yo G | 121lb | OR 45 | draw 12 | jockey Hope Regan(5) | trainer Patrick Morris (14d 0/11) | headgear p | last run 75 days | form 740-00 | MARKET 0.7% | 09:00 median 86.00 | Matchbook 190.00
    comment: Winless in his last five and unplaced in his last three, Devil's Angel returns after 75 days off, though he has run over today's trip and going before.
    DATA: model 1.1% | style Held up (led 5% of runs) | runs in data 2 | last 3: 14 Jun Cork Flat 5f Good 10/10; 10 Sep Laytown Flat 6f Standard 10/10
    DATA for: Carries 7 lb less than average
    DATA against: Official rating 45, 8 lb below field average; Trainer 0 wins from 11 runs, last 14 days; Last-run finishing speed -3.9% vs that field (faded); Lightly raced: 2 runs in our data, so the model has little to go on; Aged 10, older than most of this field; Pace: steady gallop likely, hard to come from off the pace; Course: hold-up horses have won 0.7× their fair share at 6f here

## 5:00 Wolverhampton (AW) | race_id rac_32305415207 | Midnite Ain't Yourgrandad's Bookie EBF Novice Stakes (GBB Race)
Flat | Class 4 | 6f20y | going Standard | AW | 11 runners | rating band - | age 3yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Prosewriter (hrs_17394425678) | 3yo G | 137lb | OR - | draw 11 | jockey Hollie Doyle | trainer Archie Watson (14d 2/4) | headgear - | last run 29 days | form 1 | MARKET 41.0% | 09:00 median 2.00 | Matchbook 2.26
    DATA: model 25.8% | style Held up (led 8% of runs) | runs in data 1 | last 3: 26 Oct Southwell (AW) Flat 6f Standard 1/10 fig 58
    DATA for: Best recent form figure 58, 10 lb above field average; Last-run finishing speed +3.7% vs that field (finished strongly); Has won at this trip or further
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace; Course: hold-up horses have won 0.7× their fair share at 6f here
- Gombey Rhythm (hrs_17395932813) | 3yo F | 125lb | OR - | draw 6 | jockey Billy Loughnane | trainer George Scott (14d 0/2) | headgear - | last run - days | form - | MARKET 29.7% | 09:00 median 2.75 | Matchbook 3.15
    DATA: model 5.9% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Baandee (hrs_56873845) | 3yo F | 125lb | OR 74 | draw 9 | jockey George Wood | trainer Jack Morland (14d 0/4) | headgear b (1st time) | last run 19 days | form 22-222 | MARKET 13.0% | 09:00 median 6.50 | Matchbook 7.00
    DATA: model 22.0% | style Unknown | runs in data 3 | last 3: 12 Mar Chelmsford Flat 7f Standard 2/10; 30 Apr Yarmouth Flat 7f Good To Firm 2/6; 5 Nov Chelmsford (AW) Flat 7f Standard 2/5 fig 55
    DATA for: Best recent form figure 55, 8 lb above field average; Good recent finishing positions; First-time headgear
- Flag of Nations (hrs_17391569944) | 3yo G | 130lb | OR - | draw 5 | jockey Luke Morris | trainer William Muir & Chris Grassick (14d 0/5) | headgear - | last run 29 days | form 84 | MARKET 4.6% | 09:00 median 17.00 | Matchbook 24.00
    DATA: model 9.2% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 15 Sep Wolverhampton Flat 6.1f Standard 8/12; 26 Oct Southwell (AW) Flat 6f Standard 4/10 fig 52
    DATA for: Best recent form figure 52, 4 lb above field average
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Du Val (hrs_17395931770) | 3yo F | 125lb | OR - | draw 4 | jockey Laura Pearson | trainer David Loughnane (14d 2/8) | headgear - | last run - days | form - | MARKET 3.1% | 09:00 median 21.00 | Matchbook 55.00
    DATA: model 5.9% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 25% wins (2/8), last 14 days
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Nando Tornado (hrs_17394422549) | 3yo G | 130lb | OR - | draw 1 | jockey William Pyle | trainer David & Nicola Barron (14d 0/2) | headgear - | last run 17 days | form 66 | MARKET 2.4% | 09:00 median 29.00 | Matchbook 55.00
    DATA: model 6.0% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 26 Oct Southwell (AW) Flat 6f Standard 6/10 fig 48; 7 Nov Southwell (AW) Flat 5f Standard 6/9 fig 46
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Two Steps Twice (hrs_17395031661) | 3yo F | 125lb | OR - | draw 8 | jockey Mikkel Mortensen(5) | trainer Charlie Fellowes (14d 1/6) | headgear - | last run 19 days | form 3 | MARKET 2.3% | 09:00 median 34.00 | Matchbook 48.00
    DATA: model 6.0% | style Unknown | runs in data 1 | last 3: 5 Nov Chelmsford (AW) Flat 7f Standard 3/5 fig 44
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Another Croeso (hrs_17395930727) | 5yo G | 130lb | OR - | draw 10 | jockey Tom Kiely-Marshall(3) | trainer James Evans (14d 0/1) | headgear - | last run - days | form - | MARKET 1.1% | 09:00 median 67.00 | Matchbook 180.00
    DATA: model 6.0% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Arco Sancho (hrs_17391714921) | 3yo G | 130lb | OR - | draw 7 | jockey Elle-May Croot(5) | trainer Ivan Furtado (14d 1/11) | headgear - | wind surgery | last run 10 days | form - | MARKET 1.1% | 09:00 median 76.00 | Matchbook 140.00
    DATA: model 6.6% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 14 Nov Windsor NH Flat 16f Good 8/9 fig 87
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Byerley Lady (hrs_17392551407) | 4yo F | 125lb | OR - | draw 3 | jockey Clifford Lee | trainer Ian Williams (14d 3/19) | headgear h (1st time) | last run 33 days | form 77 | MARKET 0.9% | 09:00 median 81.00 | Matchbook 210.00
    DATA: model 2.6% | style Midfield (led 8% of runs) | runs in data 2 | last 3: 29 Sep Wolverhampton Flat 7.2f Standard 7/10; 22 Oct Southwell (AW) Flat 6f Standard 7/8 fig 28
    DATA for: First-time headgear
    DATA against: Best recent form figure 28, 20 lb below field average; Lightly raced: 2 runs in our data, so the model has little to go on
- Liblex Dream (hrs_17393403538) | 4yo F | 125lb | OR - | draw 2 | jockey Robbie Downey | trainer Ivan Furtado (14d 1/11) | headgear - | wind surgery | last run 11 days | form - | MARKET 0.8% | 09:00 median 101.00 | Matchbook 230.00
    DATA: model 4.1% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 13 Nov Southwell NH Flat 16f Good 7/7
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on

## 5:30 Wolverhampton (AW) | race_id rac_32305816166 | All Weather Championship Is Back EBF Maiden Stakes (Div I) (GBB/GBBPlus Race)
Flat | Class 3 | 1m142y | going Standard | AW | 9 runners | rating band - | age 2yo
DATA pace: Lone leader - Son of Vega is the only habitual front-runner and may be allowed an easy lead.
- Zajal (hrs_17394060628) | 2yo C | 133lb | OR - | draw 9 | jockey Billy Loughnane | trainer Charlie Appleby (14d 3/5) | headgear - | last run 32 days | form 2 | MARKET 52.4% | 09:00 median 1.60 | Matchbook 1.67
    DATA: model 27.0% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 23 Oct Doncaster Flat 8f Heavy 2/10 fig 89
    DATA for: Best recent form figure 89, 27 lb above field average; Trainer 60% wins (3/5), last 14 days
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Manitoba (hrs_17393792577) | 2yo C | 133lb | OR - | draw 5 | jockey Luke Catton(3) | trainer John & Thady Gosden (14d 2/19) | headgear - | last run 32 days | form 4 | MARKET 27.3% | 09:00 median 2.50 | Matchbook 3.85
    DATA: model 18.0% | style Unknown | runs in data 1 | last 3: 23 Oct Doncaster Flat 8f Heavy 4/10 fig 83
    DATA for: Best recent form figure 83, 21 lb above field average
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Manolin (hrs_17394061671) | 2yo C | 133lb | OR - | draw 1 | jockey Callum Hutchinson | trainer Andrew Balding (14d 2/27) | headgear - | last run 34 days | form 4 | MARKET 10.8% | 09:00 median 6.00 | Matchbook 10.50
    DATA: model 11.5% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 21 Oct Newmarket Flat 8f Soft 4/5 fig 69
    DATA for: Best recent form figure 69, 7 lb above field average
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- The Great Karoo (hrs_17395559419) | 2yo G | 133lb | OR - | draw 2 | jockey Kaiya Fraser | trainer James Fanshawe (14d 0/10) | headgear - | last run - days | form - | MARKET 4.0% | 09:00 median 17.00 | Matchbook 29.00
    DATA: model 8.0% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Trainer 0 wins from 10 runs, last 14 days; Lightly raced: 0 runs in our data, so the model has little to go on
- Final Conquest (hrs_17394841835) | 2yo G | 133lb | OR - | draw 8 | jockey Daniel Muscutt | trainer James Horton (14d 0/4) | headgear - | last run 17 days | form 0 | MARKET 1.5% | 09:00 median 50.50 | Matchbook 100.00
    DATA: model 8.6% | style Held up (led 8% of runs) | runs in data 1 | last 3: 7 Nov Southwell (AW) Flat 8f Standard 10/14 fig 52
    DATA against: Best recent form figure 52, 10 lb below field average; Lightly raced: 1 run in our data, so the model has little to go on
- Son of Vega (hrs_17393191809) | 2yo C | 133lb | OR - | draw 4 | jockey Luke Morris | trainer David Simcock (14d 1/8) | headgear h (1st time) | last run 52 days | form 6 | MARKET 1.4% | 09:00 median 51.00 | Matchbook 120.00
    DATA: model 11.8% | style Leader (led 57% of runs) | runs in data 1 | last 3: 3 Oct Southwell Flat 7.1f Standard 6/10
    DATA for: First-time headgear; Pace: may get an uncontested lead
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Radio Bar (hrs_17392768351) | 2yo C | 133lb | OR - | draw 6 | jockey Kieran Shoemark | trainer Ed Walker (14d 1/13) | headgear - | last run 36 days | form 8 | MARKET 1.1% | 09:00 median 67.00 | Matchbook 140.00
    DATA: model 5.8% | style Held up (led 8% of runs) | runs in data 1 | last 3: 19 Oct Bath Flat 8f Good To Soft 8/10 fig 37
    DATA against: Best recent form figure 37, 25 lb below field average; Last-run finishing speed -2.3% vs that field (faded); Lightly raced: 1 run in our data, so the model has little to go on
- Fort McHenry (hrs_17393339915) | 2yo C | 133lb | OR - | draw 7 | jockey Paddy Bradley | trainer Charlie Fellowes (14d 1/6) | headgear - | last run 27 days | form 64 | MARKET 1.1% | 09:00 median 67.00 | Matchbook 160.00
    DATA: model 6.3% | style Held up (led 8% of runs) | runs in data 2 | last 3: 12 Oct Yarmouth Flat 7f Good To Soft 6/7; 28 Oct Nottingham Flat 8.5f Soft 4/5 fig 44
    DATA against: Best recent form figure 44, 18 lb below field average; Lightly raced: 2 runs in our data, so the model has little to go on
- Thai Boxer (hrs_17389869854) | 2yo G | 133lb | OR - | draw 3 | jockey Finley Marsh | trainer Adrian Wintle (14d 0/3) | headgear - | last run 47 days | form 70 | MARKET 0.5% | 09:00 median 151.00 | Matchbook 290.00
    DATA: model 3.0% | style Midfield (led 8% of runs) | runs in data 2 | last 3: 31 Jul Bath Flat 5.7f Firm 7/7; 8 Oct Bath Flat 8f Good 11/13
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on

## 6:00 Wolverhampton (AW) | race_id rac_32305417144 | All Weather Championship Is Back EBF Maiden Stakes (Div II) (GBB/GBBPlus Race)
Flat | Class 3 | 1m142y | going Standard | AW | 8 runners | rating band - | age 2yo
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Modernist (hrs_17395119273) | 2yo C | 133lb | OR - | draw 1 | jockey Colin Keane | trainer John & Thady Gosden (14d 2/19) | headgear - | last run - days | form - | MARKET 33.7% | 09:00 median 2.62 | Matchbook 2.68
    DATA: model 10.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Mythical Tale (hrs_17393753986) | 2yo C | 133lb | OR - | draw 4 | jockey Billy Loughnane | trainer Charlie Appleby (14d 3/5) | headgear - | last run 41 days | form 6 | MARKET 26.4% | 09:00 median 3.00 | Matchbook 3.75
    DATA: model 18.3% | style Held up (led 8% of runs) | runs in data 1 | last 3: 14 Oct Nottingham Flat 8.5f Good To Soft 6/11 fig 52
    DATA for: Best recent form figure 52, 4 lb above field average; Trainer 60% wins (3/5), last 14 days
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Top Scholar (hrs_17393426484) | 2yo C | 133lb | OR - | draw 8 | jockey Cieren Fallon | trainer William Haggas (14d 3/17) | headgear - | last run 48 days | form 3 | MARKET 20.8% | 09:00 median 4.00 | Matchbook 4.60
    DATA: model 16.0% | style Unknown | runs in data 1 | last 3: 7 Oct Nottingham Flat 8.3f Good To Soft 3/5
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Haldon Fire (hrs_17393751900) | 2yo C | 133lb | OR - | draw 5 | jockey Callum Hutchinson | trainer Andrew Balding (14d 2/27) | headgear - | last run 31 days | form 2 | MARKET 12.9% | 09:00 median 6.00 | Matchbook 7.80
    DATA: model 21.2% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 24 Oct Southwell (AW) Flat 8f Standard 2/10 fig 67
    DATA for: Best recent form figure 67, 19 lb above field average
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Carletto (hrs_17395933856) | 2yo C | 133lb | OR - | draw 6 | jockey Kieran Shoemark | trainer Ed Walker (14d 1/13) | headgear - | last run - days | form - | MARKET 2.4% | 09:00 median 32.50 | Matchbook 50.00
    DATA: model 10.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Naval Warrior (hrs_17395554204) | 2yo G | 133lb | OR - | draw 2 | jockey Jonny Peate | trainer James Fanshawe (14d 0/10) | headgear - | last run - days | form - | MARKET 2.1% | 09:00 median 41.00 | Matchbook 50.00
    DATA: model 10.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Trainer 0 wins from 10 runs, last 14 days; Lightly raced: 0 runs in our data, so the model has little to go on
- Sarfraj (hrs_17394630106) | 2yo C | 133lb | OR - | draw 3 | jockey Rob Hornby | trainer Jonathan Portman (14d 2/10) | headgear - | last run 26 days | form 8 | MARKET 1.0% | 09:00 median 81.00 | Matchbook 220.00
    DATA: model 6.1% | style Held up (led 8% of runs) | runs in data 1 | last 3: 29 Oct Bath Flat 8f Soft 8/10 fig 40
    DATA for: Trainer 20% wins (2/10), last 14 days
    DATA against: Best recent form figure 40, 8 lb below field average; Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- True Knight (hrs_17394122165) | 2yo G | 133lb | OR - | draw 7 | jockey Hollie Doyle | trainer Ed Dunlop (14d 1/4) | headgear - | last run 33 days | form 7 | MARKET 0.6% | 09:00 median 126.00 | Matchbook 260.00
    DATA: model 7.2% | style Held up (led 8% of runs) | runs in data 1 | last 3: 22 Oct Newmarket Flat 8f Soft 7/9 fig 33
    DATA against: Best recent form figure 33, 15 lb below field average; Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace

## 6:30 Wolverhampton (AW) | race_id rac_32305419081 | AWC Finals Day At Newcastle 26th March Nursery Handicap Stakes (GBBPlus Race)
Flat | Class 4 | 1m142y | going Standard | AW | 4 runners | rating band 0-85 | age 2yo
DATA pace: Even - Two likely leaders (Happy Love, Capricious Star). A fair, even gallop is most likely.
- Happy Love (hrs_66399494) | 2yo C | 135lb | OR 80 | draw 4 | jockey Billy Loughnane | trainer Charlie Johnston (14d 0/7) | headgear - | last run 33 days | form 22 | MARKET 36.3% | 09:00 median 2.50 | Matchbook 2.50
    comment: Happy Love arrives with back-to-back seconds, the latest last time out, and has run over today's trip, so he looks a solid threat at 135 lb. The main risk is that he's yet to win and has had 33 days off since that last run.
    DATA: model 26.8% | style Leader (led 57% of runs) | runs in data 2 | last 3: 4 Jul Beverley Flat 7.4f Good To Firm 2/6; 22 Oct Newmarket Flat 8f Soft 2/9 fig 57
    DATA for: Good recent finishing positions
    DATA against: Best recent form figure 57, 18 lb below field average; Recent figures 23 lb below its current mark (looks high in the weights); Lightly raced: 2 runs in our data, so the model has little to go on
- National Pride (hrs_65254826) | 2yo C | 133lb | OR 78 | draw 3 | jockey Cieren Fallon | trainer William Haggas (14d 3/17) | headgear - | last run 19 days | form 62441 | MARKET 34.7% | 09:00 median 2.50 | Matchbook 2.82
    comment: National Pride arrives in good heart after winning last time out, following a fourth two starts back and another fourth three starts back, and he's fresh enough at 19 days since his last run.
    DATA: model 27.6% | style Prominent (led 4% of runs) | runs in data 5 | last 3: 12 Sep Chester Flat 7f Soft 4/8; 19 Oct Southwell (AW) Flat 7f Standard 4/14 fig 70; 5 Nov Chelmsford (AW) Flat 7f Standard 1/11 fig 87
    DATA for: Best recent form figure 87, 12 lb above field average; Recent figures 9 lb above its current mark (looks well handicapped); Last-run finishing speed +4.2% vs that field (finished strongly)
- High Calibre (hrs_62169436) | 2yo C | 132lb | OR 77 | draw 1 | jockey Joe Leavy | trainer Richard Hannon (14d 1/10) | headgear - | last run 24 days | form 662531 | MARKET 16.0% | 09:00 median 5.00 | Matchbook 6.80
    comment: High Calibre won last time out and was third two starts back, so he arrives in good heart after 24 days off, and he has run over today's trip and going before.
    DATA: model 16.6% | style Prominent (led 29% of runs) | runs in data 7 | last 3: 16 Sep Beverley Flat 8.5f Good 5/5; 19 Oct Bath Flat 8f Good To Soft 3/13 fig 78; 31 Oct Newmarket Flat 9f Good To Soft 1/10 fig 85
    DATA for: Best recent form figure 85, 10 lb above field average; Recent figures 8 lb above its current mark (looks well handicapped); Has won at this trip or further; Good recent finishing positions
- Capricious Star (hrs_63811412) | 2yo F | 129lb | OR 74 | draw 2 | jockey Clifford Lee | trainer K. R. Burke (14d 0/10) | headgear - | last run 1 days | form 332 | MARKET 12.9% | 09:00 median 6.75 | Matchbook 7.40
    comment: Capricious Star arrives in cracking nick with a second last time out, a third two starts back and another third three starts back, and she has run over today's trip and going before. Yet to win in that spell, though, and a quick turnaround after just one day off is the main risk.
    DATA: model 29.0% | style Leader (led 38% of runs) | runs in data 3 | last 3: 16 Oct Redcar Flat 7f Good 3/7 fig 63; 6 Nov Newcastle (AW) Flat 7f Standard 3/10 fig 63; 23 Nov Wolverhampton (AW) Flat 9.5f Standard 2/5 fig 71
    DATA for: Good recent finishing positions
    DATA against: Best recent form figure 71, 4 lb below field average; Trainer 0 wins from 10 runs, last 14 days

## 7:00 Wolverhampton (AW) | race_id rac_32305421018 | Midnite: Built For 2026 Not 2006 Handicap Stakes
Flat | Class 3 | 6f20y | going Standard | AW | 9 runners | rating band 0-95 | age 3yo+
DATA pace: Lone leader - Dandana is the only habitual front-runner and may be allowed an easy lead.
- Another Abbot (hrs_39961614) | 4yo G | 132lb | OR 89 | draw 5 | jockey Cieren Fallon | trainer William Haggas (14d 3/17) | headgear t | last run 53 days | form 771820 | MARKET 19.8% | 09:00 median 4.00 | Matchbook 4.90 | CHECK (skip line 3.80)
    comment: Another Abbot is hard to fancy after an unplaced effort last time and a 53-day break, with just one win in his last six, a victory four starts back. He has run over today's trip and going, and a second two starts back is the one real positive.
    DATA: model 13.6% | style Prominent (led 8% of runs) | runs in data 8 | last 3: 10 Aug Windsor Flat 6.1f Good To Firm 8/16; 17 Sep Yarmouth Flat 6f Good 2/9; 2 Oct Ascot Flat 6f Good To Firm 16/18
    DATA for: Has won at this trip or further
    DATA against: Last-run finishing speed -3.1% vs that field (faded)
- Bolo Neighs (hrs_40859483) | 4yo G | 133lb | OR 90 | draw 6 | jockey Rhys Clutterbuck | trainer Ralph Beckett (14d 2/9) | headgear b | last run 41 days | form 936504 | MARKET 16.7% | 09:00 median 5.00 | Matchbook 5.60
    comment: Fourth last time out and a third five starts back show Bolo Neighs can run creditably, and he has run over today's trip and going, but he is winless in his last six and returns after 41 days off.
    DATA: model 8.0% | style Held up (led 5% of runs) | runs in data 10 | last 3: 8 Aug Ascot Flat 5f Good To Firm 5/10; 2 Oct Ascot Flat 6f Good To Firm 17/18; 14 Oct Kempton (AW) Flat 6f Standard / Slow 4/11 fig 89
    DATA for: Trainer 22% wins (2/9), last 14 days; Has won at this trip or further
    DATA against: Course: hold-up horses have won 0.7× their fair share at 6f here
- Silent Strike (hrs_53994038) | 3yo G | 130lb | OR 87 | draw 1 | jockey Callum Hutchinson | trainer Andrew Balding (14d 2/27) | headgear t | last run 36 days | form 212003 | MARKET 15.9% | 09:00 median 4.50 | Matchbook 6.80
    comment: Third last time out is a decent lead, but he was unplaced in the two runs before that and has won just once in his last six, so he is hard to fancy.
    DATA: model 8.0% | style Midfield (led 23% of runs) | runs in data 6 | last 3: 3 Apr Newcastle Flat 6f Standard 10/14; 13 Jun York Flat 6f Good 22/22; 19 Oct Wolverhampton (AW) Flat 6f Standard 3/12 fig 91
    DATA for: Recent figures 4 lb above its current mark (looks well handicapped); Last-run finishing speed +3.8% vs that field (finished strongly); Has won at this trip or further
- Purosangue (hrs_35828205) | 5yo G | 128lb | OR 85 | draw 3 | jockey Billy Loughnane | trainer Robert Cowell (14d 1/7) | headgear p | last run 36 days | form 458995 | MARKET 13.9% | 09:00 median 6.00 | Matchbook 6.80
    DATA: model 7.2% | style Prominent (led 8% of runs) | runs in data 7 | last 3: 30 Aug Goodwood Flat 6f Soft 9/10; 17 Sep Yarmouth Flat 6f Good 9/9; 19 Oct Wolverhampton (AW) Flat 6f Standard 5/12 fig 85
- Desert Falcon (hrs_32210332) | 6yo G | 135lb | OR 92 | draw 2 | jockey Ryan Sexton | trainer Julie Camacho (14d 1/9) | headgear p | last run 66 days | form -09960 | MARKET 10.1% | 09:00 median 8.50 | Matchbook 9.20
    comment: A 66-day break is the one reservation, though he runs off 135 lb from stall two.
    DATA: model 19.9% | style Unknown | runs in data 5 | last 3: 22 Aug York Flat 6f Good To Soft 9/20; 12 Sep Doncaster Flat 5.7f Good 6/21; 19 Sep Ayr Flat 6f Heavy 17/23
    DATA against: Poor recent finishing positions
- Dandana (hrs_54525541) | 3yo F | 132lb | OR 89 | draw 4 | jockey Callum Rodriguez | trainer Simon Crisford (14d 1/6) | headgear t | last run 73 days | form 0-0424 | MARKET 9.7% | 09:00 median 9.00 | Matchbook 9.80
    comment: Dandana has been in the frame lately, a fourth last time out and a second two starts back, and she has run over today's trip and going, but she is yet to win in her last five and returns after 73 days off. Carrying 132 lb from draw 4, she looks a midfield type.
    DATA: model 21.1% | style Leader (led 57% of runs) | runs in data 4 | last 3: 27 Jul Windsor Flat 6.1f Good To Firm 4/13; 12 Aug Salisbury Flat 6f Good To Firm 2/7; 12 Sep Lingfield Flat 5f Standard 4/10
    DATA for: Pace: may get an uncontested lead
- Alfa Kellenic (hrs_37890748) | 5yo M | 131lb | OR 88 | draw 7 | jockey Luke Morris | trainer Ivan Furtado (14d 1/11) | headgear - | last run 26 days | form 036-07 | MARKET 8.9% | 09:00 median 9.50 | Matchbook 10.50
    comment: The risk is a form line reading seventh last time out and winless in her last five starts.
    DATA: model 9.1% | style Prominent (led 8% of runs) | runs in data 2 | last 3: 10 Oct York Flat 6f Good To Soft 16/21; 29 Oct Southwell (AW) Flat 7f Standard 7/14 fig 86
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Harry Three (hrs_27040678) | 7yo G | 130lb | OR 87 | draw 8 | jockey Kieran Shoemark | trainer Clive Cox (14d 0/5) | headgear h | wind surgery | last run 822 days | form 64070/ | MARKET 3.1% | 09:00 median 29.00 | Matchbook 30.00
    comment: The main risk is a 822-day absence, which leaves fitness a major question under 130 lb from stall 8.
    DATA: model 10.1% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 822-day break; Lightly raced: 0 runs in our data, so the model has little to go on; Aged 7, older than most of this field
- One And Gone (hrs_56127708) | 3yo G | 126lb | OR 83 | draw 9 | jockey Ryan Kavanagh(3) | trainer Ian Williams (14d 3/19) | headgear - | last run 97 days | form 011070 | MARKET 1.9% | 09:00 median 41.00 | Matchbook 60.00
    comment: One And Gone has been well beaten in his last three starts, unplaced last time and a seventh before that, and returns after 97 days off, so he is hard to fancy. In his favour, he won four and five starts back and has run over today's trip and going.
    DATA: model 3.1% | style Unknown | runs in data 12 | last 3: 30 Jul Goodwood Flat 5f Good To Firm 13/18; 16 Aug Pontefract Flat 5f Good To Firm 7/8; 19 Aug York Flat 5f Good 16/19
    DATA against: Poor recent finishing positions; Returns from a 97-day break

## 7:30 Wolverhampton (AW) | race_id rac_32305422955 | AWC Season 14 Has Begun Fillies' Handicap Stakes
Flat | Class 4 | 7f36y | going Standard | AW | 10 runners | rating band 0-85 | age 3yo+
DATA pace: Lone leader - Nanoscience is the only habitual front-runner and may be allowed an easy lead.
- Queen Tamara (hrs_54150096) | 3yo F | 129lb | OR 77 | draw 4 | jockey Callum Rodriguez | trainer Harry Charlton (14d 0/1) | headgear p | last run 22 days | form -97353 | MARKET 18.9% | 09:00 median 4.33 | Matchbook 4.90 | CHECK (skip line 4.11)
    comment: Queen Tamara arrives fresh enough after 22 days, following a third last time out and a third three starts back, and she has run over today's trip and going before. She remains winless in her last five, though, and carries 129 lb off 77 from stall four.
    DATA: model 7.3% | style Prominent (led 29% of runs) | runs in data 5 | last 3: 22 Aug Redcar Flat 8f Good 3/10; 10 Sep Lingfield Flat 8f Standard 5/6; 2 Nov Chelmsford (AW) Flat 7f Standard 3/8 fig 79
    DATA for: Best recent form figure 79, 5 lb above field average; Good recent finishing positions
- Um Wadi (hrs_41503805) | 5yo M | 129lb | OR 76 | draw 11 | jockey Billy Loughnane | trainer George Boughey (14d 6/20) | headgear t | last run 21 days | form -38701 | MARKET 17.7% | 09:00 median 4.50 | Matchbook 5.30
    comment: Fresh from a win last time out 21 days ago, Um Wadi has run over today's trip and on this going, and her yard is in form; however, a seventh and an eighth in her last five starts show she's inconsistent, and she carries 129 lb from stall 11.
    DATA: model 8.3% | style Held up (led 3% of runs) | runs in data 5 | last 3: 5 May Gowran Park Flat 9.5f Good To Yielding 7/9; 26 Jun Curragh Flat 7f Good 16/17; 3 Nov Wolverhampton (AW) Flat 8.5f Standard 1/6 fig 73
    DATA for: Trainer 30% wins (6/20), last 14 days; Has won at this trip or further
- Nanoscience (hrs_56437906) | 3yo F | 126lb | OR 74 | draw 6 | jockey Callum Hutchinson | trainer Andrew Balding (14d 2/27) | headgear - | last run 33 days | form 313544 | MARKET 12.4% | 09:00 median 7.00 | Matchbook 7.00
    comment: Fourth last time out and again two starts back, she has been consistent without winning since a victory five starts back, and a 33-day break is no concern.
    DATA: model 12.0% | style Leader (led 29% of runs) | runs in data 7 | last 3: 19 Sep Newmarket Flat 7f Good 5/14; 9 Oct Newmarket Flat 7f Good To Soft 4/11; 22 Oct Newmarket Flat 8f Soft 4/15 fig 81
    DATA for: Best recent form figure 81, 7 lb above field average; Recent figures 7 lb above its current mark (looks well handicapped); Last-run finishing speed +2.0% vs that field (finished strongly); Has won at this trip or further; Pace: may get an uncontested lead
- Ghisa (hrs_56811405) | 3yo F | 132lb | OR 80 | draw 10 | jockey Paddy Bradley | trainer Charlie Fellowes (14d 1/6) | headgear h | last run 17 days | form 333142 | MARKET 11.8% | 09:00 median 7.00 | Matchbook 7.80
    comment: Ghisa comes here sharp after a second last time out, 17 days ago, and has a win three starts back in a consistent run, having also run over today's trip and going before.
    DATA: model 17.6% | style Midfield (led 4% of runs) | runs in data 6 | last 3: 11 Sep Chester Flat 7f Good To Soft 1/13; 19 Oct Pontefract Flat 6f Heavy 4/10 fig 79; 7 Nov Doncaster Flat 7f Good To Soft 2/12 fig 81
    DATA for: Best recent form figure 81, 7 lb above field average; Has won at this trip or further; Good recent finishing positions
- Inside Story (hrs_52742116) | 3yo F | 131lb | OR 79 | draw 1 | jockey Clifford Lee | trainer James Tate (14d 0/4) | headgear - | last run 22 days | form 482258 | MARKET 8.8% | 09:00 median 10.00 | Matchbook 10.00
    comment: The risk is that she is yet to win in her last six starts.
    DATA: model 12.0% | style Midfield (led 5% of runs) | runs in data 7 | last 3: 18 Aug Wolverhampton Flat 7.2f Standard 2/9; 22 Sep Southwell Flat 7.1f Standard 5/12; 2 Nov Chelmsford (AW) Flat 7f Standard 8/8 fig 53
    DATA against: Best recent form figure 53, 21 lb below field average; Recent figures 26 lb below its current mark (looks high in the weights); Last-run finishing speed -4.0% vs that field (faded)
- Enola Grey (hrs_30123646) | 6yo M | 119lb | OR 66 | draw 7 | jockey Laura Coughlan(3) | trainer Gemma Tutty (14d 0/4) | headgear - | last run 19 days | form 006034 | MARKET 7.6% | 09:00 median 11.00 | Matchbook 12.00
    comment: Enola Grey is winless in her last six, though a fourth last time out and a third two starts back show she is not out of form, and she has run over today's trip and going.
    DATA: model 4.0% | style Held up (led 3% of runs) | runs in data 11 | last 3: 22 Sep Southwell Flat 7.1f Standard 10/12; 23 Oct Wolverhampton (AW) Flat 7f Standard 3/11 fig 65; 5 Nov Southwell (AW) Flat 7f Standard 4/10 fig 67
    DATA for: Carries 9 lb less than average
    DATA against: Best recent form figure 67, 7 lb below field average; Official rating 66, 9 lb below field average; Aged 6, older than most of this field
- Queue Dos (hrs_42261198) | 4yo F | 123lb | OR 70 | draw 3 | jockey Alexandra Egan(5) | trainer J. S. Moore (14d 0/9) | headgear b | last run 8 days | form 385552 | MARKET 7.4% | 09:00 median 11.00 | Matchbook 13.00
    comment: Queue Dos is winless in her last six, though a second last time out, just eight days ago, is a fair effort and she has run over today's trip and going.
    DATA: model 8.8% | style Midfield (led 29% of runs) | runs in data 8 | last 3: 23 Oct Wolverhampton (AW) Flat 7f Standard 5/11 fig 70; 4 Nov Kempton (AW) Flat 6f Standard / Slow 5/7 fig 62; 16 Nov Wolverhampton (AW) Flat 7f Standard 2/11 fig 77
    DATA for: Recent figures 7 lb above its current mark (looks well handicapped); Last-run finishing speed +2.8% vs that field (finished strongly); Carries 5 lb less than average
    DATA against: Official rating 70, 5 lb below field average; Trainer 0 wins from 9 runs, last 14 days
- Maldevious (hrs_43796683) | 4yo F | 124lb | OR 66 | draw 8 | jockey Harry Russell | trainer Brian Ellison (14d 1/7) | headgear tp | last run 7 days | form 154451 | MARKET 5.7% | 09:00 median 10.00 | Matchbook 26.00
    comment: Won last time out and has two wins in her last six, yet she's back in just seven days and was only fourth and fifth in between, so consistency is a worry.
    DATA: model 6.1% | style Midfield (led 4% of runs) | runs in data 12 | last 3: 28 Sep Hamilton Flat 6f Soft 4/6; 5 Nov Southwell (AW) Flat 6f Standard 5/9 fig 67; 17 Nov Southwell (AW) Flat 7f Standard 1/9 fig 74
    DATA for: Recent figures 8 lb above its current mark (looks well handicapped); Last-run finishing speed +4.8% vs that field (finished strongly); Has won at this trip or further
    DATA against: Official rating 66, 9 lb below field average
- Ice Sovereigns (hrs_54555340) | 3yo F | 137lb | OR 85 | draw 5 | jockey Shane Gray | trainer Richard & Peter Fahey (14d 0/11) | headgear - | last run 22 days | form 0-0815 | MARKET 4.9% | 09:00 median 17.00 | Matchbook 19.00
    DATA: model 10.7% | style Prominent (led 23% of runs) | runs in data 4 | last 3: 19 Sep Newmarket Flat 8f Good 8/9; 12 Oct Musselburgh Flat 7.1f Good To Soft 1/7; 2 Nov Chelmsford (AW) Flat 7f Standard 5/8 fig 84
    DATA for: Best recent form figure 84, 10 lb above field average; Official rating 85, 10 lb above field average; Has won at this trip or further
    DATA against: Trainer 0 wins from 11 runs, last 14 days; Carries 9 lb more than average
- Merry (hrs_59246908) | 3yo F | 131lb | OR 79 | draw 2 | jockey Daniel Muscutt | trainer James Horton (14d 0/4) | headgear - | last run 63 days | form 452120 | MARKET 4.8% | 09:00 median 17.00 | Matchbook 19.00
    comment: Merry won three starts back and was second two starts back, but she was unplaced last time out and returns after 63 days off.
    DATA: model 13.2% | style Midfield (led 3% of runs) | runs in data 6 | last 3: 19 Aug Kempton Flat 7f Standard To Slow 1/9; 26 Aug Kempton Flat 7f Standard To Slow 2/9; 22 Sep Southwell Flat 7.1f Standard 12/12
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Last-run finishing speed -12.9% vs that field (faded)

## 8:00 Wolverhampton (AW) | race_id rac_32305424892 | Midnite Built Different Handicap Stakes (GBBPlus Race)
Flat | Class 4 | 1m5f219y | going Standard | AW | 9 runners | rating band 0-85 | age 3yo+
DATA pace: Lone leader - Yaa Min is the only habitual front-runner and may be allowed an easy lead.
- Flagbearer (hrs_17389810403) | 3yo G | 130lb | OR 80 | draw 4 | jockey Cieren Fallon | trainer William Haggas (14d 3/17) | headgear p | last run 29 days | form 4391 | MARKET 21.6% | 09:00 median 4.00 | Matchbook 4.30 | CHECK (skip line 3.80)
    comment: Carrying 130 lb off an official mark of 80 after 29 days off, he looks to have plenty to prove.
    DATA: model 9.0% | style Prominent (led 3% of runs) | runs in data 4 | last 3: 21 Aug Hamilton Flat 11.1f Good To Soft 3/3; 9 Sep Carlisle Flat 11.2f Good 9/12; 26 Oct Kempton (AW) Flat 12f Standard / Slow 1/9 fig 64
    DATA for: Good recent finishing positions; Carries 6 lb less than average
    DATA against: Best recent form figure 64, 15 lb below field average; Recent figures 16 lb below its current mark (looks high in the weights)
- Quebella (hrs_51523815) | 4yo F | 137lb | OR 82 | draw 9 | jockey Callum Rodriguez | trainer Owen Burrows (14d 1/5) | headgear - | last run 14 days | form -33420 | MARKET 19.2% | 09:00 median 4.33 | Matchbook 5.00
    comment: The risk is an unplaced run last time out and being yet to win in that spell.
    DATA: model 13.0% | style Midfield (led 29% of runs) | runs in data 4 | last 3: 12 Jun Chester Flat 10.3f Soft 3/6; 2 Sep Bath Flat 11.6f Good 4/6; 23 Sep Goodwood Flat 14f Good 2/8
    DATA for: Trainer 20% wins (1/5), last 14 days; Good recent finishing positions
- Must Believe (hrs_43062901) | 4yo G | 134lb | OR 79 | draw 6 | jockey Billy Loughnane | trainer George Baker (14d 1/5) | headgear - | last run 19 days | form 183241 | MARKET 15.9% | 09:00 median 5.00 | Matchbook 6.20
    comment: Must Believe arrives fresh from a win last time out, with a second, a fourth and a third in the other recent runs, and he has run over today's trip and going.
    DATA: model 11.1% | style Prominent (led 5% of runs) | runs in data 8 | last 3: 4 Sep Kempton Flat 16f Standard To Slow 2/8; 2 Oct Ascot Flat 15.9f Good To Firm 4/5; 5 Nov Chelmsford (AW) Flat 16f Standard 1/6 fig 80
    DATA for: Trainer 20% wins (1/5), last 14 days; Has won at this trip or further; Good recent finishing positions
- Codiak (hrs_54398393) | 4yo G | 142lb | OR 87 | draw 3 | jockey Oisin Orr | trainer Edward Bethell (14d 0/8) | headgear b | last run 34 days | form 1-1316 | MARKET 13.7% | 09:00 median 6.50 | Matchbook 6.80
    comment: The main risk is a sixth last time out and a 34-day break, while he carries 142 lb.
    DATA: model 18.3% | style Held up (led 8% of runs) | runs in data 4 | last 3: 4 Apr Wolverhampton Flat 12.2f Standard 3/7; 26 Apr Nottingham Flat 14f Good 1/6; 21 Oct Kempton (AW) Flat 16f Standard / Slow 6/14 fig 88
    DATA for: Best recent form figure 88, 9 lb above field average; Official rating 87, 5 lb above field average; Has won at this trip or further; Good recent finishing positions
    DATA against: Trainer 0 wins from 8 runs, last 14 days; Carries 6 lb more than average
- Wonder (hrs_36665125) | 5yo G | 136lb | OR 81 | draw 2 | jockey George Wood | trainer James Fanshawe (14d 0/10) | headgear p | last run 41 days | form 122356 | MARKET 9.6% | 09:00 median 9.50 | Matchbook 9.20
    comment: Beaten into sixth last time out and a fifth two starts back, this gelding has drifted from a third three starts back, though he has run over today's trip and going before.
    DATA: model 9.6% | style Prominent (led 8% of runs) | runs in data 7 | last 3: 27 Apr Lingfield Flat 12f Standard 3/8; 16 Aug Southwell Flat 12.1f Standard 5/12; 14 Oct Kempton (AW) Flat 11f Standard / Slow 6/13 fig 81
    DATA against: Trainer 0 wins from 10 runs, last 14 days
- Senor Cortez (hrs_49044506) | 5yo G | 142lb | OR 87 | draw 7 | jockey Hollie Doyle | trainer Des Donovan (14d 1/3) | headgear - | last run 36 days | form 711147 | MARKET 7.2% | 09:00 median 9.00 | Matchbook 16.50
    comment: Senor Cortez won three of his last six, including a hat-trick from five to three starts back, but he has since slipped to a fourth two starts back and a seventh last time out.
    DATA: model 11.7% | style Midfield (led 3% of runs) | runs in data 8 | last 3: 10 Aug Kempton Flat 16f Standard To Slow 1/12; 30 Aug Goodwood Flat 16f Soft 4/9; 19 Oct Pontefract Flat 18f Heavy 7/9
    DATA for: Official rating 87, 5 lb above field average; Has won at this trip or further
    DATA against: Last-run finishing speed -3.8% vs that field (faded); Carries 6 lb more than average
- Oneforthegutter (hrs_25580702) | 7yo G | 138lb | OR 83 | draw 5 | jockey Luke Morris | trainer Ian Williams (14d 3/19) | headgear v | last run 19 days | form 875726 | MARKET 5.9% | 09:00 median 15.00 | Matchbook 15.50
    comment: Oneforthegutter is yet to win in his last six, but he was second two starts back, he has run over today's trip and going, and he returns after 19 days.
    DATA: model 9.7% | style Held up (led 3% of runs) | runs in data 8 | last 3: 19 Sep Newbury Flat 13.3f Good To Firm 7/9; 27 Sep Epsom Downs Flat 12f Good 2/13; 5 Nov Southwell (AW) Flat 12f Standard 6/9 fig 73
    DATA against: Best recent form figure 73, 6 lb below field average; Recent figures 10 lb below its current mark (looks high in the weights); Aged 7, older than most of this field
- Yaa Min (hrs_46515455) | 4yo G | 139lb | OR 84 | draw 1 | jockey Darragh Keenan | trainer Hayley Burton (14d 0/4) | headgear p (1st time) | last run 7 days | form 349155 | MARKET 5.4% | 09:00 median 17.00 | Matchbook 17.00
    comment: Yaa Min arrives quickly after seven days off, with a win three starts back and a third six starts back in his last six, and he has run over today's trip and going before.
    DATA: model 15.5% | style Leader (led 38% of runs) | runs in data 12 | last 3: 26 Sep Haydock Flat 14f Heavy 1/9; 16 Oct Haydock Flat 14f Heavy 5/5 fig 70; 17 Nov Southwell (AW) Flat 12f Standard 5/11 fig 88
    DATA for: Best recent form figure 88, 9 lb above field average; Recent figures 4 lb above its current mark (looks well handicapped); Last-run finishing speed +3.5% vs that field (finished strongly); Has won at this trip or further; First-time headgear; Pace: may get an uncontested lead
- Midnight Rumble (hrs_36999977) | 5yo G | 129lb | OR 74 | draw 8 | jockey Joe Leavy | trainer Jake Thomas Coulson (14d 0/1) | headgear - | last run 94 days | form 245306 | MARKET 1.3% | 09:00 median 81.00 | Matchbook 110.00
    comment: Midnight Rumble is hard to fancy, winless in his last six and only sixth last time out, with a 94-day break to overcome and 129 lb to carry.
    DATA: model 2.0% | style Midfield (led 4% of runs) | runs in data 8 | last 3: 27 Jun Chester Flat 15.9f Good 3/7; 24 Jul York Flat 16.3f Good To Firm 13/13; 22 Aug Chester Flat 15.9f Good To Soft 6/9
    DATA for: Carries 7 lb less than average
    DATA against: Official rating 74, 8 lb below field average; Returns from a 94-day break

## 8:30 Wolverhampton (AW) | race_id rac_32305426829 | Midnite A Next Generation Betting App Handicap Stakes
Flat | Class 5 | 5f21y | going Standard | AW | 9 runners | rating band 0-75 | age 3yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Maharajas Express (hrs_29228773) | 6yo G | 133lb | OR 73 | draw 7 | jockey Billy Loughnane | trainer Ian Williams (14d 3/19) | headgear - | last run 20 days | form 221823 | MARKET 19.3% | 09:00 median 4.00 | Matchbook 5.10 | CHECK (skip line 3.80)
    comment: Maharajas Express arrives in sound order, third last time out and second two starts back, with a win four starts back, and he has run over today's trip and going before.
    DATA: model 14.8% | style Held up (led 3% of runs) | runs in data 12 | last 3: 29 Sep Bath Flat 5f Good To Firm 8/12; 29 Oct Bath Flat 5.5f Soft 2/12 fig 80; 4 Nov Nottingham Flat 5f Soft 3/10 fig 72
    DATA for: Best recent form figure 80, 13 lb above field average; Recent figures 7 lb above its current mark (looks well handicapped); Has won at this trip or further; Good recent finishing positions
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Grandlad (hrs_40293729) | 5yo G | 133lb | OR 73 | draw 5 | jockey Daniel Muscutt | trainer James Horton (14d 0/4) | headgear t | last run 7 days | form 769047 | MARKET 18.2% | 09:00 median 4.50 | Matchbook 5.00
    comment: Winless in his last six, though, so a fourth two starts back is his best recent effort.
    DATA: model 7.4% | style Prominent (led 8% of runs) | runs in data 8 | last 3: 13 Sep Doncaster Flat 5f Good 10/10; 16 Oct Newcastle (AW) Flat 5f Standard 4/11 fig 72; 17 Nov Southwell (AW) Flat 5f Standard 7/13 fig 68
    DATA for: Best recent form figure 72, 5 lb above field average; Has won at this trip or further
- Campenaerts (hrs_50434272) | 3yo G | 134lb | OR 74 | draw 10 | jockey Rob Hornby | trainer Jonathan Portman (14d 2/10) | headgear - | last run 20 days | form 782421 | MARKET 15.6% | 09:00 median 5.00 | Matchbook 6.20
    comment: The main risk is 134 lb from draw 10.
    DATA: model 18.1% | style Midfield (led 23% of runs) | runs in data 8 | last 3: 2 Oct Wolverhampton Flat 6.1f Standard 4/10; 28 Oct Nottingham Flat 5f Soft 2/9 fig 71; 4 Nov Nottingham Flat 5f Soft 1/10 fig 74
    DATA for: Best recent form figure 74, 7 lb above field average; Trainer 20% wins (2/10), last 14 days; Has won at this trip or further; Good recent finishing positions
- Showtime Mahomes (hrs_24593625) | 7yo G | 121lb | OR 61 | draw 2 | jockey Laura Pearson | trainer Grant Tuer (14d 0/5) | headgear - | last run 3 days | form 152044 | MARKET 10.1% | 09:00 median 8.00 | Matchbook 9.60
    comment: Showtime Mahomes was a fourth last time out and a fourth two starts back, and he has run over today's trip and going, though he is back after just three days and has won once in his last six starts.
    DATA: model 7.7% | style Midfield (led 4% of runs) | runs in data 13 | last 3: 26 Oct Redcar Flat 6f Heavy 11/14 fig 32; 6 Nov Newcastle (AW) Flat 6f Standard 4/14 fig 63; 21 Nov Newcastle (AW) Flat 6f Standard 4/13 fig 57
    DATA for: Has won at this trip or further; Carries 10 lb less than average
    DATA against: Best recent form figure 63, 4 lb below field average; Official rating 61, 10 lb below field average
- Truly Glamorous (hrs_53476045) | 3yo G | 131lb | OR 71 | draw 3 | jockey Gina Mangan | trainer Christopher Mason (14d 0/1) | headgear - | last run 82 days | form -41103 | MARKET 9.2% | 09:00 median 9.50 | Matchbook 9.80
    comment: Truly Glamorous bounced back to be third last time out after an unplaced run, and he won three and four starts back, but an 82-day absence and 131 lb are hard to overlook.
    DATA: model 12.7% | style Prominent (led 8% of runs) | runs in data 5 | last 3: 2 Jul Newbury Flat 5.2f Good To Firm 1/8; 30 Jul Goodwood Flat 5f Good To Firm 14/18; 3 Sep Lingfield Flat 5f Standard 3/5
    DATA for: Has won at this trip or further; Good recent finishing positions
- Burdett Estate (hrs_52388546) | 3yo G | 132lb | OR 72 | draw 8 | jockey Kieran Shoemark | trainer Brian Toomey (14d 0/1) | headgear b (1st time) | last run 26 days | form -37900 | MARKET 8.0% | 09:00 median 9.00 | Matchbook 14.00
    comment: Burdett Estate is hard to fancy, unplaced in his last two outings after a ninth and a seventh, with a third five starts back the only bright spot in a winless recent run.
    DATA: model 3.2% | style Prominent (led 38% of runs) | runs in data 5 | last 3: 7 Sep Windsor Flat 8.1f Good 9/9; 21 Sep Leicester Flat 8.2f Good 12/13; 29 Oct Bath Flat 5.5f Soft 12/12 fig 44
    DATA for: First-time headgear
    DATA against: Best recent form figure 44, 23 lb below field average; Recent figures 28 lb below its current mark (looks high in the weights); Last-run finishing speed -5.7% vs that field (faded); Poor recent finishing positions
- Rye (hrs_46078060) | 4yo F | 122lb | OR 62 | draw 1 | jockey Hollie Doyle | trainer Tony Carroll (14d 1/31) | headgear p | last run 35 days | form 426142 | MARKET 7.6% | 09:00 median 10.75 | Matchbook 13.00
    DATA: model 9.7% | style Held up (led 3% of runs) | runs in data 9 | last 3: 1 Sep Wolverhampton Flat 6.1f Standard 1/11; 29 Sep Wolverhampton Flat 6.1f Standard 4/11; 20 Oct Newcastle (AW) Flat 6f Standard 2/12 fig 62
    DATA for: Has won at this trip or further; Good recent finishing positions; Carries 9 lb less than average
    DATA against: Best recent form figure 62, 5 lb below field average; Official rating 62, 9 lb below field average; Pace: steady gallop likely, hard to come from off the pace
- Beaumadier (hrs_29748383) | 6yo G | 134lb | OR 74 | draw 4 | jockey Hope Regan(7) | trainer Mark Loughnane (14d 2/15) | headgear - | last run 7 days | form 255810 | MARKET 7.3% | 09:00 median 12.00 | Matchbook 13.50
    comment: Beaumadier won two starts back but was unplaced last time out, and he's back quickly after just seven days; he has run over today's trip and going before.
    DATA: model 12.1% | style Prominent (led 29% of runs) | runs in data 16 | last 3: 17 Aug Catterick Flat 5f Good 8/11; 20 Oct Newcastle (AW) Flat 5f Standard 1/13 fig 74; 17 Nov Southwell (AW) Flat 5f Standard 11/13 fig 61
    DATA for: Best recent form figure 74, 7 lb above field average; Has won at this trip or further
- Moe's Legacy (hrs_35796614) | 5yo M | 135lb | OR 75 | draw 9 | jockey Cieren Fallon | trainer Ronald Harris (14d 0/0) | headgear v | last run 47 days | form 274418 | MARKET 4.9% | 09:00 median 17.00 | Matchbook 19.50
    comment: The main risk is a disappointing eighth last time out, followed by a 47-day break.
    DATA: model 14.2% | style Held up (led 4% of runs) | runs in data 12 | last 3: 11 Sep Sandown Flat 5f Good To Soft 4/9; 29 Sep Bath Flat 5.7f Good To Firm 1/9; 8 Oct Bath Flat 5.7f Good 8/10
    DATA for: Has won at this trip or further
    DATA against: Pace: steady gallop likely, hard to come from off the pace
