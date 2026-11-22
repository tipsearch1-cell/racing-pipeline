# Card review packet: Cork, 2026-11-22

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
{"meeting": "cork", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 12:19 Cork | race_id rac_32305215696 | Irish Stallion Farms EBF Academy Hurdle
Hurdle |  | 2m1f0y | going Soft | Turf | 11 runners | rating band - | age 3yo
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Noon Blu Dodville (hrs_17394395431) | 3yo G | 154lb | OR - | draw 0 | jockey Donagh Meyler | trainer Emmet Mullins (14d 2/7) | headgear t (1st time) | last run 28 days | form F | MARKET 31.3% | 09:00 median 2.50 | Matchbook 2.92
    comment: Unexposed and open to improvement, Noon Blu Dodville is winless in his last start, when he fell, and returns after 28 days off; he carries 154 lb, so the limited form leaves plenty to learn.
    DATA: model 14.4% | style Unknown | runs in data 1 | last 3: 25 Oct Wexford (IRE) Hurdle 18f Soft F/8
    DATA for: Trainer 29% wins (2/7), last 14 days; First-time headgear
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on; Fell or unseated in 1 of its last 1 jumps runs
- Green Heritage (hrs_17393731040) | 3yo G | 154lb | OR - | draw 0 | jockey Jordan Gainford | trainer Cian Collins (14d 1/7) | headgear t | last run 39 days | form 3 | MARKET 22.2% | 09:00 median 3.50 | Matchbook 4.20
    comment: The one concern is that he is yet to win in recent form and carries 154 lb.
    DATA: model 18.6% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 14 Oct Punchestown Hurdle 18.9f Good 3/6
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Hansel The Purse (hrs_17393732083) | 3yo G | 154lb | OR - | draw 0 | jockey Luke Carberry(7) | trainer Michael Mulvany (14d 0/7) | headgear - | last run 28 days | form 42 | MARKET 15.1% | 09:00 median 5.00 | Matchbook 6.40
    comment: Hansel The Purse arrives in sound form after a second last time out and a fourth two starts back, and 28 days since that run suggests he should be fresh.
    DATA: model 10.9% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 14 Oct Punchestown Hurdle 18.9f Good 4/6; 25 Oct Wexford (IRE) Hurdle 18f Soft 2/8 fig 68
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Galyyath (hrs_17395860846) | 3yo G | 154lb | OR - | draw 0 | jockey Sam Ewing | trainer Paul John Gilligan (14d 0/4) | headgear - | last run - days | form - | MARKET 8.7% | 09:00 median 10.00 | Matchbook 10.00
    comment: Galyyath is an unexposed debutant with no recorded form to go on, so he's open to any amount of improvement.
    DATA: model 8.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Dublinia (hrs_17393728954) | 3yo G | 154lb | OR - | draw 0 | jockey Patrick M O'Brien(5) | trainer Michael Mulvany (14d 0/7) | headgear - | last run 12 days | form 5 | MARKET 7.9% | 09:00 median 10.00 | Matchbook 12.50
    DATA: model 7.3% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 10 Nov Fairyhouse (IRE) Hurdle 17f Good To Yielding 5/14 fig 68
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Around The Hill (hrs_17395858760) | 3yo G | 154lb | OR - | draw 0 | jockey Philip Donovan | trainer Jack Doyle (14d 0/0) | headgear - | last run - days | form - | MARKET 7.8% | 09:00 median 11.00 | Matchbook 12.00
    comment: Around The Hill is unexposed on debut with no form to assess, so there's plenty of scope for improvement. He carries 154 lb and has nothing yet to show on the racecard, which leaves him a blank canvas.
    DATA: model 8.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Our Destiny (hrs_17395251734) | 3yo G | 154lb | OR - | draw 0 | jockey James Smith(3) | trainer Ms Claire O'Connell (14d 0/3) | headgear - | last run - days | form - | MARKET 2.2% | 09:00 median 34.00 | Matchbook 44.00
    comment: He carries 154 lb and looks open to improvement as he begins his career.
    DATA: model 8.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Flip A Coin (hrs_17395859803) | 3yo G | 154lb | OR - | draw 0 | jockey Shane Markey(7) | trainer A. McCann (14d 0/3) | headgear h (1st time) | last run - days | form - | MARKET 2.1% | 09:00 median 51.00 | Matchbook 48.00
    comment: Flip A Coin is an unraced gelding with no form to go on, so he's an unexposed type with scope for improvement, and he shoulders 154 lb on what is effectively a blank-sheet debut.
    DATA: model 8.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: First-time headgear
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Way Horn (hrs_17393736255) | 3yo G | 154lb | OR - | draw 0 | jockey Mark McDonagh | trainer Sean O O'Brien (14d 0/2) | headgear - | last run 39 days | form 6 | MARKET 1.4% | 09:00 median 51.00 | Matchbook 100.00
    comment: The main risk is that he's yet to win in recent form, so he needs to improve on that sixth.
    DATA: model 6.2% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 14 Oct Punchestown Hurdle 18.9f Good 6/6
    DATA against: Last-run finishing speed -4.7% vs that field (faded); Lightly raced: 1 run in our data, so the model has little to go on
- Klaus (hrs_17395249648) | 3yo G | 154lb | OR - | draw 0 | jockey E Walsh | trainer Ciaran Murphy (14d 0/12) | headgear - | last run 12 days | form 9 | MARKET 0.9% | 09:00 median 81.00 | Matchbook 160.00
    comment: Klaus is unexposed after just one recent outing, a ninth last time out only 12 days ago, so he looks open to improvement. He's yet to win in that short spell and carries 154 lb here.
    DATA: model 5.8% | style Held up (led 8% of runs) | runs in data 1 | last 3: 10 Nov Fairyhouse (IRE) Hurdle 17f Good To Yielding 9/14
    DATA against: Trainer 0 wins from 12 runs, last 14 days; Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- One For Christy (hrs_17394396474) | 3yo F | 147lb | OR - | draw 0 | jockey Luke Burke Ott(7) | trainer L J Archdeacon (14d 0/0) | headgear - | last run 28 days | form P | MARKET 0.5% | 09:00 median 151.00 | Matchbook 210.00
    comment: One For Christy is lightly raced and unexposed, with her only recent run ending in a pulled up last time out 28 days ago, so she's yet to show her hand. She carries 147 lb and may have more to offer.
    DATA: model 2.7% | style Held up (led 8% of runs) | runs in data 1 | last 3: 25 Oct Wexford (IRE) Hurdle 18f Soft PU/8
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on; Pulled up in 1 of its last 1 jumps runs; Pace: steady gallop likely, hard to come from off the pace

## 12:49 Cork | race_id rac_32305217633 | Join Racing TV Now With A Free Trial Maiden Hurdle
Hurdle |  | 2m1f0y | going Soft | Turf | 18 runners | rating band - | age 4yo
DATA pace: Unclear - Running styles known for only 7 of 18 runners.
- Maestro Des Pins (hrs_64522829) | 4yo G | 161lb | OR - | draw 0 | jockey Danny Mullins | trainer W. P. Mullins (14d 7/31) | headgear - | last run 196 days | form 1-4 | MARKET 24.2% | 09:00 median 3.00 | Matchbook 3.10 | CHECK (skip line 2.85)
    DATA: model 17.5% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 10 May Cork Hurdle 17.3f Good 4/14
    DATA for: Trainer 23% wins (7/31), last 14 days; Last-run finishing speed +3.0% vs that field (finished strongly)
    DATA against: Returns from a 196-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Personal Space (hrs_17395867104) | 4yo F | 154lb | OR - | draw 0 | jockey Jordan Gainford | trainer Henry de Bromhead (14d 9/38) | headgear - | last run 266 days | form 1- | MARKET 23.8% | 09:00 median 2.88 | Matchbook 3.35
    DATA: model 4.0% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 24% wins (9/38), last 14 days
    DATA against: Returns from a 266-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Darby O'Gill (hrs_56559146) | 4yo G | 161lb | OR 121 | draw 0 | jockey Sam Ewing | trainer Gordon Elliott (14d 10/75) | headgear - | last run 190 days | form 25-4 | MARKET 20.8% | 09:00 median 3.00 | Matchbook 4.30
    DATA: model 8.8% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 190-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Bergomi (hrs_63202692) | 4yo G | 161lb | OR - | draw 0 | jockey Eoin Staples(5) | trainer Paul Nolan (14d 2/9) | headgear - | last run - days | form - | MARKET 4.8% | 09:00 median 15.00 | Matchbook 16.00
    DATA: model 4.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 22% wins (2/9), last 14 days
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Flooring Brandy (hrs_17395146391) | 4yo G | 161lb | OR - | draw 0 | jockey  | trainer Gavin Cromwell (14d 4/42) | headgear - | last run - days | form - | MARKET 4.3% | 09:00 median 12.00 | Matchbook 28.00
    DATA: model 4.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Rickety Kate (hrs_17390609341) | 4yo F | 154lb | OR - | draw 0 | jockey John Shinnick | trainer Joseph Patrick O'Brien (14d 5/29) | headgear - | last run - days | form - | MARKET 3.2% | 09:00 median 21.00 | Matchbook 29.00
    DATA: model 4.0% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Old Score (hrs_17395856674) | 4yo G | 161lb | OR - | draw 0 | jockey James Smith(3) | trainer Gordon Elliott (14d 10/75) | headgear - | last run - days | form - | MARKET 3.1% | 09:00 median 21.00 | Matchbook 29.00
    DATA: model 4.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Hard Ball (hrs_17395855631) | 4yo G | 161lb | OR - | draw 0 | jockey Kieren Buckley | trainer Gordon Elliott (14d 10/75) | headgear - | last run - days | form - | MARKET 2.5% | 09:00 median 26.00 | Matchbook 38.00
    DATA: model 4.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Dark Summit (hrs_51678900) | 4yo G | 161lb | OR - | draw 0 | jockey Michael Kenneally(3) | trainer Paul W Flynn (14d 0/6) | headgear - | last run 33 days | form - | MARKET 2.1% | 09:00 median 34.00 | Matchbook 44.00
    DATA: model 10.8% | style Prominent (led 23% of runs) | runs in data 11 | last 3: 27 Sep Curragh Flat 10f Heavy 16/18; 7 Oct Navan Flat 10.1f Yielding 3/16; 20 Oct Curragh (IRE) Flat 10f Yielding 2/24 fig 64
    DATA for: Good recent finishing positions
    DATA against: First run over hurdles in our data
- Loadstone (hrs_17390606212) | 4yo G | 161lb | OR - | draw 0 | jockey Cian Quirke | trainer Joseph Patrick O'Brien (14d 5/29) | headgear - | last run 15 days | form 7 | MARKET 1.7% | 09:00 median 41.00 | Matchbook 70.00
    DATA: model 9.6% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 7 Nov Gowran Park (IRE) Hurdle 16f Good To Yielding 7/12
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Michael Frances (hrs_17395865018) | 4yo G | 161lb | OR - | draw 0 | jockey  | trainer Martin Hassett (14d 0/2) | headgear - | last run - days | form - | MARKET 1.6% | 09:00 median 41.00 | Matchbook 65.00
    DATA: model 4.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Clean As A Whistle (hrs_17395853545) | 4yo G | 161lb | OR - | draw 0 | jockey  | trainer J Motherway (14d 0/2) | headgear - | last run 274 days | form P- | MARKET 1.5% | 09:00 median 41.00 | Matchbook 70.00
    DATA: model 4.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 274-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Poledriver (hrs_17395533344) | 4yo G | 161lb | OR - | draw 0 | jockey Mark McDonagh | trainer C Byrnes (14d 0/6) | headgear - | last run - days | form - | MARKET 1.3% | 09:00 median 51.00 | Matchbook 85.00
    DATA: model 4.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Puck Out (hrs_63776279) | 4yo G | 161lb | OR - | draw 0 | jockey Simon Torrens | trainer E Bolger (14d 0/0) | headgear - | last run - days | form - | MARKET 1.3% | 09:00 median 51.00 | Matchbook 90.00
    DATA: model 4.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Unfold (hrs_46515203) | 4yo G | 161lb | OR - | draw 0 | jockey Luke Carberry(7) | trainer A. McCann (14d 0/3) | headgear - | last run 41 days | form /- | MARKET 1.2% | 09:00 median 67.00 | Matchbook 90.00
    DATA: model 2.8% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 12 Oct Roscommon Flat 12.2f Soft 9/16
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Good Vibrations (hrs_62645303) | 4yo G | 161lb | OR - | draw 0 | jockey Eoin Sheehan(7) | trainer W J Burke (14d 0/2) | headgear - | last run 231 days | form 70- | MARKET 0.9% | 09:00 median 126.00 | Matchbook 90.00
    DATA: model 2.9% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 19 Mar Cork Hurdle 17.1f Yielding 7/14; 5 Apr Cork Hurdle 16.3f Yielding 14/15
    DATA against: Last-run finishing speed -5.0% vs that field (faded); Returns from a 231-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- A Poets Day Out (hrs_17394882512) | 4yo G | 161lb | OR - | draw 0 | jockey Phillip Enright | trainer Robert Tyner (14d 0/0) | headgear - | last run 18 days | form 0 | MARKET 0.8% | 09:00 median 151.00 | Matchbook 100.00
    DATA: model 2.2% | style Held up (led 8% of runs) | runs in data 1 | last 3: 4 Nov Wexford (IRE) Hurdle 16.5f Yielding 14/14
    DATA against: Last-run finishing speed -6.2% vs that field (faded); Lightly raced: 1 run in our data, so the model has little to go on
- Miss Stargazer (hrs_17394778212) | 4yo F | 154lb | OR - | draw 0 | jockey Rian Lane(7) | trainer E Bolger (14d 0/0) | headgear - | last run 21 days | form 0 | MARKET 0.8% | 09:00 median 151.00 | Matchbook 100.00
    DATA: model 1.8% | style Held up (led 8% of runs) | runs in data 1 | last 3: 1 Nov Cork (IRE) Hurdle 16f Good To Yielding 11/19
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on

## 1:19 Cork | race_id rac_32305219570 | Irish Stallion Farms EBF Maiden Hurdle
Hurdle |  | 2m1f0y | going Soft | Turf | 17 runners | rating band - | age 4yo+
DATA pace: Even - Two likely leaders (Jessbers Wish, Soul Asylum). A fair, even gallop is most likely.
- Look Me (hrs_51185946) | 5yo G | 166lb | OR - | draw 0 | jockey Danny Mullins | trainer W. P. Mullins (14d 7/31) | headgear - | last run 225 days | form 2/12- | MARKET 34.4% | 09:00 median 2.10 | Matchbook 2.44
    DATA: model 14.6% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 21 Feb Fairyhouse NH Flat 16.5f Heavy 1/4; 11 Apr Aintree NH Flat 16.9f Good To Soft 2/20
    DATA for: Trainer 23% wins (7/31), last 14 days; Last-run finishing speed +13.3% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Returns from a 225-day break; Lightly raced: 2 runs in our data, so the model has little to go on; First run over hurdles in our data
- Soul Asylum (hrs_58316006) | 5yo G | 166lb | OR - | draw 0 | jockey Sam Ewing | trainer Gordon Elliott (14d 10/75) | headgear - | last run 28 days | form 216-3 | MARKET 30.7% | 09:00 median 2.20 | Matchbook 2.88
    DATA: model 13.4% | style Leader (led 54% of runs) | runs in data 3 | last 3: 15 Feb Punchestown NH Flat 15.8f Heavy 1/4; 30 Apr Punchestown NH Flat 16.4f Yielding 6/10; 25 Oct Wexford (IRE) Hurdle 17f Soft 3/13 fig 110
    DATA for: Best recent form figure 110, 12 lb above field average; Good recent finishing positions
- Young Rebel (hrs_51434404) | 5yo G | 166lb | OR - | draw 0 | jockey Donagh Meyler | trainer Emmet Mullins (14d 2/7) | headgear h (1st time) | last run 47 days | form 1-52 | MARKET 10.7% | 09:00 median 6.50 | Matchbook 8.20
    DATA: model 16.6% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 1 Aug Galway Hurdle 16.8f Good To Yielding 5/19; 6 Oct Galway Hurdle 16.6f Yielding 2/20
    DATA for: Trainer 29% wins (2/7), last 14 days; First-time headgear
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Moonverrin (hrs_59186120) | 5yo M | 159lb | OR - | draw 0 | jockey Ricky Doyle | trainer Martin Hassett (14d 0/2) | headgear - | last run 256 days | form 2110- | MARKET 10.5% | 09:00 median 6.50 | Matchbook 8.60
    DATA: model 4.7% | style Held up (led 5% of runs) | runs in data 3 | last 3: 3 Jan Cork NH Flat 16f Yielding To Soft 1/9; 1 Feb Leopardstown NH Flat 16f Heavy 1/9; 11 Mar Cheltenham NH Flat 16.4f Good 11/21
    DATA for: Good recent finishing positions
    DATA against: Returns from a 256-day break; First run over hurdles in our data
- Jessbers Wish (hrs_50433054) | 5yo G | 166lb | OR - | draw 0 | jockey Tiernan Power Roche | trainer P. J. Rothwell (14d 0/24) | headgear - | last run 28 days | form 3/44-2 | MARKET 2.7% | 09:00 median 19.00 | Matchbook 48.00
    DATA: model 7.5% | style Leader (led 57% of runs) | runs in data 1 | last 3: 25 Oct Wexford (IRE) Hurdle 17f Soft 2/13 fig 104
    DATA for: Best recent form figure 104, 6 lb above field average
    DATA against: Trainer 0 wins from 24 runs, last 14 days; Lightly raced: 1 run in our data, so the model has little to go on
- Anunnaki (hrs_17392537848) | 6yo G | 166lb | OR - | draw 0 | jockey  | trainer P. J. Rothwell (14d 0/24) | headgear - | last run 27 days | form F/6 | MARKET 1.3% | 09:00 median 51.00 | Matchbook 80.00
    DATA: model 4.8% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 26 Oct Galway (IRE) Hurdle 16.5f Soft To Heavy 6/20
    DATA against: Trainer 0 wins from 24 runs, last 14 days; Lightly raced: 1 run in our data, so the model has little to go on
- Cross Of Moanrue (hrs_17392713072) | 6yo G | 166lb | OR - | draw 0 | jockey  | trainer P. J. Rothwell (14d 0/24) | headgear - | last run 189 days | form U338-2 | MARKET 1.2% | 09:00 median 67.00 | Matchbook 90.00
    DATA: model 4.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Trainer 0 wins from 24 runs, last 14 days; Returns from a 189-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Dusty Mills (hrs_17395218358) | 6yo G | 166lb | OR - | draw 0 | jockey Cian Quirke | trainer Bernard Martin Crowley (14d 0/3) | headgear - | last run 13 days | form S2-4 | MARKET 1.0% | 09:00 median 81.00 | Matchbook 120.00
    DATA: model 3.2% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 9 Nov Punchestown (IRE) Hurdle 16f Good To Yielding 4/10 fig 89
    DATA against: Best recent form figure 89, 9 lb below field average; Lightly raced: 1 run in our data, so the model has little to go on
- Kaspar Des Bordes (hrs_17394957608) | 6yo G | 166lb | OR - | draw 0 | jockey G B Noonan | trainer Eoin Christopher McCarthy (14d 0/4) | headgear - | last run 211 days | form 34F- | MARKET 1.0% | 09:00 median 81.00 | Matchbook 120.00
    DATA: model 4.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 211-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Daddy's Cupcake (hrs_17395530215) | 5yo M | 159lb | OR - | draw 0 | jockey Brian Barry(7) | trainer Ray Hackett (14d 0/5) | headgear - | last run - days | form - | MARKET 1.0% | 09:00 median 81.00 | Matchbook 120.00
    DATA: model 4.0% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Cracker's Diamond (hrs_17395529172) | 5yo M | 159lb | OR - | draw 0 | jockey  | trainer Ray Hackett (14d 0/5) | headgear - | last run - days | form - | MARKET 1.0% | 09:00 median 81.00 | Matchbook 120.00
    DATA: model 4.0% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Cascando (hrs_51185841) | 5yo G | 166lb | OR - | draw 0 | jockey Phillip Enright | trainer Robert Tyner (14d 0/0) | headgear - | last run 27 days | form 2P14-0 | MARKET 0.8% | 09:00 median 151.00 | Matchbook 120.00
    DATA: model 3.3% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 19 Apr Tramore Hurdle 16f Yielding 4/15; 26 Oct Galway (IRE) Hurdle 16.5f Soft To Heavy 11/20
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Moonquake (hrs_17395532301) | 5yo G | 166lb | OR - | draw 0 | jockey Niall Moore(5) | trainer W J Martin (14d 0/3) | headgear - | last run 21 days | form 4P/9-P | MARKET 0.8% | 09:00 median 151.00 | Matchbook 120.00
    DATA: model 4.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- River Ore (hrs_64556156) | 5yo G | 166lb | OR - | draw 0 | jockey Jordan Gainford | trainer John Joseph Hanlon (14d 0/9) | headgear - | last run 19 days | form 46808 | MARKET 0.8% | 09:00 median 151.00 | Matchbook 120.00
    DATA: model 1.1% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 13 Jun Hexham NH Flat 16.2f Good 8/8; 14 Oct Punchestown (IRE) Hurdle 16.5f Good 10/15; 3 Nov Fairyhouse (IRE) Hurdle 16f Good To Yielding 8/15 fig 89
    DATA against: Best recent form figure 89, 9 lb below field average; Trainer 0 wins from 9 runs, last 14 days; Poor recent finishing positions
- Tommie K (hrs_17393984489) | 5yo G | 166lb | OR - | draw 0 | jockey Simon Torrens | trainer Robert Tyner (14d 0/0) | headgear - | last run 259 days | form FP- | MARKET 0.8% | 09:00 median 151.00 | Matchbook 120.00
    DATA: model 4.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 259-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Berkshire Echo (hrs_52451651) | 6yo G | 166lb | OR - | draw 0 | jockey Liam McKenna(3) | trainer Martin Hassett (14d 0/2) | headgear - | last run 556 days | form 0/4- | MARKET 0.7% | 09:00 median 201.00 | Matchbook 120.00
    DATA: model 4.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 556-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Nothingtodowithyou (hrs_35054740) | 7yo G | 166lb | OR - | draw 0 | jockey Luke Burke Ott(7) | trainer Alexander Ott (14d 0/1) | headgear - | last run 17 days | form 828U/9 | MARKET 0.6% | 09:00 median 201.00 | Matchbook 120.00
    DATA: model 0.9% | style Held up (led 8% of runs) | runs in data 1 | last 3: 5 Nov Clonmel (IRE) Hurdle 19.5f Good 9/12
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on

## 1:49 Cork | race_id rac_32305221507 | Irish Stallion Farms EBF Mares Beginners Steeplechase
Chase |  | 2m5f50y | going Yielding To Soft | Turf | 13 runners | rating band - | age 4yo+
DATA pace: Lone leader - Bambino Fever is the only habitual front-runner and may be allowed an easy lead.
- Place De La Nation (hrs_45445099) | 5yo M | 161lb | OR - | draw 0 | jockey Danny Mullins | trainer W. P. Mullins (14d 7/31) | headgear - | last run 204 days | form 12321- | MARKET 32.0% | 09:00 median 2.63 | Matchbook 2.74
    comment: Place De La Nation arrives in cracking form, a winner last time out and again five starts back, with a second, a third and another second in between.
    DATA: model 8.9% | style Prominent (led 23% of runs) | runs in data 5 | last 3: 12 Mar Cheltenham Hurdle 16.8f Good 3/22; 5 Apr Fairyhouse Hurdle 20f Yielding To Soft 2/11; 2 May Punchestown Hurdle 20.5f Yielding 1/4
    DATA for: Trainer 23% wins (7/31), last 14 days; Last-run finishing speed +4.0% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Returns from a 204-day break; First run over fences in our data
- Bambino Fever (hrs_41052795) | 6yo M | 161lb | OR - | draw 0 | jockey Miss J Townend | trainer W. P. Mullins (14d 7/31) | headgear - | last run 255 days | form 1/210- | MARKET 23.2% | 09:00 median 3.25 | Matchbook 4.10
    comment: The main risk is a 255-day absence, plus 161 lb and an unplaced run last time out.
    DATA: model 17.4% | style Leader (led 72% of runs) | runs in data 2 | last 3: 14 Jan Fairyhouse Hurdle 18.2f Yielding 1/12; 12 Mar Cheltenham Hurdle 16.8f Good 16/22
    DATA for: Trainer 23% wins (7/31), last 14 days; Pace: may get an uncontested lead
    DATA against: Last-run finishing speed -2.3% vs that field (faded); Returns from a 255-day break; Lightly raced: 2 runs in our data, so the model has little to go on; First run over fences in our data
- Echoing Silence (hrs_39959584) | 6yo M | 161lb | OR - | draw 0 | jockey Jordan Gainford | trainer Henry de Bromhead (14d 9/38) | headgear t (1st time) | last run 35 days | form 1107-3 | MARKET 12.7% | 09:00 median 6.00 | Matchbook 7.60
    comment: Echoing Silence returned with a third last time out and bagged back-to-back wins four and five starts back, while she has run over today's trip and going before. The risk is a 35-day break and a 161 lb burden, with a seventh two starts back showing she can falter.
    DATA: model 6.4% | style Midfield (led 29% of runs) | runs in data 3 | last 3: 12 Mar Cheltenham Hurdle 16.8f Good 10/22; 1 May Punchestown Hurdle 20.6f Yielding 7/8; 18 Oct Limerick (IRE) Chase 19.5f Good To Yielding 3/4 fig 117
    DATA for: Best recent form figure 117, 15 lb above field average; Trainer 24% wins (9/38), last 14 days; First-time headgear
- Carrigmoornaspruce (hrs_45568383) | 6yo M | 161lb | OR - | draw 0 | jockey Sean Cleary-Farrell(7) | trainer W. P. Mullins (14d 7/31) | headgear - | last run 255 days | form /1220- | MARKET 9.2% | 09:00 median 9.00 | Matchbook 9.80
    comment: Carrigmoornaspruce has a solid recent profile, a winner four starts back followed by a second, two starts back, and another second three starts back, and she has run on today's going.
    DATA: model 7.2% | style Unknown | runs in data 1 | last 3: 12 Mar Cheltenham Hurdle 16.8f Good 12/22
    DATA for: Trainer 23% wins (7/31), last 14 days; Last-run finishing speed +2.4% vs that field (finished strongly)
    DATA against: Returns from a 255-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Sainte Lucie (hrs_40919935) | 5yo M | 161lb | OR - | draw 0 | jockey Charlie O'Dwyer(3) | trainer W. P. Mullins (14d 7/31) | headgear - | last run 197 days | form 0071-1 | MARKET 9.1% | 09:00 median 8.50 | Matchbook 10.50
    comment: The main risk is a 197-day absence, so fitness is the question, especially under 161 lb.
    DATA: model 17.1% | style Midfield (led 3% of runs) | runs in data 4 | last 3: 13 Mar Cheltenham Hurdle 20.3f Good To Soft 7/24; 5 Apr Cork Hurdle 19f Yielding 1/19; 9 May Killarney Hurdle 17f Good To Yielding 1/9
    DATA for: Trainer 23% wins (7/31), last 14 days; Last-run finishing speed +5.3% vs that field (finished strongly); Good recent finishing positions
    DATA against: Returns from a 197-day break; First run over fences in our data
- Mongibello (hrs_34166552) | 8yo M | 161lb | OR 128 | draw 0 | jockey Sam Ewing | trainer S. R. B. Crawford (14d 1/8) | headgear - | last run 76 days | form 2521/2 | MARKET 5.0% | 09:00 median 13.00 | Matchbook 23.00
    comment: Mongibello has been in the frame in four of her last five, including a second last time out and a win two starts back, and she has run over today's trip and going.
    DATA: model 9.7% | style Held up (led 8% of runs) | runs in data 1 | last 3: 7 Sep Galway Chase 18.2f Yielding 2/6
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Blue Velvet (hrs_41052676) | 6yo M | 161lb | OR - | draw 0 | jockey Ricky Doyle | trainer W. P. Mullins (14d 7/31) | headgear - | last run 231 days | form /210P- | MARKET 2.5% | 09:00 median 29.00 | Matchbook 48.00
    comment: Blue Velvet won three starts back and was second four runs ago, but she was pulled up last time out and has been off for 231 days, so fitness is a worry.
    DATA: model 3.7% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 26 Jan Punchestown Hurdle 19f Heavy 1/16; 12 Mar Cheltenham Hurdle 16.8f Good 11/22; 5 Apr Fairyhouse Hurdle 20f Yielding To Soft PU/11
    DATA for: Trainer 23% wins (7/31), last 14 days
    DATA against: Returns from a 231-day break; Pulled up in 1 of its last 3 jumps runs; First run over fences in our data
- Kelya (hrs_46697742) | 6yo M | 161lb | OR - | draw 0 | jockey Donagh Meyler | trainer Emmet Mullins (14d 2/7) | headgear - | last run 28 days | form 137/53 | MARKET 1.7% | 09:00 median 34.00 | Matchbook 85.00
    comment: Kelya is hard to fancy, having won only once in her last five starts, five runs back, with a seventh and fifth since, though a third last time out and a third four starts back show she can still hit the frame.
    DATA: model 4.7% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 8 Aug Wexford Chase 19.1f Good 5/6; 25 Oct Wexford (IRE) Chase 19.5f Soft 3/13 fig 98
    DATA for: Trainer 29% wins (2/7), last 14 days
    DATA against: Best recent form figure 98, 4 lb below field average; Lightly raced: 2 runs in our data, so the model has little to go on
- Changeyourstars (hrs_47345235) | 6yo M | 161lb | OR - | draw 0 | jockey Phillip Enright | trainer Patrick King (14d 0/0) | headgear ht | last run 255 days | form 92126- | MARKET 1.4% | 09:00 median 41.00 | Matchbook 120.00
    comment: Changeyourstars returns after 255 days off, having finished sixth last time out, which makes her hard to fancy, and she carries a hefty 161 lb. In her favour, she won three starts back, was a second two starts back, and has run over today's trip and going.
    DATA: model 4.6% | style Held up (led 5% of runs) | runs in data 2 | last 3: 14 Feb Gowran Park Hurdle 23f Heavy 2/5; 12 Mar Limerick Hurdle 22.8f Heavy 6/7
    DATA against: Last-run finishing speed -4.8% vs that field (faded); Returns from a 255-day break; Lightly raced: 2 runs in our data, so the model has little to go on; First run over fences in our data
- Carry On Heidi (hrs_40096063) | 6yo M | 161lb | OR - | draw 0 | jockey Michael Kenneally(3) | trainer Jeremiah Patrick Baragry (14d 0/0) | headgear - | last run 98 days | form 4333-5 | MARKET 1.2% | 09:00 median 51.00 | Matchbook 160.00
    comment: Carry On Heidi has been consistent, finishing third in three of her last five, though she was only fifth last time out and is yet to win in that spell.
    DATA: model 3.9% | style Prominent (led 4% of runs) | runs in data 3 | last 3: 3 Feb Fairyhouse Hurdle 18.4f Soft To Heavy 3/6; 12 Mar Limerick Hurdle 22.8f Heavy 3/7; 16 Aug Tramore Chase 22f Good To Yielding 5/7
    DATA for: Good recent finishing positions
    DATA against: Returns from a 98-day break; Race comments mention jumping mistakes in 2 of its last 3 runs
- My Forever Annie (hrs_17393936511) | 7yo M | 161lb | OR - | draw 0 | jockey James Smith(3) | trainer Gordon Elliott (14d 10/75) | headgear - | last run 36 days | form 1/6 | MARKET 0.8% | 09:00 median 67.00 | Matchbook 190.00
    comment: Unexposed mare with just two recent runs, a win two starts back followed by a sixth last time out, and she returns after 36 days off; carrying 161 lb, she looks open to improvement.
    DATA: model 2.1% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 17 Oct Limerick (IRE) Hurdle 23.5f Good To Yielding 6/6
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Miss Mini Bee (hrs_38532732) | 7yo M | 161lb | OR - | draw 0 | jockey Alex Harvey | trainer Patrick T Foley (14d 0/4) | headgear ht | last run 28 days | form 753P-3 | MARKET 0.7% | 09:00 median 81.00 | Matchbook 240.00
    comment: Miss Mini Bee is winless in her last five and hard to fancy, with a pulled up two starts back and nothing better than a third in that spell, though she was third last time out and has run over today's trip and on this going.
    DATA: model 7.0% | style Held up (led 3% of runs) | runs in data 5 | last 3: 7 Mar Gowran Park Hurdle 20f Heavy 3/13; 10 Apr Wexford Hurdle 20f Good To Yielding PU/14; 25 Oct Wexford (IRE) Hurdle 20.5f Soft 3/7 fig 91
    DATA against: Best recent form figure 91, 11 lb below field average; Race comments mention jumping mistakes in 3 of its last 5 runs; Pulled up in 1 of its last 5 jumps runs; First run over fences in our data
- Miss Georgina (hrs_52055955) | 6yo M | 161lb | OR - | draw 0 | jockey Tiernan Power Roche | trainer Andrew Lee (14d 0/2) | headgear - | last run 196 days | form 5443-7 | MARKET 0.6% | 09:00 median 101.00 | Matchbook 300.00
    comment: Miss Georgina is winless in her last five, beaten into seventh last time out after a third two starts back, and she returns from 196 days off carrying 161 lb.
    DATA: model 7.2% | style Prominent (led 23% of runs) | runs in data 4 | last 3: 3 Mar Leopardstown Hurdle 20.8f Soft 4/8; 26 Mar Clonmel Hurdle 18.9f Soft 3/12; 10 May Cork Hurdle 19.2f Good 7/15
    DATA against: Returns from a 196-day break; First run over fences in our data

## 2:19 Cork | race_id rac_32305223444 | Kevin McManus Bookmaker Handicap Steeplechase
Chase |  | 2m5f50y | going Yielding To Soft | Turf | 18 runners | rating band - | age 4yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Karl Des Tourelles (hrs_39698883) | 6yo G | 166lb | OR 132 | draw 0 | jockey Niall Moore(5) | trainer Philip Fenton (14d 1/2) | headgear - | last run 27 days | form 466-21 | MARKET 15.2% | 09:00 median 4.00 | Matchbook 6.20 | CHECK (skip line 3.80)
    comment: Karl Des Tourelles arrives in fine fettle, a winner last time out and second two starts back, and a gelding who has run over today's trip and on this going before. He carries 166 lb, which is a fair test, but a 27-day break looks well judged.
    DATA: model 12.8% | style Midfield (led 4% of runs) | runs in data 5 | last 3: 30 Apr Punchestown Hurdle 23.5f Yielding 6/24; 6 Oct Galway Chase 18.2f Yielding To Soft 2/8; 26 Oct Galway (IRE) Chase 18f Heavy 1/7 fig 126
    DATA for: Best recent form figure 126, 7 lb above field average; Official rating 132, 11 lb above field average; Good recent finishing positions
    DATA against: Recent figures 6 lb below its current mark (looks high in the weights); Carries 11 lb more than average
- Rockonliam (hrs_39827263) | 6yo G | 166lb | OR 132 | draw 0 | jockey Patrick M O'Brien(5) | trainer Henry de Bromhead (14d 9/38) | headgear t | last run 29 days | form 4-1112 | MARKET 10.6% | 09:00 median 5.00 | Matchbook 11.00
    comment: Rockonliam arrives in cracking form, second last time out and a winner in three of his last five starts, and he has run over today's trip and going before.
    DATA: model 9.9% | style Midfield (led 4% of runs) | runs in data 4 | last 3: 30 Jun Wexford Chase 19.5f Good 1/14; 8 Aug Wexford Chase 25f Good 1/7; 24 Oct Cheltenham Chase 20f Good 2/9 fig 128
    DATA for: Best recent form figure 128, 9 lb above field average; Official rating 132, 11 lb above field average; Trainer 24% wins (9/38), last 14 days; Has won at this trip or further; Good recent finishing positions
    DATA against: Carries 11 lb more than average
- Kobalt St Georges (hrs_39698890) | 6yo G | 143lb | OR 109 | draw 0 | jockey  | trainer Robert Tyner (14d 0/0) | headgear - | last run 28 days | form 1145-2 | MARKET 9.7% | 09:00 median 7.50 | Matchbook 8.20
    comment: Beaten into second last time out, and a winner four and five starts back, Kobalt St Georges has run over today's trip and going and arrives after 28 days off.
    DATA: model 6.7% | style Prominent (led 3% of runs) | runs in data 4 | last 3: 22 Feb Naas Chase 20f Heavy 4/12; 19 Mar Cork Hurdle 20f Yielding 5/18; 25 Oct Wexford (IRE) Chase 19.5f Soft 2/10 fig 110
    DATA for: Carries 12 lb less than average
    DATA against: Best recent form figure 110, 9 lb below field average; Official rating 109, 12 lb below field average
- On Your Way (hrs_39334239) | 8yo G | 160lb | OR 126 | draw 0 | jockey Philip Donovan | trainer C Byrnes (14d 0/6) | headgear - | last run 27 days | form 1/12-3 | MARKET 7.4% | 09:00 median 8.50 | Matchbook 12.00
    comment: He has run over today's trip and going before, and 27 days since his last run is no concern.
    DATA: model 2.7% | style Held up (led 8% of runs) | runs in data 1 | last 3: 26 Oct Galway (IRE) Chase 18f Heavy 3/7 fig 114
    DATA against: Best recent form figure 114, 5 lb below field average; Recent figures 12 lb below its current mark (looks high in the weights); Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Watch The Weather (hrs_27428527) | 10yo G | 158lb | OR 124 | draw 0 | jockey Michael Kenneally(3) | trainer R P Cody (14d 0/2) | headgear t | last run 28 days | form 533323 | MARKET 7.4% | 09:00 median 8.50 | Matchbook 12.50
    comment: Consistently in the frame, Watch The Weather was third last time out, with a second two starts back and thirds three, four and five runs ago, and he has run over today's trip and going. Yet to win in his last six, he carries 158 lb, which is the main risk.
    DATA: model 8.2% | style Held up (led 3% of runs) | runs in data 9 | last 3: 4 Sep Kilbeggan Chase 20.4f Good To Yielding 3/13; 26 Sep Listowel Hurdle 20f Good 2/14; 25 Oct Wexford (IRE) Chase 19.5f Soft 3/10 fig 126
    DATA for: Best recent form figure 126, 7 lb above field average; Good recent finishing positions
    DATA against: Race comments mention jumping mistakes in 2 of its last 5 runs; Pace: steady gallop likely, hard to come from off the pace
- Kings Jet (hrs_46013772) | 6yo G | 150lb | OR 116 | draw 0 | jockey Ricky Doyle | trainer C. W. J. Farrell (14d 1/3) | headgear p | last run 31 days | form U023F1 | MARKET 6.8% | 09:00 median 10.00 | Matchbook 12.50
    comment: Kings Jet won last time out after a fall two starts back, and he has run over today's trip, but a mixed record with a fell and an unseated in his last six, plus 150 lb off a mark of 116, makes him hard to fancy.
    DATA: model 6.9% | style Prominent (led 3% of runs) | runs in data 7 | last 3: 20 Aug Killarney Chase 20.8f Good 3/11; 25 Sep Listowel Chase 19f Good To Yielding F/14; 22 Oct Clonmel (IRE) Chase 21f Good 1/10 fig 113
    DATA for: Last-run finishing speed +5.2% vs that field (finished strongly); Has won at this trip or further; Carries 5 lb less than average
    DATA against: Best recent form figure 113, 6 lb below field average; Official rating 116, 5 lb below field average; Race comments mention jumping mistakes in 3 of its last 5 runs; Fell or unseated in 1 of its last 5 jumps runs
- El Champo (hrs_30208458) | 8yo G | 153lb | OR 119 | draw 0 | jockey Conor Smithers(7) | trainer P. J. Rothwell (14d 0/24) | headgear p | last run 35 days | form P9-462 | MARKET 5.7% | 09:00 median 13.00 | Matchbook 13.50
    comment: El Champo is winless in his last five and was pulled up five starts back, so he is hard to fancy, especially with his yard 0/24 lately and 153 lb to carry. On the plus side, he was second last time out and has run over today's trip and going.
    DATA: model 4.0% | style Prominent (led 23% of runs) | runs in data 6 | last 3: 7 Jun Punchestown Chase 20.2f Good 4/12; 26 Sep Listowel Chase 22f Good 6/13; 18 Oct Limerick (IRE) Chase 19.5f Good To Yielding 2/8 fig 119
    DATA against: Trainer 0 wins from 24 runs, last 14 days; Pulled up in 1 of its last 5 jumps runs
- Mystical Goddess (hrs_38666432) | 7yo M | 156lb | OR 122 | draw 0 | jockey Jordan Gainford | trainer Henry de Bromhead (14d 9/38) | headgear tp | last run 232 days | form 33P3P- | MARKET 4.5% | 09:00 median 15.00 | Matchbook 19.50
    DATA: model 4.5% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 22 Mar Limerick Chase 19.5f Soft To Heavy 3/8; 4 Apr Fairyhouse Chase 21.2f Yielding To Soft PU/10
    DATA for: Trainer 24% wins (9/38), last 14 days
    DATA against: Returns from a 232-day break; Lightly raced: 2 runs in our data, so the model has little to go on; Pulled up in 1 of its last 2 jumps runs
- I Am Lorenzo (hrs_38433290) | 7yo G | 160lb | OR 126 | draw 0 | jockey Eoin Staples(5) | trainer Paul Nolan (14d 2/9) | headgear - | last run 28 days | form 1339-8 | MARKET 4.3% | 09:00 median 17.00 | Matchbook 18.00
    comment: I Am Lorenzo has tailed off with an eighth last time out and a ninth before that, though a win five starts back and two thirds show he has ability, and he has run over today's trip and going. Carrying 160 lb off an official mark of 126 looks a stiff ask.
    DATA: model 3.6% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 17 Mar Down Royal Chase 20.4f Good To Yielding 3/7; 1 May Punchestown Chase 20.2f Yielding 9/22; 25 Oct Wexford (IRE) Chase 19.5f Soft 8/10 fig 114
    DATA for: Trainer 22% wins (2/9), last 14 days
    DATA against: Best recent form figure 114, 5 lb below field average; Recent figures 12 lb below its current mark (looks high in the weights); Race comments mention jumping mistakes in 2 of its last 5 runs
- A Wave Of The Sea (hrs_18562999) | 10yo G | 158lb | OR 124 | draw 0 | jockey Charlie O'Dwyer(3) | trainer J P Broderick (14d 0/0) | headgear - | last run 35 days | form 0-5714 | MARKET 4.1% | 09:00 median 15.00 | Matchbook 23.00
    comment: A Wave Of The Sea showed he can win when successful two starts back and was fourth last time out, and he has run over today's trip and going before.
    DATA: model 5.5% | style Midfield (led 3% of runs) | runs in data 8 | last 3: 21 Aug Kilbeggan Chase 25.8f Good To Yielding 1/8; 4 Oct Curragh Flat 12f Yielding 9/12; 18 Oct Limerick (IRE) Chase 24f Good To Yielding 4/11 fig 121
    DATA for: Has won at this trip or further
- Harvard Guy (hrs_33067356) | 8yo G | 159lb | OR 125 | draw 0 | jockey Simon Torrens | trainer Eddie & Patrick Harty (14d 0/2) | headgear - | last run 231 days | form 68755- | MARKET 4.0% | 09:00 median 19.00 | Matchbook 19.00
    comment: The risk is a 231-day absence and 159 lb on his back.
    DATA: model 4.1% | style Held up (led 3% of runs) | runs in data 4 | last 3: 22 Feb Naas Chase 20f Heavy 7/12; 8 Mar Naas Chase 24.8f Soft To Heavy 5/15; 5 Apr Fairyhouse Chase 16.6f Yielding To Soft 5/12
    DATA against: Returns from a 231-day break; Race comments mention jumping mistakes in 2 of its last 4 runs; Pace: steady gallop likely, hard to come from off the pace
- Al Kalila (hrs_35796740) | 7yo G | 156lb | OR 122 | draw 0 | jockey Sam Ewing | trainer S. R. B. Crawford (14d 1/8) | headgear - | last run 205 days | form 23310- | MARKET 3.6% | 09:00 median 19.00 | Matchbook 23.00
    comment: Al Kalila won two starts back and was placed in three of the four runs before that, but he was unplaced last time and returns after 205 days off, carrying 156 lb.
    DATA: model 4.3% | style Held up (led 5% of runs) | runs in data 3 | last 3: 20 Jan Down Royal Chase 24f Yielding To Soft 3/8; 28 Feb Kelso Chase 21.6f Good To Soft 1/4; 1 May Punchestown Chase 20.2f Yielding 12/22
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Last-run finishing speed -2.8% vs that field (faded); Returns from a 205-day break; Pace: steady gallop likely, hard to come from off the pace
- Rusheen (hrs_35218708) | 8yo G | 144lb | OR 110 | draw 0 | jockey  | trainer Terence O'Brien (14d 0/5) | headgear - | last run 195 days | form 1UP3-7 | MARKET 3.5% | 09:00 median 19.00 | Matchbook 25.00
    comment: Rusheen is hard to fancy after a seventh last time out and a 195-day absence, with a pulled up and an unseated in his last five starts. On the plus side, he won five starts back, was third two starts back, and has run over today's trip and going.
    DATA: model 5.0% | style Prominent (led 3% of runs) | runs in data 5 | last 3: 5 Mar Thurles Chase 21.5f Soft PU/15; 2 Apr Clonmel Chase 23.2f Soft 3/14; 11 May Killarney Chase 20.5f Good To Yielding 7/14
    DATA for: Carries 11 lb less than average
    DATA against: Official rating 110, 11 lb below field average; Last-run finishing speed -3.0% vs that field (faded); Returns from a 195-day break; Race comments mention jumping mistakes in 2 of its last 5 runs; Fell or unseated in 1 of its last 5 jumps runs; Pulled up in 1 of its last 5 jumps runs
- Jupiter Du Gite (hrs_33205151) | 7yo G | 147lb | OR 113 | draw 0 | jockey Donagh Meyler | trainer T Hogan (14d 0/0) | headgear ht | last run 28 days | form 6-2298 | MARKET 3.2% | 09:00 median 23.00 | Matchbook 25.00
    comment: Jupiter Du Gite has run over today's trip and going and was second twice in his last five, but he's been well beaten in his last two outings, a ninth then an eighth.
    DATA: model 5.0% | style Held up (led 3% of runs) | runs in data 8 | last 3: 22 Aug Killarney Hurdle 22.4f Good 2/14; 11 Sep Ballinrobe Hurdle 21.9f Good To Yielding 9/14; 25 Oct Galway (IRE) Chase 22.5f Soft To Heavy 8/9
    DATA for: Carries 8 lb less than average
    DATA against: Official rating 113, 8 lb below field average; Race comments mention jumping mistakes in 2 of its last 5 runs; Pace: steady gallop likely, hard to come from off the pace
- Meet And Greet (hrs_22138151) | 10yo G | 159lb | OR 125 | draw 0 | jockey Phillip Enright | trainer Oliver McKiernan (14d 0/6) | headgear tp | last run 35 days | form 24-F58 | MARKET 3.1% | 09:00 median 23.00 | Matchbook 28.00
    comment: The risk is his latest form, an eighth last time out, and a fifth before that, under 159 lb.
    DATA: model 4.8% | style Held up (led 3% of runs) | runs in data 6 | last 3: 23 Sep Listowel Chase 23.8f Good F/18; 26 Sep Listowel Chase 22f Good 5/13; 18 Oct Limerick (IRE) Chase 24f Good To Yielding 8/11 fig 116
    DATA against: Recent figures 9 lb below its current mark (looks high in the weights); Fell or unseated in 1 of its last 5 jumps runs; Pace: steady gallop likely, hard to come from off the pace
- Invictus Machin (hrs_32683322) | 8yo G | 160lb | OR 126 | draw 0 | jockey Kieren Buckley | trainer Gavin Cromwell (14d 4/42) | headgear h | last run 135 days | form 224-PP | MARKET 2.9% | 09:00 median 26.00 | Matchbook 30.00
    comment: Pulled up in his last two starts and now back after 135 days, Invictus Machin is yet to win in recent form, though a fourth three starts back and two seconds before that show his level, and he has run over today's trip and going. Carries 160 lb.
    DATA: model 5.6% | style Held up (led 3% of runs) | runs in data 4 | last 3: 2 May Punchestown Chase 24.5f Yielding 4/21; 25 May Ballinrobe Chase 23.4f Good PU/16; 10 Jul Kilbeggan Chase 25.4f Good PU/14
    DATA against: Returns from a 135-day break; Pulled up in 2 of its last 4 jumps runs; Pace: steady gallop likely, hard to come from off the pace
- Happy Dreams (hrs_27251630) | 9yo G | 147lb | OR 113 | draw 0 | jockey Cian Quirke | trainer Michael J McDonagh (14d 0/2) | headgear - | last run 259 days | form 21660- | MARKET 2.3% | 09:00 median 34.00 | Matchbook 38.00
    comment: Happy Dreams has been well beaten in his last two starts, unplaced and a sixth, and returns after 259 days off, which is hard to overlook under 147 lb. He has run over this trip and on this going, and he won four starts back, but that is thin support.
    DATA: model 2.9% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 11 Jan Punchestown Hurdle 20.8f Soft To Heavy 6/15; 14 Feb Gowran Park Chase 19.3f Heavy 6/9; 8 Mar Naas Hurdle 19f Soft To Heavy 14/17
    DATA for: Carries 8 lb less than average
    DATA against: Official rating 113, 8 lb below field average; Last-run finishing speed -4.8% vs that field (faded); Poor recent finishing positions; Returns from a 259-day break
- Hermino AA (hrs_32952654) | 9yo G | 155lb | OR 121 | draw 0 | jockey Gearoid Brouder(5) | trainer E McNamara (14d 0/12) | headgear p | last run 35 days | form -61086 | MARKET 1.6% | 09:00 median 41.00 | Matchbook 65.00
    comment: Hermino AA won four starts back but has managed only a sixth last time out and an eighth before that, and he returns after 35 days carrying 155 lb.
    DATA: model 3.7% | style Midfield (led 3% of runs) | runs in data 6 | last 3: 8 Jun Roscommon Chase 25.1f Yielding To Soft 1/15; 31 Jul Galway Chase 22.5f Yielding To Soft 11/20; 22 Aug Killarney Chase 20.8f Good 8/10
    DATA for: Has won at this trip or further
    DATA against: Trainer 0 wins from 12 runs, last 14 days; Last-run finishing speed -4.9% vs that field (faded)

## 2:49 Cork | race_id rac_32305225381 | William Hill Challenge Series Irish EBF Beginners Steeplechase
Chase |  | 2m5f50y | going Yielding To Soft | Turf | 19 runners | rating band - | age 4yo+
DATA pace: Even - Two likely leaders (Polepatrick, Affinity Rock). A fair, even gallop is most likely.
- Some Song (hrs_52055689) | 6yo G | 166lb | OR 124 | draw 0 | jockey Jordan Gainford | trainer Henry de Bromhead (14d 9/38) | headgear - | last run 19 days | form P6-443 | MARKET 14.7% | 09:00 median 4.33 | Matchbook 5.80 | CHECK (skip line 4.11)
    comment: Some Song arrives in sound recent form, third last time out after a fourth two starts back and another fourth three starts back, and he returns fresh enough after 19 days. He has run over today's trip, though he is yet to win in his last five and carries 166 lb.
    DATA: model 6.8% | style Midfield (led 3% of runs) | runs in data 4 | last 3: 20 Sep Listowel Chase 17.7f Good 4/5; 6 Oct Galway Chase 18.2f Yielding To Soft 4/8; 3 Nov Fairyhouse (IRE) Chase 24.5f Good To Yielding 3/7 fig 113
    DATA for: Official rating 124, 6 lb above field average; Trainer 24% wins (9/38), last 14 days
    DATA against: Race comments mention jumping mistakes in 2 of its last 4 runs
- Rosie's Wings (hrs_52741899) | 6yo G | 166lb | OR - | draw 0 | jockey Donagh Meyler | trainer Ross O'Sullivan (14d 1/18) | headgear t | last run 19 days | form 313332 | MARKET 12.2% | 09:00 median 6.00 | Matchbook 6.40
    comment: He has run over today's trip and is fresh enough after 19 days.
    DATA: model 3.9% | style Held up (led 3% of runs) | runs in data 6 | last 3: 21 Aug Kilbeggan Hurdle 18.9f Good To Yielding 3/9; 26 Sep Listowel Hurdle 20f Good 3/6; 3 Nov Fairyhouse (IRE) Chase 24.5f Good To Yielding 2/7 fig 113
    DATA for: Last-run finishing speed +2.6% vs that field (finished strongly); Good recent finishing positions
    DATA against: Race comments mention jumping mistakes in 2 of its last 5 runs
- Affinity Rock (hrs_46697119) | 6yo M | 159lb | OR 115 | draw 0 | jockey Carl Millar(5) | trainer Cian Collins (14d 1/7) | headgear t | last run 53 days | form -22342 | MARKET 8.2% | 09:00 median 9.50 | Matchbook 9.20
    comment: Affinity Rock has been consistent, finishing second last time out and placing in four of her five recent runs, yet she is winless in that spell.
    DATA: model 11.0% | style Leader (led 79% of runs) | runs in data 5 | last 3: 20 Aug Killarney Chase 23.5f Good 3/6; 11 Sep Ballinrobe Chase 23.3f Good To Yielding 4/9; 30 Sep Sligo Chase 25.8f Good 2/8
    DATA for: Last-run finishing speed +4.1% vs that field (finished strongly); Good recent finishing positions
- Speculateur (hrs_50906156) | 5yo G | 166lb | OR - | draw 0 | jockey Sam Ewing | trainer Gordon Elliott (14d 10/75) | headgear t | last run 19 days | form 333-14 | MARKET 7.6% | 09:00 median 9.00 | Matchbook 11.00
    comment: Speculateur has been in the frame consistently, a fourth last time out following a win two starts back, and he has run over today's trip and going before after a fresh 19-day break.
    DATA: model 7.4% | style Prominent (led 4% of runs) | runs in data 7 | last 3: 14 Apr Clonmel Hurdle 19.8f Yielding 3/17; 12 May Sligo Hurdle 20f Good 1/9; 3 Nov Fairyhouse (IRE) Chase 24.5f Good To Yielding 4/7 fig 108
    DATA for: Good recent finishing positions
- Gin Tonic (hrs_51831612) | 5yo G | 166lb | OR - | draw 0 | jockey Philip Donovan | trainer Paul Nolan (14d 2/9) | headgear b (1st time) | last run 113 days | form 12PP-P | MARKET 7.6% | 09:00 median 8.50 | Matchbook 11.00
    comment: Gin Tonic has pulled up in each of his last three starts after a second four starts back and a win five starts back, and he returns from 113 days off.
    DATA: model 2.1% | style Prominent (led 4% of runs) | runs in data 3 | last 3: 5 Feb Thurles Hurdle 20.4f Soft PU/6; 4 Apr Fairyhouse Hurdle 23.8f Yielding To Soft PU/20; 1 Aug Galway Hurdle 22.5f Good To Yielding PU/20
    DATA for: Trainer 22% wins (2/9), last 14 days; First-time headgear
    DATA against: Poor recent finishing positions; Returns from a 113-day break; Pulled up in 3 of its last 3 jumps runs; First run over fences in our data
- Kaiser De Chanay (hrs_48644540) | 6yo G | 166lb | OR - | draw 0 | jockey Ricky Doyle | trainer Martin Brassil (14d 1/4) | headgear t | last run 234 days | form /6571- | MARKET 6.7% | 09:00 median 10.00 | Matchbook 12.50
    comment: Kaiser De Chanay won last time out, but that came after a seventh, a fifth and a sixth, and he returns from 234 days off carrying 166 lb.
    DATA: model 6.1% | style Prominent (led 29% of runs) | runs in data 3 | last 3: 17 Jan Navan Hurdle 22f Soft To Heavy 5/12; 26 Feb Clonmel Hurdle 19.3f Heavy 7/16; 2 Apr Clonmel Hurdle 19.5f Soft 1/12
    DATA for: Last-run finishing speed +6.3% vs that field (finished strongly)
    DATA against: Returns from a 234-day break; First run over fences in our data
- Polepatrick (hrs_41090973) | 6yo G | 166lb | OR 120 | draw 0 | jockey Kieren Buckley | trainer Dermot A McLoughlin (14d 0/6) | headgear - | last run 23 days | form 31-234 | MARKET 6.4% | 09:00 median 11.00 | Matchbook 12.50
    comment: Polepatrick has been consistent, finishing fourth last time out, a third two starts back and a second three starts back, and he's had 23 days to recover, though he's slipped down the order since his win four starts back.
    DATA: model 4.2% | style Leader (led 43% of runs) | runs in data 5 | last 3: 8 Jun Roscommon Hurdle 20f Yielding To Soft 2/3; 7 Sep Galway Chase 18.2f Yielding 3/6; 30 Oct Down Royal (IRE) Chase 20f Good 4/7 fig 118
    DATA for: Best recent form figure 118, 8 lb above field average; Good recent finishing positions
    DATA against: Race comments mention jumping mistakes in 2 of its last 5 runs
- Long Branch (hrs_41052242) | 6yo G | 166lb | OR 117 | draw 0 | jockey Michael Kenneally(3) | trainer Seamus Neville (14d 0/0) | headgear - | last run 28 days | form U24-44 | MARKET 6.3% | 09:00 median 11.00 | Matchbook 13.50
    comment: Long Branch has finished fourth in each of his last three outings, with a second four starts back, so he is consistent but yet to win in that spell. He has run over today's trip and going and is fresh after 28 days, though 166 lb is a hefty burden.
    DATA: model 8.3% | style Midfield (led 3% of runs) | runs in data 6 | last 3: 29 Apr Punchestown Hurdle 19.3f Yielding 4/24; 7 May Wexford Chase 23f Good To Yielding 4/6; 25 Oct Wexford (IRE) Chase 19.5f Soft 4/13 fig 109
    DATA against: Race comments mention jumping mistakes in 2 of its last 5 runs; Fell or unseated in 1 of its last 5 jumps runs
- Found A Diamond (hrs_47345172) | 6yo G | 166lb | OR 114 | draw 0 | jockey Shane Markey(7) | trainer Ross O'Sullivan (14d 1/18) | headgear - | last run 232 days | form 51334- | MARKET 4.8% | 09:00 median 13.00 | Matchbook 19.00
    comment: Found A Diamond has been consistent, finishing fourth last time out, then a third two starts back, a third three starts back and a winner four starts back, and he has run over today's trip and going.
    DATA: model 9.6% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 14 Jan Fairyhouse Hurdle 24f Yielding 3/9; 14 Feb Haydock Hurdle 24.3f Good To Soft 3/13; 4 Apr Fairyhouse Hurdle 23.8f Yielding To Soft 4/20
    DATA for: Good recent finishing positions
    DATA against: Returns from a 232-day break; First run over fences in our data
- Chase The Moon (hrs_51341486) | 5yo G | 166lb | OR - | draw 0 | jockey Tiernan Power Roche | trainer P. J. Rothwell (14d 0/24) | headgear - | last run 28 days | form 4619-7 | MARKET 4.3% | 09:00 median 17.00 | Matchbook 19.50
    comment: Chase The Moon showed he can win with a victory three starts back, but he's been a seventh last time out and a ninth before that, and a trainer going 0/24 over the last 14 days adds to the doubts.
    DATA: model 5.2% | style Midfield (led 3% of runs) | runs in data 4 | last 3: 15 Feb Punchestown Hurdle 22.7f Heavy 1/10; 4 Apr Fairyhouse Hurdle 23.8f Yielding To Soft 9/20; 25 Oct Wexford (IRE) Chase 19.5f Soft 7/13
    DATA for: Has won at this trip or further
    DATA against: Trainer 0 wins from 24 runs, last 14 days; Race comments mention jumping mistakes in 2 of its last 4 runs
- Dubhain (hrs_52055402) | 6yo G | 166lb | OR - | draw 0 | jockey Danny Mullins | trainer S. R. B. Crawford (14d 1/8) | headgear ht | last run 192 days | form 3550-1 | MARKET 3.4% | 09:00 median 26.00 | Matchbook 24.00
    comment: Dubhain won last time out, but that came 192 days ago and he was unplaced or fifth in two of the three runs before it, so a long layoff and 166 lb make him hard to fancy.
    DATA: model 4.1% | style Prominent (led 29% of runs) | runs in data 4 | last 3: 17 Mar Down Royal Hurdle 17.5f Good To Yielding 5/19; 4 Apr Fairyhouse Hurdle 20f Yielding To Soft 10/25; 14 May Perth Hurdle 20.2f Good To Soft 1/5
    DATA against: Returns from a 192-day break; Race comments mention jumping mistakes in 3 of its last 4 runs; First run over fences in our data
- Mojoe (hrs_47620860) | 6yo G | 166lb | OR - | draw 0 | jockey Simon Torrens | trainer Patrick T Foley (14d 0/4) | headgear - | last run 19 days | form 131P-5 | MARKET 3.3% | 09:00 median 23.00 | Matchbook 24.00
    comment: Mojoe won three and five starts back and has run over today's trip and going, but a fifth last time out after being pulled up the run before leaves him with questions, and 166 lb is a hefty burden.
    DATA: model 3.0% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 8 Mar Naas Hurdle 19f Soft To Heavy 1/17; 2 May Punchestown Hurdle 20.5f Yielding PU/17; 3 Nov Fairyhouse (IRE) Hurdle 20f Good To Yielding 5/5
    DATA against: Last-run finishing speed -6.8% vs that field (faded); Pulled up in 1 of its last 5 jumps runs; First run over fences in our data
- No Looking Back (hrs_29409429) | 8yo G | 166lb | OR - | draw 0 | jockey Phillip Enright | trainer Oliver McKiernan (14d 0/6) | headgear tb | last run 28 days | form 0-7P2P | MARKET 2.6% | 09:00 median 29.00 | Matchbook 40.00
    DATA: model 3.3% | style Held up (led 3% of runs) | runs in data 7 | last 3: 24 Sep Listowel Hurdle 20f Good PU/15; 10 Oct Fairyhouse Hurdle 16f Good 2/9; 25 Oct Wexford (IRE) Chase 19.5f Soft PU/13
    DATA against: Pulled up in 2 of its last 5 jumps runs
- Maidenstreetprince (hrs_27359010) | 9yo G | 166lb | OR 120 | draw 0 | jockey Eoin Staples(5) | trainer C Byrnes (14d 0/6) | headgear v (1st time) | last run 15 days | form F32-76 | MARKET 2.5% | 09:00 median 29.00 | Matchbook 32.00
    comment: Maidenstreetprince returns a fresh 15 days after a sixth last time out, having been second three starts back and third four starts back, and he has run over today's trip and going before.
    DATA: model 4.5% | style Prominent (led 3% of runs) | runs in data 5 | last 3: 25 Sep Listowel Flat 14f Good To Yielding 11/13; 26 Oct Galway (IRE) Chase 18f Heavy 7/7 fig 109; 7 Nov Gowran Park (IRE) Chase 16f Good 6/7 fig 106
    DATA for: First-time headgear
    DATA against: Poor recent finishing positions; Aged 9, older than most of this field
- Mossy Way (hrs_47620874) | 6yo G | 166lb | OR - | draw 0 | jockey  | trainer Edward Buckley (14d 0/2) | headgear p | last run 19 days | form 743-96 | MARKET 2.3% | 09:00 median 34.00 | Matchbook 44.00
    comment: Mossy Way is yet to win in his last five, though a third three starts back and a fourth four starts back show he can get involved, and he has run over today's trip and going. A sixth last time out and a ninth before that, plus 166 lb, hold him back.
    DATA: model 2.2% | style Prominent (led 3% of runs) | runs in data 5 | last 3: 5 Apr Fairyhouse Hurdle 16.5f Yielding To Soft 3/25; 2 Oct Gowran Park Hurdle 20.2f Good 9/17; 3 Nov Fairyhouse (IRE) Chase 24.5f Good To Yielding 6/7 fig 106
    DATA against: Last-run finishing speed -2.4% vs that field (faded); Race comments mention jumping mistakes in 2 of its last 4 runs
- Between Friends (hrs_44450763) | 6yo M | 159lb | OR - | draw 0 | jockey Charlie O'Dwyer(3) | trainer E Bolger (14d 0/0) | headgear - | last run 168 days | form 5/6P-1 | MARKET 2.2% | 09:00 median 34.00 | Matchbook 40.00
    comment: Between Friends won last time out, but that came after a pulled up and a sixth in her previous two starts, and she returns from 168 days off carrying 159 lb.
    DATA: model 8.5% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 7 Jun Punchestown Hurdle 21.6f Good 1/18
    DATA for: Last-run finishing speed +8.6% vs that field (finished strongly); Has won at this trip or further
    DATA against: Returns from a 168-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Take The Free (hrs_63357567) | 4yo G | 157lb | OR - | draw 0 | jockey Peter Smithers(5) | trainer E Bolger (14d 0/0) | headgear - | last run 21 days | form 6210R5 | MARKET 1.7% | 09:00 median 41.00 | Matchbook 65.00
    comment: Hard to fancy: Take The Free was fifth last time out, refused two starts back and has won just once in his last six, a victory four starts back.
    DATA: model 2.7% | style Midfield (led 23% of runs) | runs in data 7 | last 3: 11 Sep Ballinrobe Hurdle 21.9f Good To Yielding 11/14; 14 Oct Punchestown (IRE) Hurdle 20f Good REF/13; 1 Nov Cork (IRE) Hurdle 20f Good To Yielding 5/14
    DATA for: Has won at this trip or further
    DATA against: First run over fences in our data
- Market Ready (hrs_50402338) | 5yo G | 166lb | OR - | draw 0 | jockey  | trainer Sean Aherne (14d 0/1) | headgear - | last run 15 days | form -4P237 | MARKET 1.7% | 09:00 median 41.00 | Matchbook 65.00
    comment: Winless in his last five and beaten into seventh last time out, Market Ready is hard to fancy, though a third and a second in the two runs before that show he can place. He has run over today's trip and on this going, but 166 lb is a big burden.
    DATA: model 4.8% | style Midfield (led 3% of runs) | runs in data 8 | last 3: 16 Aug Tramore Hurdle 21.4f Good To Yielding 2/9; 22 Oct Clonmel (IRE) Hurdle 20f Good To Yielding 3/13 fig 103; 7 Nov Gowran Park (IRE) Chase 20f Good 7/10
    DATA for: Good recent finishing positions
    DATA against: Best recent form figure 103, 7 lb below field average; Pulled up in 1 of its last 5 jumps runs
- King In Love (hrs_38884790) | 6yo G | 166lb | OR - | draw 0 | jockey  | trainer Sean Aherne (14d 0/1) | headgear - | last run 28 days | form 350-78 | MARKET 1.5% | 09:00 median 51.00 | Matchbook 75.00
    comment: King In Love is winless in his last five, with an eighth last time out and a seventh two starts back, so he is hard to fancy. He has run over today's trip and going, and a third five starts back is the pick of his form, but 166 lb is a big burden.
    DATA: model 2.3% | style Held up (led 3% of runs) | runs in data 4 | last 3: 8 Mar Naas Hurdle 19f Soft To Heavy 16/17; 11 May Killarney Hurdle 20.2f Good To Yielding 7/12; 25 Oct Wexford (IRE) Chase 19.5f Soft 8/13
    DATA against: Poor recent finishing positions

## 3:19 Cork | race_id rac_32305227318 | Adare Manor Opportunity Handicap Hurdle
Hurdle |  | 2m1f0y | going Soft | Turf | 13 runners | rating band - | age 3yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Lanzhou (hrs_52055654) | 5yo G | 157lb | OR 101 | draw 0 | jockey Jordan Canavan(4) | trainer J P Flavin (14d 0/1) | headgear - | last run 28 days | form -07211 | MARKET 18.4% | 09:00 median 4.33 | Matchbook 5.00 | CHECK (skip line 4.11)
    comment: Lanzhou arrives in cracking form, a winner last time out and again two starts back, with a second three starts back, and he has run over today's trip and going before. Carrying 157 lb is the main risk, though a 28-day break shouldn't concern.
    DATA: model 11.7% | style Held up (led 3% of runs) | runs in data 9 | last 3: 16 Aug Tramore Hurdle 16.6f Good To Yielding 2/14; 8 Oct Tramore Hurdle 16f Yielding 1/9; 25 Oct Galway (IRE) Chase 18f Soft To Heavy 1/13 fig 108
    DATA for: Best recent form figure 108, 9 lb above field average; Recent figures 7 lb above its current mark (looks well handicapped); Has won at this trip or further; Good recent finishing positions
    DATA against: Race comments mention jumping mistakes in 2 of its last 5 runs; Pace: steady gallop likely, hard to come from off the pace
- Theanniversary Man (hrs_35446369) | 7yo G | 148lb | OR 85 | draw 0 | jockey Conor Smithers(4) | trainer James M Barcoe (14d 2/5) | headgear - | last run 5 days | form P47671 | MARKET 17.9% | 09:00 median 4.50 | Matchbook 5.00
    comment: Theanniversary Man won last time out but was beaten in the three runs before that, finishing a seventh, a sixth and a seventh, so one good day is hard to build on under 148 lb.
    DATA: model 9.2% | style Held up (led 3% of runs) | runs in data 6 | last 3: 10 Aug Ballinrobe Hurdle 16.5f Good 6/14; 1 Nov Cork (IRE) Hurdle 16f Good To Yielding 7/21 fig 80; 17 Nov Limerick (IRE) Hurdle 16f Heavy 1/9 fig 89
    DATA for: Recent figures 4 lb above its current mark (looks well handicapped); Trainer 40% wins (2/5), last 14 days; Carries 7 lb less than average
    DATA against: Best recent form figure 89, 10 lb below field average; Official rating 85, 14 lb below field average; Pace: steady gallop likely, hard to come from off the pace
- St Lawrence's Well (hrs_47345375) | 6yo G | 167lb | OR 111 | draw 0 | jockey Eoin Staples | trainer Declan Queally (14d 0/7) | headgear t (1st time) | last run 35 days | form F5-934 | MARKET 12.9% | 09:00 median 6.00 | Matchbook 7.20
    comment: St Lawrence's Well heads into this fit from a 35-day break, having finished fourth last time out and third two starts back, and he carries 167 lb off an official mark of 111.
    DATA: model 9.2% | style Midfield (led 3% of runs) | runs in data 4 | last 3: 15 Jun Kilbeggan Hurdle 24.5f Good 9/12; 1 Oct Clonmel Hurdle 22.8f Good 3/6; 18 Oct Limerick (IRE) Hurdle 19.5f Good To Yielding 4/14 fig 108
    DATA for: Best recent form figure 108, 9 lb above field average; Official rating 111, 12 lb above field average; First-time headgear
    DATA against: Carries 12 lb more than average
- Springboard (hrs_39978218) | 7yo G | 142lb | OR 86 | draw 0 | jockey Michael Kenneally | trainer Michael J McDonagh (14d 0/2) | headgear b (1st time) | last run 10 days | form -95196 | MARKET 9.8% | 09:00 median 8.50 | Matchbook 9.00
    comment: Springboard is hard to fancy after a sixth last time out and a ninth before that, with his only win three starts back, though he has run over today's trip and is back quickly after 10 days.
    DATA: model 9.3% | style Midfield (led 3% of runs) | runs in data 7 | last 3: 6 Oct Galway Chase 18.2f Yielding To Soft 1/10; 25 Oct Galway (IRE) Chase 18f Soft To Heavy 9/13; 12 Nov Thurles (IRE) Chase 18f Good 6/12 fig 86
    DATA for: Has won at this trip or further; Carries 13 lb less than average; First-time headgear
    DATA against: Best recent form figure 86, 13 lb below field average; Official rating 86, 13 lb below field average
- Mister Loolah (hrs_48854001) | 6yo G | 156lb | OR 100 | draw 0 | jockey Luke Burke Ott(4) | trainer Alexander Ott (14d 0/1) | headgear - | last run 21 days | form PB-4F3 | MARKET 9.5% | 09:00 median 8.00 | Matchbook 9.80
    comment: Mister Loolah arrives fit after a third last time out, 21 days ago, and has run over today's trip and going, but a fell, a brought down and a pulled up in his last five starts show he's yet to win and not the safest. Carrying 156 lb off 100, he looks a midfield sort at best.
    DATA: model 3.8% | style Midfield (led 4% of runs) | runs in data 5 | last 3: 4 Oct Killarney Chase 20.8f Good To Yielding 4/4; 22 Oct Clonmel (IRE) Chase 21f Good F/15; 1 Nov Cork (IRE) Hurdle 16f Good To Yielding 3/21 fig 104
    DATA for: Best recent form figure 104, 5 lb above field average; Recent figures 4 lb above its current mark (looks well handicapped)
    DATA against: Race comments mention jumping mistakes in 2 of its last 5 runs; Fell or unseated in 1 of its last 5 jumps runs; Pulled up in 1 of its last 5 jumps runs
- Lenjoleur De Palma (hrs_46024846) | 5yo G | 162lb | OR 106 | draw 0 | jockey Patrick M O'Brien | trainer E McNamara (14d 0/12) | headgear - | last run 36 days | form 123-64 | MARKET 9.0% | 09:00 median 9.00 | Matchbook 10.00
    comment: Lenjoleur De Palma has been in the frame regularly lately, with a second four starts back and a third three starts back, and he has run over today's trip and going before.
    DATA: model 8.2% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 22 Mar Limerick Hurdle 16.2f Soft To Heavy 3/13; 24 Sep Listowel Hurdle 16f Good 6/13; 17 Oct Limerick (IRE) Hurdle 17f Good To Yielding 4/15 fig 101
    DATA for: Official rating 106, 7 lb above field average
    DATA against: Trainer 0 wins from 12 runs, last 14 days; Carries 7 lb more than average
- Royal Belief (hrs_52862628) | 4yo G | 161lb | OR 105 | draw 0 | jockey Carl Millar | trainer Cian Collins (14d 1/7) | headgear - | last run 41 days | form 5901- | MARKET 4.8% | 09:00 median 15.00 | Matchbook 21.00
    comment: Royal Belief won last time out, though he was unplaced two starts back, and he has run over today's trip after 41 days off.
    DATA: model 13.0% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 31 Mar Limerick Hurdle 16f Soft 1/12; 22 Apr Gowran Park Flat 13.7f Soft 2/13; 12 Oct Roscommon Flat 12.2f Soft 6/16
    DATA for: Official rating 105, 6 lb above field average; Good recent finishing positions
    DATA against: Carries 6 lb more than average
- You Lift Me Up (hrs_7000000805) | 4yo G | 151lb | OR 95 | draw 0 | jockey Shane Markey(4) | trainer P. J. Rothwell (14d 0/24) | headgear - | last run 30 days | form 07043 | MARKET 4.7% | 09:00 median 13.00 | Matchbook 32.00
    comment: Winless in his last five, though he comes here on a better note after a third last time out and a fourth two starts back, and he has run over today's trip and going.
    DATA: model 4.3% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 7 Sep Galway Hurdle 16.7f Yielding 17/20; 26 Sep Listowel Hurdle 16f Good 4/12; 23 Oct Sligo (IRE) Hurdle 17.5f Yielding 3/12 fig 97
    DATA against: Trainer 0 wins from 24 runs, last 14 days; Race comments mention jumping mistakes in 2 of its last 4 runs
- River Vale (hrs_28930930) | 10yo G | 163lb | OR 107 | draw 0 | jockey Kevin A Murphy(4) | trainer Michael Winters (14d 0/4) | headgear - | last run 28 days | form DF41-P | MARKET 4.3% | 09:00 median 15.00 | Matchbook 32.00
    comment: The main risk is that he was pulled up last time out.
    DATA: model 7.3% | style Prominent (led 3% of runs) | runs in data 5 | last 3: 12 Mar Limerick Chase 17.8f Heavy 4/8; 6 Apr Cork Chase 17.2f Good To Yielding 1/6; 25 Oct Wexford (IRE) Hurdle 17f Soft PU/13
    DATA for: Official rating 107, 8 lb above field average; Has won at this trip or further
    DATA against: Carries 8 lb more than average; Fell or unseated in 1 of its last 5 jumps runs; Pulled up in 1 of its last 5 jumps runs; Aged 10, older than most of this field
- Saporetti (hrs_56370587) | 4yo G | 158lb | OR 102 | draw 0 | jockey James Smith | trainer Brian M McMahon (14d 0/2) | headgear h (1st time) | last run 111 days | form 5-335 | MARKET 3.5% | 09:00 median 19.00 | Matchbook 36.00
    comment: Saporetti has been consistent without winning, with a fifth last time out, a third two starts back and another third three starts back, and he has run over today's trip and going before.
    DATA: model 11.8% | style Prominent (led 3% of runs) | runs in data 4 | last 3: 6 Jun Punchestown Hurdle 16.5f Good To Yielding 3/5; 10 Jul Cork Hurdle 17.3f Good 3/14; 3 Aug Cork Hurdle 18f Good 5/18
    DATA for: Good recent finishing positions; First-time headgear
    DATA against: Returns from a 111-day break; Race comments mention jumping mistakes in 3 of its last 4 runs
- Lar Na Pairce (hrs_51124416) | 5yo G | 158lb | OR 102 | draw 0 | jockey Rian Lane(4) | trainer E Bolger (14d 0/0) | headgear - | last run 350 days | form 790- | MARKET 2.3% | 09:00 median 26.00 | Matchbook 55.00
    comment: Lightly raced and returning after 350 days off, Lar Na Pairce showed little in his last three, unplaced last time, a ninth two starts back, and a seventh three starts back. He's yet to win in that spell, but he's unexposed and could improve, with 158 lb to carry off an official mark of 102.
    DATA: model 5.8% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 350-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Kaligo (hrs_50622551) | 7yo G | 154lb | OR 98 | draw 0 | jockey Liam McKenna | trainer C A Murphy (14d 0/6) | headgear - | last run 581 days | form 000/ | MARKET 1.7% | 09:00 median 51.00 | Matchbook 60.00
    comment: Kaligo returns after 581 days off, unplaced in each of his last three starts and yet to win in that spell, so he is unexposed with scope to improve, though he looks to need the run carrying 154 lb off an official mark of 98.
    DATA: model 5.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 581-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Issy's Lad (hrs_17393306539) | 5yo G | 140lb | OR 83 | draw 0 | jockey Peter Smithers(2) | trainer W J Austin (14d 0/1) | headgear - | last run 13 days | form 007 | MARKET 1.3% | 09:00 median 51.00 | Matchbook 120.00
    comment: Lightly raced and yet to win in his last three, Issy's Lad was seventh last time out and unplaced in the two runs before, so he remains unexposed. Back quickly after 13 days off and carrying 140 lb off an official mark of 83, he could have more to offer.
    DATA: model 0.8% | style Held up (led 5% of runs) | runs in data 3 | last 3: 14 Oct Punchestown (IRE) Hurdle 16.5f Good 14/15; 26 Oct Galway (IRE) Hurdle 16.5f Soft To Heavy 12/20; 9 Nov Punchestown (IRE) Hurdle 16f Good To Yielding 7/10
    DATA for: Carries 15 lb less than average
    DATA against: Official rating 83, 16 lb below field average; Poor recent finishing positions; Pace: steady gallop likely, hard to come from off the pace

## 3:49 Cork | race_id rac_32305229255 | William Hill Challenge Series Handicap Hurdle
Hurdle |  | 3m0f40y | going Soft | Turf | 19 runners | rating band - | age 4yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Cock And Bull (hrs_36878835) | 5yo G | 162lb | OR 99 | draw 0 | jockey Donagh Meyler | trainer Emmet Mullins (14d 2/7) | headgear t | last run 3 days | form 8570-1 | MARKET 20.7% | 09:00 median 3.25 | Matchbook 3.50 | CHECK (skip line 3.09)
    comment: Won last time out, but that came after a run of a seventh, a fifth and an eighth, and he is back in just three days under 162 lb, so he is hard to fancy.
    DATA: model 7.1% | style Prominent (led 3% of runs) | runs in data 8 | last 3: 29 Jul Galway Flat 16.5f Yielding 1/19; 10 Oct Newmarket Flat 18f Good 20/29; 19 Nov Thurles (IRE) Hurdle 20f Good 1/13 fig 100
    DATA for: Trainer 29% wins (2/7), last 14 days; Last-run finishing speed +2.2% vs that field (finished strongly); Good recent finishing positions
    DATA against: Official rating 99, 6 lb below field average
- King Of The Greys (hrs_58132802) | 5yo G | 165lb | OR 109 | draw 0 | jockey Sam Ewing | trainer Peter Fahey (14d 3/6) | headgear - | last run 19 days | form 8PPP31 | MARKET 13.6% | 09:00 median 4.33 | Matchbook 5.70
    comment: King Of The Greys arrives in good heart as a winner last time out, with a third two starts back, but three pulled-up efforts before that raise doubts about his consistency.
    DATA: model 11.0% | style Held up (led 3% of runs) | runs in data 8 | last 3: 19 Sep Navan Hurdle 19f Good PU/16; 13 Oct Punchestown Hurdle 20f Good 3/17; 3 Nov Fairyhouse (IRE) Hurdle 20f Good To Yielding 1/15 fig 105
    DATA for: Best recent form figure 105, 8 lb above field average; Trainer 50% wins (3/6), last 14 days; Last-run finishing speed +4.8% vs that field (finished strongly)
    DATA against: Pulled up in 3 of its last 5 jumps runs; Pace: steady gallop likely, hard to come from off the pace
- The Rebel Fox (hrs_59429580) | 6yo G | 168lb | OR 112 | draw 0 | jockey Ricky Doyle | trainer Ross O'Sullivan (14d 1/18) | headgear - | last run 40 days | form 225-23 | MARKET 6.0% | 09:00 median 10.00 | Matchbook 13.50
    comment: The Rebel Fox arrives in solid form, third last time out and second twice in his last five, and he has run over today's trip, though he is yet to win in that spell.
    DATA: model 8.9% | style Midfield (led 29% of runs) | runs in data 3 | last 3: 8 Mar Naas Hurdle 19f Soft To Heavy 5/14; 13 May Punchestown Hurdle 24f Good To Yielding 2/7; 13 Oct Punchestown Hurdle 20f Good 3/13
    DATA for: Official rating 112, 7 lb above field average; Good recent finishing positions
    DATA against: Carries 7 lb more than average
- Jackmoon (hrs_38433255) | 7yo G | 165lb | OR 109 | draw 0 | jockey Jordan Canavan(7) | trainer J P Flavin (14d 0/1) | headgear t | last run 168 days | form 522-33 | MARKET 5.9% | 09:00 median 10.00 | Matchbook 13.50
    comment: Jackmoon has been thereabouts, finishing third last time out, a third two starts back and a second three starts back, and he has run over today's trip and going before. Yet he is winless in his last five, returns after 168 days off and carries a hefty 165 lb.
    DATA: model 9.0% | style Prominent (led 4% of runs) | runs in data 5 | last 3: 19 Apr Tramore Hurdle 20.5f Yielding 2/10; 16 May Wexford Hurdle 24f Good To Yielding 3/13; 7 Jun Punchestown Hurdle 23.5f Good 3/13
    DATA for: Good recent finishing positions
    DATA against: Returns from a 168-day break; Race comments mention jumping mistakes in 2 of its last 5 runs
- Political Stance (hrs_52742032) | 6yo G | 151lb | OR 95 | draw 0 | jockey  | trainer C Byrnes (14d 0/6) | headgear tp | last run 5 days | form -0051P | MARKET 4.9% | 09:00 median 11.00 | Matchbook 19.50
    comment: Political Stance was pulled up last time out just five days ago, and he has only one win in his last five starts, with a fifth and two unplaced efforts before it. He has run over today's trip and won two starts back, but 151 lb is a stiff burden to carry.
    DATA: model 5.1% | style Midfield (led 3% of runs) | runs in data 7 | last 3: 4 Oct Killarney Hurdle 22.8f Good To Yielding 5/13; 17 Oct Limerick (IRE) Hurdle 21.5f Good To Yielding 1/16 fig 93; 17 Nov Limerick (IRE) Hurdle 24.5f Heavy PU/10
    DATA for: Carries 10 lb less than average
    DATA against: Best recent form figure 93, 4 lb below field average; Official rating 95, 10 lb below field average; Pulled up in 1 of its last 5 jumps runs
- Tiger Twins (hrs_57071812) | 5yo G | 164lb | OR 108 | draw 0 | jockey Thomas O'Connor(7) | trainer Eoin Christopher McCarthy (14d 0/4) | headgear t | last run 60 days | form 540-5F | MARKET 4.5% | 09:00 median 15.00 | Matchbook 16.50
    comment: Tiger Twins is yet to win in his last five, with a fall last time out following a run of fifth, unplaced, fourth and fifth, though he has run on today's going before.
    DATA: model 3.5% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 5 Apr Cork NH Flat 19f Yielding 14/16; 11 May Killarney Hurdle 20.2f Good To Yielding 5/12; 23 Sep Listowel Hurdle 24f Good F/14
    DATA against: Fell or unseated in 1 of its last 2 jumps runs
- Drumconnor Hill (hrs_58132655) | 5yo G | 153lb | OR 97 | draw 0 | jockey Jordan Gainford | trainer Cian Collins (14d 1/7) | headgear p | last run 23 days | form 470P03 | MARKET 4.5% | 09:00 median 15.00 | Matchbook 15.50
    comment: Winless in his last six, Drumconnor Hill was third last time out, but that came after an unplaced run and a pulled up in the three starts before it, which makes him hard to fancy. He has run over today's trip and is fresh enough after 23 days, though 153 lb is a big ask.
    DATA: model 3.3% | style Midfield (led 23% of runs) | runs in data 7 | last 3: 7 Sep Galway Hurdle 22.4f Yielding PU/19; 2 Oct Gowran Park Hurdle 20.2f Good 12/20; 30 Oct Down Royal (IRE) Hurdle 24.5f Good To Yielding 3/20 fig 93
    DATA for: Last-run finishing speed +6.2% vs that field (finished strongly); Carries 8 lb less than average
    DATA against: Best recent form figure 93, 4 lb below field average; Official rating 97, 8 lb below field average; Pulled up in 1 of its last 5 jumps runs
- Its Not Over Yet (hrs_34598151) | 7yo M | 150lb | OR 94 | draw 0 | jockey  | trainer Oliver McKiernan (14d 0/6) | headgear tb | last run 19 days | form -38385 | MARKET 4.1% | 09:00 median 13.00 | Matchbook 22.00
    comment: Winless in her last five, Its Not Over Yet was fifth last time out, and before that came an eighth two starts back and a third three starts back.
    DATA: model 4.9% | style Prominent (led 3% of runs) | runs in data 7 | last 3: 4 Aug Roscommon Hurdle 24f Yielding To Soft 3/15; 25 Sep Listowel Hurdle 22f Good To Yielding 8/14; 3 Nov Fairyhouse (IRE) Hurdle 24f Good To Yielding 5/12 fig 92
    DATA for: Carries 11 lb less than average
    DATA against: Best recent form figure 92, 5 lb below field average; Official rating 94, 11 lb below field average
- John The Diva (hrs_27997102) | 9yo G | 160lb | OR 104 | draw 0 | jockey Paddy Cody(7) | trainer M A Cahill (14d 0/2) | headgear - | last run 297 days | form /2523- | MARKET 3.7% | 09:00 median 17.00 | Matchbook 22.00
    comment: John The Diva arrives with a third last time out and a second two starts back, yet he is without a win in his last four and returns after 297 days off.
    DATA: model 9.2% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 11 Jan Punchestown Chase 22.6f Soft 2/12; 29 Jan Thurles Chase 20.9f Heavy 3/9
    DATA for: Good recent finishing positions
    DATA against: Returns from a 297-day break; Lightly raced: 2 runs in our data, so the model has little to go on; First run over hurdles in our data
- Toor Khov (hrs_34268514) | 8yo G | 165lb | OR 109 | draw 0 | jockey Liam Quinlan | trainer Ms M Flynn (14d 0/3) | headgear - | last run 3 days | form F24-0P | MARKET 3.7% | 09:00 median 17.00 | Matchbook 20.00
    comment: The risk is a quick return just three days after being pulled up, carrying 165 lb.
    DATA: model 2.9% | style Midfield (led 4% of runs) | runs in data 6 | last 3: 5 Apr Cork Hurdle 24.1f Yielding 4/16; 26 Sep Listowel Chase 23.8f Good 12/14; 19 Nov Thurles (IRE) Chase 22f Good PU/12
    DATA against: Race comments mention jumping mistakes in 2 of its last 5 runs; Fell or unseated in 1 of its last 5 jumps runs; Pulled up in 1 of its last 5 jumps runs
- Bergamasquo (hrs_50221297) | 5yo G | 163lb | OR 107 | draw 0 | jockey Eoin Staples(5) | trainer Gavin Cromwell (14d 4/42) | headgear b (1st time) | last run 53 days | form 944F-P | MARKET 3.7% | 09:00 median 19.00 | Matchbook 22.00
    comment: Bergamasquo is hard to fancy, pulled up last time and a faller before that, and he is winless in his last five after 53 days off.
    DATA: model 4.8% | style Midfield (led 3% of runs) | runs in data 4 | last 3: 5 Mar Thurles Hurdle 22.9f Soft 4/13; 29 Mar Downpatrick Hurdle 21.8f Yielding To Soft F/10; 30 Sep Sligo Chase 25.8f Good PU/8
    DATA for: First-time headgear
    DATA against: Fell or unseated in 1 of its last 4 jumps runs; Pulled up in 1 of its last 4 jumps runs
- Ney (hrs_24372733) | 8yo G | 165lb | OR 109 | draw 0 | jockey Kieren Buckley | trainer Edward Buckley (14d 0/2) | headgear p | last run 280 days | form 55627- | MARKET 3.5% | 09:00 median 21.00 | Matchbook 19.50
    comment: The risk is a 280-day absence, with a seventh last time out and 165 lb to carry.
    DATA: model 6.4% | style Held up (led 5% of runs) | runs in data 2 | last 3: 11 Jan Punchestown Chase 22.6f Soft 2/13; 15 Feb Punchestown Chase 27.3f Heavy 7/14
    DATA against: Returns from a 280-day break; Lightly raced: 2 runs in our data, so the model has little to go on; First run over hurdles in our data; Pace: steady gallop likely, hard to come from off the pace
- West Of Bally (hrs_51124010) | 6yo G | 167lb | OR 111 | draw 0 | jockey Gearoid Brouder(5) | trainer E McNamara (14d 0/12) | headgear - | last run 27 days | form 5138-0 | MARKET 3.4% | 09:00 median 19.00 | Matchbook 24.00
    comment: West Of Bally has a win four starts back and a third three starts back, but he's unplaced last time out and an eighth two runs ago, so the form has cooled. He has run on today's going and returns after 27 days, though 167 lb is a hefty burden for a midfield type.
    DATA: model 4.2% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 15 Feb Punchestown Hurdle 22.7f Heavy 8/10; 26 Oct Galway (IRE) Hurdle 22f Heavy 10/12 fig 104
    DATA for: Best recent form figure 104, 7 lb above field average; Official rating 111, 6 lb above field average
    DATA against: Recent figures 7 lb below its current mark (looks high in the weights); Trainer 0 wins from 12 runs, last 14 days; Carries 6 lb more than average; Lightly raced: 2 runs in our data, so the model has little to go on
- Big Debates (hrs_9711625) | 13yo G | 165lb | OR 109 | draw 0 | jockey Anna McGuinness(7) | trainer Robert Tyner (14d 0/0) | headgear - | last run 385 days | form 2P/12- | MARKET 3.4% | 09:00 median 19.00 | Matchbook 25.00
    comment: The 385-day absence is the one worry, though he carries 165 lb off an official mark of 109.
    DATA: model 4.3% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 385-day break; Lightly raced: 0 runs in our data, so the model has little to go on; Aged 13, older than most of this field
- The Miracle Man (hrs_28608090) | 8yo G | 160lb | OR 104 | draw 0 | jockey Patrick M O'Brien(5) | trainer Gordon Elliott (14d 10/75) | headgear b | last run 141 days | form 433-9P | MARKET 3.2% | 09:00 median 21.00 | Matchbook 22.00
    comment: The Miracle Man was pulled up last time and returns after 141 days, but he has run over today's trip and going, with a third and another third in his last five outings.
    DATA: model 6.5% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 8 Feb Navan Hurdle 21.8f Heavy 3/11; 12 May Sligo Hurdle 25.8f Good 9/12; 4 Jul Bellewstown Hurdle 24.5f Good PU/15
    DATA against: Returns from a 141-day break; Pulled up in 1 of its last 5 jumps runs
- Born Bright (hrs_39021472) | 7yo M | 165lb | OR 109 | draw 0 | jockey James Smith(3) | trainer Ms Claire O'Connell (14d 0/3) | headgear p | last run 50 days | form 4-34PP | MARKET 3.1% | 09:00 median 21.00 | Matchbook 25.00
    comment: The risk is obvious: she was pulled up in her last two outings and returns after 50 days off carrying 165 lb.
    DATA: model 2.8% | style Held up (led 3% of runs) | runs in data 4 | last 3: 8 Jun Roscommon Chase 25.1f Yielding To Soft 4/15; 26 Sep Listowel Chase 23.8f Good PU/14; 3 Oct Gowran Park Hurdle 24.2f Good To Yielding PU/11
    DATA against: Pulled up in 2 of its last 4 jumps runs; Pace: steady gallop likely, hard to come from off the pace
- Scotty Joe (hrs_52495562) | 5yo G | 153lb | OR 97 | draw 0 | jockey  | trainer P. J. Rothwell (14d 0/24) | headgear - | last run 80 days | form P1-608 | MARKET 3.1% | 09:00 median 21.00 | Matchbook 25.00
    comment: Scotty Joe is hard to fancy after an eighth last time out, an unplaced run and a sixth in his last three, and he returns from 80 days off with a yard 0/24 over the last 14 days. A win four starts back and a 97 mark are the positives, though 153 lb is a hefty burden.
    DATA: model 1.2% | style Held up (led 4% of runs) | runs in data 3 | last 3: 15 May Kilbeggan Hurdle 18.3f Good 6/16; 6 Jun Punchestown Hurdle 16.5f Good To Yielding 17/24; 3 Sep Kilbeggan Hurdle 16f Good To Yielding 8/11
    DATA for: Carries 8 lb less than average
    DATA against: Official rating 97, 8 lb below field average; Trainer 0 wins from 24 runs, last 14 days; Poor recent finishing positions; Pace: steady gallop likely, hard to come from off the pace
- Strange Currency (hrs_50188488) | 6yo G | 156lb | OR 100 | draw 0 | jockey Mr E M Nugent(7) | trainer Brian M McMahon (14d 0/2) | headgear - | last run 35 days | form 5-6774 | MARKET 3.1% | 09:00 median 21.00 | Matchbook 26.00
    comment: Strange Currency showed a little more when fourth last time out after two sevenths, and he has run over today's trip and on this going, but he is winless in his last five and returns after 35 days carrying 156 lb.
    DATA: model 3.0% | style Midfield (led 3% of runs) | runs in data 9 | last 3: 10 Aug Ballinrobe Hurdle 25.9f Good 7/7; 11 Sep Ballinrobe Hurdle 21.9f Good To Yielding 7/14; 18 Oct Limerick (IRE) Hurdle 24f Good To Yielding 4/8 fig 95
    DATA for: Carries 5 lb less than average
    DATA against: Race comments mention jumping mistakes in 2 of its last 5 runs
- Custers Mistake (hrs_18780965) | 9yo G | 165lb | OR 109 | draw 0 | jockey Conor Smithers(7) | trainer Peter McCreery (14d 0/1) | headgear - | last run 44 days | form 821-PP | MARKET 1.9% | 09:00 median 34.00 | Matchbook 46.00
    comment: Custers Mistake has been pulled up in his last two starts, which tempers a win three starts back and a second four starts back, though he returns after 44 days off and has run over today's trip.
    DATA: model 2.1% | style Held up (led 5% of runs) | runs in data 2 | last 3: 11 Sep Ballinrobe Chase 17.2f Good To Yielding PU/16; 9 Oct Downpatrick Chase 23.7f Good PU/14
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Pulled up in 2 of its last 2 jumps runs; First run over hurdles in our data; Pace: steady gallop likely, hard to come from off the pace
