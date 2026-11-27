# Card review packet: Dundalk (AW), 2026-11-27

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
{"meeting": "dundalk_aw", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 5:30 Dundalk (AW) | race_id rac_32305843284 | BAR 1 Casino Claiming Race
Flat |  | 0m7f0y | going Standard | AW | 9 runners | rating band - | age 2yo
DATA pace: Unclear - Running styles known for only 4 of 9 runners.
- Chicago Caray (hrs_17391961069) | 2yo G | 128lb | OR 76 | draw 5 | jockey Ben Coen | trainer J. P. Murtagh (14d 2/7) | headgear b | last run 16 days | form 848 | MARKET 29.4% | 09:00 median 3.00 | Matchbook 2.96 | CHECK (skip line 2.85)
    comment: Chicago Caray has run over today's trip and on this going, and he returns just 16 days after an eighth last time out, with a fourth two starts back his best recent effort.
    DATA: model 14.8% | style Unknown | runs in data 3 | last 3: 9 Oct Dundalk Flat 7f Standard 8/14; 28 Oct Dundalk (AW) (IRE) Flat 7f Standard 4/11 fig 60; 11 Nov Dundalk (AW) (IRE) Flat 7f Standard 8/14 fig 63
    DATA for: Best recent form figure 63, 14 lb above field average; Trainer 29% wins (2/7), last 14 days
- Rejoinder (hrs_65451442) | 2yo G | 123lb | OR 74 | draw 2 | jockey Leigh Roche | trainer Robson De Aguiar (14d 1/8) | headgear - | last run 7 days | form 94287 | MARKET 18.4% | 09:00 median 3.75 | Matchbook 6.40
    comment: Rejoinder is quick back after seven days and has run over today's trip and going, with a second three starts back his best finish in a winless recent spell.
    DATA: model 34.4% | style Midfield (led 4% of runs) | runs in data 5 | last 3: 20 Oct Curragh (IRE) Flat 6f Yielding 2/13 fig 64; 30 Oct Dundalk (AW) (IRE) Flat 5f Standard 8/13 fig 42; 20 Nov Dundalk (AW) (IRE) Flat 5f Standard 7/9 fig 65
    DATA for: Best recent form figure 65, 16 lb above field average
    DATA against: Last-run finishing speed -2.1% vs that field (faded)
- Pal Of Mine (hrs_17396157058) | 2yo C | 120lb | OR - | draw 4 | jockey W. M. Lordan | trainer Emmet Mullins (14d 3/11) | headgear - | last run - days | form - | MARKET 17.9% | 09:00 median 4.95 | Matchbook 4.90
    comment: Pal Of Mine is an unexposed colt with no recorded form, so this looks a debut outing and there's plenty of scope for improvement. He carries 120 lb from stall four.
    DATA: model 6.7% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 27% wins (3/11), last 14 days
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Let Me Free (hrs_17391825479) | 2yo F | 123lb | OR - | draw 3 | jockey Robert Whearty | trainer Gavin Cromwell (14d 4/41) | headgear - | last run 30 days | form 06 | MARKET 7.1% | 09:00 median 11.00 | Matchbook 16.50
    DATA: model 7.3% | style Midfield (led 8% of runs) | runs in data 2 | last 3: 17 Sep Naas Flat 7f Yielding 11/15; 28 Oct Dundalk (AW) (IRE) Flat 6f Standard 6/13 fig 41
    DATA against: Best recent form figure 41, 8 lb below field average; Lightly raced: 2 runs in our data, so the model has little to go on
- Present Perfect (hrs_17396158101) | 2yo F | 128lb | OR - | draw 8 | jockey Keithen Kennedy(5) | trainer Mrs J. Harrington (14d 0/8) | headgear - | last run - days | form - | MARKET 7.0% | 09:00 median 13.00 | Matchbook 13.00
    comment: Present Perfect is an unraced filly with no form to go on, so she is totally unexposed and open to any amount of improvement. She carries 128 lb from stall eight on debut.
    DATA: model 6.8% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Trainer 0 wins from 8 runs, last 14 days; Lightly raced: 0 runs in our data, so the model has little to go on
- In Sequence (hrs_17394340152) | 2yo C | 123lb | OR - | draw 6 | jockey Rory Mulligan(5) | trainer Alan McIntyre (14d 0/1) | headgear tp (1st time) | last run 35 days | form 0 | MARKET 7.0% | 09:00 median 12.00 | Matchbook 13.00
    comment: The main risk is that he was unplaced last time and remains yet to win in recent form.
    DATA: model 4.8% | style Unknown | runs in data 1 | last 3: 23 Oct Dundalk (AW) (IRE) Flat 8f Standard 10/14 fig 51
    DATA for: First-time headgear
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Waysong (hrs_17393665331) | 2yo G | 120lb | OR - | draw 1 | jockey Wesley Joyce | trainer Diego Dias (14d 0/0) | headgear b (1st time) | last run 14 days | form 58 | MARKET 5.3% | 09:00 median 15.00 | Matchbook 18.50
    comment: On the plus side, he is fresh enough after 14 days and has run over today's trip and on this going.
    DATA: model 7.3% | style Unknown | runs in data 2 | last 3: 11 Oct Naas Flat 5.9f Soft 5/7; 13 Nov Dundalk (AW) (IRE) Flat 6f Standard 8/11 fig 44
    DATA for: First-time headgear
    DATA against: Best recent form figure 44, 5 lb below field average; Lightly raced: 2 runs in our data, so the model has little to go on
- Chachaboo (hrs_17395562548) | 2yo C | 120lb | OR - | draw 9 | jockey Chris Hayes | trainer Gavin Cromwell (14d 4/41) | headgear - | last run 9 days | form 0 | MARKET 5.0% | 09:00 median 17.00 | Matchbook 18.50
    comment: The main risk is that he was unplaced last time out and is yet to win in recent form.
    DATA: model 9.9% | style Held up (led 8% of runs) | runs in data 1 | last 3: 18 Nov Dundalk (AW) (IRE) Flat 7f Standard 11/14 fig 47
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Victorious Star (hrs_17395783664) | 2yo G | 133lb | OR - | draw 7 | jockey J M Sheridan | trainer Joseph Patrick O'Brien (14d 4/35) | headgear - | last run 2 days | form 00 | MARKET 2.8% | 09:00 median 26.00 | Matchbook 50.00
    comment: He has at least run over today's trip and going before.
    DATA: model 8.1% | style Held up (led 5% of runs) | runs in data 2 | last 3: 20 Nov Dundalk (AW) (IRE) Flat 8f Standard 13/13 fig 28; 25 Nov Dundalk (AW) (IRE) Flat 7f Standard 11/14 fig 33
    DATA against: Best recent form figure 33, 16 lb below field average; Lightly raced: 2 runs in our data, so the model has little to go on

## 6:00 Dundalk (AW) | race_id rac_32305845221 | Irish Stallion Farms EBF Fillies Maiden
Flat |  | 0m6f0y | going Standard | AW | 17 runners | rating band - | age 2yo
DATA pace: Unclear - Running styles known for only 3 of 17 runners.
- Kodiak Gold (hrs_17396162273) | 2yo F | 128lb | OR - | draw 6 | jockey J M Sheridan | trainer Joseph Patrick O'Brien (14d 4/35) | headgear - | last run - days | form - | MARKET 13.1% | 09:00 median 5.50 | Matchbook 6.20 | CHECK (skip line 5.22)
    DATA: model 5.2% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Moyanna Castle (hrs_17390841930) | 2yo F | 128lb | OR - | draw 4 | jockey Rory Mulligan(5) | trainer Jamie Heavey (14d 0/0) | headgear - | last run 23 days | form 92 | MARKET 12.7% | 09:00 median 5.50 | Matchbook 6.20
    DATA: model 16.5% | style Unknown | runs in data 2 | last 3: 15 Aug Dundalk Flat 6f Standard 9/14; 4 Nov Dundalk (AW) (IRE) Flat 6f Standard 2/11 fig 55
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Ria's Angel (hrs_17393965715) | 2yo F | 128lb | OR - | draw 7 | jockey Ben Coen | trainer Mark Fahey (14d 1/6) | headgear - | last run 21 days | form 94 | MARKET 11.0% | 09:00 median 5.00 | Matchbook 9.00
    DATA: model 4.4% | style Midfield (led 8% of runs) | runs in data 2 | last 3: 17 Oct Leopardstown (IRE) Flat 7f Good 9/13 fig 43; 6 Nov Dundalk (AW) (IRE) Flat 7f Standard 4/12 fig 61
    DATA for: Best recent form figure 61, 10 lb above field average
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Chesham (hrs_63810215) | 2yo F | 128lb | OR - | draw 5 | jockey  | trainer Robson De Aguiar (14d 1/8) | headgear - | last run 196 days | form 7 | MARKET 11.0% | 09:00 median 5.50 | Matchbook 8.40
    DATA: model 5.3% | style Unknown | runs in data 1 | last 3: 15 May Leopardstown Flat 7f Good 7/7
    DATA against: Returns from a 196-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Bedouin Star (hrs_64555708) | 2yo F | 128lb | OR - | draw 3 | jockey Chris Hayes | trainer Donnacha Aidan O'Brien (14d 0/0) | headgear - | last run - days | form - | MARKET 7.9% | 09:00 median 10.00 | Matchbook 9.80
    DATA: model 5.2% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Musical Gems (hrs_17396163316) | 2yo F | 128lb | OR - | draw 14 | jockey Robert Whearty | trainer G. M. Lyons (14d 0/2) | headgear - | last run - days | form - | MARKET 7.3% | 09:00 median 10.00 | Matchbook 10.50
    DATA: model 5.2% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Thosegirlsdontplay (hrs_17396169574) | 2yo F | 128lb | OR - | draw 8 | jockey Declan McDonogh | trainer Joseph Patrick O'Brien (14d 4/35) | headgear - | last run - days | form - | MARKET 6.3% | 09:00 median 10.00 | Matchbook 14.50
    DATA: model 5.2% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Raziyya (hrs_17395960974) | 2yo F | 128lb | OR - | draw 9 | jockey Donagh O'Connor | trainer Robson De Aguiar (14d 1/8) | headgear - | last run - days | form - | MARKET 5.8% | 09:00 median 13.00 | Matchbook 14.50
    DATA: model 5.2% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Swietenia (hrs_17396168531) | 2yo F | 128lb | OR - | draw 1 | jockey W. M. Lordan | trainer Robson De Aguiar (14d 1/8) | headgear v (1st time) | last run - days | form - | MARKET 5.5% | 09:00 median 12.00 | Matchbook 16.50
    DATA: model 5.2% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: First-time headgear
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Who's Liby (hrs_17396170617) | 2yo F | 128lb | OR - | draw 17 | jockey Nicola Burns(5) | trainer G. M. Lyons (14d 0/2) | headgear - | last run - days | form - | MARKET 4.1% | 09:00 median 15.00 | Matchbook 24.00
    DATA: model 5.2% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Solar Palace (hrs_17395792008) | 2yo F | 128lb | OR - | draw 2 | jockey Seamie Heffernan | trainer Joseph Patrick O'Brien (14d 4/35) | headgear - | last run 2 days | form 9 | MARKET 3.6% | 09:00 median 17.00 | Matchbook 26.00
    DATA: model 9.7% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 25 Nov Dundalk (AW) (IRE) Flat 7f Standard 9/14 fig 38
    DATA against: Best recent form figure 38, 13 lb below field average; Lightly raced: 1 run in our data, so the model has little to go on
- Castledown (hrs_17396160187) | 2yo F | 128lb | OR - | draw 12 | jockey Adam Caffrey | trainer Daniel James Murphy (14d 1/7) | headgear - | last run - days | form - | MARKET 2.5% | 09:00 median 34.00 | Matchbook 32.00
    DATA: model 5.2% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Pop It Pebbles (hrs_17396167488) | 2yo F | 128lb | OR - | draw 15 | jockey Leigh Roche | trainer Paul W Flynn (14d 0/4) | headgear - | last run - days | form - | MARKET 2.3% | 09:00 median 34.00 | Matchbook 40.00
    DATA: model 5.2% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Aztec Moon (hrs_17396159144) | 2yo F | 128lb | OR - | draw 11 | jockey R. P. Cleary | trainer Ms Claire O'Connell (14d 1/5) | headgear - | last run - days | form - | MARKET 2.2% | 09:00 median 34.00 | Matchbook 42.00
    DATA: model 5.2% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 20% wins (1/5), last 14 days
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Parvenue Fling (hrs_17396165402) | 2yo F | 128lb | OR - | draw 13 | jockey  | trainer Eddie & Patrick Harty (14d 0/2) | headgear - | last run - days | form - | MARKET 2.1% | 09:00 median 34.00 | Matchbook 46.00
    DATA: model 5.2% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Faymiss (hrs_17396161230) | 2yo F | 128lb | OR - | draw 10 | jockey Wesley Joyce | trainer Patrick Michael Verling (14d 0/1) | headgear - | last run - days | form - | MARKET 1.5% | 09:00 median 67.00 | Matchbook 48.00
    DATA: model 5.2% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Sadie Rose (hrs_17390842973) | 2yo F | 128lb | OR - | draw 16 | jockey  | trainer F G Hand (14d 0/1) | headgear t | last run 71 days | form 000 | MARKET 1.0% | 09:00 median 126.00 | Matchbook 46.00
    DATA: model 2.0% | style Midfield (led 5% of runs) | runs in data 3 | last 3: 15 Aug Dundalk Flat 6f Standard 12/14; 23 Aug Naas Flat 5.9f Good 14/15; 17 Sep Naas Flat 5.9f Yielding 16/21
    DATA against: Last-run finishing speed -4.0% vs that field (faded); Poor recent finishing positions

## 6:30 Dundalk (AW) | race_id rac_32305847158 | Campbell & Haughey Solicitors Nursery Handicap
Flat |  | 0m6f0y | going Standard | AW | 8 runners | rating band 0-60 | age 2yo
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Invincible Irish (hrs_17389030239) | 2yo G | 138lb | OR 60 | draw 2 | jockey Ben Coen | trainer Daniel McLoughlin (14d 2/8) | headgear - | last run 7 days | form 074223 | MARKET 50.1% | 09:00 median 1.80 | Matchbook 1.71
    comment: Invincible Irish arrives in good heart, third last time out and a second two and three starts back, and he's back quickly after just seven days with experience of today's trip and going.
    DATA: model 40.8% | style Midfield (led 4% of runs) | runs in data 7 | last 3: 28 Sep Down Royal Flat 5f Good To Yielding 2/6; 11 Nov Dundalk (AW) (IRE) Flat 6f Standard 2/8 fig 71; 20 Nov Dundalk (AW) (IRE) Flat 5f Standard 3/9 fig 61
    DATA for: Best recent form figure 71, 30 lb above field average; Recent figures 11 lb above its current mark (looks well handicapped); Official rating 60, 10 lb above field average; Trainer 25% wins (2/8), last 14 days; Good recent finishing positions
    DATA against: Carries 9 lb more than average
- Tina Tereshkova (hrs_65225111) | 2yo F | 119lb | OR 38 | draw 4 | jockey Nina Doherty(10) | trainer Andrew Kinirons (14d 0/1) | headgear - | last run 9 days | form 960075 | MARKET 13.5% | 09:00 median 6.00 | Matchbook 7.00
    comment: Tina Tereshkova is winless in her last six, though a fifth last time out, just nine days ago, is her best recent effort, and she has run over today's trip and going before.
    DATA: model 10.0% | style Midfield (led 3% of runs) | runs in data 7 | last 3: 17 Sep Naas Flat 8f Yielding 11/13; 19 Oct Gowran Park (IRE) Flat 7f Yielding 7/12 fig 38; 18 Nov Dundalk (AW) (IRE) Flat 7f Standard 5/12 fig 40
    DATA for: Carries 10 lb less than average
    DATA against: Official rating 38, 12 lb below field average
- Scarlet Dream (hrs_65225090) | 2yo F | 133lb | OR 55 | draw 5 | jockey Adam Caffrey | trainer Adrian McGuinness (14d 0/17) | headgear v (1st time) | last run 14 days | form 945766 | MARKET 11.2% | 09:00 median 6.00 | Matchbook 10.50
    comment: The risk is a winless run in her last six, with a sixth last time out and another sixth before that.
    DATA: model 11.9% | style Midfield (led 5% of runs) | runs in data 7 | last 3: 2 Oct Dundalk Flat 7f Standard 7/9; 4 Nov Dundalk (AW) (IRE) Flat 7f Standard 6/7 fig 52; 13 Nov Dundalk (AW) (IRE) Flat 8f Standard 6/6 fig 45
    DATA for: Best recent form figure 52, 11 lb above field average; First-time headgear
    DATA against: Trainer 0 wins from 17 runs, last 14 days; Poor recent finishing positions
- Stellar Path (hrs_64846803) | 2yo F | 128lb | OR 50 | draw 1 | jockey R. P. Cleary | trainer Kieran P Cotter (14d 0/0) | headgear - | last run 71 days | form 988908 | MARKET 7.8% | 09:00 median 11.00 | Matchbook 12.50
    comment: The risk is a 71-day absence and a run of unplaced efforts.
    DATA: model 12.6% | style Prominent (led 29% of runs) | runs in data 6 | last 3: 5 Aug Sligo Flat 6f Yielding 9/12; 16 Aug Curragh Flat 5f Good 10/10; 17 Sep Naas Flat 5f Yielding 8/14
    DATA against: Poor recent finishing positions
- Sorrento Sunset (hrs_17391301893) | 2yo F | 129lb | OR 51 | draw 3 | jockey Conor Cusack(7) | trainer Daniel McLoughlin (14d 2/8) | headgear - | last run 7 days | form 06996 | MARKET 7.5% | 09:00 median 11.00 | Matchbook 13.00
    comment: Sorrento Sunset is winless in her last five, with a sixth last time out and a ninth two starts back, but she is quick back after seven days and has run over today's trip and going.
    DATA: model 13.0% | style Held up (led 3% of runs) | runs in data 5 | last 3: 29 Sep Cork Flat 5f Soft 9/12; 18 Nov Dundalk (AW) (IRE) Flat 7f Standard 9/12 fig 47; 20 Nov Dundalk (AW) (IRE) Flat 5f Standard 6/9 fig 43
    DATA for: Best recent form figure 47, 6 lb above field average; Trainer 25% wins (2/8), last 14 days; Last-run finishing speed +3.5% vs that field (finished strongly)
    DATA against: Poor recent finishing positions; Pace: steady gallop likely, hard to come from off the pace
- No Time Faults (hrs_64102423) | 2yo F | 133lb | OR 55 | draw 6 | jockey Nestor Kashuba(10) | trainer Kevin Thomas Coleman (14d 1/5) | headgear p (1st time) | last run 92 days | form 60008 | MARKET 4.7% | 09:00 median 19.00 | Matchbook 20.00
    comment: The risk is a poor run of form, with an eighth last time out and 92 days off, and she is yet to win in her last five starts.
    DATA: model 4.1% | style Held up (led 3% of runs) | runs in data 5 | last 3: 24 Jul Cork Flat 5f Good To Firm 10/10; 5 Aug Sligo Flat 6f Yielding 11/12; 27 Aug Navan Flat 5.8f Good 8/8
    DATA for: Trainer 20% wins (1/5), last 14 days; First-time headgear
    DATA against: Last-run finishing speed -2.7% vs that field (faded); Poor recent finishing positions; Returns from a 92-day break; Pace: steady gallop likely, hard to come from off the pace
- Mirissa Beach (hrs_66494176) | 2yo F | 131lb | OR 53 | draw 7 | jockey Robbie Colgan | trainer Chris Timmons (14d 0/0) | headgear - | last run 23 days | form 080 | MARKET 3.6% | 09:00 median 17.00 | Matchbook 48.00
    comment: Mirissa Beach is winless in her last three, unplaced last time, eighth two starts back and unplaced three starts back, so she is hard to fancy off 131 lb from draw 7.
    DATA: model 5.0% | style Midfield (led 8% of runs) | runs in data 3 | last 3: 5 Sep Navan Flat 5.8f Good 13/13; 28 Oct Dundalk (AW) (IRE) Flat 6f Standard 8/13 fig 31; 4 Nov Dundalk (AW) (IRE) Flat 6f Standard 10/11 fig 37
    DATA against: Best recent form figure 37, 4 lb below field average; Recent figures 16 lb below its current mark (looks high in the weights); Poor recent finishing positions
- Chiquitita Bee (hrs_64812776) | 2yo F | 120lb | OR 42 | draw 8 | jockey Chris Hayes | trainer Adrian McGuinness (14d 0/17) | headgear t | last run 9 days | form 90000 | MARKET 1.7% | 09:00 median 41.00 | Matchbook 80.00
    comment: Chiquitita Bee is winless in her last five, unplaced in each of her last four and a ninth five starts back, so she is hard to fancy, though she has run over today's trip and going before and is back quickly after nine days.
    DATA: model 2.7% | style Held up (led 4% of runs) | runs in data 5 | last 3: 18 Jun Leopardstown Flat 7.2f Good To Firm 10/10; 11 Jul Navan Flat 5.8f Good 16/17; 18 Nov Dundalk (AW) (IRE) Flat 7f Standard 12/12 fig 0
    DATA for: Carries 9 lb less than average
    DATA against: Best recent form figure 0, 41 lb below field average; Recent figures 42 lb below its current mark (looks high in the weights); Official rating 42, 8 lb below field average; Trainer 0 wins from 17 runs, last 14 days; Poor recent finishing positions; Pace: steady gallop likely, hard to come from off the pace

## 7:00 Dundalk (AW) | race_id rac_32305849095 | Killowen Contracts Handicap
Flat |  | 0m6f0y | going Standard | AW | 16 runners | rating band - | age 3yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Go Athletico (hrs_21666736) | 8yo G | 142lb | OR 72 | draw 7 | jockey Camillus Byrne(10) | trainer Adrian McGuinness (14d 0/17) | headgear tp | last run 23 days | form 004982 | MARKET 11.6% | 09:00 median 6.50 | Matchbook 7.00 | CHECK (skip line 6.17)
    DATA: model 7.8% | style Midfield (led 4% of runs) | runs in data 16 | last 3: 15 Oct Curragh (IRE) Flat 6f Soft 9/13 fig 68; 20 Oct Curragh (IRE) Flat 6f Yielding 8/17 fig 73; 4 Nov Dundalk (AW) (IRE) Flat 6f Standard 2/8 fig 66
    DATA for: Best recent form figure 73, 11 lb above field average; Official rating 72, 6 lb above field average; Last-run finishing speed +3.0% vs that field (finished strongly)
    DATA against: Trainer 0 wins from 17 runs, last 14 days; Carries 6 lb more than average; Aged 8, older than most of this field
- My Cubby Bear (hrs_55211184) | 3yo F | 143lb | OR 73 | draw 3 | jockey Adam Grant(7) | trainer Henry de Bromhead (14d 8/45) | headgear - | last run 51 days | form 628-23 | MARKET 10.1% | 09:00 median 6.00 | Matchbook 9.40
    comment: My Cubby Bear arrives in solid shape, third last time out and second two starts back, and she has run over today's trip and going before.
    DATA: model 22.2% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 29 Sep Cork Flat 6f Soft 2/8; 7 Oct Navan Flat 5.8f Yielding 3/13
    DATA for: Official rating 73, 7 lb above field average; Good recent finishing positions
    DATA against: Carries 7 lb more than average; Lightly raced: 2 runs in our data, so the model has little to go on
- Carrigans Grove (hrs_42912933) | 5yo M | 131lb | OR 61 | draw 2 | jockey Robyn Donaghue-Leahy(7) | trainer Patrick J Flynn (14d 2/6) | headgear b | last run 16 days | form 034515 | MARKET 9.8% | 09:00 median 7.00 | Matchbook 8.80
    comment: Carrigans Grove was a fifth last time out, 16 days ago, after a win two starts back, and she has run over today's trip and going before.
    DATA: model 7.2% | style Held up (led 8% of runs) | runs in data 11 | last 3: 21 Oct Navan (IRE) Flat 6f Yielding 5/21 fig 61; 4 Nov Dundalk (AW) (IRE) Flat 7f Standard 1/13 fig 63; 11 Nov Dundalk (AW) (IRE) Flat 7f Standard 5/14 fig 60
    DATA for: Trainer 33% wins (2/6), last 14 days; Has won at this trip or further
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Fox In Flight (hrs_57255079) | 3yo G | 144lb | OR 74 | draw 8 | jockey  | trainer David Marnane (14d 1/6) | headgear t | last run 23 days | form 959002 | MARKET 9.6% | 09:00 median 8.00 | Matchbook 7.40
    comment: Fox In Flight comes here on the back of a second last time out, 23 days ago, and has run over today's trip and going, but he is winless in his last six and was unplaced or ninth in three of the four starts before that.
    DATA: model 4.6% | style Midfield (led 5% of runs) | runs in data 9 | last 3: 15 Aug Dundalk Flat 6f Standard 11/12; 9 Sep Cork Flat 6f Good 12/22; 4 Nov Dundalk (AW) (IRE) Flat 6f Standard 2/9 fig 72
    DATA for: Best recent form figure 72, 10 lb above field average; Official rating 74, 8 lb above field average; Last-run finishing speed +2.0% vs that field (finished strongly)
    DATA against: Carries 8 lb more than average
- Alfred Tennyson (hrs_40918633) | 4yo G | 143lb | OR 73 | draw 16 | jockey Mel Sheridan(7) | trainer Denis Gerard Hogan (14d 0/15) | headgear tb | last run 78 days | form 031582 | MARKET 8.3% | 09:00 median 8.00 | Matchbook 10.50
    comment: The main risk is a 78-day absence, so fitness is the question.
    DATA: model 6.2% | style Midfield (led 4% of runs) | runs in data 16 | last 3: 12 Aug Gowran Park Flat 7f Good To Firm 5/7; 27 Aug Navan Flat 5.8f Good 8/9; 10 Sep Laytown Flat 7f Standard 2/10
    DATA for: Official rating 73, 7 lb above field average; Last-run finishing speed +3.0% vs that field (finished strongly); Has won at this trip or further
    DATA against: Trainer 0 wins from 15 runs, last 14 days; Carries 7 lb more than average
- Blue Anthem (hrs_43951131) | 4yo G | 127lb | OR 57 | draw 9 | jockey Adam Caffrey | trainer Adrian McGuinness (14d 0/17) | headgear tv | last run 9 days | form 225844 | MARKET 8.1% | 09:00 median 8.50 | Matchbook 10.00
    comment: Blue Anthem is winless in his last six, though he has been fourth in each of his last two outings, and he has run over today's trip and going.
    DATA: model 5.3% | style Held up (led 8% of runs) | runs in data 13 | last 3: 30 Oct Dundalk (AW) (IRE) Flat 5f Standard 8/14 fig 49; 11 Nov Dundalk (AW) (IRE) Flat 7f Standard 4/14 fig 57; 18 Nov Dundalk (AW) (IRE) Flat 7f Standard 4/14 fig 57
    DATA for: Carries 9 lb less than average
    DATA against: Best recent form figure 57, 5 lb below field average; Official rating 57, 9 lb below field average; Trainer 0 wins from 17 runs, last 14 days; Pace: steady gallop likely, hard to come from off the pace
- Saint Acclaim (hrs_66198846) | 3yo G | 142lb | OR 72 | draw 14 | jockey Seamie Heffernan | trainer Jordan Kidd (14d 0/0) | headgear - | last run 23 days | form 0233 | MARKET 7.5% | 09:00 median 8.00 | Matchbook 13.00
    comment: Saint Acclaim arrives in solid nick, third last time out and third again two starts back, with a second three starts back, and he's fresh enough after 23 days off. He has run over today's trip and going, though he is yet to win in his last four starts.
    DATA: model 13.0% | style Midfield (led 4% of runs) | runs in data 4 | last 3: 25 Sep Dundalk Flat 6f Standard 2/14; 21 Oct Navan (IRE) Flat 5f Yielding 3/9 fig 74; 4 Nov Dundalk (AW) (IRE) Flat 6f Standard 3/8 fig 84
    DATA for: Best recent form figure 84, 22 lb above field average; Recent figures 12 lb above its current mark (looks well handicapped); Official rating 72, 6 lb above field average; Good recent finishing positions
    DATA against: Carries 6 lb more than average
- Thaloria (hrs_52995131) | 4yo F | 133lb | OR 63 | draw 5 | jockey W. M. Lordan | trainer Miss Natalia Lupini (14d 1/9) | headgear p (1st time) | last run 16 days | form 000466 | MARKET 7.4% | 09:00 median 10.00 | Matchbook 10.00
    comment: Thaloria has run over today's trip and going and is fresh enough after 16 days, but she's winless in her last six, with a sixth last time out and another sixth before that.
    DATA: model 3.3% | style Prominent (led 4% of runs) | runs in data 10 | last 3: 28 Sep Down Royal Flat 7.1f Good To Yielding 4/14; 9 Oct Dundalk Flat 7f Standard 6/14; 11 Nov Dundalk (AW) (IRE) Flat 7f Standard 6/14 fig 59
    DATA for: Has won at this trip or further; First-time headgear
- Clonmacash (hrs_35513198) | 5yo G | 144lb | OR 74 | draw 1 | jockey  | trainer Adrian McGuinness (14d 0/17) | headgear v | last run 58 days | form 375166 | MARKET 6.3% | 09:00 median 11.00 | Matchbook 14.50
    comment: The risk is two sixth-place finishes since and a 58-day break.
    DATA: model 9.7% | style Prominent (led 3% of runs) | runs in data 19 | last 3: 22 Aug Curragh Flat 6f Good 1/27; 21 Sep Fairyhouse Flat 6f Good 6/17; 30 Sep Bellewstown Flat 5f Soft To Heavy 6/6
    DATA for: Official rating 74, 8 lb above field average; Has won at this trip or further
    DATA against: Trainer 0 wins from 17 runs, last 14 days; Carries 8 lb more than average
- Andaman Fifty (hrs_55303801) | 3yo F | 141lb | OR 71 | draw 4 | jockey Nicola Burns(5) | trainer Miss Natalia Lupini (14d 1/9) | headgear - | last run 101 days | form 259 | MARKET 5.2% | 09:00 median 12.00 | Matchbook 19.00
    comment: Andaman Fifty is winless in her last three, a second three starts back followed by a fifth and a ninth last time out, and she returns after 101 days off.
    DATA: model 7.3% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 3 May Sligo Flat 6.3f Soft 2/7; 24 Jul Cork Flat 6f Good To Firm 5/13; 18 Aug Roscommon Flat 7.5f Good To Yielding 9/15
    DATA for: Official rating 71, 5 lb above field average
    DATA against: Carries 5 lb more than average; Returns from a 101-day break
- Sovereign Cry (hrs_57622173) | 3yo G | 135lb | OR 65 | draw 6 | jockey Ben Coen | trainer Daniel James Murphy (14d 1/7) | headgear p | last run 16 days | form 998090 | MARKET 4.6% | 09:00 median 17.00 | Matchbook 18.50
    comment: Sovereign Cry has been well beaten in recent starts, with a ninth two starts back and another ninth five runs ago, though he has run over today's trip and going and returns after 16 days.
    DATA: model 2.5% | style Held up (led 8% of runs) | runs in data 13 | last 3: 21 Sep Fairyhouse Flat 6f Good 16/17; 4 Nov Dundalk (AW) (IRE) Flat 6f Standard 9/9 fig 54; 11 Nov Dundalk (AW) (IRE) Flat 5f Standard 10/13 fig 57
    DATA against: Best recent form figure 57, 5 lb below field average; Recent figures 8 lb below its current mark (looks high in the weights); Poor recent finishing positions; Pace: steady gallop likely, hard to come from off the pace
- Mint Man (hrs_36035902) | 5yo G | 135lb | OR 65 | draw 11 | jockey Chris Hayes | trainer P J F Murphy (14d 1/3) | headgear tv | last run 16 days | form 031009 | MARKET 3.3% | 09:00 median 19.00 | Matchbook 27.00
    comment: Mint Man was beaten into ninth last time out and unplaced in the two runs before, though he won four starts back and has run over today's trip and going.
    DATA: model 3.2% | style Midfield (led 29% of runs) | runs in data 10 | last 3: 22 Aug Curragh Flat 6f Good 19/27; 2 Sep Navan Flat 5f Good 13/16; 11 Nov Dundalk (AW) (IRE) Flat 5f Standard 9/13 fig 58
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 58, 4 lb below field average; Recent figures 7 lb below its current mark (looks high in the weights); Poor recent finishing positions
- I'm Spartacus (hrs_35925561) | 5yo G | 132lb | OR 62 | draw 12 | jockey Cillian Rowan(10) | trainer Adrian McGuinness (14d 0/17) | headgear - | last run 78 days | form 048005 | MARKET 3.1% | 09:00 median 21.00 | Matchbook 27.00
    comment: I'm Spartacus is winless in his last six, with a fifth last time out and a fourth five starts back the pick of a modest recent run, and he returns after 78 days off, so he is hard to fancy.
    DATA: model 2.6% | style Midfield (led 4% of runs) | runs in data 14 | last 3: 23 Aug Naas Flat 5f Good 14/19; 29 Aug Curragh Flat 6f Yielding 19/19; 10 Sep Laytown Flat 7f Standard 5/10
    DATA for: Has won at this trip or further
    DATA against: Trainer 0 wins from 17 runs, last 14 days
- All Hail (hrs_53081217) | 3yo G | 121lb | OR 51 | draw 13 | jockey Siobhan Rutledge | trainer John McConnell (14d 0/17) | headgear b | last run 7 days | form 980400 | MARKET 1.9% | 09:00 median 41.00 | Matchbook 44.00
    comment: He is back quickly after seven days, though, and has run over today's trip and going.
    DATA: model 1.5% | style Held up (led 4% of runs) | runs in data 9 | last 3: 25 Sep Dundalk Flat 6f Standard 4/14; 28 Oct Dundalk (AW) (IRE) Flat 7f Standard 12/13 fig 46; 20 Nov Dundalk (AW) (IRE) Flat 6f Standard 10/14 fig 40
    DATA for: Last-run finishing speed +2.9% vs that field (finished strongly); Carries 15 lb less than average
    DATA against: Best recent form figure 46, 16 lb below field average; Official rating 51, 15 lb below field average; Trainer 0 wins from 17 runs, last 14 days; Pace: steady gallop likely, hard to come from off the pace
- Leonie (hrs_52451931) | 3yo F | 134lb | OR 64 | draw 15 | jockey Donagh O'Connor | trainer A. McCann (14d 0/7) | headgear t | last run 16 days | form 316088 | MARKET 1.7% | 09:00 median 51.00 | Matchbook 48.00
    comment: Leonie has finished eighth in each of her last two runs and has not been better than sixth since winning five starts back, so she is hard to fancy. She has run over today's trip and going, and a quick 16-day turnaround keeps her fit, but 134 lb from stall 15 is a big ask.
    DATA: model 2.1% | style Held up (led 8% of runs) | runs in data 8 | last 3: 2 Oct Wolverhampton Flat 6.1f Standard 10/10; 21 Oct Kempton (AW) Flat 6f Standard / Slow 8/11 fig 61; 11 Nov Dundalk (AW) (IRE) Flat 8f Standard 8/8
    DATA for: Has won at this trip or further
    DATA against: Last-run finishing speed -7.3% vs that field (faded); Poor recent finishing positions; Pace: steady gallop likely, hard to come from off the pace
- Dandyville (hrs_22138172) | 8yo G | 123lb | OR 53 | draw 10 | jockey R. P. Cleary | trainer Ms Claire O'Connell (14d 1/5) | headgear - | last run 23 days | form 080070 | MARKET 1.7% | 09:00 median 51.00 | Matchbook 46.00
    comment: Dandyville is winless in his last six, with an eighth five starts back and a seventh two starts back his best finishes, so he is hard to fancy on recent evidence. He has run over today's trip and going, and comes here 23 days after his last run, off 123 lb from draw 10.
    DATA: model 1.4% | style Prominent (led 5% of runs) | runs in data 7 | last 3: 30 Sep Bellewstown Flat 7.9f Soft To Heavy 13/14; 23 Oct Dundalk (AW) (IRE) Flat 6f Standard 7/14 fig 54; 4 Nov Dundalk (AW) (IRE) Flat 7f Standard 11/13 fig 47
    DATA for: Trainer 20% wins (1/5), last 14 days; Carries 13 lb less than average
    DATA against: Best recent form figure 54, 8 lb below field average; Official rating 53, 13 lb below field average; Last-run finishing speed -3.3% vs that field (faded); Poor recent finishing positions; Aged 8, older than most of this field

## 7:30 Dundalk (AW) | race_id rac_32305851032 | BAR 1 Betting 'Bet 10 Get 50' Handicap
Flat |  | 2m0f0y | going Standard | AW | 10 runners | rating band - | age 3yo+
DATA pace: Strong pace - 3 habitual front-runners (Delta, Not Just Any Eagle, Murat). A contested lead should set things up for horses coming from behind.
- Not Just Any Eagle (hrs_30096731) | 7yo G | 135lb | OR 85 | draw 7 | jockey Robyn Donaghue-Leahy(7) | trainer Patrick J Flynn (14d 2/6) | headgear - | last run 28 days | form 324151 | MARKET 20.1% | 09:00 median 4.00 | Matchbook 4.50 | CHECK (skip line 3.80)
    DATA: model 16.0% | style Leader (led 54% of runs) | runs in data 9 | last 3: 16 Sep Clonmel Flat 16.8f Yielding 1/11; 11 Oct Naas Flat 16f Soft 5/17; 30 Oct Dundalk (AW) (IRE) Flat 12f Standard 1/9 fig 82
    DATA for: Trainer 33% wins (2/6), last 14 days; Has won at this trip or further; Good recent finishing positions
    DATA against: Pace: likely to be taken on for the lead
- Star Harbour (hrs_23500323) | 8yo G | 138lb | OR 88 | draw 5 | jockey Adam Caffrey | trainer Adrian McGuinness (14d 0/17) | headgear v | last run 14 days | form 223002 | MARKET 17.5% | 09:00 median 5.00 | Matchbook 4.90
    comment: Star Harbour arrives fresh from a second last time out just 14 days ago, with a third and two further seconds in his last six, and he has run on today's going before. Yet to win in that spell, he carries 138 lb, and that lack of a win is the main risk.
    DATA: model 9.0% | style Prominent (led 5% of runs) | runs in data 13 | last 3: 12 Sep Leopardstown Flat 13f Good 12/21; 21 Sep Listowel Flat 12f Yielding 12/15; 13 Nov Dundalk (AW) (IRE) Flat 10.5f Standard 2/10 fig 87
    DATA for: Best recent form figure 87, 6 lb above field average
    DATA against: Trainer 0 wins from 17 runs, last 14 days
- Murat (hrs_41171823) | 7yo G | 132lb | OR 82 | draw 4 | jockey R. P. Cleary | trainer Peter Lawlor (14d 0/2) | headgear - | last run 86 days | form 7129 | MARKET 16.6% | 09:00 median 5.00 | Matchbook 5.30
    comment: Murat bounced back from a seventh four starts back to win three starts back, then followed with a second, so the profile is sound, and he has run over today's trip.
    DATA: model 19.3% | style Prominent (led 54% of runs) | runs in data 6 | last 3: 9 Jul Leopardstown Flat 15f Good 1/5; 21 Aug Killarney Flat 16.8f Good 2/8; 2 Sep Navan Flat 16f Good 9/16
    DATA for: Good recent finishing positions
- Zoffman (hrs_25825562) | 7yo G | 125lb | OR 75 | draw 8 | jockey Nicola Burns(5) | trainer Noel Meade (14d 2/14) | headgear p | last run 22 days | form 030243 | MARKET 11.6% | 09:00 median 7.50 | Matchbook 7.60
    comment: Winless in his last six, Zoffman has at least been consistent, finishing third last time out and a second three starts back, and he has run over today's trip and going before.
    DATA: model 7.0% | style Midfield (led 4% of runs) | runs in data 11 | last 3: 3 Oct Gowran Park Hurdle 24.2f Good To Yielding 2/11; 30 Oct Dundalk (AW) (IRE) Flat 12f Standard 3/9 fig 72; 5 Nov Clonmel (IRE) Hurdle 24f Good 5/7 fig 114
    DATA for: Good recent finishing positions; Carries 9 lb less than average
    DATA against: Best recent form figure 72, 9 lb below field average; Official rating 75, 9 lb below field average
- Glenroyal (hrs_49389263) | 4yo G | 138lb | OR 88 | draw 6 | jockey J M Sheridan | trainer Joseph Patrick O'Brien (14d 4/35) | headgear tv (1st time) | last run 61 days | form 1-0800 | MARKET 7.8% | 09:00 median 10.00 | Matchbook 12.00
    comment: Glenroyal won five starts back but has been unplaced in three of his last four since, including last time out, and returns after 61 days off.
    DATA: model 6.4% | style Midfield (led 4% of runs) | runs in data 5 | last 3: 27 Jul Galway Flat 16.8f Good 8/20; 12 Sep Leopardstown Flat 13f Good 18/21; 27 Sep Curragh Flat 16.8f Heavy 21/30
    DATA for: First-time headgear
    DATA against: Last-run finishing speed -2.2% vs that field (faded); Poor recent finishing positions
- Delta (hrs_43797138) | 4yo G | 140lb | OR 90 | draw 2 | jockey Mel Sheridan(7) | trainer Denis Gerard Hogan (14d 0/15) | headgear p | last run 63 days | form -40247 | MARKET 6.7% | 09:00 median 11.00 | Matchbook 17.50
    comment: Off 140 lb and 63 days since a seventh last time out, that break is the one reservation.
    DATA: model 21.2% | style Leader (led 23% of runs) | runs in data 5 | last 3: 9 Jul Leopardstown Flat 15f Good 2/5; 15 Aug Tramore Flat 16f Good To Yielding 4/8; 25 Sep Listowel Flat 14f Good To Yielding 7/13
    DATA for: Official rating 90, 6 lb above field average; Last-run finishing speed +2.2% vs that field (finished strongly)
    DATA against: Trainer 0 wins from 15 runs, last 14 days; Carries 6 lb more than average; Pace: likely to be taken on for the lead
- Pillar Of Hope (hrs_22064868) | 8yo G | 130lb | OR 80 | draw 10 | jockey Patrick McGettigan(5) | trainer P Sweeney (14d 0/3) | headgear - | last run 28 days | form 481175 | MARKET 6.0% | 09:00 median 15.00 | Matchbook 13.50
    comment: Won twice in his last six starts, taking victories three and four starts back, but he's since gone seventh then fifth, and 28 days off suggests he's fresh enough.
    DATA: model 7.5% | style Prominent (led 4% of runs) | runs in data 11 | last 3: 12 Oct Roscommon Flat 12.2f Soft 1/16; 18 Oct Leopardstown (IRE) Flat 11.5f Good 7/15 fig 85; 30 Oct Dundalk (AW) (IRE) Flat 12f Standard 5/9 fig 78
    DATA for: Recent figures 5 lb above its current mark (looks well handicapped)
- Tatateo (hrs_36614963) | 5yo G | 133lb | OR 83 | draw 9 | jockey Chris Hayes | trainer Denis Gerard Hogan (14d 0/15) | headgear tp | last run 18 days | form 22-178 | MARKET 4.8% | 09:00 median 17.00 | Matchbook 19.50
    comment: Tatateo is hard to fancy after finishing eighth last time out and a seventh the start before, a clear drop from a win three starts back and a pair of seconds before that.
    DATA: model 3.5% | style Midfield (led 3% of runs) | runs in data 8 | last 3: 16 Sep Clonmel Flat 16.8f Yielding 8/11; 10 Oct Fairyhouse Chase 16.5f Good 6/6; 9 Nov Punchestown (IRE) Chase 16.5f Good To Yielding 7/7
    DATA for: Has won at this trip or further
    DATA against: Trainer 0 wins from 15 runs, last 14 days; Last-run finishing speed -2.3% vs that field (faded); Poor recent finishing positions
- Mister Adam (hrs_46697343) | 4yo G | 134lb | OR 84 | draw 3 | jockey Danny O'Leary(10) | trainer G. O'Leary (14d 0/6) | headgear - | last run 39 days | form 4316-8 | MARKET 4.5% | 09:00 median 19.00 | Matchbook 19.50
    comment: Mister Adam arrives off a 39-day break after a eighth last time out and a sixth two starts back, though he did win three starts back and has run on today's going before.
    DATA: model 6.4% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 19 Oct Gowran Park (IRE) Flat 12f Soft 8/14 fig 76
    DATA against: Best recent form figure 76, 5 lb below field average; Recent figures 8 lb below its current mark (looks high in the weights); Lightly raced: 1 run in our data, so the model has little to go on
- Spicy Margarita (hrs_46265387) | 4yo F | 138lb | OR 88 | draw 1 | jockey Donagh O'Connor | trainer Robson De Aguiar (14d 1/8) | headgear - | last run 21 days | form 870974 | MARKET 4.3% | 09:00 median 15.00 | Matchbook 26.00
    comment: The risk is a winless sequence, with nothing better than seventh in the four runs before that.
    DATA: model 3.6% | style Midfield (led 5% of runs) | runs in data 9 | last 3: 13 Sep Curragh Flat 10f Yielding 9/10; 25 Sep Dundalk Flat 10.7f Standard 7/7; 6 Nov Dundalk (AW) (IRE) Flat 8f Standard 4/8 fig 85

## 8:00 Dundalk (AW) | race_id rac_32305852969 | BAR 1 Betting 'Weekly Rewards' Apprentice Handicap
Flat |  | 0m5f0y | going Standard | AW | 11 runners | rating band 0-60 | age 3yo+
DATA pace: Lone leader - Bye Bye Now is the only habitual front-runner and may be allowed an easy lead.
- Bye Bye Now (hrs_42943698) | 4yo F | 135lb | OR 53 | draw 3 | jockey Nicola Burns(2) | trainer John McConnell (14d 0/17) | headgear p | last run 28 days | form 142764 | MARKET 18.0% | 09:00 median 4.50 | Matchbook 5.10 | CHECK (skip line 4.27)
    DATA: model 12.0% | style Leader (led 57% of runs) | runs in data 8 | last 3: 17 Jul Down Royal Flat 5f Good 7/11; 2 Oct Dundalk Flat 5f Standard 6/12; 30 Oct Dundalk (AW) (IRE) Flat 5f Standard 4/14 fig 54
    DATA for: Best recent form figure 54, 6 lb above field average; Has won at this trip or further; Pace: may get an uncontested lead
    DATA against: Trainer 0 wins from 17 runs, last 14 days
- One Cool Bear (hrs_53960053) | 3yo G | 142lb | OR 60 | draw 11 | jockey Camillus Byrne(7) | trainer Adrian McGuinness (14d 0/17) | headgear p | last run 7 days | form 773238 | MARKET 16.6% | 09:00 median 4.50 | Matchbook 5.80
    comment: He is yet to win in recent starts, but a quick seven-day turnaround keeps him fit.
    DATA: model 21.7% | style Prominent (led 5% of runs) | runs in data 15 | last 3: 30 Oct Dundalk (AW) (IRE) Flat 5f Standard 2/14 fig 61; 11 Nov Dundalk (AW) (IRE) Flat 5f Standard 3/13 fig 63; 20 Nov Dundalk (AW) (IRE) Flat 6f Standard 8/14 fig 53
    DATA for: Best recent form figure 63, 15 lb above field average; Official rating 60, 11 lb above field average; Has won at this trip or further; Good recent finishing positions
    DATA against: Trainer 0 wins from 17 runs, last 14 days; Carries 11 lb more than average
- Astute Power (hrs_56127617) | 4yo G | 137lb | OR 55 | draw 9 | jockey Patrick McGettigan | trainer Edward Lynam (14d 0/1) | headgear t | last run 16 days | form -00486 | MARKET 13.7% | 09:00 median 6.10 | Matchbook 6.20
    comment: The risk is a winless recent run, with a sixth last time out his best finish since a fourth three starts back.
    DATA: model 11.0% | style Held up (led 5% of runs) | runs in data 5 | last 3: 7 Oct Navan Flat 5.8f Yielding 4/13; 21 Oct Navan (IRE) Flat 5f Yielding 8/9 fig 24; 11 Nov Dundalk (AW) (IRE) Flat 5f Standard 6/13 fig 56
    DATA for: Best recent form figure 56, 8 lb above field average; Official rating 55, 6 lb above field average
    DATA against: Carries 6 lb more than average
- The Love Machine (hrs_53841081) | 3yo G | 130lb | OR 48 | draw 2 | jockey Jimmy Dalton(4) | trainer Sean Davis (14d 0/1) | headgear - | last run 51 days | form 005920 | MARKET 13.3% | 09:00 median 6.50 | Matchbook 6.60
    comment: Winless in his last six, The Love Machine was unplaced last time out, though a second two starts back shows he can get involved, and he has run over today's trip and going.
    DATA: model 12.8% | style Held up (led 4% of runs) | runs in data 10 | last 3: 5 Aug Sligo Flat 6f Yielding 9/12; 5 Sep Navan Flat 5f Good 2/18; 7 Oct Navan Flat 5.8f Yielding 15/22
    DATA against: Last-run finishing speed -2.5% vs that field (faded)
- The Cosy Corner (hrs_55700785) | 3yo F | 127lb | OR 45 | draw 10 | jockey Adam Grant(7) | trainer Patrick Magee (14d 0/7) | headgear p | last run 7 days | form -00436 | MARKET 11.5% | 09:00 median 7.50 | Matchbook 7.60
    comment: Sixth last time out, but a third two starts back and a fourth three starts back show she can pick up cheques, and she's back quickly after seven days, having run over today's trip and going.
    DATA: model 15.2% | style Midfield (led 4% of runs) | runs in data 5 | last 3: 2 Oct Dundalk Flat 5f Standard 4/12; 23 Oct Dundalk (AW) (IRE) Flat 6f Standard 3/14 fig 45; 20 Nov Dundalk (AW) (IRE) Flat 6f Standard 6/14 fig 44
- Shamanka (hrs_46944667) | 4yo F | 134lb | OR 52 | draw 1 | jockey Rory Mulligan | trainer Harry Cleary (14d 0/0) | headgear tb | last run 30 days | form 040568 | MARKET 5.4% | 09:00 median 13.00 | Matchbook 24.00
    comment: The risk is a form line of eighth last time out, and she is winless in her last six starts.
    DATA: model 9.5% | style Held up (led 4% of runs) | runs in data 6 | last 3: 20 Aug Leopardstown Flat 7f Good To Yielding 5/14; 31 Aug Roscommon Flat 7.4f Good To Yielding 6/14; 28 Oct Dundalk (AW) (IRE) Flat 7f Standard 8/13 fig 45
    DATA against: Recent figures 7 lb below its current mark (looks high in the weights)
- Star Allure (hrs_41346375) | 4yo F | 123lb | OR 41 | draw 5 | jockey Sadhbh Tormey(7) | trainer Ms Claire O'Connell (14d 1/5) | headgear tb | last run 23 days | form 055394 | MARKET 5.3% | 09:00 median 15.00 | Matchbook 18.00
    comment: Winless in her last six, Star Allure was fourth last time out after a ninth two starts back, and that patchy record makes her hard to fancy.
    DATA: model 3.1% | style Prominent (led 5% of runs) | runs in data 9 | last 3: 1 Oct Bellewstown Flat 5f Soft To Heavy 3/9; 30 Oct Dundalk (AW) (IRE) Flat 5f Standard 9/14 fig 32; 4 Nov Dundalk (AW) (IRE) Flat 6f Standard 4/8 fig 51
    DATA for: Recent figures 10 lb above its current mark (looks well handicapped); Trainer 20% wins (1/5), last 14 days; Carries 8 lb less than average
    DATA against: Official rating 41, 8 lb below field average
- Phil's Dream (hrs_30208178) | 6yo G | 132lb | OR 50 | draw 8 | jockey Cillian Rowan(7) | trainer Adrian McGuinness (14d 0/17) | headgear tp | last run 35 days | form 180580 | MARKET 5.1% | 09:00 median 15.00 | Matchbook 20.00
    comment: Phil's Dream was unplaced last time out and has not made the frame in his last five, though he did win six starts back and has run over today's trip and going before.
    DATA: model 4.2% | style Held up (led 4% of runs) | runs in data 8 | last 3: 1 Sep Wolverhampton Flat 6.1f Standard 5/11; 2 Oct Dundalk Flat 5f Standard 8/12; 23 Oct Dundalk (AW) (IRE) Flat 6f Standard 10/14 fig 42
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 42, 6 lb below field average; Recent figures 8 lb below its current mark (looks high in the weights); Trainer 0 wins from 17 runs, last 14 days
- Hasiyna (hrs_31188213) | 6yo M | 122lb | OR 40 | draw 7 | jockey Conor Cusack(7) | trainer John McConnell (14d 0/17) | headgear - | last run 35 days | form 697900 | MARKET 4.2% | 09:00 median 19.00 | Matchbook 24.00
    comment: Hasiyna is hard to fancy, yet to win in her last six starts and unplaced on her last two after a ninth, a seventh, another ninth and a sixth before that.
    DATA: model 2.3% | style Midfield (led 5% of runs) | runs in data 7 | last 3: 23 Aug Naas Flat 5f Good 9/19; 2 Oct Dundalk Flat 5f Standard 12/12; 23 Oct Dundalk (AW) (IRE) Flat 6f Standard 13/14 fig 31
    DATA for: Carries 9 lb less than average
    DATA against: Best recent form figure 31, 17 lb below field average; Recent figures 9 lb below its current mark (looks high in the weights); Official rating 40, 9 lb below field average; Trainer 0 wins from 17 runs, last 14 days; Poor recent finishing positions
- Gaineamh Min (hrs_17389460998) | 3yo F | 131lb | OR 49 | draw 6 | jockey Keithen Kennedy | trainer Sean Byrne (14d 0/0) | headgear - | last run 28 days | form 0707 | MARKET 3.6% | 09:00 median 17.00 | Matchbook 44.00
    comment: Gaineamh Min is hard to fancy, winless in her last four with a seventh last time out and a seventh three starts back, though she has run over today's trip and going before after 28 days off.
    DATA: model 2.9% | style Midfield (led 4% of runs) | runs in data 4 | last 3: 4 Sep Down Royal Flat 5f Good 7/12; 27 Sep Curragh Flat 6f Heavy 10/11; 30 Oct Dundalk (AW) (IRE) Flat 5f Standard 7/14 fig 43
    DATA against: Best recent form figure 43, 5 lb below field average; Recent figures 6 lb below its current mark (looks high in the weights); Poor recent finishing positions
- Prince Andorra (hrs_62360865) | 3yo G | 132lb | OR 50 | draw 4 | jockey Alan Casey(7) | trainer Ms Claire O'Connell (14d 1/5) | headgear t | last run 9 days | form 005000 | MARKET 3.4% | 09:00 median 26.00 | Matchbook 29.00
    comment: Prince Andorra is winless in his last six, with a fifth four starts back his best recent finish, though he's fresh enough after nine days off and has run over today's trip and going.
    DATA: model 5.3% | style Held up (led 3% of runs) | runs in data 9 | last 3: 9 Oct Dundalk Flat 7f Standard 11/14; 15 Oct Curragh (IRE) Flat 5f Soft 11/17 fig 47; 18 Nov Dundalk (AW) (IRE) Flat 7f Standard 10/14 fig 45
    DATA for: Trainer 20% wins (1/5), last 14 days
    DATA against: Poor recent finishing positions

## 8:30 Dundalk (AW) | race_id rac_32305854906 | Saddle Cocktail Bar At Dundalk Stadium Handicap
Flat |  | 1m2f150y | going Standard | AW | 15 runners | rating band - | age 3yo+
DATA pace: Lone leader - A Pretty Penny is the only habitual front-runner and may be allowed an easy lead.
- Movin And Groovin (hrs_42451878) | 4yo F | 134lb | OR 64 | draw 4 | jockey Nathan Crosse | trainer David Marnane (14d 1/6) | headgear - | last run 16 days | form 137381 | MARKET 19.3% | 09:00 median 4.00 | Matchbook 3.75 | CHECK (skip line 3.80)
    comment: Carrying 134 lb from stall four, she is fit after 16 days and has run over this trip and going.
    DATA: model 11.0% | style Midfield (led 4% of runs) | runs in data 6 | last 3: 12 Oct Roscommon Flat 7.5f Soft 3/13; 29 Oct Punchestown (IRE) Flat 7f Yielding 8/12 fig 36; 11 Nov Dundalk (AW) (IRE) Flat 10.5f Standard 1/14 fig 64
    DATA for: Has won at this trip or further; Good recent finishing positions
- Usuario Amigo (hrs_40805534) | 5yo G | 140lb | OR 70 | draw 14 | jockey Adam Grant(7) | trainer Richard John O'Brien (14d 1/4) | headgear - | last run 7 days | form 361762 | MARKET 11.7% | 09:00 median 6.00 | Matchbook 7.40
    comment: Usuario Amigo returns quickly after a second last time out, and he has run over today's trip and going before, though a sixth and a seventh two and three starts back temper the mood.
    DATA: model 10.4% | style Held up (led 5% of runs) | runs in data 15 | last 3: 11 Nov Dundalk (AW) (IRE) Flat 7f Standard 7/14 fig 57; 18 Nov Dundalk (AW) (IRE) Flat 8f Standard 6/13 fig 61; 20 Nov Dundalk (AW) (IRE) Flat 10.5f Standard 2/13 fig 68
    DATA for: Best recent form figure 68, 7 lb above field average; Official rating 70, 6 lb above field average; Last-run finishing speed +4.3% vs that field (finished strongly)
    DATA against: Carries 7 lb more than average
- Flying Fortress (hrs_43951047) | 4yo G | 147lb | OR 77 | draw 13 | jockey Camillus Byrne(10) | trainer Gavin Cromwell (14d 4/41) | headgear b | last run 7 days | form 240041 | MARKET 11.6% | 09:00 median 6.50 | Matchbook 6.60
    comment: Fresh from a win last time out just seven days ago, Flying Fortress is in good heart and has run over today's trip and going before.
    DATA: model 16.6% | style Prominent (led 4% of runs) | runs in data 9 | last 3: 29 Oct Punchestown (IRE) Flat 8f Yielding 11/14 fig 63; 11 Nov Dundalk (AW) (IRE) Flat 10.5f Standard 4/14 fig 72; 20 Nov Dundalk (AW) (IRE) Flat 10.5f Standard 1/13 fig 74
    DATA for: Best recent form figure 74, 13 lb above field average; Official rating 77, 13 lb above field average; Has won at this trip or further
    DATA against: Carries 14 lb more than average
- Riyazanka (hrs_17391710749) | 3yo F | 128lb | OR 62 | draw 1 | jockey Ben Coen | trainer J. P. Murtagh (14d 2/7) | headgear - | last run 16 days | form 736 | MARKET 11.2% | 09:00 median 7.00 | Matchbook 7.20
    comment: Riyazanka is hard to fancy, winless in her last three and beaten into sixth last time out, though a third two starts back shows some ability and she has run on today's going.
    DATA: model 9.2% | style Unknown | runs in data 3 | last 3: 2 Sep Navan Flat 8.1f Good 7/13; 30 Oct Dundalk (AW) (IRE) Flat 8f Standard 3/14 fig 58; 11 Nov Dundalk (AW) (IRE) Flat 8f Standard 6/13 fig 53
    DATA for: Trainer 29% wins (2/7), last 14 days; Carries 5 lb less than average
- Love Orchid (hrs_53960032) | 3yo F | 136lb | OR 70 | draw 5 | jockey Nicola Burns(5) | trainer Noel Meade (14d 2/14) | headgear p (1st time) | last run 14 days | form 236292 | MARKET 9.4% | 09:00 median 8.00 | Matchbook 9.00
    comment: Love Orchid comes here fresh from a second last time out, just 14 days ago, and has run over today's trip and going, but she is winless in her last six and was only ninth two starts back.
    DATA: model 10.9% | style Midfield (led 4% of runs) | runs in data 11 | last 3: 11 Oct Naas Flat 10.7f Soft 2/12; 19 Oct Gowran Park (IRE) Flat 12f Soft 9/14 fig 55; 13 Nov Dundalk (AW) (IRE) Flat 10.5f Standard 2/10 fig 72
    DATA for: Best recent form figure 72, 11 lb above field average; Official rating 70, 6 lb above field average; Good recent finishing positions; First-time headgear
- Tribal Moon (hrs_36665132) | 5yo G | 134lb | OR 64 | draw 7 | jockey Rory Mulligan(5) | trainer Noel C. Kelly (14d 0/6) | headgear tb | last run 7 days | form -06770 | MARKET 7.9% | 09:00 median 9.00 | Matchbook 11.00
    comment: Tribal Moon is winless in his last five, with a seventh two starts back and another seventh three back, but he's quick back after seven days and has run over today's trip and going.
    DATA: model 4.3% | style Midfield (led 5% of runs) | runs in data 10 | last 3: 16 Oct Dundalk (AW) (IRE) Flat 10.5f Standard 7/14 fig 64; 30 Oct Dundalk (AW) (IRE) Flat 12f Standard 7/9 fig 59; 20 Nov Dundalk (AW) (IRE) Flat 10.5f Standard 10/13 fig 53
    DATA against: Poor recent finishing positions
- Flame Of Forest (hrs_52176572) | 4yo G | 140lb | OR 70 | draw 2 | jockey W. M. Lordan | trainer Miss Natalia Lupini (14d 1/9) | headgear - | last run 28 days | form 007990 | MARKET 6.1% | 09:00 median 12.00 | Matchbook 13.00
    comment: The main risk is that he is yet to find a way to the front in recent runs.
    DATA: model 4.6% | style Midfield (led 5% of runs) | runs in data 6 | last 3: 25 Sep Dundalk Flat 10.7f Standard 9/14; 16 Oct Dundalk (AW) (IRE) Flat 10.5f Standard 9/11 fig 68; 30 Oct Dundalk (AW) (IRE) Flat 8f Standard 13/14 fig 48
    DATA for: Best recent form figure 68, 7 lb above field average; Official rating 70, 6 lb above field average
    DATA against: Poor recent finishing positions; Carries 7 lb more than average
- Anightaway (hrs_56559272) | 5yo G | 124lb | OR 54 | draw 15 | jockey Sean Davis | trainer Sean Davis (14d 0/1) | headgear - | last run 46 days | form 081024 | MARKET 5.6% | 09:00 median 12.00 | Matchbook 16.00
    comment: Anightaway was fourth last time out and second two starts back, but he's won just once in his last six and has been off 46 days, which makes him hard to fancy.
    DATA: model 5.9% | style Prominent (led 23% of runs) | runs in data 6 | last 3: 27 Aug Navan Flat 14f Good 18/22; 1 Oct Bellewstown Flat 12.3f Soft To Heavy 2/11; 12 Oct Roscommon Flat 12.2f Soft 4/16
    DATA for: Has won at this trip or further; Carries 9 lb less than average
    DATA against: Official rating 54, 10 lb below field average
- A Pretty Penny (hrs_55764506) | 3yo F | 130lb | OR 64 | draw 6 | jockey Julian Pietropaolo(5) | trainer Mrs Deborah Cody (14d 0/0) | headgear - | last run 72 days | form 154218 | MARKET 3.6% | 09:00 median 21.00 | Matchbook 22.00
    comment: A Pretty Penny won two starts back and six starts back, and has run over today's trip and going, but she was only eighth last time out and returns after 72 days off.
    DATA: model 8.5% | style Leader (led 43% of runs) | runs in data 8 | last 3: 7 Jul Tramore Flat 12f Good 2/11; 15 Aug Tramore Flat 12f Good To Yielding 1/8; 16 Sep Clonmel Flat 9.8f Yielding 8/9
    DATA for: Has won at this trip or further; Good recent finishing positions; Pace: may get an uncontested lead
- Wild Berries (hrs_53743235) | 3yo F | 130lb | OR 64 | draw 10 | jockey Patrick McGettigan(5) | trainer Ross O'Sullivan (14d 1/20) | headgear p | last run 63 days | form 070010 | MARKET 3.1% | 09:00 median 26.00 | Matchbook 26.00
    DATA: model 6.2% | style Midfield (led 3% of runs) | runs in data 6 | last 3: 2 Sep Navan Flat 8.1f Good 11/16; 18 Sep Dundalk Flat 10.7f Standard 1/14; 25 Sep Dundalk Flat 12f Standard 11/14
    DATA for: Has won at this trip or further
- Emily Estherfaye (hrs_17389581986) | 3yo F | 133lb | OR 67 | draw 3 | jockey Adam Browne-Souza(7) | trainer A. Slattery (14d 0/16) | headgear h | last run 16 days | form 05477 | MARKET 2.4% | 09:00 median 29.00 | Matchbook 38.00
    comment: Emily Estherfaye is winless in her last five, finishing seventh on her last two outings and no better than a fourth three starts back, so she is hard to fancy off 133 lb.
    DATA: model 1.6% | style Prominent (led 29% of runs) | runs in data 5 | last 3: 16 Sep Clonmel Flat 9.8f Yielding 4/8; 5 Oct Killarney Flat 11.2f Soft 7/7; 11 Nov Dundalk (AW) (IRE) Flat 8f Standard 7/13 fig 45
    DATA against: Best recent form figure 45, 16 lb below field average; Recent figures 22 lb below its current mark (looks high in the weights); Trainer 0 wins from 16 runs, last 14 days
- Satono Chevalier (hrs_25263385) | 8yo G | 143lb | OR 73 | draw 12 | jockey Mel Sheridan(7) | trainer M K Flannery (14d 0/2) | headgear p | last run 54 days | form 300677 | MARKET 2.4% | 09:00 median 29.00 | Matchbook 40.00
    DATA: model 5.9% | style Prominent (led 3% of runs) | runs in data 15 | last 3: 16 Sep Clonmel Flat 9.8f Yielding 6/9; 21 Sep Listowel Flat 9f Yielding 7/13; 4 Oct Curragh Flat 12f Yielding 7/12
    DATA for: Official rating 73, 9 lb above field average; Has won at this trip or further
    DATA against: Poor recent finishing positions; Carries 10 lb more than average; Aged 8, older than most of this field
- Afloat (hrs_34360746) | 6yo M | 132lb | OR 62 | draw 9 | jockey Robert Whearty | trainer Gavin Cromwell (14d 4/41) | headgear p (1st time) | last run 7 days | form 08-580 | MARKET 2.2% | 09:00 median 34.00 | Matchbook 42.00
    comment: The main risk is a winless run in her last five starts, with nothing better than a fifth three starts back.
    DATA: model 2.9% | style Held up (led 3% of runs) | runs in data 4 | last 3: 21 Sep Listowel Flat 14.2f Yielding 8/15; 1 Nov Cork (IRE) Hurdle 16f Good To Yielding F/19; 20 Nov Dundalk (AW) (IRE) Flat 10.5f Standard 12/13 fig 54
    DATA for: First-time headgear
    DATA against: Best recent form figure 54, 7 lb below field average; Recent figures 8 lb below its current mark (looks high in the weights); Poor recent finishing positions
- Rosanella (hrs_17392594170) | 3yo F | 119lb | OR 45 | draw 8 | jockey  | trainer Josh Halley (14d 0/1) | headgear h | last run 21 days | form 0077 | MARKET 2.0% | 09:00 median 34.00 | Matchbook 46.00
    comment: Rosanella is hard to fancy, having finished seventh last time out and seventh two starts back, and she is winless in her last four, with the other two runs unplaced.
    DATA: model 0.7% | style Midfield (led 5% of runs) | runs in data 4 | last 3: 7 Oct Navan Flat 5.8f Yielding 12/13; 16 Oct Dundalk (AW) (IRE) Flat 6f Standard 7/9 fig 50; 6 Nov Dundalk (AW) (IRE) Flat 8f Standard 7/14 fig 42
    DATA for: Recent figures 5 lb above its current mark (looks well handicapped); Carries 14 lb less than average
    DATA against: Best recent form figure 50, 11 lb below field average; Official rating 45, 19 lb below field average; Poor recent finishing positions
- Isthatrightkatie (hrs_53808853) | 6yo M | 130lb | OR 60 | draw 11 | jockey Killian Leonard | trainer Miss Katy Brown (14d 0/0) | headgear - | last run 16 days | form 8-0480 | MARKET 1.5% | 09:00 median 51.00 | Matchbook 60.00
    comment: Isthatrightkatie is winless in her last five, with a fourth three starts back her best effort, and she was unplaced last time out just 16 days ago.
    DATA: model 1.3% | style Prominent (led 5% of runs) | runs in data 6 | last 3: 12 Oct Roscommon Flat 10.4f Soft 4/11; 23 Oct Dundalk (AW) (IRE) Flat 10.5f Standard 8/14 fig 58; 11 Nov Dundalk (AW) (IRE) Flat 7f Standard 13/14 fig 52
