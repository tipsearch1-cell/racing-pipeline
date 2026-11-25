# Card review packet: Hereford, 2026-11-25

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
{"meeting": "hereford", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 12:31 Hereford | race_id rac_32305490750 | Octaga Security Systems Novices' Hurdle Race (GBB Race)
Hurdle | Class 4 | 2m3f147y | going Good | Turf | 8 runners | rating band - | age 4yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Moments Away (hrs_53148585) | 5yo G | 154lb | OR - | draw 0 | jockey James Best | trainer Martin Keighley (14d 1/12) | headgear t | last run 20 days | form 325-25 | MARKET 51.7% | 09:00 median 1.62 | Matchbook 1.79
    DATA: model 29.6% | style Prominent (led 29% of runs) | runs in data 5 | last 3: 11 Apr Aintree NH Flat 16.9f Good To Soft 5/20; 1 Oct Southwell Hurdle 20.4f Good 2/5; 5 Nov Newbury Hurdle 16.5f Good To Soft 5/9 fig 106
- North Gale (hrs_17394731277) | 4yo G | 153lb | OR - | draw 0 | jockey Ben Jones | trainer Ben Pauling (14d 6/36) | headgear - | last run 24 days | form 464-3 | MARKET 32.1% | 09:00 median 2.50 | Matchbook 3.00
    DATA: model 25.0% | style Held up (led 8% of runs) | runs in data 1 | last 3: 1 Nov Huntingdon Hurdle 16f Good 3/10 fig 102
    DATA for: Last-run finishing speed +2.9% vs that field (finished strongly)
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Teleleo (hrs_64938118) | 4yo G | 153lb | OR - | draw 0 | jockey Craig Nichol | trainer Martin Keighley (14d 1/12) | headgear - | last run 141 days | form 14 | MARKET 9.7% | 09:00 median 6.50 | Matchbook 13.00
    DATA: model 15.9% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 22 May Worcester NH Flat 16f Good 1/10; 7 Jul Uttoxeter NH Flat 15.8f Good 4/7
    DATA against: Returns from a 141-day break; Lightly raced: 2 runs in our data, so the model has little to go on; First run over hurdles in our data
- Jonjo Bravo (hrs_39996495) | 6yo G | 154lb | OR 98 | draw 0 | jockey Kielan Woods | trainer Shaun Lycett (14d 0/0) | headgear - | last run 336 days | form /676P- | MARKET 2.3% | 09:00 median 26.00 | Matchbook 60.00
    DATA: model 13.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 336-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Dance Ifyoucan (hrs_17394929447) | 5yo G | 154lb | OR - | draw 0 | jockey Ben Godfrey | trainer Kayley Woollacott (14d 2/10) | headgear t (1st time) | last run 21 days | form 21-FP | MARKET 1.8% | 09:00 median 34.00 | Matchbook 75.00
    DATA: model 7.5% | style Held up (led 8% of runs) | runs in data 1 | last 3: 4 Nov Chepstow Hurdle 16f Good To Soft PU/13
    DATA for: Trainer 20% wins (2/10), last 14 days; First-time headgear
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on; Pulled up in 1 of its last 1 jumps runs; Pace: steady gallop likely, hard to come from off the pace
- Lizziemouth (hrs_17392040337) | 4yo F | 146lb | OR - | draw 0 | jockey Tabitha Worsley | trainer Sarah-Jayne Davies (14d 0/6) | headgear - | last run 51 days | form 7 | MARKET 1.0% | 09:00 median 67.00 | Matchbook 130.00
    DATA: model 1.7% | style Held up (led 8% of runs) | runs in data 1 | last 3: 5 Oct Stratford NH Flat 16.3f Good To Firm 7/8
    DATA against: Last-run finishing speed -3.5% vs that field (faded); Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Jersey Tex (hrs_61910660) | 4yo G | 153lb | OR 55 | draw 0 | jockey Stan Sheppard | trainer Matt Sheppard (14d 0/3) | headgear - | last run 13 days | form 8P-77 | MARKET 0.8% | 09:00 median 81.00 | Matchbook 160.00
    DATA: model 4.8% | style Midfield (led 8% of runs) | runs in data 4 | last 3: 9 Mar Stratford Hurdle 18.7f Soft PU/6; 29 Oct Stratford Hurdle 16.5f Good To Soft 7/10; 12 Nov Hereford Hurdle 16f Good To Firm 7/12
    DATA against: Last-run finishing speed -2.5% vs that field (faded); Poor recent finishing positions; Pulled up in 1 of its last 3 jumps runs
- Maria's Joy (hrs_46547193) | 5yo M | 147lb | OR - | draw 0 | jockey Joe Anderson(3) | trainer Grace Harris (14d 0/9) | headgear - | last run 13 days | form 0/7-99 | MARKET 0.6% | 09:00 median 101.00 | Matchbook 210.00
    DATA: model 1.9% | style Held up (led 5% of runs) | runs in data 2 | last 3: 29 Oct Stratford Hurdle 16.5f Good To Soft 9/9; 12 Nov Hereford Hurdle 16f Good To Firm 9/12
    DATA against: Trainer 0 wins from 9 runs, last 14 days; Last-run finishing speed -4.5% vs that field (faded); Lightly raced: 2 runs in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace

## 1:01 Hereford | race_id rac_32305492687 | Herefordshire Community Foundation Novices' Hurdle Race (GBB Race)
Hurdle | Class 4 | 2m0f53y | going Good | Turf | 11 runners | rating band - | age 4yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Saint Argente (hrs_62941109) | 4yo G | 154lb | OR - | draw 0 | jockey Sam Twiston-Davies | trainer Warren Greatrex (14d 6/24) | headgear h | wind surgery | last run 25 days | form 1-1 | MARKET 61.9% | 09:00 median 1.35 | Matchbook 1.46
    DATA: model 23.9% | style Held up (led 5% of runs) | runs in data 2 | last 3: 26 Mar Warwick NH Flat 16f Good 1/11; 31 Oct Ascot NH Flat 15.5f Good To Firm 1/9 fig 113
    DATA for: Best recent form figure 113, 13 lb above field average; Trainer 25% wins (6/24), last 14 days; Last-run finishing speed +6.3% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; First run over hurdles in our data; Pace: steady gallop likely, hard to come from off the pace
- Legend d'Airy (hrs_62908475) | 5yo G | 154lb | OR - | draw 0 | jockey Ben Jones | trainer Ben Pauling (14d 6/36) | headgear - | last run 29 days | form 2-36 | MARKET 20.2% | 09:00 median 3.50 | Matchbook 5.20
    DATA: model 13.8% | style Midfield (led 29% of runs) | runs in data 3 | last 3: 25 Mar Hereford NH Flat 16.2f Good 2/9; 9 May Warwick NH Flat 16f Good 3/5; 27 Oct Bangor-on-Dee Hurdle 16.5f Good 6/11 fig 100
    DATA for: Good recent finishing positions
- Criminal (hrs_51735943) | 4yo G | 154lb | OR - | draw 0 | jockey Kielan Woods | trainer Fergal O'Brien (14d 4/29) | headgear - | last run 51 days | form - | MARKET 5.9% | 09:00 median 9.75 | Matchbook 25.00
    DATA: model 9.7% | style Held up (led 8% of runs) | runs in data 9 | last 3: 10 Jun Kempton Flat 8f Standard To Slow 7/11; 14 Jun Salisbury Flat 9.9f Good 2/10; 5 Oct Wolverhampton Flat 9.5f Standard 11/11
    DATA against: Last-run finishing speed -4.6% vs that field (faded); First run over hurdles in our data; Pace: steady gallop likely, hard to come from off the pace
- Sharu (hrs_59928645) | 5yo G | 154lb | OR 105 | draw 0 | jockey Sean Houlihan | trainer Carroll Gray (14d 0/0) | headgear - | last run 47 days | form 0-6224 | MARKET 3.2% | 09:00 median 21.00 | Matchbook 38.00
    DATA: model 20.5% | style Prominent (led 4% of runs) | runs in data 5 | last 3: 15 Jun Kilbeggan Hurdle 15.9f Good 2/12; 21 Jul Ballinrobe Hurdle 17.4f Good 2/13; 9 Oct Chepstow Hurdle 16.1f Good To Soft 4/10
    DATA for: Good recent finishing positions
- Lucky Bailly (hrs_59216318) | 5yo G | 154lb | OR - | draw 0 | jockey James Best | trainer Martin Keighley (14d 1/12) | headgear - | last run 27 days | form 7P-3P | MARKET 3.0% | 09:00 median 21.00 | Matchbook 40.00
    DATA: model 5.1% | style Prominent (led 4% of runs) | runs in data 3 | last 3: 26 Feb Taunton NH Flat 16.5f Good To Soft PU/12; 7 Oct Worcester NH Flat 16f Good 3/10; 29 Oct Ffos Las Hurdle 20f Heavy PU/11
    DATA against: Pulled up in 1 of its last 1 jumps runs
- Trojan Truth (hrs_29945027) | 7yo G | 154lb | OR - | draw 0 | jockey Ben Poste | trainer Ed de Giles (14d 0/2) | headgear - | last run 24 days | form 6 | MARKET 1.6% | 09:00 median 41.00 | Matchbook 85.00
    DATA: model 3.1% | style Held up (led 4% of runs) | runs in data 10 | last 3: 18 Sep Wolverhampton Flat 12.2f Standard 5/7; 28 Sep Wolverhampton Flat 14f Standard 6/10; 1 Nov Huntingdon Hurdle 16f Good 6/10 fig 86
    DATA against: Best recent form figure 86, 14 lb below field average; Pace: steady gallop likely, hard to come from off the pace
- Soizick (hrs_47531582) | 6yo M | 147lb | OR - | draw 0 | jockey Adam Wedge | trainer Henry Oliver (14d 0/6) | headgear - | last run 726 days | form 5/ | MARKET 1.2% | 09:00 median 51.00 | Matchbook 120.00
    DATA: model 4.9% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 726-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Desiderata (hrs_40095517) | 6yo G | 154lb | OR - | draw 0 | jockey Ned Fox(3) | trainer Thomas Faulkner (14d 0/7) | headgear - | last run 41 days | form 60/ | MARKET 1.2% | 09:00 median 51.00 | Matchbook 130.00
    DATA: model 10.9% | style Prominent (led 4% of runs) | runs in data 12 | last 3: 26 Aug Wolverhampton Flat 8.6f Standard 5/12; 27 Sep Ffos Las Flat 8f Soft 7/10; 15 Oct Southwell (AW) Flat 8f Standard 12/14
    DATA against: Last-run finishing speed -4.0% vs that field (faded); First run over hurdles in our data
- Himayta (hrs_17393377463) | 4yo G | 154lb | OR - | draw 0 | jockey David Noonan | trainer Henry Oliver (14d 0/6) | headgear - | last run 49 days | form 7 | MARKET 0.8% | 09:00 median 101.00 | Matchbook 190.00
    DATA: model 3.6% | style Unknown | runs in data 1 | last 3: 7 Oct Worcester NH Flat 16f Good 7/10
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Dressed Overall (hrs_17394593601) | 4yo G | 154lb | OR - | draw 0 | jockey Beau Morgan(5) | trainer Faye Bramley (14d 1/16) | headgear - | last run 13 days | form 76 | MARKET 0.7% | 09:00 median 81.00 | Matchbook 210.00
    DATA: model 3.4% | style Held up (led 5% of runs) | runs in data 2 | last 3: 29 Oct Stratford Hurdle 16.5f Good To Soft 7/9; 12 Nov Hereford Hurdle 16f Good To Firm 6/12
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Lady of The Isles (hrs_45865897) | 4yo F | 147lb | OR - | draw 0 | jockey Philip Armson(3) | trainer Sarah-Jayne Davies (14d 0/6) | headgear - | last run 30 days | form 67 | MARKET 0.5% | 09:00 median 201.00 | Matchbook 300.00
    DATA: model 1.3% | style Held up (led 3% of runs) | runs in data 6 | last 3: 25 Jul Salisbury Flat 8f Good To Firm 6/6; 5 Oct Stratford Hurdle 16.3f Good To Firm 6/6; 26 Oct Hereford Hurdle 16f Good To Firm 7/12
    DATA against: Last-run finishing speed -11.2% vs that field (faded); Poor recent finishing positions; Pace: steady gallop likely, hard to come from off the pace

## 1:31 Hereford | race_id rac_32305494624 | Castle Sychrov Novices' Handicap Steeple Chase
Chase | Class 5 | 2m0f8y | going Good | Turf | 7 runners | rating band 0-100 | age 4yo+
DATA pace: Strong pace - 3 habitual front-runners (Onehundredneighty, Prairie Queen, Monark Wood). A contested lead should set things up for horses coming from behind.
- Onehundredneighty (hrs_41814171) | 6yo G | 166lb | OR 98 | draw 0 | jockey Ben Jones | trainer Ben Pauling (14d 6/36) | headgear p (1st time) | last run 44 days | form 5-4212 | MARKET 43.5% | 09:00 median 2.00 | Matchbook 2.24
    comment: Onehundredneighty has finished second last time out, with a win two starts back and another second three starts back, and he has run over today's trip and going before. The one risk is a 44-day break, with 166 lb to carry.
    DATA: model 34.4% | style Leader (led 29% of runs) | runs in data 6 | last 3: 28 Aug Fontwell Hurdle 19.1f Good 2/7; 25 Sep Worcester Chase 16.5f Good 1/9; 12 Oct Worcester Chase 20f Good 2/9
    DATA for: Official rating 98, 7 lb above field average; Last-run finishing speed +4.3% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions; First-time headgear
    DATA against: Carries 9 lb more than average; Pace: likely to be taken on for the lead
- Prairie Queen (hrs_37702294) | 6yo M | 145lb | OR 77 | draw 0 | jockey Sean Houlihan | trainer Susan Gardner (14d 1/2) | headgear t | last run 61 days | form 3-1352 | MARKET 14.3% | 09:00 median 6.00 | Matchbook 7.00
    comment: Second last time out, and a winner four starts back, but she has been beaten since and returns after 61 days off, carrying 145 lb.
    DATA: model 12.2% | style Leader (led 43% of runs) | runs in data 9 | last 3: 17 Jun Worcester Chase 16.5f Good 3/9; 7 Jul Uttoxeter Chase 16f Good 5/10; 25 Sep Worcester Chase 16.5f Good 2/9
    DATA for: Last-run finishing speed +2.5% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions; Carries 12 lb less than average
    DATA against: Official rating 77, 14 lb below field average; Pace: likely to be taken on for the lead
- Mavis Pike (hrs_33302654) | 7yo M | 163lb | OR 95 | draw 0 | jockey Sam Twiston-Davies | trainer Nigel & Willy Twiston-Davies (14d 4/25) | headgear - | last run 11 days | form FU-325 | MARKET 11.9% | 09:00 median 7.50 | Matchbook 8.00
    comment: The main risk is 163 lb, a hefty burden off an official 95.
    DATA: model 8.6% | style Held up (led 4% of runs) | runs in data 3 | last 3: 6 Oct Huntingdon Chase 19.9f Good 3/4; 26 Oct Hereford Hurdle 16f Good To Firm 2/6 fig 101; 14 Nov Windsor Hurdle 20f Good 5/11 fig 92
    DATA for: Recent figures 6 lb above its current mark (looks well handicapped); Good recent finishing positions; Pace: a contested lead should suit its hold-up style
    DATA against: Carries 6 lb more than average
- Hans Lippershey (hrs_51735894) | 5yo G | 167lb | OR 99 | draw 0 | jockey Ciaran Gethings | trainer Ben Case (14d 0/5) | headgear - | wind surgery | last run 24 days | form 4024-6 | MARKET 11.3% | 09:00 median 7.50 | Matchbook 9.00
    comment: Hans Lippershey is yet to win in his last five, but a second three starts back and a fourth two runs ago show he's competitive, and he returns fresh after 24 days having run over today's trip and going.
    DATA: model 12.6% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 13 Mar Fakenham Hurdle 16f Good To Soft 2/5; 14 Apr Market Rasen Hurdle 18.6f Good 4/9; 1 Nov Worcester Chase 16.5f Good To Soft 6/10 fig 93
    DATA for: Official rating 99, 8 lb above field average
    DATA against: Recent figures 6 lb below its current mark (looks high in the weights); Carries 10 lb more than average
- Lheur de Gloire (hrs_58412165) | 5yo G | 168lb | OR 100 | draw 0 | jockey Beau Morgan(5) | trainer Ben Pauling (14d 6/36) | headgear t | last run 162 days | form 66-414 | MARKET 11.2% | 09:00 median 8.00 | Matchbook 8.60
    comment: The main risk is a 162-day absence under 168 lb.
    DATA: model 20.3% | style Held up (led 3% of runs) | runs in data 5 | last 3: 11 May Southwell Hurdle 15.8f Good 4/13; 28 May Market Rasen Chase 17.2f Good 1/5; 16 Jun Stratford Chase 17f Good 4/7
    DATA for: Official rating 100, 9 lb above field average; Has won at this trip or further; Pace: a contested lead should suit its hold-up style
    DATA against: Carries 11 lb more than average; Returns from a 162-day break
- Monark Wood (hrs_58099510) | 4yo G | 145lb | OR 85 | draw 0 | jockey Freddie Mitchell | trainer Max Comley (14d 2/11) | headgear t | wind surgery | last run 49 days | form 0274-5 | MARKET 6.6% | 09:00 median 13.00 | Matchbook 15.50
    comment: Monark Wood is winless in his last five, with a fifth last time out and a seventh three starts back, and he returns after 49 days off.
    DATA: model 6.9% | style Leader (led 29% of runs) | runs in data 3 | last 3: 1 Mar Huntingdon Hurdle 15.8f Good To Soft 7/8; 1 Apr Sedgefield Hurdle 19.9f Good 4/6; 7 Oct Worcester Hurdle 16f Good 5/10
    DATA for: Carries 12 lb less than average
    DATA against: Official rating 85, 6 lb below field average; First run over fences in our data; Pace: likely to be taken on for the lead
- Mystic Wind (hrs_65414720) | 4yo G | 145lb | OR 85 | draw 0 | jockey Philip Armson(3) | trainer Sarah-Jayne Davies (14d 0/6) | headgear h | last run 79 days | form 57746 | MARKET 1.0% | 09:00 median 67.00 | Matchbook 160.00
    comment: Mystic Wind is winless in his last five, finishing sixth last time out and a fourth two starts back, though he has run over today's trip and going before.
    DATA: model 5.1% | style Held up (led 4% of runs) | runs in data 5 | last 3: 7 Jul Uttoxeter Hurdle 15.8f Good 7/10; 19 Jul Stratford Hurdle 18.7f Good To Firm 4/7; 7 Sep Newton Abbot Hurdle 21.6f Good 6/8
    DATA for: Carries 12 lb less than average; Pace: a contested lead should suit its hold-up style
    DATA against: Official rating 85, 6 lb below field average; First run over fences in our data

## 2:07 Hereford | race_id rac_32305496561 | Angel Cybersecurity Handicap Hurdle Race
Hurdle | Class 5 | 2m3f147y | going Good | Turf | 11 runners | rating band 0-100 | age 3yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- God of Fire (hrs_31996209) | 6yo G | 167lb | OR 97 | draw 0 | jockey Richie McLernon | trainer Jonjo & A.J. O'Neill (14d 5/35) | headgear - | last run 30 days | form 142553 | MARKET 14.1% | 09:00 median 6.00 | Matchbook 6.60 | CHECK (skip line 5.70)
    comment: God of Fire arrives in solid recent form, third last time out and a second four starts back, and he has run over today's trip and going before.
    DATA: model 10.7% | style Prominent (led 23% of runs) | runs in data 6 | last 3: 18 Sep Newton Abbot Hurdle 16.8f Good 5/11; 5 Oct Stratford Hurdle 18.7f Good To Firm 5/6; 26 Oct Hereford Hurdle 19.5f Good To Firm 3/12 fig 99
    DATA for: Best recent form figure 99, 12 lb above field average; Official rating 97, 7 lb above field average; Last-run finishing speed +3.6% vs that field (finished strongly)
    DATA against: Carries 9 lb more than average
- Cawthorne Cracker (hrs_33036003) | 7yo G | 159lb | OR 89 | draw 0 | jockey Toby Wynne | trainer Oliver Greenall & Josh Guerriero (14d 2/13) | headgear tp | last run 29 days | form 562121 | MARKET 12.2% | 09:00 median 5.50 | Matchbook 9.40
    comment: Cawthorne Cracker arrives in cracking form, a winner last time out and a second two starts back, and he has run over today's trip and going before.
    DATA: model 19.9% | style Prominent (led 3% of runs) | runs in data 9 | last 3: 16 Sep Kelso Hurdle 18.1f Good To Firm 1/8; 29 Sep Sedgefield Hurdle 16.8f Good 2/7; 27 Oct Newcastle Hurdle 17f Good 1/10 fig 89
    DATA for: Last-run finishing speed +2.3% vs that field (finished strongly); Good recent finishing positions
- Churchman (hrs_29906555) | 8yo G | 149lb | OR 79 | draw 0 | jockey Jack Hogan | trainer Alastair Ralph (14d 0/7) | headgear p | last run 27 days | form 23-621 | MARKET 11.1% | 09:00 median 7.50 | Matchbook 8.40
    comment: Fresh enough after 27 days, he has run over today's trip and going, which is the best case for him.
    DATA: model 9.5% | style Prominent (led 8% of runs) | runs in data 8 | last 3: 10 May Ludlow Hurdle 23.8f Good 6/8; 28 May Worcester Hurdle 20f Good 2/9; 29 Oct Stratford Hurdle 18.5f Good To Soft 1/11 fig 78
    DATA for: Good recent finishing positions; Carries 9 lb less than average
    DATA against: Best recent form figure 78, 9 lb below field average; Official rating 79, 11 lb below field average
- Knighton (hrs_57223124) | 4yo G | 168lb | OR 99 | draw 0 | jockey Ben Smith(7) | trainer Oliver Greenall & Josh Guerriero (14d 2/13) | headgear t (1st time) | last run 28 days | form 42-235 | MARKET 10.8% | 09:00 median 8.00 | Matchbook 8.60
    comment: Knighton has hit the frame in three of his last five, including a second and a third in his previous two before a fifth last time out, and he's had 28 days to recover while having run on today's going before. The risk is 168 lb, a hefty burden for a gelding yet to win in that spell.
    DATA: model 9.2% | style Prominent (led 5% of runs) | runs in data 6 | last 3: 25 May Huntingdon Hurdle 15.8f Good To Firm 2/2; 8 Oct Market Rasen Hurdle 16.6f Good 3/6; 28 Oct Huntingdon Hurdle 16f Good 5/9 fig 97
    DATA for: Best recent form figure 97, 10 lb above field average; Official rating 99, 9 lb above field average; Good recent finishing positions; First-time headgear
    DATA against: Carries 10 lb more than average
- An Buachaill Rua (hrs_46233873) | 6yo G | 161lb | OR 91 | draw 0 | jockey Sean Houlihan | trainer Sheila Lewis (14d 1/7) | headgear - | last run 22 days | form 512F-5 | MARKET 9.6% | 09:00 median 9.00 | Matchbook 9.60
    comment: An Buachaill Rua showed he can win four starts back and was second three runs ago, but he was only fifth last time and fell two starts back, so consistency is a question. He has run over today's trip and going, and 22 days' rest is fine, though 161 lb is a hefty burden.
    DATA: model 9.2% | style Midfield (led 4% of runs) | runs in data 5 | last 3: 21 Mar Bangor-on-Dee Hurdle 23.1f Good 2/10; 12 Apr Ffos Las Hurdle 23.9f Good To Soft F/14; 3 Nov Warwick Hurdle 21f Good 5/10 fig 84
    DATA for: Has won at this trip or further
    DATA against: Recent figures 7 lb below its current mark (looks high in the weights); Fell or unseated in 1 of its last 5 jumps runs
- Little Pi (hrs_32597831) | 8yo G | 157lb | OR 87 | draw 0 | jockey Toby McCain-Mitchell(3) | trainer Sam Allwood (14d 1/2) | headgear p | last run 27 days | form 133-78 | MARKET 9.4% | 09:00 median 9.35 | Matchbook 9.80
    comment: Little Pi has slipped to an eighth last time out and a seventh two starts back, though he won five starts back and was third in the two runs after that, and he has run over today's trip and going.
    DATA: model 7.6% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 30 Mar Ludlow Hurdle 21.2f Good 3/6; 11 Oct Chepstow Hurdle 19.5f Good To Soft 7/13; 29 Oct Stratford Hurdle 18.5f Good To Soft 8/11 fig 82
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 82, 5 lb below field average
- Wistmans Prince (hrs_40942090) | 6yo G | 153lb | OR 83 | draw 0 | jockey Conor O'Farrell | trainer Kerry Lee (14d 1/6) | headgear tp (1st time) | last run 19 days | form 5F46-8 | MARKET 9.3% | 09:00 median 8.50 | Matchbook 11.00
    comment: Wistmans Prince is yet to win in his last five, with an eighth last time out following a sixth and a fourth, but he has run over today's trip and going and is back after 19 days.
    DATA: model 4.8% | style Held up (led 8% of runs) | runs in data 1 | last 3: 6 Nov Fontwell Hurdle 17.5f Good 8/10
    DATA for: First-time headgear
    DATA against: Official rating 83, 7 lb below field average; Last-run finishing speed -4.0% vs that field (faded); Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Gone In Sixty (hrs_30245698) | 9yo G | 151lb | OR 81 | draw 0 | jockey Bryan Carver | trainer Alex Hales (14d 0/7) | headgear - | last run 22 days | form 341552 | MARKET 8.4% | 09:00 median 10.25 | Matchbook 11.00
    comment: Gone In Sixty was beaten into second last time out, but two fifths before that and a single win four starts back make him hard to fancy, and he carries 151 lb. On the plus side, he has run over today's trip and going, and he is fresh enough after 22 days.
    DATA: model 8.0% | style Held up (led 3% of runs) | runs in data 10 | last 3: 1 Oct Southwell Chase 20.4f Good 5/6; 17 Oct Stratford Chase 22.5f Good 5/7; 3 Nov Lingfield Hurdle 19.5f Good 2/9 fig 84
    DATA for: Last-run finishing speed +2.8% vs that field (finished strongly); Has won at this trip or further; Carries 7 lb less than average
    DATA against: Official rating 81, 9 lb below field average; Aged 9, older than most of this field; Pace: steady gallop likely, hard to come from off the pace
- V Power (hrs_31982321) | 6yo G | 156lb | OR 86 | draw 0 | jockey Tabitha Worsley | trainer Thomas Faulkner (14d 0/7) | headgear t | last run 21 days | form 97P/26 | MARKET 7.1% | 09:00 median 12.00 | Matchbook 13.50
    comment: V Power is winless in his last five, with a sixth last time out and a second two starts back the only real positives, and he has run over today's trip.
    DATA: model 5.4% | style Prominent (led 3% of runs) | runs in data 12 | last 3: 26 Aug Wolverhampton Flat 14f Standard 5/7; 11 Oct Chepstow Hurdle 19.5f Good To Soft 2/13; 4 Nov Chepstow Hurdle 19.5f Good To Soft 6/16 fig 73
    DATA against: Best recent form figure 73, 14 lb below field average; Recent figures 13 lb below its current mark (looks high in the weights)
- Isabella Islay (hrs_59710805) | 4yo F | 166lb | OR 97 | draw 0 | jockey Stan Sheppard | trainer James Standen (14d 0/0) | headgear t | last run 21 days | form 931-37 | MARKET 4.6% | 09:00 median 17.00 | Matchbook 22.00
    comment: The main risk is a seventh last time out, plus 166 lb to carry.
    DATA: model 8.7% | style Midfield (led 3% of runs) | runs in data 4 | last 3: 25 Mar Hereford Hurdle 19.7f Good 1/10; 13 May Newton Abbot Hurdle 18.5f Good 3/7; 4 Nov Chepstow Hurdle 19.5f Good To Soft 7/16
    DATA for: Official rating 97, 7 lb above field average; Has won at this trip or further; Good recent finishing positions
    DATA against: Last-run finishing speed -5.0% vs that field (faded); Carries 8 lb more than average
- Lucky Sevens (hrs_60818471) | 3yo G | 150lb | OR 98 | draw 0 | jockey Ben Poste | trainer Nikki Evans (14d 0/2) | headgear p | last run 13 days | form 21424 | MARKET 3.5% | 09:00 median 21.00 | Matchbook 32.00
    comment: Lucky Sevens arrives fit after 13 days, with a fourth last time out, a second two starts back and a win four starts back, and he has run on today's going before. The main risk is the 150 lb he carries.
    DATA: model 7.1% | style Prominent (led 3% of runs) | runs in data 16 | last 3: 4 Oct Uttoxeter Hurdle 15.8f Good 4/11; 17 Oct Stratford Hurdle 16.5f Good 2/7 fig 97; 12 Nov Hereford Hurdle 16f Good To Firm 4/9 fig 98
    DATA for: Best recent form figure 98, 11 lb above field average; Official rating 98, 8 lb above field average; Carries 8 lb less than average

## 2:37 Hereford | race_id rac_32305498498 | Cuban Pete Celebration Handicap Steeple Chase (GBB Race)
Chase | Class 4 | 3m1f44y | going Good | Turf | 5 runners | rating band 0-115 | age 4yo+
DATA pace: Lone leader - Edgewell is the only habitual front-runner and may be allowed an easy lead.
- Law of Supply (hrs_28824775) | 8yo G | 165lb | OR 112 | draw 0 | jockey Tom Bellamy | trainer Kim Bailey & Mat Nicholls (14d 7/22) | headgear ht | last run 23 days | form 4F2-22 | MARKET 33.1% | 09:00 median 2.69 | Matchbook 2.94
    comment: Three seconds in a row, the latest 23 days ago, make Law of Supply a consistent and fit-looking selection, and he has run over today's trip and going before. Trainer is in form with 7 from 22 lately, though he is yet to win in his last five and carries 165 lb.
    DATA: model 33.8% | style Held up (led 5% of runs) | runs in data 3 | last 3: 1 Apr Wincanton Chase 25.1f Good 2/5; 1 Oct Southwell Chase 24.3f Good 2/4; 2 Nov Southwell Chase 24.5f Good 2/8 fig 113
    DATA for: Best recent form figure 113, 11 lb above field average; Official rating 112, 9 lb above field average; Trainer 32% wins (7/22), last 14 days; Last-run finishing speed +2.3% vs that field (finished strongly); Good recent finishing positions
    DATA against: Carries 9 lb more than average
- My Bobby's Lass (hrs_38855719) | 7yo M | 148lb | OR 95 | draw 0 | jockey Toby Wynne | trainer Mel Rowley (14d 0/11) | headgear t | last run 29 days | form 16-641 | MARKET 31.1% | 09:00 median 2.75 | Matchbook 3.25
    comment: Won last time out and has two wins in her last five starts, so My Bobby's Lass arrives in good heart after 29 days off, and she has run over today's trip and going before.
    DATA: model 23.8% | style Held up (led 5% of runs) | runs in data 3 | last 3: 4 Sep Bangor-on-Dee Chase 20.3f Good 6/7; 1 Oct Southwell Chase 20.4f Good 4/6; 27 Oct Bangor-on-Dee Chase 24f Good To Soft 1/13 fig 89
    DATA for: Last-run finishing speed +8.6% vs that field (finished strongly); Carries 8 lb less than average
    DATA against: Best recent form figure 89, 13 lb below field average; Recent figures 6 lb below its current mark (looks high in the weights); Official rating 95, 8 lb below field average; Trainer 0 wins from 11 runs, last 14 days
- Doctor Midas (hrs_40805576) | 6yo G | 156lb | OR 103 | draw 0 | jockey Paul O'Brien | trainer Henrietta C Knight (14d 1/10) | headgear t | wind surgery | last run 11 days | form 3283-U | MARKET 20.7% | 09:00 median 4.42 | Matchbook 4.60
    comment: Doctor Midas has been in the frame twice in his last five, a third two starts back and a second four starts back, and he has run over today's trip and going. Back just 11 days after unseating last time, the main risk is the 156 lb he must carry.
    DATA: model 16.7% | style Unknown | runs in data 2 | last 3: 25 Feb Wincanton Chase 25.1f Good To Soft 3/5; 14 Nov Windsor Chase 22f Good UR/6
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Fell or unseated in 1 of its last 2 jumps runs
- Minella Blueway (hrs_29907108) | 8yo G | 168lb | OR 115 | draw 0 | jockey Adam Wedge | trainer Mrs C. Williams (14d 0/23) | headgear - | last run 17 days | form F27P-5 | MARKET 7.6% | 09:00 median 12.00 | Matchbook 13.00
    comment: The main risk is a yard without a winner in its last 23 runners.
    DATA: model 13.8% | style Prominent (led 29% of runs) | runs in data 5 | last 3: 26 Feb Ludlow Chase 23.8f Good To Soft 7/7; 14 Mar Uttoxeter Chase 34f Soft PU/16; 8 Nov Ffos Las Chase 24f Good 5/6 fig 103
    DATA for: Official rating 115, 12 lb above field average
    DATA against: Recent figures 12 lb below its current mark (looks high in the weights); Trainer 0 wins from 23 runs, last 14 days; Carries 12 lb more than average; Fell or unseated in 1 of its last 5 jumps runs; Pulled up in 1 of its last 5 jumps runs
- Edgewell (hrs_34003025) | 8yo G | 143lb | OR 90 | draw 0 | jockey Harry Reed | trainer Nick Scholfield (14d 1/12) | headgear b | last run 80 days | form 31163P | MARKET 7.5% | 09:00 median 12.00 | Matchbook 13.50
    comment: Edgewell was pulled up last time out and has been off for 80 days, which makes him hard to fancy, though he won four and five starts back and was third two starts back.
    DATA: model 11.8% | style Leader (led 63% of runs) | runs in data 14 | last 3: 15 Aug Perth Chase 23.8f Good 6/7; 28 Aug Fontwell Chase 21.6f Good 3/7; 6 Sep Fontwell Chase 26f Good PU/6
    DATA for: Has won at this trip or further; Carries 13 lb less than average; Pace: may get an uncontested lead
    DATA against: Official rating 90, 13 lb below field average; Pulled up in 1 of its last 5 jumps runs

## 3:07 Hereford | race_id rac_32305500435 | Hampden Agencies Mares' Handicap Hurdle Race
Hurdle | Class 5 | 2m0f53y | going Good | Turf | 11 runners | rating band 0-100 | age 3yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Saxons Pride (hrs_58566018) | 4yo F | 165lb | OR 96 | draw 0 | jockey Tom Bellamy | trainer Alan King (14d 2/20) | headgear - | last run 30 days | form 283-3 | MARKET 28.7% | 09:00 median 3.00 | Matchbook 3.25 | CHECK (skip line 2.85)
    comment: Saxons Pride arrives in sound form, third last time out and another third two starts back, with a second four runs ago, and she has run over today's trip and going before.
    DATA: model 14.1% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 31 Mar Bangor-on-Dee Hurdle 16.7f Good 3/7; 26 Oct Hereford Hurdle 16f Good To Firm 3/12 fig 100
    DATA for: Best recent form figure 100, 17 lb above field average; Recent figures 4 lb above its current mark (looks well handicapped); Official rating 96, 8 lb above field average; Last-run finishing speed +3.4% vs that field (finished strongly); Good recent finishing positions
    DATA against: Carries 11 lb more than average; Lightly raced: 2 runs in our data, so the model has little to go on
- Ghost Dancing (hrs_58566025) | 4yo F | 160lb | OR 91 | draw 0 | jockey Kielan Woods | trainer Alan King (14d 2/20) | headgear - | last run 203 days | form 43P-4 | MARKET 13.1% | 09:00 median 6.50 | Matchbook 7.20
    comment: Ghost Dancing was fourth last time out, though she was pulled up two starts back and returns after 203 days off, which leaves fitness a question.
    DATA: model 10.5% | style Held up (led 5% of runs) | runs in data 2 | last 3: 13 Mar Fakenham Hurdle 16f Good To Soft PU/5; 6 May Newton Abbot Hurdle 16.8f Good 4/8
    DATA against: Carries 6 lb more than average; Returns from a 203-day break; Lightly raced: 2 runs in our data, so the model has little to go on; Pulled up in 1 of its last 2 jumps runs; Pace: steady gallop likely, hard to come from off the pace
- Guildhall Graduate (hrs_56188965) | 3yo F | 142lb | OR 89 | draw 0 | jockey Charlie Price | trainer Katy Price (14d 0/1) | headgear - | last run 24 days | form 5443 | MARKET 11.0% | 09:00 median 7.50 | Matchbook 8.60
    comment: Guildhall Graduate is winless in her last four, though a third last time out, a fourth three starts back and another fourth two starts back show she's consistent, and she has run over today's trip and going.
    DATA: model 9.7% | style Prominent (led 5% of runs) | runs in data 9 | last 3: 7 Oct Worcester Hurdle 16f Good 4/8; 26 Oct Hereford Hurdle 16f Good To Firm 4/8 fig 65; 1 Nov Worcester Hurdle 16f Good To Soft 3/5 fig 75
    DATA for: Carries 12 lb less than average
    DATA against: Best recent form figure 75, 8 lb below field average; Recent figures 14 lb below its current mark (looks high in the weights)
- Stopherandgo (hrs_28824859) | 9yo M | 142lb | OR 70 | draw 0 | jockey Chad Bament(5) | trainer David Flood (14d 0/3) | headgear tp | last run 15 days | form P9-854 | MARKET 10.1% | 09:00 median 8.50 | Matchbook 9.40
    comment: Winless in her last five, Stopherandgo is hard to fancy, though a fourth last time out, a fifth two starts back and only 15 days since that run offer some encouragement.
    DATA: model 5.4% | style Midfield (led 29% of runs) | runs in data 12 | last 3: 21 Oct Worcester Hurdle 20f Good To Soft 8/10 fig 59; 1 Nov Huntingdon Hurdle 16f Good 5/5 fig 77; 10 Nov Huntingdon Hurdle 16f Good 4/6 fig 59
    DATA for: Recent figures 7 lb above its current mark (looks well handicapped); Carries 12 lb less than average
    DATA against: Best recent form figure 77, 6 lb below field average; Official rating 70, 18 lb below field average; Pulled up in 1 of its last 5 jumps runs; Aged 9, older than most of this field
- Ritaan (hrs_52418037) | 4yo F | 144lb | OR 75 | draw 0 | jockey Lorcan Murtagh | trainer Georgina Nicholls (14d 0/4) | headgear t (1st time) | last run 35 days | form 5P97-4 | MARKET 8.8% | 09:00 median 9.25 | Matchbook 11.50
    comment: Ritaan showed some promise when fourth last time out, and she has run over today's trip and going before, but she is winless in her last five and was only seventh and ninth in the two runs before that.
    DATA: model 4.7% | style Held up (led 5% of runs) | runs in data 5 | last 3: 28 Mar Stratford Hurdle 16.3f Good 9/11; 22 Apr Taunton Hurdle 19f Good 7/10; 21 Oct Fontwell Hurdle 21.5f Soft 4/7 fig 72
    DATA for: Carries 10 lb less than average; First-time headgear
    DATA against: Best recent form figure 72, 11 lb below field average; Official rating 75, 13 lb below field average; Pulled up in 1 of its last 5 jumps runs; Pace: steady gallop likely, hard to come from off the pace
- Thetype Istitle (hrs_61911752) | 4yo F | 164lb | OR 95 | draw 0 | jockey Stan Sheppard | trainer Tom Lacey (14d 2/12) | headgear t | last run 13 days | form 217933 | MARKET 7.3% | 09:00 median 10.00 | Matchbook 15.00
    comment: A ninth and a seventh before that are the one reservation, and she carries 164 lb.
    DATA: model 6.6% | style Prominent (led 4% of runs) | runs in data 5 | last 3: 23 Aug Worcester NH Flat 16f Good 9/10; 20 Sep Plumpton Hurdle 20.5f Good 3/6; 12 Nov Hereford Hurdle 16f Good To Firm 3/12 fig 83
    DATA for: Official rating 95, 7 lb above field average; Has won at this trip or further; Good recent finishing positions
    DATA against: Recent figures 12 lb below its current mark (looks high in the weights); Carries 10 lb more than average
- Silvereen (hrs_58196705) | 4yo F | 168lb | OR 99 | draw 0 | jockey Sam Twiston-Davies | trainer Henry Daly (14d 3/14) | headgear - | last run 30 days | form 773-16 | MARKET 5.4% | 09:00 median 15.00 | Matchbook 18.00
    comment: Silvereen won two starts back and was third the run before, so she knows how to get her head in front, and she has run over today's trip and going before.
    DATA: model 18.6% | style Prominent (led 23% of runs) | runs in data 4 | last 3: 19 Mar Ludlow Hurdle 15.8f Good 3/12; 10 May Ludlow Hurdle 15.8f Good 1/5; 26 Oct Hereford Hurdle 16f Good To Firm 6/6
    DATA for: Official rating 99, 11 lb above field average; Trainer 21% wins (3/14), last 14 days; Has won at this trip or further; Good recent finishing positions
    DATA against: Last-run finishing speed -4.4% vs that field (faded); Carries 14 lb more than average
- Adba (hrs_58283071) | 3yo F | 152lb | OR 99 | draw 0 | jockey Harry Kimber | trainer Faye Bramley (14d 1/16) | headgear t | last run 22 days | form 65150 | MARKET 5.0% | 09:00 median 17.00 | Matchbook 19.00
    comment: Adba won three starts back but has been a fifth and unplaced since, though a 22-day break and experience over today's trip and going give her a platform.
    DATA: model 10.1% | style Held up (led 5% of runs) | runs in data 8 | last 3: 26 Sep Market Rasen Hurdle 16.6f Good 1/9; 16 Oct Uttoxeter Hurdle 16f Good 5/10 fig 92; 3 Nov Warwick Hurdle 16f Good 10/11
    DATA for: Best recent form figure 92, 9 lb above field average; Official rating 99, 11 lb above field average; Has won at this trip or further
    DATA against: Recent figures 7 lb below its current mark (looks high in the weights); Last-run finishing speed -4.8% vs that field (faded); Pace: steady gallop likely, hard to come from off the pace
- Chloe's Courage (hrs_43730729) | 4yo F | 166lb | OR 97 | draw 0 | jockey Richie McLernon | trainer John Ryan (14d 0/0) | headgear - | last run 15 days | form 343 | MARKET 4.0% | 09:00 median 19.00 | Matchbook 27.00
    comment: Chloe's Courage arrives fit after 15 days, third last time out and with a third and a fourth before that, and has run over today's trip and going. Yet to win in her last three starts, she carries 166 lb, which is the main risk.
    DATA: model 12.4% | style Midfield (led 4% of runs) | runs in data 12 | last 3: 13 Oct Southwell Hurdle 15.8f Good 4/4; 2 Nov Chelmsford (AW) Flat 7f Standard 6/13 fig 51; 10 Nov Huntingdon Hurdle 16f Good 3/7 fig 98
    DATA for: Best recent form figure 98, 15 lb above field average; Official rating 97, 9 lb above field average
    DATA against: Carries 12 lb more than average
- Opticality (hrs_27236461) | 8yo M | 142lb | OR 73 | draw 0 | jockey David Noonan | trainer Mitchell Hunt & Tim Vaughan (14d 1/4) | headgear - | last run 22 days | form 6/466- | MARKET 3.7% | 09:00 median 23.00 | Matchbook 27.00
    comment: Opticality has finished sixth last time out, a sixth two starts back, a fourth three starts back and a sixth four starts back, so she is winless in her last four, though she has run over today's trip and going and returns after 22 days.
    DATA: model 4.9% | style Prominent (led 8% of runs) | runs in data 2 | last 3: 19 Oct Southwell (AW) Flat 11f Standard 7/9 fig 33; 3 Nov Wolverhampton (AW) Flat 12f Standard 7/11 fig 46
    DATA for: Carries 12 lb less than average
    DATA against: Official rating 73, 15 lb below field average; Lightly raced: 2 runs in our data, so the model has little to go on; First run over hurdles in our data
- Ashpriors (hrs_59710798) | 4yo F | 151lb | OR 82 | draw 0 | jockey Sean Houlihan | trainer Philip Hobbs & Johnson White (14d 2/16) | headgear h | last run 22 days | form 07F-8 | MARKET 3.1% | 09:00 median 26.00 | Matchbook 36.00
    comment: Ashpriors is hard to fancy, winless in her last four starts with an eighth last time out, a faller two starts back and a seventh three starts back.
    DATA: model 3.0% | style Held up (led 4% of runs) | runs in data 3 | last 3: 9 Mar Taunton Hurdle 16.5f Good 7/8; 23 Mar Wincanton Hurdle 15.2f Good F/12; 3 Nov Lingfield Hurdle 16f Good 8/9 fig 70
    DATA against: Best recent form figure 70, 13 lb below field average; Recent figures 12 lb below its current mark (looks high in the weights); Official rating 82, 6 lb below field average; Last-run finishing speed -2.2% vs that field (faded); Poor recent finishing positions; Fell or unseated in 1 of its last 3 jumps runs; Pace: steady gallop likely, hard to come from off the pace

## 3:37 Hereford | race_id rac_32305502372 | White Heron Open National Hunt Flat Race (Category 1 Elimination) (GBB Race)
NH Flat | Class 5 | 2m0f53y | going Good | Turf | 6 runners | rating band - | age 4-5yo
DATA pace: Unclear - Running styles known for only 1 of 6 runners.
- Slavetotherhythm (hrs_17395911953) | 4yo G | 156lb | OR - | draw 0 | jockey Tom Bellamy | trainer Alan King (14d 2/20) | headgear - | last run - days | form - | MARKET 45.5% | 09:00 median 1.83 | Matchbook 2.14
    comment: Slavetotherhythm is unexposed with no recorded form to go on, so this gelding's debut offers plenty of scope for improvement. He carries 156 lb, and his profile is a blank page worth watching.
    DATA: model 16.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Mikindaguy (hrs_17395690837) | 4yo G | 156lb | OR - | draw 0 | jockey Ben Jones | trainer Emma Lavelle (14d 3/21) | headgear - | last run - days | form - | MARKET 22.8% | 09:00 median 4.00 | Matchbook 4.10
    comment: Mikindaguy is unexposed, with no recorded form to go on, so this debut is a step into the unknown and he could well improve. He carries 156 lb.
    DATA: model 16.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Unbroken Spirit (hrs_17394791771) | 4yo G | 156lb | OR - | draw 0 | jockey Luke Scott(3) | trainer Dr Richard Newland (14d 1/11) | headgear t (1st time) | last run - days | form - | MARKET 13.8% | 09:00 median 6.50 | Matchbook 6.60
    comment: Unbroken Spirit is totally unexposed, with no recorded form to go on, so this debut is a step into the unknown for the gelding. He carries 156 lb, and any improvement is there to be found.
    DATA: model 16.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: First-time headgear
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- I Never Said (hrs_17394945092) | 5yo G | 156lb | OR - | draw 0 | jockey Kielan Woods | trainer John O'Shea (14d 1/3) | headgear - | last run 21 days | form 6 | MARKET 8.0% | 09:00 median 11.00 | Matchbook 12.00
    DATA: model 17.7% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 4 Nov Chepstow NH Flat 16f Good To Soft 6/13 fig 87
    DATA for: Last-run finishing speed +4.6% vs that field (finished strongly)
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Wings of Mori (hrs_17395102585) | 4yo G | 156lb | OR - | draw 0 | jockey Conor Ring | trainer Mrs C. Williams (14d 0/23) | headgear - | last run - days | form - | MARKET 6.4% | 09:00 median 15.00 | Matchbook 15.00
    comment: Wings of Mori is an unraced gelding with no recorded form to go on, so he's an unexposed type who could well improve. He carries 156 lb, though his yard is 0/23 in the last 14 days, which tempers things.
    DATA: model 16.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Trainer 0 wins from 23 runs, last 14 days; Lightly raced: 0 runs in our data, so the model has little to go on
- Persian Storm (hrs_17395977662) | 4yo G | 156lb | OR - | draw 0 | jockey Ben Poste | trainer Nikki Evans (14d 0/2) | headgear - | last run - days | form - | MARKET 3.4% | 09:00 median 26.00 | Matchbook 32.00
    comment: Persian Storm is an unexposed gelding with no recorded form to lean on, so he arrives open to improvement and a blank sheet to work from. He carries 156 lb on what looks a debut.
    DATA: model 16.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
