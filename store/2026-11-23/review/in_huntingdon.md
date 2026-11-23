# Card review packet: Huntingdon, 2026-11-23

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
{"meeting": "huntingdon", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 12:45 Huntingdon | race_id rac_32305231192 | Annual Members At Huntingdon Maiden Hurdle Race (GBB Race)
Hurdle | Class 4 | 1m7f171y | going Good | Turf | 8 runners | rating band - | age 4yo+
DATA pace: Even - Two likely leaders (Aspull, My Mate Aj). A fair, even gallop is most likely.
- My Mate Aj (hrs_58534924) | 5yo G | 158lb | OR - | draw 0 | jockey Callum Pritchard | trainer Ben Pauling (14d 5/29) | headgear - | last run 27 days | form 341-2 | MARKET 38.9% | 09:00 median 2.25 | Matchbook 2.44
    DATA: model 19.2% | style Leader (led 57% of runs) | runs in data 3 | last 3: 19 Jan Lingfield NH Flat 16f Soft 4/6; 16 Apr Hereford NH Flat 16.2f Good 1/11; 27 Oct Newcastle Hurdle 17f Good 2/6 fig 109
    DATA for: Has won at this trip or further; Good recent finishing positions
- Double The Dance (hrs_51558192) | 5yo G | 158lb | OR - | draw 0 | jockey Freddie Mitchell(3) | trainer Jamie Moore & Josh Moore (14d 1/22) | headgear - | last run 252 days | form 1/222- | MARKET 25.9% | 09:00 median 3.25 | Matchbook 3.80
    DATA: model 18.2% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 16 Mar Plumpton NH Flat 17.8f Good To Soft 2/5
    DATA for: Last-run finishing speed +2.5% vs that field (finished strongly)
    DATA against: Returns from a 252-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Donegal (hrs_43002680) | 4yo G | 158lb | OR - | draw 0 | jockey Sean Bowen | trainer Charlie Longsdon (14d 2/14) | headgear - | last run 315 days | form 27- | MARKET 11.4% | 09:00 median 7.00 | Matchbook 9.00
    DATA: model 8.9% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 12 Jan Hereford Hurdle 16.2f Soft 7/14
    DATA against: Returns from a 315-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Big Win (hrs_54525520) | 4yo G | 158lb | OR - | draw 0 | jockey Robert Dunne | trainer James Owen (14d 3/40) | headgear - | last run 42 days | form - | MARKET 7.8% | 09:00 median 11.00 | Matchbook 13.00
    DATA: model 21.8% | style Prominent (led 3% of runs) | runs in data 4 | last 3: 6 Jun Chepstow Flat 12f Soft 1/9; 27 Jun Newcastle Flat 12.4f Standard To Slow 4/12; 12 Oct Yarmouth Flat 14.1f Good To Soft 2/11
    DATA for: Last-run finishing speed +3.6% vs that field (finished strongly); Good recent finishing positions
    DATA against: First run over hurdles in our data
- Trapper John (hrs_39848634) | 5yo G | 158lb | OR - | draw 0 | jockey Tom Cannon | trainer Harry Eustace (14d 0/8) | headgear - | last run 16 days | form 50U- | MARKET 7.6% | 09:00 median 10.00 | Matchbook 14.50
    DATA: model 9.8% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 24 Apr Chepstow Hurdle 16.1f Good UR/14; 12 Oct Yarmouth Flat 14.1f Good To Soft 7/11; 7 Nov Southwell (AW) Flat 16.5f Standard 6/10 fig 58
    DATA against: Trainer 0 wins from 8 runs, last 14 days; Poor recent finishing positions; Fell or unseated in 1 of its last 2 jumps runs
- Talladale (hrs_7000000427) | 4yo G | 158lb | OR - | draw 0 | jockey Ciaran Gethings | trainer Tom Lacey (14d 2/9) | headgear - | last run 90 days | form 53 | MARKET 7.0% | 09:00 median 12.00 | Matchbook 14.50
    DATA: model 13.5% | style Held up (led 8% of runs) | runs in data 2 | last 3: 15 Jul Uttoxeter NH Flat 15.8f Good 5/11; 25 Aug Stratford NH Flat 16.3f Good To Firm 3/8
    DATA for: Trainer 22% wins (2/9), last 14 days
    DATA against: Returns from a 90-day break; Lightly raced: 2 runs in our data, so the model has little to go on; First run over hurdles in our data
- Vinne (hrs_17395130746) | 4yo F | 151lb | OR - | draw 0 | jockey Jack Hogan | trainer Alex Hales (14d 0/5) | headgear - | last run 16 days | form 0 | MARKET 0.8% | 09:00 median 126.00 | Matchbook 170.00
    DATA: model 2.8% | style Held up (led 8% of runs) | runs in data 1 | last 3: 7 Nov Uttoxeter NH Flat 16f Good 11/14 fig 94
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Aspull (hrs_54644674) | 4yo G | 158lb | OR - | draw 0 | jockey Charlie Hammond | trainer Phil McEntee (14d 0/2) | headgear h | last run 42 days | form - | MARKET 0.5% | 09:00 median 201.00 | Matchbook 200.00
    DATA: model 5.9% | style Leader (led 57% of runs) | runs in data 8 | last 3: 31 Aug Southwell Flat 8.1f Standard 3/14; 17 Sep Southwell Flat 8.1f Standard 11/12; 12 Oct Yarmouth Flat 8f Good To Soft 11/12
    DATA against: Last-run finishing speed -2.9% vs that field (faded); First run over hurdles in our data

## 1:15 Huntingdon | race_id rac_32305233129 | Christmas Parties At Huntingdon Racecourse Handicap Hurdle Race
Hurdle | Class 5 | 1m7f171y | going Good | Turf | 12 runners | rating band 0-100 | age 3yo+
DATA pace: Lone leader - Uncle Remus is the only habitual front-runner and may be allowed an easy lead.
- Chico Magnifica (hrs_54398386) | 4yo G | 163lb | OR 95 | draw 0 | jockey Sean Bowen | trainer Olly Murphy (14d 10/50) | headgear - | last run 24 days | form 99-231 | MARKET 32.1% | 09:00 median 2.50 | Matchbook 2.86
    comment: Chico Magnifica won last time out and was third two starts back, a rise in form after two ninths, and he's fit enough after 24 days with experience of today's trip and going. The main risk is the hefty 163 lb he must carry.
    DATA: model 22.8% | style Unknown | runs in data 7 | last 3: 11 May Southwell Hurdle 15.8f Good 2/13; 4 Oct Uttoxeter Hurdle 15.8f Good 3/11; 30 Oct Uttoxeter Hurdle 16f Good 1/10 fig 97
    DATA for: Best recent form figure 97, 9 lb above field average; Official rating 95, 6 lb above field average; Trainer 20% wins (10/50), last 14 days; Last-run finishing speed +4.2% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Carries 6 lb more than average
- Tazman Dan (hrs_59961475) | 5yo G | 165lb | OR 97 | draw 0 | jockey Charlie Hammond | trainer Stuart Edmunds (14d 1/11) | headgear - | last run 26 days | form 57-443 | MARKET 20.4% | 09:00 median 4.00 | Matchbook 4.50
    comment: Yet to win in his last five, he must still carry 165 lb, which is the main risk.
    DATA: model 7.3% | style Held up (led 3% of runs) | runs in data 5 | last 3: 5 Sep Stratford Hurdle 16.3f Good 4/6; 4 Oct Uttoxeter Hurdle 15.8f Good 4/7; 28 Oct Huntingdon Hurdle 16f Good 3/9 fig 97
    DATA for: Best recent form figure 97, 9 lb above field average; Official rating 97, 8 lb above field average; Last-run finishing speed +2.9% vs that field (finished strongly)
    DATA against: Carries 8 lb more than average; Race comments mention jumping mistakes in 2 of its last 3 runs
- Uncle Remus (hrs_47313658) | 5yo G | 164lb | OR 96 | draw 0 | jockey Jonjo O'Neill Jr. | trainer Henrietta C Knight (14d 1/9) | headgear - | last run 21 days | form P51214 | MARKET 12.2% | 09:00 median 6.50 | Matchbook 7.60
    comment: Uncle Remus has won two of his last six, including two starts back, and was fourth last time out 21 days ago, while he has run over today's trip and going before.
    DATA: model 14.3% | style Leader (led 23% of runs) | runs in data 7 | last 3: 15 Sep Uttoxeter Hurdle 15.8f Good 1/13; 15 Oct Fontwell Hurdle 17.5f Good To Soft 1/9 fig 95; 2 Nov Plumpton Hurdle 16f Good 4/6 fig 95
    DATA for: Best recent form figure 95, 7 lb above field average; Official rating 96, 7 lb above field average; Has won at this trip or further; Good recent finishing positions; Pace: may get an uncontested lead
    DATA against: Carries 7 lb more than average; Race comments mention jumping mistakes in 3 of its last 5 runs; Pulled up in 1 of its last 5 jumps runs
- Dotties Star (hrs_32278421) | 7yo G | 161lb | OR 93 | draw 0 | jockey Ciaran Gethings | trainer Pat Phelan (14d 2/4) | headgear - | last run 13 days | form P42-51 | MARKET 9.2% | 09:00 median 8.50 | Matchbook 10.50
    comment: Dotties Star won last time out and returns just 13 days later, having also run over today's trip and going, though a fifth two starts back and a pulled up five runs ago show some inconsistency.
    DATA: model 6.7% | style Held up (led 4% of runs) | runs in data 9 | last 3: 11 Aug Lingfield Flat 12f Standard 10/11; 19 Oct Plumpton Hurdle 20.5f Good 5/7 fig 84; 10 Nov Lingfield Hurdle 16f Good 1/9 fig 93
    DATA for: Best recent form figure 93, 5 lb above field average; Last-run finishing speed +4.8% vs that field (finished strongly); Has won at this trip or further
- Papa Oscar (hrs_49907025) | 4yo G | 148lb | OR 80 | draw 0 | jockey Robert Dunne | trainer Clare Hobson (14d 0/5) | headgear h | last run 10 days | form 6-5624 | MARKET 6.0% | 09:00 median 12.00 | Matchbook 17.00
    comment: He's fit after ten days off, has run over today's trip and going, and carries 148 lb.
    DATA: model 3.7% | style Held up (led 3% of runs) | runs in data 6 | last 3: 16 Jun Stratford Hurdle 16.3f Good 6/12; 28 Oct Huntingdon Hurdle 16f Good 2/9 fig 80; 13 Nov Southwell Hurdle 16f Good 4/11 fig 75
    DATA for: Carries 9 lb less than average
    DATA against: Best recent form figure 80, 8 lb below field average; Official rating 80, 9 lb below field average
- Master Dunraven (hrs_34746460) | 6yo G | 147lb | OR 79 | draw 0 | jockey Conor O'Farrell | trainer Neil Mulholland (14d 3/18) | headgear p | last run 159 days | form 7036-7 | MARKET 5.0% | 09:00 median 15.00 | Matchbook 20.00
    comment: Master Dunraven is winless in his last five, with a seventh last time out and a third three starts back his best effort, and he returns after 159 days off.
    DATA: model 9.1% | style Held up (led 5% of runs) | runs in data 3 | last 3: 26 Jan Plumpton Hurdle 15.9f Soft 3/7; 26 Feb Wetherby Hurdle 16f Soft 6/8; 17 Jun Worcester Hurdle 16f Good 7/8
    DATA for: Carries 10 lb less than average
    DATA against: Official rating 79, 10 lb below field average; Returns from a 159-day break
- Saucats (hrs_40312321) | 5yo G | 153lb | OR 85 | draw 0 | jockey Callum Pritchard | trainer Syd Hosie (14d 2/10) | headgear tb (1st time) | last run 48 days | form 373714 | MARKET 3.5% | 09:00 median 23.00 | Matchbook 30.00
    DATA: model 8.5% | style Prominent (led 4% of runs) | runs in data 16 | last 3: 18 Sep Newton Abbot Hurdle 16.8f Good 7/11; 28 Sep Newton Abbot Hurdle 16.8f Good 1/5; 6 Oct Huntingdon Hurdle 19.6f Good 4/7
    DATA for: Trainer 20% wins (2/10), last 14 days; Has won at this trip or further; First-time headgear
- Zucayan (hrs_25108790) | 9yo G | 163lb | OR 95 | draw 0 | jockey Nick Slatter(3) | trainer Fergal O'Brien (14d 3/26) | headgear t | last run 50 days | form -2F788 | MARKET 3.1% | 09:00 median 23.00 | Matchbook 36.00
    comment: The risk is a winless recent spell of two eighths and a seventh, plus 163 lb after 50 days off.
    DATA: model 4.0% | style Held up (led 3% of runs) | runs in data 6 | last 3: 25 Aug Stratford Hurdle 18.7f Good To Firm 7/8; 15 Sep Uttoxeter Hurdle 15.8f Good 8/13; 4 Oct Uttoxeter Hurdle 15.8f Good 8/11
    DATA for: Official rating 95, 6 lb above field average
    DATA against: Poor recent finishing positions; Carries 6 lb more than average; Fell or unseated in 1 of its last 5 jumps runs; Aged 9, older than most of this field
- Mr Zee (hrs_21686553) | 9yo G | 148lb | OR 80 | draw 0 | jockey Bradley Harris(3) | trainer Michael Blake (14d 0/1) | headgear p | last run 295 days | form 77412- | MARKET 2.7% | 09:00 median 23.00 | Matchbook 50.00
    comment: Second last time out and a winner two starts back, but Mr Zee returns after 295 days off, which is a big question mark, and he carries 148 lb off 80.
    DATA: model 9.6% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 15 Jan Wincanton Hurdle 15.2f Heavy 1/13; 1 Feb Market Rasen Hurdle 16.6f Soft 2/8
    DATA for: Last-run finishing speed +2.7% vs that field (finished strongly); Good recent finishing positions; Carries 9 lb less than average
    DATA against: Official rating 80, 9 lb below field average; Returns from a 295-day break; Lightly raced: 2 runs in our data, so the model has little to go on; Aged 9, older than most of this field
- Callero (hrs_59275993) | 4yo G | 142lb | OR 72 | draw 0 | jockey Freddie Mitchell(3) | trainer Jamie Moore & Josh Moore (14d 1/22) | headgear b (1st time) | last run 17 days | form 67-5P4 | MARKET 2.6% | 09:00 median 23.00 | Matchbook 70.00
    comment: Callero is winless in his last five, with a fourth last time out the best of a modest bunch that also includes a pulled up two starts back, and he has run over today's trip and going.
    DATA: model 3.8% | style Midfield (led 29% of runs) | runs in data 7 | last 3: 26 May Plumpton Hurdle 15.9f Good 5/5; 3 Oct Fontwell Hurdle 19.1f Good PU/9; 6 Nov Fontwell Hurdle 17.5f Good 4/10 fig 65
    DATA for: Carries 15 lb less than average; First-time headgear
    DATA against: Best recent form figure 65, 23 lb below field average; Recent figures 7 lb below its current mark (looks high in the weights); Official rating 72, 17 lb below field average; Last-run finishing speed -2.2% vs that field (faded); Pulled up in 1 of its last 4 jumps runs
- Imperial Trooper (hrs_40919445) | 4yo G | 168lb | OR 100 | draw 0 | jockey I. J. Power | trainer Jennie Candlish (14d 4/24) | headgear - | last run 47 days | form 533 | MARKET 2.0% | 09:00 median 34.00 | Matchbook 60.00
    comment: Imperial Trooper arrives with a consistent profile, third last time out and third again two starts back, while he has run over today's trip and going before.
    DATA: model 8.1% | style Midfield (led 3% of runs) | runs in data 10 | last 3: 16 Jul Worcester Hurdle 16f Good 3/7; 25 Jul Chester Flat 12.3f Good 8/10; 7 Oct Sedgefield Hurdle 16.8f Good 3/9
    DATA for: Official rating 100, 11 lb above field average; Good recent finishing positions
    DATA against: Carries 11 lb more than average
- Amalfina (hrs_45921631) | 4yo F | 160lb | OR 92 | draw 0 | jockey Harry Atkins(5) | trainer D. J. Jeffreys (14d 0/3) | headgear - | last run 13 days | form 737V | MARKET 1.2% | 09:00 median 51.00 | Matchbook 130.00
    comment: Amalfina is without a win in her last four, though a third three starts back shows some ability, and she has run over today's trip and going before. Fresh enough after 13 days, but a seventh two starts back and a hefty 160 lb hold her back.
    DATA: model 2.1% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 11 Jun Worcester Hurdle 16f Good 7/9; 7 Jul Uttoxeter Hurdle 15.8f Good 3/10; 24 Jul Uttoxeter Hurdle 15.8f Good 7/13
    DATA for: Last-run finishing speed +3.3% vs that field (finished strongly)

## 1:45 Huntingdon | race_id rac_32305235066 | Conferences At Huntingdon 'Chasing Excellence' Beginners' Steeple Chase (GBB Race)
Chase | Class 3 | 2m7f129y | going Good | Turf | 5 runners | rating band - | age 4yo+
DATA pace: Even - Two likely leaders (Reckless Spending, Stone's Throw). A fair, even gallop is most likely.
- Crystal Island (hrs_51558073) | 5yo G | 159lb | OR 133 | draw 0 | jockey Nico de Boinville | trainer Nicky Henderson (14d 3/17) | headgear - | last run 216 days | form 1/11- | MARKET 61.1% | 09:00 median 1.50 | Matchbook 1.60
    comment: Crystal Island arrives unbeaten in his last three starts, winning last time out and again two and three starts back, and he's a strong threat under 159 lb. The main risk is a 216-day layoff, so fitness is the question.
    DATA: model 38.9% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 21 Apr Ffos Las Hurdle 20f Good 1/12
    DATA for: Official rating 133, 6 lb above field average; Last-run finishing speed +5.8% vs that field (finished strongly)
    DATA against: Returns from a 216-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Reckless Spending (hrs_46013737) | 6yo G | 159lb | OR 134 | draw 0 | jockey Robert Dunne | trainer Nicky Henderson (14d 3/17) | headgear - | last run 219 days | form 37171- | MARKET 18.4% | 09:00 median 5.00 | Matchbook 5.40
    comment: The one concern is a 219-day layoff, so fitness is the main risk.
    DATA: model 25.3% | style Leader (led 29% of runs) | runs in data 3 | last 3: 2 Feb Kempton Hurdle 21f Good To Soft 1/15; 14 Feb Haydock Hurdle 24.3f Good To Soft 7/9; 18 Apr Bangor-on-Dee Hurdle 23.1f Good 1/5
    DATA for: Official rating 134, 7 lb above field average; Has won at this trip or further; Good recent finishing positions
    DATA against: Returns from a 219-day break; First run over fences in our data
- John Barbour (hrs_41229769) | 7yo G | 159lb | OR 130 | draw 0 | jockey Jack Hogan | trainer Fergal O'Brien (14d 3/26) | headgear t | last run 31 days | form 12P1-9 | MARKET 8.0% | 09:00 median 11.00 | Matchbook 13.00
    comment: John Barbour won two starts back and five starts back, so he has a winning habit, and his 31-day break should have him fresh after a ninth last time out. He has run on today's going before and carries 159 lb, which is the one concern.
    DATA: model 9.7% | style Midfield (led 3% of runs) | runs in data 4 | last 3: 14 Mar Uttoxeter Hurdle 23.3f Soft PU/17; 12 Apr Wincanton Hurdle 21.4f Good 1/6; 23 Oct Cheltenham Hurdle 20f Good To Soft 9/11 fig 114
    DATA against: Pulled up in 1 of its last 4 jumps runs; First run over fences in our data
- Huffin An A Puffin (hrs_39901085) | 7yo G | 159lb | OR 121 | draw 0 | jockey Tom Cannon | trainer Lucy Wadham (14d 0/1) | headgear p (1st time) | wind surgery | last run 222 days | form 1/1P8- | MARKET 6.6% | 09:00 median 13.00 | Matchbook 16.00
    comment: The risk is a 222-day absence, plus an eighth last time out and 159 lb on his back.
    DATA: model 15.8% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 5 Feb Doncaster Hurdle 19.4f Soft 1/5; 28 Feb Newbury Hurdle 20.5f Good To Soft PU/9; 15 Apr Haydock Hurdle 21.2f Good 8/11
    DATA for: First-time headgear
    DATA against: Official rating 121, 6 lb below field average; Last-run finishing speed -8.1% vs that field (faded); Returns from a 222-day break; Pulled up in 1 of its last 3 jumps runs; First run over fences in our data
- Stone's Throw (hrs_39040330) | 6yo G | 159lb | OR 119 | draw 0 | jockey Sean Bowen | trainer Billy Aprahamian (14d 0/3) | headgear - | last run 255 days | form P1174- | MARKET 5.8% | 09:00 median 15.00 | Matchbook 19.00
    comment: Stone's Throw won three and four starts back, but he has since managed a fourth last time out and a seventh before that, and returns after 255 days off.
    DATA: model 10.3% | style Leader (led 38% of runs) | runs in data 2 | last 3: 21 Feb Chepstow Hurdle 23.6f Soft 7/11; 13 Mar Doncaster Hurdle 24.4f Good To Soft 4/7
    DATA against: Official rating 119, 8 lb below field average; Last-run finishing speed -2.8% vs that field (faded); Returns from a 255-day break; Lightly raced: 2 runs in our data, so the model has little to go on; First run over fences in our data

## 2:18 Huntingdon | race_id rac_32305237003 | Book Hospitality At Huntingdon Handicap Steeple Chase (GBB Race)
Chase | Class 4 | 2m0f104y | going Good | Turf | 7 runners | rating band 0-120 | age 4yo+
DATA pace: Even - Two likely leaders (Black Hawk Eagle, Homme d'Un Soir). A fair, even gallop is most likely.
- Jamada (hrs_39996488) | 6yo G | 155lb | OR 107 | draw 0 | jockey Sean Bowen | trainer Olly Murphy (14d 10/50) | headgear - | last run 33 days | form 231-34 | MARKET 34.6% | 09:00 median 2.50 | Matchbook 2.80
    comment: Jamada has been consistent, with a fourth last time out, a third two starts back, and a win three starts back, and he has run over today's trip and going.
    DATA: model 22.0% | style Held up (led 4% of runs) | runs in data 5 | last 3: 13 Apr Fakenham Hurdle 16f Good 1/4; 15 May Aintree Hurdle 16.9f Good 3/10; 21 Oct Worcester Chase 16.5f Good To Soft 4/9 fig 103
    DATA for: Trainer 20% wins (10/50), last 14 days; Last-run finishing speed +3.5% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions; Carries 5 lb less than average
    DATA against: Official rating 107, 5 lb below field average
- Inside Man (hrs_37702238) | 6yo G | 165lb | OR 117 | draw 0 | jockey Ciaran Gethings | trainer Mrs Jane Williams (14d 3/8) | headgear - | last run 19 days | form 794-42 | MARKET 21.9% | 09:00 median 4.00 | Matchbook 4.40
    comment: Inside Man arrives in cracking nick after a second last time out just 19 days ago, with a fourth and another fourth before that, and he has run over today's trip and going before. The risk is the 165 lb he carries, though he is yet to win in his last five.
    DATA: model 17.0% | style Held up (led 5% of runs) | runs in data 4 | last 3: 24 Apr Chepstow Hurdle 16.1f Good 4/5; 28 Sep Newton Abbot Chase 16.3f Good 4/4; 4 Nov Chepstow Chase 16f Good 2/4 fig 116
    DATA for: Best recent form figure 116, 10 lb above field average; Trainer 38% wins (3/8), last 14 days
- Sweeper System (hrs_47345284) | 6yo G | 156lb | OR 108 | draw 0 | jockey Toby Wynne | trainer Sam Allwood (14d 0/0) | headgear - | last run 22 days | form P13-51 | MARKET 15.1% | 09:00 median 5.50 | Matchbook 6.80
    comment: Won last time out and has two wins in his last five starts, with a third and a fifth in between, and he's fresh enough after 22 days; he has run over today's trip and going too.
    DATA: model 13.0% | style Held up (led 3% of runs) | runs in data 5 | last 3: 4 Apr Huntingdon Hurdle 15.8f Good 3/8; 16 Oct Uttoxeter Chase 16f Good 5/5 fig 88; 1 Nov Worcester Chase 16.5f Good To Soft 1/10 fig 105
    DATA for: Last-run finishing speed +4.3% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Pulled up in 1 of its last 5 jumps runs
- Yes Indeed (hrs_21387275) | 9yo G | 160lb | OR 112 | draw 0 | jockey Jonjo O'Neill Jr. | trainer Jonjo & A.J. O'Neill (14d 6/35) | headgear - | last run 172 days | form P5-335 | MARKET 11.2% | 09:00 median 8.00 | Matchbook 8.60
    comment: The main risk is a 172-day absence, with 160 lb on his back too.
    DATA: model 14.4% | style Prominent (led 29% of runs) | runs in data 6 | last 3: 4 May Warwick Chase 16.2f Good 3/8; 23 May Bangor-on-Dee Chase 17.4f Good 3/7; 4 Jun Uttoxeter Chase 20.9f Good 5/5
    DATA for: Good recent finishing positions
    DATA against: Last-run finishing speed -8.4% vs that field (faded); Returns from a 172-day break; Race comments mention jumping mistakes in 2 of its last 5 runs; Pulled up in 1 of its last 5 jumps runs
- Granny Hawkins (hrs_35512659) | 7yo M | 156lb | OR 108 | draw 0 | jockey Luke Scott(3) | trainer Dr Richard Newland (14d 1/6) | headgear - | last run 37 days | form 11-355 | MARKET 7.1% | 09:00 median 13.00 | Matchbook 13.00
    comment: Granny Hawkins has slipped to a fifth last time out and another fifth the start before, a long way from the wins she managed four and five starts back.
    DATA: model 10.4% | style Midfield (led 4% of runs) | runs in data 5 | last 3: 5 Jul Market Rasen Hurdle 16.6f Good 3/7; 1 Oct Southwell Hurdle 15.8f Good 5/8; 17 Oct Stratford Hurdle 16.5f Good 5/6 fig 97
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 97, 9 lb below field average; Recent figures 11 lb below its current mark (looks high in the weights); Last-run finishing speed -2.7% vs that field (faded); First run over fences in our data
- Black Hawk Eagle (hrs_26460035) | 8yo G | 168lb | OR 120 | draw 0 | jockey Conor O'Farrell | trainer Kerry Lee (14d 1/5) | headgear - | last run 19 days | form 31F-43 | MARKET 5.9% | 09:00 median 14.00 | Matchbook 17.50
    comment: Black Hawk Eagle bids to build on a third last time out, 19 days ago, and he has a winner four starts back, plus experience over today's trip and going.
    DATA: model 11.7% | style Leader (led 38% of runs) | runs in data 4 | last 3: 16 Apr Hereford Chase 20.9f Good F/5; 16 May Uttoxeter Chase 20f Good 4/4; 4 Nov Chepstow Chase 16f Good 3/4 fig 110
    DATA for: Official rating 120, 8 lb above field average; Trainer 20% wins (1/5), last 14 days; Has won at this trip or further
    DATA against: Recent figures 10 lb below its current mark (looks high in the weights); Last-run finishing speed -3.5% vs that field (faded); Carries 8 lb more than average; Fell or unseated in 1 of its last 4 jumps runs
- Homme d'Un Soir (hrs_20828682) | 10yo G | 163lb | OR 115 | draw 0 | jockey Robert Dunne | trainer Billy Aprahamian (14d 0/3) | headgear tv | last run 18 days | form 341P-0 | MARKET 4.2% | 09:00 median 19.00 | Matchbook 26.00
    comment: The risk is a pulled up and an unplaced effort in his last two outings, plus 163 lb to carry.
    DATA: model 11.5% | style Leader (led 57% of runs) | runs in data 5 | last 3: 23 Mar Wincanton Hurdle 15.2f Good 1/5; 4 Apr Huntingdon Chase 16.5f Good PU/6; 5 Nov Newbury Hurdle 16.5f Good To Soft 16/16
    DATA against: Pulled up in 1 of its last 5 jumps runs; Aged 10, older than most of this field

## 2:53 Huntingdon | race_id rac_32305238940 | Festive Fiver Raceday 21 December Mares' Novices' Handicap Hurdle Race
Hurdle | Class 5 | 2m4f145y | going Good | Turf | 9 runners | rating band 0-100 | age 4yo+
DATA pace: Lone leader - Midnight Pass is the only habitual front-runner and may be allowed an easy lead.
- Lets Go Mo (hrs_58196677) | 4yo F | 157lb | OR 84 | draw 0 | jockey Tom Cannon | trainer Lucy Wadham (14d 0/1) | headgear - | wind surgery | last run 20 days | form 6654-2 | MARKET 26.4% | 09:00 median 3.25 | Matchbook 3.50 | CHECK (skip line 3.09)
    comment: Lets Go Mo arrives in her best form, a second last time out after a fourth two starts back, and 20 days since that run keeps her fresh and has run on today's going before.
    DATA: model 9.8% | style Held up (led 5% of runs) | runs in data 4 | last 3: 17 Feb Market Rasen Hurdle 16.6f Soft 5/8; 15 Mar Market Rasen Hurdle 16.6f Good To Soft 4/6; 3 Nov Lingfield Hurdle 16f Good 2/9 fig 88
    DATA for: Recent figures 4 lb above its current mark (looks well handicapped); Last-run finishing speed +2.4% vs that field (finished strongly)
- Zaraquelle (hrs_44721733) | 4yo F | 162lb | OR 89 | draw 0 | jockey Callum Pritchard | trainer James Owen (14d 3/40) | headgear t | last run 13 days | form 42-245 | MARKET 15.1% | 09:00 median 5.95 | Matchbook 5.90
    comment: On the plus side, she has run over today's trip and going, is fit after 13 days, and has two seconds in that form.
    DATA: model 20.1% | style Held up (led 4% of runs) | runs in data 6 | last 3: 13 Oct Hereford Hurdle 19.7f Good To Firm 2/7; 28 Oct Huntingdon Hurdle 16f Good 4/9 fig 89; 10 Nov Lingfield Hurdle 16f Good 5/9 fig 81
- Conniemak (hrs_47161338) | 5yo M | 153lb | OR 79 | draw 0 | jockey Lorcan Murtagh | trainer Mitchell Hunt & Tim Vaughan (14d 0/3) | headgear - | last run 261 days | form 8P375- | MARKET 14.4% | 09:00 median 5.50 | Matchbook 6.80
    comment: Winless in her last five and absent for 261 days, Conniemak is hard to fancy, though a fifth last time out and a third three starts back show some ability, and she has run over today's trip and going.
    DATA: model 15.0% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 23 Jan Warwick Hurdle 19f Good To Soft 7/12; 7 Mar Hereford Hurdle 19.7f Good 5/11
    DATA for: Carries 8 lb less than average
    DATA against: Official rating 79, 8 lb below field average; Returns from a 261-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- Palma Springs (hrs_58566046) | 4yo F | 164lb | OR 91 | draw 0 | jockey Isabelle Ryder(5) | trainer Jamie Snowden (14d 5/23) | headgear t | last run 159 days | form 64-34 | MARKET 13.2% | 09:00 median 6.50 | Matchbook 7.20
    comment: Palma Springs was fourth last time out and third two starts back, so she's consistent without a win in her last four, but a 159-day absence is a concern.
    DATA: model 10.1% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 25 May Huntingdon Hurdle 15.8f Good To Firm 3/6; 17 Jun Worcester Hurdle 16f Good 4/9
    DATA for: Trainer 22% wins (5/23), last 14 days; Last-run finishing speed +3.7% vs that field (finished strongly)
    DATA against: Returns from a 159-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- Midnight Pass (hrs_54304803) | 5yo M | 163lb | OR 89 | draw 0 | jockey Sean Bowen | trainer Martin Keighley (14d 1/12) | headgear - | last run 19 days | form 4P363P | MARKET 9.7% | 09:00 median 8.50 | Matchbook 10.00
    comment: Midnight Pass has twice finished third in her last six, including two starts back, and she has run over today's trip and going, while 19 days since her last run keeps her fresh.
    DATA: model 13.2% | style Prominent (led 43% of runs) | runs in data 8 | last 3: 22 Sep Fontwell Hurdle 17.7f Good 6/9; 11 Oct Chepstow Hurdle 19.5f Good To Soft 3/13; 4 Nov Chepstow Hurdle 19.5f Good To Soft PU/16
    DATA against: Pulled up in 2 of its last 5 jumps runs
- Mistress Fox (hrs_40186384) | 6yo M | 158lb | OR 84 | draw 0 | jockey Bradley Harris(3) | trainer Neil Mulholland (14d 3/18) | headgear ht | last run 166 days | form 884-27 | MARKET 8.9% | 09:00 median 10.00 | Matchbook 10.50
    comment: Mistress Fox is winless in her last five, beaten into seventh last time and now returning after 166 days off, so she is hard to fancy under 158 lb.
    DATA: model 12.0% | style Midfield (led 4% of runs) | runs in data 7 | last 3: 27 Mar Fontwell Hurdle 17.7f Good To Soft 4/7; 6 May Fontwell Hurdle 21.7f Good 2/9; 10 Jun Fontwell Hurdle 19.1f Good 7/10
    DATA against: Returns from a 166-day break
- Bontessony Doll (hrs_64590519) | 7yo M | 168lb | OR 94 | draw 0 | jockey Jonjo O'Neill Jr. | trainer Alan Jones (14d 0/0) | headgear - | last run 164 days | form U44 | MARKET 5.4% | 09:00 median 13.00 | Matchbook 21.00
    comment: Bontessony Doll bring back-to-back fourths into this, yet she's winless in her last three and returns after 164 days off, with an unseated three starts back.
    DATA: model 2.9% | style Held up (led 4% of runs) | runs in data 3 | last 3: 13 May Newton Abbot Hurdle 16.8f Good UR/8; 27 May Newton Abbot Hurdle 16.8f Good 4/10; 12 Jun Newton Abbot Hurdle 16.8f Good 4/9
    DATA for: Official rating 94, 7 lb above field average
    DATA against: Carries 7 lb more than average; Returns from a 164-day break; Fell or unseated in 1 of its last 3 jumps runs
- Polkaface (hrs_37096262) | 6yo M | 167lb | OR 93 | draw 0 | jockey Ciaran Gethings | trainer Ben Case (14d 1/7) | headgear tp (1st time) | last run 225 days | form 7/438- | MARKET 4.8% | 09:00 median 17.00 | Matchbook 20.00
    comment: The risk is a 225-day absence, with an eighth last time out, and 167 lb to carry.
    DATA: model 8.7% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 19 Feb Huntingdon Hurdle 20.7f Heavy 4/9; 15 Mar Chepstow Hurdle 19.5f Soft 3/10; 12 Apr Ffos Las Hurdle 20f Good To Soft 8/12
    DATA for: Official rating 93, 6 lb above field average; First-time headgear
    DATA against: Last-run finishing speed -5.3% vs that field (faded); Carries 6 lb more than average; Returns from a 225-day break
- Lady Showtime (hrs_40591971) | 7yo M | 158lb | OR 84 | draw 0 | jockey David Noonan | trainer Nigel Hawke (14d 2/11) | headgear - | last run 626 days | form 63478/ | MARKET 2.2% | 09:00 median 41.00 | Matchbook 48.00
    comment: The big risk is a 626-day absence, with an eighth last time out and 158 lb on her back.
    DATA: model 8.3% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 626-day break; Lightly raced: 0 runs in our data, so the model has little to go on

## 3:23 Huntingdon | race_id rac_32305240877 | Come Racing At Huntingdon Handicap Hurdle Race
Hurdle | Class 4 | 2m3f137y | going Good | Turf | 10 runners | rating band 0-120 | age 3yo+
DATA pace: Strong pace - 3 habitual front-runners (Lewisham Grove, Fidendum, Devon Skies). A contested lead should set things up for horses coming from behind.
- Lyrical Choice (hrs_52117394) | 5yo M | 149lb | OR 101 | draw 0 | jockey David Bass | trainer Henry Daly (14d 2/14) | headgear - | last run 274 days | form 23552- | MARKET 19.4% | 09:00 median 4.50 | Matchbook 4.80 | CHECK (skip line 4.27)
    comment: Lyrical Choice arrives with a second last time out and a third four starts back, yet she is winless in her last five and has had 274 days off, so fitness is the question.
    DATA: model 9.0% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 17 Jan Taunton Hurdle 16.5f Good To Soft 5/13; 22 Feb Hereford Hurdle 16.2f Soft 2/13
    DATA for: Last-run finishing speed +3.9% vs that field (finished strongly); Carries 9 lb less than average
    DATA against: Official rating 101, 9 lb below field average; Returns from a 274-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- Emerald Breeze (hrs_48112204) | 6yo G | 168lb | OR 120 | draw 0 | jockey Ciaran Gethings | trainer Ryan Hatch (14d 0/0) | headgear - | last run 232 days | form /3231- | MARKET 17.4% | 09:00 median 4.50 | Matchbook 5.80
    DATA: model 20.1% | style Midfield (led 5% of runs) | runs in data 4 | last 3: 30 Jan Ffos Las Hurdle 15.8f Heavy 2/8; 13 Feb Chepstow Hurdle 16.1f Soft 3/14; 5 Apr Market Rasen Hurdle 20.6f Good 1/5
    DATA for: Official rating 120, 10 lb above field average; Last-run finishing speed +9.4% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Carries 10 lb more than average; Returns from a 232-day break
- Fidendum (hrs_40942118) | 7yo G | 166lb | OR 118 | draw 0 | jockey Nick Slatter(3) | trainer David Killahena & Graeme McPherson (14d 3/9) | headgear ht | last run 23 days | form -13126 | MARKET 14.6% | 09:00 median 6.00 | Matchbook 6.60
    comment: Fidendum arrives with two wins in his last five starts, as well as a second two starts back, and a fresh 23 days since a sixth last time out.
    DATA: model 11.9% | style Leader (led 79% of runs) | runs in data 6 | last 3: 5 Jul Market Rasen Hurdle 16.6f Good 1/7; 15 Aug Perth Hurdle 16.2f Good 2/8; 31 Oct Ascot Hurdle 19.5f Good To Firm 6/9 fig 113
    DATA for: Official rating 118, 8 lb above field average; Trainer 33% wins (3/9), last 14 days; Good recent finishing positions
    DATA against: Carries 8 lb more than average; Pace: likely to be taken on for the lead
- Vivid Pink (hrs_32780937) | 7yo M | 156lb | OR 108 | draw 0 | jockey Tom Cannon | trainer Alan King (14d 2/18) | headgear h | wind surgery | last run 128 days | form /41-14 | MARKET 12.0% | 09:00 median 7.00 | Matchbook 8.00
    DATA: model 11.8% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 19 Jun Market Rasen Hurdle 20.6f Good 1/10; 18 Jul Market Rasen Hurdle 20.6f Good 4/12
    DATA for: Has won at this trip or further
    DATA against: Returns from a 128-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- Lewisham Grove (hrs_50188915) | 5yo G | 166lb | OR 118 | draw 0 | jockey William Shanahan(5) | trainer Jennie Candlish (14d 4/24) | headgear - | last run 13 days | form 2152-V | MARKET 8.0% | 09:00 median 9.50 | Matchbook 13.00
    comment: Lewisham Grove booked a second two starts back after a win four runs ago, and he's fit again after just 13 days off, with experience of today's trip. The main risk is the 166 lb burden, which asks plenty even off an official mark of 118.
    DATA: model 9.5% | style Leader (led 38% of runs) | runs in data 3 | last 3: 15 Jan Newcastle Hurdle 20.3f Good To Soft 1/16; 31 Jan Musselburgh Hurdle 23.8f Good To Soft 5/5; 13 Mar Doncaster Hurdle 16.6f Good To Soft 2/4
    DATA for: Official rating 118, 8 lb above field average; Has won at this trip or further; Good recent finishing positions
    DATA against: Carries 8 lb more than average; Race comments mention jumping mistakes in 2 of its last 3 runs; Pace: likely to be taken on for the lead
- Dirty Den (hrs_37702336) | 6yo G | 159lb | OR 111 | draw 0 | jockey Callum Pritchard | trainer Syd Hosie (14d 2/10) | headgear tp | wind surgery | last run 215 days | form 31763- | MARKET 7.9% | 09:00 median 11.00 | Matchbook 12.00
    comment: Third last time out and a winner four starts back, Dirty Den has run over today's trip and going, but he returns after 215 days off and carries 159 lb.
    DATA: model 9.9% | style Held up (led 4% of runs) | runs in data 4 | last 3: 25 Feb Wincanton Hurdle 19.8f Good To Soft 7/15; 27 Mar Wetherby Hurdle 21.3f Good 6/16; 22 Apr Taunton Hurdle 19f Good 3/9
    DATA for: Trainer 20% wins (2/10), last 14 days; Has won at this trip or further; Pace: a contested lead should suit its hold-up style
    DATA against: Returns from a 215-day break
- Beau Quali (hrs_45950695) | 6yo G | 162lb | OR 114 | draw 0 | jockey Sean Bowen | trainer Christian Williams (14d 1/7) | headgear p | last run 23 days | form 21-509 | MARKET 7.0% | 09:00 median 11.00 | Matchbook 15.00
    DATA: model 5.2% | style Prominent (led 5% of runs) | runs in data 7 | last 3: 16 May Uttoxeter Hurdle 19.9f Good 5/8; 9 Oct Chepstow Hurdle 19.5f Good To Soft 14/15; 31 Oct Ascot Hurdle 19.5f Good To Firm 9/9
    DATA for: Has won at this trip or further
    DATA against: Last-run finishing speed -4.7% vs that field (faded)
- Faded Fantasy (hrs_29621662) | 7yo G | 143lb | OR 95 | draw 0 | jockey Mr J. J. Murphy-Knight(7) | trainer Christian Williams (14d 1/7) | headgear - | last run 37 days | form 854803 | MARKET 6.2% | 09:00 median 13.00 | Matchbook 16.50
    comment: Winless in his last six, Faded Fantasy is hard to fancy, though a third last time out is a more encouraging effort after a run of mid-field finishes, and he has run over today's trip and going.
    DATA: model 5.8% | style Midfield (led 23% of runs) | runs in data 8 | last 3: 15 Sep Uttoxeter Hurdle 19.9f Good 8/12; 10 Oct Chepstow Hurdle 23.6f Good To Soft 11/17; 17 Oct Newton Abbot Hurdle 21.5f Good 3/6 fig 94
    DATA for: Carries 15 lb less than average
    DATA against: Official rating 95, 15 lb below field average
- Kentucky River (hrs_46759174) | 4yo G | 158lb | OR 111 | draw 0 | jockey Robert Dunne | trainer Olly Murphy (14d 10/50) | headgear p | last run 20 days | form 71-91P | MARKET 5.6% | 09:00 median 15.50 | Matchbook 16.50
    comment: Pulled up last time out, Kentucky River is hard to fancy after a patchy run of form, though he did win two starts back and again four starts back, and has run over today's trip and going.
    DATA: model 8.5% | style Midfield (led 8% of runs) | runs in data 8 | last 3: 3 Jun Warwick Hurdle 19f Good 1/5; 31 Jul Goodwood Flat 20.6f Good To Firm 12/15; 3 Nov Warwick Hurdle 21f Good PU/10
    DATA for: Trainer 20% wins (10/50), last 14 days; Has won at this trip or further
    DATA against: Pulled up in 1 of its last 5 jumps runs
- Devon Skies (hrs_40592188) | 7yo M | 151lb | OR 103 | draw 0 | jockey Joe Williamson | trainer Philip Kirby (14d 1/9) | headgear - | last run 233 days | form 1P144- | MARKET 2.0% | 09:00 median 41.00 | Matchbook 60.00
    comment: Two fourths since a win three starts back look respectable, but Devon Skies returns after 233 days off, which makes her hard to fancy. In her favour, she carries 151 lb, she has run over today's trip and going before, and she won twice in her last five starts.
    DATA: model 8.1% | style Leader (led 79% of runs) | runs in data 3 | last 3: 30 Jan Catterick Hurdle 19.3f Soft 1/7; 26 Feb Wetherby Hurdle 19.7f Soft 4/6; 4 Apr Carlisle Hurdle 19.3f Good 4/4
    DATA for: Has won at this trip or further; Carries 7 lb less than average
    DATA against: Official rating 103, 7 lb below field average; Last-run finishing speed -4.4% vs that field (faded); Returns from a 233-day break; Pace: likely to be taken on for the lead
