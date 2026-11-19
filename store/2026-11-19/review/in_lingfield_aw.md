# Card review packet: Lingfield (AW), 2026-11-19

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


## 11:18 Lingfield (AW) | race_id rac_32304820548 | All-Weather Championship Is Back Novice Stakes (GBB Race)
Flat | Class 4 | 1m1y | going Standard | AW | 9 runners | rating band - | age 3yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Nascondino (hrs_65414587) | 3yo G | 131lb | OR 78 | draw 8 | jockey Billy Loughnane | trainer Daniel & Claire Kubler (14d 0/0) | headgear - | last run 24 days | form 7423 | MARKET 47.2% | 09:00 median 1.80 | Matchbook 1.92
    DATA: model 23.9% | style Prominent (led 38% of runs) | runs in data 4 | last 3: 9 Oct Kempton Flat 8f Standard To Slow 4/10; 14 Oct Nottingham Flat 8.3f Good To Soft 2/14; 26 Oct Redcar Flat 10f Heavy 3/10 fig 55
    DATA for: Best recent form figure 55, 12 lb above field average; Good recent finishing positions
- Silk Braid (hrs_57718073) | 3yo F | 133lb | OR 92 | draw 1 | jockey Kaiya Fraser | trainer Harry Eustace (14d 0/4) | headgear - | last run 208 days | form 1-2 | MARKET 31.3% | 09:00 median 2.50 | Matchbook 3.10
    DATA: model 41.1% | style Unknown | runs in data 1 | last 3: 25 Apr Navan Flat 5.8f Good To Yielding 2/7
    DATA against: Returns from a 208-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Zeriya (hrs_63203476) | 3yo F | 126lb | OR - | draw 5 | jockey Jason Watson | trainer Andrew Balding (14d 0/18) | headgear - | last run 185 days | form 58 | MARKET 11.7% | 09:00 median 6.00 | Matchbook 9.20
    DATA: model 6.5% | style Midfield (led 8% of runs) | runs in data 2 | last 3: 2 Apr Southwell Flat 8.1f Standard 5/5; 18 May Windsor Flat 8.1f Good 8/10
    DATA against: Trainer 0 wins from 18 runs, last 14 days; Returns from a 185-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- Quipster (hrs_17395635558) | 3yo G | 131lb | OR - | draw 2 | jockey Kieran O'Neill | trainer Lemos De Souza (14d 0/1) | headgear - | last run - days | form - | MARKET 3.5% | 09:00 median 21.00 | Matchbook 32.00
    DATA: model 6.0% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Educating Sheila (hrs_59059308) | 3yo F | 126lb | OR - | draw 9 | jockey Molly Keegan-Price(7) | trainer Jane Chapple-Hyam (14d 0/1) | headgear - | last run 339 days | form 07- | MARKET 2.1% | 09:00 median 29.00 | Matchbook 65.00
    DATA: model 5.9% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 339-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Raider (hrs_17392137336) | 3yo F | 126lb | OR - | draw 3 | jockey Grace McEntee | trainer George Boughey (14d 1/8) | headgear - | last run 17 days | form 58 | MARKET 1.9% | 09:00 median 26.00 | Matchbook 130.00
    DATA: model 8.6% | style Midfield (led 8% of runs) | runs in data 2 | last 3: 21 Sep Leicester Flat 10f Good 5/7; 2 Nov Wolverhampton (AW) Flat 9.5f Standard 8/10 fig 46
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Espressona Signora (hrs_17393259604) | 3yo F | 126lb | OR - | draw 6 | jockey Laura Pearson | trainer Gihan Arnolda (14d 0/1) | headgear - | last run 38 days | form 5 | MARKET 1.6% | 09:00 median 41.00 | Matchbook 100.00
    DATA: model 3.9% | style Unknown | runs in data 1 | last 3: 12 Oct Kempton Flat 8f Standard To Slow 5/8
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Tilsworth Emma (hrs_17391993402) | 3yo F | 126lb | OR - | draw 7 | jockey Oliver Carmichael(7) | trainer J. R. Jenkins (14d 0/2) | headgear - | last run 45 days | form 65 | MARKET 0.6% | 09:00 median 101.00 | Matchbook 300.00
    DATA: model 1.6% | style Prominent (led 38% of runs) | runs in data 2 | last 3: 9 Sep Kempton Flat 7f Standard To Slow 6/7; 5 Oct Yarmouth Flat 8f Good To Firm 5/5
    DATA against: Last-run finishing speed -2.4% vs that field (faded); Lightly raced: 2 runs in our data, so the model has little to go on
- Opal Rose (hrs_40859595) | 5yo M | 128lb | OR - | draw 4 | jockey Callum Hutchinson | trainer Joe Tickle (14d 0/3) | headgear h (1st time) | last run 17 days | form 70 | MARKET 0.2% | 09:00 median 201.00 | Matchbook 1000.00
    DATA: model 2.5% | style Held up (led 5% of runs) | runs in data 2 | last 3: 9 Oct Kempton Flat 8f Standard To Slow 7/10; 2 Nov Wolverhampton (AW) Flat 9.5f Standard 10/10 fig 29
    DATA for: First-time headgear
    DATA against: Best recent form figure 29, 14 lb below field average; Last-run finishing speed -2.3% vs that field (faded); Lightly raced: 2 runs in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace

## 11:48 Lingfield (AW) | race_id rac_32304822485 | AWC Finals Day At Newcastle 26th March Nursery Handicap Stakes
Flat | Class 4 | 7f1y | going Standard | AW | 8 runners | rating band 0-85 | age 2yo
DATA pace: Even - Two likely leaders (Rogue Imperial, Nour). A fair, even gallop is most likely.
- Rogue Imperial (hrs_64847293) | 2yo C | 134lb | OR 82 | draw 2 | jockey Rossa Ryan | trainer Archie Watson (14d 0/1) | headgear - | last run 53 days | form 537211 | MARKET 23.9% | 09:00 median 3.50 | Matchbook 4.10 | CHECK (skip line 3.32)
    comment: Rogue Imperial arrives in fine heart, a winner last time out and again two starts back, and has run over today's trip, but 53 days off the track and 134 lb from draw 2 temper the case.
    DATA: model 19.3% | style Leader (led 83% of runs) | runs in data 6 | last 3: 1 Aug Lingfield Flat 6f Good To Firm 2/7; 24 Aug Brighton Flat 6f Good To Firm 1/5; 27 Sep Epsom Downs Flat 7f Good 1/7
    DATA for: Has won at this trip or further; Good recent finishing positions
- Arthur Carrot (hrs_17390697996) | 2yo C | 127lb | OR 75 | draw 5 | jockey Billy Loughnane | trainer George Boughey (14d 1/8) | headgear - | last run 22 days | form 26324 | MARKET 19.4% | 09:00 median 4.42 | Matchbook 4.90
    comment: Arthur Carrot has been in the frame often, with a second five starts back and another two starts back, then a fourth last time out 22 days ago, though he remains winless in recent starts.
    DATA: model 8.8% | style Prominent (led 3% of runs) | runs in data 5 | last 3: 24 Sep Southwell Flat 6.1f Standard 3/11; 21 Oct Kempton (AW) Flat 7f Standard / Slow 2/14 fig 75; 28 Oct Kempton (AW) Flat 6f Standard / Slow 4/7 fig 68
    DATA for: Best recent form figure 75, 7 lb above field average; Good recent finishing positions
- Show Me Glory (hrs_17391112067) | 2yo F | 132lb | OR 80 | draw 6 | jockey Callum Hutchinson | trainer Andrew Balding (14d 0/18) | headgear - | last run 23 days | form 321 | MARKET 18.5% | 09:00 median 4.50 | Matchbook 5.30
    comment: Show Me Glory arrives in cracking form, a winner last time out, then second two starts back, and a third three starts back, with 23 days since that win.
    DATA: model 25.6% | style Prominent (led 29% of runs) | runs in data 3 | last 3: 21 Aug Newmarket Flat 7f Good To Firm 3/7; 23 Sep Kempton Flat 6f Standard To Slow 2/11; 27 Oct Wolverhampton (AW) Flat 7f Standard 1/6 fig 72
    DATA for: Best recent form figure 72, 4 lb above field average; Has won at this trip or further; Good recent finishing positions
    DATA against: Recent figures 8 lb below its current mark (looks high in the weights); Trainer 0 wins from 18 runs, last 14 days
- Rosevannion (hrs_65161467) | 2yo F | 135lb | OR 83 | draw 3 | jockey David Egan | trainer S. P. C. Woods (14d 0/0) | headgear - | last run 162 days | form 41 | MARKET 10.2% | 09:00 median 8.50 | Matchbook 9.60
    comment: The main risk is a 162-day absence, which leaves fitness the question.
    DATA: model 10.8% | style Prominent (led 8% of runs) | runs in data 2 | last 3: 29 May Wolverhampton Flat 7.2f Standard 4/6; 10 Jun Kempton Flat 7f Standard To Slow 1/9
    DATA for: Official rating 83, 6 lb above field average; Last-run finishing speed +2.6% vs that field (finished strongly); Has won at this trip or further
    DATA against: Carries 6 lb more than average; Returns from a 162-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- Bacha (hrs_65974594) | 2yo C | 121lb | OR 69 | draw 9 | jockey Freya Frain(7) | trainer George Boughey (14d 1/8) | headgear - | last run 78 days | form 533 | MARKET 9.8% | 09:00 median 9.00 | Matchbook 9.20
    DATA: model 4.8% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 27 Jun Newcastle Flat 5f Standard To Slow 5/6; 1 Aug Thirsk Flat 5f Good 3/8; 2 Sep Hamilton Flat 5f Soft 3/7
    DATA for: Good recent finishing positions; Carries 8 lb less than average
    DATA against: Official rating 69, 8 lb below field average
- Nour (hrs_62170066) | 2yo F | 131lb | OR 79 | draw 4 | jockey Pierre-Louis Jamin | trainer K. R. Burke (14d 0/9) | headgear - | last run 24 days | form 33160 | MARKET 7.8% | 09:00 median 11.00 | Matchbook 12.50
    DATA: model 9.8% | style Leader (led 29% of runs) | runs in data 4 | last 3: 25 Jul York Flat 6f Good To Firm 3/6; 27 Aug Southwell Flat 6.1f Standard 1/7; 18 Sep Ayr Flat 5f Soft 6/8
    DATA for: Good recent finishing positions
    DATA against: Trainer 0 wins from 9 runs, last 14 days
- Boy Basilica (hrs_17393467161) | 2yo C | 128lb | OR 76 | draw 1 | jockey Finley Marsh | trainer Richard Hughes (14d 0/9) | headgear - | last run 23 days | form 61 | MARKET 7.0% | 09:00 median 11.00 | Matchbook 15.50
    comment: Drawn 1, he looks hard to fancy.
    DATA: model 17.2% | style Unknown | runs in data 2 | last 3: 12 Oct Kempton Flat 7f Standard To Slow 6/11; 27 Oct Wolverhampton (AW) Flat 8.5f Standard 1/12 fig 56
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 56, 12 lb below field average; Recent figures 20 lb below its current mark (looks high in the weights); Trainer 0 wins from 9 runs, last 14 days; Lightly raced: 2 runs in our data, so the model has little to go on
- Cloud Summit (hrs_65322432) | 2yo G | 128lb | OR 76 | draw 7 | jockey Grace McEntee | trainer George Boughey (14d 1/8) | headgear - | last run 111 days | form 466 | MARKET 3.3% | 09:00 median 26.00 | Matchbook 30.00
    comment: The risk is fitness, as he's been off for 111 days and is yet to win in recent form.
    DATA: model 3.8% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 11 Jun Newbury Flat 6.5f Good To Soft 4/9; 6 Jul Lingfield Flat 7f Standard 6/9; 31 Jul Newmarket Flat 6f Good To Firm 6/7
    DATA against: Returns from a 111-day break

## 12:18 Lingfield (AW) | race_id rac_32305211822 | AWC Season 14 Has Begun / EBF Restricted Maiden Fillies' Stakes (For Horses In Band D) (Div I) (GBB Race)
Flat | Class 4 | 7f1y | going Standard | AW | 9 runners | rating band - | age 2yo
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Valley Rising (hrs_17395639730) | 2yo F | 128lb | OR - | draw 6 | jockey Callum Rodriguez | trainer Owen Burrows (14d 0/2) | headgear - | last run - days | form - | MARKET 31.5% | 09:00 median 2.75 | Matchbook 2.90
    DATA: model 8.9% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- She Is Mighty (hrs_62169842) | 2yo F | 128lb | OR - | draw 7 | jockey Rossa Ryan | trainer Steph Hollinshead (14d 0/3) | headgear - | last run 33 days | form 72 | MARKET 16.4% | 09:00 median 5.00 | Matchbook 5.80
    DATA: model 12.6% | style Midfield (led 8% of runs) | runs in data 2 | last 3: 8 Jun Leicester Flat 7f Good 7/9; 17 Oct Catterick Flat 7f Good 2/7 fig 56
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Fabulova (hrs_60820788) | 2yo F | 128lb | OR - | draw 3 | jockey Cieren Fallon | trainer Tom Clover (14d 0/0) | headgear - | last run 29 days | form 7 | MARKET 15.7% | 09:00 median 5.50 | Matchbook 5.90
    DATA: model 17.6% | style Held up (led 8% of runs) | runs in data 1 | last 3: 21 Oct Kempton (AW) Flat 7f Standard / Slow 7/10 fig 51
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace; Course: hold-up horses have won 0.7× their fair share at 7f here
- Anaream (hrs_60819885) | 2yo F | 128lb | OR - | draw 8 | jockey Billy Loughnane | trainer Jack Jones (14d 0/2) | headgear - | last run - days | form - | MARKET 11.0% | 09:00 median 7.00 | Matchbook 9.00
    DATA: model 8.9% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Clarice Starling (hrs_63811419) | 2yo F | 128lb | OR - | draw 1 | jockey George Wood | trainer Richard Spencer (14d 0/3) | headgear - | last run 37 days | form 6 | MARKET 9.6% | 09:00 median 8.75 | Matchbook 9.80
    DATA: model 21.6% | style Unknown | runs in data 1 | last 3: 13 Oct Leicester Flat 6f Good To Soft 6/11
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Farouche (hrs_17393325313) | 2yo F | 128lb | OR - | draw 9 | jockey Marco Ghiani | trainer Stuart Williams (14d 0/4) | headgear - | last run 27 days | form 64 | MARKET 8.0% | 09:00 median 11.00 | Matchbook 12.00
    DATA: model 11.2% | style Prominent (led 8% of runs) | runs in data 2 | last 3: 6 Oct Brighton Flat 8f Good To Firm 6/9; 23 Oct Wolverhampton (AW) Flat 8.5f Standard 4/9 fig 52
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Miss Clarice (hrs_17393337829) | 2yo F | 128lb | OR - | draw 2 | jockey Rob Hornby | trainer Jonathan Portman (14d 1/6) | headgear - | last run 14 days | form 94 | MARKET 6.4% | 09:00 median 13.00 | Matchbook 15.00
    DATA: model 8.7% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 6 Oct Southwell Flat 7.1f Standard 9/13; 5 Nov Southwell (AW) Flat 6f Standard 4/11 fig 51
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Acrackintime (hrs_17394184745) | 2yo F | 128lb | OR - | draw 4 | jockey Taryn Langley(5) | trainer Robert Edwards (14d 0/2) | headgear - | last run 27 days | form 9 | MARKET 1.2% | 09:00 median 85.50 | Matchbook 90.00
    DATA: model 6.4% | style Held up (led 8% of runs) | runs in data 1 | last 3: 23 Oct Wolverhampton (AW) Flat 8.5f Standard 9/9
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace; Course: hold-up horses have won 0.7× their fair share at 7f here
- Sparkling Jem (hrs_64780660) | 2yo F | 128lb | OR 34 | draw 5 | jockey Kieran O'Neill | trainer Rachel Cook & John Bridger (14d 0/0) | headgear - | last run 107 days | form 0860 | MARKET 0.2% | 09:00 median 201.00 | Matchbook 1000.00
    DATA: model 4.2% | style Held up (led 5% of runs) | runs in data 4 | last 3: 4 Jun Lingfield Flat 6f Standard 8/10; 29 Jun Kempton Flat 7f Standard To Slow 6/10; 4 Aug Lingfield Flat 7f Standard 10/10
    DATA against: Poor recent finishing positions; Returns from a 107-day break; Pace: steady gallop likely, hard to come from off the pace; Course: hold-up horses have won 0.7× their fair share at 7f here

## 12:53 Lingfield (AW) | race_id rac_32304824422 | AWC Season 14 Has Begun / EBF Restricted Maiden Fillies' Stakes (For Horses In Band D) (Div II) (GBB Race)
Flat | Class 4 | 7f1y | going Standard | AW | 8 runners | rating band - | age 2yo
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Classic Bellini (hrs_63809599) | 2yo F | 128lb | OR 64 | draw 6 | jockey David Allan | trainer Tim Easterby (14d 0/12) | headgear - | last run 14 days | form 73632 | MARKET 33.5% | 09:00 median 2.50 | Matchbook 2.84
    DATA: model 42.1% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 2 Oct Wolverhampton Flat 5.1f Standard 6/9; 13 Oct Leicester Flat 6f Good To Soft 3/12; 5 Nov Southwell (AW) Flat 6f Standard 2/11 fig 53
    DATA for: Best recent form figure 53, 16 lb above field average; Good recent finishing positions
    DATA against: Trainer 0 wins from 12 runs, last 14 days
- Star Run (hrs_17395638687) | 2yo F | 128lb | OR - | draw 5 | jockey Callum Hutchinson | trainer Andrew Balding (14d 0/18) | headgear - | last run - days | form - | MARKET 20.5% | 09:00 median 4.00 | Matchbook 4.70
    DATA: model 8.2% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Trainer 0 wins from 18 runs, last 14 days; Lightly raced: 0 runs in our data, so the model has little to go on
- Freshie (hrs_17393645514) | 2yo F | 128lb | OR - | draw 8 | jockey Joe Leavy | trainer Roger Teal (14d 0/3) | headgear - | last run 38 days | form 4 | MARKET 19.9% | 09:00 median 4.50 | Matchbook 4.70
    DATA: model 16.2% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 12 Oct Kempton Flat 8f Standard To Slow 4/10
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- One Nine Seven (hrs_17394119036) | 2yo F | 128lb | OR - | draw 3 | jockey David Egan | trainer Lemos De Souza (14d 0/1) | headgear - | last run 14 days | form 97 | MARKET 10.0% | 09:00 median 8.00 | Matchbook 10.00
    DATA: model 7.5% | style Held up (led 5% of runs) | runs in data 2 | last 3: 22 Oct Newmarket Flat 8f Soft 9/9 fig 14; 5 Nov Chelmsford (AW) Flat 7.5f Standard 7/12 fig 38
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace; Course: hold-up horses have won 0.7× their fair share at 7f here
- Grasshopper (hrs_17395636601) | 2yo F | 128lb | OR - | draw 2 | jockey Daniel Muscutt | trainer James Fanshawe (14d 0/4) | headgear - | last run - days | form - | MARKET 8.8% | 09:00 median 10.00 | Matchbook 10.50
    DATA: model 8.2% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Kameko Star (hrs_17395637644) | 2yo F | 128lb | OR - | draw 1 | jockey Callum Shepherd | trainer Jack Jones (14d 0/2) | headgear - | last run - days | form - | MARKET 5.3% | 09:00 median 15.00 | Matchbook 20.00
    DATA: model 8.2% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Stansfield Dream (hrs_17393703922) | 2yo F | 128lb | OR - | draw 7 | jockey Kaiya Fraser | trainer Harry Eustace (14d 0/4) | headgear - | last run 17 days | form 00 | MARKET 1.2% | 09:00 median 101.00 | Matchbook 110.00
    DATA: model 6.3% | style Held up (led 5% of runs) | runs in data 2 | last 3: 15 Oct Brighton Flat 7f Good 12/12 fig 28; 2 Nov Chelmsford (AW) Flat 7f Standard 10/12
    DATA against: Best recent form figure 28, 8 lb below field average; Last-run finishing speed -4.2% vs that field (faded); Lightly raced: 2 runs in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace; Course: hold-up horses have won 0.7× their fair share at 7f here
- Sassaturra (hrs_17394798029) | 2yo F | 128lb | OR - | draw 4 | jockey William Cox | trainer J. S. Moore (14d 0/7) | headgear - | last run 17 days | form 0 | MARKET 0.8% | 09:00 median 101.00 | Matchbook 230.00
    DATA: model 3.3% | style Held up (led 8% of runs) | runs in data 1 | last 3: 2 Nov Chelmsford (AW) Flat 6f Standard 12/12 fig 27
    DATA against: Best recent form figure 27, 10 lb below field average; Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace; Course: hold-up horses have won 0.7× their fair share at 7f here

## 1:28 Lingfield (AW) | race_id rac_32304826359 | AWC Trials Day - Lingfield 2nd Jan 2027 Fillies' Handicap Stakes
Flat | Class 4 | 6f1y | going Standard | AW | 5 runners | rating band 0-85 | age 3yo+
DATA pace: Even - Two likely leaders (Startling, Rajiba). A fair, even gallop is most likely.
- Zooella (hrs_53294479) | 3yo F | 135lb | OR 83 | draw 2 | jockey Rossa Ryan | trainer Ralph Beckett (14d 0/8) | headgear - | last run 24 days | form -11051 | MARKET 54.4% | 09:00 median 1.67 | Matchbook 1.78
    comment: Zooella won last time out and has three wins in her last five starts, fresh enough after 24 days off, and she has run over today's trip and going before.
    DATA: model 33.3% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 20 Aug York Flat 7f Good To Soft 18/19; 24 Sep Newmarket Flat 6f Good 5/10; 26 Oct Southwell (AW) Flat 6f Standard 1/10 fig 82
    DATA for: Best recent form figure 82, 4 lb above field average; Official rating 83, 8 lb above field average; Last-run finishing speed +2.7% vs that field (finished strongly); Has won at this trip or further
    DATA against: Trainer 0 wins from 8 runs, last 14 days; Carries 8 lb more than average
- Moostar (hrs_41305061) | 4yo F | 119lb | OR 67 | draw 5 | jockey Jack Doughty | trainer James Owen (14d 3/28) | headgear tv | last run 17 days | form 289172 | MARKET 17.6% | 09:00 median 5.00 | Matchbook 5.70
    DATA: model 17.4% | style Held up (led 5% of runs) | runs in data 12 | last 3: 6 Oct Leicester Flat 7f Good To Firm 1/10; 16 Oct Redcar Flat 7f Good 7/18 fig 68; 2 Nov Chelmsford (AW) Flat 7f Standard 2/8 fig 70
    DATA for: Last-run finishing speed +2.9% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions; Carries 8 lb less than average
    DATA against: Best recent form figure 70, 8 lb below field average; Official rating 67, 8 lb below field average
- Startling (hrs_41014057) | 4yo F | 130lb | OR 78 | draw 4 | jockey Cieren Fallon | trainer John Wainwright (14d 1/1) | headgear b | last run 17 days | form 211081 | MARKET 15.0% | 09:00 median 6.00 | Matchbook 6.60
    comment: Startling arrives in cracking nick, having won last time out, 17 days ago, and three of her last six, and she has run over today's trip and on this going before. The one concern is a poor eighth two starts back, so she must prove that was a blip under 130 lb.
    DATA: model 18.9% | style Leader (led 54% of runs) | runs in data 12 | last 3: 30 Sep Musselburgh Flat 5f Good To Soft 10/12; 19 Oct Pontefract Flat 5f Heavy 8/9 fig 52; 2 Nov Chelmsford (AW) Flat 5f Standard 1/7 fig 82
    DATA for: Best recent form figure 82, 4 lb above field average; Recent figures 4 lb above its current mark (looks well handicapped)
- Rajiba (hrs_58534875) | 3yo F | 124lb | OR 72 | draw 1 | jockey Finley Marsh | trainer Richard Hughes (14d 0/9) | headgear - | last run 111 days | form 4-2364 | MARKET 9.0% | 09:00 median 9.25 | Matchbook 12.00
    comment: The main risk is a 111-day absence, and she is yet to win in her last five.
    DATA: model 21.4% | style Leader (led 54% of runs) | runs in data 4 | last 3: 2 Jul Kempton Flat 7f Standard To Slow 3/8; 17 Jul Newbury Flat 8f Good To Firm 6/10; 31 Jul Wolverhampton Flat 7.2f Standard 4/10
    DATA against: Trainer 0 wins from 9 runs, last 14 days; Returns from a 111-day break
- Moonlight Mirage (hrs_55794963) | 3yo F | 129lb | OR 77 | draw 3 | jockey Billy Loughnane | trainer David Loughnane (14d 1/2) | headgear - | last run 218 days | form 1663-8 | MARKET 4.0% | 09:00 median 21.00 | Matchbook 26.00
    comment: The risk is a 218-day absence after an eighth last time out, so fitness is the question.
    DATA: model 9.0% | style Held up (led 8% of runs) | runs in data 1 | last 3: 15 Apr Southwell Flat 6.1f Standard 8/8
    DATA against: Returns from a 218-day break; Lightly raced: 1 run in our data, so the model has little to go on

## 2:03 Lingfield (AW) | race_id rac_32304828296 | All-Weather Championships Season XIV River Eden EBF Fillies' Stakes (Listed Race) (GBBPlus Race)
Flat | Class 1 | 1m5f | going Standard | AW | 12 runners | rating band - | age 3yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Morrophore (hrs_42616385) | 5yo M | 131lb | OR 104 | draw 13 | jockey Ryan Moore | trainer John & Thady Gosden (14d 5/14) | headgear - | last run 64 days | form 41-103 | MARKET 28.9% | 09:00 median 3.00 | Matchbook 3.15 | CHECK (skip line 2.85)
    comment: Morrophore bids to build on a third last time out, and she's a winner three starts back and again four starts back, so the form is solid.
    DATA: model 16.2% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 17 Jan Lingfield Flat 10f Standard 1/10; 20 Aug York Flat 11.9f Good To Soft 11/13; 16 Sep Yarmouth Flat 10.1f Good To Soft 3/11
    DATA for: Official rating 104, 12 lb above field average; Trainer 36% wins (5/14), last 14 days; Good recent finishing positions
- Likealot (hrs_49695107) | 4yo F | 131lb | OR 102 | draw 6 | jockey Rossa Ryan | trainer Ralph Beckett (14d 0/8) | headgear - | last run 117 days | form 221-41 | MARKET 24.7% | 09:00 median 3.45 | Matchbook 3.75
    comment: Likealot arrives in cracking form, a winner last time out, a fourth two starts back, and a winner three starts back, and she has run over today's trip and going before. The risk is a 117-day absence, and 131 lb is a hefty burden off an official mark of 102.
    DATA: model 15.1% | style Held up (led 8% of runs) | runs in data 2 | last 3: 27 Jun Chester Flat 10.3f Good 4/8; 25 Jul York Flat 11.9f Good To Firm 1/10
    DATA for: Official rating 102, 10 lb above field average; Last-run finishing speed +5.4% vs that field (finished strongly)
    DATA against: Trainer 0 wins from 8 runs, last 14 days; Returns from a 117-day break; Lightly raced: 2 runs in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Yamnah (hrs_17391521966) | 3yo F | 126lb | OR 83 | draw 12 | jockey Billy Loughnane | trainer John & Thady Gosden (14d 5/14) | headgear p | last run 24 days | form 421 | MARKET 11.1% | 09:00 median 7.50 | Matchbook 8.80
    comment: Yamnah arrives in good heart, a winner last time out, then a second two starts back, and fresh enough after 24 days, with experience of today's going.
    DATA: model 8.2% | style Held up (led 4% of runs) | runs in data 3 | last 3: 7 Sep Windsor Flat 10f Good 4/7; 7 Oct Kempton Flat 11f Standard To Slow 2/8; 26 Oct Southwell (AW) Flat 11f Standard 1/6 fig 73
    DATA for: Trainer 36% wins (5/14), last 14 days; Last-run finishing speed +6.3% vs that field (finished strongly); Good recent finishing positions
    DATA against: Best recent form figure 73, 8 lb below field average; Official rating 83, 9 lb below field average; Pace: steady gallop likely, hard to come from off the pace
- Little Dorrit (hrs_52176614) | 4yo F | 131lb | OR 101 | draw 9 | jockey Callum Rodriguez | trainer Roger Varian (14d 3/6) | headgear - | last run 25 days | form 8-5434 | MARKET 10.8% | 09:00 median 7.50 | Matchbook 9.00
    comment: Consistent sort who has finished fourth last time out, with a third two starts back, and she has run over today's trip after 25 days off.
    DATA: model 15.0% | style Prominent (led 8% of runs) | runs in data 3 | last 3: 21 Jun Pontefract Flat 12f Good 5/9; 18 Jul Newmarket Flat 12f Good To Firm 4/9; 8 Oct Bath Flat 14f Good 3/12
    DATA for: Official rating 101, 9 lb above field average; Trainer 50% wins (3/6), last 14 days
    DATA against: Course: prominent racers have won 0.6× their fair share at 13f here
- Littlecote (hrs_57316364) | 3yo F | 126lb | OR 96 | draw 7 | jockey Jason Watson | trainer Andrew Balding (14d 0/18) | headgear - | last run 42 days | form 222132 | MARKET 6.3% | 09:00 median 13.00 | Matchbook 15.50
    comment: Littlecote has finished in the first three in each of her last six starts, including a second last time out and a win three starts back, and has run over today's trip and going before. The main risk is a 42-day break, with 126 lb to carry.
    DATA: model 9.5% | style Held up (led 5% of runs) | runs in data 6 | last 3: 19 May Newcastle Flat 12.4f Standard 1/6; 18 Sep Newbury Flat 12f Good 3/8; 8 Oct Bath Flat 14f Good 2/12
    DATA for: Good recent finishing positions
    DATA against: Trainer 0 wins from 18 runs, last 14 days; Pace: steady gallop likely, hard to come from off the pace
- Pierian (hrs_64072428) | 3yo F | 126lb | OR 93 | draw 14 | jockey Cieren Fallon | trainer William Haggas (14d 3/9) | headgear p (1st time) | last run 25 days | form 140140 | MARKET 5.4% | 09:00 median 15.00 | Matchbook 18.00
    comment: Pierian has won twice in her last six starts, including a win three starts back, but she was unplaced last time out and a fourth two starts back. She has run over today's trip and is fit after 25 days off, though 126 lb and an official mark of 93 leave little room for error.
    DATA: model 10.2% | style Prominent (led 38% of runs) | runs in data 6 | last 3: 31 Jul Goodwood Flat 11.2f Good To Firm 10/13; 2 Sep Bath Flat 11.6f Good 1/6; 8 Oct Bath Flat 14f Good 4/12
    DATA for: Trainer 33% wins (3/9), last 14 days; First-time headgear
    DATA against: Course: prominent racers have won 0.6× their fair share at 13f here
- Light of Paris (hrs_63422681) | 3yo F | 126lb | OR 87 | draw 8 | jockey Sean Levey | trainer John & Thady Gosden (14d 5/14) | headgear t | last run 13 days | form 41733 | MARKET 4.4% | 09:00 median 18.00 | Matchbook 24.00
    comment: Light of Paris has been thereabouts lately, third last time out and another third two starts back, and she is fresh enough after 13 days with experience on today's going.
    DATA: model 6.0% | style Held up (led 8% of runs) | runs in data 5 | last 3: 7 Jun Goodwood Flat 9.9f Soft 7/8; 3 Oct Newmarket Flat 10f Good To Firm 3/6; 6 Nov Newcastle (AW) Flat 10f Standard 3/14 fig 86
    DATA for: Best recent form figure 86, 5 lb above field average; Trainer 36% wins (5/14), last 14 days; Good recent finishing positions
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Golden Muse (hrs_52709790) | 3yo F | 126lb | OR 88 | draw 2 | jockey Kieran Shoemark | trainer Marco Botti (14d 0/5) | headgear - | last run 30 days | form 113161 | MARKET 3.8% | 09:00 median 21.00 | Matchbook 27.00
    comment: Four wins in her last six starts, including last time out, is the standout, and she has run over today's trip and going before, but a 30-day break and a 126 lb burden are hard to overlook.
    DATA: model 7.5% | style Unknown | runs in data 7 | last 3: 10 Jun Kempton Flat 12f Standard To Slow 1/9; 11 Sep Doncaster Flat 11.9f Good 6/10; 20 Oct Yarmouth Flat 11.5f Soft 1/8 fig 83
    DATA for: Last-run finishing speed +2.3% vs that field (finished strongly); Good recent finishing positions
- Gone By (hrs_57590512) | 3yo F | 126lb | OR 91 | draw 4 | jockey Rhys Clutterbuck | trainer Ralph Beckett (14d 0/8) | headgear - | last run 34 days | form -21183 | MARKET 1.5% | 09:00 median 41.00 | Matchbook 85.00
    comment: She has run over today's trip, and 34 days since her last run is no concern.
    DATA: model 5.0% | style Prominent (led 29% of runs) | runs in data 5 | last 3: 30 Jun Salisbury Flat 12f Good To Firm 1/3; 1 Aug Newmarket Flat 12f Good To Firm 8/8; 16 Oct Haydock Flat 14f Heavy 3/5 fig 82
    DATA for: Good recent finishing positions
    DATA against: Trainer 0 wins from 8 runs, last 14 days; Course: prominent racers have won 0.6× their fair share at 13f here
- Cabrera (hrs_40319328) | 5yo M | 131lb | OR 86 | draw 1 | jockey Rob Hornby | trainer Edward Bethell (14d 0/5) | headgear - | last run 110 days | form -459V1 | MARKET 1.1% | 09:00 median 67.00 | Matchbook 120.00
    comment: Won last time out, which is the standout line, and she has run over today's trip and going before, but 110 days off is a long break and she carries 131 lb off an official mark of 86.
    DATA: model 3.7% | style Midfield (led 3% of runs) | runs in data 4 | last 3: 31 May Thirsk Flat 12f Good 5/12; 21 Jun Pontefract Flat 12f Good 9/9; 1 Aug Hamilton Flat 13.1f Good 1/10
    DATA for: Has won at this trip or further
    DATA against: Official rating 86, 6 lb below field average; Returns from a 110-day break
- Dojin (hrs_48112288) | 4yo F | 131lb | OR 85 | draw 5 | jockey David Egan | trainer S. P. C. Woods (14d 0/0) | headgear - | last run 42 days | form 123138 | MARKET 1.0% | 09:00 median 67.00 | Matchbook 130.00
    comment: Dojin has won twice in her last six starts, including a winner three starts back, and has run over today's trip and going, but a eighth last time out and 42 days off leave questions, while 131 lb is a notable burden for an official mark of 85.
    DATA: model 2.8% | style Midfield (led 8% of runs) | runs in data 7 | last 3: 15 Aug Newmarket Flat 14f Good To Firm 1/5; 17 Sep Southwell Flat 16.5f Standard 3/4; 8 Oct Bath Flat 14f Good 8/12
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Official rating 85, 7 lb below field average
- Miss Wong (hrs_45006682) | 4yo F | 131lb | OR 83 | draw 3 | jockey Callum Shepherd | trainer David Simcock (14d 0/2) | headgear - | last run 41 days | form -76560 | MARKET 1.0% | 09:00 median 101.00 | Matchbook 140.00
    DATA: model 1.0% | style Held up (led 8% of runs) | runs in data 5 | last 3: 4 Jul Beverley Flat 12.1f Good To Firm 5/5; 16 Sep Yarmouth Flat 10.1f Good To Soft 6/11; 9 Oct Newmarket Flat 10f Good To Soft 12/14
    DATA against: Official rating 83, 9 lb below field average; Last-run finishing speed -2.8% vs that field (faded); Pace: steady gallop likely, hard to come from off the pace

## 2:38 Lingfield (AW) | race_id rac_32304830233 | All-Weather Championships Season XIV Fleur De Lys Fillies' Stakes (Listed Race)
Flat | Class 1 | 1m1y | going Standard | AW | 12 runners | rating band - | age 3yo+
DATA pace: Lone leader - Enchanted Queen is the only habitual front-runner and may be allowed an easy lead.
- Enchanted Queen (hrs_55947682) | 3yo F | 126lb | OR 94 | draw 4 | jockey Billy Loughnane | trainer George Boughey (14d 1/8) | headgear - | last run 48 days | form 232-11 | MARKET 25.5% | 09:00 median 3.25 | Matchbook 3.70 | CHECK (skip line 3.09)
    comment: Winner last time out and two starts back, with a second and third before that, so the form reads well, but a 48-day absence is a concern and she has run over today's trip and going.
    DATA: model 21.9% | style Leader (led 57% of runs) | runs in data 2 | last 3: 9 Sep Kempton Flat 7f Standard To Slow 1/7; 2 Oct Wolverhampton Flat 8.6f Standard 1/4
    DATA for: Last-run finishing speed +2.9% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions; Pace: may get an uncontested lead
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Sky Safari (hrs_42073906) | 5yo M | 128lb | OR 106 | draw 9 | jockey Daniel Muscutt | trainer James Fanshawe (14d 0/4) | headgear t | last run 64 days | form -21837 | MARKET 17.6% | 09:00 median 5.00 | Matchbook 5.20
    comment: Sky Safari has run over today's trip and going and was a third two starts back, but she was only seventh last time out and returns after 64 days off.
    DATA: model 8.3% | style Unknown | runs in data 5 | last 3: 8 May Chester Flat 10.3f Good 8/9; 26 Jun Newcastle Flat 10.2f Standard To Slow 3/7; 16 Sep Yarmouth Flat 10.1f Good To Soft 7/11
    DATA for: Official rating 106, 8 lb above field average; Has won at this trip or further
- Kon Tiki (hrs_47655370) | 4yo F | 133lb | OR 107 | draw 2 | jockey Ryan Moore | trainer Jane Chapple-Hyam (14d 0/1) | headgear - | last run 47 days | form -24196 | MARKET 14.5% | 09:00 median 5.50 | Matchbook 6.80
    comment: The risk is form, with a sixth last time out and a ninth two starts back, after 47 days off.
    DATA: model 12.3% | style Midfield (led 4% of runs) | runs in data 5 | last 3: 25 Jul Ascot Flat 8f Good To Firm 1/8; 29 Aug Sandown Flat 8f Good To Soft 9/10; 3 Oct Newmarket Flat 8f Good To Firm 6/7
    DATA for: Official rating 107, 9 lb above field average; Has won at this trip or further
- Pacific Mission (hrs_55091827) | 3yo F | 126lb | OR 101 | draw 5 | jockey Colin Keane | trainer Andrew Balding (14d 0/18) | headgear t | last run 19 days | form 327633 | MARKET 12.5% | 09:00 median 7.00 | Matchbook 7.40
    comment: Pacific Mission has finished third in her last two starts, and she is back after just 19 days, so she should arrive fit; she has also run over today's trip.
    DATA: model 9.1% | style Unknown | runs in data 7 | last 3: 16 Sep Sandown Flat 8f Good 6/10; 9 Oct Newmarket Flat 10f Good To Soft 3/14; 31 Oct Newmarket Flat 10f Good To Soft 3/9 fig 103
    DATA for: Good recent finishing positions
    DATA against: Trainer 0 wins from 18 runs, last 14 days
- Aviatrice (hrs_40745887) | 4yo F | 131lb | OR 98 | draw 6 | jockey W. J. Lee | trainer David Marnane (14d 3/6) | headgear - | last run 13 days | form 328821 | MARKET 6.7% | 09:00 median 13.00 | Matchbook 14.00
    comment: Fresh from a win last time out, and a second two starts back, Aviatrice is in good heart after just 13 days, and she has run over today's trip and going.
    DATA: model 14.7% | style Prominent (led 4% of runs) | runs in data 8 | last 3: 12 Sep Leopardstown Flat 8.3f Good 8/18; 2 Oct Dundalk Flat 7f Standard 2/5; 6 Nov Dundalk (AW) (IRE) Flat 8f Standard 1/14 fig 99
    DATA for: Trainer 50% wins (3/6), last 14 days; Has won at this trip or further; Good recent finishing positions
- American Gal (hrs_46449697) | 4yo F | 128lb | OR 100 | draw 10 | jockey Rossa Ryan | trainer Ralph Beckett (14d 0/8) | headgear - | last run 47 days | form 790082 | MARKET 6.2% | 09:00 median 13.00 | Matchbook 16.50
    comment: The risk is a 47-day break and a winless run, with nothing better than eighth in the four starts before that.
    DATA: model 4.5% | style Held up (led 8% of runs) | runs in data 6 | last 3: 7 Jul Pontefract Flat 8f Good 10/12; 13 Sep Doncaster Flat 7f Good 8/19; 3 Oct Ascot Flat 7f Good To Firm 2/12
    DATA for: Last-run finishing speed +3.4% vs that field (finished strongly)
    DATA against: Trainer 0 wins from 8 runs, last 14 days
- All Moonshine (hrs_59025358) | 4yo F | 128lb | OR 93 | draw 7 | jockey Jason Watson | trainer Andrew Balding (14d 0/18) | headgear - | last run 22 days | form -11016 | MARKET 5.0% | 09:00 median 17.00 | Matchbook 19.00
    comment: All Moonshine has won three of her last five and was successful two starts back, though she was only sixth last time out after 22 days off.
    DATA: model 3.5% | style Prominent (led 29% of runs) | runs in data 5 | last 3: 17 Jun Ascot Flat 8f Good To Firm 15/24; 18 Jul Newbury Flat 7f Good To Firm 1/6; 28 Oct Nottingham Flat 8.5f Soft 6/8 fig 96
    DATA for: Last-run finishing speed +3.2% vs that field (finished strongly); Has won at this trip or further
    DATA against: Official rating 93, 5 lb below field average; Trainer 0 wins from 18 runs, last 14 days
- Song N Dance (hrs_48169863) | 4yo F | 128lb | OR 96 | draw 8 | jockey Cieren Fallon | trainer S. P. C. Woods (14d 0/0) | headgear - | last run 55 days | form 225013 | MARKET 4.3% | 09:00 median 19.00 | Matchbook 23.00
    DATA: model 8.0% | style Held up (led 5% of runs) | runs in data 6 | last 3: 28 Jul Goodwood Flat 8f Good 10/14; 7 Sep Wolverhampton Flat 8.6f Standard 1/12; 25 Sep Newmarket Flat 8f Good 3/9
    DATA for: Has won at this trip or further; Good recent finishing positions
- Arisaig (hrs_37407930) | 5yo M | 128lb | OR 97 | draw 3 | jockey Callum Shepherd | trainer Charlie Johnston (14d 0/5) | headgear - | last run 55 days | form 248377 | MARKET 2.6% | 09:00 median 29.00 | Matchbook 40.00
    comment: The risk is a 55-day break after back-to-back sevenths, leaving her yet to win in that spell.
    DATA: model 5.7% | style Held up (led 8% of runs) | runs in data 6 | last 3: 7 Jul Pontefract Flat 8f Good 3/12; 25 Jul Ascot Flat 8f Good To Firm 7/8; 25 Sep Newmarket Flat 8f Good 7/9
- Domina Ignis (hrs_58900380) | 3yo F | 126lb | OR 97 | draw 11 | jockey David Egan | trainer Kevin Philippart de Foy (14d 1/4) | headgear - | last run 47 days | form -30070 | MARKET 2.3% | 09:00 median 34.00 | Matchbook 46.00
    DATA: model 3.4% | style Prominent (led 8% of runs) | runs in data 5 | last 3: 20 Jun Ascot Flat 7f Good To Firm 13/16; 13 Sep Doncaster Flat 7f Good 7/19; 3 Oct Ascot Flat 7f Good To Firm 10/12
    DATA against: Poor recent finishing positions
- Nandita (hrs_52742179) | 3yo F | 126lb | OR 94 | draw 1 | jockey Sean Levey | trainer John & Thady Gosden (14d 5/14) | headgear - | last run 419 days | form 17736- | MARKET 1.4% | 09:00 median 51.00 | Matchbook 90.00
    comment: Nandita is hard to fancy after 419 days off, with a sixth last time out and a seventh four starts back, and her only win came five starts back.
    DATA: model 5.6% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 36% wins (5/14), last 14 days
    DATA against: Returns from a 419-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Queen's Reign (hrs_35484512) | 5yo M | 128lb | OR 94 | draw 12 | jockey Kieran Shoemark | trainer Ed Walker (14d 1/10) | headgear p | last run 39 days | form 32-630 | MARKET 1.4% | 09:00 median 51.00 | Matchbook 100.00
    comment: Winless in her last five and unplaced last time out, Queen's Reign is hard to fancy, though a third two starts back and a second four starts back show she can get involved, and she has run over today's trip and going.
    DATA: model 2.9% | style Held up (led 8% of runs) | runs in data 1 | last 3: 11 Oct Naas Flat 8f Soft 14/16
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on

## 3:08 Lingfield (AW) | race_id rac_32304832170 | ARC All Weather Bonus Is Back Handicap Stakes
Flat | Class 6 | 7f1y | going Standard | AW | 14 runners | rating band 0-60 | age 3yo+
DATA pace: Even - Two likely leaders (King of War, Snaafy). A fair, even gallop is most likely.
- Credit Forgedd It (hrs_49143612) | 3yo G | 131lb | OR 59 | draw 3 | jockey Rossa Ryan | trainer Tony Carroll (14d 2/19) | headgear - | last run 29 days | form 623023 | MARKET 20.5% | 09:00 median 3.75 | Matchbook 4.60 | CHECK (skip line 3.56)
    comment: Creditable form with a third last time out and a second two starts back, though he is yet to win in his last six and has run over today's trip and going before.
    DATA: model 9.3% | style Midfield (led 3% of runs) | runs in data 11 | last 3: 21 Sep Leicester Flat 7f Good 11/14; 7 Oct Kempton Flat 7f Standard To Slow 2/14; 21 Oct Kempton (AW) Flat 7f Standard / Slow 3/10 fig 59
    DATA for: Best recent form figure 59, 6 lb above field average; Good recent finishing positions
- Orange Emperor (hrs_50433558) | 3yo G | 132lb | OR 60 | draw 2 | jockey Myla Coppins(5) | trainer Marco Botti (14d 0/5) | headgear - | last run 17 days | form 365235 | MARKET 14.3% | 09:00 median 5.50 | Matchbook 6.60
    comment: The risk is he's yet to win in that spell and was only fifth last time.
    DATA: model 13.4% | style Prominent (led 8% of runs) | runs in data 10 | last 3: 2 Sep Kempton Flat 7f Standard To Slow 2/6; 12 Sep Lingfield Flat 7f Standard 3/9; 2 Nov Chelmsford (AW) Flat 7f Standard 5/13 fig 66
    DATA for: Best recent form figure 66, 13 lb above field average; Recent figures 6 lb above its current mark (looks well handicapped); Last-run finishing speed +2.0% vs that field (finished strongly); Good recent finishing positions
- Cooramook (hrs_44721740) | 4yo F | 132lb | OR 59 | draw 13 | jockey Billy Loughnane | trainer Mark Loughnane (14d 1/7) | headgear b | last run 23 days | form 362204 | MARKET 9.3% | 09:00 median 8.00 | Matchbook 11.00
    DATA: model 7.8% | style Midfield (led 4% of runs) | runs in data 9 | last 3: 14 Jul Wolverhampton Flat 7.2f Standard 2/9; 30 Jul Wolverhampton Flat 7.2f Standard 10/12; 27 Oct Wolverhampton (AW) Flat 7f Standard 4/9 fig 56
- Ararat (hrs_31966298) | 6yo G | 130lb | OR 57 | draw 10 | jockey Cieren Fallon | trainer Rachel Cook & John Bridger (14d 0/0) | headgear - | last run 45 days | form 856667 | MARKET 8.1% | 09:00 median 10.00 | Matchbook 11.50
    DATA: model 5.6% | style Prominent (led 29% of runs) | runs in data 14 | last 3: 28 Aug Goodwood Flat 6f Good To Firm 6/7; 23 Sep Kempton Flat 7f Standard To Slow 6/13; 5 Oct Kempton Flat 7f Standard To Slow 7/13
    DATA against: Poor recent finishing positions
- Two And Two (hrs_59609830) | 3yo F | 130lb | OR 58 | draw 6 | jockey Marco Ghiani | trainer Simon Hodgson (14d 0/0) | headgear - | last run 21 days | form 405748 | MARKET 6.1% | 09:00 median 13.00 | Matchbook 15.50
    comment: Two And Two has finished fourth, seventh and fifth in the last six without ever getting her head in front, though she has run over today's trip and going and returns after 21 days.
    DATA: model 6.5% | style Midfield (led 3% of runs) | runs in data 9 | last 3: 5 Oct Yarmouth Flat 6f Good To Firm 7/9; 19 Oct Wolverhampton (AW) Flat 6f Standard 4/13 fig 57; 29 Oct Bath Flat 5f Soft 8/15 fig 57
- The Caribbean (hrs_35025592) | 5yo G | 131lb | OR 58 | draw 5 | jockey Kieran Shoemark | trainer Thomas Faulkner (14d 0/2) | headgear b | last run 23 days | form 307847 | MARKET 6.0% | 09:00 median 13.00 | Matchbook 15.50
    comment: The Caribbean is winless in his last six, with a seventh last time out and a fourth two starts back, though he has run over today's trip and going and returns after 23 days.
    DATA: model 7.5% | style Held up (led 3% of runs) | runs in data 6 | last 3: 25 Jul Salisbury Flat 6f Good To Firm 8/10; 13 Oct Wolverhampton Flat 6.1f Standard 4/12; 27 Oct Wolverhampton (AW) Flat 7f Standard 7/11 fig 55
    DATA against: Course: hold-up horses have won 0.7× their fair share at 7f here
- Snaafy (hrs_53602017) | 3yo G | 130lb | OR 58 | draw 4 | jockey Callum Shepherd | trainer David Loughnane (14d 1/2) | headgear tp | last run 17 days | form 598330 | MARKET 6.0% | 09:00 median 13.00 | Matchbook 16.00
    comment: Snaafy is winless in his last six and unplaced last time out, which makes him hard to fancy, though a third two starts back and another three starts back show he can get involved.
    DATA: model 7.5% | style Leader (led 43% of runs) | runs in data 10 | last 3: 6 Oct Leicester Flat 7f Good To Firm 3/10; 23 Oct Wolverhampton (AW) Flat 8.5f Standard 3/10 fig 57; 2 Nov Wolverhampton (AW) Flat 9.5f Standard 10/12 fig 45
    DATA for: Good recent finishing positions
    DATA against: Last-run finishing speed -2.7% vs that field (faded)
- King of War (hrs_25443495) | 7yo G | 133lb | OR 60 | draw 9 | jockey David Egan | trainer Michael Wigham (14d 0/1) | headgear tb | last run 35 days | form 308400 | MARKET 5.8% | 09:00 median 13.00 | Matchbook 17.00
    DATA: model 6.0% | style Leader (led 79% of runs) | runs in data 9 | last 3: 23 Aug Brighton Flat 7f Good To Firm 4/7; 23 Sep Redcar Flat 7f Good 11/12; 15 Oct Brighton Flat 8f Good 12/14 fig 44
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 44, 9 lb below field average; Recent figures 16 lb below its current mark (looks high in the weights); Last-run finishing speed -3.2% vs that field (faded)
- Back At One (hrs_65068941) | 3yo G | 132lb | OR 60 | draw 11 | jockey Rhys Clutterbuck | trainer Jamie Moore & Josh Moore (14d 1/24) | headgear - | last run 52 days | form 76554 | MARKET 5.6% | 09:00 median 12.50 | Matchbook 19.50
    comment: Back At One is winless in his last five, though he has crept up to a fourth last time out after a run of fifth, fifth, sixth and seventh finishes, and he has run over today's trip and going. Fifty-two days off and a stable out of form (1/24) make him hard to fancy from stall 11.
    DATA: model 12.6% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 26 Jun Newcastle Flat 7.1f Standard To Slow 5/11; 27 Jul Southwell Flat 8.1f Standard 5/13; 28 Sep Wolverhampton Flat 9.5f Standard 4/11
- King of York (hrs_24665193) | 7yo G | 133lb | OR 60 | draw 14 | jockey Kieran O'Neill | trainer Scott Dixon (14d 0/1) | headgear p | last run 33 days | form 508967 | MARKET 4.4% | 09:00 median 17.00 | Matchbook 25.00
    comment: King of York has been well beaten lately, with a seventh last time out and a sixth two starts back, but he has run over today's trip and on this going, and 33 days off gives him a fresh edge.
    DATA: model 3.3% | style Midfield (led 3% of runs) | runs in data 11 | last 3: 24 Sep Southwell Flat 7.1f Standard 9/9; 8 Oct Southwell Flat 8.1f Standard 6/12; 17 Oct Southwell (AW) Flat 7f Standard 7/9 fig 54
    DATA for: Has won at this trip or further
    DATA against: Recent figures 6 lb below its current mark (looks high in the weights); Poor recent finishing positions
- My Boy Harry (hrs_45568460) | 4yo G | 133lb | OR 60 | draw 7 | jockey Luke Morris | trainer Hayley Burton (14d 0/1) | headgear b | last run 30 days | form 133449 | MARKET 4.3% | 09:00 median 17.00 | Matchbook 24.00
    comment: My Boy Harry has been consistent, with a fourth two starts back, another fourth three starts back, and a third before that, and he has run over today's trip and going.
    DATA: model 5.3% | style Held up (led 3% of runs) | runs in data 16 | last 3: 25 Jun Nottingham Flat 8.3f Good To Firm 4/8; 30 Jun Brighton Flat 8f Good To Firm 4/7; 20 Oct Yarmouth Flat 6f Soft 9/9 fig 32
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 32, 21 lb below field average; Recent figures 28 lb below its current mark (looks high in the weights); Course: hold-up horses have won 0.7× their fair share at 7f here
- Bomb Squad (hrs_21673918) | 8yo G | 133lb | OR 60 | draw 1 | jockey Finley Marsh | trainer John Mackie (14d 0/4) | headgear p | last run 20 days | form 213667 | MARKET 3.7% | 09:00 median 21.00 | Matchbook 26.00
    comment: Bomb Squad has slipped to a seventh last time out, with a sixth two starts back and another sixth three starts back, so he's hard to fancy now despite a win five starts back.
    DATA: model 4.1% | style Prominent (led 3% of runs) | runs in data 12 | last 3: 28 Jun Wolverhampton Flat 7.2f Standard 6/9; 21 Sep Wolverhampton Flat 6.1f Standard 6/10; 30 Oct Newcastle (AW) Flat 7f Standard 7/11 fig 54
    DATA for: Has won at this trip or further
    DATA against: Recent figures 6 lb below its current mark (looks high in the weights); Poor recent finishing positions; Aged 8, older than most of this field
- Neptune Legend (hrs_24907848) | 7yo G | 130lb | OR 57 | draw 8 | jockey Jack Doughty | trainer Tony Carroll (14d 2/19) | headgear - | last run 21 days | form 600590 | MARKET 3.2% | 09:00 median 21.00 | Matchbook 36.00
    comment: Winless in his last six, Neptune Legend was unplaced last time out and has managed only a fifth three starts back, though he has run over today's trip and going and returns after 21 days.
    DATA: model 3.6% | style Held up (led 5% of runs) | runs in data 16 | last 3: 21 Sep Leicester Flat 6f Good 5/12; 13 Oct Wolverhampton Flat 6.1f Standard 9/12; 29 Oct Bath Flat 5f Soft 12/15 fig 51
    DATA against: Recent figures 6 lb below its current mark (looks high in the weights); Course: hold-up horses have won 0.7× their fair share at 7f here
- Berning Hot (hrs_412693148) | 4yo F | 130lb | OR 57 | draw 12 | jockey William Carson | trainer Michael Attwater (14d 0/2) | headgear - | last run 35 days | form 051250 | MARKET 2.6% | 09:00 median 29.00 | Matchbook 44.00
    comment: Berning Hot was unplaced last time out and a fifth two starts back, so the recent trend is the wrong way, though she did win four starts back and has run over today's trip and going.
    DATA: model 7.4% | style Held up (led 3% of runs) | runs in data 12 | last 3: 12 Sep Lingfield Flat 8f Standard 2/8; 6 Oct Brighton Flat 7f Good To Firm 5/10; 15 Oct Brighton Flat 7f Good 13/13
    DATA for: Has won at this trip or further
    DATA against: Last-run finishing speed -9.3% vs that field (faded); Course: hold-up horses have won 0.7× their fair share at 7f here

## 3:40 Lingfield (AW) | race_id rac_32304834107 | Midnite Built Different Handicap Stakes
Flat | Class 5 | 5f6y | going Standard | AW | 8 runners | rating band 0-70 | age 3yo+
DATA pace: Even - Two likely leaders (Level Up, Roman Spring). A fair, even gallop is most likely.
- Got The Booty (hrs_56219429) | 3yo F | 135lb | OR 70 | draw 4 | jockey Rossa Ryan | trainer Clive Cox (14d 1/6) | headgear p (1st time) | last run 31 days | form 439522 | MARKET 24.5% | 09:00 median 3.50 | Matchbook 3.35 | CHECK (skip line 3.32)
    comment: Got The Booty arrives in fine heart, runner-up in each of her last two outings, and she has run over today's trip and going before.
    DATA: model 19.6% | style Prominent (led 4% of runs) | runs in data 7 | last 3: 2 Sep Kempton Flat 6f Standard To Slow 5/7; 24 Sep Southwell Flat 5f Standard 2/7; 19 Oct Wolverhampton (AW) Flat 5f Standard 2/6 fig 66
    DATA for: Good recent finishing positions; First-time headgear
- Nogo's Dream (hrs_29227191) | 6yo G | 135lb | OR 70 | draw 2 | jockey Finley Marsh | trainer Richard Hughes (14d 0/9) | headgear p | last run 21 days | form 426425 | MARKET 24.4% | 09:00 median 3.20 | Matchbook 3.05
    comment: Nogo's Dream is yet to win in his last six, but two seconds in that spell, the latest two starts back, show he is competitive, and he has run over today's trip and going.
    DATA: model 12.0% | style Midfield (led 23% of runs) | runs in data 12 | last 3: 8 Sep Goodwood Flat 5f Soft 4/6; 28 Sep Wolverhampton Flat 5.1f Standard 2/8; 29 Oct Bath Flat 5.5f Soft 5/12 fig 74
    DATA for: Best recent form figure 74, 9 lb above field average; Recent figures 4 lb above its current mark (looks well handicapped)
    DATA against: Trainer 0 wins from 9 runs, last 14 days
- Solar Invincible (hrs_55882330) | 3yo G | 132lb | OR 67 | draw 3 | jockey Billy Loughnane | trainer Roger Teal (14d 0/3) | headgear p | last run 28 days | form 542203 | MARKET 13.8% | 09:00 median 5.50 | Matchbook 5.20
    comment: Solar Invincible was third last time out and has been a second, two starts before that, so he has placed at times without a win in his last six; he has run over today's trip and going, and returns after 28 days.
    DATA: model 10.2% | style Prominent (led 5% of runs) | runs in data 9 | last 3: 27 Jul Windsor Flat 6.1f Good To Firm 2/6; 13 Aug Windsor Flat 6.1f Good To Firm 11/11; 22 Oct Newmarket Flat 5f Soft 3/7 fig 68
    DATA for: Has won at this trip or further; Good recent finishing positions
- Cayman Tai (hrs_39191495) | 4yo G | 134lb | OR 69 | draw 9 | jockey Ben Pollard(7) | trainer Richard Hannon (14d 0/4) | headgear - | last run 27 days | form 848315 | MARKET 11.5% | 09:00 median 7.70 | Matchbook 4.30
    DATA: model 16.9% | style Midfield (led 4% of runs) | runs in data 21 | last 3: 24 Sep Southwell Flat 5f Standard 3/7; 6 Oct Brighton Flat 5.3f Good To Firm 1/9; 23 Oct Wolverhampton (AW) Flat 6f Standard 5/7 fig 62
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Recent figures 7 lb below its current mark (looks high in the weights)
- Magna (hrs_43385363) | 4yo F | 132lb | OR 67 | draw 1 | jockey William Carson | trainer Tony Carroll (14d 2/19) | headgear - | last run 29 days | form 137463 | MARKET 7.4% | 09:00 median 10.00 | Matchbook 10.00
    comment: Third last time out and 29 days fresh, Magna has run over today's trip and on this going, but she's one win in her last six, a sixth and a seventh in that spell, and carries 132 lb from stall 1.
    DATA: model 13.6% | style Midfield (led 4% of runs) | runs in data 12 | last 3: 27 Jul Windsor Flat 5.1f Good To Firm 4/11; 31 Aug Chepstow Flat 5.1f Good To Soft 6/7; 21 Oct Kempton (AW) Flat 6f Standard / Slow 3/11 fig 66
    DATA for: Has won at this trip or further
- Shalaa Asker (hrs_22241317) | 8yo G | 129lb | OR 64 | draw 5 | jockey David Egan | trainer Charlie Wallis (14d 0/0) | headgear tp | last run 17 days | form 266142 | MARKET 6.9% | 09:00 median 12.00 | Matchbook 7.20
    comment: Shalaa Asker arrives in good heart, second last time out and a fourth two starts back, with a winner three starts back, and he has run over today's trip and going.
    DATA: model 12.2% | style Prominent (led 4% of runs) | runs in data 12 | last 3: 4 Jun Lingfield Flat 5f Standard 1/7; 28 Jun Wolverhampton Flat 5.1f Standard 4/5; 2 Nov Chelmsford (AW) Flat 5f Standard 2/7 fig 64
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Aged 8, older than most of this field
- Roman Spring (hrs_31069234) | 6yo G | 120lb | OR 55 | draw 8 | jockey Kieran O'Neill | trainer Rachel Cook & John Bridger (14d 0/0) | headgear t | last run 21 days | form 211615 | MARKET 5.8% | 09:00 median 14.00 | Matchbook 12.50
    comment: Roman Spring has won three of his last six, including a win two starts back, but he was only fifth last time out and a sixth three starts back shows the inconsistency.
    DATA: model 9.2% | style Prominent (led 43% of runs) | runs in data 15 | last 3: 6 Oct Brighton Flat 5.3f Good To Firm 6/9; 15 Oct Brighton Flat 6f Good 1/9 fig 58; 29 Oct Bath Flat 5.5f Soft 5/16 fig 57
    DATA for: Has won at this trip or further; Carries 11 lb less than average
    DATA against: Best recent form figure 58, 7 lb below field average; Official rating 55, 11 lb below field average
- Level Up (hrs_25810869) | 7yo G | 132lb | OR 67 | draw 6 | jockey Kieran Shoemark | trainer David Evans (14d 0/4) | headgear - | last run 22 days | form 718638 | MARKET 5.7% | 09:00 median 16.00 | Matchbook 6.80
    DATA: model 6.4% | style Leader (led 38% of runs) | runs in data 20 | last 3: 29 Sep Bath Flat 5.7f Good To Firm 6/9; 19 Oct Bath Flat 5f Good To Soft 3/8 fig 65; 28 Oct Nottingham Flat 5f Soft 8/9 fig 44
    DATA for: Has won at this trip or further
