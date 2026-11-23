# Card review packet: Bangor-on-Dee, 2026-11-23

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
{"meeting": "bangor_on_dee", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 12:05 Bangor-on-Dee | race_id rac_32305359034 | Bangor-On-Dee 'Chasing Excellence' Beginners' Steeple Chase (GBB Race)
Chase | Class 3 | 2m1f77y | going Good To Soft | Turf | 4 runners | rating band - | age 4yo+
DATA pace: Even - Two likely leaders (Le Beau Madrik, Starmount). A fair, even gallop is most likely.
- Starmount (hrs_46483073) | 6yo G | 159lb | OR 134 | draw 0 | jockey Ben Jones | trainer Ben Pauling (14d 5/29) | headgear - | last run 268 days | form /141P- | MARKET 40.2% | 09:00 median 2.25 | Matchbook 2.44
    comment: The main risk is a 268-day layoff and a pulled-up effort last time out.
    DATA: model 36.6% | style Leader (led 57% of runs) | runs in data 2 | last 3: 22 Jan Wetherby Hurdle 16f Soft 1/12; 28 Feb Kelso Hurdle 18.1f Good To Soft PU/10
    DATA against: Returns from a 268-day break; Lightly raced: 2 runs in our data, so the model has little to go on; Pulled up in 1 of its last 2 jumps runs; First run over fences in our data
- Le Beau Madrik (hrs_52021438) | 5yo G | 159lb | OR 134 | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 15/80) | headgear - | last run 9 days | form P1-923 | MARKET 26.2% | 09:00 median 3.50 | Matchbook 3.75
    comment: Le Beau Madrik arrives in sound recent form, a third last time out and a second two starts back, just nine days after that run, and he has run over today's trip and on this going before. The main risk is the 159 lb he carries, which is a big burden off 134.
    DATA: model 19.1% | style Prominent (led 43% of runs) | runs in data 6 | last 3: 9 Oct Chepstow Hurdle 16.1f Good To Soft 9/17; 30 Oct Wetherby Chase 19.5f Good 2/2 fig 113; 14 Nov Wetherby Chase 15f Good 3/4 fig 131
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Race comments mention jumping mistakes in 3 of its last 5 runs; Pulled up in 1 of its last 5 jumps runs
- Count of Vendome (hrs_39959388) | 6yo G | 159lb | OR 123 | draw 0 | jockey Brian Hughes | trainer Donald McCain (14d 3/22) | headgear - | wind surgery | last run 24 days | form 1211-2 | MARKET 18.1% | 09:00 median 5.00 | Matchbook 5.40
    comment: Three wins in his last five starts, and a second last time out, make Count of Vendome a serious threat, having run over today's trip and going and returned after 24 days. The main risk is the 159 lb burden, which is a hefty load to carry.
    DATA: model 26.9% | style Midfield (led 4% of runs) | runs in data 5 | last 3: 13 Mar Doncaster Hurdle 16.6f Good To Soft 1/4; 15 Apr Haydock Hurdle 15.7f Good 1/7; 30 Oct Uttoxeter Chase 16f Good 2/3 fig 118
    DATA for: Good recent finishing positions
    DATA against: Official rating 123, 9 lb below field average
- Fiercely Proud (hrs_32278477) | 7yo G | 159lb | OR 136 | draw 0 | jockey Kielan Woods | trainer Ben Pauling (14d 5/29) | headgear - | wind surgery | last run 227 days | form 50100- | MARKET 15.5% | 09:00 median 5.50 | Matchbook 6.80
    DATA: model 17.4% | style Prominent (led 4% of runs) | runs in data 3 | last 3: 14 Feb Ascot Hurdle 19.3f Good To Soft 1/15; 13 Mar Cheltenham Hurdle 20.3f Good To Soft 12/24; 10 Apr Aintree Hurdle 20f Good To Soft 13/22
    DATA for: Has won at this trip or further
    DATA against: Returns from a 227-day break; First run over fences in our data

## 12:35 Bangor-on-Dee | race_id rac_32305360971 | Boat At Erbistock Handicap Steeple Chase (GBB Race)
Chase | Class 4 | 2m1f77y | going Good To Soft | Turf | 8 runners | rating band 0-110 | age 4yo+
DATA pace: Even - Two likely leaders (Kiwi Rush, Falco des Pins). A fair, even gallop is most likely.
- Air Apparent (hrs_39528881) | 6yo G | 159lb | OR 105 | draw 0 | jockey Brian Hughes | trainer Seamus Mullins (14d 2/12) | headgear - | last run 6 days | form 530-11 | MARKET 46.6% | 09:00 median 1.83 | Matchbook 2.06
    comment: The main risk is carrying 159 lb off an official mark of 105.
    DATA: model 16.6% | style Prominent (led 4% of runs) | runs in data 6 | last 3: 21 Apr Ffos Las Hurdle 23.9f Good 11/12; 27 Oct Bangor-on-Dee Chase 17.5f Good To Soft 1/9 fig 103; 17 Nov Carlisle Chase 16f Good To Soft 1/6 fig 116
    DATA for: Best recent form figure 116, 9 lb above field average; Recent figures 11 lb above its current mark (looks well handicapped); Has won at this trip or further; Good recent finishing positions
    DATA against: Race comments mention jumping mistakes in 2 of its last 5 runs
- Kartoon And Co (hrs_37476614) | 6yo G | 162lb | OR 108 | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 15/80) | headgear t | wind surgery | last run 22 days | form 2326/3 | MARKET 16.6% | 09:00 median 5.00 | Matchbook 6.00
    comment: Kartoon And Co has finished in the frame in four of his last five, including a third last time out and a second five starts back, and he returns fresh after 22 days having run over today's trip and going. The one concern is the 162 lb he carries, and he remains yet to win in that spell.
    DATA: model 12.4% | style Held up (led 8% of runs) | runs in data 1 | last 3: 1 Nov Worcester Chase 16.5f Good To Soft 3/10 fig 107
    DATA for: Last-run finishing speed +3.7% vs that field (finished strongly)
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Falco des Pins (hrs_37381309) | 6yo G | 156lb | OR 102 | draw 0 | jockey Charlie Deutsch | trainer Venetia Williams (14d 0/8) | headgear - | last run 27 days | form 3112-4 | MARKET 10.7% | 09:00 median 8.00 | Matchbook 9.20
    comment: Falco des Pins arrives in solid recent form, a fourth last time out following a second, and a winner three starts back and four starts back, and he has run over today's trip and going.
    DATA: model 15.6% | style Leader (led 72% of runs) | runs in data 5 | last 3: 6 Mar Leicester Chase 15.9f Good To Soft 1/4; 14 Mar Fontwell Chase 17.8f Soft 2/4; 27 Oct Bangor-on-Dee Chase 17.5f Good To Soft 4/9 fig 100
    DATA for: Good recent finishing positions
    DATA against: Best recent form figure 100, 7 lb below field average; Trainer 0 wins from 8 runs, last 14 days
- Gustapof (hrs_50188026) | 5yo G | 160lb | OR 106 | draw 0 | jockey Jamie Brace(5) | trainer Rebecca Curtis (14d 0/6) | headgear - | last run 32 days | form 8646-1 | MARKET 9.6% | 09:00 median 9.00 | Matchbook 9.80
    comment: Gustapof won last time out and has run over today's trip and going, but that came after a sixth, a fourth, another sixth and an eighth, and he carries 160 lb off an official 106.
    DATA: model 19.5% | style Held up (led 5% of runs) | runs in data 3 | last 3: 17 Feb Newbury Hurdle 20.5f Soft 4/12; 16 Mar Ffos Las Hurdle 20f Soft 6/8; 22 Oct Ffos Las Chase 19.5f Soft 1/9 fig 105
    DATA for: Has won at this trip or further
- Kiwi Rush (hrs_40920425) | 6yo G | 161lb | OR 107 | draw 0 | jockey Paul O'Brien | trainer Harry Derham (14d 2/11) | headgear tp | last run 22 days | form 5303-F | MARKET 7.2% | 09:00 median 12.00 | Matchbook 13.50
    comment: The fall last time is the one reservation, and he is yet to win in recent starts.
    DATA: model 11.3% | style Prominent (led 43% of runs) | runs in data 5 | last 3: 25 Feb Wincanton Hurdle 19.8f Good To Soft 14/15; 29 Mar Ascot Hurdle 23.6f Good 3/8; 1 Nov Worcester Chase 16.5f Good To Soft F/10
    DATA against: Race comments mention jumping mistakes in 2 of its last 5 runs; Fell or unseated in 1 of its last 5 jumps runs
- Jhentong Enki (hrs_34073081) | 7yo G | 161lb | OR 107 | draw 0 | jockey Ben Jones | trainer Ben Pauling (14d 5/29) | headgear - | last run 27 days | form 0110-P | MARKET 5.3% | 09:00 median 15.00 | Matchbook 20.00
    comment: Jhentong Enki won twice in a row three and four starts back, and he has run over today's trip, but a pulled up last time out and an unplaced run before that are the worry.
    DATA: model 8.8% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 27 Mar Wetherby Hurdle 21.3f Good 14/16; 27 Oct Bangor-on-Dee Chase 20.5f Good To Soft PU/13
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Pulled up in 1 of its last 2 jumps runs
- Cobbler's Boy (hrs_40352368) | 6yo G | 159lb | OR 105 | draw 0 | jockey Tabitha Worsley | trainer Sarah-Jayne Davies (14d 0/2) | headgear - | last run 16 days | form -12734 | MARKET 2.5% | 09:00 median 32.50 | Matchbook 42.00
    comment: Cobbler's Boy was a fourth last time out, after a third two starts back, and he has run over today's trip and going before, while a fresh 16 days since his last run suits.
    DATA: model 4.5% | style Prominent (led 29% of runs) | runs in data 10 | last 3: 21 Jun Hexham Chase 15.6f Good 7/7; 22 Aug Newton Abbot Chase 16.3f Good To Firm 3/4; 7 Nov Aintree Chase 16f Good To Soft 4/10 fig 105
- Jasmin de Cotte (hrs_34759858) | 7yo G | 157lb | OR 103 | draw 0 | jockey Ben Poste | trainer Tom Symonds (14d 0/3) | headgear - | last run 42 days | form 613-46 | MARKET 1.5% | 09:00 median 51.00 | Matchbook 85.00
    comment: Jasmin de Cotte won four starts back and was a third three starts back, but he has slipped to a fourth then a sixth since, and returns after 42 days carrying 157 lb.
    DATA: model 11.3% | style Held up (led 5% of runs) | runs in data 7 | last 3: 28 Mar Uttoxeter Chase 24f Good To Soft 3/10; 8 May Market Rasen Chase 21.4f Good 4/7; 12 Oct Worcester Chase 16.5f Good To Soft 6/6
    DATA for: Has won at this trip or further
    DATA against: Last-run finishing speed -6.0% vs that field (faded); Race comments mention jumping mistakes in 2 of its last 5 runs

## 1:05 Bangor-on-Dee | race_id rac_32305362908 | Bangor-On-Dee Memberships Now On Sale Novices' Handicap Steeple Chase (GBB Race)
Chase | Class 4 | 2m4f72y | going Good To Soft | Turf | 11 runners | rating band 0-120 | age 4yo+
DATA pace: Even - Two likely leaders (Hard Dealt, They Want Me). A fair, even gallop is most likely.
- Dig Deep (hrs_50906142) | 5yo G | 169lb | OR 121 | draw 0 | jockey Ben Jones | trainer Ben Pauling (14d 5/29) | headgear - | last run 254 days | form 22651- | MARKET 21.4% | 09:00 median 4.00 | Matchbook 4.40 | CHECK (skip line 3.80)
    comment: Dig Deep won last time out, with a fifth two starts back and a sixth three starts back before that, but he returns after 254 days off and carries 169 lb.
    DATA: model 12.2% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 23 Jan Doncaster Hurdle 19.4f Soft 5/13; 14 Mar Uttoxeter Hurdle 19.9f Soft 1/9
    DATA for: Official rating 121, 6 lb above field average; Last-run finishing speed +6.4% vs that field (finished strongly)
    DATA against: Carries 5 lb more than average; Returns from a 254-day break; Lightly raced: 2 runs in our data, so the model has little to go on; First run over fences in our data
- Hard Dealt (hrs_41052578) | 6yo M | 168lb | OR 113 | draw 0 | jockey Stan Sheppard | trainer Henry Daly (14d 2/14) | headgear - | last run 4 days | form 224-51 | MARKET 19.3% | 09:00 median 4.33 | Matchbook 4.90
    comment: Hard Dealt arrives in cracking nick, a winner last time out just four days ago, and she has also finished second twice in her last five starts.
    DATA: model 9.9% | style Leader (led 43% of runs) | runs in data 6 | last 3: 23 Apr Warwick Hurdle 21f Good 4/10; 27 Oct Bangor-on-Dee Hurdle 23f Good 5/9 fig 110; 19 Nov Warwick Chase 20f Soft 1/7 fig 122
    DATA for: Best recent form figure 122, 7 lb above field average; Recent figures 9 lb above its current mark (looks well handicapped); Last-run finishing speed +4.1% vs that field (finished strongly); Has won at this trip or further
- They Want Me (hrs_39431763) | 6yo G | 166lb | OR 118 | draw 0 | jockey Brian Hughes | trainer Donald McCain (14d 3/22) | headgear t | last run 27 days | form 1351-1 | MARKET 14.8% | 09:00 median 5.50 | Matchbook 6.20
    comment: Won last time out and two starts back, a winner three times in his last five starts, and he has run over today's trip and going, but he carries 166 lb off an official mark of 118.
    DATA: model 11.2% | style Leader (led 43% of runs) | runs in data 4 | last 3: 8 Mar Carlisle Hurdle 17f Good To Soft 5/10; 18 Apr Bangor-on-Dee Hurdle 19.6f Good 1/7; 27 Oct Bangor-on-Dee Chase 20.5f Good To Soft 1/13 fig 116
    DATA for: Has won at this trip or further; Good recent finishing positions
- Kingbel du Lion (hrs_37757902) | 6yo G | 167lb | OR 119 | draw 0 | jockey Charlie Deutsch | trainer Venetia Williams (14d 0/8) | headgear - | last run 635 days | form 731/ | MARKET 11.0% | 09:00 median 8.00 | Matchbook 8.40
    comment: Kingbel du Lion won last time out and was third two starts back, but he returns after 635 days off and carries 167 lb, which is a lot to ask on a comeback.
    DATA: model 7.7% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Trainer 0 wins from 8 runs, last 14 days; Returns from a 635-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Roi du Risk (hrs_46265562) | 5yo G | 162lb | OR 114 | draw 0 | jockey Richie McLernon | trainer Henrietta C Knight (14d 1/9) | headgear - | last run 39 days | form 2139-3 | MARKET 10.0% | 09:00 median 8.25 | Matchbook 9.80
    comment: The main risk is the 162 lb burden, which is a hefty load off an official mark of 114.
    DATA: model 7.0% | style Midfield (led 5% of runs) | runs in data 3 | last 3: 1 Feb Market Rasen Hurdle 20.6f Soft 3/7; 7 Mar Sandown Hurdle 19.8f Soft 9/17; 15 Oct Fontwell Chase 19.5f Good To Soft 3/7 fig 114
    DATA for: Last-run finishing speed +4.1% vs that field (finished strongly); Good recent finishing positions
- Berkenshtaaap (hrs_41596975) | 6yo G | 163lb | OR 115 | draw 0 | jockey Kevin Brogan | trainer Olly Murphy (14d 10/50) | headgear - | last run 39 days | form 4041-1 | MARKET 6.5% | 09:00 median 12.00 | Matchbook 15.50
    comment: Berkenshtaaap arrives a double winner, successful last time out and two starts back, with experience of today's trip and going, but he carries 163 lb off 115 and has had 39 days off.
    DATA: model 11.6% | style Held up (led 8% of runs) | runs in data 3 | last 3: 5 Mar Haydock Hurdle 21.2f Good To Soft 4/9; 24 Apr Perth Hurdle 20.2f Good 1/10; 15 Oct Perth Chase 20f Soft 1/7 fig 109
    DATA for: Trainer 20% wins (10/50), last 14 days; Has won at this trip or further; Good recent finishing positions
    DATA against: Best recent form figure 109, 6 lb below field average; Recent figures 6 lb below its current mark (looks high in the weights)
- The Burren Man (hrs_52055472) | 5yo G | 163lb | OR 115 | draw 0 | jockey Paul O'Brien | trainer Harry Derham (14d 2/11) | headgear ht | last run 22 days | form 2/14-0 | MARKET 6.2% | 09:00 median 13.00 | Matchbook 16.00
    comment: The Burren Man built on a second four starts back to win next time, though he has tailed off since, with a fourth two starts back and unplaced last time out.
    DATA: model 6.6% | style Unknown | runs in data 2 | last 3: 17 Jan Ascot Hurdle 21.7f Soft 4/8; 1 Nov Worcester Chase 20f Good To Soft 11/13
    DATA against: Last-run finishing speed -3.6% vs that field (faded); Lightly raced: 2 runs in our data, so the model has little to go on
- French Emperor (hrs_40646956) | 6yo G | 168lb | OR 120 | draw 0 | jockey Sean Houlihan | trainer Nicky Martin (14d 0/0) | headgear - | last run 247 days | form 17381- | MARKET 4.8% | 09:00 median 17.00 | Matchbook 21.00
    comment: The main risk is a long 247-day absence, with 168 lb to carry as well.
    DATA: model 11.4% | style Midfield (led 29% of runs) | runs in data 3 | last 3: 27 Jan Chepstow Hurdle 19.5f Soft 3/10; 6 Mar Exeter Hurdle 16.7f Good To Soft 8/10; 21 Mar Bangor-on-Dee Hurdle 23.1f Good 1/6
    DATA for: Last-run finishing speed +2.7% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Returns from a 247-day break; First run over fences in our data
- Chasing Glance (hrs_35054614) | 8yo G | 167lb | OR 119 | draw 0 | jockey Finn Lambert(3) | trainer Tom Ellis (14d 1/9) | headgear t | wind surgery | last run 261 days | form 1/524- | MARKET 3.2% | 09:00 median 26.00 | Matchbook 32.00
    comment: On the plus side, he was fourth last time out, a second two starts back, and has run over today's trip and going.
    DATA: model 9.6% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 7 Feb Warwick Hurdle 19f Heavy 2/7; 7 Mar Hereford Hurdle 19.7f Good 4/12
    DATA against: Returns from a 261-day break; Lightly raced: 2 runs in our data, so the model has little to go on; First run over fences in our data
- Cedar Row (hrs_29312794) | 9yo G | 155lb | OR 107 | draw 0 | jockey Danny McMenamin | trainer Joel Parkinson & Sue Smith (14d 1/13) | headgear - | last run 915 days | form 5515F/ | MARKET 1.8% | 09:00 median 41.00 | Matchbook 70.00
    comment: Cedar Row is hard to fancy after a fall last time out and a 915-day absence, while his recent form before that reads fifth and a win three starts back, so fitness is a huge question.
    DATA: model 6.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Carries 9 lb less than average
    DATA against: Official rating 107, 8 lb below field average; Returns from a 915-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Lord Roco (hrs_24040072) | 10yo G | 156lb | OR 108 | draw 0 | jockey James Best | trainer Barry Murphy (14d 0/5) | headgear - | last run 639 days | form PP23U/ | MARKET 1.0% | 09:00 median 67.00 | Matchbook 140.00
    comment: The main risk is a 639-day absence, which makes fitness a major question under 156 lb.
    DATA: model 6.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Carries 8 lb less than average
    DATA against: Official rating 108, 7 lb below field average; Returns from a 639-day break; Lightly raced: 0 runs in our data, so the model has little to go on; Aged 10, older than most of this field

## 1:35 Bangor-on-Dee | race_id rac_32305364845 | Wrexham Lager Novices' Handicap Steeple Chase (GBB Race)
Chase | Class 4 | 3m0f30y | going Good To Soft | Turf | 12 runners | rating band 0-120 | age 4yo+
DATA pace: Strong pace - 3 habitual front-runners (Skuna Bay, De Kingpin, Outer Banks). A contested lead should set things up for horses coming from behind.
- Knead A Win (hrs_46233222) | 6yo G | 170lb | OR 122 | draw 0 | jockey Dylan Johnston | trainer Sam Thomas (14d 1/3) | headgear t | last run 225 days | form 23/22- | MARKET 14.7% | 09:00 median 5.00 | Matchbook 6.80 | CHECK (skip line 4.75)
    comment: Knead A Win has been in the frame in each of his last four starts, finishing second last time out, second two starts back, third three starts back and second four starts back, yet he's winless in that spell. Against that, a 225-day absence and 170 lb are hurdles, though he has run on today's going.
    DATA: model 20.3% | style Unknown | runs in data 1 | last 3: 12 Apr Ffos Las Hurdle 20f Good To Soft 2/11
    DATA for: Official rating 122, 10 lb above field average; Last-run finishing speed +2.5% vs that field (finished strongly)
    DATA against: Carries 10 lb more than average; Returns from a 225-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Escort'kheops (hrs_40920411) | 6yo G | 160lb | OR 112 | draw 0 | jockey Bryan Carver | trainer Laura Horsfall (14d 0/4) | headgear - | last run 27 days | form 4212-3 | MARKET 14.5% | 09:00 median 5.50 | Matchbook 6.40
    comment: Escort'kheops arrives in cracking recent form, third last time out, a second two starts back and a winner three starts back, and he has run over today's trip and going.
    DATA: model 10.3% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 16 Mar Plumpton Hurdle 20.5f Good To Soft 1/8; 31 Mar Bangor-on-Dee Hurdle 23.1f Good 2/8; 27 Oct Bangor-on-Dee Chase 20.5f Good To Soft 3/13 fig 112
    DATA for: Best recent form figure 112, 5 lb above field average; Good recent finishing positions
    DATA against: Race comments mention jumping mistakes in 2 of its last 5 runs
- Douglas Hyde (hrs_40352375) | 6yo G | 156lb | OR 108 | draw 0 | jockey Jamie Brace(5) | trainer Rebecca Curtis (14d 0/6) | headgear - | last run 248 days | form 33228- | MARKET 13.5% | 09:00 median 6.00 | Matchbook 6.80
    comment: Douglas Hyde is winless in his last five and was eighth last time out, then returns after 248 days off, which makes him hard to fancy under 156 lb.
    DATA: model 6.5% | style Prominent (led 38% of runs) | runs in data 2 | last 3: 11 Feb Hereford Hurdle 25.5f Heavy 2/3; 20 Mar Newbury Hurdle 24.3f Good To Soft 8/14
    DATA against: Last-run finishing speed -2.8% vs that field (faded); Returns from a 248-day break; Lightly raced: 2 runs in our data, so the model has little to go on; First run over fences in our data
- Crystello (hrs_50188887) | 5yo G | 151lb | OR 103 | draw 0 | jockey Paul O'Brien | trainer Harry Derham (14d 2/11) | headgear t | last run 32 days | form 4514-3 | MARKET 13.1% | 09:00 median 6.00 | Matchbook 7.20
    comment: Crystello was third last time out and has a win three starts back, with a fourth and a fifth either side, so the form is respectable but not sharp.
    DATA: model 12.1% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 15 Feb Musselburgh Hurdle 23.8f Soft 1/6; 26 Mar Chepstow Hurdle 23.6f Good To Soft 4/15; 22 Oct Ffos Las Chase 19.5f Soft 3/9 fig 97
    DATA for: Has won at this trip or further; Good recent finishing positions; Carries 10 lb less than average
    DATA against: Best recent form figure 97, 10 lb below field average; Recent figures 6 lb below its current mark (looks high in the weights); Official rating 103, 10 lb below field average
- De Kingpin (hrs_34665197) | 7yo G | 160lb | OR 112 | draw 0 | jockey Ben Jones | trainer Ben Pauling (14d 5/29) | headgear - | last run 248 days | form 4P315- | MARKET 8.2% | 09:00 median 9.50 | Matchbook 11.50
    comment: The main risk is a 248-day absence, with a fifth last time out and 160 lb to carry.
    DATA: model 12.9% | style Leader (led 54% of runs) | runs in data 3 | last 3: 14 Jan Newbury Hurdle 24.3f Good To Soft 3/17; 17 Feb Newbury Hurdle 20.5f Soft 1/12; 20 Mar Newbury Hurdle 24.3f Good To Soft 5/14
    DATA for: Good recent finishing positions
    DATA against: Returns from a 248-day break; First run over fences in our data; Pace: likely to be taken on for the lead
- Top Guy (hrs_412693680) | 6yo G | 162lb | OR 114 | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 15/80) | headgear - | last run 27 days | form 216-35 | MARKET 7.5% | 09:00 median 9.75 | Matchbook 14.00
    comment: Top Guy has shown mixed form, winning four starts back and finishing third two starts back, and he has run over today's trip and going, but a fifth last time out and a hefty 162 lb leave him with plenty to prove.
    DATA: model 4.5% | style Held up (led 5% of runs) | runs in data 7 | last 3: 19 Apr Plumpton Hurdle 25f Good 6/10; 12 Oct Worcester Chase 23f Good To Soft 3/5; 27 Oct Bangor-on-Dee Chase 20.5f Good To Soft 5/13 fig 101
    DATA for: Has won at this trip or further; Pace: a contested lead should suit its hold-up style
    DATA against: Best recent form figure 101, 6 lb below field average; Recent figures 13 lb below its current mark (looks high in the weights); Last-run finishing speed -3.2% vs that field (faded)
- Sole Solution (hrs_33051480) | 8yo G | 160lb | OR 112 | draw 0 | jockey Charlie Deutsch | trainer Venetia Williams (14d 0/8) | headgear - | last run 296 days | form /3555- | MARKET 6.5% | 09:00 median 12.00 | Matchbook 15.00
    comment: The main risk is a 296-day layoff, with 160 lb on his back too.
    DATA: model 6.3% | style Unknown | runs in data 2 | last 3: 22 Jan Huntingdon Hurdle 25f Soft 5/6; 31 Jan Sandown Hurdle 23.5f Soft 5/11
    DATA against: Trainer 0 wins from 8 runs, last 14 days; Last-run finishing speed -14.1% vs that field (faded); Returns from a 296-day break; Lightly raced: 2 runs in our data, so the model has little to go on; Race comments mention jumping mistakes in 2 of its last 2 runs; First run over fences in our data
- Joltin N Jiving (hrs_40786627) | 6yo G | 164lb | OR 116 | draw 0 | jockey Brian Hughes | trainer Donald McCain (14d 3/22) | headgear - | last run 22 days | form 552-43 | MARKET 6.3% | 09:00 median 12.00 | Matchbook 15.50
    comment: Joltin N Jiving arrives in solid order, third last time out and a second three starts back, with just 22 days since that run and experience of today's going.
    DATA: model 6.5% | style Prominent (led 23% of runs) | runs in data 4 | last 3: 13 Mar Doncaster Hurdle 20.8f Good To Soft 2/7; 4 Jun Uttoxeter Chase 20.9f Good 4/5; 1 Nov Carlisle Chase 21f Good 3/4 fig 111
    DATA for: Best recent form figure 111, 4 lb above field average; Good recent finishing positions
- Skuna Bay (hrs_37790130) | 7yo G | 167lb | OR 119 | draw 0 | jockey Kielan Woods | trainer Donald McCain (14d 3/22) | headgear - | last run 270 days | form /1524- | MARKET 6.2% | 09:00 median 12.00 | Matchbook 16.00
    comment: Skuna Bay signed off with a fourth last time out, after a second two starts back and a win four starts back, and he has run over today's trip and on this going. The big risk is a 270-day absence, though he looks a strong threat on a mark of 119.
    DATA: model 9.2% | style Leader (led 57% of runs) | runs in data 2 | last 3: 20 Jan Leicester Hurdle 20.5f Heavy 2/8; 26 Feb Wetherby Hurdle 24.1f Soft 4/10
    DATA for: Official rating 119, 6 lb above field average; Last-run finishing speed +3.5% vs that field (finished strongly)
    DATA against: Carries 6 lb more than average; Returns from a 270-day break; Lightly raced: 2 runs in our data, so the model has little to go on; First run over fences in our data; Pace: likely to be taken on for the lead
- Leading Choice (hrs_27139714) | 9yo G | 156lb | OR 108 | draw 0 | jockey Sean Houlihan | trainer Nicky Martin (14d 0/0) | headgear - | last run 37 days | form 9/33-3 | MARKET 3.7% | 09:00 median 21.00 | Matchbook 26.00
    comment: Leading Choice arrives with three straight thirds, so he's consistent, and he has run on today's going before, though he's yet to win in his last four starts.
    DATA: model 2.3% | style Held up (led 5% of runs) | runs in data 3 | last 3: 17 Feb Newbury Chase 16.4f Soft 3/3; 25 Feb Bangor-on-Dee Chase 17.4f Soft 3/3; 17 Oct Newton Abbot Chase 21f Good 3/4 fig 114
    DATA for: Best recent form figure 114, 7 lb above field average; Recent figures 6 lb above its current mark (looks well handicapped); Good recent finishing positions; Pace: a contested lead should suit its hold-up style
    DATA against: Last-run finishing speed -2.6% vs that field (faded); Aged 9, older than most of this field
- Patrick's Wells (hrs_34253653) | 7yo G | 160lb | OR 112 | draw 0 | jockey Danny McMenamin | trainer Joel Parkinson & Sue Smith (14d 1/13) | headgear p (1st time) | last run 22 days | form 0/33-4 | MARKET 3.2% | 09:00 median 23.00 | Matchbook 34.00
    comment: He has run over today's trip and going, but 160 lb is a hefty burden.
    DATA: model 3.5% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 4 Apr Carlisle Hurdle 19.3f Good 3/10; 18 Apr Bangor-on-Dee Hurdle 23.1f Good 3/5; 1 Nov Carlisle Chase 21f Good 4/4
    DATA for: Good recent finishing positions; First-time headgear
    DATA against: Last-run finishing speed -5.7% vs that field (faded)
- Outer Banks (hrs_39826871) | 6yo G | 160lb | OR 112 | draw 0 | jockey Lorcan Williams | trainer Stuart Edmunds (14d 1/11) | headgear - | wind surgery | last run 263 days | form 61/P7- | MARKET 2.6% | 09:00 median 29.00 | Matchbook 40.00
    comment: Outer Banks is hard to fancy after a seventh last time out and a pulled up two starts back, with 263 days off the track adding to the doubts.
    DATA: model 5.6% | style Leader (led 38% of runs) | runs in data 2 | last 3: 1 Feb Market Rasen Hurdle 23.1f Soft PU/7; 5 Mar Haydock Hurdle 24.3f Good To Soft 7/9
    DATA against: Last-run finishing speed -5.2% vs that field (faded); Returns from a 263-day break; Lightly raced: 2 runs in our data, so the model has little to go on; Pulled up in 1 of its last 2 jumps runs; First run over fences in our data; Pace: likely to be taken on for the lead

## 2:07 Bangor-on-Dee | race_id rac_32305366782 | Outerspace Group 'National Hunt' Maiden Hurdle Race (GBB Race)
Hurdle | Class 4 | 2m3f123y | going Good To Soft | Turf | 14 runners | rating band - | age 4yo+
DATA pace: Lone leader - Looking For Eight is the only habitual front-runner and may be allowed an easy lead.
- Grande J (hrs_17395068166) | 5yo G | 159lb | OR - | draw 0 | jockey Jamie Brace(5) | trainer Rebecca Curtis (14d 0/6) | headgear - | wind surgery | last run 289 days | form 1- | MARKET 25.4% | 09:00 median 3.00 | Matchbook 3.65 | CHECK (skip line 2.85)
    DATA: model 6.3% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 289-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Jetzet (hrs_62516538) | 4yo G | 158lb | OR - | draw 0 | jockey Kielan Woods | trainer Kim Bailey & Mat Nicholls (14d 4/18) | headgear t | last run 21 days | form 33-3 | MARKET 24.3% | 09:00 median 3.50 | Matchbook 3.55
    DATA: model 10.2% | style Prominent (led 4% of runs) | runs in data 3 | last 3: 13 Mar Doncaster NH Flat 16.6f Good To Soft 3/6; 18 Apr Bangor-on-Dee NH Flat 16.7f Good 3/11; 2 Nov Southwell Hurdle 16f Good 3/14 fig 110
    DATA for: Best recent form figure 110, 9 lb above field average; Trainer 22% wins (4/18), last 14 days; Last-run finishing speed +3.5% vs that field (finished strongly); Good recent finishing positions
- Hunting Call (hrs_17395095284) | 5yo G | 159lb | OR - | draw 0 | jockey Ben Jones | trainer Ben Pauling (14d 5/29) | headgear - | last run 203 days | form P-1 | MARKET 16.6% | 09:00 median 5.00 | Matchbook 5.30
    DATA: model 6.3% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 203-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Dylans Moon (hrs_62170871) | 6yo G | 159lb | OR - | draw 0 | jockey Finn Lambert(3) | trainer Tom Ellis (14d 1/9) | headgear - | last run 216 days | form 3F- | MARKET 8.7% | 09:00 median 9.50 | Matchbook 10.50
    DATA: model 5.3% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 14 Mar Uttoxeter Hurdle 19.9f Soft 3/9; 21 Apr Ffos Las Hurdle 20f Good F/12
    DATA against: Returns from a 216-day break; Lightly raced: 2 runs in our data, so the model has little to go on; Fell or unseated in 1 of its last 2 jumps runs
- Seeyasunday (hrs_17395400883) | 5yo G | 159lb | OR - | draw 0 | jockey Jack Tudor | trainer Oliver Greenall & Josh Guerriero (14d 2/10) | headgear - | last run 328 days | form 3- | MARKET 5.3% | 09:00 median 13.00 | Matchbook 21.00
    DATA: model 6.3% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 20% wins (2/10), last 14 days
    DATA against: Returns from a 328-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- The Gift Shop (hrs_17394535193) | 5yo G | 159lb | OR - | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 15/80) | headgear - | last run 26 days | form 1-6 | MARKET 5.2% | 09:00 median 12.50 | Matchbook 23.00
    DATA: model 8.4% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 28 Oct Newton Abbot NH Flat 17f Good To Soft 6/7 fig 91
    DATA against: Best recent form figure 91, 10 lb below field average; Last-run finishing speed -3.8% vs that field (faded); Lightly raced: 1 run in our data, so the model has little to go on
- Soldiers Trick (hrs_17394722933) | 5yo G | 159lb | OR - | draw 0 | jockey Brian Hughes | trainer Donald McCain (14d 3/22) | headgear - | last run 22 days | form 1-4 | MARKET 2.7% | 09:00 median 23.00 | Matchbook 48.00
    DATA: model 6.9% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 1 Nov Carlisle NH Flat 17f Good To Soft 4/7 fig 102
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Dukeboxrock (hrs_59742130) | 5yo G | 159lb | OR - | draw 0 | jockey Dylan Johnston | trainer Rebecca Curtis (14d 0/6) | headgear - | last run 242 days | form 55- | MARKET 2.4% | 09:00 median 34.00 | Matchbook 44.00
    DATA: model 5.4% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 24 Jan Doncaster NH Flat 16.6f Soft 5/7; 26 Mar Chepstow NH Flat 16.1f Good To Soft 5/10
    DATA against: Returns from a 242-day break; Lightly raced: 2 runs in our data, so the model has little to go on; First run over hurdles in our data
- Lord des Fresnes (hrs_17395919254) | 5yo G | 159lb | OR - | draw 0 | jockey Charlie Maggs | trainer Oliver Greenall & Josh Guerriero (14d 2/10) | headgear - | last run 303 days | form 44- | MARKET 2.0% | 09:00 median 34.00 | Matchbook 65.00
    DATA: model 6.3% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 20% wins (2/10), last 14 days
    DATA against: Returns from a 303-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Looking For Eight (hrs_59961461) | 5yo G | 159lb | OR - | draw 0 | jockey James Best | trainer Sarah-Jayne Davies (14d 0/2) | headgear - | wind surgery | last run 263 days | form 23- | MARKET 1.9% | 09:00 median 34.00 | Matchbook 70.00
    DATA: model 16.6% | style Leader (led 57% of runs) | runs in data 1 | last 3: 5 Mar Thurles NH Flat 16.6f Soft To Heavy 3/8
    DATA for: Last-run finishing speed +7.7% vs that field (finished strongly); Pace: may get an uncontested lead
    DATA against: Returns from a 263-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Always Stronger (hrs_40920292) | 6yo G | 159lb | OR - | draw 0 | jockey Lorcan Williams | trainer Stuart Edmunds (14d 1/11) | headgear - | last run 255 days | form 3/83- | MARKET 1.7% | 09:00 median 41.00 | Matchbook 85.00
    DATA: model 7.1% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 18 Feb Southwell Hurdle 20.4f Soft 8/13; 13 Mar Fakenham Hurdle 16f Good To Soft 3/5
    DATA against: Last-run finishing speed -3.4% vs that field (faded); Returns from a 255-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- Good Times Roll (hrs_17395675192) | 4yo G | 158lb | OR - | draw 0 | jockey Sean Houlihan | trainer Richard Mitford-Slade (14d 0/1) | headgear - | last run 246 days | form 6- | MARKET 1.6% | 09:00 median 51.00 | Matchbook 70.00
    DATA: model 6.2% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 246-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- George's Maze (hrs_17395917168) | 6yo G | 159lb | OR - | draw 0 | jockey Ellis Collier(5) | trainer Christian Williams (14d 1/7) | headgear - | last run - days | form - | MARKET 1.4% | 09:00 median 51.00 | Matchbook 120.00
    DATA: model 6.3% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Upweitjack (hrs_63809508) | 4yo G | 158lb | OR - | draw 0 | jockey Charlie Deutsch | trainer Mel Rowley (14d 0/6) | headgear - | last run 219 days | form 0- | MARKET 0.8% | 09:00 median 101.00 | Matchbook 240.00
    DATA: model 2.7% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 18 Apr Bangor-on-Dee NH Flat 16.7f Good 11/11
    DATA against: Last-run finishing speed -4.7% vs that field (faded); Returns from a 219-day break; Lightly raced: 1 run in our data, so the model has little to go on

## 2:42 Bangor-on-Dee | race_id rac_32305368719 | Mount Vines Mares' Maiden Hurdle Race (GBB Race)
Hurdle | Class 4 | 2m0f145y | going Good To Soft | Turf | 13 runners | rating band - | age 4yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Mille Et Une Vies (hrs_51491902) | 4yo F | 156lb | OR 135 | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 15/80) | headgear - | last run 256 days | form 32/20- | MARKET 50.2% | 09:00 median 1.67 | Matchbook 1.83
    DATA: model 13.3% | style Unknown | runs in data 1 | last 3: 12 Mar Cheltenham Hurdle 16.8f Good 18/22
    DATA against: Last-run finishing speed -3.2% vs that field (faded); Returns from a 256-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Aeropress (hrs_17394074187) | 4yo F | 156lb | OR - | draw 0 | jockey Paul O'Brien | trainer Harry Derham (14d 2/11) | headgear - | last run 33 days | form U-4 | MARKET 19.6% | 09:00 median 3.75 | Matchbook 5.30
    DATA: model 15.8% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 21 Oct Worcester Hurdle 16f Good To Soft 4/10 fig 97
    DATA for: Best recent form figure 97, 8 lb above field average; Last-run finishing speed +5.0% vs that field (finished strongly)
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Perfect Package (hrs_17395401926) | 5yo M | 156lb | OR - | draw 0 | jockey Ben Jones | trainer Ben Pauling (14d 5/29) | headgear - | last run 624 days | form 3/ | MARKET 12.5% | 09:00 median 6.50 | Matchbook 7.80
    DATA: model 5.3% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 624-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Madam To You (hrs_62393863) | 4yo F | 156lb | OR - | draw 0 | jockey Cameron Iles(5) | trainer Tom Lacey (14d 2/9) | headgear - | last run 267 days | form 1- | MARKET 6.2% | 09:00 median 13.00 | Matchbook 16.00
    DATA: model 5.3% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 22% wins (2/9), last 14 days
    DATA against: Returns from a 267-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Play It Again (hrs_49821632) | 5yo M | 156lb | OR 108 | draw 0 | jockey Brian Hughes | trainer Warren Greatrex (14d 6/20) | headgear h | wind surgery | last run 583 days | form 229P/ | MARKET 3.7% | 09:00 median 19.00 | Matchbook 38.00
    DATA: model 10.1% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 30% wins (6/20), last 14 days
    DATA against: Returns from a 583-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Crazy Alice (hrs_17394677041) | 4yo F | 156lb | OR - | draw 0 | jockey Stan Sheppard | trainer Tom Lacey (14d 2/9) | headgear - | last run 24 days | form 1-8 | MARKET 2.0% | 09:00 median 34.00 | Matchbook 65.00
    DATA: model 9.2% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 30 Oct Uttoxeter Hurdle 16f Good 8/13 fig 86
    DATA for: Trainer 22% wins (2/9), last 14 days
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Mysti Meadow (hrs_59246943) | 5yo M | 156lb | OR - | draw 0 | jockey Charlie Deutsch | trainer Mel Rowley (14d 0/6) | headgear - | last run 215 days | form 54- | MARKET 1.7% | 09:00 median 41.00 | Matchbook 85.00
    DATA: model 16.9% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 22 Apr Ludlow NH Flat 15.8f Good 4/14
    DATA for: Last-run finishing speed +3.8% vs that field (finished strongly)
    DATA against: Returns from a 215-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Vale of Tears (hrs_52055920) | 5yo M | 156lb | OR - | draw 0 | jockey Jack Tudor | trainer Christian Williams (14d 1/7) | headgear - | last run 271 days | form 4/6- | MARKET 0.9% | 09:00 median 67.00 | Matchbook 200.00
    DATA: model 3.3% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 25 Feb Bangor-on-Dee Hurdle 16.7f Soft 6/10
    DATA against: Returns from a 271-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Lady Boujee (hrs_58993228) | 5yo M | 156lb | OR - | draw 0 | jockey Liam Harrison | trainer Dan Skelton (14d 15/80) | headgear h | last run 20 days | form 265-68 | MARKET 0.9% | 09:00 median 67.00 | Matchbook 200.00
    DATA: model 6.7% | style Held up (led 3% of runs) | runs in data 4 | last 3: 28 Feb Newbury NH Flat 16.3f Good To Soft 5/8; 18 Oct Sedgefield Hurdle 17f Good 6/8 fig 85; 3 Nov Lingfield Hurdle 16f Good 8/11 fig 85
    DATA against: Best recent form figure 85, 4 lb below field average; Pace: steady gallop likely, hard to come from off the pace
- Shadow Love (hrs_17394076273) | 4yo F | 156lb | OR - | draw 0 | jockey Fern O'Brien(5) | trainer Dan Skelton (14d 15/80) | headgear - | last run 10 days | form 86 | MARKET 0.7% | 09:00 median 101.00 | Matchbook 300.00
    DATA: model 2.3% | style Held up (led 8% of runs) | runs in data 2 | last 3: 21 Oct Worcester Hurdle 16f Good To Soft 8/9; 13 Nov Southwell Hurdle 16f Good 6/7
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Another Vega (hrs_17394675998) | 4yo F | 156lb | OR - | draw 0 | jockey Kielan Woods | trainer Dan Skelton (14d 15/80) | headgear - | last run 10 days | form 05 | MARKET 0.7% | 09:00 median 101.00 | Matchbook 190.00
    DATA: model 3.9% | style Held up (led 5% of runs) | runs in data 2 | last 3: 30 Oct Uttoxeter Hurdle 16f Good 11/13; 13 Nov Southwell Hurdle 16f Good 5/7
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Mysteriosa (hrs_61975389) | 4yo F | 156lb | OR - | draw 0 | jockey Shane Fitzgerald | trainer Katy Price (14d 0/1) | headgear t | last run 28 days | form 0P-6 | MARKET 0.5% | 09:00 median 201.00 | Matchbook 380.00
    DATA: model 2.8% | style Held up (led 5% of runs) | runs in data 3 | last 3: 25 Feb Wincanton NH Flat 15.2f Good To Soft 11/14; 7 Apr Exeter NH Flat 16.7f Good PU/6; 26 Oct Hereford Hurdle 16f Good To Firm 6/12
    DATA against: Poor recent finishing positions; Pace: steady gallop likely, hard to come from off the pace
- Gaelic Heather (hrs_50402611) | 5yo M | 156lb | OR - | draw 0 | jockey Finn Lambert(3) | trainer Tom Ellis (14d 1/9) | headgear - | last run 18 days | form 2/4-9 | MARKET 0.5% | 09:00 median 201.00 | Matchbook 380.00
    DATA: model 5.0% | style Prominent (led 38% of runs) | runs in data 2 | last 3: 13 Apr Hexham NH Flat 16.2f Good 4/7; 5 Nov Newbury Hurdle 16.5f Good To Soft 9/10
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on

## 3:17 Bangor-on-Dee | race_id rac_32305370656 | Festive Meeting Saturday 28th November 'Newcomers' National Hunt Flat Race (GBB Race)
NH Flat | Class 4 | 2m0f145y | going Good To Soft | Turf | 7 runners | rating band - | age 4-5yo
DATA pace: Unclear - Running styles known for only 0 of 7 runners.
- Caveman (hrs_17394128423) | 4yo G | 156lb | OR - | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 15/80) | headgear - | last run - days | form - | MARKET 38.4% | 09:00 median 2.25 | Matchbook 2.52
    comment: Caveman is an unraced debutant with no form to go on, so he's an unexposed type who could easily improve. He carries 156 lb, and his first run should reveal plenty.
    DATA: model 14.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Cross Allegation (hrs_17395671020) | 4yo G | 156lb | OR - | draw 0 | jockey Ben Jones | trainer Ben Pauling (14d 5/29) | headgear - | last run - days | form - | MARKET 23.7% | 09:00 median 3.75 | Matchbook 3.90
    comment: Cross Allegation is a debutant with no recorded form, so he is completely unexposed and open to improvement. He carries 156 lb, and his first run should show how much progress there is to come.
    DATA: model 14.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Ghost Face (hrs_62779388) | 5yo G | 156lb | OR - | draw 0 | jockey Brian Hughes | trainer Donald McCain (14d 3/22) | headgear - | last run - days | form - | MARKET 14.6% | 09:00 median 6.00 | Matchbook 6.80
    comment: He shoulders 156 lb on debut, with nothing yet to show how he handles it.
    DATA: model 14.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Pether's Angel (hrs_64938125) | 4yo F | 149lb | OR - | draw 0 | jockey Aamilah Aswat(7) | trainer Kim Bailey & Mat Nicholls (14d 4/18) | headgear - | last run - days | form - | MARKET 9.7% | 09:00 median 9.00 | Matchbook 9.80
    comment: She carries 149 lb on debut, and the lack of any form means this is all about potential.
    DATA: model 13.2% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 22% wins (4/18), last 14 days
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Pelegro (hrs_17395923426) | 4yo C | 156lb | OR - | draw 0 | jockey Charlie Deutsch | trainer Mel Rowley (14d 0/6) | headgear - | last run - days | form - | MARKET 5.5% | 09:00 median 15.00 | Matchbook 18.50
    comment: Pelegro is an unraced colt with no form to go on, so he's an unexposed type who is open to improvement.
    DATA: model 14.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Bellshill Boy (hrs_17395665805) | 4yo G | 156lb | OR - | draw 0 | jockey Peter Kavanagh | trainer Donald McCain (14d 3/22) | headgear - | last run - days | form - | MARKET 5.2% | 09:00 median 17.00 | Matchbook 19.50
    comment: Bellshill Boy is an unexposed debutant with no form to go on, so he is open to any amount of improvement. He carries 156 lb on his first outing, and what he shows will be the first guide to his ability.
    DATA: model 14.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Kit Carson (hrs_17395688751) | 4yo G | 156lb | OR - | draw 0 | jockey James Best | trainer Richard Mitford-Slade (14d 0/1) | headgear - | last run - days | form - | MARKET 3.0% | 09:00 median 35.00 | Matchbook 38.00
    comment: Kit Carson is an unexposed debutant with no form to assess, so he's very much an unknown quantity. Carrying 156 lb, he arrives open to improvement and there's plenty to learn about him.
    DATA: model 14.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
