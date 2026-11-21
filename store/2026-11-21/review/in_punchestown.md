# Card review packet: Punchestown, 2026-11-21

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
{"meeting": "punchestown", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 11:53 Punchestown | race_id rac_32305289302 | Sebden Steel Maiden Hurdle
Hurdle |  | 2m3f87y | going Good To Yielding | Turf | 24 runners | rating band - | age 4yo
DATA pace: Unclear - Running styles known for only 10 of 24 runners.
- Delamotte (hrs_64135204) | 4yo G | 161lb | OR - | draw 0 | jockey Paul Townend | trainer W. P. Mullins (14d 6/23) | headgear - | last run 207 days | form 1- | MARKET 38.6% | 09:00 median 1.53 | Matchbook 1.89
    DATA: model 13.6% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 28 Apr Punchestown NH Flat 16.6f Yielding 1/18
    DATA for: Trainer 26% wins (6/23), last 14 days; Last-run finishing speed +8.0% vs that field (finished strongly)
    DATA against: Returns from a 207-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Kingstonian (hrs_43860026) | 4yo G | 161lb | OR - | draw 0 | jockey J. J. Slevin | trainer Joseph Patrick O'Brien (14d 3/27) | headgear - | last run 29 days | form 32 | MARKET 16.6% | 09:00 median 3.50 | Matchbook 4.40
    DATA: model 7.6% | style Prominent (led 3% of runs) | runs in data 6 | last 3: 22 Aug Killarney Hurdle 16.5f Good 3/16; 27 Sep Curragh Flat 16.8f Heavy 10/30; 23 Oct Cheltenham Hurdle 20f Good To Soft 2/7 fig 117
    DATA for: Best recent form figure 117, 5 lb above field average; Good recent finishing positions
- Brady Hartsfield (hrs_61684525) | 4yo G | 161lb | OR - | draw 0 | jockey Alex Harvey | trainer John McConnell (14d 0/15) | headgear - | last run 14 days | form 226-2 | MARKET 5.8% | 09:00 median 8.50 | Matchbook 15.00
    DATA: model 6.4% | style Prominent (led 3% of runs) | runs in data 4 | last 3: 22 Mar Limerick NH Flat 16.2f Soft To Heavy 2/7; 18 Apr Ayr NH Flat 16f Heavy 6/9; 7 Nov Gowran Park (IRE) Hurdle 16f Good To Yielding 2/12 fig 107
    DATA for: Good recent finishing positions
    DATA against: Best recent form figure 107, 5 lb below field average; Trainer 0 wins from 15 runs, last 14 days
- Menethil (hrs_17395151606) | 4yo G | 161lb | OR - | draw 0 | jockey Jack Kennedy | trainer Gordon Elliott (14d 11/68) | headgear - | last run 266 days | form 2- | MARKET 5.8% | 09:00 median 11.00 | Matchbook 12.00
    DATA: model 3.6% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 266-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Way With Words (hrs_61456150) | 4yo G | 161lb | OR - | draw 0 | jockey Mark Walsh | trainer J P Dempsey (14d 0/4) | headgear - | last run 46 days | form 2-2 | MARKET 4.8% | 09:00 median 12.00 | Matchbook 16.50
    DATA: model 7.8% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 2 Mar Leopardstown NH Flat 16f Soft To Heavy 2/8; 6 Oct Galway NH Flat 16.6f Yielding To Soft 2/8
    DATA for: Good recent finishing positions
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; First run over hurdles in our data
- Bacharach (hrs_63202685) | 4yo G | 161lb | OR - | draw 0 | jockey Keith Donoghue | trainer Gavin Cromwell (14d 4/37) | headgear t | last run 20 days | form 0-252 | MARKET 3.5% | 09:00 median 13.00 | Matchbook 29.00
    DATA: model 5.3% | style Prominent (led 3% of runs) | runs in data 4 | last 3: 25 May Ballinrobe NH Flat 16.7f Good 2/11; 2 Jul Limerick NH Flat 16.5f Good 5/8; 1 Nov Cork (IRE) Hurdle 16f Good To Yielding 2/10 fig 111
    DATA for: Good recent finishing positions
- Irragh (hrs_61718335) | 4yo G | 161lb | OR - | draw 0 | jockey Eoghan Finegan(5) | trainer Gordon Elliott (14d 11/68) | headgear h (1st time) | last run - days | form - | MARKET 1.8% | 09:00 median 51.00 | Matchbook 6.00
    DATA: model 3.6% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: First-time headgear
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Wild Swan (hrs_17395857717) | 4yo F | 154lb | OR - | draw 0 | jockey Brian Hayes | trainer C A Murphy (14d 0/1) | headgear - | last run - days | form - | MARKET 1.7% | 09:00 median 34.00 | Matchbook 6.00
    DATA: model 3.2% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Kims Word (hrs_17395899437) | 4yo F | 154lb | OR - | draw 0 | jockey Donagh Meyler | trainer Ross O'Sullivan (14d 1/14) | headgear - | last run - days | form - | MARKET 1.7% | 09:00 median 81.00 | Matchbook 7.00
    DATA: model 3.2% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Gallows Hill (hrs_17395149520) | 4yo G | 161lb | OR - | draw 0 | jockey Shane O'Callaghan(3) | trainer T M Walsh (14d 0/1) | headgear - | last run - days | form - | MARKET 1.6% | 09:00 median 67.00 | Matchbook 6.60
    DATA: model 3.6% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Alto Rey (hrs_17395460334) | 4yo G | 161lb | OR - | draw 0 | jockey Ross Berry(7) | trainer C A Murphy (14d 0/1) | headgear - | last run - days | form - | MARKET 1.6% | 09:00 median 67.00 | Matchbook 7.00
    DATA: model 3.6% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Evening Stroll (hrs_17393941726) | 4yo F | 154lb | OR - | draw 0 | jockey Aidan Kelly | trainer Padraig Roche (14d 0/5) | headgear - | last run - days | form - | MARKET 1.6% | 09:00 median 126.00 | Matchbook 7.00
    DATA: model 3.2% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Galantacht (hrs_17395854588) | 4yo F | 154lb | OR - | draw 0 | jockey Mike O'Connor | trainer Ross O'Sullivan (14d 1/14) | headgear - | last run - days | form - | MARKET 1.6% | 09:00 median 81.00 | Matchbook 7.00
    DATA: model 3.2% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Banada Breeze (hrs_17395898394) | 4yo F | 154lb | OR - | draw 0 | jockey  | trainer Mrs Denise Foster (14d 0/1) | headgear - | last run - days | form - | MARKET 1.6% | 09:00 median 101.00 | Matchbook 7.00
    DATA: model 3.2% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Toye Stud (hrs_17394711460) | 4yo G | 161lb | OR - | draw 0 | jockey Sean Flanagan | trainer C A McBratney (14d 0/2) | headgear - | last run - days | form - | MARKET 1.5% | 09:00 median 126.00 | Matchbook 7.00
    DATA: model 3.6% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Clean As A Whistle (hrs_17395853545) | 4yo G | 161lb | OR - | draw 0 | jockey  | trainer J Motherway (14d 0/2) | headgear - | last run 273 days | form P- | MARKET 1.5% | 09:00 median 126.00 | Matchbook 7.00
    DATA: model 3.6% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 273-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Smuggle The Tin (hrs_17394405861) | 4yo G | 161lb | OR - | draw 0 | jockey Richard Deegan | trainer S Slevin (14d 0/0) | headgear - | last run - days | form - | MARKET 1.4% | 09:00 median 151.00 | Matchbook 7.00
    DATA: model 3.6% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Strategic (hrs_62813100) | 4yo G | 161lb | OR - | draw 0 | jockey Kevin Healy(7) | trainer Gordon Elliott (14d 11/68) | headgear t (1st time) | last run 207 days | form 0- | MARKET 1.4% | 09:00 median 151.00 | Matchbook 7.00
    DATA: model 3.5% | style Held up (led 8% of runs) | runs in data 1 | last 3: 28 Apr Punchestown NH Flat 16.6f Yielding 18/19
    DATA for: First-time headgear
    DATA against: Last-run finishing speed -18.8% vs that field (faded); Returns from a 207-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Hetty Parker (hrs_17391026541) | 4yo F | 154lb | OR - | draw 0 | jockey  | trainer J P Dempsey (14d 0/4) | headgear - | last run 94 days | form 6 | MARKET 1.4% | 09:00 median 151.00 | Matchbook 7.00
    DATA: model 1.4% | style Held up (led 8% of runs) | runs in data 1 | last 3: 19 Aug Sligo NH Flat 18.6f Good 6/8
    DATA against: Returns from a 94-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Dooks (hrs_63171682) | 4yo G | 161lb | OR - | draw 0 | jockey Kieren Buckley | trainer Gordon Elliott (14d 11/68) | headgear - | last run 207 days | form 40- | MARKET 1.2% | 09:00 median 67.00 | Matchbook 5.70
    DATA: model 3.3% | style Held up (led 5% of runs) | runs in data 2 | last 3: 2 Apr Clonmel Hurdle 15.9f Soft 4/7; 28 Apr Punchestown NH Flat 16.6f Yielding 16/19
    DATA against: Last-run finishing speed -5.6% vs that field (faded); Returns from a 207-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- Striking Distance (hrs_17395900480) | 4yo F | 154lb | OR - | draw 0 | jockey Daniel King | trainer Ross O'Sullivan (14d 1/14) | headgear - | last run 216 days | form F33- | MARKET 1.2% | 09:00 median 67.00 | Matchbook 6.60
    DATA: model 3.2% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 216-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Calle Lorio (hrs_17395852502) | 4yo G | 161lb | OR - | draw 0 | jockey Ricky Doyle | trainer C A Murphy (14d 0/1) | headgear - | last run - days | form - | MARKET 1.1% | 09:00 median 51.00 | Matchbook 6.60
    DATA: model 3.6% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- What About Max (hrs_17393942769) | 4yo G | 161lb | OR - | draw 0 | jockey Danny Mullins | trainer Brian Hassett (14d 0/1) | headgear - | last run 26 days | form U | MARKET 0.6% | 09:00 median 201.00 | Matchbook 7.00
    DATA: model 1.4% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 26 Oct Galway (IRE) Hurdle 16.5f Soft To Heavy UR/20
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on; Fell or unseated in 1 of its last 1 jumps runs
- Blaze Of Honour (hrs_64590624) | 4yo G | 161lb | OR - | draw 0 | jockey Thomas O'Connor(7) | trainer J. R. Finn (14d 0/0) | headgear - | last run 20 days | form 596 | MARKET 0.4% | 09:00 median 201.00 | Matchbook 7.00
    DATA: model 1.7% | style Held up (led 4% of runs) | runs in data 3 | last 3: 12 May Sligo NH Flat 17.8f Good 5/15; 29 May Tramore NH Flat 16f Good 9/11; 1 Nov Cork (IRE) Hurdle 16f Good To Yielding 6/10

## 12:28 Punchestown | race_id rac_32305291239 | Conway Piling Beginners Steeplechase
Chase |  | 2m2f200y | going Good To Yielding | Turf | 21 runners | rating band - | age 4yo+
DATA pace: Strong pace - 8 habitual front-runners (Bokamsin, Eternal Reward, Goldinthemountains, Heads Up, Mighty Park, Road Exile, Tip Of The Wings, He Can't Dance). A contested lead should set things up for horses coming from behind.
- Mighty Park (hrs_52055465) | 5yo G | 166lb | OR - | draw 0 | jockey Mark Walsh | trainer W. P. Mullins (14d 6/23) | headgear - | last run 256 days | form 2/19- | MARKET 32.1% | 09:00 median 2.25 | Matchbook 2.48
    comment: Mighty Park won two starts back and was runner-up the run before, but he was only ninth last time out and returns after 256 days off, so fitness is a question; the yard's form (6/23 in the last 14 days) is a plus, though 166 lb is a hefty burden.
    DATA: model 7.3% | style Leader (led 38% of runs) | runs in data 2 | last 3: 15 Jan Fairyhouse Hurdle 16f Soft 1/16; 10 Mar Cheltenham Hurdle 16.4f Good To Soft 9/11
    DATA for: Trainer 26% wins (6/23), last 14 days
    DATA against: Last-run finishing speed -2.8% vs that field (faded); Returns from a 256-day break; Lightly raced: 2 runs in our data, so the model has little to go on; First run over fences in our data; Pace: likely to be taken on for the lead
- Saint Baco (hrs_45314584) | 5yo G | 166lb | OR - | draw 0 | jockey Paul Townend | trainer W. P. Mullins (14d 6/23) | headgear - | last run 204 days | form 16F54- | MARKET 14.3% | 09:00 median 4.00 | Matchbook 7.00
    comment: Saint Baco brings a winner five starts back and a fourth last time out, while the yard is in form with 6 from 23 over the last 14 days, and he has run over today's trip.
    DATA: model 3.8% | style Prominent (led 4% of runs) | runs in data 4 | last 3: 11 Mar Cheltenham Hurdle 21f Good F/21; 5 Apr Fairyhouse Hurdle 20f Yielding To Soft 5/11; 1 May Punchestown Hurdle 20.6f Yielding 4/8
    DATA for: Trainer 26% wins (6/23), last 14 days
    DATA against: Returns from a 204-day break; Fell or unseated in 1 of its last 4 jumps runs; First run over fences in our data
- Heads Up (hrs_412692994) | 6yo G | 166lb | OR 133 | draw 0 | jockey Danny Mullins | trainer John McConnell (14d 0/15) | headgear - | last run 22 days | form 251P-1 | MARKET 12.8% | 09:00 median 5.00 | Matchbook 7.00
    comment: He has run on today's going and carries 166 lb, though a pulled up two starts back is the one blemish.
    DATA: model 9.0% | style Leader (led 79% of runs) | runs in data 4 | last 3: 15 Feb Punchestown Hurdle 15.8f Heavy 1/4; 5 Apr Fairyhouse Hurdle 16f Yielding To Soft PU/7; 30 Oct Down Royal (IRE) Hurdle 17f Good To Yielding 1/4 fig 141
    DATA for: Best recent form figure 141, 28 lb above field average
    DATA against: Trainer 0 wins from 15 runs, last 14 days; Race comments mention jumping mistakes in 2 of its last 4 runs; Pulled up in 1 of its last 4 jumps runs; First run over fences in our data; Pace: likely to be taken on for the lead
- Laurets d'Estruval (hrs_58900548) | 5yo G | 166lb | OR - | draw 0 | jockey Daniel King | trainer W. P. Mullins (14d 6/23) | headgear - | last run 203 days | form /2106- | MARKET 7.3% | 09:00 median 9.50 | Matchbook 11.50
    comment: Laurets d'Estruval won three starts back and was a second four starts back, so the ability is there, and his trainer is in form with 6 from 23 over the last 14 days.
    DATA: model 3.9% | style Prominent (led 5% of runs) | runs in data 3 | last 3: 5 Feb Thurles Hurdle 16.2f Soft 1/17; 11 Mar Cheltenham Hurdle 21f Good 11/21; 2 May Punchestown Hurdle 20.5f Yielding 6/17
    DATA for: Trainer 26% wins (6/23), last 14 days
    DATA against: Returns from a 203-day break; First run over fences in our data
- Road Exile (hrs_46697259) | 6yo G | 166lb | OR - | draw 0 | jockey Jack Kennedy | trainer Gordon Elliott (14d 11/68) | headgear - | last run 253 days | form /312P- | MARKET 6.0% | 09:00 median 11.00 | Matchbook 14.50
    comment: Road Exile won three starts back and was a second two runs ago, but he was pulled up last time out and returns after 253 days off.
    DATA: model 3.8% | style Leader (led 38% of runs) | runs in data 2 | last 3: 11 Jan Punchestown Hurdle 16.6f Soft 2/3; 13 Mar Cheltenham Hurdle 24f Good To Soft PU/22
    DATA against: Returns from a 253-day break; Lightly raced: 2 runs in our data, so the model has little to go on; Pulled up in 1 of its last 2 jumps runs; First run over fences in our data; Pace: likely to be taken on for the lead
- Raise You Up (hrs_50906058) | 5yo G | 166lb | OR - | draw 0 | jockey  | trainer Ross O'Sullivan (14d 1/14) | headgear - | last run 206 days | form 21141- | MARKET 3.6% | 09:00 median 17.00 | Matchbook 30.00
    DATA: model 8.5% | style Prominent (led 5% of runs) | runs in data 3 | last 3: 7 Feb Naas Hurdle 18.5f Soft To Heavy 1/5; 4 Mar Naas Hurdle 16f Soft To Heavy 4/7; 29 Apr Punchestown Hurdle 19.3f Yielding 1/14
    DATA for: Last-run finishing speed +5.6% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Returns from a 206-day break; First run over fences in our data
- Fierce Handay (hrs_40494167) | 6yo G | 166lb | OR - | draw 0 | jockey Donagh Meyler | trainer Noel Meade (14d 3/12) | headgear - | last run 17 days | form 461P-4 | MARKET 3.4% | 09:00 median 21.00 | Matchbook 25.00
    comment: Fierce Handay was fourth last time out just 17 days ago and has run on today's going, but a pulled up two starts back sits awkwardly beside a win three starts back.
    DATA: model 5.2% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 6 Apr Fairyhouse Hurdle 21.5f Yielding To Soft 1/15; 2 May Punchestown Hurdle 20.5f Yielding PU/17; 4 Nov Wexford (IRE) Chase 15.5f Yielding 4/9 fig 116
    DATA for: Trainer 25% wins (3/12), last 14 days; Has won at this trip or further
    DATA against: Pulled up in 1 of its last 5 jumps runs
- Powerful (hrs_48886271) | 5yo G | 166lb | OR - | draw 0 | jockey Simon Torrens | trainer Mrs J. Harrington (14d 1/11) | headgear - | last run 207 days | form 18181- | MARKET 3.4% | 09:00 median 21.00 | Matchbook 26.00
    comment: Powerful won last time out and has three wins in his last five starts, a first and a third-from-back win alternating with two eighths, and he has run over today's trip.
    DATA: model 6.9% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 11 Jan Punchestown Hurdle 20.8f Soft To Heavy 1/15; 4 Apr Fairyhouse Hurdle 16f Yielding To Soft 8/18; 28 Apr Punchestown Hurdle 19.4f Yielding 1/24
    DATA for: Last-run finishing speed +5.1% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Returns from a 207-day break; First run over fences in our data
- He Can't Dance (hrs_39431644) | 6yo G | 166lb | OR - | draw 0 | jockey  | trainer Gordon Elliott (14d 11/68) | headgear tb | last run 201 days | form 3321-1 | MARKET 2.7% | 09:00 median 26.00 | Matchbook 34.00
    comment: He Can't Dance arrives in cracking form, a winner last time out and again two starts back, with a second and two thirds before that, and he has run over today's trip and going.
    DATA: model 11.0% | style Leader (led 23% of runs) | runs in data 5 | last 3: 4 Apr Fairyhouse Hurdle 20f Yielding To Soft 2/25; 16 Apr Limerick Hurdle 24f Soft To Heavy 1/7; 4 May Down Royal Hurdle 24f Good 1/6
    DATA for: Last-run finishing speed +7.6% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Returns from a 201-day break; First run over fences in our data; Pace: likely to be taken on for the lead
- Tip Of The Wings (hrs_50433103) | 5yo G | 166lb | OR - | draw 0 | jockey Josh Williamson(3) | trainer Gordon Elliott (14d 11/68) | headgear p | last run 231 days | form 3612P- | MARKET 1.9% | 09:00 median 41.00 | Matchbook 50.00
    comment: Pulled up last time out and off the track for 231 days, Tip Of The Wings is hard to fancy, and 166 lb is a hefty burden; still, he has run on today's going, and a second two starts back, with a win three starts back, shows he can perform.
    DATA: model 3.8% | style Leader (led 29% of runs) | runs in data 3 | last 3: 10 Feb Limerick Hurdle 15.7f Heavy 1/5; 4 Mar Naas Hurdle 16f Soft To Heavy 2/7; 4 Apr Fairyhouse Hurdle 23.8f Yielding To Soft PU/20
    DATA against: Returns from a 231-day break; Race comments mention jumping mistakes in 3 of its last 3 runs; Pulled up in 1 of its last 3 jumps runs; First run over fences in our data; Pace: likely to be taken on for the lead
- Bertutea (hrs_47531505) | 4yo G | 158lb | OR - | draw 0 | jockey Brian Hayes | trainer W. P. Mullins (14d 6/23) | headgear t | last run 13 days | form 1P07-F | MARKET 1.6% | 09:00 median 41.00 | Matchbook 65.00
    comment: Bertutea fell last time out and was seventh two starts back, so recent form is patchy, though he did win five starts back and returns quickly after 13 days.
    DATA: model 1.9% | style Midfield (led 3% of runs) | runs in data 4 | last 3: 10 Mar Cheltenham Hurdle 16.4f Good To Soft 17/22; 2 May Punchestown Hurdle 16f Yielding 7/12; 8 Nov Naas (IRE) Chase 16f Good To Yielding F/8
    DATA for: Trainer 26% wins (6/23), last 14 days
    DATA against: Poor recent finishing positions; Fell or unseated in 1 of its last 4 jumps runs; Pulled up in 1 of its last 4 jumps runs
- Bokamsin (hrs_51091068) | 6yo G | 166lb | OR - | draw 0 | jockey Mike O'Connor | trainer Henry de Bromhead (14d 9/39) | headgear t | last run 231 days | form 35410- | MARKET 1.6% | 09:00 median 41.00 | Matchbook 75.00
    comment: On the plus side, he won two starts back, and he has run over today's trip.
    DATA: model 3.8% | style Leader (led 29% of runs) | runs in data 3 | last 3: 26 Jan Punchestown Hurdle 19f Heavy 4/5; 4 Mar Naas Hurdle 16f Soft To Heavy 1/7; 4 Apr Fairyhouse Hurdle 16f Yielding To Soft 16/18
    DATA for: Trainer 23% wins (9/39), last 14 days
    DATA against: Last-run finishing speed -5.4% vs that field (faded); Returns from a 231-day break; Race comments mention jumping mistakes in 2 of its last 3 runs; First run over fences in our data; Pace: likely to be taken on for the lead
- Goldinthemountains (hrs_35232204) | 7yo G | 166lb | OR - | draw 0 | jockey Conor Brassil(3) | trainer Martin Brassil (14d 1/4) | headgear t | last run 221 days | form F9/63- | MARKET 1.5% | 09:00 median 51.00 | Matchbook 70.00
    comment: Third last time out, he has since had a long 221-day break, and that layoff plus a sixth and a ninth before it keeps this midfield type in check.
    DATA: model 5.3% | style Leader (led 57% of runs) | runs in data 1 | last 3: 14 Apr Clonmel Chase 15.6f Yielding 3/9
    DATA for: Last-run finishing speed +3.5% vs that field (finished strongly)
    DATA against: Returns from a 221-day break; Lightly raced: 1 run in our data, so the model has little to go on; Pace: likely to be taken on for the lead
- County Final (hrs_52677499) | 6yo G | 166lb | OR - | draw 0 | jockey Aidan Kelly | trainer E McNamara (14d 0/11) | headgear t | last run 26 days | form 2P08-5 | MARKET 1.3% | 09:00 median 51.00 | Matchbook 80.00
    comment: County Final was a fifth last time out, but he is winless in his last five and has been in retreat since a second five starts back, with an eighth and a pulled up in between.
    DATA: model 2.7% | style Held up (led 4% of runs) | runs in data 4 | last 3: 5 Apr Cork Hurdle 19f Yielding 13/19; 2 May Punchestown Hurdle 20.5f Yielding 8/17; 26 Oct Galway (IRE) Chase 18f Heavy 5/7 fig 114
    DATA for: Pace: a contested lead should suit its hold-up style
    DATA against: Trainer 0 wins from 11 runs, last 14 days; Pulled up in 1 of its last 4 jumps runs
- Saveforarainyday (hrs_50188831) | 5yo M | 159lb | OR - | draw 0 | jockey Conor Stone-Walsh | trainer Gavin Cromwell (14d 4/37) | headgear h | last run 17 days | form 4100-5 | MARKET 1.3% | 09:00 median 67.00 | Matchbook 80.00
    comment: Saveforarainyday is hard to fancy after a fifth last time out and two unplaced runs before that, with her win coming four starts back; she's fresh enough after 17 days and sheds nothing off 159 lb.
    DATA: model 3.4% | style Held up (led 5% of runs) | runs in data 4 | last 3: 6 Apr Fairyhouse Hurdle 16f Yielding To Soft 12/21; 1 May Punchestown Hurdle 16.2f Yielding 11/24; 4 Nov Wexford (IRE) Chase 15.5f Yielding 5/9 fig 107
    DATA for: Pace: a contested lead should suit its hold-up style
    DATA against: Best recent form figure 107, 6 lb below field average
- Eternal Reward (hrs_51185883) | 5yo G | 166lb | OR - | draw 0 | jockey J. J. Slevin | trainer Ms Margaret Mullins (14d 0/2) | headgear - | last run 14 days | form F-0612 | MARKET 1.1% | 09:00 median 67.00 | Matchbook 75.00
    DATA: model 4.0% | style Leader (led 43% of runs) | runs in data 4 | last 3: 3 Sep Kilbeggan Hurdle 19f Good To Yielding 6/8; 1 Oct Clonmel Hurdle 19.7f Good 1/11; 7 Nov Gowran Park (IRE) Chase 20f Good 2/10 fig 109
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Race comments mention jumping mistakes in 2 of its last 4 runs; Pace: likely to be taken on for the lead
- Tackletommywoowoo (hrs_412652905) | 6yo G | 166lb | OR - | draw 0 | jockey Sean Flanagan | trainer Paul Nolan (14d 3/12) | headgear - | last run 17 days | form 170-89 | MARKET 1.0% | 09:00 median 67.00 | Matchbook 120.00
    comment: Tackletommywoowoo has slipped since winning five starts back, finishing a ninth last time out and an eighth before that, though he has run over today's trip and going and returns after 17 days.
    DATA: model 2.3% | style Held up (led 3% of runs) | runs in data 4 | last 3: 13 Mar Cheltenham Hurdle 24f Good To Soft 10/22; 24 Sep Listowel Chase 22f Good 8/11; 4 Nov Wexford (IRE) Chase 15.5f Yielding 9/9 fig 101
    DATA for: Trainer 25% wins (3/12), last 14 days; Pace: a contested lead should suit its hold-up style
    DATA against: Best recent form figure 101, 12 lb below field average; Poor recent finishing positions
- Avalo (hrs_38649604) | 7yo G | 166lb | OR - | draw 0 | jockey Ethan O'Sullivan(7) | trainer Peter Fahey (14d 3/4) | headgear - | last run 38 days | form 1-0255 | MARKET 0.9% | 09:00 median 81.00 | Matchbook 120.00
    comment: Avalo has finished fifth in each of his last two starts, with a second three runs back, and he has run over today's trip and going before.
    DATA: model 7.5% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 26 Aug Bellewstown Hurdle 20.5f Good 2/11; 26 Sep Listowel Hurdle 20f Good 5/14; 14 Oct Punchestown (IRE) Hurdle 20f Good 5/13 fig 117
    DATA for: Best recent form figure 117, 4 lb above field average
    DATA against: First run over fences in our data
- Arkhill (hrs_50188600) | 7yo G | 166lb | OR - | draw 0 | jockey Mr L P Shanahan(7) | trainer Ross O'Sullivan (14d 1/14) | headgear - | last run 180 days | form 15/F-8 | MARKET 0.8% | 09:00 median 151.00 | Matchbook 120.00
    comment: Arkhill is hard to fancy after a 180-day absence, with an eighth last time out and a fall two starts back, though he did win four starts back and a fifth before that hints at some ability.
    DATA: model 1.6% | style Held up (led 8% of runs) | runs in data 1 | last 3: 25 May Ballinrobe Chase 17.2f Good 8/12
    DATA for: Pace: a contested lead should suit its hold-up style
    DATA against: Returns from a 180-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Take Stock (hrs_51341752) | 5yo G | 166lb | OR - | draw 0 | jockey Keith Donoghue | trainer Gavin Cromwell (14d 4/37) | headgear - | last run 17 days | form 3F51-6 | MARKET 0.7% | 09:00 median 126.00 | Matchbook 140.00
    DATA: model 3.4% | style Held up (led 3% of runs) | runs in data 5 | last 3: 29 Mar Downpatrick Hurdle 21.8f Yielding To Soft 5/10; 18 Apr Bellewstown Hurdle 17.1f Yielding 1/12; 4 Nov Wexford (IRE) Chase 15.5f Yielding 6/9 fig 106
    DATA for: Pace: a contested lead should suit its hold-up style
    DATA against: Best recent form figure 106, 7 lb below field average; Fell or unseated in 1 of its last 5 jumps runs
- Rock On Richie (hrs_17394494516) | 6yo G | 166lb | OR - | draw 0 | jockey  | trainer Tom Dreaper (14d 0/3) | headgear - | last run 17 days | form 521-8 | MARKET 0.7% | 09:00 median 126.00 | Matchbook 140.00
    comment: Rock On Richie was beaten into eighth last time out, which makes him hard to fancy, though he won two starts back and was second three runs ago, so the ability is there.
    DATA: model 0.8% | style Unknown | runs in data 1 | last 3: 4 Nov Wexford (IRE) Chase 15.5f Yielding 8/9 fig 104
    DATA against: Best recent form figure 104, 9 lb below field average; Lightly raced: 1 run in our data, so the model has little to go on

## 1:03 Punchestown | race_id rac_32305293176 | Boodles Florida Pearl Novice Steeplechase (Grade 2)
Chase | Class 1 | 3m0f51y | going Good To Yielding | Turf | 7 runners | rating band - | age 5yo+
DATA pace: Lone leader - Chanceawetmorning is the only habitual front-runner and may be allowed an easy lead.
- Kiss Will (hrs_39678835) | 6yo G | 157lb | OR 138 | draw 0 | jockey Paul Townend | trainer W. P. Mullins (14d 6/23) | headgear - | last run 204 days | form 225F8- | MARKET 27.0% | 09:00 median 3.25 | Matchbook 3.60 | CHECK (skip line 3.09)
    DATA: model 16.3% | style Prominent (led 3% of runs) | runs in data 4 | last 3: 12 Mar Cheltenham Chase 20.6f Good 5/18; 6 Apr Fairyhouse Chase 29.1f Yielding To Soft F/30; 1 May Punchestown Chase 20.2f Yielding 8/22
    DATA for: Trainer 26% wins (6/23), last 14 days
    DATA against: Returns from a 204-day break; Fell or unseated in 1 of its last 4 jumps runs
- Ballygunner Castle (hrs_34788670) | 7yo G | 157lb | OR 146 | draw 0 | jockey Danny Mullins | trainer W. P. Mullins (14d 6/23) | headgear - | last run 59 days | form F24-01 | MARKET 26.1% | 09:00 median 3.50 | Matchbook 3.65
    DATA: model 21.0% | style Prominent (led 23% of runs) | runs in data 4 | last 3: 1 May Punchestown Chase 20.2f Yielding 4/22; 29 Jul Galway Chase 22.5f Good 18/22; 23 Sep Listowel Chase 23.8f Good 1/18
    DATA for: Official rating 146, 10 lb above field average; Trainer 26% wins (6/23), last 14 days; Last-run finishing speed +5.2% vs that field (finished strongly); Has won at this trip or further
- The Big Clubman (hrs_39431679) | 6yo G | 157lb | OR - | draw 0 | jockey Sean O'Keeffe | trainer Paul Nolan (14d 3/12) | headgear - | last run 17 days | form 2522-1 | MARKET 19.2% | 09:00 median 4.50 | Matchbook 5.20
    DATA: model 13.1% | style Prominent (led 4% of runs) | runs in data 3 | last 3: 27 Feb Newbury Hurdle 20.5f Good To Soft 2/6; 30 Apr Punchestown Hurdle 23.5f Yielding 2/24; 4 Nov Wexford (IRE) Chase 15.5f Yielding 1/9 fig 122
    DATA for: Trainer 25% wins (3/12), last 14 days; Good recent finishing positions
    DATA against: Best recent form figure 122, 4 lb below field average
- Chanceawetmorning (hrs_40514593) | 6yo G | 160lb | OR 137 | draw 0 | jockey Jack Kennedy | trainer Gordon Elliott (14d 11/68) | headgear - | last run 38 days | form 934F11 | MARKET 10.8% | 09:00 median 8.50 | Matchbook 9.00
    DATA: model 14.6% | style Leader (led 43% of runs) | runs in data 12 | last 3: 4 Sep Kilbeggan Chase 24f Good To Yielding F/4; 30 Sep Sligo Chase 21f Good 1/6; 14 Oct Punchestown (IRE) Chase 18.5f Good 1/4 fig 133
    DATA for: Best recent form figure 133, 7 lb above field average; Last-run finishing speed +7.0% vs that field (finished strongly); Pace: may get an uncontested lead
    DATA against: Fell or unseated in 1 of its last 5 jumps runs
- Largy Star (hrs_52236639) | 7yo G | 157lb | OR - | draw 0 | jockey Keith Donoghue | trainer Gavin Cromwell (14d 4/37) | headgear - | last run 204 days | form 11231- | MARKET 8.8% | 09:00 median 9.50 | Matchbook 12.00
    DATA: model 16.1% | style Prominent (led 29% of runs) | runs in data 3 | last 3: 25 Jan Naas NH Flat 18.7f Heavy 2/10; 4 Apr Fairyhouse Hurdle 20f Yielding To Soft 3/25; 1 May Punchestown NH Flat 18.8f Yielding 1/21
    DATA for: Last-run finishing speed +17.3% vs that field (finished strongly); Good recent finishing positions
    DATA against: Returns from a 204-day break; First run over fences in our data
- King's Bucks (hrs_47620958) | 6yo G | 157lb | OR - | draw 0 | jockey Mike O'Connor | trainer Henry de Bromhead (14d 9/39) | headgear - | last run 26 days | form 32P2-2 | MARKET 6.5% | 09:00 median 13.00 | Matchbook 16.50
    DATA: model 8.4% | style Prominent (led 4% of runs) | runs in data 3 | last 3: 13 Mar Cheltenham Hurdle 24f Good To Soft PU/22; 16 Apr Limerick Hurdle 24f Soft To Heavy 2/7; 26 Oct Galway (IRE) Chase 18f Heavy 2/7 fig 124
    DATA for: Trainer 23% wins (9/39), last 14 days
    DATA against: Race comments mention jumping mistakes in 2 of its last 3 runs; Pulled up in 1 of its last 3 jumps runs
- Lady Bluebird (hrs_35596246) | 9yo M | 150lb | OR 125 | draw 0 | jockey Donagh Meyler | trainer Hugh Paul Finegan (14d 0/4) | headgear - | last run 59 days | form 263122 | MARKET 1.7% | 09:00 median 61.00 | Matchbook 65.00
    DATA: model 10.5% | style Prominent (led 3% of runs) | runs in data 9 | last 3: 30 Jun Wexford Chase 19.5f Good 1/8; 30 Jul Galway Chase 18.2f Yielding To Soft 2/7; 23 Sep Listowel Chase 19f Good 2/6
    DATA for: Last-run finishing speed +3.4% vs that field (finished strongly); Good recent finishing positions
    DATA against: Official rating 125, 12 lb below field average; Aged 9, older than most of this field

## 1:38 Punchestown | race_id rac_32305295113 | Ryans Cleaning Handicap Steeplechase
Chase |  | 2m5f70y | going Good To Yielding | Turf | 10 runners | rating band - | age 4yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Letos (hrs_37860788) | 6yo G | 140lb | OR 122 | draw 0 | jockey Conor Stone-Walsh | trainer Noel Meade (14d 3/12) | headgear - | last run 203 days | form 12044- | MARKET 28.6% | 09:00 median 3.00 | Matchbook 3.35 | CHECK (skip line 2.85)
    comment: Letos has finished fourth in each of his last two starts, but he returns after 203 days off and hasn't won since five starts back. He has run over today's trip and on this going, and a second four starts back is a plus, though 140 lb looks a stiff ask.
    DATA: model 8.8% | style Prominent (led 4% of runs) | runs in data 3 | last 3: 9 Jan Naas Hurdle 20f Soft 10/10; 12 Mar Cheltenham Hurdle 24f Good 4/24; 2 May Punchestown Hurdle 20.5f Yielding 4/17
    DATA for: Trainer 25% wins (3/12), last 14 days; Carries 13 lb less than average
    DATA against: Official rating 122, 15 lb below field average; Returns from a 203-day break; First run over fences in our data
- Predators Gold (hrs_34788838) | 7yo G | 162lb | OR 146 | draw 0 | jockey Paul Townend | trainer W. P. Mullins (14d 6/23) | headgear - | last run 207 days | form /13F6- | MARKET 24.2% | 09:00 median 3.75 | Matchbook 3.75
    comment: The one risk is a 207-day absence and a sixth last time out, so he may need the run under 162 lb.
    DATA: model 12.1% | style Prominent (led 29% of runs) | runs in data 3 | last 3: 11 Jan Punchestown Chase 19.5f Soft 3/5; 5 Apr Fairyhouse Chase 20f Yielding To Soft F/8; 28 Apr Punchestown Chase 25f Yielding 6/9
    DATA for: Official rating 146, 9 lb above field average; Trainer 26% wins (6/23), last 14 days
    DATA against: Last-run finishing speed -2.3% vs that field (faded); Carries 9 lb more than average; Returns from a 207-day break; Fell or unseated in 1 of its last 3 jumps runs
- Its Bilbo (hrs_40075924) | 5yo G | 145lb | OR 129 | draw 0 | jockey Alan O'Sullivan(5) | trainer Henry de Bromhead (14d 9/39) | headgear - | last run 49 days | form 3103-2 | MARKET 16.5% | 09:00 median 5.00 | Matchbook 5.90
    comment: Its Bilbo bounces in off a second last time out and a third two starts back, with a win four starts back, though 49 days off the track and 145 lb on his back temper the enthusiasm.
    DATA: model 11.1% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 13 Mar Cheltenham Hurdle 20.3f Good To Soft 23/24; 5 Apr Cork Hurdle 19f Yielding 3/19; 3 Oct Gowran Park Chase 20f Good To Yielding 2/6
    DATA for: Trainer 23% wins (9/39), last 14 days; Good recent finishing positions; Carries 8 lb less than average
    DATA against: Official rating 129, 8 lb below field average
- Argento Boy (hrs_39021374) | 7yo G | 160lb | OR 144 | draw 0 | jockey Sean O'Keeffe | trainer W. P. Mullins (14d 6/23) | headgear - | last run 203 days | form 11742- | MARKET 8.6% | 09:00 median 9.00 | Matchbook 12.50
    comment: Argento Boy won twice in his last five starts and was second last time out, with a fourth two starts back, and he has run over today's trip and going before. A 203-day absence is the one real risk, though a yard in form (6/23 in the last 14 days) helps.
    DATA: model 16.9% | style Midfield (led 4% of runs) | runs in data 4 | last 3: 11 Mar Cheltenham Chase 25f Good 8/14; 6 Apr Fairyhouse Chase 29.1f Yielding To Soft 4/30; 2 May Punchestown Chase 24.5f Yielding 2/21
    DATA for: Official rating 144, 7 lb above field average; Trainer 26% wins (6/23), last 14 days; Has won at this trip or further
    DATA against: Carries 7 lb more than average; Returns from a 203-day break; Race comments mention jumping mistakes in 2 of its last 4 runs
- Pure Steel (hrs_40095986) | 6yo G | 159lb | OR 143 | draw 0 | jockey Mark Walsh | trainer James Joseph Mangan (14d 0/1) | headgear - | last run 205 days | form 151U4- | MARKET 5.2% | 09:00 median 15.00 | Matchbook 21.00
    comment: On the plus side, he won three and five starts back and was fourth last time out.
    DATA: model 7.1% | style Prominent (led 3% of runs) | runs in data 4 | last 3: 15 Feb Punchestown Chase 16.5f Heavy 1/4; 5 Apr Fairyhouse Chase 20f Yielding To Soft UR/8; 30 Apr Punchestown Chase 16.3f Yielding 4/5
    DATA for: Official rating 143, 6 lb above field average
    DATA against: Last-run finishing speed -8.8% vs that field (faded); Carries 6 lb more than average; Returns from a 205-day break; Race comments mention jumping mistakes in 2 of its last 4 runs; Fell or unseated in 1 of its last 4 jumps runs
- Joystick (hrs_34361551) | 7yo G | 155lb | OR 139 | draw 0 | jockey Brian Hayes | trainer W. P. Mullins (14d 6/23) | headgear - | last run 203 days | form 616PP- | MARKET 4.2% | 09:00 median 19.00 | Matchbook 24.00
    comment: Joystick won four starts back and has run over today's trip and going, though two pulled-up runs since and a 203-day absence are worth noting.
    DATA: model 8.4% | style Prominent (led 3% of runs) | runs in data 5 | last 3: 11 Mar Cheltenham Chase 25f Good 7/14; 6 Apr Fairyhouse Chase 29.1f Yielding To Soft PU/30; 2 May Punchestown Chase 24.5f Yielding PU/21
    DATA for: Trainer 26% wins (6/23), last 14 days; Has won at this trip or further
    DATA against: Poor recent finishing positions; Returns from a 203-day break; Race comments mention jumping mistakes in 3 of its last 5 runs; Pulled up in 2 of its last 5 jumps runs
- King Of Kingsfield (hrs_29012760) | 8yo G | 155lb | OR 139 | draw 0 | jockey Jack Kennedy | trainer Gordon Elliott (14d 11/68) | headgear tp | last run 115 days | form P66-59 | MARKET 4.1% | 09:00 median 19.00 | Matchbook 25.00
    DATA: model 5.3% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 11 Apr Aintree Chase 15.8f Good To Soft 6/8; 2 Jul Limerick Hurdle 16.5f Good 5/5; 29 Jul Galway Chase 22.5f Good 9/22
    DATA against: Returns from a 115-day break
- Goraibhmaithagat (hrs_39431994) | 6yo G | 152lb | OR 136 | draw 0 | jockey Simon Torrens | trainer C A Murphy (14d 0/1) | headgear - | last run 203 days | form 3129P- | MARKET 3.4% | 09:00 median 26.00 | Matchbook 29.00
    comment: Goraibhmaithagat won four starts back and was second three starts back, but he has since run a ninth and then pulled up last time out, and that 203-day absence raises fitness doubts.
    DATA: model 14.2% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 8 Mar Naas Chase 24.8f Soft To Heavy 2/15; 6 Apr Fairyhouse Chase 29.1f Yielding To Soft 9/30; 2 May Punchestown Chase 24.5f Yielding PU/21
    DATA against: Returns from a 203-day break; Race comments mention jumping mistakes in 4 of its last 5 runs; Pulled up in 1 of its last 5 jumps runs
- Talk In The Park (hrs_33165048) | 8yo G | 140lb | OR 119 | draw 0 | jockey Michael Kenneally(3) | trainer Ross O'Sullivan (14d 1/14) | headgear b | last run 27 days | form -P5042 | MARKET 3.3% | 09:00 median 26.00 | Matchbook 29.00
    comment: Winless in his last five, Talk In The Park bounced back with a second last time out after a fourth two starts back, and he has run over today's trip and going.
    DATA: model 9.8% | style Midfield (led 4% of runs) | runs in data 6 | last 3: 22 Aug Killarney Hurdle 22.4f Good 11/14; 26 Sep Listowel Chase 22f Good 4/13; 25 Oct Galway (IRE) Chase 22.5f Soft To Heavy 2/9 fig 118
    DATA for: Carries 13 lb less than average
    DATA against: Official rating 119, 18 lb below field average; Pulled up in 1 of its last 5 jumps runs
- Spanish Harlem (hrs_30614521) | 8yo G | 166lb | OR 150 | draw 0 | jockey Danny Mullins | trainer W. P. Mullins (14d 6/23) | headgear tp | last run 207 days | form PUPPP- | MARKET 2.0% | 09:00 median 34.00 | Matchbook 70.00
    comment: Spanish Harlem has been pulled up in four of his last five starts, unseating in the other, and returns after 207 days off, so the form gives little to go on. He has run on today's going, carries 166 lb off 150, and a yard in form (6/23 over 14 days) offers some encouragement.
    DATA: model 6.3% | style Prominent (led 23% of runs) | runs in data 4 | last 3: 21 Feb Fairyhouse Chase 26f Heavy PU/9; 11 Apr Aintree Chase 34.3f Good To Soft PU/34; 28 Apr Punchestown Chase 25f Yielding PU/9
    DATA for: Official rating 150, 13 lb above field average; Trainer 26% wins (6/23), last 14 days
    DATA against: Poor recent finishing positions; Carries 13 lb more than average; Returns from a 207-day break; Race comments mention jumping mistakes in 2 of its last 4 runs; Fell or unseated in 1 of its last 4 jumps runs; Pulled up in 3 of its last 4 jumps runs

## 2:10 Punchestown | race_id rac_32303495640 | William Hill Morgiana Hurdle (Grade 1)
Hurdle | Class 1 | 2m0f160y | going Good To Yielding | Turf | 4 runners | rating band - | age 4yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Lossiemouth (hrs_29690871) | 7yo M | 159lb | OR 162 | draw 0 | jockey Paul Townend | trainer W. P. Mullins (14d 6/23) | headgear - | last run 204 days | form 11211- | MARKET 86.1% | 09:00 median 1.10 | Matchbook 1.12
    comment: Lossiemouth has won four of her last five starts, including last time out and two starts back, with a second three starts back the only blip, and she has run over today's trip and going before.
    DATA: model 46.4% | style Prominent (led 4% of runs) | runs in data 3 | last 3: 1 Feb Leopardstown Hurdle 16f Heavy 2/5; 10 Mar Cheltenham Hurdle 16.4f Good To Soft 1/9; 1 May Punchestown Hurdle 16.2f Yielding 1/7
    DATA for: Official rating 162, 16 lb above field average; Trainer 26% wins (6/23), last 14 days; Last-run finishing speed +3.7% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Returns from a 204-day break
- William Munny (hrs_39169319) | 8yo G | 166lb | OR 152 | draw 0 | jockey Sean Flanagan | trainer Barry Connell (14d 0/6) | headgear h | last run 204 days | form 212/5- | MARKET 8.1% | 09:00 median 9.00 | Matchbook 15.50
    comment: William Munny makes plenty of appeal on form, with a win three starts back and a second two starts back before a fifth last time out, and he has run over today's trip and going before. The main risk is a 204-day absence, with 166 lb to carry.
    DATA: model 10.5% | style Held up (led 8% of runs) | runs in data 1 | last 3: 1 May Punchestown Hurdle 16.2f Yielding 5/7
    DATA for: Official rating 152, 6 lb above field average
    DATA against: Returns from a 204-day break; Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Blake (hrs_37275427) | 5yo G | 166lb | OR 139 | draw 0 | jockey Donagh Meyler | trainer Noel Meade (14d 3/12) | headgear p | last run 22 days | form 52F2-2 | MARKET 2.9% | 09:00 median 29.00 | Matchbook 42.00
    comment: Blake arrives in fine heart, a second last time out and another second two starts back, and he has run over today's trip and on this going before. Yet to win in his last five, he carries 166 lb off 139, which is the main risk.
    DATA: model 24.9% | style Midfield (led 3% of runs) | runs in data 6 | last 3: 28 Apr Punchestown Hurdle 16.6f Yielding 2/8; 27 Sep Curragh Flat 16.8f Heavy 8/30; 30 Oct Down Royal (IRE) Hurdle 17f Good To Yielding 2/4 fig 133
    DATA for: Trainer 25% wins (3/12), last 14 days; Good recent finishing positions
    DATA against: Official rating 139, 8 lb below field average; Fell or unseated in 1 of its last 5 jumps runs
- Ebony King (hrs_53808846) | 5yo G | 166lb | OR 133 | draw 0 | jockey Cian Quirke | trainer A. Slattery (14d 0/15) | headgear - | last run 49 days | form 11F2-F | MARKET 2.9% | 09:00 median 34.00 | Matchbook 36.00
    comment: Won two of his last five, and was second two starts back, and he has run over today's trip and going before; the main risk is that he fell last time out and has been off for 49 days, with 166 lb to carry.
    DATA: model 18.2% | style Held up (led 3% of runs) | runs in data 5 | last 3: 12 May Killarney Flat 14.2f Good 6/6; 25 Sep Listowel Flat 14f Good To Yielding 1/13; 3 Oct Gowran Park Hurdle 16.3f Good To Yielding F/5
    DATA against: Official rating 133, 14 lb below field average; Trainer 0 wins from 15 runs, last 14 days; Fell or unseated in 1 of its last 2 jumps runs; Pace: steady gallop likely, hard to come from off the pace

## 2:45 Punchestown | race_id rac_32305297050 | Total Event Rental 3-Y-O Hurdle
Hurdle |  | 1m7f187y | going Good To Yielding | Turf | 10 runners | rating band - | age 3yo
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Momentum Of Love (hrs_64488151) | 3yo F | 151lb | OR - | draw 0 | jockey Paul Townend | trainer W. P. Mullins (14d 6/23) | headgear - | last run 199 days | form 1 | MARKET 43.4% | 09:00 median 1.91 | Matchbook 2.06
    comment: Momentum Of Love won on her only recent start, so she looks unexposed and open to improvement, though she returns after 199 days off and carries 151 lb. Her trainer is in good form, with 6 winners from 23 in the last 14 days.
    DATA: model 6.7% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 26% wins (6/23), last 14 days
    DATA against: Returns from a 199-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Danny Power (hrs_17392533676) | 3yo G | 158lb | OR - | draw 0 | jockey Mark Walsh | trainer John Queally (14d 1/1) | headgear - | last run 39 days | form 12 | MARKET 18.6% | 09:00 median 4.50 | Matchbook 4.80
    comment: Danny Power arrives in cracking form, a second last time out and a winner two starts back, and he has run over today's trip and going before.
    DATA: model 31.9% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 20 Sep Listowel Hurdle 16f Good 1/11; 13 Oct Punchestown Hurdle 16.2f Good 2/9
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Rio De La Pampa (hrs_17395472850) | 3yo G | 152lb | OR - | draw 0 | jockey Jack Kennedy | trainer Gordon Elliott (14d 11/68) | headgear - | last run 111 days | form - | MARKET 13.4% | 09:00 median 5.50 | Matchbook 7.60
    comment: Rio De La Pampa is unexposed with no recorded form to go on, so he's open to improvement. He returns after 111 days off and carries 152 lb, which makes this a hard one to pin down.
    DATA: model 6.8% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 111-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Fits Perfect (hrs_57439347) | 3yo G | 152lb | OR - | draw 0 | jockey J. J. Slevin | trainer Joseph Patrick O'Brien (14d 3/27) | headgear - | last run 26 days | form 2 | MARKET 8.1% | 09:00 median 10.00 | Matchbook 11.50
    comment: Fits Perfect was second last time out and returns after 26 days, a nicely fresh gap, while he has run over today's trip before.
    DATA: model 14.4% | style Held up (led 4% of runs) | runs in data 3 | last 3: 25 Apr Limerick Flat 8.2f Yielding 12/15; 27 Jul Galway Flat 12.4f Good 8/15; 26 Oct Galway (IRE) Hurdle 16.5f Soft To Heavy 2/10 fig 99
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Sounds Great (hrs_58133446) | 3yo F | 145lb | OR - | draw 0 | jockey Simon Torrens | trainer Mrs J. Harrington (14d 1/11) | headgear - | last run 32 days | form - | MARKET 6.1% | 09:00 median 13.00 | Matchbook 16.00
    comment: Sounds Great is unexposed, with no recorded form to go on, so she is open to improvement. She returns after 32 days off and carries 145 lb, and there is little to judge her on beyond that.
    DATA: model 8.7% | style Midfield (led 3% of runs) | runs in data 4 | last 3: 27 Apr Naas Flat 10.4f Good 7/9; 5 Oct Killarney Flat 11.2f Soft 3/7; 20 Oct Curragh (IRE) Flat 12f Yielding 2/7 fig 70
    DATA for: Good recent finishing positions
    DATA against: First run over hurdles in our data
- Fallacy (hrs_58065518) | 3yo G | 152lb | OR - | draw 0 | jockey Mr A P Ryan(3) | trainer A. Slattery (14d 0/15) | headgear - | last run 162 days | form - | MARKET 5.4% | 09:00 median 15.00 | Matchbook 18.00
    comment: Fallacy is effectively unexposed, with no recorded form to go on, so any improvement is there to be found. He returns after 162 days off and carries 152 lb, which is a stiff burden for one so lightly raced.
    DATA: model 13.5% | style Prominent (led 29% of runs) | runs in data 3 | last 3: 24 Apr Cork Flat 8f Good To Yielding 8/8; 16 May Navan Flat 10.2f Yielding 3/7; 12 Jun Gowran Park Flat 9.5f Yielding 1/5
    DATA for: Last-run finishing speed +2.7% vs that field (finished strongly); Good recent finishing positions
    DATA against: Trainer 0 wins from 15 runs, last 14 days; Returns from a 162-day break; First run over hurdles in our data
- Glorious Day (hrs_7000005040) | 3yo G | 158lb | OR - | draw 0 | jockey Keith Donoghue | trainer Gavin Cromwell (14d 4/37) | headgear - | last run 129 days | form 71 | MARKET 3.9% | 09:00 median 19.00 | Matchbook 27.00
    comment: Unexposed gelding who won last time out, having been seventh two starts back, and he looks open to improvement on that limited evidence. He returns after 129 days off and carries 158 lb.
    DATA: model 7.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 129-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Pilbara Kid (hrs_17395901523) | 3yo F | 145lb | OR - | draw 0 | jockey Conor Stone-Walsh | trainer Ian Patrick Donoghue (14d 0/11) | headgear - | last run - days | form - | MARKET 0.5% | 09:00 median 151.00 | Matchbook 350.00
    comment: Pilbara Kid is unraced, so she goes in as an unexposed filly with no form to lean on and plenty of scope for improvement.
    DATA: model 6.2% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Trainer 0 wins from 11 runs, last 14 days; Lightly raced: 0 runs in our data, so the model has little to go on
- Did Tell (hrs_17392534719) | 3yo G | 152lb | OR - | draw 0 | jockey Mark McDonagh | trainer Sean O O'Brien (14d 0/1) | headgear t (1st time) | last run 12 days | form 000 | MARKET 0.2% | 09:00 median 201.00 | Matchbook 1000.00
    comment: Unexposed and yet to win, Did Tell has been unplaced in each of his last three starts, but he's back quickly after 12 days and, lightly raced, could have improvement to come under 152 lb.
    DATA: model 1.7% | style Held up (led 4% of runs) | runs in data 3 | last 3: 20 Sep Listowel Hurdle 16f Good 11/11; 11 Oct Cork Hurdle 15.5f Good 10/10; 9 Nov Punchestown (IRE) Hurdle 16f Good To Yielding 10/10
    DATA for: First-time headgear
    DATA against: Last-run finishing speed -5.7% vs that field (faded); Poor recent finishing positions; Pace: steady gallop likely, hard to come from off the pace
- Moon Aura (hrs_63422506) | 3yo F | 145lb | OR - | draw 0 | jockey Shane Markey(7) | trainer C A McBratney (14d 0/2) | headgear p | last run 6 days | form P70 | MARKET 0.2% | 09:00 median 201.00 | Matchbook 1000.00
    comment: The main risk is her form, though: unplaced last time, a seventh two starts back, and yet to win in her last three.
    DATA: model 2.6% | style Midfield (led 4% of runs) | runs in data 8 | last 3: 28 Aug Down Royal Hurdle 17.4f Good PU/9; 31 Oct Down Royal (IRE) Hurdle 17f Good 7/8; 15 Nov Navan (IRE) Hurdle 16f Good To Yielding 10/15 fig 66
    DATA against: Poor recent finishing positions; Pulled up in 1 of its last 3 jumps runs

## 3:23 Punchestown | race_id rac_32305298987 | Albert Bartlett Triple Crown Series At Punchestown Festival 2027 Qualifier Handicap Hurdle
Hurdle |  | 2m3f87y | going Good To Yielding | Turf | 19 runners | rating band - | age 4yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Loi Des Jeux (hrs_57223467) | 5yo G | 152lb | OR 106 | draw 0 | jockey Danny Mullins | trainer Brian Hassett (14d 0/1) | headgear - | last run 35 days | form 03-121 | MARKET 17.8% | 09:00 median 4.00 | Matchbook 4.80 | CHECK (skip line 3.80)
    comment: Loi Des Jeux arrives in cracking form, a winner last time out, a second two starts back and a winner three starts back, and he has run over today's trip and going.
    DATA: model 13.9% | style Prominent (led 3% of runs) | runs in data 5 | last 3: 14 May Clonmel Hurdle 19.5f Good To Yielding 1/15; 25 Sep Listowel Hurdle 16f Good To Yielding 2/15; 17 Oct Limerick (IRE) Hurdle 21.5f Good To Yielding 1/18 fig 98
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Best recent form figure 98, 6 lb below field average; Recent figures 8 lb below its current mark (looks high in the weights)
- Gunnery Sergeant (hrs_40095629) | 6yo G | 151lb | OR 105 | draw 0 | jockey Jack Kennedy | trainer Gordon Elliott (14d 11/68) | headgear tp | last run 9 days | form 855321 | MARKET 11.3% | 09:00 median 6.50 | Matchbook 7.40
    comment: Gunnery Sergeant arrives in fine heart, a winner last time out and second two starts back, and he has run over today's trip and going before, back after just nine days.
    DATA: model 11.1% | style Midfield (led 3% of runs) | runs in data 9 | last 3: 5 Oct Fairyhouse Hurdle 20f Good 3/10; 23 Oct Sligo (IRE) Hurdle 20.5f Yielding 2/9 fig 99; 12 Nov Thurles (IRE) Hurdle 20f Good 1/11 fig 105
    DATA for: Last-run finishing speed +4.3% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
- Thankyouforthedays (hrs_52297931) | 5yo G | 155lb | OR 109 | draw 0 | jockey Keith Donoghue | trainer J P Dempsey (14d 0/4) | headgear - | last run 229 days | form 00716- | MARKET 11.1% | 09:00 median 6.00 | Matchbook 8.20
    comment: Thankyouforthedays is hard to fancy after a sixth last time out and a 229-day absence, with only one win in his last five starts, a winner two starts back, otherwise mixed form.
    DATA: model 10.0% | style Midfield (led 3% of runs) | runs in data 4 | last 3: 25 Jan Naas Hurdle 18.7f Heavy 7/16; 8 Mar Naas Hurdle 16.4f Soft To Heavy 1/10; 6 Apr Fairyhouse Hurdle 16f Yielding To Soft 6/21
    DATA for: Last-run finishing speed +2.2% vs that field (finished strongly)
    DATA against: Returns from a 229-day break
- Jacovec Cavern (hrs_30822344) | 7yo G | 166lb | OR 120 | draw 0 | jockey Richard Condon(5) | trainer Paul Hennessy (14d 0/0) | headgear p | last run 49 days | form -23P64 | MARKET 7.3% | 09:00 median 9.50 | Matchbook 12.00
    comment: The main risk is 166 lb, plus 49 days off, with him yet to win in his last five.
    DATA: model 4.4% | style Prominent (led 23% of runs) | runs in data 9 | last 3: 17 Jul Killarney Hurdle 22.8f Good PU/16; 8 Aug Wexford Chase 25f Good 6/7; 3 Oct Gowran Park Hurdle 24.2f Good To Yielding 4/11
    DATA for: Official rating 120, 11 lb above field average; Has won at this trip or further
    DATA against: Carries 11 lb more than average; Pulled up in 1 of its last 5 jumps runs
- Teenage Kiss (hrs_50402569) | 5yo M | 151lb | OR 105 | draw 0 | jockey Charlie O'Dwyer(3) | trainer Conor O'Dwyer (14d 0/3) | headgear p | last run 105 days | form 45-122 | MARKET 6.1% | 09:00 median 9.50 | Matchbook 18.50
    comment: Teenage Kiss arrives in good heart, a second last time out, another second two starts back and a win three starts back, and she has run over today's trip and going before.
    DATA: model 7.5% | style Held up (led 3% of runs) | runs in data 6 | last 3: 16 May Wexford Hurdle 24f Good To Yielding 1/13; 30 Jun Wexford Chase 23f Good 2/12; 8 Aug Wexford Chase 25f Good 2/7
    DATA for: Last-run finishing speed +4.5% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Returns from a 105-day break; Pace: steady gallop likely, hard to come from off the pace
- Inver Bay (hrs_54965435) | 7yo M | 149lb | OR 103 | draw 0 | jockey Mark Walsh | trainer Aidan Anthony Howard (14d 0/2) | headgear h | last run 12 days | form -55913 | MARKET 6.1% | 09:00 median 12.00 | Matchbook 14.00
    DATA: model 6.4% | style Held up (led 3% of runs) | runs in data 6 | last 3: 28 Sep Roscommon Hurdle 15.6f Good To Yielding 1/16; 12 Oct Roscommon Flat 12.2f Soft 1/16; 9 Nov Punchestown (IRE) Hurdle 16f Good To Yielding 3/9 fig 104
    DATA for: Good recent finishing positions; Carries 6 lb less than average
    DATA against: Official rating 103, 6 lb below field average; Pace: steady gallop likely, hard to come from off the pace
- Regno (hrs_59928561) | 5yo G | 140lb | OR 91 | draw 0 | jockey Mike O'Connor | trainer C A Murphy (14d 0/1) | headgear - | last run 215 days | form 58097- | MARKET 5.9% | 09:00 median 13.00 | Matchbook 14.50
    comment: Regno is hard to fancy: he has finished seventh, ninth, unplaced, eighth and fifth in his last five starts, and he returns after 215 days off under 140 lb.
    DATA: model 2.1% | style Held up (led 3% of runs) | runs in data 4 | last 3: 4 Mar Naas Hurdle 16f Soft To Heavy 11/20; 4 Apr Fairyhouse Hurdle 20f Yielding To Soft 9/25; 20 Apr Tramore Hurdle 16.4f Good To Yielding 7/16
    DATA for: Last-run finishing speed +3.4% vs that field (finished strongly); Carries 15 lb less than average
    DATA against: Official rating 91, 18 lb below field average; Poor recent finishing positions; Returns from a 215-day break; Pace: steady gallop likely, hard to come from off the pace
- Barrys Spirit (hrs_55545546) | 5yo G | 161lb | OR 115 | draw 0 | jockey Sean Flanagan | trainer Adrian Murray (14d 1/1) | headgear - | last run 21 days | form 415-04 | MARKET 5.7% | 09:00 median 12.00 | Matchbook 15.50
    DATA: model 3.5% | style Held up (led 8% of runs) | runs in data 2 | last 3: 2 Aug Galway Hurdle 16.7f Good 10/17; 31 Oct Down Royal (IRE) Hurdle 17f Good 4/12 fig 112
    DATA for: Best recent form figure 112, 8 lb above field average; Official rating 115, 6 lb above field average
    DATA against: Carries 6 lb more than average; Lightly raced: 2 runs in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Sonny May (hrs_29326724) | 9yo G | 155lb | OR 109 | draw 0 | jockey Mr J J Berry(7) | trainer Denis Hickey (14d 0/2) | headgear t | last run 12 days | form P0-952 | MARKET 5.0% | 09:00 median 15.00 | Matchbook 17.50
    comment: Sonny May bounced back to form with a second last time out just 12 days ago, and he has run over today's trip and going before, but he is winless in his last five and carries a hefty 155 lb off an official mark of 109.
    DATA: model 5.2% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 14 May Clonmel Hurdle 16.7f Good To Yielding 9/11; 13 Oct Punchestown Hurdle 16.2f Good 5/11; 9 Nov Punchestown (IRE) Hurdle 16f Good To Yielding 2/9 fig 110
    DATA for: Best recent form figure 110, 6 lb above field average
    DATA against: Pulled up in 1 of its last 5 jumps runs
- Rockymountainbleu (hrs_35054887) | 8yo G | 162lb | OR 116 | draw 0 | jockey Tiernan Power Roche | trainer P. J. Rothwell (14d 0/25) | headgear - | last run 13 days | form 329-6P | MARKET 3.6% | 09:00 median 17.00 | Matchbook 32.00
    DATA: model 5.2% | style Held up (led 3% of runs) | runs in data 5 | last 3: 28 Apr Punchestown Hurdle 16.6f Yielding 9/21; 14 Oct Punchestown (IRE) Hurdle 20f Good 6/13 fig 111; 8 Nov Naas (IRE) Hurdle 20f Good To Yielding PU/20
    DATA for: Best recent form figure 111, 7 lb above field average; Official rating 116, 7 lb above field average
    DATA against: Trainer 0 wins from 25 runs, last 14 days; Poor recent finishing positions; Carries 7 lb more than average; Pulled up in 1 of its last 5 jumps runs; Pace: steady gallop likely, hard to come from off the pace
- Tangara Bay (hrs_43859914) | 6yo M | 148lb | OR 102 | draw 0 | jockey Brian Hayes | trainer Peter Fahey (14d 3/4) | headgear - | last run 94 days | form 451-09 | MARKET 3.5% | 09:00 median 21.00 | Matchbook 27.00
    comment: Tangara Bay was beaten in her last two outings, a ninth last time out and unplaced the run before, and returns after 94 days off, so she is hard to fancy.
    DATA: model 2.8% | style Prominent (led 5% of runs) | runs in data 4 | last 3: 26 Mar Clonmel Hurdle 18.9f Soft 1/12; 29 Jul Galway Hurdle 22f Good 16/19; 19 Aug Sligo Hurdle 20.7f Good 9/10
    DATA for: Carries 7 lb less than average
    DATA against: Official rating 102, 7 lb below field average; Returns from a 94-day break
- Slieve Carran (hrs_34361600) | 7yo G | 160lb | OR 114 | draw 0 | jockey Simon Torrens | trainer Patrick T Foley (14d 0/4) | headgear h | last run 767 days | form 844P1/ | MARKET 3.4% | 09:00 median 19.00 | Matchbook 32.00
    comment: Slieve Carran won last time out, but that came 767 days ago, and a pulled up two starts back plus a fourth and another fourth before that tell a patchy story.
    DATA: model 4.2% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Official rating 114, 5 lb above field average
    DATA against: Carries 5 lb more than average; Returns from a 767-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Cleopatra's Needle (hrs_24770564) | 8yo M | 154lb | OR 108 | draw 0 | jockey Kieren Buckley | trainer H Rogers (14d 0/1) | headgear h | last run 38 days | form 17-464 | MARKET 2.6% | 09:00 median 17.00 | Matchbook 65.00
    comment: Fourth last time out and a winner five starts back, Cleopatra's Needle has shown some consistency, though she's finished no better than fourth in her last four outings.
    DATA: model 3.3% | style Held up (led 3% of runs) | runs in data 8 | last 3: 12 Aug Gowran Park Flat 9.5f Good To Firm 12/15; 10 Oct Fairyhouse Hurdle 16f Good 6/9; 14 Oct Punchestown (IRE) Hurdle 16.5f Good 4/5 fig 101
    DATA against: Recent figures 7 lb below its current mark (looks high in the weights); Pace: steady gallop likely, hard to come from off the pace
- Midfield Magic (hrs_63357301) | 5yo G | 153lb | OR 107 | draw 0 | jockey Conor Stone-Walsh | trainer Gavin Cromwell (14d 4/37) | headgear - | last run 26 days | form 4-90 | MARKET 2.3% | 09:00 median 23.00 | Matchbook 60.00
    comment: Midfield Magic is winless in his last three, unplaced last time out and a ninth two starts back, with a fourth three starts back his best recent effort.
    DATA: model 2.8% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 5 Apr Fairyhouse Hurdle 16.5f Yielding To Soft 4/25; 2 Oct Gowran Park Hurdle 16.4f Good 9/20; 26 Oct Galway (IRE) Hurdle 16.5f Soft To Heavy 14/20
- Krabat (hrs_23111319) | 11yo G | 152lb | OR 106 | draw 0 | jockey Sean O'Keeffe | trainer Michael J McDonagh (14d 0/2) | headgear - | last run 180 days | form 2140-7 | MARKET 1.9% | 09:00 median 26.00 | Matchbook 70.00
    comment: The risk is a 180-day absence, and a seventh last time out, under 152 lb.
    DATA: model 3.1% | style Held up (led 3% of runs) | runs in data 6 | last 3: 10 Apr Wexford Chase 19.5f Good To Yielding 4/15; 28 Apr Punchestown Hurdle 19.4f Yielding 14/24; 25 May Ballinrobe Chase 19.6f Good 7/13
    DATA for: Has won at this trip or further
    DATA against: Last-run finishing speed -3.0% vs that field (faded); Returns from a 180-day break; Aged 11, older than most of this field; Pace: steady gallop likely, hard to come from off the pace
- Needs Must (hrs_50402394) | 5yo G | 162lb | OR 116 | draw 0 | jockey Josh Williamson(3) | trainer Gordon Elliott (14d 11/68) | headgear - | last run 71 days | form 71F0-0 | MARKET 1.9% | 09:00 median 34.00 | Matchbook 48.00
    comment: Needs Must won four starts back but has since fallen and managed only unplaced efforts in his last two, and a 71-day break raises fitness questions.
    DATA: model 3.4% | style Midfield (led 3% of runs) | runs in data 4 | last 3: 4 Feb Punchestown Hurdle 19.1f Soft To Heavy F/7; 17 Mar Down Royal Hurdle 20.4f Good To Yielding 16/19; 11 Sep Ballinrobe Hurdle 21.9f Good To Yielding 14/14
    DATA for: Official rating 116, 7 lb above field average; Has won at this trip or further
    DATA against: Last-run finishing speed -3.6% vs that field (faded); Poor recent finishing positions; Carries 7 lb more than average; Fell or unseated in 1 of its last 4 jumps runs
- Backinbusiness (hrs_58565255) | 5yo G | 146lb | OR 100 | draw 0 | jockey Shane O'Callaghan(3) | trainer P. J. Rothwell (14d 0/25) | headgear tp | last run 14 days | form 3-45P5 | MARKET 1.8% | 09:00 median 34.00 | Matchbook 60.00
    comment: Fifth last time out just 14 days ago, he has run over today's trip and on this going, but he is yet to win in his last five starts and a pulled up two starts back is a worry.
    DATA: model 2.4% | style Prominent (led 23% of runs) | runs in data 4 | last 3: 6 Jun Punchestown Hurdle 19.2f Good To Yielding 5/17; 25 Oct Wexford (IRE) Hurdle 17f Soft PU/13; 7 Nov Gowran Park (IRE) Hurdle 16f Good To Yielding 5/7 fig 91
    DATA for: Carries 9 lb less than average
    DATA against: Best recent form figure 91, 13 lb below field average; Recent figures 9 lb below its current mark (looks high in the weights); Official rating 100, 9 lb below field average; Trainer 0 wins from 25 runs, last 14 days; Race comments mention jumping mistakes in 3 of its last 4 runs; Pulled up in 1 of its last 4 jumps runs
- Plunkett Street (hrs_34099632) | 8yo G | 161lb | OR 115 | draw 0 | jockey Daniel King | trainer Michael William O'Meara (14d 0/0) | headgear - | last run 50 days | form /210-0 | MARKET 1.4% | 09:00 median 34.00 | Matchbook 100.00
    comment: Plunkett Street won three starts back and was second the outing before, but he has been unplaced in his last two and returns after 50 days off. He has run over today's trip and going, though 161 lb is a stiff burden off an official mark of 115.
    DATA: model 5.8% | style Prominent (led 3% of runs) | runs in data 4 | last 3: 8 Apr Gowran Park Flat 13.8f Soft 7/10; 25 Apr Navan Flat 13f Good To Yielding 14/20; 2 Oct Gowran Park Hurdle 20.2f Good 13/14
    DATA for: Official rating 115, 6 lb above field average
    DATA against: Poor recent finishing positions; Carries 6 lb more than average
- Encanto Bruno (hrs_29409513) | 8yo G | 165lb | OR 119 | draw 0 | jockey Dylan Kidd(7) | trainer John McConnell (14d 0/15) | headgear - | last run 140 days | form 20-360 | MARKET 1.3% | 09:00 median 51.00 | Matchbook 80.00
    comment: The risk is a 140-day absence and an unplaced run last time out, with 165 lb to carry.
    DATA: model 2.9% | style Midfield (led 4% of runs) | runs in data 4 | last 3: 5 Jun Clonmel Hurdle 19.3f Good 3/4; 15 Jun Kilbeggan Hurdle 24.5f Good 6/12; 4 Jul Bellewstown Hurdle 17.2f Good 16/16
    DATA for: Official rating 119, 10 lb above field average
    DATA against: Trainer 0 wins from 15 runs, last 14 days; Last-run finishing speed -6.5% vs that field (faded); Carries 10 lb more than average; Returns from a 140-day break

## 3:53 Punchestown | race_id rac_32305300924 | WTW Willis (Pro/Am) Flat Race
NH Flat |  | 2m0f160y | going Good To Yielding | Turf | 10 runners | rating band - | age 4yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Mister Boum (hrs_17395896308) | 4yo G | 161lb | OR - | draw 0 | jockey Mr P. W. Mullins | trainer W. P. Mullins (14d 6/23) | headgear - | last run 287 days | form 1- | MARKET 36.5% | 09:00 median 2.20 | Matchbook 2.64
    comment: Unexposed gelding who won last time out, his only recent start, but he returns after 287 days off and carries 161 lb. Trainer's 6 winners from 23 in the last 14 days is a positive, and there looks to be scope for improvement.
    DATA: model 7.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 26% wins (6/23), last 14 days
    DATA against: Returns from a 287-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Chanson Du Jury (hrs_17394714589) | 4yo G | 161lb | OR - | draw 0 | jockey Mr H C Swan | trainer Gordon Elliott (14d 11/68) | headgear - | last run 223 days | form 1- | MARKET 17.0% | 09:00 median 5.00 | Matchbook 5.60
    comment: Unexposed gelding who won his only recent start, and he looks open to improvement, though he returns after 223 days off and carries 161 lb, so fitness is a question after the long break.
    DATA: model 7.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 223-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Ifuknowuknow (hrs_57718808) | 5yo G | 168lb | OR - | draw 0 | jockey Miss A B O'Connor | trainer S G Carey (14d 1/6) | headgear - | last run 22 days | form 67-12 | MARKET 13.8% | 09:00 median 5.50 | Matchbook 7.60
    comment: Ifuknowuknow arrives in cracking nick, second last time out and a winner two starts back, just 22 days ago, and he has run over today's trip and going before.
    DATA: model 14.5% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 18 Sep Downpatrick NH Flat 17.8f Good 1/12; 30 Oct Down Royal (IRE) NH Flat 17f Good To Yielding 2/8 fig 111
    DATA for: Best recent form figure 111, 15 lb above field average; Has won at this trip or further; Good recent finishing positions
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Luidgi Du Luy (hrs_56931252) | 5yo G | 168lb | OR - | draw 0 | jockey Mr C Mullins(7) | trainer Emmet Mullins (14d 2/6) | headgear t (1st time) | last run 229 days | form 319- | MARKET 10.7% | 09:00 median 8.00 | Matchbook 8.80
    comment: The main risk is a 229-day absence and a ninth last time out.
    DATA: model 13.1% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 8 Feb Navan NH Flat 16f Heavy 1/7; 6 Apr Fairyhouse NH Flat 16f Yielding To Soft 9/12
    DATA for: Trainer 33% wins (2/6), last 14 days; Has won at this trip or further; First-time headgear
    DATA against: Last-run finishing speed -4.1% vs that field (faded); Returns from a 229-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- Le Grand Retour (hrs_17389682114) | 4yo G | 161lb | OR - | draw 0 | jockey Mr J L Gleeson | trainer Peter Fahey (14d 3/4) | headgear - | last run 71 days | form 2 | MARKET 7.8% | 09:00 median 11.00 | Matchbook 11.50
    comment: The one concern is a 71-day layoff, which leaves fitness the main question.
    DATA: model 13.2% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 11 Sep Ballinrobe NH Flat 16f Good To Yielding 2/5
    DATA for: Last-run finishing speed +3.1% vs that field (finished strongly)
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Mhi Milani (hrs_63810061) | 4yo G | 168lb | OR - | draw 0 | jockey Mr J Dunne(7) | trainer Patrick T Foley (14d 0/4) | headgear ht | last run 16 days | form 5-1 | MARKET 5.2% | 09:00 median 17.00 | Matchbook 18.00
    comment: Mhi Milani won last time out, a fifth two starts back before that, and he has run over today's trip and going, but carrying 168 lb he looks hard to fancy.
    DATA: model 11.2% | style Held up (led 5% of runs) | runs in data 2 | last 3: 18 Apr Bellewstown NH Flat 17.1f Yielding 5/15; 5 Nov Clonmel (IRE) NH Flat 16.5f Good 1/12 fig 92
    DATA for: Has won at this trip or further
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Shine On Sam (hrs_17394485129) | 5yo G | 168lb | OR - | draw 0 | jockey Mr A P Ryan(3) | trainer M O Quigley (14d 0/0) | headgear h | last run 17 days | form 1 | MARKET 4.9% | 09:00 median 15.00 | Matchbook 22.00
    comment: Winner last time out and back within 17 days, Shine On Sam arrives fresh from success and has run over today's trip before.
    DATA: model 14.7% | style Held up (led 8% of runs) | runs in data 1 | last 3: 4 Nov Wexford (IRE) NH Flat 17f Yielding 1/7 fig 101
    DATA for: Best recent form figure 101, 5 lb above field average; Last-run finishing speed +5.9% vs that field (finished strongly); Has won at this trip or further
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Bluebell Breeze (hrs_65225405) | 4yo F | 161lb | OR - | draw 0 | jockey Miss Charlotte Butler(7) | trainer A D Leahy (14d 0/3) | headgear - | last run 27 days | form 074791 | MARKET 2.9% | 09:00 median 29.00 | Matchbook 38.00
    comment: Bluebell Breeze arrives a winner last time out, though that came after a ninth, a seventh and a fourth in her previous runs, so consistency is the question.
    DATA: model 11.0% | style Midfield (led 4% of runs) | runs in data 7 | last 3: 18 Sep Downpatrick Hurdle 17.8f Good 7/15; 28 Sep Roscommon Hurdle 20.2f Good To Yielding 9/15; 25 Oct Galway (IRE) NH Flat 16f Soft 1/6 fig 98
    DATA for: Has won at this trip or further
    DATA against: Race comments mention jumping mistakes in 2 of its last 2 runs
- Cant Stopthe Clock (hrs_17394810545) | 5yo M | 154lb | OR - | draw 0 | jockey Ethan O'Sullivan(7) | trainer Edward F Power (14d 1/2) | headgear h | last run 21 days | form 7 | MARKET 0.6% | 09:00 median 101.00 | Matchbook 270.00
    comment: On the plus side, she has run over today's trip and going, and 21 days since her last outing is a fair break.
    DATA: model 5.4% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 31 Oct Down Royal (IRE) NH Flat 17f Good 7/14 fig 81
    DATA against: Best recent form figure 81, 15 lb below field average; Lightly raced: 1 run in our data, so the model has little to go on
- Time Takes Time (hrs_17393743556) | 4yo G | 161lb | OR - | draw 0 | jockey Ben Kennedy(7) | trainer D Buckley (14d 0/1) | headgear - | last run 38 days | form 0 | MARKET 0.6% | 09:00 median 101.00 | Matchbook 280.00
    comment: Time Takes Time was unplaced last time out and returns after 38 days, yet to win in his last start, though he has run over today's trip and going before.
    DATA: model 1.9% | style Held up (led 8% of runs) | runs in data 1 | last 3: 14 Oct Punchestown (IRE) NH Flat 16.5f Good 10/11 fig 92
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
