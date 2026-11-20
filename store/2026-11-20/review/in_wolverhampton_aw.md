# Card review packet: Wolverhampton (AW), 2026-11-20

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


## 4:30 Wolverhampton (AW) | race_id rac_32304925146 | All Weather Championship Is Back Amateur Jockeys' Handicap Stakes
Flat | Class 6 | 1m142y | going Standard | AW | 13 runners | rating band 0-55 | age 4yo+
DATA pace: Lone leader - Offiah's Boy is the only habitual front-runner and may be allowed an easy lead.
- Book of Life (hrs_31966137) | 6yo G | 154lb | OR 53 | draw 2 | jockey Mr Jack Loughnane(7) | trainer Patrick Morris (14d 0/5) | headgear p | last run 14 days | form 732443 | MARKET 18.1% | 09:00 median 4.50 | Matchbook 5.20 | CHECK (skip line 4.27)
    comment: Book of Life arrives in solid, consistent form, third last time out, fourth in his two runs before that, and fresh from a 14-day break, with experience of today's trip and going. The main risk is that he remains yet to win in his last six, and he carries 154 lb from draw 2.
    DATA: model 13.0% | style Midfield (led 4% of runs) | runs in data 18 | last 3: 12 Sep Musselburgh Flat 8f Good 4/8; 23 Oct Wolverhampton (AW) Flat 8.5f Standard 4/10 fig 52; 6 Nov Newcastle (AW) Flat 8f Standard 3/14 fig 53
    DATA for: Best recent form figure 53, 5 lb above field average
- Pitney (hrs_34471045) | 5yo G | 153lb | OR 52 | draw 7 | jockey Mr Ross Birkett | trainer Michael Attwater (14d 0/3) | headgear v | last run 22 days | form D25045 | MARKET 17.4% | 09:00 median 4.50 | Matchbook 5.40
    comment: Pitney is yet to win in his last six, but a fifth last time out and a fourth two starts back keep him in the mix, and he has run over today's trip and going before after 22 days off.
    DATA: model 9.6% | style Midfield (led 3% of runs) | runs in data 12 | last 3: 7 Oct Kempton Flat 8f Standard To Slow 13/13; 19 Oct Bath Flat 8f Good To Soft 4/14 fig 57; 29 Oct Bath Flat 8f Soft 5/14 fig 59
    DATA for: Best recent form figure 59, 11 lb above field average; Recent figures 7 lb above its current mark (looks well handicapped)
- Age of Time (hrs_36664558) | 5yo G | 152lb | OR 51 | draw 8 | jockey Mr Eireann Cagney | trainer Tony Carroll (14d 3/22) | headgear b | last run 20 days | form 598560 | MARKET 13.3% | 09:00 median 6.00 | Matchbook 7.00
    comment: Age of Time is yet to win in his last six starts, finishing a sixth two starts back and a fifth three starts back before going unplaced last time, though he has run over today's trip and going and returns after 20 days.
    DATA: model 8.8% | style Midfield (led 29% of runs) | runs in data 12 | last 3: 6 Oct Southwell Flat 5f Standard 5/11; 24 Oct Southwell (AW) Flat 6f Standard 6/11 fig 49; 31 Oct Southwell (AW) Flat 8f Standard 10/12 fig 38
- Dumfries (hrs_30123513) | 6yo G | 151lb | OR 50 | draw 9 | jockey Miss Charli Parker(3) | trainer Ruth Carr (14d 1/5) | headgear - | last run 20 days | form 432939 | MARKET 9.7% | 09:00 median 8.00 | Matchbook 9.40
    comment: Dumfries has hit the frame in three of his last six, including a third two starts back, and has run over today's trip and going, but he was only ninth last time out and is yet to win in that spell.
    DATA: model 7.1% | style Midfield (led 4% of runs) | runs in data 9 | last 3: 10 Oct Southwell Flat 8.1f Standard 9/12; 24 Oct Southwell (AW) Flat 8f Standard 3/13 fig 50; 31 Oct Southwell (AW) Flat 8f Standard 9/12 fig 42
    DATA for: Trainer 20% wins (1/5), last 14 days
- King David (hrs_36207430) | 5yo G | 153lb | OR 52 | draw 10 | jockey Mr Bradley Furniss(5) | trainer Gay Kelleway (14d 0/1) | headgear - | last run 17 days | form 522503 | MARKET 9.2% | 09:00 median 8.50 | Matchbook 10.50
    comment: King David, a gelding, was third last time out and has been second twice in his last six, so he's in the thick of this after a fresh 17-day break, and has run over today's trip and going. Yet to win in that spell, though, and 153 lb from stall 10 is no help.
    DATA: model 9.4% | style Midfield (led 4% of runs) | runs in data 15 | last 3: 28 Sep Brighton Flat 7f Good To Firm 5/10; 6 Oct Brighton Flat 7f Good To Firm 10/10; 3 Nov Wolverhampton (AW) Flat 7f Standard 3/10 fig 50
- Borderline Madness (hrs_44384508) | 4yo F | 154lb | OR 53 | draw 4 | jockey Mr Patrick Millman | trainer William Stone (14d 0/0) | headgear p | last run 41 days | form 810655 | MARKET 8.0% | 09:00 median 10.00 | Matchbook 11.50
    comment: Borderline Madness has finished fifth in each of her last two outings, and her one win in her last six came five starts back, so she's consistent without being sharp. She has run over today's trip and going, but 41 days off and 154 lb from stall four temper the appeal.
    DATA: model 11.6% | style Held up (led 4% of runs) | runs in data 6 | last 3: 15 Aug Lingfield Flat 10f Standard 6/8; 12 Sep Lingfield Flat 8f Standard 5/8; 10 Oct Southwell Flat 8.1f Standard 5/12
    DATA for: Has won at this trip or further
- Ignition (hrs_44294817) | 4yo G | 153lb | OR 52 | draw 12 | jockey Mr James King | trainer Thomas Faulkner (14d 0/3) | headgear tp | last run 136 days | form 463901 | MARKET 5.3% | 09:00 median 11.00 | Matchbook 24.00
    comment: Ignition won last time out, but that was 136 days ago and came after a patchy run of form, including a ninth three starts back, so he is hard to fancy.
    DATA: model 6.5% | style Held up (led 4% of runs) | runs in data 8 | last 3: 17 Apr Wolverhampton Flat 9.5f Standard 9/11; 15 Jun Chepstow Flat 10f Good 10/11; 7 Jul Wolverhampton Flat 8.6f Standard 1/9
    DATA for: Last-run finishing speed +4.4% vs that field (finished strongly); Has won at this trip or further
    DATA against: Returns from a 136-day break
- Wrist Art (hrs_23119642) | 9yo G | 150lb | OR 49 | draw 11 | jockey Paul Booth(7) | trainer James Owen (14d 2/29) | headgear tv | last run 25 days | form 318525 | MARKET 5.2% | 09:00 median 15.00 | Matchbook 18.50
    comment: He has run over today's trip and going and is fresh enough after 25 days, yet 150 lb from stall 11 makes him hard to fancy.
    DATA: model 11.7% | style Held up (led 5% of runs) | runs in data 23 | last 3: 17 Sep Southwell Flat 11.1f Standard 5/9; 28 Sep Wolverhampton Flat 9.5f Standard 2/10; 26 Oct Leicester Flat 12f Soft 5/13 fig 38
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 38, 10 lb below field average; Recent figures 11 lb below its current mark (looks high in the weights); Aged 9, older than most of this field
- Offiah's Boy (hrs_41229790) | 5yo G | 153lb | OR 52 | draw 3 | jockey Miss Aimee Jones(7) | trainer Joe Tickle (14d 0/4) | headgear - | last run 52 days | form 213504 | MARKET 3.2% | 09:00 median 23.00 | Matchbook 32.00
    comment: Offiah's Boy was fourth last time out but unplaced two starts back, and the 52-day break is a concern, as is 153 lb from draw 3.
    DATA: model 6.6% | style Leader (led 43% of runs) | runs in data 10 | last 3: 2 Sep Bath Flat 11.6f Good 5/6; 14 Sep Windsor Flat 11.4f Good To Soft 10/11; 29 Sep Wolverhampton Flat 8.6f Standard 4/8
    DATA for: Has won at this trip or further; Pace: may get an uncontested lead
- Maith Mar Or (hrs_55304221) | 4yo F | 156lb | OR 55 | draw 1 | jockey Mr Simon Walker | trainer John Berry (14d 0/1) | headgear - | last run 106 days | form 54-356 | MARKET 3.2% | 09:00 median 23.00 | Matchbook 36.00
    comment: Maith Mar Or is yet to win in her last five, but a third three starts back and a fifth two runs ago show she's competitive, and she has run over today's trip and going.
    DATA: model 2.4% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 26 Jun Newmarket Flat 10f Good To Firm 3/3; 23 Jul Yarmouth Flat 11.5f Good To Firm 5/5; 6 Aug Newmarket Flat 12f Good To Firm 6/6
    DATA against: Last-run finishing speed -4.4% vs that field (faded); Returns from a 106-day break
- Molly Valentine (hrs_29228640) | 6yo M | 151lb | OR 50 | draw 5 | jockey Mr Jake Holman(7) | trainer Stephanie Cassidy (14d 0/1) | headgear - | last run 25 days | form 070082 | MARKET 3.1% | 09:00 median 23.00 | Matchbook 36.00
    comment: Molly Valentine bounced back with a second last time out after an eighth two starts back, and she has run over today's trip and going, but she's winless in her last six and carries 151 lb from stall five off an official mark of 50.
    DATA: model 5.0% | style Held up (led 4% of runs) | runs in data 6 | last 3: 16 Jun Wolverhampton Flat 8.6f Standard 10/13; 28 Sep Wolverhampton Flat 9.5f Standard 8/10; 26 Oct Leicester Flat 12f Soft 2/13 fig 55
    DATA for: Best recent form figure 55, 7 lb above field average; Recent figures 5 lb above its current mark (looks well handicapped)
- Shielas Well (hrs_42163240) | 4yo F | 150lb | OR 49 | draw 6 | jockey Mr Freddie Robson(5) | trainer Ian Williams (14d 1/8) | headgear p | last run 23 days | form 484330 | MARKET 2.7% | 09:00 median 29.00 | Matchbook 38.00
    comment: Shielas Well has hit the frame twice, with a third two starts back and another third three starts back, but she was unplaced last time out and remains winless in her last six. She has run over today's trip and going, and returns after 23 days off, carrying 150 lb from stall six.
    DATA: model 5.9% | style Prominent (led 23% of runs) | runs in data 6 | last 3: 30 Apr Yarmouth Flat 9.1f Good To Firm 3/5; 5 May Wolverhampton Flat 8.6f Standard 3/8; 28 Oct Kempton (AW) Flat 6f Standard / Slow 10/11 fig 41
    DATA for: Good recent finishing positions
    DATA against: Best recent form figure 41, 7 lb below field average; Recent figures 8 lb below its current mark (looks high in the weights)
- Port Noir (hrs_18323963) | 9yo M | 150lb | OR 49 | draw 13 | jockey Mr Louis Burke(7) | trainer Robert Stephens (14d 0/5) | headgear t | last run 28 days | form 370800 | MARKET 1.5% | 09:00 median 51.00 | Matchbook 80.00
    comment: Port Noir is hard to fancy, unplaced last time out and again two starts back, and yet to win in her last six, with a third six starts back her best recent effort and a seventh five starts back next best.
    DATA: model 2.4% | style Midfield (led 3% of runs) | runs in data 13 | last 3: 2 Jun Wolverhampton Flat 9.5f Standard 8/11; 29 Sep Wolverhampton Flat 9.5f Standard 12/13; 23 Oct Wolverhampton (AW) Flat 9.5f Standard 10/10 fig 38
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 38, 10 lb below field average; Recent figures 11 lb below its current mark (looks high in the weights); Poor recent finishing positions; Aged 9, older than most of this field

## 5:00 Wolverhampton (AW) | race_id rac_32304927083 | Midnite: Built For 2026 Not 2006 Novice Stakes (GBB Race)
Flat | Class 4 | 5f21y | going Standard | AW | 5 runners | rating band - | age 3yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Frantic (hrs_58133544) | 3yo F | 128lb | OR 65 | draw 1 | jockey Kieran Shoemark | trainer Ed Walker (14d 0/9) | headgear b | last run 14 days | form 275306 | MARKET 41.4% | 09:00 median 2.10 | Matchbook 2.40
    DATA: model 21.7% | style Held up (led 5% of runs) | runs in data 7 | last 3: 1 Sep Lingfield Flat 6f Standard 3/4; 12 Oct Yarmouth Flat 6f Good To Soft 10/13; 6 Nov Newcastle (AW) Flat 5f Standard 6/14 fig 66
    DATA for: Best recent form figure 66, 15 lb above field average; Last-run finishing speed +2.5% vs that field (finished strongly)
    DATA against: Trainer 0 wins from 9 runs, last 14 days; Pace: steady gallop likely, hard to come from off the pace
- Oliaku (hrs_52995215) | 3yo F | 128lb | OR - | draw 2 | jockey Billy Loughnane | trainer Michael Bell (14d 0/2) | headgear - | last run 31 days | form 3-5 | MARKET 29.8% | 09:00 median 3.00 | Matchbook 3.20
    DATA: model 17.8% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 20 Oct Yarmouth Flat 5f Soft 5/6 fig 40
    DATA against: Best recent form figure 40, 11 lb below field average; Lightly raced: 1 run in our data, so the model has little to go on
- Butterfly Beach (hrs_53539528) | 3yo F | 128lb | OR 69 | draw 5 | jockey Sean Dylan Bowen | trainer Ollie Sangster (14d 0/4) | headgear - | last run 13 days | form 633-42 | MARKET 17.2% | 09:00 median 5.00 | Matchbook 5.80
    DATA: model 31.3% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 13 May Yarmouth Flat 6f Soft 4/4; 7 Nov Southwell (AW) Flat 5f Standard 2/9 fig 54
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Navona Grey (hrs_64590778) | 3yo F | 128lb | OR 65 | draw 6 | jockey Clifford Lee | trainer Gay Kelleway (14d 0/1) | headgear b (1st time) | last run 112 days | form 547 | MARKET 7.5% | 09:00 median 12.00 | Matchbook 13.00
    DATA: model 17.4% | style Prominent (led 5% of runs) | runs in data 3 | last 3: 30 May Chester Flat 7f Good 5/11; 13 Jun Bath Flat 5.7f Good 4/11; 31 Jul Wolverhampton Flat 7.2f Standard 7/10
    DATA for: First-time headgear
    DATA against: Last-run finishing speed -2.9% vs that field (faded); Returns from a 112-day break
- Beatrice Briannie (hrs_17394098176) | 3yo F | 128lb | OR - | draw 3 | jockey Luke Morris | trainer Michael Appleby (14d 1/16) | headgear - | last run 29 days | form 5 | MARKET 4.2% | 09:00 median 22.00 | Matchbook 26.00
    DATA: model 11.8% | style Held up (led 8% of runs) | runs in data 1 | last 3: 22 Oct Southwell (AW) Flat 6f Standard 5/8 fig 45
    DATA against: Best recent form figure 45, 6 lb below field average; Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace

## 5:30 Wolverhampton (AW) | race_id rac_32305355160 | AWC Finals Day At Newcastle 26th March Maiden Fillies' Stakes (Div I) (GBB/GBBPlus Race)
Flat | Class 3 | 1m142y | going Standard | AW | 11 runners | rating band - | age 2yo
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Noble Light (hrs_17394902329) | 2yo F | 128lb | OR - | draw 8 | jockey Robert Havlin | trainer John & Thady Gosden (14d 4/18) | headgear - | last run 16 days | form 6 | MARKET 34.8% | 09:00 median 2.38 | Matchbook 2.56
    DATA: model 13.7% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 4 Nov Kempton (AW) Flat 8f Standard / Slow 6/13 fig 59
    DATA for: Trainer 22% wins (4/18), last 14 days; Last-run finishing speed +3.0% vs that field (finished strongly)
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Lady Phillips (hrs_17391779587) | 2yo F | 128lb | OR 79 | draw 3 | jockey Rhys Clutterbuck | trainer Ralph Beckett (14d 1/12) | headgear - | last run 22 days | form 22 | MARKET 26.4% | 09:00 median 3.00 | Matchbook 3.55
    DATA: model 48.0% | style Held up (led 5% of runs) | runs in data 2 | last 3: 13 Oct Leicester Flat 8.2f Good To Soft 2/7; 29 Oct Bath Flat 8f Soft 2/12 fig 58
    DATA for: Last-run finishing speed +2.6% vs that field (finished strongly); Good recent finishing positions
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- My Amanah (hrs_17395553161) | 2yo F | 128lb | OR - | draw 5 | jockey Billy Loughnane | trainer George Boughey (14d 2/13) | headgear - | last run - days | form - | MARKET 11.0% | 09:00 median 6.75 | Matchbook 9.20
    DATA: model 4.9% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Rose Deer (hrs_17395702310) | 2yo F | 128lb | OR - | draw 7 | jockey Clifford Lee | trainer James Tate (14d 0/0) | headgear - | last run - days | form - | MARKET 10.3% | 09:00 median 8.55 | Matchbook 8.60
    DATA: model 4.9% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Lavender Bay (hrs_17393059348) | 2yo F | 128lb | OR - | draw 1 | jockey Daniel Muscutt | trainer James Fanshawe (14d 0/6) | headgear - | last run 50 days | form 6 | MARKET 4.9% | 09:00 median 15.00 | Matchbook 21.00
    DATA: model 5.7% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 1 Oct Nottingham Flat 8.3f Good 6/7
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Edith The Fair (hrs_17395547946) | 2yo F | 128lb | OR - | draw 11 | jockey Kieran Shoemark | trainer Ed Walker (14d 0/9) | headgear - | last run - days | form - | MARKET 3.9% | 09:00 median 19.00 | Matchbook 27.00
    DATA: model 4.9% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Trainer 0 wins from 9 runs, last 14 days; Lightly raced: 0 runs in our data, so the model has little to go on
- Diablesa (hrs_17395695009) | 2yo F | 128lb | OR - | draw 2 | jockey Callum Shepherd | trainer Charlie Johnston (14d 0/6) | headgear - | last run - days | form - | MARKET 3.2% | 09:00 median 21.00 | Matchbook 44.00
    DATA: model 4.9% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Time To Approach (hrs_17395560462) | 2yo F | 128lb | OR - | draw 6 | jockey Sean Levey | trainer Alan King (14d 2/19) | headgear - | last run - days | form - | MARKET 2.7% | 09:00 median 26.00 | Matchbook 48.00
    DATA: model 4.9% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Velora (hrs_17393494279) | 2yo F | 128lb | OR - | draw 9 | jockey Luke Morris | trainer Sir Mark Prescott Bt (14d 0/3) | headgear - | last run 38 days | form 7 | MARKET 1.3% | 09:00 median 51.00 | Matchbook 180.00
    DATA: model 3.7% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 13 Oct Leicester Flat 8.2f Good To Soft 7/7
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Sa Llagosta (hrs_17393332614) | 2yo F | 128lb | OR - | draw 4 | jockey Marco Ghiani | trainer Marco Botti (14d 0/7) | headgear - | last run 39 days | form 90 | MARKET 0.7% | 09:00 median 81.00 | Matchbook 230.00
    DATA: model 2.7% | style Held up (led 5% of runs) | runs in data 2 | last 3: 6 Oct Leicester Flat 8.2f Good To Firm 9/9; 12 Oct Yarmouth Flat 10.1f Good To Soft 10/10
    DATA against: Last-run finishing speed -6.2% vs that field (faded); Lightly raced: 2 runs in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Top Marks (hrs_17393060391) | 2yo F | 128lb | OR - | draw 10 | jockey Cieren Fallon | trainer Philip McBride (14d 0/0) | headgear - | last run 46 days | form 7 | MARKET 0.7% | 09:00 median 101.00 | Matchbook 310.00
    DATA: model 1.7% | style Held up (led 8% of runs) | runs in data 1 | last 3: 5 Oct Yarmouth Flat 8f Good To Firm 7/7
    DATA against: Last-run finishing speed -6.2% vs that field (faded); Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace

## 6:00 Wolverhampton (AW) | race_id rac_32304929020 | AWC Finals Day At Newcastle 26th March Maiden Fillies' Stakes (Div II) (GBB/GBBPlus Race)
Flat | Class 3 | 1m142y | going Standard | AW | 10 runners | rating band - | age 2yo
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Zhuri (hrs_17392193658) | 2yo F | 128lb | OR 75 | draw 8 | jockey Robert Havlin | trainer John & Thady Gosden (14d 4/18) | headgear - | last run 46 days | form 42 | MARKET 54.9% | 09:00 median 1.53 | Matchbook 1.63
    DATA: model 34.1% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 19 Sep Newmarket Flat 8f Good 4/7; 5 Oct Yarmouth Flat 7f Good To Firm 2/5
    DATA for: Trainer 22% wins (4/18), last 14 days
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Sayidah Iffraaj (hrs_17392141508) | 2yo F | 128lb | OR - | draw 11 | jockey Billy Loughnane | trainer George Boughey (14d 2/13) | headgear - | last run 64 days | form 5 | MARKET 15.5% | 09:00 median 5.00 | Matchbook 6.20
    DATA: model 11.9% | style Held up (led 8% of runs) | runs in data 1 | last 3: 17 Sep Southwell Flat 7.1f Standard 5/9
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Mesolithic (hrs_17393702879) | 2yo F | 128lb | OR - | draw 2 | jockey Daniel Muscutt | trainer James Fanshawe (14d 0/6) | headgear - | last run 30 days | form 5 | MARKET 8.9% | 09:00 median 8.50 | Matchbook 11.50
    DATA: model 15.0% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 21 Oct Kempton (AW) Flat 7f Standard / Slow 5/10 fig 58
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- El Kahlaa (hrs_17395696052) | 2yo F | 128lb | OR - | draw 3 | jockey Kaiya Fraser | trainer Harry Eustace (14d 0/6) | headgear - | last run - days | form - | MARKET 7.6% | 09:00 median 10.00 | Matchbook 13.50
    DATA: model 6.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Fifth Amendment (hrs_17393493236) | 2yo F | 128lb | OR - | draw 4 | jockey Rob Hornby | trainer Jonathan Portman (14d 1/7) | headgear - | last run 23 days | form 63 | MARKET 6.4% | 09:00 median 11.00 | Matchbook 17.00
    DATA: model 5.2% | style Held up (led 8% of runs) | runs in data 2 | last 3: 9 Oct Kempton Flat 8f Standard To Slow 6/7; 28 Oct Kempton (AW) Flat 8f Standard / Slow 3/9 fig 59
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Lunar Storm (hrs_17392820501) | 2yo F | 128lb | OR - | draw 7 | jockey Sean Levey | trainer Richard Hannon (14d 0/4) | headgear - | last run 45 days | form 77 | MARKET 2.6% | 09:00 median 23.00 | Matchbook 60.00
    DATA: model 9.2% | style Held up (led 5% of runs) | runs in data 2 | last 3: 25 Sep Haydock Flat 7f Soft 7/10; 6 Oct Leicester Flat 8.2f Good To Firm 7/9
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Speaking Tree (hrs_17389234667) | 2yo F | 128lb | OR - | draw 6 | jockey Kieran Shoemark | trainer Ed Walker (14d 0/9) | headgear b (1st time) | last run 16 days | form 88 | MARKET 1.5% | 09:00 median 41.00 | Matchbook 120.00
    DATA: model 7.3% | style Held up (led 5% of runs) | runs in data 2 | last 3: 15 Sep Yarmouth Flat 7f Good To Soft 8/9; 4 Nov Kempton (AW) Flat 8f Standard / Slow 8/13 fig 49
    DATA for: First-time headgear
    DATA against: Best recent form figure 49, 6 lb below field average; Trainer 0 wins from 9 runs, last 14 days; Lightly raced: 2 runs in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Catalistic (hrs_17391883887) | 2yo F | 128lb | OR - | draw 1 | jockey George Wood | trainer Rod Millman (14d 0/2) | headgear - | last run 74 days | form 0 | MARKET 1.0% | 09:00 median 81.00 | Matchbook 200.00
    DATA: model 3.0% | style Held up (led 8% of runs) | runs in data 1 | last 3: 7 Sep Windsor Flat 6.1f Good 14/14
    DATA against: Last-run finishing speed -2.1% vs that field (faded); Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Ortenzian Twilight (hrs_17392822587) | 2yo F | 128lb | OR - | draw 5 | jockey Cieren Fallon | trainer Heather Main (14d 0/0) | headgear - | last run 39 days | form 88 | MARKET 0.9% | 09:00 median 81.00 | Matchbook 120.00
    DATA: model 3.3% | style Held up (led 5% of runs) | runs in data 2 | last 3: 25 Sep Haydock Flat 7f Soft 8/10; 12 Oct Kempton Flat 8f Standard To Slow 8/10
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Red Kateryna (hrs_17394304690) | 2yo F | 128lb | OR - | draw 9 | jockey William Cox | trainer Faye Bramley (14d 1/17) | headgear - | last run 17 days | form 0 | MARKET 0.7% | 09:00 median 81.00 | Matchbook 240.00
    DATA: model 4.8% | style Held up (led 8% of runs) | runs in data 1 | last 3: 3 Nov Wolverhampton (AW) Flat 7f Standard 10/11
    DATA against: Last-run finishing speed -18.7% vs that field (faded); Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace

## 6:30 Wolverhampton (AW) | race_id rac_32304930957 | AWC Season 14 Selling Handicap Stakes
Flat | Class 4 | 1m142y | going Standard | AW | 11 runners | rating band 0-80 | age 3yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Gunfighter (hrs_36386903) | 5yo G | 137lb | OR 77 | draw 6 | jockey Billy Loughnane | trainer John Butler (14d 0/6) | headgear - | last run 37 days | form 175131 | MARKET 31.5% | 09:00 median 2.75 | Matchbook 2.92
    comment: Gunfighter won last time out and has three wins in his last six starts, with a third two starts back, though a 37-day break raises a fitness question.
    DATA: model 32.5% | style Midfield (led 23% of runs) | runs in data 8 | last 3: 9 Sep Kempton Flat 8f Standard To Slow 1/13; 9 Oct Kempton Flat 8f Standard To Slow 3/10; 14 Oct Kempton (AW) Flat 8f Standard / Slow 1/10 fig 78
    DATA for: Best recent form figure 78, 6 lb above field average; Has won at this trip or further; Good recent finishing positions
- Great Blasket (hrs_30865961) | 6yo G | 135lb | OR 75 | draw 4 | jockey Cieren Fallon | trainer James Owen (14d 2/29) | headgear v | last run 29 days | form 133234 | MARKET 19.1% | 09:00 median 4.50 | Matchbook 5.00
    comment: Consistent sort who has finished in the first four in each of his last six starts, including a third two starts back and a second three back, and he has run over today's trip and going.
    DATA: model 13.6% | style Prominent (led 3% of runs) | runs in data 11 | last 3: 16 Sep Beverley Flat 9.9f Good 2/10; 7 Oct Nottingham Flat 10.2f Good To Soft 3/10; 22 Oct Newmarket Flat 10f Soft 4/9 fig 76
    DATA for: Has won at this trip or further; Good recent finishing positions
- Tonal (hrs_34525995) | 6yo G | 140lb | OR 80 | draw 11 | jockey Conor Whiteley(5) | trainer Ian Williams (14d 1/8) | headgear p | last run 18 days | form 150102 | MARKET 11.0% | 09:00 median 7.50 | Matchbook 8.80
    DATA: model 12.8% | style Held up (led 5% of runs) | runs in data 8 | last 3: 30 Jun Ffos Las Flat 7.4f Good 1/8; 13 Sep Bath Flat 8f Good To Soft 10/10; 2 Nov Wolverhampton (AW) Flat 7f Standard 2/9 fig 80
    DATA for: Best recent form figure 80, 8 lb above field average; Official rating 80, 6 lb above field average; Has won at this trip or further; Good recent finishing positions
    DATA against: Carries 6 lb more than average; Pace: steady gallop likely, hard to come from off the pace
- Kalamunda (hrs_35164024) | 6yo G | 136lb | OR 76 | draw 8 | jockey Kieran Shoemark | trainer Joseph Parr (14d 0/0) | headgear p | last run 15 days | form -25705 | MARKET 8.5% | 09:00 median 9.00 | Matchbook 12.00
    comment: Kalamunda is winless in his last five, with a fifth last time out and a second five starts back the best of the recent form, though he has run over today's trip and going and returns after just 15 days.
    DATA: model 7.8% | style Prominent (led 4% of runs) | runs in data 5 | last 3: 3 Sep Southwell Flat 8.1f Standard 7/9; 3 Oct Southwell Flat 8.1f Standard 10/13; 5 Nov Chelmsford (AW) Flat 7.5f Standard 5/11 fig 74
- Epictetus (hrs_31005954) | 6yo G | 137lb | OR 77 | draw 1 | jockey William Carver | trainer Jamie Osborne (14d 0/4) | headgear tp | last run 28 days | form 316089 | MARKET 6.9% | 09:00 median 12.00 | Matchbook 15.00
    comment: Epictetus has run over today's trip and on this going, and he returns after 28 days with a win five starts back among his last six runs.
    DATA: model 4.1% | style Held up (led 5% of runs) | runs in data 19 | last 3: 31 Aug Epsom Downs Flat 12f Good To Soft 10/14; 19 Sep Chester Flat 10.3f Heavy 8/9; 23 Oct Wolverhampton (AW) Flat 9.5f Standard 9/12 fig 73
    DATA for: Has won at this trip or further
    DATA against: Poor recent finishing positions; Pace: steady gallop likely, hard to come from off the pace
- Hitched (hrs_32780041) | 6yo G | 129lb | OR 69 | draw 10 | jockey Luke Morris | trainer David Simcock (14d 0/3) | headgear h | last run 15 days | form 406688 | MARKET 6.6% | 09:00 median 13.00 | Matchbook 15.00
    comment: Winless in his last six, Hitched has finished eighth in each of his last two, though he's back after 15 days and has run over today's distance and going before.
    DATA: model 2.9% | style Midfield (led 3% of runs) | runs in data 11 | last 3: 18 Jun Yarmouth Flat 8f Good To Firm 6/9; 14 Oct Kempton (AW) Flat 8f Standard / Slow 8/10 fig 63; 5 Nov Chelmsford (AW) Flat 7.5f Standard 8/11 fig 64
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 64, 8 lb below field average; Poor recent finishing positions
- Dovey Moon (hrs_45791914) | 4yo G | 132lb | OR 72 | draw 2 | jockey Charles Bishop | trainer David Evans (14d 0/5) | headgear b (1st time) | last run 15 days | form 563627 | MARKET 6.4% | 09:00 median 12.00 | Matchbook 17.50
    comment: Dovey Moon is yet to win in his last six, though a second two starts back and a third four starts back show he can get involved, and he has run over today's trip and going.
    DATA: model 11.8% | style Midfield (led 23% of runs) | runs in data 10 | last 3: 3 Oct Southwell Flat 8.1f Standard 6/13; 29 Oct Southwell (AW) Flat 8f Standard 2/13 fig 70; 5 Nov Southwell (AW) Flat 8f Standard 7/12 fig 62
    DATA for: Has won at this trip or further; First-time headgear
- Youarenotforgiven (hrs_23055879) | 8yo G | 136lb | OR 76 | draw 7 | jockey Hollie Doyle | trainer Tony Carroll (14d 3/22) | headgear - | last run 134 days | form 111069 | MARKET 3.9% | 09:00 median 19.00 | Matchbook 28.00
    comment: Youarenotforgiven won three on the spin, four to six starts back, but has since faded to a sixth and a ninth last time out, and he returns after 134 days off.
    DATA: model 2.6% | style Held up (led 4% of runs) | runs in data 8 | last 3: 9 May Nottingham Flat 8.3f Good To Firm 10/12; 11 Jun Nottingham Flat 8.3f Soft 6/9; 9 Jul Newbury Flat 8f Good To Firm 9/12
    DATA for: Has won at this trip or further
    DATA against: Poor recent finishing positions; Returns from a 134-day break; Pace: steady gallop likely, hard to come from off the pace
- King Casper (hrs_43508563) | 4yo G | 133lb | OR 73 | draw 3 | jockey Cam Hardie | trainer Antony Brittain (14d 1/9) | headgear - | last run 35 days | form 0-0804 | MARKET 2.6% | 09:00 median 34.00 | Matchbook 40.00
    comment: The main risk is a winless recent run, with nothing better than that fourth in his last five starts.
    DATA: model 5.4% | style Unknown | runs in data 4 | last 3: 8 Aug Haydock Flat 8f Good 8/13; 6 Sep York Flat 7.9f Good To Soft 14/19; 16 Oct Newcastle (AW) Flat 8f Standard 4/5 fig 63
    DATA against: Best recent form figure 63, 9 lb below field average; Recent figures 10 lb below its current mark (looks high in the weights)
- Prince Rasam (hrs_36739843) | 5yo G | 126lb | OR 66 | draw 5 | jockey Jason Watson | trainer Jamie Moore & Josh Moore (14d 1/19) | headgear p (1st time) | last run 12 days | form 66-236 | MARKET 2.2% | 09:00 median 29.00 | Matchbook 70.00
    comment: Winless in his last five, Prince Rasam was sixth last time out and has finished sixth in two of his other recent runs, so he is hard to fancy at 126 lb from draw 5. In his favour, he is back quickly after 12 days, has run over this trip and going, and was third two starts back.
    DATA: model 3.9% | style Midfield (led 4% of runs) | runs in data 4 | last 3: 3 Sep Salisbury Flat 8f Good To Soft 3/8; 10 Oct Southwell Flat 8.1f Standard 6/12; 8 Nov Sandown Hurdle 16f Good 7/7
    DATA for: Carries 8 lb less than average; First-time headgear
    DATA against: Official rating 66, 8 lb below field average
- Banner Beauty (hrs_45824485) | 4yo F | 129lb | OR 69 | draw 9 | jockey William Carson | trainer Tony Carroll (14d 3/22) | headgear - | last run 104 days | form 096-00 | MARKET 1.3% | 09:00 median 41.00 | Matchbook 140.00
    comment: The risk is obvious: she is winless in her last five and returns after 104 days off.
    DATA: model 2.6% | style Held up (led 4% of runs) | runs in data 3 | last 3: 24 May Curragh Flat 8f Good 10/19; 26 Jun Curragh Flat 8f Good 18/20; 8 Aug Wexford Hurdle 16.9f Good PU/11
    DATA against: Poor recent finishing positions; Returns from a 104-day break; Pace: steady gallop likely, hard to come from off the pace

## 7:00 Wolverhampton (AW) | race_id rac_32304932894 | AWC Trials Day - Lingfield 2nd January 2027 Nursery Handicap Stakes
Flat | Class 6 | 7f36y | going Standard | AW | 12 runners | rating band 0-65 | age 2yo
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Printing Money (hrs_63810859) | 2yo G | 134lb | OR 64 | draw 4 | jockey Andrew Mullen | trainer Dylan Cunha (14d 0/6) | headgear - | last run 14 days | form 739143 | MARKET 20.8% | 09:00 median 4.00 | Matchbook 4.20 | CHECK (skip line 3.80)
    comment: Printing Money arrives in decent order, third last time out, a fourth two starts back and a winner three starts back, and he has run over today's trip and going before after just 14 days off.
    DATA: model 19.7% | style Prominent (led 4% of runs) | runs in data 8 | last 3: 18 Sep Wolverhampton Flat 7.2f Standard 1/12; 19 Oct Wolverhampton (AW) Flat 7f Standard 4/12 fig 64; 6 Nov Newcastle (AW) Flat 7f Standard 3/11 fig 66
    DATA for: Best recent form figure 66, 6 lb above field average; Has won at this trip or further; Good recent finishing positions
- Beechwood Glory (hrs_66005100) | 2yo C | 134lb | OR 64 | draw 3 | jockey Billy Loughnane | trainer John Butler (14d 0/6) | headgear - | last run 18 days | form 532335 | MARKET 16.6% | 09:00 median 5.00 | Matchbook 5.40
    comment: The main risk is that he's yet to win and was only fifth last time.
    DATA: model 9.8% | style Midfield (led 4% of runs) | runs in data 6 | last 3: 31 Aug Chepstow Flat 6.1f Good To Soft 3/6; 21 Sep Ffos Las Flat 6f Soft 3/5; 2 Nov Chelmsford (AW) Flat 6f Standard 5/9 fig 60
    DATA for: Good recent finishing positions
- Perfect Hope (hrs_65068962) | 2yo F | 135lb | OR 65 | draw 9 | jockey Sean Levey | trainer Tom Ward (14d 0/1) | headgear tp | last run 22 days | form 822222 | MARKET 15.3% | 09:00 median 5.50 | Matchbook 5.80
    comment: She is yet to win, though, and carries 135 lb from draw 9.
    DATA: model 17.0% | style Midfield (led 4% of runs) | runs in data 8 | last 3: 18 Sep Wolverhampton Flat 7.2f Standard 2/12; 2 Oct Newcastle Flat 7.1f Standard 2/10; 29 Oct Southwell (AW) Flat 7f Standard 2/13 fig 65
    DATA for: Best recent form figure 65, 5 lb above field average; Good recent finishing positions
- Zambezi Shark (hrs_65610356) | 2yo C | 131lb | OR 61 | draw 6 | jockey Marco Ghiani | trainer Stuart Williams (14d 0/5) | headgear - | last run 30 days | form 5080 | MARKET 13.6% | 09:00 median 6.00 | Matchbook 6.80
    comment: Zambezi Shark has been well beaten lately, unplaced last time out and an eighth two starts back, though he has run over today's trip and going before and returns after 30 days off.
    DATA: model 2.6% | style Prominent (led 8% of runs) | runs in data 4 | last 3: 9 Jul Newbury Flat 6f Good To Firm 12/18; 27 Jul Southwell Flat 7.1f Standard 8/12; 21 Oct Newmarket Flat 7f Soft 11/13 fig 55
    DATA against: Best recent form figure 55, 5 lb below field average; Recent figures 6 lb below its current mark (looks high in the weights); Poor recent finishing positions
- Alfey Moon (hrs_64877274) | 2yo G | 133lb | OR 63 | draw 1 | jockey Hollie Doyle | trainer David Evans (14d 0/5) | headgear - | last run 45 days | form 0447 | MARKET 10.0% | 09:00 median 8.50 | Matchbook 9.00
    comment: Alfey Moon showed some consistency with a fourth two starts back and another fourth three starts back, but he was only seventh last time out and returns after 45 days off.
    DATA: model 7.5% | style Held up (led 8% of runs) | runs in data 4 | last 3: 4 Jun Ffos Las Flat 7.4f Good To Soft 4/5; 13 Jun Leicester Flat 7f Good 4/9; 6 Oct Leicester Flat 6f Good To Firm 7/13
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Caravel (hrs_65519664) | 2yo F | 132lb | OR 62 | draw 8 | jockey Cieren Fallon | trainer S. P. C. Woods (14d 0/4) | headgear - | last run 22 days | form 7740 | MARKET 5.8% | 09:00 median 12.00 | Matchbook 18.00
    comment: Caravel has been winless in her last four, finishing unplaced last time out and a fourth two starts back, though she has run over today's trip and going before and returns after 22 days.
    DATA: model 3.5% | style Midfield (led 5% of runs) | runs in data 4 | last 3: 18 Jul Newmarket Flat 7f Good To Firm 7/10; 29 Jul Leicester Flat 6f Good To Firm 4/4; 29 Oct Southwell (AW) Flat 7f Standard 11/13 fig 56
    DATA against: Best recent form figure 56, 4 lb below field average; Recent figures 6 lb below its current mark (looks high in the weights)
- Better Nature (hrs_64780646) | 2yo G | 132lb | OR 62 | draw 11 | jockey Rob Hornby | trainer Jonathan Portman (14d 1/7) | headgear p | last run 32 days | form 326551 | MARKET 4.1% | 09:00 median 17.00 | Matchbook 28.00
    comment: Better Nature won last time out and has run over today's trip and going, but he was beaten in three of the three starts before that, finishing a fifth, a fifth and a sixth.
    DATA: model 6.4% | style Midfield (led 3% of runs) | runs in data 7 | last 3: 29 Aug Chepstow Flat 7.1f Good To Soft 5/9; 18 Sep Wolverhampton Flat 7.2f Standard 5/12; 19 Oct Wolverhampton (AW) Flat 7f Standard 1/10 fig 60
    DATA for: Has won at this trip or further
- Orfilia (hrs_17391206980) | 2yo F | 130lb | OR 60 | draw 2 | jockey Kieran Shoemark | trainer David O'Meara (14d 0/14) | headgear - | last run 59 days | form 484 | MARKET 3.7% | 09:00 median 19.00 | Matchbook 34.00
    comment: Winless in her last three, Orfilia was fourth last time out, an eighth two starts back and a fourth three starts back, and she returns after 59 days off.
    DATA: model 9.4% | style Held up (led 5% of runs) | runs in data 3 | last 3: 22 Aug Redcar Flat 6f Good 4/12; 9 Sep Carlisle Flat 5.8f Good 8/13; 22 Sep Southwell Flat 7.1f Standard 4/10
    DATA against: Trainer 0 wins from 14 runs, last 14 days; Pace: steady gallop likely, hard to come from off the pace
- Star Bayside Boy (hrs_65678284) | 2yo F | 132lb | OR 62 | draw 10 | jockey Ashley Lewis(3) | trainer Marcus Tregoning (14d 0/0) | headgear - | last run 15 days | form 010047 | MARKET 2.9% | 09:00 median 23.00 | Matchbook 50.00
    comment: Star Bayside Boy is hard to fancy after a seventh last time out and a fourth two starts back, with just one win in her last six, five starts ago.
    DATA: model 4.5% | style Held up (led 5% of runs) | runs in data 6 | last 3: 21 Sep Leicester Flat 6f Good 11/14; 19 Oct Wolverhampton (AW) Flat 7f Standard 4/10 fig 63; 5 Nov Chelmsford (AW) Flat 7f Standard 7/11 fig 59
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Desert Legend (hrs_64324589) | 2yo G | 135lb | OR 65 | draw 7 | jockey Joe Leavy | trainer Richard Hannon (14d 0/4) | headgear b (1st time) | last run 18 days | form 303769 | MARKET 2.8% | 09:00 median 26.00 | Matchbook 44.00
    comment: Desert Legend has run over today's trip and going and is back after 18 days, but he was beaten into ninth last time out and is winless in his last six, with a third four starts back his best recent effort.
    DATA: model 4.5% | style Midfield (led 3% of runs) | runs in data 6 | last 3: 8 Aug Newmarket Flat 7f Good To Firm 7/7; 12 Oct Kempton Flat 7f Standard To Slow 6/11; 2 Nov Chelmsford (AW) Flat 6f Standard 9/9 fig 51
    DATA for: First-time headgear
    DATA against: Best recent form figure 51, 9 lb below field average; Recent figures 14 lb below its current mark (looks high in the weights); Poor recent finishing positions
- Kochella (hrs_65101862) | 2yo F | 131lb | OR 61 | draw 5 | jockey George Wood | trainer Lemos De Souza (14d 0/3) | headgear p (1st time) | last run 22 days | form 306376 | MARKET 2.6% | 09:00 median 29.00 | Matchbook 44.00
    comment: Kochella is winless in her last six and was beaten into sixth last time, following a seventh, so she is hard to fancy; she has run over today's trip and going, and a third three starts back shows she can pick up a cheque.
    DATA: model 7.5% | style Midfield (led 4% of runs) | runs in data 6 | last 3: 5 Aug Kempton Flat 6f Standard To Slow 3/10; 19 Aug Kempton Flat 7f Standard To Slow 7/13; 29 Oct Southwell (AW) Flat 7f Standard 6/13 fig 58
    DATA for: First-time headgear
- Passerine (hrs_63422716) | 2yo F | 133lb | OR 63 | draw 12 | jockey Ben Pollard(7) | trainer Richard Hannon (14d 0/4) | headgear - | last run 22 days | form 452430 | MARKET 1.8% | 09:00 median 34.00 | Matchbook 90.00
    comment: The main risk is that she is yet to win in her last six starts and was unplaced last time out.
    DATA: model 7.5% | style Prominent (led 23% of runs) | runs in data 6 | last 3: 6 Oct Leicester Flat 6f Good To Firm 4/13; 15 Oct Brighton Flat 6f Good 3/6 fig 67; 29 Oct Southwell (AW) Flat 7f Standard 10/13 fig 58
    DATA for: Best recent form figure 67, 7 lb above field average; Recent figures 4 lb above its current mark (looks well handicapped)

## 7:30 Wolverhampton (AW) | race_id rac_32304934831 | All Weather Championship Handicap Stakes
Flat | Class 2 | 7f36y | going Standard | AW | 10 runners | rating band 0-105 | age 3yo+
DATA pace: Lone leader - Carnival of Light is the only habitual front-runner and may be allowed an easy lead.
- Asuka (hrs_42912506) | 4yo G | 134lb | OR 97 | draw 10 | jockey Billy Loughnane | trainer George Boughey (14d 2/13) | headgear - | last run 22 days | form 211341 | MARKET 34.1% | 09:00 median 2.50 | Matchbook 2.74
    comment: Asuka arrives in cracking nick, having won last time out and boasting three wins in his last six starts, with a third and a fourth in between, while 22 days since his last run suggests he's fresh. He has run over today's trip and going, though 134 lb from draw 10 is a mild concern.
    DATA: model 27.5% | style Midfield (led 3% of runs) | runs in data 6 | last 3: 22 Aug Chester Flat 7.6f Good To Soft 3/13; 13 Sep Doncaster Flat 6.5f Good 4/13; 29 Oct Southwell (AW) Flat 7f Standard 1/14 fig 98
    DATA for: Best recent form figure 98, 12 lb above field average; Official rating 97, 7 lb above field average; Has won at this trip or further; Good recent finishing positions
    DATA against: Carries 8 lb more than average
- Secret Santa (hrs_52388539) | 3yo C | 123lb | OR 87 | draw 3 | jockey Sean Levey | trainer Richard Hannon (14d 0/4) | headgear - | last run 196 days | form 433-1 | MARKET 18.3% | 09:00 median 4.50 | Matchbook 5.30
    comment: The one risk is a 196-day absence, so fitness is the question from stall three at 123 lb.
    DATA: model 14.6% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 8 May Ascot Flat 6f Good 1/19
    DATA for: Last-run finishing speed +3.5% vs that field (finished strongly)
    DATA against: Returns from a 196-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Tremolo (hrs_45759490) | 4yo G | 125lb | OR 88 | draw 7 | jockey Kieran Shoemark | trainer Harry Charlton (14d 0/0) | headgear - | last run 146 days | form 9113-6 | MARKET 12.1% | 09:00 median 7.00 | Matchbook 8.00
    DATA: model 8.0% | style Held up (led 8% of runs) | runs in data 1 | last 3: 27 Jun Newcastle Flat 7.1f Standard To Slow 6/14
    DATA against: Returns from a 146-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Carnival of Light (hrs_65774940) | 4yo F | 125lb | OR 88 | draw 9 | jockey Callum Shepherd | trainer Charlie Johnston (14d 0/6) | headgear - | last run 20 days | form 110020 | MARKET 7.0% | 09:00 median 11.50 | Matchbook 14.50
    comment: Carnival of Light won five and six starts back but has been unplaced in two of her last three, though a second two starts back shows a flicker, and she's fresh enough after 20 days.
    DATA: model 4.9% | style Leader (led 29% of runs) | runs in data 7 | last 3: 20 Aug York Flat 7f Good To Soft 16/19; 12 Sep Leopardstown Flat 7f Good 17/17; 12 Oct Musselburgh Flat 7.1f Good To Soft 2/7
    DATA for: Has won at this trip or further; Pace: may get an uncontested lead
- Sea Baaeed (hrs_45568418) | 4yo G | 124lb | OR 87 | draw 2 | jockey Cieren Fallon | trainer Ian Williams (14d 1/8) | headgear - | last run 16 days | form 6342-6 | MARKET 7.0% | 09:00 median 12.00 | Matchbook 14.50
    comment: Fit after 16 days, he has run over today's trip and going before, and a second two starts back plus a third four starts back show he's consistently in the mix.
    DATA: model 4.0% | style Held up (led 8% of runs) | runs in data 1 | last 3: 4 Nov Kempton (AW) Flat 7f Standard / Slow 6/9 fig 81
    DATA against: Best recent form figure 81, 5 lb below field average; Recent figures 6 lb below its current mark (looks high in the weights); Lightly raced: 1 run in our data, so the model has little to go on
- Sword (hrs_36499883) | 5yo G | 126lb | OR 89 | draw 1 | jockey Olivia Haines(7) | trainer Stuart Williams (14d 0/5) | headgear t | last run 55 days | form 658271 | MARKET 6.2% | 09:00 median 13.00 | Matchbook 16.50
    comment: Sword won last time out but has been patchy otherwise, with a seventh and an eighth in his other recent runs, and 55 days off is a worry.
    DATA: model 13.0% | style Unknown | runs in data 8 | last 3: 22 Aug Newmarket Flat 6f Good 2/13; 5 Sep Ascot Flat 6f Good To Firm 7/13; 26 Sep Newmarket Flat 7f Good To Firm 1/12
    DATA for: Has won at this trip or further; Good recent finishing positions
- Mubasimah (hrs_57223096) | 3yo F | 123lb | OR 87 | draw 5 | jockey Callum Hutchinson | trainer Andrew Balding (14d 0/24) | headgear - | last run 32 days | form 507608 | MARKET 4.9% | 09:00 median 17.00 | Matchbook 20.00
    comment: The main risk is her form, winless in her last six, with the yard 0/24 over the past fortnight.
    DATA: model 3.9% | style Midfield (led 8% of runs) | runs in data 7 | last 3: 5 Sep Ascot Flat 7f Good To Firm 6/8; 24 Sep Newmarket Flat 6f Good 10/10; 19 Oct Pontefract Flat 6f Heavy 8/10 fig 77
    DATA against: Best recent form figure 77, 9 lb below field average; Recent figures 10 lb below its current mark (looks high in the weights); Trainer 0 wins from 24 runs, last 14 days; Poor recent finishing positions
- Rogue Messiah (hrs_55392750) | 3yo G | 122lb | OR 86 | draw 8 | jockey Luke Morris | trainer James Owen (14d 2/29) | headgear p (1st time) | last run 25 days | form 219827 | MARKET 4.8% | 09:00 median 17.00 | Matchbook 22.00
    comment: Rogue Messiah was a seventh last time out, though a second two starts back and a winner five starts back show he has ability, and he has run over today's trip and going.
    DATA: model 6.6% | style Midfield (led 8% of runs) | runs in data 6 | last 3: 11 Jul Newmarket Flat 7f Good To Firm 8/11; 23 Sep Kempton Flat 7f Standard To Slow 2/13; 26 Oct Kempton (AW) Flat 7f Standard / Slow 7/12 fig 84
    DATA for: First-time headgear
- Dapper Guest (hrs_41814759) | 4yo G | 124lb | OR 87 | draw 4 | jockey Connor Planas | trainer George Margarson (14d 0/0) | headgear p | last run 22 days | form 311004 | MARKET 3.5% | 09:00 median 23.00 | Matchbook 32.00
    comment: Dapper Guest was fourth last time out, but unplaced in the two runs before that, so the two wins four and five starts back look a while ago now.
    DATA: model 2.8% | style Held up (led 4% of runs) | runs in data 13 | last 3: 26 Sep Newmarket Flat 7f Good To Firm 11/12; 13 Oct Leicester Flat 7f Good To Soft 14/17; 29 Oct Southwell (AW) Flat 7f Standard 4/14 fig 88
    DATA for: Has won at this trip or further
- Dandy Style (hrs_50435812) | 3yo G | 137lb | OR 101 | draw 6 | jockey Clifford Lee | trainer Ian Williams (14d 1/8) | headgear - | last run 155 days | form 264231 | MARKET 2.3% | 09:00 median 29.00 | Matchbook 55.00
    comment: Dandy Style won last time out and has been in the first three in three of his last four, but he's been off for 155 days, carries 137 lb off an official mark of 101, and has run over today's trip.
    DATA: model 14.8% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Official rating 101, 11 lb above field average
    DATA against: Carries 11 lb more than average; Returns from a 155-day break; Lightly raced: 0 runs in our data, so the model has little to go on

## 8:00 Wolverhampton (AW) | race_id rac_32304936768 | Midnite It's Actually Pretty Good Handicap Stakes
Flat | Class 6 | 6f20y | going Standard | AW | 13 runners | rating band 0-55 | age 3yo+
DATA pace: Even - Two likely leaders (Sir Rodneyredblood, Our Planet). A fair, even gallop is most likely.
- Our Planet (hrs_45662183) | 4yo G | 131lb | OR 54 | draw 3 | jockey Cieren Fallon | trainer James Owen (14d 2/29) | headgear t | last run 24 days | form 666078 | MARKET 24.4% | 09:00 median 3.25 | Matchbook 3.70 | CHECK (skip line 3.09)
    DATA: model 5.5% | style Leader (led 38% of runs) | runs in data 6 | last 3: 8 Sep Leicester Flat 5f Good To Soft 10/11; 13 Oct Wolverhampton Flat 6.1f Standard 7/12; 27 Oct Wolverhampton (AW) Flat 5f Standard 8/9 fig 48
    DATA against: Recent figures 6 lb below its current mark (looks high in the weights); Poor recent finishing positions
- Barry The Worm (hrs_53081427) | 3yo G | 132lb | OR 55 | draw 8 | jockey Rob Hornby | trainer Edward Smyth-Osbourne (14d 0/0) | headgear - | last run 17 days | form 561422 | MARKET 22.4% | 09:00 median 3.50 | Matchbook 4.00
    comment: Runner-up in his last two starts, and a winner four starts back, he's in decent heart after 17 days off, and has run over today's trip and going.
    DATA: model 15.4% | style Prominent (led 23% of runs) | runs in data 10 | last 3: 15 Oct Southwell (AW) Flat 7f Standard 4/13 fig 56; 27 Oct Wolverhampton (AW) Flat 6f Standard 2/12 fig 57; 3 Nov Wolverhampton (AW) Flat 7f Standard 2/11 fig 57
    DATA for: Best recent form figure 57, 8 lb above field average; Has won at this trip or further; Good recent finishing positions
- Solid Bond (hrs_40786172) | 4yo F | 131lb | OR 54 | draw 6 | jockey Harry Davies | trainer Tony Carroll (14d 3/22) | headgear - | last run 13 days | form 192077 | MARKET 8.3% | 09:00 median 9.25 | Matchbook 11.50
    comment: Solid Bond is a threat on profile, a winner six starts back and a second four starts back, with just 13 days since her last run and experience of today's trip and going; the risk is back-to-back sevenths, and she carries 131 lb from draw 6.
    DATA: model 4.8% | style Prominent (led 3% of runs) | runs in data 8 | last 3: 5 Oct Pontefract Flat 5f Good 10/12; 14 Oct Nottingham Flat 5f Good To Soft 7/9 fig 46; 7 Nov Southwell (AW) Flat 7f Standard 7/12 fig 52
    DATA against: Poor recent finishing positions
- Love Alive (hrs_54525548) | 3yo F | 131lb | OR 54 | draw 10 | jockey Billy Loughnane | trainer John Butler (14d 0/6) | headgear ht | last run 24 days | form 359704 | MARKET 7.2% | 09:00 median 10.00 | Matchbook 14.00
    comment: Love Alive arrives fit after 24 days off, having finished fourth last time out, and she has run over today's trip and on this going before.
    DATA: model 5.4% | style Held up (led 5% of runs) | runs in data 13 | last 3: 23 Sep Kempton Flat 6f Standard To Slow 7/11; 13 Oct Wolverhampton Flat 6.1f Standard 10/12; 27 Oct Wolverhampton (AW) Flat 6f Standard 4/12 fig 56
    DATA for: Best recent form figure 56, 7 lb above field average
    DATA against: Course: hold-up horses have won 0.7× their fair share at 6f here
- My Mate Mackley (hrs_58843904) | 3yo G | 132lb | OR 55 | draw 12 | jockey Taryn Langley(5) | trainer Adam Kirby (14d 1/7) | headgear p | last run 24 days | form 244116 | MARKET 7.1% | 09:00 median 11.00 | Matchbook 13.50
    comment: Won two starts back and again three starts back before a sixth last time out, so he arrives in decent order after 24 days off, with experience of today's trip and going.
    DATA: model 15.1% | style Prominent (led 3% of runs) | runs in data 16 | last 3: 28 Sep Brighton Flat 6f Good To Firm 1/8; 6 Oct Brighton Flat 6f Good To Firm 1/9; 27 Oct Catterick Flat 6f Soft 6/10 fig 53
    DATA for: Has won at this trip or further; Good recent finishing positions
- Eldeyaar (hrs_28577640) | 7yo G | 131lb | OR 54 | draw 9 | jockey Cam Hardie | trainer Antony Brittain (14d 1/9) | headgear v | last run 24 days | form 852391 | MARKET 6.7% | 09:00 median 11.00 | Matchbook 15.50
    comment: The main risk is a patchy record, with a ninth two starts back among his other finishes.
    DATA: model 12.0% | style Prominent (led 3% of runs) | runs in data 15 | last 3: 26 Sep Ripon Flat 6f Good 3/11; 15 Oct Southwell (AW) Flat 7f Standard 9/13 fig 39; 27 Oct Catterick Flat 6f Soft 1/10 fig 69
    DATA for: Best recent form figure 69, 20 lb above field average; Recent figures 15 lb above its current mark (looks well handicapped); Has won at this trip or further; Good recent finishing positions
- Tomarlo (hrs_41410537) | 4yo G | 132lb | OR 55 | draw 4 | jockey Sean Dylan Bowen | trainer Jennie Candlish (14d 3/21) | headgear t | last run 25 days | form 315767 | MARKET 5.7% | 09:00 median 13.00 | Matchbook 17.50
    comment: Tomarlo has finished seventh, sixth and seventh in his last three outings, a slide since a win five starts back, though he has run over today's trip and going and returns after 25 days.
    DATA: model 8.0% | style Midfield (led 3% of runs) | runs in data 10 | last 3: 8 Sep Leicester Flat 6f Good To Soft 7/11; 26 Sep Southwell Flat 5f Standard 6/9; 26 Oct Southwell (AW) Flat 5f Standard 7/10 fig 47
    DATA for: Has won at this trip or further
    DATA against: Recent figures 8 lb below its current mark (looks high in the weights); Poor recent finishing positions
- Twilight Madness (hrs_22440453) | 8yo H | 132lb | OR 55 | draw 13 | jockey Alistair Rawlinson | trainer Simon Hodgson (14d 0/1) | headgear - | last run 29 days | form 980667 | MARKET 5.7% | 09:00 median 11.00 | Matchbook 22.00
    comment: The main risk is a winless recent run, with a seventh last time out, a sixth two starts back and another sixth three starts back.
    DATA: model 6.2% | style Prominent (led 3% of runs) | runs in data 12 | last 3: 4 Aug Lingfield Flat 6f Standard 6/10; 18 Aug Lingfield Flat 6f Standard 6/8; 22 Oct Southwell (AW) Flat 5f Standard 7/11 fig 52
    DATA against: Poor recent finishing positions
- Nordic Glory (hrs_24386250) | 7yo G | 132lb | OR 55 | draw 7 | jockey William Carson | trainer Michael Attwater (14d 0/3) | headgear - | last run 43 days | form 014550 | MARKET 4.2% | 09:00 median 17.00 | Matchbook 26.00
    comment: Nordic Glory has run over today's trip and on this going, and he won five starts back, but he's been fifth, fifth and unplaced since and returns after 43 days off.
    DATA: model 6.1% | style Held up (led 4% of runs) | runs in data 11 | last 3: 13 Sep Bath Flat 5.7f Good To Soft 5/17; 28 Sep Brighton Flat 6f Good To Firm 5/8; 8 Oct Bath Flat 5f Good 10/14
    DATA for: Has won at this trip or further
    DATA against: Course: hold-up horses have won 0.7× their fair share at 6f here
- Rianka (hrs_64072414) | 3yo F | 130lb | OR 53 | draw 11 | jockey Kieran Shoemark | trainer Martin Dunne (14d 0/2) | headgear t | last run 69 days | form 457195 | MARKET 2.6% | 09:00 median 29.00 | Matchbook 46.00
    comment: Rianka has only one win in her last six, a victory three starts back, and she followed it with a ninth, then a fifth last time out, after 69 days off.
    DATA: model 7.5% | style Held up (led 5% of runs) | runs in data 7 | last 3: 23 Jul Yarmouth Flat 6f Good To Firm 1/7; 13 Aug Windsor Flat 6.1f Good To Firm 9/11; 12 Sep Lingfield Flat 6f Standard 5/10
    DATA for: Has won at this trip or further
    DATA against: Course: hold-up horses have won 0.7× their fair share at 6f here
- Sweet Desire (hrs_55484576) | 4yo F | 130lb | OR 53 | draw 1 | jockey Clifford Lee | trainer Steph Hollinshead (14d 0/3) | headgear - | last run 24 days | form 048600 | MARKET 2.2% | 09:00 median 34.00 | Matchbook 65.00
    comment: Sweet Desire is hard to fancy, unplaced in her last two and yet to win in her last six, with a sixth three starts back her best recent effort bar a fourth five runs ago.
    DATA: model 2.4% | style Held up (led 5% of runs) | runs in data 6 | last 3: 11 Aug Nottingham Flat 6.1f Good To Firm 6/6; 8 Oct Bath Flat 5f Good 12/14; 27 Oct Catterick Flat 6f Soft 10/10 fig 11
    DATA against: Best recent form figure 11, 38 lb below field average; Recent figures 42 lb below its current mark (looks high in the weights); Poor recent finishing positions; Course: hold-up horses have won 0.7× their fair share at 6f here
- Sir Rodneyredblood (hrs_18809490) | 9yo G | 132lb | OR 55 | draw 5 | jockey Marco Ghiani | trainer J. R. Jenkins (14d 0/3) | headgear p | last run 129 days | form 583820 | MARKET 2.0% | 09:00 median 34.00 | Matchbook 60.00
    comment: Winless in his last six, Sir Rodneyredblood was second two starts back and has run over today's trip and going, but he was unplaced last time and returns after 129 days off.
    DATA: model 4.4% | style Leader (led 43% of runs) | runs in data 8 | last 3: 28 Apr Yarmouth Flat 6f Good 8/8; 26 Jun Yarmouth Flat 6f Good To Firm 2/6; 14 Jul Leicester Flat 6f Good To Firm 10/11
    DATA for: Has won at this trip or further
    DATA against: Last-run finishing speed -3.1% vs that field (faded); Returns from a 129-day break; Aged 9, older than most of this field
- Penny's Spirit (hrs_47313784) | 5yo M | 130lb | OR 53 | draw 2 | jockey Poppy Scott(7) | trainer Gary Brown (14d 0/1) | headgear - | last run 386 days | form /5930- | MARKET 1.5% | 09:00 median 51.00 | Matchbook 80.00
    comment: Penny's Spirit is winless in her last four, unplaced last time and returning after 386 days off, which makes her hard to fancy.
    DATA: model 7.3% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 386-day break; Lightly raced: 0 runs in our data, so the model has little to go on

## 8:30 Wolverhampton (AW) | race_id rac_32304938705 | Midnite Built Different Handicap Stakes
Flat | Class 6 | 1m1f104y | going Standard | AW | 13 runners | rating band 0-65 | age 3yo+
DATA pace: Lone leader - Sant Alessio is the only habitual front-runner and may be allowed an easy lead.
- Exotic Baby (hrs_56219436) | 3yo G | 130lb | OR 64 | draw 3 | jockey Billy Loughnane | trainer Ian Williams (14d 1/8) | headgear - | last run 22 days | form 570935 | MARKET 15.9% | 09:00 median 5.00 | Matchbook 5.70 | CHECK (skip line 4.75)
    comment: Exotic Baby arrives fresh from a fifth last time out, 22 days ago, and a third two starts back shows he can hit the frame, while he has run over today's trip and going before.
    DATA: model 6.3% | style Held up (led 5% of runs) | runs in data 9 | last 3: 3 Sep Southwell Flat 7.1f Standard 9/9; 1 Oct Newcastle Flat 8f Standard 3/10; 29 Oct Southwell (AW) Flat 8f Standard 5/13 fig 60
- San Juanito (hrs_47162094) | 4yo G | 131lb | OR 62 | draw 5 | jockey Rob Hornby | trainer Mike Murphy (14d 1/2) | headgear p | last run 13 days | form 808821 | MARKET 15.0% | 09:00 median 4.75 | Matchbook 6.80
    comment: He has run over today's trip and going, and carries 131 lb from stall five.
    DATA: model 10.7% | style Midfield (led 3% of runs) | runs in data 8 | last 3: 9 Oct Kempton Flat 7f Standard To Slow 8/11; 23 Oct Wolverhampton (AW) Flat 8.5f Standard 2/11 fig 58; 7 Nov Southwell (AW) Flat 8f Standard 1/11 fig 62
    DATA for: Good recent finishing positions
- Pulsar Star (hrs_55454140) | 4yo G | 134lb | OR 65 | draw 11 | jockey Robert Havlin | trainer Thomas Faulkner (14d 0/3) | headgear - | last run 24 days | form 966856 | MARKET 13.3% | 09:00 median 6.00 | Matchbook 6.80
    comment: The main risk is a form line of fifth and worse, yet to win in his last six starts.
    DATA: model 7.9% | style Prominent (led 4% of runs) | runs in data 8 | last 3: 21 Jul Wolverhampton Flat 9.5f Standard 8/13; 5 Oct Wolverhampton Flat 9.5f Standard 5/10; 27 Oct Wolverhampton (AW) Flat 12f Standard 6/10 fig 62
- Sant Alessio (hrs_37563883) | 5yo G | 132lb | OR 63 | draw 4 | jockey Taylor Fisher | trainer Joe Tickle (14d 0/4) | headgear - | last run 24 days | form 074844 | MARKET 10.1% | 09:00 median 7.50 | Matchbook 9.60
    comment: Sant Alessio is yet to win in his last six, though back-to-back fourths show he's competitive, and he has run over today's trip and going before after 24 days off.
    DATA: model 8.5% | style Leader (led 54% of runs) | runs in data 6 | last 3: 13 Sep Bath Flat 8f Good To Soft 8/10; 5 Oct Wolverhampton Flat 9.5f Standard 4/10; 27 Oct Wolverhampton (AW) Flat 8.5f Standard 4/10 fig 64
    DATA for: Best recent form figure 64, 6 lb above field average; Pace: may get an uncontested lead
- Chesneys Charm (hrs_42226226) | 4yo G | 130lb | OR 61 | draw 6 | jockey Elle-May Croot(5) | trainer Ivan Furtado (14d 1/7) | headgear - | last run 31 days | form 373454 | MARKET 9.2% | 09:00 median 9.00 | Matchbook 9.80
    comment: Chesneys Charm has run over today's trip and going and was a fourth last time out, with a third four starts back, yet he is winless in his last six and returns after 31 days.
    DATA: model 9.3% | style Held up (led 4% of runs) | runs in data 10 | last 3: 5 Oct Kempton Flat 12f Standard To Slow 4/10; 15 Oct Southwell (AW) Flat 11f Standard 5/7 fig 56; 20 Oct Newcastle (AW) Flat 8f Standard 4/12 fig 62
- The Dark Baron (hrs_42615769) | 4yo G | 134lb | OR 65 | draw 9 | jockey Charlie Tucker(7) | trainer Kathy Turner (14d 0/0) | headgear - | last run 22 days | form 444195 | MARKET 8.7% | 09:00 median 9.00 | Matchbook 11.00
    comment: The Dark Baron is hard to fancy after a ninth two starts back and a fifth last time out, with just the one win in his last six, a winner three starts back.
    DATA: model 10.0% | style Held up (led 3% of runs) | runs in data 11 | last 3: 15 Sep Wolverhampton Flat 9.5f Standard 1/12; 5 Oct Wolverhampton Flat 9.5f Standard 9/11; 29 Oct Bath Flat 10f Soft 5/12 fig 63
    DATA for: Best recent form figure 63, 5 lb above field average; Has won at this trip or further
- Urban Road (hrs_28221466) | 7yo G | 131lb | OR 62 | draw 8 | jockey Tom Eaves | trainer Alan Brown (14d 1/1) | headgear v | last run 21 days | form 500977 | MARKET 7.0% | 09:00 median 11.00 | Matchbook 13.50
    comment: Urban Road has finished seventh in each of his last two, after a ninth three starts back, so he is winless in recent starts, though he has run over today's trip and going and returns after 21 days.
    DATA: model 4.0% | style Held up (led 3% of runs) | runs in data 14 | last 3: 6 Jul Ripon Flat 8f Good 9/9; 16 Oct Newcastle (AW) Flat 8f Standard 7/9 fig 58; 30 Oct Newcastle (AW) Flat 10f Standard 7/14 fig 58
    DATA against: Poor recent finishing positions
- Super Hit (hrs_36529045) | 5yo G | 133lb | OR 64 | draw 12 | jockey Jason Watson | trainer James Owen (14d 2/29) | headgear ht | last run 16 days | form 552337 | MARKET 6.5% | 09:00 median 12.50 | Matchbook 14.00
    comment: Super Hit is a consistent sort, with a third three starts back, a third two starts back and a second four starts back, and he has run over today's trip and going, so a bounce back from a seventh last time out is possible after 16 days off.
    DATA: model 11.8% | style Midfield (led 4% of runs) | runs in data 18 | last 3: 5 Oct Kempton Flat 12f Standard To Slow 3/10; 15 Oct Southwell (AW) Flat 11f Standard 3/7 fig 62; 4 Nov Kempton (AW) Flat 12f Standard / Slow 7/14 fig 61
    DATA for: Has won at this trip or further; Good recent finishing positions
- Born A Rebel (hrs_37407405) | 5yo M | 131lb | OR 62 | draw 1 | jockey Clifford Lee | trainer Patrick Owens (14d 0/0) | headgear - | last run 16 days | form 230844 | MARKET 6.0% | 09:00 median 11.00 | Matchbook 18.00
    comment: Born A Rebel arrives fresh enough after 16 days, with a fourth last time out and another fourth two starts back, and she has run over today's trip and going.
    DATA: model 9.7% | style Prominent (led 5% of runs) | runs in data 12 | last 3: 22 Oct Newmarket Flat 8f Soft 8/13 fig 67; 30 Oct Newmarket Flat 8f Good To Soft 4/15 fig 69; 4 Nov Nottingham Flat 8.5f Soft 4/15 fig 68
    DATA for: Best recent form figure 69, 11 lb above field average; Recent figures 7 lb above its current mark (looks well handicapped); Last-run finishing speed +5.3% vs that field (finished strongly)
- Mc'ted (hrs_24676218) | 8yo G | 134lb | OR 65 | draw 13 | jockey Alice Bond(5) | trainer Martin Dunne (14d 0/2) | headgear - | last run 29 days | form 314460 | MARKET 2.6% | 09:00 median 23.00 | Matchbook 55.00
    comment: Mc'ted is a gelding with a win five starts back but unplaced last time and a sixth two starts back, so form has cooled.
    DATA: model 3.6% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 11 Apr Yarmouth Flat 10.1f Good 11/13; 22 Oct Southwell (AW) Flat 8f Standard 10/11 fig 52
    DATA against: Best recent form figure 52, 6 lb below field average; Recent figures 13 lb below its current mark (looks high in the weights); Lightly raced: 2 runs in our data, so the model has little to go on; Aged 8, older than most of this field
- Made All (hrs_37027032) | 5yo G | 134lb | OR 65 | draw 10 | jockey George Wood | trainer Sam England (14d 3/24) | headgear t | last run 24 days | form 533659 | MARKET 2.2% | 09:00 median 29.00 | Matchbook 60.00
    comment: Made All is winless in his last six, though he has been third twice in that spell, four and five starts back, and he has run over today's trip and going. A ninth last time out and 134 lb from draw 10 leave him with plenty to prove.
    DATA: model 7.9% | style Held up (led 4% of runs) | runs in data 15 | last 3: 29 Sep Sedgefield Hurdle 16.8f Good 1/7; 17 Oct Stratford Hurdle 16.5f Good 3/7 fig 93; 27 Oct Wolverhampton (AW) Flat 12f Standard 9/10 fig 56
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Recent figures 9 lb below its current mark (looks high in the weights)
- Rua Mor (hrs_56843682) | 4yo G | 130lb | OR 61 | draw 7 | jockey Jonny Peate | trainer Sam England (14d 3/24) | headgear - | last run 25 days | form 558380 | MARKET 2.0% | 09:00 median 40.50 | Matchbook 60.00
    comment: Rua Mor is winless in his last six, with an unplaced effort last time out and a third three starts back the only podium finish in that run.
    DATA: model 6.0% | style Prominent (led 23% of runs) | runs in data 7 | last 3: 21 Sep Wolverhampton Flat 8.6f Standard 3/10; 12 Oct Newcastle Flat 8f Standard 8/13; 26 Oct Redcar Flat 7f Heavy 12/12 fig 33
    DATA against: Best recent form figure 33, 25 lb below field average; Recent figures 28 lb below its current mark (looks high in the weights)
- King Chaos (hrs_44264423) | 5yo G | 130lb | OR 61 | draw 2 | jockey Kaiya Fraser | trainer Rebecca Menzies (14d 1/9) | headgear p | last run 22 days | form -17800 | MARKET 1.6% | 09:00 median 41.00 | Matchbook 80.00
    comment: King Chaos has been well beaten in each of his last four runs, unplaced twice most recently, after a win five starts back, and that makes him hard to fancy.
    DATA: model 4.4% | style Held up (led 5% of runs) | runs in data 5 | last 3: 30 Jul Wolverhampton Flat 8.6f Standard 8/11; 10 Aug Ayr Flat 10f Good To Soft 10/12; 29 Oct Southwell (AW) Flat 11f Standard 10/10 fig 52
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 52, 6 lb below field average; Recent figures 9 lb below its current mark (looks high in the weights); Poor recent finishing positions
