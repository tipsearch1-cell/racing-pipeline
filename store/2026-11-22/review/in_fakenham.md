# Card review packet: Fakenham, 2026-11-22

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
{"meeting": "fakenham", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 12:43 Fakenham | race_id rac_32305138216 | racingtv.com/freetrial - Last Day Mares' Handicap Hurdle Race
Hurdle | Class 4 | 2m0f3y | going Good | Turf | 5 runners | rating band 0-120 | age 3yo+
DATA pace: Even - Two likely leaders (Our Peggy, Mc'flo). A fair, even gallop is most likely.
- Our Peggy (hrs_57878156) | 5yo M | 161lb | OR 109 | draw 0 | jockey Dylan Johnston | trainer Joe Tizzard (14d 8/30) | headgear h | last run 32 days | form 642P-1 | MARKET 50.6% | 09:00 median 1.80 | Matchbook 1.88
    DATA: model 31.3% | style Leader (led 72% of runs) | runs in data 4 | last 3: 5 Mar Wincanton Hurdle 15.2f Good To Soft 2/13; 21 Mar Kelso Hurdle 16.2f Good To Soft PU/15; 21 Oct Worcester Hurdle 16f Good To Soft 1/9 fig 119
    DATA for: Best recent form figure 119, 16 lb above field average; Recent figures 10 lb above its current mark (looks well handicapped); Official rating 109, 6 lb above field average; Trainer 27% wins (8/30), last 14 days; Last-run finishing speed +4.7% vs that field (finished strongly); Has won at this trip or further
    DATA against: Pulled up in 1 of its last 4 jumps runs
- Hello Sweety (hrs_43826860) | 5yo M | 162lb | OR 110 | draw 0 | jockey Charlie Hammond | trainer Stuart Edmunds (14d 1/11) | headgear t | last run 27 days | form 1231P3 | MARKET 22.2% | 09:00 median 4.00 | Matchbook 4.40
    comment: Hello Sweety was third last time out, and she is a winner three starts back and six starts back, with a second five runs ago too, while she has run over today's trip and on the going before. Fresh enough after 27 days, though 162 lb is a hefty burden and the pulled-up effort two starts back is the one blemish.
    DATA: model 17.8% | style Held up (led 8% of runs) | runs in data 9 | last 3: 8 Sep Bangor-on-Dee Hurdle 16.7f Good 1/6; 17 Oct Stratford Hurdle 16.5f Good PU/6; 26 Oct Hereford Hurdle 16f Good To Firm 3/6 fig 106
    DATA for: Official rating 110, 7 lb above field average; Has won at this trip or further
    DATA against: Race comments mention jumping mistakes in 2 of its last 5 runs; Pulled up in 1 of its last 5 jumps runs
- Golden Falls (hrs_51024253) | 4yo F | 168lb | OR 116 | draw 0 | jockey Tom Cannon | trainer Lucy Wadham (14d 0/2) | headgear h | last run 266 days | form 27741- | MARKET 15.1% | 09:00 median 5.50 | Matchbook 7.20
    comment: The one worry is a 266-day layoff, with 168 lb to carry adding to the test.
    DATA: model 20.5% | style Midfield (led 8% of runs) | runs in data 2 | last 3: 15 Jan Ludlow Hurdle 15.8f Good To Soft 4/9; 1 Mar Huntingdon Hurdle 15.8f Good To Soft 1/8
    DATA for: Official rating 116, 13 lb above field average; Last-run finishing speed +6.0% vs that field (finished strongly); Has won at this trip or further
    DATA against: Carries 10 lb more than average; Returns from a 266-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- Dancing Dame (hrs_36123108) | 7yo M | 156lb | OR 104 | draw 0 | jockey Jonathan Burke | trainer James Owen (14d 3/39) | headgear h | last run 12 days | form 6-2514 | MARKET 9.9% | 09:00 median 9.00 | Matchbook 10.50
    comment: Dancing Dame bounced back from a fifth to win two starts back before finishing fourth last time out just 12 days ago, and she has run over today's trip and going before. The main risk is the 156 lb she must carry.
    DATA: model 23.7% | style Prominent (led 38% of runs) | runs in data 4 | last 3: 12 Jun Newton Abbot Hurdle 16.8f Good 5/9; 6 Oct Huntingdon Hurdle 19.6f Good 1/5; 10 Nov Huntingdon Hurdle 16f Good 4/7 fig 101
    DATA for: Has won at this trip or further
- Mc'flo (hrs_52021319) | 5yo M | 142lb | OR 78 | draw 0 | jockey Jack Quinlan | trainer Anthony Carson (14d 0/0) | headgear - | last run 21 days | form 4P5842 | MARKET 2.1% | 09:00 median 41.00 | Matchbook 48.00
    comment: Mc'flo is winless in her last six, though a second last time out, 21 days ago, is a genuine plus, and she has run over today's trip and going before.
    DATA: model 6.6% | style Leader (led 63% of runs) | runs in data 13 | last 3: 5 Sep Stratford Hurdle 22f Good 8/9; 19 Oct Plumpton Hurdle 16f Good 4/6 fig 56; 1 Nov Huntingdon Hurdle 16f Good 2/5 fig 86
    DATA for: Recent figures 8 lb above its current mark (looks well handicapped); Carries 16 lb less than average
    DATA against: Best recent form figure 86, 17 lb below field average; Official rating 78, 25 lb below field average; Pulled up in 1 of its last 5 jumps runs

## 1:13 Fakenham | race_id rac_32305140153 | Royal British Legion Poppy Appeal 2026 Handicap Steeple Chase
Chase | Class 5 | 2m0f59y | going Good | Turf | 4 runners | rating band 0-100 | age 4yo+
DATA pace: Lone leader - Applejack Poet is the only habitual front-runner and may be allowed an easy lead.
- Gambie Tiep (hrs_28400099) | 10yo G | 154lb | OR 83 | draw 0 | jockey Sean Bowen | trainer Olly Murphy (14d 10/52) | headgear p | last run 28 days | form 543P/5 | MARKET 30.3% | 09:00 median 3.00 | Matchbook 3.25
    comment: The main risk is that he is winless in his last five and was pulled up two starts back.
    DATA: model 19.0% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 25 Oct Market Rasen Chase 19f Good To Soft 5/5 fig 76
    DATA against: Best recent form figure 76, 8 lb below field average; Recent figures 7 lb below its current mark (looks high in the weights); Lightly raced: 1 run in our data, so the model has little to go on
- Applejack Poet (hrs_30541329) | 9yo G | 155lb | OR 84 | draw 0 | jockey Rian Corcoran(5) | trainer Barry Murphy (14d 0/5) | headgear p | last run 19 days | form P8F321 | MARKET 28.4% | 09:00 median 3.06 | Matchbook 3.60
    comment: Applejack Poet arrives in cracking nick, a winner last time out, then a second two starts back and a third three starts back, with just 19 days since that success. He has run over today's trip and going, but 155 lb is a hefty burden to carry.
    DATA: model 36.6% | style Leader (led 72% of runs) | runs in data 10 | last 3: 25 Sep Worcester Chase 16.5f Good 3/9; 17 Oct Stratford Chase 17f Good 2/4 fig 75; 3 Nov Sedgefield Chase 16.5f Good 1/8 fig 84
    DATA for: Last-run finishing speed +2.1% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions; Pace: may get an uncontested lead
    DATA against: Fell or unseated in 1 of its last 5 jumps runs
- Belle Montrose (hrs_34665610) | 7yo M | 168lb | OR 97 | draw 0 | jockey Kevin Brogan | trainer Samuel Drinkwater (14d 0/6) | headgear tp | last run 32 days | form 1223-2 | MARKET 24.5% | 09:00 median 3.75 | Matchbook 3.95
    comment: Belle Montrose has finished in the frame in all five recent runs, a second last time out following a third two starts back, and she has run over today's trip and on this going before.
    DATA: model 24.6% | style Held up (led 3% of runs) | runs in data 5 | last 3: 13 Mar Fakenham Chase 21.2f Good To Soft 2/4; 6 Apr Hereford Chase 20.9f Good 3/4; 21 Oct Fontwell Chase 18f Soft 2/5 fig 93
    DATA for: Best recent form figure 93, 9 lb above field average; Official rating 97, 12 lb above field average; Has won at this trip or further; Good recent finishing positions
    DATA against: Carries 12 lb more than average
- Getaway Jewel (hrs_20456415) | 12yo G | 147lb | OR 76 | draw 0 | jockey Alice Stevens(3) | trainer Micky Hammond & Becky Smith (14d 1/18) | headgear - | last run 19 days | form 221447 | MARKET 16.8% | 09:00 median 5.50 | Matchbook 5.80
    comment: Getaway Jewel has a solid profile, having won four starts back with a pair of seconds before that, and he has run over today's trip and going. Fresh enough after 19 days, he must bounce back from a seventh last time out, and 147 lb is a lot to carry.
    DATA: model 19.8% | style Midfield (led 3% of runs) | runs in data 8 | last 3: 31 Aug Cartmel Chase 17.3f Good To Soft 4/6; 9 Sep Sedgefield Chase 16.4f Good 4/8; 3 Nov Sedgefield Chase 16.5f Good 7/8
    DATA for: Has won at this trip or further; Carries 9 lb less than average
    DATA against: Official rating 76, 9 lb below field average; Last-run finishing speed -7.0% vs that field (faded)

## 1:43 Fakenham | race_id rac_32305142090 | Get A Free Trial Of Racing TV Now Maiden Hurdle Race (GBB Race)
Hurdle | Class 4 | 2m4f1y | going Good | Turf | 7 runners | rating band - | age 4yo+
DATA pace: Lone leader - Scotto is the only habitual front-runner and may be allowed an easy lead.
- Scotto (hrs_64779799) | 5yo G | 158lb | OR - | draw 0 | jockey Jonathan Burke | trainer James Owen (14d 3/39) | headgear t | last run 25 days | form 113 | MARKET 33.9% | 09:00 median 2.63 | Matchbook 2.82
    DATA: model 19.2% | style Leader (led 29% of runs) | runs in data 3 | last 3: 26 May Plumpton NH Flat 17.8f Good 1/6; 19 Jun Market Rasen NH Flat 16.6f Good 1/6; 28 Oct Huntingdon Hurdle 19.5f Good 3/6 fig 110
    DATA for: Best recent form figure 110, 11 lb above field average; Good recent finishing positions; Pace: may get an uncontested lead
- Eustace Grenier (hrs_58686873) | 5yo G | 158lb | OR 108 | draw 0 | jockey Sean Bowen | trainer Olly Murphy (14d 10/52) | headgear - | last run 23 days | form 43-450 | MARKET 30.0% | 09:00 median 2.88 | Matchbook 3.25
    DATA: model 27.5% | style Midfield (led 4% of runs) | runs in data 6 | last 3: 22 May Worcester Hurdle 16f Good 4/10; 7 Oct Worcester Hurdle 16f Good 5/12; 30 Oct Uttoxeter Hurdle 20f Good 10/15 fig 97
- Claim The Throne (hrs_39826857) | 6yo G | 158lb | OR - | draw 0 | jockey Dylan Johnston | trainer Joe Tizzard (14d 8/30) | headgear - | last run 385 days | form 561/P- | MARKET 19.5% | 09:00 median 4.50 | Matchbook 5.00
    DATA: model 9.7% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 27% wins (8/30), last 14 days
    DATA against: Returns from a 385-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Mister Realistic (hrs_17394541451) | 4yo G | 157lb | OR - | draw 0 | jockey Tom Cannon | trainer Lucy Wadham (14d 0/2) | headgear - | last run 17 days | form 2-8 | MARKET 8.4% | 09:00 median 11.00 | Matchbook 11.50
    DATA: model 13.5% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 5 Nov Newbury NH Flat 16.5f Good To Soft 8/11 fig 99
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- La Trinite (hrs_49110537) | 4yo F | 150lb | OR - | draw 0 | jockey Jack Quinlan | trainer Neil King (14d 0/5) | headgear - | last run 17 days | form 36 | MARKET 5.8% | 09:00 median 15.00 | Matchbook 17.50
    DATA: model 5.8% | style Midfield (led 3% of runs) | runs in data 8 | last 3: 19 Oct Bath Flat 17f Good To Soft 1/11 fig 53; 26 Oct Kempton (AW) Flat 16f Standard / Slow 7/12 fig 41; 5 Nov Newbury Hurdle 16.5f Good To Soft 6/10 fig 105
    DATA for: Best recent form figure 105, 6 lb above field average
- Tommy Tipa (hrs_63680477) | 5yo G | 158lb | OR - | draw 0 | jockey Charlie Hammond | trainer Sara Bradstock (14d 0/4) | headgear - | last run 25 days | form 55 | MARKET 1.6% | 09:00 median 41.00 | Matchbook 95.00
    DATA: model 9.0% | style Held up (led 5% of runs) | runs in data 2 | last 3: 6 May Fontwell NH Flat 17.7f Good 5/9; 28 Oct Huntingdon NH Flat 16f Good 5/9 fig 103
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; First run over hurdles in our data
- Yanka Blue (hrs_53359033) | 5yo M | 151lb | OR 75 | draw 0 | jockey Robert Dunne | trainer Barry Murphy (14d 0/5) | headgear - | last run 19 days | form P44394 | MARKET 0.8% | 09:00 median 81.00 | Matchbook 200.00
    DATA: model 15.4% | style Held up (led 5% of runs) | runs in data 13 | last 3: 13 Oct Hereford Hurdle 19.7f Good To Firm 3/7; 29 Oct Stratford Hurdle 18.5f Good To Soft 9/11 fig 68; 3 Nov Sedgefield Hurdle 20f Good 4/5 fig 82
    DATA against: Best recent form figure 82, 17 lb below field average; Last-run finishing speed -3.7% vs that field (faded)

## 2:13 Fakenham | race_id rac_32305144027 | Jumps Looks Better On Racing TV Mares' Handicap Steeple Chase (Queen Boudicca Mares' Chase Series Qualifier)
Chase | Class 5 | 2m5f44y | going Good | Turf | 6 runners | rating band 0-105 | age 4yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Chosen Hero (hrs_30016189) | 8yo M | 153lb | OR 85 | draw 0 | jockey Jonathan Burke | trainer James Owen (14d 3/39) | headgear - | last run 1 days | form PPP-15 | MARKET 41.0% | 09:00 median 2.20 | Matchbook 2.32
    comment: Chosen Hero bounced back from three pulled-up efforts to win two starts back, then ran a fifth last time out, and she has run over today's trip and going before.
    DATA: model 22.8% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 20 Apr Kelso Hurdle 18.1f Good PU/9; 3 Nov Lingfield Hurdle 16f Good 1/9 fig 86; 21 Nov Huntingdon Chase 20f Good 5/9
    DATA for: Carries 6 lb less than average
    DATA against: Official rating 85, 6 lb below field average; Pulled up in 3 of its last 5 jumps runs
- I Am The Moon (hrs_40820402) | 7yo M | 164lb | OR 96 | draw 0 | jockey Toby McCain-Mitchell(3) | trainer Nigel & Willy Twiston-Davies (14d 4/28) | headgear p | last run 144 days | form P4-248 | MARKET 18.1% | 09:00 median 5.00 | Matchbook 5.30
    comment: Yet to win in her last five, I Am The Moon still shows a second three starts back and a fourth two starts back, and she has run over today's trip and going before.
    DATA: model 12.5% | style Prominent (led 4% of runs) | runs in data 7 | last 3: 17 May Stratford Hurdle 26.4f Good To Firm 2/5; 4 Jun Uttoxeter Chase 24f Good 4/4; 1 Jul Worcester Chase 23f Good 8/11
    DATA for: Official rating 96, 5 lb above field average
    DATA against: Last-run finishing speed -7.3% vs that field (faded); Carries 5 lb more than average; Returns from a 144-day break; Pulled up in 1 of its last 5 jumps runs
- Sweet Nightingale (hrs_22797670) | 9yo M | 150lb | OR 82 | draw 0 | jockey Tristan Durrell | trainer Polly Gundry (14d 0/0) | headgear t | last run 16 days | form 133-54 | MARKET 15.5% | 09:00 median 5.00 | Matchbook 7.00
    comment: Sweet Nightingale has been in the frame in most recent runs, with a fourth last time out and a win five starts back, but she's gone down the order since, and carrying 150 lb off 82 is a big ask.
    DATA: model 8.9% | style Midfield (led 4% of runs) | runs in data 6 | last 3: 24 Apr Fontwell Chase 26f Good 3/5; 9 May Warwick Chase 24f Good 5/8; 6 Nov Fontwell Chase 26f Good To Soft 4/6 fig 78
    DATA for: Has won at this trip or further; Carries 9 lb less than average
    DATA against: Best recent form figure 78, 6 lb below field average; Official rating 82, 9 lb below field average
- Gata Ban (hrs_29621935) | 9yo M | 165lb | OR 97 | draw 0 | jockey Dylan Johnston | trainer Neil Mulholland (14d 3/20) | headgear p | last run 9 days | form 211431 | MARKET 13.7% | 09:00 median 6.00 | Matchbook 7.60
    comment: Gata Ban won last time out and has three wins in her last six starts, with just nine days since that run, so the form is hard to knock.
    DATA: model 30.4% | style Midfield (led 4% of runs) | runs in data 9 | last 3: 23 Aug Worcester Chase 23f Good 4/8; 6 Sep Fontwell Chase 26f Good 3/6; 13 Nov Southwell Chase 24.5f Good 1/5 fig 93
    DATA for: Best recent form figure 93, 10 lb above field average; Official rating 97, 6 lb above field average; Has won at this trip or further; Good recent finishing positions
    DATA against: Carries 6 lb more than average
- Eastern Shores (hrs_39959647) | 6yo M | 154lb | OR 86 | draw 0 | jockey Kielan Woods | trainer Fergal O'Brien (14d 4/31) | headgear t | last run 12 days | form 56-7P4 | MARKET 10.1% | 09:00 median 9.00 | Matchbook 9.60
    comment: The risk is a winless recent run, including a pulled up two starts back, while carrying 154 lb.
    DATA: model 11.6% | style Held up (led 4% of runs) | runs in data 6 | last 3: 19 May Huntingdon Hurdle 15.8f Good To Firm 7/8; 21 Oct Fontwell Hurdle 19f Soft PU/6; 10 Nov Huntingdon Chase 20f Good 4/6 fig 77
    DATA for: Carries 5 lb less than average
    DATA against: Best recent form figure 77, 6 lb below field average; Recent figures 9 lb below its current mark (looks high in the weights); Official rating 86, 5 lb below field average; Pulled up in 1 of its last 5 jumps runs; Pace: steady gallop likely, hard to come from off the pace
- Miss Kassiopi (hrs_38130631) | 7yo M | 168lb | OR 100 | draw 0 | jockey Ben Poste | trainer Max Young (14d 0/2) | headgear - | last run 27 days | form -721P6 | MARKET 1.6% | 09:00 median 51.00 | Matchbook 70.00
    comment: Miss Kassiopi is a threat on form, having won three starts back and finished second four runs ago, and she has run over today's trip and going before after a 27-day break; the risk is a sixth last time out and a pulled up before that, while carrying 168 lb off a mark of 100.
    DATA: model 13.8% | style Prominent (led 23% of runs) | runs in data 8 | last 3: 3 Jul Newton Abbot Hurdle 21.6f Good 1/6; 12 Jul Stratford Hurdle 18.7f Good To Firm PU/8; 26 Oct Hereford Hurdle 19.5f Good To Firm 6/12
    DATA for: Official rating 100, 9 lb above field average; Has won at this trip or further
    DATA against: Last-run finishing speed -3.6% vs that field (faded); Carries 9 lb more than average; Pulled up in 1 of its last 5 jumps runs; First run over fences in our data

## 2:43 Fakenham | race_id rac_32305145964 | Get A Free Trial At racingtv.com/freetrial Handicap Hurdle Race
Hurdle | Class 4 | 2m7f95y | going Good | Turf | 5 runners | rating band 0-120 | age 4yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Mr Mackay (hrs_33110504) | 7yo G | 162lb | OR 114 | draw 0 | jockey Toby McCain-Mitchell(3) | trainer Nigel & Willy Twiston-Davies (14d 4/28) | headgear - | last run 26 days | form 2551/2 | MARKET 32.5% | 09:00 median 2.75 | Matchbook 3.00
    comment: Top weight of 162 lb is the one reservation.
    DATA: model 29.1% | style Unknown | runs in data 1 | last 3: 27 Oct Bangor-on-Dee Hurdle 23f Good 2/9 fig 113
    DATA for: Last-run finishing speed +2.6% vs that field (finished strongly)
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- At Mangan Bridge (hrs_47621056) | 8yo G | 156lb | OR 108 | draw 0 | jockey Charlie Hammond | trainer Stuart Edmunds (14d 1/11) | headgear t | last run 23 days | form 3511-0 | MARKET 26.4% | 09:00 median 3.50 | Matchbook 3.60
    comment: On the plus side, he has won twice in his last five, has run on today's going and is fresh enough after 23 days.
    DATA: model 14.5% | style Held up (led 8% of runs) | runs in data 1 | last 3: 30 Oct Uttoxeter Hurdle 20f Good 12/15
    DATA against: Last-run finishing speed -2.3% vs that field (faded); Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Everyonesgame (hrs_27428821) | 9yo G | 158lb | OR 110 | draw 0 | jockey Chad Bament(5) | trainer Andy Irvine (14d 0/4) | headgear - | last run 20 days | form 765-22 | MARKET 17.9% | 09:00 median 5.00 | Matchbook 5.60
    comment: Everyonesgame arrives in cracking nick, runner-up last time out and again two starts back, and he's fresh enough after 20 days off, with experience of today's trip and going. Yet to win in his last five, though, and 158 lb is a hefty burden to carry.
    DATA: model 14.2% | style Midfield (led 5% of runs) | runs in data 4 | last 3: 23 Apr Warwick Hurdle 25f Good 5/5; 26 May Plumpton Hurdle 20.5f Good 2/4; 2 Nov Plumpton Hurdle 20.5f Good 2/7 fig 110
    DATA for: Good recent finishing positions
- King Jon Oliver (hrs_51091054) | 6yo G | 160lb | OR 112 | draw 0 | jockey Robert Dunne | trainer Olly Murphy (14d 10/52) | headgear b (1st time) | last run 8 days | form 1P4P-P | MARKET 17.8% | 09:00 median 5.00 | Matchbook 5.60
    comment: The risk is obvious: he has pulled up in two of his last three, and only eight days since his last run.
    DATA: model 25.2% | style Prominent (led 3% of runs) | runs in data 5 | last 3: 28 Mar Uttoxeter Hurdle 23.3f Good To Soft 4/11; 23 Apr Perth Hurdle 20.2f Good PU/8; 14 Nov Windsor Chase 20f Good PU/5
    DATA for: First-time headgear
    DATA against: Race comments mention jumping mistakes in 3 of its last 5 runs; Pulled up in 3 of its last 5 jumps runs
- Greatness Awaits (hrs_25795413) | 7yo G | 158lb | OR 110 | draw 0 | jockey Tom Cannon | trainer Sarah Humphrey (14d 0/3) | headgear tp | last run 343 days | form 45740- | MARKET 5.3% | 09:00 median 17.00 | Matchbook 19.00
    comment: The main risk is fitness, with 158 lb to carry on his return.
    DATA: model 17.0% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 343-day break; Lightly raced: 0 runs in our data, so the model has little to go on

## 3:13 Fakenham | race_id rac_32305147901 | 31 Days Free Racing TV At racingtv.com/freetrial Novices' Handicap Steeple Chase (GBB Race)
Chase | Class 4 | 3m0f38y | going Good | Turf | 5 runners | rating band 0-110 | age 4yo+
DATA pace: Lone leader - Breezethroughlife is the only habitual front-runner and may be allowed an easy lead.
- Painted Wolf (hrs_29621984) | 8yo G | 164lb | OR 102 | draw 0 | jockey Jonathan Burke | trainer Ben Case (14d 1/6) | headgear tp (1st time) | wind surgery | last run 38 days | form 5P21-4 | MARKET 28.0% | 09:00 median 3.25 | Matchbook 3.45 | CHECK (skip line 3.09)
    comment: Painted Wolf looks a strong threat, having won two starts back and finished second three starts back before a fourth last time out, and he has run on today's going before. The main risk is a 38-day absence while carrying 164 lb.
    DATA: model 24.4% | style Prominent (led 29% of runs) | runs in data 5 | last 3: 13 Mar Fakenham Hurdle 20f Good To Soft 2/4; 6 Apr Fakenham Hurdle 20f Good 1/7; 15 Oct Fontwell Hurdle 21.5f Good To Soft 4/6 fig 90
    DATA for: Good recent finishing positions; First-time headgear
    DATA against: Recent figures 12 lb below its current mark (looks high in the weights); Last-run finishing speed -2.8% vs that field (faded); Pulled up in 1 of its last 5 jumps runs; First run over fences in our data
- Mr McWhinny (hrs_412694786) | 8yo G | 168lb | OR 106 | draw 0 | jockey Finn Lambert(3) | trainer Tom Ellis (14d 1/9) | headgear t | last run 18 days | form 41112F | MARKET 25.4% | 09:00 median 3.50 | Matchbook 3.90
    comment: Mr McWhinny won three on the spin before a second two starts back, and he has run over today's trip and going, so the form reads strongly after just 18 days off. The risk is the fall last time out, with 168 lb to carry also demanding.
    DATA: model 31.3% | style Midfield (led 5% of runs) | runs in data 8 | last 3: 18 Sep Newton Abbot Chase 21f Good 1/6; 3 Oct Fontwell Hurdle 21.7f Good 2/4; 4 Nov Chepstow Chase 19.5f Good F/8
    DATA for: Official rating 106, 8 lb above field average
    DATA against: Carries 8 lb more than average; Race comments mention jumping mistakes in 2 of its last 5 runs; Fell or unseated in 1 of its last 5 jumps runs
- Hawaii du Mestivel (hrs_27566014) | 9yo G | 166lb | OR 104 | draw 0 | jockey Conor O'Farrell | trainer Neil Mulholland (14d 3/20) | headgear tp | last run 228 days | form 1/PP2- | MARKET 20.8% | 09:00 median 4.33 | Matchbook 4.70
    comment: The main risk is a 228-day absence, plus two pulled-up efforts before that second.
    DATA: model 15.6% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 2 Feb Kempton Chase 24f Good To Soft PU/10; 14 Mar Uttoxeter Chase 20f Soft PU/5; 8 Apr Fontwell Chase 21.6f Good To Soft 2/4
    DATA for: Official rating 104, 6 lb above field average; Last-run finishing speed +3.5% vs that field (finished strongly)
    DATA against: Carries 6 lb more than average; Returns from a 228-day break; Pulled up in 2 of its last 3 jumps runs
- Breezethroughlife (hrs_51123751) | 5yo G | 162lb | OR 100 | draw 0 | jockey Jack Quinlan | trainer Neil King (14d 0/5) | headgear t | wind surgery | last run 17 days | form 3-8344 | MARKET 18.2% | 09:00 median 5.00 | Matchbook 5.40
    comment: Consistent sort who has finished in the first four in four of his last five, including a third five starts back, and he has run over today's trip and going before.
    DATA: model 14.7% | style Leader (led 43% of runs) | runs in data 7 | last 3: 19 May Huntingdon Hurdle 20.7f Good To Firm 3/3; 4 Jun Uttoxeter Hurdle 23.3f Good 4/7; 5 Nov Plumpton Chase 20f Good 4/4 fig 92
    DATA for: Best recent form figure 92, 5 lb above field average; Pace: may get an uncontested lead
    DATA against: Recent figures 8 lb below its current mark (looks high in the weights); Last-run finishing speed -2.4% vs that field (faded)
- Bahtiyar (hrs_31835195) | 8yo G | 142lb | OR 78 | draw 0 | jockey Ben Poste | trainer Max Young (14d 0/2) | headgear tp | last run 19 days | form 634523 | MARKET 7.7% | 09:00 median 12.00 | Matchbook 12.50
    comment: Bahtiyar is winless in his last six, though he arrives in decent heart with a third last time out and a second two starts back, after 19 days off.
    DATA: model 14.0% | style Held up (led 4% of runs) | runs in data 11 | last 3: 5 Oct Stratford Chase 22.6f Good To Firm 5/9; 17 Oct Stratford Chase 22.5f Good 2/7 fig 78; 3 Nov Warwick Chase 25.5f Good 3/3 fig 74
    DATA for: Good recent finishing positions; Carries 18 lb less than average
    DATA against: Best recent form figure 78, 9 lb below field average; Official rating 78, 20 lb below field average
