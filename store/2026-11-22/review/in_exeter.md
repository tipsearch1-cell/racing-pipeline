# Card review packet: Exeter, 2026-11-22

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
{"meeting": "exeter", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 12:37 Exeter | race_id rac_32305124657 | Sunday At The Races With Greendale EBF Junior 'National Hunt' Hurdle Race (GBB Race)
Hurdle | Class 4 | 2m0f161y | going Good | Turf | 5 runners | rating band - | age 3yo
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Our Wee Horse (hrs_17393186594) | 3yo G | 154lb | OR - | draw 0 | jockey Paul O'Brien | trainer Harry Derham (14d 3/10) | headgear - | last run 27 days | form 25 | MARKET 39.1% | 09:00 median 2.25 | Matchbook 2.50
    comment: The main risk is that he's yet to win in his last two starts and carries 154 lb.
    DATA: model 51.4% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 3 Oct Fontwell Hurdle 17.7f Good 2/8; 26 Oct Hereford Hurdle 16f Good To Firm 5/9
    DATA for: Trainer 30% wins (3/10), last 14 days
    DATA against: Last-run finishing speed -4.6% vs that field (faded); Lightly raced: 2 runs in our data, so the model has little to go on
- Golden Dagger (hrs_17395806610) | 3yo G | 154lb | OR - | draw 0 | jockey Ciaran Gethings | trainer Mrs Jane Williams (14d 1/5) | headgear - | last run - days | form - | MARKET 30.9% | 09:00 median 3.00 | Matchbook 3.10
    comment: The gelding carries 154 lb and is wholly unexposed, which leaves him open to progress.
    DATA: model 16.2% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 20% wins (1/5), last 14 days
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Naturaouse (hrs_17395272594) | 3yo G | 154lb | OR - | draw 0 | jockey Caoilin Quinn | trainer Warren Greatrex (14d 6/17) | headgear - | last run - days | form - | MARKET 23.6% | 09:00 median 3.75 | Matchbook 4.20
    comment: Naturaouse is a complete unknown, with no recorded form on his debut, so he's unexposed and open to any amount of improvement.
    DATA: model 16.2% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 35% wins (6/17), last 14 days
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Nichoir (hrs_17395091112) | 3yo G | 154lb | OR - | draw 0 | jockey Jack Tudor | trainer Christian Williams (14d 1/6) | headgear - | last run 15 days | form 6 | MARKET 3.9% | 09:00 median 23.00 | Matchbook 27.00
    DATA: model 6.5% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 7 Nov Aintree NH Flat 17f Good To Soft 6/6 fig 89
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Royal Castle (hrs_17395276766) | 3yo G | 154lb | OR - | draw 0 | jockey David Noonan | trainer Nigel Hawke (14d 1/7) | headgear - | last run 11 days | form 6 | MARKET 2.6% | 09:00 median 41.00 | Matchbook 38.00
    comment: Unexposed gelding who finished sixth last time out just 11 days ago, so he should be fit; he's yet to win in that sole recent start and looks open to improvement carrying 154 lb.
    DATA: model 9.8% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 11 Nov Bangor-on-Dee Hurdle 16.5f Good 6/7
    DATA against: Last-run finishing speed -5.8% vs that field (faded); Lightly raced: 1 run in our data, so the model has little to go on

## 1:07 Exeter | race_id rac_32305126594 | Elf Exeter Leukaemia Fund Mares' Novices' Hurdle Race (GBB Race)
Hurdle | Class 4 | 2m7f25y | going Good | Turf | 6 runners | rating band - | age 4yo+
DATA pace: Lone leader - Poet's Muse is the only habitual front-runner and may be allowed an easy lead.
- Seventeenothree (hrs_48499241) | 6yo M | 154lb | OR 71 | draw 0 | jockey Jack Tudor | trainer Kayley Woollacott (14d 1/9) | headgear t (1st time) | last run 230 days | form 69452- | MARKET 26.4% | 09:00 median 3.50 | Matchbook 3.60 | CHECK (skip line 3.32)
    DATA: model 17.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: First-time headgear
    DATA against: Official rating 71, 7 lb below field average; Returns from a 230-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Poet's Muse (hrs_51618973) | 5yo M | 154lb | OR 82 | draw 0 | jockey Ciaran Gethings | trainer Ian Chanin (14d 0/0) | headgear p | last run 27 days | form 2-7PF6 | MARKET 25.5% | 09:00 median 3.50 | Matchbook 3.80
    DATA: model 32.9% | style Leader (led 38% of runs) | runs in data 8 | last 3: 28 Sep Newton Abbot Hurdle 26.5f Good PU/7; 11 Oct Chepstow Hurdle 23.6f Good To Soft F/12; 26 Oct Hereford Hurdle 25.5f Good To Firm 6/8 fig 77
    DATA for: Pace: may get an uncontested lead
    DATA against: Last-run finishing speed -2.6% vs that field (faded); Poor recent finishing positions; Race comments mention jumping mistakes in 2 of its last 5 runs; Fell or unseated in 1 of its last 5 jumps runs; Pulled up in 1 of its last 5 jumps runs
- Little Twig (hrs_62779920) | 5yo M | 154lb | OR - | draw 0 | jockey Harry Reed | trainer Nick Scholfield (14d 1/14) | headgear - | last run 132 days | form 7-343 | MARKET 17.4% | 09:00 median 5.00 | Matchbook 5.70
    DATA: model 18.9% | style Held up (led 8% of runs) | runs in data 2 | last 3: 26 Jun Bangor-on-Dee Hurdle 19.6f Good 4/7; 13 Jul Newton Abbot Hurdle 18.5f Good To Firm 3/4
    DATA against: Last-run finishing speed -3.2% vs that field (faded); Returns from a 132-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- Correen (hrs_17395567763) | 5yo M | 154lb | OR - | draw 0 | jockey Paddy Hanlon(5) | trainer John Joseph Hanlon (14d 0/9) | headgear - | last run 36 days | form FP-2 | MARKET 16.8% | 09:00 median 5.00 | Matchbook 6.00
    DATA: model 8.9% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Trainer 0 wins from 9 runs, last 14 days; Lightly raced: 0 runs in our data, so the model has little to go on
- Stavanger Rose (hrs_50402520) | 6yo M | 154lb | OR 80 | draw 0 | jockey Tabitha Worsley | trainer Ben Lund (14d 0/0) | headgear - | last run 19 days | form -6405F | MARKET 10.3% | 09:00 median 9.00 | Matchbook 9.40
    DATA: model 17.2% | style Midfield (led 3% of runs) | runs in data 9 | last 3: 1 Jul Worcester Hurdle 20f Good 10/11; 19 Jul Newton Abbot Hurdle 26.5f Good To Firm 5/6; 3 Nov Warwick Hurdle 21f Good F/10
    DATA against: Fell or unseated in 1 of its last 5 jumps runs
- Winding Lake (hrs_17394838706) | 5yo M | 154lb | OR - | draw 0 | jockey James Best | trainer Harriet Dickin (14d 0/4) | headgear - | last run 19 days | form P31-24 | MARKET 3.5% | 09:00 median 21.00 | Matchbook 36.00
    DATA: model 4.7% | style Unknown | runs in data 1 | last 3: 3 Nov Warwick Hurdle 19f Good 4/6
    DATA against: Last-run finishing speed -6.8% vs that field (faded); Lightly raced: 1 run in our data, so the model has little to go on

## 1:37 Exeter | race_id rac_32305128531 | Chris Down A Lifetime In Racing Novices' Limited Handicap Steeple Chase (GBB Race)
Chase | Class 3 | 3m0f54y | going Good | Turf | 6 runners | rating band 0-130 | age 4yo+
DATA pace: Lone leader - Red Dirt Road is the only habitual front-runner and may be allowed an easy lead.
- Torrent (hrs_36970423) | 5yo G | 152lb | OR 117 | draw 0 | jockey Charlie Deutsch | trainer Nigel Hawke (14d 1/7) | headgear p | last run 8 days | form 533321 | MARKET 23.7% | 09:00 median 3.75 | Matchbook 4.10 | CHECK (skip line 3.56)
    comment: Torrent arrives in cracking nick, a winner last time out, a second two starts back and a third three starts back, and he has run over today's trip and going.
    DATA: model 23.0% | style Prominent (led 29% of runs) | runs in data 9 | last 3: 15 Sep Uttoxeter Hurdle 23.3f Good 3/8; 10 Oct Chepstow Hurdle 23.6f Good To Soft 2/17; 14 Nov Uttoxeter Chase 24f Good 1/7 fig 108
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Best recent form figure 108, 9 lb below field average; Recent figures 9 lb below its current mark (looks high in the weights)
- Silver Hill (hrs_44975042) | 6yo G | 155lb | OR 120 | draw 0 | jockey Gavin Sheehan | trainer Jamie Snowden (14d 5/22) | headgear - | last run 26 days | form 1221-4 | MARKET 20.4% | 09:00 median 4.33 | Matchbook 4.80
    comment: Silver Hill brings strong recent form, with a win two starts back and another five starts back, plus two seconds in between, and he has run over today's trip after 26 days off. Last time's fourth is the one blemish, and his 155 lb burden looks the main risk.
    DATA: model 19.0% | style Prominent (led 3% of runs) | runs in data 4 | last 3: 3 Mar Newcastle Hurdle 20.3f Good To Soft 2/12; 18 Mar Hereford Hurdle 19.7f Good 1/7; 27 Oct Newcastle Chase 23.5f Good 4/4 fig 117
    DATA for: Trainer 23% wins (5/22), last 14 days; Good recent finishing positions
- Champagne Chic (hrs_48700505) | 6yo G | 162lb | OR 127 | draw 0 | jockey Lorcan Williams | trainer Jeremy Scott (14d 0/10) | headgear p | last run 29 days | form 1100-8 | MARKET 20.0% | 09:00 median 4.50 | Matchbook 4.90
    comment: Champagne Chic won twice in a row four and five starts back, and he has run over today's trip, so a bounce-back from an eighth last time out is plausible after 29 days off.
    DATA: model 13.5% | style Held up (led 5% of runs) | runs in data 5 | last 3: 12 Mar Cheltenham Hurdle 24f Good 12/24; 30 Apr Punchestown Hurdle 23.5f Yielding 22/24; 24 Oct Cheltenham Hurdle 24f Good 8/19 fig 122
    DATA for: Best recent form figure 122, 5 lb above field average; Official rating 127, 5 lb above field average; Has won at this trip or further
    DATA against: Trainer 0 wins from 10 runs, last 14 days; Poor recent finishing positions; Carries 5 lb more than average; First run over fences in our data
- Solar System (hrs_34789727) | 7yo G | 149lb | OR 114 | draw 0 | jockey Callum Pritchard | trainer Philip Hobbs & Johnson White (14d 2/13) | headgear p | last run 232 days | form /5036- | MARKET 13.4% | 09:00 median 6.50 | Matchbook 7.40
    comment: Solar System is winless in his last four, beaten into sixth last time and returning after 232 days off, which makes him hard to fancy.
    DATA: model 12.7% | style Held up (led 3% of runs) | runs in data 4 | last 3: 14 Feb Ascot Hurdle 23.6f Good To Soft 15/18; 2 Mar Southwell Chase 24.3f Soft 3/6; 4 Apr Haydock Chase 25.6f Good 6/11
    DATA for: Carries 8 lb less than average
    DATA against: Official rating 114, 8 lb below field average; Returns from a 232-day break
- Red Dirt Road (hrs_27997361) | 9yo G | 164lb | OR 129 | draw 0 | jockey Jonjo O'Neill Jr. | trainer Jonjo & A.J. O'Neill (14d 5/39) | headgear - | last run 221 days | form /P407- | MARKET 11.6% | 09:00 median 7.90 | Matchbook 8.60
    comment: Without a win in his last four starts, Red Dirt Road returns after 221 days off with a fourth three starts back his best recent finish, but he has run over today's trip and carries 164 lb off an official 129.
    DATA: model 14.6% | style Leader (led 43% of runs) | runs in data 4 | last 3: 14 Feb Haydock Hurdle 24.3f Good To Soft 4/13; 12 Mar Cheltenham Hurdle 24f Good 19/24; 15 Apr Haydock Hurdle 24.3f Good 7/10
    DATA for: Official rating 129, 7 lb above field average; Pace: may get an uncontested lead
    DATA against: Last-run finishing speed -5.1% vs that field (faded); Carries 7 lb more than average; Returns from a 221-day break; Race comments mention jumping mistakes in 2 of its last 4 runs; Pulled up in 1 of its last 4 jumps runs; First run over fences in our data
- Rickety Bridge (hrs_34652338) | 7yo G | 159lb | OR 124 | draw 0 | jockey Freddie Gingell | trainer Paul Nicholls (14d 2/17) | headgear p | last run 20 days | form 4-1113 | MARKET 10.9% | 09:00 median 8.00 | Matchbook 9.20
    comment: Rickety Bridge arrives in cracking nick, a third last time out following a hat-trick of wins, and he has run over today's trip and is fresh enough after 20 days off. The main risk is 159 lb, a hefty burden to carry.
    DATA: model 17.1% | style Held up (led 4% of runs) | runs in data 6 | last 3: 27 May Newton Abbot Chase 25.8f Good 1/4; 12 Jun Newton Abbot Chase 25.8f Good 1/4; 2 Nov Plumpton Chase 25.5f Good 3/6 fig 121
    DATA for: Best recent form figure 121, 4 lb above field average; Has won at this trip or further; Good recent finishing positions
    DATA against: Race comments mention jumping mistakes in 2 of its last 5 runs

## 2:07 Exeter | race_id rac_32305130468 | Happy 70th David Clements Handicap Hurdle Race
Hurdle | Class 3 | 2m2f111y | going Good | Turf | 5 runners | rating band 0-130 | age 3yo+
DATA pace: Lone leader - Son of Hypnos is the only habitual front-runner and may be allowed an easy lead.
- Mwabani (hrs_58412088) | 4yo G | 155lb | OR 115 | draw 0 | jockey Ciaran Gethings | trainer Mrs Jane Williams (14d 1/5) | headgear - | last run 42 days | form 222-1 | MARKET 33.8% | 09:00 median 2.63 | Matchbook 2.94
    comment: Mwabani arrives in cracking form, a winner last time out after three straight seconds, and he looks a strong threat on that evidence.
    DATA: model 28.1% | style Prominent (led 29% of runs) | runs in data 3 | last 3: 13 Feb Chepstow Hurdle 16.1f Soft 2/5; 22 Mar Exeter Hurdle 16.7f Good 2/9; 11 Oct Chepstow Hurdle 16.1f Good To Soft 1/6
    DATA for: Trainer 20% wins (1/5), last 14 days; Last-run finishing speed +7.2% vs that field (finished strongly); Good recent finishing positions
- Treasure Planet (hrs_45413144) | 4yo G | 159lb | OR 119 | draw 0 | jockey Sam Twiston-Davies | trainer Paul Nicholls (14d 2/17) | headgear - | last run 17 days | form 232-17 | MARKET 25.1% | 09:00 median 3.50 | Matchbook 4.00
    comment: The risk is a seventh last time out, plus 159 lb to carry.
    DATA: model 20.1% | style Held up (led 4% of runs) | runs in data 5 | last 3: 24 Apr Chepstow Hurdle 19.5f Good 2/8; 10 Oct Chepstow Hurdle 16.1f Good To Soft 1/12; 5 Nov Newbury Hurdle 16.5f Good To Soft 7/16 fig 118
    DATA for: Good recent finishing positions
- Handlethekettle (hrs_39148130) | 7yo G | 163lb | OR 122 | draw 0 | jockey Gavin Sheehan | trainer Jamie Snowden (14d 5/22) | headgear - | last run 23 days | form 311-22 | MARKET 20.6% | 09:00 median 4.33 | Matchbook 4.80
    comment: Handlethekettle arrives in cracking form, runner-up in his last two starts after back-to-back wins before that, and he has run over today's trip and going before.
    DATA: model 19.4% | style Unknown | runs in data 2 | last 3: 4 Sep Worcester Hurdle 20f Good 2/8; 30 Oct Wetherby Hurdle 19.5f Good 2/4 fig 121
    DATA for: Official rating 122, 5 lb above field average; Trainer 23% wins (5/22), last 14 days; Good recent finishing positions
    DATA against: Carries 6 lb more than average; Lightly raced: 2 runs in our data, so the model has little to go on
- Washington (hrs_23048634) | 10yo G | 168lb | OR 127 | draw 0 | jockey Paul O'Brien | trainer Harry Derham (14d 3/10) | headgear - | last run 23 days | form 580-71 | MARKET 16.5% | 09:00 median 5.50 | Matchbook 5.90
    comment: Washington won last time out and returns after 23 days, a fresh and fit profile for a gelding who has run over today's trip.
    DATA: model 20.9% | style Midfield (led 4% of runs) | runs in data 4 | last 3: 28 Apr Punchestown Hurdle 16.6f Yielding 10/21; 10 Oct Chepstow Hurdle 19.5f Good To Soft 7/17; 30 Oct Wetherby Hurdle 19.5f Good 1/4 fig 124
    DATA for: Official rating 127, 10 lb above field average; Trainer 30% wins (3/10), last 14 days; Has won at this trip or further
    DATA against: Carries 11 lb more than average; Aged 10, older than most of this field
- Son of Hypnos (hrs_21687946) | 9yo G | 142lb | OR 101 | draw 0 | jockey Jack Stenhouse(7) | trainer Ryan Chapman (14d 0/0) | headgear - | last run 40 days | form -74164 | MARKET 4.0% | 09:00 median 23.00 | Matchbook 25.00
    comment: Hard to fancy, as he has finished fourth and sixth in his last two runs after a win three starts back, and he comes here after 40 days off carrying 142 lb.
    DATA: model 11.6% | style Leader (led 79% of runs) | runs in data 8 | last 3: 22 Aug Newton Abbot Hurdle 18.5f Good To Firm 1/10; 18 Sep Newton Abbot Hurdle 16.8f Good 6/11; 13 Oct Hereford Hurdle 19.7f Good To Firm 4/8
    DATA for: Has won at this trip or further; Carries 15 lb less than average; Pace: may get an uncontested lead
    DATA against: Official rating 101, 16 lb below field average

## 2:37 Exeter | race_id rac_32305132405 | Exminster Golf Club Supporting Elf Handicap Steeple Chase (GBB Race)
Chase | Class 4 | 2m3f48y | going Good | Turf | 9 runners | rating band 0-120 | age 4yo+
DATA pace: Strong pace - 5 habitual front-runners (Kel du Large, Start Again, Bonza Boy, It's A Breeze, Another Folly). A contested lead should set things up for horses coming from behind.
- Kel du Large (hrs_37702364) | 6yo G | 164lb | OR 115 | draw 0 | jockey Gavin Sheehan | trainer Jamie Snowden (14d 5/22) | headgear - | last run 26 days | form 712U-4 | MARKET 25.1% | 09:00 median 3.38 | Matchbook 3.85 | CHECK (skip line 3.21)
    comment: The unseated two runs ago and the 164 lb burden are the only slight concerns.
    DATA: model 11.6% | style Leader (led 29% of runs) | runs in data 5 | last 3: 8 Mar Warwick Hurdle 21f Good To Soft 2/9; 6 Apr Plumpton Hurdle 20.5f Good UR/12; 27 Oct Bangor-on-Dee Chase 20.5f Good To Soft 4/13 fig 111
    DATA for: Official rating 115, 6 lb above field average; Trainer 23% wins (5/22), last 14 days; Has won at this trip or further
    DATA against: Carries 6 lb more than average; Fell or unseated in 1 of its last 5 jumps runs; Pace: likely to be taken on for the lead
- Koukeo (hrs_40553632) | 6yo G | 168lb | OR 119 | draw 0 | jockey Jonjo O'Neill Jr. | trainer Jonjo & A.J. O'Neill (14d 5/39) | headgear p (1st time) | last run 22 days | form 75P-42 | MARKET 22.6% | 09:00 median 3.75 | Matchbook 4.30
    DATA: model 12.0% | style Midfield (led 4% of runs) | runs in data 8 | last 3: 17 Apr Ayr Chase 16.5f Soft PU/9; 15 Oct Fontwell Chase 19.5f Good To Soft 4/7 fig 108; 31 Oct Wetherby Chase 19.5f Good 2/8 fig 121
    DATA for: Best recent form figure 121, 11 lb above field average; Official rating 119, 10 lb above field average; First-time headgear
    DATA against: Carries 10 lb more than average; Pulled up in 1 of its last 5 jumps runs
- He Knows Better (hrs_32709558) | 8yo G | 165lb | OR 116 | draw 0 | jockey Caoilin Quinn | trainer Warren Greatrex (14d 6/17) | headgear - | wind surgery | last run 212 days | form 22132- | MARKET 11.2% | 09:00 median 7.50 | Matchbook 8.60
    comment: He Knows Better arrives with a consistent profile, finishing second last time out, a third two starts back and a winner three starts back, and he has run over today's trip. The main risk is a 212-day absence, with 165 lb to carry too.
    DATA: model 16.3% | style Prominent (led 29% of runs) | runs in data 4 | last 3: 18 Feb Southwell Chase 20.4f Soft 1/7; 20 Mar Newbury Chase 22.4f Good To Soft 3/5; 24 Apr Perth Chase 23.8f Good 2/5
    DATA for: Official rating 116, 7 lb above field average; Trainer 35% wins (6/17), last 14 days; Last-run finishing speed +4.2% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Carries 7 lb more than average; Returns from a 212-day break
- Another Folly (hrs_34557726) | 7yo G | 154lb | OR 105 | draw 0 | jockey Ciaran Gethings | trainer Mrs Jane Williams (14d 1/5) | headgear p | last run 36 days | form 44-442 | MARKET 10.8% | 09:00 median 8.20 | Matchbook 8.80
    comment: Another Folly arrives in solid shape after a second last time out, following four fourths in a row, and he has run over today's trip and going before. He is yet to win in that spell though, and 154 lb after 36 days off keeps him a midfield type.
    DATA: model 9.5% | style Leader (led 83% of runs) | runs in data 5 | last 3: 4 May Warwick Chase 20f Good 4/8; 5 Oct Stratford Chase 22.6f Good To Firm 4/9; 17 Oct Newton Abbot Chase 16.5f Good 2/5 fig 103
    DATA for: Trainer 20% wins (1/5), last 14 days
    DATA against: Best recent form figure 103, 7 lb below field average; Pace: likely to be taken on for the lead
- Bonza Boy (hrs_27358702) | 9yo G | 157lb | OR 108 | draw 0 | jockey Lorcan Williams | trainer Jeremy Scott (14d 0/10) | headgear p | last run 232 days | form /6124- | MARKET 6.8% | 09:00 median 11.00 | Matchbook 16.00
    comment: In his favour, he was fourth last time out, second two starts back and has run over today's trip.
    DATA: model 11.4% | style Leader (led 29% of runs) | runs in data 3 | last 3: 9 Jan Exeter Chase 17.5f Good To Soft 1/11; 14 Feb Wincanton Chase 20.2f Heavy 2/7; 4 Apr Haydock Chase 19.9f Good 4/6
    DATA for: Good recent finishing positions
    DATA against: Trainer 0 wins from 10 runs, last 14 days; Last-run finishing speed -4.0% vs that field (faded); Returns from a 232-day break; Pace: likely to be taken on for the lead
- Start Again (hrs_41189925) | 6yo G | 160lb | OR 111 | draw 0 | jockey Jack Hogan | trainer Fergal O'Brien (14d 4/31) | headgear tp | last run 39 days | form -P6511 | MARKET 6.4% | 09:00 median 13.00 | Matchbook 15.50
    DATA: model 12.7% | style Leader (led 63% of runs) | runs in data 5 | last 3: 6 Sep Fontwell Hurdle 19.1f Good 5/5; 6 Oct Huntingdon Chase 19.9f Good 1/4; 14 Oct Wetherby Chase 19.4f Good To Firm 1/2
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Pulled up in 1 of its last 5 jumps runs; Pace: likely to be taken on for the lead
- Kingcormac (hrs_22856050) | 10yo G | 146lb | OR 97 | draw 0 | jockey Callum Pritchard | trainer Joe Tickle (14d 0/6) | headgear - | last run 235 days | form 73114- | MARKET 6.3% | 09:00 median 13.00 | Matchbook 16.00
    comment: Kingcormac won two starts back and again three starts back, then finished fourth last time out, but he returns after 235 days off and carries 146 lb off an official mark of 97.
    DATA: model 12.7% | style Held up (led 3% of runs) | runs in data 5 | last 3: 6 Mar Exeter Chase 19.2f Good To Soft 1/11; 18 Mar Hereford Chase 20.9f Good 1/6; 1 Apr Wincanton Chase 20.2f Good 4/7
    DATA for: Has won at this trip or further; Good recent finishing positions; Carries 12 lb less than average; Pace: a contested lead should suit its hold-up style
    DATA against: Official rating 97, 12 lb below field average; Returns from a 235-day break; Race comments mention jumping mistakes in 2 of its last 5 runs; Aged 10, older than most of this field
- It's A Breeze (hrs_37974853) | 7yo G | 157lb | OR 108 | draw 0 | jockey Paddy Hanlon(5) | trainer Paul Nicholls (14d 2/17) | headgear t | last run 25 days | form 411232 | MARKET 5.5% | 09:00 median 15.00 | Matchbook 19.00
    comment: He has run over today's trip and going, which helps.
    DATA: model 7.9% | style Prominent (led 43% of runs) | runs in data 12 | last 3: 27 Aug Newton Abbot Chase 21f Good To Firm 2/4; 18 Sep Newton Abbot Chase 21f Good 3/3; 28 Oct Newton Abbot Chase 21f Good To Soft 2/6 fig 105
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Best recent form figure 105, 5 lb below field average
- Fight My Fire (hrs_49821646) | 5yo G | 151lb | OR 102 | draw 0 | jockey Freddie Gingell | trainer Joe Tizzard (14d 8/30) | headgear tp (1st time) | wind surgery | last run 44 days | form 4P48-P | MARKET 5.2% | 09:00 median 17.00 | Matchbook 18.50
    comment: The risk is plain: he was pulled up last time out and is yet to score in his last five.
    DATA: model 5.9% | style Prominent (led 3% of runs) | runs in data 4 | last 3: 18 Mar Hereford Hurdle 19.7f Good 4/6; 16 Apr Hereford Hurdle 16.2f Good 8/9; 9 Oct Chepstow Hurdle 16.1f Good To Soft PU/15
    DATA for: Trainer 27% wins (8/30), last 14 days; Carries 7 lb less than average; First-time headgear
    DATA against: Official rating 102, 7 lb below field average; Pulled up in 2 of its last 4 jumps runs; First run over fences in our data

## 3:07 Exeter | race_id rac_32305134342 | Exe containers.com 'Four Years Old' Handicap Hurdle Race (Challenger Two Mile Hurdle Series Qualifier)
Hurdle | Class 4 | 2m0f161y | going Good | Turf | 6 runners | rating band 0-115 | age 4yo
DATA pace: Lone leader - Out of Aces is the only habitual front-runner and may be allowed an easy lead.
- Bandjo (hrs_58195515) | 4yo G | 168lb | OR 115 | draw 0 | jockey Isabelle Ryder(5) | trainer Georgina Nicholls (14d 0/3) | headgear - | last run 20 days | form 605-88 | MARKET 24.8% | 09:00 median 3.50 | Matchbook 3.95 | CHECK (skip line 3.32)
    comment: A 124 rating against an official mark of 115 sets him apart in this field of six.
    DATA: model 15.3% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 10 Mar Cheltenham Hurdle 16.4f Good To Soft 10/22; 29 Mar Ascot Hurdle 15.7f Good 5/10; 2 Nov Plumpton Hurdle 20.5f Good 8/12 fig 108
    DATA for: Best recent form figure 108, 8 lb above field average; Official rating 115, 10 lb above field average
    DATA against: Recent figures 7 lb below its current mark (looks high in the weights); Carries 10 lb more than average
- Arbitration (hrs_42647864) | 4yo G | 155lb | OR 102 | draw 0 | jockey Freddie Gingell | trainer Joe Tizzard (14d 8/30) | headgear t (1st time) | wind surgery | last run 36 days | form 2256 | MARKET 19.7% | 09:00 median 4.50 | Matchbook 4.90
    DATA: model 10.3% | style Held up (led 5% of runs) | runs in data 4 | last 3: 28 May Worcester Hurdle 16f Good 2/6; 22 Sep Fontwell Hurdle 17.7f Good 5/5; 17 Oct Newton Abbot Hurdle 17f Good 6/7 fig 93
    DATA for: Trainer 27% wins (8/30), last 14 days; First-time headgear
    DATA against: Best recent form figure 93, 6 lb below field average; Recent figures 9 lb below its current mark (looks high in the weights)
- Modern Style (hrs_52021396) | 4yo G | 152lb | OR 99 | draw 0 | jockey James Best | trainer Nigel Hawke (14d 1/7) | headgear p | last run 127 days | form 11-230 | MARKET 19.1% | 09:00 median 4.65 | Matchbook 5.00
    comment: Modern Style won two starts in a row four and five runs back, then a second and a third followed, so he arrives with solid recent form despite an unplaced run last time out.
    DATA: model 24.4% | style Prominent (led 3% of runs) | runs in data 6 | last 3: 16 May Uttoxeter Hurdle 15.8f Good 2/8; 3 Jun Warwick Hurdle 19f Good 3/5; 18 Jul Market Rasen Hurdle 20.6f Good 11/12
    DATA for: Has won at this trip or further; Good recent finishing positions; Carries 6 lb less than average
    DATA against: Official rating 99, 6 lb below field average; Last-run finishing speed -5.5% vs that field (faded); Returns from a 127-day break
- The Bellhop (hrs_53211655) | 4yo G | 164lb | OR 111 | draw 0 | jockey Caoilin Quinn | trainer Jamie Moore & Josh Moore (14d 1/21) | headgear b (1st time) | last run 16 days | form 345-55 | MARKET 17.8% | 09:00 median 5.00 | Matchbook 5.40
    comment: The main risk is that he is yet to win in his last five starts, with a fifth three starts back, and his yard is out of form.
    DATA: model 18.6% | style Midfield (led 4% of runs) | runs in data 5 | last 3: 19 Apr Plumpton Hurdle 20.5f Good 5/5; 10 Oct Chepstow Hurdle 16.1f Good To Soft 5/12; 6 Nov Fontwell Hurdle 19f Good 5/8 fig 109
    DATA for: Best recent form figure 109, 10 lb above field average; Official rating 111, 6 lb above field average; Last-run finishing speed +2.2% vs that field (finished strongly); First-time headgear
    DATA against: Carries 6 lb more than average
- One Island (hrs_52525984) | 4yo G | 150lb | OR 97 | draw 0 | jockey Sam Twiston-Davies | trainer Paul Nicholls (14d 2/17) | headgear tb (1st time) | wind surgery | last run 20 days | form 632-55 | MARKET 15.3% | 09:00 median 6.00 | Matchbook 6.20
    comment: One Island is winless in his last five, finishing fifth in each of his last two runs, which makes him hard to fancy, though a second and a third earlier in that sequence show he can get involved. He has run over today's trip and is fresh enough after 20 days off, and 150 lb is not a big burden.
    DATA: model 12.7% | style Prominent (led 3% of runs) | runs in data 4 | last 3: 24 Apr Chepstow Hurdle 16.1f Good 2/12; 13 May Newton Abbot Hurdle 16.8f Good 5/5; 2 Nov Plumpton Hurdle 16f Good 5/6 fig 88
    DATA for: Carries 8 lb less than average; First-time headgear
    DATA against: Best recent form figure 88, 12 lb below field average; Recent figures 9 lb below its current mark (looks high in the weights); Official rating 97, 8 lb below field average; Last-run finishing speed -2.2% vs that field (faded)
- Out of Aces (hrs_47161989) | 4yo G | 160lb | OR 107 | draw 0 | jockey Miss Ella Herbison(7) | trainer Gordon Treacy (14d 0/3) | headgear - | last run 193 days | form 40-4 | MARKET 3.3% | 09:00 median 26.00 | Matchbook 32.00
    comment: Out of Aces is winless in his last three, with a fourth last time out, an unplaced run before that and a fourth three starts back, and a 193-day absence raises fitness doubts.
    DATA: model 18.7% | style Leader (led 38% of runs) | runs in data 2 | last 3: 17 Mar Down Royal Hurdle 17.5f Good To Yielding 12/19; 13 May Punchestown Hurdle 16f Good To Yielding 4/8
    DATA for: Pace: may get an uncontested lead
    DATA against: Returns from a 193-day break; Lightly raced: 2 runs in our data, so the model has little to go on

## 3:37 Exeter | race_id rac_32305136279 | Exminster Golf Centre Richard Candy Memorial Handicap Hurdle Race
Hurdle | Class 5 | 2m5f137y | going Good | Turf | 10 runners | rating band 0-105 | age 3yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Romany Brown (hrs_40786291) | 6yo G | 166lb | OR 103 | draw 0 | jockey Ciaran Gethings | trainer Ben Case (14d 1/6) | headgear t | last run 23 days | form F-4453 | MARKET 17.8% | 09:00 median 5.00 | Matchbook 5.20 | CHECK (skip line 4.75)
    comment: Romany Brown comes here in solid recent form, third last time out after a fifth and two fourths in his previous three starts, and he's fresh enough off 23 days.
    DATA: model 12.7% | style Midfield (led 3% of runs) | runs in data 4 | last 3: 26 Jul Uttoxeter Hurdle 15.8f Good 4/6; 23 Aug Worcester Hurdle 20f Good 5/8; 30 Oct Wetherby Hurdle 21.5f Good 3/11 fig 102
    DATA for: Best recent form figure 102, 7 lb above field average; Official rating 103, 11 lb above field average; Last-run finishing speed +4.1% vs that field (finished strongly)
    DATA against: Carries 10 lb more than average
- Locked Down Lad (hrs_40332523) | 6yo G | 144lb | OR 81 | draw 0 | jockey Callum Pritchard | trainer Joe Tickle (14d 0/6) | headgear - | last run 21 days | form 8P-643 | MARKET 17.2% | 09:00 median 5.00 | Matchbook 5.50
    comment: Locked Down Lad is winless in his last five, though a third last time out and a fourth two starts back show he's heading the right way, and he has run over today's trip.
    DATA: model 11.4% | style Midfield (led 4% of runs) | runs in data 8 | last 3: 1 Jul Worcester Hurdle 20f Good 6/11; 16 Jul Worcester Hurdle 20f Good 4/7; 1 Nov Worcester Hurdle 23f Good To Soft 3/9 fig 78
    DATA for: Last-run finishing speed +3.0% vs that field (finished strongly); Carries 12 lb less than average
    DATA against: Best recent form figure 78, 17 lb below field average; Official rating 81, 11 lb below field average; Pulled up in 1 of its last 5 jumps runs
- Can You Hear Me (hrs_49389200) | 5yo G | 168lb | OR 105 | draw 0 | jockey Jack Stenhouse(7) | trainer Philip Hobbs & Johnson White (14d 2/13) | headgear h | last run 23 days | form 2692-7 | MARKET 15.3% | 09:00 median 5.50 | Matchbook 6.20
    comment: The risk is a seventh last time out and top weight of 168 lb.
    DATA: model 12.5% | style Held up (led 5% of runs) | runs in data 3 | last 3: 25 Feb Wincanton Hurdle 19.8f Good To Soft 9/15; 26 Mar Chepstow Hurdle 19.5f Good To Soft 2/10; 30 Oct Uttoxeter Hurdle 20f Good 7/15 fig 104
    DATA for: Best recent form figure 104, 9 lb above field average; Official rating 105, 13 lb above field average; Last-run finishing speed +2.2% vs that field (finished strongly)
    DATA against: Carries 12 lb more than average; Pace: steady gallop likely, hard to come from off the pace
- What A Dragon (hrs_59678815) | 5yo G | 142lb | OR 78 | draw 0 | jockey Harry Kimber | trainer Robert Walford (14d 0/4) | headgear b (1st time) | wind surgery | last run 7 days | form P803-P | MARKET 12.3% | 09:00 median 7.00 | Matchbook 7.60
    comment: What A Dragon is hard to fancy, having been pulled up last time out just seven days ago and winless in his last five, with another pulled up five starts back. A third two starts back is the one bright spot, but 142 lb off a mark of 78 is a big ask.
    DATA: model 9.3% | style Held up (led 4% of runs) | runs in data 4 | last 3: 2 Feb Kempton Hurdle 21f Good To Soft 13/15; 23 Mar Wincanton Hurdle 19.8f Good 3/12; 15 Nov Fontwell Chase 21.5f Soft PU/9
    DATA for: Carries 14 lb less than average; First-time headgear
    DATA against: Official rating 78, 14 lb below field average; Pulled up in 1 of its last 4 jumps runs; Pace: steady gallop likely, hard to come from off the pace
- Bertie Wooster (hrs_27451879) | 8yo G | 168lb | OR 105 | draw 0 | jockey Freddie Gingell | trainer Joe Tizzard (14d 8/30) | headgear t | last run 36 days | form 2244-P | MARKET 8.9% | 09:00 median 9.50 | Matchbook 11.50
    comment: Bertie Wooster showed solid form before his latest outing, with a second and a fourth, another fourth and a second in his previous four runs, and he has run over today's trip and going, with a yard in form (8 from 30). The risk is the pulled-up effort last time out, plus 168 lb and a 36-day break.
    DATA: model 17.1% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 6 Mar Exeter Chase 19.2f Good To Soft 4/11; 17 Oct Newton Abbot Chase 26f Good PU/5
    DATA for: Official rating 105, 13 lb above field average; Trainer 27% wins (8/30), last 14 days
    DATA against: Carries 12 lb more than average; Lightly raced: 2 runs in our data, so the model has little to go on; Pulled up in 1 of its last 2 jumps runs; First run over hurdles in our data
- Blue In The West (hrs_33165216) | 9yo G | 157lb | OR 94 | draw 0 | jockey Shane Quinlan(3) | trainer Ben Lund (14d 0/0) | headgear - | last run 14 days | form P12-37 | MARKET 8.3% | 09:00 median 9.50 | Matchbook 12.50
    comment: He has run over today's trip and is fit enough after 14 days, but the form is trending the wrong way.
    DATA: model 11.4% | style Held up (led 3% of runs) | runs in data 7 | last 3: 17 Apr Exeter Hurdle 21.6f Good 2/5; 9 May Warwick Hurdle 25f Good 3/6; 8 Nov Ffos Las Hurdle 24f Soft 7/11
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Race comments mention jumping mistakes in 2 of its last 5 runs; Pulled up in 1 of its last 5 jumps runs; Pace: steady gallop likely, hard to come from off the pace
- Bashful Boy (hrs_19611291) | 10yo G | 146lb | OR 83 | draw 0 | jockey Jack Tudor | trainer David Pipe (14d 2/10) | headgear tv | last run 40 days | form 0-3854 | MARKET 8.2% | 09:00 median 9.50 | Matchbook 13.00
    comment: Bashful Boy was fourth last time out and has been winless in his last five, though a third four starts back shows he can get involved.
    DATA: model 10.9% | style Midfield (led 3% of runs) | runs in data 11 | last 3: 22 Jul Worcester Hurdle 20f Good 8/13; 7 Sep Newton Abbot Hurdle 26.5f Good 5/7; 13 Oct Southwell Hurdle 24.3f Good 4/6
    DATA for: Trainer 20% wins (2/10), last 14 days; Carries 10 lb less than average
    DATA against: Official rating 83, 9 lb below field average; Race comments mention jumping mistakes in 2 of its last 4 runs; Aged 10, older than most of this field
- Hillsin (hrs_27565944) | 8yo G | 154lb | OR 91 | draw 0 | jockey James Turner(5) | trainer Alan Jones (14d 0/0) | headgear - | last run 92 days | form 0P-P79 | MARKET 6.4% | 09:00 median 15.00 | Matchbook 14.50
    comment: The main risk is form that reads poorly, with a ninth last time, a seventh before that and two pulled-up efforts prior to that.
    DATA: model 6.8% | style Midfield (led 3% of runs) | runs in data 4 | last 3: 6 May Fontwell Hurdle 21.7f Good PU/9; 4 Jun Uttoxeter Hurdle 19.9f Good 7/7; 22 Aug Newton Abbot Hurdle 18.5f Good To Firm 9/10
    DATA against: Poor recent finishing positions; Returns from a 92-day break; Pulled up in 2 of its last 4 jumps runs
- Saint Invictus (hrs_49578025) | 5yo G | 168lb | OR 105 | draw 0 | jockey James Best | trainer Syd Hosie (14d 2/11) | headgear - | last run 18 days | form 57-076 | MARKET 4.1% | 09:00 median 19.00 | Matchbook 26.00
    comment: Saint Invictus is yet to win in his last five, finishing sixth last time out and seventh two starts back, though he returns after just 18 days so should be fit.
    DATA: model 2.4% | style Midfield (led 4% of runs) | runs in data 4 | last 3: 10 Oct Chepstow Hurdle 19.5f Good To Soft 12/13; 23 Oct Cheltenham Hurdle 20f Good To Soft 7/7; 4 Nov Chepstow Hurdle 19.5f Good To Soft 6/14 fig 97
    DATA for: Official rating 105, 13 lb above field average; Last-run finishing speed +3.1% vs that field (finished strongly)
    DATA against: Recent figures 8 lb below its current mark (looks high in the weights); Poor recent finishing positions; Carries 12 lb more than average
- Deauville Lady (hrs_48244560) | 5yo M | 142lb | OR 72 | draw 0 | jockey David Noonan | trainer Nigel Hawke (14d 1/7) | headgear - | last run 18 days | form 0760-9 | MARKET 1.5% | 09:00 median 51.00 | Matchbook 95.00
    comment: Deauville Lady is yet to win in her recent form, finishing ninth last time out after a sixth three starts back, and she returns just 18 days later off 142 lb. Lightly raced and unexposed, she could still have a bit of improvement in her.
    DATA: model 5.5% | style Held up (led 3% of runs) | runs in data 4 | last 3: 12 Feb Taunton Hurdle 16.5f Heavy 6/9; 1 Apr Sedgefield Hurdle 19.9f Good 10/11; 4 Nov Chepstow Hurdle 19.5f Good To Soft 9/16
    DATA for: Carries 14 lb less than average
    DATA against: Official rating 72, 20 lb below field average; Last-run finishing speed -4.0% vs that field (faded); Poor recent finishing positions; Pace: steady gallop likely, hard to come from off the pace
