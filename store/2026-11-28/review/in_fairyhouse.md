# Card review packet: Fairyhouse, 2026-11-28

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
{"meeting": "fairyhouse", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 11:45 Fairyhouse | race_id rac_32305976937 | SIS Supporting Irish Racing Beginners Steeplechase
Chase |  | 2m5f55y | going Yielding | Turf | 13 runners | rating band - | age 4yo+
DATA pace: Strong pace - 6 habitual front-runners (He Can't Dance, Kiely's Place, King Rasko Grey, Robertjames, Spinningayarn, Narciso Has). A contested lead should set things up for horses coming from behind.
- King Rasko Grey (hrs_40553618) | 6yo G | 166lb | OR - | draw 0 | jockey Paul Townend | trainer W. P. Mullins (14d 16/53) | headgear - | last run 211 days | form /1311- | MARKET 38.4% | 09:00 median 2.20 | Matchbook 2.38
    DATA: model 14.8% | style Leader (led 29% of runs) | runs in data 3 | last 3: 1 Feb Leopardstown Hurdle 16f Heavy 3/12; 11 Mar Cheltenham Hurdle 21f Good 1/21; 1 May Punchestown Hurdle 20.6f Yielding 1/8
    DATA for: Trainer 30% wins (16/53), last 14 days; Last-run finishing speed +2.3% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Returns from a 211-day break; First run over fences in our data; Pace: likely to be taken on for the lead
- Narciso Has (hrs_52204565) | 4yo G | 157lb | OR - | draw 0 | jockey Harry Cobden | trainer W. P. Mullins (14d 16/53) | headgear - | last run 299 days | form 1/211- | MARKET 30.9% | 09:00 median 2.63 | Matchbook 3.05
    comment: Narciso Has won three of his last four starts, including last time out and two starts back, with a second three starts back in between, and he carries 157 lb with the yard in cracking form. The one real risk is a 299-day absence, so fitness is the question.
    DATA: model 14.4% | style Leader (led 57% of runs) | runs in data 1 | last 3: 2 Feb Leopardstown Hurdle 16f Heavy 1/7
    DATA for: Trainer 30% wins (16/53), last 14 days
    DATA against: Returns from a 299-day break; Lightly raced: 1 run in our data, so the model has little to go on; Pace: likely to be taken on for the lead
- Kiely's Place (hrs_48289654) | 6yo G | 166lb | OR - | draw 0 | jockey Danny Mullins | trainer W. P. Mullins (14d 16/53) | headgear - | last run 211 days | form 1/163- | MARKET 10.6% | 09:00 median 7.50 | Matchbook 9.00
    comment: Kiely's Place bounces in with a third last time out, a sixth two starts back, and back-to-back wins three and four starts back, while the yard is in cracking form at 16/53 in the last 14 days.
    DATA: model 7.1% | style Prominent (led 54% of runs) | runs in data 3 | last 3: 26 Feb Clonmel Hurdle 19.3f Heavy 1/16; 5 Apr Fairyhouse Hurdle 20f Yielding To Soft 6/11; 1 May Punchestown Hurdle 20.6f Yielding 3/8
    DATA for: Trainer 30% wins (16/53), last 14 days; Good recent finishing positions
    DATA against: Returns from a 211-day break; First run over fences in our data
- Spinningayarn (hrs_39699037) | 6yo G | 166lb | OR - | draw 0 | jockey Jack Kennedy | trainer Gordon Elliott (14d 6/65) | headgear - | last run 213 days | form 3115P- | MARKET 9.9% | 09:00 median 7.50 | Matchbook 9.80
    comment: Spinningayarn won twice in his last five starts, a winner three starts back and four starts back, but he was pulled up last time out and returns after 213 days off.
    DATA: model 7.2% | style Leader (led 43% of runs) | runs in data 4 | last 3: 26 Jan Punchestown Hurdle 19f Heavy 1/5; 13 Mar Cheltenham Hurdle 24f Good To Soft 5/22; 29 Apr Punchestown Hurdle 23.9f Yielding PU/14
    DATA against: Returns from a 213-day break; Pulled up in 1 of its last 4 jumps runs; First run over fences in our data; Pace: likely to be taken on for the lead
- Robertjames (hrs_62813079) | 5yo G | 166lb | OR - | draw 0 | jockey Sean O'Keeffe | trainer W. P. Mullins (14d 16/53) | headgear h | last run 244 days | form 1- | MARKET 2.8% | 09:00 median 23.00 | Matchbook 46.00
    comment: Winner last time out, Robertjames has run over today's trip and his yard is firing, but 244 days off is a long break and 166 lb is a big weight to carry.
    DATA: model 20.6% | style Leader (led 57% of runs) | runs in data 1 | last 3: 29 Mar Downpatrick Hurdle 21.8f Yielding To Soft 1/13
    DATA for: Trainer 30% wins (16/53), last 14 days; Last-run finishing speed +3.4% vs that field (finished strongly); Has won at this trip or further
    DATA against: Returns from a 244-day break; Lightly raced: 1 run in our data, so the model has little to go on; Pace: likely to be taken on for the lead
- He Can't Dance (hrs_39431644) | 6yo G | 166lb | OR - | draw 0 | jockey Danny Gilligan | trainer Gordon Elliott (14d 6/65) | headgear tp | last run 208 days | form 3321-1 | MARKET 2.3% | 09:00 median 26.00 | Matchbook 60.00
    comment: He Can't Dance arrives in cracking form, winning last time out and two starts back, with a second and two thirds before that, and he has run over today's trip and going.
    DATA: model 15.1% | style Leader (led 23% of runs) | runs in data 5 | last 3: 4 Apr Fairyhouse Hurdle 20f Yielding To Soft 2/25; 16 Apr Limerick Hurdle 24f Soft To Heavy 1/7; 4 May Down Royal Hurdle 24f Good 1/6
    DATA for: Last-run finishing speed +7.6% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Returns from a 208-day break; First run over fences in our data; Pace: likely to be taken on for the lead
- Zanndabad (hrs_25795245) | 7yo G | 166lb | OR - | draw 0 | jockey Daniel King | trainer A. J. Martin (14d 0/5) | headgear t | last run 29 days | form 2110-2 | MARKET 1.9% | 09:00 median 29.00 | Matchbook 80.00
    comment: Zanndabad arrives in solid form, second last time out and a winner three and four starts back, and he has run over today's trip and going, but a flat effort two runs ago and 166 lb on his back temper enthusiasm.
    DATA: model 3.3% | style Held up (led 4% of runs) | runs in data 6 | last 3: 21 Aug York Flat 11.9f Good To Soft 14/16; 27 Sep Curragh Flat 16.8f Heavy 22/30; 30 Oct Down Royal (IRE) Chase 20f Good 2/7 fig 124
    DATA for: Last-run finishing speed +3.5% vs that field (finished strongly); Pace: a contested lead should suit its hold-up style
- Sept Etoiles (hrs_49145089) | 5yo G | 166lb | OR - | draw 0 | jockey Sam Ewing | trainer Gordon Elliott (14d 6/65) | headgear - | last run 220 days | form 41613- | MARKET 1.5% | 09:00 median 41.00 | Matchbook 85.00
    comment: Sept Etoiles sets a solid standard, having finished third last time out, and a winner two starts back, with two wins in his last five and experience over today's trip and going. The one concern is a 220-day absence, plus 166 lb on his back.
    DATA: model 3.1% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 18 Jan Thurles Hurdle 22f Yielding 6/6; 4 Apr Fairyhouse Hurdle 23.8f Yielding To Soft 1/20; 22 Apr Perth Hurdle 23.9f Good 3/4
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Last-run finishing speed -3.0% vs that field (faded); Returns from a 220-day break; First run over fences in our data
- Rock On Richie (hrs_17394494516) | 6yo G | 166lb | OR - | draw 0 | jockey Conor Stone-Walsh | trainer Tom Dreaper (14d 0/1) | headgear - | last run 24 days | form 521-8 | MARKET 0.4% | 09:00 median 201.00 | Matchbook 360.00
    comment: Rock On Richie was last seen finishing eighth, which makes him hard to fancy, though he did win two starts back and was second three starts back.
    DATA: model 1.1% | style Unknown | runs in data 1 | last 3: 4 Nov Wexford (IRE) Chase 15.5f Yielding 8/9 fig 104
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Ready For Road (hrs_58133628) | 5yo G | 166lb | OR - | draw 0 | jockey Keith Donoghue | trainer Gavin Cromwell (14d 3/39) | headgear t | last run 256 days | form 4795P- | MARKET 0.3% | 09:00 median 201.00 | Matchbook 370.00
    comment: Ready For Road is hard to fancy: he was pulled up last time out, has been beaten in each of his last five starts, and returns after 256 days off.
    DATA: model 3.8% | style Held up (led 5% of runs) | runs in data 2 | last 3: 3 Feb Fairyhouse Hurdle 16f Soft To Heavy 5/12; 17 Mar Down Royal Hurdle 20.4f Good To Yielding PU/19
    DATA for: Pace: a contested lead should suit its hold-up style
    DATA against: Returns from a 256-day break; Lightly raced: 2 runs in our data, so the model has little to go on; Pulled up in 1 of its last 2 jumps runs; First run over fences in our data
- Sutherland (hrs_39996635) | 6yo G | 166lb | OR - | draw 0 | jockey Michael Kenneally(3) | trainer Gary McGill (14d 0/1) | headgear - | last run 14 days | form 3-6123 | MARKET 0.3% | 09:00 median 201.00 | Matchbook 520.00
    DATA: model 6.1% | style Held up (led 5% of runs) | runs in data 5 | last 3: 24 Mar Southwell Hurdle 20.4f Good 5/10; 18 Apr Bangor-on-Dee Hurdle 19.6f Good 3/7; 11 May Southwell Hurdle 20.4f Good 7/10
    DATA for: Pace: a contested lead should suit its hold-up style
    DATA against: Last-run finishing speed -9.3% vs that field (faded); Race comments mention jumping mistakes in 3 of its last 5 runs; First run over fences in our data
- I Can Find Em (hrs_59186372) | 5yo G | 166lb | OR - | draw 0 | jockey Alan O'Sullivan(5) | trainer Gary McGill (14d 0/1) | headgear - | last run 13 days | form 2-0960 | MARKET 0.2% | 09:00 median 201.00 | Matchbook 1000.00
    comment: I Can Find Em is hard to fancy, unplaced last time and a sixth and a ninth in the two runs before that, with a second five starts back the only bright spot in a winless recent spell.
    DATA: model 2.5% | style Held up (led 4% of runs) | runs in data 4 | last 3: 19 Sep Navan Hurdle 21f Good 9/15; 26 Sep Listowel Hurdle 20f Good 6/6; 15 Nov Navan (IRE) Hurdle 16f Good To Yielding 16/25
    DATA for: Pace: a contested lead should suit its hold-up style
    DATA against: Poor recent finishing positions; First run over fences in our data
- Maganey (hrs_17394493473) | 7yo G | 166lb | OR - | draw 0 | jockey Philip Donovan | trainer Seamus Neville (14d 0/1) | headgear - | last run 29 days | form PF1-17 | MARKET 0.2% | 09:00 median 201.00 | Matchbook 1000.00
    comment: Unexposed gelding who won two starts back and three starts back, before a seventh last time out 29 days ago; he has a fall and a pulled up in the book too, but looks open to improvement carrying 166 lb.
    DATA: model 1.0% | style Unknown | runs in data 1 | last 3: 30 Oct Down Royal (IRE) Chase 20f Good 7/7
    DATA against: Last-run finishing speed -6.4% vs that field (faded); Lightly raced: 1 run in our data, so the model has little to go on

## 12:20 Fairyhouse | race_id rac_32305978874 | Activ8 Solar Energies Irish EBF Mares Handicap Steeplechase
Chase |  | 2m4f0y | going Yielding | Turf | 8 runners | rating band - | age 4yo+
DATA pace: Even - Two likely leaders (Karamoja, The Great Nudie). A fair, even gallop is most likely.
- Katie Daniels (hrs_34961507) | 7yo M | 142lb | OR 112 | draw 0 | jockey Daniel King | trainer Cian Collins (14d 2/9) | headgear tp | last run 24 days | form 571P-4 | MARKET 17.4% | 09:00 median 5.00 | Matchbook 5.40 | CHECK (skip line 4.75)
    comment: Katie Daniels was a fourth last time out, but a pulled up two starts back and just one win in her last five, which came three starts back, leaves her hard to fancy.
    DATA: model 5.4% | style Prominent (led 5% of runs) | runs in data 5 | last 3: 5 Apr Fairyhouse Hurdle 20f Yielding To Soft 1/20; 29 Apr Punchestown Hurdle 19.3f Yielding PU/24; 4 Nov Wexford (IRE) Chase 23f Yielding 4/4
    DATA for: Trainer 22% wins (2/9), last 14 days; Has won at this trip or further; Carries 13 lb less than average
    DATA against: Official rating 112, 12 lb below field average; Last-run finishing speed -2.1% vs that field (faded); Pulled up in 1 of its last 5 jumps runs
- Karia Des Blaises (hrs_35107317) | 6yo M | 163lb | OR 133 | draw 0 | jockey Paul Townend | trainer W. P. Mullins (14d 16/53) | headgear - | last run 213 days | form /F1P9- | MARKET 16.8% | 09:00 median 5.00 | Matchbook 5.70
    comment: The risk is a 213-day absence, following a ninth last time out and a pulled up before that.
    DATA: model 11.8% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 19 Feb Thurles Chase 21.6f Soft To Heavy 1/6; 6 Apr Fairyhouse Chase 29.1f Yielding To Soft PU/30; 29 Apr Punchestown Chase 20.4f Yielding 9/14
    DATA for: Official rating 133, 8 lb above field average; Trainer 30% wins (16/53), last 14 days; Has won at this trip or further
    DATA against: Last-run finishing speed -6.9% vs that field (faded); Carries 8 lb more than average; Returns from a 213-day break; Pulled up in 1 of its last 3 jumps runs
- The Great Nudie (hrs_41378631) | 6yo M | 153lb | OR 123 | draw 0 | jockey Sean O'Keeffe | trainer Colin Bowe (14d 0/0) | headgear - | last run 34 days | form 1433-9 | MARKET 16.5% | 09:00 median 5.00 | Matchbook 5.90
    comment: Two thirds in her last four starts show she can get involved, and she has run over today's trip and going, but a ninth last time out and 34 days off leave questions.
    DATA: model 13.4% | style Leader (led 63% of runs) | runs in data 5 | last 3: 19 Feb Thurles Chase 21.6f Soft To Heavy 3/6; 14 Apr Clonmel Chase 20f Yielding 3/6; 25 Oct Wexford (IRE) Chase 19.5f Soft 9/10 fig 105
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Best recent form figure 105, 9 lb below field average; Recent figures 18 lb below its current mark (looks high in the weights)
- Karamoja (hrs_37276253) | 6yo M | 162lb | OR 132 | draw 0 | jockey Danny Mullins | trainer W. P. Mullins (14d 16/53) | headgear t | last run 211 days | form 6714F- | MARKET 15.4% | 09:00 median 5.50 | Matchbook 6.20
    comment: Karamoja won three starts back and was a fourth two outings ago, so she has a winning edge in her recent form, and she has run over today's trip before. The main risk is a 211-day absence plus a fall last time out, though the yard's 16/53 run helps.
    DATA: model 15.7% | style Leader (led 23% of runs) | runs in data 4 | last 3: 5 Mar Thurles Chase 18.1f Soft 1/9; 5 Apr Fairyhouse Chase 16.6f Yielding To Soft 4/12; 1 May Punchestown Chase 20.2f Yielding F/22
    DATA for: Official rating 132, 8 lb above field average; Trainer 30% wins (16/53), last 14 days
    DATA against: Carries 7 lb more than average; Returns from a 211-day break; Fell or unseated in 1 of its last 4 jumps runs
- Ballybawn Belter (hrs_29212855) | 8yo M | 157lb | OR 127 | draw 0 | jockey Harry Cobden | trainer Liz Doyle (14d 0/3) | headgear - | last run 20 days | form 763-P0 | MARKET 12.3% | 09:00 median 7.00 | Matchbook 7.80
    comment: The risk is a winless recent spell, including a pulled up two starts back and an unplaced run last time, under 157 lb.
    DATA: model 16.5% | style Held up (led 4% of runs) | runs in data 8 | last 3: 21 Sep Listowel Flat 12f Yielding 6/11; 5 Oct Killarney Flat 11.2f Soft 1/7; 8 Nov Naas (IRE) Hurdle 20f Good To Yielding 13/20 fig 113
    DATA against: Recent figures 14 lb below its current mark (looks high in the weights); Race comments mention jumping mistakes in 2 of its last 5 runs; Pulled up in 1 of its last 5 jumps runs
- Qualimita (hrs_35054649) | 7yo M | 158lb | OR 128 | draw 0 | jockey Jack Kennedy | trainer Gordon Elliott (14d 6/65) | headgear t | last run 370 days | form F/223- | MARKET 10.2% | 09:00 median 7.50 | Matchbook 10.00
    comment: Qualimita is yet to win in her last four but has been consistent, third last time out and second on the two runs before that, and she has experience of today's trip and going.
    DATA: model 10.6% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 370-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Break My Soul (hrs_34253212) | 7yo M | 166lb | OR 136 | draw 0 | jockey Keith Donoghue | trainer Ian Patrick Donoghue (14d 0/9) | headgear ht | last run 21 days | form 23P-25 | MARKET 7.2% | 09:00 median 12.00 | Matchbook 13.50
    comment: Break My Soul has been in the frame in three of her last five, including a second two starts back, and she has run over today's trip and going before.
    DATA: model 17.3% | style Held up (led 4% of runs) | runs in data 5 | last 3: 5 Apr Fairyhouse Chase 16.6f Yielding To Soft PU/12; 9 May Killarney Hurdle 17f Good To Yielding 2/9; 7 Nov Gowran Park (IRE) Chase 16f Good 5/7 fig 124
    DATA for: Best recent form figure 124, 10 lb above field average; Official rating 136, 12 lb above field average
    DATA against: Recent figures 12 lb below its current mark (looks high in the weights); Trainer 0 wins from 9 runs, last 14 days; Carries 11 lb more than average; Race comments mention jumping mistakes in 2 of its last 5 runs; Pulled up in 1 of its last 5 jumps runs
- Sophia Rose (hrs_51650102) | 7yo M | 140lb | OR 105 | draw 0 | jockey Conor Stone-Walsh | trainer Gavin Cromwell (14d 3/39) | headgear - | last run 151 days | form P65-28 | MARKET 4.3% | 09:00 median 19.00 | Matchbook 23.00
    comment: Winless in her last five and beaten into eighth last time, Sophia Rose is hard to fancy after 151 days off, though a second two starts back and previous experience over today's trip and going count for something, and she carries 140 lb.
    DATA: model 9.3% | style Midfield (led 3% of runs) | runs in data 6 | last 3: 1 May Punchestown Chase 20.2f Yielding 5/5; 11 May Killarney Chase 20.5f Good To Yielding 2/14; 30 Jun Wexford Chase 19.5f Good 8/14
    DATA for: Carries 15 lb less than average
    DATA against: Official rating 105, 20 lb below field average; Returns from a 151-day break; Pulled up in 1 of its last 5 jumps runs

## 12:55 Fairyhouse | race_id rac_32305980811 | EASYFIX Equine Handicap Steeplechase (Listed)
Chase | Class 1 | 2m1f0y | going Yielding | Turf | 11 runners | rating band - | age 4yo+
DATA pace: Lone leader - Raffles Dolce Vita is the only habitual front-runner and may be allowed an easy lead.
- Western Diego (hrs_28517419) | 9yo G | 155lb | OR 135 | draw 0 | jockey Paul Townend | trainer W. P. Mullins (14d 16/53) | headgear h | last run 212 days | form 314F0- | MARKET 18.2% | 09:00 median 4.50 | Matchbook 5.10 | CHECK (skip line 4.27)
    comment: The risk is a 212-day absence after an unplaced run and a fall.
    DATA: model 5.7% | style Held up (led 3% of runs) | runs in data 4 | last 3: 2 Feb Leopardstown Chase 17f Heavy 4/14; 11 Mar Cheltenham Chase 15.9f Good F/20; 30 Apr Punchestown Chase 16.3f Yielding 14/20
    DATA for: Trainer 30% wins (16/53), last 14 days; Has won at this trip or further
    DATA against: Last-run finishing speed -7.2% vs that field (faded); Returns from a 212-day break; Fell or unseated in 1 of its last 4 jumps runs
- Raffles Dolce Vita (hrs_40605824) | 5yo G | 153lb | OR 133 | draw 0 | jockey J. J. Slevin | trainer Thomas Gibney (14d 0/3) | headgear - | last run 212 days | form 64716- | MARKET 15.8% | 09:00 median 5.50 | Matchbook 5.70
    comment: Raffles Dolce Vita was sixth last time out and returns from 212 days off, and a winner two starts back is his only bright spot in a patchy recent run.
    DATA: model 10.0% | style Leader (led 29% of runs) | runs in data 3 | last 3: 22 Jan Gowran Park Chase 20f Heavy 7/9; 3 Mar Leopardstown Chase 17f Yielding 1/6; 30 Apr Punchestown Chase 16.3f Yielding 6/20
    DATA for: Has won at this trip or further; Pace: may get an uncontested lead
    DATA against: Returns from a 212-day break
- Coral River (hrs_39296397) | 7yo G | 150lb | OR 130 | draw 0 | jockey Donagh Meyler | trainer Ross O'Sullivan (14d 1/20) | headgear - | last run 33 days | form 2219-4 | MARKET 11.3% | 09:00 median 7.50 | Matchbook 8.40
    comment: Fourth last time out and a ninth the run before leave Coral River hard to fancy, with the yard just 1 from 20 lately, though he has run over today's trip and going and won three starts back.
    DATA: model 8.7% | style Prominent (led 3% of runs) | runs in data 4 | last 3: 14 Apr Clonmel Chase 20f Yielding 1/6; 30 Apr Punchestown Chase 16.3f Yielding 9/20; 26 Oct Galway (IRE) Chase 18f Heavy 4/7 fig 124
    DATA for: Has won at this trip or further
    DATA against: Recent figures 6 lb below its current mark (looks high in the weights)
- Birdie Or Bust (hrs_33096763) | 8yo M | 151lb | OR 131 | draw 0 | jockey Harry Cobden | trainer Henry de Bromhead (14d 6/36) | headgear t | last run 48 days | form 9P-341 | MARKET 10.3% | 09:00 median 7.50 | Matchbook 9.80
    comment: Winner last time out, and a fourth two starts back, Birdie Or Bust has run over today's trip and going before, but 48 days off and 151 lb are hurdles to overcome.
    DATA: model 11.1% | style Prominent (led 3% of runs) | runs in data 5 | last 3: 6 Jun Punchestown Chase 16.2f Good To Yielding 3/10; 16 Jul Killarney Hurdle 20.4f Good 4/6; 11 Oct Cork Chase 17.6f Good 1/8
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Pulled up in 1 of its last 5 jumps runs
- Jazzy Matty (hrs_32290664) | 7yo G | 165lb | OR 145 | draw 0 | jockey Danny Gilligan | trainer Cian Collins (14d 2/9) | headgear - | last run 98 days | form 5625-6 | MARKET 9.2% | 09:00 median 8.00 | Matchbook 11.50
    comment: The risk is a 98-day absence, with a sixth last time out and 165 lb to carry.
    DATA: model 15.1% | style Midfield (led 3% of runs) | runs in data 4 | last 3: 11 Mar Cheltenham Chase 15.9f Good 2/20; 10 Apr Aintree Hurdle 20f Good To Soft 5/22; 22 Aug Killarney Hurdle 22.4f Good 6/14
    DATA for: Official rating 145, 12 lb above field average; Trainer 22% wins (2/9), last 14 days
    DATA against: Carries 12 lb more than average; Returns from a 98-day break
- Manoir de Mirande (hrs_58411192) | 4yo G | 140lb | OR 125 | draw 0 | jockey Josh Williamson(3) | trainer Gordon Elliott (14d 6/65) | headgear t | last run 29 days | form 123F14 | MARKET 9.1% | 09:00 median 9.00 | Matchbook 10.50
    comment: Carrying 140 lb after 29 days off, he looks up against it.
    DATA: model 8.8% | style Prominent (led 3% of runs) | runs in data 13 | last 3: 4 Sep Kilbeggan Chase 20.4f Good To Yielding F/9; 10 Oct Fairyhouse Chase 16.5f Good 1/6; 30 Oct Down Royal (IRE) Chase 16.5f Good To Yielding 4/9 fig 125
    DATA for: Has won at this trip or further; Carries 13 lb less than average
    DATA against: Official rating 125, 8 lb below field average; Fell or unseated in 1 of its last 5 jumps runs
- Moudan (hrs_39208106) | 7yo G | 159lb | OR 139 | draw 0 | jockey Eoghan Finegan(5) | trainer Ciaran Murphy (14d 0/7) | headgear - | last run 224 days | form 95121- | MARKET 8.5% | 09:00 median 9.00 | Matchbook 12.50
    comment: Moudan won last time out and was a second two starts back, a winner three starts back too, but he returns after 224 days off and carries 159 lb.
    DATA: model 14.3% | style Prominent (led 23% of runs) | runs in data 6 | last 3: 21 Mar Navan Chase 17f Soft To Heavy 1/9; 5 Apr Fairyhouse Chase 16.6f Yielding To Soft 2/12; 18 Apr Ayr Chase 16.5f Heavy 1/7
    DATA for: Official rating 139, 6 lb above field average; Last-run finishing speed +4.8% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Carries 6 lb more than average; Returns from a 224-day break
- Springt De La Mare (hrs_34571397) | 7yo G | 153lb | OR 133 | draw 0 | jockey Conor Stone-Walsh | trainer Gavin Cromwell (14d 3/39) | headgear t | last run 587 days | form 31168/ | MARKET 4.8% | 09:00 median 19.00 | Matchbook 22.00
    comment: Springt De La Mare won three and four starts back but has slipped to a sixth two starts back and an eighth last time out, and a 587-day absence is a big question for fitness.
    DATA: model 6.9% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 587-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Drumgill (hrs_37774534) | 7yo G | 140lb | OR 116 | draw 0 | jockey Daniel King | trainer John Patrick Ryan (14d 0/8) | headgear - | last run 21 days | form 450U62 | MARKET 4.7% | 09:00 median 17.00 | Matchbook 20.00
    comment: A second last time out, 21 days ago, and experience of today's trip and going give him some respectability.
    DATA: model 5.6% | style Midfield (led 4% of runs) | runs in data 16 | last 3: 3 Oct Gowran Park Chase 20f Good To Yielding UR/6; 11 Oct Cork Chase 17.6f Good 6/8; 7 Nov Gowran Park (IRE) Chase 16f Good 2/7 fig 121
    DATA for: Recent figures 5 lb above its current mark (looks well handicapped); Carries 13 lb less than average
    DATA against: Official rating 116, 17 lb below field average; Trainer 0 wins from 8 runs, last 14 days; Fell or unseated in 1 of its last 5 jumps runs
- Dee Capo (hrs_34598060) | 7yo G | 166lb | OR 146 | draw 0 | jockey Sam Ewing | trainer Gordon Elliott (14d 6/65) | headgear - | last run 213 days | form U402P- | MARKET 4.5% | 09:00 median 17.00 | Matchbook 23.00
    DATA: model 9.9% | style Held up (led 3% of runs) | runs in data 4 | last 3: 10 Mar Cheltenham Chase 20.2f Good To Soft 14/23; 2 Apr Clonmel Chase 20f Soft 2/5; 29 Apr Punchestown Chase 20.4f Yielding PU/14
    DATA for: Official rating 146, 13 lb above field average
    DATA against: Carries 13 lb more than average; Returns from a 213-day break; Race comments mention jumping mistakes in 2 of its last 4 runs; Pulled up in 1 of its last 4 jumps runs
- The King Of Prs (hrs_29341473) | 8yo G | 149lb | OR 129 | draw 0 | jockey Patrick M O'Brien(5) | trainer Gavin Cromwell (14d 3/39) | headgear t | last run 212 days | form 947FP- | MARKET 3.6% | 09:00 median 23.00 | Matchbook 27.00
    DATA: model 3.9% | style Held up (led 3% of runs) | runs in data 4 | last 3: 14 Feb Gowran Park Hurdle 20.2f Heavy 7/14; 10 Apr Aintree Chase 21.1f Good To Soft F/27; 30 Apr Punchestown Chase 16.3f Yielding PU/20
    DATA against: Poor recent finishing positions; Returns from a 212-day break; Fell or unseated in 1 of its last 4 jumps runs; Pulled up in 1 of its last 4 jumps runs

## 1:30 Fairyhouse | race_id rac_32305982748 | Mullinam Hurdle (Grade 3)
Hurdle | Class 1 | 2m0f0y | going Yielding | Turf | 4 runners | rating band - | age 4yo
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Saratoga (hrs_42781095) | 4yo G | 166lb | OR 146 | draw 0 | jockey Harry Cobden | trainer Padraig Roche (14d 0/6) | headgear - | last run 210 days | form 33211- | MARKET 37.2% | 09:00 median 2.50 | Matchbook 2.62
    comment: Won last time out and again two starts back, with a second and two thirds before that, so Saratoga arrives in cracking form and has run over today's trip and going. The one concern is a 210-day layoff, and he carries 166 lb.
    DATA: model 38.1% | style Prominent (led 3% of runs) | runs in data 4 | last 3: 7 Feb Naas Hurdle 15.7f Soft To Heavy 2/5; 10 Mar Cheltenham Hurdle 16.4f Good To Soft 1/22; 2 May Punchestown Hurdle 16f Yielding 1/12
    DATA for: Official rating 146, 9 lb above field average; Last-run finishing speed +3.3% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Returns from a 210-day break
- Bartholomew (hrs_56127659) | 4yo G | 153lb | OR 141 | draw 0 | jockey Ricky Doyle | trainer Martin Brassil (14d 1/6) | headgear t | last run 20 days | form 412-2 | MARKET 27.6% | 09:00 median 3.25 | Matchbook 3.65
    comment: Bartholomew has finished second in each of his last two outings, and a winner three starts back, so he arrives in grand heart after 20 days off, having run over today's trip and going before.
    DATA: model 22.5% | style Prominent (led 3% of runs) | runs in data 4 | last 3: 2 May Punchestown Hurdle 16f Yielding 2/12; 1 Sep Gowran Park Flat 14f Yielding 7/13; 8 Nov Naas (IRE) Hurdle 16f Good To Yielding 2/4 fig 120
    DATA for: Best recent form figure 120, 4 lb above field average; Has won at this trip or further; Good recent finishing positions
- Huntin Boots (hrs_60343444) | 4yo G | 153lb | OR - | draw 0 | jockey Jack Kennedy | trainer Gordon Elliott (14d 6/65) | headgear - | last run 21 days | form 25-R1 | MARKET 26.0% | 09:00 median 3.50 | Matchbook 3.85
    comment: Huntin Boots arrives a last-time-out winner after 21 days off, with a second four starts back and experience over today's trip and going, making him a serious threat under 153 lb. The main risk is the refusal two starts back, which raises a question over his reliability.
    DATA: model 18.8% | style Prominent (led 4% of runs) | runs in data 4 | last 3: 28 Apr Punchestown NH Flat 16.6f Yielding 5/19; 25 Oct Wexford (IRE) Hurdle 20.5f Soft REF/11; 7 Nov Gowran Park (IRE) Hurdle 16f Good To Yielding 1/12 fig 111
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 111, 5 lb below field average
- Ole Ole (hrs_58195508) | 4yo G | 157lb | OR 125 | draw 0 | jockey Keith Donoghue | trainer Gavin Cromwell (14d 3/39) | headgear - | last run 34 days | form 2F1-81 | MARKET 9.2% | 09:00 median 10.00 | Matchbook 11.00
    DATA: model 20.7% | style Midfield (led 4% of runs) | runs in data 5 | last 3: 29 Aug Curragh Flat 12f Yielding 7/19; 24 Sep Listowel Hurdle 16f Good 8/13; 25 Oct Galway (IRE) Hurdle 20.5f Soft 1/5 fig 116
    DATA for: Has won at this trip or further
    DATA against: Official rating 125, 12 lb below field average; Race comments mention jumping mistakes in 2 of its last 4 runs; Fell or unseated in 1 of its last 4 jumps runs

## 2:05 Fairyhouse | race_id rac_32305984685 | Close Brothers Rated Novice Hurdle
Hurdle |  | 2m4f0y | going Yielding | Turf | 8 runners | rating band - | age 4yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Marco Du Seuil (hrs_64554910) | 4yo G | 159lb | OR 122 | draw 0 | jockey Jack Kennedy | trainer Gordon Elliott (14d 6/65) | headgear - | last run 27 days | form 1-231 | MARKET 29.9% | 09:00 median 2.88 | Matchbook 3.15
    DATA: model 29.3% | style Prominent (led 4% of runs) | runs in data 3 | last 3: 26 May Ballinrobe Hurdle 16.1f Good 2/15; 17 Oct Limerick (IRE) Hurdle 17f Yielding 3/16 fig 109; 1 Nov Cork (IRE) Hurdle 16f Good To Yielding 1/10 fig 115
    DATA for: Good recent finishing positions
- If You Believe (hrs_50667134) | 5yo G | 163lb | OR - | draw 0 | jockey Keith Donoghue | trainer Gavin Cromwell (14d 3/39) | headgear - | last run 33 days | form 10/4-1 | MARKET 26.0% | 09:00 median 3.25 | Matchbook 3.70
    DATA: model 11.2% | style Unknown | runs in data 1 | last 3: 26 Oct Galway (IRE) Hurdle 16.5f Soft To Heavy 1/10 fig 119
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Lureka du Noyer (hrs_52741374) | 5yo G | 158lb | OR 120 | draw 0 | jockey Daniel King | trainer Henry de Bromhead (14d 6/36) | headgear t | last run 107 days | form 48-121 | MARKET 18.1% | 09:00 median 5.00 | Matchbook 5.10
    DATA: model 20.6% | style Prominent (led 5% of runs) | runs in data 3 | last 3: 28 May Limerick Hurdle 16f Soft 1/18; 21 Jul Ballinrobe Hurdle 17.4f Good 2/5; 13 Aug Tramore Hurdle 20.5f Good 1/7
    DATA for: Last-run finishing speed +2.2% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Returns from a 107-day break
- Martymill (hrs_59186106) | 5yo G | 153lb | OR - | draw 0 | jockey James Smith(3) | trainer A. McCann (14d 0/8) | headgear p | last run 48 days | form 626131 | MARKET 9.7% | 09:00 median 9.00 | Matchbook 10.00
    DATA: model 10.8% | style Midfield (led 4% of runs) | runs in data 7 | last 3: 9 Aug Downpatrick NH Flat 18.8f Good 1/6; 15 Sep Uttoxeter Hurdle 19.9f Good 3/9; 11 Oct Cork Hurdle 20.5f Good 1/7
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Trainer 0 wins from 8 runs, last 14 days
- Joe Cool (hrs_51373623) | 4yo G | 167lb | OR - | draw 0 | jockey Donagh Meyler | trainer Noel Meade (14d 2/13) | headgear - | last run 14 days | form 13 | MARKET 8.1% | 09:00 median 10.00 | Matchbook 12.50
    DATA: model 8.7% | style Midfield (led 4% of runs) | runs in data 9 | last 3: 5 Oct Killarney Flat 11.2f Soft 2/7; 1 Nov Curragh (IRE) Flat 12f Yielding 2/19 fig 76; 14 Nov Navan (IRE) Hurdle 16f Good To Yielding 3/8 fig 114
    DATA for: Good recent finishing positions
    DATA against: Best recent form figure 114, 4 lb below field average
- El Bilo (hrs_17392983209) | 4yo G | 157lb | OR - | draw 0 | jockey Sean O'Keeffe | trainer Paul Nolan (14d 2/12) | headgear - | last run 34 days | form 81 | MARKET 3.7% | 09:00 median 19.00 | Matchbook 32.00
    DATA: model 2.7% | style Held up (led 8% of runs) | runs in data 2 | last 3: 14 Oct Punchestown (IRE) NH Flat 16.5f Good 8/11 fig 87; 25 Oct Wexford (IRE) Hurdle 20.5f Soft 1/11 fig 126
    DATA for: Best recent form figure 126, 8 lb above field average; Has won at this trip or further
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Puma's Dream (hrs_58811340) | 5yo G | 157lb | OR 119 | draw 0 | jockey Sam Ewing | trainer Gordon Elliott (14d 6/65) | headgear - | last run 254 days | form 7410- | MARKET 2.8% | 09:00 median 23.00 | Matchbook 55.00
    DATA: model 10.3% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 5 Feb Thurles Hurdle 20.4f Soft 1/14; 19 Mar Cork Hurdle 24.2f Yielding 10/10
    DATA for: Has won at this trip or further
    DATA against: Last-run finishing speed -14.9% vs that field (faded); Returns from a 254-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- Taras Halls (hrs_33479866) | 8yo G | 153lb | OR 112 | draw 0 | jockey J. J. Slevin | trainer Ms Claire O'Connell (14d 1/9) | headgear p | last run 287 days | form 1P2P4- | MARKET 1.7% | 09:00 median 41.00 | Matchbook 85.00
    DATA: model 6.4% | style Prominent (led 8% of runs) | runs in data 2 | last 3: 20 Jan Leicester Chase 22.7f Heavy PU/7; 14 Feb Haydock Chase 19.9f Good To Soft 4/11
    DATA against: Official rating 112, 6 lb below field average; Returns from a 287-day break; Lightly raced: 2 runs in our data, so the model has little to go on; Pulled up in 1 of its last 2 jumps runs; First run over hurdles in our data; Aged 8, older than most of this field

## 2:40 Fairyhouse | race_id rac_32305986622 | Kettles Country House Hotel Maiden Hurdle
Hurdle |  | 2m0f0y | going Yielding | Turf | 26 runners | rating band - | age 4yo+
DATA pace: Lone leader - Colossal Impact is the only habitual front-runner and may be allowed an easy lead.
- Green Hint (hrs_50906163) | 5yo G | 166lb | OR - | draw 0 | jockey Paul Townend | trainer W. P. Mullins (14d 16/53) | headgear - | last run 69 days | form 12/2-1 | MARKET 35.3% | 09:00 median 1.80 | Matchbook 1.87
    DATA: model 14.1% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 3 Feb Fairyhouse NH Flat 16f Soft To Heavy 2/7; 20 Sep Listowel NH Flat 16f Good 1/13
    DATA for: Trainer 30% wins (16/53), last 14 days; Last-run finishing speed +9.0% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; First run over hurdles in our data
- Premier Division (hrs_59186134) | 5yo G | 166lb | OR - | draw 0 | jockey Jack Kennedy | trainer Gordon Elliott (14d 6/65) | headgear - | last run 29 days | form 332-1 | MARKET 23.1% | 09:00 median 2.75 | Matchbook 3.15
    DATA: model 12.4% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 1 May Punchestown NH Flat 18.8f Yielding 2/21; 30 Oct Down Royal (IRE) NH Flat 17f Good To Yielding 1/8 fig 105
    DATA for: Best recent form figure 105, 13 lb above field average; Last-run finishing speed +2.1% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; First run over hurdles in our data
- Hamavi (hrs_40959261) | 5yo G | 166lb | OR - | draw 0 | jockey Keith Donoghue | trainer Gavin Cromwell (14d 3/39) | headgear - | last run 157 days | form - | MARKET 7.3% | 09:00 median 9.00 | Matchbook 11.00
    DATA: model 2.6% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 157-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Bold Script (hrs_17395850416) | 5yo G | 166lb | OR - | draw 0 | jockey Danny Gilligan | trainer Gordon Elliott (14d 6/65) | headgear - | last run 244 days | form 2- | MARKET 4.5% | 09:00 median 15.00 | Matchbook 17.00
    DATA: model 2.6% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 244-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- My Fault Again (hrs_17395465549) | 5yo G | 166lb | OR - | draw 0 | jockey Mike O'Connor | trainer Henry de Bromhead (14d 6/36) | headgear - | last run - days | form - | MARKET 3.4% | 09:00 median 19.00 | Matchbook 27.00
    DATA: model 2.6% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Cristal Clere (hrs_20663755) | 8yo G | 166lb | OR - | draw 0 | jockey Alan O'Sullivan(5) | trainer John Nallen (14d 0/0) | headgear - | last run 27 days | form 4/ | MARKET 2.8% | 09:00 median 24.00 | Matchbook 29.00
    DATA: model 2.8% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 22 Sep Listowel Flat 8f Yielding 5/11; 4 Oct Curragh Flat 9f Yielding 8/10; 1 Nov Curragh (IRE) Flat 8f Yielding To Soft 14/21 fig 87
    DATA against: First run over hurdles in our data; Aged 8, older than most of this field
- Wilton Mills Trier (hrs_59429349) | 6yo M | 159lb | OR - | draw 0 | jockey Conor Stone-Walsh | trainer Paul Martin Pierce (14d 0/0) | headgear - | last run 205 days | form 13-1 | MARKET 2.7% | 09:00 median 23.00 | Matchbook 30.00
    DATA: model 9.2% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 6 Apr Cork NH Flat 16f Yielding 3/8; 7 May Wexford NH Flat 17f Good To Yielding 1/10
    DATA for: Last-run finishing speed +3.5% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Returns from a 205-day break; Lightly raced: 2 runs in our data, so the model has little to go on; First run over hurdles in our data
- Treasure Memory (hrs_49974337) | 6yo G | 166lb | OR 110 | draw 0 | jockey Daniel King | trainer A. J. Martin (14d 0/5) | headgear - | last run 238 days | form /233P- | MARKET 2.2% | 09:00 median 29.00 | Matchbook 40.00
    DATA: model 12.2% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 1 Jan Fairyhouse Hurdle 20f Yielding 3/18; 4 Apr Fairyhouse Hurdle 20f Yielding To Soft PU/25
    DATA against: Returns from a 238-day break; Lightly raced: 2 runs in our data, so the model has little to go on; Pulled up in 1 of its last 2 jumps runs
- Clean As A Whistle (hrs_17395853545) | 4yo G | 166lb | OR - | draw 0 | jockey Harry Cobden | trainer J Motherway (14d 0/2) | headgear - | last run 280 days | form P- | MARKET 1.7% | 09:00 median 41.00 | Matchbook 65.00
    DATA: model 2.6% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 280-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Holly's Thunder (hrs_63776202) | 5yo M | 159lb | OR - | draw 0 | jockey John Shinnick | trainer Mrs Lorna Fowler (14d 0/0) | headgear - | last run 34 days | form 3-6 | MARKET 1.7% | 09:00 median 41.00 | Matchbook 55.00
    DATA: model 2.8% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 1 May Punchestown NH Flat 18.8f Yielding 3/21; 25 Oct Galway (IRE) Hurdle 16f Soft 6/8 fig 96
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Tatum (hrs_35650153) | 5yo M | 159lb | OR - | draw 0 | jockey Donagh Meyler | trainer Noel Meade (14d 2/13) | headgear - | last run 51 days | form /- | MARKET 1.5% | 09:00 median 51.00 | Matchbook 70.00
    DATA: model 3.3% | style Prominent (led 3% of runs) | runs in data 7 | last 3: 31 Jul Galway Flat 14.1f Yielding To Soft 15/18; 28 Sep Down Royal Flat 12.9f Good To Yielding 10/10; 8 Oct Thurles Flat 16.6f Yielding To Soft 5/13
    DATA against: First run over hurdles in our data
- The Farmers Bar (hrs_63586712) | 4yo G | 166lb | OR - | draw 0 | jockey E Walsh | trainer Cian Collins (14d 2/9) | headgear - | last run 24 days | form 3-784 | MARKET 1.4% | 09:00 median 51.00 | Matchbook 85.00
    DATA: model 5.9% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 7 May Wexford NH Flat 17f Good To Yielding 7/8; 2 Oct Gowran Park Hurdle 20.2f Good 8/17; 4 Nov Wexford (IRE) Hurdle 16.5f Yielding 4/14 fig 99
    DATA for: Best recent form figure 99, 7 lb above field average; Trainer 22% wins (2/9), last 14 days; Last-run finishing speed +2.7% vs that field (finished strongly)
- Confidence Within (hrs_17389779113) | 5yo G | 166lb | OR - | draw 0 | jockey Tiernan Power Roche | trainer P. J. Rothwell (14d 0/32) | headgear - | last run 14 days | form 3-130 | MARKET 1.4% | 09:00 median 67.00 | Matchbook 55.00
    DATA: model 5.8% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 8 Aug Kilbeggan NH Flat 16f Good 1/6; 25 Sep Listowel Hurdle 18.6f Good To Yielding 3/15; 14 Nov Navan (IRE) Hurdle 20f Good To Yielding 16/22
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Trainer 0 wins from 32 runs, last 14 days; Last-run finishing speed -2.9% vs that field (faded)
- Game Shadow (hrs_65224880) | 4yo G | 166lb | OR - | draw 0 | jockey Alex Harvey | trainer John McConnell (14d 0/18) | headgear - | last run 34 days | form 4130 | MARKET 1.4% | 09:00 median 67.00 | Matchbook 60.00
    DATA: model 1.9% | style Midfield (led 23% of runs) | runs in data 4 | last 3: 15 Aug Perth NH Flat 16.2f Good 1/4; 26 Sep Listowel NH Flat 16f Good 3/6; 25 Oct Wexford (IRE) Hurdle 17f Soft 11/13
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Trainer 0 wins from 18 runs, last 14 days
- Affiniseaandbeyond (hrs_17395219401) | 5yo M | 159lb | OR - | draw 0 | jockey Phillip Enright | trainer Eoin Doyle (14d 2/2) | headgear - | last run 19 days | form P2-4 | MARKET 1.3% | 09:00 median 67.00 | Matchbook 75.00
    DATA: model 1.2% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 9 Nov Punchestown (IRE) Hurdle 20.5f Good To Yielding 4/11 fig 91
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Colossal Impact (hrs_51185855) | 5yo G | 166lb | OR - | draw 0 | jockey Shane O'Callaghan(3) | trainer P. J. Rothwell (14d 0/32) | headgear - | last run 11 days | form 3-446 | MARKET 1.3% | 09:00 median 67.00 | Matchbook 75.00
    DATA: model 3.0% | style Leader (led 43% of runs) | runs in data 4 | last 3: 8 Oct Tramore NH Flat 16f Yielding 4/8; 23 Oct Sligo (IRE) Hurdle 25.5f Yielding To Soft 4/5; 17 Nov Limerick (IRE) Hurdle 16f Heavy 6/12 fig 94
    DATA for: Pace: may get an uncontested lead
    DATA against: Trainer 0 wins from 32 runs, last 14 days
- Pros And Cons (hrs_61456430) | 5yo G | 166lb | OR - | draw 0 | jockey J. J. Slevin | trainer Seamus Neville (14d 0/1) | headgear - | last run 23 days | form 711-27 | MARKET 1.2% | 09:00 median 67.00 | Matchbook 80.00
    DATA: model 1.5% | style Held up (led 5% of runs) | runs in data 2 | last 3: 6 Apr Cork NH Flat 19f Good To Yielding 7/8; 5 Nov Clonmel (IRE) Hurdle 16.5f Good 7/11 fig 93
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Gaelic Moon (hrs_17395868147) | 5yo G | 166lb | OR - | draw 0 | jockey Jordan Canavan(7) | trainer J P Flavin (14d 1/5) | headgear - | last run - days | form - | MARKET 1.2% | 09:00 median 101.00 | Matchbook 70.00
    DATA: model 2.6% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 20% wins (1/5), last 14 days
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Prophet's Path (hrs_42452130) | 5yo G | 166lb | OR - | draw 0 | jockey  | trainer Liam P Cusack (14d 0/2) | headgear - | last run 55 days | form - | MARKET 0.9% | 09:00 median 67.00 | Matchbook 100.00
    DATA: model 1.3% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 4 Oct Curragh Flat 12f Yielding 11/12
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Kaspar Des Bordes (hrs_17394957608) | 6yo G | 166lb | OR - | draw 0 | jockey  | trainer Eoin Christopher McCarthy (14d 0/6) | headgear - | last run 6 days | form 34F-6 | MARKET 0.9% | 09:00 median 101.00 | Matchbook 90.00
    DATA: model 1.9% | style Held up (led 8% of runs) | runs in data 1 | last 3: 22 Nov Cork (IRE) Hurdle 17f Soft 6/15
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Hetty Parker (hrs_17391026541) | 4yo F | 159lb | OR - | draw 0 | jockey Josh Williamson(3) | trainer J P Dempsey (14d 1/5) | headgear - | last run 101 days | form 6 | MARKET 0.5% | 09:00 median 150.00 | Matchbook 150.00
    DATA: model 1.3% | style Held up (led 8% of runs) | runs in data 1 | last 3: 19 Aug Sligo NH Flat 18.6f Good 6/8
    DATA for: Trainer 20% wins (1/5), last 14 days
    DATA against: Returns from a 101-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Cross Of Moanrue (hrs_17392713072) | 6yo G | 166lb | OR - | draw 0 | jockey  | trainer P. J. Rothwell (14d 0/32) | headgear - | last run 6 days | form 338-29 | MARKET 0.5% | 09:00 median 151.00 | Matchbook 190.00
    DATA: model 1.7% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 22 Nov Cork (IRE) Hurdle 17f Soft 9/15
    DATA against: Trainer 0 wins from 32 runs, last 14 days; Lightly raced: 1 run in our data, so the model has little to go on
- Membling (hrs_61521565) | 6yo M | 159lb | OR - | draw 0 | jockey Liam McKenna(3) | trainer M A Molloy (14d 0/0) | headgear - | last run 291 days | form 8- | MARKET 0.4% | 09:00 median 201.00 | Matchbook 160.00
    DATA: model 1.1% | style Held up (led 8% of runs) | runs in data 1 | last 3: 10 Feb Limerick Hurdle 15.7f Heavy 8/11
    DATA against: Last-run finishing speed -5.3% vs that field (faded); Returns from a 291-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Two Pats (hrs_17395288239) | 5yo G | 166lb | OR - | draw 0 | jockey Richard Condon(5) | trainer Louise G Lyons (14d 0/0) | headgear t (1st time) | last run 16 days | form 9 | MARKET 0.4% | 09:00 median 201.00 | Matchbook 190.00
    DATA: model 1.4% | style Unknown | runs in data 1 | last 3: 12 Nov Thurles (IRE) Hurdle 20f Good 9/11
    DATA for: First-time headgear
    DATA against: Last-run finishing speed -8.0% vs that field (faded); Lightly raced: 1 run in our data, so the model has little to go on
- Melody D'Arc (hrs_17391355086) | 4yo F | 159lb | OR - | draw 0 | jockey Alyse Clarke(7) | trainer John McConnell (14d 0/18) | headgear - | last run 13 days | form 800 | MARKET 0.4% | 09:00 median 201.00 | Matchbook 190.00
    DATA: model 1.5% | style Held up (led 5% of runs) | runs in data 3 | last 3: 7 Sep Galway NH Flat 16.7f Soft 8/18; 4 Nov Wexford (IRE) Hurdle 16.5f Yielding 11/14; 15 Nov Navan (IRE) Hurdle 16f Good To Yielding 12/17 fig 81
    DATA against: Best recent form figure 81, 11 lb below field average; Trainer 0 wins from 18 runs, last 14 days; Poor recent finishing positions
- Rough And Tough (hrs_34774978) | 6yo G | 166lb | OR - | draw 0 | jockey Kieren Buckley | trainer Michael Mulvany (14d 1/7) | headgear - | last run 14 days | form 80 | MARKET 0.4% | 09:00 median 201.00 | Matchbook 220.00
    DATA: model 0.8% | style Held up (led 3% of runs) | runs in data 4 | last 3: 1 Nov Curragh (IRE) Flat 7f Yielding To Soft 13/25 fig 57; 8 Nov Naas (IRE) Hurdle 16f Good To Yielding 8/12 fig 80; 14 Nov Navan (IRE) Hurdle 20f Good To Yielding 21/22
    DATA against: Best recent form figure 80, 12 lb below field average; Last-run finishing speed -10.9% vs that field (faded); Poor recent finishing positions

## 3:13 Fairyhouse | race_id rac_32305988559 | Francis McGee Memorial Handicap Hurdle
Hurdle |  | 2m4f0y | going Yielding | Turf | 20 runners | rating band - | age 4yo+
DATA pace: Even - Two likely leaders (Burru, Euro Agent). A fair, even gallop is most likely.
- Hey Now (hrs_59678787) | 5yo G | 151lb | OR 113 | draw 0 | jockey Harry Cobden | trainer Andrew McNamara (14d 0/1) | headgear t (1st time) | last run 24 days | form 45-14 | MARKET 12.1% | 09:00 median 6.00 | Matchbook 7.20 | CHECK (skip line 5.70)
    comment: Fourth last time out and a winner two starts back, Hey Now has some solid recent form and has run on today's going, but he's been beaten in all three of his other recent runs and carries 151 lb off 113.
    DATA: model 7.6% | style Prominent (led 4% of runs) | runs in data 3 | last 3: 26 Mar Clonmel Hurdle 16f Soft 5/16; 12 May Sligo Hurdle 17.8f Good 1/15; 4 Nov Wexford (IRE) Hurdle 16.5f Yielding 4/8 fig 111
    DATA for: First-time headgear
- Nelson County (hrs_40095671) | 6yo G | 151lb | OR 113 | draw 0 | jockey Danny Gilligan | trainer Ross O'Sullivan (14d 1/20) | headgear - | last run 252 days | form /4133- | MARKET 11.6% | 09:00 median 6.50 | Matchbook 7.40
    comment: Nelson County arrives with solid recent form, a third last time out, another third two starts back and a win three starts back, and he has run over today's trip and going.
    DATA: model 7.3% | style Held up (led 4% of runs) | runs in data 3 | last 3: 14 Jan Fairyhouse Chase 21.7f Yielding 1/9; 21 Feb Fairyhouse Chase 26f Heavy 3/8; 21 Mar Navan Chase 23.7f Soft To Heavy 3/12
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Returns from a 252-day break; First run over hurdles in our data
- Kim Roque (hrs_42847476) | 6yo G | 160lb | OR 122 | draw 0 | jockey Sam Ewing | trainer Joseph Patrick O'Brien (14d 3/34) | headgear - | last run 224 days | form 24543- | MARKET 11.2% | 09:00 median 6.50 | Matchbook 7.80
    comment: The risk is a 224-day absence, so fitness is the one question.
    DATA: model 10.1% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 1 Feb Leopardstown Chase 21.5f Heavy 5/23; 12 Mar Cheltenham Chase 26.3f Good 4/23; 18 Apr Ayr Chase 31.8f Heavy 3/16
    DATA for: Official rating 122, 8 lb above field average
    DATA against: Carries 8 lb more than average; Returns from a 224-day break; First run over hurdles in our data
- Fairlander (hrs_50433047) | 5yo G | 144lb | OR 106 | draw 0 | jockey Simon Torrens | trainer P. J. Rothwell (14d 0/32) | headgear - | last run 174 days | form 6430-1 | MARKET 9.2% | 09:00 median 8.00 | Matchbook 9.80
    comment: Fairlander won last time out and has run over today's trip and going, but he returns after 174 days off, carries 144 lb and comes from a yard that is 0/32 lately.
    DATA: model 7.6% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 17 Mar Down Royal Hurdle 20.4f Good To Yielding 3/19; 28 Apr Punchestown Hurdle 19.4f Yielding 15/24; 7 Jun Punchestown Hurdle 19.1f Good 1/16
    DATA for: Last-run finishing speed +2.2% vs that field (finished strongly); Good recent finishing positions; Carries 8 lb less than average
    DATA against: Official rating 106, 8 lb below field average; Trainer 0 wins from 32 runs, last 14 days; Returns from a 174-day break
- Kilt Ecossais (hrs_37489004) | 6yo G | 166lb | OR 128 | draw 0 | jockey J. J. Slevin | trainer Joseph Patrick O'Brien (14d 3/34) | headgear t (1st time) | last run 377 days | form 12112- | MARKET 8.2% | 09:00 median 8.00 | Matchbook 12.00
    comment: Unexposed gelding who has won three of his last five, including firsts two and three starts back, and was second last time out, though he returns after a 377-day absence and carries 166 lb, so there may be more to come if fit.
    DATA: model 5.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Official rating 128, 14 lb above field average; First-time headgear
    DATA against: Carries 14 lb more than average; Returns from a 377-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Harwa (hrs_61307190) | 4yo G | 161lb | OR 124 | draw 0 | jockey Conor Stone-Walsh | trainer Paul Nolan (14d 2/12) | headgear - | last run 236 days | form 22106- | MARKET 6.2% | 09:00 median 12.00 | Matchbook 14.00
    comment: Harwa won three starts back and was second in both runs before that, so the pedigree of his form is strong, and he has run on today's going before, though a sixth last time out and 236 days off the track are the main risk, with 161 lb to carry.
    DATA: model 3.8% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 3 Feb Fairyhouse Hurdle 16f Soft To Heavy 1/15; 10 Mar Cheltenham Hurdle 16.4f Good To Soft 15/22; 6 Apr Fairyhouse Hurdle 16f Yielding To Soft 6/9
    DATA for: Official rating 124, 10 lb above field average
    DATA against: Carries 9 lb more than average; Returns from a 236-day break
- Thisain'tthat (hrs_61078570) | 6yo G | 143lb | OR 105 | draw 0 | jockey Daniel King | trainer M A Molloy (14d 0/0) | headgear - | last run 202 days | form 5562-7 | MARKET 6.0% | 09:00 median 12.00 | Matchbook 15.00
    comment: He has run over today's trip and going, and a second two starts back is the pick of his form.
    DATA: model 4.1% | style Held up (led 3% of runs) | runs in data 5 | last 3: 31 Mar Limerick Hurdle 16f Soft 6/12; 14 Apr Clonmel Hurdle 19.8f Yielding 2/9; 10 May Cork Hurdle 17.3f Good 7/8
    DATA for: Carries 9 lb less than average
    DATA against: Official rating 105, 9 lb below field average; Returns from a 202-day break
- Zam Bobbler (hrs_52297938) | 5yo G | 145lb | OR 107 | draw 0 | jockey Shane O'Callaghan(3) | trainer P. J. Rothwell (14d 0/32) | headgear - | last run 237 days | form 5614- | MARKET 5.4% | 09:00 median 13.00 | Matchbook 17.00
    comment: Zam Bobbler won two starts back and was fourth last time, but he's been off 237 days, has a yard 0/32 in the last 14 days, and carries 145 lb.
    DATA: model 4.6% | style Held up (led 4% of runs) | runs in data 3 | last 3: 18 Feb Punchestown Hurdle 16.7f Soft 6/16; 17 Mar Wexford Hurdle 16f Soft 1/14; 5 Apr Fairyhouse Hurdle 20f Yielding To Soft 4/20
    DATA for: Carries 7 lb less than average
    DATA against: Official rating 107, 7 lb below field average; Trainer 0 wins from 32 runs, last 14 days; Returns from a 237-day break
- Euro Agent (hrs_59186099) | 5yo G | 144lb | OR 106 | draw 0 | jockey Josh Williamson(3) | trainer Gordon Elliott (14d 6/65) | headgear - | last run 24 days | form 722313 | MARKET 5.2% | 09:00 median 13.00 | Matchbook 18.50
    comment: He has run over today's trip and going, yet it's hard to fancy him.
    DATA: model 7.9% | style Leader (led 43% of runs) | runs in data 8 | last 3: 2 Oct Gowran Park Hurdle 20.2f Good 3/17; 9 Oct Downpatrick Hurdle 17.3f Good 1/9; 4 Nov Wexford (IRE) Hurdle 16.5f Yielding 3/8 fig 108
    DATA for: Good recent finishing positions; Carries 8 lb less than average
    DATA against: Official rating 106, 8 lb below field average
- Carrigg Island (hrs_51650039) | 6yo G | 158lb | OR 120 | draw 0 | jockey G B Noonan | trainer Eoin Christopher McCarthy (14d 0/6) | headgear h | last run 20 days | form 553-05 | MARKET 4.5% | 09:00 median 15.00 | Matchbook 22.00
    comment: Carrigg Island is winless in his last five, though a third three starts back and a fifth last time out show he's competitive, and he has run over today's trip and going after a 20-day break.
    DATA: model 4.1% | style Held up (led 5% of runs) | runs in data 2 | last 3: 24 Sep Listowel Hurdle 20f Good 10/15; 8 Nov Naas (IRE) Hurdle 20f Good To Yielding 5/20 fig 117
    DATA for: Best recent form figure 117, 6 lb above field average; Official rating 120, 6 lb above field average
    DATA against: Carries 6 lb more than average; Lightly raced: 2 runs in our data, so the model has little to go on
- Coyote Spirit (hrs_41152909) | 8yo G | 161lb | OR 123 | draw 0 | jockey Jack Kennedy | trainer Gordon Elliott (14d 6/65) | headgear p | last run 148 days | form 410-66 | MARKET 3.5% | 09:00 median 17.00 | Matchbook 30.00
    comment: Coyote Spirit won four starts back but has finished a sixth last time out, and another sixth two starts back, and returns after 148 days off while carrying 161 lb.
    DATA: model 3.8% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 5 Apr Cork Hurdle 19f Yielding 16/19; 15 Jun Kilbeggan Chase 20f Good 6/12; 3 Jul Wexford Chase 19.5f Good 6/11
    DATA for: Official rating 123, 9 lb above field average; Last-run finishing speed +2.0% vs that field (finished strongly)
    DATA against: Poor recent finishing positions; Carries 9 lb more than average; Returns from a 148-day break
- Yeah Man (hrs_28707049) | 9yo G | 161lb | OR 123 | draw 0 | jockey Keith Donoghue | trainer Gavin Cromwell (14d 3/39) | headgear - | last run 236 days | form 2P60P- | MARKET 2.7% | 09:00 median 26.00 | Matchbook 34.00
    comment: Winless in recent starts and pulled up last time, he returns after 236 days, but his official 123 looks workable even under 161 lb.
    DATA: model 3.6% | style Midfield (led 4% of runs) | runs in data 4 | last 3: 14 Feb Gowran Park Hurdle 16f Heavy 6/7; 12 Mar Cheltenham Hurdle 24f Good 16/24; 6 Apr Fairyhouse Chase 29.1f Yielding To Soft PU/30
    DATA for: Official rating 123, 9 lb above field average
    DATA against: Poor recent finishing positions; Carries 9 lb more than average; Returns from a 236-day break; Pulled up in 2 of its last 4 jumps runs
- Ms Agartha Yeats (hrs_32668433) | 8yo M | 148lb | OR 110 | draw 0 | jockey Danny Mullins | trainer F G Hand (14d 0/1) | headgear p (1st time) | last run 337 days | form 3/F0P- | MARKET 2.3% | 09:00 median 26.00 | Matchbook 48.00
    comment: Pulled up last time out and off for 337 days, she has to bounce back from a rough recent run, though a third four starts back and prior experience over today's trip give some encouragement.
    DATA: model 4.0% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: First-time headgear
    DATA against: Returns from a 337-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Magic Day (hrs_40786732) | 7yo M | 149lb | OR 111 | draw 0 | jockey Caragh Monaghan(7) | trainer Ian Patrick Donoghue (14d 0/9) | headgear t | last run 14 days | form -62436 | MARKET 2.3% | 09:00 median 26.00 | Matchbook 48.00
    comment: Magic Day was sixth last time out, 14 days ago, but she was third two starts back and second four starts back, and she has run over today's trip and going before.
    DATA: model 4.6% | style Prominent (led 3% of runs) | runs in data 7 | last 3: 21 Aug Kilbeggan Hurdle 18.9f Good To Yielding 4/15; 19 Sep Navan Hurdle 21f Good 3/15; 14 Nov Navan (IRE) Hurdle 20f Good To Yielding 6/12 fig 108
    DATA against: Trainer 0 wins from 9 runs, last 14 days; Race comments mention jumping mistakes in 2 of its last 5 runs
- Dont Go Yet (hrs_17841691) | 12yo G | 150lb | OR 112 | draw 0 | jockey Sarah Kavanagh(7) | trainer Edward Cawley (14d 0/2) | headgear - | last run 14 days | form 133-U9 | MARKET 2.0% | 09:00 median 26.00 | Matchbook 75.00
    comment: Dont Go Yet returns after a fortnight with a ninth last time out and an unseated two starts back, but a pair of thirds before that and a win five starts back show he has ability. He has run over today's trip and going, yet 150 lb is a hefty burden.
    DATA: model 4.8% | style Prominent (led 3% of runs) | runs in data 7 | last 3: 30 Apr Punchestown Chase 16.3f Yielding 3/20; 25 May Ballinrobe Chase 19.6f Good UR/13; 14 Nov Navan (IRE) Hurdle 16f Good To Yielding 9/15 fig 108
    DATA against: Race comments mention jumping mistakes in 2 of its last 5 runs; Fell or unseated in 1 of its last 5 jumps runs; Aged 12, older than most of this field
- Duke Of Leggagh (hrs_30208157) | 6yo G | 152lb | OR 114 | draw 0 | jockey Eoghan Finegan(5) | trainer Michael Mulvany (14d 1/7) | headgear t | last run 14 days | form 1P/9-7 | MARKET 1.7% | 09:00 median 34.00 | Matchbook 70.00
    comment: Duke Of Leggagh arrives quickly after 14 days, but he has slipped since winning four starts back, being pulled up and then finishing a ninth and a seventh.
    DATA: model 2.8% | style Midfield (led 23% of runs) | runs in data 6 | last 3: 15 Sep Punchestown Flat 8.1f Good 11/14; 30 Sep Bellewstown Flat 12.5f Soft To Heavy 5/12; 14 Nov Navan (IRE) Hurdle 16f Good To Yielding 7/15 fig 114
- Noble Name (hrs_49974379) | 6yo M | 143lb | OR 105 | draw 0 | jockey Patrick M O'Brien(5) | trainer Ms Claire O'Connell (14d 1/9) | headgear ht | last run 202 days | form 1435-8 | MARKET 1.7% | 09:00 median 34.00 | Matchbook 70.00
    comment: Noble Name is hard to fancy after a eighth last time out and a long 202 days off, with a fifth two starts back and a win five starts back now fading.
    DATA: model 4.0% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 10 May Cork Hurdle 19.2f Good 8/15
    DATA for: Carries 9 lb less than average
    DATA against: Official rating 105, 9 lb below field average; Returns from a 202-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Sequoiaspirit (hrs_22180501) | 9yo G | 156lb | OR 118 | draw 0 | jockey Brian Barry(7) | trainer Ray Hackett (14d 0/8) | headgear t | last run 13 days | form P-1007 | MARKET 1.6% | 09:00 median 34.00 | Matchbook 100.00
    DATA: model 2.8% | style Midfield (led 4% of runs) | runs in data 8 | last 3: 2 Sep Navan Flat 16f Good 10/16; 26 Sep Listowel Hurdle 20f Good 13/14; 15 Nov Navan (IRE) Hurdle 21f Good To Yielding 7/16 fig 111
    DATA for: Has won at this trip or further
    DATA against: Recent figures 7 lb below its current mark (looks high in the weights); Trainer 0 wins from 8 runs, last 14 days; Poor recent finishing positions; Pulled up in 1 of its last 5 jumps runs
- Portnacoo (hrs_33903975) | 8yo G | 144lb | OR 106 | draw 0 | jockey Michael Kenneally(3) | trainer H Smyth (14d 0/0) | headgear - | last run 283 days | form 4PU94- | MARKET 1.3% | 09:00 median 51.00 | Matchbook 85.00
    comment: Portnacoo showed a bit of life when fourth last time out, but he is winless in his last five and has been unseated and pulled up in that spell, while returning after 283 days off.
    DATA: model 1.9% | style Held up (led 5% of runs) | runs in data 2 | last 3: 22 Jan Gowran Park Hurdle 23.5f Heavy 9/15; 18 Feb Punchestown Hurdle 24.8f Soft 4/5
    DATA for: Carries 8 lb less than average
    DATA against: Official rating 106, 8 lb below field average; Last-run finishing speed -4.3% vs that field (faded); Returns from a 283-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- Burru (hrs_34253317) | 8yo G | 145lb | OR 107 | draw 0 | jockey Tiernan Power Roche | trainer Bernard Martin Crowley (14d 0/2) | headgear - | last run 13 days | form -10460 | MARKET 1.3% | 09:00 median 41.00 | Matchbook 140.00
    comment: Burru has been going the wrong way, unplaced last time out and a sixth two starts back, with his only win five starts back; he's quick back after 13 days.
    DATA: model 5.2% | style Leader (led 29% of runs) | runs in data 5 | last 3: 13 Aug Tramore Chase 21.8f Good 4/9; 20 Aug Killarney Chase 20.8f Good 6/11; 15 Nov Navan (IRE) Hurdle 21f Good To Yielding 13/16
    DATA for: Has won at this trip or further; Carries 7 lb less than average
    DATA against: Official rating 107, 7 lb below field average; Race comments mention jumping mistakes in 2 of its last 5 runs

## 3:43 Fairyhouse | race_id rac_32305990496 | Willie Elliott Memorial (Pro/Am) Flat Race
NH Flat |  | 2m0f0y | going Yielding | Turf | 11 runners | rating band - | age 4yo+
DATA pace: Unclear - Running styles known for only 3 of 11 runners.
- Uncle Pad (hrs_17394707288) | 5yo G | 168lb | OR - | draw 0 | jockey Mr H C Swan | trainer Gordon Elliott (14d 6/65) | headgear - | last run 300 days | form 1- | MARKET 51.6% | 09:00 median 1.62 | Matchbook 1.71
    comment: Unexposed gelding who won last time out, his only recent start, though he returns after 300 days off and carries 168 lb. Lightly raced and open to improvement, he has little form to go on beyond that win.
    DATA: model 9.0% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 300-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Golden Current (hrs_17396239455) | 5yo G | 168lb | OR - | draw 0 | jockey Mr J Dunne(7) | trainer Gordon Elliott (14d 6/65) | headgear - | last run 333 days | form 1- | MARKET 13.9% | 09:00 median 5.50 | Matchbook 7.00
    comment: Unexposed gelding who won last time out, his only recent run, though he returns after a 333-day absence and shoulders 168 lb. Lightly raced, he may have more to offer, but the long layoff adds a question over fitness.
    DATA: model 9.0% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 333-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Stanger (hrs_63776363) | 4yo G | 168lb | OR - | draw 0 | jockey Mr J L Gleeson | trainer Henry de Bromhead (14d 6/36) | headgear - | last run - days | form - | MARKET 13.9% | 09:00 median 5.50 | Matchbook 6.80
    comment: Unraced and with no form to go on, Stanger is a blank canvas on debut, so he's entirely unexposed and open to improvement. He carries 168 lb, and what he's capable of is anyone's guess until he shows it.
    DATA: model 9.0% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Noharmintrying (hrs_17391192378) | 5yo G | 168lb | OR - | draw 0 | jockey Mr D McGill(5) | trainer Aidan Anthony Howard (14d 0/2) | headgear t (1st time) | last run 96 days | form 5 | MARKET 8.4% | 09:00 median 10.50 | Matchbook 10.50
    comment: The one concern is a 96-day absence, so fitness is the main question.
    DATA: model 13.5% | style Unknown | runs in data 1 | last 3: 24 Aug Ballinrobe Hurdle 18.2f Good 5/15
    DATA for: Last-run finishing speed +3.6% vs that field (finished strongly); First-time headgear
    DATA against: Returns from a 96-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Back In Favour (hrs_52709363) | 5yo M | 161lb | OR - | draw 0 | jockey Miss A B O'Connor | trainer A. McCann (14d 0/8) | headgear h | last run 46 days | form 1-8330 | MARKET 3.1% | 09:00 median 23.00 | Matchbook 36.00
    DATA: model 11.2% | style Midfield (led 23% of runs) | runs in data 4 | last 3: 2 Aug Galway NH Flat 16f Good 3/6; 23 Sep Listowel NH Flat 20f Good 3/11; 13 Oct Punchestown NH Flat 16.2f Good 12/14
    DATA for: Good recent finishing positions
    DATA against: Trainer 0 wins from 8 runs, last 14 days
- Beautiful Moon (hrs_17396238412) | 5yo M | 161lb | OR - | draw 0 | jockey Mr Jack Paddy Carroll(7) | trainer Gordon Elliott (14d 6/65) | headgear - | last run - days | form - | MARKET 3.1% | 09:00 median 23.00 | Matchbook 40.00
    comment: Beautiful Moon is a debutant with no recorded form, so she's a complete blank and open to improvement. She carries 161 lb on her first outing, and there's nothing yet to judge her on.
    DATA: model 8.2% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Seedino (hrs_17396243627) | 5yo G | 168lb | OR - | draw 0 | jockey Mr M J Love(7) | trainer Mrs Lorna Fowler (14d 0/0) | headgear - | last run - days | form - | MARKET 1.6% | 09:00 median 41.00 | Matchbook 100.00
    comment: Seedino is an unexposed gelding with no recorded form to go on, so he's open to any amount of improvement. He carries 168 lb, and with nothing yet shown, the focus is on what he can unlock on debut.
    DATA: model 9.0% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Okingston Town (hrs_17395866061) | 4yo F | 161lb | OR - | draw 0 | jockey Harry Sexton(7) | trainer Seamus Neville (14d 0/1) | headgear - | last run 273 days | form 3- | MARKET 1.5% | 09:00 median 41.00 | Matchbook 100.00
    comment: Okingston Town finished third on her only recent start, but that came 273 days ago, so she returns after a long break. Lightly raced and unexposed, she is yet to win and could have more to offer, carrying 161 lb.
    DATA: model 8.2% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 273-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Cant Stopthe Clock (hrs_17394810545) | 5yo M | 161lb | OR - | draw 0 | jockey Sarah Kavanagh(7) | trainer Edward F Power (14d 0/0) | headgear h | last run 28 days | form 7 | MARKET 1.2% | 09:00 median 51.00 | Matchbook 140.00
    comment: The main risk is a seventh last time out, her only recent run, so she's yet to show she can bounce back.
    DATA: model 7.4% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 31 Oct Down Royal (IRE) NH Flat 17f Good 7/14 fig 81
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Mule Skinner (hrs_61911584) | 4yo G | 168lb | OR - | draw 0 | jockey Mr J P Sutton(7) | trainer Dermot A McLoughlin (14d 0/5) | headgear - | last run 168 days | form 35-8 | MARKET 1.0% | 09:00 median 67.00 | Matchbook 160.00
    comment: The main risk is a 168-day absence and an eighth last time out, so he may need the run.
    DATA: model 7.1% | style Held up (led 8% of runs) | runs in data 1 | last 3: 13 Jun Downpatrick NH Flat 18.8f Good 8/8
    DATA against: Last-run finishing speed -5.3% vs that field (faded); Returns from a 168-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Ladies Luck (hrs_17396240498) | 4yo F | 161lb | OR - | draw 0 | jockey Mr B J Walsh(7) | trainer Barry John Walsh (14d 0/0) | headgear - | last run 195 days | form 4-3 | MARKET 0.8% | 09:00 median 81.00 | Matchbook 220.00
    comment: Lightly raced and unexposed, Ladies Luck was third last time out, and a fourth two starts back, so she's yet to win but has room to progress. She returns after 195 days off and carries 161 lb.
    DATA: model 8.2% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 195-day break; Lightly raced: 0 runs in our data, so the model has little to go on
