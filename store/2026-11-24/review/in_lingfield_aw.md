# Card review packet: Lingfield (AW), 2026-11-24

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


## 11:38 Lingfield (AW) | race_id rac_32305372593 | Midnite Ain't Your Grandad's Bookie Handicap Stakes
Flat | Class 5 | 1m7f170y | going Standard | AW | 7 runners | rating band 0-75 | age 3yo+
DATA pace: Lone leader - Percy Jones is the only habitual front-runner and may be allowed an easy lead.
- Neswick (hrs_64073107) | 3yo F | 135lb | OR 73 | draw 6 | jockey Marco Ghiani | trainer Marcus Tregoning (14d 2/3) | headgear v | last run 45 days | form 34331 | MARKET 36.5% | 09:00 median 2.38 | Matchbook 2.60
    comment: Neswick arrives a last-time-out winner, having finished third in two of the starts before that, and she has run on today's going before.
    DATA: model 17.8% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 27 Aug Ffos Las Flat 11.9f Good 3/5; 26 Sep Ripon Flat 12f Good 3/9; 10 Oct Southwell Flat 14.1f Standard 1/7
    DATA for: Good recent finishing positions
- Kashooda (hrs_65322376) | 3yo F | 132lb | OR 70 | draw 8 | jockey Jason Watson | trainer Andrew Balding (14d 2/27) | headgear - | last run 26 days | form 3234 | MARKET 18.1% | 09:00 median 4.50 | Matchbook 5.70
    comment: Kashooda is consistent, finishing fourth last time out, a third two starts back, a second three starts back and a third four starts back, and she has run on today's going before.
    DATA: model 20.3% | style Midfield (led 3% of runs) | runs in data 4 | last 3: 8 Jul Kempton Flat 11f Standard To Slow 2/12; 26 Sep Southwell Flat 11.1f Standard 3/13; 29 Oct Southwell (AW) Flat 11f Standard 4/7 fig 67
    DATA for: Good recent finishing positions
- Fiefdom (hrs_64780695) | 3yo G | 133lb | OR 71 | draw 7 | jockey David Egan | trainer S. P. C. Woods (14d 1/7) | headgear - | last run 22 days | form 540441 | MARKET 15.1% | 09:00 median 6.00 | Matchbook 6.20
    comment: The main risk is a 133 lb burden that leaves him little room for error after a run of fourths before that success.
    DATA: model 15.3% | style Midfield (led 4% of runs) | runs in data 7 | last 3: 3 Sep Southwell Flat 12.1f Standard 4/7; 21 Sep Wolverhampton Flat 16.5f Standard 4/5; 2 Nov Wolverhampton (AW) Flat 14f Standard 1/9 fig 72
    DATA for: Best recent form figure 72, 4 lb above field average; Last-run finishing speed +3.5% vs that field (finished strongly)
- Division Day (hrs_53808902) | 4yo G | 139lb | OR 71 | draw 1 | jockey Robert Havlin | trainer Lydia Richards (14d 0/0) | headgear - | last run 44 days | form -15131 | MARKET 11.1% | 09:00 median 8.00 | Matchbook 8.60
    comment: Division Day has won three of his last five, including last time out, and has run over today's trip and going, but a 44-day break and 139 lb look a lot to carry.
    DATA: model 20.5% | style Prominent (led 23% of runs) | runs in data 8 | last 3: 5 Aug Pontefract Flat 17.1f Good To Firm 1/3; 4 Sep Kempton Flat 16f Standard To Slow 3/8; 11 Oct Goodwood Flat 16f Good To Soft 1/12
    DATA for: Has won at this trip or further; Good recent finishing positions; Course: prominent racers have won 1.3× their fair share at 16f here
- Youthful King (hrs_26299189) | 7yo G | 140lb | OR 72 | draw 5 | jockey Jack Dace(5) | trainer Luke Dace (14d 0/6) | headgear h | last run 6 days | form 644076 | MARKET 7.2% | 09:00 median 12.00 | Matchbook 13.50
    DATA: model 6.4% | style Midfield (led 4% of runs) | runs in data 8 | last 3: 14 Oct Kempton (AW) Flat 11f Standard / Slow 11/13 fig 61; 28 Oct Kempton (AW) Flat 12f Standard / Slow 7/10 fig 67; 18 Nov Kempton (AW) Flat 12f Standard / Slow 6/13 fig 68
    DATA against: Poor recent finishing positions; Carries 5 lb more than average; Aged 7, older than most of this field
- Fair Dinkum (hrs_33096602) | 6yo G | 130lb | OR 62 | draw 3 | jockey Taryn Langley(5) | trainer Jeremy Scott (14d 0/11) | headgear tp | last run 20 days | form 434542 | MARKET 6.7% | 09:00 median 12.50 | Matchbook 15.00
    comment: Fair Dinkum is winless in his last six, though a second last time out, 20 days ago, is a step forward, and he has run over today's trip and going.
    DATA: model 8.2% | style Held up (led 5% of runs) | runs in data 9 | last 3: 13 Sep Bath Flat 14f Good To Soft 5/12; 11 Oct Goodwood Flat 16f Good To Soft 4/12; 4 Nov Kempton (AW) Flat 12f Standard / Slow 2/14 fig 64
    DATA for: Last-run finishing speed +3.9% vs that field (finished strongly)
    DATA against: Best recent form figure 64, 4 lb below field average; Official rating 62, 7 lb below field average; Trainer 0 wins from 11 runs, last 14 days
- Percy Jones (hrs_26849354) | 7yo G | 135lb | OR 67 | draw 4 | jockey Charles Bishop | trainer Mark Loughnane (14d 2/15) | headgear /bes (1st time) | last run 22 days | form 423363 | MARKET 5.3% | 09:00 median 15.00 | Matchbook 19.50
    comment: Percy Jones is a consistent sort, third last time out and a third four starts back, with a second five runs ago, and he has run over today's trip and going at 22 days fresh. Yet to win in his last six, though, so finding that final bit remains the one big question.
    DATA: model 11.5% | style Leader (led 29% of runs) | runs in data 10 | last 3: 29 Sep Bath Flat 13.1f Good To Firm 3/13; 13 Oct Wolverhampton Flat 14f Standard 6/7; 2 Nov Wolverhampton (AW) Flat 14f Standard 3/9 fig 69
    DATA for: Last-run finishing speed +2.7% vs that field (finished strongly); Good recent finishing positions; First-time headgear; Pace: may get an uncontested lead
    DATA against: Aged 7, older than most of this field

## 12:08 Lingfield (AW) | race_id rac_32305374530 | AWC Season 14 Has Begun Nursery Handicap Stakes
Flat | Class 6 | 6f1y | going Standard | AW | 11 runners | rating band 0-65 | age 2yo
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Pride's Queen (hrs_64968029) | 2yo F | 127lb | OR 57 | draw 11 | jockey Marco Ghiani | trainer Marco Botti (14d 0/9) | headgear - | last run 19 days | form 80532 | MARKET 18.6% | 09:00 median 4.33 | Matchbook 5.00 | CHECK (skip line 4.11)
    comment: Pride's Queen arrives in decent heart after a second last time out and a third two starts back, and she has run over today's trip and on this going, but she's yet to win in her last five starts.
    DATA: model 13.0% | style Prominent (led 29% of runs) | runs in data 5 | last 3: 21 Jul Wolverhampton Flat 7.2f Standard 5/9; 19 Oct Wolverhampton (AW) Flat 7f Standard 3/12 fig 57; 5 Nov Southwell (AW) Flat 6f Standard 2/13 fig 64
    DATA for: Best recent form figure 64, 6 lb above field average; Recent figures 7 lb above its current mark (looks well handicapped); Good recent finishing positions
    DATA against: Trainer 0 wins from 9 runs, last 14 days
- Rocsane (hrs_64590750) | 2yo F | 134lb | OR 64 | draw 5 | jockey David Egan | trainer George Margarson (14d 0/0) | headgear - | last run 22 days | form 322374 | MARKET 17.8% | 09:00 median 4.33 | Matchbook 5.50
    comment: The main risk is that she remains winless in that spell, carrying 134 lb from draw 5.
    DATA: model 18.9% | style Midfield (led 23% of runs) | runs in data 7 | last 3: 30 Aug Yarmouth Flat 7f Good To Soft 3/10; 21 Sep Leicester Flat 6f Good 7/14; 2 Nov Chelmsford (AW) Flat 6f Standard 4/12 fig 58
    DATA against: Recent figures 6 lb below its current mark (looks high in the weights)
- Seathegulls (hrs_60819514) | 2yo G | 135lb | OR 65 | draw 4 | jockey Callum Shepherd | trainer Jamie Moore & Josh Moore (14d 3/27) | headgear tp | last run 115 days | form 74506 | MARKET 14.7% | 09:00 median 6.00 | Matchbook 5.90
    DATA: model 7.2% | style Prominent (led 4% of runs) | runs in data 5 | last 3: 27 Jun Windsor Flat 5.1f Good To Firm 5/8; 18 Jul Newbury Flat 5.2f Good To Firm 10/24; 1 Aug Lingfield Flat 6f Good To Firm 6/7
    DATA against: Returns from a 115-day break
- Hemustbeanangel (hrs_66198888) | 2yo G | 132lb | OR 62 | draw 12 | jockey Jason Watson | trainer Roger Teal (14d 0/7) | headgear - | last run 56 days | form 93366 | MARKET 12.1% | 09:00 median 6.50 | Matchbook 8.00
    comment: Winless in his last five, Hemustbeanangel has finished sixth in each of his last two and returns after 56 days off, which makes him hard to fancy. A pair of thirds three and four starts back and prior experience over today's trip offer some hope, but he carries 132 lb from stall 12.
    DATA: model 15.0% | style Midfield (led 4% of runs) | runs in data 5 | last 3: 17 Aug Windsor Flat 6.1f Good To Firm 3/11; 8 Sep Leicester Flat 7f Good To Soft 6/10; 29 Sep Bath Flat 5.7f Good To Firm 6/11
- True Charm (hrs_64968008) | 2yo G | 135lb | OR 65 | draw 1 | jockey Sean Levey | trainer Lemos De Souza (14d 0/4) | headgear ht | last run 55 days | form 20580 | MARKET 9.7% | 09:00 median 7.75 | Matchbook 10.50
    comment: True Charm has been unplaced last time out, and a fifth three starts back is the best of his recent efforts bar a second five runs ago, so he's yet to win in his last five starts. He has run over today's trip and returns after 55 days, but 135 lb from stall one asks plenty of him.
    DATA: model 7.5% | style Unknown | runs in data 5 | last 3: 10 Jul Chester Flat 6.1f Good 5/12; 28 Aug Sandown Flat 5f Good 8/8; 30 Sep Kempton Flat 7f Standard To Slow 10/13
- Lilywhite Hart (hrs_65938600) | 2yo F | 134lb | OR 64 | draw 3 | jockey John Egan | trainer Dean Ivory (14d 0/0) | headgear p (1st time) | last run 26 days | form 556363 | MARKET 7.7% | 09:00 median 11.00 | Matchbook 12.00
    comment: The one concern is that she's yet to win in her last six starts, with a sixth two runs back showing her inconsistency.
    DATA: model 8.0% | style Held up (led 5% of runs) | runs in data 7 | last 3: 15 Sep Yarmouth Flat 7f Good To Soft 3/8; 9 Oct Kempton Flat 6f Standard To Slow 6/8; 29 Oct Southwell (AW) Flat 7f Standard 3/13 fig 64
    DATA for: Best recent form figure 64, 6 lb above field average; Good recent finishing positions; First-time headgear
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Percy Shaw (hrs_64937978) | 2yo G | 132lb | OR 62 | draw 7 | jockey Jack Dace(5) | trainer Charles Hills (14d 0/2) | headgear - | last run 131 days | form 849 | MARKET 6.2% | 09:00 median 12.50 | Matchbook 16.00
    comment: Percy Shaw is winless in his last three, finishing ninth last time out, with a fourth two starts back the pick of it, and a 131-day layoff leaves fitness a question.
    DATA: model 3.3% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 11 Jun Newbury Flat 6.5f Good To Soft 8/9; 29 Jun Ffos Las Flat 6f Good 4/7; 16 Jul Chepstow Flat 5.1f Good To Firm 9/9
    DATA against: Returns from a 131-day break
- Lushill (hrs_65938586) | 2yo F | 129lb | OR 59 | draw 8 | jockey Edward Greatrex | trainer J. S. Moore (14d 0/9) | headgear t | last run 36 days | form 238463 | MARKET 5.0% | 09:00 median 15.00 | Matchbook 21.00
    comment: Lushill is winless in her last six, though a third last time out and a second six starts back show she is not without ability; she has run over today's trip and on this going.
    DATA: model 10.0% | style Held up (led 3% of runs) | runs in data 8 | last 3: 26 Aug Newbury Flat 7f Good To Firm 4/14; 11 Sep Salisbury Flat 7f Soft 6/9; 19 Oct Wolverhampton (AW) Flat 7f Standard 3/10 fig 58
    DATA against: Trainer 0 wins from 9 runs, last 14 days; Pace: steady gallop likely, hard to come from off the pace
- Alpha Legend (hrs_64072225) | 2yo G | 121lb | OR 51 | draw 2 | jockey Jack Callan | trainer Marco Botti (14d 0/9) | headgear hb | last run 40 days | form 887074 | MARKET 3.9% | 09:00 median 19.00 | Matchbook 29.00
    comment: Winless in his last six, Alpha Legend has finished eighth, eighth, seventh and seventh in that spell, though a fourth last time out is a step up, and he has run over today's trip and going before.
    DATA: model 4.0% | style Prominent (led 29% of runs) | runs in data 6 | last 3: 7 Sep Windsor Flat 6.1f Good 10/14; 21 Sep Wolverhampton Flat 5.1f Standard 7/9; 15 Oct Southwell (AW) Flat 5f Standard 4/12 fig 51
    DATA for: Carries 10 lb less than average
    DATA against: Best recent form figure 51, 7 lb below field average; Official rating 51, 10 lb below field average; Trainer 0 wins from 9 runs, last 14 days
- Postremo (hrs_64294958) | 2yo G | 134lb | OR 64 | draw 6 | jockey Millie Wonnacott(5) | trainer J. S. Moore (14d 0/9) | headgear - | last run 101 days | form 653 | MARKET 3.1% | 09:00 median 26.00 | Matchbook 32.00
    comment: Postremo is hard to fancy, winless in his last three and returning after 101 days off, though a third last time out, and prior experience over today's trip and going, give him something to work with.
    DATA: model 6.1% | style Midfield (led 5% of runs) | runs in data 3 | last 3: 4 May Bath Flat 5f Good 6/10; 30 Jul Wolverhampton Flat 6.1f Standard 5/10; 15 Aug Lingfield Flat 6f Standard 3/10
    DATA against: Trainer 0 wins from 9 runs, last 14 days; Returns from a 101-day break
- Havana Grey Star (hrs_64488095) | 2yo F | 131lb | OR 61 | draw 9 | jockey Charles Bishop | trainer Mark Loughnane (14d 2/15) | headgear - | last run 22 days | form 45847 | MARKET 1.4% | 09:00 median 51.00 | Matchbook 85.00
    comment: Winless in her last five, Havana Grey Star was seventh last time out, though she was fourth two starts back, and she has run over today's trip and going before, returning after 22 days.
    DATA: model 7.1% | style Held up (led 5% of runs) | runs in data 5 | last 3: 12 Jun Sandown Flat 5f Good 8/9; 2 Jul Nottingham Flat 6.1f Good To Firm 4/8; 2 Nov Wolverhampton (AW) Flat 5f Standard 7/11 fig 53
    DATA against: Best recent form figure 53, 5 lb below field average; Recent figures 8 lb below its current mark (looks high in the weights); Pace: steady gallop likely, hard to come from off the pace

## 12:38 Lingfield (AW) | race_id rac_32305376467 | AWC Finals Day At Newcastle 26th March EBF Maiden Stakes (GBB Race)
Flat | Class 4 | 6f1y | going Standard | AW | 11 runners | rating band - | age 2yo
DATA pace: Unclear - Running styles known for only 4 of 11 runners.
- Green Spain (hrs_17390993165) | 2yo F | 128lb | OR - | draw 8 | jockey Jason Watson | trainer James Tate (14d 0/4) | headgear - | last run 103 days | form 9 | MARKET 29.8% | 09:00 median 2.63 | Matchbook 3.10
    DATA: model 8.3% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 103-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Uomo Valeroso (hrs_17389284731) | 2yo C | 133lb | OR - | draw 4 | jockey Harry Davies | trainer Clive Cox (14d 0/5) | headgear - | last run 41 days | form 4 | MARKET 24.0% | 09:00 median 3.40 | Matchbook 3.90
    DATA: model 14.6% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 14 Oct Kempton (AW) Flat 6f Standard / Slow 4/8 fig 58
    DATA for: Best recent form figure 58, 18 lb above field average
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Yellow Mission (hrs_60819409) | 2yo C | 133lb | OR - | draw 11 | jockey Edward Greatrex | trainer Richard Hughes (14d 1/11) | headgear - | last run 21 days | form 55 | MARKET 13.1% | 09:00 median 6.50 | Matchbook 7.00
    DATA: model 10.3% | style Held up (led 5% of runs) | runs in data 2 | last 3: 21 Jul Salisbury Flat 6f Good To Firm 5/5; 3 Nov Wolverhampton (AW) Flat 7f Standard 5/11 fig 40
    DATA for: Last-run finishing speed +3.1% vs that field (finished strongly)
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Gilded Outlaw (hrs_17395926555) | 2yo G | 133lb | OR - | draw 10 | jockey Jack Callan | trainer George Boughey (14d 6/20) | headgear - | last run - days | form - | MARKET 11.9% | 09:00 median 7.00 | Matchbook 7.60
    DATA: model 8.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 30% wins (6/20), last 14 days
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Sand On The Run (hrs_17395928641) | 2yo F | 128lb | OR - | draw 3 | jockey David Egan | trainer Jane Chapple-Hyam (14d 1/3) | headgear - | last run - days | form - | MARKET 5.9% | 09:00 median 13.00 | Matchbook 17.00
    DATA: model 8.3% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Rhythm Runner (hrs_17395026446) | 2yo F | 128lb | OR - | draw 2 | jockey Marco Ghiani | trainer Ollie Sangster (14d 1/9) | headgear - | last run - days | form - | MARKET 4.5% | 09:00 median 17.00 | Matchbook 23.00
    DATA: model 8.3% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Nia Miss (hrs_17389269086) | 2yo F | 128lb | OR - | draw 9 | jockey Robert Havlin | trainer Conrad Allen (14d 0/2) | headgear - | last run - days | form - | MARKET 4.2% | 09:00 median 19.00 | Matchbook 24.00
    DATA: model 8.3% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Stepney Blue (hrs_17395872319) | 2yo F | 128lb | OR - | draw 1 | jockey Callum Shepherd | trainer George Baker (14d 1/5) | headgear t (1st time) | last run - days | form - | MARKET 3.4% | 09:00 median 21.00 | Matchbook 34.00
    DATA: model 8.3% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 20% wins (1/5), last 14 days; First-time headgear
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Al Mhalhel (hrs_17393056219) | 2yo C | 133lb | OR - | draw 5 | jockey Stevie Donohoe | trainer Ollie Sangster (14d 1/9) | headgear t (1st time) | last run 17 days | form 56 | MARKET 1.3% | 09:00 median 69.00 | Matchbook 130.00
    DATA: model 6.1% | style Held up (led 5% of runs) | runs in data 2 | last 3: 26 Oct Leicester Flat 6f Soft 5/7 fig 17; 7 Nov Doncaster Flat 6f Good To Soft 6/6 fig 14
    DATA for: First-time headgear
    DATA against: Best recent form figure 17, 23 lb below field average; Lightly raced: 2 runs in our data, so the model has little to go on
- My Boy Ronnie (hrs_65916816) | 2yo G | 133lb | OR - | draw 7 | jockey Kieren Fox | trainer Simon Pearce (14d 1/2) | headgear - | last run - days | form - | MARKET 1.1% | 09:00 median 67.00 | Matchbook 180.00
    DATA: model 8.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Mystical Magical (hrs_63323680) | 2yo F | 128lb | OR - | draw 6 | jockey Charles Bishop | trainer Adam Kirby (14d 1/6) | headgear - | last run 8 days | form 90 | MARKET 0.8% | 09:00 median 101.00 | Matchbook 240.00
    DATA: model 11.0% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 5 Apr Bath Flat 5f Good 9/10; 16 Nov Wolverhampton (AW) Flat 6f Standard 11/13 fig 46
    DATA for: Best recent form figure 46, 6 lb above field average
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on

## 1:08 Lingfield (AW) | race_id rac_32305378404 | All-Weather Championship Is Back Nursery Handicap Stakes
Flat | Class 6 | 5f6y | going Standard | AW | 10 runners | rating band 0-65 | age 2yo
DATA pace: Lone leader - Defiant Dream is the only habitual front-runner and may be allowed an easy lead.
- C'Est Lui (hrs_64135001) | 2yo G | 128lb | OR 55 | draw 1 | jockey Sean Levey | trainer Dylan Cunha (14d 1/9) | headgear - | last run 40 days | form 674753 | MARKET 20.5% | 09:00 median 4.00 | Matchbook 4.70 | CHECK (skip line 3.80)
    comment: C'Est Lui bounced back with a third last time out after a run of mid-division efforts, and he has experience of today's trip and going, but he's yet to win in his last six starts and returns after 40 days off.
    DATA: model 12.5% | style Prominent (led 5% of runs) | runs in data 6 | last 3: 29 Aug Windsor Flat 6.1f Soft 7/11; 21 Sep Wolverhampton Flat 5.1f Standard 5/9; 15 Oct Southwell (AW) Flat 5f Standard 3/12 fig 57
    DATA for: Best recent form figure 57, 6 lb above field average
- Last Dandelion (hrs_64135022) | 2yo F | 135lb | OR 62 | draw 7 | jockey Jack Dace(5) | trainer Stuart Williams (14d 0/4) | headgear - | last run 22 days | form 320144 | MARKET 16.4% | 09:00 median 5.00 | Matchbook 5.90
    comment: Last Dandelion arrives fit after 22 days off, a fourth last time out and another fourth two starts back, with a winner three starts back, and she has run over today's trip and going before.
    DATA: model 18.7% | style Prominent (led 29% of runs) | runs in data 12 | last 3: 29 Sep Bath Flat 5.7f Good To Firm 1/11; 23 Oct Wolverhampton (AW) Flat 6f Standard 4/13 fig 67; 2 Nov Chelmsford (AW) Flat 6f Standard 4/9 fig 59
    DATA for: Best recent form figure 67, 16 lb above field average; Recent figures 5 lb above its current mark (looks well handicapped); Official rating 62, 8 lb above field average; Has won at this trip or further
    DATA against: Carries 6 lb more than average
- Past Passion (hrs_60821201) | 2yo F | 134lb | OR 61 | draw 8 | jockey Olivia Tubb(5) | trainer Jonathan Portman (14d 2/10) | headgear - | last run 22 days | form 204346 | MARKET 13.8% | 09:00 median 6.00 | Matchbook 7.00
    comment: Past Passion has been consistent without a win, with a third three starts back and a second six starts back, and she has run over today's trip and going before.
    DATA: model 25.2% | style Prominent (led 29% of runs) | runs in data 9 | last 3: 7 Sep Windsor Flat 6.1f Good 3/14; 29 Sep Bath Flat 5.7f Good To Firm 4/11; 2 Nov Wolverhampton (AW) Flat 5f Standard 6/11 fig 55
    DATA for: Official rating 61, 7 lb above field average; Trainer 20% wins (2/10), last 14 days
    DATA against: Recent figures 6 lb below its current mark (looks high in the weights); Carries 5 lb more than average
- Defiant Dream (hrs_65322355) | 2yo F | 127lb | OR 54 | draw 6 | jockey Tyler Heard | trainer Mark Usher (14d 0/4) | headgear p | last run 27 days | form 650442 | MARKET 13.3% | 09:00 median 6.00 | Matchbook 7.20
    comment: Defiant Dream was second last time out, but she is winless in her last six, with a fourth two starts back and another fourth three starts back, and that makes her hard to fancy.
    DATA: model 9.4% | style Leader (led 38% of runs) | runs in data 8 | last 3: 27 Sep Ffos Las Flat 5f Soft 4/8; 5 Oct Wolverhampton Flat 5.1f Standard 4/10; 28 Oct Nottingham Flat 5f Soft 2/7 fig 57
    DATA for: Best recent form figure 57, 6 lb above field average; Pace: may get an uncontested lead
- Naval Cop (hrs_62169464) | 2yo F | 135lb | OR 62 | draw 3 | jockey Marco Ghiani | trainer Dylan Cunha (14d 1/9) | headgear - | last run 40 days | form 651370 | MARKET 11.2% | 09:00 median 8.00 | Matchbook 8.00
    comment: The risk is a 40-day absence and an unplaced run last time out, with a seventh two starts back, and she carries 135 lb from draw 3.
    DATA: model 13.2% | style Prominent (led 5% of runs) | runs in data 7 | last 3: 12 Sep Chester Flat 5.1f Soft 3/9; 27 Sep Ffos Las Flat 5f Soft 7/8; 15 Oct Southwell (AW) Flat 5f Standard 10/12 fig 48
    DATA for: Official rating 62, 8 lb above field average; Has won at this trip or further
    DATA against: Recent figures 14 lb below its current mark (looks high in the weights); Carries 6 lb more than average
- Dancingonthestars (hrs_60819346) | 2yo G | 118lb | OR 35 | draw 2 | jockey Connor Planas | trainer Dylan Cunha (14d 1/9) | headgear - | last run 44 days | form 907 | MARKET 7.6% | 09:00 median 11.00 | Matchbook 13.00
    comment: Dancingonthestars is hard to fancy: seventh last time, then unplaced and ninth in his previous two outings, and he is yet to win in that spell after 44 days off.
    DATA: model 0.6% | style Held up (led 8% of runs) | runs in data 3 | last 3: 16 May Doncaster Flat 5f Good To Soft 9/9; 25 Sep Newmarket Flat 7f Good 14/14; 11 Oct Goodwood Flat 6f Good To Soft 7/8
    DATA for: Carries 11 lb less than average
    DATA against: Official rating 35, 19 lb below field average; Poor recent finishing positions
- Fancied Angel (hrs_17391092250) | 2yo F | 128lb | OR 55 | draw 9 | jockey Charles Bishop | trainer Adam Kirby (14d 1/6) | headgear t | last run 22 days | form 5605 | MARKET 7.0% | 09:00 median 11.00 | Matchbook 15.00
    comment: Fancied Angel is winless in her last four, though a fifth last time out, 22 days ago, is her best recent effort, and she has run over today's trip and going before.
    DATA: model 7.6% | style Held up (led 4% of runs) | runs in data 4 | last 3: 16 Sep Beverley Flat 5f Good 6/13; 13 Oct Leicester Flat 6f Good To Soft 11/12; 2 Nov Wolverhampton (AW) Flat 5f Standard 5/11 fig 50
- Ventura Power (hrs_64968001) | 2yo G | 132lb | OR 59 | draw 10 | jockey Jack Callan | trainer George Boughey (14d 6/20) | headgear - | last run 19 days | form 496400 | MARKET 6.1% | 09:00 median 15.00 | Matchbook 15.00
    comment: Ventura Power is yet to win in his last six, with a fourth three starts back his best finish, but he has run over today's trip and going and returns after 19 days, with a yard in form at 6/20.
    DATA: model 8.4% | style Held up (led 4% of runs) | runs in data 7 | last 3: 5 Oct Yarmouth Flat 7f Good To Firm 4/8; 19 Oct Wolverhampton (AW) Flat 7f Standard 10/12 fig 45; 5 Nov Southwell (AW) Flat 6f Standard 10/13 fig 47
    DATA for: Official rating 59, 5 lb above field average; Trainer 30% wins (6/20), last 14 days
    DATA against: Best recent form figure 47, 4 lb below field average; Recent figures 12 lb below its current mark (looks high in the weights)
- Lucky Larry (hrs_65380539) | 2yo G | 118lb | OR 32 | draw 5 | jockey John Egan | trainer Dylan Cunha (14d 1/9) | headgear - | last run 17 days | form 0900 | MARKET 2.4% | 09:00 median 34.00 | Matchbook 44.00
    comment: Winless in his last four, Lucky Larry has been unplaced twice in his last three outings and finished ninth three starts back, so he is hard to fancy off 118 lb.
    DATA: model 0.6% | style Midfield (led 5% of runs) | runs in data 4 | last 3: 29 Jun Kempton Flat 7f Standard To Slow 9/11; 13 Aug Lingfield Flat 7f Standard 11/11; 7 Nov Southwell (AW) Flat 6f Standard 11/13 fig 31
    DATA for: Carries 11 lb less than average
    DATA against: Best recent form figure 31, 20 lb below field average; Official rating 32, 22 lb below field average; Poor recent finishing positions
- Courseyoudo (hrs_64590722) | 2yo G | 134lb | OR 61 | draw 4 | jockey Kieran O'Neill | trainer Tom Lacey (14d 2/12) | headgear - | last run 56 days | form 675850 | MARKET 1.7% | 09:00 median 51.00 | Matchbook 60.00
    comment: Courseyoudo has finished fifth, eighth, fifth, seventh and sixth in his last six outings before an unplaced latest, so he's yet to win in that spell, and 56 days off is a concern.
    DATA: model 3.9% | style Midfield (led 3% of runs) | runs in data 6 | last 3: 2 Jul Nottingham Flat 6.1f Good To Firm 8/8; 31 Aug Chepstow Flat 5.1f Good To Soft 5/5; 29 Sep Bath Flat 5.7f Good To Firm 11/11
    DATA for: Official rating 61, 7 lb above field average
    DATA against: Carries 5 lb more than average

## 1:38 Lingfield (AW) | race_id rac_32305380341 | Midnite It's Actually Pretty Good Maiden Stakes (GBB/GBBPlus Race)
Flat | Class 3 | 1m4f1y | going Standard | AW | 9 runners | rating band - | age 3yo+
DATA pace: Lone leader - Champion Lawman is the only habitual front-runner and may be allowed an easy lead.
- Trustintimes (hrs_46265534) | 5yo G | 138lb | OR - | draw 6 | jockey Charles Bishop | trainer Harry Fry (14d 2/4) | headgear - | last run 24 days | form 4 | MARKET 37.3% | 09:00 median 2.25 | Matchbook 2.56
    DATA: model 9.6% | style Held up (led 5% of runs) | runs in data 3 | last 3: 10 Apr Aintree Hurdle 20f Good To Soft 17/22; 14 Oct Nottingham Flat 8.3f Good To Soft 4/14; 31 Oct Ascot Hurdle 15.5f Good To Firm 1/16 fig 134
- Liam Mera Kai (hrs_51186842) | 5yo G | 138lb | OR 82 | draw 9 | jockey Edward Greatrex | trainer Warren Greatrex (14d 6/24) | headgear - | last run 29 days | form 5325 | MARKET 17.5% | 09:00 median 5.00 | Matchbook 5.40
    DATA: model 35.6% | style Midfield (led 5% of runs) | runs in data 6 | last 3: 3 Sep Southwell Flat 12.1f Standard 3/7; 26 Sep Southwell Flat 11.1f Standard 2/13; 26 Oct Kempton (AW) Flat 12f Standard / Slow 5/9 fig 62
    DATA for: Official rating 82, 15 lb above field average; Trainer 25% wins (6/24), last 14 days; Good recent finishing positions
- Sergei Breeze (hrs_56219394) | 3yo G | 133lb | OR 73 | draw 3 | jockey Charlie Tucker(7) | trainer Kathy Turner (14d 0/1) | headgear - | last run 26 days | form -43253 | MARKET 12.4% | 09:00 median 7.00 | Matchbook 7.60
    DATA: model 25.0% | style Prominent (led 4% of runs) | runs in data 5 | last 3: 16 Sep Sandown Flat 9.9f Good 2/9; 1 Oct Salisbury Flat 9.9f Soft 5/11; 29 Oct Bath Flat 10f Soft 3/12 fig 77
    DATA for: Best recent form figure 77, 15 lb above field average; Official rating 73, 6 lb above field average; Last-run finishing speed +2.4% vs that field (finished strongly); Good recent finishing positions
- Secret Squirrel (hrs_34401871) | 7yo G | 138lb | OR - | draw 7 | jockey David Egan | trainer Hughie Morrison (14d 0/4) | headgear b (1st time) | last run 10 days | form 4/3 | MARKET 10.6% | 09:00 median 8.00 | Matchbook 9.40
    DATA: model 8.5% | style Midfield (led 4% of runs) | runs in data 5 | last 3: 18 Apr Ayr Hurdle 16f Heavy 5/8; 4 Nov Nottingham Flat 14f Soft 3/10 fig 77; 14 Nov Windsor Hurdle 16f Good 8/10 fig 118
    DATA for: Best recent form figure 77, 15 lb above field average; First-time headgear
    DATA against: Aged 7, older than most of this field
- Shangri La (hrs_56713307) | 3yo F | 128lb | OR 72 | draw 8 | jockey Callum Shepherd | trainer David Simcock (14d 1/8) | headgear - | last run 35 days | form -53208 | MARKET 9.5% | 09:00 median 9.00 | Matchbook 10.00
    DATA: model 7.3% | style Held up (led 3% of runs) | runs in data 5 | last 3: 16 Sep Yarmouth Flat 11.5f Good To Soft 2/8; 11 Oct Goodwood Flat 9.9f Good To Soft 10/11; 20 Oct Yarmouth Flat 11.5f Soft 8/8 fig 46
    DATA for: Official rating 72, 5 lb above field average
    DATA against: Best recent form figure 46, 16 lb below field average; Last-run finishing speed -5.3% vs that field (faded)
- Rowlf (hrs_17391437483) | 3yo G | 133lb | OR - | draw 1 | jockey Harry Davies | trainer William Haggas (14d 3/17) | headgear t (1st time) | wind surgery | last run 29 days | form 44 | MARKET 7.0% | 09:00 median 11.00 | Matchbook 15.50
    DATA: model 7.5% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 27 Sep Epsom Downs Flat 10.1f Good 4/6; 26 Oct Redcar Flat 10f Heavy 4/10 fig 49
    DATA for: First-time headgear
    DATA against: Best recent form figure 49, 13 lb below field average; Lightly raced: 2 runs in our data, so the model has little to go on
- Champion Lawman (hrs_52236177) | 3yo C | 133lb | OR - | draw 2 | jockey Jack Callan | trainer Charlie Johnston (14d 0/7) | headgear - | last run 182 days | form 45 | MARKET 3.0% | 09:00 median 26.00 | Matchbook 40.00
    DATA: model 4.4% | style Leader (led 38% of runs) | runs in data 2 | last 3: 28 Apr Lingfield Flat 8f Standard 4/12; 26 May Redcar Flat 10f Good To Firm 5/6
    DATA for: Pace: may get an uncontested lead
    DATA against: Last-run finishing speed -2.8% vs that field (faded); Returns from a 182-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- Surrey King (hrs_58033710) | 3yo C | 133lb | OR - | draw 5 | jockey Robert Havlin | trainer Hughie Morrison (14d 0/4) | headgear - | last run 205 days | form 9-8 | MARKET 2.3% | 09:00 median 29.00 | Matchbook 60.00
    DATA: model 1.7% | style Held up (led 8% of runs) | runs in data 1 | last 3: 3 May Salisbury Flat 12f Good To Firm 8/8
    DATA against: Last-run finishing speed -3.5% vs that field (faded); Returns from a 205-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Dee's Honey (hrs_56094920) | 3yo F | 128lb | OR 40 | draw 4 | jockey Marco Ghiani | trainer Michael Keady (14d 1/3) | headgear t (1st time) | last run 90 days | form 95-990 | MARKET 0.4% | 09:00 median 151.00 | Matchbook 300.00
    DATA: model 0.4% | style Unknown | runs in data 3 | last 3: 12 Mar Chelmsford Flat 7f Standard 9/10; 14 Aug Yarmouth Flat 8f Good To Firm 9/10; 26 Aug Catterick Flat 7f Good 13/13
    DATA for: First-time headgear
    DATA against: Official rating 40, 27 lb below field average; Last-run finishing speed -15.2% vs that field (faded); Poor recent finishing positions; Returns from a 90-day break

## 2:08 Lingfield (AW) | race_id rac_32305382278 | ARC £1M Bonus Handicap Stakes
Flat | Class 6 | 1m1y | going Standard | AW | 12 runners | rating band 0-65 | age 4yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Sant Alessio (hrs_37563883) | 5yo G | 132lb | OR 63 | draw 6 | jockey Taylor Fisher | trainer Joe Tickle (14d 1/9) | headgear - | last run 4 days | form 748446 | MARKET 15.9% | 09:00 median 5.25 | Matchbook 5.90 | CHECK (skip line 4.99)
    comment: Sant Alessio is winless in his last six, though three fourths in that spell show he is rarely out of the mix, and he has run over today's trip and going. Back in just four days and carrying 132 lb from stall six, he'll need to improve on last time's sixth.
    DATA: model 17.2% | style Prominent (led 29% of runs) | runs in data 7 | last 3: 5 Oct Wolverhampton Flat 9.5f Standard 4/10; 27 Oct Wolverhampton (AW) Flat 8.5f Standard 4/10 fig 64; 20 Nov Wolverhampton (AW) Flat 9.5f Standard 6/12 fig 60
    DATA for: Best recent form figure 64, 9 lb above field average
- Valentine Boy (hrs_50036392) | 4yo G | 134lb | OR 65 | draw 4 | jockey Jack Dace(5) | trainer Luke Dace (14d 0/6) | headgear h | last run 8 days | form 846534 | MARKET 14.3% | 09:00 median 5.50 | Matchbook 6.60
    comment: Valentine Boy comes here fresh from a fourth last time out just eight days ago, and a third two starts back shows he can get involved.
    DATA: model 21.6% | style Held up (led 8% of runs) | runs in data 10 | last 3: 9 Oct Kempton Flat 8f Standard To Slow 5/10; 4 Nov Kempton (AW) Flat 8f Standard / Slow 3/13 fig 76; 16 Nov Wolverhampton (AW) Flat 7f Standard 4/11 fig 69
    DATA for: Best recent form figure 76, 21 lb above field average; Recent figures 11 lb above its current mark (looks well handicapped); Has won at this trip or further
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- The Bitter Moose (hrs_34471108) | 5yo G | 131lb | OR 62 | draw 8 | jockey Sean Levey | trainer Patrick Chamings (14d 0/2) | headgear v | last run 27 days | form 338605 | MARKET 11.1% | 09:00 median 7.00 | Matchbook 8.60
    comment: The Bitter Moose is winless in his last six, though a fifth last time out follows a run of defeats, and he has run over today's trip and going before.
    DATA: model 7.3% | style Midfield (led 3% of runs) | runs in data 9 | last 3: 21 Sep Leicester Flat 6f Good 6/12; 2 Oct Ascot Flat 7f Good To Firm 17/18; 28 Oct Kempton (AW) Flat 7f Standard / Slow 5/13 fig 63
    DATA for: Best recent form figure 63, 8 lb above field average
- Way To Dubai (hrs_31022481) | 7yo G | 130lb | OR 61 | draw 10 | jockey Jason Watson | trainer Michael Appleby (14d 0/13) | headgear - | last run 3 days | form 404375 | MARKET 10.7% | 09:00 median 7.50 | Matchbook 8.80
    comment: Winless in his last six, Way To Dubai was only fifth last time out and seventh before that, and his quick 3-day turnaround offers little cause for optimism.
    DATA: model 6.9% | style Midfield (led 5% of runs) | runs in data 17 | last 3: 28 Jul Yarmouth Flat 7f Good To Firm 3/9; 23 Oct Wolverhampton (AW) Flat 6f Standard 7/7 fig 48; 21 Nov Lingfield (AW) Flat 6f Standard 5/10 fig 58
    DATA for: Has won at this trip or further
    DATA against: Trainer 0 wins from 13 runs, last 14 days
- Rey de La Batalla (hrs_35625009) | 5yo G | 132lb | OR 63 | draw 11 | jockey Harry Davies | trainer Simon Dow (14d 0/2) | headgear - | last run 27 days | form -59094 | MARKET 10.4% | 09:00 median 7.00 | Matchbook 9.80
    comment: Rey de La Batalla comes here after a fourth last time out, and at 27 days since that run he should be fit, having already tackled today's trip and going.
    DATA: model 7.5% | style Held up (led 4% of runs) | runs in data 5 | last 3: 9 Sep Kempton Flat 7f Standard To Slow 10/14; 9 Oct Kempton Flat 7f Standard To Slow 9/11; 28 Oct Kempton (AW) Flat 7f Standard / Slow 4/13 fig 64
    DATA for: Best recent form figure 64, 9 lb above field average
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- North View (hrs_35864402) | 5yo G | 134lb | OR 65 | draw 9 | jockey Kieren Fox | trainer Tony Carroll (14d 1/31) | headgear - | last run 19 days | form 360785 | MARKET 9.3% | 09:00 median 8.00 | Matchbook 11.00
    comment: The main risk is a yard struggling at 1/31 over the last 14 days.
    DATA: model 3.7% | style Held up (led 3% of runs) | runs in data 15 | last 3: 2 Oct Wolverhampton Flat 7.2f Standard 7/9; 19 Oct Southwell (AW) Flat 6f Standard 8/10 fig 53; 5 Nov Southwell (AW) Flat 6f Standard 5/9 fig 62
    DATA for: Best recent form figure 62, 7 lb above field average
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Nordic Norm (hrs_45982300) | 4yo G | 131lb | OR 62 | draw 12 | jockey Marco Ghiani | trainer J. R. Jenkins (14d 0/4) | headgear t | last run 68 days | form 529058 | MARKET 8.2% | 09:00 median 10.00 | Matchbook 11.50
    comment: Nordic Norm is winless in his last six, beaten into eighth last time out and having had 68 days off since, so he is hard to fancy; he has run over today's trip and going, and a second five starts back shows some ability.
    DATA: model 3.0% | style Midfield (led 4% of runs) | runs in data 7 | last 3: 12 Jun Chester Flat 7.6f Soft 10/11; 23 Aug Brighton Flat 8f Good To Firm 5/5; 17 Sep Southwell Flat 8.1f Standard 8/12
- Spirit of Breeze (hrs_30907926) | 6yo G | 132lb | OR 63 | draw 7 | jockey David Egan | trainer Jamie Moore & Josh Moore (14d 3/27) | headgear tp | last run 33 days | form -33200 | MARKET 5.7% | 09:00 median 13.00 | Matchbook 18.00
    comment: Without a win in his last five starts and unplaced in his last two, Spirit of Breeze is hard to fancy, though a second three starts back and a third four starts back show he can still hit the frame.
    DATA: model 8.5% | style Held up (led 4% of runs) | runs in data 5 | last 3: 13 Aug Lingfield Flat 7f Standard 2/12; 23 Sep Kempton Flat 7f Standard To Slow 10/13; 22 Oct Newmarket Flat 7f Soft 10/12 fig 29
    DATA against: Best recent form figure 29, 26 lb below field average; Recent figures 34 lb below its current mark (looks high in the weights); Last-run finishing speed -3.3% vs that field (faded); Pace: steady gallop likely, hard to come from off the pace
- Dandy G Boy (hrs_412694842) | 4yo G | 130lb | OR 61 | draw 3 | jockey Edward Greatrex | trainer Warren Greatrex (14d 6/24) | headgear v | last run 20 days | form 662780 | MARKET 5.6% | 09:00 median 15.00 | Matchbook 17.00
    comment: Dandy G Boy has been beaten in his last three outings, an eighth and a seventh before that, but a second four starts back shows he can go close, and he has run over today's trip and going.
    DATA: model 7.5% | style Prominent (led 5% of runs) | runs in data 6 | last 3: 9 Sep Kempton Flat 7f Standard To Slow 7/14; 26 Sep Southwell Flat 8.1f Standard 8/14; 4 Nov Kempton (AW) Flat 8f Standard / Slow 11/13 fig 37
    DATA for: Trainer 25% wins (6/24), last 14 days
    DATA against: Best recent form figure 37, 18 lb below field average; Recent figures 24 lb below its current mark (looks high in the weights); Poor recent finishing positions
- Penfolds Grange (hrs_45982307) | 4yo G | 133lb | OR 64 | draw 5 | jockey Tyler Heard | trainer Mark Pattinson (14d 0/1) | headgear - | last run 34 days | form 397826 | MARKET 4.6% | 09:00 median 17.00 | Matchbook 22.00
    comment: The risk is a winless last six and a sixth last time out, with 133 lb to carry from stall five.
    DATA: model 11.6% | style Midfield (led 3% of runs) | runs in data 10 | last 3: 9 Sep Kempton Flat 7f Standard To Slow 8/14; 23 Sep Kempton Flat 7f Standard To Slow 2/13; 21 Oct Kempton (AW) Flat 7f Standard / Slow 6/10 fig 61
    DATA for: Best recent form figure 61, 6 lb above field average
- Jazzy Baby (hrs_52995285) | 4yo F | 134lb | OR 65 | draw 1 | jockey Josephine Gordon | trainer Keiran Burke (14d 0/0) | headgear - | last run 151 days | form 334050 | MARKET 2.7% | 09:00 median 26.00 | Matchbook 42.00
    comment: Jazzy Baby has twice finished third in her last six, but she was unplaced last time out and returns from 151 days off, and she is yet to win in that spell.
    DATA: model 2.7% | style Prominent (led 8% of runs) | runs in data 7 | last 3: 30 Apr Kempton Flat 8f Standard To Slow 10/10; 9 Jun Salisbury Flat 9.9f Soft 5/7; 26 Jun Newcastle Flat 8f Standard To Slow 14/14
    DATA for: Has won at this trip or further
    DATA against: Last-run finishing speed -5.7% vs that field (faded); Returns from a 151-day break
- Secret Message (hrs_65974650) | 4yo G | 132lb | OR 63 | draw 2 | jockey Connor Planas | trainer Nick Littmoden (14d 0/1) | headgear t | last run 29 days | form 087 | MARKET 1.3% | 09:00 median 51.00 | Matchbook 110.00
    comment: Secret Message is winless in his last three, finishing seventh last time out, an eighth two starts back and unplaced before that, so he is hard to fancy off 132 lb from stall 2.
    DATA: model 2.6% | style Midfield (led 4% of runs) | runs in data 4 | last 3: 9 Sep Kempton Flat 8f Standard To Slow 11/11; 3 Oct Southwell Flat 7.1f Standard 8/11; 26 Oct Kempton (AW) Flat 7f Standard / Slow 7/9 fig 34
    DATA against: Best recent form figure 34, 21 lb below field average; Recent figures 29 lb below its current mark (looks high in the weights); Poor recent finishing positions

## 2:38 Lingfield (AW) | race_id rac_32305818103 | ARC All Weather Bonus Is Back Handicap Stakes (Div I)
Flat | Class 6 | 7f1y | going Standard | AW | 12 runners | rating band 0-60 | age 3yo+
DATA pace: Lone leader - Mount Mogan is the only habitual front-runner and may be allowed an easy lead.
- Teggy Lasso (hrs_44939573) | 4yo G | 128lb | OR 53 | draw 7 | jockey Jason Watson | trainer Michael Appleby (14d 0/13) | headgear p | last run 17 days | form 453445 | MARKET 20.9% | 09:00 median 3.75 | Matchbook 4.40 | CHECK (skip line 3.56)
    comment: Teggy Lasso has been consistent without a win, finishing fifth last time out, a fourth two starts back and a fourth three starts back, and he has run over today's trip and going before after 17 days off.
    DATA: model 15.9% | style Prominent (led 23% of runs) | runs in data 7 | last 3: 13 Apr Newcastle Flat 8f Standard 4/11; 20 Apr Newcastle Flat 8f Standard 4/14; 7 Nov Southwell (AW) Flat 7f Standard 5/12 fig 53
    DATA against: Trainer 0 wins from 13 runs, last 14 days
- Lessay (hrs_36062047) | 5yo G | 135lb | OR 60 | draw 6 | jockey Dylan Hogan | trainer Patrick Morris (14d 0/11) | headgear p | last run 1 days | form 614856 | MARKET 17.4% | 09:00 median 4.50 | Matchbook 5.10
    DATA: model 13.1% | style Held up (led 5% of runs) | runs in data 16 | last 3: 25 Sep Newcastle Flat 7.1f Standard 8/11; 16 Nov Wolverhampton (AW) Flat 7f Standard 5/11 fig 63; 23 Nov Wolverhampton (AW) Flat 7f Standard 6/11 fig 56
    DATA for: Best recent form figure 63, 9 lb above field average; Official rating 60, 8 lb above field average; Has won at this trip or further
    DATA against: Trainer 0 wins from 11 runs, last 14 days; Carries 8 lb more than average; Course: hold-up horses have won 0.7× their fair share at 7f here
- Two And Two (hrs_59609830) | 3yo F | 132lb | OR 58 | draw 4 | jockey Marco Ghiani | trainer Simon Hodgson (14d 0/3) | headgear - | last run 5 days | form 057486 | MARKET 13.2% | 09:00 median 6.00 | Matchbook 7.00
    comment: The risk is a winless run in her last six, with a fourth three starts back her best finish.
    DATA: model 13.3% | style Held up (led 4% of runs) | runs in data 10 | last 3: 19 Oct Wolverhampton (AW) Flat 6f Standard 4/13 fig 57; 29 Oct Bath Flat 5f Soft 8/15 fig 57; 19 Nov Lingfield (AW) Flat 7f Standard 6/13 fig 54
    DATA for: Official rating 58, 6 lb above field average
    DATA against: Course: hold-up horses have won 0.7× their fair share at 7f here
- Twitch (hrs_27902476) | 9yo G | 131lb | OR 56 | draw 2 | jockey Georgia Dobie | trainer Craig Benton (14d 0/0) | headgear b | last run 28 days | form 642161 | MARKET 11.3% | 09:00 median 6.50 | Matchbook 8.80
    comment: Won last time out and again three starts back, with a sixth in between, so Twitch arrives in good heart after 28 days off, and he has run over today's trip and going.
    DATA: model 16.6% | style Prominent (led 3% of runs) | runs in data 10 | last 3: 18 Sep Wolverhampton Flat 7.2f Standard 1/8; 5 Oct Kempton Flat 7f Standard To Slow 6/13; 27 Oct Wolverhampton (AW) Flat 7f Standard 1/11 fig 56
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Aged 9, older than most of this field
- Sovereign Class (hrs_48818924) | 4yo F | 123lb | OR 48 | draw 12 | jockey Callum Shepherd | trainer Grant Tuer (14d 0/5) | headgear - | last run 26 days | form 360062 | MARKET 9.8% | 09:00 median 8.00 | Matchbook 9.60
    comment: Sovereign Class showed improvement with a second last time out, 26 days ago, and she has run over today's trip and going before, though she is winless in her last six and was a sixth two starts back.
    DATA: model 4.1% | style Midfield (led 3% of runs) | runs in data 6 | last 3: 9 Sep Redcar Flat 6f Good 12/16; 21 Sep Hamilton Flat 6f Soft 6/7; 29 Oct Southwell (AW) Flat 7f Standard 2/12 fig 62
    DATA for: Best recent form figure 62, 8 lb above field average; Recent figures 14 lb above its current mark (looks well handicapped)
- Jackson Street (hrs_36207507) | 5yo G | 122lb | OR 47 | draw 5 | jockey William Carson | trainer Michael Attwater (14d 1/8) | headgear - | last run 48 days | form 437557 | MARKET 6.1% | 09:00 median 13.00 | Matchbook 15.50
    comment: Jackson Street is winless in his last six, with a seventh last time out and a third five starts back his best finish in that spell, though he has run over today's trip and going.
    DATA: model 3.9% | style Midfield (led 3% of runs) | runs in data 10 | last 3: 10 Sep Lingfield Flat 7f Standard 5/10; 21 Sep Wolverhampton Flat 7.2f Standard 5/9; 7 Oct Kempton Flat 8f Standard To Slow 7/13
    DATA for: Carries 5 lb less than average
    DATA against: Official rating 47, 5 lb below field average
- Sanditon (hrs_45855138) | 4yo G | 125lb | OR 50 | draw 3 | jockey Jack Callan | trainer Charlie Johnston (14d 0/7) | headgear p | last run 26 days | form 575279 | MARKET 5.8% | 09:00 median 13.00 | Matchbook 17.50
    comment: Sanditon is hard to fancy, winless in his last six and beaten into ninth last time out, with a seventh two starts back; a second three starts back is the one bright spot.
    DATA: model 5.0% | style Midfield (led 4% of runs) | runs in data 20 | last 3: 28 Sep Wolverhampton Flat 7.2f Standard 2/11; 13 Oct Wolverhampton Flat 7.2f Standard 7/9; 29 Oct Southwell (AW) Flat 7f Standard 9/13 fig 46
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 46, 8 lb below field average
- Lahina Bay (hrs_29761354) | 6yo M | 128lb | OR 53 | draw 13 | jockey David Egan | trainer Rachel Cook & John Bridger (14d 0/3) | headgear - | last run 26 days | form 322807 | MARKET 5.3% | 09:00 median 15.00 | Matchbook 17.50
    comment: Lahina Bay has run well in the past, with a second four and five starts back, a third six back, and has run over today's trip and going.
    DATA: model 6.0% | style Prominent (led 29% of runs) | runs in data 12 | last 3: 23 Sep Kempton Flat 6f Standard To Slow 8/11; 8 Oct Bath Flat 5f Good 13/14; 29 Oct Bath Flat 5f Soft 7/15 fig 52
    DATA against: Poor recent finishing positions
- Pimentel (hrs_55794977) | 3yo F | 130lb | OR 56 | draw 11 | jockey Jack Doughty | trainer Marcus Tregoning (14d 2/3) | headgear - | last run 125 days | form 2-6237 | MARKET 4.3% | 09:00 median 15.00 | Matchbook 26.00
    comment: Pimentel has hit the frame in three of her last five, including two seconds and a third, but she was seventh last time out and returns after 125 days off. She has run over today's trip and going, yet is winless in recent starts and carries 130 lb from stall 11.
    DATA: model 9.6% | style Held up (led 4% of runs) | runs in data 4 | last 3: 27 Jun Chepstow Flat 6.1f Good To Firm 2/6; 30 Jun Brighton Flat 7f Good To Firm 3/6; 22 Jul Leicester Flat 6f Good To Firm 7/8
    DATA for: Good recent finishing positions
    DATA against: Returns from a 125-day break; Course: hold-up horses have won 0.7× their fair share at 7f here
- Mount Mogan (hrs_20530153) | 9yo G | 130lb | OR 55 | draw 1 | jockey Robert Havlin | trainer Laura Mongan (14d 0/2) | headgear p | last run 73 days | form 5-5147 | MARKET 2.4% | 09:00 median 26.00 | Matchbook 48.00
    comment: Mount Mogan was seventh last time out and returns from a 73-day break, and a fourth two starts back is the best of his recent efforts since a win three starts back, so he is hard to fancy.
    DATA: model 6.7% | style Leader (led 23% of runs) | runs in data 4 | last 3: 25 Feb Lingfield Flat 7f Standard 1/7; 30 Jul Epsom Downs Flat 6f Good To Firm 4/7; 12 Sep Lingfield Flat 8f Standard 7/8
    DATA for: Has won at this trip or further; Pace: may get an uncontested lead
    DATA against: Aged 9, older than most of this field
- Barnsnape Boy (hrs_37702378) | 5yo G | 121lb | OR 45 | draw 9 | jockey Jack Dace(5) | trainer Jim Boyle (14d 0/4) | headgear p | last run 26 days | form 448738 | MARKET 1.9% | 09:00 median 41.00 | Matchbook 60.00
    comment: Winless in his last six, Barnsnape Boy was eighth last time out 26 days ago, and he has finished no better than a third two starts back, so he is hard to fancy.
    DATA: model 3.2% | style Midfield (led 3% of runs) | runs in data 9 | last 3: 6 Aug Brighton Flat 7f Good To Firm 7/8; 6 Oct Brighton Flat 7f Good To Firm 3/10; 29 Oct Bath Flat 5.5f Soft 8/16 fig 42
    DATA for: Has won at this trip or further; Carries 6 lb less than average
    DATA against: Best recent form figure 42, 12 lb below field average; Official rating 45, 7 lb below field average
- First Encounter (hrs_35714483) | 5yo G | 121lb | OR 43 | draw 8 | jockey William Cox | trainer John Gallagher (14d 0/0) | headgear p | last run 56 days | form 054087 | MARKET 1.7% | 09:00 median 41.00 | Matchbook 65.00
    comment: First Encounter is winless in his last six, with a seventh last time out and an eighth before that, and he returns after 56 days off.
    DATA: model 2.5% | style Midfield (led 4% of runs) | runs in data 12 | last 3: 18 Jul Doncaster Flat 8f Good To Firm 11/11; 5 Aug Brighton Flat 8f Good To Firm 8/9; 29 Sep Wolverhampton Flat 8.6f Standard 7/8
    DATA for: Has won at this trip or further; Carries 6 lb less than average
    DATA against: Official rating 43, 9 lb below field average; Last-run finishing speed -4.2% vs that field (faded); Poor recent finishing positions

## 3:08 Lingfield (AW) | race_id rac_32305384215 | ARC All Weather Bonus Is Back Handicap Stakes (Div II)
Flat | Class 6 | 7f1y | going Standard | AW | 13 runners | rating band 0-60 | age 3yo+
DATA pace: Even - Two likely leaders (Denby's Dream, Zoulette). A fair, even gallop is most likely.
- Orange Emperor (hrs_50433558) | 3yo G | 135lb | OR 60 | draw 6 | jockey Myla Coppins(5) | trainer Marco Botti (14d 0/9) | headgear - | last run 5 days | form 652353 | MARKET 30.6% | 09:00 median 2.50 | Matchbook 2.98
    comment: Yet to win in that spell, he must still prove he can get his head in front from stall six.
    DATA: model 25.9% | style Prominent (led 5% of runs) | runs in data 11 | last 3: 12 Sep Lingfield Flat 7f Standard 3/9; 2 Nov Chelmsford (AW) Flat 7f Standard 5/13 fig 66; 19 Nov Lingfield (AW) Flat 7f Standard 3/13 fig 61
    DATA for: Best recent form figure 66, 21 lb above field average; Recent figures 6 lb above its current mark (looks well handicapped); Official rating 60, 8 lb above field average; Good recent finishing positions
    DATA against: Trainer 0 wins from 9 runs, last 14 days; Carries 7 lb more than average
- Tam Lin (hrs_44786490) | 4yo G | 129lb | OR 53 | draw 13 | jockey Jason Watson | trainer Michael Appleby (14d 0/13) | headgear - | last run 17 days | form 633884 | MARKET 12.3% | 09:00 median 6.00 | Matchbook 7.80
    comment: Tam Lin was a fourth last time out after a pair of eighths, and he has run over today's trip and on this going, but he is winless in his last six and carries 129 lb from stall 13.
    DATA: model 8.2% | style Prominent (led 23% of runs) | runs in data 7 | last 3: 11 Mar Southwell Flat 7.1f Standard 8/9; 20 Apr Lingfield Flat 8f Standard 8/11; 7 Nov Southwell (AW) Flat 6f Standard 4/11 fig 50
    DATA for: Best recent form figure 50, 5 lb above field average
    DATA against: Trainer 0 wins from 13 runs, last 14 days
- Rovinia (hrs_45921596) | 4yo F | 127lb | OR 51 | draw 10 | jockey Marco Ghiani | trainer Roger Teal (14d 0/7) | headgear - | last run 21 days | form 213532 | MARKET 11.2% | 09:00 median 6.50 | Matchbook 8.80
    comment: Rovinia has been consistent, finishing second last time out and third two starts back, and she has run over today's trip and going, but just one win in her last six suggests she tends to find one too good.
    DATA: model 9.9% | style Midfield (led 4% of runs) | runs in data 13 | last 3: 18 Sep Wolverhampton Flat 7.2f Standard 5/10; 30 Sep Kempton Flat 6f Standard To Slow 3/11; 3 Nov Wolverhampton (AW) Flat 7f Standard 2/10 fig 50
    DATA for: Best recent form figure 50, 5 lb above field average; Has won at this trip or further; Good recent finishing positions
- Dandy Khan (hrs_41661438) | 4yo F | 131lb | OR 55 | draw 5 | jockey Jack Dace(5) | trainer Jim Boyle (14d 0/4) | headgear - | last run 75 days | form 563369 | MARKET 9.6% | 09:00 median 8.90 | Matchbook 9.00
    comment: The risk is a ninth last time out and a 75-day absence, with 131 lb to carry from stall five.
    DATA: model 5.4% | style Held up (led 4% of runs) | runs in data 16 | last 3: 20 Aug Lingfield Flat 8f Standard 3/11; 28 Aug Sandown Flat 8f Good 6/7; 10 Sep Epsom Downs Flat 8.5f Good To Soft 9/9
    DATA for: Has won at this trip or further
    DATA against: Course: hold-up horses have won 0.7× their fair share at 7f here
- Imelda (hrs_63323631) | 3yo F | 134lb | OR 59 | draw 9 | jockey Callum Shepherd | trainer David Loughnane (14d 2/8) | headgear b | last run 28 days | form 340043 | MARKET 7.0% | 09:00 median 11.00 | Matchbook 12.50
    comment: Imelda comes here in sound recent form, third last time out and a fourth two starts back, and she has run over today's trip and on this going before.
    DATA: model 9.2% | style Prominent (led 23% of runs) | runs in data 8 | last 3: 1 Oct Nottingham Flat 6.1f Good 11/15; 13 Oct Wolverhampton Flat 7.2f Standard 4/6; 27 Oct Wolverhampton (AW) Flat 7f Standard 3/11 fig 61
    DATA for: Best recent form figure 61, 16 lb above field average; Official rating 59, 7 lb above field average; Trainer 25% wins (2/8), last 14 days
    DATA against: Carries 6 lb more than average
- Amber Honey (hrs_46634784) | 4yo F | 130lb | OR 54 | draw 7 | jockey Sean Levey | trainer Pat Phelan (14d 1/4) | headgear - | last run 55 days | form 599419 | MARKET 6.6% | 09:00 median 12.00 | Matchbook 13.50
    DATA: model 9.2% | style Prominent (led 5% of runs) | runs in data 10 | last 3: 4 Aug Lingfield Flat 9f Standard 4/6; 12 Sep Lingfield Flat 8f Standard 1/8; 30 Sep Kempton Flat 8f Standard To Slow 9/11
    DATA for: Has won at this trip or further
- Denby's Dream (hrs_54998244) | 3yo F | 132lb | OR 57 | draw 3 | jockey Kieren Fox | trainer Charlie Pike (14d 0/2) | headgear h | last run 56 days | form 716660 | MARKET 5.6% | 09:00 median 15.00 | Matchbook 15.50
    DATA: model 5.7% | style Leader (led 57% of runs) | runs in data 12 | last 3: 27 Jul Windsor Flat 8.1f Good To Firm 6/8; 13 Sep Bath Flat 8f Good To Soft 6/10; 29 Sep Bath Flat 8f Good To Firm 11/12
    DATA for: Has won at this trip or further
    DATA against: Poor recent finishing positions
- Tilsworth Max (hrs_40625249) | 6yo G | 125lb | OR 49 | draw 11 | jockey Jack Callan | trainer J. R. Jenkins (14d 0/4) | headgear - | last run 26 days | form 567230 | MARKET 4.9% | 09:00 median 15.00 | Matchbook 20.00
    DATA: model 5.3% | style Prominent (led 23% of runs) | runs in data 11 | last 3: 10 Sep Lingfield Flat 7f Standard 2/10; 28 Sep Wolverhampton Flat 7.2f Standard 3/11; 29 Oct Southwell (AW) Flat 7f Standard 12/13 fig 28
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Best recent form figure 28, 17 lb below field average; Recent figures 21 lb below its current mark (looks high in the weights)
- Lady Delila (hrs_32401635) | 6yo M | 123lb | OR 47 | draw 12 | jockey David Egan | trainer Patrick Morris (14d 0/11) | headgear p | last run 28 days | form 584815 | MARKET 3.3% | 09:00 median 21.00 | Matchbook 32.00
    comment: In her favour, she has run over today's trip and going, and returns after 28 days from stall 12.
    DATA: model 6.0% | style Midfield (led 4% of runs) | runs in data 11 | last 3: 29 Sep Wolverhampton Flat 9.5f Standard 8/13; 13 Oct Wolverhampton Flat 7.2f Standard 1/9; 27 Oct Wolverhampton (AW) Flat 7f Standard 5/11 fig 43
    DATA for: Has won at this trip or further
    DATA against: Official rating 47, 5 lb below field average; Trainer 0 wins from 11 runs, last 14 days
- Zoulette (hrs_61910618) | 3yo F | 132lb | OR 57 | draw 2 | jockey Stevie Donohoe | trainer Ollie Sangster (14d 1/9) | headgear - | last run 27 days | form 672619 | MARKET 3.0% | 09:00 median 21.00 | Matchbook 44.00
    comment: Zoulette won two starts back but was only ninth last time out, and she has run over today's trip and going before after 27 days off.
    DATA: model 7.2% | style Prominent (led 43% of runs) | runs in data 8 | last 3: 2 Jun Wolverhampton Flat 7.2f Standard 6/9; 4 Jul Beverley Flat 7.4f Good To Firm 1/6; 28 Oct Kempton (AW) Flat 8f Standard / Slow 9/9 fig 31
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 31, 14 lb below field average; Recent figures 26 lb below its current mark (looks high in the weights)
- It's A Mugs Game (hrs_56406721) | 3yo G | 121lb | OR 46 | draw 4 | jockey Josephine Gordon | trainer Joe Tickle (14d 1/9) | headgear p | last run 28 days | form 468777 | MARKET 2.5% | 09:00 median 29.00 | Matchbook 46.00
    comment: Winless in his last six, he has finished seventh in each of his last three and a fourth six starts back is his best finish in that spell, so he is hard to fancy.
    DATA: model 3.7% | style Held up (led 5% of runs) | runs in data 6 | last 3: 2 Sep Bath Flat 5.7f Good 7/8; 13 Sep Bath Flat 5f Good To Soft 7/13; 27 Oct Wolverhampton (AW) Flat 6f Standard 7/12 fig 41
    DATA for: Carries 7 lb less than average
    DATA against: Best recent form figure 41, 4 lb below field average; Official rating 46, 6 lb below field average; Poor recent finishing positions; Course: hold-up horses have won 0.7× their fair share at 7f here
- So Chic (hrs_30589216) | 6yo M | 123lb | OR 47 | draw 1 | jockey Liam Wright(3) | trainer Stephanie Cassidy (14d 0/2) | headgear - | last run 21 days | form 462087 | MARKET 2.0% | 09:00 median 30.00 | Matchbook 70.00
    comment: So Chic is winless in her last six, with a seventh last time out and an eighth before, though a second four starts back shows she has a bit of ability.
    DATA: model 2.3% | style Held up (led 4% of runs) | runs in data 8 | last 3: 11 May Wolverhampton Flat 8.6f Standard 11/13; 13 Oct Wolverhampton Flat 7.2f Standard 8/9; 3 Nov Wolverhampton (AW) Flat 7f Standard 7/11 fig 39
    DATA against: Best recent form figure 39, 6 lb below field average; Recent figures 8 lb below its current mark (looks high in the weights); Official rating 47, 5 lb below field average; Poor recent finishing positions; Course: hold-up horses have won 0.7× their fair share at 7f here
- Real Gold (hrs_56406735) | 3yo F | 120lb | OR 44 | draw 8 | jockey Kieran O'Neill | trainer Rachel Cook & John Bridger (14d 0/3) | headgear b (1st time) | last run 49 days | form 376847 | MARKET 1.3% | 09:00 median 41.00 | Matchbook 140.00
    comment: Real Gold is winless in her last six, with a seventh last time out 49 days ago, and her best finish in that spell was a third six starts back.
    DATA: model 2.0% | style Midfield (led 4% of runs) | runs in data 11 | last 3: 27 Aug Lingfield Flat 7f Standard 8/11; 12 Sep Lingfield Flat 7f Standard 4/8; 6 Oct Brighton Flat 6f Good To Firm 7/9
    DATA for: Carries 8 lb less than average; First-time headgear
    DATA against: Official rating 44, 8 lb below field average

## 3:38 Lingfield (AW) | race_id rac_32305386152 | AWC Trials Day - Lingfield 2nd Jan 2027 Handicap Stakes
Flat | Class 6 | 1m2f | going Standard | AW | 14 runners | rating band 0-55 | age 3yo
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Far Far Out (hrs_56811433) | 3yo G | 135lb | OR 55 | draw 2 | jockey William Carson | trainer Tony Carroll (14d 1/31) | headgear - | last run 19 days | form 800421 | MARKET 23.9% | 09:00 median 3.00 | Matchbook 4.00 | CHECK (skip line 2.85)
    comment: Far Far Out arrives a last-time-out winner after a second two starts back, fit after 19 days, and he has run over today's trip and going before.
    DATA: model 17.2% | style Held up (led 3% of runs) | runs in data 8 | last 3: 14 Oct Nottingham Flat 8.5f Good To Soft 4/8 fig 46; 28 Oct Kempton (AW) Flat 8f Standard / Slow 2/10 fig 63; 5 Nov Chelmsford (AW) Flat 10f Standard 1/14 fig 62
    DATA for: Best recent form figure 63, 19 lb above field average; Recent figures 8 lb above its current mark (looks well handicapped); Official rating 55, 5 lb above field average; Has won at this trip or further; Good recent finishing positions
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Meritocratic (hrs_57103459) | 3yo G | 135lb | OR 55 | draw 12 | jockey Oliver Hoodless(7) | trainer James Owen (14d 4/45) | headgear v | last run 3 days | form 355763 | MARKET 17.2% | 09:00 median 4.50 | Matchbook 5.20
    DATA: model 17.7% | style Held up (led 8% of runs) | runs in data 9 | last 3: 13 Oct Wolverhampton Flat 8.6f Standard 3/10; 26 Oct Hereford Hurdle 16f Good To Firm PU/9; 21 Nov Huntingdon Hurdle 16f Good 8/13
    DATA for: Official rating 55, 5 lb above field average
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Herstmonceux (hrs_65484783) | 3yo G | 132lb | OR 52 | draw 5 | jockey Jack Doughty | trainer William Muir & Chris Grassick (14d 0/5) | headgear - | last run 57 days | form 537 | MARKET 15.2% | 09:00 median 5.00 | Matchbook 5.90
    comment: Herstmonceux has been winless in his last three, finishing seventh last time out, with a third two starts back his best effort, and he returns after 57 days off.
    DATA: model 4.9% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 4 Aug Ffos Las Flat 8f Good 5/8; 21 Aug Salisbury Flat 9.9f Good 3/5; 28 Sep Wolverhampton Flat 8.6f Standard 7/11
- A Daughters Love (hrs_51273152) | 3yo F | 135lb | OR 55 | draw 6 | jockey Jack Dace(5) | trainer David Flood (14d 0/2) | headgear tp | last run 3 days | form 656874 | MARKET 12.6% | 09:00 median 6.00 | Matchbook 7.20
    DATA: model 16.9% | style Midfield (led 4% of runs) | runs in data 19 | last 3: 10 Oct Southwell Flat 12.1f Standard 8/11; 26 Oct Leicester Flat 12f Soft 7/13 fig 44; 21 Nov Lingfield (AW) Flat 8f Standard 4/10 fig 53
    DATA for: Best recent form figure 53, 9 lb above field average; Official rating 55, 5 lb above field average; Last-run finishing speed +3.0% vs that field (finished strongly); Has won at this trip or further
- Bennyworth (hrs_60752734) | 3yo G | 127lb | OR 47 | draw 4 | jockey David Egan | trainer Jim Boyle (14d 0/4) | headgear b (1st time) | last run 19 days | form 484860 | MARKET 5.7% | 09:00 median 13.00 | Matchbook 17.00
    comment: Bennyworth is winless in his last six, with a fourth six starts back his best finish and an unplaced effort last time out, though he has run over today's trip and going and returns after 19 days.
    DATA: model 6.0% | style Held up (led 5% of runs) | runs in data 13 | last 3: 10 Aug Windsor Flat 8.1f Good To Firm 8/10; 27 Oct Wolverhampton (AW) Flat 8.5f Standard 6/10 fig 44; 5 Nov Chelmsford (AW) Flat 10f Standard 11/14 fig 22
    DATA for: First-time headgear
    DATA against: Poor recent finishing positions; Pace: steady gallop likely, hard to come from off the pace
- Intsaar (hrs_64877372) | 3yo G | 135lb | OR 55 | draw 11 | jockey Miss Remie Morgan(7) | trainer Archie Watson (14d 2/4) | headgear - | last run 19 days | form 004 | MARKET 5.3% | 09:00 median 13.00 | Matchbook 19.00
    comment: Intsaar is hard to fancy, winless in his last three and unplaced in the two runs before a fourth last time out, 19 days ago.
    DATA: model 7.5% | style Held up (led 4% of runs) | runs in data 3 | last 3: 21 May Southwell Flat 8.1f Standard 10/12; 14 Oct Nottingham Flat 8.3f Good To Soft 10/14; 5 Nov Chelmsford (AW) Flat 7f Standard 4/5 fig 36
    DATA for: Official rating 55, 5 lb above field average
    DATA against: Best recent form figure 36, 8 lb below field average; Recent figures 19 lb below its current mark (looks high in the weights); Pace: steady gallop likely, hard to come from off the pace
- Akrivos (hrs_54712315) | 3yo G | 126lb | OR 46 | draw 3 | jockey Charles Bishop | trainer Ian Williams (14d 3/19) | headgear - | last run 217 days | form 744486 | MARKET 4.5% | 09:00 median 15.00 | Matchbook 24.00
    comment: Winless in his last six, Akrivos has bumped along with three fourths in that spell and a sixth last time out, and he has run over today's trip and going before.
    DATA: model 6.9% | style Held up (led 4% of runs) | runs in data 6 | last 3: 5 Mar Lingfield Flat 10f Standard 4/7; 26 Mar Southwell Flat 7.1f Standard 8/12; 21 Apr Yarmouth Flat 8f Good To Firm 6/9
    DATA against: Returns from a 217-day break; Pace: steady gallop likely, hard to come from off the pace
- Venturing (hrs_54149893) | 3yo G | 132lb | OR 52 | draw 13 | jockey Myla Coppins(5) | trainer Tony Carroll (14d 1/31) | headgear t | last run 28 days | form 448740 | MARKET 4.4% | 09:00 median 17.00 | Matchbook 22.00
    comment: The risk is a yard in poor form at 1/31, while he is yet to win in his last six and carries 132 lb from stall 13.
    DATA: model 5.2% | style Midfield (led 3% of runs) | runs in data 6 | last 3: 18 Aug Lingfield Flat 8f Standard 7/7; 21 Sep Wolverhampton Flat 9.5f Standard 4/11; 27 Oct Wolverhampton (AW) Flat 8.5f Standard 10/10 fig 34
    DATA against: Best recent form figure 34, 10 lb below field average; Recent figures 18 lb below its current mark (looks high in the weights)
- Turton (hrs_63908698) | 3yo G | 126lb | OR 45 | draw 7 | jockey Harry Davies | trainer Tony Carroll (14d 1/31) | headgear t | last run 19 days | form 569V04 | MARKET 4.0% | 09:00 median 17.00 | Matchbook 28.00
    comment: Turton was fourth last time out and has run over today's trip and going, while a 19-day break is no concern; however, he is winless in his last six outings and the yard is cold at 1/31 in the last 14 days.
    DATA: model 3.1% | style Prominent (led 23% of runs) | runs in data 8 | last 3: 22 Aug Lingfield Flat 12f Standard 9/9; 29 Sep Wolverhampton Flat 16.5f Standard 10/11; 5 Nov Chelmsford (AW) Flat 10f Standard 4/13 fig 50
    DATA for: Best recent form figure 50, 6 lb above field average; Recent figures 5 lb above its current mark (looks well handicapped)
- Parole Board (hrs_55948249) | 3yo F | 126lb | OR 44 | draw 14 | jockey Sean Levey | trainer Pat Phelan (14d 1/4) | headgear - | last run 224 days | form 058-78 | MARKET 2.3% | 09:00 median 34.00 | Matchbook 44.00
    comment: Winless in her last five, Parole Board has finished eighth, seventh and eighth in her last three outings and returns after 224 days off, which makes her hard to fancy from stall 14.
    DATA: model 3.1% | style Held up (led 5% of runs) | runs in data 2 | last 3: 21 Jan Lingfield Flat 8f Standard 7/8; 14 Apr Lingfield Flat 8f Standard 8/12
    DATA against: Official rating 44, 6 lb below field average; Returns from a 224-day break; Lightly raced: 2 runs in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Baggie Boy (hrs_59895794) | 3yo G | 130lb | OR 50 | draw 9 | jockey Edward Greatrex | trainer Grace Harris (14d 0/9) | headgear - | last run 27 days | form -68005 | MARKET 1.4% | 09:00 median 53.00 | Matchbook 120.00
    comment: Baggie Boy was a fifth last time out and is yet to win in his last five starts, though he has run on today's going and returns after 27 days.
    DATA: model 3.5% | style Held up (led 5% of runs) | runs in data 5 | last 3: 16 Mar Wolverhampton Flat 7.2f Standard 10/11; 21 Sep Wolverhampton Flat 7.2f Standard 10/10; 28 Oct Kempton (AW) Flat 8f Standard / Slow 5/6 fig 34
    DATA against: Best recent form figure 34, 10 lb below field average; Recent figures 16 lb below its current mark (looks high in the weights); Trainer 0 wins from 9 runs, last 14 days; Pace: steady gallop likely, hard to come from off the pace
- Emerald Reine (hrs_63422646) | 3yo F | 126lb | OR 44 | draw 1 | jockey Dylan Hogan | trainer Julia & Shelley Birkett (14d 0/2) | headgear b | last run 17 days | form 77970 | MARKET 1.4% | 09:00 median 67.00 | Matchbook 100.00
    comment: Emerald Reine has been well beaten lately, unplaced last time out, with a seventh two starts back and a ninth three starts back, and she is yet to win in that spell.
    DATA: model 2.7% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 27 May Kempton Flat 11f Standard To Slow 9/10; 21 Aug Ffos Las Flat 11.9f Good 7/10; 7 Nov Southwell (AW) Flat 12f Standard 10/10
    DATA against: Official rating 44, 6 lb below field average; Poor recent finishing positions
- Glamerous (hrs_60818457) | 3yo F | 129lb | OR 49 | draw 10 | jockey William Carver | trainer Simon Hodgson (14d 0/3) | headgear b (1st time) | last run 21 days | form 6457 | MARKET 1.1% | 09:00 median 67.00 | Matchbook 170.00
    comment: Glamerous is winless in her last four, finishing a seventh last time out, a fifth two starts back, a fourth three starts back and a sixth four starts back, so she is hard to fancy.
    DATA: model 2.2% | style Midfield (led 4% of runs) | runs in data 4 | last 3: 5 Feb Southwell Flat 11.1f Standard 4/4; 2 Mar Kempton Flat 12f Standard To Slow 5/9; 3 Nov Wolverhampton (AW) Flat 12f Standard 7/7
    DATA for: First-time headgear
    DATA against: Last-run finishing speed -10.0% vs that field (faded)
- Karmacy (hrs_56873754) | 3yo F | 128lb | OR 48 | draw 8 | jockey Kieran O'Neill | trainer Andrew Martin (14d 0/1) | headgear - | last run 27 days | form 8-87P8 | MARKET 1.1% | 09:00 median 67.00 | Matchbook 160.00
    comment: Karmacy is hard to fancy, having finished eighth last time out and, before that, pulled up, then a seventh and two more eighths, so she is winless in her last five.
    DATA: model 3.2% | style Prominent (led 5% of runs) | runs in data 4 | last 3: 12 May Lingfield Flat 7f Standard 7/8; 29 May Chepstow Flat 8.1f Good To Firm PU/7; 28 Oct Kempton (AW) Flat 8f Standard / Slow 8/10 fig 36
    DATA against: Best recent form figure 36, 8 lb below field average; Recent figures 12 lb below its current mark (looks high in the weights); Poor recent finishing positions
