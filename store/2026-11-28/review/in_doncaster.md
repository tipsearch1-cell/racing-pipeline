# Card review packet: Doncaster, 2026-11-28

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
{"meeting": "doncaster", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 11:33 Doncaster | race_id rac_32305860717 | Josie Rowe Memorial Handicap Hurdle Race
Hurdle | Class 3 | 3m84y | going Good | Turf | 3 runners | rating band 0-140 | age 3yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Paddy de Pole (hrs_30123037) | 8yo G | 166lb | OR 121 | draw 0 | jockey Mr Lucas Murphy(7) | trainer Paul Nicholls (14d 5/28) | headgear p | last run 17 days | form 4-2412 | MARKET 38.1% | 09:00 median 2.50 | Matchbook 2.50
    comment: Paddy de Pole arrives in fine fettle, a second last time out and a winner two starts back, just 17 days ago, and he has run over today's trip and going before.
    DATA: model 47.9% | style Prominent (led 3% of runs) | runs in data 4 | last 3: 26 Jul Uttoxeter Hurdle 23.3f Good 4/9; 14 Sep Sedgefield Hurdle 27f Good 1/3; 11 Nov Warwick Hurdle 25f Good 2/5 fig 119
    DATA for: Last-run finishing speed +2.8% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
- Docpickedme (hrs_21327649) | 10yo G | 168lb | OR 123 | draw 0 | jockey Charlie Maggs | trainer Richard Hobson (14d 0/2) | headgear tp | last run 23 days | form 3141-0 | MARKET 34.0% | 09:00 median 2.63 | Matchbook 2.98
    comment: Docpickedme has won twice in his last five starts, including a win two starts back, and he has run over today's trip and going before.
    DATA: model 29.9% | style Prominent (led 4% of runs) | runs in data 3 | last 3: 24 Jan Doncaster Chase 24f Soft 4/8; 28 Feb Doncaster Hurdle 24.4f Soft 1/5; 5 Nov Newbury Hurdle 24.5f Good To Soft 12/16
    DATA for: Official rating 123, 5 lb above field average; Has won at this trip or further
    DATA against: Carries 5 lb more than average
- Everyonesgame (hrs_27428821) | 9yo G | 155lb | OR 110 | draw 0 | jockey James Best | trainer Andy Irvine (14d 0/4) | headgear - | last run 26 days | form 765-22 | MARKET 27.8% | 09:00 median 3.25 | Matchbook 3.65
    comment: Everyonesgame arrives in decent heart, a second last time out and another second two starts back, and he has run over today's trip and on this going before.
    DATA: model 22.1% | style Midfield (led 5% of runs) | runs in data 4 | last 3: 23 Apr Warwick Hurdle 25f Good 5/5; 26 May Plumpton Hurdle 20.5f Good 2/4; 2 Nov Plumpton Hurdle 20.5f Good 2/7 fig 110
    DATA for: Good recent finishing positions; Carries 8 lb less than average
    DATA against: Official rating 110, 8 lb below field average

## 12:08 Doncaster | race_id rac_32305856843 | Howcroft Group Novices' Hurdle Race (Go North Night Nurse Series Qualifier) (GBB Race)
Hurdle | Class 4 | 2m128y | going Good | Turf | 6 runners | rating band - | age 4yo+
DATA pace: Lone leader - Pfingstberg is the only habitual front-runner and may be allowed an easy lead.
- One Knight (hrs_40787243) | 6yo G | 154lb | OR - | draw 0 | jockey Cameron Johnstone-Baker(7) | trainer Emma Lavelle (14d 2/19) | headgear - | last run 25 days | form 10-3U3 | MARKET 34.4% | 09:00 median 2.56 | Matchbook 2.82
    DATA: model 22.3% | style Midfield (led 4% of runs) | runs in data 5 | last 3: 20 May Ffos Las Hurdle 15.8f Good To Soft 3/5; 17 Oct Stratford Hurdle 22f Good UR/7; 3 Nov Warwick Hurdle 19f Good 3/6 fig 89
    DATA for: Last-run finishing speed +4.5% vs that field (finished strongly); Has won at this trip or further
    DATA against: Best recent form figure 89, 8 lb below field average; Fell or unseated in 1 of its last 3 jumps runs
- Down To Business (hrs_52526194) | 4yo G | 161lb | OR 112 | draw 0 | jockey Charlie Todd | trainer Dan Skelton (14d 27/97) | headgear - | last run 14 days | form 5-1042 | MARKET 29.3% | 09:00 median 3.00 | Matchbook 3.35
    DATA: model 22.3% | style Midfield (led 23% of runs) | runs in data 6 | last 3: 25 Sep Worcester Hurdle 20f Good 13/15; 3 Oct Fontwell Hurdle 17.7f Good 4/11; 14 Nov Wetherby Hurdle 16f Good 2/4 fig 108
    DATA for: Best recent form figure 108, 11 lb above field average; Trainer 28% wins (27/97), last 14 days; Has won at this trip or further
    DATA against: Race comments mention jumping mistakes in 3 of its last 5 runs
- Dancing Soldier (hrs_17394621762) | 5yo G | 154lb | OR - | draw 0 | jockey Shane Fenelon(5) | trainer Mickey Bowen (14d 1/12) | headgear t (1st time) | wind surgery | last run 363 days | form 1- | MARKET 18.2% | 09:00 median 5.00 | Matchbook 5.40
    DATA: model 13.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: First-time headgear
    DATA against: Returns from a 363-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Arm's of An Angel (hrs_50906254) | 5yo M | 147lb | OR - | draw 0 | jockey Kielan Woods | trainer David Killahena & Graeme McPherson (14d 0/7) | headgear - | last run 31 days | form P/C5-4 | MARKET 12.9% | 09:00 median 6.50 | Matchbook 8.00
    DATA: model 23.2% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 22 Apr Ludlow NH Flat 15.8f Good 5/14; 28 Oct Huntingdon NH Flat 16f Good 4/9 fig 101
    DATA for: Last-run finishing speed +2.4% vs that field (finished strongly)
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; First run over hurdles in our data
- Pfingstberg (hrs_33303921) | 6yo G | 154lb | OR - | draw 0 | jockey Charlie Maggs | trainer Mark Walford (14d 2/12) | headgear t | last run 54 days | form / | MARKET 3.7% | 09:00 median 23.00 | Matchbook 30.00
    DATA: model 9.8% | style Leader (led 57% of runs) | runs in data 2 | last 3: 30 Aug Beverley Flat 16.1f Heavy 5/7; 5 Oct Pontefract Flat 18f Good 6/6
    DATA for: Pace: may get an uncontested lead
    DATA against: Last-run finishing speed -9.2% vs that field (faded); Lightly raced: 2 runs in our data, so the model has little to go on; First run over hurdles in our data
- Northerly (hrs_62516573) | 4yo G | 154lb | OR - | draw 0 | jockey Tom Midgley(3) | trainer Nick Kent (14d 0/6) | headgear h | last run 29 days | form 3-7 | MARKET 1.5% | 09:00 median 51.00 | Matchbook 70.00
    DATA: model 8.9% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 5 Apr Market Rasen NH Flat 16.6f Good 3/6; 30 Oct Uttoxeter NH Flat 16f Good 7/8 fig 91
    DATA against: Best recent form figure 91, 6 lb below field average; Last-run finishing speed -3.9% vs that field (faded); Lightly raced: 2 runs in our data, so the model has little to go on; First run over hurdles in our data

## 12:43 Doncaster | race_id rac_32305858780 | Winter Family Raceday 29th December Novices' Limited Handicap Steeple Chase (GBB Race)
Chase | Class 3 | 2m3f31y | going Good | Turf | 4 runners | rating band 0-130 | age 4yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Palamon (hrs_31479336) | 6yo G | 165lb | OR 131 | draw 0 | jockey Harry Atkins(5) | trainer Dan Skelton (14d 27/97) | headgear tb | last run 1 days | form 512311 | MARKET 35.7% | 09:00 median 2.50 | Matchbook 2.80
    comment: Palamon arrives in cracking form, having won last time out and two starts back, and he has three wins in his last six starts. He has run over today's trip and going, and the yard is in form, though a quick return after one day off is the one query.
    DATA: model 24.3% | style Midfield (led 23% of runs) | runs in data 16 | last 3: 31 Oct Wetherby Chase 19.5f Good 3/8 fig 126; 14 Nov Wetherby Chase 19.5f Good 1/5 fig 129; 27 Nov Doncaster Chase 24f Good 1/3 fig 134
    DATA for: Best recent form figure 134, 15 lb above field average; Official rating 131, 9 lb above field average; Trainer 28% wins (27/97), last 14 days; Has won at this trip or further; Good recent finishing positions
    DATA against: Carries 9 lb more than average; Race comments mention jumping mistakes in 2 of its last 5 runs
- Nazare (hrs_47621588) | 6yo G | 153lb | OR 119 | draw 0 | jockey Kielan Woods | trainer James Owen (14d 5/46) | headgear - | last run 31 days | form 96-311 | MARKET 30.9% | 09:00 median 3.00 | Matchbook 3.15
    comment: The main risk is the 153 lb he must carry off an official mark of 119.
    DATA: model 26.6% | style Midfield (led 23% of runs) | runs in data 5 | last 3: 10 May Ludlow Chase 23.8f Good 3/4; 9 Jun Southwell Chase 20.4f Good 1/4; 28 Oct Huntingdon Chase 20f Good 1/9 fig 116
    DATA for: Last-run finishing speed +3.3% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Race comments mention jumping mistakes in 2 of its last 5 runs
- Fairlawn Skipper (hrs_40996865) | 6yo G | 151lb | OR 117 | draw 0 | jockey Shane Fenelon(5) | trainer Mickey Bowen (14d 1/12) | headgear - | last run 15 days | form U12141 | MARKET 20.1% | 09:00 median 4.50 | Matchbook 4.90
    comment: Fairlawn Skipper arrives in cracking nick, a winner last time out, a fourth two starts back, and another win three starts back, with three victories in his last six and only 15 days since his last run.
    DATA: model 29.9% | style Midfield (led 3% of runs) | runs in data 9 | last 3: 16 Sep Kelso Chase 21.6f Good To Firm 1/4; 23 Oct Cheltenham Chase 25f Good To Soft 4/11 fig 109; 13 Nov Sedgefield Chase 21f Good 1/3 fig 113
    DATA for: Has won at this trip or further; Good recent finishing positions; Carries 5 lb less than average
    DATA against: Best recent form figure 113, 6 lb below field average; Official rating 117, 5 lb below field average
- Nardaran (hrs_42041650) | 5yo G | 155lb | OR 121 | draw 0 | jockey Lorcan Murtagh | trainer Paul Nicholls (14d 5/28) | headgear tp | last run 26 days | form 663-69 | MARKET 13.2% | 09:00 median 6.75 | Matchbook 7.60
    comment: The main risk is a ninth last time out, and he also carries 155 lb.
    DATA: model 19.2% | style Prominent (led 4% of runs) | runs in data 6 | last 3: 12 Apr Wincanton Hurdle 21.4f Good 3/6; 4 May Fakenham Hurdle 20f Good 6/12; 2 Nov Plumpton Hurdle 20.5f Good 9/12 fig 112
    DATA against: Best recent form figure 112, 7 lb below field average; Recent figures 9 lb below its current mark (looks high in the weights); First run over fences in our data

## 1:18 Doncaster | race_id rac_32305862654 | Dranfields CIU National Charity Raceday Mares' Novices' Hurdle Race (GBB Race)
Hurdle | Class 3 | 2m3f88y | going Good | Turf | 7 runners | rating band - | age 4yo+
DATA pace: Lone leader - Just Rizzo is the only habitual front-runner and may be allowed an easy lead.
- Queen Alice (hrs_63390404) | 5yo M | 154lb | OR - | draw 0 | jockey Calum Hogan(5) | trainer Harry Derham (14d 1/16) | headgear - | last run 236 days | form 3- | MARKET 41.6% | 09:00 median 2.10 | Matchbook 2.32
    DATA: model 16.2% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 6 Apr Fairyhouse NH Flat 16f Yielding To Soft 3/12
    DATA for: Last-run finishing speed +6.4% vs that field (finished strongly)
    DATA against: Returns from a 236-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Briery Rose (hrs_48003809) | 6yo M | 160lb | OR - | draw 0 | jockey David Bass | trainer Henry Daly (14d 3/12) | headgear - | last run 27 days | form 5/85-1 | MARKET 24.6% | 09:00 median 3.50 | Matchbook 4.00
    DATA: model 14.4% | style Prominent (led 5% of runs) | runs in data 3 | last 3: 7 Mar Hereford NH Flat 16.2f Good 8/14; 14 Apr Market Rasen Hurdle 16.6f Good 5/7; 1 Nov Huntingdon Hurdle 19.5f Good 1/4 fig 104
    DATA for: Best recent form figure 104, 8 lb above field average; Trainer 25% wins (3/12), last 14 days; Last-run finishing speed +2.7% vs that field (finished strongly); Has won at this trip or further
- Lady Litigator (hrs_58196635) | 4yo F | 153lb | OR 103 | draw 0 | jockey Ben Godfrey | trainer Anthony Honeyball (14d 1/14) | headgear t | last run 23 days | form U62-32 | MARKET 16.2% | 09:00 median 5.50 | Matchbook 6.00
    DATA: model 42.0% | style Prominent (led 23% of runs) | runs in data 5 | last 3: 12 Apr Wincanton NH Flat 15.2f Good 2/5; 27 May Newton Abbot Hurdle 16.8f Good 3/10; 5 Nov Plumpton Hurdle 20.5f Good 2/3 fig 97
    DATA for: Last-run finishing speed +4.0% vs that field (finished strongly); Good recent finishing positions
- Harzandacassandra (hrs_56559384) | 5yo M | 154lb | OR - | draw 0 | jockey Kielan Woods | trainer David Killahena & Graeme McPherson (14d 0/7) | headgear - | last run 43 days | form 70-5 | MARKET 8.9% | 09:00 median 9.50 | Matchbook 11.50
    DATA: model 7.8% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 14 Feb Ascot NH Flat 15.7f Good To Soft 7/9; 21 Mar Newbury NH Flat 16.3f Good To Soft 12/20; 16 Oct Uttoxeter NH Flat 16f Good 5/7 fig 98
    DATA against: First run over hurdles in our data
- La Trinite (hrs_49110537) | 4yo F | 153lb | OR - | draw 0 | jockey Jack Quinlan | trainer Neil King (14d 0/6) | headgear - | last run 23 days | form 36 | MARKET 7.2% | 09:00 median 11.50 | Matchbook 14.00
    DATA: model 8.8% | style Midfield (led 3% of runs) | runs in data 8 | last 3: 19 Oct Bath Flat 17f Good To Soft 1/11 fig 53; 26 Oct Kempton (AW) Flat 16f Standard / Slow 7/12 fig 41; 5 Nov Newbury Hurdle 16.5f Good To Soft 6/10 fig 105
    DATA for: Best recent form figure 105, 10 lb above field average
- Aunt Gallie (hrs_63171633) | 5yo M | 154lb | OR - | draw 0 | jockey Nick Slatter(3) | trainer David Killahena & Graeme McPherson (14d 0/7) | headgear - | last run 31 days | form 8-7 | MARKET 1.0% | 09:00 median 67.00 | Matchbook 160.00
    DATA: model 6.8% | style Held up (led 8% of runs) | runs in data 2 | last 3: 1 Apr Southwell NH Flat 15.8f Good 8/10; 28 Oct Huntingdon NH Flat 16f Good 7/9 fig 87
    DATA against: Best recent form figure 87, 8 lb below field average; Lightly raced: 2 runs in our data, so the model has little to go on; First run over hurdles in our data
- Just Rizzo (hrs_63171591) | 4yo F | 153lb | OR - | draw 0 | jockey Charlie Todd | trainer Nick Kent (14d 0/6) | headgear - | last run 43 days | form 9-7 | MARKET 0.5% | 09:00 median 126.00 | Matchbook 310.00
    DATA: model 3.9% | style Leader (led 38% of runs) | runs in data 2 | last 3: 1 Apr Southwell NH Flat 15.8f Good 9/10; 16 Oct Uttoxeter NH Flat 16f Good 7/7 fig 82
    DATA for: Pace: may get an uncontested lead
    DATA against: Best recent form figure 82, 14 lb below field average; Last-run finishing speed -6.1% vs that field (faded); Lightly raced: 2 runs in our data, so the model has little to go on; First run over hurdles in our data

## 1:48 Doncaster | race_id rac_32305864591 | Apres Village Friday 18th December Handicap Hurdle Race (Go North Sea Pigeon Series Qualifier)
Hurdle | Class 4 | 2m0f128y | going Good | Turf | 6 runners | rating band 0-120 | age 3yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Leaumec de Mee (hrs_50841959) | 5yo G | 168lb | OR 120 | draw 0 | jockey Kielan Woods | trainer Dan Skelton (14d 27/97) | headgear - | last run 38 days | form 2145-1 | MARKET 31.1% | 09:00 median 2.75 | Matchbook 3.20
    comment: Leaumec de Mee arrives a last-time-out winner, with another victory four starts back and a second five starts back, and he has run over today's trip and going before, while the in-form yard adds to the case. The one concern is a 168 lb burden after 38 days off.
    DATA: model 28.3% | style Prominent (led 4% of runs) | runs in data 3 | last 3: 14 Jan Newbury Hurdle 16.3f Good To Soft 4/11; 27 Feb Doncaster Hurdle 16.6f Good To Soft 5/8; 21 Oct Worcester Hurdle 16f Good To Soft 1/7 fig 116
    DATA for: Best recent form figure 116, 9 lb above field average; Official rating 120, 9 lb above field average; Trainer 28% wins (27/97), last 14 days; Last-run finishing speed +6.5% vs that field (finished strongly); Has won at this trip or further
    DATA against: Carries 9 lb more than average; Race comments mention jumping mistakes in 2 of its last 3 runs
- Liberty Coach (hrs_40312986) | 5yo G | 161lb | OR 113 | draw 0 | jockey Oakley Brown(5) | trainer John & Sean Quinn (14d 1/10) | headgear - | last run 28 days | form 6P3-31 | MARKET 29.7% | 09:00 median 3.00 | Matchbook 3.25
    comment: Liberty Coach arrives a last-time-out winner, with a third and another third before that, and he has run over today's trip and going before. Carrying 161 lb is the main risk, though a 28-day break should leave him fresh.
    DATA: model 26.2% | style Prominent (led 4% of runs) | runs in data 5 | last 3: 10 Mar Sedgefield Hurdle 16.8f Good 3/7; 2 Jul Perth Hurdle 16.2f Good 3/9; 31 Oct Ayr Hurdle 16f Good To Soft 1/9 fig 114
    DATA for: Best recent form figure 114, 7 lb above field average; Has won at this trip or further; Good recent finishing positions
    DATA against: Pulled up in 1 of its last 5 jumps runs
- Flash Man (hrs_51735586) | 4yo G | 157lb | OR 109 | draw 0 | jockey Kevin Brogan | trainer Toby Lawes (14d 0/1) | headgear - | last run 20 days | form 1-2334 | MARKET 18.2% | 09:00 median 5.00 | Matchbook 5.30
    comment: Flash Man is a consistent sort, finishing fourth last time out after a third two starts back, another third three starts back and a second four starts back, and he has run over today's trip and going. Fresh enough after 20 days, his risk is that he has just one win in his last five starts.
    DATA: model 17.0% | style Prominent (led 4% of runs) | runs in data 8 | last 3: 27 Sep Epsom Downs Flat 12f Good 4/13; 10 Oct Chepstow Hurdle 16.1f Good To Soft 3/12; 8 Nov Sandown Hurdle 16f Good To Soft 4/7 fig 106
- Itsinthename (hrs_57877911) | 5yo G | 156lb | OR 108 | draw 0 | jockey Jack Quinlan | trainer Nick Scholfield (14d 1/13) | headgear tp | last run 22 days | form 167-P5 | MARKET 11.6% | 09:00 median 7.50 | Matchbook 8.80
    comment: Itsinthename is hard to fancy: he's finished fifth, pulled up, seventh and sixth since a win five starts back, and he carries 156 lb.
    DATA: model 7.0% | style Prominent (led 29% of runs) | runs in data 6 | last 3: 9 Apr Taunton Hurdle 16.5f Good 7/7; 16 May Bangor-on-Dee Hurdle 16.7f Good PU/9; 6 Nov Aintree Hurdle 17f Good To Soft 5/10 fig 106
    DATA against: Pulled up in 1 of its last 5 jumps runs
- Cotton Socks (hrs_58931166) | 4yo G | 148lb | OR 100 | draw 0 | jockey Charlie Todd | trainer Lucy Wadham (14d 0/3) | headgear - | last run 19 days | form 331-64 | MARKET 7.2% | 09:00 median 12.75 | Matchbook 14.00
    comment: He has run over today's trip and going, and a 19-day break is fine, but 148 lb is a lot to carry.
    DATA: model 14.0% | style Midfield (led 3% of runs) | runs in data 4 | last 3: 6 Apr Fakenham Hurdle 16f Good 1/6; 16 Oct Uttoxeter Hurdle 16f Good 6/10 fig 91; 9 Nov Stratford Hurdle 18.5f Good To Soft 4/7 fig 86
    DATA for: Has won at this trip or further; Carries 11 lb less than average
    DATA against: Best recent form figure 91, 16 lb below field average; Recent figures 9 lb below its current mark (looks high in the weights); Official rating 100, 11 lb below field average
- Belfrina (hrs_37821539) | 5yo M | 164lb | OR 116 | draw 0 | jockey Lorcan Murtagh | trainer David Pipe (14d 3/17) | headgear t | last run 13 days | form 2F12/P | MARKET 2.3% | 09:00 median 34.00 | Matchbook 50.00
    comment: Belfrina bounced back from a fall with a win three starts back and a second two starts back, and she has run over today's trip.
    DATA: model 7.5% | style Held up (led 5% of runs) | runs in data 2 | last 3: 29 Oct Bath Flat 10f Soft 9/12 fig 60; 15 Nov Fontwell Hurdle 17.5f Good To Soft PU/8
    DATA for: Official rating 116, 5 lb above field average
    DATA against: Carries 5 lb more than average; Lightly raced: 2 runs in our data, so the model has little to go on; Pulled up in 1 of its last 1 jumps runs; Pace: steady gallop likely, hard to come from off the pace

## 2:28 Doncaster | race_id rac_32305866528 | Doncaster 2027 Annual Membership Handicap Steeple Chase (Go North Red Rum Series Qualifier) (GBB Race)
Chase | Class 4 | 3m2f1y | going Good | Turf | 6 runners | rating band 0-115 | age 4yo+
DATA pace: Even - Two likely leaders (Copshill Lad, Breezethroughlife). A fair, even gallop is most likely.
- Camarrate (hrs_34845440) | 6yo G | 159lb | OR 106 | draw 0 | jockey Kielan Woods | trainer Donald McCain (14d 2/25) | headgear t | last run 14 days | form 1-P223 | MARKET 24.8% | 09:00 median 3.50 | Matchbook 4.00 | CHECK (skip line 3.32)
    comment: Camarrate has been in the frame in his last three, a third last time out, then a second two starts back and another second three starts back, and he's fit after 14 days with going experience.
    DATA: model 20.0% | style Midfield (led 3% of runs) | runs in data 7 | last 3: 15 Sep Uttoxeter Chase 20f Good 2/8; 16 Oct Uttoxeter Chase 24f Good 2/8 fig 105; 14 Nov Wetherby Chase 24f Good 3/4 fig 102
    DATA for: Good recent finishing positions
    DATA against: Race comments mention jumping mistakes in 2 of its last 5 runs; Pulled up in 1 of its last 5 jumps runs
- Mumford's Magic (hrs_33165153) | 8yo G | 168lb | OR 115 | draw 0 | jockey Charlie Todd | trainer Dan Skelton (14d 27/97) | headgear p | last run 35 days | form 17-612 | MARKET 20.2% | 09:00 median 4.50 | Matchbook 4.70
    comment: Second last time out, and a winner two starts back, Mumford's Magic has won twice in his last five and has run over today's trip and going before.
    DATA: model 16.3% | style Held up (led 4% of runs) | runs in data 5 | last 3: 4 Sep Worcester Chase 23f Good 6/6; 13 Oct Southwell Chase 25.8f Good 1/3; 24 Oct Kelso Chase 26f Good 2/4 fig 111
    DATA for: Best recent form figure 111, 8 lb above field average; Official rating 115, 8 lb above field average; Trainer 28% wins (27/97), last 14 days; Has won at this trip or further; Good recent finishing positions
    DATA against: Carries 8 lb more than average; Race comments mention jumping mistakes in 2 of its last 5 runs
- Copshill Lad (hrs_28903700) | 8yo G | 165lb | OR 112 | draw 0 | jockey Harry Reed | trainer Harry Derham (14d 1/16) | headgear p | last run 207 days | form 1351-6 | MARKET 17.4% | 09:00 median 5.00 | Matchbook 5.80
    comment: Copshill Lad has won twice in his last five starts, including a victory two starts back, and he has run over today's trip and on this going before; the main risk is a 207-day absence after finishing sixth last time out.
    DATA: model 26.9% | style Leader (led 38% of runs) | runs in data 2 | last 3: 24 Mar Southwell Chase 25.8f Good 1/5; 5 May Ffos Las Chase 23.8f Good 6/9
    DATA for: Official rating 112, 6 lb above field average; Has won at this trip or further
    DATA against: Carries 6 lb more than average; Returns from a 207-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- I Am The Moon (hrs_40820402) | 7yo M | 149lb | OR 96 | draw 0 | jockey Amber Jackson-Fennell(7) | trainer Nigel & Willy Twiston-Davies (14d 3/18) | headgear p | last run 150 days | form P4-248 | MARKET 14.6% | 09:00 median 6.00 | Matchbook 6.80
    comment: The main risk is a 150-day layoff, carrying 149 lb.
    DATA: model 12.2% | style Prominent (led 4% of runs) | runs in data 7 | last 3: 17 May Stratford Hurdle 26.4f Good To Firm 2/5; 4 Jun Uttoxeter Chase 24f Good 4/4; 1 Jul Worcester Chase 23f Good 8/11
    DATA for: Carries 10 lb less than average
    DATA against: Official rating 96, 10 lb below field average; Last-run finishing speed -7.3% vs that field (faded); Returns from a 150-day break; Pulled up in 1 of its last 5 jumps runs
- Getaway Vic (hrs_39568382) | 7yo G | 163lb | OR 110 | draw 0 | jockey Shane Fenelon(5) | trainer Mickey Bowen (14d 1/12) | headgear b | last run 30 days | form 2231P3 | MARKET 11.9% | 09:00 median 7.50 | Matchbook 8.40
    comment: Getaway Vic booked a third last time out, and a winner three starts back, with a second and a third also in his last six, so he rarely runs badly; he has run over today's trip and going, and 30 days since his last run is fine. The risk is a pulled-up effort two starts back and 163 lb on his back.
    DATA: model 14.7% | style Prominent (led 23% of runs) | runs in data 7 | last 3: 28 Aug Sedgefield Chase 26.3f Good 1/7; 10 Oct Hexham Chase 24.2f Good PU/9; 29 Oct Ffos Las Chase 25.5f Good 3/5 fig 106
    DATA for: Has won at this trip or further
    DATA against: Race comments mention jumping mistakes in 3 of its last 5 runs; Pulled up in 1 of its last 5 jumps runs
- Breezethroughlife (hrs_51123751) | 5yo G | 153lb | OR 100 | draw 0 | jockey Jack Quinlan | trainer Neil King (14d 0/6) | headgear t | wind surgery | last run 23 days | form 3-8344 | MARKET 11.1% | 09:00 median 8.00 | Matchbook 8.80
    comment: Breezethroughlife is yet to win in his last five starts, though back-to-back fourths last time out and two starts back, plus a third three starts back, show he is competitive.
    DATA: model 10.0% | style Leader (led 43% of runs) | runs in data 7 | last 3: 19 May Huntingdon Hurdle 20.7f Good To Firm 3/3; 4 Jun Uttoxeter Hurdle 23.3f Good 4/7; 5 Nov Plumpton Chase 20f Good 4/4 fig 92
    DATA for: Carries 6 lb less than average
    DATA against: Best recent form figure 92, 12 lb below field average; Recent figures 8 lb below its current mark (looks high in the weights); Official rating 100, 6 lb below field average; Last-run finishing speed -2.4% vs that field (faded)

## 3:10 Doncaster | race_id rac_32305868465 | Grace And Dotty Fillies' "Junior" National Hunt Flat Race (Category 1 Elimination) (GBB Race)
NH Flat | Class 5 | 2m0f128y | going Good | Turf | 9 runners | rating band - | age 3yo
DATA pace: Unclear - Running styles known for only 3 of 9 runners.
- Ignite The Night (hrs_17394604031) | 3yo F | 156lb | OR - | draw 0 | jockey Kielan Woods | trainer Fergal O'Brien (14d 5/28) | headgear - | last run 30 days | form 3 | MARKET 30.8% | 09:00 median 2.75 | Matchbook 3.00
    comment: The one concern is the 156 lb she carries, with her yet to win in recent form.
    DATA: model 14.7% | style Held up (led 8% of runs) | runs in data 1 | last 3: 29 Oct Stratford NH Flat 16.5f Good To Soft 3/9 fig 105
    DATA for: Last-run finishing speed +7.9% vs that field (finished strongly)
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Lady Loki (hrs_17394434022) | 3yo F | 156lb | OR - | draw 0 | jockey Lee Edwards | trainer Gihan Arnolda (14d 0/6) | headgear - | last run 30 days | form 2 | MARKET 21.9% | 09:00 median 3.75 | Matchbook 4.40
    comment: Runner-up last time out, Lady Loki returns after 30 days and has run over today's trip, so she should be fit enough to go one better.
    DATA: model 14.3% | style Unknown | runs in data 1 | last 3: 29 Oct Stratford NH Flat 16.5f Good To Soft 2/9 fig 107
    DATA for: Best recent form figure 107, 6 lb above field average; Last-run finishing speed +7.6% vs that field (finished strongly)
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Sarah's Surprise (hrs_17395915082) | 3yo F | 156lb | OR - | draw 0 | jockey Harry Reed | trainer Nick Scholfield (14d 1/13) | headgear - | last run - days | form - | MARKET 13.8% | 09:00 median 6.00 | Matchbook 6.80
    comment: Sarah's Surprise is an unraced filly with no form to assess, so she is wholly unexposed and open to improvement. She shoulders 156 lb on debut, and any glimpse of ability would be a bonus.
    DATA: model 10.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Karalee's Legacy (hrs_17396174789) | 3yo F | 156lb | OR - | draw 0 | jockey Luke Scott(3) | trainer Dr Richard Newland (14d 1/12) | headgear - | last run - days | form - | MARKET 10.8% | 09:00 median 7.50 | Matchbook 9.40
    comment: Karalee's Legacy is unexposed with no recorded form to lean on, so this filly's debut is a pure step into the unknown. She carries 156 lb, and there should be scope for improvement as she gains experience.
    DATA: model 10.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Jolanta (hrs_17393894791) | 3yo F | 156lb | OR - | draw 0 | jockey Charlie Maggs | trainer Rebecca Menzies (14d 0/17) | headgear - | last run - days | form - | MARKET 6.8% | 09:00 median 13.00 | Matchbook 14.00
    comment: Jolanta is an unraced filly with no recorded form, so she's totally unexposed and open to improvement. She carries 156 lb on debut, and there's nothing to go on beyond that.
    DATA: model 10.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Trainer 0 wins from 17 runs, last 14 days; Lightly raced: 0 runs in our data, so the model has little to go on
- Dance In The Mist (hrs_17394592558) | 3yo F | 156lb | OR - | draw 0 | jockey Taylor Fisher | trainer Alan King (14d 3/26) | headgear - | last run 30 days | form 5 | MARKET 6.3% | 09:00 median 13.00 | Matchbook 15.00
    comment: The main risk is the 156 lb she carries, and she is yet to win in her recent form.
    DATA: model 13.5% | style Held up (led 8% of runs) | runs in data 1 | last 3: 29 Oct Stratford NH Flat 16.5f Good To Soft 5/9 fig 100
    DATA for: Last-run finishing speed +4.8% vs that field (finished strongly)
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Noemie du Chenet (hrs_17394609246) | 3yo F | 156lb | OR - | draw 0 | jockey James Best | trainer Nigel Hawke (14d 1/10) | headgear - | last run - days | form - | MARKET 4.6% | 09:00 median 19.00 | Matchbook 22.00
    comment: Noemie du Chenet is an unraced filly with no form to assess, so she's wholly unexposed and open to improvement.
    DATA: model 10.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Dee's Gem (hrs_17396172703) | 3yo F | 156lb | OR - | draw 0 | jockey Charlie Todd | trainer Fionn McSharry (14d 0/1) | headgear - | last run - days | form - | MARKET 3.7% | 09:00 median 23.00 | Matchbook 36.00
    comment: Unexposed and with no recorded form to go on, Dee's Gem is a blank canvas on her debut, so there is scope for improvement.
    DATA: model 10.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Maria's Double (hrs_17394608203) | 3yo F | 156lb | OR - | draw 0 | jockey Joe Anderson(3) | trainer Grace Harris (14d 0/10) | headgear - | last run 17 days | form 74 | MARKET 1.3% | 09:00 median 51.00 | Matchbook 140.00
    comment: The risk is that she is yet to score in her last two.
    DATA: model 5.6% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 29 Oct Stratford NH Flat 16.5f Good To Soft 7/9 fig 87; 11 Nov Warwick NH Flat 16f Good 4/7 fig 94
    DATA against: Best recent form figure 94, 8 lb below field average; Trainer 0 wins from 10 runs, last 14 days; Last-run finishing speed -4.8% vs that field (faded); Lightly raced: 2 runs in our data, so the model has little to go on
