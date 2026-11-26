# Card review packet: Taunton, 2026-11-26

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
{"meeting": "taunton", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 12:20 Taunton | race_id rac_32305618592 | Remembering Hendrix 'National Hunt' Novices' Hurdle Race (£50,000 Cheltenham Bonus Qualifier) (GBB Race)
Hurdle | Class 4 | 2m0f104y | going Good To Firm | Turf | 6 runners | rating band - | age 4yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Fortis Et Liber (hrs_52709083) | 5yo G | 154lb | OR 112 | draw 0 | jockey Harry Atkins(5) | trainer Dan Skelton (14d 21/94) | headgear - | last run 55 days | form 2R27 | MARKET 42.8% | 09:00 median 2.10 | Matchbook 2.20
    DATA: model 43.7% | style Midfield (led 3% of runs) | runs in data 4 | last 3: 14 Aug Tramore Hurdle 16.4f Good RO/11; 31 Aug Downpatrick Hurdle 21.8f Good 2/9; 2 Oct Gowran Park Hurdle 20.2f Good 7/17
    DATA for: Trainer 22% wins (21/94), last 14 days; Last-run finishing speed +2.1% vs that field (finished strongly)
    DATA against: Fell or unseated in 1 of its last 4 jumps runs
- Theybouncewell (hrs_17394424635) | 4yo F | 147lb | OR - | draw 0 | jockey Liam Harrison | trainer Tom George (14d 0/2) | headgear - | last run 31 days | form 2 | MARKET 27.4% | 09:00 median 3.00 | Matchbook 3.70
    DATA: model 14.4% | style Held up (led 8% of runs) | runs in data 1 | last 3: 26 Oct Hereford Hurdle 19.5f Good To Firm 2/6 fig 106
    DATA for: Last-run finishing speed +4.1% vs that field (finished strongly)
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Arms Park (hrs_56961765) | 5yo G | 154lb | OR - | draw 0 | jockey Adam Wedge | trainer Mrs C. Williams (14d 0/23) | headgear - | last run 35 days | form 231-P4 | MARKET 24.3% | 09:00 median 3.75 | Matchbook 3.90
    DATA: model 18.6% | style Prominent (led 38% of runs) | runs in data 3 | last 3: 24 Mar Taunton NH Flat 16.5f Good 1/6; 7 Oct Sedgefield Hurdle 16.8f Good PU/9; 22 Oct Ffos Las Hurdle 16f Soft 4/11 fig 101
    DATA for: Has won at this trip or further
    DATA against: Trainer 0 wins from 23 runs, last 14 days; Pulled up in 1 of its last 2 jumps runs
- Timmie Two (hrs_62393982) | 4yo G | 154lb | OR - | draw 0 | jockey Bryan Carver | trainer Ian Chanin (14d 0/1) | headgear - | last run 22 days | form 23-P | MARKET 3.5% | 09:00 median 26.00 | Matchbook 29.00
    DATA: model 11.0% | style Midfield (led 8% of runs) | runs in data 2 | last 3: 22 Mar Exeter NH Flat 16.7f Good 4/7; 4 Nov Chepstow Hurdle 16f Good To Soft PU/13
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Pulled up in 1 of its last 1 jumps runs
- Maucourt d'Airy (hrs_62101550) | 4yo G | 154lb | OR - | draw 0 | jockey Ciaran O'Shea(7) | trainer Ella Pickard (14d 0/0) | headgear - | wind surgery | last run 204 days | form 4-8 | MARKET 1.3% | 09:00 median 67.00 | Matchbook 100.00
    DATA: model 7.3% | style Unknown | runs in data 2 | last 3: 1 Mar Ffos Las NH Flat 15.8f Heavy 4/4; 6 May Fontwell NH Flat 17.7f Good 8/9
    DATA against: Last-run finishing speed -7.7% vs that field (faded); Returns from a 204-day break; Lightly raced: 2 runs in our data, so the model has little to go on; First run over hurdles in our data
- She's A Driver (hrs_62326383) | 4yo F | 147lb | OR - | draw 0 | jockey James Turner(5) | trainer David Bridgwater (14d 0/2) | headgear - | last run 12 days | form 6-P | MARKET 0.8% | 09:00 median 101.00 | Matchbook 140.00
    DATA: model 5.0% | style Held up (led 8% of runs) | runs in data 2 | last 3: 9 Mar Plumpton NH Flat 17.8f Good To Soft 6/7; 14 Nov Windsor Hurdle 16f Good PU/14
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Pulled up in 1 of its last 1 jumps runs; Pace: steady gallop likely, hard to come from off the pace

## 12:55 Taunton | race_id rac_32305620529 | Denise Smith Memorial Novices' Limited Handicap Hurdle Race
Hurdle | Class 5 | 2m7f198y | going Good To Firm | Turf | 8 runners | rating band 0-95 | age 4yo+
DATA pace: Lone leader - Poet's Muse is the only habitual front-runner and may be allowed an easy lead.
- Poet's Muse (hrs_51618973) | 5yo M | 160lb | OR 82 | draw 0 | jockey Lorcan Williams | trainer Ian Chanin (14d 0/1) | headgear p | last run 4 days | form -7PF62 | MARKET 23.5% | 09:00 median 3.75 | Matchbook 4.00 | CHECK (skip line 3.56)
    comment: Runner-up last time out just four days ago, Poet's Muse is fit and race-sharp, and she has run over today's trip and going before.
    DATA: model 12.9% | style Leader (led 38% of runs) | runs in data 9 | last 3: 11 Oct Chepstow Hurdle 23.6f Good To Soft F/12; 26 Oct Hereford Hurdle 25.5f Good To Firm 6/8 fig 77; 22 Nov Exeter Hurdle 23f Good 2/5 fig 110
    DATA for: Best recent form figure 110, 23 lb above field average; Recent figures 28 lb above its current mark (looks well handicapped); Pace: may get an uncontested lead
    DATA against: Race comments mention jumping mistakes in 2 of its last 5 runs; Fell or unseated in 1 of its last 5 jumps runs; Pulled up in 1 of its last 5 jumps runs
- Dublinofficecallin (hrs_52896921) | 5yo G | 166lb | OR 88 | draw 0 | jockey Conor O'Farrell | trainer Kerry Lee (14d 1/6) | headgear - | last run 14 days | form 71-703 | MARKET 20.1% | 09:00 median 4.33 | Matchbook 4.70
    comment: Dublinofficecallin booked a third last time out just 14 days ago, and he has a win four starts back to his name, so he arrives fresh and in decent heart having run on this going before.
    DATA: model 26.9% | style Held up (led 3% of runs) | runs in data 8 | last 3: 13 May Perth Hurdle 20.2f Good To Soft 7/9; 16 Jun Stratford Hurdle 16.3f Good 10/12; 12 Nov Hereford Hurdle 21.5f Good To Firm 3/7 fig 86
    DATA for: Official rating 88, 8 lb above field average
    DATA against: Carries 8 lb more than average
- Makinbecon (hrs_41378393) | 6yo G | 159lb | OR 81 | draw 0 | jockey Callum Pritchard | trainer Barry Murphy (14d 0/6) | headgear tp | wind surgery | last run 46 days | form 31665P | MARKET 14.2% | 09:00 median 6.00 | Matchbook 7.00
    comment: Makinbecon was pulled up last time out after a fifth and two sixths before that, and a win five starts back looks a long way off now, so he is hard to fancy off 159 lb.
    DATA: model 18.1% | style Midfield (led 4% of runs) | runs in data 12 | last 3: 28 Aug Sedgefield Hurdle 19.9f Good 6/9; 7 Sep Newton Abbot Hurdle 21.6f Good 5/8; 11 Oct Chepstow Hurdle 19.5f Good To Soft PU/13
    DATA against: Pulled up in 1 of its last 5 jumps runs
- Anothermanicmonday (hrs_52772209) | 6yo G | 152lb | OR 74 | draw 0 | jockey Lucy Gardner | trainer Susan Gardner (14d 1/3) | headgear - | last run 10 days | form 6-571P | MARKET 13.9% | 09:00 median 6.00 | Matchbook 7.20
    comment: Pulled up last time out, a run just ten days ago, Anothermanicmonday is hard to fancy after a win two starts back sat between a run of sixth, fifth and seventh finishes.
    DATA: model 14.1% | style Prominent (led 38% of runs) | runs in data 6 | last 3: 13 Jul Newton Abbot Hurdle 18.5f Good To Firm 7/12; 21 Oct Fontwell Hurdle 21.5f Soft 1/7 fig 73; 16 Nov Plumpton Hurdle 25f Good To Soft PU/7
    DATA for: Carries 6 lb less than average
    DATA against: Best recent form figure 73, 14 lb below field average; Official rating 74, 6 lb below field average; Pulled up in 1 of its last 5 jumps runs
- Nowherenearmilan (hrs_61046699) | 5yo M | 163lb | OR 85 | draw 0 | jockey David Bass | trainer Max Comley (14d 2/9) | headgear p | last run 22 days | form 7358-0 | MARKET 11.7% | 09:00 median 7.50 | Matchbook 8.20
    comment: Nowherenearmilan is yet to win in her last five starts, but a third four starts back shows she can get involved, and she returns fresh after 22 days off the track.
    DATA: model 9.1% | style Midfield (led 4% of runs) | runs in data 6 | last 3: 11 Apr Chepstow Hurdle 16.1f Good To Soft 5/9; 24 Apr Chepstow Hurdle 16.1f Good 8/12; 4 Nov Chepstow Hurdle 19.5f Good To Soft 10/16
    DATA for: Official rating 85, 5 lb above field average; Trainer 22% wins (2/9), last 14 days
    DATA against: Last-run finishing speed -2.5% vs that field (faded); Carries 6 lb more than average
- C'Est Pour Moi (hrs_56559433) | 4yo G | 161lb | OR 85 | draw 0 | jockey Amber Jackson-Fennell(7) | trainer Nigel & Willy Twiston-Davies (14d 4/20) | headgear - | last run 14 days | form 967833 | MARKET 10.0% | 09:00 median 8.50 | Matchbook 10.00
    comment: C'Est Pour Moi arrives in better heart, with a third last time out and another third two starts back after a modest run of finishes, and he's fresh from a 14-day break.
    DATA: model 6.9% | style Midfield (led 4% of runs) | runs in data 6 | last 3: 10 Sep Worcester Hurdle 16f Good 8/12; 26 Oct Hereford Hurdle 19.5f Good To Firm 3/6; 12 Nov Market Rasen Hurdle 20.5f Good To Soft 3/6 fig 78
    DATA for: Official rating 85, 5 lb above field average; Trainer 20% wins (4/20), last 14 days; Good recent finishing positions
    DATA against: Best recent form figure 78, 9 lb below field average; Recent figures 7 lb below its current mark (looks high in the weights); Race comments mention jumping mistakes in 3 of its last 4 runs
- Dalcassian Girl (hrs_49578200) | 6yo M | 152lb | OR 74 | draw 0 | jockey Bryan Carver | trainer Chris Honour (14d 0/6) | headgear - | last run 12 days | form 562-4P | MARKET 4.9% | 09:00 median 17.00 | Matchbook 21.00
    DATA: model 10.0% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 22 Mar Exeter Hurdle 21.6f Good 2/3; 29 Oct Ffos Las Hurdle 16f Heavy 4/7; 14 Nov Windsor Hurdle 20f Good PU/11
    DATA for: Carries 6 lb less than average
    DATA against: Official rating 74, 6 lb below field average; Pulled up in 1 of its last 5 jumps runs
- Cantalice (hrs_50809703) | 4yo F | 147lb | OR 71 | draw 0 | jockey Megan Bevan(7) | trainer Ella Pickard (14d 0/0) | headgear tb | last run 262 days | form 4P0- | MARKET 1.7% | 09:00 median 41.00 | Matchbook 90.00
    comment: Lightly raced and unexposed, Cantalice returns after 262 days off, having been unplaced last time out, pulled up two starts back and a fourth three starts back. She is yet to win in recent starts, so any improvement is untapped, and she carries 147 lb.
    DATA: model 2.1% | style Prominent (led 38% of runs) | runs in data 2 | last 3: 11 Feb Hereford Hurdle 16.2f Heavy PU/9; 9 Mar Taunton Hurdle 16.5f Good 11/12
    DATA for: Carries 10 lb less than average
    DATA against: Official rating 71, 9 lb below field average; Last-run finishing speed -7.5% vs that field (faded); Returns from a 262-day break; Lightly raced: 2 runs in our data, so the model has little to go on; Pulled up in 1 of its last 2 jumps runs

## 1:30 Taunton | race_id rac_32305622466 | Stag Environmental Handicap Hurdle Race
Hurdle | Class 4 | 2m3f1y | going Good To Firm | Turf | 7 runners | rating band 0-120 | age 3yo+
DATA pace: Even - Two likely leaders (Cornish Storm, Into Battle). A fair, even gallop is most likely.
- Courageous Strike (hrs_35337575) | 5yo G | 164lb | OR 112 | draw 0 | jockey Sam Twiston-Davies | trainer Paul Nicholls (14d 2/21) | headgear h | wind surgery | last run 296 days | form 15236- | MARKET 24.2% | 09:00 median 3.50 | Matchbook 4.20 | CHECK (skip line 3.32)
    DATA: model 15.9% | style Prominent (led 8% of runs) | runs in data 2 | last 3: 10 Jan Kempton Hurdle 16f Good 3/8; 3 Feb Taunton Hurdle 16.5f Heavy 6/7
    DATA against: Returns from a 296-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- Taritino (hrs_29918658) | 6yo G | 151lb | OR 99 | draw 0 | jockey Callum Pritchard | trainer Joe Tickle (14d 1/10) | headgear - | last run 14 days | form 321-63 | MARKET 20.2% | 09:00 median 4.33 | Matchbook 4.80
    comment: Taritino was third last time out and a winner three starts back, with a sixth in between, and he's fit after 14 days off, having run over today's trip and going before.
    DATA: model 11.6% | style Prominent (led 8% of runs) | runs in data 16 | last 3: 13 Sep Bath Flat 14f Good To Soft 4/12; 27 Sep Epsom Downs Flat 12f Good 8/13; 12 Nov Hereford Hurdle 16f Good To Firm 3/9 fig 99
    DATA for: Has won at this trip or further; Carries 9 lb less than average
    DATA against: Official rating 99, 10 lb below field average
- Lunar Orbit (hrs_44975553) | 4yo G | 155lb | OR 104 | draw 0 | jockey Harry Atkins(5) | trainer Dan Skelton (14d 21/94) | headgear ht | last run 12 days | form 5-2P25 | MARKET 17.8% | 09:00 median 5.00 | Matchbook 5.40
    comment: The main risk is that he's yet to win and carries 155 lb.
    DATA: model 14.1% | style Held up (led 8% of runs) | runs in data 5 | last 3: 8 Sep Bangor-on-Dee Hurdle 19.6f Good PU/7; 26 Oct Hereford Hurdle 19.5f Good To Firm 2/12 fig 107; 14 Nov Uttoxeter Hurdle 20f Good 5/8 fig 100
    DATA for: Trainer 22% wins (21/94), last 14 days; Carries 5 lb less than average
    DATA against: Pulled up in 1 of its last 5 jumps runs
- Holeshot (hrs_38188738) | 7yo G | 155lb | OR 103 | draw 0 | jockey Lorcan Murtagh | trainer Mitchell Hunt & Tim Vaughan (14d 1/5) | headgear - | last run 48 days | form P4P5-6 | MARKET 12.2% | 09:00 median 7.50 | Matchbook 7.80
    comment: The main risk is a 48-day absence and a 155 lb burden, with two pulled-up efforts in his last five.
    DATA: model 10.7% | style Midfield (led 23% of runs) | runs in data 4 | last 3: 27 Mar Wetherby Chase 24.2f Good PU/9; 22 Apr Taunton Hurdle 23.9f Good 5/7; 9 Oct Chepstow Hurdle 16.1f Good To Soft 6/15
    DATA for: Trainer 20% wins (1/5), last 14 days; Carries 5 lb less than average
    DATA against: Official rating 103, 6 lb below field average; Pulled up in 1 of its last 4 jumps runs
- Into Battle (hrs_37603559) | 5yo G | 162lb | OR 110 | draw 0 | jockey Robert Dunne | trainer Robert Stephens (14d 0/4) | headgear - | last run 83 days | form 02-31 | MARKET 10.2% | 09:00 median 8.50 | Matchbook 9.60
    comment: That consistent recent form is his main plus.
    DATA: model 16.3% | style Leader (led 38% of runs) | runs in data 6 | last 3: 26 Jun Bangor-on-Dee Hurdle 16.7f Good 1/4; 23 Jul Newbury Flat 12f Good To Firm 3/4; 4 Sep Kempton Flat 16f Standard To Slow 8/8
    DATA for: Good recent finishing positions
- Cornish Storm (hrs_27154008) | 7yo G | 168lb | OR 116 | draw 0 | jockey Jay Tidball(5) | trainer Zoe Hawkins (14d 0/1) | headgear p | last run 229 days | form 91155- | MARKET 9.5% | 09:00 median 10.00 | Matchbook 10.00
    comment: The risk is a 229-day absence, plus 168 lb after back-to-back fifth-placed efforts.
    DATA: model 17.6% | style Leader (led 54% of runs) | runs in data 3 | last 3: 7 Feb Warwick Hurdle 16f Heavy 1/8; 20 Mar Newbury Hurdle 16.3f Good To Soft 5/7; 11 Apr Chepstow Hurdle 16.1f Good To Soft 5/9
    DATA for: Official rating 116, 7 lb above field average
    DATA against: Carries 8 lb more than average; Returns from a 229-day break
- Venetian Beauty (hrs_51491811) | 4yo F | 167lb | OR 116 | draw 0 | jockey Rian Corcoran(5) | trainer David Pipe (14d 2/14) | headgear - | last run 28 days | form -1P501 | MARKET 6.0% | 09:00 median 15.00 | Matchbook 17.50
    comment: Venetian Beauty won last time out, 28 days ago, and also took a win five starts back, though a pulled up and an unplaced run show she has had her ups and downs. Still unexposed, she carries 167 lb and could have more to offer.
    DATA: model 13.8% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Official rating 116, 7 lb above field average
    DATA against: Carries 7 lb more than average; Lightly raced: 0 runs in our data, so the model has little to go on

## 2:05 Taunton | race_id rac_32305624403 | Stables Business Park Handicap Hurdle Race
Hurdle | Class 5 | 2m3f1y | going Good To Firm | Turf | 12 runners | rating band 0-100 | age 3yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Savanna Storm (hrs_64360870) | 4yo G | 166lb | OR 97 | draw 0 | jockey Stan Sheppard | trainer Tom Lacey (14d 3/12) | headgear - | last run 12 days | form 748741 | MARKET 22.2% | 09:00 median 3.75 | Matchbook 4.10 | CHECK (skip line 3.56)
    comment: The main risk is 166 lb, a hefty burden, and his form before that win was patchy.
    DATA: model 7.7% | style Held up (led 4% of runs) | runs in data 6 | last 3: 10 Sep Worcester Hurdle 16f Good 7/12; 28 Sep Newton Abbot Hurdle 16.8f Good 4/6; 14 Nov Uttoxeter Hurdle 16f Good 1/12 fig 102
    DATA for: Best recent form figure 102, 12 lb above field average; Recent figures 5 lb above its current mark (looks well handicapped); Official rating 97, 10 lb above field average; Trainer 25% wins (3/12), last 14 days
    DATA against: Carries 9 lb more than average; Pace: steady gallop likely, hard to come from off the pace
- Electric Eddy (hrs_35244412) | 8yo G | 158lb | OR 88 | draw 0 | jockey Sam Twiston-Davies | trainer Nigel & Willy Twiston-Davies (14d 4/20) | headgear - | last run 23 days | form 366453 | MARKET 16.8% | 09:00 median 5.00 | Matchbook 5.40
    comment: Electric Eddy was third last time out and has been consistent without a win in his last six starts, having run over today's trip and going before.
    DATA: model 12.2% | style Midfield (led 4% of runs) | runs in data 6 | last 3: 22 Aug Newton Abbot Hurdle 18.5f Good To Firm 4/10; 26 Sep Market Rasen Hurdle 23.1f Good 5/10; 3 Nov Warwick Hurdle 21f Good 3/10 fig 88
    DATA for: Trainer 20% wins (4/20), last 14 days; Last-run finishing speed +2.3% vs that field (finished strongly)
    DATA against: Race comments mention jumping mistakes in 2 of its last 5 runs
- Asian Spice (hrs_29479254) | 8yo M | 166lb | OR 96 | draw 0 | jockey Rian Corcoran(5) | trainer David Pipe (14d 2/14) | headgear - | wind surgery | last run 223 days | form 46UP7- | MARKET 15.1% | 09:00 median 4.33 | Matchbook 7.80
    comment: Asian Spice has been out of sorts lately, with a seventh last time out and a pulled up two starts back, but she is yet to win in that spell and has run over today's trip.
    DATA: model 5.4% | style Held up (led 5% of runs) | runs in data 2 | last 3: 26 Feb Taunton Chase 21.7f Good To Soft PU/7; 17 Apr Exeter Hurdle 18.5f Good 7/10
    DATA for: Official rating 96, 10 lb above field average
    DATA against: Last-run finishing speed -3.3% vs that field (faded); Carries 9 lb more than average; Returns from a 223-day break; Lightly raced: 2 runs in our data, so the model has little to go on; Pulled up in 1 of its last 2 jumps runs; Pace: steady gallop likely, hard to come from off the pace
- Victory Shout (hrs_35767627) | 5yo G | 168lb | OR 98 | draw 0 | jockey Ciaran O'Shea(7) | trainer Syd Hosie (14d 1/11) | headgear - | last run 10 days | form 122-05 | MARKET 10.7% | 09:00 median 8.00 | Matchbook 8.60
    comment: Victory Shout bids to build on a winning run five starts back, with a second three starts back and another second four starts back, and he's fit after just 10 days off; he has run over today's trip, but a fifth last time out and 168 lb are the concern.
    DATA: model 8.4% | style Midfield (led 4% of runs) | runs in data 6 | last 3: 12 Apr Wincanton Hurdle 15.2f Good 2/8; 9 Oct Chepstow Hurdle 16.1f Good To Soft 12/15; 16 Nov Plumpton Hurdle 16f Good To Soft 5/8 fig 90
    DATA for: Official rating 98, 12 lb above field average
    DATA against: Recent figures 8 lb below its current mark (looks high in the weights); Carries 11 lb more than average
- Gone Country (hrs_46483066) | 6yo G | 158lb | OR 88 | draw 0 | jockey Tabitha Worsley | trainer Nick Gifford (14d 1/6) | headgear - | last run 18 days | form 96-115 | MARKET 8.4% | 09:00 median 9.50 | Matchbook 11.50
    comment: Gone Country won two starts back and again three starts back, though he was only fifth last time out, and he returns after 18 days carrying 158 lb off an official mark of 88.
    DATA: model 18.2% | style Midfield (led 3% of runs) | runs in data 6 | last 3: 14 May Fontwell Hurdle 21.7f Good 1/10; 19 Oct Plumpton Hurdle 20.5f Good 1/7 fig 86; 8 Nov Sandown Hurdle 20f Good To Soft 5/8
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Best recent form figure 86, 4 lb below field average
- Raffles Nobu (hrs_37380882) | 6yo G | 155lb | OR 85 | draw 0 | jockey Nathan Andrews(10) | trainer Nick Scholfield (14d 1/13) | headgear tb | last run 16 days | form 525773 | MARKET 6.5% | 09:00 median 13.00 | Matchbook 14.00
    comment: Raffles Nobu showed a return to form with a third last time out just 16 days ago, and he has run over today's trip and going before, though he is yet to win in his last six starts.
    DATA: model 9.1% | style Midfield (led 4% of runs) | runs in data 18 | last 3: 17 Oct Stratford Hurdle 16.5f Good 7/7; 26 Oct Hereford Hurdle 19.5f Good To Firm 7/12; 10 Nov Lingfield Hurdle 16f Good 3/9 fig 83
    DATA for: Last-run finishing speed +2.3% vs that field (finished strongly); Has won at this trip or further
    DATA against: Best recent form figure 83, 7 lb below field average
- The Padster (hrs_43385377) | 5yo G | 152lb | OR 82 | draw 0 | jockey Callum Pritchard | trainer Joe Tickle (14d 1/10) | headgear p | last run 22 days | form 04-24P | MARKET 6.2% | 09:00 median 13.00 | Matchbook 15.50
    comment: Pulled up last time out, The Padster is yet to win in his last five starts, though a fourth two starts back and a second three starts back show he has some ability, and he has run over today's trip and going.
    DATA: model 10.8% | style Prominent (led 3% of runs) | runs in data 5 | last 3: 12 May Hereford Hurdle 19.7f Good To Firm 2/8; 22 Jul Worcester Hurdle 20f Good 4/13; 4 Nov Chepstow Hurdle 19.5f Good To Soft PU/16
    DATA against: Pulled up in 1 of its last 5 jumps runs
- One Island (hrs_52525984) | 4yo G | 166lb | OR 97 | draw 0 | jockey Lorcan Murtagh | trainer Paul Nicholls (14d 2/21) | headgear tb | last run 4 days | form 32-553 | MARKET 5.5% | 09:00 median 15.00 | Matchbook 17.50
    comment: Back after just four days, One Island is yet to win in his last five starts, though a third last time out and a second four starts back show he is competitive.
    DATA: model 8.3% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 13 May Newton Abbot Hurdle 16.8f Good 5/5; 2 Nov Plumpton Hurdle 16f Good 5/6 fig 88; 22 Nov Exeter Hurdle 16.5f Good 3/6 fig 91
    DATA for: Official rating 97, 10 lb above field average
    DATA against: Recent figures 6 lb below its current mark (looks high in the weights); Carries 9 lb more than average
- Forest Hills (hrs_37027144) | 5yo G | 143lb | OR 73 | draw 0 | jockey Conor O'Farrell | trainer Carroll Gray (14d 0/1) | headgear - | last run 22 days | form 0765-0 | MARKET 4.1% | 09:00 median 17.00 | Matchbook 27.00
    comment: Forest Hills is winless in his last five, with an unplaced run last time out and a fifth, sixth and seventh before that, so he is hard to fancy off 143 lb and an official mark of 73.
    DATA: model 2.4% | style Held up (led 4% of runs) | runs in data 7 | last 3: 22 Apr Taunton Hurdle 19f Good 5/10; 8 Oct Bath Flat 17.1f Good UR/12; 4 Nov Chepstow Hurdle 19.5f Good To Soft 12/14
    DATA for: Carries 14 lb less than average
    DATA against: Official rating 73, 14 lb below field average; Last-run finishing speed -9.7% vs that field (faded); Pace: steady gallop likely, hard to come from off the pace
- Paddy In The Caddy (hrs_34073242) | 7yo G | 164lb | OR 94 | draw 0 | jockey Chad Bament(5) | trainer Harry Ryall (14d 0/0) | headgear t (1st time) | last run 262 days | form 90PP6- | MARKET 1.9% | 09:00 median 41.00 | Matchbook 55.00
    DATA: model 5.4% | style Prominent (led 38% of runs) | runs in data 2 | last 3: 9 Jan Exeter Chase 17.5f Good To Soft PU/11; 9 Mar Taunton Chase 16.1f Good 6/6
    DATA for: Official rating 94, 8 lb above field average; First-time headgear
    DATA against: Last-run finishing speed -5.3% vs that field (faded); Carries 7 lb more than average; Returns from a 262-day break; Lightly raced: 2 runs in our data, so the model has little to go on; Pulled up in 1 of its last 2 jumps runs; First run over hurdles in our data
- Future Times (hrs_30765154) | 6yo G | 142lb | OR 69 | draw 0 | jockey Amber Jackson-Fennell(7) | trainer Gordon Edwards (14d 0/0) | headgear p | last run 218 days | form /4808- | MARKET 1.6% | 09:00 median 51.00 | Matchbook 70.00
    comment: Future Times is hard to fancy, having finished eighth last time out and been off for 218 days since, and he is winless in his last four with a fourth four starts back the best of it.
    DATA: model 4.9% | style Prominent (led 29% of runs) | runs in data 4 | last 3: 23 Mar Wincanton Hurdle 19.8f Good 8/12; 7 Apr Exeter Hurdle 21.6f Good 11/13; 22 Apr Taunton Hurdle 19f Good 8/10
    DATA for: Carries 15 lb less than average
    DATA against: Official rating 69, 18 lb below field average; Last-run finishing speed -2.6% vs that field (faded); Poor recent finishing positions; Returns from a 218-day break
- Freddie Fleetfoot (hrs_29212582) | 8yo G | 142lb | OR 71 | draw 0 | jockey Jack Stenhouse(7) | trainer Carroll Gray (14d 0/1) | headgear - | last run 54 days | form 622-P7 | MARKET 1.0% | 09:00 median 81.00 | Matchbook 150.00
    comment: Freddie Fleetfoot is hard to fancy, having been beaten in a seventh last time out after being pulled up two starts back, and he returns from a 54-day break carrying 142 lb. On the plus side, he has run over today's trip and filled second twice in his last five starts, though he is yet to win in that spell.
    DATA: model 7.2% | style Prominent (led 8% of runs) | runs in data 2 | last 3: 15 Jan Wincanton Hurdle 15.2f Heavy 6/13; 3 Oct Fontwell Hurdle 19.1f Good 7/9
    DATA for: Carries 15 lb less than average
    DATA against: Official rating 71, 16 lb below field average; Lightly raced: 2 runs in our data, so the model has little to go on

## 2:40 Taunton | race_id rac_32305626340 | Mike Trickey & Geoff White Memorial Handicap Hurdle Race
Hurdle | Class 4 | 2m7f198y | going Good To Firm | Turf | 5 runners | rating band 0-115 | age 4yo+
DATA pace: Lone leader - Calvino is the only habitual front-runner and may be allowed an easy lead.
- Calvino (hrs_46850909) | 6yo G | 168lb | OR 113 | draw 0 | jockey Sam Twiston-Davies | trainer Paul Nicholls (14d 2/21) | headgear p | last run 29 days | form P13P-3 | MARKET 37.3% | 09:00 median 2.45 | Matchbook 2.58
    comment: Calvino arrives fresh from a third last time out, and he has won in his last five starts, a win four starts back, with a third three starts back underlining his ability.
    DATA: model 31.0% | style Leader (led 43% of runs) | runs in data 4 | last 3: 26 Feb Taunton Hurdle 19f Good To Soft 3/7; 24 Apr Fontwell Hurdle 21.7f Good PU/6; 28 Oct Newton Abbot Hurdle 21.5f Good To Soft 3/7 fig 109
    DATA for: Best recent form figure 109, 12 lb above field average; Official rating 113, 9 lb above field average; Pace: may get an uncontested lead
    DATA against: Carries 9 lb more than average; Pulled up in 1 of its last 4 jumps runs
- Lord Cauvelliere (hrs_51800336) | 5yo G | 142lb | OR 87 | draw 0 | jockey Callum Pritchard | trainer Sheila Lewis (14d 0/4) | headgear t | last run 14 days | form 56P741 | MARKET 23.7% | 09:00 median 3.75 | Matchbook 4.20
    comment: Won last time out and ran only 14 days ago, so he arrives fresh from success, but that came after a fourth, a seventh and a pulled up in his previous runs.
    DATA: model 14.9% | style Held up (led 3% of runs) | runs in data 7 | last 3: 17 Oct Stratford Hurdle 18.5f Good 7/7; 26 Oct Hereford Hurdle 19.5f Good To Firm 4/12 fig 66; 12 Nov Hereford Hurdle 25.5f Good To Firm 1/5 fig 79
    DATA for: Last-run finishing speed +2.2% vs that field (finished strongly); Has won at this trip or further; Carries 17 lb less than average
    DATA against: Best recent form figure 79, 18 lb below field average; Recent figures 8 lb below its current mark (looks high in the weights); Official rating 87, 17 lb below field average; Pulled up in 1 of its last 5 jumps runs
- Kandor (hrs_34253275) | 7yo G | 159lb | OR 104 | draw 0 | jockey Mr Daniel Williams(7) | trainer Nick Scholfield (14d 1/13) | headgear tp (1st time) | last run 10 days | form 21-455 | MARKET 15.2% | 09:00 median 6.00 | Matchbook 6.40
    comment: The risk is a pair of fifths in his last two outings while carrying 159 lb.
    DATA: model 13.0% | style Held up (led 5% of runs) | runs in data 3 | last 3: 19 May Huntingdon Chase 23.6f Good 4/7; 2 Nov Plumpton Hurdle 20.5f Good 5/7 fig 100; 16 Nov Plumpton Hurdle 20.5f Good To Soft 5/12 fig 98
    DATA for: Last-run finishing speed +4.8% vs that field (finished strongly); First-time headgear
- Tashan (hrs_46024832) | 5yo G | 166lb | OR 111 | draw 0 | jockey Adam Wedge | trainer Emma Lavelle (14d 2/21) | headgear - | last run 38 days | form 41PP-5 | MARKET 14.3% | 09:00 median 6.50 | Matchbook 6.80
    comment: Tashan showed he can win when landing a success four starts back, and he at least completed in fifth last time out after two pulled-up efforts, returning after 38 days off.
    DATA: model 19.3% | style Held up (led 5% of runs) | runs in data 2 | last 3: 4 Apr Haydock Hurdle 15.7f Good PU/11; 19 Oct Plumpton Hurdle 16f Good 5/5
    DATA for: Official rating 111, 7 lb above field average
    DATA against: Last-run finishing speed -5.7% vs that field (faded); Carries 7 lb more than average; Lightly raced: 2 runs in our data, so the model has little to go on; Pulled up in 1 of its last 2 jumps runs
- D'Jo Dela Barriere (hrs_35148904) | 7yo G | 159lb | OR 104 | draw 0 | jockey Miss Eleanor Williams(7) | trainer Mrs C. Williams (14d 0/23) | headgear - | last run 16 days | form 565-14 | MARKET 9.5% | 09:00 median 9.00 | Matchbook 11.00
    comment: The concern is a stable that is 0/23 in the last 14 days, while he carries 159 lb.
    DATA: model 21.8% | style Held up (led 3% of runs) | runs in data 5 | last 3: 30 Mar Ludlow Hurdle 21.2f Good 5/6; 26 Oct Hereford Hurdle 25.5f Good To Firm 1/8 fig 101; 10 Nov Lingfield Hurdle 23f Good 4/5 fig 97
    DATA for: Has won at this trip or further
    DATA against: Trainer 0 wins from 23 runs, last 14 days

## 3:15 Taunton | race_id rac_32305628277 | Christmas Sparkle Charity Raceday 10 December Open National Hunt Flat Race (Category 1 Elimination) (GBB Race)
NH Flat | Class 5 | 2m0f104y | going Good To Firm | Turf | 7 runners | rating band - | age 4-5yo
DATA pace: Unclear - Running styles known for only 2 of 7 runners.
- Handsome Stan (hrs_62393926) | 4yo G | 156lb | OR - | draw 0 | jockey Rian Corcoran(5) | trainer Mark Loughnane (14d 2/21) | headgear t | last run 195 days | form 51-4 | MARKET 25.0% | 09:00 median 3.50 | Matchbook 3.85 | CHECK (skip line 3.32)
    comment: The main risk is a 195-day absence, while 156 lb is a stiff burden.
    DATA: model 16.7% | style Unknown | runs in data 1 | last 3: 15 May Aintree NH Flat 16.9f Good 4/14
    DATA for: Last-run finishing speed +4.5% vs that field (finished strongly)
    DATA against: Returns from a 195-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Kilifi Creek (hrs_63457100) | 4yo G | 156lb | OR - | draw 0 | jockey Sam Twiston-Davies | trainer Paul Nicholls (14d 2/21) | headgear h (1st time) | last run 231 days | form 4- | MARKET 24.0% | 09:00 median 3.75 | Matchbook 3.90
    comment: Kilifi Creek signed off with a fourth last time out and has run over today's trip, while 156 lb is a stiff burden that needs carrying well.
    DATA: model 21.2% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 9 Apr Taunton NH Flat 16.5f Good 4/7
    DATA for: First-time headgear
    DATA against: Last-run finishing speed -2.0% vs that field (faded); Returns from a 231-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Powerful Act (hrs_17393904178) | 4yo G | 156lb | OR - | draw 0 | jockey Robbie David(5) | trainer Daisy Hitchins (14d 0/4) | headgear - | last run 23 days | form 2 | MARKET 18.7% | 09:00 median 4.33 | Matchbook 5.40
    comment: Powerful Act signed off with a second last time out just 23 days ago, so he arrives fresh and fit, and he has run over today's trip before.
    DATA: model 18.2% | style Unknown | runs in data 1 | last 3: 3 Nov Lingfield NH Flat 16f Standard / Slow 2/8 fig 109
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- French Fancy (hrs_17393555816) | 4yo G | 156lb | OR - | draw 0 | jockey Adam Wedge | trainer Mrs C. Williams (14d 0/23) | headgear - | last run 36 days | form 3 | MARKET 18.6% | 09:00 median 4.50 | Matchbook 5.30
    DATA: model 6.1% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 21 Oct Worcester NH Flat 16f Good To Soft 3/6 fig 105
    DATA against: Trainer 0 wins from 23 runs, last 14 days; Lightly raced: 1 run in our data, so the model has little to go on
- Hawkpitt (hrs_17395685622) | 4yo G | 156lb | OR - | draw 0 | jockey Jay Tidball(5) | trainer Zoe Hawkins (14d 0/1) | headgear - | last run - days | form - | MARKET 7.6% | 09:00 median 12.00 | Matchbook 12.50
    comment: Hawkpitt is an unraced gelding with no form to assess, so he arrives unexposed and open to improvement.
    DATA: model 13.0% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Snowy Hill (hrs_17395299712) | 5yo M | 149lb | OR - | draw 0 | jockey Mr Hugo Hunt(7) | trainer Keiran Burke (14d 0/1) | headgear - | last run - days | form - | MARKET 3.8% | 09:00 median 26.00 | Matchbook 25.00
    comment: Snowy Hill is unexposed, with no recorded form to go on, so this is a clean-slate debut and she looks open to improvement. She carries 149 lb, and her first run should reveal plenty.
    DATA: model 11.8% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Jack Dandy (hrs_17394539365) | 4yo G | 156lb | OR - | draw 0 | jockey Richie McLernon | trainer Jim & Suzi Best (14d 0/4) | headgear - | last run 214 days | form 35P- | MARKET 2.4% | 09:00 median 34.00 | Matchbook 55.00
    comment: Lightly raced and unexposed, Jack Dandy returns after 214 days off, having pulled up last time out, with a fifth two starts back and a third three starts back, so he could have more to offer. He is yet to win in his last three starts and carries 156 lb.
    DATA: model 13.0% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 214-day break; Lightly raced: 0 runs in our data, so the model has little to go on
