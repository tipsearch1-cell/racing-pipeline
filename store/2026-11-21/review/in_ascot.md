# Card review packet: Ascot, 2026-11-21

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
{"meeting": "ascot", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 12:20 Ascot | race_id rac_32305060736 | Ascot Shared Ownership Weekend Novices' Hurdle Race (GBB Race)
Hurdle | Class 2 | 2m5f146y | going Good To Firm | Turf | 6 runners | rating band - | age 4yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- The Walk (hrs_58282980) | 5yo G | 159lb | OR - | draw 0 | jockey Dylan Johnston | trainer Joe Tizzard (14d 7/26) | headgear - | last run 30 days | form 10-1 | MARKET 48.6% | 09:00 median 1.83 | Matchbook 2.02
    DATA: model 22.5% | style Unknown | runs in data 1 | last 3: 22 Oct Ffos Las Hurdle 16f Soft 1/10 fig 117
    DATA for: Best recent form figure 117, 9 lb above field average; Trainer 27% wins (7/26), last 14 days; Last-run finishing speed +6.7% vs that field (finished strongly)
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Vedivici (hrs_17395089026) | 4yo G | 153lb | OR - | draw 0 | jockey Ben Jones | trainer Ben Pauling (14d 4/25) | headgear - | last run 202 days | form 2- | MARKET 21.4% | 09:00 median 4.33 | Matchbook 4.50
    DATA: model 10.7% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 202-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Katarcice (hrs_46483052) | 6yo G | 159lb | OR 112 | draw 0 | jockey Jack Hogan | trainer Fergal O'Brien (14d 3/31) | headgear t | last run 18 days | form -23512 | MARKET 18.5% | 09:00 median 5.00 | Matchbook 5.20
    DATA: model 33.0% | style Prominent (led 23% of runs) | runs in data 7 | last 3: 25 Sep Worcester Hurdle 20f Good 5/15; 17 Oct Stratford Hurdle 22f Good 1/7 fig 107; 3 Nov Warwick Hurdle 21f Good 2/10 fig 111
    DATA for: Last-run finishing speed +4.6% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
- Handmedownastar (hrs_50188775) | 6yo G | 162lb | OR 118 | draw 0 | jockey Jonathan Burke | trainer Nick Scholfield (14d 1/14) | headgear p | last run 21 days | form -151P8 | MARKET 7.4% | 09:00 median 12.00 | Matchbook 13.50
    DATA: model 16.1% | style Prominent (led 23% of runs) | runs in data 7 | last 3: 16 Sep Kelso Hurdle 20.9f Good To Firm 1/2; 9 Oct Chepstow Hurdle 19.5f Good To Soft PU/11; 31 Oct Ascot Hurdle 19.5f Good To Firm 8/9
    DATA against: Last-run finishing speed -6.3% vs that field (faded); Pulled up in 1 of its last 5 jumps runs
- Ar Aghaidh Leat (hrs_17395446775) | 5yo M | 147lb | OR - | draw 0 | jockey Sam Twiston-Davies | trainer Phil McEntee (14d 0/1) | headgear h | last run 5 days | form U54-12 | MARKET 3.1% | 09:00 median 26.00 | Matchbook 36.00
    DATA: model 6.9% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 16 Nov Plumpton Hurdle 20.5f Good To Soft 2/6 fig 96
    DATA against: Best recent form figure 96, 12 lb below field average; Lightly raced: 1 run in our data, so the model has little to go on
- Ava's Friend Bill (hrs_17395805567) | 5yo G | 154lb | OR - | draw 0 | jockey Robert Dunne | trainer Rob Summers (14d 0/1) | headgear - | last run - days | form - | MARKET 1.0% | 09:00 median 67.00 | Matchbook 180.00
    DATA: model 10.9% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on

## 12:55 Ascot | race_id rac_32305062673 | Ladbrokes 1965 Steeple Chase (Grade 2) (GBB Race)
Chase | Class 1 | 2m5f13y | going Good To Firm | Turf | 3 runners | rating band - | age 4yo+
DATA pace: Even - Two likely leaders (Doyen Quest, Master Chewy). A fair, even gallop is most likely.
- Blow Your Wad (hrs_28489034) | 8yo G | 158lb | OR 151 | draw 0 | jockey Freddie Mitchell | trainer Jamie Moore & Josh Moore (14d 1/23) | headgear tp | last run 210 days | form 32412- | MARKET 38.2% | 09:00 median 2.50 | Matchbook 2.60
    comment: Blow Your Wad bids to build on a second last time out, with a win two starts back and a third five starts back in a solid recent run, and he has run over today's trip and going before. The main risk is a 210-day absence under 158 lb, with his yard also out of form.
    DATA: model 51.9% | style Held up (led 8% of runs) | runs in data 5 | last 3: 10 Mar Cheltenham Chase 25f Good To Soft 4/22; 2 Apr Chepstow Chase 19.4f Good To Soft 1/6; 25 Apr Sandown Chase 22.7f Good 2/5
    DATA for: Good recent finishing positions
    DATA against: Returns from a 210-day break; Race comments mention jumping mistakes in 2 of its last 5 runs
- Master Chewy (hrs_27428681) | 9yo G | 158lb | OR 151 | draw 0 | jockey Sam Twiston-Davies | trainer Nigel & Willy Twiston-Davies (14d 4/25) | headgear - | wind surgery | last run 15 days | form 7256-4 | MARKET 38.1% | 09:00 median 2.50 | Matchbook 2.60
    comment: Master Chewy is yet to win in his last five, but he was fourth last time out just 15 days ago and has run over today's trip and going, while a second four starts back shows his ceiling.
    DATA: model 14.6% | style Prominent (led 54% of runs) | runs in data 4 | last 3: 7 Feb Newbury Chase 16.4f Heavy 5/6; 12 Mar Cheltenham Chase 20.6f Good 6/7; 6 Nov Aintree Chase 25f Good To Soft 4/12 fig 150
- Doyen Quest (hrs_29623195) | 8yo G | 162lb | OR 147 | draw 0 | jockey Tristan Durrell | trainer Dan Skelton (14d 17/80) | headgear - | last run 20 days | form 2241-3 | MARKET 23.7% | 09:00 median 4.00 | Matchbook 4.20
    comment: Doyen Quest arrives in fine fettle, third last time out and a winner two starts back, with a second four starts back and another five starts back, and he has run over today's trip and going before. The main risk is his 162 lb burden on an official mark of 147.
    DATA: model 33.5% | style Leader (led 72% of runs) | runs in data 4 | last 3: 10 Apr Aintree Chase 25f Good To Soft 4/8; 25 Apr Sandown Chase 22.7f Good 1/5; 1 Nov Carlisle Chase 20f Good 3/3
    DATA for: Trainer 21% wins (17/80), last 14 days; Has won at this trip or further; Good recent finishing positions

## 1:30 Ascot | race_id rac_32305064610 | Ladbrokes Ascot Hurdle Race (Grade 2) (Registered As The Ascot Hurdle Race) (GBB Race)
Hurdle | Class 1 | 2m3f63y | going Good To Firm | Turf | 3 runners | rating band - | age 4yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Lucky Place (hrs_35363559) | 7yo G | 154lb | OR 150 | draw 0 | jockey Nico de Boinville | trainer Nicky Henderson (14d 2/14) | headgear - | last run 14 days | form 2302-3 | MARKET 62.7% | 09:00 median 1.53 | Matchbook 1.60
    comment: Lucky Place is bang in form, placed in four of his last five, including a third last time out and a second two starts back, and he's fit after just 14 days.
    DATA: model 31.1% | style Midfield (led 23% of runs) | runs in data 4 | last 3: 11 Mar Cheltenham Hurdle 21f Good 12/24; 25 Apr Sandown Hurdle 21.5f Good 2/4; 7 Nov Aintree Hurdle 17f Good To Soft 3/4 fig 141
    DATA for: Best recent form figure 141, 9 lb above field average; Official rating 150, 10 lb above field average; Good recent finishing positions
- Kateira (hrs_28851865) | 9yo M | 147lb | OR 140 | draw 0 | jockey Tristan Durrell | trainer Dan Skelton (14d 17/80) | headgear - | last run 21 days | form 896-01 | MARKET 33.7% | 09:00 median 2.88 | Matchbook 2.92
    comment: Kateira bounces in as a last-time-out winner after 21 days off, and she has run over today's trip and going before, so conditions hold no fears. The risk is a patchy record before that win, with nothing better than a sixth in the three runs prior, while carrying 147 lb.
    DATA: model 35.7% | style Held up (led 3% of runs) | runs in data 5 | last 3: 11 Mar Cheltenham Hurdle 21f Good 6/24; 9 Oct Chepstow Hurdle 16.1f Good To Soft 12/17; 31 Oct Wetherby Hurdle 16f Good 1/4 fig 132
    DATA for: Trainer 21% wins (17/80), last 14 days
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Fiveonefive (hrs_30672138) | 8yo G | 154lb | OR 129 | draw 0 | jockey Ben Harvey | trainer Cian Collins (14d 0/5) | headgear p | last run 7 days | form 431998 | MARKET 3.6% | 09:00 median 26.00 | Matchbook 29.00
    comment: Fiveonefive has run over today's trip and on the going, and a win four starts back shows he can deliver, with a third five starts back also in the book. Back in action just seven days after an eighth last time, the main risk is that he has finished ninth in two of his last three.
    DATA: model 33.2% | style Held up (led 4% of runs) | runs in data 10 | last 3: 8 Oct Thurles Flat 16.6f Yielding To Soft 4/9; 23 Oct Cheltenham Hurdle 16.5f Good To Soft 9/11 fig 123; 14 Nov Navan (IRE) Hurdle 16f Good To Yielding 8/15 fig 124
    DATA against: Best recent form figure 124, 8 lb below field average; Official rating 129, 11 lb below field average; Pace: steady gallop likely, hard to come from off the pace

## 2:05 Ascot | race_id rac_32305066547 | Ladbrokes Get Your Free Racing Bet Today Mares' Handicap Hurdle Race
Hurdle | Class 3 | 3m0f102y | going Good To Firm | Turf | 8 runners | rating band 0-130 | age 4yo+
DATA pace: Even - Two likely leaders (Smugglers Haven, Easy Love). A fair, even gallop is most likely.
- Easy Love (hrs_41052599) | 6yo M | 159lb | OR 116 | draw 0 | jockey Sam Twiston-Davies | trainer Anthony Honeyball (14d 3/10) | headgear - | last run 229 days | form P16P7- | MARKET 23.2% | 09:00 median 3.75 | Matchbook 4.20 | CHECK (skip line 3.56)
    comment: Easy Love is hard to fancy after a seventh last time out, with a pulled up two starts back and 229 days off the track, though she did win four starts back and has run over today's trip and going before.
    DATA: model 9.0% | style Leader (led 83% of runs) | runs in data 4 | last 3: 7 Feb Warwick Hurdle 19f Heavy 6/9; 28 Feb Doncaster Hurdle 24.4f Soft PU/8; 6 Apr Plumpton Hurdle 20.5f Good 7/12
    DATA for: Trainer 30% wins (3/10), last 14 days
    DATA against: Poor recent finishing positions; Returns from a 229-day break; Pulled up in 1 of its last 4 jumps runs
- Love of Neymore (hrs_29313060) | 8yo M | 161lb | OR 118 | draw 0 | jockey Charlie Price | trainer Robbie Llewellyn (14d 0/4) | headgear p | last run 28 days | form 4U42-5 | MARKET 17.6% | 09:00 median 5.00 | Matchbook 5.50
    comment: Fifth last time out, 28 days ago, after a second two starts back, Love of Neymore is consistent without being winning, and she has run over today's trip and going before.
    DATA: model 11.4% | style Prominent (led 4% of runs) | runs in data 6 | last 3: 26 Feb Ludlow Hurdle 23.8f Good To Soft 4/6; 18 Apr Ayr Hurdle 24.3f Heavy 3/9; 24 Oct Cheltenham Hurdle 24f Good 5/19 fig 114
    DATA against: Fell or unseated in 1 of its last 5 jumps runs
- That's Nice (hrs_39431868) | 6yo M | 164lb | OR 121 | draw 0 | jockey Nico de Boinville | trainer Nicky Henderson (14d 2/14) | headgear p | last run 24 days | form 334181 | MARKET 16.4% | 09:00 median 5.00 | Matchbook 6.20
    comment: Fresh from a win last time out, and a winner three starts back too, she comes here 24 days after that success and has run over today's trip and going, though an eighth two starts back shows the consistency isn't there.
    DATA: model 17.9% | style Prominent (led 5% of runs) | runs in data 8 | last 3: 4 Sep Worcester Hurdle 20f Good 1/8; 25 Sep Worcester Hurdle 23f Good 8/9; 28 Oct Huntingdon Hurdle 25f Good 1/6 fig 117
    DATA for: Last-run finishing speed +4.8% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
- Porter In The Park (hrs_29326920) | 9yo M | 156lb | OR 113 | draw 0 | jockey Cameron Johnstone-Baker(7) | trainer Emma Lavelle (14d 3/17) | headgear - | last run 13 days | form -3P625 | MARKET 12.3% | 09:00 median 7.00 | Matchbook 8.00
    comment: The main risk is the 156 lb she must carry, with her recent form still winless.
    DATA: model 10.2% | style Midfield (led 4% of runs) | runs in data 7 | last 3: 5 Sep Stratford Hurdle 22f Good 6/8; 28 Oct Huntingdon Hurdle 25f Good 2/6 fig 113; 8 Nov Sandown Hurdle 20f Good To Soft 5/8 fig 107
    DATA for: Carries 6 lb less than average
    DATA against: Official rating 113, 6 lb below field average; Pulled up in 1 of its last 5 jumps runs
- Smugglers Haven (hrs_35054985) | 7yo M | 168lb | OR 125 | draw 0 | jockey Miss Lily Bradstock(7) | trainer Sara Bradstock (14d 0/3) | headgear - | last run 94 days | form 1F-123 | MARKET 9.9% | 09:00 median 9.00 | Matchbook 9.80
    comment: Smugglers Haven arrives in cracking nick, third last time out and a second two starts back, with a winner three starts back, and she has run over today's trip and going before. The main risk is a 94-day break, plus 168 lb on her back.
    DATA: model 21.5% | style Leader (led 79% of runs) | runs in data 3 | last 3: 24 May Fontwell Hurdle 21.7f Good 1/4; 7 Jul Uttoxeter Hurdle 23.3f Good 2/11; 19 Aug Worcester Chase 23f Good 3/6
    DATA for: Official rating 125, 6 lb above field average; Good recent finishing positions
    DATA against: Carries 6 lb more than average; Returns from a 94-day break
- Letterston Lady (hrs_29313053) | 8yo M | 164lb | OR 121 | draw 0 | jockey Shane Fenelon(5) | trainer Mickey Bowen (14d 4/19) | headgear - | last run 16 days | form /11-27 | MARKET 8.3% | 09:00 median 11.00 | Matchbook 11.00
    comment: Letterston Lady won twice in her last four starts, taking a first four starts back and another three starts back, then a second two starts back, and she's fresh enough after 16 days; she has run over today's trip and going. The main risk is a seventh last time out, while a weight of 164 lb adds to the task.
    DATA: model 10.9% | style Held up (led 5% of runs) | runs in data 2 | last 3: 24 Sep Perth Hurdle 23.9f Good 2/11; 5 Nov Newcastle Hurdle 24f Good 7/8 fig 115
    DATA for: Trainer 21% wins (4/19), last 14 days
    DATA against: Recent figures 6 lb below its current mark (looks high in the weights); Lightly raced: 2 runs in our data, so the model has little to go on
- Miss Goldfire (hrs_34003536) | 7yo M | 159lb | OR 116 | draw 0 | jockey Ciaran O'Shea(7) | trainer Harry Fry (14d 1/5) | headgear t | last run 13 days | form 1U1247 | MARKET 7.9% | 09:00 median 11.00 | Matchbook 12.50
    comment: Miss Goldfire has slid to a seventh last time out, and a fourth two starts back, after winning four starts back, so the trend is the wrong way. She carries 159 lb, though she has run over today's trip and going, and is fresh enough after 13 days.
    DATA: model 8.2% | style Prominent (led 23% of runs) | runs in data 7 | last 3: 28 Jun Uttoxeter Hurdle 23.3f Good 2/10; 4 Oct Uttoxeter Hurdle 23.3f Good 4/5; 8 Nov Sandown Hurdle 20f Good To Soft 7/8 fig 111
    DATA for: Trainer 20% wins (1/5), last 14 days; Has won at this trip or further
    DATA against: Fell or unseated in 1 of its last 5 jumps runs
- Popova (hrs_29522892) | 9yo M | 165lb | OR 122 | draw 0 | jockey Bradley Harris(3) | trainer Neil Mulholland (14d 3/19) | headgear - | last run 347 days | form /2356- | MARKET 4.4% | 09:00 median 18.00 | Matchbook 25.00
    comment: Popova has been placed in two of her last four, a second four starts back and a third three starts back, and she has run over today's trip and going before.
    DATA: model 10.7% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 347-day break; Lightly raced: 0 runs in our data, so the model has little to go on

## 2:40 Ascot | race_id rac_32305068484 | Restorations UK Berkshire National Handicap Steeple Chase (GBB Race)
Chase | Class 2 | 3m5f75y | going Good To Firm | Turf | 9 runners | rating band 0-150 | age 5yo+
DATA pace: Strong pace - 4 habitual front-runners (Mt Fugi Park, Hold Your Fort, Sound And Fury, My Gift To You). A contested lead should set things up for horses coming from behind.
- Rock My Way (hrs_29117291) | 8yo G | 165lb | OR 137 | draw 0 | jockey Freddie Gingell | trainer Joe Tizzard (14d 7/26) | headgear tb | last run 210 days | form 18226- | MARKET 25.4% | 09:00 median 3.25 | Matchbook 3.95 | CHECK (skip line 3.09)
    comment: Rock My Way showed solid consistency with seconds two and three starts back, and he has run over today's trip and going before, while a yard in form (7 from 26 in the last 14 days) adds to the case. The main risk is a 210-day absence, with a sixth last time out and 165 lb to carry.
    DATA: model 13.2% | style Prominent (led 5% of runs) | runs in data 3 | last 3: 1 Feb Musselburgh Chase 31.3f Good To Soft 2/7; 14 Mar Uttoxeter Chase 34f Soft 2/16; 25 Apr Sandown Chase 28.7f Good 6/11
    DATA for: Official rating 137, 6 lb above field average; Trainer 27% wins (7/26), last 14 days; Good recent finishing positions
    DATA against: Carries 6 lb more than average; Returns from a 210-day break
- Brandt (hrs_32401985) | 8yo G | 157lb | OR 129 | draw 0 | jockey Mr J L Scallan(7) | trainer Cian Collins (14d 0/5) | headgear t | last run 29 days | form 67-611 | MARKET 14.0% | 09:00 median 6.00 | Matchbook 7.00
    DATA: model 14.2% | style Midfield (led 29% of runs) | runs in data 6 | last 3: 9 Jun Sligo Hurdle 25.8f Yielding 6/16; 7 Sep Galway Chase 22.5f Yielding 1/11; 23 Oct Cheltenham Chase 25f Good To Soft 1/11 fig 123
    DATA for: Good recent finishing positions
    DATA against: Recent figures 6 lb below its current mark (looks high in the weights); Race comments mention jumping mistakes in 2 of its last 5 runs
- Henry's Friend (hrs_30175740) | 9yo G | 167lb | OR 139 | draw 0 | jockey Elliott England(7) | trainer Ben Pauling (14d 4/25) | headgear p | wind surgery | last run 21 days | form 869P-7 | MARKET 11.1% | 09:00 median 8.00 | Matchbook 8.60
    comment: The main risk is that he's yet to find a win in his last five starts.
    DATA: model 9.7% | style Prominent (led 29% of runs) | runs in data 3 | last 3: 21 Feb Kempton Chase 24f Good To Soft 9/13; 25 Apr Sandown Chase 28.7f Good PU/11; 31 Oct Ascot Chase 24f Good 7/10 fig 129
    DATA for: Best recent form figure 129, 5 lb above field average; Official rating 139, 8 lb above field average
    DATA against: Recent figures 10 lb below its current mark (looks high in the weights); Poor recent finishing positions; Carries 8 lb more than average; Pulled up in 1 of its last 3 jumps runs
- Hold Your Fort (hrs_21221641) | 10yo G | 157lb | OR 129 | draw 0 | jockey Robert Dunne | trainer Debra Hamer (14d 0/0) | headgear - | last run 15 days | form 395126 | MARKET 10.6% | 09:00 median 8.50 | Matchbook 9.00
    comment: Hold Your Fort is fresh enough after 15 days and has run on today's going, with a second two starts back and a winner three starts back, but he was only sixth last time out and carries a hefty 157 lb off 129.
    DATA: model 10.1% | style Prominent (led 54% of runs) | runs in data 9 | last 3: 26 Jul Uttoxeter Chase 24f Good 1/7; 14 Oct Ffos Las Chase 24f Soft 2/8 fig 128; 6 Nov Aintree Chase 25f Good To Soft 6/12 fig 126
    DATA for: Best recent form figure 128, 4 lb above field average; Good recent finishing positions
- Our Power (hrs_11067266) | 11yo G | 168lb | OR 140 | draw 0 | jockey Dylan Johnston | trainer Sam Thomas (14d 1/3) | headgear b | last run 210 days | form /F642- | MARKET 9.5% | 09:00 median 9.25 | Matchbook 10.00
    DATA: model 10.7% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 15 Jan Wincanton Chase 26.7f Heavy 4/7; 25 Apr Sandown Chase 28.7f Good 2/11
    DATA for: Official rating 140, 9 lb above field average
    DATA against: Carries 9 lb more than average; Returns from a 210-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- Ballycamus (hrs_24494169) | 9yo G | 155lb | OR 127 | draw 0 | jockey Sam Twiston-Davies | trainer Nigel & Willy Twiston-Davies (14d 4/25) | headgear p | last run 38 days | form 9145-1 | MARKET 9.3% | 09:00 median 9.50 | Matchbook 10.50
    comment: Ballycamus won last time out and again four starts back, with a fifth and a fourth in between, and he has run on today's going before.
    DATA: model 12.0% | style Held up (led 8% of runs) | runs in data 3 | last 3: 26 Feb Ludlow Chase 23.8f Good To Soft 4/7; 21 Mar Newbury Chase 23.4f Good To Soft 5/7; 14 Oct Ffos Las Chase 24f Soft 1/6 fig 125
    DATA for: Pace: a contested lead should suit its hold-up style
- My Gift To You (hrs_28891597) | 8yo G | 148lb | OR 120 | draw 0 | jockey Jonathan Burke | trainer James Owen (14d 3/30) | headgear tv | last run 29 days | form 2-1536 | MARKET 8.6% | 09:00 median 10.00 | Matchbook 11.50
    comment: My Gift To You was only sixth last time out and has one win in his last five, that coming four starts back, so he is hard to fancy. He has run over today's trip and going before, and a third two starts back shows he can still pick up a place, but 148 lb is a big ask.
    DATA: model 7.6% | style Leader (led 23% of runs) | runs in data 4 | last 3: 23 May Cartmel Chase 25.5f Good 5/8; 28 Jun Uttoxeter Hurdle 23.3f Good 3/10; 23 Oct Cheltenham Chase 25f Good To Soft 6/11 fig 113
    DATA for: Has won at this trip or further; Carries 11 lb less than average
    DATA against: Best recent form figure 113, 11 lb below field average; Recent figures 7 lb below its current mark (looks high in the weights); Official rating 120, 11 lb below field average; Pace: likely to be taken on for the lead
- Sound And Fury (hrs_29621921) | 9yo G | 154lb | OR 126 | draw 0 | jockey Ben Jones | trainer Ben Pauling (14d 4/25) | headgear p | last run 7 days | form 6815-U | MARKET 6.6% | 09:00 median 13.00 | Matchbook 15.00
    comment: Hard to fancy after unseating last time out, just seven days ago, with a fifth two starts back following a win three starts back and little else of note.
    DATA: model 10.0% | style Leader (led 29% of runs) | runs in data 3 | last 3: 16 Feb Carlisle Chase 24.5f Good To Soft 1/7; 7 Mar Sandown Chase 24.2f Soft 5/8; 14 Nov Cheltenham Chase 25f Good UR/9
    DATA for: Carries 5 lb less than average
    DATA against: Official rating 126, 5 lb below field average; Fell or unseated in 1 of its last 3 jumps runs; Pace: likely to be taken on for the lead
- Mt Fugi Park (hrs_34073452) | 8yo G | 163lb | OR 135 | draw 0 | jockey Richie McLernon | trainer Jonjo & A.J. O'Neill (14d 6/39) | headgear b | last run 28 days | form 1-P11F | MARKET 5.0% | 09:00 median 17.00 | Matchbook 20.00
    comment: Three wins in his last five starts, including back-to-back victories two and three starts back, make Mt Fugi Park a serious threat, and he has run on today's going before. The one concern is a fall last time out, so jumping fluency matters off 163 lb after 28 days off.
    DATA: model 12.6% | style Leader (led 43% of runs) | runs in data 6 | last 3: 22 Jul Worcester Chase 23f Good 1/9; 15 Sep Uttoxeter Chase 24f Good 1/7; 24 Oct Cheltenham Chase 25f Good To Soft F/9
    DATA against: Race comments mention jumping mistakes in 3 of its last 5 runs; Fell or unseated in 1 of its last 5 jumps runs; Pulled up in 1 of its last 5 jumps runs; Pace: likely to be taken on for the lead

## 3:18 Ascot | race_id rac_32304187149 | Vietti Barolo Hurst Park Handicap Steeple Chase (Premier Handicap) (GBB Race)
Chase | Class 1 | 2m0f172y | going Good To Firm | Turf | 7 runners | rating band - | age 4yo+
DATA pace: Lone leader - Sans Bruit is the only habitual front-runner and may be allowed an easy lead.
- Vanderpoel (hrs_40786599) | 7yo G | 168lb | OR 148 | draw 0 | jockey Ben Jones | trainer Ben Pauling (14d 4/25) | headgear - | wind surgery | last run 21 days | form 2117-1 | MARKET 34.8% | 09:00 median 2.62 | Matchbook 2.78
    comment: Vanderpoel arrives in cracking form, a winner last time out and three wins in his last five starts, fresh from a 21-day break and with experience of today's trip and going. The main risk is the 168 lb he carries, which looks a stiff task off an official mark of 148.
    DATA: model 29.4% | style Prominent (led 5% of runs) | runs in data 3 | last 3: 3 Jan Sandown Chase 15.4f Good 1/5; 11 Mar Cheltenham Chase 15.9f Good 7/20; 31 Oct Ascot Chase 17f Good 1/11 fig 144
    DATA for: Best recent form figure 144, 9 lb above field average; Official rating 148, 11 lb above field average; Has won at this trip or further; Good recent finishing positions
    DATA against: Carries 11 lb more than average
- Ryan's Rocket (hrs_29283590) | 8yo G | 159lb | OR 139 | draw 0 | jockey Jonathan Burke | trainer Fergal O'Brien (14d 3/31) | headgear - | last run 226 days | form /1U61- | MARKET 14.9% | 09:00 median 6.00 | Matchbook 6.60
    comment: The risk is a 226-day absence, with 159 lb on his back.
    DATA: model 15.2% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 14 Mar Kempton Chase 20.5f Good 6/7; 9 Apr Aintree Chase 15.8f Good To Soft 1/15
    DATA for: Last-run finishing speed +4.5% vs that field (finished strongly)
    DATA against: Returns from a 226-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- Sans Bruit (hrs_24263722) | 8yo G | 153lb | OR 133 | draw 0 | jockey Jay Tidball(5) | trainer Paul Nicholls (14d 2/18) | headgear t | wind surgery | last run 14 days | form 4435-2 | MARKET 13.4% | 09:00 median 7.00 | Matchbook 7.20
    comment: Sans Bruit has been consistent, finishing second last time out after a fifth, a third and two fourths, and he's fresh from a 14-day break with experience of today's trip and going.
    DATA: model 15.6% | style Leader (led 63% of runs) | runs in data 4 | last 3: 9 Apr Aintree Chase 15.8f Good To Soft 3/15; 18 Apr Ayr Chase 16.5f Heavy 5/7; 7 Nov Aintree Chase 16f Good To Soft 2/10 fig 136
    DATA for: Good recent finishing positions; Pace: may get an uncontested lead
- Shakeyatailfeather (hrs_34845902) | 7yo M | 143lb | OR 123 | draw 0 | jockey Harry Atkins(5) | trainer Dan Skelton (14d 17/80) | headgear - | last run 6 days | form 677-3U | MARKET 11.4% | 09:00 median 8.00 | Matchbook 8.60
    comment: Shakeyatailfeather is hard to fancy, unseated last time out and winless in her last five, with a third two starts back her only finish in the first three. She is back quickly after six days, but has run over today's trip and going, and carries 143 lb.
    DATA: model 6.5% | style Held up (led 4% of runs) | runs in data 5 | last 3: 14 Mar Kempton Chase 20.5f Good 7/7; 31 Oct Ascot Chase 17f Good 3/11 fig 122; 15 Nov Cheltenham Chase 16f Good UR/9
    DATA for: Trainer 21% wins (17/80), last 14 days; Carries 14 lb less than average
    DATA against: Best recent form figure 122, 13 lb below field average; Official rating 123, 14 lb below field average; Race comments mention jumping mistakes in 2 of its last 5 runs; Fell or unseated in 1 of its last 5 jumps runs
- Calico (hrs_18952458) | 10yo G | 168lb | OR 148 | draw 0 | jockey Dominic Lewis(10) | trainer Dan Skelton (14d 17/80) | headgear tp | last run 29 days | form 404-54 | MARKET 10.4% | 09:00 median 8.50 | Matchbook 9.80
    comment: Calico is consistent, finishing fourth last time out and fifth two starts back, and he has run over today's trip and going before, returning after 29 days off.
    DATA: model 16.2% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 18 Apr Ayr Chase 16.5f Heavy 4/7; 16 May Bangor-on-Dee Chase 17.4f Good 5/7; 23 Oct Cheltenham Chase 16f Good To Soft 4/8 fig 148
    DATA for: Best recent form figure 148, 13 lb above field average; Official rating 148, 11 lb above field average; Trainer 21% wins (17/80), last 14 days
    DATA against: Carries 11 lb more than average
- Martator (hrs_21493766) | 9yo G | 167lb | OR 147 | draw 0 | jockey Charlie Deutsch | trainer Venetia Williams (14d 0/7) | headgear p | last run 21 days | form 29U1-2 | MARKET 8.0% | 09:00 median 11.00 | Matchbook 12.50
    comment: Martator brings a second last time out and a win two starts back, and he has run over today's trip and on this going, with 21 days since his last outing. The main risk is the 167 lb he must carry, which leaves little margin for error.
    DATA: model 9.7% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 31 Jan Sandown Chase 15.4f Soft UR/11; 11 Mar Cheltenham Chase 15.9f Good 1/20; 31 Oct Ascot Chase 17f Good 2/11 fig 145
    DATA for: Best recent form figure 145, 10 lb above field average; Official rating 147, 10 lb above field average
    DATA against: Carries 10 lb more than average; Fell or unseated in 1 of its last 3 jumps runs
- Gabriel's Getaway (hrs_24277456) | 9yo G | 142lb | OR 118 | draw 0 | jockey Sam Twiston-Davies | trainer Anthony Honeyball (14d 3/10) | headgear tp | last run 21 days | form 433-65 | MARKET 7.2% | 09:00 median 12.00 | Matchbook 14.50
    comment: Gabriel's Getaway is winless in his last five, fading to a fifth last time out and a sixth the run before, so he is hard to fancy at 142 lb. On the plus side, he has run over today's trip and going, was third three starts back, and comes here fresh after 21 days.
    DATA: model 7.4% | style Held up (led 4% of runs) | runs in data 5 | last 3: 28 Feb Doncaster Chase 16.4f Soft 3/5; 16 May Bangor-on-Dee Chase 17.4f Good 6/7; 31 Oct Ascot Chase 17f Good 5/11 fig 117
    DATA for: Trainer 30% wins (3/10), last 14 days; Carries 15 lb less than average
    DATA against: Best recent form figure 117, 18 lb below field average; Official rating 118, 19 lb below field average; Race comments mention jumping mistakes in 3 of its last 5 runs

## 3:48 Ascot | race_id rac_32305070421 | Ascot Advent Calendar Novices' Handicap Hurdle Race (GBB Race)
Hurdle | Class 4 | 3m0f102y | going Good To Firm | Turf | 7 runners | rating band 0-115 | age 4yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Herbygoesbananas (hrs_47033056) | 5yo G | 161lb | OR 105 | draw 0 | jockey Ben Jones | trainer Henrietta C Knight (14d 0/7) | headgear - | last run 20 days | form 3-3491 | MARKET 29.3% | 09:00 median 3.00 | Matchbook 3.30 | CHECK (skip line 2.85)
    comment: Fresh from a win last time out, Herbygoesbananas has run over today's going and returns after 20 days, but a ninth two starts back is a worry, and carrying 161 lb off an official mark of 105 looks a tall order.
    DATA: model 13.8% | style Held up (led 4% of runs) | runs in data 7 | last 3: 22 May Worcester Hurdle 23f Good 4/11; 10 Oct Chepstow Hurdle 19.5f Good To Soft 9/13; 1 Nov Worcester Hurdle 23f Good To Soft 1/9 fig 100
    DATA for: Last-run finishing speed +7.2% vs that field (finished strongly)
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Kilnew Supreme (hrs_51558087) | 5yo G | 162lb | OR 106 | draw 0 | jockey Sam Twiston-Davies | trainer Paul Nicholls (14d 2/18) | headgear t | last run 54 days | form /222-2 | MARKET 24.9% | 09:00 median 3.50 | Matchbook 3.90
    comment: The risk is the 54-day break, plus 162 lb on his back.
    DATA: model 25.9% | style Prominent (led 8% of runs) | runs in data 3 | last 3: 23 Mar Wincanton Hurdle 15.2f Good 2/12; 22 Apr Taunton Hurdle 19f Good 2/7; 28 Sep Newton Abbot Hurdle 21.6f Good 2/4
    DATA for: Good recent finishing positions
- Baile An Or (hrs_51185820) | 5yo G | 158lb | OR 102 | draw 0 | jockey Freddie Gingell | trainer Joe Tizzard (14d 7/26) | headgear - | last run 23 days | form 504-76 | MARKET 12.3% | 09:00 median 7.00 | Matchbook 7.80
    comment: Winless in his last five, Baile An Or was sixth last time out, 23 days ago, but he has run on today's going and his trainer is in cracking form (7 from 26 lately).
    DATA: model 10.6% | style Prominent (led 3% of runs) | runs in data 4 | last 3: 23 Mar Wincanton Hurdle 15.2f Good 4/12; 10 Oct Chepstow Hurdle 19.5f Good To Soft 7/13; 29 Oct Ffos Las Hurdle 20f Heavy 6/11 fig 93
    DATA for: Trainer 27% wins (7/26), last 14 days
    DATA against: Best recent form figure 93, 7 lb below field average; Recent figures 9 lb below its current mark (looks high in the weights); Last-run finishing speed -2.9% vs that field (faded)
- Mr Rafiki (hrs_51434334) | 5yo G | 166lb | OR 110 | draw 0 | jockey Richie McLernon | trainer Jonjo & A.J. O'Neill (14d 6/39) | headgear tp | last run 10 days | form 2FF221 | MARKET 10.1% | 09:00 median 8.50 | Matchbook 10.00
    comment: Fresh from a win last time out and just ten days since, Mr Rafiki has been in the frame often, with a second two starts back and another three starts back, and he has run on today's going. Carrying 166 lb off an official mark of 110 and with two falls in his last six, he has plenty to prove.
    DATA: model 16.9% | style Midfield (led 3% of runs) | runs in data 9 | last 3: 17 Oct Stratford Hurdle 22f Good 2/7 fig 106; 31 Oct Ascot Hurdle 19.5f Good To Firm 2/9 fig 106; 11 Nov Bangor-on-Dee Hurdle 23f Good 1/4 fig 106
    DATA for: Best recent form figure 106, 6 lb above field average; Official rating 110, 6 lb above field average; Last-run finishing speed +4.1% vs that field (finished strongly); Good recent finishing positions
    DATA against: Carries 6 lb more than average; Fell or unseated in 2 of its last 5 jumps runs
- Person of Interest (hrs_40095713) | 6yo G | 156lb | OR 100 | draw 0 | jockey J. P. O'Neill(10) | trainer Faye Bramley (14d 1/17) | headgear - | last run 9 days | form 612P52 | MARKET 10.0% | 09:00 median 9.00 | Matchbook 9.60
    comment: Runner-up last time out just nine days ago, he has run over today's trip and on this going, but a pulled up three starts back and a fifth two starts back show his inconsistency.
    DATA: model 12.0% | style Prominent (led 3% of runs) | runs in data 9 | last 3: 28 Aug Fontwell Chase 17.8f Good PU/6; 8 Sep Bangor-on-Dee Hurdle 19.6f Good 5/7; 12 Nov Hereford Hurdle 21.5f Good To Firm 2/7 fig 100
    DATA against: Race comments mention jumping mistakes in 2 of its last 5 runs; Pulled up in 1 of its last 5 jumps runs
- Dante's Rocco (hrs_52055745) | 5yo G | 158lb | OR 102 | draw 0 | jockey Dylan Johnston | trainer Syd Hosie (14d 2/10) | headgear - | last run 231 days | form 3434- | MARKET 8.7% | 09:00 median 9.50 | Matchbook 12.00
    comment: Dante's Rocco is winless in his last four, finishing fourth last time out, third two starts back, fourth three starts back and third four starts back, but a 231-day absence is a worry and he carries 158 lb.
    DATA: model 10.8% | style Prominent (led 4% of runs) | runs in data 3 | last 3: 17 Feb Newbury Hurdle 20.5f Soft 4/6; 23 Mar Wincanton Hurdle 15.2f Good 3/12; 4 Apr Newton Abbot Hurdle 18.5f Good 4/11
    DATA for: Trainer 20% wins (2/10), last 14 days; Last-run finishing speed +2.1% vs that field (finished strongly)
    DATA against: Returns from a 231-day break
- Muskerry Rock (hrs_34253800) | 7yo G | 161lb | OR 105 | draw 0 | jockey James Murray(10) | trainer Mickey Bowen (14d 4/19) | headgear p | last run 8 days | form 1P3443 | MARKET 4.8% | 09:00 median 19.00 | Matchbook 22.00
    comment: He has run over today's trip and going, though 161 lb is a notable burden.
    DATA: model 10.0% | style Midfield (led 4% of runs) | runs in data 10 | last 3: 10 Oct Chepstow Hurdle 23.6f Good To Soft 5/17; 24 Oct Kelso Chase 26f Good 4/4; 13 Nov Southwell Hurdle 24.5f Good 3/6 fig 103
    DATA for: Trainer 21% wins (4/19), last 14 days; Has won at this trip or further
    DATA against: Pulled up in 1 of its last 5 jumps runs
