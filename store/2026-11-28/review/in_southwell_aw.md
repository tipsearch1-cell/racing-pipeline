# Card review packet: Southwell (AW), 2026-11-28

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
{"meeting": "southwell_aw", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 4:30 Southwell (AW) | race_id rac_32305889772 | ARC All Weather Bonus Is Back Novice Stakes (GBB Race)
Flat | Class 4 | 1m13y | going Standard | AW | 8 runners | rating band - | age 3yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Levens Hall (hrs_49142604) | 3yo G | 137lb | OR - | draw 4 | jockey Robert Havlin | trainer John & Thady Gosden (14d 4/28) | headgear - | last run 138 days | form 31 | MARKET 67.2% | 09:00 median 1.29 | Matchbook 1.30
    DATA: model 22.1% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 21 May Southwell Flat 8.1f Standard 3/12; 13 Jul Windsor Flat 8.1f Good To Firm 1/11
    DATA for: Last-run finishing speed +2.3% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Returns from a 138-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- El Nay (hrs_58033619) | 3yo G | 130lb | OR 84 | draw 1 | jockey Marco Ghiani | trainer Tony Carroll (14d 2/41) | headgear - | last run 154 days | form 232324 | MARKET 14.9% | 09:00 median 4.42 | Matchbook 7.20
    DATA: model 19.9% | style Unknown | runs in data 6 | last 3: 29 May Chepstow Flat 10f Good To Firm 3/8; 13 Jun Leicester Flat 8.2f Good 2/7; 27 Jun Chester Flat 7.6f Good 4/4
    DATA for: Good recent finishing positions
    DATA against: Returns from a 154-day break
- Aura Champagne (hrs_56219415) | 3yo F | 125lb | OR 75 | draw 6 | jockey Joe Leavy | trainer Richard Hannon (14d 2/17) | headgear - | wind surgery | last run 6 days | form -33238 | MARKET 6.9% | 09:00 median 9.00 | Matchbook 17.50
    DATA: model 12.4% | style Prominent (led 5% of runs) | runs in data 5 | last 3: 7 Sep Windsor Flat 10f Good 2/7; 19 Sep Newbury Flat 8f Good To Firm 3/3; 22 Nov Lingfield (AW) Flat 8f Standard 8/9 fig 65
    DATA for: Good recent finishing positions
- Francesca's Dream (hrs_17394737535) | 3yo F | 125lb | OR - | draw 2 | jockey Cieren Fallon | trainer Hugo Palmer (14d 0/4) | headgear - | last run - days | form - | MARKET 4.7% | 09:00 median 12.00 | Matchbook 36.00
    DATA: model 9.3% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Micro Flame (hrs_17395998522) | 3yo C | 130lb | OR - | draw 5 | jockey Oisin Orr | trainer John Butler (14d 4/18) | headgear - | last run - days | form - | MARKET 2.2% | 09:00 median 34.00 | Matchbook 50.00
    DATA: model 9.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 22% wins (4/18), last 14 days
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- I Am Legend (hrs_35938518) | 6yo M | 127lb | OR - | draw 8 | jockey Jonny Peate | trainer Jane Chapple-Hyam (14d 1/4) | headgear - | last run 1255 days | form 6/ | MARKET 1.6% | 09:00 median 41.00 | Matchbook 100.00
    DATA: model 9.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 1255-day break; Lightly raced: 0 runs in our data, so the model has little to go on; Aged 6, older than most of this field
- Beatrice Briannie (hrs_17394098176) | 3yo F | 125lb | OR - | draw 7 | jockey Clifford Lee | trainer Michael Appleby (14d 2/24) | headgear - | last run 8 days | form 54 | MARKET 1.5% | 09:00 median 41.00 | Matchbook 130.00
    DATA: model 8.3% | style Held up (led 8% of runs) | runs in data 2 | last 3: 22 Oct Southwell (AW) Flat 6f Standard 5/8 fig 45; 20 Nov Wolverhampton (AW) Flat 5f Standard 4/5 fig 41
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Quipster (hrs_17395635558) | 3yo G | 130lb | OR - | draw 3 | jockey Kieran O'Neill | trainer Lemos De Souza (14d 1/5) | headgear - | last run 9 days | form 9 | MARKET 1.1% | 09:00 median 67.00 | Matchbook 160.00
    DATA: model 9.1% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 19 Nov Lingfield (AW) Flat 8f Standard 9/9
    DATA for: Trainer 20% wins (1/5), last 14 days
    DATA against: Last-run finishing speed -10.7% vs that field (faded); Lightly raced: 1 run in our data, so the model has little to go on

## 5:00 Southwell (AW) | race_id rac_32305891709 | All-Weather Championship Is Back Nursery Handicap Stakes
Flat | Class 5 | 7f14y | going Standard | AW | 13 runners | rating band 0-75 | age 2yo
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Arthur Carrot (hrs_17390697996) | 2yo C | 141lb | OR 81 | draw 7 | jockey Jack Callan | trainer George Boughey (14d 7/26) | headgear - | last run 9 days | form 263241 | MARKET 22.1% | 09:00 median 3.50 | Matchbook 4.10 | CHECK (skip line 3.32)
    comment: Arthur Carrot arrives in winning form, having scored last time out just nine days ago, and he has been in the first four in five of his last six, with a yard in form and experience of today's trip and going. The one concern is 141 lb off an official mark of 81 after that latest success.
    DATA: model 19.3% | style Prominent (led 3% of runs) | runs in data 6 | last 3: 21 Oct Kempton (AW) Flat 7f Standard / Slow 2/14 fig 75; 28 Oct Kempton (AW) Flat 6f Standard / Slow 4/7 fig 68; 19 Nov Lingfield (AW) Flat 7f Standard 1/8 fig 77
    DATA for: Best recent form figure 77, 12 lb above field average; Official rating 81, 10 lb above field average; Trainer 27% wins (7/26), last 14 days; Has won at this trip or further; Good recent finishing positions
    DATA against: Carries 10 lb more than average
- Marsala (hrs_66130638) | 2yo F | 132lb | OR 72 | draw 3 | jockey Hector Crouch | trainer Ralph Beckett (14d 4/16) | headgear - | last run 63 days | form 4733 | MARKET 17.5% | 09:00 median 4.50 | Matchbook 5.10
    comment: She has run over today's trip, but 63 days off and 132 lb are the main concerns.
    DATA: model 8.3% | style Held up (led 3% of runs) | runs in data 4 | last 3: 12 Aug Kempton Flat 7f Standard To Slow 7/12; 4 Sep Haydock Flat 6f Heavy 3/4; 26 Sep Newmarket Flat 7f Good To Firm 3/10
    DATA for: Trainer 25% wins (4/16), last 14 days; Good recent finishing positions
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Bacha (hrs_65974594) | 2yo C | 132lb | OR 72 | draw 9 | jockey Freya Frain(7) | trainer George Boughey (14d 7/26) | headgear - | last run 9 days | form 5332 | MARKET 15.2% | 09:00 median 5.00 | Matchbook 6.00
    comment: Bacha arrives in solid nick, second last time out and third in the two runs before that, with just nine days since that effort and experience of today's trip and going.
    DATA: model 12.8% | style Held up (led 3% of runs) | runs in data 4 | last 3: 1 Aug Thirsk Flat 5f Good 3/8; 2 Sep Hamilton Flat 5f Soft 3/7; 19 Nov Lingfield (AW) Flat 7f Standard 2/8 fig 68
    DATA for: Trainer 27% wins (7/26), last 14 days; Last-run finishing speed +3.4% vs that field (finished strongly); Good recent finishing positions
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Thai Baht (hrs_17391344656) | 2yo F | 127lb | OR 67 | draw 6 | jockey Callum Rodriguez | trainer Owen Burrows (14d 2/7) | headgear - | last run 23 days | form 2851 | MARKET 11.0% | 09:00 median 7.00 | Matchbook 8.40
    comment: Fresh from a last-time-out win after 23 days off, Thai Baht has run over today's trip and going, though a fifth and an eighth in the two runs before that show her consistency is a question.
    DATA: model 5.7% | style Midfield (led 4% of runs) | runs in data 4 | last 3: 7 Sep Windsor Flat 6.1f Good 8/14; 5 Oct Wolverhampton Flat 6.1f Standard 5/8; 5 Nov Southwell (AW) Flat 6f Standard 1/13 fig 73
    DATA for: Best recent form figure 73, 8 lb above field average; Recent figures 6 lb above its current mark (looks well handicapped); Trainer 29% wins (2/7), last 14 days
- Odegaard (hrs_65380567) | 2yo G | 129lb | OR 69 | draw 1 | jockey Aiden Brookes | trainer Micky Hammond & Becky Smith (14d 1/18) | headgear - | last run 22 days | form 54552 | MARKET 8.5% | 09:00 median 8.50 | Matchbook 12.00
    DATA: model 7.6% | style Held up (led 4% of runs) | runs in data 5 | last 3: 25 Jul Newcastle Flat 6f Standard To Slow 5/14; 19 Oct Wolverhampton (AW) Flat 7f Standard 5/12 fig 66; 6 Nov Newcastle (AW) Flat 7f Standard 2/11 fig 70
    DATA for: Best recent form figure 70, 5 lb above field average; Last-run finishing speed +2.6% vs that field (finished strongly)
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Knightbolt (hrs_17390700082) | 2yo C | 133lb | OR 73 | draw 12 | jockey Kevin Stott | trainer Kevin Ryan (14d 0/4) | headgear - | last run 23 days | form 483 | MARKET 6.1% | 09:00 median 12.00 | Matchbook 16.00
    comment: Knightbolt was third last time out, but he is winless in his last three starts, with an eighth two starts back and a fourth three starts back.
    DATA: model 5.1% | style Prominent (led 4% of runs) | runs in data 3 | last 3: 14 Aug Thirsk Flat 6f Good 4/11; 2 Oct Newcastle Flat 6f Standard 8/12; 5 Nov Southwell (AW) Flat 7f Standard 3/9 fig 54
    DATA against: Best recent form figure 54, 11 lb below field average; Recent figures 19 lb below its current mark (looks high in the weights)
- Lion's Den (hrs_64555421) | 2yo G | 128lb | OR 68 | draw 10 | jockey Mark Winn | trainer Michael Dods (14d 2/12) | headgear - | last run 42 days | form 61 | MARKET 4.2% | 09:00 median 15.00 | Matchbook 28.00
    DATA: model 9.2% | style Held up (led 8% of runs) | runs in data 2 | last 3: 25 Sep Newcastle Flat 7.1f Standard 6/13; 17 Oct Catterick Flat 7f Good 1/7 fig 62
    DATA for: Has won at this trip or further
    DATA against: Recent figures 6 lb below its current mark (looks high in the weights); Lightly raced: 2 runs in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Mojito Madness (hrs_60819486) | 2yo C | 135lb | OR 75 | draw 11 | jockey Rhys Clutterbuck | trainer Gihan Arnolda (14d 0/6) | headgear - | last run 71 days | form 53199 | MARKET 3.4% | 09:00 median 23.00 | Matchbook 27.00
    comment: Mojito Madness has gone ninth in his last two starts after a win three starts back, and he returns after 71 days off, though he has run over today's trip.
    DATA: model 5.6% | style Midfield (led 8% of runs) | runs in data 5 | last 3: 19 Jul Redcar Flat 7f Good To Firm 1/13; 22 Aug Newmarket Flat 6f Good 9/18; 18 Sep Newbury Flat 7f Good 9/11
    DATA for: Has won at this trip or further
- From Me To You (hrs_60820403) | 2yo G | 128lb | OR 68 | draw 2 | jockey Joe Leavy | trainer Richard Hannon (14d 2/17) | headgear - | last run 30 days | form 063619 | MARKET 3.2% | 09:00 median 23.00 | Matchbook 38.00
    comment: From Me To You was beaten into ninth last time out and has only one win in his last six starts, a first two starts back, so he is hard to fancy. In his favour, he has run over today's trip and going, and a 30-day break is no concern.
    DATA: model 7.2% | style Midfield (led 4% of runs) | runs in data 11 | last 3: 24 Sep Southwell Flat 7.1f Standard 6/12; 23 Oct Wolverhampton (AW) Flat 6f Standard 1/13 fig 70; 29 Oct Southwell (AW) Flat 7f Standard 9/13 fig 57
    DATA for: Best recent form figure 70, 5 lb above field average
- Koodini (hrs_64360849) | 2yo C | 128lb | OR 68 | draw 5 | jockey Clifford Lee | trainer Hugo Palmer (14d 0/4) | headgear p | last run 43 days | form 310494 | MARKET 2.6% | 09:00 median 29.00 | Matchbook 46.00
    comment: Koodini was a fourth last time out, though a ninth two starts back and a win five starts back show how patchy his recent form has been.
    DATA: model 4.4% | style Midfield (led 4% of runs) | runs in data 10 | last 3: 3 Sep Haydock Flat 7f Soft 4/10; 19 Sep Chester Flat 7f Heavy 9/11; 16 Oct Haydock Flat 7f Heavy 4/9 fig 63
    DATA for: Has won at this trip or further
- Bullrider (hrs_66198867) | 2yo G | 130lb | OR 70 | draw 13 | jockey Paul Mulrennan | trainer Phillip Makin (14d 0/7) | headgear - | last run 59 days | form 23566 | MARKET 2.6% | 09:00 median 31.50 | Matchbook 40.00
    comment: The risk is a 59-day break after a pair of sixth-place finishes, and he's yet to win in that spell.
    DATA: model 9.9% | style Prominent (led 38% of runs) | runs in data 5 | last 3: 6 Aug Southwell Flat 8.1f Standard 5/8; 17 Sep Southwell Flat 7.1f Standard 6/11; 30 Sep Kempton Flat 7f Standard To Slow 6/13
- Frumoasa (hrs_62170129) | 2yo F | 127lb | OR 67 | draw 8 | jockey Paddy Bradley | trainer Charlie Fellowes (14d 3/13) | headgear p | last run 26 days | form 13006 | MARKET 2.0% | 09:00 median 36.00 | Matchbook 65.00
    comment: Frumoasa has run over today's trip and going, scored five starts back and was third four starts back, and returns fresh after 26 days.
    DATA: model 1.9% | style Prominent (led 5% of runs) | runs in data 5 | last 3: 22 Aug Newmarket Flat 6f Good 18/18; 10 Sep Lingfield Flat 6f Standard 10/12; 2 Nov Chelmsford (AW) Flat 6f Standard 6/9 fig 64
    DATA for: Trainer 23% wins (3/13), last 14 days
    DATA against: Poor recent finishing positions
- Jeepers Fortune (hrs_17391656513) | 2yo G | 129lb | OR 69 | draw 4 | jockey Tom Eaves | trainer David Evans (14d 0/10) | headgear - | last run 35 days | form 676 | MARKET 1.6% | 09:00 median 41.00 | Matchbook 80.00
    DATA: model 3.1% | style Midfield (led 5% of runs) | runs in data 3 | last 3: 2 Sep Kempton Flat 7f Standard To Slow 6/10; 25 Sep Newmarket Flat 7f Good 7/14; 24 Oct Southwell (AW) Flat 8f Standard 6/10 fig 53
    DATA against: Best recent form figure 53, 12 lb below field average; Recent figures 16 lb below its current mark (looks high in the weights); Trainer 0 wins from 10 runs, last 14 days; Poor recent finishing positions

## 5:30 Southwell (AW) | race_id rac_32306184196 | Midnite A Next Generation Betting App Handicap Stakes (Div I)
Flat | Class 5 | 7f14y | going Standard | AW | 12 runners | rating band 0-75 | age 3yo+
DATA pace: Lone leader - Jellystone Park is the only habitual front-runner and may be allowed an easy lead.
- Goldwork (hrs_50433481) | 3yo G | 143lb | OR 81 | draw 5 | jockey Oliver Carmichael(5) | trainer Eve Johnson Houghton (14d 1/4) | headgear - | last run 11 days | form 364431 | MARKET 18.2% | 09:00 median 4.00 | Matchbook 5.40 | CHECK (skip line 3.80)
    comment: Last-time winner Goldwork is fresh from that success just 11 days ago and has run over today's trip and on the going, while a third two starts back keeps his form tidy.
    DATA: model 21.4% | style Held up (led 5% of runs) | runs in data 11 | last 3: 5 Oct Kempton Flat 6f Standard To Slow 4/10; 7 Oct Kempton Flat 6f Standard To Slow 3/11; 17 Nov Southwell (AW) Flat 6f Standard 1/13 fig 87
    DATA for: Best recent form figure 87, 17 lb above field average; Recent figures 6 lb above its current mark (looks well handicapped); Official rating 81, 10 lb above field average; Last-run finishing speed +4.8% vs that field (finished strongly); Good recent finishing positions
    DATA against: Carries 9 lb more than average
- Lady Mariko (hrs_47098863) | 4yo F | 138lb | OR 75 | draw 12 | jockey Marco Ghiani | trainer Dylan Cunha (14d 2/16) | headgear - | last run 6 days | form 004613 | MARKET 17.5% | 09:00 median 4.50 | Matchbook 5.20
    comment: Third last time out and a winner two starts back, Lady Mariko is in good heart, back quickly after six days and with experience of both today's trip and the going.
    DATA: model 19.0% | style Midfield (led 3% of runs) | runs in data 12 | last 3: 21 Oct Kempton (AW) Flat 6f Standard / Slow 6/11 fig 66; 5 Nov Southwell (AW) Flat 7f Standard 1/10 fig 80; 22 Nov Lingfield (AW) Flat 7f Standard 3/11 fig 71
    DATA for: Best recent form figure 80, 10 lb above field average; Recent figures 5 lb above its current mark (looks well handicapped); Has won at this trip or further; Good recent finishing positions
- Red Hat Eagle (hrs_32613483) | 6yo G | 132lb | OR 69 | draw 4 | jockey Kevin Stott | trainer Michael Appleby (14d 2/24) | headgear tp | last run 11 days | form 523523 | MARKET 15.7% | 09:00 median 5.00 | Matchbook 5.90
    comment: The risk is simple: he is yet to win in his last six starts, and 132 lb is a big burden.
    DATA: model 10.5% | style Prominent (led 8% of runs) | runs in data 12 | last 3: 9 Oct Kempton Flat 7f Standard To Slow 5/11; 24 Oct Southwell (AW) Flat 7f Standard 2/14 fig 80; 17 Nov Southwell (AW) Flat 7f Standard 3/11 fig 66
    DATA for: Best recent form figure 80, 10 lb above field average; Recent figures 11 lb above its current mark (looks well handicapped); Good recent finishing positions
- King of Ithaca (hrs_30123457) | 6yo G | 132lb | OR 69 | draw 9 | jockey Hector Crouch | trainer James Tate (14d 0/7) | headgear - | last run 24 days | form 584260 | MARKET 9.9% | 09:00 median 7.00 | Matchbook 10.00
    comment: King of Ithaca is winless in his last six, unplaced last time and a sixth two starts back, so he is hard to fancy, though a second three starts back shows he can sometimes get involved.
    DATA: model 6.2% | style Held up (led 5% of runs) | runs in data 8 | last 3: 18 Sep Wolverhampton Flat 7.2f Standard 2/12; 8 Oct Southwell Flat 7.1f Standard 6/12; 4 Nov Kempton (AW) Flat 7f Standard / Slow 10/11 fig 49
    DATA against: Best recent form figure 49, 21 lb below field average; Recent figures 20 lb below its current mark (looks high in the weights)
- Tasdeed (hrs_45193442) | 5yo G | 136lb | OR 73 | draw 10 | jockey Kieren Fox | trainer Charlie Pike (14d 0/6) | headgear tb | last run 65 days | form 0-7841 | MARKET 9.7% | 09:00 median 8.00 | Matchbook 9.80
    comment: Tasdeed won last time out after a fourth two starts back, and he has run over today's trip and going before, but a 65-day break raises fitness questions and 136 lb is a stiff burden off an official 73.
    DATA: model 8.6% | style Midfield (led 4% of runs) | runs in data 4 | last 3: 6 Apr Kempton Flat 8f Standard To Slow 8/9; 9 Sep Kempton Flat 7f Standard To Slow 4/14; 24 Sep Southwell Flat 7.1f Standard 1/9
    DATA for: Has won at this trip or further
- Jellystone Park (hrs_52054415) | 3yo G | 135lb | OR 73 | draw 7 | jockey George Bass | trainer Jack Channon (14d 0/10) | headgear ht | last run 23 days | form 421003 | MARKET 8.3% | 09:00 median 10.00 | Matchbook 11.00
    comment: Third last time out and fresh enough after 23 days, Jellystone Park has run over today's trip and going, but he has failed to place in the two runs before that.
    DATA: model 4.8% | style Prominent (led 54% of runs) | runs in data 6 | last 3: 1 Oct Salisbury Flat 6f Soft 14/14; 23 Oct Doncaster Flat 6f Heavy 10/11 fig 28; 5 Nov Southwell (AW) Flat 6f Standard 3/9 fig 71
    DATA against: Trainer 0 wins from 10 runs, last 14 days
- Lunario (hrs_33081713) | 6yo G | 134lb | OR 71 | draw 6 | jockey Jack Dace(5) | trainer Luke Dace (14d 0/8) | headgear tv | last run 33 days | form 016463 | MARKET 6.8% | 09:00 median 12.00 | Matchbook 13.50
    DATA: model 5.3% | style Midfield (led 29% of runs) | runs in data 9 | last 3: 19 Sep Newmarket Flat 7f Good 4/14; 9 Oct Newmarket Flat 7f Good To Soft 6/11; 26 Oct Kempton (AW) Flat 7f Standard / Slow 3/12 fig 75
    DATA for: Best recent form figure 75, 5 lb above field average; Recent figures 4 lb above its current mark (looks well handicapped); Has won at this trip or further
    DATA against: Trainer 0 wins from 8 runs, last 14 days
- Yaajooz (hrs_34472004) | 5yo G | 131lb | OR 68 | draw 8 | jockey Clifford Lee | trainer Michael & David Easterby (14d 1/12) | headgear - | last run 29 days | form 036816 | MARKET 6.0% | 09:00 median 13.00 | Matchbook 15.50
    comment: Yaajooz was sixth last time out and has finished eighth and sixth in two of his other recent runs, which makes him hard to fancy, though he did win two starts back and has run over today's trip and going.
    DATA: model 7.9% | style Held up (led 4% of runs) | runs in data 8 | last 3: 30 Sep Catterick Flat 7f Good 8/9; 20 Oct Newcastle (AW) Flat 7f Standard 1/14 fig 71; 30 Oct Newcastle (AW) Flat 7f Standard 6/11 fig 63
    DATA for: Has won at this trip or further
- Abduction (hrs_21743631) | 8yo G | 134lb | OR 71 | draw 1 | jockey Rob Hornby | trainer Charlie Wallis (14d 0/3) | headgear - | last run 24 days | form 243632 | MARKET 3.6% | 09:00 median 21.00 | Matchbook 28.00
    DATA: model 9.8% | style Held up (led 3% of runs) | runs in data 17 | last 3: 29 Sep Ayr Flat 7.2f Heavy 6/10; 12 Oct Newcastle Flat 7.1f Standard 3/13; 4 Nov Musselburgh Flat 7f Soft 2/12 fig 73
    DATA for: Last-run finishing speed +4.3% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Aged 8, older than most of this field
- Electric Avenue (hrs_35796656) | 6yo M | 126lb | OR 63 | draw 2 | jockey Joanna Mason | trainer Ruth Carr (14d 3/14) | headgear - | last run 213 days | form 468906 | MARKET 2.0% | 09:00 median 41.00 | Matchbook 55.00
    comment: Electric Avenue is winless in her last six, finishing sixth last time out and no better than a fourth six starts back, and she returns after 213 days off.
    DATA: model 1.6% | style Held up (led 3% of runs) | runs in data 6 | last 3: 14 Mar Southwell Flat 7.1f Standard 9/11; 28 Mar Doncaster Flat 10.2f Good To Soft 15/15; 29 Apr Southwell Flat 8.1f Standard 6/9
    DATA for: Trainer 21% wins (3/14), last 14 days; Carries 8 lb less than average
    DATA against: Official rating 63, 8 lb below field average; Poor recent finishing positions; Returns from a 213-day break
- Patricia R (hrs_53476101) | 4yo F | 135lb | OR 72 | draw 11 | jockey Ryan Sexton | trainer Julie Camacho (14d 1/14) | headgear h | last run 42 days | form 210-78 | MARKET 1.4% | 09:00 median 51.00 | Matchbook 110.00
    comment: Patricia R has slipped to an eighth last time out and a seventh two starts back, though she won four starts back and has run over today's trip and going before.
    DATA: model 3.0% | style Held up (led 8% of runs) | runs in data 2 | last 3: 22 Sep Southwell Flat 7.1f Standard 7/12; 17 Oct Southwell (AW) Flat 8f Standard 8/8 fig 59
    DATA against: Best recent form figure 59, 11 lb below field average; Recent figures 13 lb below its current mark (looks high in the weights); Lightly raced: 2 runs in our data, so the model has little to go on
- Spy Kingdom (hrs_50965026) | 4yo G | 136lb | OR 73 | draw 3 | jockey Paddy Bradley | trainer Adam Kirby (14d 1/11) | headgear - | last run 35 days | form -50P00 | MARKET 1.0% | 09:00 median 81.00 | Matchbook 130.00
    comment: Winless in his last five, Spy Kingdom has been unplaced in his last two and pulled up three starts back, though a fifth five starts back is his best recent effort and he has run over today's trip. Carrying 136 lb from stall three after 35 days off, he rates 75 against an official 73.
    DATA: model 2.0% | style Held up (led 5% of runs) | runs in data 3 | last 3: 21 Sep Leicester Flat 8.2f Good PU/13; 14 Oct Kempton (AW) Flat 7f Standard / Slow 11/12 fig 57; 24 Oct Doncaster Flat 7f Heavy 13/13
    DATA against: Best recent form figure 57, 13 lb below field average; Recent figures 16 lb below its current mark (looks high in the weights); Poor recent finishing positions

## 6:00 Southwell (AW) | race_id rac_32305893646 | Midnite A Next Generation Betting App Handicap Stakes (Div II)
Flat | Class 5 | 7f14y | going Standard | AW | 11 runners | rating band 0-75 | age 3yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Venetian Sky (hrs_57590561) | 3yo F | 135lb | OR 73 | draw 6 | jockey Cieren Fallon | trainer William Haggas (14d 4/29) | headgear - | last run 29 days | form 452843 | MARKET 14.5% | 09:00 median 5.50 | Matchbook 6.60 | CHECK (skip line 5.22)
    DATA: model 13.0% | style Held up (led 3% of runs) | runs in data 8 | last 3: 9 Sep Kempton Flat 8f Standard To Slow 8/11; 5 Oct Yarmouth Flat 8f Good To Firm 4/11; 30 Oct Newcastle (AW) Flat 7f Standard 3/9 fig 63
    DATA against: Recent figures 10 lb below its current mark (looks high in the weights); Pace: steady gallop likely, hard to come from off the pace
- Native Honey (hrs_412694709) | 4yo G | 134lb | OR 71 | draw 10 | jockey Paul Mulrennan | trainer Jim Goldie (14d 1/18) | headgear - | last run 42 days | form 155681 | MARKET 14.1% | 09:00 median 5.50 | Matchbook 7.00
    DATA: model 7.6% | style Prominent (led 5% of runs) | runs in data 11 | last 3: 5 Sep Thirsk Flat 7f Good To Soft 6/9; 21 Sep Hamilton Flat 6f Soft 8/8; 17 Oct Southwell (AW) Flat 7f Standard 1/9 fig 68
    DATA for: Has won at this trip or further
- Decem Starr (hrs_50433467) | 3yo G | 131lb | OR 69 | draw 7 | jockey Dylan Hogan | trainer Julie Camacho (14d 1/14) | headgear - | last run 21 days | form 408207 | MARKET 13.1% | 09:00 median 6.50 | Matchbook 7.00
    comment: Decem Starr is yet to win in his last six, with a seventh last time out following a second three starts back, though he has run over today's trip and going and returns after 21 days.
    DATA: model 9.4% | style Midfield (led 4% of runs) | runs in data 7 | last 3: 26 Sep Southwell Flat 7.1f Standard 2/12; 27 Oct Catterick Flat 7f Soft 10/15 fig 59; 7 Nov Doncaster Flat 7f Good To Soft 7/12 fig 59
    DATA against: Best recent form figure 59, 6 lb below field average; Recent figures 10 lb below its current mark (looks high in the weights)
- Stenmark (hrs_41939156) | 4yo G | 138lb | OR 75 | draw 3 | jockey Rhys Clutterbuck | trainer Gihan Arnolda (14d 0/6) | headgear - | last run 6 days | form 382608 | MARKET 12.3% | 09:00 median 7.00 | Matchbook 7.40
    comment: The risk is a poor recent return, with an eighth last time out and only six days since that run.
    DATA: model 8.4% | style Midfield (led 4% of runs) | runs in data 8 | last 3: 16 Jul Chepstow Flat 8.1f Good To Firm 6/6; 31 Oct Newmarket Flat 7f Good To Soft 12/16 fig 62; 22 Nov Lingfield (AW) Flat 7f Standard 8/11 fig 68
    DATA against: Recent figures 7 lb below its current mark (looks high in the weights); Poor recent finishing positions
- Seoul Force (hrs_52862537) | 3yo G | 136lb | OR 74 | draw 8 | jockey Rowan Scott | trainer Phillip Makin (14d 0/7) | headgear - | last run 189 days | form 3541-6 | MARKET 11.0% | 09:00 median 8.00 | Matchbook 8.20
    comment: Seoul Force has a win two starts back, and a third five starts back, in his last five outings, and he has run over today's trip and on the going before.
    DATA: model 13.7% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 23 May Curragh Flat 7f Good 6/13
    DATA against: Returns from a 189-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Mo Anam Chara (hrs_56843850) | 3yo F | 134lb | OR 72 | draw 2 | jockey Andrew Mullen | trainer Geoffrey Harker (14d 0/0) | headgear - | last run 33 days | form 012153 | MARKET 9.6% | 09:00 median 9.00 | Matchbook 9.40
    comment: Mo Anam Chara arrives in solid form, third last time out and a winner three starts back, with two wins in her last six, and she has run over today's trip and going before.
    DATA: model 13.6% | style Midfield (led 3% of runs) | runs in data 6 | last 3: 14 Sep Thirsk Flat 7f Good 1/10; 30 Sep Catterick Flat 7f Good 5/9; 26 Oct Southwell (AW) Flat 8f Standard 3/9 fig 73
    DATA for: Best recent form figure 73, 8 lb above field average; Has won at this trip or further; Good recent finishing positions
- Glamorous Angela (hrs_40919256) | 4yo F | 135lb | OR 72 | draw 9 | jockey P. J. McDonald | trainer Geoff Oldroyd (14d 1/3) | headgear - | last run 347 days | form 323- | MARKET 8.1% | 09:00 median 9.00 | Matchbook 13.00
    comment: Placed in all three recent starts, with a third last time out, a second two starts back and a third three starts back, but yet to win in that spell, and a 347-day absence raises fitness doubts.
    DATA: model 9.3% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 347-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Stanley Spencer (hrs_33875625) | 5yo G | 137lb | OR 74 | draw 4 | jockey Oisin Orr | trainer Fionn McSharry (14d 0/1) | headgear p | last run 23 days | form 080006 | MARKET 7.6% | 09:00 median 9.50 | Matchbook 14.00
    comment: The main risk is a string of unplaced runs, leaving him winless in his last six.
    DATA: model 6.4% | style Midfield (led 4% of runs) | runs in data 12 | last 3: 9 Oct York Flat 7f Good To Soft 18/20; 22 Oct Southwell (AW) Flat 6f Standard 10/10 fig 59; 5 Nov Southwell (AW) Flat 6f Standard 6/9 fig 75
    DATA for: Best recent form figure 75, 10 lb above field average
    DATA against: Poor recent finishing positions
- Beauty Choice (hrs_19208154) | 9yo G | 129lb | OR 66 | draw 1 | jockey Joanna Mason | trainer Michael & David Easterby (14d 1/12) | headgear - | last run 21 days | form 400918 | MARKET 7.1% | 09:00 median 12.00 | Matchbook 13.50
    comment: Beauty Choice won two starts back but was beaten into eighth last time and has been inconsistent around that success, though he has run over today's trip and going and returns after 21 days.
    DATA: model 6.7% | style Prominent (led 3% of runs) | runs in data 7 | last 3: 17 Sep Pontefract Flat 6f Good 9/12; 26 Oct Redcar Flat 6f Heavy 1/14 fig 77; 7 Nov Doncaster Flat 7f Good To Soft 8/12 fig 63
    DATA for: Best recent form figure 77, 12 lb above field average; Recent figures 11 lb above its current mark (looks well handicapped); Carries 5 lb less than average
    DATA against: Official rating 66, 6 lb below field average; Aged 9, older than most of this field
- Regal Desire (hrs_64388723) | 3yo F | 132lb | OR 70 | draw 11 | jockey Tom Eaves | trainer Brian Ellison (14d 1/9) | headgear p (1st time) | last run 29 days | form 22989 | MARKET 1.9% | 09:00 median 41.00 | Matchbook 65.00
    comment: Regal Desire has run poorly lately, with a ninth last time out, an eighth two starts back and another ninth before that, though she did finish second four and five starts back.
    DATA: model 5.4% | style Held up (led 5% of runs) | runs in data 5 | last 3: 5 Sep Newcastle Flat 7.1f Standard 9/9; 5 Oct Pontefract Flat 8f Good 8/13; 30 Oct Newcastle (AW) Flat 8f Standard 9/10 fig 62
    DATA for: First-time headgear
    DATA against: Recent figures 8 lb below its current mark (looks high in the weights); Poor recent finishing positions; Pace: steady gallop likely, hard to come from off the pace
- Dark Angel Light (hrs_64877302) | 3yo F | 133lb | OR 71 | draw 5 | jockey Ryan Sexton | trainer Julie Camacho (14d 1/14) | headgear - | last run 33 days | form 7176 | MARKET 0.9% | 09:00 median 101.00 | Matchbook 140.00
    comment: Dark Angel Light is hard to fancy after a sixth last time out and a seventh two starts back, though she did win three starts back and has run over today's trip and going.
    DATA: model 6.6% | style Held up (led 5% of runs) | runs in data 4 | last 3: 26 Jun Doncaster Flat 6f Good To Firm 1/8; 5 Sep Newcastle Flat 6f Standard 7/7; 26 Oct Southwell (AW) Flat 6f Standard 6/8 fig 39
    DATA against: Best recent form figure 39, 26 lb below field average; Recent figures 32 lb below its current mark (looks high in the weights); Pace: steady gallop likely, hard to come from off the pace

## 6:30 Southwell (AW) | race_id rac_32305895583 | AWC Season 14 Has Begun EBF Fillies' Novice Stakes (GBB Race)
Flat | Class 3 | 7f14y | going Standard | AW | 8 runners | rating band - | age 2yo
DATA pace: Unclear - Running styles known for only 3 of 8 runners.
- Unfurled (hrs_17394083574) | 2yo F | 130lb | OR - | draw 7 | jockey Harry Davies | trainer Simon Crisford (14d 5/13) | headgear - | last run 32 days | form 2 | MARKET 34.4% | 09:00 median 2.50 | Matchbook 2.58
    DATA: model 25.4% | style Held up (led 8% of runs) | runs in data 1 | last 3: 27 Oct Wolverhampton (AW) Flat 7f Standard 2/6 fig 70
    DATA for: Best recent form figure 70, 9 lb above field average; Trainer 38% wins (5/13), last 14 days
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Secha (hrs_17396118467) | 2yo F | 130lb | OR - | draw 1 | jockey Robert Havlin | trainer John & Thady Gosden (14d 4/28) | headgear - | last run - days | form - | MARKET 20.8% | 09:00 median 3.62 | Matchbook 4.90
    DATA: model 11.2% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Mantuba (hrs_17395882749) | 2yo F | 130lb | OR - | draw 3 | jockey Cieren Fallon | trainer William Haggas (14d 4/29) | headgear - | last run - days | form - | MARKET 18.7% | 09:00 median 5.00 | Matchbook 5.00
    DATA: model 11.2% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Late Night Show (hrs_17391111024) | 2yo F | 130lb | OR - | draw 8 | jockey Clifford Lee | trainer K. R. Burke (14d 1/12) | headgear - | last run 43 days | form 65 | MARKET 7.0% | 09:00 median 11.25 | Matchbook 14.50
    DATA: model 11.8% | style Held up (led 8% of runs) | runs in data 2 | last 3: 21 Aug Newmarket Flat 7f Good To Firm 6/7; 16 Oct Redcar Flat 7f Good 5/7 fig 56
    DATA against: Best recent form figure 56, 5 lb below field average; Lightly raced: 2 runs in our data, so the model has little to go on
- Al Basos (hrs_17395879620) | 2yo F | 130lb | OR - | draw 2 | jockey Oisin Orr | trainer Edward Bethell (14d 0/14) | headgear - | last run - days | form - | MARKET 6.7% | 09:00 median 13.00 | Matchbook 15.00
    DATA: model 11.2% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Trainer 0 wins from 14 runs, last 14 days; Lightly raced: 0 runs in our data, so the model has little to go on
- Shakiara (hrs_17396181047) | 2yo F | 130lb | OR - | draw 5 | jockey Kieran Shoemark | trainer Ed Walker (14d 2/28) | headgear - | last run - days | form - | MARKET 5.4% | 09:00 median 15.00 | Matchbook 19.00
    DATA: model 11.2% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Hootie Frutti (hrs_17395809739) | 2yo F | 130lb | OR - | draw 6 | jockey Sean Levey | trainer Richard Hannon (14d 2/17) | headgear - | last run - days | form - | MARKET 5.0% | 09:00 median 17.00 | Matchbook 20.00
    DATA: model 11.2% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- State of America (hrs_17389805188) | 2yo F | 130lb | OR - | draw 4 | jockey Hector Crouch | trainer Ollie Sangster (14d 1/15) | headgear - | last run 32 days | form 86 | MARKET 2.0% | 09:00 median 53.00 | Matchbook 55.00
    DATA: model 6.8% | style Held up (led 8% of runs) | runs in data 2 | last 3: 26 Aug Newbury Flat 6f Good To Firm 8/10; 27 Oct Wolverhampton (AW) Flat 7f Standard 6/6 fig 56
    DATA against: Best recent form figure 56, 5 lb below field average; Lightly raced: 2 runs in our data, so the model has little to go on

## 7:00 Southwell (AW) | race_id rac_32305897520 | AWC Finals Day At Newcastle 26th March Nursery Handicap Stakes
Flat | Class 4 | 6f16y | going Standard | AW | 9 runners | rating band 0-85 | age 2yo
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Henley On Thames (hrs_65287250) | 2yo C | 137lb | OR 87 | draw 1 | jockey Rowan Scott | trainer Kevin Philippart de Foy (14d 3/12) | headgear - | last run 31 days | form 221142 | MARKET 27.7% | 09:00 median 3.25 | Matchbook 3.25 | CHECK (skip line 3.09)
    comment: Henley On Thames arrives in cracking nick, finishing second last time out and a winner three and four starts back, so he has hit the frame in five of his last six.
    DATA: model 18.8% | style Prominent (led 23% of runs) | runs in data 7 | last 3: 19 Aug York Flat 6f Good 1/18; 11 Sep Doncaster Flat 6f Good 4/15; 28 Oct Kempton (AW) Flat 6f Standard / Slow 2/7 fig 84
    DATA for: Best recent form figure 84, 14 lb above field average; Official rating 87, 9 lb above field average; Trainer 25% wins (3/12), last 14 days; Has won at this trip or further; Good recent finishing positions
    DATA against: Carries 9 lb more than average
- Palms Oasis (hrs_17392761050) | 2yo C | 124lb | OR 74 | draw 6 | jockey Ross Coakley | trainer Roger Varian (14d 6/10) | headgear - | last run 21 days | form 421 | MARKET 19.9% | 09:00 median 3.75 | Matchbook 5.30
    comment: Palms Oasis arrives in good heart, a winner last time out after a second two starts back and a fourth three starts back, and he has run over today's trip and going.
    DATA: model 13.4% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 24 Sep Southwell Flat 6.1f Standard 4/11; 17 Oct Southwell (AW) Flat 6f Standard 2/11 fig 70; 7 Nov Southwell (AW) Flat 6f Standard 1/13 fig 69
    DATA for: Trainer 60% wins (6/10), last 14 days; Has won at this trip or further; Good recent finishing positions
- Blue Pete (hrs_65036027) | 2yo C | 131lb | OR 81 | draw 3 | jockey Daniel Muscutt | trainer Michael Appleby (14d 2/24) | headgear - | last run 26 days | form 73221 | MARKET 15.6% | 09:00 median 5.50 | Matchbook 5.90
    comment: Blue Pete won last time out and was second, then another second, in the starts before that, so he arrives in rude form after 26 days off, with experience of today's trip and going.
    DATA: model 14.4% | style Prominent (led 5% of runs) | runs in data 5 | last 3: 9 Sep Redcar Flat 6f Good 2/7; 12 Oct Musselburgh Flat 7.1f Good To Soft 2/4; 2 Nov Chelmsford (AW) Flat 6f Standard 1/9 fig 81
    DATA for: Best recent form figure 81, 11 lb above field average; Has won at this trip or further; Good recent finishing positions
- Angel Sense (hrs_64168034) | 2yo F | 129lb | OR 79 | draw 4 | jockey Marco Ghiani | trainer Marco Botti (14d 1/15) | headgear p (1st time) | last run 79 days | form 233618 | MARKET 12.9% | 09:00 median 6.90 | Matchbook 7.20
    comment: Angel Sense won two starts back and has been placed in three of her other recent runs, but she was eighth last time out and returns after 79 days off.
    DATA: model 7.5% | style Prominent (led 3% of runs) | runs in data 6 | last 3: 9 Jul Newbury Flat 6f Good To Firm 6/11; 30 Jul Wolverhampton Flat 6.1f Standard 1/10; 10 Sep Doncaster Flat 6.5f Good To Soft 8/11
    DATA for: Has won at this trip or further; First-time headgear
- Fully Stocked (hrs_65916823) | 2yo G | 126lb | OR 76 | draw 2 | jockey Sean Dylan Bowen | trainer Jennie Candlish (14d 3/23) | headgear - | last run 42 days | form 24321 | MARKET 8.4% | 09:00 median 10.00 | Matchbook 11.50
    comment: Fully Stocked arrives a last-time-out winner, with a second, third, fourth and second before that, and he has run over today's trip and going before.
    DATA: model 18.0% | style Unknown | runs in data 5 | last 3: 10 Sep Lingfield Flat 6f Standard 3/10; 3 Oct Southwell Flat 7.1f Standard 2/10; 17 Oct Southwell (AW) Flat 6f Standard 1/11 fig 73
    DATA for: Has won at this trip or further; Good recent finishing positions
- Longshanks Luke (hrs_7000000392) | 2yo G | 127lb | OR 77 | draw 7 | jockey Oisin Orr | trainer Patrick Neville (14d 0/1) | headgear - | last run 40 days | form 8441 | MARKET 5.7% | 09:00 median 15.00 | Matchbook 17.00
    comment: He has run over today's trip and is drawn seven, carrying 127 lb.
    DATA: model 6.6% | style Held up (led 4% of runs) | runs in data 4 | last 3: 5 Aug Pontefract Flat 6f Good To Firm 4/8; 11 Aug Hamilton Flat 6f Good 4/6; 19 Oct Pontefract Flat 6f Soft 1/6 fig 74
    DATA for: Last-run finishing speed +2.8% vs that field (finished strongly); Has won at this trip or further
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Cloud Summit (hrs_65322432) | 2yo G | 123lb | OR 73 | draw 5 | jockey Jack Callan | trainer George Boughey (14d 7/26) | headgear - | last run 9 days | form 4666 | MARKET 3.9% | 09:00 median 21.00 | Matchbook 26.00
    comment: Cloud Summit has finished sixth in each of his last three outings, with a fourth four starts back, yet he's winless in recent starts, though back quickly after nine days and with experience of today's trip and going.
    DATA: model 3.2% | style Midfield (led 4% of runs) | runs in data 4 | last 3: 6 Jul Lingfield Flat 7f Standard 6/9; 31 Jul Newmarket Flat 6f Good To Firm 6/7; 19 Nov Lingfield (AW) Flat 7f Standard 6/8 fig 68
    DATA for: Trainer 27% wins (7/26), last 14 days; Carries 5 lb less than average
    DATA against: Official rating 73, 5 lb below field average; Poor recent finishing positions
- Lady Blanche (hrs_63650314) | 2yo F | 128lb | OR 78 | draw 9 | jockey Clifford Lee | trainer K. R. Burke (14d 1/12) | headgear - | last run 10 days | form 3183 | MARKET 3.5% | 09:00 median 23.00 | Matchbook 32.00
    comment: The risk is an eighth two starts back, which shows she can be inconsistent.
    DATA: model 8.9% | style Prominent (led 29% of runs) | runs in data 4 | last 3: 29 Apr Bath Flat 5.7f Firm 1/10; 15 May York Flat 5f Good 8/10; 18 Nov Kempton (AW) Flat 6f Standard / Slow 3/5 fig 72
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Recent figures 6 lb below its current mark (looks high in the weights)
- Green Star (hrs_17390484181) | 2yo G | 129lb | OR 79 | draw 8 | jockey Tom Eaves | trainer David Evans (14d 0/10) | headgear - | last run 40 days | form 246 | MARKET 2.4% | 09:00 median 29.00 | Matchbook 50.00
    comment: He has run over today's trip and gets a 40-day break, but 129 lb from stall eight is a big ask.
    DATA: model 9.3% | style Midfield (led 5% of runs) | runs in data 3 | last 3: 12 Sep Chester Flat 7f Soft 2/8; 3 Oct Redcar Flat 7f Good 4/7; 19 Oct Pontefract Flat 6f Soft 6/6 fig 41
    DATA against: Best recent form figure 41, 29 lb below field average; Recent figures 38 lb below its current mark (looks high in the weights); Trainer 0 wins from 10 runs, last 14 days; Last-run finishing speed -4.4% vs that field (faded)

## 7:30 Southwell (AW) | race_id rac_32305899457 | Midnite Built Different Handicap Stakes
Flat | Class 2 | 4f214y | going Standard | AW | 6 runners | rating band 0-105 | age 3yo+
DATA pace: Even - Two likely leaders (Dazzling Haze, Ancient State). A fair, even gallop is most likely.
- Elyam (hrs_43062929) | 4yo G | 135lb | OR 93 | draw 5 | jockey Jason Hart | trainer Michael Herrington (14d 1/5) | headgear - | last run 29 days | form 53/111 | MARKET 43.7% | 09:00 median 2.00 | Matchbook 2.22
    comment: Elyam arrives in cracking form, a winner last time out, and a winner two starts back, and a winner three starts back, with a third four starts back before that.
    DATA: model 45.7% | style Unknown | runs in data 3 | last 3: 3 Sep Southwell Flat 5f Standard 1/6; 26 Sep Southwell Flat 5f Standard 1/10; 30 Oct Newcastle (AW) Flat 5f Standard 1/12 fig 99
    DATA for: Best recent form figure 99, 8 lb above field average; Recent figures 6 lb above its current mark (looks well handicapped); Official rating 93, 6 lb above field average; Trainer 20% wins (1/5), last 14 days; Has won at this trip or further; Good recent finishing positions
    DATA against: Carries 6 lb more than average
- Ancient State (hrs_48414100) | 4yo G | 129lb | OR 87 | draw 1 | jockey Shay Farmer(5) | trainer Adam Kirby (14d 1/11) | headgear t/ce | last run 21 days | form 214526 | MARKET 19.4% | 09:00 median 4.50 | Matchbook 5.00
    comment: Beaten into sixth last time out and without a win since a success five starts back, Ancient State is hard to fancy, though a second two starts back and 21 days since his last run are mild positives.
    DATA: model 12.8% | style Leader (led 38% of runs) | runs in data 14 | last 3: 3 Oct Ascot Flat 5f Good To Firm 5/12; 24 Oct Doncaster Flat 5f Heavy 2/10 fig 87; 7 Nov Doncaster Flat 6f Good To Soft 6/22 fig 91
    DATA for: Recent figures 4 lb above its current mark (looks well handicapped); Has won at this trip or further; Course: front-runners have won 1.3× their fair share at 5f here
- Rhythm N Hooves (hrs_29918651) | 6yo G | 131lb | OR 89 | draw 2 | jockey Barry McHugh | trainer Robert Cowell (14d 1/10) | headgear v | last run 12 days | form 818214 | MARKET 15.1% | 09:00 median 6.00 | Matchbook 6.40
    comment: Rhythm N Hooves arrives fresh from a fourth last time out, 12 days ago, and has a winner two starts back and another five starts back, with a second three starts back, plus he has run over today's trip and going before. The main risk is a patchy record, with an eighth four starts back showing he can underperform.
    DATA: model 17.0% | style Prominent (led 8% of runs) | runs in data 14 | last 3: 3 Oct Ascot Flat 5f Good To Firm 2/12; 24 Oct Southwell (AW) Flat 5f Standard 1/12 fig 93; 16 Nov Wolverhampton (AW) Flat 5f Standard 4/11 fig 85
    DATA for: Recent figures 4 lb above its current mark (looks well handicapped); Has won at this trip or further; Good recent finishing positions
- Baldomero (hrs_22897546) | 8yo G | 122lb | OR 80 | draw 4 | jockey Joanna Mason | trainer Michael Appleby (14d 2/24) | headgear v | last run 7 days | form 944256 | MARKET 14.4% | 09:00 median 6.50 | Matchbook 6.60
    comment: The risk is that he's yet to win in his last six starts.
    DATA: model 12.5% | style Prominent (led 4% of runs) | runs in data 14 | last 3: 9 Oct York Flat 5f Good To Soft 2/14; 17 Oct Catterick Flat 6f Good 5/10 fig 83; 21 Nov Lingfield (AW) Flat 6f Standard 6/11 fig 75
    DATA for: Carries 7 lb less than average
    DATA against: Best recent form figure 83, 8 lb below field average; Official rating 80, 7 lb below field average; Aged 8, older than most of this field
- Dazzling Haze (hrs_52862705) | 3yo F | 131lb | OR 89 | draw 3 | jockey Marco Ghiani | trainer Robert Cowell (14d 1/10) | headgear - | last run 121 days | form 5-5100 | MARKET 5.3% | 09:00 median 15.00 | Matchbook 19.50
    comment: The main risk is a 121-day absence after two unplaced runs, with 131 lb to carry from stall three.
    DATA: model 6.0% | style Leader (led 57% of runs) | runs in data 4 | last 3: 31 May Thirsk Flat 5f Good 1/12; 19 Jun Ascot Flat 5f Good To Firm 10/27; 30 Jul Goodwood Flat 5f Good To Firm 12/18
    DATA for: Has won at this trip or further; Course: front-runners have won 1.3× their fair share at 5f here
    DATA against: Returns from a 121-day break
- Jack The Bachelor (hrs_52897194) | 3yo G | 126lb | OR 84 | draw 6 | jockey Cam Hardie | trainer Antony Brittain (14d 2/17) | headgear h | last run 309 days | form 1603-4 | MARKET 2.0% | 09:00 median 34.00 | Matchbook 75.00
    comment: Returning after 309 days off, Jack The Bachelor is hard to fancy: his only win in his last five came five starts back, though a fourth last time out and a third two starts back show he was running respectably before the break.
    DATA: model 6.0% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 23 Jan Southwell Flat 5f Standard 4/7
    DATA against: Returns from a 309-day break; Lightly raced: 1 run in our data, so the model has little to go on

## 8:00 Southwell (AW) | race_id rac_32305901394 | Midnite: Built For 2027 Not 2007 Handicap Stakes
Flat | Class 4 | 4f214y | going Standard | AW | 8 runners | rating band 0-85 | age 3yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Leading Times (hrs_57041586) | 4yo G | 134lb | OR 81 | draw 7 | jockey Kaiya Fraser | trainer Rebecca Menzies (14d 0/17) | headgear - | last run 21 days | form 12-161 | MARKET 26.2% | 09:00 median 3.25 | Matchbook 3.75 | CHECK (skip line 3.09)
    comment: Leading Times has won three of his last five, including last time out 21 days ago, and has run over today's trip and going before.
    DATA: model 23.6% | style Held up (led 5% of runs) | runs in data 3 | last 3: 24 Sep Southwell Flat 5f Standard 1/5; 16 Oct Newcastle (AW) Flat 5f Standard 6/11 fig 77; 7 Nov Southwell (AW) Flat 5f Standard 1/14 fig 83
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Trainer 0 wins from 17 runs, last 14 days; Pace: steady gallop likely, hard to come from off the pace; Course: hold-up horses have won 0.6× their fair share at 5f here
- Atticum (hrs_56525413) | 3yo C | 135lb | OR 82 | draw 4 | jockey Marco Ghiani | trainer Robert Cowell (14d 1/10) | headgear - | last run 56 days | form -55334 | MARKET 20.1% | 09:00 median 4.50 | Matchbook 4.70
    comment: The risk is a 56-day break, and he is yet to win in his last five starts.
    DATA: model 19.5% | style Prominent (led 5% of runs) | runs in data 5 | last 3: 20 Jun Redcar Flat 5f Good 3/6; 29 Jul Sandown Flat 5f Good To Firm 3/6; 3 Oct Ascot Flat 5f Good To Firm 4/12
    DATA for: Good recent finishing positions
- Sir Yoshi (hrs_40745957) | 4yo G | 135lb | OR 82 | draw 8 | jockey David Nolan | trainer Geoffrey Harker (14d 0/0) | headgear b | last run 29 days | form 948354 | MARKET 16.6% | 09:00 median 5.50 | Matchbook 5.70
    comment: Sir Yoshi is yet to win in his last six, but he arrives fresh after 29 days, having been fourth last time out, and has run over today's trip and going before.
    DATA: model 13.2% | style Midfield (led 3% of runs) | runs in data 10 | last 3: 21 Sep Hamilton Flat 5f Soft 3/6; 17 Oct Catterick Flat 5f Good 5/12 fig 87; 30 Oct Newcastle (AW) Flat 5f Standard 4/12 fig 88
    DATA for: Best recent form figure 88, 9 lb above field average; Recent figures 6 lb above its current mark (looks well handicapped)
- Call Margot (hrs_52496213) | 3yo F | 129lb | OR 76 | draw 3 | jockey Rowan Scott | trainer Gemma Tutty (14d 1/9) | headgear - | last run 21 days | form 039016 | MARKET 11.2% | 09:00 median 7.50 | Matchbook 8.80
    comment: Call Margot was sixth last time out, having won two starts back, and she's fit enough after 21 days, with experience of today's trip and going. Carrying 129 lb from stall three, she looks held by an inconsistent record, with only one win in her last six starts.
    DATA: model 9.2% | style Held up (led 4% of runs) | runs in data 13 | last 3: 30 Sep Musselburgh Flat 5f Good To Soft 12/12; 19 Oct Wolverhampton (AW) Flat 5f Standard 1/6 fig 71; 7 Nov Southwell (AW) Flat 5f Standard 6/14 fig 76
    DATA for: Has won at this trip or further
    DATA against: Pace: steady gallop likely, hard to come from off the pace; Course: hold-up horses have won 0.6× their fair share at 5f here
- Toolatetonegotiate (hrs_41189442) | 4yo F | 132lb | OR 79 | draw 6 | jockey Millie Wonnacott(5) | trainer Daisy Hitchins (14d 0/5) | headgear p | last run 21 days | form 108232 | MARKET 10.5% | 09:00 median 8.50 | Matchbook 9.20
    comment: Toolatetonegotiate arrives in decent shape, runner-up last time out and a third two starts back, with 21 days since her last run and experience of today's trip and going.
    DATA: model 16.9% | style Held up (led 3% of runs) | runs in data 13 | last 3: 3 Sep Lingfield Flat 5f Standard 2/5; 29 Sep Bath Flat 5f Good To Firm 3/12; 7 Nov Southwell (AW) Flat 5f Standard 2/14 fig 82
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Pace: steady gallop likely, hard to come from off the pace; Course: hold-up horses have won 0.6× their fair share at 5f here
- Alligator Alley (hrs_17762514) | 9yo G | 135lb | OR 82 | draw 5 | jockey Joanna Mason | trainer Ruth Carr (14d 3/14) | headgear - | last run 12 days | form -69800 | MARKET 6.4% | 09:00 median 12.00 | Matchbook 17.00
    DATA: model 4.0% | style Held up (led 5% of runs) | runs in data 5 | last 3: 5 Jul Southwell Flat 5f Standard 8/9; 30 Oct Newcastle (AW) Flat 5f Standard 10/12 fig 73; 16 Nov Wolverhampton (AW) Flat 5f Standard 10/11 fig 74
    DATA for: Trainer 21% wins (3/14), last 14 days
    DATA against: Best recent form figure 74, 5 lb below field average; Recent figures 8 lb below its current mark (looks high in the weights); Poor recent finishing positions; Aged 9, older than most of this field; Pace: steady gallop likely, hard to come from off the pace; Course: hold-up horses have won 0.6× their fair share at 5f here
- Anaisa (hrs_51866311) | 3yo F | 125lb | OR 72 | draw 1 | jockey Sean Kirrane | trainer Tim Easterby (14d 2/14) | headgear t | last run 11 days | form 734083 | MARKET 6.3% | 09:00 median 14.25 | Matchbook 15.50
    comment: Anaisa is fresh from a third last time out, 11 days ago, and has run over today's trip and going, but she is winless in her last six and was only eighth two starts back.
    DATA: model 4.0% | style Held up (led 4% of runs) | runs in data 11 | last 3: 30 Sep Musselburgh Flat 5f Good To Soft 11/12; 26 Oct Southwell (AW) Flat 6f Standard 8/10 fig 60; 17 Nov Southwell (AW) Flat 5f Standard 3/13 fig 74
    DATA for: Carries 7 lb less than average
    DATA against: Best recent form figure 74, 5 lb below field average; Official rating 72, 7 lb below field average; Pace: steady gallop likely, hard to come from off the pace; Course: hold-up horses have won 0.6× their fair share at 5f here
- Fenlander (hrs_36235073) | 5yo G | 133lb | OR 80 | draw 2 | jockey Warren Fentiman(3) | trainer Olly Williams (14d 0/1) | headgear - | last run 21 days | form 331109 | MARKET 2.6% | 09:00 median 34.00 | Matchbook 44.00
    comment: Fenlander has slipped to a ninth last time out and unplaced the run before, a long way from the pair of wins three and four starts back, and he is hard to fancy off 133 lb.
    DATA: model 9.6% | style Midfield (led 3% of runs) | runs in data 16 | last 3: 26 Oct Leicester Flat 5f Soft 1/7 fig 78; 30 Oct Newmarket Flat 5f Good To Soft 13/13 fig 51; 7 Nov Southwell (AW) Flat 5f Standard 9/14 fig 73
    DATA for: Has won at this trip or further

## 8:30 Southwell (AW) | race_id rac_32305903331 | Make The Move To Midnite Handicap Stakes (GBBPlus Race)
Flat | Class 2 | 1m4f14y | going Standard | AW | 8 runners | rating band 0-105 | age 3yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Lord d'Or (hrs_55545749) | 3yo C | 124lb | OR 86 | draw 7 | jockey P. J. McDonald | trainer Andrew Balding (14d 4/41) | headgear p | last run 50 days | form 222242 | MARKET 33.4% | 09:00 median 2.63 | Matchbook 2.86
    comment: Winless in his last six, Lord d'Or has been runner-up in five of them, including last time out, but that habit of going close is the best he offers.
    DATA: model 8.5% | style Prominent (led 29% of runs) | runs in data 6 | last 3: 21 Aug Hamilton Flat 11.1f Good To Soft 2/3; 5 Sep Ascot Flat 12f Good To Firm 4/9; 9 Oct Newmarket Flat 12f Good 2/10
    DATA for: Good recent finishing positions; Carries 10 lb less than average
    DATA against: Official rating 86, 5 lb below field average
- Castle Cove (hrs_41596772) | 5yo G | 142lb | OR 99 | draw 8 | jockey Cieren Fallon | trainer William Haggas (14d 4/29) | headgear h | last run 21 days | form 6441-0 | MARKET 22.7% | 09:00 median 3.50 | Matchbook 4.40
    comment: The main risk is an unplaced effort last time out, which he needs to bounce back from.
    DATA: model 29.2% | style Held up (led 8% of runs) | runs in data 1 | last 3: 7 Nov Doncaster Flat 12f Good To Soft 13/23 fig 95
    DATA for: Official rating 99, 8 lb above field average
    DATA against: Carries 8 lb more than average; Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Tawajjah (hrs_38018379) | 5yo G | 131lb | OR 88 | draw 1 | jockey Jonny Peate | trainer Oli Rix (14d 0/0) | headgear - | last run 77 days | form 21/213 | MARKET 17.3% | 09:00 median 5.00 | Matchbook 5.60
    comment: Tawajjah's recent form reads well, with a third last time out, a winner two starts back and another win four starts back, and he has run on today's going.
    DATA: model 25.1% | style Held up (led 8% of runs) | runs in data 3 | last 3: 9 Jul Newmarket Flat 8f Good To Firm 2/13; 23 Jul Sandown Flat 9.9f Good To Firm 1/6; 12 Sep Doncaster Flat 10.2f Good 3/12
    DATA for: Last-run finishing speed +2.5% vs that field (finished strongly); Good recent finishing positions
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Master Builder (hrs_40918794) | 5yo G | 132lb | OR 89 | draw 2 | jockey Sean Levey | trainer David Menuisier (14d 0/5) | headgear - | last run 21 days | form 0-1040 | MARKET 8.8% | 09:00 median 10.75 | Matchbook 10.50
    comment: Master Builder won four starts back and has run over today's trip, and a fourth two starts back shows he can still pick up some of the pieces, while 21 days since his last run suggests freshness.
    DATA: model 9.2% | style Held up (led 3% of runs) | runs in data 4 | last 3: 21 Aug York Flat 11.9f Good To Soft 12/16; 10 Oct York Flat 13.9f Good To Soft 4/12; 7 Nov Doncaster Flat 12f Good To Soft 12/23 fig 86
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 86, 6 lb below field average; Pace: steady gallop likely, hard to come from off the pace
- Ghaiyya (hrs_43730568) | 4yo F | 131lb | OR 88 | draw 4 | jockey Hector Crouch | trainer Charlie Johnston (14d 0/15) | headgear - | last run 21 days | form 248620 | MARKET 6.1% | 09:00 median 15.00 | Matchbook 15.50
    comment: Ghaiyya was second two starts back but unplaced last time out, and she's yet to win in her last six; she's back after 21 days with experience of today's trip and going.
    DATA: model 5.8% | style Midfield (led 23% of runs) | runs in data 7 | last 3: 11 Jul Ascot Flat 12f Good To Firm 6/8; 24 Jul Ascot Flat 15.9f Good To Firm 2/4; 7 Nov Doncaster Flat 12f Good To Soft 21/23
    DATA for: Has won at this trip or further
    DATA against: Trainer 0 wins from 15 runs, last 14 days
- Orchard Keeper (hrs_39109819) | 5yo M | 134lb | OR 91 | draw 5 | jockey Sean Dylan Bowen | trainer Roger Varian (14d 6/10) | headgear - | last run 51 days | form 4-5549 | MARKET 5.2% | 09:00 median 17.00 | Matchbook 18.50
    comment: The risk is a ninth last time out and a 51-day break, while 134 lb is a notable burden.
    DATA: model 7.5% | style Midfield (led 4% of runs) | runs in data 4 | last 3: 22 Aug Chester Flat 14.4f Good To Soft 5/8; 24 Sep Newmarket Flat 16f Good 4/10; 8 Oct Bath Flat 14f Good 9/12
    DATA for: Trainer 60% wins (6/10), last 14 days
- Deira Mile (hrs_36515178) | 5yo G | 142lb | OR 99 | draw 6 | jockey Darragh O'Sullivan(7) | trainer Jessica Bedi (14d 0/8) | headgear v (1st time) | last run 9 days | form 8-6785 | MARKET 3.3% | 09:00 median 23.00 | Matchbook 36.00
    DATA: model 8.5% | style Held up (led 4% of runs) | runs in data 4 | last 3: 15 May York Flat 13.9f Good 7/7; 7 Nov Doncaster Flat 12f Good To Soft 8/23 fig 104; 19 Nov Newcastle (AW) Flat 10f Standard 5/8 fig 94
    DATA for: Best recent form figure 104, 12 lb above field average; Recent figures 5 lb above its current mark (looks well handicapped); Official rating 99, 8 lb above field average; First-time headgear
    DATA against: Trainer 0 wins from 8 runs, last 14 days; Carries 8 lb more than average; Pace: steady gallop likely, hard to come from off the pace
- Brasil Power (hrs_25795280) | 7yo G | 133lb | OR 90 | draw 3 | jockey Jack Callan | trainer George Boughey (14d 7/26) | headgear t | last run 10 days | form 090980 | MARKET 3.2% | 09:00 median 26.00 | Matchbook 34.00
    comment: Brasil Power is winless in his last six, finishing eighth and ninth in two of his last three after an unplaced latest effort, though he has run over today's trip and going and is back quickly after 10 days.
    DATA: model 6.3% | style Unknown | runs in data 11 | last 3: 4 Jul Sandown Flat 9.9f Good To Firm 9/9; 21 Oct Kempton (AW) Flat 16f Standard / Slow 8/14 fig 85; 18 Nov Kempton (AW) Flat 8f Standard / Slow 12/14 fig 75
    DATA for: Trainer 27% wins (7/26), last 14 days; Has won at this trip or further
    DATA against: Best recent form figure 85, 8 lb below field average; Poor recent finishing positions
