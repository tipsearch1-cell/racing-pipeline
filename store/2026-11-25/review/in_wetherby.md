# Card review packet: Wetherby, 2026-11-25

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
{"meeting": "wetherby", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 12:16 Wetherby | race_id rac_32305535301 | Book Now For The BoyleSports Christmas Meeting Mares' Novices' Hurdle Race (Herring Queen Mares' Novices' Hurdle Series Qualifier) (GBB Race)
Hurdle | Class 4 | 2m | going Good | Turf | 8 runners | rating band - | age 4yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Mets Ta Ceinture (hrs_57757672) | 4yo F | 154lb | OR - | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 20/94) | headgear - | last run 259 days | form 1212- | MARKET 80.6% | 09:00 median 1.08 | Matchbook 1.12
    DATA: model 23.5% | style Unknown | runs in data 1 | last 3: 11 Mar Cheltenham NH Flat 16.4f Good 2/21
    DATA for: Trainer 21% wins (20/94), last 14 days; Last-run finishing speed +4.2% vs that field (finished strongly)
    DATA against: Returns from a 259-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Island Jetaway (hrs_62393905) | 4yo F | 154lb | OR - | draw 0 | jockey Gavin Sheehan | trainer Billy Aprahamian (14d 0/6) | headgear - | last run 194 days | form 1-2 | MARKET 7.0% | 09:00 median 9.00 | Matchbook 18.50
    DATA: model 19.3% | style Held up (led 8% of runs) | runs in data 1 | last 3: 15 May Aintree NH Flat 16.9f Good 2/14
    DATA for: Last-run finishing speed +5.3% vs that field (finished strongly)
    DATA against: Returns from a 194-day break; Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Marie d'Altalinara (hrs_64522934) | 4yo F | 154lb | OR - | draw 0 | jockey Callum Pritchard | trainer Ben Pauling (14d 6/36) | headgear t (1st time) | wind surgery | last run 198 days | form 8 | MARKET 3.5% | 09:00 median 13.00 | Matchbook 90.00
    DATA: model 15.5% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 11 May Southwell NH Flat 15.8f Good 8/10
    DATA for: First-time headgear
    DATA against: Last-run finishing speed -5.7% vs that field (faded); Returns from a 198-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Annie Mulligan (hrs_17393695578) | 5yo M | 154lb | OR - | draw 0 | jockey Jonathan England | trainer Sam England (14d 6/29) | headgear - | last run 227 days | form 322F1- | MARKET 2.8% | 09:00 median 19.00 | Matchbook 60.00
    DATA: model 10.8% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 21% wins (6/29), last 14 days
    DATA against: Returns from a 227-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Eroico (hrs_41379457) | 4yo F | 154lb | OR - | draw 0 | jockey Ryan Mania | trainer Martin Todhunter (14d 0/4) | headgear - | last run 16 days | form 6 | MARKET 2.2% | 09:00 median 26.00 | Matchbook 65.00
    DATA: model 10.0% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 24 Jun Carlisle Flat 11.2f Good To Firm 4/10; 1 Aug Hamilton Flat 13.1f Good 6/10; 9 Nov Carlisle Hurdle 17f Good To Soft 6/14 fig 98
- Atlantic Blue (hrs_61455723) | 5yo M | 154lb | OR - | draw 0 | jockey David Bass | trainer Henry Daly (14d 3/14) | headgear - | last run 254 days | form 74- | MARKET 2.0% | 09:00 median 29.00 | Matchbook 70.00
    DATA: model 7.2% | style Held up (led 8% of runs) | runs in data 2 | last 3: 7 Feb Warwick NH Flat 16f Heavy 7/8; 16 Mar Ffos Las NH Flat 15.8f Soft 4/5
    DATA for: Trainer 21% wins (3/14), last 14 days; Last-run finishing speed +5.2% vs that field (finished strongly)
    DATA against: Returns from a 254-day break; Lightly raced: 2 runs in our data, so the model has little to go on; First run over hurdles in our data; Pace: steady gallop likely, hard to come from off the pace
- Jota's Gold (hrs_61110917) | 5yo M | 154lb | OR - | draw 0 | jockey Jonjo O'Neill Jr. | trainer Jonjo & A.J. O'Neill (14d 5/35) | headgear - | last run 25 days | form 8-7 | MARKET 1.1% | 09:00 median 51.00 | Matchbook 160.00
    DATA: model 6.8% | style Held up (led 5% of runs) | runs in data 2 | last 3: 7 Feb Warwick NH Flat 16f Heavy 8/8; 31 Oct Ascot NH Flat 15.5f Good To Firm 7/9 fig 76
    DATA against: Last-run finishing speed -2.7% vs that field (faded); Lightly raced: 2 runs in our data, so the model has little to go on; First run over hurdles in our data; Pace: steady gallop likely, hard to come from off the pace
- Recobella (hrs_47191424) | 5yo M | 154lb | OR - | draw 0 | jockey Joe Williamson | trainer Philip Kirby (14d 1/12) | headgear - | last run 11 days | form 4 | MARKET 0.8% | 09:00 median 67.00 | Matchbook 180.00
    DATA: model 6.8% | style Prominent (led 8% of runs) | runs in data 10 | last 3: 5 Sep Newcastle Flat 12.4f Standard 5/6; 3 Oct Redcar Flat 10f Good 4/9; 14 Nov Wetherby Hurdle 16f Good 4/4
    DATA against: Last-run finishing speed -6.3% vs that field (faded)

## 12:46 Wetherby | race_id rac_32305537238 | wetherbyracing.co.uk Handicap Hurdle Race
Hurdle | Class 5 | 3m26y | going Good | Turf | 12 runners | rating band 0-100 | age 4yo+
DATA pace: Lone leader - Glory Hights is the only habitual front-runner and may be allowed an easy lead.
- I Heard A Rumour (hrs_60492404) | 5yo M | 166lb | OR 98 | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 20/94) | headgear - | last run 21 days | form U74-61 | MARKET 36.9% | 09:00 median 2.10 | Matchbook 2.56
    comment: Fresh from a win last time out 21 days ago, she has run on today's going, but a sixth and a fourth before that show inconsistency.
    DATA: model 20.7% | style Held up (led 4% of runs) | runs in data 5 | last 3: 17 Mar Wetherby Hurdle 19.7f Good To Soft 4/6; 7 Oct Worcester Hurdle 16f Good 6/10; 4 Nov Chepstow Hurdle 19.5f Good To Soft 1/16 fig 95
    DATA for: Best recent form figure 95, 11 lb above field average; Official rating 98, 10 lb above field average; Trainer 21% wins (20/94), last 14 days; Last-run finishing speed +8.7% vs that field (finished strongly)
    DATA against: Carries 10 lb more than average; Race comments mention jumping mistakes in 2 of its last 5 runs; Fell or unseated in 1 of its last 5 jumps runs
- Getaway Master (hrs_24373006) | 9yo G | 152lb | OR 84 | draw 0 | jockey Sean Bowen | trainer Micky Hammond & Becky Smith (14d 1/17) | headgear p (1st time) | last run 19 days | form 9-4708 | MARKET 13.2% | 09:00 median 6.00 | Matchbook 7.20
    comment: The risk is form figures of eighth last time out and a ninth five starts back, leaving him winless in his last five and carrying 152 lb.
    DATA: model 10.9% | style Held up (led 5% of runs) | runs in data 7 | last 3: 29 Aug Cartmel Hurdle 25.4f Good 7/12; 22 Oct Carlisle Hurdle 20f Good 10/13; 6 Nov Hexham Hurdle 23.5f Good 8/10 fig 80
    DATA for: First-time headgear
    DATA against: Best recent form figure 80, 4 lb below field average; Poor recent finishing positions
- Moveonbuy (hrs_38417176) | 6yo M | 149lb | OR 81 | draw 0 | jockey Oscar Palmer(7) | trainer Andrew Crook (14d 1/2) | headgear p | last run 23 days | form 5662-2 | MARKET 11.9% | 09:00 median 7.00 | Matchbook 7.60
    comment: Without a win in her last five, Moveonbuy is hard to fancy, though back-to-back seconds show she is in good heart and she has run over today's trip and going.
    DATA: model 9.1% | style Held up (led 4% of runs) | runs in data 6 | last 3: 4 Mar Catterick Hurdle 25.3f Good 6/8; 27 Mar Wetherby Hurdle 24.1f Good 2/15; 2 Nov Southwell Hurdle 24.5f Good 2/8 fig 78
    DATA for: Good recent finishing positions; Carries 7 lb less than average
    DATA against: Best recent form figure 78, 6 lb below field average; Official rating 81, 7 lb below field average
- Glory Hights (hrs_33479859) | 10yo G | 151lb | OR 83 | draw 0 | jockey Danny McMenamin | trainer Chris Grant (14d 1/5) | headgear p | last run 26 days | form 5246-5 | MARKET 11.2% | 09:00 median 7.00 | Matchbook 8.40
    comment: Glory Hights has been consistent without troubling the judge lately, finishing fifth last time out after a sixth and a fourth, though a second four starts back shows his ceiling.
    DATA: model 10.2% | style Leader (led 43% of runs) | runs in data 5 | last 3: 14 Mar Newcastle Hurdle 20.3f Good To Soft 4/15; 31 Mar Newcastle Hurdle 20.3f Good To Soft 6/9; 30 Oct Wetherby Hurdle 21.5f Good 5/11 fig 82
    DATA for: Trainer 20% wins (1/5), last 14 days; Last-run finishing speed +3.3% vs that field (finished strongly); Carries 5 lb less than average; Pace: may get an uncontested lead
    DATA against: Aged 10, older than most of this field
- Masterminding (hrs_25427598) | 7yo G | 152lb | OR 84 | draw 0 | jockey Leah Noreci(7) | trainer James Moffatt (14d 0/6) | headgear - | last run 19 days | form 232493 | MARKET 6.3% | 09:00 median 13.00 | Matchbook 15.00
    comment: Masterminding is winless in his last six, though a third last time out, 19 days ago, and a pair of seconds in that spell show he's competitive, and he has run over today's trip and going before.
    DATA: model 9.2% | style Midfield (led 5% of runs) | runs in data 6 | last 3: 29 Aug Cartmel Hurdle 25.4f Good 4/12; 23 Sep Perth Hurdle 23.9f Good 9/12; 6 Nov Hexham Hurdle 23.5f Good 3/10 fig 83
    DATA for: Last-run finishing speed +2.4% vs that field (finished strongly)
    DATA against: Race comments mention jumping mistakes in 2 of its last 5 runs
- Final Straw (hrs_53504248) | 6yo G | 165lb | OR 97 | draw 0 | jockey Callum Bewley | trainer Martin Todhunter (14d 0/4) | headgear p | last run 20 days | form 116-05 | MARKET 4.6% | 09:00 median 17.00 | Matchbook 21.00
    comment: Twice a winner in his last five starts, taking the last two of those wins four and five runs back, and he has run over today's trip and going before, while a 20-day break suits. Slipping to fifth last time and carrying 165 lb is the main risk.
    DATA: model 6.9% | style Midfield (led 8% of runs) | runs in data 2 | last 3: 22 Oct Carlisle Hurdle 20f Good 10/13; 5 Nov Newcastle Hurdle 20.5f Good 5/8 fig 89
    DATA for: Best recent form figure 89, 5 lb above field average; Official rating 97, 9 lb above field average
    DATA against: Recent figures 8 lb below its current mark (looks high in the weights); Carries 9 lb more than average; Lightly raced: 2 runs in our data, so the model has little to go on
- Smart Bucks (hrs_46850839) | 6yo G | 142lb | OR 69 | draw 0 | jockey Joe Williamson | trainer Philip Kirby (14d 1/12) | headgear p | last run 251 days | form 42674- | MARKET 3.7% | 09:00 median 21.00 | Matchbook 26.00
    DATA: model 5.3% | style Prominent (led 4% of runs) | runs in data 4 | last 3: 22 Jan Wetherby Hurdle 24.1f Soft 6/7; 24 Feb Catterick Hurdle 25.3f Good To Soft 7/9; 19 Mar Sedgefield Hurdle 27f Good 4/7
    DATA for: Carries 14 lb less than average
    DATA against: Official rating 69, 19 lb below field average; Returns from a 251-day break
- Mr Ramoon (hrs_49326025) | 6yo G | 168lb | OR 100 | draw 0 | jockey Conor Rabbitt(3) | trainer Susan Corbett (14d 1/8) | headgear - | last run 52 days | form 4/9-72 | MARKET 3.6% | 09:00 median 19.00 | Matchbook 29.00
    comment: Mr Ramoon steps up from a good second last time out, though he is yet to win in his last four starts, and the 52-day break is the one reservation.
    DATA: model 6.7% | style Prominent (led 5% of runs) | runs in data 3 | last 3: 15 Jan Newcastle Hurdle 20.3f Good To Soft 9/16; 13 Jun Hexham Hurdle 16.2f Good 7/9; 4 Oct Kelso Hurdle 20.9f Good To Firm 2/3
    DATA for: Official rating 100, 12 lb above field average
    DATA against: Carries 12 lb more than average
- Matoury (hrs_32278442) | 7yo G | 155lb | OR 87 | draw 0 | jockey Charlie Maggs | trainer Mike Sowersby (14d 0/5) | headgear t | last run 24 days | form 311777 | MARKET 2.8% | 09:00 median 30.00 | Matchbook 34.00
    comment: Matoury has finished seventh in each of his last three starts, so it's hard to fancy him after a 24-day break, even though he won twice before that, a winner four starts back and again five starts back.
    DATA: model 6.6% | style Midfield (led 4% of runs) | runs in data 7 | last 3: 20 Jul Cartmel Hurdle 22.1f Good 7/9; 26 Sep Market Rasen Hurdle 23.1f Good 7/10; 1 Nov Huntingdon Hurdle 25f Good 7/8 fig 83
    DATA against: Poor recent finishing positions
- It's Party Time (hrs_50433026) | 5yo G | 153lb | OR 85 | draw 0 | jockey Charlie Hammond | trainer Nick Kent (14d 0/2) | headgear p (1st time) | last run 234 days | form /PP4P- | MARKET 2.3% | 09:00 median 29.00 | Matchbook 50.00
    comment: It's Party Time has been pulled up in three of his last four starts, with a fourth two starts back his only completed effort, and he returns after 234 days off.
    DATA: model 3.7% | style Prominent (led 5% of runs) | runs in data 3 | last 3: 18 Feb Southwell Hurdle 20.4f Soft PU/13; 13 Mar Doncaster Hurdle 16.6f Good To Soft 4/4; 5 Apr Market Rasen Chase 17.2f Good PU/8
    DATA for: First-time headgear
    DATA against: Returns from a 234-day break; Pulled up in 2 of its last 3 jumps runs
- Jacenry (hrs_34652751) | 7yo G | 165lb | OR 97 | draw 0 | jockey Ben Harvey | trainer William Harvey (14d 0/0) | headgear - | last run 759 days | form 127FP/ | MARKET 2.0% | 09:00 median 34.00 | Matchbook 80.00
    comment: The big risk is a 759-day absence, with a pulled up last time out and a fall before that, under 165 lb.
    DATA: model 7.3% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Official rating 97, 9 lb above field average
    DATA against: Carries 9 lb more than average; Returns from a 759-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Rock Armour (hrs_40899635) | 5yo G | 154lb | OR 86 | draw 0 | jockey Joshua Thompson(5) | trainer David Thompson (14d 0/4) | headgear - | last run 22 days | form 53U3P | MARKET 1.4% | 09:00 median 41.00 | Matchbook 110.00
    comment: Rock Armour is hard to fancy, pulled up last time out and winless in his last five, with an unseated rider three starts back adding to the doubts. A third two starts back and experience on today's going offer some support, but 154 lb is a big ask.
    DATA: model 3.3% | style Held up (led 3% of runs) | runs in data 11 | last 3: 10 Oct Hexham Hurdle 16.2f Good UR/9; 18 Oct Sedgefield Hurdle 20f Good 3/3; 3 Nov Sedgefield Hurdle 20f Good PU/11
    DATA against: Fell or unseated in 1 of its last 5 jumps runs; Pulled up in 1 of its last 5 jumps runs

## 1:16 Wetherby | race_id rac_32305539175 | Join Racing TV Now Handicap Steeple Chase (Go North Red Rum Series Qualifier) (GBB Race)
Chase | Class 4 | 3m45y | going Good | Turf | 10 runners | rating band 0-110 | age 4yo+
DATA pace: Lone leader - Rockinastorm is the only habitual front-runner and may be allowed an easy lead.
- In The Age (hrs_39959682) | 6yo G | 168lb | OR 110 | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 20/94) | headgear p (1st time) | last run 24 days | form 124-55 | MARKET 21.1% | 09:00 median 4.00 | Matchbook 4.40 | CHECK (skip line 3.80)
    comment: The risk is a form line that has tailed off, with a fifth last time out and another fifth two starts back, while he carries 168 lb.
    DATA: model 9.4% | style Held up (led 3% of runs) | runs in data 5 | last 3: 21 Mar Bangor-on-Dee Hurdle 19.6f Good 4/7; 7 Oct Worcester Chase 20f Good 5/6; 1 Nov Worcester Chase 20f Good To Soft 5/15 fig 106
    DATA for: Trainer 21% wins (20/94), last 14 days; First-time headgear
- Slaney Opera (hrs_29816514) | 8yo G | 163lb | OR 105 | draw 0 | jockey James Murray(7) | trainer John Wainwright (14d 1/2) | headgear t | last run 11 days | form F23121 | MARKET 14.4% | 09:00 median 5.50 | Matchbook 7.00
    comment: Slaney Opera arrives in cracking nick, a winner last time out and again three starts back, with a second in between, and he has run over today's trip and going.
    DATA: model 11.4% | style Midfield (led 3% of runs) | runs in data 13 | last 3: 16 Oct Uttoxeter Chase 24f Good 1/8 fig 98; 31 Oct Wetherby Chase 24f Good 2/4 fig 99; 14 Nov Wetherby Chase 24f Good 1/4 fig 99
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Recent figures 6 lb below its current mark (looks high in the weights); Race comments mention jumping mistakes in 2 of its last 5 runs
- Jeteye (hrs_32780258) | 9yo G | 162lb | OR 104 | draw 0 | jockey Jonathan England | trainer Sam England (14d 6/29) | headgear tb | last run 5 days | form 215111 | MARKET 12.7% | 09:00 median 7.00 | Matchbook 7.20
    comment: That said, he has won his last three, four of his last six, and has run over today's trip and going before.
    DATA: model 9.4% | style Prominent (led 23% of runs) | runs in data 12 | last 3: 3 Nov Sedgefield Chase 26.5f Good 1/4 fig 99; 13 Nov Sedgefield Hurdle 27f Good 1/5 fig 100; 20 Nov Catterick Hurdle 25.5f Good 1/8 fig 101
    DATA for: Trainer 21% wins (6/29), last 14 days; Last-run finishing speed +3.2% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Race comments mention jumping mistakes in 2 of its last 5 runs
- Ski Lodge (hrs_35150325) | 7yo G | 170lb | OR 112 | draw 0 | jockey Jonathan Burke | trainer Alan King (14d 2/20) | headgear - | wind surgery | last run 207 days | form 2F44-5 | MARKET 12.1% | 09:00 median 7.00 | Matchbook 7.80
    comment: The risk is a 207-day absence under 170 lb.
    DATA: model 13.4% | style Midfield (led 3% of runs) | runs in data 4 | last 3: 26 Feb Wetherby Chase 24.2f Soft 4/6; 4 Apr Haydock Chase 25.6f Good 4/11; 2 May Uttoxeter Chase 20.9f Good 5/8
    DATA for: Official rating 112, 5 lb above field average
    DATA against: Last-run finishing speed -2.7% vs that field (faded); Carries 5 lb more than average; Returns from a 207-day break; Fell or unseated in 1 of its last 4 jumps runs
- Dearkeithandkaty (hrs_48247612) | 5yo G | 169lb | OR 111 | draw 0 | jockey Jonjo O'Neill Jr. | trainer Jonjo & A.J. O'Neill (14d 5/35) | headgear - | last run 34 days | form 222-P1 | MARKET 12.0% | 09:00 median 7.00 | Matchbook 8.00
    comment: Dearkeithandkaty won last time out, 34 days ago, and has run over today's trip and going, but a pulled up two starts back and 169 lb on his back temper enthusiasm.
    DATA: model 16.1% | style Prominent (led 5% of runs) | runs in data 6 | last 3: 14 Apr Newton Abbot Hurdle 26.5f Good 2/6; 22 May Worcester Hurdle 23f Good PU/11; 22 Oct Carlisle Chase 20f Good 1/4 fig 107
    DATA for: Best recent form figure 107, 4 lb above field average; Has won at this trip or further
    DATA against: Pulled up in 1 of its last 5 jumps runs
- Rockinastorm (hrs_27251532) | 9yo G | 169lb | OR 111 | draw 0 | jockey David Bass | trainer Henry Daly (14d 3/14) | headgear - | last run 272 days | form /F573- | MARKET 8.1% | 09:00 median 10.00 | Matchbook 12.50
    comment: The risk is a 272-day absence, plus 169 lb on his back, and he is yet to win in his last four starts.
    DATA: model 9.4% | style Leader (led 38% of runs) | runs in data 2 | last 3: 18 Jan Windsor Chase 28.7f Soft 7/16; 26 Feb Ludlow Chase 23.8f Good To Soft 3/7
    DATA for: Trainer 21% wins (3/14), last 14 days; Pace: may get an uncontested lead
    DATA against: Returns from a 272-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- Redeeming Love (hrs_40786452) | 6yo M | 154lb | OR 96 | draw 0 | jockey Jamie Hamilton | trainer Mark Walford (14d 2/7) | headgear t | last run 16 days | form 6733-6 | MARKET 7.5% | 09:00 median 11.00 | Matchbook 13.50
    comment: Redeeming Love is winless in her last five, though two thirds, two and three starts back, show she can reach the frame; a sixth last time out and a fresh 16 days off are fair, and she has run over this trip and going.
    DATA: model 7.3% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 24 Mar Southwell Hurdle 24.3f Good 3/7; 13 Apr Hexham Chase 24.2f Good 3/14; 9 Nov Carlisle Chase 20f Good 6/7 fig 92
    DATA for: Trainer 29% wins (2/7), last 14 days; Good recent finishing positions; Carries 11 lb less than average
    DATA against: Best recent form figure 92, 10 lb below field average; Official rating 96, 11 lb below field average
- One More Stroke (hrs_34073277) | 7yo G | 168lb | OR 110 | draw 0 | jockey Callum Bewley | trainer Daragh Bourke (14d 0/0) | headgear t | wind surgery | last run 25 days | form 3/45-5 | MARKET 5.5% | 09:00 median 13.00 | Matchbook 20.00
    comment: He is yet to win in that spell, and 168 lb is a hefty burden.
    DATA: model 6.0% | style Held up (led 8% of runs) | runs in data 1 | last 3: 31 Oct Ayr Chase 20.5f Good To Soft 5/10 fig 110
    DATA for: Best recent form figure 110, 8 lb above field average
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Daly Boy (hrs_47837118) | 6yo G | 160lb | OR 102 | draw 0 | jockey Jack Tudor | trainer Oliver Greenall & Josh Guerriero (14d 2/13) | headgear t | wind surgery | last run 29 days | form 5P55-0 | MARKET 4.2% | 09:00 median 19.00 | Matchbook 26.00
    comment: Winless in his last five, Daly Boy was unplaced last time out and has managed a fifth two starts back, and another fifth three starts back.
    DATA: model 7.5% | style Midfield (led 23% of runs) | runs in data 5 | last 3: 5 Mar Haydock Hurdle 24.3f Good To Soft 5/9; 31 Mar Bangor-on-Dee Hurdle 23.1f Good 5/8; 27 Oct Bangor-on-Dee Chase 24f Good To Soft 10/13
    DATA for: Carries 5 lb less than average
    DATA against: Official rating 102, 5 lb below field average; Last-run finishing speed -6.0% vs that field (faded); Pulled up in 1 of its last 5 jumps runs
- Trac (hrs_23380147) | 9yo G | 167lb | OR 109 | draw 0 | jockey Sean Bowen | trainer Micky Hammond & Becky Smith (14d 1/17) | headgear p | last run 248 days | form 25116- | MARKET 2.5% | 09:00 median 29.00 | Matchbook 48.00
    comment: Trac won two starts back and again three starts back, but he was only sixth last time out and returns after 248 days off, so fitness is the question.
    DATA: model 10.0% | style Prominent (led 38% of runs) | runs in data 2 | last 3: 16 Feb Carlisle Chase 20f Good To Soft 1/8; 22 Mar Carlisle Chase 20f Good To Soft 6/13
    DATA against: Returns from a 248-day break; Lightly raced: 2 runs in our data, so the model has little to go on

## 1:46 Wetherby | race_id rac_32305839410 | Visit racingtv.com Handicap Hurdle Race (Go North Cab On Target Series Qualifier) (Div I)
Hurdle | Class 4 | 2m3f154y | going Good | Turf | 10 runners | rating band 0-115 | age 3yo+
DATA pace: Lone leader - Kefir d'Oudairies is the only habitual front-runner and may be allowed an easy lead.
- Kefir d'Oudairies (hrs_41442009) | 6yo G | 163lb | OR 110 | draw 0 | jockey Sean Bowen | trainer Olly Murphy (14d 8/51) | headgear t | wind surgery | last run 14 days | form 5244-1 | MARKET 32.9% | 09:00 median 2.62 | Matchbook 2.84
    comment: Kefir d'Oudairies arrives fresh from a win last time out just 14 days ago, with a fourth and another fourth before that, and he has run over today's trip and going before. The risk is the hefty 163 lb he must carry.
    DATA: model 29.2% | style Leader (led 57% of runs) | runs in data 2 | last 3: 28 Feb Doncaster Hurdle 19.4f Soft 4/8; 11 Nov Warwick Hurdle 21f Good 1/3 fig 114
    DATA for: Best recent form figure 114, 8 lb above field average; Recent figures 4 lb above its current mark (looks well handicapped); Has won at this trip or further; Pace: may get an uncontested lead
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- El Gavilan (hrs_47773922) | 5yo G | 164lb | OR 111 | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 20/94) | headgear p | last run 34 days | form 115P-5 | MARKET 25.3% | 09:00 median 3.25 | Matchbook 3.85
    comment: El Gavilan won twice four and five starts back and was fifth last time out, but he was pulled up two starts back and has had 34 days off since. He has run over today's trip and going, though 164 lb is a big burden for a midfield type.
    DATA: model 12.6% | style Prominent (led 23% of runs) | runs in data 7 | last 3: 16 Mar Ffos Las Hurdle 20f Soft 5/8; 12 Apr Ffos Las Hurdle 20f Good To Soft PU/10; 22 Oct Ffos Las Hurdle 24f Soft 5/8 fig 104
    DATA for: Official rating 111, 5 lb above field average; Trainer 21% wins (20/94), last 14 days; Has won at this trip or further
    DATA against: Recent figures 7 lb below its current mark (looks high in the weights); Carries 5 lb more than average; Race comments mention jumping mistakes in 2 of its last 5 runs; Pulled up in 1 of its last 5 jumps runs
- Diamond Koda (hrs_35388983) | 7yo G | 160lb | OR 107 | draw 0 | jockey Tom Broughton(3) | trainer Nick Kent (14d 0/2) | headgear p | last run 26 days | form 5153-9 | MARKET 11.3% | 09:00 median 7.50 | Matchbook 8.60
    comment: The risk is a ninth last time out, and he carries 160 lb off an official mark of 107.
    DATA: model 13.2% | style Prominent (led 5% of runs) | runs in data 4 | last 3: 21 Mar Newbury Hurdle 18.8f Good To Soft 5/9; 11 Apr Newcastle Hurdle 20.3f Good 3/6; 30 Oct Uttoxeter Hurdle 20f Good 9/15 fig 98
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 98, 8 lb below field average; Recent figures 9 lb below its current mark (looks high in the weights)
- Bertie's Ballet (hrs_28903588) | 8yo G | 166lb | OR 113 | draw 0 | jockey Peter Kavanagh | trainer Dianne Sayer (14d 0/2) | headgear - | last run 34 days | form 7408-4 | MARKET 9.8% | 09:00 median 9.00 | Matchbook 9.60
    comment: Bertie's Ballet is yet to win in his last five, but he was fourth last time out 34 days ago and has run over today's trip and going before.
    DATA: model 12.0% | style Prominent (led 29% of runs) | runs in data 5 | last 3: 28 Feb Kelso Hurdle 16.2f Good To Soft 12/17; 17 Apr Ayr Hurdle 16f Soft 8/15; 22 Oct Carlisle Hurdle 17f Good 4/7 fig 109
    DATA for: Official rating 113, 7 lb above field average
    DATA against: Carries 7 lb more than average
- Dontelimurnamepike (hrs_59116785) | 4yo G | 156lb | OR 104 | draw 0 | jockey Danny McMenamin | trainer Ruth Jefferson (14d 0/0) | headgear - | last run 37 days | form R554- | MARKET 5.7% | 09:00 median 15.00 | Matchbook 17.50
    comment: Winless in his last four, Dontelimurnamepike was a fourth last time out, a fifth two starts back and another fifth three starts back, with a refusal before that, so he is hard to fancy off 156 lb.
    DATA: model 3.2% | style Held up (led 5% of runs) | runs in data 4 | last 3: 14 Apr Market Rasen Hurdle 20.6f Good 4/6; 8 Oct Southwell Flat 11.1f Standard 4/7; 19 Oct Southwell (AW) Flat 11f Standard 4/5 fig 60
- Old Gregorian (hrs_33344829) | 7yo G | 170lb | OR 117 | draw 0 | jockey Derek Fox | trainer Lucinda Russell & Michael Scudamore (14d 1/19) | headgear t | last run 34 days | form 146-54 | MARKET 5.1% | 09:00 median 17.00 | Matchbook 18.50
    DATA: model 7.3% | style Held up (led 3% of runs) | runs in data 4 | last 3: 20 Apr Kelso Chase 21.6f Good 6/8; 25 May Cartmel Chase 21.2f Good 5/5; 22 Oct Carlisle Chase 20f Good 4/4 fig 106
    DATA for: Official rating 117, 11 lb above field average
    DATA against: Recent figures 11 lb below its current mark (looks high in the weights); Carries 11 lb more than average; First run over hurdles in our data
- Kaikoura (hrs_38884776) | 6yo G | 145lb | OR 92 | draw 0 | jockey Nathan Moscrop | trainer Susan Corbett (14d 1/8) | headgear ht | last run 22 days | form 75-469 | MARKET 5.1% | 09:00 median 17.00 | Matchbook 19.00
    comment: Kaikoura is winless in his last five, finishing ninth last time out and no better than a fourth three starts back, so he is hard to fancy carrying 145 lb off an official mark of 92.
    DATA: model 5.8% | style Held up (led 4% of runs) | runs in data 3 | last 3: 5 Jul Market Rasen Hurdle 16.6f Good 4/7; 2 Oct Hexham Hurdle 16.2f Good 6/7; 3 Nov Sedgefield Hurdle 17f Good 9/11
    DATA for: Carries 14 lb less than average
    DATA against: Official rating 92, 14 lb below field average; Last-run finishing speed -4.8% vs that field (faded); Race comments mention jumping mistakes in 2 of its last 3 runs
- Norah's Legacy (hrs_37987880) | 6yo G | 149lb | OR 96 | draw 0 | jockey Joe Williamson | trainer Philip Kirby (14d 1/12) | headgear - | last run 650 days | form 55246/ | MARKET 2.2% | 09:00 median 26.00 | Matchbook 70.00
    comment: Winless in his last five and back after 650 days off, Norah's Legacy is hard to fancy, having been sixth last time out and fourth two starts back. In his favour, he has run over today's trip and going, and a second three starts back shows some ability off 149 lb.
    DATA: model 6.1% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Carries 10 lb less than average
    DATA against: Official rating 96, 10 lb below field average; Returns from a 650-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Kel Raffles (hrs_45315032) | 6yo G | 157lb | OR 104 | draw 0 | jockey Alice Stevens(3) | trainer Samantha & Jacqueline Coward (14d 0/0) | headgear - | last run 380 days | form 54/4P- | MARKET 1.3% | 09:00 median 41.00 | Matchbook 170.00
    comment: Kel Raffles was pulled up last time out and has been off for 380 days since, though he had finished a fourth two starts back, a fourth three starts back and a fifth before that. He has run over today's trip and going, but a weight of 157 lb and that long absence hold him back.
    DATA: model 6.9% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 380-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Fine Thing (hrs_51831717) | 5yo M | 158lb | OR 105 | draw 0 | jockey Jonathan England | trainer Sam England (14d 6/29) | headgear - | last run 11 days | form 114306 | MARKET 1.2% | 09:00 median 51.00 | Matchbook 110.00
    comment: Fine Thing won five and six starts back but has since drifted, a third three starts back giving way to an unplaced run and a sixth last time out, though she's fresh enough after 11 days and has run over today's trip and going.
    DATA: model 3.6% | style Midfield (led 29% of runs) | runs in data 7 | last 3: 4 Oct Kelso Hurdle 20.9f Good To Firm 3/3; 30 Oct Uttoxeter Hurdle 20f Good 14/15; 14 Nov Wetherby Hurdle 21.5f Good 6/6
    DATA for: Trainer 21% wins (6/29), last 14 days; Has won at this trip or further
    DATA against: Last-run finishing speed -9.2% vs that field (faded)

## 2:16 Wetherby | race_id rac_32305541112 | Visit racingtv.com Handicap Hurdle Race (Go North Cab On Target Series Qualifier) (Div II)
Hurdle | Class 4 | 2m3f154y | going Good | Turf | 9 runners | rating band 0-115 | age 3yo+
DATA pace: Lone leader - Punxsutawney Phil is the only habitual front-runner and may be allowed an easy lead.
- Theatre Tom (hrs_40786361) | 7yo G | 157lb | OR 104 | draw 0 | jockey Sean Bowen | trainer Olly Murphy (14d 8/51) | headgear - | last run 24 days | form 57/4F2 | MARKET 23.6% | 09:00 median 3.50 | Matchbook 4.20 | CHECK (skip line 3.32)
    DATA: model 19.9% | style Midfield (led 8% of runs) | runs in data 3 | last 3: 6 Jun Worcester Hurdle 20f Good 4/6; 4 Sep Worcester Hurdle 20f Good F/8; 1 Nov Worcester Hurdle 23f Good To Soft 2/9 fig 102
    DATA for: Last-run finishing speed +4.6% vs that field (finished strongly)
    DATA against: Fell or unseated in 1 of its last 3 jumps runs
- Gentleman Bill (hrs_38305561) | 8yo G | 170lb | OR 117 | draw 0 | jockey Jack Tudor | trainer Oliver Greenall & Josh Guerriero (14d 2/13) | headgear p | last run 26 days | form F854-2 | MARKET 17.8% | 09:00 median 5.00 | Matchbook 5.20
    comment: Gentleman Bill comes here in rising form, second last time out and a fourth two starts back, and he has run over today's trip and going before after a 26-day break.
    DATA: model 14.9% | style Prominent (led 3% of runs) | runs in data 5 | last 3: 21 Mar Bangor-on-Dee Hurdle 23.1f Good 5/6; 23 Apr Perth Hurdle 20.2f Good 4/9; 30 Oct Uttoxeter Hurdle 20f Good 2/15 fig 118
    DATA for: Best recent form figure 118, 16 lb above field average; Official rating 117, 11 lb above field average; Last-run finishing speed +4.3% vs that field (finished strongly)
    DATA against: Carries 11 lb more than average; Fell or unseated in 1 of its last 5 jumps runs
- Hay Max (hrs_51186863) | 5yo G | 161lb | OR 108 | draw 0 | jockey Gavin Sheehan | trainer Charlie Longsdon (14d 2/17) | headgear - | last run 38 days | form 3537-1 | MARKET 15.1% | 09:00 median 5.50 | Matchbook 6.60
    comment: Hay Max won last time out and has run over today's trip and going, but a seventh two starts back sits in mixed recent form, and 161 lb is a hefty burden after 38 days off.
    DATA: model 11.7% | style Midfield (led 4% of runs) | runs in data 4 | last 3: 1 Apr Sedgefield Hurdle 19.9f Good 3/6; 23 Apr Warwick Hurdle 19f Good 7/10; 18 Oct Sedgefield Hurdle 17f Good 1/8 fig 102
    DATA for: Last-run finishing speed +3.5% vs that field (finished strongly); Good recent finishing positions
    DATA against: Recent figures 6 lb below its current mark (looks high in the weights)
- Mandarb (hrs_38338895) | 5yo G | 163lb | OR 110 | draw 0 | jockey Alice Stevens(3) | trainer Micky Hammond & Becky Smith (14d 1/17) | headgear h | last run 243 days | form 5/712- | MARKET 13.1% | 09:00 median 6.50 | Matchbook 7.40
    comment: Mandarb was second last time out, and a winner two starts back, so the recent form reads well, and he has run over today's trip and going before.
    DATA: model 13.5% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 27 Mar Wetherby Hurdle 21.3f Good 2/16
    DATA for: Last-run finishing speed +7.3% vs that field (finished strongly)
    DATA against: Returns from a 243-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Azahara Palace (hrs_35107583) | 6yo M | 165lb | OR 112 | draw 0 | jockey Oakley Brown(5) | trainer Adrian Keatley (14d 1/7) | headgear t | last run 69 days | form 1527U- | MARKET 10.0% | 09:00 median 8.00 | Matchbook 10.00
    comment: The risk is a 69-day absence after unseating last time out, with 165 lb to carry.
    DATA: model 8.0% | style Held up (led 3% of runs) | runs in data 5 | last 3: 18 Apr Ayr Hurdle 24.3f Heavy UR/9; 17 May Hamilton Flat 9.2f Good 6/8; 17 Sep Ayr Flat 13.1f Soft 9/11
    DATA for: Official rating 112, 6 lb above field average
    DATA against: Poor recent finishing positions; Carries 6 lb more than average; Fell or unseated in 1 of its last 3 jumps runs
- La Lolita (hrs_53743389) | 5yo M | 144lb | OR 91 | draw 0 | jockey Jonathan England | trainer Sam England (14d 6/29) | headgear t | last run 18 days | form -54595 | MARKET 7.6% | 09:00 median 12.00 | Matchbook 12.50
    comment: La Lolita is winless in her last five, finishing fifth last time out, a ninth two starts back and nowhere better than a fourth four starts back, which makes her hard to fancy off 144 lb.
    DATA: model 9.8% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 4 Sep Bangor-on-Dee Hurdle 19.6f Good 5/11; 22 Oct Carlisle Hurdle 20f Good 9/13 fig 78; 7 Nov Uttoxeter Hurdle 20f Good 5/9 fig 87
    DATA for: Trainer 21% wins (6/29), last 14 days; Carries 15 lb less than average
    DATA against: Best recent form figure 87, 14 lb below field average; Official rating 91, 15 lb below field average
- Punxsutawney Phil (hrs_23706921) | 9yo G | 160lb | OR 107 | draw 0 | jockey Jamie Hamilton | trainer Mark Walford (14d 2/7) | headgear p | last run 19 days | form 42/P75 | MARKET 6.7% | 09:00 median 12.00 | Matchbook 15.50
    comment: The risk is a winless recent run, including a fifth last time, under a hefty 160 lb.
    DATA: model 8.3% | style Leader (led 23% of runs) | runs in data 5 | last 3: 10 Oct Chepstow Hurdle 23.6f Good To Soft PU/17; 24 Oct Kelso Hurdle 22.5f Good 7/9 fig 106; 6 Nov Hexham Hurdle 20f Good 5/9 fig 107
    DATA for: Best recent form figure 107, 6 lb above field average; Trainer 29% wins (2/7), last 14 days; Pace: may get an uncontested lead
    DATA against: Pulled up in 1 of its last 3 jumps runs; Aged 9, older than most of this field
- Time In A Bottle (hrs_40225311) | 6yo M | 157lb | OR 104 | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 20/94) | headgear ht | last run 13 days | form 26F-66 | MARKET 3.9% | 09:00 median 21.00 | Matchbook 26.00
    comment: Winless in her last five, Time In A Bottle has finished sixth in her last two outings and fell three starts back, so she is hard to fancy under 157 lb. On the plus side, she has run over today's trip and going, is fresh from a run 13 days ago, and was second five starts back.
    DATA: model 11.5% | style Held up (led 8% of runs) | runs in data 2 | last 3: 15 Sep Uttoxeter Hurdle 19.9f Good 6/9; 12 Nov Market Rasen Hurdle 16.5f Good To Soft 6/7
    DATA for: Trainer 21% wins (20/94), last 14 days
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Dramatic License (hrs_40553499) | 6yo G | 150lb | OR 97 | draw 0 | jockey Callum Bewley | trainer John Wainwright (14d 1/2) | headgear - | last run 26 days | form 50P-P7 | MARKET 2.3% | 09:00 median 41.00 | Matchbook 40.00
    DATA: model 2.5% | style Held up (led 3% of runs) | runs in data 4 | last 3: 31 Mar Newcastle Hurdle 22f Good To Soft PU/8; 8 May Market Rasen Hurdle 23.1f Good PU/8; 30 Oct Wetherby Hurdle 21.5f Good 7/11 fig 93
    DATA for: Carries 9 lb less than average
    DATA against: Best recent form figure 93, 8 lb below field average; Official rating 97, 9 lb below field average; Poor recent finishing positions; Pulled up in 2 of its last 4 jumps runs

## 2:46 Wetherby | race_id rac_32305543049 | Watch Racing TV In HD Novices' Handicap Steeple Chase (Go North Forgive 'N Forget Series Qualifier) (GBB Race)
Chase | Class 4 | 1m7f36y | going Good | Turf | 8 runners | rating band 0-120 | age 4yo+
DATA pace: Even - Two likely leaders (Smart Decision, Halftheworldaway). A fair, even gallop is most likely.
- Albie Littlewood (hrs_37520980) | 7yo G | 168lb | OR 120 | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 20/94) | headgear - | last run 35 days | form 6511-1 | MARKET 33.6% | 09:00 median 2.63 | Matchbook 2.80
    comment: Albie Littlewood arrives on a hat-trick of wins, having won last time out, two starts back and three starts back, so the form is hard to knock.
    DATA: model 21.5% | style Held up (led 5% of runs) | runs in data 2 | last 3: 22 Jan Huntingdon Hurdle 20.7f Soft 1/15; 21 Oct Worcester Chase 16.5f Good To Soft 1/9 fig 112
    DATA for: Official rating 120, 5 lb above field average; Trainer 21% wins (20/94), last 14 days; Last-run finishing speed +4.9% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Recent figures 8 lb below its current mark (looks high in the weights); Carries 5 lb more than average; Lightly raced: 2 runs in our data, so the model has little to go on
- Gaelic Rover (hrs_49578116) | 5yo G | 165lb | OR 117 | draw 0 | jockey Ryan Mania | trainer Ruth Jefferson (14d 0/0) | headgear - | last run 249 days | form 321F3- | MARKET 15.4% | 09:00 median 5.50 | Matchbook 6.40
    comment: The main risk is a 249-day absence, with 165 lb to carry.
    DATA: model 10.8% | style Prominent (led 8% of runs) | runs in data 3 | last 3: 15 Jan Newcastle Hurdle 16.9f Good To Soft 1/12; 28 Feb Kelso Hurdle 18.1f Good To Soft F/10; 21 Mar Kelso Hurdle 20.9f Good To Soft 3/7
    DATA for: Last-run finishing speed +3.5% vs that field (finished strongly); Has won at this trip or further
    DATA against: Returns from a 249-day break; Fell or unseated in 1 of its last 3 jumps runs; First run over fences in our data
- Smart Decision (hrs_46602913) | 5yo G | 166lb | OR 118 | draw 0 | jockey Jamie Hamilton | trainer Tim Easterby (14d 2/12) | headgear - | last run 11 days | form 4755-2 | MARKET 13.4% | 09:00 median 6.50 | Matchbook 7.20
    comment: Yet to win in his last five, though, and 166 lb is the main risk.
    DATA: model 8.7% | style Leader (led 29% of runs) | runs in data 6 | last 3: 25 Mar Hexham Hurdle 16.2f Soft 5/9; 4 Apr Haydock Hurdle 15.7f Good 5/11; 14 Nov Wetherby Chase 15f Good 2/4 fig 115
    DATA for: Best recent form figure 115, 6 lb above field average
    DATA against: Race comments mention jumping mistakes in 2 of its last 5 runs
- Anariza (hrs_40332565) | 6yo M | 155lb | OR 107 | draw 0 | jockey Robert Dunne | trainer Tom Ellis (14d 1/13) | headgear - | last run 22 days | form 3593-6 | MARKET 9.2% | 09:00 median 9.50 | Matchbook 10.50
    comment: Anariza returns 22 days after a sixth last time out, with a third two starts back and another five starts back, yet she's winless in her last five and has run over today's trip and going before.
    DATA: model 8.0% | style Held up (led 3% of runs) | runs in data 5 | last 3: 21 Mar Kelso Hurdle 16.2f Good To Soft 9/15; 19 Apr Stratford Hurdle 16.3f Good 3/10; 3 Nov Lingfield Chase 16f Good 6/8 fig 104
    DATA for: Carries 8 lb less than average
    DATA against: Best recent form figure 104, 5 lb below field average; Official rating 107, 8 lb below field average
- Caballo de Guerra (hrs_46850895) | 5yo G | 164lb | OR 116 | draw 0 | jockey Derek Fox | trainer Lucinda Russell & Michael Scudamore (14d 1/19) | headgear - | last run 34 days | form 456-23 | MARKET 7.7% | 09:00 median 12.00 | Matchbook 12.00
    comment: Placed in his last two, a third last time out and a second two starts back, Caballo de Guerra has run over today's trip and going before, and a 34-day break should leave him fresh.
    DATA: model 13.2% | style Midfield (led 4% of runs) | runs in data 5 | last 3: 17 Apr Ayr Hurdle 16f Soft 6/15; 23 Sep Perth Hurdle 16.2f Good 2/10; 22 Oct Carlisle Hurdle 17f Good 3/7 fig 112
    DATA for: Good recent finishing positions
    DATA against: First run over fences in our data
- Ninna Collina (hrs_47161331) | 5yo M | 169lb | OR 121 | draw 0 | jockey Sean Quinlan | trainer Jedd O'Keeffe (14d 0/3) | headgear - | last run 332 days | form 3/111- | MARKET 7.6% | 09:00 median 12.00 | Matchbook 12.50
    comment: Ninna Collina arrives on a hat-trick of wins, having also taken the race three starts back after a third four runs ago, and she has run over today's trip and going before. The single main risk is a 332-day absence, with 169 lb to carry.
    DATA: model 11.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Official rating 121, 6 lb above field average
    DATA against: Carries 6 lb more than average; Returns from a 332-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Kazar Forez (hrs_40166056) | 6yo G | 156lb | OR 108 | draw 0 | jockey Sean Bowen | trainer Micky Hammond & Becky Smith (14d 1/17) | headgear - | last run 264 days | form /1113- | MARKET 7.0% | 09:00 median 11.00 | Matchbook 15.50
    comment: He has run over today's trip, which is some comfort.
    DATA: model 12.8% | style Midfield (led 8% of runs) | runs in data 3 | last 3: 25 Jan Sedgefield Hurdle 16.8f Good To Soft 1/7; 30 Jan Catterick Hurdle 15.7f Soft 1/5; 6 Mar Ayr Hurdle 20.5f Soft 3/10
    DATA for: Has won at this trip or further; Good recent finishing positions; Carries 7 lb less than average
    DATA against: Official rating 108, 7 lb below field average; Returns from a 264-day break; First run over fences in our data
- Halftheworldaway (hrs_51558171) | 5yo M | 160lb | OR 112 | draw 0 | jockey Jack Tudor | trainer Oliver Greenall & Josh Guerriero (14d 2/13) | headgear - | last run 25 days | form 3211-8 | MARKET 6.1% | 09:00 median 13.00 | Matchbook 18.00
    comment: Halftheworldaway won two starts back and three starts back, but she was only eighth last time out, and she returns after 25 days carrying 160 lb.
    DATA: model 13.5% | style Prominent (led 43% of runs) | runs in data 4 | last 3: 25 Feb Bangor-on-Dee Hurdle 16.7f Soft 1/10; 31 Mar Bangor-on-Dee Hurdle 16.7f Good 1/7; 31 Oct Ayr Chase 20.5f Good To Soft 8/10 fig 101
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Best recent form figure 101, 8 lb below field average; Recent figures 11 lb below its current mark (looks high in the weights)

## 3:16 Wetherby | race_id rac_32305544986 | Watch Race Replays At racingtv.com Mares' National Hunt Flat Race (Conditional & Amateur Jockeys' Race) (Category 1 Elimination) (GBB Race)
NH Flat | Class 5 | 2m | going Good | Turf | 9 runners | rating band - | age 4-5yo
DATA pace: Unclear - Running styles known for only 4 of 9 runners.
- Northern Singer (hrs_17393582934) | 5yo M | 163lb | OR - | draw 0 | jockey Harry Atkins(5) | trainer Dan Skelton (14d 20/94) | headgear h | last run 46 days | form P1-1 | MARKET 57.2% | 09:00 median 1.53 | Matchbook 1.59
    comment: Northern Singer arrives an in-form mare, a winner last time out and again two starts back, and she has run over today's trip before.
    DATA: model 46.5% | style Unknown | runs in data 1 | last 3: 10 Oct Chepstow NH Flat 16.1f Good To Soft 1/8
    DATA for: Trainer 21% wins (20/94), last 14 days; Last-run finishing speed +8.2% vs that field (finished strongly); Has won at this trip or further
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Kirsty's Legacy (hrs_17395980791) | 4yo F | 156lb | OR - | draw 0 | jockey Fern O'Brien(5) | trainer Fergal O'Brien (14d 4/29) | headgear - | last run - days | form - | MARKET 10.2% | 09:00 median 8.00 | Matchbook 9.60
    comment: Kirsty's Legacy is unexposed, with no recorded form to go on, so this debut is a pure step into the unknown for the filly. She carries 156 lb, and there should be plenty of scope for improvement as she learns her trade.
    DATA: model 7.3% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Go Jackie (hrs_17395979748) | 4yo F | 156lb | OR - | draw 0 | jockey Nathan Andrews(10) | trainer Nick Scholfield (14d 1/12) | headgear - | last run - days | form - | MARKET 9.0% | 09:00 median 8.00 | Matchbook 12.50
    comment: Go Jackie is an unraced filly with no form to assess, so she is a completely unexposed sort who may well have improvement in her. She carries 156 lb on debut, and the first run should reveal plenty.
    DATA: model 7.3% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Share A Dream (hrs_63202923) | 4yo F | 156lb | OR - | draw 0 | jockey Alan O'Sullivan(5) | trainer William Harvey (14d 0/0) | headgear - | last run 211 days | form 0- | MARKET 8.6% | 09:00 median 8.75 | Matchbook 12.50
    comment: Lightly raced and unexposed, Share A Dream was unplaced on her only recent start and returns after 211 days off, so she is open to improvement. She is yet to win in that limited form and carries 156 lb.
    DATA: model 10.6% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 28 Apr Punchestown NH Flat 16.6f Yielding 17/19
    DATA against: Last-run finishing speed -10.0% vs that field (faded); Returns from a 211-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Little Ruby (hrs_61046685) | 5yo M | 156lb | OR - | draw 0 | jockey Tom Midgley(3) | trainer Mark Walford (14d 2/7) | headgear - | last run 245 days | form 04- | MARKET 5.6% | 09:00 median 13.00 | Matchbook 19.00
    DATA: model 3.9% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 18 Feb Southwell NH Flat 15.8f Soft 10/11; 25 Mar Hexham NH Flat 16.2f Soft 4/8
    DATA for: Trainer 29% wins (2/7), last 14 days; Last-run finishing speed +6.5% vs that field (finished strongly)
    DATA against: Returns from a 245-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- Brown Eyes Falco (hrs_17395978705) | 4yo F | 156lb | OR - | draw 0 | jockey Charlie Maggs | trainer Mark Walford (14d 2/7) | headgear - | last run - days | form - | MARKET 4.5% | 09:00 median 17.00 | Matchbook 25.00
    comment: Unraced and making her debut, Brown Eyes Falco is totally unexposed, so there's no form to lean on and plenty of scope for improvement.
    DATA: model 7.3% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 29% wins (2/7), last 14 days
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Stevies Dream (hrs_17395983920) | 4yo F | 156lb | OR - | draw 0 | jockey Joshua Thompson(5) | trainer Mark Walford (14d 2/7) | headgear - | last run - days | form - | MARKET 2.7% | 09:00 median 26.00 | Matchbook 55.00
    comment: Stevies Dream is unraced, so this debutant is a blank canvas with plenty of scope to improve, and nothing in her profile can be held against her yet.
    DATA: model 7.3% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 29% wins (2/7), last 14 days
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Samantha's Lady (hrs_17393907307) | 4yo F | 156lb | OR - | draw 0 | jockey Conor Rabbitt(3) | trainer Susan Corbett (14d 1/8) | headgear - | last run 38 days | form 4 | MARKET 1.2% | 09:00 median 51.00 | Matchbook 120.00
    comment: The main risk is the 156 lb she carries, and she is yet to win in her recent form.
    DATA: model 5.5% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 18 Oct Sedgefield NH Flat 17f Good 4/5 fig 89
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Ciel d'Azur (hrs_17395168294) | 4yo F | 156lb | OR - | draw 0 | jockey Oscar Palmer(7) | trainer Andrew Crook (14d 1/2) | headgear - | last run 16 days | form 7 | MARKET 0.9% | 09:00 median 81.00 | Matchbook 160.00
    comment: Lightly raced and unexposed, Ciel d'Azur has just the one recent run to go on, a seventh last time out 16 days ago, so she looks open to improvement. She is yet to win and carries 156 lb.
    DATA: model 4.2% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 9 Nov Carlisle NH Flat 17f Good To Soft 7/11
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
