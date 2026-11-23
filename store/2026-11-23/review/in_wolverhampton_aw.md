# Card review packet: Wolverhampton (AW), 2026-11-23

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


## 4:30 Wolverhampton (AW) | race_id rac_32305271869 | Midnight A Next Generation Betting App Handicap Stakes
Flat | Class 6 | 1m1f104y | going Standard | AW | 13 runners | rating band 0-60 | age 3yo+
DATA pace: Even - Two likely leaders (Symphony of Joy, Eighty Eight). A fair, even gallop is most likely.
- Eighty Eight (hrs_25825541) | 7yo G | 135lb | OR 57 | draw 12 | jockey Luke Morris | trainer James Owen (14d 3/40) | headgear - | last run 18 days | form -33921 | MARKET 27.1% | 09:00 median 3.00 | Matchbook 3.30 | CHECK (skip line 2.85)
    comment: Eighty Eight won last time out and was second two starts back, so he arrives fresh from an 18-day break and has run over today's trip and going.
    DATA: model 18.3% | style Leader (led 29% of runs) | runs in data 5 | last 3: 13 Mar Dundalk Flat 10.7f Standard 9/14; 27 Oct Wolverhampton (AW) Flat 8.5f Standard 2/10 fig 53; 5 Nov Chelmsford (AW) Flat 10f Standard 1/13 fig 62
    DATA for: Best recent form figure 62, 11 lb above field average; Recent figures 5 lb above its current mark (looks well handicapped); Has won at this trip or further; Good recent finishing positions
    DATA against: Aged 7, older than most of this field
- Law of Design (hrs_43796431) | 4yo G | 137lb | OR 59 | draw 3 | jockey Ryan Kavanagh(3) | trainer Ian Williams (14d 2/14) | headgear b | last run 19 days | form 523589 | MARKET 14.1% | 09:00 median 5.50 | Matchbook 6.60
    DATA: model 7.7% | style Prominent (led 29% of runs) | runs in data 11 | last 3: 3 Oct Redcar Flat 8f Good 5/14; 13 Oct Leicester Flat 8.2f Good To Soft 8/9; 4 Nov Nottingham Flat 8.5f Soft 9/15 fig 42
    DATA against: Best recent form figure 42, 9 lb below field average; Recent figures 17 lb below its current mark (looks high in the weights)
- Token Love (hrs_54304747) | 4yo G | 135lb | OR 57 | draw 13 | jockey Aiden Brookes | trainer Micky Hammond & Becky Smith (14d 1/15) | headgear t | last run 21 days | form 742302 | MARKET 13.1% | 09:00 median 6.00 | Matchbook 7.20
    comment: Token Love is yet to win in his last six starts, though he was second last time out and has a third and a second in that run, and he has run over today's trip and going.
    DATA: model 11.3% | style Prominent (led 4% of runs) | runs in data 6 | last 3: 25 Jul Newcastle Flat 10.2f Standard To Slow 3/13; 25 Sep Newcastle Flat 10.2f Standard 10/14; 2 Nov Wolverhampton (AW) Flat 9.5f Standard 2/12 fig 58
    DATA for: Best recent form figure 58, 7 lb above field average; Good recent finishing positions
- Imola (hrs_36779883) | 5yo M | 137lb | OR 59 | draw 4 | jockey Clifford Lee | trainer Joey Ramsden (14d 0/1) | headgear v (1st time) | last run 21 days | form 600476 | MARKET 12.2% | 09:00 median 6.00 | Matchbook 8.20
    comment: Imola is winless in her last six, with a sixth last time out and a fourth three starts back, though she's fresh enough after 21 days and has run over today's trip and going.
    DATA: model 5.8% | style Held up (led 3% of runs) | runs in data 14 | last 3: 12 Oct Newcastle Flat 8f Standard 4/13; 22 Oct Southwell (AW) Flat 8f Standard 7/10 fig 53; 2 Nov Wolverhampton (AW) Flat 9.5f Standard 6/12 fig 57
    DATA for: Best recent form figure 57, 6 lb above field average; Has won at this trip or further; First-time headgear
- Beachborough Girl (hrs_45855257) | 4yo F | 138lb | OR 60 | draw 2 | jockey Dylan Hogan | trainer Julia & Shelley Birkett (14d 0/0) | headgear tp | last run 19 days | form 327158 | MARKET 5.9% | 09:00 median 13.00 | Matchbook 16.50
    comment: Beachborough Girl won three starts back but has since finished a fifth, then an eighth last time out, so the form is cooling.
    DATA: model 10.2% | style Midfield (led 4% of runs) | runs in data 8 | last 3: 2 Jun Wolverhampton Flat 9.5f Standard 1/11; 16 Jun Wolverhampton Flat 9.5f Standard 5/11; 4 Nov Kempton (AW) Flat 8f Standard / Slow 8/13 fig 49
    DATA for: Has won at this trip or further
    DATA against: Recent figures 11 lb below its current mark (looks high in the weights)
- Glitter Code (hrs_41813933) | 4yo G | 136lb | OR 58 | draw 8 | jockey Callum Shepherd | trainer William Knight (14d 0/0) | headgear p | last run 28 days | form 076140 | MARKET 5.2% | 09:00 median 15.00 | Matchbook 18.50
    comment: Glitter Code was unplaced last time out and has one win in his last six, a victory three starts back, followed by a fourth two runs ago.
    DATA: model 9.0% | style Held up (led 5% of runs) | runs in data 7 | last 3: 31 Aug Ripon Flat 10.9f Soft 1/10; 17 Sep Southwell Flat 11.1f Standard 4/9; 26 Oct Leicester Flat 12f Soft 13/13
    DATA for: Has won at this trip or further
- Ceinture d'Orion (hrs_64072323) | 3yo F | 132lb | OR 57 | draw 1 | jockey Kieran Shoemark | trainer David O'Meara (14d 0/12) | headgear p | last run 16 days | form 437465 | MARKET 4.4% | 09:00 median 19.00 | Matchbook 21.00
    comment: Winless in her last six, Ceinture d'Orion was fifth last time out and has finished no better than a third five starts back, so she is hard to fancy; she has run over today's trip and going, and a 16-day break keeps her fit.
    DATA: model 9.1% | style Prominent (led 3% of runs) | runs in data 9 | last 3: 17 Sep Southwell Flat 8.1f Standard 4/12; 19 Oct Southwell (AW) Flat 8f Standard 6/14 fig 57; 7 Nov Southwell (AW) Flat 8f Standard 5/11 fig 56
    DATA for: Best recent form figure 57, 6 lb above field average
    DATA against: Trainer 0 wins from 12 runs, last 14 days
- Miss Guinevere (hrs_62813002) | 3yo F | 133lb | OR 58 | draw 11 | jockey Paddy Bradley | trainer Charlie Fellowes (14d 1/5) | headgear h | last run 31 days | form 543364 | MARKET 4.1% | 09:00 median 19.00 | Matchbook 24.00
    comment: Miss Guinevere has been consistent without a win, finishing fourth last time out, with a third three starts back and another four starts back, and she has run over today's trip and going before.
    DATA: model 4.0% | style Midfield (led 3% of runs) | runs in data 7 | last 3: 11 Sep Salisbury Flat 9.9f Soft 3/10; 28 Sep Brighton Flat 11.9f Good To Firm 6/7; 23 Oct Wolverhampton (AW) Flat 12f Standard 4/5 fig 55
    DATA for: Trainer 20% wins (1/5), last 14 days
- Symphony of Joy (hrs_55273141) | 4yo G | 138lb | OR 60 | draw 6 | jockey Matthew Lloyd Slater(7) | trainer Kevin & Lauren Frost (14d 1/5) | headgear t | last run 27 days | form 063438 | MARKET 3.4% | 09:00 median 23.00 | Matchbook 29.00
    comment: Symphony of Joy has run over today's trip and going and was third two starts back, with a fourth and another third before that, so he's rarely far away despite being winless in recent starts.
    DATA: model 6.2% | style Leader (led 72% of runs) | runs in data 7 | last 3: 3 Aug Nottingham Flat 8.3f Good To Firm 4/5; 30 Aug Yarmouth Flat 8f Good To Soft 3/5; 27 Oct Wolverhampton (AW) Flat 8.5f Standard 8/10 fig 51
    DATA for: Trainer 20% wins (1/5), last 14 days
    DATA against: Recent figures 9 lb below its current mark (looks high in the weights)
- Riyadh Gem (hrs_45855124) | 4yo G | 136lb | OR 58 | draw 9 | jockey William Cox | trainer Faye Bramley (14d 1/17) | headgear - | last run 25 days | form 3-8500 | MARKET 3.0% | 09:00 median 23.00 | Matchbook 36.00
    comment: The risk is a winless recent run, including two unplaced efforts latest, under 136 lb.
    DATA: model 4.1% | style Held up (led 5% of runs) | runs in data 4 | last 3: 19 Mar Newcastle Flat 10.2f Standard 5/10; 15 May Newbury Flat 8f Good 13/13; 29 Oct Bath Flat 8f Soft 13/14 fig 34
    DATA against: Best recent form figure 34, 17 lb below field average; Recent figures 24 lb below its current mark (looks high in the weights)
- Create (hrs_30455194) | 6yo M | 127lb | OR 49 | draw 10 | jockey Kieran O'Neill | trainer Scott Dixon (14d 0/3) | headgear p | last run 20 days | form 107324 | MARKET 2.8% | 09:00 median 21.00 | Matchbook 48.00
    comment: Create was beaten into fourth last time out, after a second two starts back and a third three starts back, so she is consistent enough, but she has won just once in her last six and her only success came six starts back.
    DATA: model 5.4% | style Midfield (led 4% of runs) | runs in data 12 | last 3: 28 Sep Wolverhampton Flat 7.2f Standard 3/11; 13 Oct Wolverhampton Flat 7.2f Standard 2/9; 3 Nov Wolverhampton (AW) Flat 7f Standard 4/11 fig 47
    DATA for: Good recent finishing positions; Carries 8 lb less than average
    DATA against: Best recent form figure 47, 4 lb below field average; Official rating 49, 9 lb below field average
- She's Ideal (hrs_41191248) | 4yo F | 136lb | OR 58 | draw 5 | jockey Daniel Muscutt | trainer Bernard Llewellyn & Robert Williams (14d 0/2) | headgear p | last run 35 days | form 138478 | MARKET 2.6% | 09:00 median 27.50 | Matchbook 42.00
    comment: She's Ideal arrives off two modest runs, an eighth last time out and a seventh two starts back, though she did finish fourth three starts back and has run over today's trip and going.
    DATA: model 5.0% | style Midfield (led 4% of runs) | runs in data 14 | last 3: 10 Sep Laytown Flat 6f Standard 4/10; 8 Oct Bath Flat 10.2f Good 7/9; 19 Oct Bath Flat 8f Good To Soft 8/14 fig 53
    DATA for: Has won at this trip or further
- Boogie Inthejungle (hrs_45824492) | 4yo F | 136lb | OR 58 | draw 7 | jockey Joe Leavy | trainer James Evans (14d 0/0) | headgear - | last run 171 days | form 79088- | MARKET 2.2% | 09:00 median 27.50 | Matchbook 65.00
    comment: Carrying 136 lb from draw 7, she is yet to win in recent starts.
    DATA: model 3.9% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 31 Mar Limerick Hurdle 16f Soft 6/11; 16 May Wexford Hurdle 17f Good To Yielding 8/13; 5 Jun Clonmel Hurdle 16.5f Good 9/16
    DATA against: Poor recent finishing positions; Returns from a 171-day break

## 5:00 Wolverhampton (AW) | race_id rac_32305769678 | All Weather Championship Is Back Nursery Handicap Stakes
Flat | Class 5 | 1m1f104y | going Standard | AW | 6 runners | rating band 0-75 | age 2yo
DATA pace: Even - Two likely leaders (Capricious Star, Aquila d'Oro). A fair, even gallop is most likely.
- Capricious Star (hrs_63811412) | 2yo F | 135lb | OR 74 | draw 5 | jockey Clifford Lee | trainer K. R. Burke (14d 0/7) | headgear - | last run 17 days | form 33 | MARKET 32.9% | 09:00 median 2.75 | Matchbook 2.88
    comment: Capricious Star has finished third in both recent starts, is fresh enough after 17 days off, and has run on today's going before, so she looks a solid threat from stall five. The main risk is that she's yet to win and now carries 135 lb off a mark of 74.
    DATA: model 37.7% | style Leader (led 38% of runs) | runs in data 2 | last 3: 16 Oct Redcar Flat 7f Good 3/7 fig 63; 6 Nov Newcastle (AW) Flat 7f Standard 3/10 fig 63
    DATA for: Official rating 74, 8 lb above field average; Good recent finishing positions
    DATA against: Recent figures 11 lb below its current mark (looks high in the weights); Carries 8 lb more than average; Lightly raced: 2 runs in our data, so the model has little to go on
- Princess Lottie (hrs_65774989) | 2yo F | 134lb | OR 73 | draw 1 | jockey Jason Watson | trainer Philip McBride (14d 0/1) | headgear - | last run 23 days | form 54246 | MARKET 21.1% | 09:00 median 4.33 | Matchbook 4.50
    comment: Princess Lottie is consistent, with a second three starts back and a fourth two runs ago, and she has run over today's trip, returning fresh after 23 days.
    DATA: model 18.9% | style Held up (led 3% of runs) | runs in data 5 | last 3: 4 Sep Haydock Flat 8f Heavy 2/4; 1 Oct Nottingham Flat 8.3f Good 4/7; 31 Oct Newmarket Flat 9f Good To Soft 6/10 fig 73
    DATA for: Best recent form figure 73, 12 lb above field average; Official rating 73, 6 lb above field average
    DATA against: Carries 6 lb more than average
- Orchard Hatches (hrs_17389819790) | 2yo F | 128lb | OR 67 | draw 2 | jockey Dougie Costello | trainer Marcus Tregoning (14d 1/2) | headgear - | last run 35 days | form 8335 | MARKET 19.9% | 09:00 median 4.50 | Matchbook 4.80
    comment: The one concern is that she is yet to win and has been off for 35 days.
    DATA: model 21.0% | style Midfield (led 23% of runs) | runs in data 4 | last 3: 13 Aug Salisbury Flat 8f Good 3/4; 12 Sep Bath Flat 8f Good 3/12; 19 Oct Pontefract Flat 8f Soft 5/11 fig 63
    DATA for: Last-run finishing speed +2.6% vs that field (finished strongly); Good recent finishing positions
- Distant Sun (hrs_17391095379) | 2yo G | 116lb | OR 55 | draw 4 | jockey Hollie Doyle | trainer Ed Dunlop (14d 1/2) | headgear - | last run 35 days | form 9809 | MARKET 12.6% | 09:00 median 6.50 | Matchbook 8.20
    comment: Distant Sun is hard to fancy, having finished ninth last time out and eighth three starts back, and he is winless in his last four.
    DATA: model 1.4% | style Held up (led 5% of runs) | runs in data 4 | last 3: 24 Sep Pontefract Flat 8f Good 8/9; 6 Oct Southwell Flat 7.1f Standard 13/13; 19 Oct Southwell (AW) Flat 7f Standard 9/14 fig 47
    DATA for: Carries 12 lb less than average
    DATA against: Best recent form figure 47, 14 lb below field average; Recent figures 8 lb below its current mark (looks high in the weights); Official rating 55, 12 lb below field average; Poor recent finishing positions
- Aquila d'Oro (hrs_17392932102) | 2yo F | 129lb | OR 68 | draw 6 | jockey Luke Morris | trainer Oliver Cole (14d 0/0) | headgear - | last run 19 days | form 055 | MARKET 8.3% | 09:00 median 11.00 | Matchbook 11.50
    comment: Aquila d'Oro is winless in her last three, finishing fifth last time out, and a fifth two starts back, with an unplaced effort before that, so it's hard to make a case on form.
    DATA: model 7.1% | style Leader (led 38% of runs) | runs in data 3 | last 3: 26 Sep Newmarket Flat 7f Good To Firm 10/10; 7 Oct Kempton Flat 7f Standard To Slow 5/12; 4 Nov Kempton (AW) Flat 8f Standard / Slow 5/12 fig 56
    DATA against: Best recent form figure 56, 4 lb below field average; Recent figures 12 lb below its current mark (looks high in the weights)
- Hello You Ten (hrs_66655519) | 2yo G | 123lb | OR 62 | draw 3 | jockey Kieran O'Neill | trainer Scott Dixon (14d 0/3) | headgear t | last run 35 days | form 303827 | MARKET 5.2% | 09:00 median 17.00 | Matchbook 19.50
    comment: The main risk is a seventh last time out and 35 days off, so he is yet to show he's back on song.
    DATA: model 14.0% | style Prominent (led 23% of runs) | runs in data 7 | last 3: 28 Sep Brighton Flat 8f Good To Firm 8/13; 8 Oct Southwell Flat 8.1f Standard 2/11; 19 Oct Wolverhampton (AW) Flat 7f Standard 7/12 fig 61

## 5:30 Wolverhampton (AW) | race_id rac_32305273806 | AWC Finals Day At Newcastle - 26th March EBF Maiden Stakes (GBB Race)
Flat | Class 4 | 6f20y | going Standard | AW | 12 runners | rating band - | age 2yo
DATA pace: Unclear - Running styles known for only 4 of 12 runners.
- Geometric (hrs_17389306634) | 2yo C | 133lb | OR - | draw 12 | jockey Joe Leavy | trainer Clive Cox (14d 0/4) | headgear t (1st time) | last run - days | form - | MARKET 32.5% | 09:00 median 2.50 | Matchbook 2.82
    DATA: model 7.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: First-time headgear
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Kodi Morse (hrs_17394846007) | 2yo C | 133lb | OR - | draw 5 | jockey Marco Ghiani | trainer Ismail Mohammed & Jose Santos (14d 0/1) | headgear h (1st time) | last run 20 days | form 3 | MARKET 24.0% | 09:00 median 3.50 | Matchbook 3.70
    DATA: model 13.6% | style Held up (led 8% of runs) | runs in data 1 | last 3: 3 Nov Wolverhampton (AW) Flat 5f Standard 3/8 fig 71
    DATA for: Best recent form figure 71, 11 lb above field average; First-time headgear
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on; Course: hold-up horses have won 0.7× their fair share at 6f here
- Casting Coach (hrs_17392696384) | 2yo F | 128lb | OR 71 | draw 4 | jockey Callum Rodriguez | trainer Ollie Sangster (14d 1/5) | headgear - | last run 20 days | form 344 | MARKET 12.3% | 09:00 median 6.50 | Matchbook 7.80
    DATA: model 17.7% | style Held up (led 5% of runs) | runs in data 3 | last 3: 24 Sep Pontefract Flat 6f Good 3/8; 8 Oct Bath Flat 5f Good 4/7; 3 Nov Wolverhampton (AW) Flat 5f Standard 4/8 fig 66
    DATA for: Best recent form figure 66, 6 lb above field average; Trainer 20% wins (1/5), last 14 days
    DATA against: Course: hold-up horses have won 0.7× their fair share at 6f here
- Queen of Christmas (hrs_65287243) | 2yo F | 128lb | OR - | draw 3 | jockey Clifford Lee | trainer K. R. Burke (14d 0/7) | headgear - | last run 152 days | form 54 | MARKET 10.1% | 09:00 median 7.50 | Matchbook 9.80
    DATA: model 6.8% | style Prominent (led 8% of runs) | runs in data 2 | last 3: 3 Jun Nottingham Flat 5f Good 5/10; 24 Jun Carlisle Flat 5f Good To Firm 4/4
    DATA against: Last-run finishing speed -2.5% vs that field (faded); Returns from a 152-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- Frontier Run (hrs_17395870233) | 2yo G | 133lb | OR - | draw 1 | jockey Kieran Shoemark | trainer Oliver Cole (14d 0/0) | headgear - | last run - days | form - | MARKET 6.6% | 09:00 median 12.00 | Matchbook 15.00
    DATA: model 7.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Incandescence (hrs_17394162842) | 2yo G | 133lb | OR - | draw 7 | jockey Finley Marsh | trainer Warren Greatrex (14d 6/20) | headgear - | last run - days | form - | MARKET 3.2% | 09:00 median 27.50 | Matchbook 36.00
    DATA: model 7.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 30% wins (6/20), last 14 days
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Girl From Havana (hrs_64556198) | 2yo F | 128lb | OR - | draw 9 | jockey Jack Doughty | trainer Dr Richard Newland (14d 1/6) | headgear - | last run - days | form - | MARKET 2.7% | 09:00 median 26.00 | Matchbook 46.00
    DATA: model 7.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Deshaies (hrs_17393586063) | 2yo G | 133lb | OR - | draw 8 | jockey Luke Morris | trainer Oliver Cole (14d 0/0) | headgear - | last run - days | form - | MARKET 2.5% | 09:00 median 34.00 | Matchbook 50.00
    DATA: model 7.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Tarragindi (hrs_17395113015) | 2yo G | 133lb | OR - | draw 11 | jockey Edward Greatrex | trainer Warren Greatrex (14d 6/20) | headgear - | last run - days | form - | MARKET 2.1% | 09:00 median 34.00 | Matchbook 55.00
    DATA: model 7.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 30% wins (6/20), last 14 days
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Purist (hrs_17394081488) | 2yo F | 128lb | OR - | draw 2 | jockey Stevie Donohoe | trainer Ollie Sangster (14d 1/5) | headgear h | last run 28 days | form 5 | MARKET 1.8% | 09:00 median 34.00 | Matchbook 85.00
    DATA: model 5.1% | style Held up (led 8% of runs) | runs in data 1 | last 3: 26 Oct Leicester Flat 6f Soft 5/6 fig 44
    DATA for: Trainer 20% wins (1/5), last 14 days
    DATA against: Best recent form figure 44, 16 lb below field average; Lightly raced: 1 run in our data, so the model has little to go on; Course: hold-up horses have won 0.7× their fair share at 6f here
- Lady Skipworth (hrs_60821012) | 2yo F | 128lb | OR - | draw 6 | jockey Lloyd Applegate(7) | trainer Dr Richard Newland (14d 1/6) | headgear - | last run 191 days | form 0 | MARKET 1.2% | 09:00 median 67.00 | Matchbook 100.00
    DATA: model 4.6% | style Unknown | runs in data 1 | last 3: 16 May Thirsk Flat 5f Good 11/12
    DATA against: Returns from a 191-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Maggie's Faith (hrs_17395871276) | 2yo C | 133lb | OR - | draw 10 | jockey Dougie Costello | trainer Steph Hollinshead (14d 0/3) | headgear - | last run - days | form - | MARKET 0.9% | 09:00 median 67.00 | Matchbook 200.00
    DATA: model 7.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on

## 6:00 Wolverhampton (AW) | race_id rac_32305275743 | Make The Move To Midnite Handicap Stakes
Flat | Class 6 | 5f21y | going Standard | AW | 10 runners | rating band 0-55 | age 3yo+
DATA pace: Lone leader - Our Planet is the only habitual front-runner and may be allowed an easy lead.
- Our Planet (hrs_45662183) | 4yo G | 139lb | OR 54 | draw 5 | jockey Kieran Shoemark | trainer James Owen (14d 3/40) | headgear t | last run 3 days | form 660781 | MARKET 54.3% | 09:00 median 1.53 | Matchbook 1.67
    DATA: model 16.9% | style Leader (led 38% of runs) | runs in data 7 | last 3: 13 Oct Wolverhampton Flat 6.1f Standard 7/12; 27 Oct Wolverhampton (AW) Flat 5f Standard 8/9 fig 48; 20 Nov Wolverhampton (AW) Flat 6f Standard 1/13 fig 60
    DATA for: Best recent form figure 60, 10 lb above field average; Recent figures 6 lb above its current mark (looks well handicapped); Has won at this trip or further; Pace: may get an uncontested lead
    DATA against: Carries 6 lb more than average
- Cabeza de Llave (hrs_27301694) | 7yo G | 131lb | OR 51 | draw 9 | jockey Alistair Rawlinson | trainer Michael Attwater (14d 1/6) | headgear - | last run 27 days | form 855441 | MARKET 9.0% | 09:00 median 9.00 | Matchbook 11.00
    comment: He carries 131 lb from draw 9.
    DATA: model 18.7% | style Midfield (led 4% of runs) | runs in data 11 | last 3: 16 Sep Sandown Flat 5f Good 4/10; 2 Oct Wolverhampton Flat 5.1f Standard 4/11; 27 Oct Wolverhampton (AW) Flat 5f Standard 1/9 fig 49
    DATA for: Has won at this trip or further
- Fancy Dancer (hrs_41090854) | 4yo F | 132lb | OR 52 | draw 3 | jockey Luke Morris | trainer Hayley Burton (14d 0/3) | headgear b | last run 20 days | form 022932 | MARKET 6.5% | 09:00 median 12.00 | Matchbook 15.50
    comment: Drawn three, she carries 132 lb.
    DATA: model 10.6% | style Midfield (led 8% of runs) | runs in data 11 | last 3: 2 Oct Wolverhampton Flat 5.1f Standard 9/11; 26 Oct Southwell (AW) Flat 5f Standard 3/10 fig 53; 3 Nov Wolverhampton (AW) Flat 5f Standard 2/9 fig 52
    DATA for: Good recent finishing positions
- Kiss Don't Tell (hrs_55700764) | 3yo F | 134lb | OR 54 | draw 2 | jockey Kyle McHugh(7) | trainer Nick Littmoden (14d 0/0) | headgear - | last run 27 days | form 2-8086 | MARKET 5.6% | 09:00 median 15.00 | Matchbook 16.50
    comment: The risk is a recent slide, with a sixth last time out and an eighth before that, while she's still yet to win in her last five.
    DATA: model 8.8% | style Midfield (led 4% of runs) | runs in data 4 | last 3: 22 Aug Curragh Flat 6f Good 17/27; 4 Sep Down Royal Flat 5f Good 8/12; 27 Oct Wolverhampton (AW) Flat 5f Standard 6/9 fig 49
    DATA against: Poor recent finishing positions
- Beach Partee (hrs_49141645) | 3yo G | 130lb | OR 50 | draw 6 | jockey Kieran O'Neill | trainer Scott Dixon (14d 0/3) | headgear v | last run 20 days | form 423044 | MARKET 5.4% | 09:00 median 15.00 | Matchbook 18.00
    comment: Beach Partee has finished fourth in each of his last two outings and returns after 20 days, having run over today's trip and going before, but he is yet to win in his last six starts.
    DATA: model 8.2% | style Midfield (led 23% of runs) | runs in data 19 | last 3: 17 Oct Southwell (AW) Flat 6f Standard 10/12 fig 40; 26 Oct Southwell (AW) Flat 5f Standard 4/9 fig 53; 3 Nov Wolverhampton (AW) Flat 5f Standard 4/9 fig 49
- Stash The Cash (hrs_36023372) | 5yo G | 131lb | OR 51 | draw 8 | jockey Charles Bishop | trainer Adam Kirby (14d 1/5) | headgear tb | last run 20 days | form 266283 | MARKET 5.3% | 09:00 median 13.00 | Matchbook 21.00
    comment: The risk is that he is yet to win in his last six starts, despite two seconds.
    DATA: model 10.6% | style Prominent (led 23% of runs) | runs in data 6 | last 3: 28 Apr Southwell Flat 5f Standard 2/8; 26 Oct Southwell (AW) Flat 5f Standard 8/10 fig 42; 3 Nov Wolverhampton (AW) Flat 5f Standard 3/9 fig 51
    DATA for: Trainer 20% wins (1/5), last 14 days; Good recent finishing positions
- Gustav Graves (hrs_24698562) | 8yo G | 135lb | OR 55 | draw 11 | jockey Jack Doughty | trainer Derek Shaw (14d 0/0) | headgear - | last run 27 days | form 423685 | MARKET 4.7% | 09:00 median 17.00 | Matchbook 21.00
    comment: The risk is a fading profile, as he has finished fifth, eighth and sixth in his last three and remains winless.
    DATA: model 6.3% | style Held up (led 8% of runs) | runs in data 11 | last 3: 20 Mar Wolverhampton Flat 5.1f Standard 6/9; 6 Apr Wolverhampton Flat 6.1f Standard 8/9; 27 Oct Wolverhampton (AW) Flat 5f Standard 5/9 fig 51
    DATA against: Aged 8, older than most of this field
- Piperstown (hrs_37260328) | 5yo G | 130lb | OR 50 | draw 7 | jockey Matthew Lloyd Slater(7) | trainer Kevin & Lauren Frost (14d 1/5) | headgear t | last run 16 days | form 115098 | MARKET 3.6% | 09:00 median 23.00 | Matchbook 27.00
    comment: Piperstown is hard to fancy after an eighth last time out and a ninth two starts back, a long way from the back-to-back wins five and six starts back.
    DATA: model 3.2% | style Midfield (led 4% of runs) | runs in data 11 | last 3: 12 Oct Newcastle Flat 6f Standard 12/12; 24 Oct Southwell (AW) Flat 6f Standard 9/11 fig 39; 7 Nov Southwell (AW) Flat 6f Standard 8/11 fig 41
    DATA for: Trainer 20% wins (1/5), last 14 days; Has won at this trip or further
    DATA against: Best recent form figure 41, 9 lb below field average; Recent figures 9 lb below its current mark (looks high in the weights); Poor recent finishing positions
- Bessie Wallis (hrs_55061930) | 3yo F | 133lb | OR 53 | draw 4 | jockey James Glennon(7) | trainer Michael Attwater (14d 1/6) | headgear - | last run 20 days | form 878266 | MARKET 2.9% | 09:00 median 23.00 | Matchbook 44.00
    comment: Bessie Wallis has run over today's trip and going and comes back after 20 days, but she is yet to win in her last six starts, with a second three starts back her best finish and two sixths since.
    DATA: model 10.3% | style Prominent (led 5% of runs) | runs in data 10 | last 3: 15 Oct Brighton Flat 6f Good 2/9 fig 58; 27 Oct Wolverhampton (AW) Flat 6f Standard 6/12 fig 49; 3 Nov Wolverhampton (AW) Flat 5f Standard 6/9 fig 50
    DATA for: Best recent form figure 58, 8 lb above field average; Recent figures 5 lb above its current mark (looks well handicapped)
- Bold Return (hrs_53743361) | 3yo F | 132lb | OR 52 | draw 1 | jockey Clifford Lee | trainer Steph Hollinshead (14d 0/3) | headgear - | last run 27 days | form 62-400 | MARKET 2.8% | 09:00 median 29.00 | Matchbook 42.00
    comment: Winless in her last five, Bold Return was unplaced last time out and two starts back, though a fourth three starts back and a second four starts back show some ability, and she has run over today's trip and going.
    DATA: model 6.4% | style Midfield (led 5% of runs) | runs in data 3 | last 3: 26 Mar Southwell Flat 5f Standard 4/12; 26 Apr Nottingham Flat 6.1f Good 14/15; 27 Oct Wolverhampton (AW) Flat 6f Standard 11/12 fig 36
    DATA against: Best recent form figure 36, 14 lb below field average; Recent figures 16 lb below its current mark (looks high in the weights)

## 6:30 Wolverhampton (AW) | race_id rac_32305277680 | Make The Move To Midnite Handicap Stakes
Flat | Class 5 | 1m4f51y | going Standard | AW | 12 runners | rating band 0-75 | age 3yo+
DATA pace: Strong pace - 3 habitual front-runners (Spirit of Jura, Dance Time, Helga). A contested lead should set things up for horses coming from behind.
- Barachiel (hrs_49695086) | 5yo G | 132lb | OR 68 | draw 12 | jockey Robert Havlin | trainer Robert Stephens (14d 0/4) | headgear - | last run 20 days | form 56621 | MARKET 28.4% | 09:00 median 2.88 | Matchbook 3.10
    comment: He has run over today's trip and going, and a 20-day break is no concern, yet it's a tough ask to fancy him.
    DATA: model 10.4% | style Midfield (led 29% of runs) | runs in data 7 | last 3: 29 Sep Wolverhampton Flat 7.2f Standard 6/10; 27 Oct Wolverhampton (AW) Flat 12f Standard 2/10 fig 65; 3 Nov Wolverhampton (AW) Flat 12f Standard 1/7 fig 64
    DATA for: Last-run finishing speed +2.7% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
- Saxophonist (hrs_55177605) | 3yo G | 133lb | OR 74 | draw 9 | jockey Callum Rodriguez | trainer David O'Meara (14d 0/12) | headgear - | last run 31 days | form 522721 | MARKET 21.6% | 09:00 median 3.75 | Matchbook 4.10
    comment: He has run over today's trip and going, and 31 days since his last run is fine, though 133 lb is a notable burden.
    DATA: model 17.7% | style Held up (led 4% of runs) | runs in data 8 | last 3: 23 Sep Redcar Flat 10f Good 7/12; 16 Oct Newcastle (AW) Flat 12.5f Standard 2/12 fig 74; 23 Oct Wolverhampton (AW) Flat 12f Standard 1/5 fig 77
    DATA for: Best recent form figure 77, 10 lb above field average; Has won at this trip or further; Good recent finishing positions; Pace: a contested lead should suit its hold-up style
    DATA against: Trainer 0 wins from 12 runs, last 14 days
- Kaaranah (hrs_22033354) | 8yo G | 139lb | OR 75 | draw 11 | jockey David Egan | trainer John Butler (14d 2/11) | headgear - | last run 27 days | form 511322 | MARKET 9.9% | 09:00 median 8.00 | Matchbook 9.20
    comment: Kaaranah arrives in cracking form, runner-up in each of his last two starts, a third three starts back, and a winner four and five starts back, with 27 days since his last run and experience of today's trip and going.
    DATA: model 13.5% | style Held up (led 3% of runs) | runs in data 11 | last 3: 13 Aug Lingfield Flat 10f Standard 3/8; 5 Oct Wolverhampton Flat 9.5f Standard 2/10; 27 Oct Wolverhampton (AW) Flat 9.5f Standard 2/8 fig 74
    DATA for: Best recent form figure 74, 7 lb above field average; Good recent finishing positions; Pace: a contested lead should suit its hold-up style
    DATA against: Carries 5 lb more than average; Aged 8, older than most of this field
- Charlie's Choice (hrs_34775195) | 6yo G | 136lb | OR 72 | draw 5 | jockey Taryn Langley(5) | trainer David Simcock (14d 0/6) | headgear - | last run 27 days | form 704487 | MARKET 7.2% | 09:00 median 11.00 | Matchbook 12.50
    comment: The risk is his current slide, a seventh last time out and an eighth before that, leaving him winless in his last six.
    DATA: model 4.3% | style Held up (led 3% of runs) | runs in data 14 | last 3: 18 Jun Yarmouth Flat 10.1f Good To Firm 4/6; 14 Oct Kempton (AW) Flat 11f Standard / Slow 8/13 fig 71; 27 Oct Wolverhampton (AW) Flat 12f Standard 7/10 fig 67
    DATA for: Best recent form figure 71, 4 lb above field average; Has won at this trip or further; Pace: a contested lead should suit its hold-up style
- Magician of Riga (hrs_52054765) | 3yo G | 130lb | OR 71 | draw 3 | jockey Sean Levey | trainer Richard Hannon (14d 1/9) | headgear - | last run 21 days | form 113556 | MARKET 7.0% | 09:00 median 11.00 | Matchbook 13.50
    comment: Twice a winner in his last six starts, Magician of Riga has since cooled to a fifth, a fifth and a sixth last time out, though he has run over today's trip and going and returns after 21 days.
    DATA: model 6.7% | style Midfield (led 3% of runs) | runs in data 8 | last 3: 9 Jul Newbury Flat 10f Good To Firm 5/7; 5 Oct Wolverhampton Flat 9.5f Standard 5/11; 2 Nov Chelmsford (AW) Flat 10f Standard 6/8 fig 59
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 59, 8 lb below field average; Recent figures 12 lb below its current mark (looks high in the weights)
- Aleen (hrs_54555375) | 3yo F | 131lb | OR 72 | draw 4 | jockey Luke Morris | trainer Sir Mark Prescott Bt (14d 0/5) | headgear - | last run 368 days | form 32512- | MARKET 6.0% | 09:00 median 11.00 | Matchbook 18.00
    comment: Aleen arrives on a good run, second last time out and a winner two starts back, with a fifth three starts back the only blip in her last five, and she has run on today's going before.
    DATA: model 8.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 368-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Dance Time (hrs_32401810) | 6yo M | 134lb | OR 70 | draw 2 | jockey Laura Pearson | trainer David Loughnane (14d 2/5) | headgear - | last run 80 days | form 73V234 | MARKET 6.0% | 09:00 median 12.00 | Matchbook 17.00
    comment: Dance Time has been consistent without winning, finishing fourth last time out after a third and a second before that, and she has run over today's trip and going before.
    DATA: model 9.6% | style Leader (led 38% of runs) | runs in data 8 | last 3: 11 Aug Carlisle Flat 14.1f Good 2/6; 18 Aug Wolverhampton Flat 14f Standard 3/9; 4 Sep Haydock Flat 14f Heavy 4/8
    DATA for: Trainer 40% wins (2/5), last 14 days; Good recent finishing positions
    DATA against: Pace: likely to be taken on for the lead
- Seventy (hrs_39960424) | 4yo G | 134lb | OR 70 | draw 7 | jockey Kieran Shoemark | trainer Sam England (14d 5/22) | headgear - | last run 150 days | form 331212 | MARKET 5.0% | 09:00 median 15.00 | Matchbook 19.50
    comment: Seventy has banked a second last time out and two wins in his last six starts, with every run in the frame, but a 150-day absence and 134 lb are real concerns.
    DATA: model 7.9% | style Held up (led 3% of runs) | runs in data 8 | last 3: 25 May Windsor Flat 11.4f Good To Firm 2/3; 15 Jun Windsor Flat 11.4f Good To Firm 1/7; 26 Jun Newmarket Flat 12f Good To Firm 2/4
    DATA for: Trainer 23% wins (5/22), last 14 days; Has won at this trip or further; Good recent finishing positions; Pace: a contested lead should suit its hold-up style
    DATA against: Returns from a 150-day break
- Melody de Vega (hrs_56591052) | 3yo F | 132lb | OR 73 | draw 8 | jockey Hollie Doyle | trainer Tom Ward (14d 0/2) | headgear - | last run 44 days | form 821630 | MARKET 3.1% | 09:00 median 23.00 | Matchbook 38.00
    comment: Unplaced last time out after a third two starts back, she won four starts back and has run over today's trip and going, but a 44-day break and 132 lb leave questions.
    DATA: model 7.9% | style Prominent (led 8% of runs) | runs in data 8 | last 3: 29 Jul Sandown Flat 9.9f Good To Firm 6/10; 24 Sep Southwell Flat 11.1f Standard 3/12; 10 Oct Southwell Flat 12.1f Standard 11/11
- Spirit of Jura (hrs_46450425) | 4yo F | 139lb | OR 75 | draw 1 | jockey Callum Shepherd | trainer Charlie Johnston (14d 0/6) | headgear v (1st time) | last run 48 days | form 525366 | MARKET 2.3% | 09:00 median 29.00 | Matchbook 50.00
    comment: Yet to win in her last six, Spirit of Jura has still been a third three starts back and a second five starts back, and she has run over today's trip and going before.
    DATA: model 2.7% | style Leader (led 79% of runs) | runs in data 8 | last 3: 17 Jul Hamilton Flat 12.1f Good To Firm 3/3; 2 Sep Bath Flat 11.6f Good 6/6; 6 Oct Southwell Flat 12.1f Standard 6/6
    DATA for: First-time headgear
    DATA against: Carries 5 lb more than average; Pace: likely to be taken on for the lead
- Three Dons (hrs_23568321) | 7yo G | 131lb | OR 67 | draw 10 | jockey Molly Gunn(5) | trainer Tony Carroll (14d 1/26) | headgear - | last run 240 days | form 8940-9 | MARKET 2.0% | 09:00 median 29.00 | Matchbook 85.00
    comment: Three Dons has been well beaten in recent starts, finishing ninth last time out and without a win in his last five, and he returns after 240 days off with a yard out of form.
    DATA: model 6.0% | style Prominent (led 5% of runs) | runs in data 3 | last 3: 20 Jan Leicester Hurdle 15.5f Heavy 3/12; 9 Feb Catterick Hurdle 15.7f Soft 2/7; 28 Mar Doncaster Flat 10.2f Good To Soft 9/14
    DATA for: Good recent finishing positions
    DATA against: Returns from a 240-day break
- Helga (hrs_59831247) | 3yo F | 133lb | OR 74 | draw 6 | jockey George Bass | trainer Jack Channon (14d 0/6) | headgear - | last run 25 days | form 8-150 | MARKET 1.4% | 09:00 median 41.00 | Matchbook 110.00
    comment: Helga is hard to fancy, unplaced last time out and a fifth two starts back, with her one win three starts back now fading, and she carries 133 lb off an official mark of 74.
    DATA: model 5.0% | style Leader (led 38% of runs) | runs in data 3 | last 3: 19 Jan Kempton Flat 11f Standard To Slow 1/9; 25 Feb Kempton Flat 11f Standard To Slow 5/5; 29 Oct Bath Flat 10f Soft 11/12 fig 54
    DATA against: Best recent form figure 54, 13 lb below field average; Recent figures 20 lb below its current mark (looks high in the weights); Last-run finishing speed -3.2% vs that field (faded); Pace: likely to be taken on for the lead

## 7:00 Wolverhampton (AW) | race_id rac_32305279617 | AWC Season 14 Has Begun Handicap Stakes (Div I)
Flat | Class 6 | 7f36y | going Standard | AW | 12 runners | rating band 0-65 | age 3yo+
DATA pace: Even - Two likely leaders (Crown The Future, On Key). A fair, even gallop is most likely.
- Ridger (hrs_65549820) | 3yo G | 134lb | OR 62 | draw 3 | jockey Stevie Donohoe | trainer Ollie Sangster (14d 1/5) | headgear t | last run 16 days | form 231122 | MARKET 18.4% | 09:00 median 4.50 | Matchbook 4.90 | CHECK (skip line 4.27)
    comment: Ridger's recent form is hard to knock, with a second last time out, another second two starts back and a winner three starts back, and he's fresh enough after 16 days.
    DATA: model 18.5% | style Midfield (led 3% of runs) | runs in data 10 | last 3: 5 Oct Kempton Flat 7f Standard To Slow 1/10; 27 Oct Wolverhampton (AW) Flat 7f Standard 2/9 fig 57; 7 Nov Southwell (AW) Flat 7f Standard 2/12 fig 66
    DATA for: Best recent form figure 66, 9 lb above field average; Recent figures 4 lb above its current mark (looks well handicapped); Trainer 20% wins (1/5), last 14 days; Has won at this trip or further; Good recent finishing positions
- Dark Mandate (hrs_53294423) | 3yo G | 135lb | OR 63 | draw 7 | jockey Charles Bishop | trainer Eve Johnson Houghton (14d 1/2) | headgear p (1st time) | last run 21 days | form -42124 | MARKET 15.7% | 09:00 median 5.00 | Matchbook 5.90
    comment: Dark Mandate has been consistent, with a fourth last time out, a second two starts back and a win three starts back, and he has run over today's trip and going before. A 21-day break is fine, but 135 lb from draw 7 and an official mark of 63 leave little margin in a fairly open race.
    DATA: model 14.6% | style Midfield (led 5% of runs) | runs in data 5 | last 3: 29 Sep Wolverhampton Flat 7.2f Standard 1/10; 21 Oct Kempton (AW) Flat 7f Standard / Slow 2/10 fig 62; 2 Nov Chelmsford (AW) Flat 7f Standard 4/13 fig 69
    DATA for: Best recent form figure 69, 12 lb above field average; Recent figures 6 lb above its current mark (looks well handicapped); Last-run finishing speed +4.6% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions; First-time headgear
- Giorgio M (hrs_37276246) | 5yo G | 142lb | OR 64 | draw 1 | jockey Hope Regan(7) | trainer Mark Loughnane (14d 2/11) | headgear tp | last run 2 days | form 777911 | MARKET 13.8% | 09:00 median 5.50 | Matchbook 7.20
    comment: Giorgio M arrives in top form, winning last time out and again two starts back, and he's fit after just two days off.
    DATA: model 14.6% | style Midfield (led 23% of runs) | runs in data 11 | last 3: 2 Jul Kempton Flat 6f Standard To Slow 9/11; 16 Nov Wolverhampton (AW) Flat 7f Standard 1/11 fig 72; 21 Nov Lingfield (AW) Flat 6f Standard 1/10 fig 67
    DATA for: Best recent form figure 72, 15 lb above field average; Recent figures 8 lb above its current mark (looks well handicapped); Has won at this trip or further; Good recent finishing positions
    DATA against: Carries 8 lb more than average
- Montpellier Green (hrs_39960333) | 4yo G | 122lb | OR 49 | draw 6 | jockey Edward Greatrex | trainer Ian Williams (14d 2/14) | headgear p | last run 17 days | form 00-856 | MARKET 11.6% | 09:00 median 7.00 | Matchbook 7.80
    comment: He has run over today's trip and going, and a 17-day turnaround keeps him fit, but that's about all he has going for him.
    DATA: model 5.0% | style Held up (led 5% of runs) | runs in data 3 | last 3: 10 Jul Chester Flat 7f Good 8/10; 2 Oct Wolverhampton Flat 6.1f Standard 5/10; 6 Nov Newcastle (AW) Flat 6f Standard 6/14 fig 49
    DATA for: Carries 12 lb less than average
    DATA against: Best recent form figure 49, 8 lb below field average; Official rating 49, 12 lb below field average
- Crown The Future (hrs_56007973) | 3yo G | 133lb | OR 61 | draw 8 | jockey Charlie Tucker(7) | trainer Tony Carroll (14d 1/26) | headgear - | last run 16 days | form 521221 | MARKET 11.3% | 09:00 median 7.00 | Matchbook 8.40
    comment: Crown The Future won last time out and has finished first or second in five of his last six, with a fresh 16-day turnaround and experience of today's trip and going.
    DATA: model 13.5% | style Leader (led 43% of runs) | runs in data 11 | last 3: 24 Oct Southwell (AW) Flat 8f Standard 2/13 fig 59; 28 Oct Kempton (AW) Flat 8f Standard / Slow 2/6 fig 62; 7 Nov Southwell (AW) Flat 7f Standard 1/12 fig 64
    DATA for: Best recent form figure 64, 7 lb above field average; Has won at this trip or further; Good recent finishing positions
- Because We Can (hrs_54494447) | 3yo G | 137lb | OR 65 | draw 9 | jockey Clifford Lee | trainer Michael Keady (14d 0/2) | headgear b (1st time) | last run 47 days | form -15953 | MARKET 7.5% | 09:00 median 10.00 | Matchbook 13.50
    comment: The main risk is a 47-day absence, with a ninth three starts back showing his form has been patchy.
    DATA: model 7.2% | style Midfield (led 4% of runs) | runs in data 5 | last 3: 27 Mar Lingfield Flat 7f Standard 9/10; 24 Sep Southwell Flat 7.1f Standard 5/9; 7 Oct Kempton Flat 7f Standard To Slow 3/14
    DATA for: Has won at this trip or further; First-time headgear
- Lessay (hrs_36062047) | 5yo G | 133lb | OR 60 | draw 10 | jockey Paddy Bradley | trainer Patrick Morris (14d 0/9) | headgear p | last run 7 days | form 261485 | MARKET 6.3% | 09:00 median 12.00 | Matchbook 16.50
    comment: Lessay has a win four starts back and a fifth last time out, but he's been beaten in the last two, and he's back quickly after just seven days.
    DATA: model 3.5% | style Held up (led 4% of runs) | runs in data 15 | last 3: 2 Sep Newcastle Flat 7.1f Standard 4/12; 25 Sep Newcastle Flat 7.1f Standard 8/11; 16 Nov Wolverhampton (AW) Flat 7f Standard 5/11 fig 63
    DATA for: Best recent form figure 63, 6 lb above field average; Last-run finishing speed +2.8% vs that field (finished strongly); Has won at this trip or further
    DATA against: Trainer 0 wins from 9 runs, last 14 days
- Spirit of Jenny (hrs_53116322) | 4yo F | 135lb | OR 62 | draw 2 | jockey Dougie Costello | trainer Steph Hollinshead (14d 0/3) | headgear - | last run 18 days | form 128556 | MARKET 4.5% | 09:00 median 15.00 | Matchbook 24.00
    comment: Spirit of Jenny's recent form is modest, with a sixth last time out, but she has run over today's trip and going and is fresh enough after 18 days.
    DATA: model 8.0% | style Held up (led 3% of runs) | runs in data 7 | last 3: 14 Aug Newmarket Flat 6f Good To Firm 5/12; 13 Oct Leicester Flat 6f Good To Soft 5/18; 5 Nov Southwell (AW) Flat 7f Standard 6/10 fig 56
    DATA against: Recent figures 6 lb below its current mark (looks high in the weights)
- On Key (hrs_44417639) | 4yo G | 130lb | OR 57 | draw 5 | jockey Kieran O'Neill | trainer Scott Dixon (14d 0/3) | headgear p | last run 27 days | form 237429 | MARKET 3.3% | 09:00 median 21.00 | Matchbook 34.00
    comment: On Key is yet to win in his last six, but a second two starts back and a third five starts back show he's capable of going close, and he has run over today's trip and going.
    DATA: model 3.7% | style Leader (led 23% of runs) | runs in data 20 | last 3: 10 Sep Lingfield Flat 7f Standard 4/10; 13 Oct Wolverhampton Flat 6.1f Standard 2/12; 27 Oct Wolverhampton (AW) Flat 7f Standard 9/9 fig 41
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 41, 16 lb below field average; Recent figures 16 lb below its current mark (looks high in the weights)
- State of Madness (hrs_41565055) | 5yo G | 138lb | OR 65 | draw 12 | jockey Luke Morris | trainer Mark Loughnane (14d 2/11) | headgear - | last run 95 days | form 345248 | MARKET 3.2% | 09:00 median 23.00 | Matchbook 38.00
    comment: The risk is a last-time-out eighth and a 95-day absence, so fitness is the question.
    DATA: model 5.4% | style Prominent (led 5% of runs) | runs in data 10 | last 3: 22 Jun Brighton Flat 7f Good To Firm 2/5; 6 Aug Brighton Flat 7f Good To Firm 4/6; 20 Aug Lingfield Flat 7f Standard 8/11
    DATA against: Returns from a 95-day break
- Chifa (hrs_25263357) | 9yo G | 136lb | OR 63 | draw 11 | jockey Finley Marsh | trainer Ed de Giles (14d 0/1) | headgear - | last run 162 days | form 907690 | MARKET 2.2% | 09:00 median 34.00 | Matchbook 44.00
    comment: Winless in his last six, Chifa has finished unplaced last time out and no better than a sixth three starts back, and he returns after 162 days off.
    DATA: model 2.4% | style Midfield (led 3% of runs) | runs in data 7 | last 3: 14 Apr Lingfield Flat 7f Standard 6/11; 2 May Doncaster Flat 7f Good To Firm 9/10; 14 Jun Doncaster Flat 7f Good 10/12
    DATA for: Has won at this trip or further
    DATA against: Poor recent finishing positions; Returns from a 162-day break; Aged 9, older than most of this field
- Punchbowl Flyer (hrs_19138861) | 9yo G | 133lb | OR 60 | draw 4 | jockey Alexandra Egan(5) | trainer John O'Shea (14d 0/1) | headgear b | last run 25 days | form 167450 | MARKET 2.2% | 09:00 median 34.00 | Matchbook 46.00
    comment: Punchbowl Flyer is hard to fancy, unplaced last time out and with a fifth, a fourth, a seventh and a sixth in the four runs before that, his one win coming six starts back.
    DATA: model 3.6% | style Prominent (led 23% of runs) | runs in data 17 | last 3: 7 Sep Windsor Flat 6.1f Good 4/13; 28 Sep Hamilton Flat 6f Soft 5/6; 29 Oct Bath Flat 5.5f Soft 11/12 fig 33
    DATA against: Best recent form figure 33, 24 lb below field average; Recent figures 27 lb below its current mark (looks high in the weights); Last-run finishing speed -3.8% vs that field (faded); Aged 9, older than most of this field

## 7:30 Wolverhampton (AW) | race_id rac_32305281554 | AWC Season 14 Has Begun Handicap Stakes (Div II)
Flat | Class 6 | 7f36y | going Standard | AW | 11 runners | rating band 0-65 | age 3yo+
DATA pace: Strong pace - 3 habitual front-runners (Beauzon, Girls Allowed, Lhebayeb). A contested lead should set things up for horses coming from behind.
- Yehudi (hrs_41662271) | 4yo G | 138lb | OR 65 | draw 10 | jockey Jonny Peate | trainer Mark Loughnane (14d 2/11) | headgear t/bes | last run 7 days | form 461316 | MARKET 20.6% | 09:00 median 4.00 | Matchbook 4.30 | CHECK (skip line 3.80)
    comment: Yehudi has won twice in his last six starts, including a victory two starts back, and he's back quickly after just seven days, having run over today's trip and on the going before.
    DATA: model 18.3% | style Prominent (led 3% of runs) | runs in data 10 | last 3: 4 Jun Lingfield Flat 7f Standard 3/12; 23 Oct Wolverhampton (AW) Flat 8.5f Standard 1/10 fig 62; 16 Nov Wolverhampton (AW) Flat 8.5f Standard 6/12 fig 60
    DATA for: Official rating 65, 5 lb above field average; Has won at this trip or further; Good recent finishing positions
    DATA against: Carries 6 lb more than average
- Good Karma (hrs_29736280) | 6yo G | 132lb | OR 59 | draw 6 | jockey Ethan Tindall(5) | trainer John David Riches (14d 0/0) | headgear p | last run 16 days | form 343366 | MARKET 17.0% | 09:00 median 4.50 | Matchbook 5.50
    comment: Good Karma is winless in his last six, though he was third three and four starts back and has run over today's trip and going, while two sixths since leave him with questions.
    DATA: model 7.8% | style Midfield (led 23% of runs) | runs in data 14 | last 3: 17 Sep Pontefract Flat 6f Good 3/12; 26 Sep Ripon Flat 6f Good 6/11; 7 Nov Southwell (AW) Flat 8f Standard 6/11 fig 54
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 54, 5 lb below field average
- Girls Allowed (hrs_55700939) | 3yo F | 134lb | OR 62 | draw 5 | jockey Dylan Hogan | trainer Julia & Shelley Birkett (14d 0/0) | headgear - | last run 26 days | form 629011 | MARKET 16.7% | 09:00 median 4.50 | Matchbook 5.80
    comment: She has run over today's trip, yet the weight looks a stiff ask.
    DATA: model 15.2% | style Prominent (led 43% of runs) | runs in data 7 | last 3: 12 Sep Bath Flat 8f Good 11/14; 9 Oct Kempton Flat 8f Standard To Slow 1/13; 28 Oct Kempton (AW) Flat 8f Standard / Slow 1/10 fig 71
    DATA for: Best recent form figure 71, 12 lb above field average; Recent figures 9 lb above its current mark (looks well handicapped); Has won at this trip or further; Good recent finishing positions
- Jamie Sommers (hrs_54027211) | 3yo F | 135lb | OR 63 | draw 8 | jockey Hollie Doyle | trainer David Loughnane (14d 2/5) | headgear - | last run 21 days | form 340303 | MARKET 10.5% | 09:00 median 7.50 | Matchbook 8.80
    comment: Jamie Sommers arrives in decent heart after a third last time out, and she has run over today's trip and on the going before.
    DATA: model 7.8% | style Prominent (led 23% of runs) | runs in data 9 | last 3: 3 Jun Nottingham Flat 8.3f Good 3/10; 19 Jun Newmarket Flat 8f Good 10/10; 2 Nov Wolverhampton (AW) Flat 8.5f Standard 3/8 fig 60
    DATA for: Trainer 40% wins (2/5), last 14 days; Good recent finishing positions
- Monsieur Patat (hrs_21686462) | 9yo G | 137lb | OR 64 | draw 4 | jockey Finley Marsh | trainer Adrian Wintle (14d 0/2) | headgear - | last run 19 days | form 275322 | MARKET 10.4% | 09:00 median 8.00 | Matchbook 8.80
    comment: Monsieur Patat has finished second in each of his last two starts, a third three starts back too, and he returns after 19 days having run over today's trip and going.
    DATA: model 18.0% | style Midfield (led 4% of runs) | runs in data 7 | last 3: 7 Sep Windsor Flat 6.1f Good 3/13; 29 Sep Bath Flat 5.7f Good To Firm 2/9; 4 Nov Kempton (AW) Flat 6f Standard / Slow 2/11 fig 66
    DATA for: Best recent form figure 66, 7 lb above field average; Good recent finishing positions
    DATA against: Aged 9, older than most of this field
- Profit Street (hrs_36738660) | 5yo G | 136lb | OR 63 | draw 2 | jockey Taryn Langley(5) | trainer Joey Ramsden (14d 0/1) | headgear - | last run 44 days | form 235766 | MARKET 8.0% | 09:00 median 10.00 | Matchbook 11.50
    comment: The risk is form that has tailed off, with a sixth last time out and another sixth two starts back, after a second six starts back.
    DATA: model 4.7% | style Held up (led 3% of runs) | runs in data 13 | last 3: 18 May Lingfield Flat 6f Good 7/7; 24 Sep Southwell Flat 7.1f Standard 6/9; 10 Oct Southwell Flat 6.1f Standard 6/9
    DATA for: Has won at this trip or further; Pace: a contested lead should suit its hold-up style
    DATA against: Poor recent finishing positions
- Chapman's Peak (hrs_55978566) | 3yo G | 134lb | OR 62 | draw 3 | jockey Kaiya Fraser | trainer Ed Dunlop (14d 1/2) | headgear - | wind surgery | last run 61 days | form 884230 | MARKET 6.1% | 09:00 median 13.00 | Matchbook 16.00
    comment: On the plus side, he was third two starts back and second three back, and he has run over today's trip and going.
    DATA: model 10.6% | style Midfield (led 5% of runs) | runs in data 7 | last 3: 15 Aug Lingfield Flat 8f Standard 2/6; 2 Sep Kempton Flat 7f Standard To Slow 3/6; 23 Sep Kempton Flat 7f Standard To Slow 13/13
    DATA for: Good recent finishing positions
    DATA against: Last-run finishing speed -3.2% vs that field (faded)
- Lhebayeb (hrs_22487976) | 8yo M | 119lb | OR 46 | draw 1 | jockey Rose Dawes(3) | trainer Richard Price (14d 0/0) | headgear - | last run 41 days | form 094443 | MARKET 3.0% | 09:00 median 23.00 | Matchbook 40.00
    comment: Lhebayeb is winless in her last six, though a third last time out, after three fourths in the previous four runs, shows she is rarely far away, and she has run over today's trip and going.
    DATA: model 3.9% | style Leader (led 29% of runs) | runs in data 12 | last 3: 28 Jul Ffos Las Flat 8f Good 4/7; 29 Sep Wolverhampton Flat 8.6f Standard 4/8; 13 Oct Wolverhampton Flat 7.2f Standard 3/9
    DATA for: Has won at this trip or further; Carries 13 lb less than average
    DATA against: Official rating 46, 14 lb below field average; Pace: likely to be taken on for the lead
- Beauzon (hrs_24506272) | 7yo G | 137lb | OR 64 | draw 11 | jockey Ryan Kavanagh(3) | trainer Ian Williams (14d 2/14) | headgear - | last run 26 days | form 000060 | MARKET 2.9% | 09:00 median 27.50 | Matchbook 42.00
    comment: Beauzon is hard to fancy, unplaced in five of his last six starts and yet to win in that spell, with a sixth two starts back his best finish.
    DATA: model 2.4% | style Leader (led 54% of runs) | runs in data 19 | last 3: 3 Oct Southwell Flat 6.1f Standard 13/13; 17 Oct Southwell (AW) Flat 7f Standard 6/9 fig 59; 28 Oct Kempton (AW) Flat 7f Standard / Slow 11/13 fig 51
    DATA against: Poor recent finishing positions; Pace: likely to be taken on for the lead
- Romanovich (hrs_30344804) | 7yo G | 122lb | OR 49 | draw 9 | jockey Connor Planas | trainer John O'Shea (14d 0/1) | headgear b | last run 20 days | form 357056 | MARKET 2.7% | 09:00 median 33.00 | Matchbook 40.00
    comment: Romanovich has been mostly well beaten of late, with a sixth last time out and a fifth two starts back, and he's yet to win in his last six outings.
    DATA: model 2.2% | style Held up (led 5% of runs) | runs in data 12 | last 3: 16 Jul Chepstow Flat 7.1f Good To Firm 10/12; 28 Sep Wolverhampton Flat 7.2f Standard 5/11; 3 Nov Wolverhampton (AW) Flat 7f Standard 6/11 fig 43
    DATA for: Has won at this trip or further; Carries 10 lb less than average; Pace: a contested lead should suit its hold-up style
    DATA against: Best recent form figure 43, 16 lb below field average; Recent figures 6 lb below its current mark (looks high in the weights); Official rating 49, 11 lb below field average
- Mr Tony (hrs_50433537) | 3yo G | 133lb | OR 61 | draw 7 | jockey William Carson | trainer Tony Carroll (14d 1/26) | headgear - | last run 31 days | form 3-1470 | MARKET 2.3% | 09:00 median 34.00 | Matchbook 48.00
    comment: Mr Tony won four starts back but has faded since, with an unplaced effort last time and a seventh two starts back, though he has run over today's trip and going before. A 31-day break and a cold stable (1/26 in the last 14 days) temper the appeal from stall 7.
    DATA: model 9.1% | style Midfield (led 4% of runs) | runs in data 4 | last 3: 13 Sep Bath Flat 8f Good To Soft 4/10; 14 Oct Nottingham Flat 8.5f Good To Soft 7/10 fig 55; 23 Oct Wolverhampton (AW) Flat 8.5f Standard 10/11 fig 33
    DATA for: Has won at this trip or further
    DATA against: Recent figures 6 lb below its current mark (looks high in the weights)

## 8:00 Wolverhampton (AW) | race_id rac_32305283491 | AWC Trials Day - Lingfield 2nd January 2027 Handicap Stakes
Flat | Class 4 | 7f36y | going Standard | AW | 11 runners | rating band 0-85 | age 3yo+
DATA pace: Lone leader - King's Vanity is the only habitual front-runner and may be allowed an easy lead.
- Monarch's Gold (hrs_56219422) | 3yo G | 139lb | OR 87 | draw 5 | jockey Rowan Scott | trainer Kevin Philippart de Foy (14d 2/7) | headgear - | last run 52 days | form 293565 | MARKET 23.5% | 09:00 median 3.50 | Matchbook 3.90 | CHECK (skip line 3.32)
    comment: Monarch's Gold is yet to win in his last six, but he has run over today's trip and going, and a third four starts back and a second six starts back show he can get involved.
    DATA: model 12.1% | style Midfield (led 4% of runs) | runs in data 9 | last 3: 2 Aug Chester Flat 7f Good 5/10; 29 Aug Sandown Flat 7f Good To Soft 6/8; 2 Oct Ascot Flat 8f Good To Firm 5/9
    DATA for: Official rating 87, 7 lb above field average; Trainer 29% wins (2/7), last 14 days
    DATA against: Carries 6 lb more than average
- Pietro (hrs_41189743) | 4yo G | 133lb | OR 80 | draw 2 | jockey Daniel Muscutt | trainer James Fanshawe (14d 0/9) | headgear p (1st time) | last run 34 days | form 130733 | MARKET 18.0% | 09:00 median 4.50 | Matchbook 5.20
    comment: Pietro was third last time out and third two starts back, so he arrives consistent, and he has run over today's trip and going before; against that, he's only won once in his last six starts and a 34-day break leaves fitness a question. Drawn two and carrying 133 lb off 80, he looks a midfield sort.
    DATA: model 15.3% | style Held up (led 4% of runs) | runs in data 6 | last 3: 27 Aug Southwell Flat 7.1f Standard 7/11; 13 Sep Doncaster Flat 6.5f Good 3/13; 20 Oct Yarmouth Flat 7f Soft 3/9 fig 77
    DATA for: Best recent form figure 77, 8 lb above field average; Has won at this trip or further; Good recent finishing positions; First-time headgear
    DATA against: Trainer 0 wins from 9 runs, last 14 days
- The Watcher (hrs_48447280) | 4yo G | 139lb | OR 86 | draw 8 | jockey Clifford Lee | trainer K. R. Burke (14d 0/7) | headgear - | last run 586 days | form 1/19- | MARKET 17.1% | 09:00 median 4.50 | Matchbook 5.80
    comment: The Watcher won two starts back and three starts back, but he was only ninth last time out and returns after a 586-day absence.
    DATA: model 11.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Official rating 86, 6 lb above field average
    DATA against: Carries 6 lb more than average; Returns from a 586-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Drifts Away (hrs_37027039) | 5yo G | 134lb | OR 81 | draw 7 | jockey Kieran Shoemark | trainer T. J. Kent (14d 0/6) | headgear b | last run 28 days | form 711926 | MARKET 12.1% | 09:00 median 7.10 | Matchbook 7.40
    comment: Drifts Away won twice in his last six starts, though a sixth last time out and a ninth three starts back show a patchy recent record.
    DATA: model 17.4% | style Prominent (led 4% of runs) | runs in data 6 | last 3: 19 Sep Newmarket Flat 9f Good 9/14; 5 Oct Yarmouth Flat 8f Good To Firm 2/11; 26 Oct Kempton (AW) Flat 8f Standard / Slow 6/13 fig 81
    DATA for: Best recent form figure 81, 12 lb above field average; Has won at this trip or further
- Reciprocated (hrs_52054254) | 3yo G | 129lb | OR 77 | draw 9 | jockey Hollie Doyle | trainer David Loughnane (14d 2/5) | headgear t | last run 21 days | form 000652 | MARKET 8.2% | 09:00 median 9.00 | Matchbook 13.00
    comment: Reciprocated bounced back to form with a second last time out, and at 21 days since that run he should be fresh, having run over today's trip and going before.
    DATA: model 9.6% | style Prominent (led 23% of runs) | runs in data 8 | last 3: 5 Oct Wolverhampton Flat 7.2f Standard 6/11; 19 Oct Wolverhampton (AW) Flat 7f Standard 5/12 fig 78; 2 Nov Wolverhampton (AW) Flat 7f Standard 2/7 fig 73
    DATA for: Best recent form figure 78, 9 lb above field average; Trainer 40% wins (2/5), last 14 days
- Shah (hrs_43984220) | 4yo G | 140lb | OR 87 | draw 4 | jockey Charles Bishop | trainer Alan King (14d 2/18) | headgear h (1st time) | wind surgery | last run 191 days | form 2221/0 | MARKET 5.7% | 09:00 median 15.00 | Matchbook 16.00
    comment: The risk is a 191-day absence, plus an unplaced effort last time out.
    DATA: model 7.5% | style Unknown | runs in data 1 | last 3: 16 May Newmarket Flat 7f Good 11/11
    DATA for: Official rating 87, 7 lb above field average; First-time headgear
    DATA against: Last-run finishing speed -5.0% vs that field (faded); Carries 7 lb more than average; Returns from a 191-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Treasure Time (hrs_34472669) | 5yo G | 135lb | OR 82 | draw 1 | jockey Marco Ghiani | trainer John & Sean Quinn (14d 1/6) | headgear - | last run 47 days | form 040-08 | MARKET 5.5% | 09:00 median 15.00 | Matchbook 17.00
    comment: The main risk is a poor recent book: an eighth last time out and winless in his last five starts, after 47 days off.
    DATA: model 4.9% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 12 Sep Doncaster Flat 8f Good 17/17; 7 Oct Nottingham Flat 8.3f Good To Soft 8/9
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Jez Bomb (hrs_36999998) | 5yo G | 130lb | OR 77 | draw 11 | jockey Jonny Peate | trainer Sam England (14d 5/22) | headgear - | last run 28 days | form 175685 | MARKET 3.7% | 09:00 median 21.00 | Matchbook 27.00
    comment: He has run over today's trip and going, and 28 days off is fine, but 130 lb from stall 11 is a lot to ask.
    DATA: model 8.4% | style Held up (led 4% of runs) | runs in data 15 | last 3: 24 Sep Pontefract Flat 10f Good 6/9; 10 Oct York Flat 7.9f Soft 8/20; 26 Oct Redcar Flat 8f Heavy 5/10 fig 76
    DATA for: Best recent form figure 76, 7 lb above field average; Trainer 23% wins (5/22), last 14 days; Has won at this trip or further
- City Cyclone (hrs_31919636) | 6yo G | 129lb | OR 76 | draw 3 | jockey William Carson | trainer Tony Carroll (14d 1/26) | headgear - | last run 28 days | form 111850 | MARKET 2.3% | 09:00 median 29.00 | Matchbook 55.00
    comment: City Cyclone won three on the bounce before fading to a fifth two starts back, an eighth three starts back and then unplaced last time, and the form has clearly cooled.
    DATA: model 3.0% | style Held up (led 3% of runs) | runs in data 6 | last 3: 28 Mar Kempton Flat 6f Standard To Slow 8/11; 9 Apr Wolverhampton Flat 6.1f Standard 5/6; 26 Oct Kempton (AW) Flat 7f Standard / Slow 12/12 fig 32
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 32, 37 lb below field average; Recent figures 44 lb below its current mark (looks high in the weights)
- King's Vanity (hrs_36809640) | 6yo G | 128lb | OR 75 | draw 10 | jockey Dougie Costello | trainer Marcus Tregoning (14d 1/2) | headgear - | last run 210 days | form 16/9-4 | MARKET 2.2% | 09:00 median 38.50 | Matchbook 50.00
    comment: King's Vanity chased home a fourth last time out and has run over today's trip and going, but a 210-day absence and a ninth and a sixth since his win four starts back raise fitness doubts.
    DATA: model 6.3% | style Leader (led 57% of runs) | runs in data 1 | last 3: 27 Apr Lingfield Flat 7f Standard 4/7
    DATA for: Carries 5 lb less than average; Pace: may get an uncontested lead
    DATA against: Official rating 75, 5 lb below field average; Returns from a 210-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Follow Your Heart (hrs_22616804) | 8yo G | 128lb | OR 75 | draw 6 | jockey Luke Morris | trainer Mark Loughnane (14d 2/11) | headgear t | last run 21 days | form 640075 | MARKET 1.6% | 09:00 median 41.00 | Matchbook 85.00
    comment: Winless in his last six, Follow Your Heart was fifth last time out, and a seventh two starts back and nothing better than a fourth five starts back make him hard to fancy.
    DATA: model 4.2% | style Midfield (led 3% of runs) | runs in data 7 | last 3: 14 Jun Doncaster Flat 7f Good 11/12; 14 Jul Ffos Las Flat 7.4f Good 7/9; 2 Nov Wolverhampton (AW) Flat 7f Standard 5/9 fig 71
    DATA for: Carries 5 lb less than average
    DATA against: Official rating 75, 5 lb below field average; Aged 8, older than most of this field

## 8:30 Wolverhampton (AW) | race_id rac_32305285428 | AWC Season 14 Handicap Stakes
Flat | Class 5 | 1m142y | going Standard | AW | 10 runners | rating band 0-70 | age 3yo+
DATA pace: Even - Two likely leaders (Clatford, Pipily). A fair, even gallop is most likely.
- Hitched (hrs_32780041) | 6yo G | 139lb | OR 69 | draw 7 | jockey Luke Morris | trainer David Simcock (14d 0/6) | headgear h | last run 3 days | form 066884 | MARKET 29.0% | 09:00 median 3.00 | Matchbook 3.10 | CHECK (skip line 2.85)
    DATA: model 8.7% | style Held up (led 3% of runs) | runs in data 12 | last 3: 14 Oct Kempton (AW) Flat 8f Standard / Slow 8/10 fig 63; 5 Nov Chelmsford (AW) Flat 7.5f Standard 8/11 fig 64; 20 Nov Wolverhampton (AW) Flat 8.5f Standard 4/11 fig 67
    DATA for: Best recent form figure 67, 5 lb above field average; Has won at this trip or further
- Sovereign Bay (hrs_61307162) | 3yo G | 135lb | OR 68 | draw 4 | jockey Jason Watson | trainer James Owen (14d 3/40) | headgear ht | last run 21 days | form 344502 | MARKET 21.5% | 09:00 median 3.75 | Matchbook 4.70
    comment: Sovereign Bay is yet to win in his last six, but a second last time out and a recent break of 21 days point to a gelding in decent shape, and he has run over today's trip and going.
    DATA: model 10.5% | style Held up (led 5% of runs) | runs in data 7 | last 3: 6 Jun Lingfield Flat 9f Soft 5/7; 5 Jul Southwell Flat 8.1f Standard 13/14; 2 Nov Wolverhampton (AW) Flat 8.5f Standard 2/8 fig 64
- Galba (hrs_50434706) | 3yo C | 142lb | OR 69 | draw 10 | jockey Matthew Lloyd Slater(7) | trainer Kevin & Lauren Frost (14d 1/5) | headgear - | last run 7 days | form 233441 | MARKET 16.5% | 09:00 median 5.00 | Matchbook 5.80
    comment: Galba arrives in cracking nick, a winner last time out just seven days ago, and he has run over today's trip and going before, with a consistent run of finishes behind that success. The risk is the quick turnaround under 142 lb from stall 10.
    DATA: model 26.3% | style Held up (led 8% of runs) | runs in data 10 | last 3: 5 Oct Pontefract Flat 8f Good 4/13; 26 Oct Southwell (AW) Flat 8f Standard 4/9 fig 70; 16 Nov Wolverhampton (AW) Flat 8.5f Standard 1/12 fig 68
    DATA for: Best recent form figure 70, 8 lb above field average; Trainer 20% wins (1/5), last 14 days; Last-run finishing speed +2.3% vs that field (finished strongly); Has won at this trip or further
    DATA against: Carries 6 lb more than average
- Shadowmere (hrs_56278306) | 3yo G | 135lb | OR 68 | draw 6 | jockey Callum Shepherd | trainer George Baker (14d 1/5) | headgear - | last run 105 days | form 835-20 | MARKET 8.5% | 09:00 median 10.00 | Matchbook 12.00
    comment: Shadowmere is hard to fancy after being unplaced last time and then 105 days off, and he is winless in his last five, though a second two starts back and a third four starts back show he can make the frame.
    DATA: model 12.2% | style Unknown | runs in data 2 | last 3: 23 May Windsor Flat 8.1f Good To Firm 2/10; 10 Aug Kempton Flat 8f Standard To Slow 14/14
    DATA for: Trainer 20% wins (1/5), last 14 days
    DATA against: Last-run finishing speed -15.3% vs that field (faded); Returns from a 105-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- He's A Gentleman (hrs_24819557) | 7yo G | 138lb | OR 68 | draw 9 | jockey David Egan | trainer Hugo Palmer (14d 0/1) | headgear - | last run 21 days | form 227758 | MARKET 8.2% | 09:00 median 9.50 | Matchbook 12.50
    comment: He's A Gentleman has been out of the frame lately, with an eighth last time out, but he was second five and six starts back and has run over today's trip and going before.
    DATA: model 8.3% | style Held up (led 4% of runs) | runs in data 7 | last 3: 18 Aug Wolverhampton Flat 7.2f Standard 7/9; 2 Oct Wolverhampton Flat 7.2f Standard 5/9; 2 Nov Wolverhampton (AW) Flat 7f Standard 8/9 fig 59
    DATA against: Recent figures 9 lb below its current mark (looks high in the weights); Aged 7, older than most of this field
- Pipily (hrs_53539402) | 3yo F | 129lb | OR 62 | draw 2 | jockey Clifford Lee | trainer T. J. Kent (14d 0/6) | headgear p | last run 41 days | form 724356 | MARKET 5.4% | 09:00 median 16.25 | Matchbook 16.50
    comment: Pipily is winless in her last six, and a sixth last time out after a fifth two starts back suggests she's drifting the wrong way, while 41 days off and 129 lb don't help. On the plus side, she has run over today's trip and going, and a second five starts back shows she has some ability.
    DATA: model 11.0% | style Leader (led 29% of runs) | runs in data 6 | last 3: 1 Sep Wolverhampton Flat 9.5f Standard 3/10; 28 Sep Wolverhampton Flat 9.5f Standard 5/11; 13 Oct Wolverhampton Flat 12.2f Standard 6/11
    DATA for: Carries 7 lb less than average
    DATA against: Official rating 62, 5 lb below field average
- Ecclefechan (hrs_53390295) | 3yo G | 137lb | OR 70 | draw 3 | jockey Kieran O'Neill | trainer Scott Dixon (14d 0/3) | headgear p | last run 34 days | form 117905 | MARKET 4.4% | 09:00 median 18.00 | Matchbook 24.00
    comment: Ecclefechan won twice five and six starts back but has faded since, finishing a fifth last time out 34 days ago, and he has run over today's trip and going.
    DATA: model 7.4% | style Midfield (led 3% of runs) | runs in data 14 | last 3: 24 Sep Newmarket Flat 8f Good 9/12; 5 Oct Yarmouth Flat 8f Good To Firm 10/11; 20 Oct Yarmouth Flat 7f Soft 5/9 fig 65
    DATA for: Has won at this trip or further
- Galileo Island (hrs_52831044) | 3yo G | 134lb | OR 67 | draw 8 | jockey Sean Levey | trainer Tom Ward (14d 0/2) | headgear - | last run 25 days | form 483900 | MARKET 2.8% | 09:00 median 29.00 | Matchbook 42.00
    comment: The risk is a winless run, with unplaced efforts in his last two outings.
    DATA: model 3.6% | style Prominent (led 3% of runs) | runs in data 6 | last 3: 10 Sep Epsom Downs Flat 7f Good To Soft 9/9; 5 Oct Yarmouth Flat 8f Good To Firm 11/11; 29 Oct Southwell (AW) Flat 8f Standard 13/13 fig 47
    DATA against: Best recent form figure 47, 15 lb below field average; Recent figures 20 lb below its current mark (looks high in the weights); Poor recent finishing positions
- Law Supreme (hrs_29226295) | 7yo G | 138lb | OR 68 | draw 1 | jockey Edward Greatrex | trainer Ian Williams (14d 2/14) | headgear tp | last run 163 days | form 214837 | MARKET 2.5% | 09:00 median 34.00 | Matchbook 48.00
    comment: Law Supreme was a seventh last time out, though he has a third two starts back and a winner five starts back, and has run over today's trip and going.
    DATA: model 6.8% | style Midfield (led 4% of runs) | runs in data 10 | last 3: 2 May Thirsk Flat 8f Good To Firm 8/9; 20 May Yarmouth Flat 10.1f Good 3/7; 13 Jun Leicester Flat 10f Good 7/10
    DATA for: Has won at this trip or further
    DATA against: Returns from a 163-day break; Aged 7, older than most of this field
- Clatford (hrs_57316406) | 3yo G | 132lb | OR 65 | draw 5 | jockey Christian Howarth(3) | trainer Scott Dixon (14d 0/3) | headgear p (1st time) | last run 38 days | form 4200 | MARKET 1.2% | 09:00 median 67.00 | Matchbook 150.00
    comment: Clatford has been unplaced in his last two outings and is winless in recent starts, so he is hard to fancy, though a second three starts back and experience of today's trip and going offer some hope.
    DATA: model 5.1% | style Leader (led 43% of runs) | runs in data 4 | last 3: 21 Mar Southwell Flat 8.1f Standard 2/9; 18 Jun Southwell Flat 8.1f Standard 11/13; 16 Oct Newcastle (AW) Flat 10f Standard 10/11
    DATA for: First-time headgear
