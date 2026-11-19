# Card review packet: Thurles, 2026-11-19

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
{"meeting": "thurles", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 12:08 Thurles | race_id rac_32304752753 | Irish Stallion Farms EBF Beginners Steeplechase
Chase |  | 2m5f132y | going Good | Turf | 8 runners | rating band - | age 4yo+
DATA pace: Even - Two likely leaders (Court Compliance, Fire Coral). A fair, even gallop is most likely.
- Doctor Steinberg (hrs_39996453) | 6yo G | 166lb | OR - | draw 0 | jockey Paul Townend | trainer W. P. Mullins (14d 4/21) | headgear - | last run 204 days | form 111P9- | MARKET 61.5% | 09:00 median 1.40 | Matchbook 1.49
    comment: Three wins in his last five starts is a strong profile, with a hat-trick of victories three, four and five starts back, and he has run over today's trip and going before. The risk is a 204-day absence, with a ninth last time out and a pulled up before that, while carrying 166 lb.
    DATA: model 13.8% | style Prominent (led 38% of runs) | runs in data 3 | last 3: 2 Feb Leopardstown Hurdle 22.2f Heavy 1/8; 13 Mar Cheltenham Hurdle 24f Good To Soft PU/22; 29 Apr Punchestown Hurdle 23.9f Yielding 9/14
    DATA for: Has won at this trip or further
    DATA against: Last-run finishing speed -7.6% vs that field (faded); Returns from a 204-day break; Pulled up in 1 of its last 3 jumps runs; First run over fences in our data
- Court Compliance (hrs_39996446) | 6yo G | 166lb | OR - | draw 0 | jockey Philip Byrnes | trainer William Durkan (14d 0/3) | headgear - | last run 229 days | form 22216- | MARKET 10.8% | 09:00 median 7.00 | Matchbook 9.40
    comment: Court Compliance won two starts back and was second in three of his last five, so he's a consistent sort who has run over today's trip and carries 166 lb. The main risk is a 229-day absence, after a sixth last time out.
    DATA: model 14.8% | style Leader (led 54% of runs) | runs in data 3 | last 3: 17 Jan Navan Hurdle 22f Soft To Heavy 2/12; 18 Feb Punchestown Hurdle 20.1f Soft 1/7; 4 Apr Fairyhouse Hurdle 23.8f Yielding To Soft 6/20
    DATA for: Good recent finishing positions
    DATA against: Returns from a 229-day break; First run over fences in our data
- Stede Bonnet (hrs_52742039) | 5yo G | 166lb | OR 126 | draw 0 | jockey Jack Kennedy | trainer Gordon Elliott (14d 12/72) | headgear - | last run 46 days | form 0-2302 | MARKET 9.1% | 09:00 median 9.00 | Matchbook 11.00
    comment: Stede Bonnet arrives in cracking nick after a second last time out, with a third and another second in his last five too, and he has run over today's trip and on the going. Yet to win in that spell, though, and 166 lb after 46 days off is the main risk.
    DATA: model 19.1% | style Prominent (led 3% of runs) | runs in data 8 | last 3: 10 Jul Kilbeggan Hurdle 20f Good 3/14; 1 Aug Galway Hurdle 22.5f Good To Yielding 14/20; 4 Oct Killarney Chase 20.8f Good To Yielding 2/4
    DATA for: Good recent finishing positions
- Franciscan Rock (hrs_28607999) | 9yo G | 166lb | OR 132 | draw 0 | jockey Josh Williamson(3) | trainer M F Morris (14d 0/2) | headgear p | last run 9 days | form 9527-7 | MARKET 6.7% | 09:00 median 12.00 | Matchbook 14.50
    comment: He is back quickly after nine days and carries 166 lb, though two sevenths of late temper enthusiasm.
    DATA: model 8.5% | style Prominent (led 4% of runs) | runs in data 4 | last 3: 11 Mar Cheltenham Hurdle 21f Good 2/24; 30 Apr Punchestown Hurdle 23.5f Yielding 7/8; 10 Nov Fairyhouse (IRE) Chase 20f Good To Yielding 7/9 fig 109
    DATA for: Official rating 132, 11 lb above field average
    DATA against: Aged 9, older than most of this field
- Fort Dino (hrs_53476010) | 5yo G | 166lb | OR - | draw 0 | jockey Mike O'Connor | trainer Henry de Bromhead (14d 7/38) | headgear t | last run 56 days | form 418-29 | MARKET 5.8% | 09:00 median 10.00 | Matchbook 24.00
    comment: Fort Dino was beaten into ninth last time out and has been off for 56 days, which makes him hard to fancy, though he has run on today's going before, and a second two starts back and a win four starts back show he can bounce back.
    DATA: model 8.4% | style Midfield (led 5% of runs) | runs in data 3 | last 3: 30 Apr Punchestown Hurdle 16.4f Yielding 8/11; 20 Aug Killarney Chase 23.5f Good 2/6; 24 Sep Listowel Chase 22f Good 9/11
    DATA against: Last-run finishing speed -6.2% vs that field (faded); Race comments mention jumping mistakes in 2 of its last 3 runs
- Walks In June (hrs_40920054) | 6yo G | 166lb | OR - | draw 0 | jockey Jordan Gainford | trainer Henry de Bromhead (14d 7/38) | headgear t (1st time) | last run 20 days | form 1610-6 | MARKET 3.1% | 09:00 median 26.00 | Matchbook 32.00
    comment: Walks In June has won twice in his last five starts, a first and another three starts back, but he was only sixth last time out and unplaced the run before.
    DATA: model 3.2% | style Held up (led 8% of runs) | runs in data 2 | last 3: 11 Mar Cheltenham Hurdle 21f Good 18/21; 30 Oct Down Royal (IRE) Chase 20f Good 6/7
    DATA for: First-time headgear
    DATA against: Last-run finishing speed -3.6% vs that field (faded); Lightly raced: 2 runs in our data, so the model has little to go on
- Fire Coral (hrs_32090744) | 7yo M | 159lb | OR 106 | draw 0 | jockey Phillip Enright | trainer S Curling (14d 0/1) | headgear tp | last run 44 days | form P38311 | MARKET 1.6% | 09:00 median 34.00 | Matchbook 95.00
    comment: Fire Coral arrives in cracking form, a winner last time out and again two starts back, and she has run over today's trip and going, but 44 days off and 159 lb are hard asks.
    DATA: model 25.0% | style Leader (led 54% of runs) | runs in data 7 | last 3: 28 Aug Down Royal Hurdle 24f Good 3/15; 25 Sep Listowel Hurdle 22f Good To Yielding 1/14; 6 Oct Galway Hurdle 22.3f Yielding To Soft 1/7
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Official rating 106, 15 lb below field average; Race comments mention jumping mistakes in 2 of its last 5 runs; First run over fences in our data
- Farnahoe Rebel (hrs_17395566720) | 7yo G | 166lb | OR - | draw 0 | jockey Michael Kenneally(3) | trainer Raymond Hurley (14d 0/1) | headgear - | last run 186 days | form 4P1-72 | MARKET 1.4% | 09:00 median 81.00 | Matchbook 65.00
    comment: Unexposed gelding who finished second last time out, and a winner three starts back, though he returns after 186 days off and carries 166 lb. Lightly raced, he looks open to further improvement.
    DATA: model 7.2% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 186-day break; Lightly raced: 0 runs in our data, so the model has little to go on

## 12:40 Thurles | race_id rac_32304754690 | William Hill Challenge Series Handicap Steeplechase
Chase |  | 2m6f0y | going Good | Turf | 14 runners | rating band - | age 4yo+
DATA pace: Even - Two likely leaders (Labondance, Clonbury Bridge). A fair, even gallop is most likely.
- Iamagetaway (hrs_34073193) | 7yo G | 166lb | OR 110 | draw 0 | jockey Sam Ewing | trainer W R Crawford (14d 1/3) | headgear h | last run 41 days | form 073-01 | MARKET 19.2% | 09:00 median 3.75 | Matchbook 4.80 | CHECK (skip line 3.56)
    comment: The main risk is the 166 lb he must carry, with his form before that win patchy.
    DATA: model 14.5% | style Prominent (led 29% of runs) | runs in data 3 | last 3: 24 Apr Kilbeggan Chase 20f Good To Yielding 3/14; 11 May Killarney Chase 20.5f Good To Yielding 10/14; 9 Oct Downpatrick Chase 19.5f Good 1/8
    DATA for: Official rating 110, 8 lb above field average; Good recent finishing positions
    DATA against: Carries 9 lb more than average
- That's About Right (hrs_33774461) | 8yo G | 150lb | OR 94 | draw 0 | jockey Shane O'Callaghan(3) | trainer P. J. Rothwell (14d 0/24) | headgear tp | last run 7 days | form 484853 | MARKET 12.0% | 09:00 median 6.00 | Matchbook 7.60
    comment: Third last time out and back quickly after seven days, he has run over today's trip and going before, but he is yet to win in his last six starts and the yard is 0/24 over the last fortnight.
    DATA: model 4.8% | style Held up (led 3% of runs) | runs in data 11 | last 3: 7 Sep Galway Chase 22.5f Yielding 8/11; 8 Oct Tramore Hurdle 20.3f Yielding 5/7; 12 Nov Thurles (IRE) Chase 18f Good 3/12 fig 94
    DATA for: Last-run finishing speed +4.1% vs that field (finished strongly); Carries 7 lb less than average
    DATA against: Official rating 94, 8 lb below field average; Trainer 0 wins from 24 runs, last 14 days
- Doctor Confusion (hrs_46045356) | 5yo G | 159lb | OR 103 | draw 0 | jockey Jordan Gainford | trainer Henry de Bromhead (14d 7/38) | headgear t | last run 42 days | form P-8433 | MARKET 11.4% | 09:00 median 6.00 | Matchbook 8.40
    comment: Doctor Confusion arrives on a fair upward curve, third last time out and third again two starts back, and he has run on today's going before. Yet he is winless in recent starts, carries 159 lb off 103 and returns after 42 days off.
    DATA: model 7.0% | style Prominent (led 23% of runs) | runs in data 4 | last 3: 16 Aug Tramore Hurdle 16.6f Good To Yielding 4/14; 18 Sep Downpatrick Chase 17.8f Good 3/12; 8 Oct Tramore Chase 20.4f Yielding 3/12
    DATA for: Last-run finishing speed +3.9% vs that field (finished strongly); Good recent finishing positions
- Hees Dynamite (hrs_34874476) | 8yo G | 157lb | OR 101 | draw 0 | jockey Patrick M O'Brien(5) | trainer E McNamara (14d 0/10) | headgear - | last run 44 days | form -20544 | MARKET 10.6% | 09:00 median 6.50 | Matchbook 9.00
    DATA: model 11.4% | style Prominent (led 3% of runs) | runs in data 5 | last 3: 22 Aug Killarney Hurdle 22.4f Good 5/14; 26 Sep Listowel Chase 23.8f Good 4/14; 6 Oct Galway Chase 22.5f Yielding To Soft 4/8
    DATA against: Trainer 0 wins from 10 runs, last 14 days; Race comments mention jumping mistakes in 2 of its last 5 runs
- Smallcraftwarning (hrs_31083213) | 9yo G | 156lb | OR 100 | draw 0 | jockey Daniel King | trainer John Patrick Ryan (14d 0/11) | headgear t | last run 14 days | form 4112F6 | MARKET 7.7% | 09:00 median 10.00 | Matchbook 12.00
    comment: Back-to-back wins four and five starts back give Smallcraftwarning a solid base, and he has run over today's trip and going, but he was only sixth last time out and fell two starts back before that.
    DATA: model 3.2% | style Midfield (led 3% of runs) | runs in data 16 | last 3: 10 Oct Fairyhouse Chase 24.5f Good 2/9; 14 Oct Punchestown (IRE) Chase 23f Good F/4; 5 Nov Clonmel (IRE) Hurdle 24f Good 6/7 fig 106
    DATA for: Best recent form figure 106, 14 lb above field average; Recent figures 6 lb above its current mark (looks well handicapped); Has won at this trip or further
    DATA against: Trainer 0 wins from 11 runs, last 14 days; Race comments mention jumping mistakes in 2 of its last 5 runs; Fell or unseated in 1 of its last 5 jumps runs
- Roc My Haarth (hrs_46515259) | 7yo G | 157lb | OR 101 | draw 0 | jockey Brian Barry(7) | trainer Ray Hackett (14d 0/5) | headgear - | last run 24 days | form 61-664 | MARKET 7.2% | 09:00 median 11.00 | Matchbook 12.00
    comment: Roc My Haarth is hard to fancy, having finished a sixth, a sixth, then a fourth since his win four starts back, and he carries 157 lb off an official mark of 101.
    DATA: model 11.5% | style Prominent (led 3% of runs) | runs in data 7 | last 3: 7 Sep Galway Hurdle 16.7f Yielding 6/20; 28 Sep Roscommon Hurdle 24.1f Good To Yielding 6/11; 26 Oct Galway (IRE) Hurdle 24f Heavy 4/19 fig 85
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 85, 7 lb below field average; Recent figures 16 lb below its current mark (looks high in the weights); Race comments mention jumping mistakes in 2 of its last 5 runs
- Toor Khov (hrs_34268514) | 8yo G | 167lb | OR 111 | draw 0 | jockey Liam Quinlan | trainer Ms M Flynn (14d 0/1) | headgear - | last run 54 days | form 1F24-0 | MARKET 5.5% | 09:00 median 13.00 | Matchbook 17.00
    comment: Toor Khov has a win five starts back and a second three starts back, but he was unplaced last time out and returns after 54 days off, which raises fitness questions.
    DATA: model 11.2% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 19 Mar Cork Hurdle 24.2f Yielding 2/10; 5 Apr Cork Hurdle 24.1f Yielding 4/16; 26 Sep Listowel Chase 23.8f Good 12/14
    DATA for: Official rating 111, 9 lb above field average
    DATA against: Last-run finishing speed -6.6% vs that field (faded); Carries 10 lb more than average; Race comments mention jumping mistakes in 2 of its last 5 runs; Fell or unseated in 1 of its last 5 jumps runs
- Schiehallion (hrs_37395211) | 9yo G | 152lb | OR 96 | draw 0 | jockey Alix Balfe(7) | trainer Dermot A McLoughlin (14d 0/7) | headgear v | last run 16 days | form 5P0416 | MARKET 5.4% | 09:00 median 13.00 | Matchbook 17.00
    comment: Beaten into a sixth last time out, Schiehallion has shown little consistency, though he did land a win two starts back, and he has run over today's trip and going before.
    DATA: model 7.1% | style Midfield (led 3% of runs) | runs in data 9 | last 3: 18 Sep Downpatrick Chase 23.5f Good 4/15; 9 Oct Downpatrick Chase 23.7f Good 1/14; 3 Nov Fairyhouse (IRE) Chase 24.5f Good To Yielding 6/7 fig 91
    DATA for: Has won at this trip or further; Carries 5 lb less than average
    DATA against: Official rating 96, 6 lb below field average; Pulled up in 1 of its last 5 jumps runs
- Brother Hollie (hrs_57654618) | 4yo G | 140lb | OR 92 | draw 0 | jockey Josh Williamson(3) | trainer Mark Michael McNiff (14d 0/1) | headgear t | last run 27 days | form -8305U | MARKET 4.3% | 09:00 median 21.00 | Matchbook 19.00
    comment: Brother Hollie is hard to fancy after unseating last time out and being winless in his last five, with a fifth two starts back his best recent effort bar a third four starts back.
    DATA: model 4.5% | style Midfield (led 3% of runs) | runs in data 7 | last 3: 7 Sep Galway Hurdle 16.7f Yielding 19/20; 30 Sep Sligo Chase 21f Good 5/15; 23 Oct Sligo (IRE) Hurdle 20.5f Yielding To Soft UR/12
    DATA for: Carries 17 lb less than average
    DATA against: Official rating 92, 10 lb below field average; Fell or unseated in 1 of its last 5 jumps runs
- Wing Back (hrs_39698897) | 6yo G | 146lb | OR 90 | draw 0 | jockey Aidan Kelly | trainer Charlie Keegan (14d 0/1) | headgear h | last run 28 days | form -967P4 | MARKET 3.8% | 09:00 median 23.00 | Matchbook 23.00
    comment: Wing Back is hard to fancy, winless in his last five and pulled up two starts back, with a ninth, a sixth and a seventh also in the book.
    DATA: model 5.8% | style Held up (led 3% of runs) | runs in data 5 | last 3: 31 Aug Downpatrick Chase 19.5f Good 7/15; 30 Sep Sligo Chase 21f Good PU/15; 22 Oct Clonmel (IRE) Chase 21f Good 4/15 fig 83
    DATA for: Carries 11 lb less than average
    DATA against: Best recent form figure 83, 9 lb below field average; Recent figures 7 lb below its current mark (looks high in the weights); Official rating 90, 12 lb below field average; Pulled up in 1 of its last 5 jumps runs
- Dundaniel (hrs_21328020) | 11yo G | 162lb | OR 106 | draw 0 | jockey Eoin Staples(5) | trainer N F Glynn (14d 0/0) | headgear - | last run 308 days | form 25345- | MARKET 3.7% | 09:00 median 23.00 | Matchbook 29.00
    comment: The main risk is a 308-day absence under 162 lb.
    DATA: model 7.3% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 15 Jan Fairyhouse Chase 21f Soft 5/14
    DATA against: Carries 5 lb more than average; Returns from a 308-day break; Lightly raced: 1 run in our data, so the model has little to go on; Aged 11, older than most of this field
- Gatsby Grey (hrs_23796549) | 10yo G | 156lb | OR 100 | draw 0 | jockey Phillip Enright | trainer Oliver McKiernan (14d 0/7) | headgear tp | last run 28 days | form PPP-76 | MARKET 3.5% | 09:00 median 26.00 | Matchbook 22.00
    DATA: model 3.2% | style Held up (led 3% of runs) | runs in data 7 | last 3: 21 Sep Listowel Flat 12f Yielding 10/11; 10 Oct Fairyhouse Chase 24.5f Good 7/9; 22 Oct Clonmel (IRE) Chase 21f Good 6/10 fig 94
    DATA against: Recent figures 6 lb below its current mark (looks high in the weights); Poor recent finishing positions; Pulled up in 3 of its last 5 jumps runs
- Labondance (hrs_53358893) | 5yo M | 168lb | OR 112 | draw 0 | jockey Donagh Meyler | trainer Emmet Mullins (14d 0/3) | headgear tp | last run 19 days | form F-440U | MARKET 3.1% | 09:00 median 21.00 | Matchbook 34.00
    comment: Labondance is hard to fancy, having unseated last time out and fallen five starts back, with a fourth three starts back and another fourth four starts back her best finishes in recent runs.
    DATA: model 5.6% | style Leader (led 72% of runs) | runs in data 4 | last 3: 20 Sep Listowel Hurdle 22f Good 4/16; 13 Oct Punchestown Hurdle 23.4f Good 12/18; 31 Oct Down Royal (IRE) Chase 24f Good UR/12
    DATA for: Official rating 112, 10 lb above field average
    DATA against: Carries 11 lb more than average; Fell or unseated in 1 of its last 4 jumps runs
- Clonbury Bridge (hrs_21526659) | 10yo G | 162lb | OR 106 | draw 0 | jockey Keith Donoghue | trainer J P Dempsey (14d 0/4) | headgear tp | last run 25 days | form P4-P50 | MARKET 2.6% | 09:00 median 34.00 | Matchbook 36.00
    comment: The risk is a patchy record: unplaced last time, a fifth two starts back, and two pulled-up efforts in his last five.
    DATA: model 3.0% | style Leader (led 23% of runs) | runs in data 4 | last 3: 25 May Ballinrobe Chase 19.6f Good PU/13; 10 Oct Fairyhouse Chase 24.5f Good 5/9; 25 Oct Galway (IRE) Chase 18f Soft To Heavy 11/13
    DATA against: Carries 5 lb more than average; Pulled up in 1 of its last 4 jumps runs

## 1:15 Thurles | race_id rac_32304756627 | Irish Stallion Farms EBF Novice Hurdle
Hurdle |  | 2m6f110y | going Good | Turf | 4 runners | rating band - | age 5yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Hi Ho Idaho (hrs_52055752) | 5yo G | 164lb | OR 121 | draw 0 | jockey Danny Gilligan | trainer Cian Collins (14d 1/6) | headgear t | last run 57 days | form 32-182 | MARKET 33.6% | 09:00 median 2.75 | Matchbook 2.84
    DATA: model 23.6% | style Prominent (led 23% of runs) | runs in data 5 | last 3: 11 May Killarney Hurdle 20.2f Good To Yielding 1/12; 20 Aug Killarney Hurdle 17f Good 8/10; 23 Sep Listowel Hurdle 24f Good 2/14
    DATA for: Last-run finishing speed +2.1% vs that field (finished strongly); Good recent finishing positions
- Brother Walfrid (hrs_51434208) | 5yo G | 164lb | OR 117 | draw 0 | jockey Jack Kennedy | trainer Gordon Elliott (14d 12/72) | headgear tp (1st time) | last run 25 days | form 415264 | MARKET 27.5% | 09:00 median 3.00 | Matchbook 3.70
    DATA: model 20.9% | style Midfield (led 4% of runs) | runs in data 7 | last 3: 20 Aug Killarney Hurdle 22.8f Good 2/5; 18 Sep Downpatrick Hurdle 21.5f Good 6/9; 25 Oct Galway (IRE) Hurdle 20.5f Soft 4/5 fig 105
    DATA for: First-time headgear
    DATA against: Race comments mention jumping mistakes in 4 of its last 5 runs
- Minella Emperor (hrs_41190226) | 7yo G | 164lb | OR 124 | draw 0 | jockey Mr M J O'Neill(7) | trainer Emmet Mullins (14d 0/3) | headgear - | last run 18 days | form 20P-1P | MARKET 23.6% | 09:00 median 3.75 | Matchbook 4.10
    DATA: model 17.9% | style Midfield (led 3% of runs) | runs in data 6 | last 3: 4 Apr Fairyhouse Hurdle 23.8f Yielding To Soft PU/20; 11 Oct Cork Hurdle 24.2f Good 1/3; 1 Nov Cork (IRE) Hurdle 24.5f Good To Yielding PU/6
    DATA for: Official rating 124, 5 lb above field average; Has won at this trip or further
    DATA against: Race comments mention jumping mistakes in 2 of its last 5 runs; Pulled up in 2 of its last 5 jumps runs
- Little Ginger (hrs_61684539) | 5yo G | 164lb | OR 113 | draw 0 | jockey Alan O'Sullivan(5) | trainer James Andrew Fahey (14d 0/6) | headgear - | last run 41 days | form 4-1021 | MARKET 15.3% | 09:00 median 6.00 | Matchbook 6.20
    DATA: model 37.6% | style Prominent (led 3% of runs) | runs in data 6 | last 3: 6 Jun Punchestown Hurdle 16.5f Good To Yielding 12/24; 18 Sep Downpatrick Hurdle 17.8f Good 2/15; 9 Oct Downpatrick Hurdle 21.8f Good 1/6
    DATA for: Good recent finishing positions
    DATA against: Official rating 113, 6 lb below field average

## 1:50 Thurles | race_id rac_32304758564 | Irish Stallion Farms EBF Mares Maiden Hurdle
Hurdle |  | 2m6f110y | going Good | Turf | 15 runners | rating band - | age 4yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Light Up The Dark (hrs_37932475) | 5yo M | 161lb | OR - | draw 0 | jockey Mark Walsh | trainer Joseph Patrick O'Brien (14d 3/27) | headgear - | last run 25 days | form 11/2 | MARKET 35.9% | 09:00 median 2.20 | Matchbook 2.50
    DATA: model 16.5% | style Midfield (led 3% of runs) | runs in data 7 | last 3: 27 Sep Curragh Flat 16.8f Heavy 19/30; 11 Oct Naas Flat 16f Soft 10/17; 25 Oct Galway (IRE) Hurdle 16f Soft 2/8 fig 103
    DATA for: Best recent form figure 103, 10 lb above field average
- I Dont Really Care (hrs_59928120) | 5yo M | 153lb | OR 116 | draw 0 | jockey Daniel King | trainer Ray Hackett (14d 0/5) | headgear - | last run 18 days | form -43F43 | MARKET 29.0% | 09:00 median 2.75 | Matchbook 3.10
    DATA: model 12.1% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 28 Sep Roscommon Hurdle 20.2f Good To Yielding F/15; 17 Oct Limerick (IRE) Hurdle 23.5f Good To Yielding 4/6 fig 121; 1 Nov Cork (IRE) Hurdle 16f Good To Yielding 3/19 fig 108
    DATA for: Best recent form figure 121, 28 lb above field average
    DATA against: Fell or unseated in 1 of its last 5 jumps runs
- Dinner Dance (hrs_60343346) | 5yo M | 153lb | OR - | draw 0 | jockey Jack Kennedy | trainer Gordon Elliott (14d 12/72) | headgear - | last run 33 days | form 1-25 | MARKET 11.6% | 09:00 median 5.50 | Matchbook 9.40
    DATA: model 12.4% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 22 May Downpatrick NH Flat 17.8f Good To Yielding 2/7; 17 Oct Limerick (IRE) NH Flat 17f Good To Yielding 5/8 fig 102
    DATA for: Best recent form figure 102, 9 lb above field average
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; First run over hurdles in our data
- Jury Time (hrs_51124087) | 5yo M | 153lb | OR - | draw 0 | jockey Phillip Enright | trainer S Curling (14d 0/1) | headgear - | last run 24 days | form 1323-5 | MARKET 11.0% | 09:00 median 7.50 | Matchbook 8.20
    DATA: model 13.2% | style Prominent (led 38% of runs) | runs in data 3 | last 3: 10 Feb Limerick NH Flat 15.7f Heavy 2/7; 12 Mar Limerick NH Flat 16.9f Heavy 3/7; 26 Oct Galway (IRE) Hurdle 16.5f Soft To Heavy 5/10
    DATA for: Good recent finishing positions
- An Lachin Beag (hrs_58565472) | 6yo M | 153lb | OR - | draw 0 | jockey Paddy Cleary(7) | trainer Nigel Thomas Slevin (14d 0/4) | headgear - | last run 45 days | form 30-F47 | MARKET 3.0% | 09:00 median 21.00 | Matchbook 50.00
    DATA: model 10.4% | style Prominent (led 5% of runs) | runs in data 3 | last 3: 6 Aug Sligo Hurdle 17.9f Good F/13; 7 Sep Galway NH Flat 16.7f Soft 4/18; 5 Oct Fairyhouse Hurdle 20f Good 7/10
    DATA against: Fell or unseated in 1 of its last 2 jumps runs
- Mystery Decision (hrs_17390030476) | 7yo M | 153lb | OR 94 | draw 0 | jockey Eoghan Finegan(5) | trainer Hugh Paul Finegan (14d 0/1) | headgear t | last run 20 days | form -564P5 | MARKET 2.2% | 09:00 median 34.00 | Matchbook 55.00
    DATA: model 5.7% | style Held up (led 4% of runs) | runs in data 3 | last 3: 8 Aug Kilbeggan Hurdle 19f Good 5/13; 26 Aug Bellewstown Hurdle 20.5f Good 6/14; 30 Oct Down Royal (IRE) Hurdle 22.5f Yielding 5/9 fig 83
    DATA for: Last-run finishing speed +3.0% vs that field (finished strongly)
    DATA against: Best recent form figure 83, 10 lb below field average; Pace: steady gallop likely, hard to come from off the pace
- Filly Butler (hrs_17394781341) | 5yo M | 153lb | OR - | draw 0 | jockey John Shinnick | trainer G Ahern (14d 0/0) | headgear - | last run 18 days | form 4 | MARKET 1.8% | 09:00 median 34.00 | Matchbook 70.00
    DATA: model 2.5% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 1 Nov Cork (IRE) Hurdle 16f Good To Yielding 4/19
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Hadie (hrs_17395568806) | 4yo F | 152lb | OR - | draw 0 | jockey Carl Millar(5) | trainer David Kenneth Budds (14d 1/2) | headgear - | last run - days | form - | MARKET 1.2% | 09:00 median 67.00 | Matchbook 110.00
    DATA: model 3.9% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Crios Cu Chulainn (hrs_64036742) | 5yo M | 153lb | OR - | draw 0 | jockey Harry Sexton(7) | trainer David K Walsh (14d 0/0) | headgear - | last run 33 days | form 9760 | MARKET 1.1% | 09:00 median 51.00 | Matchbook 140.00
    DATA: model 8.4% | style Midfield (led 5% of runs) | runs in data 4 | last 3: 27 May Wexford NH Flat 20f Good To Yielding 7/13; 9 Jun Sligo Hurdle 17.7f Yielding 6/11; 17 Oct Limerick (IRE) Hurdle 19f Good To Yielding 13/18
    DATA against: Poor recent finishing positions
- Park On The Green (hrs_17393944855) | 6yo M | 153lb | OR - | draw 0 | jockey Mr D Doyle(5) | trainer Timothy Doyle (14d 0/2) | headgear - | last run 33 days | form 7 | MARKET 1.0% | 09:00 median 81.00 | Matchbook 180.00
    DATA: model 3.3% | style Held up (led 8% of runs) | runs in data 1 | last 3: 17 Oct Limerick (IRE) NH Flat 17f Good To Yielding 7/8
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Rarely Miss Taken (hrs_65225377) | 5yo M | 153lb | OR - | draw 0 | jockey Sam Ewing | trainer W R Crawford (14d 1/3) | headgear - | last run 19 days | form 00 | MARKET 0.7% | 09:00 median 101.00 | Matchbook 300.00
    DATA: model 4.7% | style Held up (led 5% of runs) | runs in data 2 | last 3: 31 May Kilbeggan NH Flat 15.7f Good To Yielding 10/10; 31 Oct Down Royal (IRE) NH Flat 17f Good 10/14 fig 84
    DATA against: Best recent form figure 84, 9 lb below field average; Lightly raced: 2 runs in our data, so the model has little to go on; First run over hurdles in our data; Pace: steady gallop likely, hard to come from off the pace
- Eagle River (hrs_52495366) | 5yo M | 153lb | OR - | draw 0 | jockey Liam Quinlan | trainer Ms M Flynn (14d 0/1) | headgear - | last run 18 days | form /F4-P0 | MARKET 0.6% | 09:00 median 126.00 | Matchbook 370.00
    DATA: model 2.1% | style Held up (led 5% of runs) | runs in data 2 | last 3: 11 May Killarney Hurdle 22.5f Good To Yielding PU/16; 1 Nov Cork (IRE) Hurdle 16f Good To Yielding 13/19
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Pulled up in 1 of its last 2 jumps runs; Pace: steady gallop likely, hard to come from off the pace
- Sea Swirl (hrs_17393429613) | 6yo M | 153lb | OR - | draw 0 | jockey John Aherne(7) | trainer Lawrence Walshe (14d 0/1) | headgear - | last run 14 days | form /FP-86 | MARKET 0.4% | 09:00 median 201.00 | Matchbook 380.00
    DATA: model 1.6% | style Held up (led 5% of runs) | runs in data 2 | last 3: 8 Oct Tramore NH Flat 16f Yielding 8/8; 5 Nov Clonmel (IRE) Hurdle 19.5f Good 6/12 fig 66
    DATA against: Best recent form figure 66, 27 lb below field average; Lightly raced: 2 runs in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Hello Wee Love (hrs_66432121) | 4yo F | 152lb | OR - | draw 0 | jockey Alex Harvey | trainer R K Watson (14d 0/3) | headgear h (1st time) | last run 20 days | form P9 | MARKET 0.2% | 09:00 median 201.00 | Matchbook 1000.00
    DATA: model 1.5% | style Held up (led 5% of runs) | runs in data 2 | last 3: 14 Jul Downpatrick Hurdle 21.8f Good PU/12; 30 Oct Down Royal (IRE) Hurdle 22.5f Yielding 9/9
    DATA for: First-time headgear
    DATA against: Last-run finishing speed -11.5% vs that field (faded); Lightly raced: 2 runs in our data, so the model has little to go on; Pulled up in 1 of its last 2 jumps runs; Pace: steady gallop likely, hard to come from off the pace
- Pat's Prodigies (hrs_17393749814) | 4yo F | 152lb | OR - | draw 0 | jockey Tiernan Power Roche | trainer P. J. Rothwell (14d 0/24) | headgear - | last run 15 days | form 000 | MARKET 0.2% | 09:00 median 201.00 | Matchbook 1000.00
    DATA: model 1.7% | style Held up (led 4% of runs) | runs in data 3 | last 3: 13 Oct Punchestown NH Flat 16.2f Good 10/14; 23 Oct Sligo (IRE) Hurdle 17.5f Yielding 12/13; 4 Nov Wexford (IRE) Hurdle 16.5f Yielding 12/14
    DATA against: Trainer 0 wins from 24 runs, last 14 days; Last-run finishing speed -5.0% vs that field (faded); Poor recent finishing positions; Pace: steady gallop likely, hard to come from off the pace

## 2:25 Thurles | race_id rac_32304760501 | William Hill Challenge Series Handicap Hurdle
Hurdle |  | 2m4f0y | going Good | Turf | 17 runners | rating band - | age 3yo+
DATA pace: Even - Two likely leaders (Mont Star, Ocean Murphy). A fair, even gallop is most likely.
- Cock And Bull (hrs_36878835) | 5yo G | 156lb | OR 99 | draw 0 | jockey Donagh Meyler | trainer Emmet Mullins (14d 0/3) | headgear t | last run 40 days | form 8570- | MARKET 23.3% | 09:00 median 3.00 | Matchbook 4.00 | CHECK (skip line 2.85)
    comment: Cock And Bull is winless in his last four, finishing unplaced last time, then seventh, fifth and eighth, and a 40-day break does little to suggest a turnaround.
    DATA: model 8.6% | style Prominent (led 3% of runs) | runs in data 7 | last 3: 26 Jun Curragh Flat 16.3f Good 3/11; 29 Jul Galway Flat 16.5f Yielding 1/19; 10 Oct Newmarket Flat 18f Good 20/29
    DATA for: Good recent finishing positions
    DATA against: Last-run finishing speed -3.1% vs that field (faded)
- Ocean Murphy (hrs_57654562) | 4yo G | 159lb | OR 103 | draw 0 | jockey Harry Sexton(7) | trainer P. J. Rothwell (14d 0/24) | headgear p | last run 48 days | form -91216 | MARKET 8.3% | 09:00 median 9.50 | Matchbook 10.50
    comment: Ocean Murphy won two starts back and four starts back, with a second three starts back, but he was only sixth last time out and returns after 48 days off, while the yard is 0/24 in the last 14 days.
    DATA: model 9.3% | style Leader (led 63% of runs) | runs in data 7 | last 3: 8 Aug Wexford Hurdle 20.2f Good 2/6; 24 Aug Ballinrobe Hurdle 18.2f Good 1/5; 2 Oct Gowran Park Hurdle 20.2f Good 6/14
    DATA for: Official rating 103, 6 lb above field average; Has won at this trip or further; Good recent finishing positions
    DATA against: Trainer 0 wins from 24 runs, last 14 days
- Crowsatedappletart (hrs_27565923) | 9yo G | 164lb | OR 107 | draw 0 | jockey Eoghan Finegan(5) | trainer Michael Winters (14d 1/4) | headgear tp | last run 25 days | form 165P62 | MARKET 8.3% | 09:00 median 7.50 | Matchbook 13.50
    comment: The main risk is a hefty 164 lb, with only one win in his last six starts.
    DATA: model 6.9% | style Midfield (led 4% of runs) | runs in data 7 | last 3: 11 Oct Cork Chase 17.6f Good PU/8; 18 Oct Limerick (IRE) Hurdle 19.5f Good To Yielding 6/14 fig 91; 25 Oct Wexford (IRE) Hurdle 17f Soft 2/13 fig 107
    DATA for: Best recent form figure 107, 15 lb above field average; Official rating 107, 10 lb above field average
    DATA against: Carries 10 lb more than average; Race comments mention jumping mistakes in 2 of its last 5 runs; Pulled up in 1 of its last 5 jumps runs
- Hidalgo Des Mottes (hrs_30002329) | 9yo G | 144lb | OR 87 | draw 0 | jockey Ms N M Bradley(7) | trainer Eoin Griffin (14d 0/2) | headgear tp | last run 9 days | form 829582 | MARKET 8.2% | 09:00 median 9.00 | Matchbook 11.50
    comment: Winless in his last six, Hidalgo Des Mottes is hard to fancy, with an eighth and a ninth among his last four before a second last time out, though he is back quickly after nine days.
    DATA: model 4.6% | style Prominent (led 3% of runs) | runs in data 8 | last 3: 2 Oct Gowran Park Hurdle 20.2f Good 5/13; 13 Oct Punchestown Hurdle 20f Good 8/17; 10 Nov Fairyhouse (IRE) Hurdle 20.5f Good To Yielding 2/11 fig 88
    DATA for: Carries 10 lb less than average
    DATA against: Best recent form figure 88, 4 lb below field average; Official rating 87, 10 lb below field average
- Allo Al Khawaneej (hrs_28014084) | 6yo G | 163lb | OR 106 | draw 0 | jockey Philip Byrnes | trainer C Byrnes (14d 0/8) | headgear v | last run 10 days | form -40325 | MARKET 7.7% | 09:00 median 10.00 | Matchbook 11.50
    comment: Fit after just ten days off, Allo Al Khawaneej has shown placed form, with a second and a third in his last five outings, and he has run over today's trip and going before.
    DATA: model 10.6% | style Midfield (led 23% of runs) | runs in data 5 | last 3: 26 Aug Bellewstown Hurdle 20.5f Good 3/13; 1 Oct Clonmel Hurdle 19.7f Good 2/13; 9 Nov Punchestown (IRE) Hurdle 16f Good To Yielding 5/9 fig 106
    DATA for: Best recent form figure 106, 14 lb above field average; Official rating 106, 9 lb above field average; Good recent finishing positions
    DATA against: Trainer 0 wins from 8 runs, last 14 days; Carries 9 lb more than average; Race comments mention jumping mistakes in 3 of its last 5 runs
- Migdam (hrs_26131126) | 7yo G | 161lb | OR 104 | draw 0 | jockey Phillip Enright | trainer Declan Queally (14d 0/7) | headgear - | last run 49 days | form 18-747 | MARKET 7.4% | 09:00 median 9.00 | Matchbook 13.50
    comment: The main risk is a 49-day break and a seventh last time out, with 161 lb to carry.
    DATA: model 5.2% | style Held up (led 3% of runs) | runs in data 5 | last 3: 4 Sep Kilbeggan Hurdle 16.1f Good To Yielding 7/9; 18 Sep Downpatrick Hurdle 17.8f Good 4/10; 1 Oct Clonmel Hurdle 19.7f Good 7/13
    DATA for: Official rating 104, 7 lb above field average
    DATA against: Carries 7 lb more than average
- Our Girl Ellie (hrs_45445260) | 6yo M | 144lb | OR 87 | draw 0 | jockey Michael Kenneally(3) | trainer Stephen Ryan (14d 0/0) | headgear t | last run 33 days | form 6-0093 | MARKET 7.2% | 09:00 median 10.00 | Matchbook 13.00
    DATA: model 2.9% | style Midfield (led 3% of runs) | runs in data 4 | last 3: 28 Sep Roscommon Hurdle 15.6f Good To Yielding 12/16; 11 Oct Cork Hurdle 18.9f Good 9/14; 17 Oct Limerick (IRE) Hurdle 17f Good To Yielding 3/15 fig 83
    DATA for: Carries 10 lb less than average
    DATA against: Best recent form figure 83, 9 lb below field average; Official rating 87, 10 lb below field average
- Demanding Gerry (hrs_37164064) | 7yo M | 141lb | OR 84 | draw 0 | jockey Philip Donovan | trainer James Andrew Fahey (14d 0/6) | headgear tp (1st time) | last run 12 days | form 4P4524 | MARKET 5.1% | 09:00 median 15.00 | Matchbook 18.50
    comment: Winless in her last six, Demanding Gerry has been consistent without cracking it, with a fourth last time out, 12 days ago, and a second two starts back, but a pulled up five starts back shows the risk.
    DATA: model 7.6% | style Midfield (led 3% of runs) | runs in data 7 | last 3: 19 Sep Navan Hurdle 19f Good 5/15; 1 Oct Clonmel Hurdle 19.7f Good 2/11; 7 Nov Gowran Park (IRE) Hurdle 20f Good To Yielding 4/14 fig 81
    DATA for: Carries 13 lb less than average; First-time headgear
    DATA against: Best recent form figure 81, 11 lb below field average; Official rating 84, 13 lb below field average; Pulled up in 1 of its last 5 jumps runs
- Mont Star (hrs_58963044) | 4yo G | 159lb | OR 103 | draw 0 | jockey Mike O'Connor | trainer Henry de Bromhead (14d 7/38) | headgear t | last run 103 days | form 8-26 | MARKET 4.9% | 09:00 median 15.00 | Matchbook 19.00
    comment: Mont Star is winless in his last three, finishing sixth last time out, and a 103-day absence plus a burden of 159 lb make him hard to fancy.
    DATA: model 9.6% | style Leader (led 38% of runs) | runs in data 2 | last 3: 10 Jul Cork Hurdle 17.3f Good 2/14; 8 Aug Kilbeggan Hurdle 19f Good 6/13
    DATA for: Official rating 103, 6 lb above field average
    DATA against: Returns from a 103-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- Liberated Light (hrs_27110405) | 7yo G | 153lb | OR 96 | draw 0 | jockey Mr J L Gleeson | trainer John E & Thomas Kiely (14d 0/3) | headgear tp | last run 54 days | form 72-019 | MARKET 4.9% | 09:00 median 15.00 | Matchbook 19.50
    DATA: model 5.9% | style Held up (led 3% of runs) | runs in data 9 | last 3: 2 Sep Navan Flat 16f Good 3/16; 21 Sep Listowel Flat 14.2f Yielding 5/15; 26 Sep Listowel Hurdle 22f Good 9/17
    DATA against: Race comments mention jumping mistakes in 2 of its last 5 runs
- River Vale (hrs_28930930) | 10yo G | 164lb | OR 107 | draw 0 | jockey Kevin A Murphy(7) | trainer Michael Winters (14d 1/4) | headgear - | last run 25 days | form DF41-P | MARKET 3.8% | 09:00 median 19.00 | Matchbook 26.00
    comment: River Vale won two starts back and has run over today's trip and going, but he was pulled up last time out and has a fell and a disqualification in his last five.
    DATA: model 7.1% | style Prominent (led 3% of runs) | runs in data 5 | last 3: 12 Mar Limerick Chase 17.8f Heavy 4/8; 6 Apr Cork Chase 17.2f Good To Yielding 1/6; 25 Oct Wexford (IRE) Hurdle 17f Soft PU/13
    DATA for: Official rating 107, 10 lb above field average
    DATA against: Carries 10 lb more than average; Fell or unseated in 1 of its last 5 jumps runs; Pulled up in 1 of its last 5 jumps runs; Aged 10, older than most of this field
- Coolboy Christy (hrs_50906268) | 5yo G | 148lb | OR 91 | draw 0 | jockey Shane O'Callaghan(3) | trainer P. J. Rothwell (14d 0/24) | headgear b | last run 32 days | form 450509 | MARKET 3.7% | 09:00 median 19.00 | Matchbook 27.00
    DATA: model 4.7% | style Held up (led 3% of runs) | runs in data 11 | last 3: 19 Aug Sligo Hurdle 20.7f Good 5/10; 4 Oct Killarney Hurdle 22.8f Good To Yielding 10/13; 18 Oct Limerick (IRE) Hurdle 19.5f Good To Yielding 9/14
    DATA for: Carries 6 lb less than average
    DATA against: Official rating 91, 6 lb below field average; Trainer 0 wins from 24 runs, last 14 days; Race comments mention jumping mistakes in 2 of its last 5 runs
- Getaway Charlie (hrs_24555454) | 10yo G | 163lb | OR 106 | draw 0 | jockey Mr D Doyle(5) | trainer Timothy Doyle (14d 0/2) | headgear b (1st time) | last run 9 days | form 401576 | MARKET 3.4% | 09:00 median 23.00 | Matchbook 27.00
    comment: The risk is a slide of a sixth and a seventh in his last two, and he carries 163 lb.
    DATA: model 8.2% | style Held up (led 3% of runs) | runs in data 8 | last 3: 2 Oct Gowran Park Hurdle 20.2f Good 5/20; 13 Oct Punchestown Hurdle 23.4f Good 7/18; 10 Nov Fairyhouse (IRE) Hurdle 20.5f Good To Yielding 6/11 fig 98
    DATA for: Best recent form figure 98, 6 lb above field average; Official rating 106, 9 lb above field average; Has won at this trip or further; First-time headgear
    DATA against: Recent figures 8 lb below its current mark (looks high in the weights); Carries 9 lb more than average; Race comments mention jumping mistakes in 2 of its last 5 runs; Aged 10, older than most of this field
- Ollie La Ba Ba (hrs_34571635) | 8yo G | 166lb | OR 109 | draw 0 | jockey G B Noonan | trainer Eoin Christopher McCarthy (14d 0/6) | headgear t | last run 91 days | form 166-69 | MARKET 1.3% | 09:00 median 51.00 | Matchbook 100.00
    comment: Ollie La Ba Ba won five starts back but has since finished a sixth, a sixth and another sixth before a ninth last time out, and returns after 91 days off.
    DATA: model 3.5% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 8 Jun Roscommon Hurdle 20f Yielding To Soft 6/9; 20 Aug Killarney Chase 20.8f Good 9/11
    DATA for: Official rating 109, 12 lb above field average
    DATA against: Carries 12 lb more than average; Returns from a 91-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- Futurum Regem (hrs_14995246) | 10yo G | 148lb | OR 91 | draw 0 | jockey Patrick M O'Brien(5) | trainer Hugh Paul Finegan (14d 0/1) | headgear b | last run 9 days | form 9578-8 | MARKET 1.0% | 09:00 median 67.00 | Matchbook 130.00
    comment: Futurum Regem has finished eighth, eighth, seventh, fifth and ninth in his last five starts, so he is winless in that spell, but he is back quickly after nine days and has run over today's trip and going.
    DATA: model 2.3% | style Held up (led 8% of runs) | runs in data 1 | last 3: 10 Nov Fairyhouse (IRE) Hurdle 20.5f Good To Yielding 8/11 fig 83
    DATA for: Carries 6 lb less than average
    DATA against: Best recent form figure 83, 9 lb below field average; Recent figures 8 lb below its current mark (looks high in the weights); Official rating 91, 6 lb below field average; Lightly raced: 1 run in our data, so the model has little to go on; Aged 10, older than most of this field
- Thedreamistilalive (hrs_66619462) | 4yo F | 140lb | OR 77 | draw 0 | jockey Rian Lane(7) | trainer Donncha Duggan (14d 0/2) | headgear t | last run 97 days | form 906 | MARKET 0.8% | 09:00 median 67.00 | Matchbook 210.00
    comment: Winless in her last three, with a sixth last time out, an unplaced run two starts back and a ninth three starts back, and 97 days off, Thedreamistilalive is hard to fancy under 140 lb.
    DATA: model 1.3% | style Held up (led 4% of runs) | runs in data 3 | last 3: 10 Jul Kilbeggan Hurdle 16f Good 9/11; 1 Aug Galway Hurdle 16.8f Good To Yielding 15/19; 14 Aug Tramore Hurdle 21f Good 6/15
    DATA for: Carries 14 lb less than average
    DATA against: Official rating 77, 20 lb below field average; Poor recent finishing positions; Returns from a 97-day break
- Jay Jay Zee (hrs_34961339) | 7yo G | 148lb | OR 91 | draw 0 | jockey Conor Smithers(7) | trainer Charlie Keegan (14d 0/1) | headgear - | last run 25 days | form /F-008 | MARKET 0.8% | 09:00 median 81.00 | Matchbook 160.00
    comment: Jay Jay Zee is winless in his last four, finishing eighth last time out after two unplaced runs and a fall four starts back, though he has run over today's trip and returns after 25 days.
    DATA: model 1.8% | style Held up (led 3% of runs) | runs in data 4 | last 3: 7 Sep Galway Hurdle 16.7f Yielding 20/20; 6 Oct Galway Hurdle 16.6f Yielding To Soft 10/11; 25 Oct Wexford (IRE) Hurdle 17f Soft 8/13
    DATA for: Carries 6 lb less than average
    DATA against: Official rating 91, 6 lb below field average; Poor recent finishing positions; Fell or unseated in 1 of its last 4 jumps runs

## 3:00 Thurles | race_id rac_32304762438 | Racing Again On The 26th November Handicap Hurdle
Hurdle |  | 1m7f169y | going Good | Turf | 17 runners | rating band 0-100 | age 3yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Max Meridius (hrs_40260661) | 5yo G | 160lb | OR 92 | draw 0 | jockey Danny Gilligan | trainer Thomas Mullins (14d 0/7) | headgear - | last run 7 days | form 510553 | MARKET 31.1% | 09:00 median 2.63 | Matchbook 2.74
    comment: Third last time out and back quickly after seven days, Max Meridius has run over today's trip and going, but he's finished fifth in two of the three runs before that and his one win came five starts back.
    DATA: model 16.3% | style Prominent (led 23% of runs) | runs in data 14 | last 3: 8 Oct Thurles Flat 12.7f Yielding 1/14; 20 Oct Curragh (IRE) Flat 10f Yielding 14/24 fig 52; 12 Nov Thurles (IRE) Hurdle 16f Good 3/16 fig 94
    DATA for: Best recent form figure 94, 10 lb above field average; Official rating 92, 7 lb above field average; Has won at this trip or further; Good recent finishing positions
    DATA against: Carries 7 lb more than average; Race comments mention jumping mistakes in 2 of its last 5 runs
- Liceo (hrs_36192702) | 6yo G | 168lb | OR 100 | draw 0 | jockey P J O'Hanlon | trainer Dermot A McLoughlin (14d 0/7) | headgear tp | last run 7 days | form 353522 | MARKET 16.4% | 09:00 median 4.50 | Matchbook 5.60
    comment: Liceo arrives in cracking nick, runner-up last time out and a second two starts back, having run just seven days ago, and he has run over today's trip and going before. Yet to win in his last six, he must defy 168 lb, which is the one real concern.
    DATA: model 9.4% | style Midfield (led 3% of runs) | runs in data 7 | last 3: 8 Aug Kilbeggan Hurdle 16f Good 5/13; 10 Oct Fairyhouse Hurdle 16f Good 2/15; 12 Nov Thurles (IRE) Hurdle 16f Good 2/16 fig 103
    DATA for: Best recent form figure 103, 19 lb above field average; Official rating 100, 15 lb above field average; Good recent finishing positions
    DATA against: Carries 15 lb more than average
- Atlantic Wonder (hrs_29243354) | 9yo G | 141lb | OR 73 | draw 0 | jockey Daniel King | trainer A. J. Martin (14d 0/10) | headgear t | last run 14 days | form 9P-565 | MARKET 8.4% | 09:00 median 8.50 | Matchbook 11.50
    comment: Winless in his last five, Atlantic Wonder has finished fifth, sixth, fifth, pulled up and ninth, so he is hard to fancy off 141 lb.
    DATA: model 7.6% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 28 Sep Roscommon Hurdle 15.6f Good To Yielding 5/16; 23 Oct Sligo (IRE) Hurdle 17.5f Yielding 6/13 fig 65; 5 Nov Clonmel (IRE) Chase 17f Good To Yielding 5/15 fig 73
    DATA for: Carries 12 lb less than average
    DATA against: Best recent form figure 73, 11 lb below field average; Official rating 73, 12 lb below field average; Trainer 0 wins from 10 runs, last 14 days; Pulled up in 1 of its last 5 jumps runs
- Phoenix Arizona (hrs_39431553) | 7yo G | 161lb | OR 93 | draw 0 | jockey Thomas O'Connor(7) | trainer John J Cullen (14d 0/0) | headgear p | last run 20 days | form 281355 | MARKET 8.1% | 09:00 median 9.00 | Matchbook 12.00
    comment: Phoenix Arizona has run fifth in each of his last two outings, a third three starts back and a win four starts back showing he can get involved, and he's fit enough after 20 days.
    DATA: model 6.8% | style Prominent (led 3% of runs) | runs in data 11 | last 3: 30 Sep Sligo Chase 17.7f Good 3/7; 11 Oct Cork Chase 17.6f Good 5/7; 30 Oct Down Royal (IRE) Chase 16.5f Good To Yielding 5/9 fig 97
    DATA for: Best recent form figure 97, 13 lb above field average; Recent figures 4 lb above its current mark (looks well handicapped); Official rating 93, 8 lb above field average; Has won at this trip or further
    DATA against: Carries 8 lb more than average; Race comments mention jumping mistakes in 2 of its last 5 runs
- Amron Diamond (hrs_35054698) | 7yo G | 140lb | OR 72 | draw 0 | jockey Michael Kenneally(3) | trainer James M Barcoe (14d 2/4) | headgear - | last run 14 days | form 4P-009 | MARKET 5.6% | 09:00 median 13.00 | Matchbook 19.00
    comment: Amron Diamond has been out of form, with a ninth last time out and nothing better than a fourth five starts back, though he is only 14 days since his last run and has run over today's trip and going.
    DATA: model 4.6% | style Midfield (led 5% of runs) | runs in data 3 | last 3: 14 May Clonmel Hurdle 19.5f Good To Yielding 13/15; 28 Sep Roscommon Hurdle 20.2f Good To Yielding 11/16; 5 Nov Clonmel (IRE) Chase 17f Good To Yielding 9/15 fig 63
    DATA for: Carries 13 lb less than average
    DATA against: Best recent form figure 63, 21 lb below field average; Recent figures 9 lb below its current mark (looks high in the weights); Official rating 72, 13 lb below field average; Poor recent finishing positions
- Deed Pole (hrs_32709649) | 6yo G | 168lb | OR 100 | draw 0 | jockey Danny Power(7) | trainer Terence O'Brien (14d 0/4) | headgear - | last run 187 days | form 6270-3 | MARKET 5.5% | 09:00 median 11.00 | Matchbook 23.00
    comment: The one concern is a 187-day absence, with 168 lb to carry.
    DATA: model 11.5% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 25 Apr Limerick Flat 11.9f Yielding 3/16; 16 May Wexford Hurdle 17f Good To Yielding 3/13
    DATA for: Official rating 100, 15 lb above field average; Last-run finishing speed +3.2% vs that field (finished strongly); Good recent finishing positions
    DATA against: Carries 15 lb more than average; Returns from a 187-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- Hob's Angel (hrs_30441138) | 10yo M | 140lb | OR 72 | draw 0 | jockey Josh Williamson(3) | trainer James M Barcoe (14d 2/4) | headgear - | last run 15 days | form 364U96 | MARKET 4.8% | 09:00 median 15.00 | Matchbook 20.00
    comment: Winless in her last six, Hob's Angel was sixth last time out after a ninth and an unseated, so she is hard to fancy, though she is fresh enough after 15 days and has run over today's trip and going.
    DATA: model 5.4% | style Midfield (led 3% of runs) | runs in data 10 | last 3: 9 Oct Downpatrick Hurdle 21.8f Good UR/14; 13 Oct Punchestown Hurdle 20f Good 9/15; 4 Nov Wexford (IRE) Hurdle 20f Yielding 6/13 fig 64
    DATA for: Last-run finishing speed +3.1% vs that field (finished strongly); Has won at this trip or further; Carries 13 lb less than average
    DATA against: Best recent form figure 64, 20 lb below field average; Recent figures 8 lb below its current mark (looks high in the weights); Official rating 72, 13 lb below field average; Poor recent finishing positions; Fell or unseated in 1 of its last 5 jumps runs; Aged 10, older than most of this field
- Beat The Devil (hrs_51650298) | 4yo G | 165lb | OR 97 | draw 0 | jockey Keith Donoghue | trainer Patrick Magee (14d 0/6) | headgear t | last run 4 days | form P-9740 | MARKET 3.0% | 09:00 median 23.00 | Matchbook 36.00
    comment: Winless in his last five, with a fourth two starts back his best finish and an unplaced effort last time out, Beat The Devil is back after just four days and has run on today's going before.
    DATA: model 5.4% | style Held up (led 5% of runs) | runs in data 19 | last 3: 16 Oct Dundalk (AW) (IRE) Flat 10.5f Standard 6/13 fig 41; 23 Oct Sligo (IRE) Hurdle 17.5f Yielding 4/12 fig 97; 15 Nov Navan (IRE) Hurdle 16f Good To Yielding 13/25
    DATA for: Best recent form figure 97, 13 lb above field average; Official rating 97, 12 lb above field average
    DATA against: Carries 12 lb more than average; Pace: steady gallop likely, hard to come from off the pace
- Glengarriff (hrs_35137221) | 5yo G | 160lb | OR 92 | draw 0 | jockey Kieren Buckley | trainer Patrick Downey (14d 0/0) | headgear - | last run 28 days | form -00389 | MARKET 3.0% | 09:00 median 19.00 | Matchbook 46.00
    comment: Glengarriff has run over today's trip and on this going, and a third three starts back is his best recent effort, but he's winless in his last five and was ninth last time out, 28 days ago.
    DATA: model 4.0% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 4 Sep Kilbeggan Hurdle 16.1f Good To Yielding 3/13; 25 Sep Listowel Hurdle 16f Good To Yielding 8/15; 22 Oct Clonmel (IRE) Hurdle 17f Good To Yielding 9/16 fig 88
    DATA for: Official rating 92, 7 lb above field average
    DATA against: Carries 7 lb more than average
- Getaway Henry (hrs_30567943) | 9yo G | 153lb | OR 85 | draw 0 | jockey Gavin Brouder | trainer Daniel Joseph O'Leary (14d 0/2) | headgear b | last run 7 days | form -P1080 | MARKET 3.0% | 09:00 median 21.00 | Matchbook 40.00
    comment: Getaway Henry won four starts back but has been unplaced last time out and an eighth two starts back since, and he returns just seven days after his last run.
    DATA: model 6.1% | style Held up (led 3% of runs) | runs in data 5 | last 3: 10 Jul Cork Hurdle 17.3f Good 16/23; 22 Jul Wexford Chase 15.5f Good 8/13; 12 Nov Thurles (IRE) Hurdle 16f Good 11/17 fig 78
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 78, 6 lb below field average; Recent figures 7 lb below its current mark (looks high in the weights); Poor recent finishing positions; Pulled up in 1 of its last 5 jumps runs; Pace: steady gallop likely, hard to come from off the pace
- Banphrionsa Alainn (hrs_58565416) | 5yo M | 143lb | OR 75 | draw 0 | jockey Harry Sexton(7) | trainer John Joseph Hanlon (14d 0/12) | headgear - | last run 61 days | form 0-05P0 | MARKET 2.8% | 09:00 median 19.00 | Matchbook 55.00
    comment: Winless in her last five, with an unplaced effort last time and a pulled up two starts back, Banphrionsa Alainn is hard to fancy after 61 days off and carrying 143 lb.
    DATA: model 3.5% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 14 Aug Tramore Hurdle 21f Good 5/15; 31 Aug Downpatrick Hurdle 17.8f Good PU/11; 19 Sep Navan Hurdle 19f Good 11/16
    DATA for: Carries 10 lb less than average
    DATA against: Official rating 75, 10 lb below field average; Trainer 0 wins from 12 runs, last 14 days; Last-run finishing speed -4.3% vs that field (faded); Pulled up in 1 of its last 5 jumps runs
- Figero (hrs_55241676) | 5yo G | 164lb | OR 96 | draw 0 | jockey Donagh Meyler | trainer Thomas Mullins (14d 0/7) | headgear t | last run 12 days | form -15068 | MARKET 2.2% | 09:00 median 29.00 | Matchbook 55.00
    comment: The main risk is a slide through a sixth two starts back and an eighth last time out, while he carries 164 lb.
    DATA: model 4.6% | style Midfield (led 4% of runs) | runs in data 8 | last 3: 1 Sep Gowran Park Flat 14f Yielding 13/13; 6 Oct Galway Hurdle 16.6f Yielding To Soft 6/11; 7 Nov Gowran Park (IRE) Hurdle 16f Good To Yielding 8/8
    DATA for: Official rating 96, 11 lb above field average; Has won at this trip or further
    DATA against: Poor recent finishing positions; Carries 11 lb more than average
- Ballycommon Chapel (hrs_28739095) | 8yo M | 145lb | OR 77 | draw 0 | jockey Sean O'Keeffe | trainer R Donohoe (14d 0/4) | headgear - | last run 448 days | form 4U087- | MARKET 1.8% | 09:00 median 34.00 | Matchbook 70.00
    comment: Ballycommon Chapel is yet to win in her last five starts, with a seventh last time out, an eighth before that, and a 448-day absence to shake off.
    DATA: model 3.8% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Carries 8 lb less than average
    DATA against: Official rating 77, 8 lb below field average; Returns from a 448-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Letters To Juliet (hrs_36426985) | 8yo M | 157lb | OR 89 | draw 0 | jockey Patrick M O'Brien(5) | trainer Patrick Downey (14d 0/0) | headgear ht | last run 27 days | form 570-08 | MARKET 1.6% | 09:00 median 41.00 | Matchbook 80.00
    comment: Letters To Juliet has been well beaten of late, an eighth last time out and winless in her last five, though she has run over today's trip and going before and returns after 27 days.
    DATA: model 3.4% | style Held up (led 5% of runs) | runs in data 2 | last 3: 19 Sep Navan Hurdle 15.8f Good 13/13; 23 Oct Sligo (IRE) Hurdle 17.5f Yielding 8/13
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Avandra (hrs_40393444) | 6yo M | 140lb | OR 72 | draw 0 | jockey Shane O'Callaghan(3) | trainer P. J. Rothwell (14d 0/24) | headgear b | last run 12 days | form 534070 | MARKET 1.5% | 09:00 median 41.00 | Matchbook 95.00
    comment: Avandra is winless in her last six, unplaced last time and only a seventh two starts back, with a third five runs ago her best finish.
    DATA: model 4.0% | style Midfield (led 5% of runs) | runs in data 11 | last 3: 26 Aug Bellewstown Hurdle 17.2f Good 10/15; 28 Sep Roscommon Hurdle 15.6f Good To Yielding 7/16; 7 Nov Gowran Park (IRE) Hurdle 20f Good To Yielding 11/14
    DATA for: Carries 13 lb less than average
    DATA against: Official rating 72, 13 lb below field average; Trainer 0 wins from 24 runs, last 14 days; Poor recent finishing positions
- Nugentstown Sue (hrs_46416363) | 7yo M | 146lb | OR 78 | draw 0 | jockey Conor Stone-Walsh | trainer Hugh Paul Finegan (14d 0/1) | headgear tb | last run 45 days | form 0500-P | MARKET 0.7% | 09:00 median 101.00 | Matchbook 220.00
    comment: Pulled up last time out and winless in her last five, with just a fifth four starts back to show, Nugentstown Sue is hard to fancy after 45 days off and carrying 146 lb.
    DATA: model 1.8% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 31 Aug Roscommon Flat 12.1f Good To Yielding 14/15; 5 Sep Navan Flat 10f Good 19/21; 5 Oct Fairyhouse Hurdle 16f Good PU/16
    DATA for: Carries 7 lb less than average
    DATA against: Official rating 78, 7 lb below field average; Poor recent finishing positions; Pulled up in 1 of its last 1 jumps runs
- Final Decision (hrs_32751229) | 7yo M | 158lb | OR 90 | draw 0 | jockey Tiernan Power Roche | trainer P. J. Rothwell (14d 0/24) | headgear p | last run 12 days | form F0/000 | MARKET 0.6% | 09:00 median 101.00 | Matchbook 200.00
    comment: Fit after just 12 days off, Final Decision has run over today's trip and on this going, though she's been unplaced in each of her last four outings after a fall five starts back.
    DATA: model 1.8% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 16 May Wexford Hurdle 17f Good To Yielding 13/14; 10 Aug Ballinrobe Hurdle 16.5f Good 14/14; 7 Nov Gowran Park (IRE) Hurdle 20f Good To Yielding 11/13
    DATA against: Trainer 0 wins from 24 runs, last 14 days; Poor recent finishing positions

## 3:30 Thurles | race_id rac_32304764375 | Sign Up To GavinLynchRacing.com (Q.R.) Maiden Hurdle
Hurdle |  | 1m7f169y | going Good | Turf | 12 runners | rating band - | age 4yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Legendary Status (hrs_17395569849) | 4yo G | 158lb | OR - | draw 0 | jockey Mr P. W. Mullins | trainer W. P. Mullins (14d 4/21) | headgear - | last run 242 days | form P2- | MARKET 66.3% | 09:00 median 1.22 | Matchbook 1.33
    DATA: model 5.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 242-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Marhaba Ghaiyyath (hrs_47065060) | 4yo G | 166lb | OR - | draw 0 | jockey Mr J L Gleeson | trainer John Joseph Hanlon (14d 0/12) | headgear - | last run 142 days | form /- | MARKET 15.3% | 09:00 median 4.00 | Matchbook 9.40
    DATA: model 13.4% | style Held up (led 5% of runs) | runs in data 4 | last 3: 21 Apr Pontefract Flat 10f Good 5/8; 2 May Newmarket Flat 9f Good To Firm 12/12; 30 Jun Musselburgh Flat 8.9f Good 8/9
    DATA against: Trainer 0 wins from 12 runs, last 14 days; Returns from a 142-day break; First run over hurdles in our data; Pace: steady gallop likely, hard to come from off the pace
- How Decc (hrs_29327123) | 8yo G | 158lb | OR 76 | draw 0 | jockey Miss H Heffernan(7) | trainer James Andrew Fahey (14d 0/6) | headgear - | last run 10 days | form 0/P-40 | MARKET 3.7% | 09:00 median 21.00 | Matchbook 30.00
    DATA: model 30.7% | style Held up (led 8% of runs) | runs in data 2 | last 3: 13 Oct Punchestown Hurdle 20f Good 4/17; 9 Nov Punchestown (IRE) Hurdle 20.5f Good To Yielding 13/22 fig 69
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Aged 8, older than most of this field; Pace: steady gallop likely, hard to come from off the pace
- Quinlan (hrs_17392710986) | 4yo G | 158lb | OR - | draw 0 | jockey Mr L P Shanahan(7) | trainer Ross O'Sullivan (14d 1/14) | headgear t (1st time) | last run 12 days | form U | MARKET 2.7% | 09:00 median 21.00 | Matchbook 60.00
    DATA: model 5.6% | style Unknown | runs in data 1 | last 3: 7 Nov Gowran Park (IRE) Hurdle 16f Good To Yielding UR/12
    DATA for: First-time headgear
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on; Fell or unseated in 1 of its last 1 jumps runs
- Hillview Lass (hrs_17394782384) | 6yo M | 151lb | OR - | draw 0 | jockey Mr B Leahy(7) | trainer Donncha Duggan (14d 0/2) | headgear - | last run 18 days | form PP42-0 | MARKET 2.3% | 09:00 median 26.00 | Matchbook 75.00
    DATA: model 3.6% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 1 Nov Cork (IRE) Hurdle 16f Good To Yielding 10/19
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Ruled By The Sun (hrs_63650132) | 5yo G | 158lb | OR 90 | draw 0 | jockey Mr L Hackett(7) | trainer Ray Hackett (14d 0/5) | headgear t | last run 24 days | form -7P047 | MARKET 1.9% | 09:00 median 41.00 | Matchbook 70.00
    DATA: model 8.8% | style Held up (led 3% of runs) | runs in data 6 | last 3: 4 Aug Roscommon Hurdle 20.2f Yielding To Soft 12/16; 11 Oct Cork Hurdle 20.5f Good 4/7; 26 Oct Galway (IRE) Hurdle 16.5f Soft To Heavy 7/10
    DATA against: Pulled up in 1 of its last 4 jumps runs; Pace: steady gallop likely, hard to come from off the pace
- Smithfield (hrs_55484443) | 4yo G | 158lb | OR - | draw 0 | jockey Mr J P Sampson(7) | trainer L Young (14d 0/1) | headgear h (1st time) | last run 35 days | form - | MARKET 1.8% | 09:00 median 34.00 | Matchbook 95.00
    DATA: model 10.4% | style Prominent (led 3% of runs) | runs in data 5 | last 3: 18 Jun Leopardstown Flat 8f Good To Firm 11/16; 3 Jul Bellewstown Flat 7.9f Good 9/15; 15 Oct Curragh (IRE) Flat 7f Soft 20/20
    DATA for: First-time headgear
    DATA against: Poor recent finishing positions; First run over hurdles in our data
- Mamoosh (hrs_17395570892) | 4yo F | 151lb | OR - | draw 0 | jockey Miss L Costello(7) | trainer E Seymour (14d 0/1) | headgear - | last run - days | form - | MARKET 1.7% | 09:00 median 51.00 | Matchbook 90.00
    DATA: model 5.0% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- The Mighty Mallard (hrs_17395571935) | 4yo G | 158lb | OR - | draw 0 | jockey Mr B M Coonan(7) | trainer Francis Casey (14d 0/0) | headgear - | last run - days | form - | MARKET 1.6% | 09:00 median 51.00 | Matchbook 100.00
    DATA: model 5.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Menez Are (hrs_17392714115) | 4yo G | 158lb | OR - | draw 0 | jockey Mr C K Whyte(7) | trainer Paul John Gilligan (14d 0/3) | headgear - | last run 24 days | form U5P-08 | MARKET 1.2% | 09:00 median 81.00 | Matchbook 140.00
    DATA: model 3.5% | style Held up (led 5% of runs) | runs in data 2 | last 3: 25 Sep Listowel Hurdle 18.6f Good To Yielding 11/15; 26 Oct Galway (IRE) Hurdle 16.5f Soft To Heavy 8/20
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Getaway Dreams (hrs_65068780) | 5yo M | 151lb | OR - | draw 0 | jockey Mr J Pratt(7) | trainer James Joseph Mangan (14d 0/0) | headgear - | last run 33 days | form 8 | MARKET 1.0% | 09:00 median 81.00 | Matchbook 200.00
    DATA: model 3.8% | style Held up (led 8% of runs) | runs in data 1 | last 3: 17 Oct Limerick (IRE) NH Flat 17f Good To Yielding 8/8
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- A Hug Or Two (hrs_17394378743) | 5yo G | 158lb | OR - | draw 0 | jockey Mr F Colleran(7) | trainer Richard James Daniels (14d 0/0) | headgear - | last run 24 days | form 0 | MARKET 0.6% | 09:00 median 151.00 | Matchbook 300.00
    DATA: model 4.2% | style Held up (led 8% of runs) | runs in data 1 | last 3: 26 Oct Galway (IRE) Hurdle 16.5f Soft To Heavy 17/20
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
