# Card review packet: Lingfield, 2026-11-26

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
{"meeting": "lingfield", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 12:37 Lingfield | race_id rac_32305593411 | Sky Sports Racing Virgin 512 Conditional Jockeys' Handicap Hurdle Race
Hurdle | Class 5 | 2m7f0y | going Good | Turf | 7 runners | rating band 0-105 | age 4yo+
DATA pace: Lone leader - Betty's Tiara is the only habitual front-runner and may be allowed an easy lead.
- Cooler Than Me (hrs_29012718) | 8yo G | 159lb | OR 96 | draw 0 | jockey Fern O'Brien(3) | trainer Fergal O'Brien (14d 4/30) | headgear p | last run 23 days | form 1123-1 | MARKET 29.5% | 09:00 median 3.00 | Matchbook 3.20 | CHECK (skip line 2.85)
    comment: Cooler Than Me won last time out and has three wins in his last five starts, with a third and a second in between, while 23 days off is no concern and he has run on today's going.
    DATA: model 19.3% | style Midfield (led 4% of runs) | runs in data 6 | last 3: 26 Feb Taunton Hurdle 19f Good To Soft 2/9; 4 Apr Carlisle Hurdle 25f Good 3/10; 3 Nov Lingfield Hurdle 19.5f Good 1/9 fig 97
    DATA for: Last-run finishing speed +2.7% vs that field (finished strongly); Good recent finishing positions
    DATA against: Race comments mention jumping mistakes in 2 of its last 5 runs
- Teorie (hrs_31660727) | 6yo G | 165lb | OR 102 | draw 0 | jockey Toby McCain-Mitchell | trainer James Owen (14d 4/46) | headgear p | last run 16 days | form 567-61 | MARKET 29.3% | 09:00 median 2.88 | Matchbook 3.35
    comment: The risk is his burden of 165 lb, plus a run of sixth, seventh and sixth before that win.
    DATA: model 16.9% | style Midfield (led 3% of runs) | runs in data 8 | last 3: 17 Apr Exeter Hurdle 23.1f Good 7/8; 17 Oct Stratford Hurdle 18.5f Good 6/7 fig 85; 10 Nov Huntingdon Hurdle 20.5f Good 1/5 fig 99
    DATA for: Best recent form figure 99, 4 lb above field average
- Bright Legend (hrs_31300234) | 6yo G | 165lb | OR 102 | draw 0 | jockey J. P. O'Neill(10) | trainer Faye Bramley (14d 1/15) | headgear t | last run 16 days | form 574382 | MARKET 14.8% | 09:00 median 6.00 | Matchbook 6.40
    comment: Bright Legend arrives in decent nick after a second last time out, just 16 days ago, and has run over today's trip and going before; he's yet to win in his last six, though, and that weight of 165 lb is the main risk.
    DATA: model 18.6% | style Prominent (led 29% of runs) | runs in data 12 | last 3: 11 Oct Chepstow Hurdle 23.6f Good To Soft 3/12; 30 Oct Wetherby Hurdle 21.5f Good 8/11 fig 97; 10 Nov Huntingdon Hurdle 16f Good 2/6 fig 101
    DATA for: Best recent form figure 101, 6 lb above field average; Good recent finishing positions
- Betty's Tiara (hrs_32567801) | 8yo M | 168lb | OR 105 | draw 0 | jockey Beau Morgan(3) | trainer Ben Pauling (14d 8/41) | headgear tv | last run 16 days | form 815231 | MARKET 10.8% | 09:00 median 8.00 | Matchbook 8.80
    DATA: model 19.6% | style Leader (led 79% of runs) | runs in data 8 | last 3: 13 Oct Hereford Hurdle 25.5f Good To Firm 2/4; 28 Oct Huntingdon Hurdle 25f Good 3/6 fig 101; 10 Nov Lingfield Hurdle 23f Good 1/5 fig 103
    DATA for: Best recent form figure 103, 8 lb above field average; Official rating 105, 6 lb above field average; Has won at this trip or further; Good recent finishing positions; Pace: may get an uncontested lead
    DATA against: Carries 6 lb more than average
- Nancefordshore (hrs_51341647) | 5yo G | 159lb | OR 96 | draw 0 | jockey Joe Anderson | trainer Grace Harris (14d 0/9) | headgear - | last run 18 days | form P66F-6 | MARKET 6.6% | 09:00 median 12.00 | Matchbook 16.50
    comment: Nancefordshore is hard to fancy, yet to win in his last five starts and having finished sixth last time out after a fall and a pulled up in that sequence, while 159 lb is a stiff burden off 96.
    DATA: model 7.6% | style Held up (led 4% of runs) | runs in data 4 | last 3: 7 Mar Hereford Hurdle 19.7f Good 6/12; 26 Mar Chepstow Hurdle 19.5f Good To Soft F/10; 8 Nov Ffos Las Hurdle 20f Soft 6/8 fig 83
    DATA against: Best recent form figure 83, 12 lb below field average; Recent figures 13 lb below its current mark (looks high in the weights); Trainer 0 wins from 9 runs, last 14 days; Poor recent finishing positions; Fell or unseated in 1 of its last 4 jumps runs
- Shengai Enki (hrs_34153553) | 7yo G | 156lb | OR 93 | draw 0 | jockey Isabelle Ryder | trainer Barry Brennan (14d 0/3) | headgear p | last run 31 days | form P5-P85 | MARKET 4.5% | 09:00 median 20.50 | Matchbook 22.00
    DATA: model 6.1% | style Midfield (led 4% of runs) | runs in data 5 | last 3: 11 May Southwell Hurdle 20.4f Good PU/10; 11 Oct Chepstow Hurdle 23.6f Good To Soft 8/12; 26 Oct Hereford Hurdle 25.5f Good To Firm 5/8 fig 87
    DATA for: Carries 6 lb less than average
    DATA against: Best recent form figure 87, 8 lb below field average; Recent figures 6 lb below its current mark (looks high in the weights); Official rating 93, 6 lb below field average; Race comments mention jumping mistakes in 2 of its last 5 runs; Pulled up in 2 of its last 5 jumps runs
- West Orchard (hrs_27027280) | 9yo G | 164lb | OR 101 | draw 0 | jockey Will Featherstone(6) | trainer Joe Tizzard (14d 7/26) | headgear p | last run 46 days | form 5231-0 | MARKET 4.5% | 09:00 median 19.00 | Matchbook 23.00
    comment: In his favour, he has run over today's trip and going, and his trainer's yard is in form.
    DATA: model 11.8% | style Prominent (led 4% of runs) | runs in data 4 | last 3: 16 Mar Plumpton Chase 25.7f Good To Soft 3/7; 24 Apr Fontwell Hurdle 25.8f Good 1/8; 11 Oct Chepstow Hurdle 23.6f Good To Soft 10/12
    DATA for: Trainer 27% wins (7/26), last 14 days; Has won at this trip or further; Good recent finishing positions
    DATA against: Last-run finishing speed -8.1% vs that field (faded)

## 1:12 Lingfield | race_id rac_32305595348 | Tips For Every Race At raceday-ready.com Handicap Steeple Chase
Chase | Class 5 | 2m4f0y | going Good | Turf | 6 runners | rating band 0-100 | age 4yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Lifetime In Milan (hrs_37701391) | 7yo G | 151lb | OR 83 | draw 0 | jockey Freddie Gordon | trainer Chris Gordon (14d 2/7) | headgear - | last run 277 days | form 1/P44- | MARKET 27.0% | 09:00 median 3.00 | Matchbook 3.80 | CHECK (skip line 2.85)
    comment: Lightly raced and open to improvement, Lifetime In Milan won four starts back and was fourth on each of his last two outings, though he returns after 277 days off and carries 151 lb, so fitness is the question.
    DATA: model 12.5% | style Midfield (led 5% of runs) | runs in data 3 | last 3: 16 Jan Windsor Hurdle 24f Soft PU/6; 5 Feb Lingfield Hurdle 19.5f Heavy 4/6; 22 Feb Fontwell Hurdle 19.1f Heavy 4/6
    DATA for: Trainer 29% wins (2/7), last 14 days
    DATA against: Last-run finishing speed -3.7% vs that field (faded); Returns from a 277-day break; Pulled up in 1 of its last 3 jumps runs; First run over fences in our data
- Honey Jack (hrs_37889656) | 7yo G | 158lb | OR 90 | draw 0 | jockey Freddie Gingell | trainer Joe Tizzard (14d 7/26) | headgear t | wind surgery | last run 609 days | form 64153/ | MARKET 26.2% | 09:00 median 3.50 | Matchbook 3.55
    comment: Honey Jack was a third last time out and a winner three starts back, and he has run over today's trip and on this going before, with a yard in cracking form (7 from 26). The one big risk is a 609-day absence, plus 158 lb is a hefty burden.
    DATA: model 14.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 27% wins (7/26), last 14 days
    DATA against: Returns from a 609-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Ballybay (hrs_28190995) | 9yo G | 142lb | OR 73 | draw 0 | jockey Freddie Mitchell(3) | trainer Murty McGrath (14d 0/0) | headgear ht | last run 216 days | form /PP56- | MARKET 14.3% | 09:00 median 6.50 | Matchbook 6.60
    comment: Ballybay is winless in his last four, pulled up twice before a fifth and a sixth last time out, and returns after 216 days off.
    DATA: model 11.7% | style Prominent (led 38% of runs) | runs in data 2 | last 3: 5 Apr Plumpton Hurdle 17.8f Good 5/9; 24 Apr Fontwell Chase 19.5f Good 6/12
    DATA for: Carries 14 lb less than average
    DATA against: Official rating 73, 14 lb below field average; Returns from a 216-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- Poncho (hrs_30207716) | 8yo G | 168lb | OR 100 | draw 0 | jockey Caoilin Quinn | trainer Jamie Moore & Josh Moore (14d 3/30) | headgear p | last run 23 days | form 6/1F-7 | MARKET 13.4% | 09:00 median 6.50 | Matchbook 7.60
    comment: Poncho comes here fresh enough after 23 days off, a winner three starts back, and he has run over today's trip and going before.
    DATA: model 19.5% | style Held up (led 4% of runs) | runs in data 3 | last 3: 3 Jan Sandown Hurdle 19.8f Good F/10; 11 Oct Goodwood Flat 16f Good To Soft 10/12; 3 Nov Lingfield Chase 16f Good 7/8 fig 87
    DATA for: Official rating 100, 12 lb above field average
    DATA against: Recent figures 13 lb below its current mark (looks high in the weights); Poor recent finishing positions; Carries 12 lb more than average; Race comments mention jumping mistakes in 2 of its last 2 runs; Fell or unseated in 1 of its last 2 jumps runs; Pace: steady gallop likely, hard to come from off the pace
- Pop's Folly (hrs_47098807) | 6yo G | 155lb | OR 87 | draw 0 | jockey James Best | trainer Georgina Nicholls (14d 0/5) | headgear p (1st time) | last run 45 days | form 563P-P | MARKET 12.3% | 09:00 median 7.50 | Matchbook 7.60
    comment: The main risk is two pulled-up efforts in a row, with a 45-day break to account for.
    DATA: model 20.8% | style Held up (led 4% of runs) | runs in data 5 | last 3: 1 Mar Huntingdon Hurdle 25f Good To Soft 3/7; 17 Mar Exeter Hurdle 23.1f Good To Soft PU/17; 12 Oct Worcester Chase 20f Good PU/9
    DATA for: First-time headgear
    DATA against: Race comments mention jumping mistakes in 2 of its last 5 runs; Pulled up in 2 of its last 5 jumps runs; Pace: steady gallop likely, hard to come from off the pace
- Kitsilano (hrs_25040757) | 9yo G | 160lb | OR 92 | draw 0 | jockey Ciaran Gethings | trainer David Bridgwater (14d 0/2) | headgear p | last run 216 days | form 3134B- | MARKET 6.7% | 09:00 median 12.00 | Matchbook 16.50
    DATA: model 21.1% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 23 Feb Plumpton Chase 17f Soft 3/5; 27 Mar Fontwell Chase 21.6f Good To Soft 4/5; 24 Apr Fontwell Chase 19.5f Good BD/12
    DATA against: Returns from a 216-day break; Fell or unseated in 1 of its last 5 jumps runs

## 1:47 Lingfield | race_id rac_32305597285 | Mark Sheasby Birthday Celebration Mares' Maiden Hurdle Race (GBB Race)
Hurdle | Class 4 | 2m3f110y | going Good | Turf | 12 runners | rating band - | age 4yo+
DATA pace: Lone leader - Pure Ocean is the only habitual front-runner and may be allowed an easy lead.
- True To My Word (hrs_17396043371) | 4yo F | 155lb | OR - | draw 0 | jockey Ben Jones | trainer Ben Pauling (14d 8/41) | headgear - | last run 263 days | form 1- | MARKET 28.6% | 09:00 median 2.88 | Matchbook 3.25
    DATA: model 7.0% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 263-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Rainbow Tara (hrs_51897545) | 6yo M | 156lb | OR - | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 21/94) | headgear - | last run 25 days | form 7/25-9 | MARKET 19.4% | 09:00 median 4.42 | Matchbook 4.70
    DATA: model 10.3% | style Prominent (led 38% of runs) | runs in data 2 | last 3: 3 Mar Newcastle NH Flat 16.9f Good To Soft 5/7; 1 Nov Worcester Hurdle 16f Good To Soft 9/16 fig 88
    DATA for: Trainer 22% wins (21/94), last 14 days
    DATA against: Best recent form figure 88, 7 lb below field average; Lightly raced: 2 runs in our data, so the model has little to go on
- Western Charm (hrs_59645495) | 5yo M | 156lb | OR - | draw 0 | jockey Ben Godfrey | trainer Anthony Honeyball (14d 1/9) | headgear - | last run 28 days | form 6195-4 | MARKET 14.6% | 09:00 median 6.00 | Matchbook 6.20
    DATA: model 8.9% | style Midfield (led 4% of runs) | runs in data 4 | last 3: 7 Mar Sandown NH Flat 16f Soft 9/10; 12 Apr Wincanton NH Flat 15.2f Good 5/5; 29 Oct Stratford Hurdle 22f Good To Soft 4/9 fig 99
    DATA for: Last-run finishing speed +2.4% vs that field (finished strongly)
- Pure Ocean (hrs_58843960) | 5yo M | 156lb | OR - | draw 0 | jockey Kevin Brogan | trainer Richard Bandey (14d 0/1) | headgear - | last run 253 days | form 522- | MARKET 10.6% | 09:00 median 7.50 | Matchbook 9.00
    DATA: model 16.8% | style Leader (led 57% of runs) | runs in data 2 | last 3: 27 Jan Newcastle NH Flat 16.3f Soft 2/8; 18 Mar Huntingdon Hurdle 19.6f Good 2/6
    DATA for: Last-run finishing speed +4.4% vs that field (finished strongly); Good recent finishing positions; Pace: may get an uncontested lead
    DATA against: Returns from a 253-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- Ashburton (hrs_56559692) | 4yo F | 155lb | OR - | draw 0 | jockey Rex Dingle | trainer Anthony Honeyball (14d 1/9) | headgear - | last run 274 days | form 25- | MARKET 8.3% | 09:00 median 10.00 | Matchbook 11.50
    DATA: model 14.2% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 25 Feb Wincanton NH Flat 15.2f Good To Soft 5/14
    DATA for: Last-run finishing speed +3.4% vs that field (finished strongly)
    DATA against: Returns from a 274-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Marvetta (hrs_62326425) | 5yo M | 156lb | OR - | draw 0 | jockey Freddie Gingell | trainer Joe Tizzard (14d 7/26) | headgear - | last run 257 days | form 8- | MARKET 5.9% | 09:00 median 12.00 | Matchbook 18.50
    DATA: model 8.2% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 14 Mar Uttoxeter NH Flat 15.8f Soft 8/12
    DATA for: Trainer 27% wins (7/26), last 14 days
    DATA against: Returns from a 257-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Its A Vibe (hrs_17392704728) | 4yo F | 155lb | OR - | draw 0 | jockey Joe Anderson(3) | trainer Grace Harris (14d 0/9) | headgear - | last run 63 days | form P-4 | MARKET 4.2% | 09:00 median 19.00 | Matchbook 25.00
    DATA: model 2.6% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 24 Sep Listowel Hurdle 16f Good 4/14
    DATA against: Trainer 0 wins from 9 runs, last 14 days; Lightly raced: 1 run in our data, so the model has little to go on
- Grizzled Squirrel (hrs_53081476) | 5yo M | 156lb | OR - | draw 0 | jockey Caoilin Quinn | trainer Jamie Moore & Josh Moore (14d 3/30) | headgear - | last run 285 days | form 539- | MARKET 2.3% | 09:00 median 29.00 | Matchbook 55.00
    DATA: model 7.3% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 14 Feb Ascot NH Flat 15.7f Good To Soft 9/9
    DATA against: Last-run finishing speed -2.2% vs that field (faded); Returns from a 285-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Amber Dancer (hrs_17396040242) | 5yo M | 156lb | OR - | draw 0 | jockey Jack Quinlan | trainer Neil King (14d 0/3) | headgear t (1st time) | last run 277 days | form 2- | MARKET 1.7% | 09:00 median 34.00 | Matchbook 100.00
    DATA: model 7.0% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: First-time headgear
    DATA against: Returns from a 277-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Gone Away Madam (hrs_35416710) | 8yo M | 156lb | OR - | draw 0 | jockey Jonjo O'Neill Jr. | trainer Neil King (14d 0/3) | headgear - | last run 957 days | form 1487/ | MARKET 1.6% | 09:00 median 34.00 | Matchbook 100.00
    DATA: model 7.0% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 957-day break; Lightly raced: 0 runs in our data, so the model has little to go on; Aged 8, older than most of this field
- Lady Kloppenheim (hrs_41072724) | 6yo M | 156lb | OR - | draw 0 | jockey Freddie Gordon | trainer Harry Ryall (14d 0/0) | headgear - | last run 559 days | form 713/6- | MARKET 1.6% | 09:00 median 41.00 | Matchbook 75.00
    DATA: model 7.0% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 559-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Valentine Wren (hrs_17395129703) | 4yo F | 155lb | OR - | draw 0 | jockey Sean Houlihan | trainer Samuel Drinkwater (14d 0/5) | headgear - | last run 19 days | form 0 | MARKET 1.1% | 09:00 median 51.00 | Matchbook 180.00
    DATA: model 3.7% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 7 Nov Uttoxeter NH Flat 16f Good 10/14 fig 99
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on

## 2:22 Lingfield | race_id rac_32305599222 | Follow @AtTheRaces On X Novices' Limited Handicap Steeple Chase (GBB Race)
Chase | Class 3 | 2m4f0y | going Good | Turf | 6 runners | rating band 0-130 | age 4yo+
DATA pace: Lone leader - Kasino des Mottes is the only habitual front-runner and may be allowed an easy lead.
- Laughing John (hrs_48499311) | 5yo G | 156lb | OR 122 | draw 0 | jockey Nico de Boinville | trainer Nicky Henderson (14d 4/21) | headgear - | last run 30 days | form /110-F | MARKET 32.8% | 09:00 median 2.75 | Matchbook 2.96
    comment: Laughing John fell last time out and was unplaced the run before, so the confidence from back-to-back wins three and four starts back has drained away, and he has 156 lb to carry off 122.
    DATA: model 24.3% | style Prominent (led 8% of runs) | runs in data 3 | last 3: 25 Feb Wincanton Hurdle 19.8f Good To Soft 1/15; 28 Apr Punchestown Hurdle 19.4f Yielding 10/24; 27 Oct Bangor-on-Dee Chase 20.5f Good To Soft F/13
    DATA for: Has won at this trip or further
    DATA against: Fell or unseated in 1 of its last 3 jumps runs
- Blue Carpet (hrs_45759602) | 6yo G | 166lb | OR 132 | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 21/94) | headgear - | last run 236 days | form 21212- | MARKET 22.5% | 09:00 median 3.75 | Matchbook 4.50
    comment: Blue Carpet arrives in cracking recent form, second last time out, a winner two starts back and another winner four starts back, and he has run over today's trip and on this going before. The one concern is a 236-day absence, which leaves fitness the main risk under 166 lb.
    DATA: model 30.0% | style Held up (led 5% of runs) | runs in data 2 | last 3: 26 Feb Wetherby Hurdle 24.1f Soft 1/10; 4 Apr Haydock Hurdle 24.3f Good 2/9
    DATA for: Official rating 132, 8 lb above field average; Trainer 22% wins (21/94), last 14 days; Last-run finishing speed +3.1% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Carries 8 lb more than average; Returns from a 236-day break; Lightly raced: 2 runs in our data, so the model has little to go on; First run over fences in our data
- Fortune Timmy (hrs_47837237) | 6yo G | 166lb | OR 132 | draw 0 | jockey Freddie Gordon | trainer Chris Gordon (14d 2/7) | headgear - | last run 229 days | form 31300- | MARKET 20.9% | 09:00 median 4.50 | Matchbook 4.50
    comment: A 229-day absence and two unplaced runs since are the reservation, though 166 lb is a sizeable burden.
    DATA: model 12.4% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 24 Jan Cheltenham Hurdle 20.3f Soft 3/7; 11 Mar Cheltenham Hurdle 21f Good 12/21; 11 Apr Aintree Hurdle 24.7f Good To Soft 17/22
    DATA for: Official rating 132, 8 lb above field average; Trainer 29% wins (2/7), last 14 days
    DATA against: Last-run finishing speed -8.2% vs that field (faded); Carries 8 lb more than average; Returns from a 229-day break; First run over fences in our data
- Kasino des Mottes (hrs_41052263) | 6yo G | 156lb | OR 122 | draw 0 | jockey Freddie Gingell | trainer Joe Tizzard (14d 7/26) | headgear - | last run 33 days | form 5380-5 | MARKET 11.6% | 09:00 median 7.50 | Matchbook 8.80
    comment: The main risk is that he's yet to win in his last five starts and shoulders 156 lb.
    DATA: model 8.2% | style Leader (led 54% of runs) | runs in data 4 | last 3: 14 Feb Haydock Hurdle 24.3f Good To Soft 8/9; 14 Mar Uttoxeter Hurdle 19.9f Soft 10/14; 24 Oct Cheltenham Chase 25f Good To Soft 5/6
    DATA for: Trainer 27% wins (7/26), last 14 days; Pace: may get an uncontested lead
- Royal Way (hrs_38370892) | 6yo G | 152lb | OR 118 | draw 0 | jockey Sean Houlihan | trainer Jamie Moore & Josh Moore (14d 3/30) | headgear - | last run 206 days | form 3124-2 | MARKET 6.7% | 09:00 median 13.00 | Matchbook 15.00
    comment: Royal Way has finished in the first four in each of his last five starts, including a second last time out and a win four starts back, and he has run over today's trip and going before. The one concern is a 206-day absence, with 152 lb to carry.
    DATA: model 16.6% | style Midfield (led 4% of runs) | runs in data 6 | last 3: 29 Mar Ascot Hurdle 21.7f Good 2/9; 25 Apr Sandown Hurdle 19.8f Good 4/10; 4 May Fakenham Hurdle 20f Good 2/12
    DATA for: Last-run finishing speed +3.9% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions; Carries 6 lb less than average
    DATA against: Official rating 118, 6 lb below field average; Returns from a 206-day break; Race comments mention jumping mistakes in 2 of its last 5 runs; First run over fences in our data
- General Briar (hrs_37890594) | 7yo G | 150lb | OR 116 | draw 0 | jockey Caoilin Quinn | trainer Chris Gordon (14d 2/7) | headgear - | last run 21 days | form 11PP-0 | MARKET 5.5% | 09:00 median 15.00 | Matchbook 19.00
    comment: General Briar was unplaced last time out and pulled up in his two runs before that, which makes him hard to fancy, though he won four and five starts back and has run over today's trip and going.
    DATA: model 8.4% | style Prominent (led 23% of runs) | runs in data 4 | last 3: 7 Mar Sandown Hurdle 16f Soft PU/18; 5 Apr Plumpton Hurdle 15.9f Good PU/14; 5 Nov Newbury Hurdle 16.5f Good To Soft 11/16 fig 106
    DATA for: Trainer 29% wins (2/7), last 14 days; Carries 8 lb less than average
    DATA against: Recent figures 10 lb below its current mark (looks high in the weights); Official rating 116, 8 lb below field average; Poor recent finishing positions; Pulled up in 2 of its last 4 jumps runs; First run over fences in our data

## 2:57 Lingfield | race_id rac_32305601159 | Get Raceday Ready Novices' Hurdle Race (GBB Race)
Hurdle | Class 4 | 2m0f0y | going Good | Turf | 9 runners | rating band - | age 4yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Forthfactor (hrs_50187865) | 5yo G | 161lb | OR - | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 21/94) | headgear - | last run 28 days | form /151-1 | MARKET 63.1% | 09:00 median 1.40 | Matchbook 1.43
    DATA: model 27.2% | style Unknown | runs in data 2 | last 3: 11 Apr Aintree NH Flat 16.9f Good To Soft 1/20; 29 Oct Stratford Hurdle 16.5f Good To Soft 1/9 fig 115
    DATA for: Trainer 22% wins (21/94), last 14 days; Last-run finishing speed +2.3% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Milou du Chenet (hrs_58316265) | 4yo G | 154lb | OR 120 | draw 0 | jockey Jonjo O'Neill Jr. | trainer Warren Greatrex (14d 4/25) | headgear - | last run 294 days | form 112- | MARKET 20.2% | 09:00 median 3.75 | Matchbook 5.10
    DATA: model 28.7% | style Unknown | runs in data 1 | last 3: 5 Feb Doncaster Hurdle 16.6f Soft 2/8
    DATA for: Last-run finishing speed +5.5% vs that field (finished strongly)
    DATA against: Returns from a 294-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Ruling Planet (hrs_50809724) | 4yo G | 154lb | OR - | draw 0 | jockey Ben Jones | trainer Ben Pauling (14d 8/41) | headgear t | last run 24 days | form 21-6 | MARKET 7.0% | 09:00 median 9.50 | Matchbook 17.00
    DATA: model 11.0% | style Held up (led 8% of runs) | runs in data 1 | last 3: 2 Nov Southwell Hurdle 16f Good 6/14
    DATA for: Last-run finishing speed +2.1% vs that field (finished strongly)
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Tythingman (hrs_61910674) | 4yo G | 154lb | OR - | draw 0 | jockey Freddie Gingell | trainer Joe Tizzard (14d 7/26) | headgear - | wind surgery | last run 33 days | form 1-0 | MARKET 3.0% | 09:00 median 19.00 | Matchbook 50.00
    DATA: model 8.2% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 22 Feb Hereford NH Flat 16.2f Soft 1/10; 24 Oct Cheltenham NH Flat 16.5f Good To Soft 10/10
    DATA for: Trainer 27% wins (7/26), last 14 days; Has won at this trip or further
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; First run over hurdles in our data
- Intrastellar (hrs_61242566) | 5yo G | 154lb | OR - | draw 0 | jockey Kevin Brogan | trainer Jonjo & A.J. O'Neill (14d 4/35) | headgear h (1st time) | last run - days | form - | MARKET 2.3% | 09:00 median 26.00 | Matchbook 75.00
    DATA: model 6.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: First-time headgear
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Push Push (hrs_17396044414) | 5yo M | 147lb | OR - | draw 0 | jockey Harry Reed | trainer Chris Gordon (14d 2/7) | headgear h (1st time) | last run 305 days | form 52P22- | MARKET 1.6% | 09:00 median 34.00 | Matchbook 120.00
    DATA: model 5.9% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 29% wins (2/7), last 14 days; First-time headgear
    DATA against: Returns from a 305-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Uncle Scrooge (hrs_17394064800) | 5yo G | 154lb | OR - | draw 0 | jockey Freddie Gordon | trainer Chris Gordon (14d 2/7) | headgear - | last run 36 days | form 3/P2-8 | MARKET 1.5% | 09:00 median 41.00 | Matchbook 95.00
    DATA: model 7.1% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 21 Oct Fontwell Hurdle 19f Soft 8/11
    DATA for: Trainer 29% wins (2/7), last 14 days
    DATA against: Last-run finishing speed -5.2% vs that field (faded); Lightly raced: 1 run in our data, so the model has little to go on
- Fury Lad (hrs_35243278) | 7yo G | 154lb | OR - | draw 0 | jockey Freddie Mitchell(3) | trainer Richard Rowe (14d 0/1) | headgear - | last run 257 days | form 6/PP4- | MARKET 0.7% | 09:00 median 81.00 | Matchbook 250.00
    DATA: model 1.1% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 14 Mar Kempton Hurdle 21f Good 4/5
    DATA against: Last-run finishing speed -11.0% vs that field (faded); Returns from a 257-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Don de La Frontera (hrs_62393940) | 5yo G | 154lb | OR - | draw 0 | jockey Jack Quinlan | trainer Neil King (14d 0/3) | headgear h (1st time) | last run 125 days | form 78-79 | MARKET 0.6% | 09:00 median 101.00 | Matchbook 280.00
    DATA: model 4.4% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 5 Jul Market Rasen NH Flat 16.6f Good 7/11; 24 Jul Uttoxeter Hurdle 15.8f Good 9/13
    DATA for: First-time headgear
    DATA against: Last-run finishing speed -7.4% vs that field (faded); Returns from a 125-day break; Lightly raced: 2 runs in our data, so the model has little to go on

## 3:32 Lingfield | race_id rac_32305603096 | Follow @attheraces On Instagram Handicap Hurdle Race
Hurdle | Class 4 | 2m3f110y | going Good | Turf | 7 runners | rating band 0-110 | age 3yo+
DATA pace: Lone leader - Marhaba Prince is the only habitual front-runner and may be allowed an easy lead.
- Rip Wheeler (hrs_39431371) | 6yo G | 160lb | OR 102 | draw 0 | jockey Cian Murphy(10) | trainer Jamie Moore & Josh Moore (14d 3/30) | headgear - | last run 10 days | form 1241-2 | MARKET 33.7% | 09:00 median 2.63 | Matchbook 2.76
    comment: Rip Wheeler booked a second last time out, a winner two starts back, and has twice won in his last five outings; he's fresh from just ten days ago and has run over today's trip and going.
    DATA: model 24.5% | style Held up (led 3% of runs) | runs in data 6 | last 3: 27 Mar Fontwell Chase 19.5f Good To Soft 4/8; 8 Apr Fontwell Chase 21.6f Good To Soft 1/4; 16 Nov Plumpton Hurdle 20.5f Good To Soft 2/12 fig 101
    DATA for: Last-run finishing speed +7.6% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Best recent form figure 101, 4 lb below field average
- Marhaba Prince (hrs_47685015) | 5yo G | 169lb | OR 111 | draw 0 | jockey James Robottom(10) | trainer Anthony Honeyball (14d 1/9) | headgear t | last run 11 days | form 21-P81 | MARKET 27.9% | 09:00 median 2.94 | Matchbook 3.60
    comment: Marhaba Prince won last time out just 11 days ago and has two wins in his last five starts, so he arrives fresh and in form, having run over today's trip.
    DATA: model 29.9% | style Leader (led 63% of runs) | runs in data 5 | last 3: 2 May Hexham Hurdle 16.2f Good PU/6; 28 Oct Newton Abbot Hurdle 17f Good To Soft 8/8 fig 102; 15 Nov Fontwell Hurdle 17.5f Good To Soft 1/8 fig 113
    DATA for: Best recent form figure 113, 8 lb above field average; Official rating 111, 10 lb above field average; Pace: may get an uncontested lead
    DATA against: Carries 11 lb more than average; Pulled up in 1 of its last 5 jumps runs
- Ventara (hrs_34401864) | 8yo G | 146lb | OR 88 | draw 0 | jockey Dylan Johnston | trainer Joe Tizzard (14d 7/26) | headgear - | last run 561 days | form 426/9- | MARKET 12.8% | 09:00 median 7.00 | Matchbook 7.60
    comment: Ventara returns after 561 days off, having finished ninth last time out, though he was second three starts back and has run over today's trip. Winless in his last four, he carries 146 lb off 88, but the yard's 7 from 26 lately offers some encouragement.
    DATA: model 8.8% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 27% wins (7/26), last 14 days; Carries 12 lb less than average
    DATA against: Official rating 88, 13 lb below field average; Returns from a 561-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Moon Monarch (hrs_412653178) | 6yo G | 142lb | OR 84 | draw 0 | jockey Harry Reed | trainer Chris Gordon (14d 2/7) | headgear - | last run 221 days | form 558/7- | MARKET 10.2% | 09:00 median 8.00 | Matchbook 10.00
    comment: Moon Monarch is winless in his last four, finishing seventh last time out, with an eighth and two fifths before that, and returns after 221 days off.
    DATA: model 6.1% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 19 Apr Plumpton Hurdle 15.9f Good 7/7
    DATA for: Trainer 29% wins (2/7), last 14 days; Carries 16 lb less than average
    DATA against: Official rating 84, 17 lb below field average; Last-run finishing speed -3.5% vs that field (faded); Returns from a 221-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Rock On Cowboy (hrs_29226407) | 9yo G | 163lb | OR 105 | draw 0 | jockey Jack Hogan | trainer Fergal O'Brien (14d 4/30) | headgear p | last run 29 days | form 31/2-6 | MARKET 6.2% | 09:00 median 13.00 | Matchbook 15.50
    comment: Rock On Cowboy has a sound profile, a second two starts back and a winner three starts back, and he has run over today's trip and going before after a 29-day break.
    DATA: model 11.2% | style Unknown | runs in data 1 | last 3: 28 Oct Newton Abbot Hurdle 17f Good To Soft 6/8 fig 101
    DATA against: Best recent form figure 101, 4 lb below field average; Lightly raced: 1 run in our data, so the model has little to go on; Aged 9, older than most of this field
- Longmoor (hrs_62779458) | 4yo G | 161lb | OR 104 | draw 0 | jockey Freddie Gingell | trainer Joe Tizzard (14d 7/26) | headgear - | last run 36 days | form 34-6 | MARKET 5.0% | 09:00 median 19.00 | Matchbook 19.50
    comment: Longmoor is winless in his last three, sliding from a third to a fourth and then a sixth last time out, and he has been off for 36 days, so he is hard to fancy under 161 lb.
    DATA: model 11.3% | style Prominent (led 5% of runs) | runs in data 3 | last 3: 22 Mar Exeter Hurdle 16.7f Good 3/9; 11 Apr Chepstow Hurdle 16.1f Good To Soft 4/7; 21 Oct Worcester Hurdle 16f Good To Soft 6/7
    DATA for: Trainer 27% wins (7/26), last 14 days
    DATA against: Last-run finishing speed -4.0% vs that field (faded)
- Galactique (hrs_53928385) | 4yo G | 167lb | OR 110 | draw 0 | jockey Caoilin Quinn | trainer Murty McGrath (14d 0/0) | headgear - | last run 242 days | form 11760- | MARKET 4.2% | 09:00 median 21.00 | Matchbook 23.00
    comment: The main risk is a 242-day absence after finishing unplaced last time.
    DATA: model 8.3% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 7 Mar Sandown Hurdle 16f Soft 6/6; 29 Mar Ascot Hurdle 15.7f Good 10/10
    DATA for: Official rating 110, 9 lb above field average
    DATA against: Carries 9 lb more than average; Returns from a 242-day break; Lightly raced: 2 runs in our data, so the model has little to go on
