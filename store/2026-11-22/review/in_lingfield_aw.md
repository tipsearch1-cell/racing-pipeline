# Card review packet: Lingfield (AW), 2026-11-22

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


## 11:25 Lingfield (AW) | race_id rac_32305149838 | All-Weather Championship Is Back "Hands And Heels" Apprentice Handicap Stakes (Part Of The Racing Excellence Series)
Flat | Class 5 | 7f1y | going Standard | AW | 12 runners | rating band 0-75 | age 3yo+
DATA pace: Even - Two likely leaders (Handle With Care, This Farh). A fair, even gallop is most likely.
- Mister Mojito (hrs_35257866) | 5yo G | 138lb | OR 75 | draw 12 | jockey Joe Bradnam | trainer T. J. Kent (14d 0/5) | headgear t | last run 18 days | form 562131 | MARKET 17.3% | 09:00 median 4.50 | Matchbook 5.50 | CHECK (skip line 4.27)
    comment: Mister Mojito arrives in cracking form, a winner last time out, a third two starts back, and a winner three starts back, and he has run over today's trip and going before. Fresh enough after 18 days, he looks a real threat, though 138 lb is the main concern.
    DATA: model 19.0% | style Held up (led 5% of runs) | runs in data 6 | last 3: 4 Aug Lingfield Flat 7f Standard 1/11; 15 Aug Newmarket Flat 7f Good To Firm 3/6; 4 Nov Kempton (AW) Flat 7f Standard / Slow 1/11 fig 79
    DATA for: Best recent form figure 79, 8 lb above field average; Recent figures 4 lb above its current mark (looks well handicapped); Has won at this trip or further; Good recent finishing positions
    DATA against: Course: hold-up horses have won 0.7× their fair share at 7f here
- Stenmark (hrs_41939156) | 4yo G | 138lb | OR 75 | draw 4 | jockey Oliver Hoodless(3) | trainer Gihan Arnolda (14d 0/4) | headgear - | last run 22 days | form 538260 | MARKET 14.9% | 09:00 median 5.50 | Matchbook 6.20
    comment: Stenmark is yet to win in his last six starts but has hit the frame twice, a second three starts back and a third five starts back, and he has run over today's trip and going. Unplaced last time out and 22 days since that run, he carries 138 lb from stall four, so he looks a solid midfield sort rather than a clear threat.
    DATA: model 8.2% | style Midfield (led 4% of runs) | runs in data 7 | last 3: 9 Jul Epsom Downs Flat 7f Good To Firm 2/6; 16 Jul Chepstow Flat 8.1f Good To Firm 6/6; 31 Oct Newmarket Flat 7f Good To Soft 12/16 fig 62
    DATA against: Best recent form figure 62, 9 lb below field average; Recent figures 13 lb below its current mark (looks high in the weights)
- Lady Mariko (hrs_47098863) | 4yo F | 138lb | OR 75 | draw 6 | jockey Hope Regan(5) | trainer Dylan Cunha (14d 1/6) | headgear - | last run 17 days | form 600461 | MARKET 11.7% | 09:00 median 7.00 | Matchbook 7.80
    comment: Lady Mariko won last time out just 17 days ago and has run over today's trip and going before, so she arrives fresh and in form. The risk is a patchy record before that, with a sixth two starts back, and 138 lb to carry from stall six.
    DATA: model 16.6% | style Midfield (led 4% of runs) | runs in data 11 | last 3: 6 Oct Southwell Flat 7.1f Standard 4/10; 21 Oct Kempton (AW) Flat 6f Standard / Slow 6/11 fig 66; 5 Nov Southwell (AW) Flat 7f Standard 1/10 fig 80
    DATA for: Best recent form figure 80, 9 lb above field average; Recent figures 5 lb above its current mark (looks well handicapped); Has won at this trip or further
- Handle With Care (hrs_43002505) | 4yo F | 138lb | OR 75 | draw 7 | jockey Chloe Lyons | trainer Marco Botti (14d 0/8) | headgear - | last run 20 days | form 347136 | MARKET 11.5% | 09:00 median 7.00 | Matchbook 8.20
    comment: Handle With Care has a solid profile, a winner three starts back and a third two starts back, and she has run over today's trip and going before, returning fresh after 20 days.
    DATA: model 11.5% | style Leader (led 43% of runs) | runs in data 6 | last 3: 12 May Lingfield Flat 7f Standard 1/9; 22 Sep Southwell Flat 7.1f Standard 3/12; 2 Nov Chelmsford (AW) Flat 7f Standard 6/8 fig 71
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Trainer 0 wins from 8 runs, last 14 days
- Arantes Nascimento (hrs_36588559) | 5yo G | 134lb | OR 71 | draw 8 | jockey James Glennon(5) | trainer Michael Attwater (14d 1/4) | headgear - | last run 31 days | form 226657 | MARKET 11.4% | 09:00 median 7.25 | Matchbook 8.00
    comment: Without a win in his last six, his latest seventh is the one reservation, but a 31-day break and an official mark of 71 give him a good chance.
    DATA: model 5.8% | style Prominent (led 4% of runs) | runs in data 11 | last 3: 8 Aug Lingfield Flat 7f Standard 6/7; 7 Oct Kempton Flat 7f Standard To Slow 5/8; 22 Oct Newmarket Flat 7f Soft 7/12 fig 69
    DATA for: Has won at this trip or further
- This Farh (hrs_43508444) | 4yo G | 134lb | OR 71 | draw 1 | jockey Jude Maher(5) | trainer David Loughnane (14d 1/4) | headgear p | last run 17 days | form 145666 | MARKET 7.0% | 09:00 median 11.00 | Matchbook 14.00
    comment: This Farh has finished sixth in each of his last three outings and has slipped steadily since winning six starts back, though he's fresh enough after 17 days and has run over today's trip and going.
    DATA: model 5.0% | style Leader (led 54% of runs) | runs in data 11 | last 3: 22 Sep Beverley Flat 7.3f Good 6/10; 2 Oct Wolverhampton Flat 7.2f Standard 6/9; 5 Nov Chelmsford (AW) Flat 7.5f Standard 6/11 fig 69
    DATA for: Has won at this trip or further
    DATA against: Poor recent finishing positions
- Guilty Verdict (hrs_55484597) | 3yo G | 126lb | OR 64 | draw 2 | jockey Molly Keegan-Price(3) | trainer Jim Boyle (14d 0/3) | headgear - | last run 23 days | form 39-926 | MARKET 6.6% | 09:00 median 11.00 | Matchbook 16.00
    comment: Guilty Verdict is winless in his last five, with a sixth last time out and two ninths in the book, so he's hard to fancy; a second two starts back and a third five starts back show he can hit the frame, and he has run over today's trip.
    DATA: model 6.7% | style Midfield (led 8% of runs) | runs in data 3 | last 3: 29 Sep Bath Flat 5.7f Good To Firm 9/9; 22 Oct Newmarket Flat 8f Soft 2/13 fig 72; 30 Oct Newmarket Flat 8f Good To Soft 6/15 fig 60
    DATA for: Recent figures 8 lb above its current mark (looks well handicapped); Carries 8 lb less than average
    DATA against: Official rating 64, 7 lb below field average
- Viking Glory (hrs_55763918) | 3yo G | 130lb | OR 68 | draw 5 | jockey Lloyd Applegate(7) | trainer Dr Richard Newland (14d 1/4) | headgear tp | last run 32 days | form 317471 | MARKET 4.9% | 09:00 median 13.00 | Matchbook 24.00
    comment: He has run over today's trip and going, and 130 lb from draw 5 after 32 days off is no easy task.
    DATA: model 8.2% | style Unknown | runs in data 10 | last 3: 17 Sep Yarmouth Flat 7f Good 4/13; 28 Sep Brighton Flat 7f Good To Firm 7/10; 21 Oct Kempton (AW) Flat 7f Standard / Slow 1/10 fig 67
    DATA for: Has won at this trip or further
- H Key Lails (hrs_31069556) | 6yo G | 134lb | OR 71 | draw 9 | jockey Jude Fernandes | trainer Michael Attwater (14d 1/4) | headgear p | last run 83 days | form 317747 | MARKET 4.5% | 09:00 median 17.00 | Matchbook 22.00
    comment: H Key Lails has finished seventh in two of his last three outings, including last time, and returns after an 83-day break, which makes him hard to fancy. On the plus side, he has run over today's trip and going, and a winner five starts back shows he can score.
    DATA: model 4.2% | style Prominent (led 23% of runs) | runs in data 8 | last 3: 24 Jul Ascot Flat 7f Good To Firm 7/11; 6 Aug Sandown Flat 8f Good To Firm 4/6; 31 Aug Epsom Downs Flat 8.5f Good To Soft 7/8
    DATA for: Has won at this trip or further
- Mighty Vega (hrs_51273138) | 3yo G | 132lb | OR 70 | draw 3 | jockey Isobelle Chalmers | trainer Scott Dixon (14d 0/1) | headgear tp | last run 17 days | form 130750 | MARKET 3.7% | 09:00 median 21.00 | Matchbook 27.00
    comment: Mighty Vega arrives 17 days after an unplaced run, with a fifth two starts back and a seventh before that, so recent form is modest, though he did win six starts back.
    DATA: model 3.4% | style Midfield (led 3% of runs) | runs in data 14 | last 3: 26 Sep Southwell Flat 6.1f Standard 7/13; 22 Oct Southwell (AW) Flat 6f Standard 5/9 fig 69; 5 Nov Chelmsford (AW) Flat 7.5f Standard 11/11 fig 54
    DATA for: Has won at this trip or further
- Mr Ubiquitous (hrs_41597059) | 4yo G | 134lb | OR 71 | draw 10 | jockey Travis Ford(7) | trainer Harry Eustace (14d 0/6) | headgear - | last run 73 days | form 150548 | MARKET 3.4% | 09:00 median 20.00 | Matchbook 36.00
    comment: Mr Ubiquitous is hard to fancy, having finished eighth last time out and been beaten in all five starts since a win six starts back, with 73 days off since.
    DATA: model 5.0% | style Midfield (led 5% of runs) | runs in data 6 | last 3: 23 Jul Yarmouth Flat 7f Good To Firm 5/6; 14 Aug Newmarket Flat 8f Good To Firm 4/8; 10 Sep Epsom Downs Flat 8.5f Good To Soft 8/9
    DATA for: Has won at this trip or further
- Thankuappreciate (hrs_30865681) | 6yo G | 131lb | OR 68 | draw 11 | jockey Ben Pollard(5) | trainer Tony Carroll (14d 1/22) | headgear - | last run 69 days | form 413457 | MARKET 3.1% | 09:00 median 23.00 | Matchbook 36.00
    comment: Thankuappreciate has run over today's trip and on this going, and he won five starts back, but he's tailed off since with a seventh last time out.
    DATA: model 6.2% | style Held up (led 4% of runs) | runs in data 6 | last 3: 11 Mar Southwell Flat 7.1f Standard 4/9; 11 Apr Southwell Flat 6.1f Standard 5/8; 14 Sep Windsor Flat 6.1f Good To Soft 7/13
    DATA against: Course: hold-up horses have won 0.7× their fair share at 7f here

## 11:55 Lingfield (AW) | race_id rac_32305591474 | AWC Season 14 Has Begun EBF Novice Stakes (Div I) (GBB/GBBPlus Race)
Flat | Class 3 | 1m1y | going Standard | AW | 11 runners | rating band - | age 2yo
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Arkat (hrs_17394169100) | 2yo C | 133lb | OR - | draw 4 | jockey Callum Rodriguez | trainer Roger Varian (14d 4/6) | headgear - | last run 23 days | form 3 | MARKET 30.2% | 09:00 median 2.69 | Matchbook 3.15
    DATA: model 20.6% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 30 Oct Newmarket Flat 7f Good To Soft 3/12 fig 55
    DATA for: Best recent form figure 55, 9 lb above field average; Trainer 67% wins (4/6), last 14 days
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Reign Over All (hrs_17394442366) | 2yo C | 133lb | OR - | draw 10 | jockey William Buick | trainer Owen Burrows (14d 0/3) | headgear - | last run 23 days | form 5 | MARKET 24.1% | 09:00 median 3.50 | Matchbook 3.85
    DATA: model 17.4% | style Held up (led 8% of runs) | runs in data 1 | last 3: 30 Oct Newmarket Flat 7f Good To Soft 5/12 fig 54
    DATA for: Best recent form figure 54, 8 lb above field average
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Rey de Vega (hrs_17391009853) | 2yo C | 133lb | OR - | draw 12 | jockey Billy Loughnane | trainer George Boughey (14d 5/15) | headgear - | last run - days | form - | MARKET 13.1% | 09:00 median 6.50 | Matchbook 7.20
    DATA: model 6.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 33% wins (5/15), last 14 days
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Medvedev (hrs_17394670783) | 2yo C | 133lb | OR - | draw 3 | jockey Cieren Fallon | trainer William Haggas (14d 3/12) | headgear - | last run 23 days | form 8 | MARKET 6.6% | 09:00 median 12.00 | Matchbook 15.50
    DATA: model 9.6% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 30 Oct Newmarket Flat 7f Good To Soft 8/12 fig 44
    DATA for: Trainer 25% wins (3/12), last 14 days
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Ordnance (hrs_17395811825) | 2yo G | 133lb | OR - | draw 6 | jockey Oisin Murphy | trainer Andrew Balding (14d 2/23) | headgear - | last run - days | form - | MARKET 6.0% | 09:00 median 14.50 | Matchbook 15.00
    DATA: model 6.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Frankenstyne (hrs_17395808696) | 2yo G | 133lb | OR - | draw 2 | jockey George Bass | trainer Jack Channon (14d 0/5) | headgear - | last run - days | form - | MARKET 5.8% | 09:00 median 13.00 | Matchbook 17.50
    DATA: model 6.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Basics (hrs_17394909630) | 2yo G | 133lb | OR - | draw 1 | jockey Harry Davies | trainer Simon Crisford (14d 1/4) | headgear t | last run 18 days | form 5 | MARKET 5.4% | 09:00 median 13.00 | Matchbook 21.00
    DATA: model 17.9% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 4 Nov Kempton (AW) Flat 8f Standard / Slow 5/13 fig 56
    DATA for: Best recent form figure 56, 10 lb above field average
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Toderby (hrs_17395121359) | 2yo C | 133lb | OR - | draw 5 | jockey Kieran Shoemark | trainer Ed Walker (14d 0/12) | headgear - | last run - days | form - | MARKET 5.4% | 09:00 median 15.00 | Matchbook 18.00
    DATA: model 6.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Trainer 0 wins from 12 runs, last 14 days; Lightly raced: 0 runs in our data, so the model has little to go on
- Rupertsbeenrumbled (hrs_17393053090) | 2yo G | 133lb | OR - | draw 8 | jockey Robbie Downey | trainer David Evans (14d 0/8) | headgear - | last run 24 days | form 97 | MARKET 1.9% | 09:00 median 51.00 | Matchbook 65.00
    DATA: model 2.8% | style Held up (led 5% of runs) | runs in data 2 | last 3: 19 Oct Bath Flat 8f Good To Soft 9/10 fig 33; 29 Oct Bath Flat 8f Soft 7/10 fig 44
    DATA against: Trainer 0 wins from 8 runs, last 14 days; Last-run finishing speed -2.1% vs that field (faded); Lightly raced: 2 runs in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Dashing Digger (hrs_64780548) | 2yo C | 133lb | OR - | draw 7 | jockey Hollie Doyle | trainer William Stone (14d 0/1) | headgear - | last run 31 days | form 66 | MARKET 1.0% | 09:00 median 81.00 | Matchbook 100.00
    DATA: model 3.8% | style Held up (led 5% of runs) | runs in data 2 | last 3: 18 May Lingfield Flat 7f Good 6/6; 22 Oct Newmarket Flat 8f Soft 6/9 fig 31
    DATA against: Best recent form figure 31, 15 lb below field average; Lightly raced: 2 runs in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Stellar Max (hrs_17392563923) | 2yo C | 133lb | OR - | draw 11 | jockey Luke Morris | trainer Sir Mark Prescott Bt (14d 0/3) | headgear - | last run 29 days | form 079 | MARKET 0.7% | 09:00 median 101.00 | Matchbook 210.00
    DATA: model 1.9% | style Held up (led 8% of runs) | runs in data 3 | last 3: 30 Sep Kempton Flat 8f Standard To Slow 11/11; 12 Oct Yarmouth Flat 7f Good To Soft 7/7; 24 Oct Southwell (AW) Flat 8f Standard 9/10 fig 39
    DATA against: Best recent form figure 39, 7 lb below field average; Poor recent finishing positions; Pace: steady gallop likely, hard to come from off the pace

## 12:25 Lingfield (AW) | race_id rac_32305151775 | AWC Season 14 Has Begun EBF Novice Stakes (Div II) (GBB/GBBPlus Race)
Flat | Class 3 | 1m1y | going Standard | AW | 10 runners | rating band - | age 2yo
DATA pace: Unclear - Running styles known for only 4 of 10 runners.
- Sea Fortress (hrs_17395644945) | 2yo C | 133lb | OR - | draw 11 | jockey William Buick | trainer John & Thady Gosden (14d 2/17) | headgear h (1st time) | last run - days | form - | MARKET 32.8% | 09:00 median 2.63 | Matchbook 2.74
    DATA: model 8.0% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: First-time headgear
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Quorum (hrs_17392812157) | 2yo C | 133lb | OR - | draw 8 | jockey Cieren Fallon | trainer William Haggas (14d 3/12) | headgear - | last run 58 days | form 9 | MARKET 30.3% | 09:00 median 2.62 | Matchbook 3.20
    DATA: model 24.7% | style Held up (led 8% of runs) | runs in data 1 | last 3: 25 Sep Newmarket Flat 7f Good 9/14
    DATA for: Trainer 25% wins (3/12), last 14 days
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Shareek (hrs_17392230163) | 2yo C | 133lb | OR - | draw 5 | jockey Callum Rodriguez | trainer Owen Burrows (14d 0/3) | headgear - | last run 48 days | form 5 | MARKET 17.4% | 09:00 median 4.75 | Matchbook 5.30
    DATA: model 19.6% | style Held up (led 8% of runs) | runs in data 1 | last 3: 5 Oct Kempton Flat 8f Standard To Slow 5/8
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Lady's Mantle (hrs_17395697095) | 2yo F | 128lb | OR - | draw 1 | jockey Oisin Murphy | trainer Andrew Balding (14d 2/23) | headgear - | last run - days | form - | MARKET 6.7% | 09:00 median 11.00 | Matchbook 16.00
    DATA: model 7.9% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Two of A Kind (hrs_17395812868) | 2yo C | 133lb | OR - | draw 4 | jockey Billy Loughnane | trainer Ollie Sangster (14d 1/4) | headgear - | last run - days | form - | MARKET 5.8% | 09:00 median 13.00 | Matchbook 18.50
    DATA: model 8.0% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Victory Max (hrs_17394844964) | 2yo G | 133lb | OR - | draw 2 | jockey George Wood | trainer Harry Eustace (14d 0/6) | headgear - | last run - days | form - | MARKET 2.5% | 09:00 median 29.00 | Matchbook 55.00
    DATA: model 8.0% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Magari (hrs_17395810782) | 2yo C | 133lb | OR - | draw 3 | jockey David Egan | trainer S. P. C. Woods (14d 0/5) | headgear - | last run - days | form - | MARKET 2.1% | 09:00 median 41.00 | Matchbook 48.00
    DATA: model 8.0% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Greenhurst (hrs_17394160756) | 2yo C | 133lb | OR - | draw 6 | jockey Gina Mangan | trainer Dr Richard Newland (14d 1/4) | headgear - | last run - days | form - | MARKET 1.3% | 09:00 median 51.00 | Matchbook 130.00
    DATA: model 8.0% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Cinq Coins (hrs_17390311043) | 2yo G | 133lb | OR - | draw 9 | jockey Joe Leavy | trainer Roger Teal (14d 0/5) | headgear - | last run 60 days | form 57 | MARKET 0.7% | 09:00 median 101.00 | Matchbook 270.00
    DATA: model 4.7% | style Held up (led 8% of runs) | runs in data 2 | last 3: 6 Aug Brighton Flat 7f Good To Firm 5/5; 23 Sep Kempton Flat 8f Standard To Slow 7/9
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Wowaditaka (hrs_17392688040) | 2yo G | 133lb | OR - | draw 10 | jockey Luke Morris | trainer Sir Mark Prescott Bt (14d 0/3) | headgear - | last run 34 days | form 00 | MARKET 0.4% | 09:00 median 201.00 | Matchbook 400.00
    DATA: model 3.1% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 1 Oct Salisbury Flat 7f Soft 12/12; 19 Oct Bath Flat 8f Good To Soft 10/10 fig 24
    DATA against: Last-run finishing speed -5.3% vs that field (faded); Lightly raced: 2 runs in our data, so the model has little to go on

## 12:55 Lingfield (AW) | race_id rac_32305153712 | Midnite A Next Generation Betting App Novice Stakes (GBB/GBBPlus Race)
Flat | Class 3 | 1m2f1y | going Standard | AW | 10 runners | rating band - | age 3yo+
DATA pace: Unclear - Running styles known for only 3 of 10 runners.
- Olympic Charter (hrs_63422751) | 3yo G | 137lb | OR - | draw 4 | jockey William Buick | trainer Charlie Appleby (14d 2/4) | headgear - | last run 228 days | form 1 | MARKET 45.3% | 09:00 median 1.91 | Matchbook 1.99
    DATA: model 28.5% | style Unknown | runs in data 1 | last 3: 8 Apr Nottingham Flat 10.2f Good 1/9
    DATA for: Last-run finishing speed +2.2% vs that field (finished strongly); Has won at this trip or further
    DATA against: Returns from a 228-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Aqeeq (hrs_17395815997) | 3yo C | 130lb | OR - | draw 3 | jockey Oisin Murphy | trainer Saeed bin Suroor (14d 0/0) | headgear - | last run - days | form - | MARKET 14.1% | 09:00 median 6.00 | Matchbook 6.80
    DATA: model 7.2% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Medaali (hrs_17393646557) | 3yo G | 130lb | OR - | draw 5 | jockey Callum Shepherd | trainer Simon Crisford (14d 1/4) | headgear t | last run 20 days | form 53 | MARKET 10.4% | 09:00 median 7.25 | Matchbook 9.80
    DATA: model 18.0% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 14 Oct Nottingham Flat 8.3f Good To Soft 5/14; 2 Nov Wolverhampton (AW) Flat 9.5f Standard 3/10 fig 60
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Nada Two (hrs_55947633) | 3yo F | 125lb | OR - | draw 6 | jockey Clifford Lee | trainer James Tate (14d 0/3) | headgear - | last run 421 days | form 22- | MARKET 8.8% | 09:00 median 9.00 | Matchbook 11.00
    DATA: model 7.1% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 421-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Maneuver (hrs_55764443) | 3yo F | 125lb | OR - | draw 9 | jockey Robert Havlin | trainer John & Thady Gosden (14d 2/17) | headgear - | last run 51 days | form 23-U | MARKET 8.1% | 09:00 median 9.50 | Matchbook 12.50
    DATA: model 5.1% | style Unknown | runs in data 1 | last 3: 2 Oct Newcastle Flat 8f Standard UR/6
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Al Kairouan (hrs_17395814954) | 3yo C | 130lb | OR - | draw 2 | jockey Kieran Shoemark | trainer Saeed bin Suroor (14d 0/0) | headgear - | last run - days | form - | MARKET 7.4% | 09:00 median 10.00 | Matchbook 15.00
    DATA: model 7.2% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Light Snowfall (hrs_66272276) | 3yo F | 125lb | OR - | draw 8 | jockey Billy Loughnane | trainer Saeed bin Suroor (14d 0/0) | headgear - | last run 43 days | form 4 | MARKET 3.3% | 09:00 median 19.00 | Matchbook 38.00
    DATA: model 11.5% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 10 Oct Southwell Flat 7.1f Standard 4/7
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- A'Ellie (hrs_17395813911) | 3yo F | 125lb | OR - | draw 7 | jockey Rob Hornby | trainer James Keane (14d 1/1) | headgear - | last run - days | form - | MARKET 1.1% | 09:00 median 81.00 | Matchbook 110.00
    DATA: model 7.1% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Jackabean (hrs_17395817040) | 3yo G | 130lb | OR - | draw 10 | jockey Joe Leavy | trainer Jack Morland (14d 0/3) | headgear t (1st time) | wind surgery | last run - days | form - | MARKET 0.9% | 09:00 median 101.00 | Matchbook 130.00
    DATA: model 7.2% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: First-time headgear
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Anchor (hrs_62876324) | 4yo G | 133lb | OR - | draw 1 | jockey Jack Doughty | trainer Clare Hobson (14d 0/3) | headgear b | last run 81 days | form 06 | MARKET 0.4% | 09:00 median 201.00 | Matchbook 420.00
    DATA: model 1.1% | style Held up (led 5% of runs) | runs in data 3 | last 3: 24 Mar Southwell NH Flat 15.8f Good 7/7; 5 Aug Kempton Flat 11f Standard To Slow 12/12; 2 Sep Kempton Flat 11f Standard To Slow 6/6
    DATA against: Poor recent finishing positions

## 1:25 Lingfield (AW) | race_id rac_32305155649 | Midnite It's Actually Pretty Good Handicap Stakes (GBBPlus Race)
Flat | Class 4 | 1m2f1y | going Standard | AW | 8 runners | rating band 0-85 | age 3yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Merci Monsieur (hrs_56007959) | 3yo G | 132lb | OR 80 | draw 1 | jockey Oisin Murphy | trainer Andrew Balding (14d 2/23) | headgear - | last run 27 days | form 35-1 | MARKET 32.8% | 09:00 median 2.75 | Matchbook 2.84
    comment: Merci Monsieur won last time out and has run over today's trip and going, but he is hard to fancy off an official 80, carrying 132 lb from stall one.
    DATA: model 37.0% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 26 Oct Redcar Flat 10f Heavy 1/10 fig 60
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 60, 14 lb below field average; Recent figures 20 lb below its current mark (looks high in the weights); Lightly raced: 1 run in our data, so the model has little to go on
- Duke's Command (hrs_36738786) | 5yo G | 139lb | OR 84 | draw 9 | jockey Billy Loughnane | trainer David O'Meara (14d 0/11) | headgear - | last run 34 days | form 508365 | MARKET 16.8% | 09:00 median 5.00 | Matchbook 5.90
    comment: Duke's Command is yet to win in his last six starts, but a third three starts back is the pick of his recent form, and he has run over today's trip and going before.
    DATA: model 13.1% | style Midfield (led 3% of runs) | runs in data 9 | last 3: 22 Sep Southwell Flat 8.1f Standard 3/9; 7 Oct Nottingham Flat 8.3f Good To Soft 6/9; 19 Oct Southwell (AW) Flat 8f Standard 5/11 fig 86
    DATA for: Best recent form figure 86, 12 lb above field average; Last-run finishing speed +2.4% vs that field (finished strongly)
    DATA against: Trainer 0 wins from 11 runs, last 14 days; Carries 5 lb more than average
- Politely (hrs_53633055) | 3yo F | 134lb | OR 82 | draw 5 | jockey Callum Rodriguez | trainer Owen Burrows (14d 0/3) | headgear - | last run 19 days | form 115952 | MARKET 16.7% | 09:00 median 5.00 | Matchbook 5.90
    comment: Politely bounces back from a ninth three starts back with a second last time out, and she has won twice in her last six, though those wins came five and six starts back.
    DATA: model 12.9% | style Midfield (led 3% of runs) | runs in data 6 | last 3: 19 Jun Goodwood Flat 8f Good 9/10; 22 Sep Southwell Flat 8.1f Standard 5/11; 3 Nov Wolverhampton (AW) Flat 8.5f Standard 2/6 fig 80
    DATA for: Best recent form figure 80, 6 lb above field average
- Gilet (hrs_42521864) | 4yo G | 132lb | OR 77 | draw 3 | jockey Edward Greatrex | trainer Warren Greatrex (14d 6/17) | headgear - | last run 27 days | form 4-3665 | MARKET 10.8% | 09:00 median 8.00 | Matchbook 9.00
    comment: The risk is a winless run, with fifth last time out following two sixths.
    DATA: model 11.5% | style Midfield (led 5% of runs) | runs in data 4 | last 3: 4 Sep Kempton Flat 7f Standard To Slow 6/13; 30 Sep Kempton Flat 8f Standard To Slow 6/13; 26 Oct Kempton (AW) Flat 8f Standard / Slow 5/13 fig 77
    DATA for: Trainer 35% wins (6/17), last 14 days
- Crack On Boys (hrs_47621553) | 4yo G | 137lb | OR 82 | draw 8 | jockey David Egan | trainer Tom Clover (14d 0/1) | headgear - | last run 41 days | form 56-898 | MARKET 10.1% | 09:00 median 8.50 | Matchbook 9.60
    comment: The risk is form figures of eighth, ninth, eighth in his last three outings.
    DATA: model 7.7% | style Midfield (led 8% of runs) | runs in data 3 | last 3: 16 Jan Newcastle Flat 8f Standard 8/9; 20 Feb Southwell Flat 8.1f Standard 9/12; 12 Oct Kempton Flat 8f Standard To Slow 8/14
    DATA against: Poor recent finishing positions
- Wyld Bill (hrs_40514663) | 5yo G | 142lb | OR 87 | draw 6 | jockey Jack Dace(5) | trainer Gihan Arnolda (14d 0/4) | headgear b | last run 18 days | form -13500 | MARKET 6.9% | 09:00 median 13.00 | Matchbook 13.50
    comment: The main risk is two unplaced runs since a fifth three starts back, though he's back after 18 days off, and he carries 142 lb from draw 6.
    DATA: model 4.8% | style Midfield (led 4% of runs) | runs in data 5 | last 3: 3 Apr Lingfield Flat 10f Standard 5/14; 10 Oct York Flat 10.3f Soft 18/18; 4 Nov Nottingham Flat 8.5f Soft 10/14 fig 71
    DATA for: Official rating 87, 8 lb above field average; Has won at this trip or further
    DATA against: Recent figures 16 lb below its current mark (looks high in the weights); Last-run finishing speed -2.0% vs that field (faded); Carries 8 lb more than average
- Caledonian (hrs_43228864) | 4yo G | 126lb | OR 71 | draw 2 | jockey Callum Shepherd | trainer David Simcock (14d 0/5) | headgear - | last run 20 days | form 584551 | MARKET 4.0% | 09:00 median 19.00 | Matchbook 27.00
    comment: Fresh from a run 20 days ago, he has run over today's trip and going, which is something in his favour.
    DATA: model 7.7% | style Held up (led 4% of runs) | runs in data 6 | last 3: 21 Jul Wolverhampton Flat 9.5f Standard 5/13; 17 Oct Southwell (AW) Flat 11f Standard 5/6 fig 59; 2 Nov Wolverhampton (AW) Flat 9.5f Standard 1/9 fig 69
    DATA for: Has won at this trip or further; Carries 8 lb less than average
    DATA against: Best recent form figure 69, 5 lb below field average; Official rating 71, 8 lb below field average; Pace: steady gallop likely, hard to come from off the pace
- Francesi (hrs_26975004) | 7yo G | 127lb | OR 72 | draw 4 | jockey Myla Coppins(5) | trainer Tony Carroll (14d 1/22) | headgear - | last run 40 days | form 573743 | MARKET 1.9% | 09:00 median 41.00 | Matchbook 60.00
    comment: Francesi is winless in his last six, though he was third last time and has run over today's trip and going before.
    DATA: model 5.4% | style Midfield (led 4% of runs) | runs in data 12 | last 3: 3 Apr Lingfield Flat 12f Standard 7/15; 19 Sep Newmarket Flat 9f Good 4/14; 13 Oct Leicester Flat 8.2f Good To Soft 3/9
    DATA for: Carries 7 lb less than average
    DATA against: Official rating 72, 7 lb below field average; Aged 7, older than most of this field

## 1:55 Lingfield (AW) | race_id rac_32305157586 | AWC Finals Day At Newcastle 26th March Fillies' Handicap Stakes
Flat | Class 5 | 1m1y | going Standard | AW | 9 runners | rating band 0-75 | age 3yo+
DATA pace: Lone leader - Eazy On The Eye is the only habitual front-runner and may be allowed an easy lead.
- Maria da Silva (hrs_49141575) | 3yo F | 135lb | OR 74 | draw 6 | jockey Oisin Murphy | trainer Andrew Balding (14d 2/23) | headgear - | last run 25 days | form 114451 | MARKET 38.8% | 09:00 median 2.20 | Matchbook 2.40
    comment: Won last time out and has three wins in her last six starts, though a fifth and two fourths in between show she can be inconsistent; she has run over today's trip and going, and 25 days since her last run is fine.
    DATA: model 23.2% | style Midfield (led 3% of runs) | runs in data 6 | last 3: 14 Sep Windsor Flat 8.1f Good To Soft 4/12; 12 Oct Newcastle Flat 8f Standard 5/11; 28 Oct Kempton (AW) Flat 8f Standard / Slow 1/9 fig 73
    DATA for: Has won at this trip or further
- Lady Milton (hrs_55177654) | 3yo F | 133lb | OR 72 | draw 8 | jockey Rob Hornby | trainer Jonathan Portman (14d 1/9) | headgear - | last run 86 days | form 123230 | MARKET 10.2% | 09:00 median 8.50 | Matchbook 9.20
    comment: The risk is an 86-day absence and an unplaced run last time out.
    DATA: model 11.6% | style Prominent (led 4% of runs) | runs in data 6 | last 3: 13 Jul Windsor Flat 10f Good To Firm 2/5; 29 Jul Sandown Flat 9.9f Good To Firm 3/10; 28 Aug Goodwood Flat 9.9f Good To Firm 11/12
    DATA for: Has won at this trip or further; Good recent finishing positions
- Eazy On The Eye (hrs_45314892) | 4yo F | 136lb | OR 73 | draw 3 | jockey George Wood | trainer Heather Main (14d 0/2) | headgear - | last run 31 days | form 222712 | MARKET 9.3% | 09:00 median 8.50 | Matchbook 11.00
    comment: Eazy On The Eye arrives in cracking nick, second last time out and a winner two starts back, with four runner-up finishes in her last six, and she has run over today's trip and on the going.
    DATA: model 18.3% | style Leader (led 43% of runs) | runs in data 11 | last 3: 4 Sep Ascot Flat 8f Good 7/11; 27 Sep Epsom Downs Flat 7f Good 1/10; 22 Oct Newmarket Flat 7f Soft 2/12 fig 89
    DATA for: Best recent form figure 89, 15 lb above field average; Recent figures 16 lb above its current mark (looks well handicapped); Last-run finishing speed +3.9% vs that field (finished strongly); Good recent finishing positions; Pace: may get an uncontested lead
- Lahan Kingman (hrs_55454084) | 3yo F | 129lb | OR 68 | draw 5 | jockey Finley Marsh | trainer Richard Hughes (14d 1/10) | headgear b | last run 6 days | form 244275 | MARKET 9.2% | 09:00 median 9.00 | Matchbook 10.50
    comment: Yet to win in her last six, Lahan Kingman has been consistent enough, with a second three starts back and another six starts back, and she has run over today's trip and going.
    DATA: model 10.4% | style Midfield (led 5% of runs) | runs in data 7 | last 3: 2 Oct Wolverhampton Flat 6.1f Standard 2/7; 21 Oct Kempton (AW) Flat 6f Standard / Slow 7/11 fig 65; 16 Nov Wolverhampton (AW) Flat 8.5f Standard 5/12 fig 64
    DATA against: Best recent form figure 65, 9 lb below field average
- Madame de Sevigne (hrs_36864919) | 5yo M | 134lb | OR 71 | draw 9 | jockey Darragh Keenan | trainer Des Donovan (14d 1/2) | headgear - | last run 92 days | form 387904 | MARKET 9.0% | 09:00 median 9.00 | Matchbook 11.00
    comment: The risk is a 92-day absence, with her last six runs also yielding no win.
    DATA: model 4.7% | style Midfield (led 4% of runs) | runs in data 8 | last 3: 19 Jun Newmarket Flat 7f Good 9/10; 25 Jul York Flat 7.9f Good To Firm 14/15; 22 Aug Lingfield Flat 8f Standard 4/6
    DATA against: Returns from a 92-day break
- Hamdania (hrs_58931236) | 3yo F | 132lb | OR 71 | draw 1 | jockey Callum Rodriguez | trainer James Horton (14d 0/3) | headgear v (1st time) | last run 20 days | form 1-2864 | MARKET 7.0% | 09:00 median 12.00 | Matchbook 14.00
    comment: Hamdania has been on the upgrade, with a fourth last time out following a sixth and an eighth, but her win came five starts back, so she is hard to fancy.
    DATA: model 7.9% | style Prominent (led 29% of runs) | runs in data 4 | last 3: 24 Sep Southwell Flat 11.1f Standard 8/12; 12 Oct Yarmouth Flat 11.5f Good To Soft 6/12; 2 Nov Chelmsford (AW) Flat 10f Standard 4/8 fig 71
    DATA for: First-time headgear
- Nakaaha (hrs_46667985) | 4yo F | 137lb | OR 74 | draw 4 | jockey David Egan | trainer Grace Harris (14d 1/8) | headgear h | last run 17 days | form 020747 | MARKET 6.9% | 09:00 median 12.00 | Matchbook 14.50
    DATA: model 8.9% | style Held up (led 4% of runs) | runs in data 12 | last 3: 3 Oct Southwell Flat 8.1f Standard 7/13; 22 Oct Southwell (AW) Flat 8f Standard 4/11 fig 73; 5 Nov Chelmsford (AW) Flat 7.5f Standard 7/11 fig 70
    DATA for: Has won at this trip or further
- Cixi (hrs_57102829) | 3yo F | 124lb | OR 63 | draw 7 | jockey Robert Havlin | trainer Jim Boyle (14d 0/3) | headgear - | last run 46 days | form 407635 | MARKET 5.7% | 09:00 median 13.00 | Matchbook 19.00
    comment: Cixi is winless in her last six, with a third two starts back and a fourth six starts back her best efforts, and she returns after 46 days off.
    DATA: model 6.3% | style Held up (led 5% of runs) | runs in data 7 | last 3: 3 Sep Lingfield Flat 7f Standard 6/10; 28 Sep Brighton Flat 7f Good To Firm 3/10; 7 Oct Kempton Flat 7f Standard To Slow 5/14
    DATA for: Carries 9 lb less than average
    DATA against: Official rating 63, 8 lb below field average
- Aura Champagne (hrs_56219415) | 3yo F | 136lb | OR 75 | draw 2 | jockey Joe Leavy | trainer Richard Hannon (14d 1/8) | headgear - | wind surgery | last run 64 days | form 3-3323 | MARKET 4.0% | 09:00 median 21.00 | Matchbook 26.00
    comment: Aura Champagne has finished in the frame in all five recent starts, including a third last time out and a second two starts back, yet she is winless in that spell. A 64-day absence and 136 lb from stall 2 temper the appeal, though she has run over today's trip.
    DATA: model 8.8% | style Prominent (led 4% of runs) | runs in data 4 | last 3: 3 Aug Nottingham Flat 8.3f Good To Firm 3/5; 7 Sep Windsor Flat 10f Good 2/7; 19 Sep Newbury Flat 8f Good To Firm 3/3
    DATA for: Good recent finishing positions

## 2:25 Lingfield (AW) | race_id rac_32305159523 | Make The Move To Midnite Handicap Stakes
Flat | Class 6 | 5f6y | going Standard | AW | 10 runners | rating band 0-60 | age 3yo+
DATA pace: Lone leader - Jane of The Jungle is the only habitual front-runner and may be allowed an easy lead.
- Lazzar (hrs_44816562) | 4yo G | 134lb | OR 60 | draw 6 | jockey David Egan | trainer Charlie Wallis (14d 0/1) | headgear - | last run 25 days | form 464545 | MARKET 25.7% | 09:00 median 3.50 | Matchbook 3.65 | CHECK (skip line 3.32)
    comment: Lazzar is consistent without a win, finishing fifth last time out and fourth two starts back, and he has run over today's trip and going before.
    DATA: model 13.9% | style Held up (led 3% of runs) | runs in data 17 | last 3: 11 Sep Sandown Flat 5f Good To Soft 5/9; 3 Oct Southwell Flat 6.1f Standard 4/13; 28 Oct Kempton (AW) Flat 6f Standard / Slow 5/11 fig 60
    DATA for: Best recent form figure 60, 5 lb above field average; Has won at this trip or further
- Diamond Dreamer (hrs_32210241) | 6yo G | 131lb | OR 57 | draw 4 | jockey Kieran Shoemark | trainer Patrick Chamings (14d 0/1) | headgear b | last run 27 days | form 760744 | MARKET 14.6% | 09:00 median 5.50 | Matchbook 7.00
    comment: Diamond Dreamer arrives with back-to-back fourths and has run over today's trip and going, but he's winless in his last six and was only seventh three starts back.
    DATA: model 7.3% | style Midfield (led 4% of runs) | runs in data 11 | last 3: 18 Aug Lingfield Flat 6f Standard 7/9; 28 Sep Brighton Flat 5.3f Good To Firm 4/9; 26 Oct Kempton (AW) Flat 6f Standard / Slow 4/12 fig 66
    DATA for: Best recent form figure 66, 11 lb above field average; Recent figures 9 lb above its current mark (looks well handicapped)
- One For Harvey (hrs_43002491) | 4yo F | 134lb | OR 60 | draw 10 | jockey Jack Doughty | trainer Clare Hobson (14d 0/3) | headgear - | last run 31 days | form 6-5413 | MARKET 13.1% | 09:00 median 6.50 | Matchbook 7.60
    comment: One For Harvey arrives in good heart after a third last time out, and a win two starts back, while she has run over today's trip and going before.
    DATA: model 27.4% | style Midfield (led 5% of runs) | runs in data 4 | last 3: 13 Aug Windsor Flat 6.1f Good To Firm 4/11; 17 Sep Southwell Flat 5f Standard 1/12; 22 Oct Southwell (AW) Flat 5f Standard 3/11 fig 62
    DATA for: Best recent form figure 62, 7 lb above field average; Has won at this trip or further; Good recent finishing positions
- Little Jaybee (hrs_52055031) | 3yo F | 133lb | OR 59 | draw 1 | jockey Billy Loughnane | trainer David Evans (14d 0/8) | headgear - | last run 17 days | form 221749 | MARKET 12.4% | 09:00 median 6.50 | Matchbook 8.20
    comment: Little Jaybee won four starts back and was runner-up twice before that, but she has faded since, finishing a seventh, a fourth, then a ninth last time out.
    DATA: model 13.5% | style Prominent (led 3% of runs) | runs in data 12 | last 3: 8 Oct Bath Flat 5f Good 7/14; 19 Oct Wolverhampton (AW) Flat 5f Standard 4/11 fig 59; 5 Nov Southwell (AW) Flat 5f Standard 9/13 fig 52
    DATA for: Best recent form figure 59, 4 lb above field average; Has won at this trip or further
    DATA against: Trainer 0 wins from 8 runs, last 14 days
- Davorge Nation (hrs_54059635) | 3yo G | 131lb | OR 57 | draw 3 | jockey Clifford Lee | trainer Tony Carroll (14d 1/22) | headgear - | last run 69 days | form 37-694 | MARKET 9.3% | 09:00 median 9.80 | Matchbook 10.00
    comment: The risk is a 69-day absence and a yard struggling at 1/22.
    DATA: model 4.5% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 8 Jun Leicester Flat 5f Good 6/6; 16 Jul Thirsk Flat 5f Good To Firm 9/9; 14 Sep Windsor Flat 5.1f Good To Soft 4/12
- Express Train (hrs_49012838) | 4yo G | 130lb | OR 56 | draw 8 | jockey Robert Havlin | trainer Richard Phillips (14d 1/1) | headgear - | last run 27 days | form 907545 | MARKET 8.1% | 09:00 median 11.00 | Matchbook 12.00
    comment: He has run over today's trip and going, and 130 lb from draw 8 is no help.
    DATA: model 8.7% | style Prominent (led 29% of runs) | runs in data 8 | last 3: 18 Aug Lingfield Flat 6f Standard 5/9; 1 Sep Wolverhampton Flat 6.1f Standard 4/11; 26 Oct Kempton (AW) Flat 6f Standard / Slow 5/12 fig 62
    DATA for: Best recent form figure 62, 7 lb above field average; Recent figures 6 lb above its current mark (looks well handicapped)
- La Belle Forest (hrs_57590610) | 3yo F | 131lb | OR 57 | draw 2 | jockey Hollie Doyle | trainer Archie Watson (14d 2/4) | headgear t | last run 26 days | form 664703 | MARKET 5.9% | 09:00 median 12.00 | Matchbook 19.50
    comment: She has run over today's trip and going, and carries 131 lb from draw 2.
    DATA: model 6.0% | style Held up (led 5% of runs) | runs in data 8 | last 3: 7 Sep Wolverhampton Flat 5.1f Standard 7/9; 22 Sep Southwell Flat 6.1f Standard 12/12; 27 Oct Wolverhampton (AW) Flat 5f Standard 3/9 fig 56
    DATA for: Has won at this trip or further
- Nuevo Slovo (hrs_51273187) | 3yo G | 134lb | OR 60 | draw 5 | jockey Paddy Bradley | trainer Simon Pearce (14d 0/1) | headgear b (1st time) | last run 33 days | form 046078 | MARKET 5.2% | 09:00 median 17.00 | Matchbook 18.50
    comment: The main risk is simply that he is winless in his last six and returns after 33 days.
    DATA: model 3.6% | style Prominent (led 3% of runs) | runs in data 7 | last 3: 16 Sep Yarmouth Flat 6f Good To Soft 11/12; 29 Sep Bath Flat 5.7f Good To Firm 7/9; 20 Oct Yarmouth Flat 6f Soft 8/9 fig 39
    DATA for: First-time headgear
    DATA against: Best recent form figure 39, 16 lb below field average; Recent figures 21 lb below its current mark (looks high in the weights); Last-run finishing speed -3.9% vs that field (faded); Poor recent finishing positions
- Sheik Yerbouti (hrs_61521614) | 5yo G | 133lb | OR 59 | draw 7 | jockey Darragh Keenan | trainer Grace Harris (14d 1/8) | headgear - | last run 34 days | form 037510 | MARKET 3.6% | 09:00 median 23.00 | Matchbook 28.00
    comment: Sheik Yerbouti was unplaced last time out and has just one win in his last six, a victor two starts back, so he's hard to fancy after 34 days off, carrying 133 lb from stall seven.
    DATA: model 10.3% | style Prominent (led 23% of runs) | runs in data 7 | last 3: 15 Sep Wolverhampton Flat 5.1f Standard 5/9; 2 Oct Wolverhampton Flat 5.1f Standard 1/11; 19 Oct Wolverhampton (AW) Flat 5f Standard 11/11 fig 36
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 36, 19 lb below field average; Recent figures 23 lb below its current mark (looks high in the weights)
- Jane of The Jungle (hrs_53081406) | 3yo F | 130lb | OR 56 | draw 9 | jockey Kieran O'Neill | trainer Scott Dixon (14d 0/1) | headgear - | last run 177 days | form 268344 | MARKET 2.2% | 09:00 median 34.00 | Matchbook 65.00
    comment: Jane of The Jungle was fourth on each of her last two starts and a third three starts back, and she has run over today's trip and going, but she is yet to win in her last six and returns after 177 days off.
    DATA: model 4.9% | style Leader (led 54% of runs) | runs in data 7 | last 3: 30 Apr Southwell Flat 6.1f Standard 3/11; 21 May Chepstow Flat 5.1f Good To Soft 4/5; 29 May Brighton Flat 6f Good To Firm 4/6
    DATA for: Pace: may get an uncontested lead
    DATA against: Returns from a 177-day break

## 2:55 Lingfield (AW) | race_id rac_32305161460 | Midnite: Built For 2026 Not 2006 Handicap Stakes
Flat | Class 6 | 1m2f1y | going Standard | AW | 12 runners | rating band 0-55 | age 4yo+
DATA pace: Lone leader - Shielas Well is the only habitual front-runner and may be allowed an easy lead.
- Wellwhatshappenin (hrs_45413151) | 4yo G | 134lb | OR 54 | draw 5 | jockey Hollie Doyle | trainer David Flood (14d 0/2) | headgear tp | last run 17 days | form 842162 | MARKET 23.2% | 09:00 median 3.50 | Matchbook 3.90 | CHECK (skip line 3.32)
    comment: Wellwhatshappenin steps out just 17 days after a second last time out, and he has a win three starts back in a solid recent profile. He has run over today's trip and going before, though a sixth two starts back is the one blemish.
    DATA: model 15.9% | style Prominent (led 4% of runs) | runs in data 8 | last 3: 27 Sep Ffos Las Flat 10f Soft 1/5; 28 Oct Nottingham Flat 10f Soft 6/15 fig 55; 5 Nov Chelmsford (AW) Flat 10f Standard 2/13 fig 61
    DATA for: Best recent form figure 61, 15 lb above field average; Recent figures 7 lb above its current mark (looks well handicapped); Has won at this trip or further; Good recent finishing positions
- Poke The Bear (hrs_43827000) | 4yo G | 133lb | OR 53 | draw 12 | jockey Tyler Heard | trainer Hayley Burton (14d 0/2) | headgear t | last run 17 days | form 607454 | MARKET 11.0% | 09:00 median 7.25 | Matchbook 8.40
    comment: Poke The Bear is winless in his last six, finishing fourth last time out and a fifth two starts back, which makes him hard to fancy at 133 lb from stall 12.
    DATA: model 7.2% | style Midfield (led 4% of runs) | runs in data 12 | last 3: 2 Jun Wolverhampton Flat 9.5f Standard 4/11; 26 Jun Newmarket Flat 8f Good To Firm 5/7; 5 Nov Chelmsford (AW) Flat 10f Standard 4/14 fig 59
    DATA for: Best recent form figure 59, 13 lb above field average; Recent figures 6 lb above its current mark (looks well handicapped)
- Electric Bass (hrs_47869066) | 4yo G | 132lb | OR 52 | draw 3 | jockey Kieran Shoemark | trainer Roger Teal (14d 0/5) | headgear h | last run 69 days | form 225347 | MARKET 10.3% | 09:00 median 8.00 | Matchbook 8.60
    comment: Electric Bass has been consistent without breaking through, with a third three starts back and two seconds earlier, but he was only seventh last time and returns after 69 days off. He has run over today's trip and going, yet carries 132 lb from stall three and is yet to win in his last six.
    DATA: model 9.7% | style Unknown | runs in data 6 | last 3: 16 Jul Chepstow Flat 10f Good To Firm 3/4; 2 Sep Bath Flat 8f Good 4/11; 14 Sep Windsor Flat 11.4f Good To Soft 7/11
- Little Tiger (hrs_31421656) | 6yo G | 130lb | OR 50 | draw 2 | jockey Billy Loughnane | trainer William Stone (14d 0/1) | headgear p | last run 27 days | form -46207 | MARKET 9.1% | 09:00 median 8.50 | Matchbook 10.50
    comment: Little Tiger is winless in his last five, beaten into seventh last time out, and only a second three starts back stands out in an otherwise modest run.
    DATA: model 9.3% | style Held up (led 4% of runs) | runs in data 5 | last 3: 8 Sep Leicester Flat 10f Good To Soft 2/9; 13 Oct Leicester Flat 10f Good To Soft 10/13; 26 Oct Leicester Flat 10f Soft 7/16 fig 45
- Manton Road (hrs_42943936) | 4yo G | 134lb | OR 54 | draw 6 | jockey Kieren Fox | trainer Richard Phillips (14d 1/1) | headgear - | last run 54 days | form 315433 | MARKET 8.8% | 09:00 median 8.50 | Matchbook 11.50
    comment: Manton Road has been consistent, third in each of his last two starts and a winner five starts back, and he has run over today's trip and on the going, but 54 days off and 134 lb from draw 6 temper the appeal.
    DATA: model 12.6% | style Held up (led 4% of runs) | runs in data 12 | last 3: 26 Aug Wolverhampton Flat 8.6f Standard 4/12; 15 Sep Wolverhampton Flat 8.6f Standard 3/12; 29 Sep Wolverhampton Flat 9.5f Standard 3/13
    DATA for: Last-run finishing speed +2.3% vs that field (finished strongly); Good recent finishing positions
- Far Ahead (hrs_40919424) | 4yo G | 127lb | OR 47 | draw 14 | jockey Ethan Tindall(5) | trainer Richard & Peter Fahey (14d 0/7) | headgear - | last run 22 days | form 702227 | MARKET 8.0% | 09:00 median 10.00 | Matchbook 12.00
    comment: Far Ahead is yet to win in his last six starts and was only seventh last time out, though three seconds in the previous four runs show he can get close.
    DATA: model 8.9% | style Prominent (led 3% of runs) | runs in data 10 | last 3: 17 Jun Hamilton Flat 9.2f Good 2/6; 29 Jun Pontefract Flat 8f Good 2/9; 31 Oct Southwell (AW) Flat 8f Standard 7/12 fig 44
    DATA for: Good recent finishing positions
- Merapi (hrs_53960305) | 4yo F | 134lb | OR 54 | draw 8 | jockey Cieren Fallon | trainer Michael Keady (14d 0/1) | headgear v (1st time) | last run 41 days | form 222648 | MARKET 7.6% | 09:00 median 9.50 | Matchbook 13.50
    DATA: model 7.5% | style Held up (led 8% of runs) | runs in data 8 | last 3: 28 May Yarmouth Flat 8f Good To Firm 6/9; 8 Sep Leicester Flat 10f Good To Soft 4/9; 12 Oct Yarmouth Flat 8f Good To Soft 8/12
    DATA for: First-time headgear
- Muy Muy Loco (hrs_41305026) | 4yo G | 131lb | OR 51 | draw 7 | jockey Luke Morris | trainer Simon Dow (14d 0/1) | headgear h | last run 17 days | form 605489 | MARKET 7.1% | 09:00 median 11.00 | Matchbook 14.00
    comment: Muy Muy Loco is winless in his last six, with a ninth last time out and an eighth before that, though a fourth three starts back shows he can be competitive.
    DATA: model 5.3% | style Held up (led 5% of runs) | runs in data 9 | last 3: 12 Sep Lingfield Flat 8f Standard 4/8; 15 Oct Brighton Flat 10f Good 8/9; 5 Nov Chelmsford (AW) Flat 10f Standard 9/14 fig 48
    DATA for: Has won at this trip or further
- Charencey (hrs_36515605) | 6yo G | 129lb | OR 49 | draw 10 | jockey Joe Leavy | trainer Ian Williams (14d 2/12) | headgear tv | last run 75 days | form 622335 | MARKET 6.1% | 09:00 median 13.00 | Matchbook 15.50
    comment: Charencey has been in the frame in four of his last six, including a third two starts back and another third three starts back, but he is yet to win and was only fifth last time. A 75-day absence and 129 lb are the concerns, though he has run over today's trip and going.
    DATA: model 11.5% | style Prominent (led 5% of runs) | runs in data 8 | last 3: 11 Aug Lingfield Flat 12f Standard 3/11; 21 Aug Ffos Las Flat 10f Good 3/10; 8 Sep Leicester Flat 10f Good To Soft 5/9
    DATA for: Good recent finishing positions
- Uzincso (hrs_19261746) | 10yo G | 132lb | OR 52 | draw 1 | jockey David Egan | trainer John Butler (14d 2/10) | headgear p | last run 27 days | form 434689 | MARKET 4.0% | 09:00 median 17.00 | Matchbook 27.00
    comment: The risk is a form line that has faded to eighth and ninth in his last two, and he's yet to win in recent starts.
    DATA: model 5.1% | style Midfield (led 3% of runs) | runs in data 7 | last 3: 9 Sep Kempton Flat 11f Standard To Slow 6/12; 23 Sep Kempton Flat 11f Standard To Slow 8/14; 26 Oct Kempton (AW) Flat 11f Standard / Slow 9/10 fig 32
    DATA for: Trainer 20% wins (2/10), last 14 days
    DATA against: Best recent form figure 32, 14 lb below field average; Recent figures 20 lb below its current mark (looks high in the weights); Poor recent finishing positions; Aged 10, older than most of this field
- Shielas Well (hrs_42163240) | 4yo F | 129lb | OR 49 | draw 9 | jockey Ryan Kavanagh(3) | trainer Ian Williams (14d 2/12) | headgear p | last run 2 days | form 843300 | MARKET 3.0% | 09:00 median 26.00 | Matchbook 38.00
    comment: Winless in her last six, Shielas Well was unplaced last time out and again two starts back, and she's back after just two days, so she's hard to fancy. A third three starts back and another four starts back, plus experience of today's trip and going, are the positives, but 129 lb from draw 9 is a big ask.
    DATA: model 3.5% | style Leader (led 43% of runs) | runs in data 7 | last 3: 5 May Wolverhampton Flat 8.6f Standard 3/8; 28 Oct Kempton (AW) Flat 6f Standard / Slow 10/11 fig 41; 20 Nov Wolverhampton (AW) Flat 8.5f Standard 10/13 fig 31
    DATA for: Pace: may get an uncontested lead
    DATA against: Best recent form figure 41, 5 lb below field average; Recent figures 8 lb below its current mark (looks high in the weights); Last-run finishing speed -3.3% vs that field (faded)
- Kondratiev Wave (hrs_19807081) | 9yo G | 130lb | OR 50 | draw 11 | jockey Clifford Lee | trainer Tony Carroll (14d 1/22) | headgear p | last run 22 days | form 624390 | MARKET 1.8% | 09:00 median 41.00 | Matchbook 65.00
    comment: Winless in his last six, Kondratiev Wave was unplaced last time and ninth two starts back, though he was third three starts back and has run on today's going.
    DATA: model 3.6% | style Prominent (led 3% of runs) | runs in data 15 | last 3: 24 Aug Brighton Flat 7f Good To Firm 3/9; 5 Oct Kempton Flat 7f Standard To Slow 9/13; 31 Oct Southwell (AW) Flat 8f Standard 10/14 fig 41
    DATA against: Best recent form figure 41, 5 lb below field average; Recent figures 9 lb below its current mark (looks high in the weights)

## 3:25 Lingfield (AW) | race_id rac_32305163397 | Midnite Ain't Your Grandad's Bookie Handicap Stakes
Flat | Class 6 | 1m7f170y | going Standard | AW | 9 runners | rating band 0-65 | age 3yo+
DATA pace: Even - Two likely leaders (Calshot Spit, In The Post). A fair, even gallop is most likely.
- In The Post (hrs_55454119) | 4yo G | 134lb | OR 57 | draw 8 | jockey Marco Ghiani | trainer Dylan Cunha (14d 1/6) | headgear - | last run 18 days | form 684333 | MARKET 20.9% | 09:00 median 4.00 | Matchbook 4.60 | CHECK (skip line 3.80)
    comment: The main risk is that he's yet to win in his last six, so he may again be found short at the line.
    DATA: model 16.4% | style Prominent (led 43% of runs) | runs in data 6 | last 3: 16 May Doncaster Flat 11.9f Good To Soft 3/7; 31 May Nottingham Flat 14f Good 3/7; 4 Nov Kempton (AW) Flat 12f Standard / Slow 3/14 fig 60
    DATA for: Best recent form figure 60, 5 lb above field average; Good recent finishing positions; Course: prominent racers have won 1.3× their fair share at 16f here
- Chilli King (hrs_63323694) | 3yo G | 131lb | OR 60 | draw 4 | jockey Charles Bishop | trainer Emma Lavelle (14d 3/18) | headgear - | last run 31 days | form 7605 | MARKET 19.7% | 09:00 median 4.50 | Matchbook 4.70
    comment: Chilli King is hard to fancy, winless in his last four with a fifth last time out, then unplaced, a sixth and a seventh before that.
    DATA: model 10.5% | style Midfield (led 4% of runs) | runs in data 4 | last 3: 30 Apr Southwell Flat 11.1f Standard 6/8; 26 Sep Southwell Flat 11.1f Standard 10/13; 22 Oct Southwell (AW) Flat 14f Standard 5/12 fig 59
    DATA for: Best recent form figure 59, 4 lb above field average; Last-run finishing speed +3.1% vs that field (finished strongly)
- Notable Charm (hrs_52709706) | 3yo G | 122lb | OR 51 | draw 1 | jockey Tyler Heard | trainer Marcus Tregoning (14d 0/1) | headgear b | last run 54 days | form 464523 | MARKET 15.0% | 09:00 median 5.50 | Matchbook 6.60
    comment: Notable Charm is winless in his last six, though he was third last time out and a second two starts back, so the form is creeping the right way.
    DATA: model 4.5% | style Prominent (led 4% of runs) | runs in data 9 | last 3: 2 Sep Bath Flat 14f Good 5/10; 21 Sep Wolverhampton Flat 16.5f Standard 2/5; 29 Sep Wolverhampton Flat 16.5f Standard 3/11
    DATA for: Last-run finishing speed +5.2% vs that field (finished strongly); Good recent finishing positions; Carries 12 lb less than average; Course: prominent racers have won 1.3× their fair share at 16f here
    DATA against: Official rating 51, 8 lb below field average
- Noble Grace (hrs_51523885) | 5yo M | 140lb | OR 63 | draw 6 | jockey Edward Greatrex | trainer Warren Greatrex (14d 6/17) | headgear p | last run 27 days | form 413713 | MARKET 11.3% | 09:00 median 7.50 | Matchbook 8.60
    comment: Noble Grace arrives in good heart, third last time out and a winner two starts back, with two wins in her last six, and she has run over today's trip and going before.
    DATA: model 18.0% | style Held up (led 4% of runs) | runs in data 11 | last 3: 13 Sep Bath Flat 14f Good To Soft 7/12; 5 Oct Pontefract Flat 18f Good 1/6; 26 Oct Kempton (AW) Flat 16f Standard / Slow 3/12 fig 61
    DATA for: Best recent form figure 61, 6 lb above field average; Trainer 35% wins (6/17), last 14 days; Has won at this trip or further; Good recent finishing positions
    DATA against: Carries 6 lb more than average
- Autumn's Breeze (hrs_41939121) | 5yo M | 142lb | OR 65 | draw 2 | jockey David Egan | trainer Jamie Moore & Josh Moore (14d 1/21) | headgear b (1st time) | last run 18 days | form 9-9P38 | MARKET 11.0% | 09:00 median 7.00 | Matchbook 9.60
    comment: Autumn's Breeze is yet to win in her last five starts, but a third two starts back is her best recent effort, and she has run over today's trip and returns after just 18 days.
    DATA: model 9.7% | style Unknown | runs in data 4 | last 3: 15 May Newbury Flat 12f Good PU/15; 7 Oct Kempton Flat 16f Standard To Slow 3/9; 4 Nov Nottingham Flat 16f Soft 8/13 fig 51
    DATA for: Official rating 65, 6 lb above field average; Last-run finishing speed +4.5% vs that field (finished strongly); First-time headgear
    DATA against: Best recent form figure 51, 4 lb below field average; Recent figures 14 lb below its current mark (looks high in the weights); Carries 8 lb more than average
- Snapius (hrs_24758412) | 7yo G | 125lb | OR 48 | draw 7 | jockey Hollie Doyle | trainer James Owen (14d 3/39) | headgear - | last run 184 days | form 997/4- | MARKET 10.0% | 09:00 median 8.75 | Matchbook 9.60
    comment: Snapius showed a little more when fourth last time out, after a seventh and two ninth-placed runs, and has run over today's trip and going, but he is winless in his last four and returns after 184 days off.
    DATA: model 6.2% | style Midfield (led 3% of runs) | runs in data 7 | last 3: 23 Apr Warwick Hurdle 19f Good 4/9; 10 May Ludlow Hurdle 21.2f Good 2/8; 22 May Worcester Hurdle 20f Good 4/7
    DATA for: Last-run finishing speed +2.2% vs that field (finished strongly); Carries 9 lb less than average
    DATA against: Official rating 48, 11 lb below field average; Returns from a 184-day break
- State Express (hrs_7000000357) | 3yo C | 134lb | OR 63 | draw 9 | jockey Cieren Fallon | trainer S. P. C. Woods (14d 0/5) | headgear - | last run 27 days | form 45510 | MARKET 5.1% | 09:00 median 17.00 | Matchbook 19.00
    comment: State Express was unplaced last time out and has just one win in his last five starts, a victory two starts back, with a run of fifth, fifth and fourth before that, so he's hard to fancy.
    DATA: model 12.7% | style Midfield (led 4% of runs) | runs in data 5 | last 3: 25 Aug Lingfield Flat 10f Standard 5/7; 8 Oct Southwell Flat 14.1f Standard 1/12; 26 Oct Kempton (AW) Flat 16f Standard / Slow 10/12 fig 44
    DATA against: Best recent form figure 44, 11 lb below field average; Recent figures 19 lb below its current mark (looks high in the weights)
- Calshot Spit (hrs_37446850) | 6yo G | 136lb | OR 59 | draw 3 | jockey Rose Dawes(3) | trainer Sheena West (14d 0/2) | headgear - | last run 19 days | form 118/92 | MARKET 5.0% | 09:00 median 17.00 | Matchbook 20.00
    comment: Calshot Spit bounced back to be second last time out, 19 days ago, and has won twice in his last five, though a ninth and an eighth in between show his consistency has wobbled. He has run on today's going, but 136 lb is a hefty burden off a mark of 59.
    DATA: model 15.8% | style Prominent (led 43% of runs) | runs in data 6 | last 3: 29 Sep Bath Flat 13.1f Good To Firm 9/13; 8 Oct Bath Flat 17.1f Good 2/12; 3 Nov Lingfield Hurdle 19.5f Good 4/9 fig 101
    DATA for: Last-run finishing speed +2.1% vs that field (finished strongly); Course: prominent racers have won 1.3× their fair share at 16f here
- Little Peter (hrs_34456555) | 8yo G | 142lb | OR 65 | draw 5 | jockey Gina Mangan | trainer John Berry (14d 0/2) | headgear - | last run 175 days | form /560-6 | MARKET 2.1% | 09:00 median 41.00 | Matchbook 55.00
    comment: The main risk is a 175-day absence after finishing sixth last time out and fifth four starts back.
    DATA: model 6.1% | style Unknown | runs in data 1 | last 3: 31 May Nottingham Flat 14f Good 6/7
    DATA for: Official rating 65, 6 lb above field average
    DATA against: Carries 8 lb more than average; Returns from a 175-day break; Lightly raced: 1 run in our data, so the model has little to go on; Aged 8, older than most of this field
