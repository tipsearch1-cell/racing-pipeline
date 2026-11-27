# Card review packet: Doncaster, 2026-11-27

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


## 12:00 Doncaster | race_id rac_32305717379 | Golden Scoop Novices' Limited Handicap Steeple Chase (GBB Race)
Chase | Class 3 | 2m7f214y | going Good | Turf | 3 runners | rating band - | age 4yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Kent de Thaix (hrs_49325913) | 6yo G | 155lb | OR 122 | draw 0 | jockey Jonathan England | trainer Sam England (14d 6/29) | headgear t | wind surgery | last run 31 days | form P516-2 | MARKET 42.1% | 09:00 median 2.20 | Matchbook 2.32
    comment: Kent de Thaix arrives in decent shape after a second last time out, and a winner three starts back, with experience over today's trip and going after a 31-day break. The risk is a hefty 155 lb, and he was only sixth two starts back.
    DATA: model 27.5% | style Held up (led 3% of runs) | runs in data 5 | last 3: 27 Mar Wetherby Hurdle 24.1f Good 1/6; 17 Apr Ayr Hurdle 24.3f Soft 6/15; 27 Oct Newcastle Chase 23.5f Good 2/4 fig 119
    DATA for: Trainer 21% wins (6/29), last 14 days; Has won at this trip or further; Good recent finishing positions
    DATA against: Pulled up in 1 of its last 5 jumps runs; Pace: steady gallop likely, hard to come from off the pace
- Palamon (hrs_31479336) | 6yo G | 164lb | OR 131 | draw 0 | jockey Dominic Lewis(10) | trainer Dan Skelton (14d 23/95) | headgear tb | last run 13 days | form 351231 | MARKET 29.8% | 09:00 median 3.00 | Matchbook 3.40
    comment: Palamon heads the field on current form, winning last time out and again four starts back, with a third and a second in between, and he returns after just 13 days. He has run over today's trip and going, though 164 lb is a notable burden.
    DATA: model 56.0% | style Held up (led 3% of runs) | runs in data 15 | last 3: 19 Oct Plumpton Chase 20f Good 2/5 fig 119; 31 Oct Wetherby Chase 19.5f Good 3/8 fig 126; 14 Nov Wetherby Chase 19.5f Good 1/5 fig 129
    DATA for: Best recent form figure 129, 8 lb above field average; Official rating 131, 8 lb above field average; Trainer 24% wins (23/95), last 14 days; Good recent finishing positions
    DATA against: Carries 8 lb more than average; Pace: steady gallop likely, hard to come from off the pace
- Kayf Dancer (hrs_33660928) | 8yo G | 150lb | OR 117 | draw 0 | jockey Shane Fenelon(5) | trainer Mickey Bowen (14d 1/11) | headgear - | last run 36 days | form 1-6242 | MARKET 28.1% | 09:00 median 3.25 | Matchbook 3.50
    comment: Kayf Dancer was second last time out and a fourth two starts back, a consistent profile for a gelding who has run over today's trip and on this going before.
    DATA: model 16.5% | style Held up (led 3% of runs) | runs in data 6 | last 3: 31 Aug Cartmel Hurdle 25.4f Good To Soft 2/7; 25 Sep Worcester Chase 23f Good 4/4; 22 Oct Ffos Las Chase 24f Soft 2/7 fig 116
    DATA for: Last-run finishing speed +4.3% vs that field (finished strongly); Good recent finishing positions; Carries 6 lb less than average
    DATA against: Best recent form figure 116, 5 lb below field average; Official rating 117, 6 lb below field average; Race comments mention jumping mistakes in 2 of its last 5 runs; Pace: steady gallop likely, hard to come from off the pace

## 12:30 Doncaster | race_id rac_32305713505 | Steve Martin Memorial EBF Junior 'National Hunt' Hurdle Race (GBB Race)
Hurdle | Class 4 | 2m128y | going Good | Turf | 6 runners | rating band - | age 3yo
DATA pace: Unclear - Running styles known for only 1 of 6 runners.
- Invino Honnetete (hrs_17393682019) | 3yo G | 161lb | OR - | draw 0 | jockey David Bass | trainer Kerry Lee (14d 2/7) | headgear h (1st time) | last run 50 days | form 1 | MARKET 27.2% | 09:00 median 3.25 | Matchbook 3.45 | CHECK (skip line 3.09)
    comment: Winner on his latest outing and unexposed, Invino Honnetete returns after 50 days off carrying 161 lb, and with so little form to go on there could well be more to come from him.
    DATA: model 17.3% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 29% wins (2/7), last 14 days; First-time headgear
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Navrom (hrs_17396109080) | 3yo G | 154lb | OR - | draw 0 | jockey Kielan Woods | trainer Dan Skelton (14d 23/95) | headgear - | last run - days | form - | MARKET 24.2% | 09:00 median 3.50 | Matchbook 4.00
    comment: Navrom is an unexposed debutant with no recorded form to go on, so he's open to improvement from the outset. He carries 154 lb, and with nothing yet to judge him on, this first look is the key.
    DATA: model 15.8% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 24% wins (23/95), last 14 days
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Low Tide (hrs_17395008715) | 3yo G | 154lb | OR - | draw 0 | jockey Danny McMenamin | trainer Tim Easterby (14d 2/14) | headgear - | last run - days | form - | MARKET 18.4% | 09:00 median 5.00 | Matchbook 5.00
    comment: Low Tide is an unexposed debutant with no recorded form to go on, so he remains open to improvement. He carries 154 lb, and his first outing should reveal plenty about what he can do.
    DATA: model 15.8% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Fiery Logic (hrs_17396106994) | 3yo G | 154lb | OR - | draw 0 | jockey Peter Kavanagh | trainer Donald McCain (14d 2/21) | headgear - | last run - days | form - | MARKET 17.0% | 09:00 median 5.00 | Matchbook 5.80
    comment: Fiery Logic is totally unexposed on his debut, so there's no form to lean on and plenty of scope for improvement.
    DATA: model 15.8% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Jubilate (hrs_17396108037) | 3yo G | 154lb | OR - | draw 0 | jockey Richie McLernon | trainer Rebecca Menzies (14d 0/10) | headgear - | last run - days | form - | MARKET 11.8% | 09:00 median 7.50 | Matchbook 8.20
    comment: Jubilate is an unraced debutant with no form to go on, so he's an unexposed gelding open to any amount of improvement. He carries 154 lb on his first look at a racecourse.
    DATA: model 15.8% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Trainer 0 wins from 10 runs, last 14 days; Lightly raced: 0 runs in our data, so the model has little to go on
- Dundeelin (hrs_17393577719) | 3yo G | 154lb | OR - | draw 0 | jockey James Best | trainer Nigel Hawke (14d 2/10) | headgear p (1st time) | last run 12 days | form PP | MARKET 1.4% | 09:00 median 67.00 | Matchbook 100.00
    comment: Dundeelin is lightly raced and unexposed, with a pulled up last time out and another pulled up two starts back offering little to judge him on, so any improvement is a leap of faith. He's back quickly after 12 days and carries 154 lb.
    DATA: model 19.5% | style Held up (led 8% of runs) | runs in data 2 | last 3: 10 Oct Chepstow Hurdle 16.1f Good To Soft PU/11; 15 Nov Fontwell Hurdle 17.5f Soft PU/10
    DATA for: Trainer 20% wins (2/10), last 14 days; First-time headgear
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Pulled up in 2 of its last 2 jumps runs

## 1:00 Doncaster | race_id rac_32305715442 | Ice Cream Direct UK Members Maiden Hurdle Race (GBB Race)
Hurdle | Class 4 | 2m4f181y | going Good | Turf | 5 runners | rating band - | age 4yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Matty's Mate (hrs_65287229) | 5yo G | 158lb | OR - | draw 0 | jockey Freddie Gingell | trainer Paul Nicholls (14d 2/22) | headgear - | last run 177 days | form 2 | MARKET 64.8% | 09:00 median 1.44 | Matchbook 1.47
    DATA: model 41.3% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 3 Jun Newton Abbot NH Flat 16.8f Good To Soft 2/8
    DATA for: Last-run finishing speed +11.2% vs that field (finished strongly)
    DATA against: Returns from a 177-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Masterius (hrs_64523277) | 4yo G | 157lb | OR - | draw 0 | jockey Rian Corcoran(5) | trainer David Pipe (14d 2/14) | headgear - | last run 27 days | form 22314 | MARKET 19.4% | 09:00 median 4.50 | Matchbook 5.20
    DATA: model 23.2% | style Prominent (led 29% of runs) | runs in data 4 | last 3: 5 Jul Market Rasen NH Flat 16.6f Good 3/11; 13 Oct Southwell NH Flat 15.8f Good 1/4; 31 Oct Ascot Hurdle 15.5f Good To Firm 4/5 fig 96
    DATA for: Good recent finishing positions
- Landsborough (hrs_52236450) | 5yo G | 158lb | OR - | draw 0 | jockey Shane Fenelon(5) | trainer Mickey Bowen (14d 1/11) | headgear p (1st time) | last run 34 days | form 25-6 | MARKET 5.9% | 09:00 median 15.00 | Matchbook 18.00
    DATA: model 8.2% | style Held up (led 8% of runs) | runs in data 1 | last 3: 24 Oct Cheltenham Hurdle 24f Good 6/6
    DATA for: First-time headgear
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Dshipdatnevrsailed (hrs_17394662439) | 5yo G | 158lb | OR - | draw 0 | jockey Tom Midgley(3) | trainer Nick Kent (14d 0/3) | headgear - | last run 215 days | form P2- | MARKET 5.2% | 09:00 median 17.00 | Matchbook 21.00
    DATA: model 15.8% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 215-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Regal Thunder (hrs_52236436) | 5yo G | 158lb | OR - | draw 0 | jockey Joe Williamson | trainer Philip Kirby (14d 1/13) | headgear - | last run 22 days | form 333-65 | MARKET 4.8% | 09:00 median 17.00 | Matchbook 24.00
    DATA: model 11.5% | style Held up (led 5% of runs) | runs in data 3 | last 3: 11 Apr Newcastle NH Flat 16.9f Good 3/10; 27 Oct Newcastle NH Flat 17f Good 6/9 fig 92; 5 Nov Newcastle Hurdle 20.5f Good 5/8
    DATA against: Pace: steady gallop likely, hard to come from off the pace

## 1:35 Doncaster | race_id rac_32305719316 | Kelly's Dairy Soft Ice Cream Handicap Steeple Chase (GBB Race)
Chase | Class 3 | 2m3f31y | going Good | Turf | 6 runners | rating band 0-135 | age 4yo+
DATA pace: Even - Two likely leaders (Toothless, Cuban Court). A fair, even gallop is most likely.
- Toothless (hrs_33547703) | 8yo G | 163lb | OR 129 | draw 0 | jockey Freddie Gingell | trainer Paul Nicholls (14d 2/22) | headgear tp | wind surgery | last run 29 days | form 1223-1 | MARKET 30.0% | 09:00 median 3.00 | Matchbook 3.25 | CHECK (skip line 2.85)
    comment: Toothless arrives a winner last time out, with a third two starts back, a second three starts back and another second four starts back, and he has run over today's trip and on this going. The one risk is the 163 lb he carries after a 29-day break.
    DATA: model 27.2% | style Leader (led 38% of runs) | runs in data 5 | last 3: 7 Mar Sandown Chase 20.1f Soft 2/3; 23 Apr Perth Chase 20.1f Good 3/7; 29 Oct Ffos Las Chase 19.5f Good 1/6 fig 124
    DATA for: Best recent form figure 124, 5 lb above field average; Has won at this trip or further; Good recent finishing positions
    DATA against: Race comments mention jumping mistakes in 3 of its last 5 runs
- Cuban Court (hrs_29593011) | 8yo G | 148lb | OR 114 | draw 0 | jockey Jack Quinlan | trainer Neil King (14d 0/5) | headgear t | last run 30 days | form 6114-3 | MARKET 26.0% | 09:00 median 3.50 | Matchbook 3.75
    DATA: model 13.2% | style Leader (led 38% of runs) | runs in data 5 | last 3: 13 Mar Doncaster Chase 19.1f Good To Soft 1/3; 14 Apr Market Rasen Chase 19.2f Good 4/4; 28 Oct Huntingdon Chase 20f Good 3/9 fig 111
    DATA for: Has won at this trip or further; Good recent finishing positions; Carries 12 lb less than average
    DATA against: Best recent form figure 111, 8 lb below field average; Official rating 114, 12 lb below field average
- Bowmore (hrs_32683301) | 8yo G | 162lb | OR 128 | draw 0 | jockey Daire McConville(7) | trainer Charlie Longsdon (14d 2/14) | headgear - | last run 19 days | form 300-33 | MARKET 18.2% | 09:00 median 5.00 | Matchbook 5.30
    comment: The main risk is that he is yet to win in his last five and carries 162 lb.
    DATA: model 19.7% | style Unknown | runs in data 4 | last 3: 10 Apr Aintree Hurdle 20f Good To Soft 12/22; 24 May Uttoxeter Hurdle 19.9f Good 3/11; 8 Nov Sandown Hurdle 20f Good 3/6 fig 127
    DATA for: Best recent form figure 127, 8 lb above field average; Good recent finishing positions
    DATA against: First run over fences in our data
- Primoz (hrs_34760047) | 8yo G | 164lb | OR 130 | draw 0 | jockey Derek Fox | trainer Lucinda Russell & Michael Scudamore (14d 1/19) | headgear t | last run 28 days | form 31B-25 | MARKET 13.7% | 09:00 median 6.50 | Matchbook 7.40
    comment: Primoz makes plenty of appeal, with a second two starts back and a win four starts back, and he has run over today's trip and on the going before.
    DATA: model 16.8% | style Prominent (led 38% of runs) | runs in data 5 | last 3: 10 Apr Aintree Chase 21.1f Good To Soft BD/27; 4 Oct Kelso Chase 17.1f Good To Firm 2/4; 30 Oct Wetherby Chase 19.5f Good 5/6 fig 121
    DATA for: Has won at this trip or further
    DATA against: Recent figures 9 lb below its current mark (looks high in the weights); Last-run finishing speed -3.1% vs that field (faded); Fell or unseated in 1 of its last 5 jumps runs
- Jaipaletemps (hrs_35218302) | 7yo G | 152lb | OR 118 | draw 0 | jockey Rian Corcoran(5) | trainer David Pipe (14d 2/14) | headgear t | last run 22 days | form 214-63 | MARKET 8.6% | 09:00 median 10.00 | Matchbook 12.00
    comment: Jaipaletemps was third last time out, but a sixth and a fourth before that, and a win four starts back is fading from view.
    DATA: model 9.1% | style Midfield (led 5% of runs) | runs in data 7 | last 3: 2 Apr Chepstow Chase 19.4f Good To Soft 4/6; 22 Oct Ffos Las Chase 16f Soft 6/6 fig 110; 5 Nov Plumpton Chase 20f Good 3/3
    DATA for: Has won at this trip or further; Carries 8 lb less than average
    DATA against: Best recent form figure 110, 9 lb below field average; Recent figures 8 lb below its current mark (looks high in the weights); Official rating 118, 8 lb below field average; Last-run finishing speed -4.9% vs that field (faded)
- Il Ridoto (hrs_24102631) | 9yo G | 168lb | OR 134 | draw 0 | jockey Danny McMenamin | trainer Henry Hogarth (14d 0/0) | headgear tp | last run 224 days | form 8720P- | MARKET 3.5% | 09:00 median 26.00 | Matchbook 28.00
    DATA: model 14.0% | style Prominent (led 8% of runs) | runs in data 3 | last 3: 1 Jan Cheltenham Chase 20.6f Good 2/9; 12 Mar Cheltenham Chase 26.3f Good 15/23; 17 Apr Ayr Chase 20.5f Soft PU/9
    DATA for: Official rating 134, 8 lb above field average
    DATA against: Carries 8 lb more than average; Returns from a 224-day break; Pulled up in 1 of its last 3 jumps runs

## 2:10 Doncaster | race_id rac_32305721253 | Cadburys Ice Cream Novices' Handicap Hurdle Race
Hurdle | Class 5 | 2m0f128y | going Good | Turf | 9 runners | rating band 0-100 | age 3yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Nobody Told Me (hrs_31259193) | 6yo G | 150lb | OR 74 | draw 0 | jockey Harry Atkins(5) | trainer Dan Skelton (14d 23/95) | headgear - | last run 3 days | form 5543-1 | MARKET 55.4% | 09:00 median 1.53 | Matchbook 1.66
    comment: The form before that win, a third, a fourth and two fifths, is hard to get excited about.
    DATA: model 19.4% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 7 Mar Hereford Hurdle 19.7f Good 4/11; 26 Mar Chepstow Hurdle 16.1f Good To Soft 3/7; 24 Nov Southwell Hurdle 16f Good 1/14 fig 85
    DATA for: Recent figures 11 lb above its current mark (looks well handicapped); Trainer 24% wins (23/95), last 14 days; Has won at this trip or further; Good recent finishing positions; Carries 7 lb less than average
    DATA against: Official rating 74, 13 lb below field average; Race comments mention jumping mistakes in 2 of its last 5 runs
- River Glance (hrs_50187837) | 5yo G | 142lb | OR 71 | draw 0 | jockey Lilly Pinchin | trainer Emma-Jane Bishop (14d 0/0) | headgear ht | wind surgery | last run 29 days | form P705-3 | MARKET 15.0% | 09:00 median 5.50 | Matchbook 6.40
    comment: He has run over today's trip and going before, but 142 lb is a stiff burden.
    DATA: model 13.1% | style Midfield (led 4% of runs) | runs in data 4 | last 3: 18 Feb Ludlow Hurdle 15.8f Soft 10/12; 28 Mar Stratford Hurdle 16.3f Good 5/11; 29 Oct Stratford Hurdle 18.5f Good To Soft 3/11 fig 71
    DATA for: Carries 15 lb less than average
    DATA against: Best recent form figure 71, 16 lb below field average; Official rating 71, 16 lb below field average; Race comments mention jumping mistakes in 2 of its last 4 runs
- Blue Sky Dreaming (hrs_50401673) | 5yo G | 167lb | OR 98 | draw 0 | jockey Kielan Woods | trainer Alan King (14d 4/26) | headgear - | last run 24 days | form 44P4-8 | MARKET 11.5% | 09:00 median 7.00 | Matchbook 8.60
    comment: Blue Sky Dreaming is yet to win in his last five starts, but he has been a fourth three times in his last four completed runs, and he returns fresh after 24 days with experience of today's trip and going.
    DATA: model 13.9% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 19 Jan Lingfield Hurdle 19.5f Soft PU/13; 23 Feb Plumpton Hurdle 15.9f Soft 4/7; 3 Nov Warwick Hurdle 16f Good 8/11 fig 93
    DATA for: Best recent form figure 93, 6 lb above field average; Official rating 98, 11 lb above field average
    DATA against: Carries 10 lb more than average; Pulled up in 1 of its last 3 jumps runs
- Moi Mon Vieux (hrs_64621466) | 4yo G | 149lb | OR 80 | draw 0 | jockey James Best | trainer Richard Hobson (14d 0/4) | headgear t | last run 13 days | form 24463 | MARKET 7.0% | 09:00 median 11.00 | Matchbook 14.50
    comment: The one concern is that he's yet to win in his last five starts, with 149 lb to carry.
    DATA: model 4.0% | style Midfield (led 4% of runs) | runs in data 5 | last 3: 25 Sep Worcester Hurdle 20f Good 4/9; 15 Oct Fontwell Hurdle 19f Good To Soft 6/7; 14 Nov Uttoxeter Hurdle 16f Good 3/12 fig 85
    DATA for: Recent figures 5 lb above its current mark (looks well handicapped); Carries 8 lb less than average
    DATA against: Official rating 80, 7 lb below field average
- Hijo de La Luna (hrs_34774964) | 6yo G | 155lb | OR 86 | draw 0 | jockey Jack Quinlan | trainer Simon West (14d 0/3) | headgear v | last run 59 days | form P5-434 | MARKET 3.9% | 09:00 median 21.00 | Matchbook 27.00
    comment: Fourth last time out, and a third two starts back, show Hijo de La Luna is running consistently, and he has run over today's trip and going before.
    DATA: model 12.6% | style Held up (led 3% of runs) | runs in data 14 | last 3: 28 Aug Sedgefield Hurdle 16.8f Good 4/10; 16 Sep Kelso Hurdle 18.1f Good To Firm 3/8; 29 Sep Sedgefield Hurdle 19.9f Good 4/8
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Gallant Lion (hrs_31631334) | 6yo G | 168lb | OR 99 | draw 0 | jockey Charlie Todd | trainer Ian Williams (14d 3/32) | headgear - | last run 24 days | form 45/5-7 | MARKET 2.9% | 09:00 median 26.00 | Matchbook 40.00
    comment: Gallant Lion has run over today's trip and going and was a fourth four starts back, with fifth-place finishes in the two runs after that, and he returns fresh after 24 days.
    DATA: model 11.7% | style Midfield (led 5% of runs) | runs in data 8 | last 3: 28 Sep Brighton Flat 11.9f Good To Firm 4/7; 9 Oct Kempton Flat 12f Standard To Slow 6/7; 3 Nov Warwick Hurdle 16f Good 7/11 fig 94
    DATA for: Best recent form figure 94, 7 lb above field average; Official rating 99, 12 lb above field average
    DATA against: Carries 11 lb more than average
- Kenny's Jewel (hrs_57654534) | 4yo F | 167lb | OR 98 | draw 0 | jockey Lee Edwards | trainer Dylan Cunha (14d 2/15) | headgear tp | last run 26 days | form 8-0615 | MARKET 2.1% | 09:00 median 34.00 | Matchbook 65.00
    comment: Kenny's Jewel won two starts back but was only fifth last time out, and she has a patchy look beyond that, with a sixth and an eighth in her last five.
    DATA: model 18.0% | style Prominent (led 3% of runs) | runs in data 4 | last 3: 3 Aug Cork Hurdle 17f Good 6/18; 14 Aug Tramore Hurdle 21f Good 1/15; 1 Nov Huntingdon Hurdle 20.5f Good 5/7 fig 89
    DATA for: Official rating 98, 11 lb above field average; Has won at this trip or further
    DATA against: Recent figures 9 lb below its current mark (looks high in the weights); Last-run finishing speed -4.0% vs that field (faded); Carries 10 lb more than average
- Enziya (hrs_46265366) | 4yo G | 154lb | OR 85 | draw 0 | jockey Rian Corcoran(5) | trainer Kevin Pickard (14d 0/1) | headgear tp | last run 10 days | form 57F8-P | MARKET 1.2% | 09:00 median 67.00 | Matchbook 130.00
    comment: Enziya is winless in his last five, with a pulled up last time out and a fall three starts back, though he's only 10 days since that run and has run over today's trip.
    DATA: model 4.0% | style Held up (led 3% of runs) | runs in data 4 | last 3: 18 Sep Newton Abbot Hurdle 16.8f Good PU/11; 5 Nov Chelmsford (AW) Flat 16f Standard 5/6 fig 66; 17 Nov Southwell (AW) Flat 12f Standard 6/11 fig 51
    DATA against: Pulled up in 1 of its last 2 jumps runs; Pace: steady gallop likely, hard to come from off the pace
- Laios Tresor (hrs_49578130) | 5yo G | 162lb | OR 93 | draw 0 | jockey Tabitha Worsley | trainer Georgie Howell (14d 0/1) | headgear - | last run 36 days | form 4/88-8 | MARKET 1.1% | 09:00 median 51.00 | Matchbook 170.00
    comment: Laios Tresor has finished eighth in each of his last three starts after a fourth four runs back, and he is yet to score in that spell.
    DATA: model 3.2% | style Held up (led 5% of runs) | runs in data 3 | last 3: 22 Jan Huntingdon Hurdle 15.8f Soft 8/16; 12 Apr Ffos Las Hurdle 15.8f Good To Soft 8/12; 22 Oct Ffos Las Hurdle 16f Soft 8/11 fig 91
    DATA for: Best recent form figure 91, 4 lb above field average; Official rating 93, 6 lb above field average
    DATA against: Poor recent finishing positions; Pace: steady gallop likely, hard to come from off the pace

## 2:45 Doncaster | race_id rac_32305723190 | Download The At The Races App Handicap Hurdle Race (Go North Cab On Target Series Qualifier)
Hurdle | Class 5 | 2m3f88y | going Good | Turf | 8 runners | rating band 0-100 | age 3yo+
DATA pace: Even - Two likely leaders (Dusky Days, Bannister). A fair, even gallop is most likely.
- Anxious Moments (hrs_61911598) | 4yo G | 162lb | OR 92 | draw 0 | jockey Richie McLernon | trainer Charlie Longsdon (14d 2/14) | headgear - | last run 25 days | form -69611 | MARKET 38.4% | 09:00 median 2.20 | Matchbook 2.54
    comment: Two wins in his last five, including last time out, is a real positive, and he has run over today's trip and going, but 162 lb off an official 92 is a big ask.
    DATA: model 21.5% | style Midfield (led 4% of runs) | runs in data 6 | last 3: 20 Sep Plumpton Hurdle 20.5f Good 6/6; 13 Oct Southwell Hurdle 20.4f Good 1/11; 2 Nov Southwell Hurdle 20.5f Good 1/11 fig 83
    DATA for: Official rating 92, 8 lb above field average; Last-run finishing speed +4.8% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Recent figures 9 lb below its current mark (looks high in the weights); Carries 7 lb more than average
- Thesoldiersminit (hrs_57439228) | 5yo G | 158lb | OR 87 | draw 0 | jockey Robert Dunne | trainer Sam Allwood (14d 1/3) | headgear - | last run 31 days | form 735-42 | MARKET 21.0% | 09:00 median 4.33 | Matchbook 4.50
    comment: Thesoldiersminit arrives in decent heart after a second last time out, following a fourth and a fifth, and he has run on today's going before.
    DATA: model 15.7% | style Midfield (led 3% of runs) | runs in data 4 | last 3: 1 Mar Huntingdon Hurdle 15.8f Good To Soft 5/7; 7 Oct Worcester Hurdle 16f Good 4/10; 27 Oct Newcastle Hurdle 17f Good 2/10 fig 90
    DATA for: Best recent form figure 90, 7 lb above field average; Last-run finishing speed +3.2% vs that field (finished strongly)
- Bannister (hrs_19992483) | 9yo G | 154lb | OR 83 | draw 0 | jockey Tom Broughton(3) | trainer Nick Kent (14d 0/3) | headgear - | last run 29 days | form 604744 | MARKET 10.2% | 09:00 median 8.00 | Matchbook 9.80
    comment: Bannister is yet to win in his last six starts, but he has finished fourth in two of his last three, and he has run over today's trip and going before.
    DATA: model 9.2% | style Leader (led 63% of runs) | runs in data 6 | last 3: 14 Sep Sedgefield Hurdle 19.9f Good 7/10; 8 Oct Market Rasen Hurdle 16.6f Good 4/6; 29 Oct Stratford Hurdle 18.5f Good To Soft 4/11 fig 83
    DATA against: Aged 9, older than most of this field
- Dusky Days (hrs_24846549) | 9yo G | 160lb | OR 89 | draw 0 | jockey Leah Noreci(7) | trainer James Moffatt (14d 0/6) | headgear p | last run 20 days | form 786852 | MARKET 7.8% | 09:00 median 11.00 | Matchbook 12.50
    comment: Dusky Days bounced back with a second last time out, just 20 days ago, and he has run over today's trip and on this going before. A big weight of 160 lb is the main risk, with his earlier form reading fifth, eighth, sixth, eighth and seventh.
    DATA: model 11.1% | style Leader (led 29% of runs) | runs in data 8 | last 3: 29 Aug Cartmel Hurdle 25.4f Good 8/12; 22 Oct Carlisle Hurdle 20f Good 5/13 fig 80; 7 Nov Kelso Hurdle 21f Good 2/11 fig 88
    DATA for: Best recent form figure 88, 5 lb above field average
    DATA against: Carries 5 lb more than average; Aged 9, older than most of this field
- Snapaudaciaheros (hrs_412652912) | 6yo M | 155lb | OR 84 | draw 0 | jockey Joe Williamson | trainer Rebecca Menzies (14d 0/10) | headgear tp | last run 24 days | form -P1735 | MARKET 7.6% | 09:00 median 11.00 | Matchbook 13.50
    comment: Snapaudaciaheros was fifth last time out and a third two starts back, but she has a seventh and a pulled up in her last five and has won just once, four starts back.
    DATA: model 12.5% | style Prominent (led 4% of runs) | runs in data 9 | last 3: 21 Jun Hexham Hurdle 16.2f Good 7/10; 20 Oct Hexham Hurdle 16f Good 3/10 fig 87; 3 Nov Sedgefield Hurdle 17f Good 5/11 fig 80
    DATA for: Best recent form figure 87, 4 lb above field average
    DATA against: Trainer 0 wins from 10 runs, last 14 days; Pulled up in 1 of its last 5 jumps runs
- Bouboule (hrs_48700470) | 4yo G | 144lb | OR 74 | draw 0 | jockey Danny McMenamin | trainer Gillian Boanas (14d 0/1) | headgear tb | last run 15 days | form 765534 | MARKET 6.4% | 09:00 median 13.00 | Matchbook 16.00
    comment: Fourth last time out and a third two starts back, Bouboule has been creeping closer, and he has run on today's going and is fresh enough after 15 days off.
    DATA: model 10.4% | style Midfield (led 3% of runs) | runs in data 13 | last 3: 20 Oct Hexham Hurdle 16f Good 5/10 fig 76; 27 Oct Newcastle Hurdle 17f Good 3/10 fig 78; 12 Nov Market Rasen Hurdle 20.5f Good To Soft 4/6
    DATA for: Recent figures 4 lb above its current mark (looks well handicapped); Carries 11 lb less than average
    DATA against: Best recent form figure 78, 5 lb below field average; Official rating 74, 10 lb below field average
- Klapton Boy (hrs_41052172) | 6yo G | 149lb | OR 78 | draw 0 | jockey Charlie Hammond | trainer Nick Kent (14d 0/3) | headgear p (1st time) | last run 14 days | form 56-64P | MARKET 5.8% | 09:00 median 15.00 | Matchbook 17.00
    comment: Klapton Boy has run over today's trip and on this going, and a fourth two starts back shows he can get involved, while 14 days since his last run keeps him fresh.
    DATA: model 9.9% | style Prominent (led 3% of runs) | runs in data 5 | last 3: 8 May Market Rasen Hurdle 16.6f Good 6/9; 25 Oct Market Rasen Hurdle 16.5f Good To Soft 4/6 fig 77; 13 Nov Southwell Hurdle 16f Good PU/11
    DATA for: Carries 6 lb less than average; First-time headgear
    DATA against: Best recent form figure 77, 6 lb below field average; Official rating 78, 6 lb below field average; Pulled up in 1 of its last 5 jumps runs
- Eyeeye (hrs_30455124) | 6yo G | 157lb | OR 86 | draw 0 | jockey Kielan Woods | trainer Clare Ellam (14d 0/1) | headgear - | last run 3 days | form 508479 | MARKET 2.8% | 09:00 median 29.00 | Matchbook 38.00
    comment: The risk is a winless run in his last six, with no finish better than a fourth.
    DATA: model 9.8% | style Held up (led 4% of runs) | runs in data 10 | last 3: 13 Oct Southwell Hurdle 20.4f Good 4/11; 6 Nov Fontwell Hurdle 17.5f Good 7/10 fig 73; 24 Nov Southwell Hurdle 24.5f Good 9/9 fig 76
    DATA against: Best recent form figure 76, 7 lb below field average; Recent figures 10 lb below its current mark (looks high in the weights)

## 3:20 Doncaster | race_id rac_32305725127 | Apres Village At Doncaster Racecourse 'Hands & Heels' Handicap Hurdle Race (Conditional & Amateur Jockeys' Race) (Part Of The Racing Excellence Series)
Hurdle | Class 5 | 3m0f84y | going Good | Turf | 5 runners | rating band 0-105 | age 4yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Sledgehammer (hrs_58565304) | 6yo G | 156lb | OR 99 | draw 0 | jockey Mr S Cotter(3) | trainer Adrian Keatley (14d 1/7) | headgear - | last run 3 days | form 64F111 | MARKET 48.9% | 09:00 median 1.80 | Matchbook 1.99
    comment: He has run over today's trip and going before.
    DATA: model 42.0% | style Held up (led 3% of runs) | runs in data 9 | last 3: 10 Oct Hexham Chase 24.2f Good 1/9; 31 Oct Wetherby Chase 24f Good 1/4 fig 92; 24 Nov Southwell Chase 24.5f Good 1/9 fig 102
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Race comments mention jumping mistakes in 2 of its last 5 runs; Fell or unseated in 1 of its last 5 jumps runs; First run over hurdles in our data; Pace: steady gallop likely, hard to come from off the pace
- Biglesisback (hrs_52451658) | 6yo M | 161lb | OR 104 | draw 0 | jockey Gregor Walkingshaw | trainer Lucinda Russell & Michael Scudamore (14d 1/19) | headgear - | last run 38 days | form 2P3-22 | MARKET 20.2% | 09:00 median 4.50 | Matchbook 4.80
    comment: Biglesisback arrives in cracking nick, second last time out and again two starts back, with a third three starts back, and she has run over today's trip and on this going before. The one concern is that she is yet to win in her last five and shoulders 161 lb.
    DATA: model 24.1% | style Midfield (led 23% of runs) | runs in data 5 | last 3: 17 Mar Wetherby Hurdle 19.7f Good To Soft 3/6; 24 Sep Perth Hurdle 20.2f Good 2/5; 20 Oct Hexham Hurdle 20f Good 2/5 fig 99
    DATA for: Last-run finishing speed +3.3% vs that field (finished strongly); Good recent finishing positions
    DATA against: Pulled up in 1 of its last 5 jumps runs
- Johnny Moonshine (hrs_50188873) | 5yo G | 161lb | OR 104 | draw 0 | jockey Harry Brown | trainer Donald McCain (14d 2/21) | headgear - | wind surgery | last run 36 days | form 446P-4 | MARKET 17.0% | 09:00 median 5.50 | Matchbook 5.50
    comment: The risk is that he's yet to win in his last five starts and carries 161 lb.
    DATA: model 14.0% | style Prominent (led 3% of runs) | runs in data 4 | last 3: 16 Feb Carlisle Hurdle 19.3f Good To Soft 6/10; 18 Apr Bangor-on-Dee Hurdle 23.1f Good PU/5; 22 Oct Carlisle Hurdle 17f Good 4/13 fig 110
    DATA for: Best recent form figure 110, 8 lb above field average; Recent figures 6 lb above its current mark (looks well handicapped)
    DATA against: Race comments mention jumping mistakes in 2 of its last 4 runs; Pulled up in 1 of its last 4 jumps runs
- Vaguely Royal (hrs_31996251) | 6yo G | 162lb | OR 105 | draw 0 | jockey Richard Upton(3) | trainer Ian Williams (14d 3/32) | headgear v | last run 32 days | form 3/55P- | MARKET 10.5% | 09:00 median 9.00 | Matchbook 9.20
    comment: Vaguely Royal is yet to win in his last four, but a third four starts back and two fifths since show some consistency, and he has run on today's going before.
    DATA: model 10.3% | style Held up (led 3% of runs) | runs in data 14 | last 3: 2 Oct Ascot Flat 15.9f Good To Firm 5/5; 10 Oct Newmarket Flat 18f Good 13/29; 26 Oct Southwell (AW) Flat 16.5f Standard 4/6
    DATA against: First run over hurdles in our data; Pace: steady gallop likely, hard to come from off the pace
- Glitz And Glamour (hrs_50433019) | 5yo M | 160lb | OR 103 | draw 0 | jockey Mr Evan Lonergan(5) | trainer Neil King (14d 0/5) | headgear - | last run 11 days | form -P6046 | MARKET 3.5% | 09:00 median 29.00 | Matchbook 30.00
    comment: She has run on today's going and is back quickly after 11 days, but 160 lb is a big ask.
    DATA: model 9.7% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 4 Aug Roscommon Hurdle 24f Yielding To Soft 11/15; 28 Sep Newton Abbot Hurdle 26.5f Good 4/7; 16 Nov Plumpton Hurdle 20.5f Good To Soft 6/12 fig 97
    DATA for: Last-run finishing speed +4.3% vs that field (finished strongly)
    DATA against: Best recent form figure 97, 5 lb below field average; Recent figures 6 lb below its current mark (looks high in the weights); Pulled up in 1 of its last 5 jumps runs
