# Card review packet: Kempton (AW), 2026-11-25

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
{"meeting": "kempton_aw", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 4:20 Kempton (AW) | race_id rac_32305841347 | Racing TV EBF Fillies' Restricted Novice Stakes (For Horses In Bands B, C And D) (Div I) (GBB Race)
Flat | Class 4 | 7f | going Standard / Slow | AW | 10 runners | rating band - | age 2yo
DATA pace: Unclear - Running styles known for only 4 of 10 runners.
- Bet You Can't (hrs_17395546903) | 2yo F | 125lb | OR - | draw 2 | jockey Billy Loughnane | trainer George Boughey (14d 6/22) | headgear - | last run - days | form - | MARKET 41.0% | 09:00 median 2.10 | Matchbook 2.20
    DATA: model 9.0% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 27% wins (6/22), last 14 days
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Jalapeno Gal (hrs_17395989135) | 2yo F | 128lb | OR - | draw 9 | jockey George Downing | trainer Ed Walker (14d 1/15) | headgear - | last run - days | form - | MARKET 14.7% | 09:00 median 5.50 | Matchbook 6.60
    DATA: model 9.0% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Zenith (hrs_17395995393) | 2yo F | 128lb | OR - | draw 4 | jockey Hollie Doyle | trainer Alan King (14d 2/20) | headgear - | last run - days | form - | MARKET 11.9% | 09:00 median 6.50 | Matchbook 8.20
    DATA: model 9.0% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Kiss of Life (hrs_66494106) | 2yo F | 125lb | OR - | draw 5 | jockey George Bass | trainer Jack Channon (14d 0/7) | headgear - | last run 49 days | form 89 | MARKET 9.5% | 09:00 median 9.00 | Matchbook 9.60
    DATA: model 14.3% | style Prominent (led 8% of runs) | runs in data 2 | last 3: 9 Jul Newbury Flat 6f Good To Firm 8/10; 7 Oct Kempton Flat 7f Standard To Slow 9/12
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Spiders From Mars (hrs_60821117) | 2yo F | 128lb | OR - | draw 6 | jockey Ashley Lewis(3) | trainer Ed Walker (14d 1/15) | headgear - | last run - days | form - | MARKET 6.7% | 09:00 median 12.00 | Matchbook 14.50
    DATA: model 9.0% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Amnaa's Dream (hrs_17395984963) | 2yo F | 125lb | OR - | draw 8 | jockey Joe Leavy | trainer Roger Teal (14d 0/9) | headgear - | last run - days | form - | MARKET 5.9% | 09:00 median 13.00 | Matchbook 17.50
    DATA: model 9.0% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Trainer 0 wins from 9 runs, last 14 days; Lightly raced: 0 runs in our data, so the model has little to go on
- Lady Aethelflaed (hrs_17393335743) | 2yo F | 125lb | OR - | draw 11 | jockey Sean Levey | trainer David Menuisier (14d 0/3) | headgear - | last run 50 days | form 0 | MARKET 4.9% | 09:00 median 17.00 | Matchbook 19.00
    DATA: model 17.9% | style Held up (led 8% of runs) | runs in data 1 | last 3: 6 Oct Southwell Flat 7.1f Standard 12/13
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Atina Superiore (hrs_17394186831) | 2yo F | 125lb | OR - | draw 3 | jockey Finley Marsh | trainer Ed de Giles (14d 0/2) | headgear - | last run - days | form - | MARKET 3.0% | 09:00 median 23.00 | Matchbook 44.00
    DATA: model 9.0% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Maeveontime (hrs_17393471333) | 2yo F | 125lb | OR - | draw 10 | jockey Andrew Mullen | trainer Dylan Cunha (14d 2/13) | headgear - | last run 18 days | form 00 | MARKET 1.3% | 09:00 median 51.00 | Matchbook 180.00
    DATA: model 7.6% | style Midfield (led 8% of runs) | runs in data 2 | last 3: 8 Oct Southwell Flat 6.1f Standard 10/11; 7 Nov Southwell (AW) Flat 6f Standard 13/13 fig 13
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Deja Vu Diva (hrs_64590757) | 2yo F | 122lb | OR 16 | draw 1 | jockey Jack Doughty | trainer Clare Hobson (14d 0/5) | headgear p (1st time) | last run 133 days | form 896 | MARKET 1.1% | 09:00 median 67.00 | Matchbook 170.00
    DATA: model 6.2% | style Held up (led 4% of runs) | runs in data 3 | last 3: 13 May Yarmouth Flat 6f Soft 8/8; 4 Jun Lingfield Flat 6f Standard 9/10; 15 Jul Lingfield Flat 6f Good To Firm 6/7
    DATA for: First-time headgear
    DATA against: Last-run finishing speed -5.6% vs that field (faded); Poor recent finishing positions; Returns from a 133-day break

## 4:50 Kempton (AW) | race_id rac_32305504309 | Racing TV EBF Fillies' Restricted Novice Stakes (For Horses In Bands B, C And D) (Div II) (GBB Race)
Flat | Class 4 | 7f | going Standard / Slow | AW | 9 runners | rating band - | age 2yo
DATA pace: Unclear - Running styles known for only 3 of 9 runners.
- Lady's Grace (hrs_17391762899) | 2yo F | 125lb | OR 70 | draw 4 | jockey Robert Havlin | trainer John & Thady Gosden (14d 2/21) | headgear v (1st time) | last run 23 days | form 433 | MARKET 35.7% | 09:00 median 2.38 | Matchbook 2.60
    DATA: model 34.6% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 6 Oct Southwell Flat 7.1f Standard 4/13; 21 Oct Kempton (AW) Flat 7f Standard / Slow 3/10 fig 67; 2 Nov Chelmsford (AW) Flat 7f Standard 3/12 fig 54
    DATA for: Best recent form figure 67, 9 lb above field average; Good recent finishing positions; First-time headgear
- Garden Maze (hrs_17392419989) | 2yo F | 122lb | OR - | draw 5 | jockey Oisin Murphy | trainer Andrew Balding (14d 4/32) | headgear - | last run - days | form - | MARKET 17.3% | 09:00 median 5.00 | Matchbook 5.30
    DATA: model 8.6% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Sand Dance (hrs_17393758158) | 2yo F | 128lb | OR - | draw 3 | jockey Hollie Doyle | trainer S. P. C. Woods (14d 1/8) | headgear - | last run 28 days | form 85 | MARKET 17.0% | 09:00 median 5.25 | Matchbook 5.30
    DATA: model 6.0% | style Prominent (led 38% of runs) | runs in data 2 | last 3: 14 Oct Kempton (AW) Flat 7f Standard / Slow 8/10 fig 59; 28 Oct Kempton (AW) Flat 8f Standard / Slow 5/9 fig 58
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Annie Hall (hrs_17394741707) | 2yo F | 128lb | OR - | draw 6 | jockey Luke Morris | trainer Oliver Cole (14d 0/4) | headgear - | last run 18 days | form 6 | MARKET 11.9% | 09:00 median 6.50 | Matchbook 8.40
    DATA: model 7.4% | style Held up (led 8% of runs) | runs in data 1 | last 3: 7 Nov Southwell (AW) Flat 6f Standard 6/13 fig 47
    DATA against: Best recent form figure 47, 11 lb below field average; Lightly raced: 1 run in our data, so the model has little to go on
- Tansy (hrs_17395994350) | 2yo F | 128lb | OR - | draw 1 | jockey George Downing | trainer Ed Walker (14d 1/15) | headgear - | last run - days | form - | MARKET 5.2% | 09:00 median 15.00 | Matchbook 21.00
    DATA: model 8.7% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Flamme Doree (hrs_60821432) | 2yo F | 125lb | OR - | draw 9 | jockey Ashley Lewis(3) | trainer Ed Walker (14d 1/15) | headgear - | last run - days | form - | MARKET 4.6% | 09:00 median 19.00 | Matchbook 21.00
    DATA: model 8.7% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Danebury Rose (hrs_17395986006) | 2yo F | 125lb | OR - | draw 7 | jockey Kieren Fox | trainer Charlie Pike (14d 0/3) | headgear - | last run - days | form - | MARKET 3.7% | 09:00 median 21.00 | Matchbook 30.00
    DATA: model 8.7% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Shot At Love (hrs_17395993307) | 2yo F | 128lb | OR - | draw 10 | jockey Marco Ghiani | trainer Stuart Williams (14d 0/5) | headgear - | last run - days | form - | MARKET 2.4% | 09:00 median 34.00 | Matchbook 50.00
    DATA: model 8.7% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Nine Petals (hrs_17395992264) | 2yo F | 125lb | OR - | draw 2 | jockey William Cox | trainer Tom Dascombe (14d 0/1) | headgear - | last run - days | form - | MARKET 2.2% | 09:00 median 29.00 | Matchbook 85.00
    DATA: model 8.7% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on

## 5:20 Kempton (AW) | race_id rac_32305506246 | Unibet/British Stallion Studs EBF Novice Stakes (GBB Race)
Flat | Class 4 | 7f | going Standard / Slow | AW | 8 runners | rating band - | age 3yo+
DATA pace: Unclear - Running styles known for only 1 of 8 runners.
- Highest Peak (hrs_17395997479) | 3yo G | 133lb | OR - | draw 7 | jockey Billy Loughnane | trainer Charlie Appleby (14d 3/7) | headgear - | last run - days | form - | MARKET 55.2% | 09:00 median 1.57 | Matchbook 1.65
    DATA: model 9.9% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 43% wins (3/7), last 14 days
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Lean d'Aislingean (hrs_64488088) | 3yo C | 133lb | OR 80 | draw 5 | jockey Kieren Fox | trainer Charlie Pike (14d 0/3) | headgear - | last run 46 days | form 93200 | MARKET 25.2% | 09:00 median 3.25 | Matchbook 3.80
    DATA: model 15.3% | style Unknown | runs in data 5 | last 3: 30 Jun Ffos Las Flat 8f Good 2/8; 30 Jul Goodwood Flat 9.9f Good To Firm 13/14; 10 Oct York Flat 10.3f Good To Soft 12/19
- Crown Knott (hrs_63551243) | 3yo G | 133lb | OR - | draw 2 | jockey Rob Hornby | trainer Mark Loughnane (14d 2/18) | headgear - | wind surgery | last run 223 days | form 6 | MARKET 9.0% | 09:00 median 7.00 | Matchbook 14.50
    DATA: model 26.3% | style Unknown | runs in data 1 | last 3: 16 Apr Newmarket Flat 8f Good 6/10
    DATA against: Returns from a 223-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Acclamique (hrs_17394100262) | 3yo F | 128lb | OR - | draw 4 | jockey Hollie Doyle | trainer William Haggas (14d 4/22) | headgear t | last run 34 days | form 6 | MARKET 3.8% | 09:00 median 17.00 | Matchbook 36.00
    DATA: model 15.9% | style Held up (led 8% of runs) | runs in data 1 | last 3: 22 Oct Southwell (AW) Flat 6f Standard 6/8 fig 38
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Soul Survivor (hrs_63809445) | 3yo G | 133lb | OR - | draw 3 | jockey Rose Dawes(3) | trainer Jack Channon (14d 0/7) | headgear - | last run - days | form - | MARKET 2.7% | 09:00 median 24.50 | Matchbook 60.00
    DATA: model 9.9% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Allthemcs (hrs_17395996436) | 3yo G | 133lb | OR - | draw 1 | jockey Dylan Hogan | trainer John Butler (14d 2/12) | headgear - | last run - days | form - | MARKET 1.8% | 09:00 median 34.00 | Matchbook 90.00
    DATA: model 9.9% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Rumblin' Along (hrs_17395999565) | 3yo G | 133lb | OR - | draw 8 | jockey Jonny Peate | trainer Brian Toomey (14d 0/2) | headgear - | last run - days | form - | MARKET 1.5% | 09:00 median 45.00 | Matchbook 120.00
    DATA: model 9.9% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Crack O'Nine (hrs_17394440280) | 3yo G | 133lb | OR - | draw 6 | jockey William Carson | trainer Michael Attwater (14d 1/9) | headgear - | last run 30 days | form 9 | MARKET 0.9% | 09:00 median 69.00 | Matchbook 190.00
    DATA: model 3.0% | style Unknown | runs in data 1 | last 3: 26 Oct Kempton (AW) Flat 7f Standard / Slow 9/9 fig 33
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on

## 5:50 Kempton (AW) | race_id rac_32305508183 | Try Unibet's New Racing Bet Builder Nursery Handicap Stakes
Flat | Class 6 | 1m | going Standard / Slow | AW | 14 runners | rating band 0-65 | age 2yo
DATA pace: Lone leader - Hoosier is the only habitual front-runner and may be allowed an easy lead.
- Admiral Leach (hrs_62168820) | 2yo G | 133lb | OR 59 | draw 5 | jockey Robert Havlin | trainer Ed Dunlop (14d 1/5) | headgear - | last run 19 days | form 0905 | MARKET 17.3% | 09:00 median 4.50 | Matchbook 5.40 | CHECK (skip line 4.27)
    comment: Admiral Leach was a fifth last time out just 19 days ago and has run over today's trip, but he is winless in his last four starts, with a ninth and two unplaced efforts before that.
    DATA: model 5.9% | style Midfield (led 3% of runs) | runs in data 4 | last 3: 4 Sep Kempton Flat 7f Standard To Slow 9/13; 18 Sep Newbury Flat 6f Good 12/15; 6 Nov Newcastle (AW) Flat 7f Standard 5/11 fig 60
    DATA for: Best recent form figure 60, 7 lb above field average; Trainer 20% wins (1/5), last 14 days
- Casablanca Dream (hrs_7000002121) | 2yo F | 133lb | OR 59 | draw 9 | jockey Oisin Murphy | trainer Marco Botti (14d 0/12) | headgear - | last run 48 days | form 65533 | MARKET 16.0% | 09:00 median 5.00 | Matchbook 6.00
    comment: The main risk is a 48-day break, though she is yet to win in her last five starts.
    DATA: model 19.3% | style Prominent (led 4% of runs) | runs in data 5 | last 3: 1 Sep Wolverhampton Flat 7.2f Standard 5/9; 17 Sep Yarmouth Flat 8f Good 3/10; 8 Oct Southwell Flat 8.1f Standard 3/12
    DATA for: Good recent finishing positions
    DATA against: Trainer 0 wins from 12 runs, last 14 days
- Tarn Hows (hrs_17391767071) | 2yo G | 135lb | OR 61 | draw 7 | jockey Billy Loughnane | trainer Daniel & Claire Kubler (14d 1/1) | headgear - | last run 27 days | form 0737 | MARKET 14.8% | 09:00 median 5.50 | Matchbook 6.00
    comment: Tarn Hows was seventh last time out, though he was third two starts back, and he has run over today's trip after 27 days off.
    DATA: model 7.6% | style Midfield (led 3% of runs) | runs in data 4 | last 3: 23 Sep Kempton Flat 8f Standard To Slow 7/9; 8 Oct Bath Flat 8f Good 3/13; 29 Oct Southwell (AW) Flat 7f Standard 7/13 fig 59
    DATA for: Best recent form figure 59, 6 lb above field average
- Angel of Heaven (hrs_65869615) | 2yo F | 126lb | OR 52 | draw 2 | jockey Hollie Doyle | trainer James Fanshawe (14d 0/13) | headgear - | last run 69 days | form 787 | MARKET 14.7% | 09:00 median 5.50 | Matchbook 6.00
    comment: Angel of Heaven is winless in her last three, finishing seventh last time out, an eighth two starts back and a seventh three starts back, and she returns after 69 days off.
    DATA: model 5.9% | style Held up (led 4% of runs) | runs in data 3 | last 3: 29 Jun Kempton Flat 7f Standard To Slow 7/11; 18 Jul Newmarket Flat 7f Good To Firm 8/10; 17 Sep Southwell Flat 7.1f Standard 7/11
    DATA against: Trainer 0 wins from 13 runs, last 14 days; Poor recent finishing positions
- Blue Skies Above (hrs_60819108) | 2yo G | 135lb | OR 61 | draw 6 | jockey Luke Morris | trainer Oliver Cole (14d 0/4) | headgear p (1st time) | last run 58 days | form 85095 | MARKET 7.7% | 09:00 median 11.00 | Matchbook 11.50
    comment: The 58-day break is the one question mark.
    DATA: model 12.3% | style Prominent (led 23% of runs) | runs in data 5 | last 3: 9 Jun Salisbury Flat 6f Soft 10/11; 7 Sep Windsor Flat 6.1f Good 9/14; 28 Sep Brighton Flat 8f Good To Firm 5/13
    DATA for: First-time headgear
- Lopefernza (hrs_65710869) | 2yo G | 131lb | OR 57 | draw 12 | jockey Jack Doughty | trainer David Loughnane (14d 2/11) | headgear t | last run 27 days | form 66755 | MARKET 6.1% | 09:00 median 13.00 | Matchbook 15.50
    comment: Lopefernza has finished fifth in his last two starts and is winless in his last five, so he's consistent without threatening, though 27 days off suggests he's fresh and he has run over today's trip.
    DATA: model 8.8% | style Midfield (led 5% of runs) | runs in data 5 | last 3: 3 Sep Haydock Flat 7f Soft 7/7; 24 Sep Southwell Flat 7.1f Standard 5/12; 29 Oct Southwell (AW) Flat 7f Standard 5/13 fig 55
- Windmill (hrs_7000000385) | 2yo F | 125lb | OR 51 | draw 3 | jockey Sean Levey | trainer Ollie Sangster (14d 1/12) | headgear - | last run 30 days | form 084 | MARKET 5.3% | 09:00 median 15.00 | Matchbook 18.00
    comment: Windmill showed a bit of promise when fourth last time out, after an eighth two starts back, though she is winless in her last three and has had 30 days off since.
    DATA: model 4.1% | style Held up (led 4% of runs) | runs in data 3 | last 3: 17 Jul Newbury Flat 6f Good To Firm 10/11; 9 Aug Chepstow Flat 6.1f Good To Firm 8/9; 26 Oct Leicester Flat 6f Soft 4/6 fig 66
    DATA for: Best recent form figure 66, 13 lb above field average; Recent figures 15 lb above its current mark (looks well handicapped); Carries 5 lb less than average
    DATA against: Official rating 51, 5 lb below field average
- Magical Life (hrs_63323673) | 2yo F | 130lb | OR 56 | draw 8 | jockey John Egan | trainer J. S. Moore (14d 0/12) | headgear - | last run 20 days | form 667284 | MARKET 5.0% | 09:00 median 15.00 | Matchbook 19.50
    comment: Magical Life steps up from a fourth last time out, 20 days ago, and a second three starts back shows her ceiling.
    DATA: model 9.6% | style Midfield (led 4% of runs) | runs in data 15 | last 3: 19 Oct Bath Flat 8f Good To Soft 2/13 fig 64; 31 Oct Newmarket Flat 9f Good To Soft 8/10 fig 38; 5 Nov Chelmsford (AW) Flat 10f Standard 4/9 fig 55
    DATA for: Best recent form figure 64, 11 lb above field average; Recent figures 8 lb above its current mark (looks well handicapped); Has won at this trip or further
    DATA against: Trainer 0 wins from 12 runs, last 14 days
- Hoosier (hrs_64167950) | 2yo F | 134lb | OR 60 | draw 1 | jockey Marco Ghiani | trainer Marco Botti (14d 0/12) | headgear h | last run 27 days | form 54460 | MARKET 3.0% | 09:00 median 26.00 | Matchbook 32.00
    comment: The risk is that she is without a win in that spell and was unplaced last time out, while carrying 134 lb from stall one.
    DATA: model 13.0% | style Leader (led 29% of runs) | runs in data 5 | last 3: 5 Oct Wolverhampton Flat 6.1f Standard 4/8; 19 Oct Wolverhampton (AW) Flat 7f Standard 6/10 fig 59; 29 Oct Southwell (AW) Flat 7f Standard 13/13 fig 34
    DATA for: Best recent form figure 59, 6 lb above field average; Pace: may get an uncontested lead
    DATA against: Trainer 0 wins from 12 runs, last 14 days
- Champagne Charlee (hrs_66399522) | 2yo G | 125lb | OR 51 | draw 14 | jockey Jack Dace(5) | trainer Stuart Williams (14d 0/5) | headgear t | last run 111 days | form 906 | MARKET 2.6% | 09:00 median 29.00 | Matchbook 40.00
    comment: Champagne Charlee is winless in his last three, finishing sixth last time, then unplaced, then ninth, and returns after 111 days off, so he is hard to fancy.
    DATA: model 1.4% | style Held up (led 8% of runs) | runs in data 3 | last 3: 4 Jul Leicester Flat 6f Good To Firm 9/9; 23 Jul Southwell Flat 6.1f Standard 11/12; 6 Aug Sandown Flat 5f Good To Firm 6/9
    DATA for: Last-run finishing speed +2.3% vs that field (finished strongly); Carries 5 lb less than average
    DATA against: Official rating 51, 5 lb below field average; Poor recent finishing positions; Returns from a 111-day break
- Miss Faithfull (hrs_17391722222) | 2yo F | 130lb | OR 56 | draw 10 | jockey Paddy Bradley | trainer Charlie Fellowes (14d 3/9) | headgear h | last run 25 days | form 590 | MARKET 2.5% | 09:00 median 26.00 | Matchbook 50.00
    comment: Miss Faithfull has been out of the frame in her last three, with an unplaced effort last time, a ninth two starts back and a fifth three starts back, though she's had 25 days to freshen up and has run over today's trip.
    DATA: model 1.9% | style Held up (led 4% of runs) | runs in data 3 | last 3: 3 Sep Salisbury Flat 8f Good To Soft 5/9; 26 Sep Haydock Flat 8f Heavy 9/9; 31 Oct Newmarket Flat 7f Good To Soft 10/11 fig 49
    DATA for: Trainer 33% wins (3/9), last 14 days
    DATA against: Recent figures 7 lb below its current mark (looks high in the weights)
- Marralyn (hrs_63741923) | 2yo F | 129lb | OR 55 | draw 4 | jockey Dylan Hogan | trainer Ollie Sangster (14d 1/12) | headgear - | last run 51 days | form 583776 | MARKET 2.0% | 09:00 median 29.00 | Matchbook 75.00
    comment: Marralyn is winless in her last six, with a third four starts back and a fifth six starts back her best finishes, and she returns after 51 days off.
    DATA: model 5.4% | style Midfield (led 5% of runs) | runs in data 6 | last 3: 25 Jul Lingfield Flat 5f Good To Firm 7/7; 7 Sep Windsor Flat 6.1f Good 7/14; 5 Oct Yarmouth Flat 7f Good To Firm 6/8
    DATA against: Poor recent finishing positions
- Nil Satis Supreme (hrs_17391388462) | 2yo G | 129lb | OR 55 | draw 11 | jockey Jonny Peate | trainer Mark Loughnane (14d 2/18) | headgear b (1st time) | last run 29 days | form 807 | MARKET 2.0% | 09:00 median 34.00 | Matchbook 65.00
    comment: He has run over today's trip and returns after 29 days, but 129 lb from stall 11 is a lot to ask.
    DATA: model 2.1% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 26 Aug Wolverhampton Flat 6.1f Standard 8/11; 12 Oct Kempton Flat 7f Standard To Slow 10/11; 27 Oct Wolverhampton (AW) Flat 8.5f Standard 7/12 fig 39
    DATA for: First-time headgear
    DATA against: Best recent form figure 39, 14 lb below field average; Recent figures 16 lb below its current mark (looks high in the weights); Poor recent finishing positions
- Desert Move (hrs_65519643) | 2yo G | 128lb | OR 54 | draw 13 | jockey Tyler Heard | trainer Simon Dow (14d 0/3) | headgear - | last run 42 days | form 558 | MARKET 0.9% | 09:00 median 67.00 | Matchbook 170.00
    comment: Desert Move is hard to fancy, having finished eighth last time out, then a fifth two starts back, and another fifth three starts back, so he is winless in recent starts and returns after 42 days off.
    DATA: model 2.8% | style Prominent (led 8% of runs) | runs in data 3 | last 3: 10 Jun Hamilton Flat 6f Good To Soft 5/5; 4 Jul Beverley Flat 5f Good To Firm 5/7; 14 Oct Kempton (AW) Flat 6f Standard / Slow 8/8 fig 24
    DATA against: Best recent form figure 24, 29 lb below field average; Recent figures 30 lb below its current mark (looks high in the weights); Last-run finishing speed -4.9% vs that field (faded)

## 6:25 Kempton (AW) | race_id rac_32305510120 | Bet £20 Get £20 With Unibet Handicap Stakes
Flat | Class 6 | 1m | going Standard / Slow | AW | 12 runners | rating band 0-60 | age 3yo
DATA pace: Lone leader - Heated Moment is the only habitual front-runner and may be allowed an easy lead.
- Roccobear (hrs_57590183) | 3yo G | 132lb | OR 57 | draw 4 | jockey Marco Ghiani | trainer J. R. Jenkins (14d 1/6) | headgear - | last run 28 days | form 563543 | MARKET 16.6% | 09:00 median 5.00 | Matchbook 5.40 | CHECK (skip line 4.75)
    comment: Third last time out and a third four starts back, Roccobear has been consistently in the mix, and he's had 28 days to recover while having run over today's trip and going before.
    DATA: model 10.2% | style Midfield (led 5% of runs) | runs in data 8 | last 3: 8 Jul Kempton Flat 8f Standard To Slow 5/13; 29 Sep Wolverhampton Flat 7.2f Standard 4/10; 28 Oct Kempton (AW) Flat 8f Standard / Slow 3/6 fig 61
    DATA for: Best recent form figure 61, 6 lb above field average; Recent figures 4 lb above its current mark (looks well handicapped)
- Melodical (hrs_52452176) | 3yo F | 135lb | OR 60 | draw 7 | jockey Ashley Lewis(3) | trainer Ed Walker (14d 1/15) | headgear - | last run 28 days | form -65531 | MARKET 16.2% | 09:00 median 4.50 | Matchbook 6.20
    comment: Winning last time out is a clear plus for Melodical, a third two starts back adding to the picture, and she has run over today's trip after 28 days off.
    DATA: model 14.4% | style Prominent (led 8% of runs) | runs in data 5 | last 3: 12 Sep Lingfield Flat 8f Standard 5/9; 30 Sep Kempton Flat 8f Standard To Slow 3/11; 28 Oct Kempton (AW) Flat 8f Standard / Slow 1/6 fig 63
    DATA for: Best recent form figure 63, 8 lb above field average; Has won at this trip or further; Good recent finishing positions
- Aurelune (hrs_61012630) | 3yo F | 133lb | OR 58 | draw 1 | jockey Billy Loughnane | trainer Richard & Peter Fahey (14d 0/12) | headgear p (1st time) | last run 37 days | form 367322 | MARKET 15.8% | 09:00 median 5.00 | Matchbook 5.90
    comment: Aurelune is winless in her last six, though two seconds in her latest two runs and a third three starts back show she is competitive, and she has run over today's trip.
    DATA: model 14.1% | style Prominent (led 3% of runs) | runs in data 7 | last 3: 4 Jul Leicester Flat 8.2f Good To Firm 3/9; 2 Sep Hamilton Flat 8.3f Soft 2/10; 19 Oct Southwell (AW) Flat 8f Standard 2/14 fig 60
    DATA for: Best recent form figure 60, 5 lb above field average; Good recent finishing positions; First-time headgear
    DATA against: Trainer 0 wins from 12 runs, last 14 days
- Karakula Dancer (hrs_49142709) | 3yo G | 132lb | OR 57 | draw 5 | jockey Alice Bond(5) | trainer Martin Dunne (14d 0/4) | headgear p | last run 4 days | form 833486 | MARKET 13.7% | 09:00 median 6.00 | Matchbook 6.80
    comment: Karakula Dancer is yet to win in his last six, though thirds four and five starts back show he can get involved, and he has run over today's trip and going.
    DATA: model 8.6% | style Midfield (led 3% of runs) | runs in data 15 | last 3: 30 Sep Kempton Flat 8f Standard To Slow 4/11; 23 Oct Wolverhampton (AW) Flat 8.5f Standard 8/11 fig 51; 21 Nov Newcastle (AW) Flat 8f Standard 6/13 fig 52
    DATA for: Has won at this trip or further
- Blue Hill (hrs_50435315) | 3yo F | 132lb | OR 57 | draw 6 | jockey Shay Farmer(5) | trainer Adam Kirby (14d 1/8) | headgear - | last run 28 days | form 545573 | MARKET 11.7% | 09:00 median 7.00 | Matchbook 8.00
    DATA: model 9.0% | style Midfield (led 29% of runs) | runs in data 6 | last 3: 10 Sep Epsom Downs Flat 12f Good To Soft 5/14; 14 Oct Nottingham Flat 8.5f Good To Soft 7/8 fig 45; 28 Oct Kempton (AW) Flat 8f Standard / Slow 3/10 fig 67
    DATA for: Best recent form figure 67, 12 lb above field average; Recent figures 10 lb above its current mark (looks well handicapped)
- Upsomdowns (hrs_56406812) | 3yo C | 133lb | OR 58 | draw 10 | jockey Paddy Bradley | trainer Pat Phelan (14d 1/5) | headgear p (1st time) | last run 28 days | form 280404 | MARKET 10.2% | 09:00 median 8.00 | Matchbook 9.20
    comment: Upsomdowns was fourth last time out and fourth again three starts back, but he's yet to win in his last six outings, with a second six starts back his best finish.
    DATA: model 9.3% | style Midfield (led 3% of runs) | runs in data 6 | last 3: 23 Sep Kempton Flat 7f Standard To Slow 4/13; 7 Oct Kempton Flat 7f Standard To Slow 10/14; 28 Oct Kempton (AW) Flat 8f Standard / Slow 4/10 fig 67
    DATA for: Best recent form figure 67, 12 lb above field average; Recent figures 9 lb above its current mark (looks well handicapped); Trainer 20% wins (1/5), last 14 days; First-time headgear
- Q T Pie (hrs_54555515) | 3yo F | 134lb | OR 59 | draw 8 | jockey William Carson | trainer Tom Dascombe (14d 0/1) | headgear p | last run 28 days | form 295884 | MARKET 3.7% | 09:00 median 21.00 | Matchbook 30.00
    comment: The risk is a winless run in her last six, with two eighths in the middle of that sequence, and she carries 134 lb from draw 8.
    DATA: model 5.3% | style Held up (led 5% of runs) | runs in data 6 | last 3: 16 Sep Yarmouth Flat 6f Good To Soft 8/12; 13 Oct Wolverhampton Flat 6.1f Standard 8/12; 28 Oct Kempton (AW) Flat 8f Standard / Slow 4/9 fig 57
- Starakova (hrs_53539514) | 3yo F | 132lb | OR 57 | draw 9 | jockey Harry Vigors(5) | trainer Warren Greatrex (14d 6/24) | headgear p | last run 37 days | form 173109 | MARKET 3.6% | 09:00 median 21.00 | Matchbook 30.00
    comment: Starakova has won twice in her last six, a first three starts back and another six starts back, but she was unplaced two starts back and only ninth last time out, 37 days ago.
    DATA: model 9.5% | style Held up (led 4% of runs) | runs in data 8 | last 3: 6 Aug Southwell Flat 8.1f Standard 1/8; 24 Sep Southwell Flat 8.1f Standard 11/13; 19 Oct Southwell (AW) Flat 8f Standard 9/14 fig 52
    DATA for: Trainer 25% wins (6/24), last 14 days; Has won at this trip or further
- Heated Moment (hrs_55515964) | 3yo F | 127lb | OR 52 | draw 11 | jockey Robert Havlin | trainer Conrad Allen (14d 0/3) | headgear - | last run 4 days | form 5-5547 | MARKET 2.7% | 09:00 median 29.00 | Matchbook 40.00
    comment: Heated Moment is yet to win in her last five starts, finishing seventh last time out, with a fourth two starts back the best of a modest bunch.
    DATA: model 10.0% | style Leader (led 57% of runs) | runs in data 4 | last 3: 8 May Ripon Flat 9.8f Good 5/8; 8 Jun Windsor Flat 8.1f Good To Soft 4/12; 21 Nov Lingfield (AW) Flat 8f Standard 7/10 fig 39
    DATA for: Carries 6 lb less than average; Pace: may get an uncontested lead
    DATA against: Best recent form figure 39, 16 lb below field average; Recent figures 13 lb below its current mark (looks high in the weights); Official rating 52, 6 lb below field average; Last-run finishing speed -2.5% vs that field (faded)
- Wield (hrs_54644695) | 3yo G | 135lb | OR 60 | draw 13 | jockey Luke Morris | trainer Joseph Parr (14d 0/2) | headgear t | last run 21 days | form 729000 | MARKET 2.2% | 09:00 median 38.00 | Matchbook 48.00
    comment: Wield has been unplaced in his last three outings and is winless in his last six, though a second five starts back shows he can hit the frame, and he has run over today's trip.
    DATA: model 4.1% | style Midfield (led 4% of runs) | runs in data 10 | last 3: 3 Oct Southwell Flat 8.1f Standard 11/13; 22 Oct Newmarket Flat 8f Soft 13/13 fig 27; 4 Nov Kempton (AW) Flat 8f Standard / Slow 10/13 fig 40
    DATA against: Best recent form figure 40, 15 lb below field average; Recent figures 20 lb below its current mark (looks high in the weights); Poor recent finishing positions
- Venetian Romance (hrs_54933781) | 3yo F | 131lb | OR 56 | draw 3 | jockey Kieren Fox | trainer Michael Attwater (14d 1/9) | headgear p | last run 29 days | form 626956 | MARKET 2.1% | 09:00 median 34.00 | Matchbook 60.00
    comment: Venetian Romance has run over today's trip and on this going, and her last two outings, a sixth then a fifth two starts back, show her holding her own after a 29-day break. Yet to win in her last six, she still gets the nod on overall profile, with her second five starts back the best of her recent finishes.
    DATA: model 2.8% | style Midfield (led 5% of runs) | runs in data 8 | last 3: 12 Sep Lingfield Flat 7f Standard 9/9; 6 Oct Brighton Flat 8f Good To Firm 5/10; 27 Oct Wolverhampton (AW) Flat 7f Standard 6/9 fig 50
    DATA against: Best recent form figure 50, 5 lb below field average; Recent figures 6 lb below its current mark (looks high in the weights)
- Salamis Bay (hrs_60944919) | 3yo F | 134lb | OR 59 | draw 12 | jockey Hollie Doyle | trainer Gay Kelleway (14d 0/4) | headgear p (1st time) | last run 150 days | form 44759 | MARKET 1.5% | 09:00 median 41.00 | Matchbook 110.00
    comment: Winless in her last five and beaten into ninth last time out, Salamis Bay returns after 150 days off, which makes her hard to fancy, though two fourths in her last five show she is not completely out of her depth.
    DATA: model 2.8% | style Prominent (led 3% of runs) | runs in data 5 | last 3: 8 May Ascot Flat 10f Good 7/7; 11 Jun Yarmouth Flat 11.5f Soft 5/8; 28 Jun Wolverhampton Flat 9.5f Standard 9/11
    DATA for: First-time headgear
    DATA against: Returns from a 150-day break

## 7:00 Kempton (AW) | race_id rac_32305512057 | Unibet Floodlit Stakes (Listed Race)
Flat | Class 1 | 1m3f219y | going Standard / Slow | AW | 8 runners | rating band - | age 3yo+
DATA pace: Lone leader - Virtual Rock is the only habitual front-runner and may be allowed an easy lead.
- El Cordobes (hrs_36035601) | 5yo G | 133lb | OR 114 | draw 2 | jockey Billy Loughnane | trainer Charlie Appleby (14d 3/7) | headgear - | last run 25 days | form 33-530 | MARKET 38.7% | 09:00 median 2.25 | Matchbook 2.46
    comment: El Cordobes has hit the frame in three of his last five, including a third two starts back, but he was unplaced last time out and is yet to win in that spell.
    DATA: model 17.7% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Official rating 114, 11 lb above field average; Trainer 43% wins (3/7), last 14 days
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Amiloc (hrs_43951012) | 4yo G | 133lb | OR 113 | draw 5 | jockey Hollie Doyle | trainer Ralph Beckett (14d 2/10) | headgear - | last run 39 days | form 66U717 | MARKET 17.6% | 09:00 median 5.00 | Matchbook 5.40
    comment: A seventh last time out after 39 days off is the main concern, and he carries 133 lb.
    DATA: model 12.8% | style Prominent (led 5% of runs) | runs in data 6 | last 3: 21 Aug York Flat 16.3f Good To Soft 7/8; 11 Sep Salisbury Flat 14.2f Soft 1/4; 17 Oct Ascot Flat 16f Good 7/10 fig 104
    DATA for: Best recent form figure 104, 9 lb above field average; Official rating 113, 10 lb above field average; Trainer 20% wins (2/10), last 14 days; Has won at this trip or further
- Constitution Hill (hrs_24675280) | 9yo G | 133lb | OR 106 | draw 7 | jockey Oisin Murphy | trainer Nicky Henderson (14d 4/20) | headgear - | last run 31 days | form 1145 | MARKET 15.6% | 09:00 median 5.50 | Matchbook 6.20
    comment: The risk is a drift in form, with a fifth last time out following a fourth two starts back.
    DATA: model 18.9% | style Held up (led 5% of runs) | runs in data 3 | last 3: 20 Feb Southwell Flat 12.1f Standard 1/13; 25 Mar Kempton Flat 12f Standard To Slow 1/8; 5 Sep Kempton Flat 12f Standard To Slow 4/5
    DATA for: Trainer 20% wins (4/20), last 14 days; Has won at this trip or further; Good recent finishing positions
    DATA against: Aged 9, older than most of this field; Course: hold-up horses have won 0.7× their fair share at 12f here
- Royal Playwright (hrs_41629609) | 4yo C | 133lb | OR 106 | draw 8 | jockey Jason Watson | trainer Andrew Balding (14d 4/32) | headgear - | last run 26 days | form 53-522 | MARKET 13.6% | 09:00 median 6.50 | Matchbook 6.80
    comment: Royal Playwright arrives in cracking nick, runner-up last time out and again two starts back, and he returns fresh after 26 days having run over today's trip before. The one worry is that he's yet to win in his last five starts, so he still has to get his head in front.
    DATA: model 11.3% | style Held up (led 8% of runs) | runs in data 3 | last 3: 5 Jun Epsom Downs Flat 8.5f Good To Soft 5/8; 3 Oct Ascot Flat 12f Good To Firm 2/5; 30 Oct Newmarket Flat 12f Good To Soft 2/6 fig 114
    DATA for: Best recent form figure 114, 19 lb above field average; Last-run finishing speed +2.3% vs that field (finished strongly); Good recent finishing positions
    DATA against: Course: hold-up horses have won 0.7× their fair share at 12f here
- Lion's Pride (hrs_34962193) | 6yo G | 133lb | OR 107 | draw 1 | jockey Robert Havlin | trainer John & Thady Gosden (14d 2/21) | headgear - | last run 63 days | form 5-6464 | MARKET 6.7% | 09:00 median 13.00 | Matchbook 14.50
    comment: Lion's Pride has been consistent, finishing a fourth last time out and sitting in the top six in each of his last five starts, and he has run over today's trip and going before.
    DATA: model 6.7% | style Unknown | runs in data 3 | last 3: 18 Apr Newbury Flat 12f Good 4/6; 1 May Newmarket Flat 12f Good To Firm 6/6; 23 Sep Goodwood Flat 9.9f Good 4/5
- Besieged (hrs_63422639) | 3yo C | 128lb | OR 90 | draw 4 | jockey Lewis Edmunds | trainer Harry Charlton (14d 0/2) | headgear p (1st time) | last run 76 days | form 2210 | MARKET 5.3% | 09:00 median 17.00 | Matchbook 18.00
    comment: Unplaced last time out and off a 76-day break, Besieged is hard to fancy, though he did win two starts back and was second three and four starts back, and has run on today's going.
    DATA: model 7.8% | style Prominent (led 8% of runs) | runs in data 4 | last 3: 15 May Newbury Flat 10f Good 2/11; 9 Jun Salisbury Flat 9.9f Soft 1/10; 10 Sep Doncaster Flat 10.2f Good To Soft 11/11
    DATA for: Good recent finishing positions; First-time headgear
    DATA against: Official rating 90, 13 lb below field average
- Janey Mackers (hrs_45662232) | 4yo F | 128lb | OR 90 | draw 3 | jockey Sean Levey | trainer David Menuisier (14d 0/3) | headgear - | last run 32 days | form 150-30 | MARKET 1.4% | 09:00 median 41.00 | Matchbook 120.00
    comment: Janey Mackers was unplaced last time out and has only a third two starts back to show since her win five starts back, which makes her hard to fancy off 128 lb.
    DATA: model 4.0% | style Held up (led 5% of runs) | runs in data 2 | last 3: 8 May Chester Flat 10.3f Good 3/11; 24 Oct Doncaster Flat 10f Heavy 10/14 fig 68
    DATA against: Best recent form figure 68, 27 lb below field average; Official rating 90, 13 lb below field average; Lightly raced: 2 runs in our data, so the model has little to go on; Course: hold-up horses have won 0.7× their fair share at 12f here
- Virtual Rock (hrs_27343379) | 7yo G | 133lb | OR 100 | draw 6 | jockey Darragh Keenan | trainer Des Donovan (14d 1/4) | headgear t | last run 4 days | form 4361/0 | MARKET 1.2% | 09:00 median 67.00 | Matchbook 130.00
    comment: Lightly raced and open to improvement, Virtual Rock won two starts back before going unplaced last time, and he turns out again just four days later; he carries 133 lb with an official mark of 100.
    DATA: model 20.8% | style Leader (led 38% of runs) | runs in data 6 | last 3: 22 Sep Fontwell Hurdle 17.7f Good 1/5; 14 Oct Wetherby Hurdle 19.5f Good To Firm 2/5 fig 113; 21 Nov Huntingdon Hurdle 16f Good 1/11 fig 128
    DATA for: Good recent finishing positions; Pace: may get an uncontested lead

## 7:30 Kempton (AW) | race_id rac_32305513994 | Unibet London Middle Distance Series (Final) Handicap Stakes (Series Final - Qualified Horses Only) (GBBPlus Race)
Flat | Class 2 | 1m2f219y | going Standard / Slow | AW | 14 runners | rating band - | age 3yo+
DATA pace: Even - Two likely leaders (Forever Penywern, Sax Avoidance). A fair, even gallop is most likely.
- Classical Allusion (hrs_45474807) | 4yo G | 119lb | OR 86 | draw 5 | jockey Oisin Murphy | trainer Andrew Balding (14d 4/32) | headgear - | last run 63 days | form 250661 | MARKET 18.1% | 09:00 median 4.33 | Matchbook 5.00 | CHECK (skip line 4.11)
    DATA: model 6.6% | style Midfield (led 4% of runs) | runs in data 6 | last 3: 12 Aug Kempton Flat 12f Standard To Slow 6/12; 29 Aug Goodwood Flat 12f Soft 6/9; 23 Sep Kempton Flat 11f Standard To Slow 1/8
    DATA for: Has won at this trip or further
- Tryfan (hrs_35149394) | 5yo G | 117lb | OR 84 | draw 1 | jockey Shay Farmer(5) | trainer Harry Charlton (14d 0/2) | headgear p | last run 42 days | form 071532 | MARKET 14.7% | 09:00 median 5.50 | Matchbook 6.00
    comment: Tryfan has been in the frame lately, second last time out and third two starts back, but he has won only once in his last six, four starts back, and a 42-day break raises fitness questions.
    DATA: model 5.9% | style Held up (led 8% of runs) | runs in data 8 | last 3: 15 Aug Newbury Flat 12f Good To Firm 5/5; 22 Sep Southwell Flat 12.1f Standard 3/10; 14 Oct Kempton (AW) Flat 11f Standard / Slow 2/13 fig 87
    DATA for: Has won at this trip or further; Good recent finishing positions
- Solarize (hrs_43287748) | 4yo C | 127lb | OR 94 | draw 8 | jockey Callum Shepherd | trainer Charlie Johnston (14d 0/10) | headgear v (1st time) | last run 18 days | form 5-2114 | MARKET 10.6% | 09:00 median 8.00 | Matchbook 8.40
    comment: Solarize arrives fit after 18 days, a winner two and three starts back before a fourth last time out, and he has run over today's trip and on this going. Drawn eight and carrying 127 lb, his main risk is that the latest fourth suggests the winning run may have stalled.
    DATA: model 19.6% | style Prominent (led 3% of runs) | runs in data 4 | last 3: 22 Sep Southwell Flat 12.1f Standard 1/10; 6 Oct Leicester Flat 11.8f Good To Firm 1/5; 7 Nov Doncaster Flat 12f Good To Soft 4/23 fig 98
    DATA for: Best recent form figure 98, 10 lb above field average; Recent figures 4 lb above its current mark (looks well handicapped); Official rating 94, 6 lb above field average; Has won at this trip or further; Good recent finishing positions; First-time headgear
    DATA against: Trainer 0 wins from 10 runs, last 14 days; Carries 6 lb more than average
- Tiernan (hrs_53211613) | 4yo G | 117lb | OR 84 | draw 3 | jockey Andrew Mullen | trainer Iain Jardine (14d 0/9) | headgear p (1st time) | last run 36 days | form 152635 | MARKET 8.2% | 09:00 median 9.50 | Matchbook 12.00
    comment: Tiernan arrives on a 36-day break after a fifth last time out, with a third two starts back showing some consistency, though he has won once in his last six, six starts back.
    DATA: model 5.4% | style Held up (led 3% of runs) | runs in data 9 | last 3: 17 Sep Ayr Flat 10f Soft 6/11; 30 Sep Kempton Flat 11f Standard To Slow 3/10; 20 Oct Newcastle (AW) Flat 12.5f Standard 5/9 fig 78
    DATA for: Has won at this trip or further; First-time headgear
    DATA against: Best recent form figure 78, 10 lb below field average; Recent figures 6 lb below its current mark (looks high in the weights); Trainer 0 wins from 9 runs, last 14 days
- War Hawk (hrs_46046042) | 4yo G | 121lb | OR 88 | draw 10 | jockey Harry Davies | trainer Simon Crisford (14d 2/7) | headgear t | last run 42 days | form 365561 | MARKET 7.9% | 09:00 median 11.00 | Matchbook 10.00
    comment: War Hawk won last time out, but that sits among a run of fifth and sixth-place finishes before it, and a 42-day break makes it hard to fancy at 121 lb from draw 10.
    DATA: model 8.0% | style Held up (led 4% of runs) | runs in data 3 | last 3: 17 Jul Newmarket Flat 10f Good To Firm 5/6; 30 Aug Goodwood Flat 9.9f Soft 6/10; 14 Oct Kempton (AW) Flat 11f Standard / Slow 1/13 fig 88
    DATA for: Trainer 29% wins (2/7), last 14 days; Has won at this trip or further
- Cape Fear (hrs_57718689) | 3yo C | 115lb | OR 86 | draw 6 | jockey Nicola Currie | trainer Andrew Balding (14d 4/32) | headgear - | last run 56 days | form 132152 | MARKET 6.8% | 09:00 median 12.25 | Matchbook 12.50
    DATA: model 5.5% | style Prominent (led 23% of runs) | runs in data 10 | last 3: 24 Aug Windsor Flat 11.4f Good To Firm 1/7; 5 Sep Ascot Flat 12f Good To Firm 5/9; 30 Sep Kempton Flat 11f Standard To Slow 2/10
    DATA for: Has won at this trip or further; Good recent finishing positions; Carries 6 lb less than average
- Paradias (hrs_26319475) | 7yo G | 138lb | OR 105 | draw 11 | jockey Sean Levey | trainer Alan King (14d 2/20) | headgear - | last run 95 days | form 135530 | MARKET 6.4% | 09:00 median 10.00 | Matchbook 18.00
    comment: Paradias has made the frame twice in his last six, a third two starts back and another third five starts back, and he has run over today's trip and going before.
    DATA: model 6.1% | style Held up (led 4% of runs) | runs in data 7 | last 3: 28 May Sandown Flat 16.2f Good 5/7; 3 Jul Sandown Flat 16.2f Good 3/4; 22 Aug York Flat 13.9f Good To Soft 11/22
    DATA for: Official rating 105, 17 lb above field average; Has won at this trip or further
    DATA against: Carries 17 lb more than average; Returns from a 95-day break
- King's Code (hrs_31069213) | 6yo G | 122lb | OR 89 | draw 9 | jockey Hollie Doyle | trainer David Evans (14d 0/9) | headgear v | last run 50 days | form 188873 | MARKET 5.9% | 09:00 median 11.00 | Matchbook 18.50
    comment: King's Code showed signs of revival with a third last time out, though that followed a seventh and three eighths, with a win six starts back.
    DATA: model 3.5% | style Prominent (led 23% of runs) | runs in data 14 | last 3: 5 Sep Kempton Flat 12f Standard To Slow 8/11; 19 Sep Newbury Flat 10f Good To Firm 7/11; 6 Oct Leicester Flat 11.8f Good To Firm 3/5
    DATA against: Trainer 0 wins from 9 runs, last 14 days
- Hamlet's Night (hrs_38073616) | 5yo G | 116lb | OR 83 | draw 7 | jockey Luke Morris | trainer James Owen (14d 4/46) | headgear p | last run 25 days | form 64-131 | MARKET 4.5% | 09:00 median 17.00 | Matchbook 21.00
    comment: Won last time out and again three starts back, with a third two starts back, so Hamlet's Night arrives in good heart after 25 days off, and he has run over today's trip and going.
    DATA: model 2.3% | style Held up (led 4% of runs) | runs in data 9 | last 3: 9 Oct Chepstow Hurdle 16.1f Good To Soft 10/17; 22 Oct Carlisle Hurdle 17f Good 6/8 fig 136; 31 Oct Ascot Hurdle 15.5f Good To Firm 14/16 fig 113
    DATA for: Has won at this trip or further; Carries 5 lb less than average
    DATA against: Official rating 83, 5 lb below field average; Poor recent finishing positions
- Londoner (hrs_31300283) | 6yo G | 120lb | OR 87 | draw 14 | jockey Marco Ghiani | trainer Daniel & Claire Kubler (14d 1/1) | headgear p | last run 42 days | form 424243 | MARKET 4.5% | 09:00 median 17.00 | Matchbook 22.00
    comment: Londoner has been in the frame often, a third last time out, a fourth two starts back and a second three starts back, but he is winless in his last six and hasn't been seen for 42 days.
    DATA: model 10.7% | style Held up (led 4% of runs) | runs in data 14 | last 3: 7 Sep Wolverhampton Flat 8.6f Standard 2/12; 22 Sep Southwell Flat 8.1f Standard 4/11; 14 Oct Kempton (AW) Flat 11f Standard / Slow 3/13 fig 91
    DATA for: Recent figures 4 lb above its current mark (looks well handicapped); Good recent finishing positions
- Forever Penywern (hrs_39961481) | 4yo G | 119lb | OR 86 | draw 4 | jockey Harry Vigors(5) | trainer Warren Greatrex (14d 6/24) | headgear - | last run 28 days | form 1-1382 | MARKET 4.2% | 09:00 median 17.00 | Matchbook 25.00
    DATA: model 8.1% | style Leader (led 54% of runs) | runs in data 8 | last 3: 12 Aug Kempton Flat 12f Standard To Slow 3/12; 30 Sep Kempton Flat 11f Standard To Slow 8/10; 28 Oct Kempton (AW) Flat 12f Standard / Slow 2/10 fig 85
    DATA for: Trainer 25% wins (6/24), last 14 days; Has won at this trip or further; Good recent finishing positions
- Haku (hrs_27301645) | 7yo G | 127lb | OR 94 | draw 13 | jockey Billy Loughnane | trainer Mark Loughnane (14d 2/18) | headgear - | last run 81 days | form 3-7385 | MARKET 3.6% | 09:00 median 15.00 | Matchbook 44.00
    comment: Haku has twice finished third in his last five, a third five starts back among them, and he has run over today's trip and going before.
    DATA: model 5.3% | style Prominent (led 3% of runs) | runs in data 4 | last 3: 1 Aug Newmarket Flat 12f Good To Firm 3/8; 29 Aug Goodwood Flat 12f Soft 8/9; 5 Sep Kempton Flat 12f Standard To Slow 5/11
    DATA for: Official rating 94, 6 lb above field average
    DATA against: Carries 6 lb more than average
- Sax Avoidance (hrs_64523018) | 3yo F | 114lb | OR 76 | draw 2 | jockey Tyler Heard | trainer Charlie Pike (14d 0/3) | headgear - | last run 51 days | form 543112 | MARKET 2.6% | 09:00 median 21.00 | Matchbook 55.00
    DATA: model 6.9% | style Leader (led 57% of runs) | runs in data 6 | last 3: 11 Sep Salisbury Flat 9.9f Soft 1/10; 14 Sep Kempton Flat 11f Standard To Slow 1/9; 5 Oct Kempton Flat 11f Standard To Slow 2/9
    DATA for: Has won at this trip or further; Good recent finishing positions; Carries 7 lb less than average
    DATA against: Official rating 76, 12 lb below field average
- Night Breeze (hrs_36738772) | 6yo G | 126lb | OR 93 | draw 12 | jockey Charles Bishop | trainer Ian Williams (14d 3/23) | headgear t | last run 18 days | form 233590 | MARKET 1.9% | 09:00 median 34.00 | Matchbook 75.00
    comment: Night Breeze is yet to win in his last six starts, but he showed a second and two thirds before a fifth and a ninth, and he returns just 18 days after an unplaced last run.
    DATA: model 6.0% | style Held up (led 8% of runs) | runs in data 14 | last 3: 8 Aug Ascot Flat 12f Good To Firm 5/10; 12 Sep Doncaster Flat 10.2f Good 9/12; 7 Nov Doncaster Flat 12f Good To Soft 10/23 fig 92
    DATA for: Has won at this trip or further

## 8:00 Kempton (AW) | race_id rac_32305515931 | Unibet's New VAR Goal Guarantee Fillies' Handicap Stakes
Flat | Class 5 | 1m2f219y | going Standard / Slow | AW | 11 runners | rating band 0-70 | age 3yo+
DATA pace: Lone leader - Lunella is the only habitual front-runner and may be allowed an easy lead.
- Midnight Media (hrs_55795019) | 3yo F | 136lb | OR 70 | draw 14 | jockey Lewis Edmunds | trainer William Muir & Chris Grassick (14d 0/6) | headgear - | last run 7 days | form 224132 | MARKET 22.1% | 09:00 median 3.75 | Matchbook 4.20 | CHECK (skip line 3.56)
    comment: Consistent filly who finished second last time out, and a third two starts back, with a winner three starts back, though she's only won once in her last six and turned out just seven days ago.
    DATA: model 24.0% | style Prominent (led 23% of runs) | runs in data 15 | last 3: 13 Oct Wolverhampton Flat 12.2f Standard 1/11; 29 Oct Southwell (AW) Flat 11f Standard 3/7 fig 70; 18 Nov Kempton (AW) Flat 12f Standard / Slow 2/13 fig 76
    DATA for: Best recent form figure 76, 7 lb above field average; Recent figures 6 lb above its current mark (looks well handicapped); Has won at this trip or further; Good recent finishing positions
- Ghost Story (hrs_41263670) | 5yo M | 137lb | OR 67 | draw 4 | jockey Billy Loughnane | trainer John Butler (14d 2/12) | headgear - | last run 21 days | form 344921 | MARKET 20.7% | 09:00 median 4.00 | Matchbook 4.40
    comment: Ghost Story won last time out and was second two starts back, with fresh legs after 21 days, and she has run over today's trip and on this going before.
    DATA: model 14.2% | style Midfield (led 3% of runs) | runs in data 9 | last 3: 8 Oct Ayr Flat 10f Heavy 9/12; 23 Oct Doncaster Flat 10f Heavy 2/18 fig 64; 4 Nov Nottingham Flat 10f Soft 1/9 fig 67
    DATA for: Last-run finishing speed +2.2% vs that field (finished strongly); Good recent finishing positions
- Glenna (hrs_55764401) | 3yo F | 136lb | OR 70 | draw 5 | jockey Sean Levey | trainer Tom Ward (14d 0/5) | headgear - | last run 21 days | form 133722 | MARKET 17.2% | 09:00 median 5.00 | Matchbook 5.10
    comment: Glenna arrives in sound heart, runner-up in her last two starts and a winner six starts back, fresh enough after 21 days off and she has run over today's trip and going.
    DATA: model 13.0% | style Prominent (led 8% of runs) | runs in data 9 | last 3: 18 Sep Newbury Flat 12f Good 7/8; 14 Oct Kempton (AW) Flat 11f Standard / Slow 2/9 fig 70; 4 Nov Nottingham Flat 10f Soft 2/9 fig 70
    DATA for: Has won at this trip or further; Good recent finishing positions
- Caraway (hrs_55516027) | 3yo F | 132lb | OR 66 | draw 1 | jockey Darragh Keenan | trainer William Haggas (14d 4/22) | headgear - | last run 22 days | form 225122 | MARKET 12.2% | 09:00 median 6.50 | Matchbook 7.80
    comment: Caraway has finished second last time out, and a second two starts back, with a winner three starts back, so she's consistent and fit after 22 days off.
    DATA: model 13.5% | style Held up (led 4% of runs) | runs in data 11 | last 3: 5 Oct Wolverhampton Flat 12.2f Standard 1/11; 23 Oct Wolverhampton (AW) Flat 12f Standard 2/5 fig 70; 3 Nov Wolverhampton (AW) Flat 12f Standard 2/7 fig 62
    DATA for: Recent figures 4 lb above its current mark (looks well handicapped); Last-run finishing speed +2.6% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
- Solar Pass (hrs_47004510) | 4yo F | 139lb | OR 69 | draw 3 | jockey Charlie Tucker(7) | trainer Andrew Balding (14d 4/32) | headgear tp | last run 30 days | form 227705 | MARKET 6.5% | 09:00 median 13.00 | Matchbook 14.00
    comment: The risk is that she is winless in her last six and was only fifth last time, with 139 lb to carry from stall three.
    DATA: model 5.3% | style Prominent (led 8% of runs) | runs in data 9 | last 3: 23 Sep Goodwood Flat 14f Good 7/8; 11 Oct Goodwood Flat 16f Good To Soft 11/12; 26 Oct Southwell (AW) Flat 16.5f Standard 5/6
    DATA for: Has won at this trip or further
    DATA against: Last-run finishing speed -7.1% vs that field (faded)
- Moontune (hrs_17390014831) | 3yo F | 136lb | OR 70 | draw 2 | jockey Marco Ghiani | trainer Stuart Williams (14d 0/5) | headgear - | last run 51 days | form 442 | MARKET 6.3% | 09:00 median 9.50 | Matchbook 21.00
    comment: Moontune was second last time out, with a fourth two starts back and another fourth three starts back, yet she is winless in her last three and returns after 51 days off.
    DATA: model 4.5% | style Held up (led 8% of runs) | runs in data 3 | last 3: 3 Aug Nottingham Flat 8.3f Good To Firm 4/5; 4 Sep Kempton Flat 8f Standard To Slow 4/4; 5 Oct Yarmouth Flat 8f Good To Firm 2/5
- Lunella (hrs_64460249) | 3yo F | 134lb | OR 68 | draw 11 | jockey Hector Crouch | trainer Ollie Sangster (14d 1/12) | headgear - | last run 23 days | form 3244 | MARKET 5.1% | 09:00 median 13.00 | Matchbook 23.00
    comment: Lunella has been consistent, finishing a fourth last time out, a fourth two starts back, a second three starts back and a third four starts back, and she has run over today's trip before.
    DATA: model 6.4% | style Leader (led 38% of runs) | runs in data 4 | last 3: 15 Jul Lingfield Flat 11.6f Good To Firm 2/4; 12 Aug Kempton Flat 12f Standard To Slow 4/5; 2 Nov Wolverhampton (AW) Flat 9.5f Standard 4/9 fig 66
    DATA for: Pace: may get an uncontested lead
- Lucky Luna (hrs_50435042) | 3yo F | 135lb | OR 69 | draw 6 | jockey Joe Leavy | trainer Richard Hannon (14d 1/11) | headgear - | last run 21 days | form 162598 | MARKET 3.4% | 09:00 median 23.00 | Matchbook 29.00
    comment: The risk is a slide, with an eighth last time out and a ninth before that.
    DATA: model 5.4% | style Prominent (led 5% of runs) | runs in data 8 | last 3: 18 Sep Newbury Flat 10f Good 5/8; 5 Oct Kempton Flat 11f Standard To Slow 9/9; 4 Nov Nottingham Flat 10f Soft 8/9 fig 60
    DATA against: Best recent form figure 60, 9 lb below field average; Recent figures 9 lb below its current mark (looks high in the weights)
- Just Queen High (hrs_53602290) | 4yo F | 133lb | OR 63 | draw 8 | jockey Charles Bishop | trainer Ian Williams (14d 3/23) | headgear p | last run 21 days | form 097028 | MARKET 2.6% | 09:00 median 23.00 | Matchbook 48.00
    comment: Winless in her last six, Just Queen High was eighth last time out 21 days ago and has little else to shout about, though a second two starts back shows she can get involved.
    DATA: model 6.5% | style Midfield (led 4% of runs) | runs in data 8 | last 3: 2 Oct Newcastle Flat 7.1f Standard 12/13; 29 Oct Bath Flat 8f Soft 2/14 fig 74; 4 Nov Nottingham Flat 8.5f Soft 8/15 fig 44
    DATA for: Best recent form figure 74, 5 lb above field average; Recent figures 11 lb above its current mark (looks well handicapped); Last-run finishing speed +2.1% vs that field (finished strongly)
- Golden Phase (hrs_30123366) | 6yo M | 131lb | OR 61 | draw 12 | jockey Hollie Doyle | trainer Denis Coakley (14d 1/4) | headgear - | last run 63 days | form 30-640 | MARKET 2.0% | 09:00 median 26.00 | Matchbook 95.00
    comment: Golden Phase is winless in her last five, unplaced last time and a fourth two starts back, and she returns after 63 days off, so she is hard to fancy. In her favour, she has run over today's trip and on this going, and she's drawn 12.
    DATA: model 2.8% | style Held up (led 4% of runs) | runs in data 3 | last 3: 24 Jul Sandown Flat 9.9f Good To Firm 6/6; 28 Aug Sandown Flat 9.9f Good 4/8; 23 Sep Kempton Flat 11f Standard To Slow 14/14
    DATA against: Official rating 61, 6 lb below field average; Last-run finishing speed -5.3% vs that field (faded); Aged 6, older than most of this field
- Star of Dubai (hrs_47192159) | 4yo F | 135lb | OR 65 | draw 10 | jockey Rob Hornby | trainer Denis Coakley (14d 1/4) | headgear - | last run 89 days | form 86-950 | MARKET 1.8% | 09:00 median 41.00 | Matchbook 70.00
    comment: Star of Dubai is winless in her last five, finishing unplaced last time out and a fifth two starts back, and she returns after 89 days off.
    DATA: model 4.3% | style Prominent (led 5% of runs) | runs in data 3 | last 3: 11 Jul Ascot Flat 8f Good To Firm 9/9; 27 Jul Windsor Flat 8.1f Good To Firm 5/8; 28 Aug Goodwood Flat 9.9f Good To Firm 12/12
    DATA against: Last-run finishing speed -5.2% vs that field (faded)

## 8:30 Kempton (AW) | race_id rac_32305517868 | Try Unibet's New Smartview Racecards Handicap Stakes
Flat | Class 5 | 7f | going Standard / Slow | AW | 14 runners | rating band 0-70 | age 3yo+
DATA pace: Even - Two likely leaders (Token Gesture, King Cherry). A fair, even gallop is most likely.
- Split Elevens (hrs_21713517) | 8yo G | 136lb | OR 67 | draw 6 | jockey Billy Loughnane | trainer John Butler (14d 2/12) | headgear - | last run 9 days | form 122223 | MARKET 19.4% | 09:00 median 4.33 | Matchbook 4.50 | CHECK (skip line 4.11)
    comment: Split Elevens is consistent, with a third last time out and four seconds before that, though he has just the one win in his last six starts and that came six starts back.
    DATA: model 19.7% | style Held up (led 3% of runs) | runs in data 13 | last 3: 17 Oct Southwell (AW) Flat 7f Standard 2/9 fig 70; 28 Oct Kempton (AW) Flat 7f Standard / Slow 2/13 fig 70; 16 Nov Wolverhampton (AW) Flat 7f Standard 3/11 fig 72
    DATA for: Best recent form figure 72, 10 lb above field average; Recent figures 5 lb above its current mark (looks well handicapped); Has won at this trip or further; Good recent finishing positions
- Phoenix of Dreams (hrs_38058132) | 5yo G | 142lb | OR 68 | draw 11 | jockey James Sullivan | trainer John & Sean Quinn (14d 1/8) | headgear - | last run 8 days | form 732181 | MARKET 18.4% | 09:00 median 4.50 | Matchbook 5.00
    comment: The one concern is a 142 lb burden from draw 11, with an eighth two starts back showing he can have an off day.
    DATA: model 16.7% | style Midfield (led 4% of runs) | runs in data 12 | last 3: 9 Oct Kempton Flat 7f Standard To Slow 1/11; 26 Oct Redcar Flat 7f Heavy 8/12 fig 61; 17 Nov Southwell (AW) Flat 7f Standard 1/11 fig 77
    DATA for: Best recent form figure 77, 15 lb above field average; Recent figures 9 lb above its current mark (looks well handicapped); Last-run finishing speed +3.3% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Carries 8 lb more than average
- Billy Mill (hrs_20977614) | 8yo G | 138lb | OR 69 | draw 9 | jockey Lewis Edmunds | trainer Rod Millman (14d 0/3) | headgear - | last run 125 days | form 322263 | MARKET 12.0% | 09:00 median 5.00 | Matchbook 10.00
    comment: Billy Mill has been thereabouts in his recent starts, third last time out and a runner-up three starts back, and he has run over today's trip and going before. He is yet to win in his last six starts, and 125 days off is the main risk, with 138 lb to carry from draw nine.
    DATA: model 7.9% | style Held up (led 3% of runs) | runs in data 11 | last 3: 10 Jun Kempton Flat 8f Standard To Slow 2/11; 2 Jul Kempton Flat 8f Standard To Slow 6/10; 23 Jul Sandown Flat 8f Good To Firm 3/12
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Returns from a 125-day break
- Guilty Verdict (hrs_55484597) | 3yo G | 132lb | OR 64 | draw 2 | jockey Hector Crouch | trainer Jim Boyle (14d 0/7) | headgear - | last run 26 days | form 39-926 | MARKET 11.8% | 09:00 median 7.00 | Matchbook 7.60
    comment: Guilty Verdict is winless in his last five, though a second two starts back and a third five runs ago show he can get involved, and he has run over today's trip. A sixth last time out 26 days ago and 132 lb from stall 2 keep him in the midfield.
    DATA: model 8.4% | style Midfield (led 8% of runs) | runs in data 3 | last 3: 29 Sep Bath Flat 5.7f Good To Firm 9/9; 22 Oct Newmarket Flat 8f Soft 2/13 fig 72; 30 Oct Newmarket Flat 8f Good To Soft 6/15 fig 60
    DATA for: Best recent form figure 72, 10 lb above field average; Recent figures 8 lb above its current mark (looks well handicapped)
- Arctician (hrs_21794528) | 8yo G | 137lb | OR 68 | draw 10 | jockey Paddy Bradley | trainer Simon Dow (14d 0/3) | headgear - | last run 21 days | form 478707 | MARKET 10.5% | 09:00 median 8.00 | Matchbook 8.40
    comment: The risk is a poor recent run of sevenths and an eighth, leaving him winless in his last six, carrying 137 lb from stall ten.
    DATA: model 4.5% | style Midfield (led 5% of runs) | runs in data 7 | last 3: 12 Aug Kempton Flat 7f Standard To Slow 7/11; 9 Sep Kempton Flat 8f Standard To Slow 13/13; 4 Nov Kempton (AW) Flat 7f Standard / Slow 7/11 fig 66
    DATA against: Poor recent finishing positions
- Rhythm N Rock (hrs_22914752) | 8yo G | 136lb | OR 67 | draw 7 | jockey Neil Callan | trainer John Butler (14d 2/12) | headgear - | last run 21 days | form 015765 | MARKET 8.8% | 09:00 median 9.00 | Matchbook 10.50
    comment: His last three finishes (fifth, sixth, seventh) are a worry, but he carries 136 lb from draw 7.
    DATA: model 8.1% | style Held up (led 4% of runs) | runs in data 7 | last 3: 9 Sep Kempton Flat 8f Standard To Slow 7/13; 22 Oct Newmarket Flat 8f Soft 6/13 fig 73; 4 Nov Kempton (AW) Flat 7f Standard / Slow 5/11 fig 69
    DATA for: Best recent form figure 73, 11 lb above field average; Recent figures 6 lb above its current mark (looks well handicapped); Has won at this trip or further
- Token Gesture (hrs_42815010) | 4yo G | 133lb | OR 64 | draw 3 | jockey Rose Dawes(3) | trainer Mark Usher (14d 0/5) | headgear p | last run 287 days | form 8U-716 | MARKET 4.5% | 09:00 median 17.00 | Matchbook 21.00
    DATA: model 6.9% | style Leader (led 38% of runs) | runs in data 3 | last 3: 6 Jan Wolverhampton Flat 8.6f Standard 7/9; 19 Jan Kempton Flat 8f Standard To Slow 1/8; 11 Feb Kempton Flat 7f Standard To Slow 6/9
    DATA for: Has won at this trip or further
    DATA against: Returns from a 287-day break
- Mollstar (hrs_57590533) | 3yo F | 130lb | OR 62 | draw 1 | jockey Ashley Lewis(3) | trainer Ed Walker (14d 1/15) | headgear - | last run 34 days | form 37-296 | MARKET 3.7% | 09:00 median 21.00 | Matchbook 27.00
    comment: Mollstar is winless in her last five, finishing sixth last time out and a ninth two starts back, which makes her hard to fancy, though a second three starts back shows she can bridge the gap.
    DATA: model 4.1% | style Prominent (led 4% of runs) | runs in data 3 | last 3: 12 Aug Ffos Las Flat 6f Good 2/3; 11 Sep Salisbury Flat 6f Soft 9/12; 22 Oct Newmarket Flat 7f Soft 6/12 fig 60
    DATA for: Last-run finishing speed +2.3% vs that field (finished strongly)
- Hello Humphrey (hrs_53777150) | 3yo G | 131lb | OR 63 | draw 14 | jockey Joey Haynes | trainer Mark Usher (14d 0/5) | headgear - | last run 350 days | form 22343- | MARKET 2.5% | 09:00 median 26.00 | Matchbook 48.00
    comment: Hello Humphrey has been consistent, with a third last time out, a fourth two starts back, a third three starts back and seconds before that, but he is yet to win in that spell.
    DATA: model 5.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 350-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- King Cherry (hrs_63357406) | 3yo G | 127lb | OR 59 | draw 12 | jockey Sean Levey | trainer Stuart Williams (14d 0/5) | headgear ht | last run 28 days | form 091030 | MARKET 2.3% | 09:00 median 26.00 | Matchbook 60.00
    comment: King Cherry was unplaced last time out and has just one win in his last six starts, a victory four starts back, though a third two starts back shows he can still make the frame.
    DATA: model 4.6% | style Leader (led 54% of runs) | runs in data 13 | last 3: 7 Oct Nottingham Flat 6.1f Good To Soft 11/14; 17 Oct Southwell (AW) Flat 6f Standard 3/12 fig 60; 28 Oct Kempton (AW) Flat 6f Standard / Slow 11/11 fig 17
    DATA for: Carries 7 lb less than average
    DATA against: Official rating 59, 6 lb below field average
- Hexagonal (hrs_56961548) | 5yo G | 131lb | OR 62 | draw 13 | jockey Finley Marsh | trainer Jim & Suzi Best (14d 0/2) | headgear - | last run 28 days | form 071979 | MARKET 1.9% | 09:00 median 29.00 | Matchbook 75.00
    comment: Hexagonal has been well beaten lately, ninth last time out and a seventh two starts back, though he did win four starts back and has run over today's trip.
    DATA: model 2.1% | style Midfield (led 3% of runs) | runs in data 15 | last 3: 4 Sep Down Royal Flat 10.7f Good 9/14; 14 Oct Kempton (AW) Flat 8f Standard / Slow 7/9 fig 60; 28 Oct Kempton (AW) Flat 7f Standard / Slow 9/13 fig 55
    DATA for: Has won at this trip or further
    DATA against: Poor recent finishing positions
- Pints In Peace (hrs_51308327) | 3yo G | 137lb | OR 69 | draw 8 | jockey Tom Queally | trainer Jim & Suzi Best (14d 0/2) | headgear - | last run 26 days | form 656998 | MARKET 1.7% | 09:00 median 34.00 | Matchbook 80.00
    comment: Winless in his last six, Pints In Peace was eighth last time out after a ninth, a ninth and a sixth before that, so he is hard to fancy.
    DATA: model 2.1% | style Held up (led 4% of runs) | runs in data 14 | last 3: 28 Sep Brighton Flat 8f Good To Firm 9/10; 14 Oct Kempton (AW) Flat 7f Standard / Slow 9/12 fig 60; 30 Oct Newmarket Flat 8f Good To Soft 8/15 fig 53
    DATA for: Has won at this trip or further
    DATA against: Recent figures 9 lb below its current mark (looks high in the weights); Poor recent finishing positions
- Assessment (hrs_27372471) | 7yo G | 134lb | OR 65 | draw 4 | jockey Darragh Keenan | trainer Des Donovan (14d 1/4) | headgear t | last run 9 days | form 0209/0 | MARKET 1.3% | 09:00 median 51.00 | Matchbook 120.00
    comment: Assessment is winless in his last five, with a second four starts back the one bright spot among four unplaced runs, though he's fresh enough after nine days and has run over today's trip and going.
    DATA: model 5.5% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 16 Nov Wolverhampton (AW) Flat 7f Standard 11/11 fig 24
    DATA against: Best recent form figure 24, 38 lb below field average; Recent figures 41 lb below its current mark (looks high in the weights); Last-run finishing speed -5.8% vs that field (faded); Lightly raced: 1 run in our data, so the model has little to go on
- Enough Already (hrs_13021708) | 10yo G | 128lb | OR 59 | draw 5 | jockey William Cox | trainer Jim & Suzi Best (14d 0/2) | headgear - | last run 305 days | form 9836-7 | MARKET 1.2% | 09:00 median 41.00 | Matchbook 150.00
    comment: Seventh last time out and a third three starts back, this gelding returns after 305 days off and is winless in his last five, though he has run over today's trip and going before.
    DATA: model 3.7% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 24 Jan Lingfield Flat 12f Standard 7/12
    DATA for: Carries 6 lb less than average
    DATA against: Official rating 59, 6 lb below field average; Returns from a 305-day break; Lightly raced: 1 run in our data, so the model has little to go on; Aged 10, older than most of this field
