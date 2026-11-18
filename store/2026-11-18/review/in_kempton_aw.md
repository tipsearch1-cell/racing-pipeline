# Card review packet: Kempton (AW), 2026-11-18

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
   treat it as one opinion, not the answer); "fig" is a performance figure (higher = better) for that past run;
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


## 4:25 Kempton (AW) | race_id rac_32305043303 | Unibet/British Stallion Studs EBF Restricted Novice Stakes (For Horses In Bands B, C And D) (Rider Restricted Race) (Div I) (GBB Race)
Flat | Class 5 | 6f | going Standard / Slow | AW | 11 runners | rating band - | age 2yo
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Brave Country (hrs_17392826759) | 2yo C | 132lb | OR 75 | draw 4 | jockey George Downing | trainer Ed Walker (14d 1/9) | headgear - | last run 28 days | form 23 | MARKET 34.0% | 09:00 median 2.38 | Matchbook 2.78
    DATA: model 18.0% | style Held up (led 5% of runs) | runs in data 2 | last 3: 25 Sep Haydock 7f Soft 2/8; 21 Oct Newmarket 7f Soft 3/5 fig 62
    DATA for: Best recent form figure 62, 10 lb above field average; Good recent finishing positions
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Tredegar Square (hrs_17390467493) | 2yo G | 133lb | OR 77 | draw 6 | jockey Jonny Peate | trainer James Fanshawe (14d 0/1) | headgear - | last run 37 days | form 15 | MARKET 26.5% | 09:00 median 3.25 | Matchbook 3.40
    DATA: model 34.5% | style Prominent (led 8% of runs) | runs in data 2 | last 3: 10 Aug Kempton 7f Standard To Slow 1/12; 12 Oct Kempton 7f Standard To Slow 5/11
    DATA for: Has won at this trip or further
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Gliding Martha (hrs_65190573) | 2yo F | 127lb | OR - | draw 2 | jockey M. P. Sheehy | trainer Denis Coakley (14d 0/1) | headgear - | last run 151 days | form 25 | MARKET 15.4% | 09:00 median 5.50 | Matchbook 6.00
    DATA: model 9.8% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 30 May Lingfield 7f Good To Firm 2/8; 20 Jun Doncaster 7f Good To Firm 5/13
    DATA against: Returns from a 151-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- From The Stars (hrs_17394158670) | 2yo C | 129lb | OR - | draw 7 | jockey Donagh Murphy(5) | trainer Richard Hughes (14d 0/9) | headgear - | last run - days | form - | MARKET 6.1% | 09:00 median 13.00 | Matchbook 17.50
    DATA: model 5.7% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Trainer 0 wins from 9 runs, last 14 days; Lightly raced: 0 runs in our data, so the model has little to go on
- Livorno (hrs_17394163885) | 2yo C | 132lb | OR - | draw 8 | jockey Dougie Costello | trainer Charles Hills (14d 0/1) | headgear - | last run 19 days | form 5 | MARKET 4.9% | 09:00 median 17.00 | Matchbook 20.00
    DATA: model 5.4% | style Held up (led 8% of runs) | runs in data 1 | last 3: 30 Oct Newmarket 6f Good To Soft 5/7 fig 66
    DATA for: Best recent form figure 66, 14 lb above field average
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Manssoor (hrs_17395543774) | 2yo C | 132lb | OR - | draw 12 | jockey Kieren Fox | trainer John Butler (14d 2/6) | headgear - | last run - days | form - | MARKET 4.8% | 09:00 median 19.00 | Matchbook 20.00
    DATA: model 5.8% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 33% wins (2/6), last 14 days
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Miss Roxie Hart (hrs_17395545860) | 2yo F | 124lb | OR - | draw 3 | jockey Megan Smith(7) | trainer George Boughey (14d 1/5) | headgear - | last run - days | form - | MARKET 2.9% | 09:00 median 23.00 | Matchbook 50.00
    DATA: model 5.7% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 20% wins (1/5), last 14 days
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Saxon Crest (hrs_17393975102) | 2yo G | 132lb | OR - | draw 1 | jockey George Bass | trainer Jack Channon (14d 1/6) | headgear - | last run 19 days | form 0 | MARKET 2.2% | 09:00 median 34.00 | Matchbook 60.00
    DATA: model 3.1% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 30 Oct Newmarket 7f Good To Soft 10/10 fig 22
    DATA against: Best recent form figure 22, 30 lb below field average; Last-run finishing speed -4.1% vs that field (faded); Lightly raced: 1 run in our data, so the model has little to go on
- Bad Baker (hrs_60820893) | 2yo C | 129lb | OR - | draw 5 | jockey Tom Eaves | trainer James Horton (14d 0/6) | headgear - | last run 32 days | form 06 | MARKET 1.7% | 09:00 median 41.00 | Matchbook 120.00
    DATA: model 4.5% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 11 May Wolverhampton 6.1f Standard 11/11; 17 Oct Southwell (AW) 6f Standard 6/11 fig 56
    DATA for: Best recent form figure 56, 4 lb above field average
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Heavenly (hrs_17395450947) | 2yo F | 124lb | OR - | draw 9 | jockey William Cox | trainer J. S. Moore (14d 0/4) | headgear - | last run - days | form - | MARKET 1.0% | 09:00 median 67.00 | Matchbook 200.00
    DATA: model 5.7% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Harriet Vane (hrs_64967994) | 2yo F | 121lb | OR - | draw 11 | jockey Nicola Currie | trainer Michael Attwater (14d 0/1) | headgear - | last run 179 days | form 0 | MARKET 0.5% | 09:00 median 151.00 | Matchbook 380.00
    DATA: model 1.7% | style Unknown | runs in data 1 | last 3: 23 May Windsor 6.1f Good To Firm 12/12
    DATA against: Last-run finishing speed -3.3% vs that field (faded); Returns from a 179-day break; Lightly raced: 1 run in our data, so the model has little to go on

## 5:00 Kempton (AW) | race_id rac_32304712076 | Unibet/British Stallion Studs EBF Restricted Novice Stakes (For Horses In Bands B, C And D) (Rider Restricted Race) (Div II) (GBB Race)
Flat | Class 5 | 6f | going Standard / Slow | AW | 12 runners | rating band - | age 2yo
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Angel Footsteps (hrs_63810187) | 2yo F | 122lb | OR - | draw 6 | jockey Connor Planas | trainer Marco Botti (14d 0/6) | headgear - | last run 212 days | form 2 | MARKET 45.9% | 09:00 median 1.80 | Matchbook 1.96
    DATA: model 20.8% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 20 Apr Redcar 5f Good To Firm 2/9
    DATA against: Returns from a 212-day break; Lightly raced: 1 run in our data, so the model has little to go on
- King's Flight (hrs_17395542731) | 2yo G | 133lb | OR - | draw 7 | jockey Donagh Murphy(5) | trainer Richard Hughes (14d 0/9) | headgear - | last run - days | form - | MARKET 12.6% | 09:00 median 6.90 | Matchbook 7.40
    DATA: model 6.9% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Trainer 0 wins from 9 runs, last 14 days; Lightly raced: 0 runs in our data, so the model has little to go on
- Amandari (hrs_17393632998) | 2yo C | 133lb | OR - | draw 11 | jockey Tyler Heard | trainer John & Thady Gosden (14d 4/10) | headgear h | last run 15 days | form 57 | MARKET 11.1% | 09:00 median 7.00 | Matchbook 8.60
    DATA: model 17.7% | style Held up (led 8% of runs) | runs in data 2 | last 3: 12 Oct Yarmouth 7f Good To Soft 5/7; 3 Nov Wolverhampton (AW) 7f Standard 7/11 fig 35
    DATA for: Trainer 40% wins (4/10), last 14 days; Last-run finishing speed +2.3% vs that field (finished strongly)
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Tuxedo Black (hrs_17393755029) | 2yo G | 133lb | OR - | draw 9 | jockey Dougie Costello | trainer Charles Hills (14d 0/1) | headgear - | last run - days | form - | MARKET 9.7% | 09:00 median 8.50 | Matchbook 9.00
    DATA: model 6.9% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Platinum Force (hrs_65710841) | 2yo G | 130lb | OR - | draw 10 | jockey Ross Coakley | trainer Michael Bell (14d 1/3) | headgear - | last run 147 days | form 8 | MARKET 8.5% | 09:00 median 9.25 | Matchbook 11.50
    DATA: model 9.1% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 24 Jun Carlisle 6.9f Good To Firm 8/11
    DATA against: Returns from a 147-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Pull And Prey (hrs_17395454076) | 2yo F | 125lb | OR - | draw 3 | jockey Nicola Currie | trainer Lemos De Souza (14d 0/3) | headgear - | last run - days | form - | MARKET 3.1% | 09:00 median 21.00 | Matchbook 55.00
    DATA: model 6.7% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Thriving Miss Lacy (hrs_17394439237) | 2yo F | 128lb | OR - | draw 2 | jockey M. P. Sheehy | trainer Denis Coakley (14d 0/1) | headgear - | last run 13 days | form 8 | MARKET 2.6% | 09:00 median 26.00 | Matchbook 46.00
    DATA: model 7.9% | style Held up (led 8% of runs) | runs in data 1 | last 3: 5 Nov Southwell (AW) 6f Standard 8/11 fig 44
    DATA for: Best recent form figure 44, 10 lb above field average
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Go For It (hrs_17393788405) | 2yo G | 127lb | OR - | draw 8 | jockey Rhys Clutterbuck | trainer J. S. Moore (14d 0/4) | headgear - | last run - days | form - | MARKET 1.7% | 09:00 median 41.00 | Matchbook 120.00
    DATA: model 6.8% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- At My Expense (hrs_17393585020) | 2yo G | 127lb | OR - | draw 12 | jockey William Cox | trainer Roger Teal (14d 0/4) | headgear - | last run 38 days | form 8 | MARKET 1.4% | 09:00 median 51.00 | Matchbook 150.00
    DATA: model 4.7% | style Held up (led 8% of runs) | runs in data 1 | last 3: 11 Oct Goodwood 6f Good To Soft 8/8
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Don't Tempt Harry (hrs_17394626977) | 2yo G | 130lb | OR - | draw 4 | jockey Laura Coughlan(3) | trainer Adrian Wintle (14d 1/1) | headgear - | last run 20 days | form 0 | MARKET 1.1% | 09:00 median 67.00 | Matchbook 150.00
    DATA: model 4.4% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 29 Oct Bath 8f Soft 11/12 fig 18
    DATA against: Best recent form figure 18, 16 lb below field average; Last-run finishing speed -6.4% vs that field (faded); Lightly raced: 1 run in our data, so the model has little to go on
- Brigand (hrs_17394667654) | 2yo C | 127lb | OR - | draw 1 | jockey Jack Dace(5) | trainer Jim Boyle (14d 0/1) | headgear - | last run 19 days | form 7 | MARKET 1.1% | 09:00 median 67.00 | Matchbook 170.00
    DATA: model 3.1% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 30 Oct Newmarket 6f Good To Soft 7/7 fig 40
    DATA for: Best recent form figure 40, 6 lb above field average
    DATA against: Last-run finishing speed -3.2% vs that field (faded); Lightly raced: 1 run in our data, so the model has little to go on
- Enalia (hrs_17393699750) | 2yo F | 125lb | OR - | draw 5 | jockey Joey Haynes | trainer Adam Kirby (14d 0/7) | headgear - | last run 36 days | form 8 | MARKET 1.1% | 09:00 median 81.00 | Matchbook 110.00
    DATA: model 5.0% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 13 Oct Leicester 6f Good To Soft 8/11
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on

## 5:30 Kempton (AW) | race_id rac_32304714013 | Unibet 40,000+ Live Streamed Events Nursery Handicap Stakes (Rider Restricted Race)
Flat | Class 4 | 6f | going Standard / Slow | AW | 5 runners | rating band 0-85 | age 2yo
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Divine Whisper (hrs_64847062) | 2yo F | 136lb | OR 86 | draw 5 | jockey Toby Moore(7) | trainer George Boughey (14d 1/5) | headgear - | last run 39 days | form 2139 | MARKET 28.8% | 09:00 median 3.00 | Matchbook 3.35 | CHECK (skip line 2.85)
    comment: Divine Whisper has been in the frame regularly, a second four starts back, a winner three starts back and a third two starts back, and she has run over today's trip.
    DATA: model 34.5% | style Midfield (led 4% of runs) | runs in data 4 | last 3: 27 Jun Windsor 5.1f Good To Firm 1/8; 29 Jul Goodwood 5f Good To Firm 3/9; 10 Oct York 6f Soft 9/10
    DATA for: Official rating 86, 7 lb above field average; Trainer 20% wins (1/5), last 14 days; Good recent finishing positions
    DATA against: Carries 7 lb more than average
- Nightbloom (hrs_63811181) | 2yo F | 126lb | OR 76 | draw 4 | jockey Laura Pearson | trainer Kevin Philippart de Foy (14d 0/3) | headgear t | wind surgery | last run 50 days | form 661 | MARKET 21.3% | 09:00 median 4.33 | Matchbook 4.30
    comment: Nightbloom won last time out, but that came after a pair of sixths, and she returns after 50 days off.
    DATA: model 16.6% | style Prominent (led 8% of runs) | runs in data 3 | last 3: 3 Jul Beverley 5f Good To Firm 6/7; 24 Jul Sandown 5f Good To Firm 6/8; 29 Sep Wolverhampton 6.1f Standard 1/7
    DATA for: Has won at this trip or further
- Conciliate (hrs_64812902) | 2yo C | 128lb | OR 78 | draw 1 | jockey M. P. Sheehy | trainer John Butler (14d 2/6) | headgear - | last run 21 days | form 731027 | MARKET 21.1% | 09:00 median 4.00 | Matchbook 4.80
    comment: Conciliate bounced back to form with a second two starts back and has won within his last four runs, while he has run over today's trip and returns after 21 days. The main risk is a seventh last time out, so he needs to show that was a blip from stall one.
    DATA: model 9.9% | style Prominent (led 29% of runs) | runs in data 6 | last 3: 22 Aug Newmarket 6f Good 15/18; 17 Sep Yarmouth 6f Good 2/8; 28 Oct Kempton (AW) 6f Standard / Slow 7/7 fig 67
    DATA for: Trainer 33% wins (2/6), last 14 days; Has won at this trip or further
    DATA against: Recent figures 11 lb below its current mark (looks high in the weights)
- Lady Blanche (hrs_63650314) | 2yo F | 130lb | OR 80 | draw 3 | jockey William Cox | trainer K. R. Burke (14d 0/9) | headgear - | last run 187 days | form 318 | MARKET 18.5% | 09:00 median 4.50 | Matchbook 5.30
    comment: Lady Blanche won two starts back and was third three starts back, so the profile is solid, and she has run over today's trip from stall three.
    DATA: model 27.4% | style Prominent (led 29% of runs) | runs in data 3 | last 3: 15 Apr Beverley 5f Good To Soft 3/11; 29 Apr Bath 5.7f Firm 1/10; 15 May York 5f Good 8/10
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Trainer 0 wins from 9 runs, last 14 days; Returns from a 187-day break
- Paper View (hrs_62169485) | 2yo G | 126lb | OR 76 | draw 2 | jockey Dougie Costello | trainer Richard Hannon (14d 0/5) | headgear - | last run 41 days | form 119366 | MARKET 10.3% | 09:00 median 9.00 | Matchbook 9.20
    comment: Paper View won twice in his last six starts, five and six starts back, and has a third three starts back, while he has run over today's trip before.
    DATA: model 11.5% | style Held up (led 4% of runs) | runs in data 9 | last 3: 17 Aug Windsor 5.1f Good To Firm 3/5; 12 Sep Chester 5.1f Soft 6/9; 8 Oct Southwell 5f Standard 6/7
    DATA for: Has won at this trip or further
    DATA against: Pace: steady gallop likely, hard to come from off the pace

## 6:00 Kempton (AW) | race_id rac_32304715950 | Unibet's New VAR Goal Guarantee Nursery Handicap Stakes (Rider Restricted Race)
Flat | Class 5 | 1m | going Standard / Slow | AW | 11 runners | rating band 0-75 | age 2yo
DATA pace: Strong pace - 3 habitual front-runners (You're Sensational, Q T Boy, Bearly Blue). A contested lead should set things up for horses coming from behind.
- Divine Rhythm (hrs_17392144637) | 2yo C | 135lb | OR 73 | draw 6 | jockey Ross Coakley | trainer William Haggas (14d 2/7) | headgear - | last run 20 days | form 34 | MARKET 31.2% | 09:00 median 2.75 | Matchbook 2.92
    comment: Winless in his last two, Divine Rhythm was fourth last time out, and a third two starts back, so he has been in the frame without quite getting there.
    DATA: model 23.2% | style Held up (led 5% of runs) | runs in data 2 | last 3: 16 Sep Yarmouth 7f Good To Soft 3/7; 29 Oct Bath 8f Soft 4/10 fig 55
    DATA for: Trainer 29% wins (2/7), last 14 days; Pace: a contested lead should suit its hold-up style
    DATA against: Recent figures 18 lb below its current mark (looks high in the weights); Lightly raced: 2 runs in our data, so the model has little to go on
- Somers Isles (hrs_7000002254) | 2yo F | 135lb | OR 73 | draw 2 | jockey Nicola Currie | trainer Andrew Balding (14d 1/14) | headgear - | last run 28 days | form 2337 | MARKET 12.2% | 09:00 median 7.00 | Matchbook 7.40
    comment: Somers Isles is yet to win in her last four starts, but she has been thereabouts with a second four starts back and thirds two and three runs ago, and she has run over today's trip.
    DATA: model 16.3% | style Unknown | runs in data 4 | last 3: 26 Aug Newbury 6f Good To Firm 3/10; 19 Sep Chester 7f Heavy 3/11; 21 Oct Kempton (AW) 7f Standard / Slow 7/14 fig 70
    DATA for: Best recent form figure 70, 11 lb above field average; Good recent finishing positions
- Diamondise (hrs_17390777264) | 2yo G | 125lb | OR 63 | draw 4 | jockey Rhys Elliott(5) | trainer William Muir & Chris Grassick (14d 0/3) | headgear - | last run 20 days | form 0984 | MARKET 11.3% | 09:00 median 6.50 | Matchbook 9.00
    comment: Diamondise is winless in his last four, though a fourth last time out, 20 days ago, is a step up on an eighth and a ninth before it.
    DATA: model 3.2% | style Held up (led 4% of runs) | runs in data 4 | last 3: 28 Aug Sandown 7f Good 9/10; 19 Sep Newbury 7f Good To Firm 8/8; 29 Oct Southwell (AW) 7f Standard 4/13 fig 62
    DATA for: Carries 5 lb less than average; Pace: a contested lead should suit its hold-up style
    DATA against: Official rating 63, 5 lb below field average
- You're Sensational (hrs_17392192615) | 2yo F | 133lb | OR 71 | draw 3 | jockey Luke Catton(3) | trainer John & Thady Gosden (14d 4/10) | headgear p | last run 14 days | form 563 | MARKET 11.3% | 09:00 median 8.00 | Matchbook 8.00
    comment: Third last time out, 14 days ago, after a sixth and a fifth, she's yet to win in her last three starts, though she has run over today's trip.
    DATA: model 12.8% | style Leader (led 72% of runs) | runs in data 3 | last 3: 15 Sep Yarmouth 7f Good To Soft 5/9; 14 Oct Kempton (AW) 7f Standard / Slow 6/10 fig 67; 4 Nov Kempton (AW) 8f Standard / Slow 3/12 fig 59
    DATA for: Best recent form figure 67, 8 lb above field average; Trainer 40% wins (4/10), last 14 days
    DATA against: Pace: likely to be taken on for the lead
- El Paso (hrs_66586009) | 2yo C | 131lb | OR 69 | draw 7 | jockey Taylor Fisher | trainer Alan King (14d 3/18) | headgear - | last run 30 days | form 567 | MARKET 7.0% | 09:00 median 12.00 | Matchbook 14.00
    comment: El Paso is winless in his last three, finishing a fifth three starts back, a sixth two starts back and a seventh last time out, so the trend is the wrong way.
    DATA: model 2.6% | style Held up (led 4% of runs) | runs in data 3 | last 3: 14 Jul Ffos Las 6f Good 5/5; 28 Aug Sandown 7f Good 6/10; 19 Oct Southwell (AW) 7f Standard 7/14 fig 55
    DATA for: Pace: a contested lead should suit its hold-up style
    DATA against: Recent figures 14 lb below its current mark (looks high in the weights)
- Q T Boy (hrs_66655526) | 2yo G | 129lb | OR 67 | draw 9 | jockey Tom Eaves | trainer David Evans (14d 0/8) | headgear - | last run 20 days | form 742162 | MARKET 6.6% | 09:00 median 13.00 | Matchbook 14.00
    comment: Q T Boy arrives in decent nick after finishing second last time out, 20 days ago, and was a winner three starts back, while he has run over today's trip before.
    DATA: model 8.8% | style Leader (led 54% of runs) | runs in data 7 | last 3: 13 Sep Bath 8f Good To Soft 1/11; 21 Sep Leicester 8.2f Good 6/6; 29 Oct Bath 8f Soft 2/7 fig 75
    DATA for: Best recent form figure 75, 16 lb above field average; Recent figures 8 lb above its current mark (looks well handicapped); Has won at this trip or further; Good recent finishing positions
    DATA against: Trainer 0 wins from 8 runs, last 14 days; Pace: likely to be taken on for the lead
- Kiah (hrs_65938978) | 2yo F | 133lb | OR 71 | draw 5 | jockey Connor Planas | trainer Brian Meehan (14d 0/0) | headgear - | last run 30 days | form 032400 | MARKET 6.3% | 09:00 median 12.00 | Matchbook 16.50
    comment: Kiah has been unplaced in her last two outings after a second four starts back and a fourth three starts back, so she's slipped from that earlier level. She has run over today's trip and returns after 30 days, but she's yet to win in her last six and carries 133 lb from stall five.
    DATA: model 3.8% | style Midfield (led 29% of runs) | runs in data 6 | last 3: 27 Aug Lingfield 8f Standard 4/4; 26 Sep Newmarket 7f Good To Firm 10/10; 19 Oct Bath 8f Good To Soft 11/13 fig 53
    DATA against: Best recent form figure 53, 6 lb below field average; Recent figures 18 lb below its current mark (looks high in the weights)
- Global Success (hrs_63741895) | 2yo F | 129lb | OR 67 | draw 1 | jockey M. P. Sheehy | trainer J. S. Moore (14d 0/4) | headgear b | last run 30 days | form 253492 | MARKET 6.2% | 09:00 median 12.00 | Matchbook 17.00
    comment: She is yet to win in that spell though, and a ninth two starts back shows the risk of inconsistency.
    DATA: model 9.6% | style Midfield (led 5% of runs) | runs in data 11 | last 3: 18 Sep Ayr 7.2f Soft 4/8; 3 Oct Redcar 6f Good 9/13; 19 Oct Wolverhampton (AW) 7f Standard 2/12 fig 68
    DATA for: Best recent form figure 68, 9 lb above field average
- Arlecchino's Moon (hrs_65974559) | 2yo C | 128lb | OR 66 | draw 8 | jockey Dougie Costello | trainer Mark Usher (14d 0/3) | headgear - | last run 18 days | form 89510 | MARKET 3.8% | 09:00 median 23.00 | Matchbook 24.00
    comment: Won two starts back, but unplaced last time out, and he's run over today's trip and going before after 18 days off. Carrying 128 lb from stall eight, his 68 rating sits seventh of eleven, which keeps him a midfield proposition.
    DATA: model 6.5% | style Midfield (led 4% of runs) | runs in data 5 | last 3: 4 Sep Kempton 8f Standard To Slow 5/12; 8 Oct Southwell 8.1f Standard 1/12; 31 Oct Newmarket 9f Good To Soft 10/10 fig 40
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 40, 19 lb below field average; Recent figures 26 lb below its current mark (looks high in the weights)
- Bearly Blue (hrs_64847041) | 2yo F | 128lb | OR 66 | draw 10 | jockey Donagh Murphy(5) | trainer Richard Hughes (14d 0/9) | headgear p | last run 16 days | form 72547 | MARKET 2.0% | 09:00 median 34.00 | Matchbook 65.00
    comment: Bearly Blue is yet to win in her last five starts but has a second four starts back and a fourth two runs ago, and she's fresh from a 16-day break and has run on today's going.
    DATA: model 5.9% | style Leader (led 29% of runs) | runs in data 5 | last 3: 2 Jul Nottingham 6.1f Good To Firm 5/6; 11 Sep Chester 6.1f Good To Soft 4/9; 2 Nov Chelmsford (AW) 6f Standard 7/9 fig 59
    DATA against: Recent figures 7 lb below its current mark (looks high in the weights); Trainer 0 wins from 9 runs, last 14 days; Pace: likely to be taken on for the lead
- Storm Force Ten (hrs_17390466450) | 2yo G | 129lb | OR 67 | draw 11 | jockey William Carver | trainer Jamie Osborne (14d 0/2) | headgear b (1st time) | last run 34 days | form 03555 | MARKET 2.0% | 09:00 median 34.00 | Matchbook 60.00
    comment: Three fifths on the bounce, after a third four starts back, shows Storm Force Ten is consistent without quite getting his head in front, and he has run over today's trip.
    DATA: model 7.3% | style Held up (led 3% of runs) | runs in data 5 | last 3: 4 Sep Ascot 6f Good 5/7; 17 Sep Southwell 7.1f Standard 5/11; 15 Oct Brighton 6f Good 5/6 fig 41
    DATA for: First-time headgear; Pace: a contested lead should suit its hold-up style
    DATA against: Best recent form figure 41, 18 lb below field average; Recent figures 26 lb below its current mark (looks high in the weights); Last-run finishing speed -2.7% vs that field (faded)

## 6:30 Kempton (AW) | race_id rac_32304717887 | Juddmonte EBF Restricted Maiden Stakes (For Horses In Bands B, C And D) (Rider Restricted Race) (GBB/GBBPlus Race)
Flat | Class 2 | 1m | going Standard / Slow | AW | 14 runners | rating band - | age 2yo
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Sterling Cooper (hrs_17391918306) | 2yo C | 133lb | OR - | draw 4 | jockey Nicola Currie | trainer Andrew Balding (14d 1/14) | headgear - | last run 54 days | form 73 | MARKET 29.4% | 09:00 median 2.88 | Matchbook 2.88
    DATA: model 5.9% | style Prominent (led 38% of runs) | runs in data 2 | last 3: 8 Sep Leicester 7f Good To Soft 7/9; 25 Sep Newmarket 7f Good 3/14
    DATA for: Last-run finishing speed +2.0% vs that field (finished strongly)
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Playing Card (hrs_17392683868) | 2yo G | 133lb | OR - | draw 7 | jockey Dougie Costello | trainer Harry Eustace (14d 0/4) | headgear - | last run 35 days | form 27 | MARKET 12.3% | 09:00 median 6.80 | Matchbook 7.20
    DATA: model 11.5% | style Prominent (led 38% of runs) | runs in data 2 | last 3: 23 Sep Kempton 8f Standard To Slow 2/9; 14 Oct Nottingham 8.5f Good To Soft 7/11 fig 51
    DATA against: Best recent form figure 51, 4 lb below field average; Last-run finishing speed -3.1% vs that field (faded); Lightly raced: 2 runs in our data, so the model has little to go on
- Lady Margo (hrs_17394561268) | 2yo F | 128lb | OR - | draw 11 | jockey Luke Catton | trainer John & Thady Gosden (14d 4/10) | headgear - | last run 21 days | form 4 | MARKET 11.8% | 09:00 median 6.50 | Matchbook 8.00
    DATA: model 11.9% | style Held up (led 8% of runs) | runs in data 1 | last 3: 28 Oct Kempton (AW) 8f Standard / Slow 4/9 fig 59
    DATA for: Trainer 40% wins (4/10), last 14 days
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Ala Et Prece (hrs_17394441323) | 2yo C | 133lb | OR - | draw 5 | jockey Tom Eaves | trainer James Keane (14d 0/0) | headgear - | last run 23 days | form 3 | MARKET 10.6% | 09:00 median 7.00 | Matchbook 9.00
    DATA: model 10.7% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 26 Oct Kempton (AW) 7f Standard / Slow 3/9 fig 50
    DATA against: Best recent form figure 50, 5 lb below field average; Lightly raced: 1 run in our data, so the model has little to go on
- Present Dream (hrs_17393757115) | 2yo F | 128lb | OR - | draw 2 | jockey Laura Pearson | trainer David Menuisier (14d 0/2) | headgear - | last run 28 days | form 4 | MARKET 9.1% | 09:00 median 9.00 | Matchbook 9.80
    DATA: model 8.2% | style Held up (led 8% of runs) | runs in data 1 | last 3: 21 Oct Newmarket 7f Good To Soft 4/8 fig 49
    DATA against: Best recent form figure 49, 6 lb below field average; Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Civilon (hrs_17394623848) | 2yo C | 130lb | OR - | draw 14 | jockey Rhys Clutterbuck | trainer Hughie Morrison (14d 0/2) | headgear - | last run 20 days | form 3 | MARKET 5.0% | 09:00 median 15.00 | Matchbook 19.00
    DATA: model 7.6% | style Held up (led 8% of runs) | runs in data 1 | last 3: 29 Oct Bath 8f Soft 3/12 fig 62
    DATA for: Best recent form figure 62, 7 lb above field average; Last-run finishing speed +3.8% vs that field (finished strongly)
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Gilder Roy (hrs_17389965810) | 2yo C | 133lb | OR - | draw 9 | jockey Christian Howarth | trainer James Owen (14d 4/32) | headgear - | last run 37 days | form 73 | MARKET 4.6% | 09:00 median 15.00 | Matchbook 24.00
    DATA: model 3.4% | style Prominent (led 8% of runs) | runs in data 2 | last 3: 26 Aug Kempton 8f Standard To Slow 7/8; 12 Oct Yarmouth 10.1f Good To Soft 3/10
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Ivory Seraph (hrs_17394549795) | 2yo C | 133lb | OR - | draw 10 | jockey Josephine Gordon | trainer Marco Botti (14d 0/6) | headgear - | last run - days | form - | MARKET 3.7% | 09:00 median 21.00 | Matchbook 27.00
    DATA: model 6.3% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Askara (hrs_17395030618) | 2yo C | 130lb | OR - | draw 8 | jockey George Downing | trainer Ed Walker (14d 1/9) | headgear - | last run - days | form - | MARKET 3.4% | 09:00 median 23.00 | Matchbook 29.00
    DATA: model 6.2% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Grecian Warrior (hrs_17395551075) | 2yo C | 127lb | OR - | draw 6 | jockey George Bass | trainer Jack Channon (14d 1/6) | headgear - | last run - days | form - | MARKET 3.0% | 09:00 median 26.00 | Matchbook 34.00
    DATA: model 6.2% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Radical Bay (hrs_17392487784) | 2yo G | 130lb | OR - | draw 3 | jockey Jack Dace | trainer Amanda Perrett (14d 0/0) | headgear - | last run 20 days | form 04 | MARKET 2.3% | 09:00 median 34.00 | Matchbook 48.00
    DATA: model 3.6% | style Held up (led 5% of runs) | runs in data 2 | last 3: 12 Oct Kempton 7f Standard To Slow 10/11; 29 Oct Bath 8f Soft 4/12 fig 61
    DATA for: Best recent form figure 61, 6 lb above field average; Last-run finishing speed +3.9% vs that field (finished strongly)
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Global Twilight (hrs_17395548989) | 2yo G | 133lb | OR - | draw 13 | jockey Stevie Donohoe | trainer Charlie Fellowes (14d 1/7) | headgear - | last run - days | form - | MARKET 2.2% | 09:00 median 34.00 | Matchbook 48.00
    DATA: model 6.3% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Quiet Rebellion (hrs_17395558376) | 2yo F | 128lb | OR - | draw 12 | jockey Mikkel Mortensen | trainer Charlie Fellowes (14d 1/7) | headgear - | last run - days | form - | MARKET 1.4% | 09:00 median 51.00 | Matchbook 85.00
    DATA: model 6.2% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Augusta Savage (hrs_17394084617) | 2yo F | 125lb | OR - | draw 1 | jockey Laura Coughlan | trainer Ed de Giles (14d 0/0) | headgear - | last run - days | form - | MARKET 1.1% | 09:00 median 51.00 | Matchbook 160.00
    DATA: model 6.1% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on

## 7:00 Kempton (AW) | race_id rac_32304719824 | Try Unibet's New VAR Goal Guarantee Handicap Stakes (London Mile Series Qualifier) (Rider Restricted Race)
Flat | Class 2 | 1m | going Standard / Slow | AW | 14 runners | rating band 0-105 | age 3yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Palladas (hrs_56746403) | 3yo C | 129lb | OR 95 | draw 1 | jockey Connor Planas | trainer Charlie Appleby (14d 2/4) | headgear - | last run 26 days | form 114 | MARKET 29.9% | 09:00 median 2.69 | Matchbook 2.98
    comment: Carrying 129 lb from stall 1, he looks outclassed on pace figures.
    DATA: model 17.7% | style Midfield (led 5% of runs) | runs in data 3 | last 3: 28 Jan Kempton 8f Standard To Fast 1/12; 16 Aug Southwell 8.1f Standard 1/10; 23 Oct Doncaster 7f Heavy 4/9 fig 89
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Best recent form figure 89, 4 lb below field average; Recent figures 6 lb below its current mark (looks high in the weights)
- Princling (hrs_57654303) | 3yo G | 124lb | OR 90 | draw 3 | jockey M. P. Sheehy | trainer William Haggas (14d 2/7) | headgear - | last run 47 days | form -14563 | MARKET 22.6% | 09:00 median 3.50 | Matchbook 4.00
    comment: Princling has only one win in his last five, five starts back, and a sixth and a fifth since then show a slide before a third last time out.
    DATA: model 5.4% | style Midfield (led 8% of runs) | runs in data 5 | last 3: 20 Jun Ascot 10f Good To Firm 5/16; 10 Jul Newmarket 10f Good To Firm 6/6; 2 Oct Ascot 8f Good To Firm 3/9
    DATA for: Trainer 29% wins (2/7), last 14 days; Has won at this trip or further; Carries 7 lb less than average
    DATA against: Official rating 90, 6 lb below field average
- Wise Prince (hrs_57316322) | 3yo G | 133lb | OR 99 | draw 9 | jockey Tyler Heard | trainer John & Thady Gosden (14d 4/10) | headgear - | last run 21 days | form -38485 | MARKET 9.3% | 09:00 median 8.00 | Matchbook 10.50
    comment: Wise Prince is fresh enough after 21 days off, and he showed up best when third five starts back, with a fifth last time out suggesting he's in decent shape.
    DATA: model 6.9% | style Midfield (led 5% of runs) | runs in data 5 | last 3: 28 May Sandown 8f Good 4/8; 18 Jun Ascot 8f Good To Firm 8/30; 28 Oct Nottingham 8.5f Soft 5/8 fig 103
    DATA for: Best recent form figure 103, 10 lb above field average; Recent figures 4 lb above its current mark (looks well handicapped); Trainer 40% wins (4/10), last 14 days
- Ebt's Guard (hrs_35714455) | 5yo G | 140lb | OR 104 | draw 11 | jockey Rhys Elliott(5) | trainer William Muir & Chris Grassick (14d 0/3) | headgear - | last run 21 days | form 944332 | MARKET 7.5% | 09:00 median 10.00 | Matchbook 13.00
    comment: Yet to win in his last six, he carries 140 lb from draw 11, which is the main risk.
    DATA: model 16.8% | style Midfield (led 3% of runs) | runs in data 10 | last 3: 12 Sep Doncaster 8f Good 3/17; 17 Oct Ascot 8f Good 3/20 fig 105; 28 Oct Nottingham 8.5f Soft 2/8 fig 107
    DATA for: Best recent form figure 107, 14 lb above field average; Official rating 104, 8 lb above field average; Last-run finishing speed +2.4% vs that field (finished strongly); Good recent finishing positions
    DATA against: Carries 9 lb more than average
- Hard Endeavor (hrs_51866360) | 4yo C | 134lb | OR 98 | draw 12 | jockey Sorin Moldoveanu(7) | trainer Jane Chapple-Hyam (14d 0/0) | headgear - | last run 53 days | form -04250 | MARKET 6.8% | 09:00 median 11.00 | Matchbook 14.50
    comment: Hard Endeavor is winless in his last five and was unplaced last time out, though a second three starts back shows he can run well, and he has run over today's trip and going before.
    DATA: model 10.4% | style Midfield (led 4% of runs) | runs in data 5 | last 3: 4 Jul Sandown 8f Good To Firm 2/14; 4 Sep Ascot 8f Good 5/13; 26 Sep Newmarket 9f Good To Firm 11/27
- Shafdar (hrs_46233733) | 4yo G | 128lb | OR 92 | draw 6 | jockey William Cox | trainer Ian Williams (14d 0/9) | headgear t | last run 25 days | form 644104 | MARKET 5.1% | 09:00 median 15.00 | Matchbook 19.00
    comment: Shafdar was fourth last time out, 25 days ago, and has a win three starts back in his last six, though he was unplaced two starts back.
    DATA: model 9.0% | style Midfield (led 5% of runs) | runs in data 12 | last 3: 12 Sep Chester 10.3f Soft 1/10; 26 Sep Newmarket 9f Good To Firm 12/27; 24 Oct Doncaster 10f Heavy 4/14 fig 92
    DATA for: Has won at this trip or further
    DATA against: Trainer 0 wins from 9 runs, last 14 days
- Oliver Show (hrs_32249217) | 6yo G | 125lb | OR 89 | draw 8 | jockey Toby Moore(7) | trainer George Boughey (14d 1/5) | headgear tp | last run 20 days | form 442766 | MARKET 4.8% | 09:00 median 15.00 | Matchbook 22.00
    comment: Oliver Show has been beaten into sixth in each of his last two, and he is winless in his last six, though a second four starts back shows he can get closer.
    DATA: model 3.3% | style Held up (led 4% of runs) | runs in data 7 | last 3: 13 Sep Doncaster 6.5f Good 7/13; 23 Sep Goodwood 8f Good 6/7; 29 Oct Southwell (AW) 7f Standard 6/14 fig 89
    DATA for: Trainer 20% wins (1/5), last 14 days; Carries 6 lb less than average
    DATA against: Best recent form figure 89, 4 lb below field average; Official rating 89, 6 lb below field average; Poor recent finishing positions; Pace: steady gallop likely, hard to come from off the pace
- Chantilly Lace (hrs_45378375) | 4yo F | 139lb | OR 103 | draw 7 | jockey Rhys Clutterbuck | trainer Ralph Beckett (14d 0/7) | headgear - | last run 199 days | form 5535-5 | MARKET 3.5% | 09:00 median 21.00 | Matchbook 29.00
    comment: Fifth last time out and fifth two starts back, with a third three starts back, she is consistent without a win in her last five, and has run over today's trip.
    DATA: model 8.5% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 3 May Newmarket 9f Good To Firm 5/10
    DATA for: Official rating 103, 8 lb above field average
    DATA against: Carries 8 lb more than average; Returns from a 199-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Two Tempting (hrs_28098266) | 7yo G | 131lb | OR 95 | draw 10 | jockey Tom Eaves | trainer Jonathan Portman (14d 1/9) | headgear - | last run 56 days | form 330405 | MARKET 3.0% | 09:00 median 23.00 | Matchbook 36.00
    comment: He has run over today's trip and going, but 56 days off and no win in his last six outings is the main risk.
    DATA: model 4.7% | style Prominent (led 4% of runs) | runs in data 7 | last 3: 22 Aug Chester 7.6f Good To Soft 4/13; 5 Sep Kempton 8f Standard To Slow 10/14; 23 Sep Goodwood 8f Good 5/7
    DATA against: Aged 7, older than most of this field
- Mister Winston (hrs_44816625) | 4yo G | 134lb | OR 98 | draw 14 | jockey Alfie Redman(7) | trainer Andrew Balding (14d 1/14) | headgear - | last run 32 days | form 007860 | MARKET 1.9% | 09:00 median 51.00 | Matchbook 50.00
    comment: Mister Winston has been well beaten in recent outings, unplaced last time and a sixth two starts back, and he is yet to win in his last six, though he has run over today's trip and returns after 32 days off.
    DATA: model 4.0% | style Held up (led 8% of runs) | runs in data 9 | last 3: 12 Sep Doncaster 8f Good 8/17; 26 Sep Haydock 8f Heavy 6/9; 17 Oct Ascot 8f Good 19/20 fig 84
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 84, 9 lb below field average; Recent figures 14 lb below its current mark (looks high in the weights); Last-run finishing speed -3.3% vs that field (faded); Poor recent finishing positions; Pace: steady gallop likely, hard to come from off the pace
- Brian (hrs_412693176) | 4yo G | 133lb | OR 97 | draw 4 | jockey Millie Wonnacott(5) | trainer J. S. Moore (14d 0/4) | headgear - | last run 14 days | form 721004 | MARKET 1.8% | 09:00 median 41.00 | Matchbook 65.00
    comment: Brian was fourth last time out just 14 days ago, and he has run over today's trip and going, but he's been unplaced in the two runs before that and his only win in his last six came four starts back.
    DATA: model 2.9% | style Midfield (led 3% of runs) | runs in data 8 | last 3: 11 Oct Goodwood 8f Good To Soft 10/13; 17 Oct Ascot 8f Good 15/20 fig 90; 4 Nov Kempton (AW) 7f Standard / Slow 4/9 fig 96
- Aalto (hrs_32936428) | 6yo G | 127lb | OR 91 | draw 13 | jockey Dougie Costello | trainer Ian Williams (14d 0/9) | headgear t | last run 46 days | form 213320 | MARKET 1.7% | 09:00 median 34.00 | Matchbook 80.00
    comment: He has run over today's trip and on the going, and carries 127 lb from stall 13.
    DATA: model 7.3% | style Held up (led 8% of runs) | runs in data 8 | last 3: 4 Sep Ascot 7f Good 3/8; 19 Sep Newbury 7f Good To Firm 2/16; 3 Oct Ascot 7f Good To Firm 18/18
    DATA for: Good recent finishing positions
    DATA against: Trainer 0 wins from 9 runs, last 14 days; Pace: steady gallop likely, hard to come from off the pace
- Tarkhan (hrs_35039599) | 7yo G | 130lb | OR 94 | draw 5 | jockey William Carver | trainer Jamie Osborne (14d 0/2) | headgear - | last run 235 days | form 7200-0 | MARKET 1.2% | 09:00 median 51.00 | Matchbook 140.00
    comment: Tarkhan returns after 235 days off, having been unplaced in his last three outings, though he was second four starts back and has run over today's trip.
    DATA: model 1.3% | style Unknown | runs in data 1 | last 3: 28 Mar Doncaster 8f Good To Soft 18/21
    DATA against: Last-run finishing speed -4.8% vs that field (faded); Returns from a 235-day break; Lightly raced: 1 run in our data, so the model has little to go on; Aged 7, older than most of this field
- Brasil Power (hrs_25795280) | 7yo G | 128lb | OR 92 | draw 2 | jockey Megan Smith(7) | trainer George Boughey (14d 1/5) | headgear t | last run 28 days | form 609098 | MARKET 0.8% | 09:00 median 81.00 | Matchbook 200.00
    comment: Winless in his last six, Brasil Power has finished eighth last time out, a ninth two starts back and a ninth four starts back, so he is hard to fancy.
    DATA: model 1.8% | style Held up (led 8% of runs) | runs in data 10 | last 3: 18 Jun Ascot 7f Good To Firm 19/28; 4 Jul Sandown 9.9f Good To Firm 9/9; 21 Oct Kempton (AW) 16f Standard / Slow 8/14 fig 85
    DATA for: Trainer 20% wins (1/5), last 14 days; Has won at this trip or further
    DATA against: Best recent form figure 85, 8 lb below field average; Recent figures 7 lb below its current mark (looks high in the weights); Poor recent finishing positions; Aged 7, older than most of this field; Pace: steady gallop likely, hard to come from off the pace

## 7:30 Kempton (AW) | race_id rac_32304721761 | Unibet Interactive Handicap Stakes (London Stayers' Series Qualifier) (GBBPlus Race)
Flat | Class 4 | 1m7f218y | going Standard / Slow | AW | 7 runners | rating band 0-85 | age 3yo+
DATA pace: Lone leader - Provision is the only habitual front-runner and may be allowed an easy lead.
- Zachary Hickes (hrs_47655377) | 4yo G | 139lb | OR 82 | draw 3 | jockey Ross Coakley | trainer Roger Varian (14d 2/6) | headgear - | last run 36 days | form 641231 | MARKET 37.5% | 09:00 median 2.38 | Matchbook 2.48
    comment: Zachary Hickes arrives in cracking form, a winner last time out, a third two starts back, and a second three starts back, and he has run on today's going before. Carrying 139 lb off a mark of 82 after 36 days off, the layoff is the one concern.
    DATA: model 35.0% | style Midfield (led 3% of runs) | runs in data 6 | last 3: 29 Aug Goodwood 14f Soft 2/9; 17 Sep Yarmouth 14.1f Good 3/10; 13 Oct Wolverhampton 14f Standard 1/7
    DATA for: Trainer 33% wins (2/6), last 14 days; Good recent finishing positions
- Mr Freedom (hrs_25286429) | 7yo G | 130lb | OR 73 | draw 6 | jockey Rose Dawes(3) | trainer Sheena West (14d 0/2) | headgear p | last run 13 days | form 854423 | MARKET 16.6% | 09:00 median 5.00 | Matchbook 6.00
    comment: Mr Freedom is fresh from a third last time out, and a second two starts back, and he returns after just 13 days with experience of today's trip and going.
    DATA: model 13.9% | style Midfield (led 3% of runs) | runs in data 8 | last 3: 1 Oct Salisbury 14.2f Soft 4/10; 11 Oct Goodwood 16f Good To Soft 2/12; 5 Nov Chelmsford (AW) 16f Standard 3/6 fig 74
    DATA for: Good recent finishing positions; Carries 5 lb less than average
    DATA against: Official rating 73, 5 lb below field average
- Squire Danagher (hrs_31698065) | 6yo G | 143lb | OR 86 | draw 2 | jockey Connor Planas | trainer Emma Lavelle (14d 3/13) | headgear b | last run 28 days | form 1/1930 | MARKET 13.5% | 09:00 median 6.00 | Matchbook 7.40
    comment: Squire Danagher won twice in his last five starts, taking a win four starts back and another five starts back, and he bounced back from a ninth three starts back with a third two starts back.
    DATA: model 9.0% | style Held up (led 4% of runs) | runs in data 4 | last 3: 30 Aug Goodwood 16f Soft 9/9; 19 Sep Newmarket 18f Good 3/6; 21 Oct Kempton (AW) 16f Standard / Slow 10/14 fig 78
    DATA for: Official rating 86, 8 lb above field average; Trainer 23% wins (3/13), last 14 days
    DATA against: Recent figures 8 lb below its current mark (looks high in the weights); Carries 8 lb more than average
- Environment Amigo (hrs_40132820) | 5yo G | 137lb | OR 80 | draw 5 | jockey Jonny Peate | trainer James Fanshawe (14d 0/1) | headgear t | last run 462 days | form 21/42- | MARKET 13.2% | 09:00 median 6.00 | Matchbook 7.80
    comment: Environment Amigo bids to build on a second last time out, with a win three starts back and a fourth two runs ago, and he has run over today's trip and going before. The big risk is a 462-day absence, and 137 lb is no small burden.
    DATA: model 14.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 462-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Tarbat Ness (hrs_29295357) | 7yo G | 133lb | OR 76 | draw 1 | jockey Liam Wright(3) | trainer John Berry (14d 0/1) | headgear b | last run 23 days | form 103221 | MARKET 8.3% | 09:00 median 11.00 | Matchbook 11.50
    DATA: model 12.7% | style Held up (led 5% of runs) | runs in data 14 | last 3: 3 Sep Newcastle 16.3f Standard 2/4; 26 Sep Ripon 16f Good 2/5; 26 Oct Southwell (AW) 16.5f Standard 1/6 fig 67
    DATA for: Last-run finishing speed +7.7% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Best recent form figure 67, 8 lb below field average; Recent figures 9 lb below its current mark (looks high in the weights)
- Provision (hrs_55392876) | 4yo G | 123lb | OR 65 | draw 4 | jockey Nicola Currie | trainer Barry Brennan (14d 0/1) | headgear - | last run 39 days | form 533-83 | MARKET 7.0% | 09:00 median 13.00 | Matchbook 13.50
    comment: Provision has hit the frame in three of his last five, including a third last time out, but he is winless in that spell and a eighth two starts back shows his limits.
    DATA: model 7.4% | style Leader (led 54% of runs) | runs in data 7 | last 3: 22 Jul Worcester 16f Good 1/9; 8 Sep Bangor-on-Dee 16.7f Good 3/8; 10 Oct Chepstow 16.1f Good To Soft F/12
    DATA for: Carries 12 lb less than average; Pace: may get an uncontested lead
    DATA against: Official rating 65, 13 lb below field average
- Majestic (hrs_29394456) | 8yo G | 141lb | OR 84 | draw 7 | jockey George Bass | trainer Jack Channon (14d 1/6) | headgear - | last run 21 days | form 420306 | MARKET 3.8% | 09:00 median 23.00 | Matchbook 26.00
    comment: Majestic is yet to win in his last six, but he has been a third three starts back and a second five starts back, and returns fresh after 21 days off.
    DATA: model 7.5% | style Held up (led 3% of runs) | runs in data 7 | last 3: 7 Aug Thirsk 12f Good 3/6; 5 Sep Kempton 12f Standard To Slow 11/11; 28 Oct Kempton (AW) 12f Standard / Slow 6/10 fig 79
    DATA for: Best recent form figure 79, 4 lb above field average; Official rating 84, 6 lb above field average
    DATA against: Carries 6 lb more than average

## 8:00 Kempton (AW) | race_id rac_32304723698 | Unibet 3 Uniboosts A Day Handicap Stakes (Rider Restricted Race)
Flat | Class 4 | 7f | going Standard / Slow | AW | 13 runners | rating band 0-85 | age 3yo+
DATA pace: Lone leader - Mister Bluebird is the only habitual front-runner and may be allowed an easy lead.
- I'm Workin On It (hrs_45314864) | 4yo G | 138lb | OR 85 | draw 4 | jockey Kieren Fox | trainer Rod Millman (14d 0/1) | headgear p | last run 23 days | form 204439 | MARKET 17.7% | 09:00 median 4.33 | Matchbook 5.60 | CHECK (skip line 4.11)
    comment: I'm Workin On It is yet to win in his last six starts but has hit the frame, a third two starts back and a second six starts back, and he has run over today's distance and going before.
    DATA: model 10.2% | style Prominent (led 8% of runs) | runs in data 11 | last 3: 5 Sep Kempton 8f Standard To Slow 4/14; 12 Oct Kempton 8f Standard To Slow 3/14; 26 Oct Kempton (AW) 7f Standard / Slow 9/12 fig 77
    DATA for: Official rating 85, 5 lb above field average; Has won at this trip or further
    DATA against: Recent figures 8 lb below its current mark (looks high in the weights); Carries 5 lb more than average
- Enacting (hrs_45314822) | 4yo G | 131lb | OR 78 | draw 6 | jockey Jonny Peate | trainer James Fanshawe (14d 0/1) | headgear h | last run 41 days | form 541/2 | MARKET 16.2% | 09:00 median 5.00 | Matchbook 5.70
    comment: Enacting arrives in good heart, second last time out and a winner two starts back, and he has run over today's trip and going before, but 41 days off and 131 lb may temper him.
    DATA: model 12.7% | style Held up (led 8% of runs) | runs in data 1 | last 3: 8 Oct Southwell 7.1f Standard 2/12
    DATA for: Last-run finishing speed +4.7% vs that field (finished strongly)
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Pinatubo's Legacy (hrs_41661529) | 4yo G | 136lb | OR 83 | draw 11 | jockey Connor Planas | trainer T. J. Kent (14d 0/1) | headgear - | last run 23 days | form -30502 | MARKET 14.7% | 09:00 median 5.75 | Matchbook 6.20
    comment: Runner-up last time out after 23 days off, he has a fair profile for a midfield type, and has run over today's trip before.
    DATA: model 8.5% | style Held up (led 3% of runs) | runs in data 5 | last 3: 8 Aug Newmarket 7f Good To Firm 5/10; 12 Sep Doncaster 8f Good 16/17; 26 Oct Kempton (AW) 7f Standard / Slow 2/12 fig 88
    DATA for: Best recent form figure 88, 10 lb above field average; Recent figures 5 lb above its current mark (looks well handicapped)
- Caragio (hrs_32061239) | 6yo G | 134lb | OR 81 | draw 2 | jockey Shay Farmer(5) | trainer Adam Kirby (14d 0/7) | headgear /es | last run 18 days | form 633112 | MARKET 12.7% | 09:00 median 6.50 | Matchbook 7.20
    comment: Caragio arrives in cracking form, second last time out and a winner two and three starts back, and he returns after 18 days having run over today's trip and going.
    DATA: model 17.9% | style Midfield (led 5% of runs) | runs in data 9 | last 3: 7 Oct Kempton 7f Standard To Slow 1/8; 21 Oct Kempton (AW) 6f Standard / Slow 1/12 fig 82; 31 Oct Newmarket 6f Good To Soft 2/10 fig 84
    DATA for: Best recent form figure 84, 6 lb above field average; Has won at this trip or further; Good recent finishing positions
- Comic Hero (hrs_52054387) | 3yo G | 133lb | OR 81 | draw 8 | jockey Nicola Currie | trainer Andrew Balding (14d 1/14) | headgear - | last run 158 days | form 2-1526 | MARKET 10.7% | 09:00 median 8.00 | Matchbook 9.00
    DATA: model 6.4% | style Prominent (led 8% of runs) | runs in data 4 | last 3: 4 Apr Musselburgh 8f Soft 5/6; 1 May Newmarket 8f Good To Firm 2/9; 13 Jun Chester 7.6f Good To Soft 6/9
    DATA for: Has won at this trip or further
    DATA against: Returns from a 158-day break
- Chalk Mountain (hrs_31631355) | 6yo G | 130lb | OR 77 | draw 3 | jockey Alfie Redman(7) | trainer Zoe Hawkins (14d 0/0) | headgear t | last run 16 days | form 463486 | MARKET 8.3% | 09:00 median 9.25 | Matchbook 12.50
    comment: Chalk Mountain has run over today's trip and going and was third four starts back, but he's yet to win in his last six and comes here on the back of a sixth and an eighth.
    DATA: model 7.7% | style Midfield (led 4% of runs) | runs in data 12 | last 3: 30 Sep Kempton 8f Standard To Slow 4/13; 14 Oct Kempton (AW) 7f Standard / Slow 8/12 fig 75; 2 Nov Wolverhampton (AW) 7f Standard 6/9 fig 71
    DATA for: Has won at this trip or further
- Enricher (hrs_53689713) | 3yo G | 129lb | OR 77 | draw 1 | jockey Rhys Elliott(5) | trainer William Muir & Chris Grassick (14d 0/3) | headgear p | last run 16 days | form -09961 | MARKET 6.2% | 09:00 median 12.00 | Matchbook 17.50
    comment: On the plus side, he's fresh from a 16-day break and has run over today's trip, with 129 lb from stall one.
    DATA: model 5.0% | style Held up (led 3% of runs) | runs in data 5 | last 3: 19 Sep Newmarket 6f Good 9/9; 14 Oct Kempton (AW) 7f Standard / Slow 6/12 fig 73; 2 Nov Wolverhampton (AW) 7f Standard 1/7 fig 72
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 73, 5 lb below field average
- Society Kiss (hrs_52615122) | 3yo F | 136lb | OR 84 | draw 5 | jockey Stevie Donohoe | trainer John Mackie (14d 0/5) | headgear p | last run 16 days | form 320031 | MARKET 4.1% | 09:00 median 17.00 | Matchbook 27.00
    comment: Society Kiss won last time out and was third two starts back, and she's fresh enough after 16 days, having run over today's trip before.
    DATA: model 7.8% | style Held up (led 4% of runs) | runs in data 6 | last 3: 18 Sep Ayr 6f Soft 23/24; 1 Oct Newcastle 6f Standard 3/9; 2 Nov Chelmsford (AW) 7f Standard 1/8 fig 86
    DATA for: Best recent form figure 86, 8 lb above field average; Last-run finishing speed +3.8% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
- Shihoku (hrs_36207388) | 5yo G | 128lb | OR 75 | draw 13 | jockey Christian Howarth(3) | trainer James Owen (14d 4/32) | headgear tp (1st time) | last run 153 days | form 6-4708 | MARKET 2.9% | 09:00 median 23.00 | Matchbook 38.00
    comment: Shihoku is winless in his last five, finishing eighth last time out and never better than a fourth four starts back, and he returns after 153 days off.
    DATA: model 2.0% | style Held up (led 8% of runs) | runs in data 4 | last 3: 4 Mar Kempton 8f Standard To Slow 7/11; 11 Apr Yarmouth 10.1f Good 13/13; 18 Jun Yarmouth 8f Good To Firm 8/9
    DATA for: First-time headgear
    DATA against: Official rating 75, 5 lb below field average; Last-run finishing speed -3.5% vs that field (faded); Poor recent finishing positions; Returns from a 153-day break
- Bell Shot (hrs_25263273) | 7yo G | 134lb | OR 81 | draw 7 | jockey Jude Maher(7) | trainer Michael Appleby (14d 1/13) | headgear p | last run 44 days | form 342027 | MARKET 2.7% | 09:00 median 26.00 | Matchbook 40.00
    comment: The risk is a seventh last time out and a 44-day layoff, so he may need to bounce back from the break.
    DATA: model 5.4% | style Unknown | runs in data 12 | last 3: 12 Aug Beverley 7.3f Good To Firm 10/10; 24 Sep Pontefract 6f Good 2/14; 5 Oct Pontefract 6f Good 7/10
    DATA against: Last-run finishing speed -2.8% vs that field (faded)
- Mister Bluebird (hrs_22111432) | 8yo G | 131lb | OR 78 | draw 12 | jockey Jack Dace(5) | trainer Heather Main (14d 0/0) | headgear - | last run 18 days | form 207305 | MARKET 1.5% | 09:00 median 41.00 | Matchbook 85.00
    comment: Fit after 18 days off, Mister Bluebird has run over today's trip and on this going, and he was a third three starts back, with a second six starts back too.
    DATA: model 5.6% | style Leader (led 29% of runs) | runs in data 8 | last 3: 8 Sep Goodwood 6f Soft 3/7; 23 Sep Goodwood 6f Good 11/15; 31 Oct Newmarket 7f Good To Soft 5/16 fig 84
    DATA for: Best recent form figure 84, 6 lb above field average; Recent figures 6 lb above its current mark (looks well handicapped); Pace: may get an uncontested lead
    DATA against: Aged 8, older than most of this field
- Uniting (hrs_50590351) | 4yo G | 129lb | OR 76 | draw 9 | jockey Jude Fernandes(7) | trainer Luke Dace (14d 0/2) | headgear - | last run 23 days | form -79320 | MARKET 1.4% | 09:00 median 51.00 | Matchbook 140.00
    comment: Uniting is winless in his last five and was unplaced last time out, though a second and a third two and three starts back show he can get involved.
    DATA: model 5.4% | style Midfield (led 5% of runs) | runs in data 5 | last 3: 12 Mar Chelmsford 8f Standard 3/7; 7 Apr Southwell 8.1f Standard 2/13; 26 Oct Kempton (AW) 8f Standard / Slow 12/13 fig 58
    DATA for: Good recent finishing positions
    DATA against: Best recent form figure 58, 20 lb below field average; Recent figures 18 lb below its current mark (looks high in the weights)
- One More (hrs_44570750) | 4yo G | 137lb | OR 84 | draw 10 | jockey Joey Haynes | trainer Chelsea Banham (14d 1/1) | headgear - | last run 37 days | form -08150 | MARKET 0.9% | 09:00 median 81.00 | Matchbook 150.00
    comment: The main risk is a poor latest run, unplaced last time out, after a 37-day break.
    DATA: model 5.4% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 27 Mar Lingfield 7f Standard 1/9; 6 Apr Wolverhampton 7.2f Standard 5/6; 12 Oct Kempton 8f Standard To Slow 14/14
    DATA for: Has won at this trip or further

## 8:30 Kempton (AW) | race_id rac_32304725635 | Unibet More Extra Place Races Handicap Stakes (Rider Restricted Race)
Flat | Class 5 | 1m3f219y | going Standard / Slow | AW | 13 runners | rating band 0-75 | age 3yo+
DATA pace: Strong pace - 3 habitual front-runners (Maestro Del Mar, Snooker McCrew, We Ride At Dawn). A contested lead should set things up for horses coming from behind.
- Crown Of Crowns (hrs_17392180099) | 3yo F | 134lb | OR 74 | draw 8 | jockey Ross Coakley | trainer William Haggas (14d 2/7) | headgear - | last run 41 days | form 41 | MARKET 24.1% | 09:00 median 3.25 | Matchbook 3.80 | CHECK (skip line 3.09)
    comment: Fresh from a win last time out, with a fourth two starts back, she has run over today's trip and is 41 days off the track, but carrying 134 lb off an official 74 looks a big ask.
    DATA: model 16.1% | style Held up (led 5% of runs) | runs in data 2 | last 3: 14 Sep Windsor 11.4f Good To Soft 4/7; 8 Oct Southwell 11.1f Standard 1/7
    DATA for: Trainer 29% wins (2/7), last 14 days; Pace: a contested lead should suit its hold-up style
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Course: hold-up horses have won 0.7× their fair share at 12f here
- Maestro Del Mar (hrs_48498996) | 4yo G | 139lb | OR 74 | draw 1 | jockey Connor Planas | trainer Ismail Mohammed & Jose Santos (14d 0/1) | headgear p (1st time) | last run 16 days | form -32432 | MARKET 15.4% | 09:00 median 5.00 | Matchbook 6.00
    comment: Maestro Del Mar is consistent, with a second last time out and a third two starts back, yet he is winless in his last five and has only been placed rather than getting his head in front. Fresh enough after 16 days and he has run over today's trip, but 139 lb is a hefty burden for a 74-rated gelding.
    DATA: model 10.8% | style Leader (led 38% of runs) | runs in data 5 | last 3: 3 Sep Southwell 12.1f Standard 4/7; 27 Sep Epsom Downs 10.1f Good 3/6; 2 Nov Chelmsford (AW) 10f Standard 2/8 fig 75
    DATA for: Best recent form figure 75, 8 lb above field average; Good recent finishing positions; First-time headgear
    DATA against: Pace: likely to be taken on for the lead
- Snooker McCrew (hrs_38306226) | 5yo G | 133lb | OR 68 | draw 9 | jockey Alfie Redman(7) | trainer Max Comley (14d 2/7) | headgear - | last run 14 days | form 561111 | MARKET 13.7% | 09:00 median 5.50 | Matchbook 6.80
    comment: He has run over today's trip, yet the big weight and modest figures make him tough to fancy.
    DATA: model 15.4% | style Leader (led 29% of runs) | runs in data 7 | last 3: 22 Sep Beverley 9.9f Good 1/12; 7 Oct Kempton 8f Standard To Slow 1/13; 4 Nov Kempton (AW) 8f Standard / Slow 1/13 fig 78
    DATA for: Best recent form figure 78, 11 lb above field average; Recent figures 10 lb above its current mark (looks well handicapped); Trainer 29% wins (2/7), last 14 days; Last-run finishing speed +2.0% vs that field (finished strongly); Good recent finishing positions
    DATA against: Pace: likely to be taken on for the lead
- Dust Cover (hrs_51557709) | 4yo G | 137lb | OR 72 | draw 6 | jockey Josephine Gordon | trainer Ross Burdon (14d 0/1) | headgear - | last run 39 days | form 025455 | MARKET 12.2% | 09:00 median 6.00 | Matchbook 7.80
    comment: The main risk is a yet-to-win profile, with a fifth last time out and another fifth the start before.
    DATA: model 6.4% | style Midfield (led 3% of runs) | runs in data 8 | last 3: 8 Jul Kempton 16f Standard To Slow 4/9; 12 Aug Kempton 12f Standard To Slow 5/12; 10 Oct Southwell 14.1f Standard 5/7
- Midnight Media (hrs_55795019) | 3yo F | 130lb | OR 70 | draw 7 | jockey Rhys Elliott(5) | trainer William Muir & Chris Grassick (14d 0/3) | headgear - | last run 20 days | form 122413 | MARKET 10.7% | 09:00 median 7.00 | Matchbook 8.80
    DATA: model 11.5% | style Prominent (led 23% of runs) | runs in data 14 | last 3: 24 Sep Southwell 11.1f Standard 4/12; 13 Oct Wolverhampton 12.2f Standard 1/11; 29 Oct Southwell (AW) 11f Standard 3/7 fig 70
    DATA for: Has won at this trip or further; Good recent finishing positions
- Harlington (hrs_37932363) | 5yo G | 132lb | OR 67 | draw 10 | jockey Liam Wright(3) | trainer Charlie Clover (14d 0/4) | headgear p | last run 40 days | form 133852 | MARKET 5.0% | 09:00 median 15.00 | Matchbook 19.00
    comment: Harlington was second last time out and has been in the first three in four of his last six, but a fifth and an eighth in between show inconsistency, and he returns after 40 days.
    DATA: model 4.6% | style Held up (led 5% of runs) | runs in data 9 | last 3: 2 Jul Newbury 10f Good To Firm 8/11; 24 Jul Sandown 9.9f Good To Firm 5/6; 9 Oct Kempton 12f Standard To Slow 2/7
    DATA for: Pace: a contested lead should suit its hold-up style
    DATA against: Course: hold-up horses have won 0.7× their fair share at 12f here
- We Ride At Dawn (hrs_56961709) | 3yo F | 130lb | OR 70 | draw 3 | jockey Rhys Clutterbuck | trainer Robert Edwards (14d 0/1) | headgear - | last run 96 days | form -02411 | MARKET 4.4% | 09:00 median 17.00 | Matchbook 23.00
    comment: She arrives on a two-race winning streak, a first last time out and another two starts back, and has run over today's trip and going, but a 96-day absence and 130 lb on her back temper the enthusiasm.
    DATA: model 8.4% | style Leader (led 54% of runs) | runs in data 5 | last 3: 1 Jul Bath 11.6f Firm 4/7; 23 Jul Sandown 9.9f Good To Firm 1/7; 14 Aug Newbury 10f Good To Firm 1/4
    DATA for: Last-run finishing speed +2.1% vs that field (finished strongly); Good recent finishing positions
    DATA against: Returns from a 96-day break; Pace: likely to be taken on for the lead
- Youthful King (hrs_26299189) | 7yo G | 137lb | OR 72 | draw 4 | jockey Jack Dace(5) | trainer Luke Dace (14d 0/2) | headgear h | last run 21 days | form 864407 | MARKET 3.5% | 09:00 median 23.00 | Matchbook 27.00
    comment: The risk is a seventh last time out and no finish better than a fourth in that spell.
    DATA: model 1.9% | style Prominent (led 5% of runs) | runs in data 7 | last 3: 20 Jun Newmarket 14f Good To Firm 4/5; 14 Oct Kempton (AW) 11f Standard / Slow 11/13 fig 61; 28 Oct Kempton (AW) 12f Standard / Slow 7/10 fig 67
    DATA against: Aged 7, older than most of this field
- Marquetry (hrs_17391520923) | 3yo F | 133lb | OR 73 | draw 5 | jockey William Carver | trainer Andrew Balding (14d 1/14) | headgear - | last run 14 days | form 7236 | MARKET 3.3% | 09:00 median 26.00 | Matchbook 29.00
    comment: Marquetry is hard to fancy, as she was only sixth last time out and is winless in her last four, though a third two starts back and a second three starts back show she can get involved.
    DATA: model 8.6% | style Prominent (led 3% of runs) | runs in data 4 | last 3: 14 Sep Windsor 11.4f Good To Soft 2/7; 7 Oct Kempton 11f Standard To Slow 3/8; 4 Nov Nottingham 14f Soft 6/10 fig 64
    DATA for: Good recent finishing positions
    DATA against: Recent figures 9 lb below its current mark (looks high in the weights)
- Pappa Louis (hrs_41304746) | 4yo G | 134lb | OR 69 | draw 13 | jockey Jonny Peate | trainer Mark Loughnane (14d 1/7) | headgear - | wind surgery | last run 20 days | form 5222-4 | MARKET 3.0% | 09:00 median 26.00 | Matchbook 32.00
    comment: The risk is that he is yet to win and carries 134 lb.
    DATA: model 6.4% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 29 Oct Southwell (AW) 11f Standard 4/10 fig 63
    DATA against: Best recent form figure 63, 4 lb below field average; Recent figures 6 lb below its current mark (looks high in the weights); Lightly raced: 1 run in our data, so the model has little to go on
- King Kernow (hrs_43002533) | 4yo G | 132lb | OR 67 | draw 2 | jockey Taylor Fisher | trainer J. S. Moore (14d 0/4) | headgear - | last run 523 days | form 2/222- | MARKET 2.7% | 09:00 median 29.00 | Matchbook 40.00
    comment: King Kernow has finished second in each of his last four starts, yet he is still without a win, and he returns after 523 days off.
    DATA: model 5.3% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 523-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Velardo (hrs_57255135) | 4yo G | 136lb | OR 71 | draw 11 | jockey Dougie Costello | trainer Michael Gates (14d 0/0) | headgear - | last run 14 days | form 58-75 | MARKET 1.4% | 09:00 median 41.00 | Matchbook 100.00
    comment: Velardo is winless in his last four, finishing fifth last time out and a seventh two starts back, though he is back quickly after 14 days and has run over today's trip.
    DATA: model 2.4% | style Held up (led 5% of runs) | runs in data 2 | last 3: 8 Oct Southwell 11.1f Standard 7/7; 4 Nov Nottingham 14f Soft 5/10 fig 72
    DATA for: Best recent form figure 72, 5 lb above field average; Pace: a contested lead should suit its hold-up style
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Course: hold-up horses have won 0.7× their fair share at 12f here
- Marhaba The Champ (hrs_26718496) | 7yo G | 140lb | OR 75 | draw 12 | jockey Stevie Donohoe | trainer Sophie Leech (14d 0/1) | headgear h | wind surgery | last run 35 days | form 0-09R0 | MARKET 0.6% | 09:00 median 151.00 | Matchbook 210.00
    DATA: model 2.3% | style Held up (led 4% of runs) | runs in data 6 | last 3: 3 Jun Newton Abbot 16.8f Good To Soft 6/12; 23 Jun Newton Abbot 18.5f Good PU/10; 14 Oct Kempton (AW) 11f Standard / Slow 13/13 fig 48
    DATA for: Pace: a contested lead should suit its hold-up style
    DATA against: Best recent form figure 48, 19 lb below field average; Recent figures 27 lb below its current mark (looks high in the weights); Poor recent finishing positions; Carries 6 lb more than average; Aged 7, older than most of this field; Course: hold-up horses have won 0.7× their fair share at 12f here
