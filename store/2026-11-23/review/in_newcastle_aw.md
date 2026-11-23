# Card review packet: Newcastle (AW), 2026-11-23

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


## 3:30 Newcastle (AW) | race_id rac_32305256373 | Midnite A Next Generation Betting App Apprentice Handicap Stakes
Flat | Class 5 | 1m2f42y | going Standard | AW | 12 runners | rating band 0-70 | age 3yo+
DATA pace: Strong pace - 3 habitual front-runners (Rory's Gold, Alpine Sierra, Uncle Liam). A contested lead should set things up for horses coming from behind.
- Rory's Gold (hrs_47065046) | 4yo G | 137lb | OR 65 | draw 11 | jockey Amie Waugh | trainer Simon Waugh (14d 0/1) | headgear - | last run 2 days | form 731023 | MARKET 25.8% | 09:00 median 3.23 | Matchbook 3.35 | CHECK (skip line 3.06)
    comment: Rory's Gold arrives in good heart with a third last time out and a second two starts back, and he has run over today's trip and going, though a quick return after just two days and 137 lb are hurdles.
    DATA: model 14.7% | style Leader (led 38% of runs) | runs in data 11 | last 3: 8 Oct Ayr Flat 8f Heavy 10/13; 30 Oct Newcastle (AW) Flat 10f Standard 2/14 fig 64; 21 Nov Newcastle (AW) Flat 12.5f Standard 3/9 fig 61
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Pace: likely to be taken on for the lead
- Koko Blue (hrs_44105376) | 4yo F | 138lb | OR 66 | draw 2 | jockey Molly Keegan-Price(7) | trainer Tom Clover (14d 0/2) | headgear - | last run 52 days | form 332311 | MARKET 18.9% | 09:00 median 4.00 | Matchbook 4.90
    comment: Koko Blue arrives on a two-race winning streak and has run over today's trip and going, but a 52-day absence and 138 lb are fair questions.
    DATA: model 20.5% | style Prominent (led 29% of runs) | runs in data 6 | last 3: 4 Aug Lingfield Flat 11.6f Good To Firm 3/7; 2 Sep Newcastle Flat 10.2f Standard 1/7; 2 Oct Newcastle Flat 10.2f Standard 1/10
    DATA for: Last-run finishing speed +2.3% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
- Golspie (hrs_35123662) | 6yo G | 138lb | OR 66 | draw 5 | jockey Ashley Lewis | trainer Patrick Morris (14d 0/9) | headgear p | last run 24 days | form 331421 | MARKET 11.2% | 09:00 median 7.00 | Matchbook 8.00
    comment: Winner last time out and a second two starts back, Golspie arrives fit after 24 days and has run over today's trip and going before.
    DATA: model 10.4% | style Midfield (led 3% of runs) | runs in data 20 | last 3: 29 Sep Wolverhampton Flat 12.2f Standard 4/6; 22 Oct Southwell (AW) Flat 11f Standard 2/11 fig 60; 30 Oct Newcastle (AW) Flat 10f Standard 1/14 fig 65
    DATA for: Best recent form figure 65, 5 lb above field average; Has won at this trip or further; Good recent finishing positions
    DATA against: Trainer 0 wins from 9 runs, last 14 days
- Titian (hrs_21926786) | 8yo G | 135lb | OR 63 | draw 10 | jockey Tom Kiely-Marshall | trainer Julie Camacho (14d 1/5) | headgear b (1st time) | last run 24 days | form 044773 | MARKET 9.2% | 09:00 median 9.00 | Matchbook 9.20
    comment: The risk is he's yet to win in his last six starts, with two sevenths in the run before.
    DATA: model 4.5% | style Held up (led 5% of runs) | runs in data 7 | last 3: 9 Sep Redcar Flat 10f Good 7/9; 25 Sep Haydock Flat 10.2f Soft 7/7; 30 Oct Newcastle (AW) Flat 10f Standard 3/14 fig 62
    DATA for: Trainer 20% wins (1/5), last 14 days; First-time headgear; Pace: a contested lead should suit its hold-up style
    DATA against: Aged 8, older than most of this field
- Uncle Liam (hrs_45256764) | 4yo G | 129lb | OR 57 | draw 14 | jockey Lauren Young(3) | trainer Jim Goldie (14d 1/7) | headgear - | last run 56 days | form 154133 | MARKET 6.0% | 09:00 median 12.00 | Matchbook 16.50
    comment: He has run over today's trip and carries 129 lb from stall 14.
    DATA: model 10.0% | style Leader (led 57% of runs) | runs in data 8 | last 3: 2 Sep Hamilton Flat 11.1f Soft 1/8; 20 Sep Hamilton Flat 12.1f Heavy 3/6; 28 Sep Hamilton Flat 12.1f Soft 3/10
    DATA for: Has won at this trip or further; Good recent finishing positions; Carries 7 lb less than average
    DATA against: Official rating 57, 7 lb below field average; Pace: likely to be taken on for the lead
- Project Geofin (hrs_35431466) | 5yo G | 141lb | OR 69 | draw 9 | jockey Warren Fentiman | trainer Geoff Oldroyd (14d 1/2) | headgear - | last run 24 days | form 703800 | MARKET 5.8% | 09:00 median 13.00 | Matchbook 17.50
    DATA: model 5.1% | style Held up (led 3% of runs) | runs in data 6 | last 3: 29 Aug Beverley Flat 9.9f Soft 8/8; 10 Oct York Flat 10.3f Good To Soft 13/19; 30 Oct Newcastle (AW) Flat 8f Standard 10/10 fig 59
    DATA for: Official rating 69, 5 lb above field average; Pace: a contested lead should suit its hold-up style
    DATA against: Recent figures 10 lb below its current mark (looks high in the weights); Poor recent finishing positions; Carries 5 lb more than average
- Tommo's Ginjaninja (hrs_49142373) | 3yo G | 131lb | OR 62 | draw 12 | jockey Finlay Bassett(7) | trainer Michael & David Easterby (14d 0/5) | headgear - | last run 31 days | form 094026 | MARKET 5.6% | 09:00 median 13.00 | Matchbook 18.00
    comment: Sixth last time out and a second two starts back show some ability, and he has run over today's trip and going before, but he is yet to win in his last six starts. Carrying 131 lb from draw 12 off a 62 mark, he rates seventh of 14 on ours, so he looks a midfield type.
    DATA: model 4.8% | style Held up (led 5% of runs) | runs in data 11 | last 3: 11 Sep Chester Flat 10.3f Good To Soft 10/11; 3 Oct Redcar Flat 10f Good 2/9; 23 Oct Wolverhampton (AW) Flat 8.5f Standard 6/11 fig 59
    DATA for: Pace: a contested lead should suit its hold-up style
- Lone Piper (hrs_40514670) | 5yo G | 137lb | OR 65 | draw 4 | jockey Oliver Carmichael(5) | trainer Phillip Makin (14d 0/6) | headgear p | last run 24 days | form 577-87 | MARKET 4.3% | 09:00 median 17.00 | Matchbook 25.00
    comment: Fitness is fine after 24 days off, so the main risk is a run of finishes no better than seventh in his last four outings.
    DATA: model 2.4% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 12 Oct Musselburgh Flat 8.9f Good To Soft 8/8; 30 Oct Newcastle (AW) Flat 8f Standard 7/10 fig 61
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Alpine Sierra (hrs_24855355) | 8yo G | 132lb | OR 60 | draw 13 | jockey Rhys Elliott | trainer Jim Goldie (14d 1/7) | headgear - | last run 19 days | form 353465 | MARKET 3.8% | 09:00 median 21.00 | Matchbook 27.00
    comment: Alpine Sierra is winless in his last six, finishing fifth last time out and sixth two starts back, so he is hard to fancy, though he has run over today's trip and going and was third six starts back.
    DATA: model 6.1% | style Leader (led 54% of runs) | runs in data 18 | last 3: 18 Sep Ayr Flat 13.1f Soft 4/10; 12 Oct Musselburgh Flat 16f Good To Soft 6/8; 4 Nov Musselburgh Flat 12.5f Soft 5/10 fig 55
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 55, 5 lb below field average; Aged 8, older than most of this field; Pace: likely to be taken on for the lead
- Alpine Stroll (hrs_22689219) | 8yo G | 142lb | OR 70 | draw 8 | jockey Shay Farmer(3) | trainer Tony Culhane & Stella Barclay (14d 0/2) | headgear - | last run 390 days | form 01911- | MARKET 3.3% | 09:00 median 21.00 | Matchbook 34.00
    comment: Alpine Stroll has won three of his last five starts, including last time out and two starts back, and has run over today's trip and going before.
    DATA: model 10.2% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Official rating 70, 6 lb above field average
    DATA against: Carries 6 lb more than average; Returns from a 390-day break; Lightly raced: 0 runs in our data, so the model has little to go on; Aged 8, older than most of this field
- Royal Blaze (hrs_35336700) | 5yo G | 134lb | OR 62 | draw 6 | jockey Alex Jary | trainer Ewan Whillans (14d 0/8) | headgear tp | last run 2 days | form 911085 | MARKET 3.1% | 09:00 median 29.00 | Matchbook 32.00
    comment: Royal Blaze has gone fifth, then eighth, then unplaced since back-to-back wins four and five starts back, and he's turned out again just two days later, which is a hard sell.
    DATA: model 4.1% | style Midfield (led 3% of runs) | runs in data 10 | last 3: 10 Aug Ayr Flat 10f Good To Soft 10/11; 8 Oct Ayr Flat 10f Heavy 8/12; 21 Nov Newcastle (AW) Flat 12.5f Standard 5/9 fig 57
    DATA for: Has won at this trip or further
    DATA against: Trainer 0 wins from 8 runs, last 14 days
- Jaminoz (hrs_30487170) | 7yo G | 135lb | OR 63 | draw 1 | jockey Lexie Clarkson(7) | trainer Lucinda Russell & Michael Scudamore (14d 4/26) | headgear tb | last run 167 days | form 14-451 | MARKET 3.0% | 09:00 median 17.00 | Matchbook 60.00
    comment: Jaminoz won last time out and has two wins in his last five, with experience over today's trip and going, but a 167-day absence is a concern and he carries 135 lb from stall one.
    DATA: model 7.1% | style Prominent (led 4% of runs) | runs in data 3 | last 3: 3 May Hamilton Flat 11.1f Good 4/8; 17 May Hamilton Flat 11.1f Good 5/10; 9 Jun Carlisle Flat 11.2f Good To Soft 1/10
    DATA for: Last-run finishing speed +2.9% vs that field (finished strongly); Has won at this trip or further
    DATA against: Returns from a 167-day break

## 4:05 Newcastle (AW) | race_id rac_32305258310 | All-Weather Championship Is Back EBF Restricted Maiden Stakes (For Horses In Bands B, C And D) (GBB Race)
Flat | Class 4 | 7f14y | going Standard | AW | 11 runners | rating band - | age 2yo
DATA pace: Unclear - Running styles known for only 5 of 11 runners.
- Old Compton (hrs_17394427764) | 2yo C | 130lb | OR - | draw 2 | jockey Cieren Fallon | trainer William Haggas (14d 3/14) | headgear - | last run 24 days | form 3 | MARKET 46.6% | 09:00 median 1.83 | Matchbook 1.89
    DATA: model 17.7% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 30 Oct Newmarket Flat 7f Good To Soft 3/10 fig 54
    DATA for: Trainer 21% wins (3/14), last 14 days; Last-run finishing speed +2.9% vs that field (finished strongly)
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Good Bye Girl (hrs_17395550032) | 2yo F | 128lb | OR - | draw 11 | jockey Billy Loughnane | trainer George Boughey (14d 5/17) | headgear - | last run - days | form - | MARKET 12.4% | 09:00 median 6.50 | Matchbook 7.80
    DATA: model 7.8% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 29% wins (5/17), last 14 days
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Raguel (hrs_17393974059) | 2yo C | 130lb | OR - | draw 6 | jockey Ryan Sexton | trainer Julie Camacho (14d 1/5) | headgear - | last run 28 days | form 5 | MARKET 11.1% | 09:00 median 7.00 | Matchbook 8.80
    DATA: model 8.2% | style Held up (led 8% of runs) | runs in data 1 | last 3: 26 Oct Redcar Flat 7f Soft 5/11 fig 56
    DATA for: Best recent form figure 56, 5 lb above field average; Trainer 20% wins (1/5), last 14 days; Last-run finishing speed +3.9% vs that field (finished strongly)
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Rogue Inferno (hrs_17392559751) | 2yo G | 133lb | OR - | draw 8 | jockey Oisin Orr | trainer Edward Bethell (14d 0/6) | headgear - | last run 18 days | form 94 | MARKET 9.1% | 09:00 median 9.00 | Matchbook 10.50
    DATA: model 5.1% | style Prominent (led 8% of runs) | runs in data 2 | last 3: 22 Sep Southwell Flat 8.1f Standard 9/9; 5 Nov Southwell (AW) Flat 7f Standard 4/9 fig 54
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Pippy Boy (hrs_17391803576) | 2yo G | 133lb | OR - | draw 7 | jockey George Wood | trainer Jennie Candlish (14d 4/24) | headgear - | last run 51 days | form 93 | MARKET 7.6% | 09:00 median 11.00 | Matchbook 12.50
    DATA: model 8.8% | style Unknown | runs in data 2 | last 3: 5 Sep Thirsk Flat 6f Good To Soft 9/13; 3 Oct Southwell Flat 7.1f Standard 3/10
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Pushing The Limits (hrs_17392828845) | 2yo G | 127lb | OR - | draw 9 | jockey Conor Whiteley(5) | trainer Stephen Hanlon (14d 0/2) | headgear - | last run 38 days | form 35 | MARKET 5.5% | 09:00 median 13.00 | Matchbook 19.50
    DATA: model 17.3% | style Prominent (led 38% of runs) | runs in data 2 | last 3: 25 Sep Newcastle Flat 7.1f Standard 3/13; 16 Oct Redcar Flat 8f Good 5/10 fig 46
    DATA against: Best recent form figure 46, 5 lb below field average; Lightly raced: 2 runs in our data, so the model has little to go on
- Granite Force (hrs_17389961638) | 2yo C | 127lb | OR - | draw 5 | jockey Kevin Stott | trainer Michael Appleby (14d 0/12) | headgear - | last run - days | form - | MARKET 2.4% | 09:00 median 34.00 | Matchbook 46.00
    DATA: model 7.7% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Trainer 0 wins from 12 runs, last 14 days; Lightly raced: 0 runs in our data, so the model has little to go on
- Luma Nyota (hrs_17395876491) | 2yo F | 128lb | OR - | draw 10 | jockey Joanna Mason | trainer Gemma Tutty (14d 0/3) | headgear - | last run - days | form - | MARKET 1.9% | 09:00 median 41.00 | Matchbook 75.00
    DATA: model 7.8% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Annayalla (hrs_17395874405) | 2yo F | 122lb | OR - | draw 3 | jockey Cam Hardie | trainer Ollie Pears (14d 0/0) | headgear - | last run - days | form - | MARKET 1.5% | 09:00 median 41.00 | Matchbook 120.00
    DATA: model 7.6% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Radio Braga (hrs_17395878577) | 2yo G | 127lb | OR - | draw 1 | jockey Billy Garritty | trainer Liam Bailey (14d 0/1) | headgear - | last run - days | form - | MARKET 1.0% | 09:00 median 67.00 | Matchbook 190.00
    DATA: model 7.7% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Another Festival (hrs_17393187637) | 2yo F | 122lb | OR - | draw 4 | jockey William Pyle | trainer Craig Lidster (14d 0/2) | headgear - | last run 17 days | form 7 | MARKET 1.0% | 09:00 median 101.00 | Matchbook 180.00
    DATA: model 4.4% | style Held up (led 8% of runs) | runs in data 1 | last 3: 6 Nov Newcastle (AW) Flat 7f Standard 7/10 fig 45
    DATA against: Best recent form figure 45, 6 lb below field average; Lightly raced: 1 run in our data, so the model has little to go on

## 4:40 Newcastle (AW) | race_id rac_32305260247 | AWC Finals Day At Newcastle 26th March Nursery Handicap Stakes
Flat | Class 5 | 5f | going Standard | AW | 7 runners | rating band 0-75 | age 2yo
DATA pace: Even - Two likely leaders (American Psycho, Cyberspace). A fair, even gallop is most likely.
- Dowman (hrs_63323687) | 2yo G | 140lb | OR 74 | draw 5 | jockey Billy Loughnane | trainer George Boughey (14d 5/17) | headgear t | last run 6 days | form 125231 | MARKET 51.2% | 09:00 median 1.73 | Matchbook 1.85
    comment: Dowman arrives in cracking form, a winner last time out just six days ago, with a third two starts back and a second three starts back, and he has run over today's trip and going before.
    DATA: model 31.1% | style Midfield (led 8% of runs) | runs in data 8 | last 3: 12 Sep Bath Flat 5f Good 2/10; 19 Oct Southwell (AW) Flat 6f Standard 3/13 fig 75; 17 Nov Southwell (AW) Flat 5f Standard 1/5 fig 82
    DATA for: Best recent form figure 82, 11 lb above field average; Recent figures 8 lb above its current mark (looks well handicapped); Trainer 29% wins (5/17), last 14 days; Last-run finishing speed +2.3% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Carries 7 lb more than average
- Big Hitter (hrs_64460193) | 2yo F | 135lb | OR 75 | draw 1 | jockey P. J. McDonald | trainer Jamie Osborne (14d 0/5) | headgear t | last run 30 days | form 22317 | MARKET 16.2% | 09:00 median 5.50 | Matchbook 5.90
    DATA: model 12.1% | style Prominent (led 29% of runs) | runs in data 5 | last 3: 8 Jul Catterick Flat 5f Good To Firm 3/6; 13 Sep Bath Flat 5f Good To Soft 1/7; 24 Oct Doncaster Flat 6f Heavy 7/7 fig 68
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Recent figures 7 lb below its current mark (looks high in the weights); Last-run finishing speed -2.3% vs that field (faded)
- Cyberspace (hrs_17391718050) | 2yo G | 130lb | OR 70 | draw 6 | jockey Conor Whiteley(5) | trainer Bryan Smart (14d 1/4) | headgear - | last run 27 days | form 5222 | MARKET 12.4% | 09:00 median 7.00 | Matchbook 8.00
    comment: Cyberspace has finished second in each of his last three starts, a consistent profile, and he returns after 27 days with experience of today's trip and going.
    DATA: model 25.5% | style Leader (led 54% of runs) | runs in data 4 | last 3: 15 Sep Redcar Flat 5f Good 2/8; 28 Sep Hamilton Flat 5f Soft 2/6; 27 Oct Catterick Flat 5f Soft 2/9 fig 66
    DATA for: Good recent finishing positions
    DATA against: Best recent form figure 66, 5 lb below field average
- American Psycho (hrs_64621494) | 2yo G | 133lb | OR 73 | draw 2 | jockey M. P. Sheehy | trainer Adrian Keatley (14d 0/5) | headgear - | last run 83 days | form 2742 | MARKET 7.0% | 09:00 median 11.00 | Matchbook 16.00
    comment: American Psycho comes here a runner-up last time out, with another second four starts back, and he has run over today's trip and on the going before.
    DATA: model 8.6% | style Leader (led 29% of runs) | runs in data 4 | last 3: 18 May Wolverhampton Flat 5.1f Standard 7/7; 25 Jul Lingfield Flat 5f Good To Firm 4/7; 1 Sep Ripon Flat 5f Soft 2/5
- The Stony Baker (hrs_17391390548) | 2yo C | 133lb | OR 73 | draw 7 | jockey Kevin Stott | trainer Lisa Williamson (14d 0/0) | headgear t | last run 27 days | form 901 | MARKET 6.0% | 09:00 median 15.00 | Matchbook 17.00
    comment: The Stony Baker won last time out and has run over today's trip and going, but he was unplaced and ninth in the two runs before that, so the form is patchy.
    DATA: model 2.6% | style Prominent (led 8% of runs) | runs in data 3 | last 3: 11 Sep Chester Flat 6.1f Good To Soft 9/9; 24 Sep Southwell Flat 6.1f Standard 10/11; 27 Oct Catterick Flat 5f Soft 1/9 fig 69
    DATA for: Has won at this trip or further
- Jolly Good Fellows (hrs_63357448) | 2yo F | 130lb | OR 70 | draw 3 | jockey Gina Mangan | trainer Dr Richard Newland (14d 1/6) | headgear - | last run 195 days | form 3317 | MARKET 3.8% | 09:00 median 21.00 | Matchbook 28.00
    DATA: model 10.8% | style Prominent (led 38% of runs) | runs in data 4 | last 3: 21 Apr Pontefract Flat 5f Good 3/8; 4 May Bath Flat 5f Good 1/10; 12 May Bath Flat 5f Firm 7/7
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Last-run finishing speed -3.5% vs that field (faded); Returns from a 195-day break
- Eleven Eighty Two (hrs_65036111) | 2yo F | 127lb | OR 67 | draw 4 | jockey Andrew Mullen | trainer Ben Haslam (14d 2/7) | headgear - | last run 85 days | form 42268 | MARKET 3.5% | 09:00 median 21.00 | Matchbook 34.00
    comment: Eleven Eighty Two is winless in her last five and was beaten into eighth last time out, 85 days ago, which makes her hard to fancy.
    DATA: model 9.2% | style Prominent (led 5% of runs) | runs in data 5 | last 3: 6 Jul Ripon Flat 6f Good 2/11; 27 Jul Ripon Flat 6f Good To Firm 6/6; 30 Aug Beverley Flat 5f Heavy 8/13
    DATA for: Trainer 29% wins (2/7), last 14 days; Carries 6 lb less than average

## 5:15 Newcastle (AW) | race_id rac_32305262184 | AWC Season 14 Has Begun Fillies' Novice Stakes (GBB Race)
Flat | Class 3 | 7f14y | going Standard | AW | 9 runners | rating band - | age 2yo
DATA pace: Unclear - Running styles known for only 4 of 9 runners.
- Faithful (hrs_17392059111) | 2yo F | 128lb | OR - | draw 4 | jockey Cieren Fallon | trainer William Haggas (14d 3/14) | headgear - | last run 49 days | form 3 | MARKET 36.1% | 09:00 median 2.25 | Matchbook 2.60
    DATA: model 16.9% | style Held up (led 8% of runs) | runs in data 1 | last 3: 5 Oct Yarmouth Flat 7f Good To Firm 3/5
    DATA for: Trainer 21% wins (3/14), last 14 days
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Ruby Sands (hrs_62169233) | 2yo F | 128lb | OR 77 | draw 9 | jockey Barry McHugh | trainer Ollie Sangster (14d 1/5) | headgear - | last run 23 days | form 3328 | MARKET 18.7% | 09:00 median 4.50 | Matchbook 5.00
    DATA: model 19.8% | style Held up (led 3% of runs) | runs in data 4 | last 3: 26 Sep Newmarket Flat 7f Good To Firm 3/10; 10 Oct Southwell Flat 7.1f Standard 2/9; 31 Oct Newmarket Flat 8f Good To Soft 8/11 fig 71
    DATA for: Trainer 20% wins (1/5), last 14 days; Good recent finishing positions
- Bintbossom (hrs_17395880663) | 2yo F | 128lb | OR - | draw 6 | jockey Sean Dylan Bowen | trainer Roger Varian (14d 4/7) | headgear - | last run - days | form - | MARKET 11.4% | 09:00 median 7.50 | Matchbook 8.40
    DATA: model 9.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 57% wins (4/7), last 14 days
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Banner Babe (hrs_17392255195) | 2yo F | 128lb | OR - | draw 8 | jockey Billy Loughnane | trainer George Boughey (14d 5/17) | headgear - | last run - days | form - | MARKET 10.6% | 09:00 median 8.00 | Matchbook 9.00
    DATA: model 9.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 29% wins (5/17), last 14 days
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Angelcatcher (hrs_17395449904) | 2yo F | 128lb | OR - | draw 1 | jockey Sam James | trainer K. R. Burke (14d 0/7) | headgear - | last run - days | form - | MARKET 8.8% | 09:00 median 9.50 | Matchbook 10.50
    DATA: model 9.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Love Dubai (hrs_65225202) | 2yo F | 128lb | OR - | draw 2 | jockey Kevin Stott | trainer Oliver Cole (14d 0/0) | headgear - | last run - days | form - | MARKET 5.1% | 09:00 median 17.00 | Matchbook 19.00
    DATA: model 9.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Sea of Serenity (hrs_17395883792) | 2yo F | 128lb | OR - | draw 3 | jockey Jason Hart | trainer Edward Bethell (14d 0/6) | headgear - | last run - days | form - | MARKET 5.1% | 09:00 median 17.00 | Matchbook 19.00
    DATA: model 9.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Cant Bear The Heat (hrs_17395069209) | 2yo F | 128lb | OR - | draw 5 | jockey Sean Kirrane | trainer Michael Dods (14d 0/7) | headgear - | last run 17 days | form 5 | MARKET 2.5% | 09:00 median 34.00 | Matchbook 40.00
    DATA: model 12.2% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 6 Nov Newcastle (AW) Flat 7f Standard 5/10 fig 54
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Aunty Patsy (hrs_66305743) | 2yo F | 128lb | OR - | draw 7 | jockey Oisin Orr | trainer Richard & Peter Fahey (14d 0/8) | headgear - | last run 144 days | form 5 | MARKET 1.8% | 09:00 median 51.00 | Matchbook 65.00
    DATA: model 4.0% | style Held up (led 8% of runs) | runs in data 1 | last 3: 2 Jul Yarmouth Flat 7f Good To Firm 5/5
    DATA against: Trainer 0 wins from 8 runs, last 14 days; Returns from a 144-day break; Lightly raced: 1 run in our data, so the model has little to go on

## 5:45 Newcastle (AW) | race_id rac_32305264121 | Midnite It's Actually Pretty Good Handicap Stakes (Div I)
Flat | Class 5 | 6f | going Standard | AW | 10 runners | rating band 0-70 | age 3yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Encore (hrs_56591094) | 4yo F | 135lb | OR 70 | draw 3 | jockey Cieren Fallon | trainer William Haggas (14d 3/14) | headgear - | last run 28 days | form 5-2127 | MARKET 18.8% | 09:00 median 4.33 | Matchbook 5.10 | CHECK (skip line 4.11)
    comment: Encore has been in the frame often lately, with a win three starts back and a second two starts back, but she was only seventh last time out after 28 days off. She has run over today's trip and going, though carrying 135 lb from stall 3 leaves plenty to prove.
    DATA: model 20.6% | style Midfield (led 4% of runs) | runs in data 4 | last 3: 14 Sep Kempton Flat 6f Standard To Slow 1/8; 17 Oct Southwell (AW) Flat 7f Standard 2/9 fig 69; 26 Oct Southwell (AW) Flat 6f Standard 7/10 fig 63
    DATA for: Trainer 21% wins (3/14), last 14 days; Has won at this trip or further; Good recent finishing positions
- Wise Crack (hrs_54337472) | 3yo G | 132lb | OR 67 | draw 5 | jockey James Sullivan | trainer Ruth Carr (14d 1/5) | headgear v | last run 17 days | form 453331 | MARKET 13.8% | 09:00 median 6.00 | Matchbook 7.00
    comment: Wise Crack arrives in cracking nick, a winner last time out after three thirds in his previous four runs, and he's fresh from a 17-day break with experience of today's trip and going.
    DATA: model 16.6% | style Held up (led 4% of runs) | runs in data 12 | last 3: 10 Oct Southwell Flat 6.1f Standard 3/9; 26 Oct Redcar Flat 6f Heavy 3/14 fig 75; 6 Nov Newcastle (AW) Flat 6f Standard 1/14 fig 69
    DATA for: Best recent form figure 75, 10 lb above field average; Recent figures 8 lb above its current mark (looks well handicapped); Trainer 20% wins (1/5), last 14 days; Last-run finishing speed +2.7% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- The Green Man (hrs_29761508) | 7yo G | 131lb | OR 66 | draw 4 | jockey Kevin Stott | trainer Philip Kirby (14d 1/9) | headgear tv | last run 24 days | form 304675 | MARKET 12.6% | 09:00 median 6.50 | Matchbook 7.60
    comment: The Green Man is winless in his last six, though a fifth last time out, 24 days ago, keeps him ticking over, and he has run over today's trip and going before.
    DATA: model 6.1% | style Held up (led 5% of runs) | runs in data 13 | last 3: 4 Jul Carlisle Flat 7.8f Good 6/7; 12 Oct Newcastle Flat 6f Standard 7/11; 30 Oct Newcastle (AW) Flat 6f Standard 5/11 fig 66
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Noelies Dream (hrs_52452078) | 3yo G | 132lb | OR 67 | draw 1 | jockey Andrew Mullen | trainer Dylan Cunha (14d 1/8) | headgear t | last run 17 days | form 15-052 | MARKET 11.7% | 09:00 median 7.25 | Matchbook 8.00
    DATA: model 5.9% | style Held up (led 5% of runs) | runs in data 3 | last 3: 7 Sep Windsor Flat 6.1f Good 13/13; 14 Sep Windsor Flat 6.1f Good To Soft 5/13; 6 Nov Newcastle (AW) Flat 6f Standard 2/14 fig 69
    DATA for: Last-run finishing speed +2.3% vs that field (finished strongly)
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Moonstone Boy (hrs_34471850) | 5yo G | 132lb | OR 67 | draw 7 | jockey George Wood | trainer Jennie Candlish (14d 4/24) | headgear v (1st time) | last run 38 days | form 778465 | MARKET 10.8% | 09:00 median 7.50 | Matchbook 9.00
    comment: Moonstone Boy is yet to win in his last six starts, but he has run over today's trip and going before, and a fourth three starts back is his best recent finish, with a fifth last time out.
    DATA: model 10.0% | style Midfield (led 3% of runs) | runs in data 7 | last 3: 4 Sep Haydock Flat 5f Heavy 4/11; 19 Sep Chester Flat 6.1f Heavy 6/10; 16 Oct Haydock Flat 5f Heavy 5/14 fig 75
    DATA for: Best recent form figure 75, 10 lb above field average; Recent figures 8 lb above its current mark (looks well handicapped); First-time headgear
- Spun To Gold (hrs_36836982) | 5yo G | 116lb | OR 50 | draw 9 | jockey Lauren Young(5) | trainer Jim Goldie (14d 1/7) | headgear - | last run 2 days | form 535603 | MARKET 8.3% | 09:00 median 10.00 | Matchbook 11.50
    comment: Drawn nine and carrying 116 lb, he's hard to fancy.
    DATA: model 3.4% | style Held up (led 5% of runs) | runs in data 8 | last 3: 30 Mar Wolverhampton Flat 6.1f Standard 6/12; 6 Nov Newcastle (AW) Flat 6f Standard 10/14 fig 48; 21 Nov Newcastle (AW) Flat 5f Standard 3/14 fig 56
    DATA for: Recent figures 6 lb above its current mark (looks well handicapped); Carries 14 lb less than average
    DATA against: Best recent form figure 56, 9 lb below field average; Official rating 50, 15 lb below field average; Pace: steady gallop likely, hard to come from off the pace
- Storm Esme (hrs_52054758) | 3yo F | 133lb | OR 68 | draw 8 | jockey David Allan | trainer Tim Easterby (14d 1/10) | headgear p | last run 24 days | form 584182 | MARKET 8.3% | 09:00 median 9.50 | Matchbook 12.50
    DATA: model 14.0% | style Midfield (led 3% of runs) | runs in data 9 | last 3: 5 Sep Newcastle Flat 6f Standard 1/14; 6 Oct Southwell Flat 6.1f Standard 8/10; 30 Oct Newcastle (AW) Flat 6f Standard 2/9 fig 65
    DATA for: Has won at this trip or further; Good recent finishing positions
- Lumenbourg (hrs_37807098) | 5yo G | 127lb | OR 62 | draw 2 | jockey Jason Hart | trainer Katie Scott (14d 0/3) | headgear b (1st time) | last run 28 days | form 465230 | MARKET 6.7% | 09:00 median 13.00 | Matchbook 15.00
    comment: Lumenbourg is winless in his last six and was unplaced last time out, which makes him hard to fancy, though a third two starts back and a second three starts back show he can get involved.
    DATA: model 9.4% | style Prominent (led 23% of runs) | runs in data 9 | last 3: 2 Sep Hamilton Flat 6f Soft 2/13; 28 Sep Hamilton Flat 6f Soft 3/6; 26 Oct Redcar Flat 6f Heavy 10/14 fig 48
    DATA for: Has won at this trip or further; Good recent finishing positions; First-time headgear
    DATA against: Best recent form figure 48, 17 lb below field average; Recent figures 14 lb below its current mark (looks high in the weights)
- Mythical Phoenix (hrs_35446243) | 6yo G | 134lb | OR 69 | draw 10 | jockey Tom Kiely-Marshall(3) | trainer Julie Camacho (14d 1/5) | headgear h | last run 31 days | form -06586 | MARKET 5.2% | 09:00 median 16.50 | Matchbook 18.50
    comment: The main risk is a winless run, with a sixth, eighth, fifth and sixth in his last four.
    DATA: model 7.7% | style Held up (led 8% of runs) | runs in data 5 | last 3: 5 Sep Thirsk Flat 7f Good To Soft 5/9; 22 Sep Beverley Flat 7.3f Good 8/10; 23 Oct Doncaster Flat 6f Heavy 6/11 fig 65
    DATA for: Trainer 20% wins (1/5), last 14 days
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Jersey Maverick (hrs_39960781) | 4yo G | 133lb | OR 68 | draw 6 | jockey Oliver Stammers | trainer Ben Haslam (14d 2/7) | headgear p | last run 46 days | form 823450 | MARKET 3.9% | 09:00 median 21.00 | Matchbook 25.00
    comment: The risk is a 46-day break and an unplaced run last time out, with 133 lb to carry from stall 6.
    DATA: model 6.2% | style Unknown | runs in data 8 | last 3: 15 Aug Newmarket Flat 7f Good To Firm 4/6; 9 Sep Kempton Flat 7f Standard To Slow 5/14; 8 Oct Southwell Flat 7.1f Standard 12/12
    DATA for: Trainer 29% wins (2/7), last 14 days
    DATA against: Last-run finishing speed -5.4% vs that field (faded)

## 6:15 Newcastle (AW) | race_id rac_32305711568 | Midnite It's Actually Pretty Good Handicap Stakes (Div II)
Flat | Class 5 | 6f | going Standard | AW | 9 runners | rating band 0-70 | age 3yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Azure Zain (hrs_52418205) | 4yo G | 135lb | OR 70 | draw 2 | jockey Oisin Orr | trainer Richard & Peter Fahey (14d 0/8) | headgear - | last run 27 days | form 166377 | MARKET 22.0% | 09:00 median 4.00 | Matchbook 4.20 | CHECK (skip line 3.80)
    comment: The risk is a form line that has slipped to back-to-back sevenths, and he carries 135 lb from draw 2.
    DATA: model 10.7% | style Midfield (led 4% of runs) | runs in data 7 | last 3: 27 Aug Southwell Flat 6.1f Standard 3/11; 21 Sep Hamilton Flat 6f Soft 7/8; 27 Oct Catterick Flat 6f Soft 7/8 fig 58
    DATA for: Has won at this trip or further
    DATA against: Recent figures 12 lb below its current mark (looks high in the weights); Trainer 0 wins from 8 runs, last 14 days
- Kings Merchant (hrs_36454271) | 5yo G | 132lb | OR 67 | draw 3 | jockey Kevin Stott | trainer Philip Kirby (14d 1/9) | headgear p | last run 17 days | form 451381 | MARKET 16.8% | 09:00 median 5.00 | Matchbook 5.80
    comment: Kings Merchant won last time out, 17 days ago, and also won four starts back, though an eighth two starts back shows his consistency can wobble.
    DATA: model 11.9% | style Midfield (led 3% of runs) | runs in data 15 | last 3: 26 Sep Ripon Flat 6f Good 3/10; 17 Oct Catterick Flat 7f Good 8/10 fig 51; 6 Nov Newcastle (AW) Flat 6f Standard 1/14 fig 71
    DATA for: Best recent form figure 71, 10 lb above field average; Recent figures 4 lb above its current mark (looks well handicapped); Last-run finishing speed +2.4% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
- Raatea (hrs_19681459) | 9yo G | 134lb | OR 69 | draw 4 | jockey Tom Kiely-Marshall(3) | trainer Julie Camacho (14d 1/5) | headgear hp | last run 16 days | form 350400 | MARKET 13.2% | 09:00 median 6.50 | Matchbook 7.40
    comment: The risk is a winless run in his last six, including two unplaced efforts most recently, and 134 lb to carry.
    DATA: model 6.3% | style Prominent (led 8% of runs) | runs in data 7 | last 3: 22 Aug Redcar Flat 6f Good 4/11; 13 Sep Doncaster Flat 6f Good 11/16; 7 Nov Doncaster Flat 7f Good To Soft 12/12 fig 34
    DATA for: Trainer 20% wins (1/5), last 14 days
    DATA against: Best recent form figure 34, 27 lb below field average; Recent figures 35 lb below its current mark (looks high in the weights); Aged 9, older than most of this field
- Go Victor (hrs_51800455) | 3yo G | 131lb | OR 66 | draw 8 | jockey Billy Garritty | trainer Tony Culhane & Stella Barclay (14d 0/2) | headgear p | last run 17 days | form 130112 | MARKET 12.0% | 09:00 median 7.00 | Matchbook 8.20
    comment: Fit after 17 days, he has run over this trip and on this going.
    DATA: model 21.4% | style Midfield (led 3% of runs) | runs in data 9 | last 3: 22 Sep Beverley Flat 5f Good 1/6; 5 Oct Pontefract Flat 5f Good 1/12; 6 Nov Newcastle (AW) Flat 5f Standard 2/14 fig 70
    DATA for: Best recent form figure 70, 9 lb above field average; Recent figures 4 lb above its current mark (looks well handicapped); Has won at this trip or further; Good recent finishing positions
- Sugar Baby (hrs_23848041) | 8yo G | 133lb | OR 68 | draw 9 | jockey David Nolan | trainer Peter Niven (14d 0/2) | headgear - | last run 17 days | form 750916 | MARKET 9.8% | 09:00 median 8.50 | Matchbook 10.00
    comment: Sugar Baby won two starts back but was only sixth last time, and that win is the lone bright spot in a patchy run of finishes, so he is hard to fancy.
    DATA: model 12.1% | style Prominent (led 29% of runs) | runs in data 11 | last 3: 16 Oct Redcar Flat 6f Good 9/12 fig 56; 30 Oct Newcastle (AW) Flat 6f Standard 1/11 fig 68; 6 Nov Newcastle (AW) Flat 6f Standard 6/14 fig 65
    DATA for: Best recent form figure 68, 7 lb above field average; Has won at this trip or further
- Brave Traveller (hrs_56844011) | 3yo G | 132lb | OR 67 | draw 7 | jockey Oisin McSweeney | trainer Bryan Smart (14d 1/4) | headgear - | last run 24 days | form 273255 | MARKET 9.6% | 09:00 median 9.00 | Matchbook 10.00
    comment: Brave Traveller has been consistent without a win, a fifth last time out, a fifth two starts back and a second three starts back, and he has run over today's trip and going.
    DATA: model 11.1% | style Midfield (led 4% of runs) | runs in data 8 | last 3: 31 Jul Newcastle Flat 5f Standard To Slow 2/12; 8 Aug Redcar Flat 6f Good To Firm 5/7; 30 Oct Newcastle (AW) Flat 6f Standard 5/9 fig 64
- Mr Dreamseller (hrs_56746452) | 4yo G | 132lb | OR 67 | draw 1 | jockey William Pyle | trainer David & Nicola Barron (14d 0/0) | headgear - | last run 18 days | form 410774 | MARKET 7.1% | 09:00 median 12.00 | Matchbook 13.50
    comment: He carries 132 lb from stall one.
    DATA: model 11.2% | style Midfield (led 4% of runs) | runs in data 7 | last 3: 2 May Thirsk Flat 6f Good To Firm 7/9; 18 May Carlisle Flat 5.8f Soft 7/12; 5 Nov Southwell (AW) Flat 6f Standard 4/9 fig 65
    DATA for: Best recent form figure 65, 4 lb above field average; Has won at this trip or further
- Winter Crown (hrs_30151303) | 6yo G | 121lb | OR 56 | draw 6 | jockey Joanna Mason | trainer Liam Bailey (14d 0/1) | headgear - | last run 17 days | form 867537 | MARKET 5.6% | 09:00 median 15.00 | Matchbook 18.00
    comment: Winter Crown is hard to fancy, winless in his last six and only a seventh last time out, with a third two starts back his best finish in that run.
    DATA: model 5.9% | style Prominent (led 3% of runs) | runs in data 6 | last 3: 27 Oct Catterick Flat 6f Soft 5/10 fig 56; 30 Oct Newcastle (AW) Flat 6f Standard 3/11 fig 57; 6 Nov Newcastle (AW) Flat 6f Standard 7/14 fig 56
    DATA for: Carries 10 lb less than average
    DATA against: Official rating 56, 10 lb below field average
- Come On Eibhlin (hrs_53841102) | 3yo F | 132lb | OR 67 | draw 5 | jockey Andrew Mullen | trainer Ben Haslam (14d 2/7) | headgear - | last run 77 days | form 345930 | MARKET 4.0% | 09:00 median 21.00 | Matchbook 26.00
    comment: The main risk is a 77-day layoff after an unplaced latest run, and she remains winless in her last six.
    DATA: model 9.4% | style Midfield (led 4% of runs) | runs in data 9 | last 3: 29 Jul Sandown Flat 9.9f Good To Firm 9/10; 11 Aug Nottingham Flat 6.1f Good To Firm 3/6; 7 Sep Windsor Flat 6.1f Good 11/13
    DATA for: Trainer 29% wins (2/7), last 14 days

## 6:45 Newcastle (AW) | race_id rac_32305266058 | Midnite: Built For 2026 Not 2006 Handicap Stakes
Flat | Class 6 | 6f | going Standard | AW | 14 runners | rating band 0-55 | age 3yo+
DATA pace: Even - Two likely leaders (Tomorrow Day, Henriette Ronner). A fair, even gallop is most likely.
- Lord Abama (hrs_27166524) | 7yo G | 131lb | OR 52 | draw 7 | jockey Billy Loughnane | trainer Michael Dods (14d 0/7) | headgear b | last run 17 days | form 973413 | MARKET 19.8% | 09:00 median 4.00 | Matchbook 4.40 | CHECK (skip line 3.80)
    comment: Lord Abama is in cracking recent form, third last time out, and a winner two starts back, with just 17 days since that run keeping him fresh.
    DATA: model 12.0% | style Prominent (led 29% of runs) | runs in data 12 | last 3: 25 Sep Newcastle Flat 6f Standard 4/12; 20 Oct Newcastle (AW) Flat 6f Standard 1/12 fig 51; 6 Nov Newcastle (AW) Flat 6f Standard 3/14 fig 55
    DATA for: Best recent form figure 55, 7 lb above field average; Has won at this trip or further; Good recent finishing positions
- Multaneighttothree (hrs_60527747) | 4yo G | 134lb | OR 55 | draw 9 | jockey Oliver Stammers | trainer Grant Tuer (14d 0/4) | headgear - | last run 95 days | form 3594 | MARKET 17.2% | 09:00 median 4.33 | Matchbook 5.30
    comment: Multaneighttothree is winless in his last four, with a ninth and a fifth in that sequence, and he returns after 95 days off.
    DATA: model 6.0% | style Midfield (led 4% of runs) | runs in data 4 | last 3: 4 Feb Newcastle Flat 8f Standard 5/10; 24 Feb Newcastle Flat 8f Standard 9/10; 20 Aug Newcastle Flat 6f Standard 4/14
    DATA against: Returns from a 95-day break
- Tomorrow Day (hrs_36137451) | 5yo G | 132lb | OR 53 | draw 1 | jockey Rhys Elliott(5) | trainer Mark Usher (14d 0/3) | headgear tv | last run 24 days | form 0-2213 | MARKET 11.6% | 09:00 median 7.00 | Matchbook 7.40
    comment: Tomorrow Day has been in the frame in four of his last five, including a win two starts back and a third last time out, and he has run over today's trip and going.
    DATA: model 17.3% | style Leader (led 38% of runs) | runs in data 4 | last 3: 11 Mar Newcastle Flat 6f Standard 2/7; 3 Sep Newcastle Flat 6f Standard 1/8; 30 Oct Newcastle (AW) Flat 7f Standard 3/11 fig 54
    DATA for: Best recent form figure 54, 6 lb above field average; Has won at this trip or further; Good recent finishing positions; Course: front-runners have won 1.3× their fair share at 6f here
- Henriette Ronner (hrs_49142877) | 3yo F | 131lb | OR 52 | draw 4 | jockey Darragh Keenan | trainer Charlie Clover (14d 1/3) | headgear - | last run 116 days | form 509852 | MARKET 7.6% | 09:00 median 9.00 | Matchbook 13.00
    comment: Henriette Ronner arrives off a second last time out, though she has been beaten in the five runs before that and returns after 116 days away.
    DATA: model 4.5% | style Leader (led 57% of runs) | runs in data 10 | last 3: 9 Jul Carlisle Flat 5.8f Good To Firm 8/11; 23 Jul Southwell Flat 5f Standard 5/7; 30 Jul Nottingham Flat 6.1f Good To Firm 2/7
    DATA for: Has won at this trip or further; Course: front-runners have won 1.3× their fair share at 6f here
    DATA against: Returns from a 116-day break
- Yaaser (hrs_22439851) | 8yo G | 130lb | OR 51 | draw 3 | jockey Lauren Young(5) | trainer Jim Goldie (14d 1/7) | headgear - | last run 17 days | form 488395 | MARKET 7.6% | 09:00 median 9.00 | Matchbook 13.00
    comment: The main risk is that he is winless in his last six and carries 130 lb from stall three.
    DATA: model 8.6% | style Held up (led 4% of runs) | runs in data 15 | last 3: 25 Sep Newcastle Flat 10.2f Standard 3/14; 30 Oct Newcastle (AW) Flat 10f Standard 9/14 fig 43; 6 Nov Newcastle (AW) Flat 8f Standard 5/14 fig 50
    DATA for: Last-run finishing speed +2.1% vs that field (finished strongly)
    DATA against: Aged 8, older than most of this field
- Reenie's Dream (hrs_51766792) | 4yo F | 132lb | OR 53 | draw 11 | jockey Oisin McSweeney | trainer Bryan Smart (14d 1/4) | headgear h | last run 42 days | form 488416 | MARKET 7.4% | 09:00 median 11.00 | Matchbook 11.50
    comment: Reenie's Dream won two starts back but was only sixth last time out, and she returns after 42 days off having run over today's trip and going before.
    DATA: model 12.4% | style Unknown | runs in data 8 | last 3: 3 Sep Newcastle Flat 6f Standard 4/7; 25 Sep Newcastle Flat 6f Standard 1/12; 12 Oct Newcastle Flat 6f Standard 6/12
    DATA for: Has won at this trip or further
- Teardrops (hrs_39962335) | 4yo G | 132lb | OR 53 | draw 5 | jockey Darragh O'Sullivan(7) | trainer Tony Carroll (14d 1/26) | headgear b | last run 16 days | form 480003 | MARKET 7.2% | 09:00 median 11.00 | Matchbook 12.50
    comment: Teardrops comes into this on the back of a third last time out, just 16 days ago, and has run over today's trip and going before, but he is winless in his last six and unplaced in the three runs before that.
    DATA: model 4.3% | style Midfield (led 4% of runs) | runs in data 12 | last 3: 28 Jun Wolverhampton Flat 6.1f Standard 10/12; 2 Oct Wolverhampton Flat 5.1f Standard 10/11; 7 Nov Southwell (AW) Flat 6f Standard 3/11 fig 50
    DATA for: Has won at this trip or further
- Triple P (hrs_7000002303) | 3yo G | 134lb | OR 55 | draw 12 | jockey Duran Fentiman | trainer Tim Easterby (14d 1/10) | headgear - | last run 38 days | form 43280 | MARKET 4.6% | 09:00 median 17.00 | Matchbook 20.00
    comment: Triple P is yet to win in his last five starts, though a second and a third in that run show he can get involved, and he has run over today's trip and going; unplaced last time and 38 days off, he carries 134 lb from stall 12.
    DATA: model 6.3% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 8 Sep Catterick Flat 6f Good To Soft 2/6; 26 Sep Ripon Flat 6f Good 8/11; 16 Oct Redcar Flat 7f Good 15/18 fig 31
    DATA against: Best recent form figure 31, 17 lb below field average; Recent figures 24 lb below its current mark (looks high in the weights)
- Kilfrush Blue (hrs_55484653) | 3yo G | 134lb | OR 55 | draw 2 | jockey James Sullivan | trainer Ruth Carr (14d 1/5) | headgear - | last run 159 days | form 8-95 | MARKET 4.5% | 09:00 median 15.00 | Matchbook 25.00
    comment: Kilfrush Blue is winless in his last three, finishing fifth last time out after a ninth and an eighth, and he returns from 159 days off carrying 134 lb from draw 2.
    DATA: model 2.1% | style Held up (led 5% of runs) | runs in data 2 | last 3: 16 May Doncaster Flat 6f Good To Soft 9/10; 17 Jun Ripon Flat 6f Good 5/5
    DATA for: Trainer 20% wins (1/5), last 14 days
    DATA against: Returns from a 159-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- Snuggle (hrs_30231964) | 6yo G | 134lb | OR 55 | draw 6 | jockey Tom Eaves | trainer Thomas Faulkner (14d 0/5) | headgear - | last run 28 days | form 64-498 | MARKET 3.1% | 09:00 median 26.00 | Matchbook 30.00
    comment: The main risk is a form line showing an eighth last time out and a ninth before that, and he is yet to win in his last five starts.
    DATA: model 8.8% | style Prominent (led 8% of runs) | runs in data 3 | last 3: 21 May Chepstow Flat 6.1f Good To Soft 4/12; 6 Jun Chepstow Flat 6.1f Soft 9/11; 26 Oct Redcar Flat 6f Heavy 8/14 fig 60
    DATA for: Best recent form figure 60, 12 lb above field average; Recent figures 5 lb above its current mark (looks well handicapped)
- Believe In Lies (hrs_50123444) | 5yo M | 134lb | OR 55 | draw 8 | jockey William Pyle | trainer David & Nicola Barron (14d 0/0) | headgear - | last run 273 days | form 0-5533 | MARKET 3.1% | 09:00 median 23.00 | Matchbook 36.00
    comment: Back-to-back thirds in her last two starts show she's in decent heart, and she has run over today's trip and going, but she's yet to win in recent form and returns after 273 days off.
    DATA: model 9.0% | style Midfield (led 3% of runs) | runs in data 4 | last 3: 13 Jan Newcastle Flat 7.1f Standard 5/6; 9 Feb Wolverhampton Flat 7.2f Standard 3/11; 23 Feb Wolverhampton Flat 7.2f Standard 3/9
    DATA for: Good recent finishing positions
    DATA against: Returns from a 273-day break
- Ramon di Loria (hrs_22241121) | 8yo G | 131lb | OR 52 | draw 13 | jockey Greg Fairley | trainer Ewan Whillans (14d 0/8) | headgear p | last run 16 days | form 332680 | MARKET 2.9% | 09:00 median 26.00 | Matchbook 34.00
    comment: Ramon di Loria was second four starts back and third in the two runs before that, and he's fresh from a 16-day break with experience of today's trip and going.
    DATA: model 3.0% | style Prominent (led 4% of runs) | runs in data 17 | last 3: 20 Jul Ayr Flat 7.2f Good To Firm 6/6; 12 Oct Musselburgh Flat 7.1f Good To Soft 8/11; 7 Nov Southwell (AW) Flat 7f Standard 10/12 fig 45
    DATA for: Has won at this trip or further
    DATA against: Recent figures 7 lb below its current mark (looks high in the weights); Trainer 0 wins from 8 runs, last 14 days; Poor recent finishing positions; Aged 8, older than most of this field
- Orbital Chime (hrs_31117912) | 6yo G | 131lb | OR 52 | draw 14 | jockey Mark Winn | trainer Helen Cuthbert (14d 0/0) | headgear v | last run 38 days | form 668607 | MARKET 1.9% | 09:00 median 41.00 | Matchbook 60.00
    comment: Winless in his last six, Orbital Chime has finished sixth or worse each time, including a seventh last time out, though he has run over today's trip and going before and arrives after 38 days off.
    DATA: model 3.9% | style Midfield (led 3% of runs) | runs in data 12 | last 3: 8 Jun Carlisle Flat 6.9f Soft 6/10; 9 Jul Carlisle Flat 5.8f Good To Firm 10/11; 16 Oct Newcastle (AW) Flat 7f Standard 7/9 fig 40
    DATA against: Best recent form figure 40, 8 lb below field average; Recent figures 12 lb below its current mark (looks high in the weights); Poor recent finishing positions
- Teddy Shaw (hrs_61307155) | 5yo G | 132lb | OR 53 | draw 10 | jockey Joanna Mason | trainer Ruth Carr (14d 1/5) | headgear - | last run 171 days | form 7800 | MARKET 1.4% | 09:00 median 50.50 | Matchbook 100.00
    comment: Teddy Shaw is winless in his last four, finishing unplaced twice, then an eighth three starts back and a seventh four starts back, and he returns after 171 days off.
    DATA: model 1.7% | style Held up (led 4% of runs) | runs in data 4 | last 3: 24 Feb Newcastle Flat 6f Standard 8/11; 19 Mar Newcastle Flat 6f Standard 10/11; 5 Jun Thirsk Flat 6f Good 10/10
    DATA for: Trainer 20% wins (1/5), last 14 days
    DATA against: Poor recent finishing positions; Returns from a 171-day break

## 7:15 Newcastle (AW) | race_id rac_32305267995 | Make The Move To Midnite Handicap Stakes
Flat | Class 6 | 5f | going Standard | AW | 13 runners | rating band 0-65 | age 3yo+
DATA pace: Lone leader - Water of Leith is the only habitual front-runner and may be allowed an easy lead.
- Simba's Pride (hrs_51800448) | 3yo G | 132lb | OR 62 | draw 14 | jockey Mark Winn | trainer Michael Dods (14d 0/7) | headgear h | last run 17 days | form 740323 | MARKET 18.3% | 09:00 median 4.17 | Matchbook 5.00 | CHECK (skip line 3.96)
    comment: Simba's Pride arrives in cracking nick, third last time out, a second two starts back and a third three starts back, and he's back after just 17 days.
    DATA: model 14.3% | style Midfield (led 5% of runs) | runs in data 15 | last 3: 5 Oct Pontefract Flat 5f Good 3/12; 20 Oct Newcastle (AW) Flat 5f Standard 2/13 fig 62; 6 Nov Newcastle (AW) Flat 5f Standard 3/14 fig 66
    DATA for: Best recent form figure 66, 10 lb above field average; Recent figures 4 lb above its current mark (looks well handicapped); Has won at this trip or further; Good recent finishing positions
- Too Much (hrs_33177837) | 6yo M | 131lb | OR 61 | draw 1 | jockey David Allan | trainer David Thompson (14d 0/3) | headgear h | last run 2 days | form 548628 | MARKET 16.8% | 09:00 median 4.42 | Matchbook 5.40
    comment: Eighth last time out just two days ago, Too Much is a quick turnaround, though she was second two starts back and has run over today's trip and going before.
    DATA: model 11.5% | style Held up (led 5% of runs) | runs in data 10 | last 3: 26 Oct Redcar Flat 6f Heavy 6/14 fig 61; 6 Nov Newcastle (AW) Flat 6f Standard 2/14 fig 66; 21 Nov Newcastle (AW) Flat 6f Standard 8/13 fig 52
    DATA for: Best recent form figure 66, 10 lb above field average; Recent figures 5 lb above its current mark (looks well handicapped); Has won at this trip or further
- Justmyluck (hrs_55634124) | 3yo G | 130lb | OR 60 | draw 11 | jockey William Pyle | trainer Linda Perratt (14d 0/4) | headgear h | last run 19 days | form 599704 | MARKET 14.3% | 09:00 median 5.50 | Matchbook 6.40
    comment: Justmyluck bounced back with a fourth last time out after a run of modest efforts, and he has run over today's trip and going before, but he is winless in his last six and carries 130 lb from stall 11.
    DATA: model 7.3% | style Held up (led 5% of runs) | runs in data 10 | last 3: 17 Sep Ayr Flat 5f Soft 7/20; 20 Oct Newcastle (AW) Flat 5f Standard 12/13 fig 50; 4 Nov Musselburgh Flat 5f Soft 4/11 fig 61
    DATA for: Best recent form figure 61, 4 lb above field average; Has won at this trip or further
- Sunday River (hrs_49141869) | 3yo F | 130lb | OR 60 | draw 13 | jockey Billy Loughnane | trainer Brian Ellison (14d 1/6) | headgear p (1st time) | last run 28 days | form 0-330 | MARKET 9.3% | 09:00 median 9.00 | Matchbook 9.40
    comment: Sunday River is winless in her last four and was unplaced last time out, though a third two starts back, and another third three starts back, show she can get involved.
    DATA: model 7.6% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 24 Sep Southwell Flat 5f Standard 3/5; 16 Oct Newcastle (AW) Flat 5f Standard 3/6 fig 60; 26 Oct Redcar Flat 6f Heavy 13/14 fig 34
    DATA for: Good recent finishing positions; First-time headgear
- Believeinmenow (hrs_51373749) | 3yo G | 135lb | OR 65 | draw 7 | jockey Faye McManoman | trainer Nigel Tinkler (14d 0/3) | headgear tv (1st time) | last run 24 days | form 394248 | MARKET 7.7% | 09:00 median 10.00 | Matchbook 12.00
    comment: The risk is an eighth last time out, so he needs to bounce back from that.
    DATA: model 9.6% | style Held up (led 5% of runs) | runs in data 10 | last 3: 5 Sep Newcastle Flat 6f Standard 2/14; 24 Sep Southwell Flat 5f Standard 4/5; 30 Oct Newcastle (AW) Flat 6f Standard 8/9 fig 54
    DATA for: First-time headgear
    DATA against: Recent figures 11 lb below its current mark (looks high in the weights)
- Hi Lord (hrs_45598490) | 4yo G | 134lb | OR 64 | draw 3 | jockey Conor Whiteley(5) | trainer Stephen Hanlon (14d 0/2) | headgear - | last run 46 days | form 305081 | MARKET 7.4% | 09:00 median 9.50 | Matchbook 13.50
    comment: The main risk is a 46-day break, plus a mixed record before that win and 134 lb to carry from stall three.
    DATA: model 14.2% | style Midfield (led 8% of runs) | runs in data 11 | last 3: 17 Sep Ayr Flat 5f Soft 11/20; 3 Oct Southwell Flat 5f Standard 8/10; 8 Oct Bath Flat 5f Good 1/14
    DATA for: Has won at this trip or further
- Toptime (hrs_20976088) | 8yo G | 132lb | OR 62 | draw 4 | jockey Darragh Keenan | trainer Roy Bowring (14d 0/2) | headgear - | last run 44 days | form 132715 | MARKET 7.3% | 09:00 median 10.00 | Matchbook 13.50
    comment: Toptime was only fifth last time out after winning two starts back, and he's been inconsistent in that spell, with a seventh three starts back in between.
    DATA: model 10.7% | style Prominent (led 8% of runs) | runs in data 7 | last 3: 8 Sep Leicester Flat 5f Good To Soft 7/11; 3 Oct Southwell Flat 5f Standard 1/10; 10 Oct Southwell Flat 6.1f Standard 5/8
    DATA for: Has won at this trip or further
    DATA against: Aged 8, older than most of this field
- Water of Leith (hrs_21972587) | 8yo G | 129lb | OR 59 | draw 9 | jockey Lauren Young(5) | trainer Jim Goldie (14d 1/7) | headgear - | last run 107 days | form 553650 | MARKET 5.8% | 09:00 median 12.00 | Matchbook 17.00
    comment: Winless in his last six, Water of Leith has been consistent in the pack, with a third four starts back his best finish, and he has run over today's trip and going before.
    DATA: model 4.2% | style Leader (led 72% of runs) | runs in data 16 | last 3: 13 Jul Ayr Flat 6f Good To Firm 6/8; 27 Jul Ayr Flat 6f Good To Firm 5/9; 8 Aug Ayr Flat 5f Good 12/12
    DATA for: Has won at this trip or further; Pace: may get an uncontested lead
    DATA against: Returns from a 107-day break; Aged 8, older than most of this field
- The Tunguska Event (hrs_55665981) | 3yo G | 129lb | OR 59 | draw 2 | jockey Jason Hart | trainer John & Sean Quinn (14d 1/6) | headgear - | last run 17 days | form 136470 | MARKET 3.3% | 09:00 median 26.00 | Matchbook 29.00
    comment: The Tunguska Event has drifted since winning six starts back, with a seventh two starts back and an unplaced run last time, though he's fresh enough after 17 days and has run over today's trip and going.
    DATA: model 4.9% | style Unknown | runs in data 10 | last 3: 22 Jul Leicester Flat 6f Good To Firm 4/8; 5 Aug Pontefract Flat 5f Good To Firm 7/9; 6 Nov Newcastle (AW) Flat 6f Standard 13/14 fig 25
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 25, 32 lb below field average; Recent figures 34 lb below its current mark (looks high in the weights); Last-run finishing speed -5.3% vs that field (faded)
- Herakles (hrs_32568480) | 6yo G | 135lb | OR 65 | draw 10 | jockey Ryan Sexton | trainer Paul Midgley (14d 0/3) | headgear - | last run 17 days | form 421400 | MARKET 3.2% | 09:00 median 26.00 | Matchbook 28.00
    comment: Herakles won four starts back and was a fourth three starts back, but he's been unplaced in his last two outings, so the form has tailed off.
    DATA: model 5.6% | style Held up (led 4% of runs) | runs in data 7 | last 3: 28 May Ripon Flat 5f Good 4/8; 20 Oct Newcastle (AW) Flat 5f Standard 13/13 fig 52; 6 Nov Newcastle (AW) Flat 5f Standard 12/14 fig 50
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 52, 4 lb below field average; Recent figures 13 lb below its current mark (looks high in the weights)
- Contorno (hrs_55061832) | 3yo G | 123lb | OR 53 | draw 12 | jockey Andrew Mullen | trainer Tom Tate (14d 0/0) | headgear - | last run 151 days | form 415980 | MARKET 2.7% | 09:00 median 26.00 | Matchbook 38.00
    comment: Contorno has been well beaten lately, unplaced last time out, then an eighth and a ninth, and he returns after 151 days off, so he is hard to fancy.
    DATA: model 2.2% | style Midfield (led 3% of runs) | runs in data 7 | last 3: 25 Apr Ripon Flat 6f Good 9/10; 9 May Nottingham Flat 5f Good To Firm 8/9; 25 Jun Newcastle Flat 5f Standard To Slow 10/12
    DATA for: Has won at this trip or further; Carries 8 lb less than average
    DATA against: Official rating 53, 8 lb below field average; Poor recent finishing positions; Returns from a 151-day break
- Fordham Flyer (hrs_56094843) | 3yo G | 129lb | OR 59 | draw 6 | jockey Cam Hardie | trainer Philip Kirby (14d 1/9) | headgear - | last run 28 days | form 4-9960 | MARKET 2.0% | 09:00 median 34.00 | Matchbook 60.00
    comment: Fordham Flyer has run over today's trip and on this going, but he's yet to win in his last five starts, with an unplaced effort last time out and a ninth three starts back.
    DATA: model 4.9% | style Held up (led 4% of runs) | runs in data 4 | last 3: 2 Oct Wolverhampton Flat 6.1f Standard 9/10; 16 Oct Haydock Flat 5f Heavy 6/14 fig 68; 26 Oct Redcar Flat 6f Heavy 12/14 fig 34
    DATA for: Best recent form figure 68, 12 lb above field average; Recent figures 9 lb above its current mark (looks well handicapped)
    DATA against: Poor recent finishing positions
- Cast No Shadow (hrs_36386959) | 5yo G | 131lb | OR 61 | draw 5 | jockey Cieren Fallon | trainer Hugo Palmer (14d 0/1) | headgear b | last run 305 days | form 3807-8 | MARKET 1.8% | 09:00 median 41.00 | Matchbook 60.00
    comment: Cast No Shadow is hard to fancy, having finished eighth last time out and seventh two starts back, and he is winless in his last five. He returns from 305 days off and has run over today's trip and going, and a third five starts back is the best of it, but 131 lb from stall 5 is a lot to ask.
    DATA: model 3.1% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 22 Jan Southwell Flat 5f Standard 8/8
    DATA against: Last-run finishing speed -6.2% vs that field (faded); Returns from a 305-day break; Lightly raced: 1 run in our data, so the model has little to go on

## 7:45 Newcastle (AW) | race_id rac_32305269932 | AW Trials Day - Lingfield 2nd Jan 2027 Handicap Stakes
Flat | Class 6 | 1m5y | going Standard | AW | 14 runners | rating band 0-55 | age 3yo+
DATA pace: Lone leader - Pallas Lord is the only habitual front-runner and may be allowed an easy lead.
- Concert Boy (hrs_29917818) | 6yo G | 135lb | OR 55 | draw 4 | jockey Jason Hart | trainer Katie Scott (14d 0/3) | headgear b | last run 2 days | form 706415 | MARKET 25.1% | 09:00 median 3.25 | Matchbook 3.35 | CHECK (skip line 3.09)
    comment: Concert Boy was fifth last time out, and a winner two starts back, but he's back after just two days and has a mixed run of finishes behind him.
    DATA: model 16.1% | style Held up (led 3% of runs) | runs in data 17 | last 3: 30 Sep Musselburgh Flat 7.1f Good To Soft 4/11; 30 Oct Newcastle (AW) Flat 7f Standard 1/11 fig 55; 21 Nov Newcastle (AW) Flat 8f Standard 5/13 fig 52
    DATA for: Best recent form figure 55, 8 lb above field average
- Barleybrown (hrs_30567817) | 6yo G | 134lb | OR 54 | draw 5 | jockey Joanna Mason | trainer Ruth Carr (14d 1/5) | headgear b | last run 17 days | form 522442 | MARKET 16.5% | 09:00 median 4.50 | Matchbook 5.50
    comment: Barleybrown has been consistent, second last time out after 17 days off and a second again four starts back, yet he's winless in his last six and has run over today's trip and going before.
    DATA: model 10.1% | style Held up (led 3% of runs) | runs in data 12 | last 3: 25 Sep Newcastle Flat 8f Standard 4/11; 17 Oct Southwell (AW) Flat 8f Standard 4/11 fig 51; 6 Nov Newcastle (AW) Flat 8f Standard 2/14 fig 54
    DATA for: Best recent form figure 54, 7 lb above field average; Trainer 20% wins (1/5), last 14 days; Last-run finishing speed +2.8% vs that field (finished strongly)
- Boy Star (hrs_57590596) | 3yo C | 133lb | OR 55 | draw 1 | jockey Oisin Orr | trainer Richard & Peter Fahey (14d 0/8) | headgear - | last run 27 days | form 800-8 | MARKET 9.0% | 09:00 median 8.50 | Matchbook 10.00
    comment: Boy Star has finished eighth last time out and is winless in his last four starts, with an eighth four starts back too, so he is hard to fancy.
    DATA: model 5.8% | style Held up (led 8% of runs) | runs in data 1 | last 3: 27 Oct Wolverhampton (AW) Flat 7f Standard 8/11 fig 51
    DATA for: Best recent form figure 51, 4 lb above field average
    DATA against: Trainer 0 wins from 8 runs, last 14 days; Lightly raced: 1 run in our data, so the model has little to go on
- African Spirit (hrs_37289504) | 5yo G | 133lb | OR 53 | draw 2 | jockey Billy Loughnane | trainer Ian Williams (14d 2/14) | headgear tp | last run 30 days | form 833317 | MARKET 8.9% | 09:00 median 8.50 | Matchbook 10.00
    comment: African Spirit won two starts back and has been third three times in his last six, but he was only seventh last time out after 30 days off.
    DATA: model 12.2% | style Midfield (led 3% of runs) | runs in data 7 | last 3: 10 Sep Lingfield Flat 7f Standard 3/11; 29 Sep Wolverhampton Flat 8.6f Standard 1/8; 24 Oct Southwell (AW) Flat 8f Standard 7/13 fig 49
    DATA for: Has won at this trip or further; Good recent finishing positions
- Haltonwood (hrs_61943378) | 3yo G | 131lb | OR 53 | draw 12 | jockey David Nolan | trainer Ivan Furtado (14d 1/10) | headgear v (1st time) | last run 17 days | form 943508 | MARKET 7.2% | 09:00 median 11.00 | Matchbook 12.50
    comment: The risk is a form line that reads eighth last time out and winless in his last six.
    DATA: model 3.6% | style Prominent (led 3% of runs) | runs in data 8 | last 3: 2 Oct Newcastle Flat 10.2f Standard 5/9; 16 Oct Redcar Flat 10f Good 14/14; 6 Nov Newcastle (AW) Flat 8f Standard 8/14 fig 47
    DATA for: First-time headgear
    DATA against: Recent figures 6 lb below its current mark (looks high in the weights)
- Oilisa (hrs_46667971) | 4yo F | 133lb | OR 53 | draw 11 | jockey Jack Garritty | trainer Mark Walford (14d 2/6) | headgear - | last run 75 days | form 6-0052 | MARKET 5.3% | 09:00 median 13.00 | Matchbook 19.00
    comment: Oilisa arrives on the back of a second last time out, a clear step up on a fifth two starts back, and she has experience of both today's trip and the going.
    DATA: model 8.0% | style Midfield (led 3% of runs) | runs in data 4 | last 3: 17 May Ripon Flat 8f Good 10/13; 30 May Beverley Flat 8.5f Good To Firm 5/11; 9 Sep Redcar Flat 8f Good 2/19
    DATA for: Trainer 33% wins (2/6), last 14 days; Last-run finishing speed +2.9% vs that field (finished strongly)
- Walk On Walk On (hrs_53148704) | 3yo G | 131lb | OR 53 | draw 6 | jockey Ryan Sexton | trainer Philip Kirby (14d 1/9) | headgear p | last run 17 days | form 527167 | MARKET 5.2% | 09:00 median 13.00 | Matchbook 19.00
    comment: Walk On Walk On has finished seventh and sixth in his last two outings, so he is hard to fancy, though he did win three starts back and has run over today's trip and going.
    DATA: model 7.6% | style Prominent (led 23% of runs) | runs in data 10 | last 3: 2 Sep Newcastle Flat 8f Standard 1/9; 19 Sep Newcastle Flat 8f Standard 6/10; 6 Nov Newcastle (AW) Flat 8f Standard 7/14 fig 48
    DATA for: Has won at this trip or further
- Infantry Officer (hrs_40919452) | 4yo G | 133lb | OR 53 | draw 9 | jockey Darragh O'Sullivan(7) | trainer Tony Carroll (14d 1/26) | headgear - | last run 16 days | form 5796-8 | MARKET 4.1% | 09:00 median 17.00 | Matchbook 25.00
    comment: The main risk is a yard in poor form, just 1/26 lately.
    DATA: model 3.3% | style Unknown | runs in data 1 | last 3: 7 Nov Southwell (AW) Flat 7f Standard 8/12 fig 47
    DATA against: Recent figures 6 lb below its current mark (looks high in the weights); Lightly raced: 1 run in our data, so the model has little to go on
- Ravenswell (hrs_38002335) | 5yo G | 129lb | OR 49 | draw 13 | jockey Tom Eaves | trainer Thomas Faulkner (14d 0/5) | headgear t (1st time) | last run 28 days | form 7-5883 | MARKET 4.0% | 09:00 median 17.00 | Matchbook 26.00
    comment: He has run over today's trip and going, and is fresh enough after 28 days, but 129 lb from stall 13 is a big ask.
    DATA: model 6.1% | style Held up (led 3% of runs) | runs in data 4 | last 3: 4 Jun Hamilton Flat 12.1f Good 8/11; 26 Aug Wolverhampton Flat 12.2f Standard 8/11; 26 Oct Redcar Flat 10f Heavy 3/14 fig 53
    DATA for: Best recent form figure 53, 6 lb above field average; Recent figures 4 lb above its current mark (looks well handicapped); Last-run finishing speed +5.9% vs that field (finished strongly); First-time headgear
- Ana Emaraaty (hrs_31725148) | 6yo G | 133lb | OR 53 | draw 8 | jockey Lauren Young(5) | trainer Jim Goldie (14d 1/7) | headgear b | last run 17 days | form 184590 | MARKET 3.7% | 09:00 median 19.00 | Matchbook 28.00
    comment: Ana Emaraaty has been below his best lately, unplaced last time out and a ninth two starts back, though he did win six starts back and has run over today's trip and going.
    DATA: model 4.0% | style Held up (led 5% of runs) | runs in data 7 | last 3: 27 Feb Wolverhampton Flat 8.6f Standard 5/11; 5 Mar Newcastle Flat 10.2f Standard 9/10; 6 Nov Newcastle (AW) Flat 8f Standard 10/14 fig 47
    DATA against: Recent figures 6 lb below its current mark (looks high in the weights)
- Penny Mountain (hrs_42195531) | 5yo M | 130lb | OR 50 | draw 10 | jockey Greg Fairley | trainer Gary Rutherford (14d 0/1) | headgear - | last run 17 days | form 633550 | MARKET 3.4% | 09:00 median 15.00 | Matchbook 44.00
    comment: Penny Mountain is winless in her last six, though two thirds four and five starts back and back-to-back fifths show she's rarely far away, and she has run over today's trip and going.
    DATA: model 3.7% | style Held up (led 3% of runs) | runs in data 14 | last 3: 5 Jul Ayr Flat 7.2f Good 5/11; 13 Jul Ayr Flat 7.2f Good To Firm 5/9; 6 Nov Newcastle (AW) Flat 6f Standard 13/14 fig 25
    DATA against: Best recent form figure 25, 22 lb below field average; Recent figures 25 lb below its current mark (looks high in the weights)
- Misemerald (hrs_35895832) | 5yo M | 131lb | OR 51 | draw 7 | jockey Kevin Stott | trainer Philip Kirby (14d 1/9) | headgear p | last run 54 days | form 423135 | MARKET 3.3% | 09:00 median 21.00 | Matchbook 36.00
    comment: Misemerald has been consistent, with a win three starts back and a third two starts back, but she was only fifth last time out and returns after 54 days off.
    DATA: model 12.3% | style Midfield (led 3% of runs) | runs in data 11 | last 3: 24 Aug Musselburgh Flat 8f Good 1/13; 28 Aug Thirsk Flat 8f Good 3/11; 30 Sep Musselburgh Flat 7.1f Good To Soft 5/11
    DATA for: Has won at this trip or further; Good recent finishing positions
- Kelpie Grey (hrs_31287837) | 6yo G | 132lb | OR 52 | draw 14 | jockey Rhys Elliott(5) | trainer Jim Goldie (14d 1/7) | headgear v | last run 17 days | form 732390 | MARKET 2.3% | 09:00 median 34.00 | Matchbook 55.00
    comment: Kelpie Grey has been in the frame in three of his last six, including a second four starts back, and he's fresh from a 17-day break, having run over today's trip and going before.
    DATA: model 5.4% | style Midfield (led 4% of runs) | runs in data 15 | last 3: 30 Sep Musselburgh Flat 7.1f Good To Soft 3/11; 12 Oct Musselburgh Flat 7.1f Good To Soft 9/11; 6 Nov Newcastle (AW) Flat 8f Standard 13/14 fig 40
    DATA against: Best recent form figure 40, 7 lb below field average; Recent figures 12 lb below its current mark (looks high in the weights)
- Pallas Lord (hrs_24651375) | 8yo G | 129lb | OR 49 | draw 3 | jockey Sean Kirrane | trainer Donald Whillans (14d 0/3) | headgear t | last run 17 days | form 740000 | MARKET 2.1% | 09:00 median 29.00 | Matchbook 70.00
    comment: Pallas Lord is yet to win in his last six starts, with four unplaced runs since a fourth five starts back, though he has run over today's trip and going and is fresh enough after 17 days.
    DATA: model 1.8% | style Leader (led 43% of runs) | runs in data 15 | last 3: 12 Oct Musselburgh Flat 7.1f Good To Soft 10/11; 30 Oct Newcastle (AW) Flat 7f Standard 10/10 fig 23; 6 Nov Newcastle (AW) Flat 8f Standard 11/14 fig 43
    DATA for: Pace: may get an uncontested lead
    DATA against: Recent figures 6 lb below its current mark (looks high in the weights); Last-run finishing speed -2.4% vs that field (faded); Poor recent finishing positions; Aged 8, older than most of this field
