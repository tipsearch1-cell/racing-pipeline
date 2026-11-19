# Card review packet: Warwick, 2026-11-19

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
{"meeting": "warwick", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 11:27 Warwick | race_id rac_32304851540 | Hazelton Mountford Insurance Brokers EBF Fillies' Junior 'National Hunt' Hurdle Race (GBB Race)
Hurdle | Class 4 | 2m | going Soft | Turf | 4 runners | rating band - | age 3yo
DATA pace: Unclear - Running styles known for only 0 of 4 runners.
- Leslie's Pride (hrs_17395613655) | 3yo F | 154lb | OR - | draw 0 | jockey Paul O'Brien | trainer Harry Derham (14d 3/12) | headgear - | last run - days | form - | MARKET 51.2% | 09:00 median 1.80 | Matchbook 1.88
    comment: Leslie's Pride is unraced, so this is a debut with nothing to go on form-wise, which makes her unexposed and open to improvement. She carries 154 lb, and there's no recorded run to judge her by yet.
    DATA: model 25.0% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 25% wins (3/12), last 14 days
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Saq of Gold (hrs_17395615741) | 3yo F | 154lb | OR - | draw 0 | jockey Jonathan Burke | trainer James Owen (14d 3/28) | headgear h (1st time) | last run - days | form - | MARKET 17.8% | 09:00 median 5.00 | Matchbook 5.60
    comment: Unexposed and open to improvement, this filly makes her debut with no recorded form to go on, so she is one to learn about on the day. She carries 154 lb, and her ability is still an unknown.
    DATA: model 25.0% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: First-time headgear
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Noble Fleur (hrs_17395614698) | 3yo F | 154lb | OR - | draw 0 | jockey Sean Bowen | trainer Martin Keighley (14d 3/11) | headgear - | last run - days | form - | MARKET 16.1% | 09:00 median 5.50 | Matchbook 6.20
    comment: Noble Fleur is unexposed on her debut with no form to assess, so any progress is a bonus, and she shoulders 154 lb. Plenty of room for improvement as a newcomer, but she's one to learn from rather than lean on today.
    DATA: model 25.0% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 27% wins (3/11), last 14 days
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Hera d'Inor (hrs_17395612612) | 3yo F | 154lb | OR - | draw 0 | jockey Rex Dingle | trainer Warren Greatrex (14d 4/17) | headgear - | wind surgery | last run - days | form - | MARKET 14.9% | 09:00 median 6.00 | Matchbook 6.80
    comment: Hera d'Inor is an unraced filly with no form to assess, so she is wholly unexposed and open to improvement. She carries 154 lb on debut, and nothing yet says what she can do.
    DATA: model 25.0% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 24% wins (4/17), last 14 days
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on

## 11:57 Warwick | race_id rac_32305213759 | Olly Murphy Proudly Sponsored By Betano 'National Hunt' Maiden Hurdle Race (Div I) (GBB Race)
Hurdle | Class 4 | 2m | going Soft | Turf | 15 runners | rating band - | age 4yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Friendly Glance (hrs_62101592) | 4yo G | 158lb | OR - | draw 0 | jockey Tom Bellamy | trainer Alan King (14d 2/16) | headgear - | last run 264 days | form 1- | MARKET 29.6% | 09:00 median 2.75 | Matchbook 2.98
    DATA: model 13.4% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 28 Feb Doncaster NH Flat 16.6f Soft 1/8
    DATA for: Last-run finishing speed +9.0% vs that field (finished strongly); Has won at this trip or further
    DATA against: Returns from a 264-day break; Lightly raced: 1 run in our data, so the model has little to go on
- St Gabriel (hrs_63202846) | 4yo G | 158lb | OR - | draw 0 | jockey Nico de Boinville | trainer Nicky Henderson (14d 3/12) | headgear - | last run 194 days | form 1 | MARKET 22.2% | 09:00 median 3.50 | Matchbook 4.20
    DATA: model 11.6% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 9 May Haydock NH Flat 15.7f Good To Soft 1/9
    DATA for: Trainer 25% wins (3/12), last 14 days; Last-run finishing speed +7.2% vs that field (finished strongly); Has won at this trip or further
    DATA against: Returns from a 194-day break; Lightly raced: 1 run in our data, so the model has little to go on
- L'Unique Allen (hrs_62615105) | 5yo G | 158lb | OR - | draw 0 | jockey Sean Bowen | trainer Olly Murphy (14d 7/45) | headgear - | last run 247 days | form 2- | MARKET 17.8% | 09:00 median 4.33 | Matchbook 5.20
    DATA: model 13.1% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 17 Mar Wetherby NH Flat 16f Good To Soft 2/9
    DATA for: Last-run finishing speed +5.9% vs that field (finished strongly)
    DATA against: Returns from a 247-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Power of Silence (hrs_50666854) | 5yo G | 158lb | OR - | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 18/80) | headgear - | last run 287 days | form 5/24- | MARKET 12.6% | 09:00 median 6.50 | Matchbook 7.00
    DATA: model 7.6% | style Held up (led 8% of runs) | runs in data 1 | last 3: 5 Feb Huntingdon NH Flat 15.8f Soft 4/8
    DATA for: Trainer 22% wins (18/80), last 14 days; Last-run finishing speed +2.5% vs that field (finished strongly)
    DATA against: Returns from a 287-day break; Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Prince Vinny (hrs_58412116) | 4yo G | 158lb | OR - | draw 0 | jockey Harry Cobden | trainer Emma Lavelle (14d 3/14) | headgear - | last run 45 days | form 686-2 | MARKET 5.6% | 09:00 median 13.00 | Matchbook 17.50
    DATA: model 2.8% | style Held up (led 5% of runs) | runs in data 2 | last 3: 22 Mar Exeter Hurdle 16.7f Good 6/9; 5 Oct Stratford Hurdle 16.3f Good To Firm 2/6
    DATA for: Trainer 21% wins (3/14), last 14 days; Last-run finishing speed +5.2% vs that field (finished strongly)
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Artaban (hrs_62876338) | 5yo G | 158lb | OR - | draw 0 | jockey Sam Twiston-Davies | trainer Paul Nicholls (14d 2/16) | headgear - | wind surgery | last run 240 days | form 3- | MARKET 4.0% | 09:00 median 17.00 | Matchbook 28.00
    DATA: model 9.2% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 24 Mar Taunton NH Flat 16.5f Good 3/6
    DATA against: Returns from a 240-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Twentysixsoldiers (hrs_17395517699) | 4yo G | 158lb | OR - | draw 0 | jockey Gavin Sheehan | trainer Billy Aprahamian (14d 0/2) | headgear - | last run 229 days | form 3- | MARKET 1.9% | 09:00 median 41.00 | Matchbook 60.00
    DATA: model 5.1% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 229-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Sub Editor (hrs_17394733363) | 5yo G | 158lb | OR - | draw 0 | jockey Kevin Brogan | trainer Olly Murphy (14d 7/45) | headgear - | last run 18 days | form 1-6 | MARKET 1.5% | 09:00 median 51.00 | Matchbook 100.00
    DATA: model 7.1% | style Held up (led 8% of runs) | runs in data 1 | last 3: 1 Nov Worcester Hurdle 16f Good To Soft 6/16 fig 106
    DATA for: Best recent form figure 106, 9 lb above field average; Last-run finishing speed +3.5% vs that field (finished strongly)
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Elmsford (hrs_17393840555) | 4yo G | 158lb | OR - | draw 0 | jockey Ben Jones | trainer Ben Pauling (14d 4/21) | headgear h (1st time) | last run 34 days | form 9-34 | MARKET 1.2% | 09:00 median 51.00 | Matchbook 150.00
    DATA: model 5.3% | style Held up (led 8% of runs) | runs in data 1 | last 3: 16 Oct Uttoxeter Hurdle 16f Good 4/10
    DATA for: Last-run finishing speed +2.8% vs that field (finished strongly); First-time headgear
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Roxy Rocks (hrs_62876331) | 5yo M | 151lb | OR - | draw 0 | jockey Bryan Carver | trainer Chris Honour (14d 0/4) | headgear - | last run 39 days | form 43-6 | MARKET 0.7% | 09:00 median 151.00 | Matchbook 160.00
    DATA: model 2.2% | style Prominent (led 38% of runs) | runs in data 3 | last 3: 24 Mar Taunton NH Flat 16.5f Good 4/6; 17 Apr Exeter NH Flat 16.7f Good 3/5; 11 Oct Chepstow NH Flat 16.1f Good To Soft 6/6
    DATA against: Last-run finishing speed -7.6% vs that field (faded); First run over hurdles in our data
- For Her Glory (hrs_64522962) | 4yo F | 151lb | OR - | draw 0 | jockey Liam Harrison | trainer David Brace (14d 0/1) | headgear h | last run 139 days | form 134 | MARKET 0.7% | 09:00 median 101.00 | Matchbook 240.00
    DATA: model 8.8% | style Unknown | runs in data 3 | last 3: 11 May Southwell NH Flat 15.8f Good 1/10; 2 Jun Southwell NH Flat 15.8f Good 3/6; 3 Jul Newton Abbot Hurdle 16.8f Good 4/8
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Returns from a 139-day break
- All Good To Go (hrs_60527761) | 5yo G | 158lb | OR - | draw 0 | jockey Kielan Woods | trainer Alex Hales (14d 0/4) | headgear h | last run 22 days | form 4-8 | MARKET 0.6% | 09:00 median 126.00 | Matchbook 250.00
    DATA: model 2.0% | style Held up (led 8% of runs) | runs in data 2 | last 3: 18 Jan Fakenham NH Flat 16f Good To Soft 4/4; 28 Oct Huntingdon NH Flat 16f Good 8/9 fig 92
    DATA against: Best recent form figure 92, 5 lb below field average; Lightly raced: 2 runs in our data, so the model has little to go on; First run over hurdles in our data; Pace: steady gallop likely, hard to come from off the pace
- Golden Sanjida (hrs_60722543) | 4yo F | 151lb | OR - | draw 0 | jockey Lewis Stones(3) | trainer Olly Murphy (14d 7/45) | headgear - | last run 11 days | form 402-68 | MARKET 0.6% | 09:00 median 101.00 | Matchbook 380.00
    DATA: model 2.8% | style Held up (led 4% of runs) | runs in data 5 | last 3: 19 Apr Plumpton NH Flat 17.8f Good 2/7; 30 Oct Uttoxeter Hurdle 16f Good 6/13 fig 92; 8 Nov Ffos Las Hurdle 16f Soft 8/11 fig 84
    DATA against: Best recent form figure 92, 5 lb below field average; Pace: steady gallop likely, hard to come from off the pace
- Our Rarest Hour (hrs_17395616784) | 4yo G | 158lb | OR - | draw 0 | jockey Lee Edwards | trainer Claire Dyson (14d 0/0) | headgear - | last run 26 days | form 53 | MARKET 0.6% | 09:00 median 101.00 | Matchbook 460.00
    DATA: model 5.1% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Triple Edge (hrs_62235824) | 4yo G | 158lb | OR - | draw 0 | jockey Lorcan Williams | trainer Chester Williams (14d 0/4) | headgear - | last run 11 days | form 84-6 | MARKET 0.3% | 09:00 median 151.00 | Matchbook 990.00
    DATA: model 3.8% | style Midfield (led 29% of runs) | runs in data 3 | last 3: 5 Mar Wincanton NH Flat 15.2f Good To Soft 8/12; 7 Apr Exeter NH Flat 16.7f Good 4/6; 8 Nov Sandown Hurdle 16f Good 6/7

## 12:27 Warwick | race_id rac_32304853477 | Olly Murphy Proudly Sponsored By Betano 'National Hunt' Maiden Hurdle Race (Div II) (GBB Race)
Hurdle | Class 4 | 2m | going Soft | Turf | 14 runners | rating band - | age 4yo+
DATA pace: Even - Two likely leaders (Burk Flight, Roximan). A fair, even gallop is most likely.
- Smile John Boy (hrs_58715265) | 5yo G | 158lb | OR - | draw 0 | jockey Ben Jones | trainer Ben Pauling (14d 4/21) | headgear - | last run 21 days | form 1240-3 | MARKET 44.6% | 09:00 median 1.87 | Matchbook 1.99
    DATA: model 13.1% | style Unknown | runs in data 3 | last 3: 21 Feb Kempton NH Flat 16f Good To Soft 4/13; 11 Apr Aintree NH Flat 16.9f Good To Soft 10/20; 29 Oct Stratford Hurdle 16.5f Good To Soft 3/10 fig 112
    DATA for: Best recent form figure 112, 9 lb above field average; Last-run finishing speed +5.0% vs that field (finished strongly)
- Half Hoping (hrs_48853889) | 5yo G | 158lb | OR - | draw 0 | jockey Tom Cannon | trainer Nick Gifford (14d 1/5) | headgear - | last run 285 days | form 214- | MARKET 17.8% | 09:00 median 4.42 | Matchbook 5.30
    DATA: model 9.1% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 7 Feb Newbury NH Flat 16.3f Heavy 4/10
    DATA for: Trainer 20% wins (1/5), last 14 days; Last-run finishing speed +7.5% vs that field (finished strongly)
    DATA against: Returns from a 285-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Rock On Ronnie (hrs_60090205) | 5yo G | 158lb | OR - | draw 0 | jockey Sean Bowen | trainer Olly Murphy (14d 7/45) | headgear - | last run 21 days | form 73-2 | MARKET 13.6% | 09:00 median 6.00 | Matchbook 6.80
    DATA: model 14.3% | style Held up (led 8% of runs) | runs in data 2 | last 3: 24 Apr Perth NH Flat 16.2f Good 3/11; 29 Oct Stratford Hurdle 16.5f Good To Soft 2/9 fig 96
    DATA for: Good recent finishing positions
    DATA against: Best recent form figure 96, 7 lb below field average; Lightly raced: 2 runs in our data, so the model has little to go on
- Crookhaven (hrs_17395398797) | 5yo G | 158lb | OR - | draw 0 | jockey Jonathan Burke | trainer Olly Murphy (14d 7/45) | headgear - | last run 207 days | form 21- | MARKET 10.4% | 09:00 median 6.50 | Matchbook 10.50
    DATA: model 5.3% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 207-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Roximan (hrs_58844002) | 4yo G | 158lb | OR - | draw 0 | jockey Sam Twiston-Davies | trainer Paul Nicholls (14d 2/16) | headgear t (1st time) | last run 266 days | form 308- | MARKET 3.7% | 09:00 median 17.00 | Matchbook 36.00
    DATA: model 8.7% | style Leader (led 38% of runs) | runs in data 2 | last 3: 1 Jan Cheltenham NH Flat 16.8f Good 14/16; 26 Feb Taunton NH Flat 16.5f Good To Soft 8/12
    DATA for: First-time headgear
    DATA against: Last-run finishing speed -6.7% vs that field (faded); Returns from a 266-day break; Lightly raced: 2 runs in our data, so the model has little to go on; First run over hurdles in our data
- Bebe And Bean (hrs_47869003) | 6yo G | 158lb | OR - | draw 0 | jockey Kevin Brogan | trainer Olly Murphy (14d 7/45) | headgear t | last run 221 days | form 55/6- | MARKET 2.5% | 09:00 median 26.00 | Matchbook 48.00
    DATA: model 11.5% | style Unknown | runs in data 1 | last 3: 12 Apr Ffos Las Hurdle 15.8f Good To Soft 6/12
    DATA against: Returns from a 221-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Burk Flight (hrs_17394787599) | 4yo G | 158lb | OR - | draw 0 | jockey Robert Dunne | trainer Olly Murphy (14d 7/45) | headgear - | last run 16 days | form 5 | MARKET 1.9% | 09:00 median 34.00 | Matchbook 65.00
    DATA: model 14.2% | style Leader (led 57% of runs) | runs in data 1 | last 3: 3 Nov Lingfield NH Flat 16f Standard / Slow 5/8 fig 101
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Short Sell (hrs_62135738) | 5yo G | 158lb | OR - | draw 0 | jockey Charlie Todd | trainer Dan Skelton (14d 18/80) | headgear - | last run 17 days | form 31-898 | MARKET 1.2% | 09:00 median 46.00 | Matchbook 270.00
    DATA: model 1.9% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 14 May Fontwell NH Flat 17.7f Good 8/12; 9 Oct Chepstow Hurdle 16.1f Good To Soft 9/10; 2 Nov Southwell Hurdle 16f Good 8/14
    DATA for: Trainer 22% wins (18/80), last 14 days
    DATA against: Last-run finishing speed -2.6% vs that field (faded); Poor recent finishing positions
- Peterman (hrs_17395610526) | 6yo G | 158lb | OR - | draw 0 | jockey Kielan Woods | trainer Ian Williams (14d 0/8) | headgear - | last run - days | form - | MARKET 1.0% | 09:00 median 81.00 | Matchbook 160.00
    DATA: model 5.3% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Trainer 0 wins from 8 runs, last 14 days; Lightly raced: 0 runs in our data, so the model has little to go on
- Pixie Dust (hrs_58315985) | 5yo M | 151lb | OR - | draw 0 | jockey Nick Slatter(3) | trainer D. J. Jeffreys (14d 0/4) | headgear - | last run 256 days | form 352- | MARKET 0.9% | 09:00 median 86.00 | Matchbook 170.00
    DATA: model 4.8% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 256-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Jim Santiago Bowie (hrs_62006637) | 5yo G | 158lb | OR - | draw 0 | jockey Isabelle Ryder(5) | trainer Dominic Ffrench Davis (14d 0/0) | headgear - | last run 217 days | form 79- | MARKET 0.7% | 09:00 median 126.00 | Matchbook 200.00
    DATA: model 3.7% | style Midfield (led 8% of runs) | runs in data 2 | last 3: 26 Feb Taunton NH Flat 16.5f Good To Soft 7/12; 16 Apr Hereford NH Flat 16.2f Good 9/11
    DATA against: Last-run finishing speed -4.5% vs that field (faded); Returns from a 217-day break; Lightly raced: 2 runs in our data, so the model has little to go on; First run over hurdles in our data
- Wannabe Sporty (hrs_17392041380) | 4yo G | 158lb | OR - | draw 0 | jockey James Best | trainer Martin Keighley (14d 3/11) | headgear - | last run 43 days | form 77 | MARKET 0.7% | 09:00 median 151.00 | Matchbook 220.00
    DATA: model 4.0% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 10 Sep Worcester NH Flat 16f Good 7/8; 7 Oct Worcester Hurdle 16f Good 7/12
    DATA for: Trainer 27% wins (3/11), last 14 days
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Wet Sail (hrs_17392042423) | 4yo F | 151lb | OR - | draw 0 | jockey Tristan Durrell | trainer Dan Skelton (14d 18/80) | headgear - | last run 13 days | form 99 | MARKET 0.5% | 09:00 median 201.00 | Matchbook 400.00
    DATA: model 2.2% | style Held up (led 8% of runs) | runs in data 2 | last 3: 21 Oct Worcester Hurdle 16f Good To Soft 9/10; 6 Nov Fontwell Hurdle 17.5f Good 9/10
    DATA for: Trainer 22% wins (18/80), last 14 days
    DATA against: Last-run finishing speed -7.1% vs that field (faded); Lightly raced: 2 runs in our data, so the model has little to go on
- T R Five (hrs_60250099) | 5yo G | 158lb | OR - | draw 0 | jockey Stan Sheppard | trainer David Bridgwater (14d 0/2) | headgear - | wind surgery | last run 18 days | form 8P-8 | MARKET 0.4% | 09:00 median 201.00 | Matchbook 420.00
    DATA: model 1.8% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 7 Mar Hereford Hurdle 19.7f Good PU/12; 1 Nov Huntingdon Hurdle 16f Good 8/10
    DATA against: Last-run finishing speed -6.0% vs that field (faded); Lightly raced: 2 runs in our data, so the model has little to go on; Pulled up in 1 of its last 2 jumps runs

## 1:02 Warwick | race_id rac_32304859288 | Great British Bonus Supporting Breeders' Day Mares' Novices' Hurdle Race (GBB Race)
Hurdle | Class 4 | 2m3f | going Soft | Turf | 10 runners | rating band - | age 4yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Largy Force (hrs_29816430) | 8yo M | 154lb | OR 127 | draw 0 | jockey Sean Bowen | trainer Olly Murphy (14d 7/45) | headgear - | wind surgery | last run 189 days | form 1212-1 | MARKET 33.4% | 09:00 median 2.50 | Matchbook 2.88
    DATA: model 34.0% | style Midfield (led 4% of runs) | runs in data 4 | last 3: 26 Feb Wetherby Chase 19.4f Soft 1/8; 28 Mar Uttoxeter Chase 24f Good To Soft 2/10; 14 May Perth Chase 23.8f Good To Soft 1/6
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Returns from a 189-day break; First run over hurdles in our data; Aged 8, older than most of this field
- Capricciose (hrs_57504356) | 5yo M | 154lb | OR - | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 18/80) | headgear - | last run 21 days | form 315-3 | MARKET 30.0% | 09:00 median 2.88 | Matchbook 3.10
    DATA: model 8.4% | style Held up (led 5% of runs) | runs in data 2 | last 3: 7 Mar Sandown NH Flat 16f Soft 5/10; 29 Oct Stratford Hurdle 22f Good To Soft 3/9 fig 106
    DATA for: Trainer 22% wins (18/80), last 14 days; Last-run finishing speed +6.1% vs that field (finished strongly)
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Vrheligonne (hrs_58132795) | 5yo M | 154lb | OR - | draw 0 | jockey Ben Jones | trainer Ben Pauling (14d 4/21) | headgear - | last run 28 days | form 222-2 | MARKET 19.3% | 09:00 median 4.33 | Matchbook 5.00
    DATA: model 12.5% | style Prominent (led 29% of runs) | runs in data 3 | last 3: 7 Feb Warwick NH Flat 16f Heavy 2/8; 14 Mar Uttoxeter NH Flat 15.8f Soft 2/12; 22 Oct Ffos Las Hurdle 20f Soft 2/8 fig 110
    DATA for: Good recent finishing positions
- Emiko (hrs_50667029) | 5yo M | 154lb | OR - | draw 0 | jockey Tom Bellamy | trainer Alan King (14d 2/16) | headgear - | last run 239 days | form 55/12- | MARKET 6.9% | 09:00 median 11.00 | Matchbook 15.50
    DATA: model 13.0% | style Unknown | runs in data 1 | last 3: 25 Mar Hexham NH Flat 16.2f Soft 2/8
    DATA for: Last-run finishing speed +8.4% vs that field (finished strongly)
    DATA against: Returns from a 239-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Golden Bouquet (hrs_64522969) | 4yo F | 153lb | OR - | draw 0 | jockey Nico de Boinville | trainer Nicky Henderson (14d 3/12) | headgear - | last run 192 days | form 4 | MARKET 5.2% | 09:00 median 17.00 | Matchbook 18.50
    DATA: model 11.2% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 11 May Southwell NH Flat 15.8f Good 4/10
    DATA for: Trainer 25% wins (3/12), last 14 days; Last-run finishing speed +2.2% vs that field (finished strongly)
    DATA against: Returns from a 192-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Hollie Potter (hrs_63575029) | 5yo M | 154lb | OR - | draw 0 | jockey Sam Twiston-Davies | trainer Henry Daly (14d 0/14) | headgear - | last run 221 days | form 4- | MARKET 1.9% | 09:00 median 34.00 | Matchbook 75.00
    DATA: model 4.1% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 12 Apr Wincanton NH Flat 15.2f Good 4/5
    DATA against: Trainer 0 wins from 14 runs, last 14 days; Returns from a 221-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Farm Assured (hrs_17393007198) | 5yo M | 154lb | OR - | draw 0 | jockey Benjamin Macey(5) | trainer Samuel Drinkwater (14d 1/6) | headgear - | last run 40 days | form 1-P5 | MARKET 1.1% | 09:00 median 101.00 | Matchbook 80.00
    DATA: model 3.5% | style Unknown | runs in data 1 | last 3: 10 Oct Chepstow NH Flat 16.1f Good To Soft 5/8
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Safari (hrs_61842060) | 6yo M | 154lb | OR - | draw 0 | jockey Tabitha Worsley | trainer Nick Gifford (14d 1/5) | headgear - | last run 272 days | form 4- | MARKET 1.1% | 09:00 median 51.00 | Matchbook 180.00
    DATA: model 6.7% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 20 Feb Warwick NH Flat 16f Soft 4/8
    DATA for: Trainer 20% wins (1/5), last 14 days; Last-run finishing speed +2.8% vs that field (finished strongly)
    DATA against: Returns from a 272-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Levant Lady (hrs_17395618870) | 6yo M | 154lb | OR - | draw 0 | jockey Charlie Deutsch | trainer Venetia Williams (14d 0/4) | headgear - | last run 256 days | form PP8- | MARKET 0.9% | 09:00 median 81.00 | Matchbook 130.00
    DATA: model 5.8% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 256-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Tierbay (hrs_58686859) | 6yo M | 154lb | OR - | draw 0 | jockey Lee Edwards | trainer Claire Dyson (14d 0/0) | headgear - | last run 239 days | form 99PP- | MARKET 0.2% | 09:00 median 251.00 | Matchbook 1000.00
    DATA: model 0.9% | style Held up (led 5% of runs) | runs in data 2 | last 3: 23 Jan Doncaster Hurdle 19.4f Soft PU/13; 25 Mar Hereford Hurdle 19.7f Good PU/10
    DATA against: Returns from a 239-day break; Lightly raced: 2 runs in our data, so the model has little to go on; Pulled up in 2 of its last 2 jumps runs; Pace: steady gallop likely, hard to come from off the pace

## 1:37 Warwick | race_id rac_32304857351 | Denis O'Connell Memorial Veterans' Handicap Steeple Chase (Leg 9 Of The Stayers' Veterans' Chase Series)
Chase | Class 2 | 3m | going Soft | Turf | 8 runners | rating band 0-150 | age 9yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- The Boola Boss (hrs_22856141) | 10yo G | 144lb | OR 120 | draw 0 | jockey Jamie Brace(5) | trainer Rebecca Curtis (14d 2/5) | headgear t | last run 36 days | form 341-31 | MARKET 21.9% | 09:00 median 4.00 | Matchbook 4.40 | CHECK (skip line 3.80)
    comment: The Boola Boss arrives in cracking form, a winner last time out and again three starts back, and he has run over today's trip and going.
    DATA: model 18.5% | style Midfield (led 4% of runs) | runs in data 4 | last 3: 11 Apr Chepstow Chase 23.6f Good To Soft 1/8; 5 May Ffos Las Chase 23.8f Good 3/9; 14 Oct Ffos Las Chase 24f Soft 1/8 fig 116
    DATA for: Trainer 40% wins (2/5), last 14 days; Has won at this trip or further; Good recent finishing positions; Carries 13 lb less than average
    DATA against: Best recent form figure 116, 8 lb below field average; Official rating 120, 13 lb below field average; Race comments mention jumping mistakes in 3 of its last 4 runs
- Git Maker (hrs_22738604) | 10yo G | 156lb | OR 132 | draw 0 | jockey Gavin Sheehan | trainer Jamie Snowden (14d 7/23) | headgear b | last run 215 days | form 3P532- | MARKET 15.7% | 09:00 median 5.50 | Matchbook 6.20
    comment: Git Maker has been placed in three of his last five, including a second last time out and a third two starts back, and has run over today's trip and going, but he is winless in that spell and returns after 215 days off carrying 156 lb.
    DATA: model 15.0% | style Prominent (led 29% of runs) | runs in data 3 | last 3: 14 Feb Haydock Chase 28.4f Good To Soft 5/11; 14 Mar Uttoxeter Chase 34f Soft 3/16; 18 Apr Ayr Chase 31.8f Heavy 2/16
    DATA for: Trainer 30% wins (7/23), last 14 days; Good recent finishing positions
    DATA against: Returns from a 215-day break
- Nocte Volatus (hrs_20373927) | 11yo G | 158lb | OR 134 | draw 0 | jockey Stan Sheppard | trainer Tom Lacey (14d 4/11) | headgear t | last run 36 days | form F117-4 | MARKET 15.3% | 09:00 median 6.00 | Matchbook 6.20
    comment: The risk is a fourth last time out after a seventh, and 158 lb is a hefty burden after 36 days off.
    DATA: model 11.4% | style Held up (led 5% of runs) | runs in data 3 | last 3: 3 Jan Sandown Chase 24.2f Good 1/9; 14 Feb Ascot Chase 23.8f Good To Soft 7/11; 14 Oct Ffos Las Chase 24f Soft 4/8 fig 125
    DATA for: Trainer 36% wins (4/11), last 14 days; Has won at this trip or further
    DATA against: Recent figures 9 lb below its current mark (looks high in the weights); Pace: steady gallop likely, hard to come from off the pace
- Knappers Hill (hrs_22722602) | 10yo G | 162lb | OR 138 | draw 0 | jockey Sam Twiston-Davies | trainer Paul Nicholls (14d 2/16) | headgear - | last run 243 days | form /43PP- | MARKET 12.7% | 09:00 median 6.50 | Matchbook 8.20
    comment: The risk is a 243-day absence, with two pulled-up runs most recently and 162 lb to carry.
    DATA: model 8.3% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 7 Feb Warwick Chase 20f Heavy PU/7; 21 Mar Newbury Chase 19.9f Good To Soft PU/7
    DATA against: Returns from a 243-day break; Lightly raced: 2 runs in our data, so the model has little to go on; Pulled up in 2 of its last 2 jumps runs
- Pounding Poet (hrs_22268589) | 10yo G | 155lb | OR 131 | draw 0 | jockey Jonathan Burke | trainer Tom Lacey (14d 4/11) | headgear tv | last run 215 days | form 12531- | MARKET 12.0% | 09:00 median 7.50 | Matchbook 8.00
    comment: He has run over today's trip and going, which is the main positive.
    DATA: model 14.0% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 18 Apr Ayr Chase 24.1f Heavy 1/11
    DATA for: Trainer 36% wins (4/11), last 14 days; Last-run finishing speed +5.6% vs that field (finished strongly); Has won at this trip or further
    DATA against: Returns from a 215-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Sure Touch (hrs_23537801) | 10yo G | 153lb | OR 129 | draw 0 | jockey Sean Bowen | trainer Olly Murphy (14d 7/45) | headgear tb | last run 25 days | form -34343 | MARKET 11.4% | 09:00 median 6.50 | Matchbook 9.80
    comment: Sure Touch is consistent, finishing third last time out, with a fourth two starts back and a third three starts back, and he has run over today's trip and going. Yet he is winless in his last five and carries 153 lb off 129, so he looks more of a place type than a winner.
    DATA: model 10.4% | style Prominent (led 3% of runs) | runs in data 5 | last 3: 4 Sep Bangor-on-Dee Chase 24.1f Good 3/5; 26 Sep Market Rasen Chase 21.4f Good 4/4; 25 Oct Market Rasen Chase 21.5f Good To Soft 3/5 fig 131
    DATA for: Best recent form figure 131, 7 lb above field average; Good recent finishing positions
- Iron Bridge (hrs_24228743) | 10yo G | 162lb | OR 138 | draw 0 | jockey Jonjo O'Neill Jr. | trainer Jonjo & A.J. O'Neill (14d 6/30) | headgear p | last run 36 days | form P231-P | MARKET 7.2% | 09:00 median 12.00 | Matchbook 14.00
    comment: The main risk is that he was pulled up last time out, 36 days ago, and he carries 162 lb.
    DATA: model 15.6% | style Prominent (led 4% of runs) | runs in data 5 | last 3: 22 Mar Exeter Chase 30.7f Good 3/6; 15 Apr Haydock Chase 25.6f Good 1/7; 14 Oct Ffos Las Chase 24f Soft PU/8
    DATA for: Trainer 20% wins (6/30), last 14 days; Has won at this trip or further
    DATA against: Race comments mention jumping mistakes in 4 of its last 5 runs; Pulled up in 2 of its last 5 jumps runs
- Hang In There (hrs_14995512) | 12yo G | 168lb | OR 144 | draw 0 | jockey Ben Jones | trainer Emma Lavelle (14d 3/14) | headgear - | last run 26 days | form 34-4P0 | MARKET 3.9% | 09:00 median 23.00 | Matchbook 25.00
    DATA: model 6.8% | style Held up (led 3% of runs) | runs in data 5 | last 3: 4 May Fakenham Chase 24.2f Good 4/7; 28 Jun Uttoxeter Chase 24f Good PU/13; 24 Oct Cheltenham Hurdle 24f Good 15/19
    DATA for: Official rating 144, 11 lb above field average; Trainer 21% wins (3/14), last 14 days
    DATA against: Carries 11 lb more than average; Race comments mention jumping mistakes in 2 of its last 5 runs; Pulled up in 1 of its last 5 jumps runs; Pace: steady gallop likely, hard to come from off the pace

## 2:12 Warwick | race_id rac_32304855414 | Omoda And Jaecoo Race To Victory Mares' Handicap Hurdle Race (Challenger Mares' Hurdle Series Qualifier)
Hurdle | Class 3 | 2m5f5y | going Soft | Turf | 9 runners | rating band 0-125 | age 4yo+
DATA pace: Even - Two likely leaders (Betty's Daisy, Analiese). A fair, even gallop is most likely.
- Strong Run (hrs_46169683) | 7yo M | 165lb | OR 117 | draw 0 | jockey Kielan Woods | trainer Fergal O'Brien (14d 3/27) | headgear t | last run 23 days | form 1261-U | MARKET 19.9% | 09:00 median 4.50 | Matchbook 4.70 | CHECK (skip line 4.27)
    comment: In her favour, she was a winner two starts back, and has run over today's trip and going.
    DATA: model 14.4% | style Prominent (led 23% of runs) | runs in data 4 | last 3: 21 Mar Newbury Hurdle 20.5f Good To Soft 6/15; 24 Apr Fontwell Hurdle 21.7f Good 1/7; 27 Oct Bangor-on-Dee Chase 20.5f Good To Soft UR/13
    DATA for: Has won at this trip or further
    DATA against: Race comments mention jumping mistakes in 2 of its last 4 runs; Fell or unseated in 1 of its last 4 jumps runs
- Analiese (hrs_48644680) | 5yo M | 168lb | OR 120 | draw 0 | jockey Charlie Deutsch | trainer Mel Rowley (14d 1/8) | headgear - | last run 218 days | form 11214- | MARKET 14.5% | 09:00 median 6.00 | Matchbook 6.60
    comment: The main risk is a 218-day absence, with 168 lb to carry.
    DATA: model 20.6% | style Leader (led 38% of runs) | runs in data 3 | last 3: 28 Feb Newbury Hurdle 20.5f Good To Soft 2/9; 15 Mar Chepstow Hurdle 19.5f Soft 1/9; 15 Apr Haydock Hurdle 21.2f Good 4/11
    DATA for: Official rating 120, 6 lb above field average; Good recent finishing positions
    DATA against: Carries 6 lb more than average; Returns from a 218-day break
- Crystal Spring (hrs_46547172) | 5yo M | 154lb | OR 106 | draw 0 | jockey Charlie Hammond | trainer Stuart Edmunds (14d 1/8) | headgear p (1st time) | last run 23 days | form 3126-7 | MARKET 13.5% | 09:00 median 6.50 | Matchbook 7.00
    comment: Crystal Spring has tailed off with a seventh last time out and a sixth the start before, so it is hard to fancy her, though a win four starts back and a second three starts back show she can do better.
    DATA: model 10.0% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 27 Oct Bangor-on-Dee Hurdle 19.5f Good 7/10 fig 98
    DATA for: Carries 8 lb less than average; First-time headgear
    DATA against: Recent figures 8 lb below its current mark (looks high in the weights); Official rating 106, 8 lb below field average; Lightly raced: 1 run in our data, so the model has little to go on
- Miss Cynthia (hrs_31880758) | 6yo M | 161lb | OR 113 | draw 0 | jockey Miss Heidi Palin(5) | trainer Dan Skelton (14d 18/80) | headgear p | wind surgery | last run 40 days | form /710-3 | MARKET 12.6% | 09:00 median 6.50 | Matchbook 8.20
    comment: Miss Cynthia bounced back with a third last time out, and she's a winner three starts back who has run over today's trip and going before.
    DATA: model 11.9% | style Held up (led 4% of runs) | runs in data 3 | last 3: 18 Jan Fakenham Hurdle 20f Good To Soft 1/7; 27 Mar Wetherby Hurdle 21.3f Good 11/16; 10 Oct Chepstow Hurdle 19.5f Good To Soft 3/9
    DATA for: Trainer 22% wins (18/80), last 14 days; Good recent finishing positions
- Easy To Follow (hrs_33479005) | 8yo M | 156lb | OR 108 | draw 0 | jockey Sean Bowen | trainer Olly Murphy (14d 7/45) | headgear - | last run 189 days | form /24P-2 | MARKET 10.9% | 09:00 median 7.50 | Matchbook 9.20
    comment: Easy To Follow was second last time out and a fourth three starts back, but she was pulled up in between and has been off for 189 days, while carrying 156 lb.
    DATA: model 6.8% | style Held up (led 8% of runs) | runs in data 2 | last 3: 22 Jan Huntingdon Chase 23.6f Soft PU/4; 14 May Perth Hurdle 20.2f Good To Soft 2/5
    DATA for: Carries 6 lb less than average
    DATA against: Official rating 108, 6 lb below field average; Returns from a 189-day break; Lightly raced: 2 runs in our data, so the model has little to go on; Pulled up in 1 of its last 2 jumps runs
- I Spy A Diva (hrs_24638789) | 9yo M | 162lb | OR 114 | draw 0 | jockey Tom Bellamy | trainer Kim Bailey & Mat Nicholls (14d 1/10) | headgear - | last run 23 days | form 6843-5 | MARKET 10.6% | 09:00 median 8.50 | Matchbook 8.80
    DATA: model 9.4% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 1 Jan Windsor Hurdle 20f Good 3/8; 27 Oct Bangor-on-Dee Hurdle 19.5f Good 5/10 fig 108
    DATA against: Recent figures 6 lb below its current mark (looks high in the weights); Lightly raced: 2 runs in our data, so the model has little to go on; Aged 9, older than most of this field
- Party Vibes (hrs_34571411) | 8yo M | 164lb | OR 116 | draw 0 | jockey Sam Twiston-Davies | trainer Henry Daly (14d 0/14) | headgear - | last run 201 days | form 1P51-5 | MARKET 7.9% | 09:00 median 11.00 | Matchbook 12.50
    DATA: model 11.4% | style Midfield (led 4% of runs) | runs in data 4 | last 3: 18 Feb Ludlow Chase 20.1f Soft 5/8; 6 Apr Hereford Chase 20.9f Good 1/4; 2 May Uttoxeter Chase 24f Good 5/6
    DATA for: Has won at this trip or further
    DATA against: Trainer 0 wins from 14 runs, last 14 days; Last-run finishing speed -9.1% vs that field (faded); Returns from a 201-day break; Pulled up in 1 of its last 4 jumps runs
- Betty's Daisy (hrs_49174223) | 6yo M | 168lb | OR 120 | draw 0 | jockey Ben Jones | trainer Ben Pauling (14d 4/21) | headgear tp (1st time) | wind surgery | last run 23 days | form 812P-0 | MARKET 7.0% | 09:00 median 12.00 | Matchbook 14.50
    comment: Betty's Daisy won four starts back and was a second three starts back, but she was pulled up two starts back and unplaced last time, so the form has tailed off.
    DATA: model 8.6% | style Leader (led 72% of runs) | runs in data 3 | last 3: 23 Jan Warwick Hurdle 19f Good To Soft 2/16; 21 Mar Newbury Hurdle 20.5f Good To Soft PU/15; 27 Oct Bangor-on-Dee Hurdle 19.5f Good 10/10
    DATA for: Official rating 120, 6 lb above field average; First-time headgear
    DATA against: Last-run finishing speed -4.2% vs that field (faded); Carries 6 lb more than average; Pulled up in 1 of its last 3 jumps runs
- Shallow Bowles (hrs_51650095) | 6yo M | 156lb | OR 108 | draw 0 | jockey Mr Daniel Williams(7) | trainer Nick Scholfield (14d 0/13) | headgear t (1st time) | last run 282 days | form 4846- | MARKET 3.2% | 09:00 median 23.00 | Matchbook 34.00
    comment: Winless in her last four, Shallow Bowles was sixth last time out, with a fourth and an eighth before that, and she returns after 282 days off.
    DATA: model 6.9% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 29 Jan Thurles Hurdle 15.8f Heavy 4/18; 10 Feb Limerick Hurdle 15.7f Heavy 6/11
    DATA for: Carries 6 lb less than average; First-time headgear
    DATA against: Official rating 108, 6 lb below field average; Trainer 0 wins from 13 runs, last 14 days; Returns from a 282-day break; Lightly raced: 2 runs in our data, so the model has little to go on

## 2:47 Warwick | race_id rac_32304861225 | Grumpy & Granny's Golden Gallops Mares' Handicap Steeple Chase (Challenger Mares' Chase Series Qualifier) (GBB Race)
Chase | Class 4 | 2m4f | going Soft | Turf | 7 runners | rating band 0-120 | age 4yo+
DATA pace: Lone leader - Hard Dealt is the only habitual front-runner and may be allowed an easy lead.
- Coolanna (hrs_41052802) | 6yo M | 168lb | OR 119 | draw 0 | jockey Tom Bellamy | trainer Kim Bailey & Mat Nicholls (14d 1/10) | headgear t | last run 264 days | form 2/114- | MARKET 20.4% | 09:00 median 4.00 | Matchbook 5.00 | CHECK (skip line 3.80)
    comment: The one big risk is a 264-day absence, with 168 lb on her back too.
    DATA: model 24.7% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 29 Jan Wincanton Hurdle 21.4f Heavy 1/11; 28 Feb Doncaster Hurdle 24.4f Soft 4/8
    DATA for: Official rating 119, 7 lb above field average; Has won at this trip or further
    DATA against: Carries 9 lb more than average; Returns from a 264-day break; Lightly raced: 2 runs in our data, so the model has little to go on; First run over fences in our data
- Indannya (hrs_51090928) | 5yo M | 165lb | OR 116 | draw 0 | jockey Lorcan Williams | trainer Chester Williams (14d 0/4) | headgear - | last run 243 days | form 31819- | MARKET 17.9% | 09:00 median 5.05 | Matchbook 5.20
    comment: A ninth last time and 243 days off are the reservations, but 165 lb is manageable off 116.
    DATA: model 18.7% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 7 Feb Warwick Hurdle 19f Heavy 8/9; 5 Mar Wincanton Hurdle 15.2f Good To Soft 1/13; 21 Mar Newbury Hurdle 20.5f Good To Soft 9/15
    DATA against: Last-run finishing speed -8.4% vs that field (faded); Carries 6 lb more than average; Returns from a 243-day break; First run over fences in our data
- Zahra Dodville (hrs_51766428) | 4yo F | 153lb | OR 113 | draw 0 | jockey Jonathan Burke | trainer James Owen (14d 3/28) | headgear - | wind surgery | last run 113 days | form 513-20 | MARKET 16.9% | 09:00 median 5.00 | Matchbook 5.80
    comment: Zahra Dodville has been in the frame in two of her last three before an unplaced latest, having finished second two starts back and third three starts back, and she has run on today's going before.
    DATA: model 15.0% | style Prominent (led 8% of runs) | runs in data 2 | last 3: 23 May Cartmel Hurdle 17.2f Good 2/10; 29 Jul Galway Hurdle 16.5f Good 12/20
    DATA for: Carries 6 lb less than average
    DATA against: Returns from a 113-day break; Lightly raced: 2 runs in our data, so the model has little to go on; First run over fences in our data
- Broomfield Aderra (hrs_39959633) | 6yo M | 164lb | OR 115 | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 18/80) | headgear p (1st time) | last run 18 days | form 351-58 | MARKET 14.4% | 09:00 median 6.30 | Matchbook 6.40
    comment: Broomfield Aderra has run over today's trip and on this going, and she won three starts back, with a third five runs ago too.
    DATA: model 13.2% | style Midfield (led 4% of runs) | runs in data 4 | last 3: 27 Mar Fontwell Hurdle 21.7f Good To Soft 1/3; 12 Oct Worcester Chase 20f Good To Soft 5/7; 1 Nov Worcester Chase 20f Good To Soft 8/13 fig 106
    DATA for: Trainer 22% wins (18/80), last 14 days; Has won at this trip or further; First-time headgear
    DATA against: Recent figures 9 lb below its current mark (looks high in the weights)
- Hard Dealt (hrs_41052578) | 6yo M | 162lb | OR 113 | draw 0 | jockey Sam Twiston-Davies | trainer Henry Daly (14d 0/14) | headgear - | last run 23 days | form 7224-5 | MARKET 13.9% | 09:00 median 6.00 | Matchbook 7.00
    comment: Fifth last time out and a fourth two starts back, Hard Dealt has been in the frame's vicinity without a win in her last five, though two seconds before that show she's competitive.
    DATA: model 13.1% | style Leader (led 23% of runs) | runs in data 5 | last 3: 29 Mar Ascot Hurdle 23.6f Good 2/8; 23 Apr Warwick Hurdle 21f Good 4/10; 27 Oct Bangor-on-Dee Hurdle 23f Good 5/9 fig 110
    DATA for: Best recent form figure 110, 7 lb above field average; Pace: may get an uncontested lead
    DATA against: Trainer 0 wins from 14 runs, last 14 days; First run over fences in our data
- Presenting Doy (hrs_37790382) | 7yo M | 158lb | OR 109 | draw 0 | jockey Harry Cobden | trainer Emma Lavelle (14d 3/14) | headgear - | wind surgery | last run 222 days | form 2/P95- | MARKET 10.9% | 09:00 median 8.00 | Matchbook 8.80
    comment: Winless in her last four and absent for 222 days, Presenting Doy is hard to fancy after a fifth last time out, a ninth two starts back and a pulled up before that, though a second four starts back shows some ability.
    DATA: model 9.8% | style Held up (led 5% of runs) | runs in data 2 | last 3: 17 Feb Market Rasen Hurdle 20.6f Soft 9/12; 11 Apr Chepstow Hurdle 23.6f Good To Soft 5/6
    DATA for: Trainer 21% wins (3/14), last 14 days
    DATA against: Last-run finishing speed -3.9% vs that field (faded); Returns from a 222-day break; Lightly raced: 2 runs in our data, so the model has little to go on; First run over fences in our data
- Where's Cato (hrs_39827298) | 7yo M | 146lb | OR 97 | draw 0 | jockey Adam Wedge | trainer Mrs C. Williams (14d 1/24) | headgear - | last run 31 days | form 123-54 | MARKET 5.6% | 09:00 median 15.00 | Matchbook 19.50
    comment: Where's Cato has tailed off since winning five starts back, finishing second, third, fifth, then fourth last time, and a yard-stick trainer on 1/24 lately doesn't help under 146 lb.
    DATA: model 5.5% | style Prominent (led 3% of runs) | runs in data 5 | last 3: 13 Mar Fakenham Chase 21.2f Good To Soft 3/4; 10 Oct Chepstow Hurdle 19.5f Good To Soft 5/9; 19 Oct Plumpton Hurdle 25f Good 4/5 fig 92
    DATA for: Has won at this trip or further; Carries 13 lb less than average
    DATA against: Best recent form figure 92, 11 lb below field average; Official rating 97, 15 lb below field average

## 3:17 Warwick | race_id rac_32304863162 | Thoroughbred Breeders' Association Supporting Breeders' Day Mares' Open National Hunt Flat Race (Category 1 Elimination) (GBB Race)
NH Flat | Class 5 | 2m | going Soft | Turf | 16 runners | rating band - | age 4-5yo
DATA pace: Unclear - Running styles known for only 2 of 16 runners.
- Ellie Marie (hrs_17395617827) | 5yo M | 156lb | OR - | draw 0 | jockey Sam Twiston-Davies | trainer Paul Nicholls (14d 2/16) | headgear - | last run 571 days | form 2/ | MARKET 15.3% | 09:00 median 5.00 | Matchbook 5.90 | CHECK (skip line 4.75)
    comment: Ellie Marie is unexposed, with a second last time out her only recent form, though she returns after 571 days off and carries 156 lb. Yet to win in that sole start, she may have more to offer.
    DATA: model 6.1% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 571-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Olive Noir (hrs_17395174552) | 4yo F | 156lb | OR - | draw 0 | jockey Ben Jones | trainer Ben Pauling (14d 4/21) | headgear - | last run - days | form - | MARKET 14.4% | 09:00 median 5.50 | Matchbook 6.40
    comment: Olive Noir is unraced, so she's a pure debut proposition and an unknown quantity, carrying 156 lb.
    DATA: model 6.1% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Galant Jewel (hrs_17395625128) | 4yo F | 156lb | OR - | draw 0 | jockey Sean Bowen | trainer Olly Murphy (14d 7/45) | headgear - | last run 179 days | form 51 | MARKET 11.1% | 09:00 median 7.00 | Matchbook 8.20
    comment: Unexposed filly who won last time out and was a fifth two starts back, so there's likely more to come, though she returns after 179 days off and carries 156 lb.
    DATA: model 6.1% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 179-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Elodie Bijou (hrs_17395169337) | 4yo F | 156lb | OR - | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 18/80) | headgear - | last run - days | form - | MARKET 11.1% | 09:00 median 7.50 | Matchbook 7.80
    comment: Elodie Bijou is unraced, so she's a completely unexposed filly with no form to judge and plenty of scope to improve.
    DATA: model 6.1% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 22% wins (18/80), last 14 days
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Kells Bay (hrs_17395393582) | 4yo F | 156lb | OR - | draw 0 | jockey Jonathan Burke | trainer Nick Scholfield (14d 0/13) | headgear - | last run 235 days | form 1- | MARKET 7.8% | 09:00 median 8.00 | Matchbook 15.00
    comment: Kells Bay won her only recent start, but that came 235 days ago, so she returns after a long break; she is unexposed and open to improvement, though top weight of 156 lb is a notable burden.
    DATA: model 6.1% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Trainer 0 wins from 13 runs, last 14 days; Returns from a 235-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Fiercestone (hrs_17395624085) | 5yo M | 156lb | OR - | draw 0 | jockey Harry Cobden | trainer Emma Lavelle (14d 3/14) | headgear - | last run 193 days | form 2-1 | MARKET 7.8% | 09:00 median 10.00 | Matchbook 12.00
    comment: Unexposed mare who won last time out, with a second two starts back, so the recent form is progressive. She returns after 193 days off and carries 156 lb, but she looks open to further improvement.
    DATA: model 6.1% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 21% wins (3/14), last 14 days
    DATA against: Returns from a 193-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Mighty Harmony (hrs_64522948) | 4yo F | 156lb | OR - | draw 0 | jockey Stan Sheppard | trainer Henry Daly (14d 0/14) | headgear - | last run 192 days | form 4 | MARKET 6.0% | 09:00 median 13.00 | Matchbook 15.50
    comment: The main risk is fitness, as she returns after 192 days off.
    DATA: model 6.9% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 11 May Southwell NH Flat 15.8f Good 4/10
    DATA for: Last-run finishing speed +8.5% vs that field (finished strongly)
    DATA against: Trainer 0 wins from 14 runs, last 14 days; Returns from a 192-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Autumn In Sonora (hrs_17395411313) | 4yo F | 156lb | OR - | draw 0 | jockey Charlie Hammond | trainer Stuart Edmunds (14d 1/8) | headgear - | wind surgery | last run - days | form - | MARKET 5.7% | 09:00 median 12.00 | Matchbook 18.50
    comment: Autumn In Sonora is an unraced filly with no form to assess, so she is a blank canvas and open to plenty of improvement.
    DATA: model 6.1% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Agreymiracleseeker (hrs_63323582) | 4yo F | 156lb | OR - | draw 0 | jockey Tom Bellamy | trainer Alan King (14d 2/16) | headgear - | last run 192 days | form 6-3 | MARKET 4.6% | 09:00 median 17.00 | Matchbook 19.50
    DATA: model 7.6% | style Held up (led 5% of runs) | runs in data 2 | last 3: 4 Apr Newton Abbot NH Flat 16.8f Good 6/12; 11 May Southwell NH Flat 15.8f Good 3/10
    DATA for: Last-run finishing speed +5.4% vs that field (finished strongly)
    DATA against: Returns from a 192-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- Bellabelini (hrs_17395620956) | 5yo M | 156lb | OR - | draw 0 | jockey Kielan Woods | trainer Fergal O'Brien (14d 3/27) | headgear - | last run - days | form - | MARKET 4.0% | 09:00 median 21.00 | Matchbook 22.00
    comment: Bellabelini is unraced, so she's an unexposed sort with plenty of scope to improve, and she lines up with no form to lean on. She carries 156 lb on debut, so her first public effort should reveal plenty.
    DATA: model 6.1% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Molly Hastings (hrs_61842067) | 5yo M | 156lb | OR - | draw 0 | jockey Caoilin Quinn | trainer Tom Symonds (14d 0/10) | headgear h (1st time) | last run - days | form - | MARKET 2.9% | 09:00 median 26.00 | Matchbook 36.00
    comment: Molly Hastings is unexposed on her debut, with no form to go on, so she's open to any amount of improvement. She carries 156 lb, and it's a case of seeing what she shows first time out.
    DATA: model 6.1% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: First-time headgear
    DATA against: Trainer 0 wins from 10 runs, last 14 days; Lightly raced: 0 runs in our data, so the model has little to go on
- Miss Spec (hrs_17394533107) | 5yo M | 156lb | OR - | draw 0 | jockey Fern O'Brien(5) | trainer Fergal O'Brien (14d 3/27) | headgear - | last run 22 days | form 1-4 | MARKET 2.7% | 09:00 median 23.00 | Matchbook 48.00
    DATA: model 5.7% | style Unknown | runs in data 1 | last 3: 28 Oct Newton Abbot NH Flat 17f Good To Soft 4/7 fig 86
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Rosa Villosa (hrs_62645562) | 4yo F | 156lb | OR - | draw 0 | jockey Cameron Johnstone-Baker(7) | trainer Emma Lavelle (14d 3/14) | headgear - | last run - days | form - | MARKET 2.3% | 09:00 median 41.00 | Matchbook 40.00
    comment: Rosa Villosa is an unraced filly with no form to assess, so she's very much an unknown quantity and open to plenty of improvement. She carries 156 lb on debut, and her first outing should reveal plenty.
    DATA: model 6.1% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 21% wins (3/14), last 14 days
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Eliza Williams (hrs_17395623042) | 4yo F | 156lb | OR - | draw 0 | jockey Charlie Deutsch | trainer Mel Rowley (14d 1/8) | headgear - | last run - days | form - | MARKET 1.8% | 09:00 median 41.00 | Matchbook 70.00
    comment: Unraced and open to improvement, this filly has no recorded form to go on, so she remains an unexposed type. She carries 156 lb on her debut, and her first run should reveal plenty.
    DATA: model 6.1% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Magna Ruby (hrs_17395629300) | 5yo M | 156lb | OR - | draw 0 | jockey Ciaran Gethings | trainer Alastair Ralph (14d 0/5) | headgear - | last run - days | form - | MARKET 1.5% | 09:00 median 41.00 | Matchbook 110.00
    comment: Unraced and with no form to go on, Magna Ruby is a blank canvas who looks open to improvement. She carries 156 lb on debut, and her unexposed profile means there is plenty still to learn.
    DATA: model 6.1% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Sparkswillfly (hrs_17395632429) | 4yo F | 156lb | OR - | draw 0 | jockey Isabelle Ryder(5) | trainer Barry Brennan (14d 0/2) | headgear - | last run - days | form - | MARKET 0.9% | 09:00 median 81.00 | Matchbook 140.00
    comment: Sparkswillfly is an unexposed filly with no recorded form to go on, so she arrives open to improvement on her debut. She carries 156 lb, and a first run will reveal plenty about where she stands.
    DATA: model 6.1% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
