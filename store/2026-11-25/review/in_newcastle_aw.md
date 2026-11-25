# Card review packet: Newcastle (AW), 2026-11-25

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


## 2:25 Newcastle (AW) | race_id rac_32305519805 | Midnite A Next Generation Betting App Handicap Stakes (GBBPlus Race)
Flat | Class 4 | 1m2f42y | going Standard | AW | 12 runners | rating band 0-85 | age 3yo+
DATA pace: Lone leader - Wadacre Icon is the only habitual front-runner and may be allowed an easy lead.
- Always Happy (hrs_62394339) | 3yo F | 140lb | OR 87 | draw 6 | jockey Sean Dylan Bowen | trainer Roger Varian (14d 5/8) | headgear - | last run 39 days | form 1222 | MARKET 19.7% | 09:00 median 4.00 | Matchbook 4.70 | CHECK (skip line 3.80)
    comment: Always Happy has finished second in each of her last three starts, following a win four starts back, and she has run on today's going before.
    DATA: model 22.6% | style Prominent (led 29% of runs) | runs in data 4 | last 3: 12 May Lingfield Flat 8f Standard 2/12; 29 May Wolverhampton Flat 8.6f Standard 2/6; 17 Oct Southwell (AW) Flat 8f Standard 2/8 fig 87
    DATA for: Best recent form figure 87, 16 lb above field average; Official rating 87, 11 lb above field average; Trainer 62% wins (5/8), last 14 days; Good recent finishing positions
    DATA against: Carries 9 lb more than average
- Arbaawy (hrs_55454063) | 3yo C | 129lb | OR 76 | draw 8 | jockey David Egan | trainer John Butler (14d 2/12) | headgear p | last run 21 days | form 036225 | MARKET 16.0% | 09:00 median 5.00 | Matchbook 5.70
    comment: The risk is that he's yet to win in his last six starts and carries 129 lb from draw 8.
    DATA: model 10.7% | style Held up (led 3% of runs) | runs in data 10 | last 3: 1 Oct Salisbury Flat 9.9f Soft 2/12; 22 Oct Newmarket Flat 10f Soft 2/9 fig 81; 4 Nov Nottingham Flat 10f Soft 5/9 fig 74
    DATA for: Best recent form figure 81, 10 lb above field average; Recent figures 5 lb above its current mark (looks well handicapped); Good recent finishing positions
- Per Contra (hrs_35991977) | 5yo G | 137lb | OR 81 | draw 5 | jockey Sean Kirrane | trainer Tim Easterby (14d 2/12) | headgear p | last run 19 days | form 313829 | MARKET 13.5% | 09:00 median 6.00 | Matchbook 6.80
    DATA: model 9.6% | style Held up (led 3% of runs) | runs in data 15 | last 3: 10 Oct York Flat 10.3f Good To Soft 8/19; 19 Oct Pontefract Flat 10f Heavy 2/9 fig 89; 6 Nov Newcastle (AW) Flat 10f Standard 9/14 fig 77
    DATA for: Best recent form figure 89, 18 lb above field average; Recent figures 8 lb above its current mark (looks well handicapped); Last-run finishing speed +2.3% vs that field (finished strongly); Has won at this trip or further
    DATA against: Carries 6 lb more than average
- Tropical Sands (hrs_64072309) | 3yo F | 129lb | OR 76 | draw 3 | jockey Kieran Shoemark | trainer Ed Walker (14d 1/15) | headgear - | last run 26 days | form 43253 | MARKET 13.5% | 09:00 median 6.00 | Matchbook 6.80
    comment: Tropical Sands is winless in her last five, though she was third last time out and has finished in the first three in two of her other recent runs, so she's consistent without landing a blow.
    DATA: model 7.1% | style Prominent (led 5% of runs) | runs in data 5 | last 3: 7 Aug Haydock Flat 10.2f Good 2/3; 29 Aug Goodwood Flat 9.9f Soft 5/8; 30 Oct Newmarket Flat 10f Good To Soft 3/6 fig 71
    DATA for: Last-run finishing speed +2.6% vs that field (finished strongly); Good recent finishing positions
- Borjina (hrs_57103368) | 3yo F | 126lb | OR 73 | draw 10 | jockey Oisin Orr | trainer Edward Bethell (14d 0/9) | headgear - | last run 21 days | form 253424 | MARKET 11.9% | 09:00 median 7.00 | Matchbook 7.60
    comment: Borjina is consistent, with a second two starts back and a third four starts back among her recent finishes, and she returns after 21 days having run over today's trip and going before.
    DATA: model 8.6% | style Prominent (led 8% of runs) | runs in data 8 | last 3: 23 Sep Redcar Flat 10f Good 4/12; 7 Oct Nottingham Flat 10.2f Good To Soft 2/13; 4 Nov Nottingham Flat 10f Soft 4/9 fig 72
    DATA for: Carries 5 lb less than average
    DATA against: Trainer 0 wins from 9 runs, last 14 days
- Wadacre Icon (hrs_17391999660) | 3yo G | 129lb | OR 76 | draw 12 | jockey Jason Hart | trainer Charlie Johnston (14d 0/10) | headgear - | last run 30 days | form 245 | MARKET 7.5% | 09:00 median 11.00 | Matchbook 12.50
    comment: Wadacre Icon is winless in his last three, fading from a second three starts back to a fourth, then a fifth last time out, and he has run over today's trip.
    DATA: model 11.0% | style Leader (led 38% of runs) | runs in data 3 | last 3: 9 Sep Carlisle Flat 11.2f Good 2/12; 26 Sep Ripon Flat 12f Good 4/9; 26 Oct Redcar Flat 10f Heavy 5/10 fig 44
    DATA for: Pace: may get an uncontested lead
    DATA against: Best recent form figure 44, 27 lb below field average; Recent figures 32 lb below its current mark (looks high in the weights); Trainer 0 wins from 10 runs, last 14 days
- Geo (hrs_42520975) | 4yo F | 125lb | OR 69 | draw 7 | jockey Lauren Young(5) | trainer Jim Goldie (14d 1/14) | headgear - | last run 33 days | form 346130 | MARKET 6.1% | 09:00 median 12.00 | Matchbook 16.50
    DATA: model 4.9% | style Prominent (led 8% of runs) | runs in data 15 | last 3: 17 Sep Ayr Flat 10f Soft 1/7; 28 Sep Hamilton Flat 8.3f Soft 3/13; 23 Oct Doncaster Flat 10f Heavy 17/18
    DATA for: Has won at this trip or further; Good recent finishing positions; Carries 6 lb less than average
    DATA against: Official rating 69, 7 lb below field average
- Triple Force (hrs_37316762) | 5yo G | 129lb | OR 73 | draw 2 | jockey Tom Eaves | trainer Craig Lidster (14d 0/3) | headgear - | last run 67 days | form -04342 | MARKET 3.0% | 09:00 median 19.00 | Matchbook 55.00
    comment: Second last time out and a third three starts back show Triple Force is running with credit, though he is yet to win in his last five and returns after 67 days.
    DATA: model 8.6% | style Prominent (led 5% of runs) | runs in data 5 | last 3: 12 Jun York Flat 10.3f Good 3/18; 27 Jun Chester Flat 12.3f Good 4/8; 19 Sep Newmarket Flat 9f Good 2/14
    DATA for: Good recent finishing positions
- Morcar (hrs_29227163) | 6yo G | 134lb | OR 78 | draw 4 | jockey Ben Pollard(7) | trainer Richard Hannon (14d 1/11) | headgear b | last run 93 days | form 561262 | MARKET 3.0% | 09:00 median 21.00 | Matchbook 40.00
    comment: Morcar was second last time out and a winner four starts back, and he has run over today's trip and going before, but a 93-day absence and a sixth two starts back raise fitness and consistency questions.
    DATA: model 4.6% | style Midfield (led 3% of runs) | runs in data 7 | last 3: 13 Jul Windsor Flat 10f Good To Firm 2/7; 23 Jul Sandown Flat 9.9f Good To Firm 6/6; 24 Aug Windsor Flat 11.4f Good To Firm 2/7
    DATA for: Last-run finishing speed +2.2% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Returns from a 93-day break
- Caromb (hrs_47313952) | 4yo G | 140lb | OR 84 | draw 9 | jockey Mark Winn | trainer David O'Meara (14d 1/14) | headgear ht (1st time) | last run 19 days | form 054970 | MARKET 2.7% | 09:00 median 26.00 | Matchbook 42.00
    comment: Caromb is yet to score in his last six starts, with a seventh two starts back and a ninth three back, though a fourth four starts back shows he can run to a respectable level. He has run over today's trip and going before and is fresh enough after 19 days, but 140 lb from stall nine off a mark of 84 looks a lot to ask.
    DATA: model 6.3% | style Held up (led 5% of runs) | runs in data 2 | last 3: 12 Oct Kempton Flat 8f Standard To Slow 7/14; 6 Nov Newcastle (AW) Flat 10f Standard 12/14 fig 70
    DATA for: Official rating 84, 8 lb above field average; First-time headgear
    DATA against: Recent figures 14 lb below its current mark (looks high in the weights); Carries 9 lb more than average; Lightly raced: 2 runs in our data, so the model has little to go on
- Izzari (hrs_42520926) | 5yo G | 130lb | OR 74 | draw 1 | jockey Cara Tuke(7) | trainer Iain Jardine (14d 0/9) | headgear - | last run 21 days | form 814187 | MARKET 2.2% | 09:00 median 41.00 | Matchbook 46.00
    comment: Izzari has slipped to a seventh last time out and an eighth before that, which makes him hard to fancy, though he won three starts back and five starts back.
    DATA: model 5.0% | style Midfield (led 4% of runs) | runs in data 13 | last 3: 10 Oct Southwell Flat 8.1f Standard 1/12; 22 Oct Southwell (AW) Flat 8f Standard 8/11 fig 66; 4 Nov Musselburgh Flat 8f Soft 7/10 fig 65
    DATA against: Best recent form figure 66, 5 lb below field average; Recent figures 8 lb below its current mark (looks high in the weights); Trainer 0 wins from 9 runs, last 14 days
- High Point (hrs_35149184) | 5yo G | 126lb | OR 70 | draw 11 | jockey Greg Fairley | trainer Iain Jardine (14d 0/9) | headgear - | last run 19 days | form 006890 | MARKET 1.0% | 09:00 median 81.00 | Matchbook 170.00
    comment: High Point is hard to fancy, unplaced last time out and without a win in his last six starts, with a ninth and an eighth before that.
    DATA: model 1.0% | style Midfield (led 4% of runs) | runs in data 11 | last 3: 10 Oct York Flat 13.9f Good To Soft 8/12; 20 Oct Newcastle (AW) Flat 12.5f Standard 9/9 fig 61; 6 Nov Newcastle (AW) Flat 10f Standard 14/14 fig 51
    DATA for: Has won at this trip or further; Carries 5 lb less than average
    DATA against: Best recent form figure 61, 10 lb below field average; Recent figures 9 lb below its current mark (looks high in the weights); Official rating 70, 6 lb below field average; Trainer 0 wins from 9 runs, last 14 days; Last-run finishing speed -2.1% vs that field (faded); Poor recent finishing positions

## 2:55 Newcastle (AW) | race_id rac_32305521742 | All-Weather Championship Is Back EBF Fillies' Novice Stakes (GBB Race)
Flat | Class 4 | 6f | going Standard | AW | 9 runners | rating band - | age 2yo
DATA pace: Unclear - Running styles known for only 2 of 9 runners.
- Persian Coast (hrs_17392615030) | 2yo F | 128lb | OR - | draw 6 | jockey Rowan Scott | trainer Kevin Philippart de Foy (14d 3/8) | headgear - | last run 9 days | form 4 | MARKET 30.8% | 09:00 median 2.75 | Matchbook 2.94
    DATA: model 18.9% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 16 Nov Wolverhampton (AW) Flat 6f Standard 4/13 fig 64
    DATA for: Trainer 38% wins (3/8), last 14 days
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Sweet Pea (hrs_17394438194) | 2yo F | 128lb | OR - | draw 7 | jockey Kieran Shoemark | trainer Ed Walker (14d 1/15) | headgear - | last run - days | form - | MARKET 15.5% | 09:00 median 6.00 | Matchbook 6.00
    DATA: model 9.8% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Blowing Up A Storm (hrs_17392171755) | 2yo F | 128lb | OR - | draw 2 | jockey Alex Jary(3) | trainer Nigel Tinkler (14d 0/4) | headgear - | last run 72 days | form 3 | MARKET 14.8% | 09:00 median 5.00 | Matchbook 6.60
    DATA: model 11.8% | style Unknown | runs in data 1 | last 3: 14 Sep Kempton Flat 6f Standard To Slow 3/8
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Perfect Supernova (hrs_17396000608) | 2yo F | 128lb | OR - | draw 8 | jockey Oisin Orr | trainer Charlie Fellowes (14d 3/9) | headgear - | last run - days | form - | MARKET 11.1% | 09:00 median 8.00 | Matchbook 8.40
    DATA: model 9.8% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 33% wins (3/9), last 14 days
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Lucky For Baileys (hrs_17395451990) | 2yo F | 128lb | OR - | draw 1 | jockey Cieren Fallon | trainer Charlie Johnston (14d 0/10) | headgear - | last run - days | form - | MARKET 9.4% | 09:00 median 9.00 | Matchbook 11.00
    DATA: model 9.8% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Trainer 0 wins from 10 runs, last 14 days; Lightly raced: 0 runs in our data, so the model has little to go on
- Beautiful Force (hrs_17393454645) | 2yo F | 128lb | OR - | draw 4 | jockey Jason Hart | trainer John & Sean Quinn (14d 1/8) | headgear - | last run 30 days | form 3 | MARKET 8.9% | 09:00 median 9.90 | Matchbook 10.50
    DATA: model 10.4% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 26 Oct Leicester Flat 6f Soft 3/6 fig 74
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- The Resdev Pumpkin (hrs_17396001651) | 2yo F | 128lb | OR - | draw 10 | jockey Billy Garritty | trainer Michael & David Easterby (14d 1/7) | headgear - | last run - days | form - | MARKET 3.5% | 09:00 median 23.00 | Matchbook 32.00
    DATA: model 9.8% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Wafflebomb (hrs_17396002694) | 2yo F | 128lb | OR - | draw 9 | jockey Oisin McSweeney | trainer Bryan Smart (14d 1/7) | headgear - | last run - days | form - | MARKET 3.3% | 09:00 median 23.00 | Matchbook 38.00
    DATA: model 9.8% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Cornish Pol (hrs_64847006) | 2yo F | 128lb | OR - | draw 3 | jockey Sean Dylan Bowen | trainer Ivan Furtado (14d 1/14) | headgear - | last run - days | form - | MARKET 2.7% | 09:00 median 34.00 | Matchbook 40.00
    DATA: model 9.8% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on

## 3:25 Newcastle (AW) | race_id rac_32305523679 | AWC Finals Day At Newcastle 26th March EBF Restricted Novice Stakes (For Horses In Bands B, C And D) (GBB/GBBPlus Race)
Flat | Class 4 | 1m5y | going Standard | AW | 12 runners | rating band - | age 2yo
DATA pace: Unclear - Running styles known for only 5 of 12 runners.
- Grinanbearit (hrs_17392818415) | 2yo F | 125lb | OR 75 | draw 4 | jockey Kieran Shoemark | trainer Ed Walker (14d 1/15) | headgear - | last run 35 days | form 32 | MARKET 26.8% | 09:00 median 3.00 | Matchbook 3.45 | CHECK (skip line 2.85)
    DATA: model 27.8% | style Prominent (led 38% of runs) | runs in data 2 | last 3: 25 Sep Haydock Flat 7f Soft 3/10; 21 Oct Newmarket Flat 7f Good To Soft 2/8 fig 56
    DATA for: Best recent form figure 56, 14 lb above field average; Good recent finishing positions
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- St Edmund (hrs_17396006866) | 2yo C | 133lb | OR - | draw 10 | jockey Daniel Muscutt | trainer John & Thady Gosden (14d 2/21) | headgear - | last run - days | form - | MARKET 25.9% | 09:00 median 3.12 | Matchbook 3.55
    DATA: model 6.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Alfonso (hrs_17394655138) | 2yo C | 130lb | OR - | draw 6 | jockey Cieren Fallon | trainer William Haggas (14d 4/22) | headgear - | last run 26 days | form 7 | MARKET 16.1% | 09:00 median 5.35 | Matchbook 5.60
    DATA: model 6.8% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 30 Oct Newmarket Flat 7f Good To Soft 7/12 fig 46
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Quavo (hrs_17396005823) | 2yo C | 133lb | OR - | draw 7 | jockey Jack Callan | trainer George Boughey (14d 6/22) | headgear - | last run - days | form - | MARKET 7.1% | 09:00 median 12.00 | Matchbook 13.50
    DATA: model 6.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 27% wins (6/22), last 14 days
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Helvellyn (hrs_17396003737) | 2yo C | 133lb | OR - | draw 3 | jockey Rowan Scott | trainer Charlie Johnston (14d 0/10) | headgear - | last run - days | form - | MARKET 5.6% | 09:00 median 12.00 | Matchbook 21.00
    DATA: model 6.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Trainer 0 wins from 10 runs, last 14 days; Lightly raced: 0 runs in our data, so the model has little to go on
- Plinian (hrs_17395877534) | 2yo C | 133lb | OR - | draw 9 | jockey Oisin Orr | trainer Edward Bethell (14d 0/9) | headgear - | last run - days | form - | MARKET 5.2% | 09:00 median 15.00 | Matchbook 17.50
    DATA: model 6.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Trainer 0 wins from 9 runs, last 14 days; Lightly raced: 0 runs in our data, so the model has little to go on
- Leading Statesman (hrs_17395552118) | 2yo C | 133lb | OR - | draw 1 | jockey David Egan | trainer Tom Clover (14d 0/3) | headgear - | last run - days | form - | MARKET 4.9% | 09:00 median 17.00 | Matchbook 20.00
    DATA: model 6.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Global Twilight (hrs_17395548989) | 2yo G | 133lb | OR - | draw 2 | jockey Kaiya Fraser | trainer Charlie Fellowes (14d 3/9) | headgear - | last run 7 days | form 0 | MARKET 2.0% | 09:00 median 41.00 | Matchbook 65.00
    DATA: model 8.0% | style Unknown | runs in data 1 | last 3: 18 Nov Kempton (AW) Flat 8f Standard / Slow 12/14 fig 43
    DATA for: Trainer 33% wins (3/9), last 14 days
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Saxon Law (hrs_17394309905) | 2yo C | 133lb | OR - | draw 8 | jockey Mark Winn | trainer David O'Meara (14d 1/14) | headgear - | last run 32 days | form 0 | MARKET 2.0% | 09:00 median 29.00 | Matchbook 85.00
    DATA: model 4.9% | style Held up (led 8% of runs) | runs in data 1 | last 3: 24 Oct Southwell (AW) Flat 8f Standard 10/10 fig 37
    DATA against: Best recent form figure 37, 5 lb below field average; Lightly raced: 1 run in our data, so the model has little to go on
- Jr's Dream (hrs_7000002632) | 2yo G | 130lb | OR - | draw 12 | jockey Ryan Sexton | trainer Julie Camacho (14d 1/11) | headgear - | last run - days | form - | MARKET 1.9% | 09:00 median 34.00 | Matchbook 85.00
    DATA: model 6.3% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- White Rose Warrior (hrs_60820018) | 2yo G | 127lb | OR - | draw 5 | jockey William Pyle | trainer Craig Lidster (14d 0/3) | headgear - | last run 29 days | form 5 | MARKET 1.9% | 09:00 median 29.00 | Matchbook 80.00
    DATA: model 8.0% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 27 Oct Wolverhampton (AW) Flat 8.5f Standard 5/12 fig 42
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Arkenforce (hrs_17393457774) | 2yo C | 127lb | OR - | draw 11 | jockey Alistair Rawlinson | trainer Michael Appleby (14d 0/16) | headgear - | last run 29 days | form 80 | MARKET 0.7% | 09:00 median 126.00 | Matchbook 330.00
    DATA: model 6.3% | style Held up (led 5% of runs) | runs in data 2 | last 3: 8 Oct Bath Flat 8f Good 8/13; 27 Oct Wolverhampton (AW) Flat 8.5f Standard 11/12 fig 30
    DATA against: Best recent form figure 30, 12 lb below field average; Trainer 0 wins from 16 runs, last 14 days; Lightly raced: 2 runs in our data, so the model has little to go on

## 3:55 Newcastle (AW) | race_id rac_32305525616 | AWC Season 14 Has Begun Handicap Stakes
Flat | Class 3 | 1m5y | going Standard | AW | 12 runners | rating band 0-95 | age 3yo+
DATA pace: Lone leader - Canvas is the only habitual front-runner and may be allowed an easy lead.
- Lighting Thunder (hrs_56811419) | 3yo C | 132lb | OR 89 | draw 2 | jockey Cieren Fallon | trainer John & Thady Gosden (14d 2/21) | headgear - | last run 25 days | form 2-214 | MARKET 33.3% | 09:00 median 2.50 | Matchbook 2.68
    comment: Lighting Thunder was fourth last time out, and a winner two starts back, with a second three starts back and another second four starts back, so he's consistent and fresh enough after 25 days.
    DATA: model 20.3% | style Prominent (led 5% of runs) | runs in data 3 | last 3: 18 Apr Newbury Flat 8f Good 2/25; 9 May Nottingham Flat 8.3f Good To Firm 1/6; 31 Oct Newmarket Flat 8f Good To Soft 4/14 fig 97
    DATA for: Best recent form figure 97, 6 lb above field average; Recent figures 8 lb above its current mark (looks well handicapped); Has won at this trip or further; Good recent finishing positions
- McMurray (hrs_52418170) | 3yo G | 136lb | OR 93 | draw 7 | jockey Jack Callan | trainer George Boughey (14d 6/22) | headgear - | last run 67 days | form 111-10 | MARKET 12.5% | 09:00 median 6.50 | Matchbook 7.40
    comment: McMurray won four of his last five starts, with victories two, three, four and five starts back, but he was unplaced last time out and returns after 67 days off.
    DATA: model 14.3% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 7 May Chester Flat 7.6f Good 1/12; 19 Sep Ayr Flat 8f Heavy 11/14
    DATA for: Trainer 27% wins (6/22), last 14 days; Has won at this trip or further
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Lost Signal (hrs_54613727) | 3yo C | 134lb | OR 91 | draw 8 | jockey Kieran Shoemark | trainer Richard Hannon (14d 1/11) | headgear - | last run 109 days | form 11-274 | MARKET 9.5% | 09:00 median 9.00 | Matchbook 9.40
    DATA: model 9.5% | style Unknown | runs in data 2 | last 3: 14 Apr Newmarket Flat 7f Good 2/5; 8 Aug Haydock Flat 8f Good 4/13
    DATA for: Last-run finishing speed +2.1% vs that field (finished strongly)
    DATA against: Returns from a 109-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- Supido (hrs_42880257) | 4yo G | 136lb | OR 91 | draw 4 | jockey Edward Greatrex | trainer Ian Williams (14d 3/23) | headgear t | last run 25 days | form 740036 | MARKET 8.4% | 09:00 median 9.00 | Matchbook 12.00
    comment: The risk is that he is winless in his last six and was only sixth last time out.
    DATA: model 5.4% | style Held up (led 5% of runs) | runs in data 7 | last 3: 5 Sep Kempton Flat 8f Standard To Slow 12/14; 11 Oct Goodwood Flat 8f Good To Soft 3/13; 31 Oct Newmarket Flat 8f Good To Soft 6/14 fig 95
    DATA for: Best recent form figure 95, 4 lb above field average; Recent figures 4 lb above its current mark (looks well handicapped); Has won at this trip or further
- God of War (hrs_40918913) | 4yo G | 132lb | OR 87 | draw 6 | jockey David Egan | trainer Tom Clover (14d 0/3) | headgear - | last run 25 days | form 574433 | MARKET 8.0% | 09:00 median 10.00 | Matchbook 12.00
    comment: Yet to win in his last six, so finding the extra gear to get his head in front is the one question.
    DATA: model 8.0% | style Prominent (led 5% of runs) | runs in data 9 | last 3: 17 Sep Yarmouth Flat 6f Good 4/9; 13 Oct Leicester Flat 7f Good To Soft 3/17; 31 Oct Newmarket Flat 8f Good To Soft 3/14 fig 98
    DATA for: Best recent form figure 98, 8 lb above field average; Recent figures 11 lb above its current mark (looks well handicapped); Good recent finishing positions
- Saytarr (hrs_39960403) | 4yo G | 137lb | OR 92 | draw 12 | jockey Daniel Muscutt | trainer James Horton (14d 0/7) | headgear - | last run 123 days | form 113510 | MARKET 5.8% | 09:00 median 13.00 | Matchbook 16.50
    comment: Saytarr won three of his last six, including two starts back, but he was unplaced last time out and returns after 123 days off.
    DATA: model 5.5% | style Held up (led 3% of runs) | runs in data 7 | last 3: 28 May Sandown Flat 8f Good 5/7; 29 Jun Kempton Flat 8f Standard To Slow 1/14; 25 Jul Ascot Flat 7f Good To Firm 11/16
    DATA for: Has won at this trip or further
    DATA against: Returns from a 123-day break
- Nepal (hrs_47869164) | 4yo G | 131lb | OR 86 | draw 9 | jockey Jason Hart | trainer Ivan Furtado (14d 1/14) | headgear v | last run 40 days | form 810401 | MARKET 5.7% | 09:00 median 13.00 | Matchbook 18.00
    comment: Nepal won last time out and has two wins in his last six, but the form is patchy either side, with an unplaced run two starts back and a fourth three starts back.
    DATA: model 3.9% | style Prominent (led 29% of runs) | runs in data 3 | last 3: 19 Jul Redcar Flat 10f Good To Firm 4/4; 9 Sep Redcar Flat 10f Good 10/11; 16 Oct Newcastle (AW) Flat 8f Standard 1/9 fig 87
    DATA for: Has won at this trip or further
- Canvas (hrs_42005474) | 4yo G | 133lb | OR 88 | draw 5 | jockey Kieran O'Neill | trainer Scott Dixon (14d 0/10) | headgear p | last run 33 days | form 622161 | MARKET 5.2% | 09:00 median 12.00 | Matchbook 24.00
    comment: Canvas won last time out and has two wins in his last six, with a second and a win before that sixth, so the form is hardly poor, and he has run over today's trip and going.
    DATA: model 14.2% | style Leader (led 29% of runs) | runs in data 9 | last 3: 5 Oct Wolverhampton Flat 9.5f Standard 1/11; 10 Oct York Flat 7.9f Soft 6/20; 23 Oct Wolverhampton (AW) Flat 9.5f Standard 1/12 fig 84
    DATA for: Has won at this trip or further; Good recent finishing positions; Pace: may get an uncontested lead
    DATA against: Best recent form figure 84, 6 lb below field average; Trainer 0 wins from 10 runs, last 14 days
- Fantastic Fox (hrs_22828953) | 8yo G | 131lb | OR 86 | draw 11 | jockey Sean Dylan Bowen | trainer Roger Varian (14d 5/8) | headgear - | last run 44 days | form 70-014 | MARKET 4.0% | 09:00 median 17.00 | Matchbook 28.00
    comment: Fourth last time out and a winner two starts back, Fantastic Fox has run over today's trip and on this going, but 44 days off and 131 lb leave him a little to prove.
    DATA: model 8.7% | style Held up (led 4% of runs) | runs in data 3 | last 3: 13 Jun York Flat 8.8f Good 11/16; 25 Jul Newcastle Flat 8f Standard To Slow 1/12; 12 Oct Kempton Flat 8f Standard To Slow 4/14
    DATA for: Trainer 62% wins (5/8), last 14 days; Has won at this trip or further
    DATA against: Aged 8, older than most of this field
- Samra Green (hrs_55516034) | 3yo F | 127lb | OR 84 | draw 10 | jockey Clifford Lee | trainer K. R. Burke (14d 0/10) | headgear - | last run 44 days | form 17-205 | MARKET 2.9% | 09:00 median 21.00 | Matchbook 48.00
    comment: Samra Green was fifth last time out and unplaced the run before, so the recent form is patchy, though she was second three starts back and won five starts back.
    DATA: model 4.2% | style Prominent (led 38% of runs) | runs in data 3 | last 3: 12 Apr Musselburgh Flat 8f Good To Soft 2/11; 13 Sep Doncaster Flat 7f Good 14/14; 12 Oct Musselburgh Flat 7.1f Good To Soft 5/7
    DATA for: Carries 6 lb less than average
    DATA against: Trainer 0 wins from 10 runs, last 14 days
- Previous (hrs_54090743) | 3yo F | 133lb | OR 90 | draw 13 | jockey Rowan Scott | trainer Kevin Philippart de Foy (14d 3/8) | headgear - | last run 35 days | form 1213-4 | MARKET 2.8% | 09:00 median 23.00 | Matchbook 44.00
    comment: In her favour, she's a winner three starts back and has run over today's trip and going, carrying 133 lb from draw 13.
    DATA: model 4.3% | style Held up (led 8% of runs) | runs in data 1 | last 3: 21 Oct Newmarket Flat 8f Soft 4/5 fig 82
    DATA for: Trainer 38% wins (3/8), last 14 days
    DATA against: Best recent form figure 82, 8 lb below field average; Recent figures 8 lb below its current mark (looks high in the weights); Lightly raced: 1 run in our data, so the model has little to go on
- Old Cock (hrs_40514691) | 5yo G | 133lb | OR 88 | draw 3 | jockey Cam Hardie | trainer Antony Brittain (14d 2/13) | headgear t | wind surgery | last run 195 days | form 140-00 | MARKET 2.0% | 09:00 median 41.00 | Matchbook 55.00
    comment: Old Cock was last seen winning five starts back but has been unplaced in his last three, and a 195-day absence raises fitness questions.
    DATA: model 1.8% | style Midfield (led 8% of runs) | runs in data 2 | last 3: 18 Apr Newbury Flat 8f Good 20/24; 14 May York Flat 7.9f Good 16/18
    DATA against: Last-run finishing speed -2.5% vs that field (faded); Returns from a 195-day break; Lightly raced: 2 runs in our data, so the model has little to go on

## 4:25 Newcastle (AW) | race_id rac_32305527553 | Make The Move To Midnite Handicap Stakes
Flat | Class 4 | 6f | going Standard | AW | 11 runners | rating band 0-80 | age 3yo+
DATA pace: Strong pace - 3 habitual front-runners (Angel Love, Saffron Dandy, Venture Capital). A contested lead should set things up for horses coming from behind.
- Massimo Blue (hrs_47162024) | 4yo G | 132lb | OR 77 | draw 11 | jockey Edward Greatrex | trainer Dylan Cunha (14d 2/13) | headgear - | last run 26 days | form 114612 | MARKET 18.7% | 09:00 median 4.33 | Matchbook 5.00 | CHECK (skip line 4.11)
    comment: Massimo Blue arrives in fine heart, a second last time out and a winner two starts back, with three wins in his last six and experience of today's trip and going after 26 days off.
    DATA: model 18.6% | style Midfield (led 3% of runs) | runs in data 10 | last 3: 26 Sep Southwell Flat 6.1f Standard 6/13; 19 Oct Southwell (AW) Flat 6f Standard 1/10 fig 79; 30 Oct Newcastle (AW) Flat 6f Standard 2/11 fig 73
    DATA for: Best recent form figure 79, 7 lb above field average; Has won at this trip or further; Good recent finishing positions
- Diligent Resdev (hrs_37701622) | 5yo G | 130lb | OR 75 | draw 6 | jockey Joanna Mason | trainer Michael & David Easterby (14d 1/7) | headgear v | last run 41 days | form 969606 | MARKET 16.8% | 09:00 median 5.00 | Matchbook 5.50
    comment: The risk is a sixth last time out and no win in his last six, plus 41 days off and 130 lb from stall six.
    DATA: model 8.1% | style Held up (led 5% of runs) | runs in data 6 | last 3: 3 Sep Southwell Flat 6.1f Standard 6/12; 9 Oct York Flat 7f Good To Soft 11/20; 15 Oct Southwell (AW) Flat 8f Standard 6/11 fig 71
    DATA for: Pace: a contested lead should suit its hold-up style
    DATA against: Poor recent finishing positions
- Itsatenfromlen (hrs_41939919) | 4yo G | 134lb | OR 79 | draw 4 | jockey Jason Hart | trainer Ivan Furtado (14d 1/14) | headgear - | last run 6 days | form 9-0505 | MARKET 16.2% | 09:00 median 5.00 | Matchbook 5.80
    comment: Quick back-up in six days after a fifth last time out, and he has run over today's trip and going before, though he is yet to win in his last five starts.
    DATA: model 7.5% | style Held up (led 8% of runs) | runs in data 3 | last 3: 1 Oct Nottingham Flat 8.3f Good 5/9; 24 Oct Doncaster Flat 7f Heavy 11/12; 19 Nov Newcastle (AW) Flat 6f Standard 5/14 fig 80
    DATA for: Best recent form figure 80, 8 lb above field average; Pace: a contested lead should suit its hold-up style
- Angel Love (hrs_56065891) | 3yo F | 134lb | OR 79 | draw 5 | jockey Rowan Scott | trainer Kevin Philippart de Foy (14d 3/8) | headgear - | last run 30 days | form -07312 | MARKET 11.8% | 09:00 median 7.20 | Matchbook 7.80
    comment: Second last time out, and a winner two starts back, Angel Love arrives in solid recent form and has run over today's trip and going before.
    DATA: model 13.9% | style Leader (led 43% of runs) | runs in data 5 | last 3: 31 Jul Wolverhampton Flat 6.1f Standard 3/10; 1 Oct Newcastle Flat 6f Standard 1/9; 26 Oct Southwell (AW) Flat 6f Standard 2/10 fig 81
    DATA for: Best recent form figure 81, 9 lb above field average; Trainer 38% wins (3/8), last 14 days; Has won at this trip or further; Good recent finishing positions; Course: front-runners have won 1.3× their fair share at 6f here
    DATA against: Pace: likely to be taken on for the lead
- Dandy Magic (hrs_42521689) | 4yo F | 135lb | OR 80 | draw 7 | jockey Lauren Young(5) | trainer Jim Goldie (14d 1/14) | headgear - | last run 21 days | form 245316 | MARKET 8.4% | 09:00 median 10.00 | Matchbook 11.00
    comment: Dandy Magic returns 21 days after a sixth last time out, though she was a winner two starts back and has run over today's trip and going before; carrying 135 lb from stall seven, her one win in six recent starts keeps her mid-pack.
    DATA: model 13.1% | style Held up (led 3% of runs) | runs in data 17 | last 3: 12 Oct Musselburgh Flat 7.1f Good To Soft 3/7; 19 Oct Pontefract Flat 6f Heavy 1/10 fig 82; 4 Nov Musselburgh Flat 7f Soft 6/12 fig 76
    DATA for: Best recent form figure 82, 10 lb above field average; Has won at this trip or further; Good recent finishing positions; Pace: a contested lead should suit its hold-up style
- Venture Capital (hrs_36179283) | 5yo G | 127lb | OR 72 | draw 9 | jockey Shane Gray | trainer Kevin Ryan (14d 0/2) | headgear v (1st time) | last run 25 days | form 894588 | MARKET 7.8% | 09:00 median 11.00 | Matchbook 12.00
    comment: Venture Capital has finished eighth in his last two outings and is winless in recent starts, though a fourth four starts back shows he can get closer, and he has run over today's trip and going.
    DATA: model 5.7% | style Leader (led 43% of runs) | runs in data 9 | last 3: 13 Sep Doncaster Flat 5f Good 5/16; 16 Oct Newcastle (AW) Flat 5f Standard 8/11 fig 69; 31 Oct Newmarket Flat 6f Good To Soft 8/10 fig 62
    DATA for: First-time headgear; Course: front-runners have won 1.3× their fair share at 6f here
    DATA against: Pace: likely to be taken on for the lead
- Juan Les Pins (hrs_19797358) | 9yo G | 132lb | OR 77 | draw 2 | jockey Kevin Stott | trainer Michael Appleby (14d 0/16) | headgear - | last run 26 days | form 906317 | MARKET 7.3% | 09:00 median 11.00 | Matchbook 13.00
    comment: The risk is a seventh last time out, though 26 days' rest should help.
    DATA: model 9.7% | style Unknown | runs in data 16 | last 3: 26 Sep Southwell Flat 5f Standard 3/10; 12 Oct Newcastle Flat 6f Standard 1/12; 30 Oct Newcastle (AW) Flat 5f Standard 7/12 fig 75
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Trainer 0 wins from 16 runs, last 14 days; Aged 9, older than most of this field
- Harry's Halo (hrs_30980789) | 6yo G | 128lb | OR 73 | draw 8 | jockey Oliver Stammers | trainer Kevin & Lauren Frost (14d 1/9) | headgear t | last run 25 days | form 332195 | MARKET 5.0% | 09:00 median 17.00 | Matchbook 19.00
    comment: Harry's Halo was a fifth last time out and a ninth before that, so the recent trend is the wrong way, though he did win three starts back and has been in the first three in four of his last six.
    DATA: model 7.4% | style Held up (led 4% of runs) | runs in data 6 | last 3: 8 Sep Leicester Flat 6f Good To Soft 1/11; 16 Oct Haydock Flat 5f Heavy 9/14 fig 60; 31 Oct Newmarket Flat 6f Good To Soft 5/10 fig 68
    DATA for: Has won at this trip or further; Pace: a contested lead should suit its hold-up style
    DATA against: Best recent form figure 68, 4 lb below field average
- Hallandale Beach (hrs_52054191) | 3yo G | 126lb | OR 71 | draw 1 | jockey Kieran O'Neill | trainer Scott Dixon (14d 0/10) | headgear t | last run 111 days | form 553313 | MARKET 3.6% | 09:00 median 13.00 | Matchbook 80.00
    comment: Hallandale Beach arrives with solid recent form, third last time out and a winner two starts back, and he has run over today's trip and going, but 111 days off is a concern.
    DATA: model 6.8% | style Midfield (led 29% of runs) | runs in data 7 | last 3: 15 Jun Windsor Flat 5.1f Good To Firm 3/10; 27 Jun Chepstow Flat 6.1f Good To Firm 1/6; 6 Aug Chepstow Flat 6.1f Good To Firm 3/4
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Trainer 0 wins from 10 runs, last 14 days; Returns from a 111-day break
- Yorkshire Glory (hrs_40132855) | 5yo G | 127lb | OR 72 | draw 10 | jockey Aiden Brookes | trainer Ben Haslam (14d 2/9) | headgear - | last run 21 days | form 118000 | MARKET 2.9% | 09:00 median 29.00 | Matchbook 34.00
    comment: Yorkshire Glory has been unplaced in each of his last three outings, after a win five starts back and another six back, so the form has clearly tailed off.
    DATA: model 2.5% | style Midfield (led 4% of runs) | runs in data 13 | last 3: 15 Sep Redcar Flat 6f Good 10/14; 12 Oct Newcastle Flat 6f Standard 10/11; 4 Nov Musselburgh Flat 7f Soft 12/12
    DATA for: Trainer 22% wins (2/9), last 14 days; Has won at this trip or further
    DATA against: Last-run finishing speed -11.3% vs that field (faded); Poor recent finishing positions
- Saffron Dandy (hrs_51897629) | 3yo F | 133lb | OR 78 | draw 3 | jockey Ben Pollard(7) | trainer Richard Hannon (14d 1/11) | headgear - | last run 37 days | form 686150 | MARKET 1.5% | 09:00 median 51.00 | Matchbook 75.00
    comment: The main risk is a flat recent profile, unplaced last time out and a fifth two starts back, after 37 days off.
    DATA: model 6.7% | style Prominent (led 43% of runs) | runs in data 9 | last 3: 12 Jun Goodwood Flat 5f Soft 1/4; 3 Jul Doncaster Flat 5f Good To Firm 5/8; 19 Oct Wolverhampton (AW) Flat 6f Standard 12/12 fig 43
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 43, 29 lb below field average; Recent figures 35 lb below its current mark (looks high in the weights); Last-run finishing speed -4.7% vs that field (faded)

## 5:00 Newcastle (AW) | race_id rac_32305529490 | AW Trials Day - Lingfield 2nd Jan 2027 Handicap Stakes
Flat | Class 5 | 1m5y | going Standard | AW | 9 runners | rating band 0-75 | age 3yo
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Shadow Boxer (hrs_63203483) | 3yo G | 135lb | OR 75 | draw 6 | jockey Kieran Shoemark | trainer Simon Crisford (14d 2/7) | headgear tv | last run 27 days | form 332 | MARKET 20.3% | 09:00 median 4.40 | Matchbook 4.40 | CHECK (skip line 4.18)
    comment: Shadow Boxer is yet to win in his last three starts but has been consistent, finishing second last time out, then a third two starts back, and another third three starts back. He has run over today's trip and going and is fresh after 27 days off, though he's still searching for that breakthrough and carries 135 lb from stall 6.
    DATA: model 22.4% | style Midfield (led 5% of runs) | runs in data 3 | last 3: 15 Apr Southwell Flat 8.1f Standard 3/12; 28 Sep Wolverhampton Flat 8.6f Standard 3/11; 29 Oct Southwell (AW) Flat 8f Standard 2/8 fig 60
    DATA for: Trainer 29% wins (2/7), last 14 days; Good recent finishing positions
    DATA against: Best recent form figure 60, 9 lb below field average; Recent figures 15 lb below its current mark (looks high in the weights)
- Yimmna (hrs_65036055) | 3yo F | 134lb | OR 74 | draw 7 | jockey Cieren Fallon | trainer William Haggas (14d 4/22) | headgear - | last run 30 days | form 72232 | MARKET 17.5% | 09:00 median 4.50 | Matchbook 5.70
    comment: Yimmna comes here in fine fettle, with a second last time out, a third two starts back and a second three starts back, and she has run over today's trip and going before.
    DATA: model 15.6% | style Prominent (led 8% of runs) | runs in data 5 | last 3: 8 Aug Redcar Flat 7f Good To Firm 2/8; 9 Sep Kempton Flat 7f Standard To Slow 3/7; 26 Oct Southwell (AW) Flat 8f Standard 2/9 fig 80
    DATA for: Best recent form figure 80, 11 lb above field average; Recent figures 6 lb above its current mark (looks well handicapped); Last-run finishing speed +2.5% vs that field (finished strongly); Good recent finishing positions
- Rapide Vega (hrs_52496192) | 3yo G | 135lb | OR 75 | draw 5 | jockey M. P. Sheehy | trainer Adrian Keatley (14d 1/7) | headgear v | last run 34 days | form 251253 | MARKET 13.4% | 09:00 median 6.50 | Matchbook 7.00
    comment: Rapide Vega arrives in solid shape, third last time out and a winner four starts back, and he has run over today's trip and going before.
    DATA: model 17.6% | style Midfield (led 4% of runs) | runs in data 8 | last 3: 29 Aug Beverley Flat 9.9f Soft 2/8; 19 Sep Newmarket Flat 9f Good 5/14; 22 Oct Southwell (AW) Flat 8f Standard 3/11 fig 73
    DATA for: Best recent form figure 73, 4 lb above field average; Last-run finishing speed +2.9% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
- Aqua Bear (hrs_55030073) | 3yo G | 135lb | OR 75 | draw 8 | jockey Edward Greatrex | trainer Ian Williams (14d 3/23) | headgear - | last run 46 days | form 403000 | MARKET 12.2% | 09:00 median 7.00 | Matchbook 7.80
    comment: Aqua Bear is winless in his last six and unplaced in his last three, but a third four starts back shows he can get involved, and he has run over today's trip and going before.
    DATA: model 3.3% | style Midfield (led 8% of runs) | runs in data 6 | last 3: 10 Jul Newmarket Flat 7f Good To Firm 11/11; 30 Jul Goodwood Flat 8f Good To Firm 17/19; 10 Oct York Flat 7.9f Soft 19/20
    DATA against: Last-run finishing speed -8.0% vs that field (faded); Poor recent finishing positions
- Leopards Rock (hrs_64780702) | 3yo G | 131lb | OR 71 | draw 4 | jockey P. J. McDonald | trainer Edward Bethell (14d 0/9) | headgear p | last run 34 days | form 235472 | MARKET 11.0% | 09:00 median 8.00 | Matchbook 8.60
    comment: Leopards Rock bounces in off a second last time out and has finished in the first three in three of his last six, though he is yet to win in that spell and a seventh two starts back shows his consistency can wobble.
    DATA: model 7.7% | style Midfield (led 29% of runs) | runs in data 7 | last 3: 9 Sep Carlisle Flat 6.9f Good 4/10; 29 Sep Ayr Flat 8f Heavy 7/8; 22 Oct Southwell (AW) Flat 8f Standard 2/11 fig 70
    DATA for: Last-run finishing speed +2.7% vs that field (finished strongly)
    DATA against: Trainer 0 wins from 9 runs, last 14 days
- Filly Eilish (hrs_61521670) | 3yo F | 134lb | OR 74 | draw 1 | jockey Jason Hart | trainer Ivan Furtado (14d 1/14) | headgear t | last run 34 days | form 155421 | MARKET 9.7% | 09:00 median 7.50 | Matchbook 11.50
    comment: Filly Eilish won last time out and was second two starts back, with experience of today's trip and going, so the form reads well, but she had been beaten in a couple of fifths before that and has 134 lb from stall one.
    DATA: model 13.8% | style Midfield (led 5% of runs) | runs in data 10 | last 3: 18 Sep Ayr Flat 8f Soft 4/8; 12 Oct Musselburgh Flat 8.9f Good To Soft 2/8; 22 Oct Southwell (AW) Flat 8f Standard 1/10 fig 71
    DATA for: Has won at this trip or further; Good recent finishing positions
- Blue To Blue (hrs_51988979) | 3yo G | 135lb | OR 75 | draw 2 | jockey Harry Russell | trainer Ruth Jefferson (14d 0/0) | headgear h | last run 26 days | form 503006 | MARKET 9.0% | 09:00 median 9.00 | Matchbook 11.00
    comment: Blue To Blue is yet to win in his last six, but he has run over today's trip and going, and a third four starts back shows he can hit the frame.
    DATA: model 6.5% | style Held up (led 4% of runs) | runs in data 9 | last 3: 3 Sep Haydock Flat 10.2f Soft 11/13; 26 Sep Market Rasen Hurdle 16.6f Good PU/7; 30 Oct Newcastle (AW) Flat 8f Standard 6/10 fig 69
    DATA against: Recent figures 6 lb below its current mark (looks high in the weights); Poor recent finishing positions; Pace: steady gallop likely, hard to come from off the pace
- Ephron (hrs_56065982) | 3yo G | 129lb | OR 69 | draw 3 | jockey Joanna Mason | trainer Gemma Tutty (14d 1/6) | headgear - | last run 71 days | form 527167 | MARKET 5.0% | 09:00 median 17.00 | Matchbook 19.50
    comment: Ephron is hard to fancy after a seventh last time out, a sixth before that, and a 71-day break, though he did win three starts back and has run over today's trip and going.
    DATA: model 9.4% | style Held up (led 5% of runs) | runs in data 7 | last 3: 1 Aug Hamilton Flat 8.3f Good 1/10; 19 Aug Carlisle Flat 7.8f Soft 6/9; 15 Sep Redcar Flat 8f Good 7/13
    DATA for: Last-run finishing speed +2.3% vs that field (finished strongly); Has won at this trip or further
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Skewsby (hrs_60125877) | 3yo G | 130lb | OR 70 | draw 9 | jockey Billy Garritty | trainer Michael & David Easterby (14d 1/7) | headgear v (1st time) | last run 18 days | form 73268 | MARKET 1.9% | 09:00 median 41.00 | Matchbook 70.00
    DATA: model 3.7% | style Held up (led 5% of runs) | runs in data 5 | last 3: 23 Sep Redcar Flat 7f Good 2/8; 3 Oct Southwell Flat 7.1f Standard 6/11; 7 Nov Doncaster Flat 7f Good To Soft 8/12 fig 58
    DATA for: First-time headgear
    DATA against: Best recent form figure 58, 11 lb below field average; Recent figures 12 lb below its current mark (looks high in the weights); Pace: steady gallop likely, hard to come from off the pace

## 5:30 Newcastle (AW) | race_id rac_32305531427 | Midnite: Built For 2026 Not 2006 Handicap Stakes
Flat | Class 6 | 5f | going Standard | AW | 14 runners | rating band 0-60 | age 3yo+
DATA pace: Lone leader - Wrestling Revenue is the only habitual front-runner and may be allowed an easy lead.
- Dc Cogent (hrs_46913300) | 4yo G | 135lb | OR 60 | draw 4 | jockey Paul Mulrennan | trainer Bryan Smart (14d 1/7) | headgear - | last run 55 days | form 837329 | MARKET 16.1% | 09:00 median 5.00 | Matchbook 5.40 | CHECK (skip line 4.75)
    comment: The risk is a ninth last time out and 55 days off.
    DATA: model 10.7% | style Midfield (led 3% of runs) | runs in data 12 | last 3: 3 Sep Newcastle Flat 5f Standard 3/8; 15 Sep Redcar Flat 5f Good 2/13; 1 Oct Newcastle Flat 5f Standard 9/9
    DATA for: Official rating 60, 6 lb above field average; Good recent finishing positions
    DATA against: Carries 6 lb more than average
- Woolridge (hrs_54712217) | 4yo G | 134lb | OR 59 | draw 9 | jockey Kieran O'Neill | trainer Scott Dixon (14d 0/10) | headgear p | last run 20 days | form 548130 | MARKET 15.6% | 09:00 median 5.00 | Matchbook 5.70
    comment: Woolridge was unplaced last time out, but he has a third two starts back and a winner three starts back, and he has run over today's trip and going.
    DATA: model 12.4% | style Midfield (led 23% of runs) | runs in data 11 | last 3: 12 Oct Newcastle Flat 6f Standard 1/12; 20 Oct Newcastle (AW) Flat 6f Standard 3/12 fig 55; 5 Nov Chelmsford (AW) Flat 6f Standard 10/10 fig 42
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Trainer 0 wins from 10 runs, last 14 days
- King's Crown (hrs_29691396) | 6yo G | 135lb | OR 60 | draw 12 | jockey Rhys Elliott(5) | trainer Michael Dods (14d 1/10) | headgear tp | last run 19 days | form 405000 | MARKET 11.4% | 09:00 median 7.00 | Matchbook 7.60
    DATA: model 6.9% | style Midfield (led 29% of runs) | runs in data 13 | last 3: 17 Sep Ayr Flat 5f Soft 10/20; 5 Oct Pontefract Flat 6f Good 11/12; 6 Nov Newcastle (AW) Flat 5f Standard 11/14 fig 50
    DATA for: Official rating 60, 6 lb above field average; Has won at this trip or further
    DATA against: Recent figures 10 lb below its current mark (looks high in the weights); Poor recent finishing positions; Carries 6 lb more than average
- Henery Hawk (hrs_26102909) | 7yo G | 132lb | OR 57 | draw 11 | jockey Kaiya Fraser | trainer Linda Perratt (14d 1/5) | headgear - | last run 71 days | form 353724 | MARKET 8.7% | 09:00 median 9.00 | Matchbook 10.00
    comment: Fourth last time out and a second two starts back suggest Henery Hawk is competitive, and he has run over today's trip and going, but he is yet to win in his last six and returns after 71 days off.
    DATA: model 13.0% | style Midfield (led 4% of runs) | runs in data 14 | last 3: 10 Aug Ayr Flat 6f Good To Soft 7/13; 1 Sep Wolverhampton Flat 5.1f Standard 2/8; 15 Sep Wolverhampton Flat 5.1f Standard 4/9
    DATA for: Trainer 20% wins (1/5), last 14 days; Has won at this trip or further
- South Shore Island (hrs_42005376) | 4yo G | 121lb | OR 46 | draw 10 | jockey Jack Callan | trainer Lizzie Quinlan (14d 2/9) | headgear tp | last run 67 days | form 342453 | MARKET 8.6% | 09:00 median 9.50 | Matchbook 10.00
    comment: South Shore Island was third last time out and has been in the first five in each of his last six starts, yet he's winless in that spell, and 67 days off the track is a concern.
    DATA: model 6.9% | style Prominent (led 23% of runs) | runs in data 6 | last 3: 11 Aug Hamilton Flat 5f Good 4/7; 22 Aug Redcar Flat 6f Good 5/16; 19 Sep Newcastle Flat 5f Standard 3/9
    DATA for: Trainer 22% wins (2/9), last 14 days; Carries 8 lb less than average
    DATA against: Official rating 46, 8 lb below field average
- Golden Havana (hrs_55665876) | 3yo G | 134lb | OR 59 | draw 2 | jockey Sean Kirrane | trainer Michael Dods (14d 1/10) | headgear v | last run 36 days | form 225065 | MARKET 6.9% | 09:00 median 10.00 | Matchbook 14.50
    comment: The main risk is that he is yet to win in that spell and arrives fresh off a 36-day break after finishing fifth last time.
    DATA: model 5.6% | style Held up (led 3% of runs) | runs in data 11 | last 3: 15 Sep Redcar Flat 5f Good 12/13; 1 Oct Newcastle Flat 5f Standard 6/9; 20 Oct Newcastle (AW) Flat 5f Standard 5/13 fig 57
    DATA for: Best recent form figure 57, 5 lb above field average
- Shatin Venture (hrs_36035916) | 5yo G | 121lb | OR 46 | draw 13 | jockey Tom Kiely-Marshall(3) | trainer Linda Perratt (14d 1/5) | headgear - | last run 40 days | form 259923 | MARKET 6.0% | 09:00 median 11.00 | Matchbook 17.50
    comment: Shatin Venture was third last time out and a second two starts back, but he is yet to win in his last six starts and has two ninth-place finishes in that spell.
    DATA: model 4.8% | style Held up (led 5% of runs) | runs in data 8 | last 3: 2 Sep Newcastle Flat 5f Standard 9/9; 25 Sep Newcastle Flat 5f Standard 2/8; 16 Oct Newcastle (AW) Flat 5f Standard 3/10 fig 46
    DATA for: Trainer 20% wins (1/5), last 14 days; Good recent finishing positions; Carries 8 lb less than average
    DATA against: Best recent form figure 46, 6 lb below field average; Official rating 46, 8 lb below field average
- Wrestling Revenue (hrs_36234639) | 5yo G | 127lb | OR 52 | draw 7 | jockey Jude Maher(7) | trainer Stephen Hanlon (14d 0/4) | headgear - | last run 40 days | form 075654 | MARKET 5.3% | 09:00 median 12.00 | Matchbook 21.00
    comment: Wrestling Revenue is winless in his last six, with a fourth last time out the best of a run of fifth, sixth and fifth finishes, and 40 days off makes him hard to fancy.
    DATA: model 7.4% | style Leader (led 43% of runs) | runs in data 7 | last 3: 11 Jun Nottingham Flat 5f Soft 6/6; 12 Sep Musselburgh Flat 5f Good 5/11; 16 Oct Redcar Flat 5f Good 4/10 fig 53
    DATA for: Pace: may get an uncontested lead
- Delagate This Lord (hrs_8454103) | 12yo G | 133lb | OR 58 | draw 14 | jockey Billy Garritty | trainer Stephen Hanlon (14d 0/4) | headgear - | last run 19 days | form 348-08 | MARKET 5.2% | 09:00 median 15.00 | Matchbook 17.50
    comment: The risk is a run of eighth, unplaced, eighth, leaving him winless lately.
    DATA: model 4.5% | style Held up (led 5% of runs) | runs in data 2 | last 3: 26 Oct Redcar Flat 6f Heavy 13/14 fig 11; 6 Nov Newcastle (AW) Flat 6f Standard 8/14 fig 59
    DATA for: Best recent form figure 59, 7 lb above field average
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Aged 12, older than most of this field
- Auntie Jo (hrs_41877675) | 4yo F | 127lb | OR 52 | draw 1 | jockey Sean Dylan Bowen | trainer Katie Scott (14d 0/5) | headgear b | last run 18 days | form 153736 | MARKET 5.1% | 09:00 median 13.00 | Matchbook 19.50
    comment: Auntie Jo has finished third twice in her last six outings and was sixth last time, 18 days ago, so she's fit enough, and she has run over today's trip and going.
    DATA: model 5.0% | style Midfield (led 4% of runs) | runs in data 18 | last 3: 21 Jul Wolverhampton Flat 6.1f Standard 7/11; 20 Oct Newcastle (AW) Flat 5f Standard 3/10 fig 53; 7 Nov Southwell (AW) Flat 6f Standard 6/11 fig 49
    DATA for: Has won at this trip or further
- Crypto Quest (hrs_24456215) | 7yo G | 128lb | OR 53 | draw 5 | jockey Christian Howarth(3) | trainer Scott Dixon (14d 0/10) | headgear - | last run 34 days | form 067204 | MARKET 3.0% | 09:00 median 19.00 | Matchbook 42.00
    comment: Crypto Quest is winless in his last six, with a fourth last time out the best of his recent efforts bar a second three starts back, so he is hard to fancy at 128 lb from draw 5.
    DATA: model 7.9% | style Midfield (led 8% of runs) | runs in data 6 | last 3: 6 Oct Southwell Flat 5f Standard 2/11; 16 Oct Newcastle (AW) Flat 5f Standard 10/10 fig 33; 22 Oct Southwell (AW) Flat 5f Standard 4/11 fig 55
    DATA against: Trainer 0 wins from 10 runs, last 14 days
- Until Dawn (hrs_42451892) | 4yo F | 132lb | OR 57 | draw 3 | jockey Tom Eaves | trainer Alan Brown (14d 0/2) | headgear - | last run 182 days | form 8-7367 | MARKET 2.9% | 09:00 median 23.00 | Matchbook 40.00
    DATA: model 8.3% | style Unknown | runs in data 4 | last 3: 3 May Hamilton Flat 5f Good 3/12; 15 May Hamilton Flat 5f Good 6/10; 27 May Beverley Flat 5f Good To Firm 7/9
    DATA against: Last-run finishing speed -3.1% vs that field (faded); Returns from a 182-day break
- Powernap (hrs_53960263) | 3yo F | 127lb | OR 52 | draw 6 | jockey Jake Dickson(5) | trainer Jessica Bedi (14d 0/7) | headgear t | last run 40 days | form 218549 | MARKET 2.6% | 09:00 median 23.00 | Matchbook 46.00
    comment: Beaten in her last four outings, including a ninth last time out, Powernap has slipped since winning five starts back, though she has run over today's trip and going before.
    DATA: model 4.8% | style Midfield (led 3% of runs) | runs in data 9 | last 3: 26 Aug Catterick Flat 6f Good 5/5; 1 Oct Newcastle Flat 5f Standard 4/9; 16 Oct Newcastle (AW) Flat 5f Standard 9/10 fig 39
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 39, 13 lb below field average; Recent figures 13 lb below its current mark (looks high in the weights)
- Thank The Lord (hrs_25312637) | 7yo G | 121lb | OR 46 | draw 8 | jockey Cam Hardie | trainer Stephen Hanlon (14d 0/4) | headgear v | last run 110 days | form 860909 | MARKET 2.5% | 09:00 median 21.00 | Matchbook 60.00
    comment: Winless in his last six, Thank The Lord was beaten into ninth last time out and returns from a 110-day absence, and he has been unplaced or worse throughout, so he is hard to fancy. He has run over today's trip and going, and a mark of 46 is low, but that is about all he has going for him.
    DATA: model 1.6% | style Prominent (led 5% of runs) | runs in data 6 | last 3: 23 Mar Wolverhampton Flat 6.1f Standard 9/9; 24 Apr Doncaster Flat 5f Good To Firm 14/14; 7 Aug Thirsk Flat 6f Good 9/9
    DATA for: Carries 8 lb less than average
    DATA against: Official rating 46, 8 lb below field average; Last-run finishing speed -7.8% vs that field (faded); Poor recent finishing positions; Returns from a 110-day break

## 6:00 Newcastle (AW) | race_id rac_32305533364 | All-Weather Championship Season 14 Has Begun Apprentice Handicap Stakes (Div I)
Flat | Class 6 | 7f14y | going Standard | AW | 12 runners | rating band 0-55 | age 3yo+
DATA pace: Lone leader - Tomorrow Day is the only habitual front-runner and may be allowed an easy lead.
- Multaneighttothree (hrs_60527747) | 4yo G | 135lb | OR 55 | draw 7 | jockey Ryan Kavanagh | trainer Grant Tuer (14d 0/6) | headgear - | last run 2 days | form 35945 | MARKET 21.3% | 09:00 median 3.75 | Matchbook 4.30 | CHECK (skip line 3.56)
    comment: Quick back-up after a fifth last time out two days ago, Multaneighttothree has run over today's trip and on this going, and he was third five starts back.
    DATA: model 20.1% | style Midfield (led 4% of runs) | runs in data 5 | last 3: 24 Feb Newcastle Flat 8f Standard 9/10; 20 Aug Newcastle Flat 6f Standard 4/14; 23 Nov Newcastle (AW) Flat 6f Standard 5/13 fig 54
    DATA for: Best recent form figure 54, 5 lb above field average; Official rating 55, 7 lb above field average
    DATA against: Carries 6 lb more than average
- Tomorrow Day (hrs_36137451) | 5yo G | 133lb | OR 53 | draw 3 | jockey Rhys Elliott | trainer Mark Usher (14d 0/5) | headgear tv | last run 2 days | form -22134 | MARKET 18.1% | 09:00 median 4.50 | Matchbook 4.90
    comment: Tomorrow Day has been consistent, with a fourth last time out, a third two starts back and a winner three starts back, and he has run over today's trip and going before.
    DATA: model 20.6% | style Leader (led 29% of runs) | runs in data 5 | last 3: 3 Sep Newcastle Flat 6f Standard 1/8; 30 Oct Newcastle (AW) Flat 7f Standard 3/11 fig 54; 23 Nov Newcastle (AW) Flat 6f Standard 4/13 fig 53
    DATA for: Best recent form figure 54, 5 lb above field average; Official rating 53, 5 lb above field average; Good recent finishing positions; Pace: may get an uncontested lead
- Diligent Henry (hrs_36207647) | 5yo G | 126lb | OR 45 | draw 10 | jockey Molly Keegan-Price(7) | trainer Gemma Tutty (14d 1/6) | headgear b | last run 1 days | form 505671 | MARKET 14.3% | 09:00 median 5.25 | Matchbook 6.60
    comment: Diligent Henry won last time out and is back after just one day, though that came after a run of fifth, sixth and seventh finishes before it.
    DATA: model 9.0% | style Prominent (led 4% of runs) | runs in data 9 | last 3: 21 Jun Pontefract Flat 6f Good 6/11; 29 Oct Southwell (AW) Flat 7f Standard 7/13 fig 41; 24 Nov Wolverhampton (AW) Flat 6f Standard 1/13 fig 58
    DATA for: Best recent form figure 58, 9 lb above field average; Recent figures 13 lb above its current mark (looks well handicapped)
- Teardrops (hrs_39962335) | 4yo G | 133lb | OR 53 | draw 12 | jockey Darragh O'Sullivan(5) | trainer Tony Carroll (14d 2/36) | headgear b | last run 2 days | form 800033 | MARKET 13.3% | 09:00 median 6.00 | Matchbook 6.80
    comment: Teardrops arrives in better heart with a third last time out and another third two starts back, though he's winless in his last six and was only two days ago, so freshness is a question. He has run over today's trip and going, but 133 lb from draw 12 asks plenty.
    DATA: model 8.8% | style Prominent (led 4% of runs) | runs in data 13 | last 3: 2 Oct Wolverhampton Flat 5.1f Standard 10/11; 7 Nov Southwell (AW) Flat 6f Standard 3/11 fig 50; 23 Nov Newcastle (AW) Flat 6f Standard 3/13 fig 54
    DATA for: Best recent form figure 54, 5 lb above field average; Official rating 53, 5 lb above field average; Good recent finishing positions
- The New Bay Pearl (hrs_47655293) | 4yo F | 130lb | OR 50 | draw 8 | jockey Jake Dickson(3) | trainer Simon Whitaker (14d 0/3) | headgear - | last run 19 days | form 443550 | MARKET 8.6% | 09:00 median 9.50 | Matchbook 11.00
    comment: The New Bay Pearl has run over today's trip and going and returns after 19 days, a third four starts back her best finish in a winless recent spell.
    DATA: model 6.6% | style Midfield (led 4% of runs) | runs in data 9 | last 3: 9 Sep Redcar Flat 8f Good 5/19; 17 Oct Southwell (AW) Flat 8f Standard 5/11 fig 51; 6 Nov Newcastle (AW) Flat 8f Standard 14/14 fig 36
    DATA against: Last-run finishing speed -4.0% vs that field (faded)
- Take The A Train (hrs_45475584) | 4yo G | 129lb | OR 49 | draw 13 | jockey Jack Callan | trainer Stephen Hanlon (14d 0/4) | headgear - | last run 30 days | form 9-2027 | MARKET 6.1% | 09:00 median 13.00 | Matchbook 15.50
    comment: Seventh last time out after a second two starts back, he is yet to win in his last five and returns 30 days on, though he has run over today's trip and going before.
    DATA: model 7.5% | style Prominent (led 8% of runs) | runs in data 4 | last 3: 30 Mar Wolverhampton Flat 8.6f Standard 10/11; 20 Apr Newcastle Flat 8f Standard 2/14; 26 Oct Redcar Flat 10f Heavy 7/14 fig 39
    DATA for: Last-run finishing speed +2.9% vs that field (finished strongly)
    DATA against: Best recent form figure 39, 10 lb below field average; Recent figures 10 lb below its current mark (looks high in the weights)
- Lady Delila (hrs_32401635) | 6yo M | 127lb | OR 47 | draw 11 | jockey Alexandra Egan(5) | trainer Patrick Morris (14d 0/14) | headgear p | last run 1 days | form 848150 | MARKET 4.5% | 09:00 median 17.00 | Matchbook 23.00
    comment: Lady Delila is hard to fancy after an unplaced run last time out, just one day ago, and a fifth two starts back, with her one win three starts back now fading.
    DATA: model 7.7% | style Midfield (led 3% of runs) | runs in data 12 | last 3: 13 Oct Wolverhampton Flat 7.2f Standard 1/9; 27 Oct Wolverhampton (AW) Flat 7f Standard 5/11 fig 43; 24 Nov Lingfield (AW) Flat 7f Standard 12/13 fig 34
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 43, 6 lb below field average; Trainer 0 wins from 14 runs, last 14 days
- Mickey Mongoose (hrs_30151296) | 6yo G | 126lb | OR 46 | draw 1 | jockey Warren Fentiman | trainer Olly Williams (14d 0/0) | headgear b | last run 27 days | form 400644 | MARKET 4.2% | 09:00 median 19.00 | Matchbook 24.00
    comment: Mickey Mongoose has finished fourth in his last two outings, and he has run over today's trip and going before, but he is yet to win in his last six starts.
    DATA: model 5.9% | style Held up (led 4% of runs) | runs in data 13 | last 3: 28 Sep Wolverhampton Flat 7.2f Standard 6/11; 15 Oct Southwell (AW) Flat 7f Standard 4/11 fig 49; 29 Oct Southwell (AW) Flat 7f Standard 4/13 fig 48
    DATA for: Has won at this trip or further
- Neapolitan (hrs_36484980) | 5yo G | 129lb | OR 49 | draw 6 | jockey Ethan Tindall(3) | trainer Antony Brittain (14d 2/13) | headgear tp | last run 40 days | form 06-775 | MARKET 3.3% | 09:00 median 23.00 | Matchbook 32.00
    comment: The risk is a winless sequence of finishes no better than fifth, while carrying 129 lb from stall 6.
    DATA: model 6.2% | style Held up (led 4% of runs) | runs in data 3 | last 3: 8 Sep Catterick Flat 6f Good To Soft 7/9; 15 Sep Wolverhampton Flat 6.1f Standard 7/12; 16 Oct Newcastle (AW) Flat 7f Standard 5/9 fig 42
    DATA against: Best recent form figure 42, 7 lb below field average; Recent figures 7 lb below its current mark (looks high in the weights)
- She's A Goldigger (hrs_51273369) | 4yo F | 126lb | OR 45 | draw 5 | jockey Olivia Tubb(3) | trainer Mark Walford (14d 2/7) | headgear - | last run 27 days | form 530786 | MARKET 2.7% | 09:00 median 23.00 | Matchbook 50.00
    comment: She's A Goldigger is hard to fancy, having finished sixth, eighth and seventh in her last three outings and remaining winless in her last six, with a third five starts back her best recent effort. She has run over today's trip and going, but that is about the only positive.
    DATA: model 4.0% | style Midfield (led 3% of runs) | runs in data 8 | last 3: 8 Sep Catterick Flat 7f Good To Soft 7/11; 16 Sep Beverley Flat 8.5f Good 8/10; 29 Oct Southwell (AW) Flat 7f Standard 6/13 fig 43
    DATA for: Trainer 29% wins (2/7), last 14 days
    DATA against: Best recent form figure 43, 6 lb below field average; Poor recent finishing positions
- Breeze Star (hrs_55061853) | 3yo G | 125lb | OR 42 | draw 2 | jockey Alex Jary | trainer Linda Perratt (14d 1/5) | headgear - | last run 77 days | form -87894 | MARKET 2.4% | 09:00 median 24.50 | Matchbook 60.00
    comment: Winless in his last five, Breeze Star was a fourth last time out but had finished eighth, seventh, eighth and ninth before that, and a 77-day break adds to the doubts.
    DATA: model 2.5% | style Held up (led 3% of runs) | runs in data 5 | last 3: 25 Jul Newcastle Flat 5f Standard To Slow 8/10; 24 Aug Musselburgh Flat 5f Good 9/10; 9 Sep Redcar Flat 6f Good 4/16
    DATA for: Trainer 20% wins (1/5), last 14 days; Last-run finishing speed +3.2% vs that field (finished strongly)
    DATA against: Official rating 42, 6 lb below field average
- Poet (hrs_25908855) | 7yo G | 126lb | OR 37 | draw 4 | jockey Christian Howarth | trainer Scott Dixon (14d 0/10) | headgear p | last run 126 days | form 097790 | MARKET 1.4% | 09:00 median 51.00 | Matchbook 120.00
    comment: Poet is hard to fancy, unplaced last time and beaten in every one of his last six runs, with a ninth, two sevenths and another ninth before that, and he returns after 126 days off.
    DATA: model 1.0% | style Prominent (led 23% of runs) | runs in data 10 | last 3: 7 Jul Brighton Flat 6f Good To Firm 7/11; 16 Jul Chepstow Flat 7.1f Good To Firm 9/12; 22 Jul Lingfield Flat 7f Good To Firm 10/12
    DATA against: Official rating 37, 11 lb below field average; Trainer 0 wins from 10 runs, last 14 days; Last-run finishing speed -2.1% vs that field (faded); Poor recent finishing positions; Returns from a 126-day break

## 6:30 Newcastle (AW) | race_id rac_32305837473 | All-Weather Championship Season 14 Has Begun Apprentice Handicap Stakes (Div II)
Flat | Class 6 | 7f14y | going Standard | AW | 13 runners | rating band 0-55 | age 3yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Victory Sound (hrs_39961719) | 4yo G | 132lb | OR 52 | draw 13 | jockey Rhys Elliott | trainer Mark Usher (14d 0/5) | headgear - | last run 4 days | form 215326 | MARKET 17.9% | 09:00 median 4.50 | Matchbook 5.00 | CHECK (skip line 4.27)
    comment: Victory Sound was sixth last time out, though he's been in the frame with a second two starts back and a third three starts back, and he has run over today's trip and going before.
    DATA: model 16.2% | style Midfield (led 3% of runs) | runs in data 11 | last 3: 2 Oct Newcastle Flat 7.1f Standard 3/13; 30 Oct Newcastle (AW) Flat 7f Standard 2/10 fig 56; 21 Nov Lingfield (AW) Flat 8f Standard 6/11 fig 49
    DATA for: Best recent form figure 56, 9 lb above field average; Recent figures 4 lb above its current mark (looks well handicapped); Good recent finishing positions
- Gressington (hrs_37026010) | 5yo G | 135lb | OR 55 | draw 5 | jockey Tom Kiely-Marshall | trainer Julie Camacho (14d 1/11) | headgear h (1st time) | last run 36 days | form 474540 | MARKET 17.2% | 09:00 median 5.00 | Matchbook 5.00
    comment: Gressington has been consistent without a win, with a fourth two starts back and another fourth six runs ago, and he has run over today's trip and going.
    DATA: model 10.2% | style Midfield (led 4% of runs) | runs in data 13 | last 3: 5 Sep Newcastle Flat 7.1f Standard 5/9; 1 Oct Newcastle Flat 8f Standard 4/8; 20 Oct Newcastle (AW) Flat 7f Standard 12/14 fig 47
    DATA for: Official rating 55, 7 lb above field average; First-time headgear
    DATA against: Recent figures 8 lb below its current mark (looks high in the weights); Carries 6 lb more than average
- Joud (hrs_59059259) | 3yo F | 133lb | OR 54 | draw 6 | jockey Jack Callan | trainer Edward Bethell (14d 0/9) | headgear - | last run 25 days | form -45263 | MARKET 11.7% | 09:00 median 6.50 | Matchbook 8.00
    comment: Joud has been consistent without a win, finishing third last time out and a second three starts back, and she has run over today's trip and going before.
    DATA: model 16.7% | style Midfield (led 4% of runs) | runs in data 5 | last 3: 21 Sep Wolverhampton Flat 7.2f Standard 2/10; 15 Oct Southwell (AW) Flat 8f Standard 6/14 fig 53; 31 Oct Southwell (AW) Flat 8f Standard 3/12 fig 53
    DATA for: Best recent form figure 53, 6 lb above field average; Official rating 54, 6 lb above field average; Good recent finishing positions
    DATA against: Trainer 0 wins from 9 runs, last 14 days
- Sovereign Class (hrs_48818924) | 4yo F | 128lb | OR 48 | draw 4 | jockey Ryan Kavanagh | trainer Grant Tuer (14d 0/6) | headgear - | last run 27 days | form 360062 | MARKET 11.3% | 09:00 median 6.50 | Matchbook 8.40
    comment: Sovereign Class was a second last time out and has run over today's trip and on this going, but she is yet to win in her last six starts and has finished sixth twice in that spell.
    DATA: model 4.7% | style Midfield (led 3% of runs) | runs in data 6 | last 3: 9 Sep Redcar Flat 6f Good 12/16; 21 Sep Hamilton Flat 6f Soft 6/7; 29 Oct Southwell (AW) Flat 7f Standard 2/12 fig 62
    DATA for: Best recent form figure 62, 15 lb above field average; Recent figures 14 lb above its current mark (looks well handicapped)
- Coulsty Exchange (hrs_60977231) | 4yo F | 129lb | OR 49 | draw 8 | jockey Cara Tuke(7) | trainer Iain Jardine (14d 0/9) | headgear t | wind surgery | last run 27 days | form 736625 | MARKET 11.2% | 09:00 median 7.00 | Matchbook 8.20
    comment: The risk is that she is yet to win in her last six, and a fifth last time out leaves her to prove she can get her head in front.
    DATA: model 12.4% | style Midfield (led 3% of runs) | runs in data 6 | last 3: 2 Oct Newcastle Flat 6f Standard 6/10; 16 Oct Newcastle (AW) Flat 7f Standard 2/9 fig 52; 29 Oct Southwell (AW) Flat 7f Standard 5/13 fig 48
    DATA for: Best recent form figure 52, 5 lb above field average
    DATA against: Trainer 0 wins from 9 runs, last 14 days
- Yaaser (hrs_22439851) | 8yo G | 131lb | OR 51 | draw 3 | jockey Lauren Young(3) | trainer Jim Goldie (14d 1/14) | headgear - | last run 2 days | form 883950 | MARKET 9.5% | 09:00 median 7.50 | Matchbook 10.50
    comment: The risk is a quick return just two days after an unplaced effort, with 131 lb to carry from stall three.
    DATA: model 9.7% | style Held up (led 4% of runs) | runs in data 16 | last 3: 30 Oct Newcastle (AW) Flat 10f Standard 9/14 fig 43; 6 Nov Newcastle (AW) Flat 8f Standard 5/14 fig 50; 23 Nov Newcastle (AW) Flat 6f Standard 11/13 fig 35
    DATA against: Aged 8, older than most of this field; Pace: steady gallop likely, hard to come from off the pace
- Mister Sky Blue (hrs_43605611) | 4yo G | 126lb | OR 45 | draw 10 | jockey Laura Coughlan | trainer Gemma Tutty (14d 1/6) | headgear - | last run 27 days | form 344444 | MARKET 6.1% | 09:00 median 12.50 | Matchbook 15.50
    comment: Mister Sky Blue arrives consistent, with five straight fourths since a third six starts back, and he has run over today's trip and going before.
    DATA: model 5.6% | style Prominent (led 5% of runs) | runs in data 12 | last 3: 8 Sep Catterick Flat 7f Good To Soft 4/11; 30 Sep Catterick Flat 6f Good 4/10; 29 Oct Southwell (AW) Flat 7f Standard 4/12 fig 58
    DATA for: Best recent form figure 58, 11 lb above field average; Recent figures 13 lb above its current mark (looks well handicapped)
- Spirited Dancer (hrs_39060392) | 4yo F | 126lb | OR 46 | draw 1 | jockey Myla Coppins(5) | trainer Tony Carroll (14d 2/36) | headgear - | last run 36 days | form 862555 | MARKET 4.7% | 09:00 median 14.00 | Matchbook 25.00
    comment: Spirited Dancer has finished fifth in each of her last three outings, with a second four starts back her best effort, and she has run over today's trip and going before.
    DATA: model 8.2% | style Held up (led 4% of runs) | runs in data 12 | last 3: 13 Sep Bath Flat 5f Good To Soft 5/13; 2 Oct Wolverhampton Flat 5.1f Standard 5/11; 20 Oct Newcastle (AW) Flat 5f Standard 5/10 fig 43
    DATA against: Best recent form figure 43, 4 lb below field average; Pace: steady gallop likely, hard to come from off the pace
- Yaahobby (hrs_24735053) | 7yo G | 128lb | OR 48 | draw 9 | jockey Ethan Tindall(3) | trainer Antony Brittain (14d 2/13) | headgear t | last run 8 days | form 913947 | MARKET 3.2% | 09:00 median 23.00 | Matchbook 32.00
    comment: He has run over this trip and on this going and is race-fit after eight days, but that's thin support from stall nine.
    DATA: model 7.1% | style Held up (led 4% of runs) | runs in data 12 | last 3: 12 Oct Newcastle Flat 6f Standard 9/12; 2 Nov Wolverhampton (AW) Flat 6f Standard 4/10 fig 47; 17 Nov Southwell (AW) Flat 7f Standard 7/11 fig 40
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Toy Soldier (hrs_39961607) | 4yo G | 127lb | OR 47 | draw 2 | jockey Lexie Clarkson(7) | trainer Lucinda Russell & Michael Scudamore (14d 1/19) | headgear - | last run 40 days | form 875588 | MARKET 2.2% | 09:00 median 29.00 | Matchbook 65.00
    comment: Toy Soldier has finished eighth in his last two outings and is yet to win in his last six, though he has run over today's trip and on this going before.
    DATA: model 4.6% | style Held up (led 4% of runs) | runs in data 12 | last 3: 21 Sep Hamilton Flat 8.3f Soft 5/7; 29 Sep Ayr Flat 7.2f Heavy 8/11; 16 Oct Newcastle (AW) Flat 7f Standard 8/8 fig 28
    DATA against: Best recent form figure 28, 19 lb below field average; Recent figures 19 lb below its current mark (looks high in the weights); Pace: steady gallop likely, hard to come from off the pace
- Ganthorpe (hrs_58347884) | 3yo G | 125lb | OR 44 | draw 12 | jockey Finlay Bassett(7) | trainer Michael & David Easterby (14d 1/7) | headgear - | last run 63 days | form 777009 | MARKET 1.8% | 09:00 median 34.00 | Matchbook 75.00
    comment: Ganthorpe is winless in his last six, finishing ninth last time out 63 days ago, and has been seventh at best when placed in that spell.
    DATA: model 2.0% | style Prominent (led 8% of runs) | runs in data 13 | last 3: 12 Aug Beverley Flat 7.3f Good To Firm 10/13; 14 Sep Thirsk Flat 6f Good 10/11; 23 Sep Redcar Flat 7f Good 9/12
    DATA against: Poor recent finishing positions
- Billyjoegold (hrs_62779318) | 4yo G | 126lb | OR 44 | draw 11 | jockey Taryn Langley | trainer Ruth Carr (14d 2/10) | headgear - | last run 162 days | form 309700 | MARKET 1.8% | 09:00 median 41.00 | Matchbook 80.00
    comment: Billyjoegold is winless in his last six, with three unplaced efforts and a seventh and ninth in that spell, and he returns after 162 days off.
    DATA: model 1.1% | style Midfield (led 3% of runs) | runs in data 6 | last 3: 21 May Southwell Flat 7.1f Standard 7/9; 2 Jun Newcastle Flat 8f Standard 13/13; 16 Jun Beverley Flat 7.4f Good 13/14
    DATA for: Trainer 20% wins (2/10), last 14 days
    DATA against: Poor recent finishing positions; Returns from a 162-day break
- My Mate Beattie (hrs_39962209) | 4yo F | 126lb | OR 42 | draw 7 | jockey Christian Howarth | trainer Scott Dixon (14d 0/10) | headgear v | last run 41 days | form 357000 | MARKET 1.4% | 09:00 median 41.00 | Matchbook 100.00
    comment: Unplaced in her last three and without a win in her last six, My Mate Beattie is hard to fancy, though she has run over today's trip and going and a third six starts back is her best recent finish.
    DATA: model 1.6% | style Held up (led 3% of runs) | runs in data 12 | last 3: 19 Sep Newcastle Flat 6f Standard 10/10; 28 Sep Wolverhampton Flat 7.2f Standard 10/11; 15 Oct Southwell (AW) Flat 7f Standard 10/13 fig 26
    DATA against: Best recent form figure 26, 21 lb below field average; Recent figures 16 lb below its current mark (looks high in the weights); Official rating 42, 6 lb below field average; Trainer 0 wins from 10 runs, last 14 days; Poor recent finishing positions; Pace: steady gallop likely, hard to come from off the pace
