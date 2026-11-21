# Card review packet: Lingfield (AW), 2026-11-21

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
{"meeting": "lingfield_aw", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 11:00 Lingfield (AW) | race_id rac_32305093665 | AWC Trials Day - Lingfield 2nd Jan 2027 Handicap Stakes
Flat | Class 6 | 1m1y | going Standard | AW | 11 runners | rating band 0-55 | age 3yo
DATA pace: Even - Two likely leaders (Who Is Alice, Heated Moment). A fair, even gallop is most likely.
- Honey Dale (hrs_57942094) | 3yo F | 135lb | OR 55 | draw 10 | jockey Billy Loughnane | trainer Charlie Clover (14d 0/1) | headgear - | last run 26 days | form 950501 | MARKET 49.3% | 09:00 median 1.73 | Matchbook 1.87
    comment: Fresh from a win last time out 26 days ago, Honey Dale has run over today's trip and going, but she was unplaced in two of the three runs before that.
    DATA: model 20.6% | style Prominent (led 23% of runs) | runs in data 7 | last 3: 22 Jun Ballinrobe Flat 9.7f Yielding 12/14; 17 Jul Killarney Hurdle 17f Good PU/12; 26 Oct Southwell (AW) Flat 7f Standard 1/11 fig 46
    DATA for: Best recent form figure 46, 5 lb above field average; Last-run finishing speed +3.5% vs that field (finished strongly)
    DATA against: Recent figures 9 lb below its current mark (looks high in the weights)
- Labiche (hrs_50435105) | 3yo G | 129lb | OR 49 | draw 7 | jockey Luke Morris | trainer James Owen (14d 3/30) | headgear - | last run 16 days | form 303546 | MARKET 15.5% | 09:00 median 5.00 | Matchbook 6.60
    comment: Labiche has been consistent without a win, with a sixth last time out and a fourth two starts back, and he has run over today's trip and going before after a 16-day break.
    DATA: model 12.1% | style Midfield (led 4% of runs) | runs in data 6 | last 3: 27 Jun Windsor Flat 8.1f Good To Firm 5/5; 2 Nov Wolverhampton (AW) Flat 8.5f Standard 4/8 fig 47; 5 Nov Chelmsford (AW) Flat 10f Standard 6/14 fig 52
    DATA for: Best recent form figure 52, 11 lb above field average
- Grey Sands (hrs_52054184) | 3yo C | 130lb | OR 50 | draw 2 | jockey Sean Levey | trainer Kim Bailey & Mat Nicholls (14d 3/17) | headgear tv | last run 43 days | form 375595 | MARKET 10.6% | 09:00 median 7.50 | Matchbook 9.40
    comment: The main risk is a 43-day absence plus 130 lb from stall two.
    DATA: model 6.2% | style Midfield (led 3% of runs) | runs in data 9 | last 3: 28 Aug Fontwell Hurdle 17.7f Good PU/8; 21 Sep Wolverhampton Flat 12.2f Standard 9/9; 9 Oct Kempton Flat 8f Standard To Slow 5/13
    DATA for: Has won at this trip or further
- A Daughters Love (hrs_51273152) | 3yo F | 135lb | OR 55 | draw 4 | jockey Kieran Shoemark | trainer David Flood (14d 0/1) | headgear tp (1st time) | last run 26 days | form 865687 | MARKET 6.1% | 09:00 median 12.00 | Matchbook 18.00
    comment: Winless in her last six, A Daughters Love has finished seventh, eighth, sixth, fifth, sixth and eighth, though she has run over today's trip and going and comes back after 26 days.
    DATA: model 7.9% | style Midfield (led 5% of runs) | runs in data 18 | last 3: 8 Oct Bath Flat 10.2f Good 6/8; 10 Oct Southwell Flat 12.1f Standard 8/11; 26 Oct Leicester Flat 12f Soft 7/13 fig 44
    DATA for: Has won at this trip or further; First-time headgear
    DATA against: Recent figures 11 lb below its current mark (looks high in the weights); Poor recent finishing positions
- Heated Moment (hrs_55515964) | 3yo F | 132lb | OR 52 | draw 3 | jockey Robert Havlin | trainer Conrad Allen (14d 0/0) | headgear b | last run 166 days | form 75-554 | MARKET 5.7% | 09:00 median 13.00 | Matchbook 19.00
    comment: Heated Moment is yet to win but has finished fourth last time out, and a fifth two starts back, so she is consistent, and she has run over today's trip and going before.
    DATA: model 12.0% | style Leader (led 57% of runs) | runs in data 3 | last 3: 21 Apr Yarmouth Flat 10.1f Good To Firm 5/9; 8 May Ripon Flat 9.8f Good 5/8; 8 Jun Windsor Flat 8.1f Good To Soft 4/12
    DATA against: Returns from a 166-day break
- Who Is Alice (hrs_53420409) | 3yo F | 133lb | OR 53 | draw 1 | jockey George Bass | trainer Grace Harris (14d 1/7) | headgear h | last run 37 days | form 553053 | MARKET 3.6% | 09:00 median 21.00 | Matchbook 28.00
    comment: The risk is that she is winless in her last six and carries 133 lb after 37 days off.
    DATA: model 11.2% | style Leader (led 29% of runs) | runs in data 9 | last 3: 12 Sep Bath Flat 8f Good 13/14; 21 Sep Ffos Las Flat 8f Soft 5/9; 15 Oct Brighton Flat 7f Good 3/13 fig 56
    DATA for: Best recent form figure 56, 15 lb above field average
- Anncanya (hrs_66494127) | 3yo F | 131lb | OR 51 | draw 6 | jockey Marco Ghiani | trainer Peter Chapple-Hyam (14d 0/0) | headgear - | last run 26 days | form 666 | MARKET 2.5% | 09:00 median 29.00 | Matchbook 48.00
    comment: She has run over today's trip and going, and 26 days off is no concern, but 131 lb from stall six looks a lot to ask.
    DATA: model 3.8% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 17 Jul Newmarket Flat 8f Good To Firm 6/6; 25 Aug Lingfield Flat 10f Standard 6/7; 26 Oct Kempton (AW) Flat 7f Standard / Slow 6/9 fig 32
    DATA against: Best recent form figure 32, 9 lb below field average; Recent figures 19 lb below its current mark (looks high in the weights); Poor recent finishing positions
- Rogue Desire (hrs_55795012) | 3yo F | 130lb | OR 50 | draw 9 | jockey Cieren Fallon | trainer Tony Carroll (14d 1/15) | headgear - | last run 28 days | form 575570 | MARKET 2.3% | 09:00 median 34.00 | Matchbook 44.00
    comment: The risk is that she's yet to win in her last six and was unplaced last time, while carrying 130 lb from stall nine.
    DATA: model 3.4% | style Midfield (led 4% of runs) | runs in data 6 | last 3: 2 Sep Kempton Flat 11f Standard To Slow 5/5; 22 Sep Southwell Flat 16.5f Standard 7/9; 24 Oct Southwell (AW) Flat 8f Standard 10/13 fig 43
    DATA against: Recent figures 7 lb below its current mark (looks high in the weights)
- Case Study (hrs_56188846) | 3yo F | 135lb | OR 55 | draw 5 | jockey Daniel Muscutt | trainer Laura Mongan (14d 0/0) | headgear p | last run 59 days | form -82048 | MARKET 1.6% | 09:00 median 41.00 | Matchbook 85.00
    comment: Case Study is yet to win in her last five starts, with an eighth last time out following a fourth two starts back, though a second four starts back shows she can go close.
    DATA: model 7.6% | style Midfield (led 4% of runs) | runs in data 5 | last 3: 19 Jun Redcar Flat 7f Good 10/10; 21 Jul Wolverhampton Flat 8.6f Standard 4/10; 23 Sep Kempton Flat 8f Standard To Slow 8/10
    DATA against: Last-run finishing speed -2.3% vs that field (faded)
- Seapearl (hrs_57286824) | 3yo F | 130lb | OR 50 | draw 11 | jockey Edward Greatrex | trainer Oliver Cole (14d 0/0) | headgear - | last run 24 days | form 69699 | MARKET 1.5% | 09:00 median 51.00 | Matchbook 70.00
    comment: Seapearl is winless in her last five, finishing ninth last time out, ninth two starts back and a sixth five starts back, so she is hard to fancy.
    DATA: model 8.0% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 7 Feb Lingfield Flat 7f Standard 6/9; 7 Apr Southwell Flat 7.1f Standard 9/9; 28 Oct Kempton (AW) Flat 8f Standard / Slow 9/10 fig 26
    DATA against: Best recent form figure 26, 15 lb below field average; Recent figures 24 lb below its current mark (looks high in the weights); Poor recent finishing positions
- Grimese's Special (hrs_56370657) | 3yo F | 128lb | OR 48 | draw 8 | jockey David Egan | trainer J. S. Moore (14d 0/7) | headgear b | last run 23 days | form 085560 | MARKET 1.2% | 09:00 median 67.00 | Matchbook 90.00
    comment: Winless in her last six, with an unplaced effort last time out and a best finish of fifth over that spell, this filly is hard to fancy from stall 8 off 128 lb.
    DATA: model 7.1% | style Midfield (led 5% of runs) | runs in data 6 | last 3: 13 Sep Bath Flat 8f Good To Soft 5/10; 21 Sep Ffos Las Flat 8f Soft 6/9; 29 Oct Bath Flat 5.5f Soft 15/16 fig 30
    DATA against: Best recent form figure 30, 11 lb below field average; Recent figures 18 lb below its current mark (looks high in the weights)

## 11:30 Lingfield (AW) | race_id rac_32305459758 | All-Weather Championship Is Back EBF Novice Stakes (Div I) (GBB Race)
Flat | Class 3 | 7f1y | going Standard | AW | 12 runners | rating band - | age 2yo
DATA pace: Lone leader - King Gamrah is the only habitual front-runner and may be allowed an easy lead.
- El Mutamaken (hrs_17395819126) | 2yo G | 133lb | OR - | draw 10 | jockey Billy Loughnane | trainer Owen Burrows (14d 0/2) | headgear - | last run - days | form - | MARKET 24.2% | 09:00 median 3.25 | Matchbook 3.95 | CHECK (skip line 3.09)
    DATA: model 7.3% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Le Drakkar (hrs_17391657556) | 2yo C | 133lb | OR - | draw 6 | jockey David Egan | trainer Kevin Philippart de Foy (14d 2/6) | headgear t | last run 26 days | form 6 | MARKET 20.9% | 09:00 median 4.00 | Matchbook 4.40
    DATA: model 12.0% | style Held up (led 8% of runs) | runs in data 1 | last 3: 26 Oct Kempton (AW) Flat 7f Standard / Slow 6/9 fig 48
    DATA for: Best recent form figure 48, 4 lb above field average; Trainer 33% wins (2/6), last 14 days
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on; Course: hold-up horses have won 0.7× their fair share at 7f here
- Al Lazzaz (hrs_17395807653) | 2yo C | 133lb | OR - | draw 3 | jockey Sean Levey | trainer Richard Hannon (14d 0/5) | headgear - | last run - days | form - | MARKET 16.3% | 09:00 median 5.00 | Matchbook 5.80
    DATA: model 7.3% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Aziz Malak (hrs_17395818083) | 2yo G | 133lb | OR - | draw 2 | jockey Harry Davies | trainer Simon & Ed Crisford (14d 1/3) | headgear - | last run - days | form - | MARKET 11.2% | 09:00 median 7.50 | Matchbook 8.40
    DATA: model 7.3% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Pigou (hrs_17393635084) | 2yo G | 133lb | OR - | draw 12 | jockey Daniel Muscutt | trainer James Fanshawe (14d 0/7) | headgear - | last run 40 days | form 4 | MARKET 9.8% | 09:00 median 8.50 | Matchbook 9.60
    DATA: model 11.4% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 12 Oct Yarmouth Flat 7f Good To Soft 4/7
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- If You Like (hrs_17392196787) | 2yo C | 133lb | OR - | draw 4 | jockey Cieren Fallon | trainer William Haggas (14d 2/11) | headgear t | last run 26 days | form 63 | MARKET 4.8% | 09:00 median 17.00 | Matchbook 20.00
    DATA: model 9.2% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 15 Sep Yarmouth Flat 6f Good To Soft 6/6; 26 Oct Leicester Flat 6f Soft 3/7 fig 36
    DATA against: Best recent form figure 36, 8 lb below field average; Lightly raced: 2 runs in our data, so the model has little to go on
- King Gamrah (hrs_17393011370) | 2yo C | 133lb | OR - | draw 8 | jockey Luke Morris | trainer James Tate (14d 0/1) | headgear - | last run 26 days | form 7 | MARKET 3.9% | 09:00 median 21.00 | Matchbook 25.00
    DATA: model 11.9% | style Leader (led 57% of runs) | runs in data 1 | last 3: 26 Oct Kempton (AW) Flat 7f Standard / Slow 7/10 fig 44
    DATA for: Pace: may get an uncontested lead
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Hot Mission (hrs_17395820169) | 2yo C | 133lb | OR - | draw 9 | jockey Harry Vigors(5) | trainer Ollie Sangster (14d 0/1) | headgear - | last run - days | form - | MARKET 3.0% | 09:00 median 26.00 | Matchbook 36.00
    DATA: model 7.3% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Boy's Slipper (hrs_17393017628) | 2yo G | 133lb | OR - | draw 11 | jockey Nicola Currie | trainer Henry Candy (14d 0/0) | headgear - | last run 26 days | form 08 | MARKET 2.0% | 09:00 median 41.00 | Matchbook 55.00
    DATA: model 6.0% | style Held up (led 5% of runs) | runs in data 2 | last 3: 1 Oct Salisbury Flat 8f Soft 11/12; 26 Oct Kempton (AW) Flat 7f Standard / Slow 8/10 fig 42
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Course: hold-up horses have won 0.7× their fair share at 7f here
- St Peter's Cross (hrs_17394165971) | 2yo C | 133lb | OR - | draw 7 | jockey Jack Dace(5) | trainer Luke Dace (14d 0/4) | headgear h (1st time) | last run 26 days | form 0 | MARKET 1.9% | 09:00 median 41.00 | Matchbook 65.00
    DATA: model 3.9% | style Held up (led 8% of runs) | runs in data 1 | last 3: 26 Oct Kempton (AW) Flat 7f Standard / Slow 10/10 fig 38
    DATA for: First-time headgear
    DATA against: Best recent form figure 38, 6 lb below field average; Lightly raced: 1 run in our data, so the model has little to go on; Course: hold-up horses have won 0.7× their fair share at 7f here
- Force Field (hrs_17393789448) | 2yo C | 133lb | OR - | draw 5 | jockey Paddy Bradley | trainer Jim Boyle (14d 0/1) | headgear - | last run 37 days | form 7 | MARKET 1.4% | 09:00 median 51.00 | Matchbook 110.00
    DATA: model 9.1% | style Unknown | runs in data 1 | last 3: 15 Oct Brighton Flat 7f Good 7/12 fig 56
    DATA for: Best recent form figure 56, 12 lb above field average
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Paddy Cool (hrs_17393639256) | 2yo C | 133lb | OR - | draw 1 | jockey William Carson | trainer Tony Carroll (14d 1/15) | headgear - | last run - days | form - | MARKET 0.7% | 09:00 median 101.00 | Matchbook 220.00
    DATA: model 7.3% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on

## 12:00 Lingfield (AW) | race_id rac_32305095602 | All-Weather Championship Is Back EBF Novice Stakes (Div II) (GBB Race)
Flat | Class 3 | 7f1y | going Standard | AW | 12 runners | rating band - | age 2yo
DATA pace: Unclear - Running styles known for only 5 of 12 runners.
- Bibury Star (hrs_17394839749) | 2yo C | 133lb | OR - | draw 5 | jockey Billy Loughnane | trainer Richard Hughes (14d 1/8) | headgear - | last run 18 days | form 2 | MARKET 51.0% | 09:00 median 1.53 | Matchbook 1.81
    DATA: model 32.2% | style Unknown | runs in data 1 | last 3: 3 Nov Wolverhampton (AW) Flat 7f Standard 2/11 fig 49
    DATA for: Last-run finishing speed +4.2% vs that field (finished strongly)
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Sunday Slew (hrs_17395647031) | 2yo C | 133lb | OR - | draw 4 | jockey Kieran Shoemark | trainer Ed Walker (14d 0/9) | headgear - | last run - days | form - | MARKET 10.9% | 09:00 median 7.50 | Matchbook 8.40
    DATA: model 5.6% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Trainer 0 wins from 9 runs, last 14 days; Lightly raced: 0 runs in our data, so the model has little to go on
- I Know You By Now (hrs_17394161799) | 2yo G | 133lb | OR - | draw 7 | jockey Joe Leavy | trainer Clive Cox (14d 0/3) | headgear - | last run 22 days | form 4 | MARKET 9.7% | 09:00 median 8.25 | Matchbook 9.60
    DATA: model 13.8% | style Unknown | runs in data 1 | last 3: 30 Oct Newmarket Flat 6f Good To Soft 4/7 fig 67
    DATA for: Best recent form figure 67, 20 lb above field average
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Vallejo (hrs_17394182659) | 2yo C | 133lb | OR - | draw 11 | jockey Callum Hutchinson | trainer Andrew Balding (14d 1/22) | headgear - | last run 29 days | form 9 | MARKET 9.6% | 09:00 median 9.00 | Matchbook 9.00
    DATA: model 6.8% | style Unknown | runs in data 1 | last 3: 23 Oct Doncaster Flat 8f Heavy 9/10 fig 45
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Bedford Benny Boy (hrs_17391731609) | 2yo C | 133lb | OR - | draw 8 | jockey Sean Levey | trainer David Menuisier (14d 0/1) | headgear - | last run 79 days | form 7 | MARKET 4.8% | 09:00 median 17.00 | Matchbook 19.50
    DATA: model 4.4% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 3 Sep Haydock Flat 8f Soft 7/9
    DATA against: Last-run finishing speed -3.2% vs that field (faded); Lightly raced: 1 run in our data, so the model has little to go on
- Gattino (hrs_17394668697) | 2yo C | 133lb | OR - | draw 2 | jockey David Egan | trainer John Butler (14d 1/8) | headgear - | last run 14 days | form 73 | MARKET 3.4% | 09:00 median 26.00 | Matchbook 30.00
    DATA: model 8.9% | style Held up (led 5% of runs) | runs in data 2 | last 3: 30 Oct Newmarket Flat 7f Good To Soft 7/10 fig 38; 7 Nov Doncaster Flat 6f Good To Soft 3/6 fig 58
    DATA for: Best recent form figure 58, 11 lb above field average
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Course: hold-up horses have won 0.7× their fair share at 7f here
- Shabby (hrs_17392898726) | 2yo F | 128lb | OR - | draw 9 | jockey Callum Shepherd | trainer Michael Bell (14d 1/2) | headgear - | last run 24 days | form 76 | MARKET 2.7% | 09:00 median 26.00 | Matchbook 44.00
    DATA: model 3.9% | style Held up (led 8% of runs) | runs in data 2 | last 3: 26 Sep Haydock Flat 8f Heavy 7/9; 28 Oct Nottingham Flat 8.5f Soft 6/9 fig 42
    DATA against: Best recent form figure 42, 5 lb below field average; Lightly raced: 2 runs in our data, so the model has little to go on; Course: hold-up horses have won 0.7× their fair share at 7f here
- Starman Waiting (hrs_17394671826) | 2yo G | 133lb | OR - | draw 6 | jockey Darragh Keenan | trainer George Scott (14d 0/0) | headgear - | last run 22 days | form 8 | MARKET 2.1% | 09:00 median 29.00 | Matchbook 65.00
    DATA: model 8.7% | style Unknown | runs in data 1 | last 3: 30 Oct Newmarket Flat 7f Good To Soft 8/10 fig 34
    DATA against: Best recent form figure 34, 13 lb below field average; Lightly raced: 1 run in our data, so the model has little to go on
- Onesmallstepforman (hrs_17394628020) | 2yo G | 133lb | OR - | draw 1 | jockey Paddy Bradley | trainer Jim Boyle (14d 0/1) | headgear - | last run - days | form - | MARKET 1.9% | 09:00 median 41.00 | Matchbook 70.00
    DATA: model 5.6% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Monee Talks (hrs_17395821212) | 2yo G | 133lb | OR - | draw 12 | jockey William Carson | trainer Tony Carroll (14d 1/15) | headgear - | last run - days | form - | MARKET 1.4% | 09:00 median 67.00 | Matchbook 90.00
    DATA: model 5.6% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Lead To Gold (hrs_17393098982) | 2yo G | 133lb | OR - | draw 3 | jockey Sean Dylan Bowen | trainer Ollie Sangster (14d 0/1) | headgear - | last run 38 days | form 97 | MARKET 1.3% | 09:00 median 67.00 | Matchbook 120.00
    DATA: model 1.6% | style Held up (led 5% of runs) | runs in data 2 | last 3: 2 Oct Wolverhampton Flat 5.1f Standard 9/9; 14 Oct Kempton (AW) Flat 6f Standard / Slow 7/8 fig 49
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Course: hold-up horses have won 0.7× their fair share at 7f here
- Sir Marryat (hrs_17393023886) | 2yo C | 133lb | OR - | draw 10 | jockey Charles Bishop | trainer Brian Meehan (14d 0/1) | headgear - | last run 33 days | form 90 | MARKET 1.1% | 09:00 median 101.00 | Matchbook 140.00
    DATA: model 2.8% | style Held up (led 5% of runs) | runs in data 2 | last 3: 1 Oct Salisbury Flat 8f Soft 9/12; 19 Oct Southwell (AW) Flat 7f Standard 13/14 fig 31
    DATA against: Best recent form figure 31, 16 lb below field average; Lightly raced: 2 runs in our data, so the model has little to go on; Course: hold-up horses have won 0.7× their fair share at 7f here

## 12:35 Lingfield (AW) | race_id rac_32305097539 | AWC Season 14 Has Begun EBF Novice Stakes (GBB Race)
Flat | Class 4 | 5f6y | going Standard | AW | 10 runners | rating band - | age 2yo
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Iris Olivia (hrs_63809620) | 2yo F | 128lb | OR 75 | draw 10 | jockey David Egan | trainer Charlie Clover (14d 0/1) | headgear v (1st time) | last run 38 days | form 72344 | MARKET 48.3% | 09:00 median 1.73 | Matchbook 1.82
    DATA: model 49.3% | style Prominent (led 5% of runs) | runs in data 5 | last 3: 1 Sep Wolverhampton Flat 7.2f Standard 3/9; 24 Sep Pontefract Flat 6f Good 4/8; 14 Oct Kempton (AW) Flat 7f Standard / Slow 4/10 fig 71
    DATA for: Best recent form figure 71, 20 lb above field average; First-time headgear
- Crimson Blaze (hrs_63357497) | 2yo F | 128lb | OR 64 | draw 7 | jockey Billy Loughnane | trainer Richard Hughes (14d 1/8) | headgear - | last run 51 days | form 686432 | MARKET 18.7% | 09:00 median 3.50 | Matchbook 6.00
    DATA: model 7.5% | style Held up (led 8% of runs) | runs in data 7 | last 3: 11 Aug Lingfield Flat 5f Standard 4/5; 13 Sep Bath Flat 5f Good To Soft 3/7; 1 Oct Nottingham Flat 5f Good 2/4
    DATA for: Good recent finishing positions
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Time To Climb (hrs_17391046358) | 2yo C | 133lb | OR - | draw 9 | jockey Marco Ghiani | trainer Stuart Williams (14d 0/3) | headgear h (1st time) | last run 35 days | form 04 | MARKET 9.2% | 09:00 median 9.00 | Matchbook 9.40
    DATA: model 10.5% | style Held up (led 5% of runs) | runs in data 2 | last 3: 19 Aug Kempton Flat 7f Standard To Slow 10/12; 17 Oct Southwell (AW) Flat 5f Standard 4/12 fig 63
    DATA for: Best recent form figure 63, 12 lb above field average; First-time headgear
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Romantic Pursuit (hrs_63650468) | 2yo F | 128lb | OR - | draw 8 | jockey Darragh Keenan | trainer George Scott (14d 0/0) | headgear - | last run - days | form - | MARKET 5.9% | 09:00 median 13.00 | Matchbook 16.00
    DATA: model 5.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Virago Parvenue (hrs_17393329485) | 2yo F | 128lb | OR - | draw 3 | jockey Sean Levey | trainer Richard Hannon (14d 0/5) | headgear - | last run - days | form - | MARKET 5.5% | 09:00 median 15.00 | Matchbook 17.00
    DATA: model 5.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Heart of Glass (hrs_60821705) | 2yo G | 133lb | OR - | draw 5 | jockey George Wood | trainer Richard Spencer (14d 0/3) | headgear h | last run 35 days | form 0 | MARKET 5.3% | 09:00 median 15.00 | Matchbook 18.00
    DATA: model 6.9% | style Held up (led 8% of runs) | runs in data 1 | last 3: 17 Oct Southwell (AW) Flat 5f Standard 10/12 fig 27
    DATA against: Best recent form figure 27, 24 lb below field average; Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Goldtrader (hrs_63810999) | 2yo G | 133lb | OR - | draw 4 | jockey Kieran Shoemark | trainer Ed Walker (14d 0/9) | headgear h (1st time) | last run 84 days | form 97 | MARKET 2.7% | 09:00 median 29.00 | Matchbook 38.00
    DATA: model 4.4% | style Held up (led 8% of runs) | runs in data 2 | last 3: 23 May Salisbury Flat 5f Good 9/9; 29 Aug Windsor Flat 6.1f Soft 7/9
    DATA for: First-time headgear
    DATA against: Trainer 0 wins from 9 runs, last 14 days; Lightly raced: 2 runs in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Without You (hrs_17393265862) | 2yo F | 128lb | OR - | draw 1 | jockey Luke Morris | trainer James Tate (14d 0/1) | headgear - | last run 47 days | form 8 | MARKET 1.7% | 09:00 median 41.00 | Matchbook 80.00
    DATA: model 4.5% | style Unknown | runs in data 1 | last 3: 5 Oct Wolverhampton Flat 6.1f Standard 8/8
    DATA against: Last-run finishing speed -4.2% vs that field (faded); Lightly raced: 1 run in our data, so the model has little to go on
- Hosta (hrs_17393421269) | 2yo F | 128lb | OR - | draw 6 | jockey Rob Hornby | trainer Hughie Morrison (14d 0/3) | headgear - | last run 19 days | form 70 | MARKET 1.4% | 09:00 median 67.00 | Matchbook 80.00
    DATA: model 3.1% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 7 Oct Nottingham Flat 6.1f Good 7/8; 2 Nov Chelmsford (AW) Flat 6f Standard 10/12 fig 45
    DATA against: Best recent form figure 45, 6 lb below field average; Lightly raced: 2 runs in our data, so the model has little to go on
- Faster Love (hrs_17392146723) | 2yo F | 128lb | OR - | draw 2 | jockey Jack Dace(5) | trainer Gay Kelleway (14d 0/2) | headgear - | last run 44 days | form 7 | MARKET 1.2% | 09:00 median 81.00 | Matchbook 120.00
    DATA: model 2.9% | style Unknown | runs in data 1 | last 3: 8 Oct Bath Flat 5f Good 7/7
    DATA against: Last-run finishing speed -2.5% vs that field (faded); Lightly raced: 1 run in our data, so the model has little to go on

## 1:10 Lingfield (AW) | race_id rac_32305099476 | Midnite: Built For 2026 Not 2006 Handicap Stakes
Flat | Class 5 | 1m2f | going Standard | AW | 12 runners | rating band 0-75 | age 3yo+
DATA pace: Even - Two likely leaders (Bubbles Wonky, Pleasant Man). A fair, even gallop is most likely.
- Mr Nugget (hrs_41325396) | 5yo G | 135lb | OR 71 | draw 5 | jockey David Egan | trainer David Simcock (14d 0/4) | headgear - | last run 5 days | form 956952 | MARKET 17.8% | 09:00 median 4.50 | Matchbook 5.30 | CHECK (skip line 4.27)
    comment: Mr Nugget is hard to fancy, yet to win in his last six starts and finishing fifth or worse in five of them, though a second last time out and a quick five-day turnaround show he is in some heart.
    DATA: model 5.8% | style Held up (led 3% of runs) | runs in data 13 | last 3: 9 Oct Kempton Flat 8f Standard To Slow 9/10; 2 Nov Chelmsford (AW) Flat 10f Standard 5/8 fig 70; 16 Nov Wolverhampton (AW) Flat 9.5f Standard 2/12 fig 71
    DATA for: Best recent form figure 71, 6 lb above field average; Last-run finishing speed +2.2% vs that field (finished strongly); Has won at this trip or further
- Oracle Mission (hrs_58843428) | 3yo G | 135lb | OR 74 | draw 12 | jockey Kaiya Fraser | trainer Harry Eustace (14d 0/5) | headgear - | last run 25 days | form 31-865 | MARKET 12.8% | 09:00 median 6.25 | Matchbook 7.40
    comment: Oracle Mission has drifted through a fifth last time out, a sixth and an eighth, though a win four starts back shows he can deliver, and he has run over today's trip and going.
    DATA: model 8.0% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 9 May Lingfield Flat 7f Good To Firm 8/8; 1 Oct Salisbury Flat 9.9f Soft 6/12; 27 Oct Catterick Flat 12f Soft 5/10 fig 70
    DATA for: Best recent form figure 70, 5 lb above field average
- Fallacious Promise (hrs_58133565) | 3yo G | 136lb | OR 75 | draw 7 | jockey Luke Morris | trainer John Butler (14d 1/8) | headgear - | last run 26 days | form 121168 | MARKET 12.6% | 09:00 median 7.00 | Matchbook 7.00
    comment: Three wins in his last six starts catch the eye, but Fallacious Promise has since slipped to a sixth and then an eighth last time out, and he has run over today's trip and going.
    DATA: model 10.2% | style Midfield (led 4% of runs) | runs in data 10 | last 3: 15 Aug Lingfield Flat 8f Standard 1/6; 4 Sep Kempton Flat 8f Standard To Slow 6/7; 26 Oct Kempton (AW) Flat 8f Standard / Slow 8/13 fig 73
    DATA for: Best recent form figure 73, 8 lb above field average
- Cancan In The Rain (hrs_30980838) | 6yo G | 135lb | OR 71 | draw 8 | jockey George Wood | trainer Gihan Arnolda (14d 0/2) | headgear - | last run 43 days | form 483065 | MARKET 11.7% | 09:00 median 7.00 | Matchbook 8.00
    comment: He is winless in his last six and returns after 43 days, but a fifth last time out keeps him in the picture.
    DATA: model 7.8% | style Midfield (led 4% of runs) | runs in data 7 | last 3: 4 Sep Ascot Flat 8f Good 10/11; 24 Sep Newmarket Flat 8f Good 6/12; 9 Oct Kempton Flat 8f Standard To Slow 5/10
- King's Hand (hrs_44076025) | 4yo G | 139lb | OR 75 | draw 2 | jockey Billy Loughnane | trainer Joseph Parr (14d 0/1) | headgear h | last run 177 days | form 312412 | MARKET 10.6% | 09:00 median 7.00 | Matchbook 9.60
    comment: King's Hand arrives in strong recent form, second last time out and a winner two starts back, and has run over today's trip and going before.
    DATA: model 12.0% | style Midfield (led 4% of runs) | runs in data 7 | last 3: 18 Mar Kempton Flat 11f Standard To Slow 4/8; 18 May Lingfield Flat 10f Good 1/8; 28 May Yarmouth Flat 10.1f Good To Firm 2/4
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Returns from a 177-day break
- Newfangled (hrs_35864437) | 5yo G | 133lb | OR 69 | draw 11 | jockey Harry Davies | trainer Jonathan Portman (14d 1/8) | headgear p | last run 25 days | form 464377 | MARKET 8.1% | 09:00 median 10.00 | Matchbook 12.00
    comment: Two sevenths in his last two starts are the main risk, and he is still winless in his last six.
    DATA: model 6.9% | style Midfield (led 3% of runs) | runs in data 10 | last 3: 14 Sep Windsor Flat 8.1f Good To Soft 3/12; 28 Sep Brighton Flat 8f Good To Firm 7/10; 27 Oct Wolverhampton (AW) Flat 9.5f Standard 7/8 fig 57
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 57, 8 lb below field average; Recent figures 12 lb below its current mark (looks high in the weights)
- Dream Pirate (hrs_32638214) | 6yo G | 136lb | OR 72 | draw 9 | jockey Marco Ghiani | trainer T. J. Kent (14d 0/4) | headgear b | last run 26 days | form -19613 | MARKET 7.2% | 09:00 median 11.50 | Matchbook 13.50
    comment: Dream Pirate arrives with a third last time out, and a winner two starts back, after 26 days off, and he has run over today's trip and going.
    DATA: model 8.6% | style Midfield (led 4% of runs) | runs in data 5 | last 3: 20 May Yarmouth Flat 10.1f Good 6/7; 13 Oct Leicester Flat 8.2f Good To Soft 1/9; 26 Oct Leicester Flat 8f Soft 3/10 fig 66
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Recent figures 6 lb below its current mark (looks high in the weights)
- Celestias Comet (hrs_45855299) | 4yo F | 134lb | OR 70 | draw 6 | jockey Jonny Peate | trainer James Fanshawe (14d 0/7) | headgear h | last run 30 days | form 551729 | MARKET 6.8% | 09:00 median 12.00 | Matchbook 14.50
    DATA: model 10.9% | style Held up (led 3% of runs) | runs in data 8 | last 3: 29 Jul Sandown Flat 9.9f Good To Firm 7/10; 1 Oct Nottingham Flat 10.2f Good 2/14; 22 Oct Southwell (AW) Flat 11f Standard 9/11 fig 64
    DATA for: Has won at this trip or further
    DATA against: Recent figures 6 lb below its current mark (looks high in the weights)
- Pleasant Man (hrs_22381583) | 8yo G | 137lb | OR 73 | draw 4 | jockey Taryn Langley(5) | trainer Joey Ramsden (14d 0/0) | headgear p | last run 51 days | form 313851 | MARKET 3.8% | 09:00 median 17.00 | Matchbook 34.00
    comment: Pleasant Man arrives a last-time-out winner, with two wins in his last six starts, and he has run over today's trip and going before.
    DATA: model 6.6% | style Leader (led 43% of runs) | runs in data 16 | last 3: 10 Jul York Flat 11.9f Good To Firm 8/10; 25 Sep Haydock Flat 10.2f Soft 5/7; 1 Oct Nottingham Flat 10.2f Good 1/14
    DATA for: Has won at this trip or further
    DATA against: Aged 8, older than most of this field
- Bubbles Wonky (hrs_36614893) | 5yo G | 139lb | OR 75 | draw 3 | jockey Daniel Muscutt | trainer Mark Pattinson (14d 0/0) | headgear - | last run 26 days | form 331340 | MARKET 3.6% | 09:00 median 21.00 | Matchbook 29.00
    DATA: model 7.6% | style Leader (led 38% of runs) | runs in data 10 | last 3: 29 Aug Windsor Flat 8.1f Soft 3/8; 27 Sep Epsom Downs Flat 8.5f Good 4/8; 26 Oct Kempton (AW) Flat 8f Standard / Slow 11/13 fig 56
    DATA against: Best recent form figure 56, 9 lb below field average; Recent figures 19 lb below its current mark (looks high in the weights)
- Royal Bodyguard (hrs_50434349) | 3yo G | 133lb | OR 72 | draw 1 | jockey Callum Shepherd | trainer Michael Bell (14d 1/2) | headgear - | last run 72 days | form 364210 | MARKET 2.9% | 09:00 median 26.00 | Matchbook 40.00
    comment: Unplaced last time out and off a 72-day break, Royal Bodyguard is hard to fancy, though he did win two starts back, and he has run over today's trip and going before.
    DATA: model 11.8% | style Prominent (led 8% of runs) | runs in data 7 | last 3: 12 Aug Ffos Las Flat 8f Good 2/5; 22 Aug Newmarket Flat 8f Good 1/7; 10 Sep Epsom Downs Flat 8.5f Good To Soft 10/10
    DATA for: Good recent finishing positions
- Director's Cut (hrs_57941989) | 3yo G | 130lb | OR 69 | draw 10 | jockey Josephine Gordon | trainer Ross Burdon (14d 1/2) | headgear v (1st time) | last run 22 days | form -55008 | MARKET 2.2% | 09:00 median 34.00 | Matchbook 55.00
    comment: Director's Cut is winless in his last five, finishing eighth last time out after two unplaced runs, which makes him hard to fancy, though he has run over today's trip and going and returns after 22 days.
    DATA: model 3.8% | style Prominent (led 29% of runs) | runs in data 5 | last 3: 29 Jun Kempton Flat 8f Standard To Slow 10/14; 11 Sep Doncaster Flat 10.2f Good 16/17; 30 Oct Newcastle (AW) Flat 8f Standard 8/10 fig 62
    DATA for: Carries 5 lb less than average; First-time headgear
    DATA against: Recent figures 7 lb below its current mark (looks high in the weights); Poor recent finishing positions

## 1:45 Lingfield (AW) | race_id rac_32305101413 | Midnite Built Different Handicap Stakes
Flat | Class 4 | 6f1y | going Standard | AW | 11 runners | rating band 0-85 | age 3yo+
DATA pace: Lone leader - Hucklesbrook is the only habitual front-runner and may be allowed an easy lead.
- Uncle Don (hrs_42327698) | 4yo G | 135lb | OR 85 | draw 3 | jockey Marco Ghiani | trainer Robert Cowell (14d 0/5) | headgear - | last run 14 days | form 520548 | MARKET 25.5% | 09:00 median 3.25 | Matchbook 3.60 | CHECK (skip line 3.09)
    DATA: model 13.5% | style Prominent (led 8% of runs) | runs in data 7 | last 3: 10 Aug Windsor Flat 6.1f Good To Firm 5/16; 19 Sep Ayr Flat 6f Heavy 4/23; 7 Nov Doncaster Flat 6f Good To Soft 8/22 fig 89
    DATA for: Best recent form figure 89, 10 lb above field average; Recent figures 4 lb above its current mark (looks well handicapped)
- Tan Rapido (hrs_35459018) | 5yo G | 131lb | OR 81 | draw 5 | jockey Paddy Bradley | trainer Charlie Fellowes (14d 1/4) | headgear - | last run 5 days | form 788123 | MARKET 23.7% | 09:00 median 3.50 | Matchbook 3.85
    comment: Tan Rapido arrives in good heart with a third last time out, a second before that and a winner three starts back, and he has run over today's trip and going.
    DATA: model 16.0% | style Midfield (led 4% of runs) | runs in data 6 | last 3: 6 Jul Lingfield Flat 5f Standard 1/9; 3 Nov Wolverhampton (AW) Flat 6f Standard 2/12 fig 82; 16 Nov Wolverhampton (AW) Flat 5f Standard 3/11 fig 79
    DATA for: Good recent finishing positions
- Hucklesbrook (hrs_41503966) | 4yo G | 135lb | OR 85 | draw 6 | jockey Kieran Shoemark | trainer Roger Teal (14d 0/4) | headgear - | last run 56 days | form -48036 | MARKET 10.2% | 09:00 median 8.00 | Matchbook 9.40
    comment: The risk is a 56-day break after a sixth last time out, and he is yet to win in his last five starts.
    DATA: model 7.8% | style Leader (led 38% of runs) | runs in data 5 | last 3: 27 Jul Windsor Flat 6.1f Good To Firm 10/13; 15 Aug Newbury Flat 5.2f Good To Firm 3/12; 26 Sep Haydock Flat 5f Heavy 6/10
    DATA for: Pace: may get an uncontested lead
- Baldomero (hrs_22897546) | 8yo G | 131lb | OR 81 | draw 9 | jockey Cieren Fallon | trainer Michael Appleby (14d 0/8) | headgear b | last run 35 days | form 694425 | MARKET 8.9% | 09:00 median 8.50 | Matchbook 11.50
    comment: Baldomero was second two starts back and fifth last time out, and he has run over today's trip and going before, so his figures look a sound fit.
    DATA: model 10.8% | style Prominent (led 5% of runs) | runs in data 13 | last 3: 11 Sep Salisbury Flat 6f Soft 4/8; 9 Oct York Flat 5f Good To Soft 2/14; 17 Oct Catterick Flat 6f Good 5/10 fig 83
    DATA for: Best recent form figure 83, 4 lb above field average
    DATA against: Trainer 0 wins from 8 runs, last 14 days; Aged 8, older than most of this field
- Artagnan (hrs_41782391) | 4yo G | 130lb | OR 80 | draw 4 | jockey Billy Loughnane | trainer Ian Williams (14d 2/11) | headgear - | last run 33 days | form 240389 | MARKET 8.6% | 09:00 median 9.00 | Matchbook 11.50
    comment: Artagnan has run over today's trip and going, and a third three starts back shows he can go close, but he's yet to win in his last six and comes here on the back of an eighth and a ninth.
    DATA: model 3.8% | style Held up (led 5% of runs) | runs in data 6 | last 3: 29 Jul Redcar Flat 6f Good To Firm 3/7; 5 Oct Pontefract Flat 6f Good 8/10; 19 Oct Wolverhampton (AW) Flat 6f Standard 9/12 fig 78
- Brosay (hrs_40225717) | 4yo G | 133lb | OR 83 | draw 11 | jockey Kieren Fox | trainer Charlie Pike (14d 0/1) | headgear b | last run 41 days | form 992263 | MARKET 7.2% | 09:00 median 11.00 | Matchbook 13.50
    comment: The one concern is that he is yet to win in that spell and returns after 41 days off.
    DATA: model 13.2% | style Held up (led 8% of runs) | runs in data 13 | last 3: 23 Sep Goodwood Flat 6f Good 2/15; 1 Oct Salisbury Flat 6f Soft 6/14; 11 Oct Goodwood Flat 6f Good To Soft 3/13
    DATA for: Good recent finishing positions
- Angel Gabriel (hrs_50433432) | 3yo G | 132lb | OR 82 | draw 2 | jockey Luke Morris | trainer Michael Keady (14d 0/0) | headgear - | last run 29 days | form 834135 | MARKET 3.9% | 09:00 median 19.00 | Matchbook 27.00
    comment: Fifth last time out after a third two starts back, and a winner three starts back, Angel Gabriel is consistent and has run over today's trip and going, though he carries 132 lb from stall two and has just one win in his last six starts.
    DATA: model 14.5% | style Prominent (led 29% of runs) | runs in data 7 | last 3: 29 Aug Windsor Flat 6.1f Soft 1/6; 26 Sep Haydock Flat 6f Heavy 3/11; 23 Oct Doncaster Flat 6f Heavy 5/11 fig 84
    DATA for: Best recent form figure 84, 5 lb above field average; Has won at this trip or further; Good recent finishing positions
- Shaman Champion (hrs_52641484) | 3yo G | 130lb | OR 80 | draw 7 | jockey Callum Shepherd | trainer Henrietta C Knight (14d 0/7) | headgear - | last run 30 days | form 003507 | MARKET 3.6% | 09:00 median 21.00 | Matchbook 29.00
    comment: Shaman Champion has run over today's trip and going, and a third four starts back shows he can pick up a cheque, but he's yet to win in his last six and was seventh last time out.
    DATA: model 4.2% | style Midfield (led 3% of runs) | runs in data 7 | last 3: 2 Sep Kempton Flat 7f Standard To Slow 5/7; 23 Sep Kempton Flat 7f Standard To Slow 13/13; 22 Oct Newmarket Flat 6f Soft 7/12 fig 78
- Supreme King (hrs_31005933) | 6yo G | 130lb | OR 80 | draw 1 | jockey Charles Bishop | trainer David Evans (14d 0/7) | headgear - | last run 21 days | form 563353 | MARKET 3.4% | 09:00 median 23.00 | Matchbook 34.00
    comment: Supreme King has finished third last time out, and a third three starts back, while still yet to win in his last six, and he's had 21 days to recover; he has run over today's trip and going.
    DATA: model 7.8% | style Held up (led 5% of runs) | runs in data 18 | last 3: 19 Sep Chester Flat 6.1f Heavy 3/10; 1 Oct Salisbury Flat 6f Soft 5/14; 31 Oct Newmarket Flat 6f Good To Soft 3/10 fig 79
    DATA for: Has won at this trip or further; Good recent finishing positions
- Star Chorus (hrs_45887737) | 4yo G | 130lb | OR 80 | draw 12 | jockey Rob Hornby | trainer Mike Murphy (14d 0/1) | headgear - | last run 21 days | form 604010 | MARKET 3.0% | 09:00 median 23.00 | Matchbook 38.00
    comment: Star Chorus is hard to fancy after finishing unplaced last time out, and he's had only one win in his last six starts, a victory two starts back.
    DATA: model 5.3% | style Unknown | runs in data 15 | last 3: 23 Sep Goodwood Flat 6f Good 12/15; 5 Oct Kempton Flat 6f Standard To Slow 1/10; 31 Oct Newmarket Flat 6f Good To Soft 10/10 fig 63
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 63, 16 lb below field average; Recent figures 17 lb below its current mark (looks high in the weights)
- Seven Questions (hrs_35336917) | 5yo G | 129lb | OR 79 | draw 8 | jockey Jack Dace(5) | trainer Robert Cowell (14d 0/5) | headgear - | last run 22 days | form 700487 | MARKET 2.1% | 09:00 median 29.00 | Matchbook 65.00
    comment: He has run over today's trip and returns after 22 days, but 129 lb from stall 8 offers little encouragement.
    DATA: model 3.3% | style Midfield (led 8% of runs) | runs in data 10 | last 3: 30 Aug Yarmouth Flat 5.2f Good To Soft 4/4; 6 Oct Leicester Flat 5f Good To Firm 8/11; 30 Oct Newmarket Flat 5f Good To Soft 7/13 fig 75
    DATA against: Best recent form figure 75, 4 lb below field average

## 2:20 Lingfield (AW) | race_id rac_32305103350 | Midnite A Next Generation Betting App Handicap Stakes
Flat | Class 6 | 6f1y | going Standard | AW | 11 runners | rating band 0-65 | age 3yo+
DATA pace: Lone leader - Midnight Call is the only habitual front-runner and may be allowed an easy lead.
- Giorgio M (hrs_37276246) | 5yo G | 138lb | OR 64 | draw 6 | jockey Billy Loughnane | trainer Mark Loughnane (14d 1/8) | headgear tp | last run 5 days | form 477791 | MARKET 23.8% | 09:00 median 3.50 | Matchbook 3.85 | CHECK (skip line 3.32)
    comment: The risk is a patchy record before that win, with three sevenths and a ninth in the run prior.
    DATA: model 7.3% | style Midfield (led 29% of runs) | runs in data 10 | last 3: 1 Jun Wolverhampton Flat 6.1f Standard 7/12; 2 Jul Kempton Flat 6f Standard To Slow 9/11; 16 Nov Wolverhampton (AW) Flat 7f Standard 1/11 fig 72
    DATA for: Best recent form figure 72, 11 lb above field average; Recent figures 8 lb above its current mark (looks well handicapped); Has won at this trip or further
- Fuseboard (hrs_58380287) | 3yo G | 132lb | OR 63 | draw 8 | jockey Joey Haynes | trainer Chelsea Banham (14d 1/2) | headgear - | last run 93 days | form 0-6411 | MARKET 14.2% | 09:00 median 5.50 | Matchbook 6.80
    DATA: model 14.4% | style Prominent (led 38% of runs) | runs in data 4 | last 3: 12 May Lingfield Flat 7f Standard 4/8; 7 Jul Wolverhampton Flat 5.1f Standard 1/7; 20 Aug Lingfield Flat 6f Standard 1/11
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Returns from a 93-day break
- Yachtsman (hrs_53633027) | 3yo G | 133lb | OR 64 | draw 7 | jockey Neil Callan | trainer Jack Morland (14d 0/0) | headgear p (1st time) | last run 19 days | form 494893 | MARKET 13.0% | 09:00 median 6.50 | Matchbook 7.00
    comment: The risk is a winless run in his last six starts, with finishes of ninth and eighth in that spell.
    DATA: model 9.0% | style Midfield (led 4% of runs) | runs in data 10 | last 3: 8 Sep Leicester Flat 6f Good To Soft 8/11; 15 Oct Brighton Flat 8f Good 9/14 fig 59; 2 Nov Chelmsford (AW) Flat 7f Standard 3/13 fig 71
    DATA for: Best recent form figure 71, 10 lb above field average; Recent figures 7 lb above its current mark (looks well handicapped); Last-run finishing speed +3.1% vs that field (finished strongly); Has won at this trip or further; First-time headgear
- Phoenix Moon (hrs_33790281) | 5yo M | 133lb | OR 64 | draw 12 | jockey Rob Hornby | trainer Denis Coakley (14d 1/2) | headgear - | last run 17 days | form 388612 | MARKET 9.5% | 09:00 median 8.50 | Matchbook 10.00
    comment: Phoenix Moon arrives in good heart, second last time out and a winner two starts back, with 17 days since her last run and experience of today's trip and going.
    DATA: model 9.0% | style Midfield (led 3% of runs) | runs in data 9 | last 3: 1 Sep Lingfield Flat 6f Standard 6/8; 2 Oct Wolverhampton Flat 6.1f Standard 1/10; 4 Nov Kempton (AW) Flat 6f Standard / Slow 2/7 fig 67
    DATA for: Best recent form figure 67, 6 lb above field average; Has won at this trip or further; Good recent finishing positions
- Macarone (hrs_35713769) | 5yo G | 134lb | OR 65 | draw 9 | jockey Ben Ffrench Davis(5) | trainer Grace Harris (14d 1/7) | headgear - | last run 19 days | form 511111 | MARKET 8.2% | 09:00 median 8.50 | Matchbook 13.50
    DATA: model 20.3% | style Midfield (led 3% of runs) | runs in data 16 | last 3: 27 Sep Ffos Las Flat 6f Soft 1/11; 19 Oct Wolverhampton (AW) Flat 6f Standard 1/13 fig 57; 2 Nov Wolverhampton (AW) Flat 6f Standard 1/10 fig 63
    DATA for: Has won at this trip or further; Good recent finishing positions
- Herculeus (hrs_45346098) | 4yo G | 133lb | OR 64 | draw 10 | jockey Edward Greatrex | trainer William Muir & Chris Grassick (14d 0/4) | headgear b | last run 24 days | form 506080 | MARKET 7.0% | 09:00 median 12.00 | Matchbook 13.00
    comment: The risk is obvious, though: he's winless in his last six, with a fifth six starts back his best finish.
    DATA: model 5.8% | style Midfield (led 4% of runs) | runs in data 7 | last 3: 9 Sep Kempton Flat 8f Standard To Slow 10/13; 24 Sep Southwell Flat 7.1f Standard 8/9; 28 Oct Kempton (AW) Flat 7f Standard / Slow 10/13 fig 57
    DATA against: Best recent form figure 57, 4 lb below field average; Recent figures 7 lb below its current mark (looks high in the weights); Poor recent finishing positions
- Elvetham (hrs_43797187) | 4yo G | 133lb | OR 64 | draw 5 | jockey Robert Havlin | trainer Conrad Allen (14d 0/0) | headgear b | last run 19 days | form 101695 | MARKET 5.8% | 09:00 median 13.00 | Matchbook 17.50
    comment: Elvetham has slipped to a fifth, a ninth and a sixth in his last three runs after winning four starts back, so it's hard to fancy him now, though he has run over today's trip and going and is back after 19 days.
    DATA: model 4.2% | style Midfield (led 23% of runs) | runs in data 17 | last 3: 24 Sep Southwell Flat 5f Standard 6/7; 21 Oct Kempton (AW) Flat 6f Standard / Slow 9/12 fig 57; 2 Nov Chelmsford (AW) Flat 5f Standard 5/7 fig 58
    DATA for: Has won at this trip or further
    DATA against: Recent figures 6 lb below its current mark (looks high in the weights)
- Way To Dubai (hrs_31022481) | 7yo G | 130lb | OR 61 | draw 1 | jockey Jason Watson | trainer Michael Appleby (14d 0/8) | headgear - | last run 29 days | form 040437 | MARKET 5.4% | 09:00 median 15.00 | Matchbook 18.00
    comment: Way To Dubai was beaten into seventh last time out, but he has a third two starts back and a fourth three starts back, and has run over today's trip and going.
    DATA: model 5.6% | style Held up (led 8% of runs) | runs in data 16 | last 3: 1 Jul Thirsk Flat 7f Good To Firm 4/10; 28 Jul Yarmouth Flat 7f Good To Firm 3/9; 23 Oct Wolverhampton (AW) Flat 6f Standard 7/7 fig 48
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 48, 13 lb below field average; Recent figures 13 lb below its current mark (looks high in the weights); Trainer 0 wins from 8 runs, last 14 days; Aged 7, older than most of this field
- Far Too Fizzy (hrs_52054849) | 3yo G | 134lb | OR 65 | draw 4 | jockey Laura Pearson | trainer David Loughnane (14d 1/4) | headgear - | last run 16 days | form 354719 | MARKET 5.2% | 09:00 median 13.00 | Matchbook 23.00
    comment: Far Too Fizzy won two starts back but was only ninth last time out, and he has run over today's trip and on the going before.
    DATA: model 9.7% | style Held up (led 4% of runs) | runs in data 14 | last 3: 2 Oct Wolverhampton Flat 6.1f Standard 7/10; 13 Oct Wolverhampton Flat 6.1f Standard 1/12; 5 Nov Chelmsford (AW) Flat 6f Standard 9/10 fig 50
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 50, 11 lb below field average; Recent figures 15 lb below its current mark (looks high in the weights)
- An Outlaw's Grace (hrs_39190438) | 4yo G | 134lb | OR 65 | draw 3 | jockey Ben Pollard(7) | trainer Richard Hannon (14d 0/5) | headgear p | last run 17 days | form 260757 | MARKET 4.8% | 09:00 median 17.00 | Matchbook 20.00
    comment: Official mark of 65 looks workable from draw 3, though he's yet to win in his last six and was seventh last time out.
    DATA: model 6.3% | style Held up (led 3% of runs) | runs in data 15 | last 3: 7 Oct Kempton Flat 6f Standard To Slow 7/11; 19 Oct Bath Flat 5f Good To Soft 5/8 fig 64; 4 Nov Kempton (AW) Flat 6f Standard / Slow 7/11 fig 62
- Midnight Call (hrs_36527981) | 5yo M | 132lb | OR 63 | draw 2 | jockey Luke Morris | trainer Tony Carroll (14d 1/15) | headgear - | last run 44 days | form 410275 | MARKET 3.0% | 09:00 median 26.00 | Matchbook 34.00
    comment: Midnight Call has been beaten in her last two, a fifth last time out and a seventh two starts back, and returns after 44 days off, which makes her hard to fancy. She has run over today's trip and going, and a win five starts back is the best of her recent form, but 132 lb from draw 2 is no gift.
    DATA: model 8.5% | style Leader (led 43% of runs) | runs in data 13 | last 3: 7 Sep Wolverhampton Flat 5.1f Standard 2/9; 21 Sep Wolverhampton Flat 6.1f Standard 7/10; 8 Oct Bath Flat 5f Good 5/14
    DATA for: Has won at this trip or further; Pace: may get an uncontested lead

## 3:05 Lingfield (AW) | race_id rac_32305105287 | Make The Move To Midnite Handicap Stakes
Flat | Class 5 | 1m1y | going Standard | AW | 11 runners | rating band 0-70 | age 3yo+
DATA pace: Strong pace - 3 habitual front-runners (Panama Black, Dion Baker, Musical Soldier). A contested lead should set things up for horses coming from behind.
- The Anthony Gover (hrs_62615126) | 3yo G | 134lb | OR 68 | draw 6 | jockey Billy Loughnane | trainer Dr Richard Newland (14d 0/0) | headgear b | last run 19 days | form 211323 | MARKET 32.5% | 09:00 median 2.63 | Matchbook 2.82
    comment: The Anthony Gover arrives in cracking form, with a third last time out, a second two starts back and two wins in his last six, and he has run over today's trip and going before.
    DATA: model 21.7% | style Midfield (led 4% of runs) | runs in data 13 | last 3: 28 Sep Wolverhampton Flat 9.5f Standard 3/11; 19 Oct Wolverhampton (AW) Flat 9.5f Standard 2/10 fig 64; 2 Nov Wolverhampton (AW) Flat 9.5f Standard 3/9 fig 67
    DATA for: Best recent form figure 67, 13 lb above field average; Official rating 68, 6 lb above field average; Has won at this trip or further; Good recent finishing positions
- Victory Sound (hrs_39961719) | 4yo G | 120lb | OR 52 | draw 8 | jockey Gina Mangan | trainer Mark Usher (14d 0/2) | headgear p | last run 22 days | form 621532 | MARKET 14.3% | 09:00 median 5.75 | Matchbook 6.60
    comment: Victory Sound was second last time out and third two starts back, so the form is respectable, but he has just one win in his last six and that came four starts back.
    DATA: model 7.2% | style Held up (led 4% of runs) | runs in data 10 | last 3: 23 Sep Kempton Flat 7f Standard To Slow 5/13; 2 Oct Newcastle Flat 7.1f Standard 3/13; 30 Oct Newcastle (AW) Flat 7f Standard 2/10 fig 56
    DATA for: Recent figures 4 lb above its current mark (looks well handicapped); Good recent finishing positions; Carries 10 lb less than average; Pace: a contested lead should suit its hold-up style
    DATA against: Official rating 52, 10 lb below field average
- Mooncoin (hrs_62360858) | 3yo F | 123lb | OR 57 | draw 4 | jockey Cieren Fallon | trainer Jack Jones (14d 0/3) | headgear - | last run 50 days | form 909 | MARKET 10.7% | 09:00 median 7.50 | Matchbook 9.20
    comment: Mooncoin is winless in her last three, finishing ninth last time out, unplaced two starts back and ninth three starts back, and she returns after 50 days off.
    DATA: model 1.8% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 6 Mar Dundalk Flat 8f Standard 9/14; 21 Sep Fairyhouse Flat 7f Good 10/17; 2 Oct Dundalk Flat 7f Standard 9/13
    DATA for: Carries 7 lb less than average
    DATA against: Official rating 57, 5 lb below field average; Poor recent finishing positions
- Didaar (hrs_34471276) | 5yo G | 133lb | OR 65 | draw 11 | jockey Darragh Keenan | trainer Gihan Arnolda (14d 0/2) | headgear - | last run 16 days | form 713566 | MARKET 9.2% | 09:00 median 9.00 | Matchbook 10.50
    comment: Didaar has finished sixth in each of his last two, though a third four starts back and a win five starts back show he can go well, and he's had only 16 days off.
    DATA: model 8.0% | style Held up (led 4% of runs) | runs in data 7 | last 3: 6 Aug Newmarket Flat 12f Good To Firm 5/6; 1 Oct Nottingham Flat 10.2f Good 6/14; 5 Nov Southwell (AW) Flat 8f Standard 6/12 fig 59
    DATA for: Best recent form figure 59, 5 lb above field average; Has won at this trip or further; Pace: a contested lead should suit its hold-up style
    DATA against: Recent figures 6 lb below its current mark (looks high in the weights)
- Musical Soldier (hrs_53269237) | 3yo G | 135lb | OR 69 | draw 12 | jockey Sean Dylan Bowen | trainer Ollie Sangster (14d 0/1) | headgear t | last run 73 days | form 211122 | MARKET 9.0% | 09:00 median 9.00 | Matchbook 11.00
    comment: Musical Soldier arrives in fine heart, a second last time out and another second two starts back after three straight wins before that, and he has run over today's trip and going.
    DATA: model 25.0% | style Leader (led 23% of runs) | runs in data 14 | last 3: 25 Aug Lingfield Flat 7f Standard 1/8; 1 Sep Lingfield Flat 8f Standard 2/5; 9 Sep Kempton Flat 7f Standard To Slow 2/14
    DATA for: Official rating 69, 7 lb above field average; Good recent finishing positions
    DATA against: Carries 5 lb more than average; Pace: likely to be taken on for the lead
- Starlight Sami (hrs_53572596) | 3yo G | 134lb | OR 68 | draw 1 | jockey George Bass | trainer Denis Coakley (14d 1/2) | headgear v (1st time) | last run 26 days | form 310796 | MARKET 6.8% | 09:00 median 11.00 | Matchbook 15.50
    comment: Starlight Sami won five starts back and has run over today's trip and on this going, so he knows the conditions, and he returns fresh after 26 days.
    DATA: model 8.2% | style Midfield (led 4% of runs) | runs in data 6 | last 3: 17 Jul Newbury Flat 8f Good To Firm 7/10; 20 Aug Lingfield Flat 7f Standard 9/11; 26 Oct Southwell (AW) Flat 8f Standard 6/9 fig 59
    DATA for: Best recent form figure 59, 5 lb above field average; Official rating 68, 6 lb above field average; First-time headgear
    DATA against: Recent figures 9 lb below its current mark (looks high in the weights); Poor recent finishing positions
- Panama Black (hrs_45314927) | 4yo G | 138lb | OR 70 | draw 3 | jockey Luke Morris | trainer Laura Mongan (14d 0/0) | headgear p | last run 17 days | form 347866 | MARKET 6.3% | 09:00 median 13.00 | Matchbook 15.50
    comment: The main risk is that he has finished sixth last time out, and a sixth before that, so he needs to arrest that slide.
    DATA: model 7.0% | style Leader (led 38% of runs) | runs in data 8 | last 3: 18 May Lingfield Flat 10f Good 8/8; 6 Oct Brighton Flat 8f Good To Firm 6/10; 4 Nov Kempton (AW) Flat 7f Standard / Slow 6/11 fig 71
    DATA for: Best recent form figure 71, 17 lb above field average; Official rating 70, 8 lb above field average
    DATA against: Poor recent finishing positions; Carries 8 lb more than average; Pace: likely to be taken on for the lead
- Dion Baker (hrs_27206634) | 7yo G | 137lb | OR 69 | draw 2 | jockey David Egan | trainer Michael Wigham (14d 0/1) | headgear p | last run 54 days | form 382948 | MARKET 4.8% | 09:00 median 17.00 | Matchbook 20.00
    DATA: model 8.7% | style Leader (led 79% of runs) | runs in data 16 | last 3: 23 Aug Brighton Flat 6f Good To Firm 9/16; 1 Sep Brighton Flat 7f Good 4/6; 28 Sep Brighton Flat 8f Good To Firm 8/10
    DATA for: Official rating 69, 7 lb above field average
    DATA against: Carries 7 lb more than average; Aged 7, older than most of this field; Pace: likely to be taken on for the lead
- Blue Collar Lad (hrs_24386243) | 7yo G | 119lb | OR 49 | draw 7 | jockey Tyler Heard | trainer Daniel Steele (14d 0/0) | headgear p | last run 37 days | form 270432 | MARKET 3.6% | 09:00 median 21.00 | Matchbook 29.00
    comment: Blue Collar Lad is winless in his last six, though he has been consistent, finishing second last time out and third the run before, and he has run over today's trip and going.
    DATA: model 6.2% | style Midfield (led 3% of runs) | runs in data 6 | last 3: 10 Sep Lingfield Flat 7f Standard 4/11; 10 Oct Southwell Flat 8.1f Standard 3/12; 15 Oct Brighton Flat 7f Good 2/13 fig 52
    DATA for: Good recent finishing positions; Carries 11 lb less than average
    DATA against: Official rating 49, 13 lb below field average; Aged 7, older than most of this field
- Wind Summer (hrs_56961807) | 3yo G | 129lb | OR 63 | draw 9 | jockey Jack Dace(5) | trainer Luke Dace (14d 0/4) | headgear p | last run 17 days | form 701400 | MARKET 1.4% | 09:00 median 51.00 | Matchbook 90.00
    comment: Wind Summer won four starts back and was a fourth three starts back, but he has been unplaced in his last two outings, so the form has cooled.
    DATA: model 4.1% | style Prominent (led 29% of runs) | runs in data 8 | last 3: 5 Oct Kempton Flat 8f Standard To Slow 4/10; 22 Oct Newmarket Flat 8f Soft 12/13 fig 33; 4 Nov Kempton (AW) Flat 7f Standard / Slow 11/11 fig 28
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 33, 21 lb below field average; Recent figures 30 lb below its current mark (looks high in the weights); Last-run finishing speed -3.5% vs that field (faded)
- Upepo (hrs_30865807) | 6yo G | 124lb | OR 56 | draw 5 | jockey Myla Coppins(5) | trainer Tony Carroll (14d 1/15) | headgear - | last run 14 days | form 349760 | MARKET 1.3% | 09:00 median 51.00 | Matchbook 100.00
    comment: Upepo is winless in his last six and unplaced last time, though he has run over today's trip and going before and is back quickly after 14 days.
    DATA: model 1.9% | style Midfield (led 4% of runs) | runs in data 7 | last 3: 30 Apr Lingfield Flat 12f Standard 7/8; 19 May Lingfield Flat 11.6f Good 6/8; 7 Nov Southwell (AW) Flat 8f Standard 11/11 fig 38
    DATA for: Carries 6 lb less than average
    DATA against: Best recent form figure 38, 16 lb below field average; Recent figures 18 lb below its current mark (looks high in the weights); Official rating 56, 6 lb below field average; Poor recent finishing positions

## 3:40 Lingfield (AW) | race_id rac_32305107224 | Midnite It's Actually Pretty Good Handicap Stakes
Flat | Class 6 | 1m4f1y | going Standard | AW | 12 runners | rating band 0-65 | age 3yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Brave Leader (hrs_57255660) | 3yo G | 132lb | OR 65 | draw 4 | jockey Luke Morris | trainer James Owen (14d 3/30) | headgear p | last run 26 days | form 646931 | MARKET 32.5% | 09:00 median 2.50 | Matchbook 2.74
    comment: He has run over today's trip and going, and 26 days since his last run is no concern, yet 132 lb is a lot to carry.
    DATA: model 21.5% | style Midfield (led 3% of runs) | runs in data 6 | last 3: 27 Aug Ffos Las Flat 10f Good 9/9; 8 Sep Goodwood Flat 9.9f Soft 3/10; 26 Oct Kempton (AW) Flat 11f Standard / Slow 1/10 fig 65
    DATA for: Best recent form figure 65, 6 lb above field average; Good recent finishing positions
- Adalo (hrs_64257984) | 3yo G | 132lb | OR 65 | draw 2 | jockey Cieren Fallon | trainer William Haggas (14d 2/11) | headgear t | wind surgery | last run 131 days | form 767 | MARKET 17.5% | 09:00 median 4.50 | Matchbook 5.30
    comment: Adalo is hard to fancy, having finished seventh, sixth and seventh in his last three starts and now returning after 131 days off.
    DATA: model 9.3% | style Midfield (led 8% of runs) | runs in data 3 | last 3: 2 May Goodwood Flat 8f Good 7/9; 15 Jun Windsor Flat 10f Good To Firm 6/13; 13 Jul Windsor Flat 8.1f Good To Firm 7/11
    DATA against: Poor recent finishing positions; Returns from a 131-day break
- Little Miss India (hrs_42042196) | 5yo M | 136lb | OR 64 | draw 12 | jockey Marco Ghiani | trainer James Owen (14d 3/30) | headgear h | last run 17 days | form 504785 | MARKET 13.2% | 09:00 median 6.00 | Matchbook 6.80
    comment: The risk is a winless run in her last six, with a fourth four starts back her best of late.
    DATA: model 10.2% | style Held up (led 3% of runs) | runs in data 12 | last 3: 5 Oct Wolverhampton Flat 9.5f Standard 7/11; 19 Oct Wolverhampton (AW) Flat 9.5f Standard 8/10 fig 59; 4 Nov Kempton (AW) Flat 12f Standard / Slow 5/14 fig 64
    DATA for: Best recent form figure 64, 6 lb above field average; Last-run finishing speed +3.1% vs that field (finished strongly); Has won at this trip or further
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Off Spin (hrs_44199232) | 4yo G | 135lb | OR 63 | draw 8 | jockey Billy Loughnane | trainer Gay Kelleway (14d 0/2) | headgear t | last run 17 days | form 325151 | MARKET 9.1% | 09:00 median 7.50 | Matchbook 11.50
    comment: Off Spin won last time out and again three starts back, so he arrives fresh enough after 17 days, and he has run over today's trip and going.
    DATA: model 16.1% | style Held up (led 3% of runs) | runs in data 13 | last 3: 28 Sep Hamilton Flat 12.1f Soft 1/10; 8 Oct Ayr Flat 13.1f Heavy 5/5; 4 Nov Musselburgh Flat 12.5f Soft 1/10 fig 66
    DATA for: Best recent form figure 66, 8 lb above field average; Last-run finishing speed +5.5% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Raintown (hrs_32371423) | 6yo G | 137lb | OR 65 | draw 5 | jockey David Egan | trainer J. S. Moore (14d 0/7) | headgear - | last run 64 days | form 231237 | MARKET 8.5% | 09:00 median 9.50 | Matchbook 11.00
    comment: Raintown has hit the frame in five of his last six, including a win four starts back and a third two starts back, and he has run over today's trip and going before.
    DATA: model 11.3% | style Held up (led 4% of runs) | runs in data 11 | last 3: 14 Aug Newbury Flat 10f Good To Firm 2/4; 28 Aug Ffos Las Flat 11.9f Good To Soft 3/5; 18 Sep Newbury Flat 10f Good 7/8
    DATA for: Good recent finishing positions
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Tortured Soul (hrs_36738604) | 6yo G | 137lb | OR 65 | draw 9 | jockey Neil Callan | trainer Tony Carroll (14d 1/15) | headgear - | last run 19 days | form 240979 | MARKET 7.8% | 09:00 median 10.00 | Matchbook 12.50
    comment: The risk is form figures of ninth, seventh and ninth in his last three outings, and he is winless in recent starts.
    DATA: model 5.3% | style Midfield (led 4% of runs) | runs in data 13 | last 3: 21 Sep Leicester Flat 8.2f Good 9/13; 5 Oct Wolverhampton Flat 9.5f Standard 7/10; 2 Nov Wolverhampton (AW) Flat 9.5f Standard 9/9 fig 49
    DATA against: Best recent form figure 49, 10 lb below field average; Recent figures 16 lb below its current mark (looks high in the weights); Poor recent finishing positions
- Masterofperfection (hrs_43796655) | 4yo G | 136lb | OR 64 | draw 7 | jockey Gina Mangan | trainer Dr Richard Newland (14d 0/0) | headgear p | last run 513 days | form 56612- | MARKET 4.4% | 09:00 median 17.00 | Matchbook 23.00
    comment: Second last time out and a winner two starts back, Masterofperfection has the recent form to interest, and he has run over today's trip and going, but a 513-day absence and 136 lb are real hurdles.
    DATA: model 7.6% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 513-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Letmebetheboss (hrs_36023456) | 5yo G | 131lb | OR 59 | draw 1 | jockey William Carson | trainer Tony Carroll (14d 1/15) | headgear p (1st time) | last run 26 days | form 4-7980 | MARKET 1.9% | 09:00 median 36.00 | Matchbook 70.00
    comment: Letmebetheboss is hard to fancy, unplaced last time and finishing eighth, ninth and seventh before that, so he is winless in his last five starts.
    DATA: model 4.0% | style Prominent (led 23% of runs) | runs in data 4 | last 3: 14 Sep Kempton Flat 11f Standard To Slow 9/9; 5 Oct Kempton Flat 12f Standard To Slow 8/10; 26 Oct Kempton (AW) Flat 16f Standard / Slow 11/12
    DATA for: First-time headgear
    DATA against: Poor recent finishing positions
- Liberate (hrs_43892485) | 4yo F | 137lb | OR 65 | draw 11 | jockey Tom Queally | trainer Jim & Suzi Best (14d 1/3) | headgear - | last run 19 days | form 159787 | MARKET 1.5% | 09:00 median 34.00 | Matchbook 120.00
    comment: Liberate has run over today's trip and going and is fresh enough after 19 days, but the filly has finished seventh, eighth, seventh and ninth since a win six starts back, and 137 lb is no help.
    DATA: model 5.4% | style Held up (led 5% of runs) | runs in data 18 | last 3: 9 Oct Kempton Flat 8f Standard To Slow 7/10; 22 Oct Southwell (AW) Flat 8f Standard 8/10 fig 59; 2 Nov Chelmsford (AW) Flat 10f Standard 7/8 fig 51
    DATA for: Has won at this trip or further
    DATA against: Recent figures 6 lb below its current mark (looks high in the weights); Poor recent finishing positions; Pace: steady gallop likely, hard to come from off the pace
- Somkiyr (hrs_58380301) | 5yo G | 134lb | OR 62 | draw 10 | jockey Rhys Clutterbuck | trainer Andy Irvine (14d 0/3) | headgear - | last run 17 days | form /88D60 | MARKET 1.4% | 09:00 median 51.00 | Matchbook 150.00
    comment: Somkiyr is winless in his last five, with a sixth two starts back his best finish in a modest run of form, though he is fresh enough after 17 days off.
    DATA: model 3.7% | style Held up (led 3% of runs) | runs in data 9 | last 3: 5 Jun Goodwood Flat 9.1f Good To Soft 8/8; 14 Jun Salisbury Flat 9.9f Good 6/10; 4 Nov Nottingham Flat 8.5f Soft 13/15
    DATA against: Last-run finishing speed -5.6% vs that field (faded); Poor recent finishing positions; Pace: steady gallop likely, hard to come from off the pace
- Perzaaneh (hrs_58844023) | 4yo F | 130lb | OR 58 | draw 3 | jockey Callum Hutchinson | trainer Patrick Chamings (14d 0/0) | headgear h | last run 26 days | form 687 | MARKET 1.2% | 09:00 median 41.00 | Matchbook 140.00
    comment: Perzaaneh is hard to fancy, having finished seventh last time out, an eighth two starts back and a sixth three starts back, and she is yet to win in that spell.
    DATA: model 1.5% | style Held up (led 4% of runs) | runs in data 3 | last 3: 14 Jun Salisbury Flat 9.9f Good 6/6; 7 Oct Kempton Flat 11f Standard To Slow 8/8; 26 Oct Kempton (AW) Flat 12f Standard / Slow 7/9 fig 48
    DATA against: Best recent form figure 48, 10 lb below field average; Recent figures 10 lb below its current mark (looks high in the weights); Poor recent finishing positions; Pace: steady gallop likely, hard to come from off the pace
- Soy Loco (hrs_49389144) | 4yo G | 132lb | OR 60 | draw 6 | jockey Paddy Bradley | trainer Simon Dow (14d 0/0) | headgear - | last run 17 days | form 6550-0 | MARKET 1.1% | 09:00 median 69.00 | Matchbook 160.00
    comment: The main risk is a winless recent run, with unplaced efforts in his last two starts.
    DATA: model 4.1% | style Held up (led 8% of runs) | runs in data 1 | last 3: 4 Nov Kempton (AW) Flat 8f Standard / Slow 13/13
    DATA against: Last-run finishing speed -7.2% vs that field (faded); Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
