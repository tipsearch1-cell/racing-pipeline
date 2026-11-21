# Card review packet: Newcastle (AW), 2026-11-21

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


## 2:49 Newcastle (AW) | race_id rac_32305461695 | Make The Move To Midnite Handicap Stakes (Div I)
Flat | Class 5 | 1m4f98y | going Standard | AW | 9 runners | rating band 0-70 | age 3yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Mr Moonshine (hrs_53743431) | 3yo G | 134lb | OR 69 | draw 7 | jockey Oisin Orr | trainer Richard & Peter Fahey (14d 0/6) | headgear p | last run 23 days | form 310462 | MARKET 27.8% | 09:00 median 2.88 | Matchbook 3.50
    comment: Mr Moonshine was second last time out and has run over today's trip and going, while a fresh 23 days since that effort suits.
    DATA: model 26.8% | style Midfield (led 3% of runs) | runs in data 9 | last 3: 1 Oct Newcastle Flat 12.4f Standard 4/11; 16 Oct Newcastle (AW) Flat 12.5f Standard 6/12 fig 64; 29 Oct Southwell (AW) Flat 11f Standard 2/10 fig 65
    DATA for: Official rating 69, 5 lb above field average; Has won at this trip or further
- Fleur de Mer (hrs_32538562) | 6yo M | 132lb | OR 62 | draw 9 | jockey Billy Garritty | trainer Martin Todhunter (14d 0/5) | headgear v | last run 23 days | form 325712 | MARKET 24.9% | 09:00 median 3.25 | Matchbook 3.85
    comment: Fleur de Mer arrives in good heart after a second last time out, and a winner two starts back, with 23 days since that run and experience of today's trip and going.
    DATA: model 15.1% | style Midfield (led 3% of runs) | runs in data 11 | last 3: 6 Oct Southwell Flat 11.1f Standard 7/9; 17 Oct Southwell (AW) Flat 14f Standard 1/6 fig 62; 29 Oct Southwell (AW) Flat 14f Standard 2/12 fig 60
    DATA for: Has won at this trip or further; Good recent finishing positions
- Dream Harder (hrs_26369840) | 7yo G | 140lb | OR 70 | draw 5 | jockey Hollie Doyle | trainer Mark Loughnane (14d 1/8) | headgear tv | last run 25 days | form 147665 | MARKET 10.6% | 09:00 median 8.00 | Matchbook 8.80
    comment: Dream Harder showed he can win when successful six starts back, and at 25 days since his last run he should be fresh, having run over today's trip and on this going before.
    DATA: model 11.6% | style Midfield (led 3% of runs) | runs in data 8 | last 3: 26 Sep Southwell Flat 12.1f Standard 6/8; 10 Oct Southwell Flat 12.1f Standard 6/11; 27 Oct Wolverhampton (AW) Flat 12f Standard 5/10 fig 67
    DATA for: Best recent form figure 67, 6 lb above field average; Official rating 70, 6 lb above field average; Has won at this trip or further
    DATA against: Carries 7 lb more than average
- Prince Achille (hrs_26796035) | 7yo G | 127lb | OR 57 | draw 8 | jockey Conor Whiteley(5) | trainer Jedd O'Keeffe (14d 0/2) | headgear - | last run 14 days | form 783435 | MARKET 9.8% | 09:00 median 9.00 | Matchbook 9.60
    comment: Prince Achille is winless in his last six, though a third two starts back and another third four starts back show he can reach the frame, and he has run over today's trip and going.
    DATA: model 8.7% | style Midfield (led 4% of runs) | runs in data 8 | last 3: 25 Sep Newcastle Flat 10.2f Standard 4/14; 16 Oct Newcastle (AW) Flat 12.5f Standard 3/12 fig 58; 7 Nov Southwell (AW) Flat 12f Standard 5/10 fig 55
    DATA for: Carries 6 lb less than average
    DATA against: Official rating 57, 7 lb below field average
- West Tyrone (hrs_43605632) | 4yo G | 137lb | OR 67 | draw 4 | jockey Shane Gray | trainer Lizzie Quinlan (14d 1/10) | headgear v (1st time) | last run 23 days | form 031703 | MARKET 8.7% | 09:00 median 9.50 | Matchbook 11.50
    comment: West Tyrone arrives off a third last time out, and a winner four starts back, with a 23-day break and experience over today's trip and going, though the two runs between were a seventh and an unplaced effort.
    DATA: model 10.6% | style Prominent (led 23% of runs) | runs in data 7 | last 3: 11 Sep Chester Flat 10.3f Good To Soft 7/11; 8 Oct Ayr Flat 10f Heavy 10/12; 29 Oct Southwell (AW) Flat 11f Standard 3/10 fig 62
    DATA for: First-time headgear
- Naval Command (hrs_45192602) | 4yo G | 140lb | OR 70 | draw 1 | jockey Jason Hart | trainer Rebecca Menzies (14d 0/9) | headgear tp (1st time) | last run 16 days | form 659558 | MARKET 6.6% | 09:00 median 13.00 | Matchbook 14.00
    comment: The risk is a string of finishes outside the first four.
    DATA: model 8.5% | style Midfield (led 4% of runs) | runs in data 6 | last 3: 16 Jul Epsom Downs Flat 12f Good To Firm 5/7; 10 Sep Epsom Downs Flat 12f Good To Soft 5/6; 5 Nov Southwell (AW) Flat 12f Standard 8/9 fig 53
    DATA for: Official rating 70, 6 lb above field average; First-time headgear
    DATA against: Best recent form figure 53, 8 lb below field average; Recent figures 17 lb below its current mark (looks high in the weights); Trainer 0 wins from 9 runs, last 14 days; Carries 7 lb more than average
- Annandale (hrs_20662299) | 8yo G | 128lb | OR 58 | draw 2 | jockey Lauren Young(5) | trainer Jim Goldie (14d 0/2) | headgear - | last run 80 days | form 133425 | MARKET 4.5% | 09:00 median 19.00 | Matchbook 22.00
    comment: Annandale has been in the frame often, with a second two starts back and thirds four and five runs ago, but he was only fifth last time and returns after 80 days off.
    DATA: model 11.5% | style Held up (led 3% of runs) | runs in data 12 | last 3: 13 Jul Ayr Flat 13.1f Good To Firm 4/6; 27 Aug Carlisle Flat 11.2f Good 2/9; 2 Sep Hamilton Flat 11.1f Soft 5/8
    DATA against: Official rating 58, 6 lb below field average; Pace: steady gallop likely, hard to come from off the pace
- Chicago Storm (hrs_29593102) | 7yo G | 136lb | OR 66 | draw 6 | jockey Millie Wonnacott(5) | trainer Barry Murtagh (14d 0/1) | headgear - | last run 18 days | form 35-416 | MARKET 3.9% | 09:00 median 23.00 | Matchbook 28.00
    comment: The risk is a sixth last time out, and he carries 136 lb.
    DATA: model 2.4% | style Midfield (led 3% of runs) | runs in data 8 | last 3: 24 Jul Uttoxeter Hurdle 15.8f Good 11/11; 22 Oct Carlisle Hurdle 20f Good 13/13; 3 Nov Sedgefield Hurdle 17f Good PU/11
    DATA against: Poor recent finishing positions
- Beckon (hrs_58843393) | 3yo F | 122lb | OR 57 | draw 3 | jockey Cam Hardie | trainer Susan Corbett (14d 1/7) | headgear t (1st time) | last run 51 days | form 399057 | MARKET 3.2% | 09:00 median 26.00 | Matchbook 32.00
    comment: Beckon is hard to fancy, having finished seventh last time out after a ninth and another ninth earlier, and she is winless in her last six starts after a third six starts back. She has run over today's trip and going and the 51-day break is a query, though her 122 lb is workable off an official mark of 57.
    DATA: model 4.8% | style Midfield (led 3% of runs) | runs in data 7 | last 3: 9 Sep Redcar Flat 8f Good 14/19; 25 Sep Newcastle Flat 12.4f Standard 5/12; 1 Oct Newcastle Flat 12.4f Standard 7/11
    DATA for: Carries 11 lb less than average; First-time headgear
    DATA against: Official rating 57, 7 lb below field average

## 3:29 Newcastle (AW) | race_id rac_32305109161 | Make The Move To Midnite Handicap Stakes (Div II)
Flat | Class 5 | 1m4f98y | going Standard | AW | 9 runners | rating band 0-70 | age 3yo+
DATA pace: Lone leader - Rory's Gold is the only habitual front-runner and may be allowed an easy lead.
- Humble Spark (hrs_28532693) | 6yo G | 140lb | OR 70 | draw 6 | jockey Lauren Young(5) | trainer Jim Goldie (14d 0/2) | headgear p | last run 15 days | form 665947 | MARKET 27.7% | 09:00 median 3.00 | Matchbook 3.45 | CHECK (skip line 2.85)
    comment: Humble Spark is yet to win in his last six, with a fourth two starts back his best finish, but he's fresh from a 15-day break and has run over today's trip and going before.
    DATA: model 7.9% | style Midfield (led 5% of runs) | runs in data 16 | last 3: 21 Sep Hamilton Flat 12.1f Soft 9/12; 30 Sep Musselburgh Flat 8.9f Good To Soft 4/6; 6 Nov Newcastle (AW) Flat 10f Standard 7/14 fig 68
    DATA for: Best recent form figure 68, 7 lb above field average; Official rating 70, 8 lb above field average
    DATA against: Carries 8 lb more than average
- Rory's Gold (hrs_47065046) | 4yo G | 135lb | OR 65 | draw 2 | jockey Amie Waugh(3) | trainer Simon Waugh (14d 0/0) | headgear - | last run 22 days | form 873102 | MARKET 17.3% | 09:00 median 5.00 | Matchbook 5.40
    DATA: model 20.7% | style Leader (led 38% of runs) | runs in data 10 | last 3: 25 Sep Newcastle Flat 10.2f Standard 1/14; 8 Oct Ayr Flat 8f Heavy 10/13; 30 Oct Newcastle (AW) Flat 10f Standard 2/14 fig 64
    DATA for: Good recent finishing positions; Pace: may get an uncontested lead
- Kartini (hrs_412692889) | 4yo F | 133lb | OR 63 | draw 8 | jockey Tom Eaves | trainer Simon Whitaker (14d 0/2) | headgear - | last run 17 days | form 654712 | MARKET 13.5% | 09:00 median 5.50 | Matchbook 7.80
    comment: She has run over today's trip and going, and carries 133 lb.
    DATA: model 19.1% | style Held up (led 3% of runs) | runs in data 8 | last 3: 3 Oct Redcar Flat 10f Good 7/9; 26 Oct Redcar Flat 10f Heavy 1/14 fig 65; 4 Nov Musselburgh Flat 12.5f Soft 2/11 fig 64
    DATA for: Best recent form figure 65, 4 lb above field average; Last-run finishing speed +6.3% vs that field (finished strongly); Good recent finishing positions
- Regalian (hrs_50187746) | 4yo G | 136lb | OR 66 | draw 4 | jockey David Nolan | trainer Tony Coyle & Kaine Wood (14d 0/0) | headgear p | last run 23 days | form 886897 | MARKET 11.8% | 09:00 median 7.50 | Matchbook 7.80
    comment: The risk is obvious, though: he is winless in his last six, with a seventh last time out his best finish in that spell bar a sixth four starts back.
    DATA: model 9.3% | style Held up (led 3% of runs) | runs in data 8 | last 3: 29 Aug Beverley Flat 8.5f Soft 8/10; 12 Oct Newcastle Flat 7.1f Standard 9/13; 29 Oct Southwell (AW) Flat 11f Standard 7/10 fig 62
    DATA against: Poor recent finishing positions
- Elemental Eye (hrs_34472123) | 5yo G | 137lb | OR 67 | draw 5 | jockey Andrew Mullen | trainer Iain Jardine (14d 0/5) | headgear b | last run 18 days | form 531278 | MARKET 8.9% | 09:00 median 9.00 | Matchbook 11.50
    comment: The risk is a poor recent run, with an eighth last time out and a seventh the start before.
    DATA: model 21.3% | style Midfield (led 3% of runs) | runs in data 11 | last 3: 24 Sep Perth Hurdle 16.2f Good 1/9; 16 Oct Newcastle (AW) Flat 12.5f Standard 8/12 fig 60; 3 Nov Sedgefield Hurdle 17f Good 2/11 fig 98
    DATA for: Official rating 67, 5 lb above field average; Last-run finishing speed +2.6% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Recent figures 7 lb below its current mark (looks high in the weights); Carries 5 lb more than average
- Spirit of Nature (hrs_55731998) | 4yo G | 121lb | OR 49 | draw 3 | jockey Joanna Mason | trainer Jim Goldie (14d 0/2) | headgear - | last run 28 days | form 706720 | MARKET 8.4% | 09:00 median 10.00 | Matchbook 11.50
    comment: Winless in his last six and unplaced last time out, Spirit of Nature has a single second two starts back to show amid a string of sevenths and sixths, so he is hard to fancy.
    DATA: model 4.5% | style Held up (led 3% of runs) | runs in data 6 | last 3: 2 Sep Hamilton Flat 11.1f Soft 7/8; 25 Sep Newcastle Flat 12.4f Standard 2/12; 24 Oct Southwell (AW) Flat 12f Standard 13/14
    DATA for: Carries 11 lb less than average
    DATA against: Official rating 49, 13 lb below field average
- Royal Blaze (hrs_35336700) | 5yo G | 132lb | OR 62 | draw 9 | jockey Greg Fairley | trainer Ewan Whillans (14d 0/9) | headgear tp | last run 44 days | form 391108 | MARKET 6.8% | 09:00 median 13.00 | Matchbook 13.50
    comment: Royal Blaze has slipped to an eighth last time out and unplaced the start before, after back-to-back wins three and four starts back, so he is hard to fancy after 44 days off.
    DATA: model 9.8% | style Midfield (led 3% of runs) | runs in data 9 | last 3: 27 Jul Ayr Flat 10f Good To Firm 1/9; 10 Aug Ayr Flat 10f Good To Soft 10/11; 8 Oct Ayr Flat 10f Heavy 8/12
    DATA against: Trainer 0 wins from 9 runs, last 14 days
- Dragonflame (hrs_43287741) | 4yo G | 127lb | OR 57 | draw 1 | jockey Rowan Scott | trainer Rebecca Menzies (14d 0/9) | headgear p (1st time) | last run 35 days | form 0-9060 | MARKET 2.8% | 09:00 median 34.00 | Matchbook 42.00
    comment: Dragonflame is winless in his last five and was unplaced last time, with a sixth two starts back his best recent effort, though he has run on today's going and returns after 35 days off.
    DATA: model 2.1% | style Midfield (led 29% of runs) | runs in data 4 | last 3: 2 Sep Newcastle Flat 8f Standard 10/11; 25 Sep Haydock Flat 10.2f Soft 6/7; 17 Oct Catterick Flat 14f Good 10/10 fig 45
    DATA for: Carries 5 lb less than average; First-time headgear
    DATA against: Best recent form figure 45, 16 lb below field average; Recent figures 12 lb below its current mark (looks high in the weights); Trainer 0 wins from 9 runs, last 14 days; Poor recent finishing positions
- Spooky Wooky (hrs_53960179) | 4yo G | 127lb | OR 57 | draw 7 | jockey Aiden Brookes | trainer Simon West (14d 0/2) | headgear tp (1st time) | last run 71 days | form 36-74P | MARKET 2.7% | 09:00 median 34.00 | Matchbook 36.00
    comment: The risk is a pulled-up effort last time and 71 days off, so he needs to bounce back.
    DATA: model 5.3% | style Prominent (led 38% of runs) | runs in data 3 | last 3: 5 Jul Southwell Flat 14.1f Standard 7/7; 8 Aug Redcar Flat 14f Good To Firm 4/9; 11 Sep Chester Flat 15.9f Good To Soft PU/12
    DATA for: Carries 5 lb less than average; First-time headgear

## 4:00 Newcastle (AW) | race_id rac_32305111098 | All-Weather Championship Is Back Restricted Novice Stakes (For Horses In Bands B, C And D) (GBB Race)
Flat | Class 5 | 6f | going Standard | AW | 6 runners | rating band - | age 2yo
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Bondy Boy (hrs_17389254484) | 2yo C | 130lb | OR - | draw 3 | jockey Oisin Murphy | trainer Geoff Oldroyd (14d 0/1) | headgear - | last run 14 days | form 2 | MARKET 74.8% | 09:00 median 1.17 | Matchbook 1.22
    DATA: model 61.9% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 7 Nov Southwell (AW) Flat 6f Standard 2/13 fig 63
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Clink (hrs_60819339) | 2yo C | 133lb | OR - | draw 5 | jockey Hollie Doyle | trainer Heather Main (14d 0/1) | headgear - | last run 26 days | form 09 | MARKET 6.2% | 09:00 median 12.00 | Matchbook 19.00
    DATA: model 5.8% | style Prominent (led 8% of runs) | runs in data 2 | last 3: 25 Sep Newmarket Flat 7f Good 13/14; 26 Oct Kempton (AW) Flat 7f Standard / Slow 9/10 fig 42
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Maiden's Bower (hrs_17395824341) | 2yo G | 130lb | OR - | draw 4 | jockey Sam James | trainer Phillip Makin (14d 0/3) | headgear h (1st time) | last run - days | form - | MARKET 6.1% | 09:00 median 13.00 | Matchbook 17.50
    DATA: model 9.7% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: First-time headgear
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Maharry (hrs_17395823298) | 2yo F | 125lb | OR - | draw 1 | jockey Clifford Lee | trainer Craig Lidster (14d 0/1) | headgear - | last run - days | form - | MARKET 5.7% | 09:00 median 12.00 | Matchbook 23.00
    DATA: model 9.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Obsidian Bay (hrs_17395556290) | 2yo F | 122lb | OR - | draw 6 | jockey Kieran O'Neill | trainer Jennie Candlish (14d 3/20) | headgear - | last run - days | form - | MARKET 4.4% | 09:00 median 17.00 | Matchbook 26.00
    DATA: model 9.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Havana Cohiba (hrs_66586002) | 2yo G | 130lb | OR - | draw 2 | jockey Oisin Orr | trainer Edward Bethell (14d 0/4) | headgear - | last run 61 days | form 05 | MARKET 2.9% | 09:00 median 34.00 | Matchbook 36.00
    DATA: model 3.7% | style Prominent (led 8% of runs) | runs in data 2 | last 3: 10 Jul Chester Flat 6.1f Good 12/12; 21 Sep Hamilton Flat 5f Soft 5/5
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on

## 4:30 Newcastle (AW) | race_id rac_32305113035 | AWC Finals Day At Newcastle 26th March Nursery Handicap Stakes
Flat | Class 6 | 1m5y | going Standard | AW | 9 runners | rating band 0-65 | age 2yo
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Eagle Storm (hrs_17389956423) | 2yo F | 131lb | OR 60 | draw 8 | jockey Jason Hart | trainer Jennie Candlish (14d 3/20) | headgear - | last run 15 days | form 8361 | MARKET 27.9% | 09:00 median 3.00 | Matchbook 3.40 | CHECK (skip line 2.85)
    comment: The main risk is her 131 lb from draw 8, with a sixth and an eighth in her last four showing she isn't consistent.
    DATA: model 10.1% | style Midfield (led 4% of runs) | runs in data 4 | last 3: 17 Aug Wolverhampton Flat 7.2f Standard 3/8; 8 Oct Southwell Flat 6.1f Standard 6/11; 6 Nov Newcastle (AW) Flat 7f Standard 1/11 fig 61
    DATA for: Best recent form figure 61, 12 lb above field average; Last-run finishing speed +2.3% vs that field (finished strongly); Good recent finishing positions
- Court Legend (hrs_65610426) | 2yo G | 135lb | OR 64 | draw 9 | jockey Joanna Mason | trainer Michael & David Easterby (14d 0/3) | headgear - | last run 66 days | form 050213 | MARKET 19.4% | 09:00 median 4.50 | Matchbook 4.90
    comment: He has run over today's trip, though 66 days off is a mild reservation.
    DATA: model 26.4% | style Held up (led 5% of runs) | runs in data 6 | last 3: 13 Aug Beverley Flat 7.3f Good To Firm 2/10; 30 Aug Beverley Flat 7.3f Heavy 1/9; 16 Sep Beverley Flat 8.5f Good 3/5
    DATA for: Official rating 64, 6 lb above field average; Good recent finishing positions
    DATA against: Carries 6 lb more than average; Pace: steady gallop likely, hard to come from off the pace
- Benedetti (hrs_17392241636) | 2yo F | 135lb | OR 64 | draw 3 | jockey Oisin Orr | trainer Edward Bethell (14d 0/4) | headgear - | last run 15 days | form 44 | MARKET 13.1% | 09:00 median 7.00 | Matchbook 7.00
    comment: Benedetti has finished fourth in both recent outings, including last time out 15 days ago, and has run over today's trip and going before.
    DATA: model 17.8% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 16 Sep Beverley Flat 7.3f Good 4/8; 6 Nov Newcastle (AW) Flat 7f Standard 4/10 fig 55
    DATA for: Best recent form figure 55, 6 lb above field average; Official rating 64, 6 lb above field average
    DATA against: Recent figures 9 lb below its current mark (looks high in the weights); Carries 6 lb more than average; Lightly raced: 2 runs in our data, so the model has little to go on
- Sankhum Galaxy (hrs_17390210915) | 2yo C | 119lb | OR 48 | draw 5 | jockey Andrew Mullen | trainer Ben Haslam (14d 3/6) | headgear - | last run 15 days | form 80636 | MARKET 11.6% | 09:00 median 7.50 | Matchbook 8.20
    comment: Winless in his last five, Sankhum Galaxy was a sixth last time out, and his only top-three finish was a third two starts back, so he is hard to fancy.
    DATA: model 7.0% | style Held up (led 3% of runs) | runs in data 5 | last 3: 9 Sep Redcar Flat 6f Good 6/7; 2 Oct Newcastle Flat 7.1f Standard 3/10; 6 Nov Newcastle (AW) Flat 7f Standard 6/11 fig 41
    DATA for: Trainer 50% wins (3/6), last 14 days; Carries 10 lb less than average
    DATA against: Best recent form figure 41, 8 lb below field average; Recent figures 7 lb below its current mark (looks high in the weights); Official rating 48, 10 lb below field average; Pace: steady gallop likely, hard to come from off the pace
- Adoramus (hrs_64167943) | 2yo C | 133lb | OR 62 | draw 1 | jockey Clifford Lee | trainer Jack Morland (14d 0/0) | headgear b (1st time) | last run 39 days | form 3567 | MARKET 9.8% | 09:00 median 9.00 | Matchbook 9.60
    comment: The risk is a slide to a seventh last time, a sixth two starts back and a fifth before that, so he is yet to show he's turning that around after 39 days off.
    DATA: model 10.7% | style Midfield (led 4% of runs) | runs in data 4 | last 3: 22 May Pontefract Flat 6f Good To Soft 5/9; 29 Jun Windsor Flat 6.1f Good To Firm 6/11; 13 Oct Leicester Flat 8.2f Good To Soft 7/10
    DATA for: First-time headgear
- Rubyroo (hrs_17390420558) | 2yo F | 134lb | OR 63 | draw 6 | jockey Rowan Scott | trainer Hugo Palmer (14d 0/0) | headgear p | last run 15 days | form 3752 | MARKET 9.7% | 09:00 median 8.50 | Matchbook 10.50
    comment: The main risk is that she is yet to win, with a fifth and a seventh also in the last four starts.
    DATA: model 9.4% | style Held up (led 3% of runs) | runs in data 4 | last 3: 3 Sep Salisbury Flat 7f Good To Soft 7/8; 28 Sep Wolverhampton Flat 7.2f Standard 5/7; 6 Nov Newcastle (AW) Flat 8f Standard 2/5 fig 59
    DATA for: Best recent form figure 59, 10 lb above field average; Official rating 63, 5 lb above field average
    DATA against: Carries 5 lb more than average; Pace: steady gallop likely, hard to come from off the pace
- Wild Orchid (hrs_17389468299) | 2yo F | 124lb | OR 53 | draw 2 | jockey Jack Callan | trainer Charlie Johnston (14d 0/5) | headgear - | last run 16 days | form 475418 | MARKET 4.8% | 09:00 median 17.00 | Matchbook 22.00
    comment: Wild Orchid won two starts back but was beaten into eighth last time out, and she's been mixed otherwise in recent runs; she has run over today's trip and going, and returns after 16 days.
    DATA: model 13.3% | style Prominent (led 4% of runs) | runs in data 6 | last 3: 17 Sep Yarmouth Flat 8f Good 4/10; 28 Sep Brighton Flat 8f Good To Firm 1/13; 5 Nov Chelmsford (AW) Flat 10f Standard 8/9 fig 31
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 31, 18 lb below field average; Recent figures 22 lb below its current mark (looks high in the weights)
- Aurora Valkyrie (hrs_64779722) | 2yo F | 126lb | OR 55 | draw 7 | jockey Sam James | trainer Phillip Makin (14d 0/3) | headgear - | last run 50 days | form 853740 | MARKET 2.1% | 09:00 median 41.00 | Matchbook 55.00
    comment: Winless in her last six, Aurora Valkyrie was unplaced last time and a fourth two starts back, and a 50-day break does little to help a filly who has run over today's trip and going.
    DATA: model 3.6% | style Prominent (led 29% of runs) | runs in data 6 | last 3: 31 Jul Musselburgh Flat 7.1f Good 7/7; 27 Aug Carlisle Flat 7.8f Good 4/5; 2 Oct Newcastle Flat 7.1f Standard 10/10
    DATA against: Last-run finishing speed -7.5% vs that field (faded)
- Mohangel (hrs_60821509) | 2yo F | 122lb | OR 51 | draw 4 | jockey Cam Hardie | trainer Michael Appleby (14d 0/8) | headgear p | last run 44 days | form 0960 | MARKET 1.6% | 09:00 median 41.00 | Matchbook 120.00
    comment: Mohangel is winless in her last four, finishing unplaced last time, a sixth two starts back and a ninth three starts back, after 44 days off.
    DATA: model 1.8% | style Held up (led 8% of runs) | runs in data 4 | last 3: 8 Jul Kempton Flat 6f Standard To Slow 9/9; 22 Sep Southwell Flat 7.1f Standard 6/10; 8 Oct Southwell Flat 8.1f Standard 11/11
    DATA for: Carries 7 lb less than average
    DATA against: Official rating 51, 7 lb below field average; Trainer 0 wins from 8 runs, last 14 days; Last-run finishing speed -2.0% vs that field (faded); Poor recent finishing positions; Pace: steady gallop likely, hard to come from off the pace

## 5:00 Newcastle (AW) | race_id rac_32305114972 | AWC Season 14 Has Begun Novice Stakes (GBB Race)
Flat | Class 4 | 5f | going Standard | AW | 6 runners | rating band - | age 2yo
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Cornichon (hrs_17392412688) | 2yo C | 133lb | OR 72 | draw 5 | jockey Callum Rodriguez | trainer Roger Varian (14d 3/5) | headgear - | last run 41 days | form 42 | MARKET 69.7% | 09:00 median 1.30 | Matchbook 1.34
    DATA: model 70.6% | style Held up (led 5% of runs) | runs in data 2 | last 3: 18 Sep Newbury Flat 6f Good 4/15; 11 Oct Goodwood Flat 6f Good To Soft 2/8
    DATA for: Official rating 72, 14 lb above field average; Trainer 60% wins (3/5), last 14 days
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Debutante (hrs_66586072) | 2yo F | 128lb | OR - | draw 2 | jockey Ashley Lewis(3) | trainer Ed Walker (14d 0/9) | headgear t | last run 17 days | form 43 | MARKET 15.0% | 09:00 median 5.00 | Matchbook 7.40
    DATA: model 3.6% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 25 Jul Salisbury Flat 6f Good To Firm 4/4; 4 Nov Nottingham Flat 5f Soft 3/4 fig 46
    DATA against: Best recent form figure 46, 6 lb below field average; Trainer 0 wins from 9 runs, last 14 days; Lightly raced: 2 runs in our data, so the model has little to go on
- Kalahari Flame (hrs_64168041) | 2yo F | 128lb | OR - | draw 4 | jockey Andrew Mullen | trainer Ben Haslam (14d 3/6) | headgear - | last run 25 days | form 93 | MARKET 4.8% | 09:00 median 17.00 | Matchbook 22.00
    DATA: model 6.3% | style Held up (led 5% of runs) | runs in data 2 | last 3: 16 May Thirsk Flat 5f Good 9/10; 27 Oct Catterick Flat 5f Soft 3/9 fig 52
    DATA for: Trainer 50% wins (3/6), last 14 days
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Steel At Heart (hrs_17393472376) | 2yo G | 133lb | OR - | draw 6 | jockey Jason Hart | trainer John & Sean Quinn (14d 1/4) | headgear - | last run 14 days | form 5 | MARKET 4.3% | 09:00 median 23.00 | Matchbook 22.00
    DATA: model 4.8% | style Unknown | runs in data 1 | last 3: 7 Nov Doncaster Flat 6f Good To Soft 5/6 fig 53
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Time And Effort (hrs_64812916) | 2yo F | 128lb | OR 57 | draw 1 | jockey Rhys Elliott(5) | trainer Patrick Morris (14d 0/5) | headgear - | last run 29 days | form 028846 | MARKET 4.3% | 09:00 median 19.00 | Matchbook 25.00
    DATA: model 11.3% | style Midfield (led 4% of runs) | runs in data 7 | last 3: 7 Sep Wolverhampton Flat 5.1f Standard 8/11; 21 Sep Wolverhampton Flat 5.1f Standard 4/9; 23 Oct Wolverhampton (AW) Flat 6f Standard 6/13 fig 57
    DATA for: Best recent form figure 57, 5 lb above field average
- Bea Kindly (hrs_63810180) | 2yo F | 128lb | OR 45 | draw 3 | jockey Barry McHugh | trainer Tracy Waggott (14d 0/2) | headgear - | last run 88 days | form 96905 | MARKET 1.8% | 09:00 median 41.00 | Matchbook 90.00
    DATA: model 3.3% | style Midfield (led 4% of runs) | runs in data 5 | last 3: 16 May Thirsk Flat 5f Good 9/12; 24 Jul Thirsk Flat 6f Good To Firm 12/12; 25 Aug Musselburgh Flat 5f Good 5/7
    DATA against: Official rating 45, 13 lb below field average

## 5:30 Newcastle (AW) | race_id rac_32305116909 | Midnite: Built For 2026 Not 2006 Handicap Stakes
Flat | Class 6 | 5f | going Standard | AW | 14 runners | rating band 0-55 | age 3yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Uncle Sam (hrs_412652982) | 4yo G | 129lb | OR 49 | draw 8 | jockey Jason Hart | trainer Ray Craggs (14d 0/0) | headgear p | last run 28 days | form -26323 | MARKET 20.8% | 09:00 median 3.75 | Matchbook 4.40 | CHECK (skip line 3.56)
    comment: Uncle Sam arrives in solid nick, with a third last time out, a second two starts back and a third three starts before that, and he has run over today's trip and going.
    DATA: model 13.9% | style Prominent (led 23% of runs) | runs in data 5 | last 3: 3 Sep Newcastle Flat 6f Standard 3/8; 25 Sep Newcastle Flat 6f Standard 2/12; 24 Oct Southwell (AW) Flat 6f Standard 3/11 fig 57
    DATA for: Best recent form figure 57, 13 lb above field average; Recent figures 8 lb above its current mark (looks well handicapped); Good recent finishing positions
- Ganesha (hrs_35624883) | 5yo G | 132lb | OR 52 | draw 12 | jockey Sam James | trainer Phillip Makin (14d 0/3) | headgear - | last run 17 days | form 560507 | MARKET 15.7% | 09:00 median 5.00 | Matchbook 5.70
    comment: The risk is plain: he's winless in his last six, with a seventh last time out.
    DATA: model 5.6% | style Prominent (led 5% of runs) | runs in data 9 | last 3: 21 May Musselburgh Flat 5f Good 5/8; 12 Oct Musselburgh Flat 5f Good To Soft 12/14; 4 Nov Musselburgh Flat 5f Soft 7/11 fig 43
    DATA against: Recent figures 9 lb below its current mark (looks high in the weights)
- Ardaddy (hrs_41189645) | 4yo G | 130lb | OR 50 | draw 6 | jockey Clifford Lee | trainer Michael Appleby (14d 0/8) | headgear - | last run 23 days | form 465730 | MARKET 8.9% | 09:00 median 9.45 | Matchbook 9.60
    comment: Ardaddy is yet to win in his last six starts, though a third two runs back shows he can get involved, and he has run over today's trip and going before.
    DATA: model 5.4% | style Prominent (led 4% of runs) | runs in data 11 | last 3: 28 Mar Southwell Flat 8.1f Standard 7/8; 11 Apr Southwell Flat 7.1f Standard 3/9; 29 Oct Southwell (AW) Flat 7f Standard 13/13 fig 20
    DATA against: Best recent form figure 20, 24 lb below field average; Recent figures 30 lb below its current mark (looks high in the weights); Trainer 0 wins from 8 runs, last 14 days
- Khabib (hrs_22111509) | 8yo G | 131lb | OR 51 | draw 5 | jockey Oisin Orr | trainer Ray Craggs (14d 0/0) | headgear b | last run 46 days | form 897436 | MARKET 8.4% | 09:00 median 9.00 | Matchbook 11.50
    comment: Khabib was a sixth last time out and a third two starts back, so he has shown a flicker of form, though he is winless in his last six and returns after 46 days off.
    DATA: model 11.8% | style Midfield (led 3% of runs) | runs in data 7 | last 3: 19 Sep Newcastle Flat 5f Standard 4/9; 25 Sep Newcastle Flat 5f Standard 3/8; 6 Oct Southwell Flat 5f Standard 6/11
    DATA against: Aged 8, older than most of this field
- Pivotal Terms (hrs_56127785) | 3yo F | 135lb | OR 55 | draw 7 | jockey Andrew Mullen | trainer Iain Jardine (14d 0/5) | headgear - | last run 26 days | form 504712 | MARKET 8.1% | 09:00 median 8.00 | Matchbook 14.50
    comment: Pivotal Terms booked a second last time out and a win two starts back, and she returns after a fresh 26 days with experience of both today's trip and going.
    DATA: model 15.2% | style Held up (led 5% of runs) | runs in data 13 | last 3: 2 Sep Newcastle Flat 5f Standard 7/9; 17 Oct Southwell (AW) Flat 6f Standard 1/12 fig 55; 26 Oct Southwell (AW) Flat 5f Standard 2/9 fig 61
    DATA for: Best recent form figure 61, 17 lb above field average; Recent figures 6 lb above its current mark (looks well handicapped); Last-run finishing speed +2.4% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Auradue (hrs_64257935) | 4yo F | 131lb | OR 51 | draw 9 | jockey Alistair Rawlinson | trainer Roy Bowring (14d 0/0) | headgear b | last run 26 days | form 664781 | MARKET 8.0% | 09:00 median 9.50 | Matchbook 12.00
    comment: Auradue won last time out, but that sits among a string of sixth, sixth, fourth, seventh and eighth finishes before it, and carrying 131 lb from draw 9 she is hard to fancy. On the plus side, she has run over today's trip and going, and is fresh enough after 26 days.
    DATA: model 7.8% | style Prominent (led 5% of runs) | runs in data 6 | last 3: 25 Jul Newcastle Flat 5f Standard To Slow 7/10; 15 Oct Southwell (AW) Flat 7f Standard 8/11 fig 34; 26 Oct Southwell (AW) Flat 5f Standard 1/9 fig 55
    DATA for: Best recent form figure 55, 11 lb above field average; Recent figures 4 lb above its current mark (looks well handicapped); Has won at this trip or further
- Zuffolo (hrs_29229088) | 6yo G | 134lb | OR 54 | draw 1 | jockey Rhys Elliott(5) | trainer Michael Dods (14d 0/5) | headgear b | last run 36 days | form 313832 | MARKET 6.4% | 09:00 median 9.50 | Matchbook 18.50
    comment: Zuffolo bids to build on a second last time out, with a third two starts back and a winner five starts back showing he's consistent, and he has run over today's trip and going.
    DATA: model 11.3% | style Prominent (led 38% of runs) | runs in data 10 | last 3: 15 Sep Redcar Flat 5f Good 8/13; 30 Sep Catterick Flat 5f Good 3/7; 16 Oct Newcastle (AW) Flat 5f Standard 2/10 fig 55
    DATA for: Best recent form figure 55, 11 lb above field average; Has won at this trip or further; Good recent finishing positions
- Spun To Gold (hrs_36836982) | 5yo G | 130lb | OR 50 | draw 13 | jockey Lauren Young(5) | trainer Jim Goldie (14d 0/2) | headgear - | last run 15 days | form 253560 | MARKET 6.4% | 09:00 median 12.00 | Matchbook 15.50
    comment: Spun To Gold has run over today's trip and going, and returns just 15 days after an unplaced effort, having finished a third four starts back and a second six starts back.
    DATA: model 6.2% | style Held up (led 5% of runs) | runs in data 7 | last 3: 21 Mar Newcastle Flat 6f Standard 5/8; 30 Mar Wolverhampton Flat 6.1f Standard 6/12; 6 Nov Newcastle (AW) Flat 6f Standard 10/14 fig 48
    DATA for: Best recent form figure 48, 4 lb above field average
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- What What What (hrs_44417646) | 4yo G | 130lb | OR 50 | draw 3 | jockey Joanna Mason | trainer Michael & David Easterby (14d 0/3) | headgear - | last run 172 days | form 391073 | MARKET 5.0% | 09:00 median 15.00 | Matchbook 19.50
    comment: Third last time out and a winner four starts back, he has been in the frame in three of his last six, but a 172-day absence raises fitness questions, and he has run over today's trip and going before.
    DATA: model 4.2% | style Midfield (led 3% of runs) | runs in data 8 | last 3: 18 Apr Thirsk Flat 6f Good 15/17; 30 Apr Southwell Flat 6.1f Standard 7/7; 2 Jun Newcastle Flat 5f Standard 3/8
    DATA for: Has won at this trip or further
    DATA against: Returns from a 172-day break
- Doon The Glen (hrs_36079939) | 6yo G | 127lb | OR 47 | draw 2 | jockey Shane Gray | trainer Jim Goldie (14d 0/2) | headgear v | last run 32 days | form 755646 | MARKET 4.1% | 09:00 median 21.00 | Matchbook 22.00
    comment: He has run over today's trip and going, and a 47 official mark offers some hope.
    DATA: model 6.0% | style Midfield (led 4% of runs) | runs in data 21 | last 3: 2 Sep Hamilton Flat 6f Soft 6/13; 20 Sep Hamilton Flat 5f Heavy 4/8; 20 Oct Newcastle (AW) Flat 5f Standard 6/10 fig 43
    DATA for: Has won at this trip or further
- Queensmaite (hrs_51491559) | 4yo F | 131lb | OR 51 | draw 10 | jockey Finley Marsh | trainer Roy Bowring (14d 0/0) | headgear b (1st time) | last run 112 days | form 57-890 | MARKET 2.7% | 09:00 median 29.00 | Matchbook 38.00
    comment: Queensmaite has been drifting through her recent runs, unplaced last time, then a ninth, an eighth, a seventh and a fifth, and she returns after 112 days off. She has run over today's trip and going and sits on 51 officially, but 131 lb from stall 10 is a big ask for a winless filly.
    DATA: model 2.7% | style Unknown | runs in data 3 | last 3: 9 Apr Southwell Flat 5f Standard 8/8; 28 Apr Southwell Flat 6.1f Standard 9/10; 1 Aug Doncaster Flat 7f Good To Firm 11/11
    DATA for: First-time headgear
    DATA against: Last-run finishing speed -5.3% vs that field (faded); Poor recent finishing positions; Returns from a 112-day break
- Monticristo Boy (hrs_42042161) | 4yo G | 127lb | OR 47 | draw 4 | jockey Oisin McSweeney | trainer Peter Niven (14d 0/1) | headgear - | wind surgery | last run 194 days | form 4785-9 | MARKET 2.4% | 09:00 median 34.00 | Matchbook 44.00
    comment: Monticristo Boy is winless in his last five, finishing ninth last time out and no better than a fourth five starts back, and he returns after 194 days off.
    DATA: model 3.3% | style Unknown | runs in data 1 | last 3: 11 May Catterick Flat 5f Good 9/11
    DATA against: Returns from a 194-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Great Success (hrs_55882456) | 3yo G | 126lb | OR 46 | draw 11 | jockey Kieran O'Neill | trainer Scott Dixon (14d 0/0) | headgear b | last run 26 days | form 450059 | MARKET 1.7% | 09:00 median 34.00 | Matchbook 90.00
    comment: Great Success is yet to win in his last six starts and was a ninth last time out, though a fifth two starts back shows he can run respectably, and he has run over today's trip and going.
    DATA: model 2.9% | style Prominent (led 4% of runs) | runs in data 9 | last 3: 31 Aug Southwell Flat 6.1f Standard 11/12; 16 Oct Newcastle (AW) Flat 5f Standard 5/10 fig 47; 26 Oct Southwell (AW) Flat 5f Standard 9/9 fig 21
    DATA against: Last-run finishing speed -2.2% vs that field (faded)
- Sands of Seve (hrs_52055024) | 3yo G | 128lb | OR 48 | draw 14 | jockey Billy Garritty | trainer Stephen Hanlon (14d 0/0) | headgear - | last run 16 days | form 266540 | MARKET 1.4% | 09:00 median 41.00 | Matchbook 110.00
    comment: Sands of Seve is winless in his last six and has finished unplaced last time out, then a fourth, a fifth and two sixths, so he is hard to fancy. He has run over today's trip and going, and a second six starts back is his best effort.
    DATA: model 3.7% | style Unknown | runs in data 11 | last 3: 24 Aug Musselburgh Flat 5f Good 5/10; 2 Sep Newcastle Flat 5f Standard 4/9; 5 Nov Southwell (AW) Flat 5f Standard 13/13 fig 8
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 8, 36 lb below field average; Recent figures 40 lb below its current mark (looks high in the weights)

## 6:00 Newcastle (AW) | race_id rac_32305118846 | AW Trials Day - Lingfield 2nd Jan 2027 Handicap Stakes
Flat | Class 6 | 1m5y | going Standard | AW | 14 runners | rating band 0-65 | age 3yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Oppenheimer (hrs_54842515) | 3yo G | 136lb | OR 63 | draw 6 | jockey Hollie Doyle | trainer James Owen (14d 3/30) | headgear - | last run 18 days | form 400311 | MARKET 30.4% | 09:00 median 2.50 | Matchbook 3.00
    comment: Oppenheimer arrives in cracking nick, a winner last time out and again two starts back, just 18 days after his latest run, and he has run over today's trip and going.
    DATA: model 25.7% | style Held up (led 5% of runs) | runs in data 8 | last 3: 5 Oct Killarney Flat 8.1f Soft 3/15; 31 Oct Southwell (AW) Flat 8f Standard 1/14 fig 66; 3 Nov Wolverhampton (AW) Flat 7f Standard 1/11 fig 58
    DATA for: Best recent form figure 66, 7 lb above field average; Has won at this trip or further; Good recent finishing positions
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Our Dagger (hrs_37192281) | 5yo G | 134lb | OR 59 | draw 3 | jockey Finley Marsh | trainer Adrian Wintle (14d 1/2) | headgear - | last run 45 days | form 00-572 | MARKET 13.3% | 09:00 median 5.50 | Matchbook 7.00
    DATA: model 6.1% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 30 Mar Kempton Flat 7f Standard To Slow 5/6; 4 Aug Ffos Las Flat 7.4f Good 7/9; 7 Oct Kempton Flat 8f Standard To Slow 2/13
- Titainium (hrs_41130194) | 5yo G | 136lb | OR 61 | draw 2 | jockey Oliver Stammers | trainer Grant Tuer (14d 0/2) | headgear - | last run 14 days | form 876942 | MARKET 13.1% | 09:00 median 6.00 | Matchbook 6.80
    comment: Titainium comes here on the back of a second last time out, a fresh 14 days ago, and has run over today's trip and going, but he's yet to win in his last six starts and finished no better than a fourth in the five runs before that.
    DATA: model 8.9% | style Held up (led 3% of runs) | runs in data 6 | last 3: 24 Aug Musselburgh Flat 8.9f Good 9/11; 20 Oct Newcastle (AW) Flat 8f Standard 4/12 fig 58; 7 Nov Southwell (AW) Flat 8f Standard 2/11 fig 62
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Battle Standard (hrs_62202133) | 3yo G | 137lb | OR 64 | draw 9 | jockey Clifford Lee | trainer Jack Morland (14d 0/0) | headgear - | last run 29 days | form 04916 | MARKET 7.9% | 09:00 median 10.00 | Matchbook 11.50
    comment: Battle Standard won two starts back but was only sixth last time out, and a 29-day break gives him a fresh look; he has run over today's trip and going before.
    DATA: model 11.3% | style Held up (led 4% of runs) | runs in data 5 | last 3: 17 Apr Wolverhampton Flat 7.2f Standard 9/9; 15 Oct Southwell (AW) Flat 8f Standard 1/14 fig 69; 23 Oct Wolverhampton (AW) Flat 8.5f Standard 6/10 fig 46
    DATA for: Best recent form figure 69, 10 lb above field average; Recent figures 5 lb above its current mark (looks well handicapped); Has won at this trip or further
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Karakula Dancer (hrs_49142709) | 3yo G | 130lb | OR 57 | draw 7 | jockey Alice Bond(5) | trainer Martin Dunne (14d 0/2) | headgear p | last run 29 days | form 383348 | MARKET 5.8% | 09:00 median 11.00 | Matchbook 20.00
    comment: Winless in his last six, Karakula Dancer has still been third three times in that spell, including three and four starts back, and has run over today's trip and going, but a lowly eighth last time out after 29 days off tempers enthusiasm from stall seven.
    DATA: model 4.1% | style Midfield (led 4% of runs) | runs in data 14 | last 3: 9 Sep Kempton Flat 8f Standard To Slow 3/14; 30 Sep Kempton Flat 8f Standard To Slow 4/11; 23 Oct Wolverhampton (AW) Flat 8.5f Standard 8/11 fig 51
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 51, 8 lb below field average; Recent figures 6 lb below its current mark (looks high in the weights)
- Concert Boy (hrs_29917818) | 6yo G | 130lb | OR 55 | draw 11 | jockey Jason Hart | trainer Katie Scott (14d 0/2) | headgear b | last run 22 days | form 870641 | MARKET 5.5% | 09:00 median 13.00 | Matchbook 18.00
    comment: Last-time-out winner who has run over today's trip and on this going, but that was his only success in his last six starts, with a fourth, sixth and seventh before it, and he carries 130 lb from stall 11.
    DATA: model 6.6% | style Held up (led 3% of runs) | runs in data 16 | last 3: 10 Aug Ayr Flat 8f Good To Soft 6/10; 30 Sep Musselburgh Flat 7.1f Good To Soft 4/11; 30 Oct Newcastle (AW) Flat 7f Standard 1/11 fig 55
    DATA against: Best recent form figure 55, 4 lb below field average; Official rating 55, 5 lb below field average; Pace: steady gallop likely, hard to come from off the pace
- Mount King (hrs_30330090) | 6yo G | 138lb | OR 63 | draw 8 | jockey David Allan | trainer Tim Easterby (14d 1/8) | headgear tb | last run 23 days | form 465923 | MARKET 5.1% | 09:00 median 15.00 | Matchbook 19.50
    comment: Mount King arrives in decent heart, third last time out and a second two starts back, with a fresh 23-day break and experience of today's trip and going.
    DATA: model 7.6% | style Midfield (led 4% of runs) | runs in data 14 | last 3: 3 Oct Redcar Flat 8f Good 9/14; 5 Oct Pontefract Flat 8f Good 2/13; 29 Oct Southwell (AW) Flat 8f Standard 3/13 fig 62
    DATA for: Has won at this trip or further; Good recent finishing positions
- Asian Journey (hrs_54525618) | 5yo G | 132lb | OR 57 | draw 13 | jockey Rhys Elliott(5) | trainer Sam England (14d 4/23) | headgear t | last run 14 days | form 123857 | MARKET 3.8% | 09:00 median 19.00 | Matchbook 26.00
    comment: The main risk is a fading profile, having finished seventh last time out, and a fifth two starts back.
    DATA: model 4.1% | style Midfield (led 3% of runs) | runs in data 15 | last 3: 8 Oct Southwell Flat 8.1f Standard 8/12; 23 Oct Wolverhampton (AW) Flat 8.5f Standard 5/10 fig 55; 7 Nov Southwell (AW) Flat 8f Standard 7/11 fig 52
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 55, 4 lb below field average
- Starliner (hrs_35729652) | 5yo G | 139lb | OR 64 | draw 1 | jockey William Pyle | trainer Linda Perratt (14d 0/3) | headgear p | last run 22 days | form 221885 | MARKET 3.4% | 09:00 median 21.00 | Matchbook 30.00
    comment: Starliner makes plenty of appeal on profile: he has run over today's trip and on this going, and a win four starts back sits alongside a pair of seconds earlier in the form.
    DATA: model 5.9% | style Held up (led 4% of runs) | runs in data 21 | last 3: 17 Sep Ayr Flat 8f Soft 8/13; 20 Oct Newcastle (AW) Flat 8f Standard 8/12 fig 62; 30 Oct Newcastle (AW) Flat 7f Standard 5/10 fig 68
    DATA for: Best recent form figure 68, 9 lb above field average; Recent figures 4 lb above its current mark (looks well handicapped); Has won at this trip or further
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Harry The Rogue (hrs_35700049) | 5yo G | 138lb | OR 63 | draw 12 | jockey Jude Maher(7) | trainer Stephen Hanlon (14d 0/0) | headgear - | last run 25 days | form 000995 | MARKET 3.3% | 09:00 median 26.00 | Matchbook 28.00
    comment: Harry The Rogue is yet to win in his last six, but a fifth last time out, 25 days ago, suggests he's heading the right way, and he has run over today's trip and going before. The risk is a poor run of ninth-placed efforts before that, off 138 lb from draw 12.
    DATA: model 3.5% | style Midfield (led 23% of runs) | runs in data 10 | last 3: 2 Sep Newcastle Flat 8f Standard 9/11; 13 Oct Leicester Flat 8.2f Good To Soft 9/9; 27 Oct Wolverhampton (AW) Flat 8.5f Standard 5/10 fig 63
- Boubyan (hrs_43667057) | 4yo G | 138lb | OR 63 | draw 4 | jockey Kevin Stott | trainer Lawrence Mullaney (14d 0/1) | headgear p | last run 32 days | form 335516 | MARKET 3.0% | 09:00 median 26.00 | Matchbook 36.00
    comment: Boubyan was a winner two starts back but could only manage a sixth last time out, and he returns after 32 days having run over today's trip and going before.
    DATA: model 7.6% | style Midfield (led 8% of runs) | runs in data 15 | last 3: 29 Sep Wolverhampton Flat 12.2f Standard 5/6; 12 Oct Newcastle Flat 8f Standard 1/13; 20 Oct Newcastle (AW) Flat 8f Standard 6/12 fig 54
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 54, 5 lb below field average; Recent figures 9 lb below its current mark (looks high in the weights)
- Power Strike (hrs_62101676) | 3yo G | 134lb | OR 61 | draw 5 | jockey Ryan Sexton | trainer Julie Camacho (14d 1/4) | headgear - | wind surgery | last run 33 days | form 60777 | MARKET 2.3% | 09:00 median 34.00 | Matchbook 42.00
    comment: The one risk is a winless run of three straight sevenths, so he needs to find a little more.
    DATA: model 4.9% | style Prominent (led 23% of runs) | runs in data 5 | last 3: 9 Apr Gowran Park Flat 9.6f Soft 7/8; 31 Aug Southwell Flat 8.1f Standard 7/10; 19 Oct Southwell (AW) Flat 8f Standard 7/14 fig 59
    DATA for: Last-run finishing speed +2.3% vs that field (finished strongly)
    DATA against: Poor recent finishing positions
- Dolo's Star (hrs_58133579) | 3yo F | 135lb | OR 62 | draw 14 | jockey David Nolan | trainer Ivan Furtado (14d 1/9) | headgear p (1st time) | last run 32 days | form 420305 | MARKET 1.7% | 09:00 median 34.00 | Matchbook 85.00
    comment: Dolo's Star is winless in her last six, with a fifth last time out and an unplaced run before it, and her 32-day break does little to help. She has run over today's trip and going, and a second five starts back is the pick of her form, but she's hard to fancy from stall 14 with 135 lb on her back.
    DATA: model 2.1% | style Prominent (led 3% of runs) | runs in data 7 | last 3: 16 Jul Thirsk Flat 7f Good To Firm 3/3; 17 Sep Southwell Flat 8.1f Standard 12/12; 20 Oct Newcastle (AW) Flat 7f Standard 5/14 fig 60
    DATA for: First-time headgear
- Carwyn (hrs_54149872) | 3yo G | 124lb | OR 51 | draw 10 | jockey Alexandra Egan(5) | trainer Patrick Morris (14d 0/5) | headgear p | last run 19 days | form 990706 | MARKET 1.6% | 09:00 median 41.00 | Matchbook 80.00
    comment: Carwyn is winless in his last six, with a sixth last time out the best of a string of finishes that also includes two ninths, and that makes him hard to fancy. He has at least run over today's trip and going, is back after 19 days and runs off a lowly 51 from draw 10.
    DATA: model 1.4% | style Midfield (led 23% of runs) | runs in data 7 | last 3: 31 Aug Southwell Flat 11.1f Standard 7/7; 25 Sep Newcastle Flat 10.2f Standard 12/14; 2 Nov Wolverhampton (AW) Flat 8.5f Standard 6/8 fig 47
    DATA for: Carries 10 lb less than average
    DATA against: Best recent form figure 47, 12 lb below field average; Official rating 51, 9 lb below field average; Poor recent finishing positions

## 6:30 Newcastle (AW) | race_id rac_32305120783 | All-Weather Championship Season 14 Has Begun Handicap Stakes
Flat | Class 6 | 7f14y | going Standard | AW | 14 runners | rating band 0-65 | age 3yo+
DATA pace: Strong pace - 3 habitual front-runners (Fickle McSelfish, Tasever, Front Gunner). A contested lead should set things up for horses coming from behind.
- Oxford Circus (hrs_46078032) | 4yo G | 134lb | OR 61 | draw 8 | jockey Hollie Doyle | trainer James Owen (14d 3/30) | headgear v | last run 15 days | form 094511 | MARKET 40.2% | 09:00 median 1.91 | Matchbook 2.20
    comment: He has run over today's trip and going, but 134 lb from stall eight is a big ask.
    DATA: model 15.5% | style Held up (led 4% of runs) | runs in data 15 | last 3: 15 Oct Southwell (AW) Flat 8f Standard 5/14 fig 49; 31 Oct Southwell (AW) Flat 8f Standard 1/12 fig 54; 6 Nov Newcastle (AW) Flat 8f Standard 1/14 fig 55
    DATA for: Last-run finishing speed +3.1% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions; Pace: a contested lead should suit its hold-up style
    DATA against: Recent figures 6 lb below its current mark (looks high in the weights)
- Tough Enough (hrs_29918035) | 6yo G | 133lb | OR 60 | draw 14 | jockey Ethan Tindall(5) | trainer Antony Brittain (14d 1/11) | headgear - | last run 16 days | form 064076 | MARKET 6.9% | 09:00 median 11.00 | Matchbook 13.50
    comment: The risk is a winless run in his last six starts, with nothing better than a fourth four starts back.
    DATA: model 5.1% | style Held up (led 8% of runs) | runs in data 8 | last 3: 24 Jul York Flat 6f Good To Firm 12/21; 16 Aug Southwell Flat 6.1f Standard 7/14; 5 Nov Southwell (AW) Flat 6f Standard 6/9 fig 55
    DATA for: Pace: a contested lead should suit its hold-up style
    DATA against: Poor recent finishing positions
- Forest Phoenix (hrs_63390327) | 3yo G | 135lb | OR 63 | draw 7 | jockey David Allan | trainer Tim Easterby (14d 1/8) | headgear - | last run 30 days | form 810804 | MARKET 6.7% | 09:00 median 11.00 | Matchbook 14.50
    comment: Forest Phoenix comes into this on the back of a fourth last time out, 30 days ago, and he has run over today's trip and on the going before.
    DATA: model 3.6% | style Prominent (led 5% of runs) | runs in data 8 | last 3: 10 Jul York Flat 7.9f Good To Firm 8/11; 25 Jul York Flat 7f Good To Firm 11/12; 22 Oct Newmarket Flat 7f Soft 4/12 fig 75
    DATA for: Best recent form figure 75, 19 lb above field average; Recent figures 12 lb above its current mark (looks well handicapped)
- Jkr Cobbler (hrs_25637822) | 7yo G | 136lb | OR 63 | draw 13 | jockey Shay Farmer(5) | trainer Iain Jardine (14d 0/5) | headgear - | last run 17 days | form 149919 | MARKET 6.0% | 09:00 median 11.00 | Matchbook 18.00
    comment: Two wins in his last six starts, a winner two starts back and again six starts back, but he has finished ninth last time out and in two of his other recent runs.
    DATA: model 7.3% | style Held up (led 4% of runs) | runs in data 13 | last 3: 30 Sep Musselburgh Flat 7.1f Good To Soft 9/11; 12 Oct Musselburgh Flat 7.1f Good To Soft 1/11; 4 Nov Musselburgh Flat 7f Soft 9/12 fig 53
    DATA for: Has won at this trip or further; Pace: a contested lead should suit its hold-up style
    DATA against: Recent figures 10 lb below its current mark (looks high in the weights)
- Kit Gabriel (hrs_25082309) | 7yo G | 138lb | OR 65 | draw 11 | jockey Clifford Lee | trainer Simon Pearce (14d 0/0) | headgear - | last run 64 days | form 320604 | MARKET 5.7% | 09:00 median 12.00 | Matchbook 18.50
    comment: A 64-day break is the main risk, as he is yet to win in his last six starts.
    DATA: model 5.1% | style Midfield (led 4% of runs) | runs in data 11 | last 3: 7 Jul Wolverhampton Flat 8.6f Standard 6/12; 31 Jul Wolverhampton Flat 7.2f Standard 10/10; 18 Sep Wolverhampton Flat 7.2f Standard 4/12
- Get Up Everybody (hrs_46169648) | 4yo G | 133lb | OR 60 | draw 2 | jockey David Nolan | trainer Paul Midgley (14d 0/2) | headgear - | last run 15 days | form 314245 | MARKET 5.1% | 09:00 median 15.00 | Matchbook 18.50
    comment: Fifth last time out after a fourth and a second, Get Up Everybody has been consistent without winning since a victory five starts back, and he returns fresh enough after 15 days.
    DATA: model 11.0% | style Held up (led 3% of runs) | runs in data 11 | last 3: 2 Oct Newcastle Flat 6f Standard 2/10; 20 Oct Newcastle (AW) Flat 7f Standard 4/14 fig 59; 6 Nov Newcastle (AW) Flat 6f Standard 5/14 fig 61
    DATA for: Best recent form figure 61, 5 lb above field average; Pace: a contested lead should suit its hold-up style
- Tasever (hrs_30765105) | 6yo G | 133lb | OR 60 | draw 5 | jockey Ashley Lewis(3) | trainer Patrick Morris (14d 0/5) | headgear p | last run 32 days | form 870407 | MARKET 5.0% | 09:00 median 15.00 | Matchbook 20.00
    comment: Tasever is yet to win in his last six starts, with a seventh last time out and a fourth three starts back his best recent efforts, though he has run over today's trip and going before.
    DATA: model 3.4% | style Leader (led 54% of runs) | runs in data 13 | last 3: 2 Sep Newcastle Flat 7.1f Standard 4/12; 25 Sep Newcastle Flat 7.1f Standard 11/11; 20 Oct Newcastle (AW) Flat 8f Standard 7/12 fig 58
    DATA for: Has won at this trip or further
    DATA against: Pace: likely to be taken on for the lead
- Front Gunner (hrs_37505237) | 5yo G | 129lb | OR 56 | draw 6 | jockey Tom Eaves | trainer Ivan Furtado (14d 1/9) | headgear - | last run 155 days | form 927667 | MARKET 4.8% | 09:00 median 17.00 | Matchbook 18.50
    comment: Front Gunner has finished seventh last time out, a sixth two starts back and another sixth three starts back, and is winless in his last six, though a second five starts back shows a bit of ability.
    DATA: model 4.0% | style Prominent (led 54% of runs) | runs in data 7 | last 3: 12 Mar Newcastle Flat 7.1f Standard 6/11; 2 May Thirsk Flat 8f Good To Firm 6/9; 19 Jun Redcar Flat 7f Good 7/14
    DATA for: Carries 5 lb less than average
    DATA against: Official rating 56, 6 lb below field average; Poor recent finishing positions; Returns from a 155-day break
- Operation Gimcrack (hrs_29227212) | 6yo G | 134lb | OR 61 | draw 4 | jockey Oisin McSweeney | trainer Bryan Smart (14d 1/3) | headgear - | last run 63 days | form 506231 | MARKET 4.7% | 09:00 median 13.00 | Matchbook 27.00
    comment: He has run over today's trip and going, and 134 lb from stall four is a hefty burden.
    DATA: model 15.6% | style Midfield (led 4% of runs) | runs in data 9 | last 3: 1 Aug Doncaster Flat 7f Good To Firm 2/11; 20 Aug Newcastle Flat 6f Standard 3/14; 19 Sep Newcastle Flat 6f Standard 1/10
    DATA for: Has won at this trip or further; Good recent finishing positions
- Master of Entropy (hrs_57160131) | 3yo G | 137lb | OR 65 | draw 1 | jockey Jason Hart | trainer John & Sean Quinn (14d 1/4) | headgear - | last run 81 days | form 564666 | MARKET 3.8% | 09:00 median 19.00 | Matchbook 28.00
    comment: The risk is a poor recent run, with sixth last time out and yet to win in his last six starts after 81 days off.
    DATA: model 4.8% | style Prominent (led 4% of runs) | runs in data 7 | last 3: 8 Jul Catterick Flat 7f Good To Firm 6/9; 26 Jul Pontefract Flat 8f Good To Firm 6/7; 1 Sep Wolverhampton Flat 8.6f Standard 6/6
    DATA against: Poor recent finishing positions
- Ice Show (hrs_63810131) | 3yo F | 130lb | OR 58 | draw 10 | jockey Mark Winn | trainer David O'Meara (14d 0/11) | headgear h | last run 40 days | form 560310 | MARKET 3.7% | 09:00 median 17.00 | Matchbook 32.00
    comment: Ice Show was unplaced last time out and has been off for 40 days, which makes her hard to fancy, though she won two starts back and has run over today's trip and going before.
    DATA: model 9.4% | style Midfield (led 5% of runs) | runs in data 7 | last 3: 8 Aug Redcar Flat 8f Good To Firm 3/8; 2 Oct Newcastle Flat 7.1f Standard 1/12; 12 Oct Newcastle Flat 8f Standard 12/13
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Trainer 0 wins from 11 runs, last 14 days
- The Gay Blade (hrs_26356659) | 7yo G | 138lb | OR 65 | draw 3 | jockey Andrew Mullen | trainer Iain Jardine (14d 0/5) | headgear - | last run 17 days | form 087457 | MARKET 3.4% | 09:00 median 21.00 | Matchbook 32.00
    comment: The Gay Blade is yet to win in his last six starts, finishing seventh last time out and fifth two starts back, though a fourth three starts back is his best recent effort. He has run over today's trip and going and is fresh off a 17-day break, but 138 lb from draw 3 looks a lot to carry.
    DATA: model 8.4% | style Prominent (led 5% of runs) | runs in data 18 | last 3: 17 Oct Catterick Flat 6f Good 4/10 fig 70; 27 Oct Catterick Flat 7f Soft 5/15 fig 71; 4 Nov Musselburgh Flat 7f Soft 7/12 fig 59
    DATA for: Best recent form figure 71, 15 lb above field average; Recent figures 6 lb above its current mark (looks well handicapped); Has won at this trip or further
- Fickle McSelfish (hrs_58931215) | 3yo C | 134lb | OR 62 | draw 9 | jockey Oisin Orr | trainer Tony Coyle & Kaine Wood (14d 0/0) | headgear p | last run 38 days | form 513298 | MARKET 2.2% | 09:00 median 29.00 | Matchbook 55.00
    comment: Fickle McSelfish has been placed twice since winning five starts back, but he's finished only eighth last time out and ninth before that.
    DATA: model 4.0% | style Leader (led 63% of runs) | runs in data 8 | last 3: 16 Apr Ripon Flat 8f Good To Soft 2/11; 1 Oct Newcastle Flat 8f Standard 9/10; 14 Oct Nottingham Flat 8.5f Good To Soft 8/8 fig 45
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 45, 11 lb below field average; Recent figures 17 lb below its current mark (looks high in the weights); Last-run finishing speed -3.4% vs that field (faded); Pace: likely to be taken on for the lead
- Henry Halflight (hrs_61242069) | 3yo G | 136lb | OR 64 | draw 12 | jockey Billy Garritty | trainer Liam Bailey (14d 0/0) | headgear p (1st time) | last run 32 days | form 718060 | MARKET 1.8% | 09:00 median 41.00 | Matchbook 90.00
    comment: Henry Halflight has been well beaten in his last three outings, with a sixth two starts back the best of them, and his only win came five starts back.
    DATA: model 2.8% | style Held up (led 5% of runs) | runs in data 7 | last 3: 15 Sep Redcar Flat 8f Good 13/13; 1 Oct Newcastle Flat 7.1f Standard 6/10; 20 Oct Newcastle (AW) Flat 8f Standard 12/12 fig 32
    DATA for: Has won at this trip or further; First-time headgear; Pace: a contested lead should suit its hold-up style
    DATA against: Best recent form figure 32, 24 lb below field average; Recent figures 32 lb below its current mark (looks high in the weights); Poor recent finishing positions

## 7:00 Newcastle (AW) | race_id rac_32305122720 | Midnite Built Different Handicap Stakes
Flat | Class 6 | 6f | going Standard | AW | 13 runners | rating band 0-65 | age 3yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Rousham (hrs_62678000) | 3yo G | 132lb | OR 63 | draw 11 | jockey Faye McManoman | trainer Nigel Tinkler (14d 0/2) | headgear hp | last run 22 days | form 460373 | MARKET 12.1% | 09:00 median 6.50 | Matchbook 7.60 | CHECK (skip line 6.17)
    comment: Rousham arrives on a fair recent note, third last time out and another third three starts back, and he has run over today's trip and going before. He is yet to win in his last six starts though, and 132 lb from draw 11 leaves plenty to prove.
    DATA: model 9.1% | style Midfield (led 4% of runs) | runs in data 11 | last 3: 1 Oct Newcastle Flat 7.1f Standard 3/10; 20 Oct Newcastle (AW) Flat 7f Standard 7/14 fig 57; 30 Oct Newcastle (AW) Flat 6f Standard 3/9 fig 59
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Best recent form figure 59, 5 lb below field average
- Educating Rita (hrs_40919655) | 4yo F | 132lb | OR 63 | draw 12 | jockey Kevin Stott | trainer Philip Kirby (14d 1/8) | headgear - | last run 15 days | form 056349 | MARKET 11.4% | 09:00 median 7.50 | Matchbook 7.60
    DATA: model 12.7% | style Held up (led 3% of runs) | runs in data 8 | last 3: 20 Oct Newcastle (AW) Flat 7f Standard 3/14 fig 65; 30 Oct Newcastle (AW) Flat 7f Standard 4/11 fig 64; 6 Nov Newcastle (AW) Flat 6f Standard 9/14 fig 61
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Bright (hrs_34874399) | 6yo G | 134lb | OR 65 | draw 14 | jockey Finley Marsh | trainer Mark Loughnane (14d 1/8) | headgear - | last run 22 days | form 787008 | MARKET 10.8% | 09:00 median 7.50 | Matchbook 8.60
    comment: He is yet to win in his last six, which is the one reservation, and he carries 134 lb from stall 14.
    DATA: model 6.0% | style Midfield (led 3% of runs) | runs in data 8 | last 3: 15 Aug Doncaster Flat 7f Good To Firm 12/12; 1 Oct Nottingham Flat 6.1f Good 13/15; 30 Oct Newcastle (AW) Flat 6f Standard 8/11 fig 59
    DATA against: Best recent form figure 59, 5 lb below field average; Recent figures 6 lb below its current mark (looks high in the weights); Poor recent finishing positions
- Too Much (hrs_33177837) | 6yo M | 130lb | OR 61 | draw 3 | jockey David Allan | trainer David Thompson (14d 0/2) | headgear h | last run 15 days | form 154862 | MARKET 9.7% | 09:00 median 8.00 | Matchbook 9.60
    comment: Too Much is hard to fancy, having managed just one win in her last six, back six starts ago, with a sixth and an eighth in the middle of that run.
    DATA: model 6.7% | style Held up (led 5% of runs) | runs in data 9 | last 3: 19 Sep Newcastle Flat 6f Standard 8/10; 26 Oct Redcar Flat 6f Heavy 6/14 fig 61; 6 Nov Newcastle (AW) Flat 6f Standard 2/14 fig 66
    DATA for: Recent figures 5 lb above its current mark (looks well handicapped)
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Wish This (hrs_41191255) | 4yo G | 131lb | OR 62 | draw 9 | jockey Tom Eaves | trainer Alan Brown (14d 0/1) | headgear b | last run 22 days | form 592663 | MARKET 9.6% | 09:00 median 9.10 | Matchbook 9.20
    DATA: model 8.0% | style Prominent (led 4% of runs) | runs in data 9 | last 3: 5 Sep Newcastle Flat 7.1f Standard 6/8; 20 Oct Newcastle (AW) Flat 6f Standard 6/12 fig 58; 30 Oct Newcastle (AW) Flat 7f Standard 3/10 fig 66
    DATA for: Recent figures 4 lb above its current mark (looks well handicapped)
- Jimmy Knocker (hrs_39678716) | 5yo G | 134lb | OR 65 | draw 4 | jockey Sean Kirrane | trainer Andi Brown (14d 0/0) | headgear t | last run 40 days | form 752782 | MARKET 9.5% | 09:00 median 8.00 | Matchbook 10.00
    DATA: model 9.1% | style Held up (led 3% of runs) | runs in data 7 | last 3: 31 Jul Newmarket Flat 6f Good To Firm 7/10; 7 Sep Windsor Flat 6.1f Good 8/13; 12 Oct Kempton Flat 6f Standard To Slow 2/10
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Havanagreattime (hrs_36302553) | 5yo G | 131lb | OR 62 | draw 13 | jockey Joanna Mason | trainer Ruth Carr (14d 1/3) | headgear - | last run 15 days | form 980099 | MARKET 6.3% | 09:00 median 13.00 | Matchbook 14.50
    comment: Havanagreattime has finished ninth in each of his last two outings and is winless in his last six, though he's back quickly after 15 days and has run over today's trip and going.
    DATA: model 3.4% | style Prominent (led 29% of runs) | runs in data 7 | last 3: 1 Oct Nottingham Flat 6.1f Good 14/15; 12 Oct Newcastle Flat 6f Standard 9/12; 6 Nov Newcastle (AW) Flat 6f Standard 9/14 fig 60
    DATA against: Poor recent finishing positions
- Roaring Ralph (hrs_29227254) | 6yo G | 134lb | OR 65 | draw 6 | jockey Rhys Elliott(5) | trainer Michael Dods (14d 0/5) | headgear - | last run 22 days | form 750039 | MARKET 6.3% | 09:00 median 12.00 | Matchbook 15.50
    DATA: model 4.1% | style Midfield (led 29% of runs) | runs in data 16 | last 3: 3 Oct Southwell Flat 6.1f Standard 11/13; 12 Oct Newcastle Flat 6f Standard 3/11; 30 Oct Newcastle (AW) Flat 6f Standard 9/11 fig 58
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 58, 6 lb below field average; Recent figures 7 lb below its current mark (looks high in the weights)
- Showtime Mahomes (hrs_24593625) | 7yo G | 130lb | OR 61 | draw 5 | jockey Oliver Stammers | trainer Grant Tuer (14d 0/2) | headgear - | last run 15 days | form 315204 | MARKET 5.8% | 09:00 median 13.00 | Matchbook 16.50
    comment: Fourth last time out, 15 days ago, and a second three starts back show Showtime Mahomes is still in the mix, while he has run over today's trip and on the going.
    DATA: model 8.5% | style Midfield (led 3% of runs) | runs in data 12 | last 3: 16 Oct Redcar Flat 6f Good 2/12 fig 70; 26 Oct Redcar Flat 6f Heavy 11/14 fig 32; 6 Nov Newcastle (AW) Flat 6f Standard 4/14 fig 63
    DATA for: Best recent form figure 70, 6 lb above field average; Recent figures 9 lb above its current mark (looks well handicapped); Has won at this trip or further
- Blue Force (hrs_35864409) | 5yo G | 133lb | OR 64 | draw 7 | jockey Cam Hardie | trainer Antony Brittain (14d 1/11) | headgear h | last run 33 days | form 914425 | MARKET 5.0% | 09:00 median 15.00 | Matchbook 19.50
    comment: Blue Force was fifth last time out and has only one win in his last six, coming five starts back, so he is hard to fancy; a second two starts back and a 33-day break plus experience over today's trip and going offer some respite.
    DATA: model 11.8% | style Midfield (led 4% of runs) | runs in data 13 | last 3: 19 Sep Newcastle Flat 5f Standard 4/10; 1 Oct Newcastle Flat 5f Standard 2/9; 19 Oct Wolverhampton (AW) Flat 5f Standard 5/11 fig 62
    DATA for: Has won at this trip or further
- Red Dahlia (hrs_17391580374) | 3yo F | 132lb | OR 63 | draw 2 | jockey Hollie Doyle | trainer Lawrence Mullaney (14d 0/1) | headgear - | last run 42 days | form 774 | MARKET 5.0% | 09:00 median 12.00 | Matchbook 26.00
    DATA: model 6.4% | style Prominent (led 4% of runs) | runs in data 3 | last 3: 30 Aug Cork Flat 6f Yielding 7/16; 21 Sep Fairyhouse Flat 7f Good 7/17; 10 Oct Naas Flat 7f Soft 4/11
- Miss Rainbow (hrs_35054425) | 5yo M | 130lb | OR 61 | draw 10 | jockey Jason Hart | trainer Tracy Waggott (14d 0/2) | headgear v | last run 26 days | form 341833 | MARKET 4.6% | 09:00 median 17.00 | Matchbook 21.00
    comment: Miss Rainbow has finished third in her last two starts and won four starts back, but an eighth three starts back shows her limits, and she has to shoulder 130 lb from draw 10.
    DATA: model 7.6% | style Prominent (led 5% of runs) | runs in data 13 | last 3: 17 Aug Catterick Flat 6f Good 8/9; 8 Sep Catterick Flat 6f Good To Soft 3/9; 26 Oct Redcar Flat 6f Heavy 3/14 fig 71
    DATA for: Best recent form figure 71, 7 lb above field average; Recent figures 10 lb above its current mark (looks well handicapped); Has won at this trip or further; Good recent finishing positions
- Habrdi (hrs_36454159) | 5yo G | 131lb | OR 62 | draw 1 | jockey James Sullivan | trainer Ruth Carr (14d 1/3) | headgear p | last run 163 days | form 486234 | MARKET 3.9% | 09:00 median 13.00 | Matchbook 42.00
    comment: Habrdi has been in the frame lately, with a second and a third among his last six, but he is winless in that spell and returns after 163 days off.
    DATA: model 6.5% | style Unknown | runs in data 10 | last 3: 5 May Ayr Flat 7.2f Good To Firm 2/7; 20 May Ayr Flat 7.2f Good To Firm 3/8; 11 Jun Catterick Flat 7f Good To Soft 4/6
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Returns from a 163-day break
