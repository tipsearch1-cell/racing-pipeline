# Card review packet: Newcastle (AW), 2026-11-19

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
{"meeting": "newcastle_aw", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 3:35 Newcastle (AW) | race_id rac_32304836044 | Midnite It's Actually Pretty Good Handicap Stakes (GBBPlus Race)
Flat | Class 2 | 1m2f42y | going Standard | AW | 8 runners | rating band 0-105 | age 3yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Water To Wine (hrs_63551250) | 3yo G | 135lb | OR 102 | draw 2 | jockey Robert Havlin | trainer John & Thady Gosden (14d 5/14) | headgear - | last run 40 days | form 1130 | MARKET 40.4% | 09:00 median 2.20 | Matchbook 2.36
    comment: Water To Wine won two of his last four, including a winner three starts back, but he was unplaced last time out and returns after 40 days off.
    DATA: model 22.0% | style Prominent (led 29% of runs) | runs in data 4 | last 3: 27 May Kempton Flat 11f Standard To Slow 1/10; 19 Jun Ascot Flat 12f Good To Firm 3/5; 10 Oct York Flat 10.3f Soft 16/18
    DATA for: Official rating 102, 8 lb above field average; Trainer 36% wins (5/14), last 14 days; Has won at this trip or further; Good recent finishing positions
    DATA against: Last-run finishing speed -2.7% vs that field (faded); Carries 6 lb more than average
- Stoneacre Donny (hrs_54965456) | 3yo G | 124lb | OR 91 | draw 8 | jockey Duran Fentiman | trainer Tim Easterby (14d 0/12) | headgear - | last run 13 days | form 329152 | MARKET 20.7% | 09:00 median 4.33 | Matchbook 4.60
    comment: Beaten out of the first three only twice in his last six, Stoneacre Donny was second last time out just 13 days ago and has run over today's trip and going before.
    DATA: model 17.0% | style Midfield (led 3% of runs) | runs in data 8 | last 3: 6 Sep York Flat 10.3f Good To Soft 1/15; 10 Sep Doncaster Flat 10.2f Good To Soft 5/11; 6 Nov Newcastle (AW) Flat 10f Standard 2/14 fig 90
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Trainer 0 wins from 12 runs, last 14 days
- Savvy Disko (hrs_57406972) | 3yo C | 125lb | OR 92 | draw 4 | jockey Jack Callan | trainer S. P. C. Woods (14d 0/0) | headgear - | last run 64 days | form 4-11F6 | MARKET 11.3% | 09:00 median 8.00 | Matchbook 8.40
    comment: Two wins in his last five starts, a winner three starts back and again four starts back, makes him a serious threat, and he has run over today's trip and going before. The risk is a sixth last time out, a fall before that and a 64-day break.
    DATA: model 9.2% | style Prominent (led 8% of runs) | runs in data 4 | last 3: 27 Jun Lingfield Flat 9f Good To Firm 1/5; 30 Jul Goodwood Flat 9.9f Good To Firm F/14; 16 Sep Yarmouth Flat 9.1f Good To Soft 6/11
- Paddy The Squire (hrs_32209310) | 6yo G | 140lb | OR 104 | draw 1 | jockey Andrew Mullen | trainer Iain Jardine (14d 0/4) | headgear tb | last run 40 days | form 632026 | MARKET 9.8% | 09:00 median 7.50 | Matchbook 12.00
    comment: The main risk is a sixth last time out and a 40-day absence, while he remains winless in his last six.
    DATA: model 19.7% | style Prominent (led 5% of runs) | runs in data 6 | last 3: 22 Aug York Flat 13.9f Good To Soft 14/22; 19 Sep Newbury Flat 10f Good To Firm 2/11; 10 Oct York Flat 10.3f Soft 6/18
    DATA for: Official rating 104, 10 lb above field average; Last-run finishing speed +2.2% vs that field (finished strongly)
    DATA against: Carries 11 lb more than average
- Ozat (hrs_40132876) | 5yo G | 129lb | OR 93 | draw 6 | jockey Edward Greatrex | trainer Ian Williams (14d 0/8) | headgear - | last run 41 days | form 800370 | MARKET 9.3% | 09:00 median 9.50 | Matchbook 10.50
    comment: The main risk is a winless recent run, including an unplaced effort last time out after 41 days off.
    DATA: model 8.9% | style Held up (led 8% of runs) | runs in data 8 | last 3: 8 Aug Ascot Flat 8f Good To Firm 3/10; 4 Sep Ascot Flat 8f Good 7/13; 9 Oct York Flat 7.9f Good To Soft 17/17
    DATA against: Trainer 0 wins from 8 runs, last 14 days; Pace: steady gallop likely, hard to come from off the pace
- Pearl Eye (hrs_29917916) | 6yo G | 121lb | OR 85 | draw 7 | jockey Lauren Young(5) | trainer Jim Goldie (14d 0/7) | headgear p | last run 26 days | form 466125 | MARKET 5.2% | 09:00 median 17.00 | Matchbook 19.00
    comment: Pearl Eye was fifth last time out, but he did win three starts back and was second the run after, so there is some substance to his form.
    DATA: model 10.9% | style Held up (led 3% of runs) | runs in data 12 | last 3: 17 Sep Ayr Flat 13.1f Soft 1/11; 10 Oct York Flat 10.3f Good To Soft 2/19; 24 Oct Doncaster Flat 10f Heavy 5/14 fig 84
    DATA for: Has won at this trip or further; Good recent finishing positions; Carries 8 lb less than average
    DATA against: Best recent form figure 84, 9 lb below field average; Official rating 85, 9 lb below field average; Pace: steady gallop likely, hard to come from off the pace
- Deira Mile (hrs_36515178) | 5yo G | 138lb | OR 102 | draw 3 | jockey Darragh O'Sullivan(7) | trainer Jessica Bedi (14d 0/6) | headgear p | last run 12 days | form 68-678 | MARKET 1.7% | 09:00 median 41.00 | Matchbook 80.00
    comment: He is yet to win in his last five starts, but he carries 138 lb from stall three.
    DATA: model 5.2% | style Held up (led 5% of runs) | runs in data 3 | last 3: 1 May Ascot Flat 15.9f Good To Firm 6/8; 15 May York Flat 13.9f Good 7/7; 7 Nov Doncaster Flat 12f Good To Soft 8/23 fig 104
    DATA for: Best recent form figure 104, 11 lb above field average; Official rating 102, 8 lb above field average
    DATA against: Poor recent finishing positions; Carries 9 lb more than average; Pace: steady gallop likely, hard to come from off the pace
- Eddaari (hrs_56778358) | 3yo G | 118lb | OR 81 | draw 5 | jockey Rhys Elliott(5) | trainer Gary Hanmer (14d 0/4) | headgear - | last run 187 days | form 632-18 | MARKET 1.6% | 09:00 median 51.00 | Matchbook 70.00
    comment: He carries 118 lb from draw 5.
    DATA: model 7.1% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 13 Apr Newcastle Flat 8f Standard 1/8; 16 May Newmarket Flat 10f Good 8/8
    DATA for: Carries 11 lb less than average
    DATA against: Official rating 81, 13 lb below field average; Last-run finishing speed -5.1% vs that field (faded); Returns from a 187-day break; Lightly raced: 2 runs in our data, so the model has little to go on

## 4:10 Newcastle (AW) | race_id rac_32304837981 | AWC Finals Day At Newcastle 26th March Novice Stakes (GBB Race)
Flat | Class 4 | 7f14y | going Standard | AW | 13 runners | rating band - | age 3yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Big Money (hrs_59025379) | 3yo G | 132lb | OR 76 | draw 8 | jockey Jason Hart | trainer Michael Appleby (14d 1/14) | headgear - | last run 24 days | form 4-22 | MARKET 28.8% | 09:00 median 2.75 | Matchbook 3.25
    DATA: model 52.1% | style Held up (led 8% of runs) | runs in data 2 | last 3: 3 Oct Southwell Flat 7.1f Standard 2/11; 26 Oct Southwell (AW) Flat 6f Standard 2/10 fig 57
    DATA for: Best recent form figure 57, 4 lb above field average; Good recent finishing positions
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- El Ra'ady (hrs_17395634515) | 3yo G | 132lb | OR - | draw 3 | jockey Harry Davies | trainer William Haggas (14d 3/9) | headgear - | last run - days | form - | MARKET 26.0% | 09:00 median 3.25 | Matchbook 3.40
    DATA: model 3.6% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 33% wins (3/9), last 14 days
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Nip About (hrs_17392689083) | 3yo G | 132lb | OR 77 | draw 9 | jockey Billy Garritty | trainer Tracy Waggott (14d 0/1) | headgear - | last run 20 days | form 552 | MARKET 18.8% | 09:00 median 4.50 | Matchbook 4.70
    DATA: model 10.8% | style Held up (led 5% of runs) | runs in data 3 | last 3: 23 Sep Redcar Flat 7f Good 5/8; 16 Oct Newcastle (AW) Flat 5f Standard 5/6 fig 58; 30 Oct Newcastle (AW) Flat 7f Standard 2/9 fig 68
    DATA for: Best recent form figure 68, 16 lb above field average
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Veronique (hrs_66368470) | 3yo F | 127lb | OR - | draw 5 | jockey P. J. McDonald | trainer Andrew Balding (14d 0/18) | headgear - | last run 131 days | form 7 | MARKET 10.3% | 09:00 median 7.00 | Matchbook 9.80
    DATA: model 2.8% | style Held up (led 8% of runs) | runs in data 1 | last 3: 11 Jul Chester Flat 7f Good 7/7
    DATA against: Trainer 0 wins from 18 runs, last 14 days; Returns from a 131-day break; Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Janora (hrs_17391090164) | 3yo F | 127lb | OR 66 | draw 12 | jockey Dale Swift | trainer Brian Ellison (14d 1/6) | headgear t (1st time) | last run 26 days | form 6430 | MARKET 4.7% | 09:00 median 17.00 | Matchbook 21.00
    DATA: model 6.3% | style Held up (led 3% of runs) | runs in data 4 | last 3: 5 Sep Newcastle Flat 7.1f Standard 4/9; 25 Sep Newcastle Flat 6f Standard 3/5; 24 Oct Southwell (AW) Flat 7f Standard 11/14 fig 59
    DATA for: Best recent form figure 59, 6 lb above field average; First-time headgear
    DATA against: Official rating 66, 7 lb below field average; Pace: steady gallop likely, hard to come from off the pace
- Win Or Lose (hrs_17395611569) | 3yo G | 132lb | OR - | draw 11 | jockey David Nolan | trainer Ivan Furtado (14d 1/5) | headgear - | last run - days | form - | MARKET 3.3% | 09:00 median 21.00 | Matchbook 38.00
    DATA: model 3.6% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 20% wins (1/5), last 14 days
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Ezenli (hrs_17394289045) | 4yo G | 133lb | OR - | draw 1 | jockey Hollie Doyle | trainer Archie Watson (14d 0/1) | headgear - | last run 9 days | form - | MARKET 2.0% | 09:00 median 30.00 | Matchbook 90.00
    DATA: model 4.5% | style Held up (led 8% of runs) | runs in data 2 | last 3: 25 Oct Market Rasen NH Flat 16.5f Good To Soft 4/4; 10 Nov Lingfield (AW) NH Flat 16f Standard / Slow 3/4 fig 92
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Savernake (hrs_17392475268) | 3yo G | 132lb | OR - | draw 4 | jockey Cam Hardie | trainer Antony Brittain (14d 1/5) | headgear - | last run 20 days | form 46 | MARKET 1.6% | 09:00 median 51.00 | Matchbook 100.00
    DATA: model 3.6% | style Held up (led 5% of runs) | runs in data 2 | last 3: 19 Sep Newcastle Flat 7.1f Standard 4/6; 30 Oct Newcastle (AW) Flat 7f Standard 6/9 fig 46
    DATA for: Trainer 20% wins (1/5), last 14 days
    DATA against: Best recent form figure 46, 6 lb below field average; Lightly raced: 2 runs in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Casement Park (hrs_17391997574) | 3yo G | 132lb | OR - | draw 7 | jockey Aiden Brookes | trainer Simon West (14d 0/1) | headgear - | last run 21 days | form 04 | MARKET 1.2% | 09:00 median 51.00 | Matchbook 140.00
    DATA: model 1.7% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 9 Sep Carlisle Flat 11.2f Good 11/12; 29 Oct Southwell (AW) Flat 8f Standard 4/8 fig 46
    DATA against: Best recent form figure 46, 6 lb below field average; Lightly raced: 2 runs in our data, so the model has little to go on
- Wind The Bobbin Up (hrs_17394685385) | 3yo G | 132lb | OR - | draw 13 | jockey Tom Eaves | trainer Tracy Waggott (14d 0/1) | headgear - | last run - days | form - | MARKET 1.1% | 09:00 median 81.00 | Matchbook 120.00
    DATA: model 3.6% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Momotombo (hrs_17393595450) | 3yo F | 127lb | OR - | draw 6 | jockey Ryan Sexton | trainer Julie Camacho (14d 0/6) | headgear - | last run 21 days | form 55 | MARKET 0.8% | 09:00 median 101.00 | Matchbook 220.00
    DATA: model 2.6% | style Held up (led 5% of runs) | runs in data 2 | last 3: 10 Oct Southwell Flat 7.1f Standard 5/7; 29 Oct Southwell (AW) Flat 8f Standard 5/8 fig 39
    DATA against: Best recent form figure 39, 14 lb below field average; Lightly raced: 2 runs in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Medran (hrs_17392896640) | 3yo G | 132lb | OR - | draw 10 | jockey Oliver Stammers | trainer Grant Tuer (14d 1/4) | headgear - | last run 38 days | form 85 | MARKET 0.7% | 09:00 median 101.00 | Matchbook 180.00
    DATA: model 1.3% | style Held up (led 5% of runs) | runs in data 2 | last 3: 26 Sep Ripon Flat 12f Good 8/9; 12 Oct Newcastle Flat 10.2f Standard 5/7
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Elsy D (hrs_17395640773) | 3yo G | 132lb | OR - | draw 2 | jockey Andrew Mullen | trainer Chris Grant (14d 1/3) | headgear - | last run - days | form - | MARKET 0.7% | 09:00 median 101.00 | Matchbook 200.00
    DATA: model 3.6% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on

## 4:40 Newcastle (AW) | race_id rac_32304839918 | AW Trials Day - Lingfield 2nd Jan 2027 Nursery Handicap Stakes
Flat | Class 6 | 6f | going Standard | AW | 12 runners | rating band 0-65 | age 2yo
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Espresso Breeze (hrs_17392238507) | 2yo C | 135lb | OR 65 | draw 8 | jockey Conor Whiteley(5) | trainer Bryan Smart (14d 1/4) | headgear - | last run 33 days | form 795 | MARKET 18.3% | 09:00 median 4.42 | Matchbook 5.00 | CHECK (skip line 4.20)
    comment: Espresso Breeze is winless in his last three, finishing fifth last time out after a ninth and a seventh, though he has run over today's trip and going and returns after 33 days off.
    DATA: model 8.1% | style Held up (led 5% of runs) | runs in data 3 | last 3: 16 Sep Beverley Flat 5f Good 7/13; 2 Oct Newcastle Flat 6f Standard 9/12; 17 Oct Southwell (AW) Flat 6f Standard 5/11 fig 58
    DATA for: Official rating 65, 11 lb above field average
    DATA against: Recent figures 7 lb below its current mark (looks high in the weights); Carries 11 lb more than average; Pace: steady gallop likely, hard to come from off the pace
- Angelic Melody (hrs_17389663340) | 2yo F | 126lb | OR 56 | draw 12 | jockey Ryan Sexton | trainer Julie Camacho (14d 0/6) | headgear p | last run 14 days | form 6754 | MARKET 16.4% | 09:00 median 5.00 | Matchbook 5.50
    DATA: model 12.7% | style Held up (led 8% of runs) | runs in data 4 | last 3: 9 Sep Carlisle Flat 5.8f Good 7/13; 13 Oct Leicester Flat 6f Good To Soft 5/11; 5 Nov Southwell (AW) Flat 6f Standard 4/13 fig 62
    DATA for: Best recent form figure 62, 6 lb above field average; Recent figures 6 lb above its current mark (looks well handicapped)
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Ma Fille de Reve (hrs_65322411) | 2yo F | 122lb | OR 52 | draw 1 | jockey Zak Wheatley | trainer Declan Carroll (14d 0/4) | headgear - | last run 44 days | form 66528 | MARKET 12.4% | 09:00 median 6.00 | Matchbook 8.20
    comment: A 44-day break and 122 lb from stall one temper the case.
    DATA: model 16.8% | style Midfield (led 4% of runs) | runs in data 5 | last 3: 8 Jul Catterick Flat 5f Good To Firm 5/6; 14 Sep Thirsk Flat 6f Good 2/16; 6 Oct Leicester Flat 6f Good To Firm 8/13
- Yorkshire Dream (hrs_64621543) | 2yo G | 116lb | OR 46 | draw 7 | jockey Andrew Mullen | trainer Ben Haslam (14d 2/5) | headgear p | last run 50 days | form 570934 | MARKET 12.0% | 09:00 median 6.50 | Matchbook 8.00
    comment: Yorkshire Dream is winless in his last six, though a fourth last time out and a third two starts back show he can get involved, and he has run over today's trip and going.
    DATA: model 7.4% | style Held up (led 5% of runs) | runs in data 6 | last 3: 13 Aug Beverley Flat 7.3f Good To Firm 9/10; 2 Sep Newcastle Flat 6f Standard 3/11; 30 Sep Musselburgh Flat 5f Good To Soft 4/6
    DATA for: Trainer 40% wins (2/5), last 14 days; Carries 8 lb less than average
    DATA against: Official rating 46, 8 lb below field average; Pace: steady gallop likely, hard to come from off the pace
- River Jordan (hrs_63323414) | 2yo G | 123lb | OR 53 | draw 5 | jockey Rowan Scott | trainer Phillip Makin (14d 0/1) | headgear - | wind surgery | last run 66 days | form 75760 | MARKET 8.7% | 09:00 median 9.00 | Matchbook 11.50
    comment: River Jordan is winless in his last five, finishing unplaced last time, then sixth and seventh, and returns after 66 days off, though he has run over today's trip and going.
    DATA: model 9.5% | style Held up (led 4% of runs) | runs in data 5 | last 3: 1 Aug Thirsk Flat 5f Good 7/8; 2 Sep Newcastle Flat 6f Standard 6/11; 14 Sep Thirsk Flat 6f Good 11/16
    DATA against: Poor recent finishing positions; Pace: steady gallop likely, hard to come from off the pace
- North Coates (hrs_17390793952) | 2yo G | 116lb | OR 46 | draw 11 | jockey Finlay Bassett(7) | trainer Michael & David Easterby (14d 0/7) | headgear - | last run 50 days | form 56752 | MARKET 6.6% | 09:00 median 12.00 | Matchbook 14.50
    comment: North Coates was second last time out, but he is winless in his last five and was well held in the three runs before that, with a 50-day break to overcome.
    DATA: model 6.3% | style Held up (led 8% of runs) | runs in data 5 | last 3: 11 Sep Chester Flat 6.1f Good To Soft 7/9; 28 Sep Hamilton Flat 6f Soft 5/7; 30 Sep Musselburgh Flat 5f Good To Soft 2/6
    DATA for: Carries 8 lb less than average
    DATA against: Official rating 46, 8 lb below field average; Pace: steady gallop likely, hard to come from off the pace
- Crystal Kraken (hrs_64135015) | 2yo F | 128lb | OR 58 | draw 10 | jockey M. P. Sheehy | trainer Dylan Cunha (14d 0/7) | headgear - | last run 45 days | form 223005 | MARKET 5.8% | 09:00 median 13.00 | Matchbook 17.00
    comment: The risk is that she's yet to win and was only fifth last time, after 45 days off.
    DATA: model 6.2% | style Held up (led 5% of runs) | runs in data 10 | last 3: 7 Sep Wolverhampton Flat 5.1f Standard 11/11; 21 Sep Leicester Flat 6f Good 14/14; 5 Oct Yarmouth Flat 7f Good To Firm 5/8
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Mollisha (hrs_17389051099) | 2yo F | 132lb | OR 62 | draw 4 | jockey Clifford Lee | trainer Brian Ellison (14d 1/6) | headgear p (1st time) | last run 17 days | form 34770 | MARKET 5.3% | 09:00 median 15.00 | Matchbook 18.00
    comment: Mollisha has run over today's trip and on this going, and she returns after a fresh 17 days, but she's winless in her last five, with a third five starts back her best finish.
    DATA: model 9.7% | style Prominent (led 5% of runs) | runs in data 5 | last 3: 2 Oct Newcastle Flat 6f Standard 7/12; 22 Oct Southwell (AW) Flat 6f Standard 7/8 fig 60; 2 Nov Wolverhampton (AW) Flat 5f Standard 11/11 fig 52
    DATA for: Best recent form figure 60, 4 lb above field average; Official rating 62, 8 lb above field average; First-time headgear
    DATA against: Poor recent finishing positions; Carries 8 lb more than average
- Kumharas (hrs_17391574116) | 2yo F | 128lb | OR 58 | draw 3 | jockey Oisin McSweeney | trainer Richard & Peter Fahey (14d 1/11) | headgear - | last run 23 days | form 545 | MARKET 4.5% | 09:00 median 17.00 | Matchbook 23.00
    comment: Kumharas has finished a fifth last time out, a fourth two starts back and a fifth three starts back, so she is yet to win in her last three and has a bit to prove, though she has run over today's trip and is fresh enough after 23 days off.
    DATA: model 11.5% | style Prominent (led 29% of runs) | runs in data 3 | last 3: 1 Sep Ripon Flat 5f Soft 5/5; 21 Sep Hamilton Flat 5f Soft 4/5; 27 Oct Catterick Flat 5f Soft 5/9 fig 47
    DATA against: Best recent form figure 47, 9 lb below field average; Recent figures 11 lb below its current mark (looks high in the weights)
- Turbo Shandy (hrs_65642437) | 2yo F | 122lb | OR 52 | draw 2 | jockey Sean Dylan Bowen | trainer Ivan Furtado (14d 1/5) | headgear p (1st time) | last run 136 days | form 947 | MARKET 4.5% | 09:00 median 15.00 | Matchbook 26.00
    comment: Turbo Shandy is hard to fancy, having finished seventh last time out, a fourth two starts back and a ninth three starts back, and she returns after 136 days off.
    DATA: model 3.6% | style Held up (led 5% of runs) | runs in data 3 | last 3: 13 Jun Chester Flat 7f Good To Soft 9/11; 22 Jun Musselburgh Flat 7.1f Good 4/5; 6 Jul Ripon Flat 6f Good 7/11
    DATA for: Trainer 20% wins (1/5), last 14 days; First-time headgear
    DATA against: Returns from a 136-day break; Pace: steady gallop likely, hard to come from off the pace
- Halcon (hrs_65322390) | 2yo F | 127lb | OR 57 | draw 6 | jockey Sean Kirrane | trainer Tim Easterby (14d 0/12) | headgear b (1st time) | last run 13 days | form 36808 | MARKET 3.0% | 09:00 median 29.00 | Matchbook 36.00
    comment: The risk is form that has tailed off, with an eighth last time out and a third five starts back her best finish.
    DATA: model 7.0% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 29 Aug Beverley Flat 7.3f Soft 8/13; 9 Sep Carlisle Flat 5.8f Good 10/13; 6 Nov Newcastle (AW) Flat 7f Standard 8/11 fig 53
    DATA for: First-time headgear
    DATA against: Trainer 0 wins from 12 runs, last 14 days; Poor recent finishing positions
- Hey Dougie (hrs_66585995) | 2yo C | 115lb | OR 44 | draw 9 | jockey Aiden Brookes | trainer Philip Kirby (14d 1/13) | headgear - | last run 89 days | form 000 | MARKET 2.5% | 09:00 median 34.00 | Matchbook 46.00
    comment: Hey Dougie is hard to fancy, unplaced in each of his last three starts and returning after 89 days off, though he has run over today's trip and runs off a lowly official mark of 44.
    DATA: model 1.2% | style Held up (led 4% of runs) | runs in data 3 | last 3: 10 Jul Chester Flat 6.1f Good 11/12; 22 Jul Catterick Flat 7f Good To Firm 10/10; 22 Aug Redcar Flat 6f Good 11/12
    DATA for: Carries 9 lb less than average
    DATA against: Official rating 44, 10 lb below field average; Poor recent finishing positions; Pace: steady gallop likely, hard to come from off the pace

## 5:10 Newcastle (AW) | race_id rac_32304841855 | All-Weather Championship Is Back EBF Novice Stakes (Div I) (GBB Race)
Flat | Class 3 | 7f14y | going Standard | AW | 7 runners | rating band - | age 2yo
DATA pace: Unclear - Running styles known for only 3 of 7 runners.
- High Threshold (hrs_17393095853) | 2yo C | 133lb | OR - | draw 4 | jockey Hollie Doyle | trainer Archie Watson (14d 0/1) | headgear - | last run 48 days | form 2 | MARKET 33.9% | 09:00 median 2.63 | Matchbook 2.80
    DATA: model 29.4% | style Held up (led 8% of runs) | runs in data 1 | last 3: 2 Oct Newcastle Flat 6f Standard 2/12
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Idealise (hrs_17394173272) | 2yo C | 133lb | OR - | draw 7 | jockey P. J. McDonald | trainer Andrew Balding (14d 0/18) | headgear - | last run 24 days | form 6 | MARKET 23.2% | 09:00 median 3.75 | Matchbook 4.20
    DATA: model 27.8% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 26 Oct Kempton (AW) Flat 7f Standard / Slow 6/10 fig 45
    DATA against: Trainer 0 wins from 18 runs, last 14 days; Lightly raced: 1 run in our data, so the model has little to go on
- Tabkir (hrs_17395648074) | 2yo C | 133lb | OR - | draw 1 | jockey Robert Havlin | trainer John & Thady Gosden (14d 5/14) | headgear - | last run - days | form - | MARKET 19.0% | 09:00 median 4.50 | Matchbook 5.30
    DATA: model 10.6% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 36% wins (5/14), last 14 days
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Bronze Cascade (hrs_17395642859) | 2yo C | 133lb | OR - | draw 5 | jockey Clifford Lee | trainer K. R. Burke (14d 0/9) | headgear - | last run - days | form - | MARKET 13.8% | 09:00 median 6.50 | Matchbook 7.00
    DATA: model 10.6% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Trainer 0 wins from 9 runs, last 14 days; Lightly raced: 0 runs in our data, so the model has little to go on
- Third Chapter (hrs_17395649117) | 2yo C | 133lb | OR - | draw 6 | jockey Shane Foley | trainer William Haggas (14d 3/9) | headgear - | last run - days | form - | MARKET 9.3% | 09:00 median 9.00 | Matchbook 11.50
    DATA: model 10.6% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 33% wins (3/9), last 14 days
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Spruce (hrs_65036048) | 2yo G | 133lb | OR - | draw 8 | jockey Oliver Stammers | trainer Grant Tuer (14d 1/4) | headgear - | last run 48 days | form 60 | MARKET 0.5% | 09:00 median 201.00 | Matchbook 290.00
    DATA: model 6.4% | style Unknown | runs in data 2 | last 3: 30 Jun Salisbury Flat 7f Good To Firm 6/8; 2 Oct Newcastle Flat 6f Standard 12/12
    DATA against: Last-run finishing speed -3.3% vs that field (faded); Lightly raced: 2 runs in our data, so the model has little to go on
- Binksy Boy (hrs_17392462752) | 2yo G | 133lb | OR - | draw 2 | jockey Sam James | trainer Phillip Makin (14d 0/1) | headgear - | last run 24 days | form 08 | MARKET 0.4% | 09:00 median 201.00 | Matchbook 310.00
    DATA: model 4.6% | style Held up (led 5% of runs) | runs in data 2 | last 3: 25 Sep Newcastle Flat 7.1f Standard 13/13; 26 Oct Redcar Flat 7f Soft 8/11 fig 20
    DATA against: Last-run finishing speed -3.0% vs that field (faded); Lightly raced: 2 runs in our data, so the model has little to go on

## 5:40 Newcastle (AW) | race_id rac_32304843792 | All-Weather Championship Is Back EBF Novice Stakes (Div II) (GBB Race)
Flat | Class 3 | 7f14y | going Standard | AW | 7 runners | rating band - | age 2yo
DATA pace: Unclear - Running styles known for only 2 of 7 runners.
- Shimmering Shadow (hrs_17391713878) | 2yo C | 133lb | OR - | draw 3 | jockey Harry Davies | trainer Simon & Ed Crisford (14d 0/3) | headgear - | last run 76 days | form 7 | MARKET 32.6% | 09:00 median 2.63 | Matchbook 2.86
    DATA: model 27.3% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 4 Sep Ascot Flat 7f Good 7/11
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Inkjet (hrs_17391925607) | 2yo C | 133lb | OR - | draw 5 | jockey Jack Callan | trainer William Haggas (14d 3/9) | headgear - | last run 72 days | form 8 | MARKET 22.8% | 09:00 median 3.75 | Matchbook 4.20
    DATA: model 14.7% | style Unknown | runs in data 1 | last 3: 8 Sep Leicester Flat 7f Good To Soft 8/9
    DATA for: Trainer 33% wins (3/9), last 14 days
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Sede Vacante (hrs_17395645988) | 2yo C | 133lb | OR - | draw 7 | jockey Clifford Lee | trainer K. R. Burke (14d 0/9) | headgear - | last run - days | form - | MARKET 21.5% | 09:00 median 4.00 | Matchbook 4.40
    DATA: model 11.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Trainer 0 wins from 9 runs, last 14 days; Lightly raced: 0 runs in our data, so the model has little to go on
- On A Boat That Day (hrs_17389295161) | 2yo C | 133lb | OR - | draw 6 | jockey Sean Dylan Bowen | trainer Roger Varian (14d 3/6) | headgear - | last run - days | form - | MARKET 16.7% | 09:00 median 5.50 | Matchbook 5.50
    DATA: model 11.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 50% wins (3/6), last 14 days
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Hot Moonstone (hrs_17393848899) | 2yo C | 133lb | OR - | draw 4 | jockey Jason Hart | trainer Jennie Candlish (14d 3/20) | headgear - | last run 12 days | form 4 | MARKET 3.8% | 09:00 median 26.00 | Matchbook 26.00
    DATA: model 20.2% | style Unknown | runs in data 1 | last 3: 7 Nov Doncaster Flat 6f Good To Soft 4/6 fig 57
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Wadacre Gabriel (hrs_17391446870) | 2yo C | 133lb | OR - | draw 8 | jockey Rowan Scott | trainer Charlie Johnston (14d 0/5) | headgear - | last run 75 days | form 7 | MARKET 2.2% | 09:00 median 26.00 | Matchbook 90.00
    DATA: model 9.0% | style Unknown | runs in data 1 | last 3: 5 Sep Newcastle Flat 7.1f Standard 7/7
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Lady Mombasa (hrs_17392755835) | 2yo F | 128lb | OR - | draw 1 | jockey Tom Eaves | trainer Ann Duffield (14d 0/1) | headgear - | last run 13 days | form 78 | MARKET 0.5% | 09:00 median 201.00 | Matchbook 220.00
    DATA: model 5.9% | style Held up (led 5% of runs) | runs in data 2 | last 3: 26 Oct Redcar Flat 7f Soft 7/11 fig 20; 6 Nov Newcastle (AW) Flat 7f Standard 8/10 fig 45
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on

## 6:10 Newcastle (AW) | race_id rac_32304845729 | AWC Is Back Handicap Stakes
Flat | Class 4 | 7f14y | going Standard | AW | 14 runners | rating band 0-80 | age 3yo+
DATA pace: Lone leader - Pol Roger is the only habitual front-runner and may be allowed an easy lead.
- Frankies Dream (hrs_42226156) | 4yo G | 137lb | OR 78 | draw 14 | jockey Jason Hart | trainer Jennie Candlish (14d 3/20) | headgear h | last run 40 days | form 788420 | MARKET 22.6% | 09:00 median 3.50 | Matchbook 3.85 | CHECK (skip line 3.32)
    comment: Frankies Dream bounced back with a second two starts ago, but he was unplaced last time and has been winless in his last six, returning after 40 days off.
    DATA: model 12.9% | style Held up (led 4% of runs) | runs in data 11 | last 3: 5 Sep Thirsk Flat 7f Good To Soft 4/9; 25 Sep Newcastle Flat 7.1f Standard 2/11; 10 Oct York Flat 7.9f Soft 12/20
    DATA for: Last-run finishing speed +2.6% vs that field (finished strongly)
- Intrusively (hrs_39191502) | 4yo G | 130lb | OR 71 | draw 5 | jockey Joanna Mason | trainer Michael Appleby (14d 1/14) | headgear tp | last run 12 days | form 975145 | MARKET 12.2% | 09:00 median 6.50 | Matchbook 7.60
    comment: Intrusively has been consistent lately, with a fifth last time out, a fourth two starts back and a win three starts back, and he's fresh from a run 12 days ago.
    DATA: model 7.4% | style Held up (led 4% of runs) | runs in data 12 | last 3: 12 Oct Newcastle Flat 7.1f Standard 1/13; 16 Oct Newcastle (AW) Flat 8f Standard 4/9 fig 65; 7 Nov Doncaster Flat 7f Good To Soft 5/12 fig 74
    DATA for: Has won at this trip or further
    DATA against: Official rating 71, 5 lb below field average
- Nursia (hrs_54712252) | 3yo G | 135lb | OR 77 | draw 7 | jockey Kevin Stott | trainer Kevin Ryan (14d 0/3) | headgear - | last run 35 days | form -15825 | MARKET 10.3% | 09:00 median 7.75 | Matchbook 8.80
    comment: Nursia was only fifth last time out and has been beaten in three of his last four runs bar a second two starts back, so he's hard to fancy after 35 days off. He has run over today's trip and going, and a win five starts back shows he can score.
    DATA: model 8.4% | style Midfield (led 5% of runs) | runs in data 5 | last 3: 24 Jul York Flat 5.4f Good To Firm 8/12; 22 Sep Beverley Flat 7.3f Good 2/9; 15 Oct Southwell (AW) Flat 8f Standard 5/11 fig 77
    DATA for: Best recent form figure 77, 4 lb above field average; Last-run finishing speed +2.0% vs that field (finished strongly)
- Prosperitas (hrs_43508451) | 4yo G | 135lb | OR 76 | draw 13 | jockey Clifford Lee | trainer T. J. Kent (14d 0/2) | headgear p | last run 19 days | form -04490 | MARKET 9.3% | 09:00 median 8.80 | Matchbook 9.60
    comment: The risk is a recent slide, unplaced last time and a ninth two starts back, and he remains winless in his last five.
    DATA: model 7.5% | style Held up (led 3% of runs) | runs in data 5 | last 3: 23 Sep Kempton Flat 7f Standard To Slow 4/13; 24 Oct Doncaster Flat 7f Heavy 9/12 fig 40; 31 Oct Newmarket Flat 7f Good To Soft 11/16 fig 64
    DATA against: Best recent form figure 64, 9 lb below field average; Recent figures 12 lb below its current mark (looks high in the weights)
- Montezin (hrs_57439256) | 4yo G | 138lb | OR 79 | draw 8 | jockey Cam Hardie | trainer Antony Brittain (14d 1/5) | headgear tp | last run 17 days | form 851016 | MARKET 8.0% | 09:00 median 9.00 | Matchbook 12.50
    comment: Montezin brings win-laden recent form, a winner two starts back and again four starts back, before a sixth last time out, and he returns after 17 days having run over today's trip and going.
    DATA: model 8.4% | style Midfield (led 5% of runs) | runs in data 9 | last 3: 5 Sep Haydock Flat 7f Soft 10/11; 8 Oct Southwell Flat 7.1f Standard 1/12; 2 Nov Wolverhampton (AW) Flat 7f Standard 6/7 fig 70
    DATA for: Trainer 20% wins (1/5), last 14 days; Has won at this trip or further
    DATA against: Recent figures 9 lb below its current mark (looks high in the weights)
- Luminare (hrs_52555300) | 3yo F | 134lb | OR 76 | draw 6 | jockey Harry Davies | trainer William Haggas (14d 3/9) | headgear - | last run 64 days | form 232248 | MARKET 7.6% | 09:00 median 9.00 | Matchbook 14.00
    comment: Luminare is winless in her last six, and after an eighth last time out and a 64-day break she is hard to fancy, especially carrying 134 lb from draw six. In her favour, she has run over today's trip and going, and was second three starts back.
    DATA: model 8.4% | style Held up (led 8% of runs) | runs in data 7 | last 3: 17 Jul Newbury Flat 8f Good To Firm 2/10; 3 Sep Southwell Flat 8.1f Standard 4/8; 16 Sep Sandown Flat 8f Good 8/10
    DATA for: Trainer 33% wins (3/9), last 14 days
- We Dare To Dream (hrs_42715820) | 4yo G | 134lb | OR 75 | draw 2 | jockey Conor Whiteley(5) | trainer David O'Meara (14d 0/12) | headgear t | last run 12 days | form 60-883 | MARKET 7.1% | 09:00 median 10.00 | Matchbook 15.00
    comment: Third last time out and only 12 days ago, so he arrives fit and in better heart, though he's yet to win in his last five starts and was eighth in the two runs before that.
    DATA: model 4.2% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 1 Oct Nottingham Flat 8.3f Good 8/9; 17 Oct Catterick Flat 7f Good 8/9 fig 53; 7 Nov Doncaster Flat 7f Good To Soft 3/12 fig 82
    DATA for: Best recent form figure 82, 9 lb above field average; Recent figures 7 lb above its current mark (looks well handicapped)
    DATA against: Trainer 0 wins from 12 runs, last 14 days
- Fifty Nifty (hrs_40941327) | 5yo G | 137lb | OR 78 | draw 3 | jockey Dale Swift | trainer Brian Ellison (14d 1/6) | headgear /es | last run 12 days | form 352856 | MARKET 6.1% | 09:00 median 12.00 | Matchbook 16.00
    comment: Fifty Nifty has been in the frame in two of his last six, including a second four starts back, and he's fresh from a run 12 days ago having already run over today's trip and going.
    DATA: model 6.3% | style Held up (led 8% of runs) | runs in data 11 | last 3: 19 Sep Newmarket Flat 6f Good 8/9; 5 Oct Kempton Flat 6f Standard To Slow 5/9; 7 Nov Doncaster Flat 7f Good To Soft 6/12 fig 76
- Hilltop (hrs_39488323) | 5yo M | 132lb | OR 73 | draw 11 | jockey Aiden Brookes | trainer Iain Jardine (14d 0/4) | headgear - | last run 27 days | form 443427 | MARKET 4.0% | 09:00 median 17.00 | Matchbook 28.00
    comment: Hilltop is consistent but winless in her last six, with a second two starts back and a third four starts back, though she was only seventh last time out.
    DATA: model 10.1% | style Prominent (led 8% of runs) | runs in data 9 | last 3: 11 Sep Chester Flat 7f Good To Soft 4/13; 2 Oct Wolverhampton Flat 7.2f Standard 2/9; 23 Oct Wolverhampton (AW) Flat 7f Standard 7/11 fig 69
    DATA for: Has won at this trip or further
- The Dragon King (hrs_40353418) | 4yo G | 137lb | OR 78 | draw 10 | jockey Edward Greatrex | trainer Robert Cowell (14d 0/6) | headgear p (1st time) | last run 17 days | form 582897 | MARKET 3.5% | 09:00 median 21.00 | Matchbook 29.00
    comment: The risk is a recent slide of seventh, ninth and eighth, and he remains winless in his last six.
    DATA: model 3.6% | style Held up (led 5% of runs) | runs in data 9 | last 3: 9 Jul Newbury Flat 8f Good To Firm 8/12; 5 Oct Wolverhampton Flat 7.2f Standard 9/11; 2 Nov Wolverhampton (AW) Flat 7f Standard 7/7 fig 68
    DATA for: First-time headgear
    DATA against: Best recent form figure 68, 5 lb below field average; Recent figures 10 lb below its current mark (looks high in the weights); Poor recent finishing positions
- The Childe of Hale (hrs_42226324) | 4yo G | 131lb | OR 72 | draw 12 | jockey Tom Eaves | trainer Ivan Furtado (14d 1/5) | headgear p | last run 41 days | form 905129 | MARKET 2.8% | 09:00 median 26.00 | Matchbook 40.00
    comment: Beaten into ninth last time out after a second two starts back and a win three starts back, he looks hard to fancy now, with 41 days off and 131 lb on his back from stall 12.
    DATA: model 11.0% | style Midfield (led 4% of runs) | runs in data 6 | last 3: 9 Sep Redcar Flat 7f Good 1/15; 14 Sep Thirsk Flat 7f Good 2/12; 9 Oct York Flat 7f Good To Soft 9/20
    DATA for: Trainer 20% wins (1/5), last 14 days; Has won at this trip or further; Good recent finishing positions
- Fozzie (hrs_56525448) | 3yo G | 135lb | OR 77 | draw 9 | jockey Andrew Mullen | trainer Iain Jardine (14d 0/4) | headgear p (1st time) | last run 156 days | form 7-2234 | MARKET 2.4% | 09:00 median 26.00 | Matchbook 48.00
    comment: Fozzie has been in the frame in three of his last five, finishing a fourth last time out, a third two starts back and a second three starts back, and he has run over today's trip. Yet to win, he returns after 156 days off and carries 135 lb from stall nine.
    DATA: model 5.8% | style Unknown | runs in data 4 | last 3: 7 May Redcar Flat 8f Good 2/10; 2 Jun Pontefract Flat 10f Good 3/4; 16 Jun Beverley Flat 7.4f Good 4/9
    DATA for: Good recent finishing positions; First-time headgear
    DATA against: Returns from a 156-day break
- King of Fury (hrs_36515619) | 6yo G | 135lb | OR 76 | draw 1 | jockey Sean Kirrane | trainer Michael Dods (14d 0/7) | headgear - | last run 41 days | form 119070 | MARKET 2.2% | 09:00 median 34.00 | Matchbook 50.00
    comment: Two wins in his last six starts, but he's been well beaten since, with a seventh two starts back and a ninth four starts back, and he returns after 41 days off.
    DATA: model 2.6% | style Midfield (led 5% of runs) | runs in data 11 | last 3: 27 Aug Southwell Flat 7.1f Standard 10/11; 22 Sep Southwell Flat 8.1f Standard 7/11; 9 Oct York Flat 7f Good To Soft 17/20
    DATA for: Has won at this trip or further
    DATA against: Poor recent finishing positions
- Pol Roger (hrs_31148579) | 6yo G | 138lb | OR 79 | draw 4 | jockey Rhys Elliott(5) | trainer Michael Dods (14d 0/7) | headgear - | last run 12 days | form 210490 | MARKET 2.0% | 09:00 median 34.00 | Matchbook 70.00
    comment: Pol Roger has been well beaten in his last two, unplaced last time out and a ninth two starts back, though a winner five starts back and a second six starts back show he has ability.
    DATA: model 3.4% | style Leader (led 54% of runs) | runs in data 11 | last 3: 17 Oct Catterick Flat 12f Good 4/7 fig 76; 27 Oct Catterick Flat 12f Soft 9/10; 7 Nov Doncaster Flat 7f Good To Soft 10/12 fig 59
    DATA for: Has won at this trip or further; Pace: may get an uncontested lead

## 6:40 Newcastle (AW) | race_id rac_32304847666 | Midnite Ain't Your Grandad's Bookie Handicap Stakes
Flat | Class 4 | 6f | going Standard | AW | 14 runners | rating band 0-85 | age 3yo+
DATA pace: Lone leader - Hunky Dory is the only habitual front-runner and may be allowed an easy lead.
- Starmade (hrs_56494697) | 3yo G | 135lb | OR 85 | draw 12 | jockey Robert Havlin | trainer Ed Dunlop (14d 1/3) | headgear - | last run 16 days | form 315083 | MARKET 17.6% | 09:00 median 4.50 | Matchbook 5.20 | CHECK (skip line 4.27)
    comment: Starmade comes here fresh from a third last time out just 16 days ago, and he has run over today's trip and on this going before. A winner five starts back, he is a solid each-way profile from stall 12 off 135 lb, with last-but-one's eighth and an unplaced run before that the blemishes.
    DATA: model 11.8% | style Held up (led 4% of runs) | runs in data 6 | last 3: 9 Jul Newmarket Flat 6f Good To Firm 10/13; 28 Aug Thirsk Flat 6f Good 8/18; 3 Nov Wolverhampton (AW) Flat 6f Standard 3/12 fig 87
    DATA for: Best recent form figure 87, 6 lb above field average; Last-run finishing speed +2.2% vs that field (finished strongly); Has won at this trip or further
- We Never Stop (hrs_35336889) | 5yo G | 135lb | OR 85 | draw 10 | jockey Kevin Stott | trainer Kevin Ryan (14d 0/3) | headgear - | last run 61 days | form 002070 | MARKET 15.7% | 09:00 median 5.00 | Matchbook 5.80
    DATA: model 3.7% | style Midfield (led 4% of runs) | runs in data 10 | last 3: 25 Jul York Flat 6f Good To Firm 21/21; 28 Aug Thirsk Flat 6f Good 7/18; 19 Sep Ayr Flat 6f Heavy 22/23
    DATA against: Last-run finishing speed -5.4% vs that field (faded); Poor recent finishing positions
- So Darn Hot (hrs_41442072) | 4yo G | 137lb | OR 87 | draw 8 | jockey Rowan Scott | trainer Kevin Philippart de Foy (14d 1/4) | headgear - | last run 12 days | form 705300 | MARKET 12.3% | 09:00 median 6.50 | Matchbook 7.40
    comment: Fresh after just 12 days, So Darn Hot has run over today's trip and going, and a third three starts back is his best recent effort.
    DATA: model 8.0% | style Midfield (led 3% of runs) | runs in data 8 | last 3: 12 Aug Salisbury Flat 6f Good To Firm 3/7; 26 Sep Haydock Flat 6f Heavy 11/11; 7 Nov Doncaster Flat 6f Good To Soft 12/22 fig 84
- Yes I'm Mali (hrs_39961831) | 4yo G | 135lb | OR 85 | draw 9 | jockey Conor Whiteley(5) | trainer David O'Meara (14d 0/12) | headgear - | last run 28 days | form 521042 | MARKET 9.3% | 09:00 median 8.50 | Matchbook 10.00
    comment: Yes I'm Mali was second last time out and has been in the first five in five of his last six, with a win four starts back, and he has run over today's trip and going before.
    DATA: model 11.2% | style Prominent (led 4% of runs) | runs in data 15 | last 3: 19 Sep Newbury Flat 7f Good To Firm 11/16; 26 Sep Ripon Flat 6f Good 4/12; 22 Oct Newmarket Flat 6f Soft 2/12 fig 85
    DATA for: Has won at this trip or further
    DATA against: Trainer 0 wins from 12 runs, last 14 days
- Milford (hrs_41629602) | 4yo G | 134lb | OR 84 | draw 14 | jockey Hollie Doyle | trainer Julie Camacho (14d 0/6) | headgear v | last run 26 days | form 928205 | MARKET 7.5% | 09:00 median 10.00 | Matchbook 13.00
    comment: The main risk is a winless recent record, with a fifth last time out and 134 lb to carry from stall 14.
    DATA: model 11.6% | style Prominent (led 4% of runs) | runs in data 8 | last 3: 13 Sep Doncaster Flat 6.5f Good 2/13; 18 Sep Ayr Flat 6f Soft 12/24; 24 Oct Doncaster Flat 5f Heavy 5/10 fig 81
- Zain Primus (hrs_55665967) | 3yo C | 135lb | OR 85 | draw 2 | jockey P. J. McDonald | trainer John Butler (14d 0/5) | headgear - | last run 34 days | form 311090 | MARKET 7.1% | 09:00 median 11.00 | Matchbook 13.50
    comment: Zain Primus has finished unplaced last time out and a ninth two starts back, so the two wins four and five starts back look a while ago now, and 135 lb from stall two is a big ask.
    DATA: model 3.5% | style Midfield (led 23% of runs) | runs in data 6 | last 3: 19 Aug York Flat 5f Good 17/19; 26 Sep Haydock Flat 6f Heavy 9/11; 16 Oct Haydock Flat 5f Heavy 14/14
    DATA for: Has won at this trip or further
    DATA against: Poor recent finishing positions
- Lorna B (hrs_46383974) | 4yo F | 134lb | OR 84 | draw 5 | jockey Dale Swift | trainer Brian Ellison (14d 1/6) | headgear - | last run 31 days | form 125-41 | MARKET 6.8% | 09:00 median 11.00 | Matchbook 15.00
    DATA: model 14.9% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 16 May Doncaster Flat 6f Good To Soft 4/12; 19 Oct Wolverhampton (AW) Flat 7f Standard 1/12 fig 86
    DATA for: Best recent form figure 86, 4 lb above field average; Has won at this trip or further
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Wicket Keeper (hrs_40919130) | 4yo G | 132lb | OR 82 | draw 4 | jockey Cam Hardie | trainer Antony Brittain (14d 1/5) | headgear - | last run 35 days | form -46004 | MARKET 5.2% | 09:00 median 15.00 | Matchbook 18.00
    DATA: model 3.1% | style Unknown | runs in data 5 | last 3: 13 May York Flat 6f Good 21/22; 19 Sep Ayr Flat 6f Heavy 23/23; 15 Oct Southwell (AW) Flat 6f Standard 4/9 fig 82
    DATA for: Trainer 20% wins (1/5), last 14 days
- Percy's Star (hrs_63586306) | 3yo G | 126lb | OR 76 | draw 1 | jockey Harry Davies | trainer Chris Dwyer (14d 0/2) | headgear p | last run 57 days | form 416621 | MARKET 4.8% | 09:00 median 13.00 | Matchbook 25.00
    comment: He has run over today's trip and going, and carries 126 lb from stall one.
    DATA: model 6.2% | style Prominent (led 23% of runs) | runs in data 8 | last 3: 18 Aug Wolverhampton Flat 6.1f Standard 6/8; 15 Sep Yarmouth Flat 7f Good To Soft 2/9; 23 Sep Goodwood Flat 6f Good 1/15
    DATA for: Last-run finishing speed +2.1% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions; Carries 6 lb less than average
    DATA against: Official rating 76, 6 lb below field average
- Beale Street (hrs_37475389) | 5yo G | 131lb | OR 81 | draw 11 | jockey Oisin McSweeney | trainer Bryan Smart (14d 1/4) | headgear - | last run 26 days | form 010217 | MARKET 3.6% | 09:00 median 21.00 | Matchbook 27.00
    comment: Beale Street won two starts back and five starts back, but he was seventh last time out and returns after 26 days.
    DATA: model 9.0% | style Held up (led 8% of runs) | runs in data 9 | last 3: 14 Jun Doncaster Flat 7f Good 2/11; 26 Jun Doncaster Flat 7f Good To Firm 1/7; 24 Oct Doncaster Flat 7f Heavy 7/13 fig 71
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Best recent form figure 71, 10 lb below field average; Recent figures 10 lb below its current mark (looks high in the weights)
- Sixtygeesbaby (hrs_43667197) | 4yo G | 131lb | OR 81 | draw 7 | jockey Mark Winn | trainer David O'Meara (14d 0/12) | headgear tv | last run 19 days | form 513034 | MARKET 3.5% | 09:00 median 23.00 | Matchbook 27.00
    comment: Fourth last time out and third two starts back, Sixtygeesbaby is knocking on the door and is fresh enough after 19 days, with experience over today's trip.
    DATA: model 6.3% | style Held up (led 8% of runs) | runs in data 12 | last 3: 13 Sep Doncaster Flat 6f Good 16/16; 15 Sep Redcar Flat 6f Good 3/14; 31 Oct Newmarket Flat 6f Good To Soft 4/10 fig 83
    DATA for: Has won at this trip or further
    DATA against: Trainer 0 wins from 12 runs, last 14 days
- Hunky Dory (hrs_43951005) | 4yo G | 132lb | OR 82 | draw 3 | jockey Tom Kiely-Marshall(3) | trainer Linda Perratt (14d 0/3) | headgear p | last run 15 days | form 361063 | MARKET 3.3% | 09:00 median 23.00 | Matchbook 30.00
    comment: Third last time out and fresh enough after 15 days, Hunky Dory has run over today's trip and going and won four starts back, though he's only one win in his last six and was a sixth two starts back.
    DATA: model 3.4% | style Leader (led 29% of runs) | runs in data 11 | last 3: 18 Sep Ayr Flat 6f Soft 24/24; 15 Oct Southwell (AW) Flat 6f Standard 6/9 fig 77; 4 Nov Musselburgh Flat 7f Soft 3/12 fig 81
    DATA for: Has won at this trip or further; Pace: may get an uncontested lead; Course: front-runners have won 1.3× their fair share at 6f here
- Itsatenfromlen (hrs_41939919) | 4yo G | 129lb | OR 79 | draw 6 | jockey Jason Hart | trainer Ivan Furtado (14d 1/5) | headgear t | last run 26 days | form 19-050 | MARKET 1.6% | 09:00 median 38.50 | Matchbook 85.00
    comment: Itsatenfromlen has been out of sorts since a win five starts back, with a fifth two starts back the best of his recent efforts, though he has run over today's trip and comes here fresh after 26 days off.
    DATA: model 3.3% | style Unknown | runs in data 2 | last 3: 1 Oct Nottingham Flat 8.3f Good 5/9; 24 Oct Doncaster Flat 7f Heavy 11/12
    DATA for: Trainer 20% wins (1/5), last 14 days
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Waistcoat (hrs_37246566) | 5yo G | 128lb | OR 78 | draw 13 | jockey William Carver | trainer Ross Burdon (14d 1/1) | headgear t | last run 36 days | form 901657 | MARKET 1.6% | 09:00 median 38.50 | Matchbook 80.00
    comment: Waistcoat has finished seventh, fifth and sixth in his last three runs, and his win came four starts back, so the form is drifting the wrong way after 36 days off.
    DATA: model 4.1% | style Held up (led 3% of runs) | runs in data 7 | last 3: 17 Aug Windsor Flat 6.1f Good To Firm 6/8; 19 Sep Newmarket Flat 6f Good 5/9; 14 Oct Kempton (AW) Flat 7f Standard / Slow 7/12 fig 75
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 75, 6 lb below field average

## 7:10 Newcastle (AW) | race_id rac_32305287365 | AWC Season 14 Has Begun Handicap Stakes
Flat | Class 6 | 7f14y | going Standard | AW | 14 runners | rating band 0-60 | age 3yo
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Liquid Cooled (hrs_58469243) | 3yo G | 124lb | OR 49 | draw 3 | jockey Andrew Mullen | trainer Ben Haslam (14d 2/5) | headgear - | last run 20 days | form 356307 | MARKET 16.6% | 09:00 median 4.33 | Matchbook 5.70 | CHECK (skip line 4.11)
    comment: Liquid Cooled was seventh last time out, though he has been third three starts back and third six starts back, and has run over today's trip and going before.
    DATA: model 4.5% | style Held up (led 4% of runs) | runs in data 8 | last 3: 3 Sep Newcastle Flat 6f Standard 3/7; 20 Oct Newcastle (AW) Flat 5f Standard 10/10 fig 33; 30 Oct Newcastle (AW) Flat 6f Standard 7/9 fig 43
    DATA for: Trainer 40% wins (2/5), last 14 days
    DATA against: Best recent form figure 43, 5 lb below field average; Recent figures 6 lb below its current mark (looks high in the weights); Pace: steady gallop likely, hard to come from off the pace
- Real Jack (hrs_52054555) | 3yo G | 134lb | OR 59 | draw 8 | jockey Sean Kirrane | trainer Michael Dods (14d 0/7) | headgear - | last run 38 days | form 677242 | MARKET 16.2% | 09:00 median 4.50 | Matchbook 5.70
    comment: The risk is that he is yet to win in his last six starts, and 134 lb from draw 8 is a hefty burden after 38 days off.
    DATA: model 20.0% | style Prominent (led 4% of runs) | runs in data 8 | last 3: 8 Sep Catterick Flat 7f Good To Soft 2/12; 14 Sep Thirsk Flat 7f Good 4/10; 12 Oct Musselburgh Flat 7.1f Good To Soft 2/11
    DATA for: Official rating 59, 8 lb above field average; Good recent finishing positions
    DATA against: Carries 7 lb more than average
- Saxon Prince (hrs_57471113) | 3yo G | 130lb | OR 55 | draw 13 | jockey Jason Hart | trainer John & Sean Quinn (14d 1/7) | headgear tb (1st time) | last run 34 days | form 609640 | MARKET 12.4% | 09:00 median 6.50 | Matchbook 7.20
    comment: The concern is a winless run in his last six, with a fourth two starts back his best finish.
    DATA: model 10.2% | style Held up (led 3% of runs) | runs in data 8 | last 3: 17 Sep Ayr Flat 7.2f Soft 6/14; 8 Oct Ayr Flat 7.2f Heavy 4/10; 16 Oct Redcar Flat 7f Good 12/18 fig 47
    DATA for: First-time headgear
    DATA against: Recent figures 8 lb below its current mark (looks high in the weights); Pace: steady gallop likely, hard to come from off the pace
- Archangel Josepi (hrs_56559181) | 3yo G | 132lb | OR 57 | draw 7 | jockey Sam James | trainer Katie Scott (14d 0/3) | headgear - | last run 13 days | form 327526 | MARKET 11.8% | 09:00 median 6.50 | Matchbook 7.80
    comment: Archangel Josepi is yet to win in his last six, though two seconds, a third and a sixth last time out show he's consistent enough, and he's fit after 13 days off, having run over today's trip and going.
    DATA: model 13.9% | style Prominent (led 5% of runs) | runs in data 8 | last 3: 12 Oct Musselburgh Flat 7.1f Good To Soft 5/11; 31 Oct Southwell (AW) Flat 8f Standard 2/12 fig 59; 6 Nov Newcastle (AW) Flat 8f Standard 6/14 fig 50
    DATA for: Best recent form figure 59, 11 lb above field average; Official rating 57, 6 lb above field average
- Forever Twenty (hrs_61521663) | 3yo F | 121lb | OR 46 | draw 2 | jockey Hollie Doyle | trainer Ivan Furtado (14d 1/5) | headgear t | last run 48 days | form 039463 | MARKET 10.4% | 09:00 median 7.00 | Matchbook 9.20
    comment: Forever Twenty arrives on a good note after a third last time out, and she has run over today's trip and going, but she is winless in her last six and returns after 48 days off.
    DATA: model 5.1% | style Midfield (led 8% of runs) | runs in data 12 | last 3: 3 Sep Newcastle Flat 7.1f Standard 4/12; 16 Sep Beverley Flat 8.5f Good 6/10; 2 Oct Newcastle Flat 7.1f Standard 3/12
    DATA for: Trainer 20% wins (1/5), last 14 days; Last-run finishing speed +3.3% vs that field (finished strongly); Carries 6 lb less than average
- Masai Angel (hrs_53743501) | 3yo G | 128lb | OR 53 | draw 1 | jockey Billy Garritty | trainer Richard & Peter Fahey (14d 1/11) | headgear h (1st time) | last run 12 days | form 005735 | MARKET 9.6% | 09:00 median 8.00 | Matchbook 9.60
    comment: Masai Angel is yet to win in his last six, though a fifth last time out and a third two starts back show he's competitive, and he's fresh enough off a 12-day break having run over today's trip and going. Carrying 128 lb from stall one, he'd need to step up again to trouble the principals.
    DATA: model 9.3% | style Midfield (led 23% of runs) | runs in data 9 | last 3: 16 Oct Newcastle (AW) Flat 5f Standard 7/10 fig 45; 27 Oct Wolverhampton (AW) Flat 6f Standard 3/12 fig 55; 7 Nov Southwell (AW) Flat 6f Standard 5/11 fig 50
    DATA for: Best recent form figure 55, 7 lb above field average; First-time headgear
- Irish Incentive (hrs_58380231) | 3yo F | 135lb | OR 60 | draw 4 | jockey M. P. Sheehy | trainer Adrian Keatley (14d 0/4) | headgear t (1st time) | last run 40 days | form 256038 | MARKET 4.9% | 09:00 median 15.00 | Matchbook 19.50
    comment: Last-time eighth and no win in her last six are the only blemishes.
    DATA: model 10.2% | style Midfield (led 3% of runs) | runs in data 7 | last 3: 16 May Doncaster Flat 8f Good To Soft 12/14; 23 Sep Redcar Flat 7f Good 3/12; 10 Oct Southwell Flat 6.1f Standard 8/9
    DATA for: Official rating 60, 9 lb above field average; First-time headgear
    DATA against: Carries 8 lb more than average
- Yesnia (hrs_58165212) | 3yo F | 121lb | OR 45 | draw 5 | jockey Zak Wheatley | trainer Declan Carroll (14d 0/4) | headgear t | last run 24 days | form 0-7784 | MARKET 4.4% | 09:00 median 17.00 | Matchbook 22.00
    comment: Yesnia is winless in her last five, with a seventh and an eighth before a fourth last time out, so she is hard to fancy at this level.
    DATA: model 4.4% | style Midfield (led 4% of runs) | runs in data 4 | last 3: 1 Jun Wolverhampton Flat 5.1f Standard 7/11; 11 Jun Nottingham Flat 6.1f Soft 8/9; 26 Oct Southwell (AW) Flat 7f Standard 4/11 fig 46
    DATA for: Carries 6 lb less than average
    DATA against: Official rating 45, 6 lb below field average
- Twilight Dawn (hrs_53871321) | 3yo F | 121lb | OR 45 | draw 14 | jockey Joanna Mason | trainer Simon Whitaker (14d 0/4) | headgear - | last run 24 days | form 533005 | MARKET 3.3% | 09:00 median 23.00 | Matchbook 28.00
    comment: Winless in her last six, Twilight Dawn was a fifth last time out, 24 days ago, after two unplaced runs, and she looks hard to fancy at 121 lb from stall 14.
    DATA: model 3.3% | style Midfield (led 3% of runs) | runs in data 6 | last 3: 25 Jul Newcastle Flat 7.1f Standard To Slow 11/13; 26 Aug Catterick Flat 7f Good 10/13; 26 Oct Southwell (AW) Flat 7f Standard 5/11 fig 43
    DATA for: Last-run finishing speed +2.5% vs that field (finished strongly); Carries 6 lb less than average
    DATA against: Best recent form figure 43, 5 lb below field average; Official rating 45, 6 lb below field average
- Uncertainty (hrs_50434769) | 3yo F | 132lb | OR 57 | draw 9 | jockey Barry McHugh | trainer Simon Whitaker (14d 0/4) | headgear - | last run 12 days | form 057150 | MARKET 2.8% | 09:00 median 26.00 | Matchbook 42.00
    DATA: model 7.6% | style Midfield (led 3% of runs) | runs in data 11 | last 3: 16 Oct Redcar Flat 7f Good 1/18 fig 72; 26 Oct Redcar Flat 7f Heavy 5/12 fig 55; 7 Nov Southwell (AW) Flat 7f Standard 11/12 fig 40
    DATA for: Best recent form figure 72, 24 lb above field average; Recent figures 15 lb above its current mark (looks well handicapped); Official rating 57, 6 lb above field average; Has won at this trip or further
- Container Express (hrs_56188860) | 3yo G | 121lb | OR 45 | draw 10 | jockey Aiden Brookes | trainer Philip Kirby (14d 1/13) | headgear - | last run 23 days | form 553459 | MARKET 2.2% | 09:00 median 34.00 | Matchbook 55.00
    comment: Container Express is winless in his last six and was beaten into ninth last time out, so he is hard to fancy, though a third four starts back and a fourth three starts back show some consistency.
    DATA: model 3.5% | style Midfield (led 4% of runs) | runs in data 6 | last 3: 11 Mar Newcastle Flat 6f Standard 4/10; 19 Mar Newcastle Flat 7.1f Standard 5/10; 27 Oct Catterick Flat 6f Soft 9/10 fig 16
    DATA for: Carries 6 lb less than average
    DATA against: Best recent form figure 16, 32 lb below field average; Recent figures 29 lb below its current mark (looks high in the weights); Official rating 45, 6 lb below field average
- Danrana (hrs_54965519) | 3yo F | 131lb | OR 56 | draw 11 | jockey Oisin McSweeney | trainer Fionn McSharry (14d 0/0) | headgear - | last run 56 days | form 8-0580 | MARKET 2.2% | 09:00 median 34.00 | Matchbook 48.00
    comment: Danrana is winless in her last five, with an eighth and a fifth in the middle of that run, and she returns after 56 days off.
    DATA: model 4.8% | style Midfield (led 4% of runs) | runs in data 4 | last 3: 1 Aug Doncaster Flat 7f Good To Firm 5/11; 19 Aug Carlisle Flat 6.9f Soft 8/9; 24 Sep Southwell Flat 8.1f Standard 12/13
    DATA for: Official rating 56, 5 lb above field average
- Scheffler (hrs_62908503) | 3yo G | 128lb | OR 53 | draw 6 | jockey Tom Eaves | trainer Adrian Nicholls (14d 0/1) | headgear b | last run 42 days | form 904730 | MARKET 1.8% | 09:00 median 34.00 | Matchbook 75.00
    comment: Scheffler was unplaced last time out after a third two starts back, and he has run over today's trip and going, though he's winless in his last six and returns after 42 days off.
    DATA: model 2.7% | style Prominent (led 3% of runs) | runs in data 8 | last 3: 3 Aug Ripon Flat 8f Good 7/7; 2 Sep Hamilton Flat 8.3f Soft 3/10; 8 Oct Ayr Flat 8f Heavy 13/13
    DATA against: Last-run finishing speed -7.6% vs that field (faded)
- Midnight Serenade (hrs_65451477) | 3yo F | 121lb | OR 32 | draw 12 | jockey Finlay Bassett(7) | trainer R. Mike Smith (14d 0/7) | headgear h | last run 13 days | form 587 | MARKET 1.5% | 09:00 median 67.00 | Matchbook 80.00
    comment: Midnight Serenade is winless in her last three, finishing seventh last time out, then an eighth and a fifth, so she is hard to fancy.
    DATA: model 0.4% | style Midfield (led 5% of runs) | runs in data 3 | last 3: 1 Aug Hamilton Flat 11.1f Good 5/5; 11 Aug Hamilton Flat 8.3f Good 8/8; 6 Nov Newcastle (AW) Flat 10f Standard 7/7
    DATA for: Carries 6 lb less than average
    DATA against: Official rating 32, 19 lb below field average; Last-run finishing speed -5.8% vs that field (faded)

## 7:40 Newcastle (AW) | race_id rac_32304849603 | Midnite: Built For 2026 Not 2006 Handicap Stakes
Flat | Class 4 | 5f | going Standard | AW | 14 runners | rating band 0-80 | age 3yo+
DATA pace: Even - Two likely leaders (Come On Over, Tees Spirit). A fair, even gallop is most likely.
- Paddy's Day (hrs_29227226) | 6yo G | 134lb | OR 79 | draw 6 | jockey Ethan Tindall(5) | trainer Nigel Tinkler (14d 1/1) | headgear tp (1st time) | last run 20 days | form 396635 | MARKET 18.1% | 09:00 median 4.33 | Matchbook 4.90 | CHECK (skip line 4.11)
    comment: The risk is he's yet to win in his last six starts.
    DATA: model 9.0% | style Prominent (led 4% of runs) | runs in data 13 | last 3: 26 Sep Southwell Flat 5f Standard 6/10; 16 Oct Newcastle (AW) Flat 5f Standard 3/11 fig 79; 30 Oct Newcastle (AW) Flat 5f Standard 5/12 fig 83
    DATA for: Best recent form figure 83, 13 lb above field average; Recent figures 4 lb above its current mark (looks well handicapped); First-time headgear
- Kinetic Force (hrs_41938694) | 4yo G | 135lb | OR 80 | draw 12 | jockey Joanna Mason | trainer Ruth Carr (14d 1/7) | headgear - | last run 12 days | form 773243 | MARKET 12.4% | 09:00 median 6.00 | Matchbook 7.60
    comment: Kinetic Force arrives fit after just 12 days, having finished third last time out, a fourth two starts back and a second three starts back, and he has run over today's trip and going before. The risk is that he is yet to win in his last six, carrying 135 lb from stall 12.
    DATA: model 15.0% | style Midfield (led 3% of runs) | runs in data 10 | last 3: 16 Oct Newcastle (AW) Flat 5f Standard 2/11 fig 81; 20 Oct Yarmouth Flat 5f Soft 4/8 fig 72; 7 Nov Southwell (AW) Flat 5f Standard 3/14 fig 83
    DATA for: Best recent form figure 83, 13 lb above field average; Has won at this trip or further; Good recent finishing positions
- Oriental Prince (hrs_40205844) | 5yo G | 128lb | OR 73 | draw 13 | jockey Lauren Young(5) | trainer Jim Goldie (14d 0/7) | headgear - | last run 27 days | form 826149 | MARKET 10.8% | 09:00 median 7.00 | Matchbook 8.40
    comment: Oriental Prince was beaten into ninth last time out and has only one win in his last six, a victory three starts back, so he is hard to fancy.
    DATA: model 7.4% | style Midfield (led 5% of runs) | runs in data 12 | last 3: 6 Sep York Flat 5.4f Good To Soft 1/21; 17 Sep Ayr Flat 5f Soft 4/20; 23 Oct Doncaster Flat 6f Heavy 9/11 fig 51
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 51, 19 lb below field average; Recent figures 22 lb below its current mark (looks high in the weights)
- Changeofmind (hrs_30765112) | 6yo G | 131lb | OR 76 | draw 1 | jockey David Nolan | trainer Declan Carroll (14d 0/4) | headgear - | last run 12 days | form 230754 | MARKET 9.8% | 09:00 median 7.50 | Matchbook 9.60
    DATA: model 7.0% | style Midfield (led 3% of runs) | runs in data 11 | last 3: 28 Sep Hamilton Flat 5f Soft 7/9; 19 Oct Pontefract Flat 5f Heavy 5/9 fig 78; 7 Nov Southwell (AW) Flat 5f Standard 4/14 fig 78
    DATA for: Best recent form figure 78, 8 lb above field average; Has won at this trip or further
- Duran (hrs_35624890) | 5yo G | 127lb | OR 72 | draw 7 | jockey Alex Jary(3) | trainer Nigel Tinkler (14d 1/1) | headgear t | last run 13 days | form 078451 | MARKET 8.4% | 09:00 median 9.00 | Matchbook 11.50
    comment: The risk is a patchy record before that, with a fifth two starts back and a fourth three starts back his best efforts in that spell.
    DATA: model 10.3% | style Prominent (led 5% of runs) | runs in data 9 | last 3: 16 Oct Haydock Flat 5f Heavy 4/14 fig 87; 28 Oct Nottingham Flat 5f Soft 5/9 fig 65; 6 Nov Newcastle (AW) Flat 5f Standard 1/14 fig 75
    DATA for: Best recent form figure 87, 17 lb above field average; Recent figures 15 lb above its current mark (looks well handicapped); Has won at this trip or further
- South Shore (hrs_35321048) | 5yo G | 129lb | OR 74 | draw 10 | jockey Edward Greatrex | trainer Robert Cowell (14d 0/6) | headgear - | last run 12 days | form 221295 | MARKET 7.4% | 09:00 median 10.00 | Matchbook 13.00
    comment: South Shore was fifth last time out after a ninth two starts back, so the recent trend is soft, though he did win four starts back and has run over today's trip and going.
    DATA: model 7.9% | style Prominent (led 4% of runs) | runs in data 13 | last 3: 29 Sep Bath Flat 5f Good To Firm 2/12; 16 Oct Haydock Flat 5f Heavy 9/14 fig 70; 7 Nov Southwell (AW) Flat 5f Standard 5/14 fig 75
    DATA for: Best recent form figure 75, 5 lb above field average; Has won at this trip or further
- Come On Over (hrs_53294451) | 3yo G | 131lb | OR 76 | draw 11 | jockey Mark Winn | trainer David O'Meara (14d 0/12) | headgear v | last run 28 days | form 122226 | MARKET 7.2% | 09:00 median 10.00 | Matchbook 14.00
    comment: Four seconds on the spin before a sixth last time out show he's consistently in the mix, and he's run over today's trip and going, but he's only won once in his last six and carries 131 lb from stall 11.
    DATA: model 9.7% | style Leader (led 38% of runs) | runs in data 14 | last 3: 18 Sep Wolverhampton Flat 6.1f Standard 2/10; 26 Sep Southwell Flat 6.1f Standard 2/13; 22 Oct Southwell (AW) Flat 6f Standard 6/9 fig 73
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Trainer 0 wins from 12 runs, last 14 days
- Kirkdale (hrs_43418060) | 4yo G | 134lb | OR 79 | draw 14 | jockey Jack Callan | trainer Edward Bethell (14d 0/5) | headgear b | last run 28 days | form 411207 | MARKET 6.5% | 09:00 median 12.00 | Matchbook 14.00
    comment: Kirkdale won four and five starts back and was second three runs ago, but he has faded since, unplaced and then seventh last time out. He has run over today's trip and going, and a 28-day break gives a fresh look, though 134 lb from draw 14 and a 79 mark leave plenty to prove.
    DATA: model 8.6% | style Held up (led 3% of runs) | runs in data 6 | last 3: 3 Sep Southwell Flat 6.1f Standard 2/12; 19 Sep Chester Flat 6.1f Heavy 10/10; 22 Oct Southwell (AW) Flat 6f Standard 7/9 fig 74
    DATA for: Best recent form figure 74, 4 lb above field average; Has won at this trip or further
- Curious Rover (hrs_36555512) | 5yo G | 127lb | OR 72 | draw 2 | jockey Hollie Doyle | trainer Katie Scott (14d 0/3) | headgear - | last run 14 days | form 140053 | MARKET 5.2% | 09:00 median 11.50 | Matchbook 24.00
    comment: Third last time out and fresh from just 14 days ago, he has run over today's trip and going, but he has won only once in his last six, back six starts ago, and a run of fifth and two unplaced efforts before that makes him hard to fancy.
    DATA: model 4.9% | style Prominent (led 29% of runs) | runs in data 11 | last 3: 3 Oct Redcar Flat 5f Good 10/13; 16 Oct Newcastle (AW) Flat 5f Standard 5/11 fig 71; 5 Nov Southwell (AW) Flat 6f Standard 3/9 fig 75
    DATA for: Best recent form figure 75, 5 lb above field average; Has won at this trip or further
- Rock of England (hrs_30455362) | 6yo G | 133lb | OR 78 | draw 9 | jockey Kevin Stott | trainer Paul Midgley (14d 0/5) | headgear - | last run 20 days | form 441320 | MARKET 4.8% | 09:00 median 15.00 | Matchbook 20.00
    comment: Rock of England bids to bounce back from an unplaced latest run, having been second two starts back and third three back, and he has run over today's trip and going.
    DATA: model 7.9% | style Prominent (led 3% of runs) | runs in data 12 | last 3: 13 Sep Doncaster Flat 5f Good 3/10; 19 Oct Pontefract Flat 5f Heavy 2/9 fig 87; 30 Oct Newmarket Flat 5f Good To Soft 10/13 fig 71
    DATA for: Best recent form figure 87, 17 lb above field average; Recent figures 9 lb above its current mark (looks well handicapped); Has won at this trip or further; Good recent finishing positions
- Master of My Fate (hrs_35840875) | 5yo G | 132lb | OR 77 | draw 3 | jockey Jason Hart | trainer John & Sean Quinn (14d 1/7) | headgear - | last run 12 days | form 507800 | MARKET 3.0% | 09:00 median 23.00 | Matchbook 36.00
    comment: Master of My Fate has been unplaced last time out and two runs back, with an eighth three starts back, so he is winless in his last six, though he is fresh from a 12-day break and has run over today's trip and going.
    DATA: model 2.8% | style Midfield (led 5% of runs) | runs in data 13 | last 3: 3 Jul Beverley Flat 5f Good To Firm 8/8; 25 Jul Chester Flat 5.1f Good 11/11; 7 Nov Southwell (AW) Flat 5f Standard 13/14 fig 64
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 64, 6 lb below field average; Recent figures 13 lb below its current mark (looks high in the weights); Poor recent finishing positions
- Blinky (hrs_41152986) | 4yo G | 131lb | OR 76 | draw 8 | jockey Cam Hardie | trainer Antony Brittain (14d 1/5) | headgear p | last run 111 days | form 800440 | MARKET 2.9% | 09:00 median 26.00 | Matchbook 38.00
    comment: Blinky has been winless in his last six, though back-to-back fourths two and three starts back show he can get involved, and he has run over today's trip and going.
    DATA: model 4.8% | style Held up (led 4% of runs) | runs in data 6 | last 3: 13 Jun Chester Flat 5.1f Good To Soft 4/10; 5 Jul Southwell Flat 5f Standard 4/9; 31 Jul Wolverhampton Flat 6.1f Standard 10/10
    DATA for: Trainer 20% wins (1/5), last 14 days
    DATA against: Returns from a 111-day break
- Our Absent Friends (hrs_20977796) | 8yo G | 128lb | OR 73 | draw 4 | jockey Rowan Scott | trainer Tristan Davidson (14d 1/5) | headgear t | last run 34 days | form 533920 | MARKET 2.6% | 09:00 median 29.00 | Matchbook 42.00
    comment: Unplaced last time out and winless in his last six, this gelding is hard to fancy, though a second two starts back and a pair of thirds earlier show he can get involved, and he has run over today's trip and going.
    DATA: model 3.2% | style Prominent (led 23% of runs) | runs in data 19 | last 3: 26 Sep Ripon Flat 5f Good 9/14; 3 Oct Redcar Flat 5f Good 2/13; 16 Oct Haydock Flat 5f Heavy 14/14 fig 17
    DATA for: Trainer 20% wins (1/5), last 14 days; Has won at this trip or further
    DATA against: Best recent form figure 17, 53 lb below field average; Recent figures 56 lb below its current mark (looks high in the weights); Aged 8, older than most of this field
- Tees Spirit (hrs_22372525) | 8yo G | 127lb | OR 72 | draw 5 | jockey Tom Eaves | trainer Adrian Nicholls (14d 0/1) | headgear - | last run 12 days | form 00-900 | MARKET 1.1% | 09:00 median 69.00 | Matchbook 180.00
    comment: Winless in his last five and unplaced last time out, Tees Spirit has little form to lean on, though he's fresh enough after 12 days and has run over today's trip and going.
    DATA: model 1.7% | style Leader (led 57% of runs) | runs in data 3 | last 3: 26 Sep Southwell Flat 5f Standard 9/10; 3 Oct Redcar Flat 5f Good 13/13; 7 Nov Southwell (AW) Flat 5f Standard 10/14 fig 62
    DATA against: Best recent form figure 62, 8 lb below field average; Recent figures 10 lb below its current mark (looks high in the weights); Poor recent finishing positions; Aged 8, older than most of this field
