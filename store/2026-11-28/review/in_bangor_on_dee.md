# Card review packet: Bangor-on-Dee, 2026-11-28

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


## 11:50 Bangor-on-Dee | race_id rac_32305905268 | Hope House Children's Hospices Conditional Jockeys' Training Series Handicap Hurdle Race (Part Of The Racing Excellence Series)
Hurdle | Class 5 | 2m7f32y | going Good To Soft | Turf | 7 runners | rating band 0-100 | age 4yo+
DATA pace: Even - Two likely leaders (Clondaw Royale, Malinas Glory). A fair, even gallop is most likely.
- Cahier's Den (hrs_40095650) | 6yo G | 166lb | OR 98 | draw 0 | jockey Harry Brown(6) | trainer Donald McCain (14d 2/25) | headgear - | wind surgery | last run 32 days | form 432-67 | MARKET 33.7% | 09:00 median 2.63 | Matchbook 2.82
    comment: Cahier's Den was a seventh last time out and a sixth the start before, though he was second three starts back, and he has run over today's trip. Yet to win in his last five, he carries 166 lb off a mark of 98 after 32 days off.
    DATA: model 20.7% | style Midfield (led 4% of runs) | runs in data 5 | last 3: 31 Mar Newcastle Chase 23.4f Good To Soft 2/6; 16 May Bangor-on-Dee Chase 24.1f Good 6/10; 27 Oct Bangor-on-Dee Chase 24f Good To Soft 7/13 fig 93
    DATA for: Best recent form figure 93, 4 lb above field average; Official rating 98, 5 lb above field average
    DATA against: Carries 5 lb more than average; Race comments mention jumping mistakes in 2 of its last 5 runs; First run over hurdles in our data
- Cool Master (hrs_59150581) | 5yo G | 151lb | OR 83 | draw 0 | jockey Ben Smith(3) | trainer Oliver Greenall & Josh Guerriero (14d 4/18) | headgear p | last run 19 days | form 949-04 | MARKET 18.3% | 09:00 median 4.50 | Matchbook 5.60
    comment: Cool Master is winless in his last five, with a fourth last time out his best finish in that run and a ninth and unplaced effort before it, so he is hard to fancy.
    DATA: model 9.5% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 24 Mar Southwell Hurdle 20.4f Good 9/12; 21 Oct Worcester Hurdle 20f Good To Soft 10/10; 9 Nov Carlisle Hurdle 19.5f Good To Soft 4/10 fig 83
    DATA for: Trainer 22% wins (4/18), last 14 days; Carries 10 lb less than average
    DATA against: Best recent form figure 83, 6 lb below field average; Official rating 83, 10 lb below field average
- Eaststone Buck's (hrs_50187830) | 5yo G | 145lb | OR 77 | draw 0 | jockey Cian Murphy(5) | trainer Venetia Williams (14d 0/11) | headgear - | last run 221 days | form /6920- | MARKET 17.8% | 09:00 median 5.00 | Matchbook 5.30
    comment: Eaststone Buck's is hard to fancy after 221 days off and an unplaced run last time out, and he is winless in his last four starts.
    DATA: model 12.1% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 8 Jan Ffos Las Hurdle 20f Heavy 9/12; 9 Mar Stratford Hurdle 22f Soft 2/9; 21 Apr Ffos Las Hurdle 23.9f Good 10/12
    DATA for: Carries 16 lb less than average
    DATA against: Official rating 77, 16 lb below field average; Trainer 0 wins from 11 runs, last 14 days; Last-run finishing speed -3.4% vs that field (faded); Returns from a 221-day break
- Malinas Glory (hrs_24228806) | 9yo G | 164lb | OR 96 | draw 0 | jockey Jack Stenhouse(3) | trainer Alastair Ralph (14d 0/5) | headgear t | last run 33 days | form 11-D52 | MARKET 10.9% | 09:00 median 7.50 | Matchbook 9.60
    comment: Malinas Glory returns after 33 days having finished second last time out, and he has won twice in his last five starts, a first four starts back and another five starts back.
    DATA: model 20.6% | style Leader (led 72% of runs) | runs in data 3 | last 3: 9 May Warwick Chase 24f Good 1/4; 22 Sep Warwick Chase 20f Good To Firm 5/6; 26 Oct Hereford Hurdle 25.5f Good To Firm 2/8 fig 94
    DATA for: Best recent form figure 94, 5 lb above field average; Has won at this trip or further; Good recent finishing positions
- Clondaw Royale (hrs_34665274) | 7yo G | 167lb | OR 99 | draw 0 | jockey Richard Upton(5) | trainer Jonjo & A.J. O'Neill (14d 4/33) | headgear - | last run 20 days | form 13P-68 | MARKET 8.0% | 09:00 median 11.00 | Matchbook 13.00
    DATA: model 11.2% | style Leader (led 38% of runs) | runs in data 5 | last 3: 26 Mar Chepstow Hurdle 23.6f Good To Soft PU/15; 21 Oct Worcester Hurdle 20f Good To Soft 6/8 fig 86; 8 Nov Ffos Las Hurdle 24f Soft 8/11
    DATA for: Official rating 99, 6 lb above field average; Has won at this trip or further
    DATA against: Recent figures 13 lb below its current mark (looks high in the weights); Poor recent finishing positions; Carries 6 lb more than average; Pulled up in 1 of its last 5 jumps runs
- Exmoor Forest (hrs_28518245) | 9yo G | 168lb | OR 100 | draw 0 | jockey James Robottom(5) | trainer Nigel Hawke (14d 1/10) | headgear p | last run 491 days | form 333/9- | MARKET 5.7% | 09:00 median 15.00 | Matchbook 18.00
    DATA: model 13.7% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Official rating 100, 7 lb above field average
    DATA against: Carries 7 lb more than average; Returns from a 491-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Rehill Relic (hrs_35232106) | 7yo G | 164lb | OR 96 | draw 0 | jockey Troy Walsh(5) | trainer Sam Allwood (14d 1/4) | headgear p | last run 21 days | form 413F-8 | MARKET 5.6% | 09:00 median 16.50 | Matchbook 17.00
    comment: Rehill Relic arrives 21 days after an eighth last time out, with a faller two starts back blotting a record that includes a third three starts back and a win four starts back.
    DATA: model 12.2% | style Held up (led 5% of runs) | runs in data 3 | last 3: 25 Jan Sedgefield Chase 19.3f Good To Soft 3/5; 27 Feb Doncaster Chase 19.1f Good To Soft F/5; 7 Nov Uttoxeter Hurdle 23.5f Good 8/9
    DATA against: Fell or unseated in 1 of its last 3 jumps runs

## 12:25 Bangor-on-Dee | race_id rac_32305907205 | Wrexham Lager Maiden Hurdle Race (GBB Race)
Hurdle | Class 4 | 2m3f123y | going Good To Soft | Turf | 12 runners | rating band - | age 4yo+
DATA pace: Lone leader - Pointofdifference is the only habitual front-runner and may be allowed an easy lead.
- Pointofdifference (hrs_17394099219) | 5yo G | 158lb | OR - | draw 0 | jockey Jamie Brace(5) | trainer Rebecca Curtis (14d 0/10) | headgear - | last run 37 days | form 11-1 | MARKET 51.7% | 09:00 median 1.57 | Matchbook 1.68
    DATA: model 29.1% | style Leader (led 57% of runs) | runs in data 1 | last 3: 22 Oct Ffos Las NH Flat 16f Soft 1/6 fig 108
    DATA for: Best recent form figure 108, 9 lb above field average; Last-run finishing speed +4.3% vs that field (finished strongly); Pace: may get an uncontested lead
    DATA against: Trainer 0 wins from 10 runs, last 14 days; Lightly raced: 1 run in our data, so the model has little to go on
- Cool Customer (hrs_51124332) | 5yo G | 158lb | OR - | draw 0 | jockey Fern O'Brien(5) | trainer Fergal O'Brien (14d 5/28) | headgear - | last run 24 days | form /231-3 | MARKET 27.1% | 09:00 median 2.50 | Matchbook 3.85
    DATA: model 23.2% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 12 Jan Hereford NH Flat 16.2f Soft 3/10; 15 Mar Chepstow NH Flat 16.1f Soft 1/8; 4 Nov Chepstow Hurdle 19.5f Good To Soft 3/14 fig 101
    DATA for: Last-run finishing speed +5.7% vs that field (finished strongly); Good recent finishing positions
- Koaly Play (hrs_17395279895) | 4yo G | 157lb | OR - | draw 0 | jockey Toby Wynne | trainer Oliver Greenall & Josh Guerriero (14d 4/18) | headgear t (1st time) | last run 265 days | form 1- | MARKET 10.6% | 09:00 median 6.00 | Matchbook 11.00
    DATA: model 4.9% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 22% wins (4/18), last 14 days; First-time headgear
    DATA against: Returns from a 265-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Ballyteige (hrs_17394661396) | 5yo G | 158lb | OR - | draw 0 | jockey Toby McCain-Mitchell(3) | trainer Sam Allwood (14d 1/4) | headgear - | last run 27 days | form 1-6 | MARKET 2.4% | 09:00 median 26.00 | Matchbook 48.00
    DATA: model 5.1% | style Unknown | runs in data 1 | last 3: 1 Nov Carlisle Hurdle 20f Good To Soft 6/8 fig 91
    DATA against: Best recent form figure 91, 8 lb below field average; Lightly raced: 1 run in our data, so the model has little to go on
- Emral Bridge (hrs_63171570) | 4yo G | 157lb | OR - | draw 0 | jockey Craig Nichol | trainer Oliver Greenall & Josh Guerriero (14d 4/18) | headgear - | last run 32 days | form 5-7 | MARKET 2.2% | 09:00 median 29.00 | Matchbook 55.00
    DATA: model 6.6% | style Held up (led 5% of runs) | runs in data 2 | last 3: 18 Apr Bangor-on-Dee NH Flat 16.7f Good 5/11; 27 Oct Bangor-on-Dee Hurdle 16.5f Good 7/11 fig 102
    DATA for: Trainer 22% wins (4/18), last 14 days
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Blackswan d'Oroux (hrs_60250113) | 5yo G | 158lb | OR - | draw 0 | jockey Liam Harrison | trainer Dan Skelton (14d 27/97) | headgear - | last run 19 days | form 8-5 | MARKET 2.2% | 09:00 median 26.00 | Matchbook 60.00
    DATA: model 13.9% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 9 Jan Exeter NH Flat 16.7f Good To Soft 8/11; 9 Nov Stratford Hurdle 16.5f Good To Soft 5/12 fig 97
    DATA for: Trainer 28% wins (27/97), last 14 days
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Goliath Flight (hrs_62361215) | 4yo G | 157lb | OR - | draw 0 | jockey Robert Dunne | trainer Dan Skelton (14d 27/97) | headgear - | last run 37 days | form 5-76 | MARKET 1.2% | 09:00 median 51.00 | Matchbook 100.00
    DATA: model 3.1% | style Held up (led 4% of runs) | runs in data 3 | last 3: 9 Mar Stratford NH Flat 16.3f Soft 5/7; 9 Oct Chepstow Hurdle 16.1f Good To Soft 7/10; 22 Oct Ffos Las Hurdle 16f Soft 6/11 fig 98
    DATA for: Trainer 28% wins (27/97), last 14 days
- Britway Belle (hrs_51341570) | 5yo M | 151lb | OR - | draw 0 | jockey David Noonan | trainer Henry Oliver (14d 0/3) | headgear - | wind surgery | last run 14 days | form 733-55 | MARKET 1.0% | 09:00 median 59.00 | Matchbook 160.00
    DATA: model 6.8% | style Held up (led 3% of runs) | runs in data 5 | last 3: 22 Apr Ludlow NH Flat 15.8f Good 3/14; 24 May Uttoxeter Hurdle 19.9f Good 5/7; 14 Nov Uttoxeter Hurdle 20f Good 5/7 fig 96
- Menasha (hrs_17395109886) | 4yo G | 157lb | OR - | draw 0 | jockey Oscar Palmer(7) | trainer Henry Oliver (14d 0/3) | headgear - | last run 14 days | form 2-0 | MARKET 0.8% | 09:00 median 81.00 | Matchbook 260.00
    DATA: model 2.6% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 14 Nov Uttoxeter NH Flat 16f Good 11/12
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Georgie Simmons (hrs_17394673912) | 6yo G | 158lb | OR - | draw 0 | jockey Jack Power(5) | trainer Simon Edwards (14d 0/0) | headgear - | last run 25 days | form 6/5 | MARKET 0.4% | 09:00 median 185.50 | Matchbook 340.00
    DATA: model 1.4% | style Held up (led 8% of runs) | runs in data 1 | last 3: 3 Nov Warwick Hurdle 19f Good 5/6
    DATA against: Last-run finishing speed -5.3% vs that field (faded); Lightly raced: 1 run in our data, so the model has little to go on
- Lunar Lily (hrs_59216297) | 6yo M | 151lb | OR - | draw 0 | jockey Freddie Mitchell(3) | trainer Tom Gretton (14d 0/4) | headgear p (1st time) | last run 224 days | form PP5- | MARKET 0.2% | 09:00 median 201.00 | Matchbook 1000.00
    DATA: model 1.8% | style Unknown | runs in data 1 | last 3: 23 Jan Warwick Hurdle 19f Good To Soft PU/16
    DATA for: First-time headgear
    DATA against: Returns from a 224-day break; Lightly raced: 1 run in our data, so the model has little to go on; Pulled up in 1 of its last 1 jumps runs
- Maxiani (hrs_63357126) | 4yo F | 150lb | OR - | draw 0 | jockey Adam Wedge | trainer David Dennis (14d 1/2) | headgear - | last run 38 days | form 6-P0 | MARKET 0.2% | 09:00 median 201.00 | Matchbook 1000.00
    DATA: model 1.6% | style Prominent (led 8% of runs) | runs in data 2 | last 3: 4 May Warwick Hurdle 16f Good PU/13; 21 Oct Worcester Hurdle 16f Good To Soft 10/10
    DATA against: Last-run finishing speed -14.0% vs that field (faded); Lightly raced: 2 runs in our data, so the model has little to go on; Pulled up in 1 of its last 2 jumps runs

## 1:00 Bangor-on-Dee | race_id rac_32305909142 | Howard Evans Roofing & Cladding Mares' Handicap Steeple Chase (Challenger Mares' Chase Series Qualifier) (GBB Race)
Chase | Class 3 | 2m4f72y | going Good To Soft | Turf | 7 runners | rating band 0-125 | age 4yo+
DATA pace: Even - Two likely leaders (Trinity Street, It's Easy). A fair, even gallop is most likely.
- Trinity Street (hrs_51558010) | 5yo M | 162lb | OR 117 | draw 0 | jockey Stan Sheppard | trainer Henry Daly (14d 3/12) | headgear - | last run 30 days | form 3254-1 | MARKET 43.5% | 09:00 median 2.00 | Matchbook 2.22
    comment: Won last time out and has finished in the first five in each of her last five starts, so Trinity Street arrives in good heart after 30 days off, and she has run over today's trip.
    DATA: model 31.7% | style Leader (led 43% of runs) | runs in data 4 | last 3: 17 Feb Market Rasen Hurdle 16.6f Soft 5/9; 21 Mar Newbury Hurdle 20.5f Good To Soft 4/15; 29 Oct Stratford Hurdle 22f Good To Soft 1/9 fig 110
    DATA for: Best recent form figure 110, 8 lb above field average; Official rating 117, 6 lb above field average; Trainer 25% wins (3/12), last 14 days; Last-run finishing speed +8.1% vs that field (finished strongly); Has won at this trip or further
    DATA against: Recent figures 7 lb below its current mark (looks high in the weights); Carries 6 lb more than average; First run over fences in our data
- It's Easy (hrs_24467954) | 8yo M | 152lb | OR 107 | draw 0 | jockey Adam Wedge | trainer Mrs C. Williams (14d 1/24) | headgear - | last run 30 days | form 87P-23 | MARKET 11.7% | 09:00 median 7.50 | Matchbook 8.40
    DATA: model 16.2% | style Leader (led 54% of runs) | runs in data 4 | last 3: 9 Feb Plumpton Chase 17f Soft PU/5; 21 Oct Fontwell Hurdle 19f Soft 2/6 fig 105; 29 Oct Ffos Las Hurdle 20f Heavy 3/6 fig 94
    DATA against: Last-run finishing speed -2.5% vs that field (faded); Race comments mention jumping mistakes in 2 of its last 4 runs; Pulled up in 1 of its last 4 jumps runs
- Lexie's Moon (hrs_33975053) | 8yo M | 147lb | OR 102 | draw 0 | jockey Craig Nichol | trainer Laura Horsfall (14d 0/3) | headgear - | last run 27 days | form /622-9 | MARKET 11.5% | 09:00 median 8.00 | Matchbook 8.40
    comment: Lexie's Moon was beaten into ninth last time out and is winless in her last four, which makes her hard to fancy, though a second two starts back and another second three starts back show she can go close.
    DATA: model 15.6% | style Prominent (led 29% of runs) | runs in data 3 | last 3: 11 Jan Fontwell Hurdle 19.1f Soft 2/14; 24 Jan Uttoxeter Hurdle 15.8f Soft 2/5; 1 Nov Worcester Chase 20f Good To Soft 9/15 fig 90
    DATA for: Good recent finishing positions; Carries 9 lb less than average
    DATA against: Best recent form figure 90, 12 lb below field average; Recent figures 12 lb below its current mark (looks high in the weights); Official rating 102, 9 lb below field average; Last-run finishing speed -2.5% vs that field (faded)
- Epinephrine (hrs_37563071) | 6yo M | 154lb | OR 109 | draw 0 | jockey Ned Fox(3) | trainer Venetia Williams (14d 0/11) | headgear - | last run 228 days | form 32425- | MARKET 10.9% | 09:00 median 8.50 | Matchbook 8.80
    comment: The main risk is a 228-day absence, with 154 lb to carry after a fifth last time out.
    DATA: model 14.3% | style Midfield (led 4% of runs) | runs in data 5 | last 3: 8 Mar Warwick Chase 16.2f Good To Soft 4/6; 21 Mar Bangor-on-Dee Chase 17.4f Good 2/5; 14 Apr Market Rasen Chase 21.4f Good 5/7
    DATA against: Trainer 0 wins from 11 runs, last 14 days; Last-run finishing speed -2.9% vs that field (faded); Returns from a 228-day break
- Future Bucks (hrs_58844044) | 5yo M | 144lb | OR 99 | draw 0 | jockey Isabelle Ryder(5) | trainer Jamie Snowden (14d 4/15) | headgear ht (1st time) | wind surgery | last run 206 days | form 134P-6 | MARKET 10.5% | 09:00 median 8.50 | Matchbook 9.40
    comment: The big risk is a 206-day absence after a sixth and a pulled up.
    DATA: model 6.7% | style Prominent (led 5% of runs) | runs in data 3 | last 3: 3 Feb Carlisle Hurdle 19.3f Good To Soft 4/7; 21 Mar Newbury Hurdle 20.5f Good To Soft PU/15; 6 May Newton Abbot Hurdle 16.8f Good 6/8
    DATA for: Trainer 27% wins (4/15), last 14 days; Carries 12 lb less than average; First-time headgear
    DATA against: Official rating 99, 12 lb below field average; Last-run finishing speed -10.6% vs that field (faded); Returns from a 206-day break; Pulled up in 1 of its last 3 jumps runs; First run over fences in our data
- Pottersville (hrs_51865975) | 7yo M | 168lb | OR 123 | draw 0 | jockey Jamie Brace(5) | trainer Rebecca Curtis (14d 0/10) | headgear - | wind surgery | last run 224 days | form 0148P- | MARKET 7.3% | 09:00 median 11.00 | Matchbook 15.00
    comment: Pottersville won four starts back but has since slipped to a fourth, an eighth and then pulled up last time out, and she returns after 224 days off.
    DATA: model 7.4% | style Held up (led 4% of runs) | runs in data 3 | last 3: 1 Jan Windsor Hurdle 22f Good 4/4; 24 Jan Doncaster Hurdle 24.4f Soft 8/8; 18 Apr Bangor-on-Dee Hurdle 23.1f Good PU/5
    DATA for: Official rating 123, 12 lb above field average
    DATA against: Trainer 0 wins from 10 runs, last 14 days; Carries 12 lb more than average; Returns from a 224-day break; Pulled up in 1 of its last 3 jumps runs; First run over fences in our data
- All The Glory (hrs_24638754) | 9yo M | 162lb | OR 117 | draw 0 | jockey David Noonan | trainer Jonjo & A.J. O'Neill (14d 4/33) | headgear p | last run 19 days | form 47P-33 | MARKET 4.7% | 09:00 median 17.00 | Matchbook 24.00
    comment: All The Glory arrives in good heart after finishing third last time out, and a third two starts back, just 19 days ago, and she has run over today's trip before.
    DATA: model 8.1% | style Held up (led 3% of runs) | runs in data 6 | last 3: 14 Apr Market Rasen Chase 21.4f Good PU/7; 15 Oct Fontwell Chase 21.5f Good To Soft 3/4; 9 Nov Carlisle Chase 16f Good 3/3
    DATA for: Official rating 117, 6 lb above field average
    DATA against: Carries 6 lb more than average; Pulled up in 1 of its last 5 jumps runs

## 1:33 Bangor-on-Dee | race_id rac_32306186133 | Paul Ferguson Jumpers To Follow Novices' Hurdle Race (Div I) (GBB Race)
Hurdle | Class 3 | 2m145y | going Good To Soft | Turf | 8 runners | rating band - | age 4yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Scott's Legacy (hrs_59862502) | 4yo G | 160lb | OR - | draw 0 | jockey Toby McCain-Mitchell(3) | trainer Nigel & Willy Twiston-Davies (14d 3/18) | headgear - | last run 36 days | form 51-17 | MARKET 65.5% | 09:00 median 1.29 | Matchbook 1.34
    DATA: model 28.8% | style Midfield (led 8% of runs) | runs in data 3 | last 3: 24 Mar Southwell NH Flat 15.8f Good 1/7; 28 Sep Newton Abbot Hurdle 16.8f Good 1/6; 23 Oct Cheltenham Hurdle 16.5f Good To Soft 7/10 fig 119
    DATA for: Has won at this trip or further; Good recent finishing positions
- Works For Me (hrs_17395162036) | 4yo G | 154lb | OR - | draw 0 | jockey Peter Kavanagh | trainer Donald McCain (14d 2/25) | headgear - | last run 208 days | form 1 | MARKET 11.0% | 09:00 median 5.50 | Matchbook 11.50
    DATA: model 9.8% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 208-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Montevallo (hrs_17395280938) | 5yo G | 154lb | OR - | draw 0 | jockey Toby Wynne | trainer Oliver Greenall & Josh Guerriero (14d 4/18) | headgear - | last run 280 days | form 42- | MARKET 10.9% | 09:00 median 6.50 | Matchbook 9.80
    DATA: model 9.8% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 22% wins (4/18), last 14 days
    DATA against: Returns from a 280-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Our Pedro (hrs_17396175832) | 6yo G | 154lb | OR - | draw 0 | jockey Bradley Harris(3) | trainer Neil Mulholland (14d 1/14) | headgear - | last run - days | form - | MARKET 5.9% | 09:00 median 12.00 | Matchbook 19.00
    DATA: model 9.8% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Minutes To Spare (hrs_62296689) | 5yo G | 154lb | OR - | draw 0 | jockey Adam Wedge | trainer Donald McCain (14d 2/25) | headgear t | wind surgery | last run 19 days | form 8-9 | MARKET 2.9% | 09:00 median 23.00 | Matchbook 42.00
    DATA: model 23.0% | style Held up (led 5% of runs) | runs in data 2 | last 3: 6 Mar Ayr Hurdle 16f Soft 8/12; 9 Nov Carlisle Hurdle 17f Good To Soft 9/14
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Get Busy Jumping (hrs_17394499731) | 5yo G | 154lb | OR - | draw 0 | jockey Craig Nichol | trainer Oliver Greenall & Josh Guerriero (14d 4/18) | headgear h (1st time) | last run 17 days | form 85 | MARKET 2.3% | 09:00 median 29.00 | Matchbook 55.00
    DATA: model 5.7% | style Midfield (led 8% of runs) | runs in data 2 | last 3: 27 Oct Bangor-on-Dee Hurdle 16.5f Good 8/11; 11 Nov Bangor-on-Dee Hurdle 16.5f Good 5/7 fig 105
    DATA for: Trainer 22% wins (4/18), last 14 days; First-time headgear
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Jeu Magic (hrs_17394930490) | 4yo G | 154lb | OR - | draw 0 | jockey Conor Ring | trainer Mrs C. Williams (14d 1/24) | headgear - | last run 24 days | form 7 | MARKET 0.8% | 09:00 median 81.00 | Matchbook 260.00
    DATA: model 8.5% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 4 Nov Chepstow Hurdle 16f Good To Soft 7/13
    DATA against: Last-run finishing speed -6.2% vs that field (faded); Lightly raced: 1 run in our data, so the model has little to go on
- New Chapter (hrs_17394934662) | 4yo F | 147lb | OR - | draw 0 | jockey David Noonan | trainer Alastair Ralph (14d 0/5) | headgear - | last run 21 days | form 0 | MARKET 0.8% | 09:00 median 126.00 | Matchbook 160.00
    DATA: model 4.4% | style Held up (led 8% of runs) | runs in data 1 | last 3: 7 Nov Uttoxeter Hurdle 16f Good 11/13
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace

## 2:10 Bangor-on-Dee | race_id rac_32305911079 | Paul Ferguson Jumpers To Follow Novices' Hurdle Race (Div II) (GBB Race)
Hurdle | Class 3 | 2m145y | going Good To Soft | Turf | 9 runners | rating band - | age 4yo+
DATA pace: Lone leader - Hang Out is the only habitual front-runner and may be allowed an easy lead.
- Hang Out (hrs_17394658267) | 5yo G | 160lb | OR - | draw 0 | jockey Harry Brown(7) | trainer Donald McCain (14d 2/25) | headgear - | last run 17 days | form 1-1 | MARKET 44.5% | 09:00 median 1.73 | Matchbook 2.18
    DATA: model 11.7% | style Leader (led 57% of runs) | runs in data 1 | last 3: 11 Nov Bangor-on-Dee Hurdle 16.5f Good 1/7 fig 119
    DATA for: Last-run finishing speed +3.4% vs that field (finished strongly); Has won at this trip or further; Pace: may get an uncontested lead
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Loki (hrs_53420353) | 4yo G | 154lb | OR - | draw 0 | jockey Robert Dunne | trainer Oliver Greenall & Josh Guerriero (14d 4/18) | headgear - | last run 24 days | form - | MARKET 26.8% | 09:00 median 3.25 | Matchbook 3.15
    DATA: model 17.5% | style Midfield (led 3% of runs) | runs in data 4 | last 3: 12 Sep Chester Flat 12.3f Soft 10/11; 16 Oct Haydock Flat 14f Heavy 2/5 fig 76; 4 Nov Nottingham Flat 16f Soft 4/13 fig 71
    DATA for: Trainer 22% wins (4/18), last 14 days; Last-run finishing speed +6.5% vs that field (finished strongly)
    DATA against: First run over hurdles in our data
- Written In Gold (hrs_17395940114) | 4yo G | 154lb | OR - | draw 0 | jockey David Noonan | trainer Jonjo & A.J. O'Neill (14d 4/33) | headgear - | last run - days | form - | MARKET 9.3% | 09:00 median 8.50 | Matchbook 10.50
    DATA: model 9.8% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Bears Socks (hrs_17394937791) | 5yo G | 154lb | OR - | draw 0 | jockey Philip Armson(3) | trainer Dan Horsford (14d 1/1) | headgear - | last run 24 days | form 22-4 | MARKET 8.8% | 09:00 median 8.50 | Matchbook 11.50
    DATA: model 12.5% | style Held up (led 8% of runs) | runs in data 1 | last 3: 4 Nov Chepstow NH Flat 16f Good To Soft 4/13 fig 93
    DATA for: Last-run finishing speed +8.8% vs that field (finished strongly)
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Old Colony (hrs_17395160993) | 4yo G | 154lb | OR - | draw 0 | jockey Peter Kavanagh | trainer Donald McCain (14d 2/25) | headgear - | last run 19 days | form 3-7 | MARKET 5.8% | 09:00 median 13.00 | Matchbook 18.00
    DATA: model 16.9% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 9 Nov Carlisle Hurdle 17f Good To Soft 7/14
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Queen Marcia (hrs_50590288) | 5yo M | 147lb | OR - | draw 0 | jockey Jamie Brace(5) | trainer D. J. Jeffreys (14d 0/4) | headgear - | last run 259 days | form 6/46- | MARKET 2.3% | 09:00 median 30.00 | Matchbook 65.00
    DATA: model 8.9% | style Prominent (led 8% of runs) | runs in data 2 | last 3: 14 Feb Ascot NH Flat 15.7f Good To Soft 4/9; 14 Mar Uttoxeter NH Flat 15.8f Soft 6/12
    DATA against: Returns from a 259-day break; Lightly raced: 2 runs in our data, so the model has little to go on; First run over hurdles in our data
- Mahbury (hrs_17395939071) | 7yo G | 154lb | OR - | draw 0 | jockey Ben Poste | trainer Max Young (14d 0/0) | headgear - | last run 973 days | form P2/ | MARKET 1.1% | 09:00 median 51.00 | Matchbook 180.00
    DATA: model 9.8% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 973-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Deferred Interest (hrs_53539507) | 5yo G | 154lb | OR - | draw 0 | jockey Bradley Harris(3) | trainer Neil Mulholland (14d 1/14) | headgear p | last run 54 days | form 8P- | MARKET 0.7% | 09:00 median 81.00 | Matchbook 240.00
    DATA: model 9.9% | style Prominent (led 38% of runs) | runs in data 4 | last 3: 9 Feb Wolverhampton Flat 12.2f Standard 4/8; 13 Mar Southwell Flat 14.1f Standard 10/10; 5 Oct Kempton Flat 12f Standard To Slow 9/10
    DATA against: First run over hurdles in our data
- Lilycala (hrs_63809676) | 5yo M | 147lb | OR - | draw 0 | jockey Freddie Mitchell(3) | trainer Tom Gretton (14d 0/4) | headgear t | last run 196 days | form 0-4 | MARKET 0.7% | 09:00 median 101.00 | Matchbook 220.00
    DATA: model 3.0% | style Prominent (led 8% of runs) | runs in data 2 | last 3: 19 Apr Stratford Hurdle 16.3f Good 11/13; 16 May Bangor-on-Dee Hurdle 16.7f Good 4/11
    DATA against: Returns from a 196-day break; Lightly raced: 2 runs in our data, so the model has little to go on

## 2:45 Bangor-on-Dee | race_id rac_32305913016 | Follow Dave Win 60th Birthday Handicap Steeple Chase (GBB Race)
Chase | Class 4 | 2m1f77y | going Good To Soft | Turf | 9 runners | rating band 0-120 | age 4yo+
DATA pace: Lone leader - Whiskeywealth is the only habitual front-runner and may be allowed an easy lead.
- Doctors Hill (hrs_47837363) | 6yo G | 157lb | OR 109 | draw 0 | jockey Jack Stenhouse(7) | trainer Philip Hobbs & Johnson White (14d 3/17) | headgear - | last run 37 days | form 2663-4 | MARKET 32.0% | 09:00 median 2.75 | Matchbook 2.90
    comment: The risk is that he is yet to win in his last five starts and carries 157 lb after 37 days off.
    DATA: model 13.4% | style Held up (led 3% of runs) | runs in data 5 | last 3: 21 Mar Newbury Hurdle 18.8f Good To Soft 6/9; 11 Apr Chepstow Hurdle 16.1f Good To Soft 3/9; 22 Oct Ffos Las Chase 16f Soft 4/6 fig 107
    DATA for: Best recent form figure 107, 8 lb above field average
- Locquirec (hrs_53052391) | 5yo G | 149lb | OR 101 | draw 0 | jockey Toby Wynne | trainer Oliver Greenall & Josh Guerriero (14d 4/18) | headgear p | wind surgery | last run 32 days | form 66F6-6 | MARKET 12.2% | 09:00 median 7.50 | Matchbook 7.60
    comment: Locquirec is hard to fancy, having finished sixth in four of his last five starts, including last time out, and he fell three starts back, so he is yet to win in that spell.
    DATA: model 5.0% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 28 Feb Newbury Hurdle 16.3f Good To Soft F/6; 18 Apr Bangor-on-Dee Hurdle 19.6f Good 6/7; 27 Oct Bangor-on-Dee Chase 17.5f Good To Soft 6/9 fig 96
    DATA for: Trainer 22% wins (4/18), last 14 days; Carries 11 lb less than average
    DATA against: Official rating 101, 11 lb below field average; Poor recent finishing positions; Fell or unseated in 1 of its last 5 jumps runs
- The Hawkstonian (hrs_46602892) | 6yo G | 162lb | OR 114 | draw 0 | jockey Liam Harrison | trainer Ben Pauling (14d 8/39) | headgear t | last run 276 days | form /3513- | MARKET 11.3% | 09:00 median 7.50 | Matchbook 8.40
    comment: The Hawkstonian was third last time out and a winner two starts back, with a fifth three starts back and a third four starts back, and he has run over today's trip.
    DATA: model 11.1% | style Midfield (led 8% of runs) | runs in data 2 | last 3: 30 Jan Ffos Las Hurdle 15.8f Heavy 1/8; 25 Feb Bangor-on-Dee Hurdle 16.7f Soft 3/5
    DATA for: Trainer 21% wins (8/39), last 14 days; Good recent finishing positions
    DATA against: Returns from a 276-day break; Lightly raced: 2 runs in our data, so the model has little to go on; First run over fences in our data
- A Moments Madness (hrs_38884594) | 7yo G | 169lb | OR 121 | draw 0 | jockey Mr Albi Tufnell(7) | trainer Fergal O'Brien (14d 5/28) | headgear - | last run 233 days | form 21/30- | MARKET 10.8% | 09:00 median 8.50 | Matchbook 8.60
    comment: The big risk is a 233-day absence, and he was unplaced last time out.
    DATA: model 11.9% | style Held up (led 8% of runs) | runs in data 2 | last 3: 8 Mar Carlisle Chase 20.9f Good To Soft 3/6; 9 Apr Aintree Chase 21.1f Good To Soft 11/24
    DATA for: Official rating 121, 9 lb above field average
    DATA against: Carries 9 lb more than average; Returns from a 233-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- Mr Mojo Risin (hrs_47555452) | 6yo G | 155lb | OR 107 | draw 0 | jockey Peter Kavanagh | trainer Donald McCain (14d 2/25) | headgear t | last run 196 days | form 4/54-2 | MARKET 9.6% | 09:00 median 9.00 | Matchbook 10.00
    comment: Mr Mojo Risin is winless in his last four, though he was second last time out, with a fourth, a fifth and another fourth before that, and he has run over today's trip.
    DATA: model 17.7% | style Unknown | runs in data 2 | last 3: 2 Apr Kelso Hurdle 16.2f Good 4/10; 16 May Bangor-on-Dee Hurdle 16.7f Good 2/11
    DATA for: Last-run finishing speed +5.4% vs that field (finished strongly); Carries 5 lb less than average
    DATA against: Official rating 107, 5 lb below field average; Returns from a 196-day break; Lightly raced: 2 runs in our data, so the model has little to go on; First run over fences in our data
- Luron d'Oudairies (hrs_53475996) | 5yo G | 168lb | OR 120 | draw 0 | jockey Ned Fox(3) | trainer Venetia Williams (14d 0/11) | headgear - | last run 186 days | form FP4-64 | MARKET 9.4% | 09:00 median 9.00 | Matchbook 10.50
    comment: Returning after 186 days off, Luron d'Oudairies was fourth last time out and sixth two starts back, so the recent form is fairly steady without being progressive. He is yet to win in that spell, though he looks unexposed and open to improvement under 168 lb.
    DATA: model 9.6% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Official rating 120, 8 lb above field average
    DATA against: Trainer 0 wins from 11 runs, last 14 days; Carries 8 lb more than average; Returns from a 186-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Royal Mer (hrs_31965255) | 8yo G | 169lb | OR 121 | draw 0 | jockey David Noonan | trainer David Pipe (14d 3/17) | headgear t | last run 268 days | form 22311- | MARKET 8.1% | 09:00 median 7.50 | Matchbook 18.00
    comment: Royal Mer arrives in form, having won last time out and two starts back, with a third and two seconds before that, and he has run over today's trip. The big risk is a 268-day layoff, and a weight of 169 lb won't help.
    DATA: model 20.8% | style Prominent (led 29% of runs) | runs in data 4 | last 3: 26 Jan Hereford Chase 16f Soft 3/5; 14 Feb Wincanton Chase 15.7f Heavy 1/7; 5 Mar Wincanton Chase 20.2f Good To Soft 1/5
    DATA for: Official rating 121, 9 lb above field average; Last-run finishing speed +3.8% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Carries 9 lb more than average; Returns from a 268-day break
- Kourosh (hrs_38174255) | 6yo G | 148lb | OR 100 | draw 0 | jockey Lilly Pinchin | trainer Henry Oliver (14d 0/3) | headgear - | last run 34 days | form P324/3 | MARKET 4.5% | 09:00 median 19.00 | Matchbook 23.00
    comment: Kourosh arrives in solid form, third last time out and a second three starts back, and has run over today's trip, but he is yet to win in his last five and carries 148 lb after 34 days off.
    DATA: model 7.1% | style Held up (led 8% of runs) | runs in data 1 | last 3: 25 Oct Market Rasen Hurdle 16.5f Good To Soft 3/6 fig 95
    DATA for: Carries 12 lb less than average
    DATA against: Best recent form figure 95, 4 lb below field average; Official rating 100, 12 lb below field average; Lightly raced: 1 run in our data, so the model has little to go on
- Whiskeywealth (hrs_21327705) | 10yo G | 165lb | OR 117 | draw 0 | jockey Toby McCain-Mitchell(3) | trainer Donald McCain (14d 2/25) | headgear - | last run 22 days | form /396-0 | MARKET 2.3% | 09:00 median 29.00 | Matchbook 70.00
    comment: Whiskeywealth is winless in his last four, but he was third four starts back and has run over today's trip, while a 22-day break suggests he's fresh enough.
    DATA: model 3.2% | style Leader (led 57% of runs) | runs in data 1 | last 3: 6 Nov Aintree Hurdle 17f Good To Soft 10/10
    DATA for: Pace: may get an uncontested lead
    DATA against: Last-run finishing speed -9.0% vs that field (faded); Lightly raced: 1 run in our data, so the model has little to go on; Aged 10, older than most of this field

## 3:25 Bangor-on-Dee | race_id rac_32305914953 | Pennine Flooring On The Radio Handicap Steeple Chase (Challenger Staying Chase Series Qualifier) (GBB Race)
Chase | Class 3 | 3m30y | going Good To Soft | Turf | 12 runners | rating band 0-125 | age 4yo+
DATA pace: Lone leader - Paddy O'Mahler is the only habitual front-runner and may be allowed an easy lead.
- The Price of Peace (hrs_49326053) | 7yo G | 168lb | OR 125 | draw 0 | jockey Jamie Brace(5) | trainer Rebecca Curtis (14d 0/10) | headgear - | last run 260 days | form /215P- | MARKET 21.7% | 09:00 median 4.00 | Matchbook 4.10 | CHECK (skip line 3.80)
    comment: The big risk is a 260-day absence after he was pulled up last time out.
    DATA: model 5.3% | style Held up (led 5% of runs) | runs in data 2 | last 3: 24 Jan Doncaster Hurdle 24.4f Soft 5/12; 13 Mar Cheltenham Hurdle 24f Good To Soft PU/22
    DATA for: Official rating 125, 6 lb above field average
    DATA against: Trainer 0 wins from 10 runs, last 14 days; Carries 6 lb more than average; Returns from a 260-day break; Lightly raced: 2 runs in our data, so the model has little to go on; Pulled up in 1 of its last 2 jumps runs; First run over fences in our data
- Big Cadillac (hrs_39699289) | 6yo G | 166lb | OR 123 | draw 0 | jockey Robert Dunne | trainer Dan Skelton (14d 27/97) | headgear t | last run 47 days | form 6634-1 | MARKET 13.6% | 09:00 median 5.00 | Matchbook 8.20
    comment: Fresh from a last-time-out win, with a fourth and a third before that, Big Cadillac arrives in decent heart and has run over today's trip, while a yard in form helps.
    DATA: model 12.9% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 18 Feb Southwell Hurdle 20.4f Soft 3/13; 8 Mar Warwick Hurdle 26f Good To Soft 4/7; 12 Oct Worcester Chase 23f Good To Soft 1/5
    DATA for: Trainer 28% wins (27/97), last 14 days; Last-run finishing speed +5.4% vs that field (finished strongly); Good recent finishing positions
- Laganhill (hrs_48353361) | 8yo G | 167lb | OR 124 | draw 0 | jockey Stan Sheppard | trainer Henry Daly (14d 3/12) | headgear - | last run 238 days | form 4272P- | MARKET 10.6% | 09:00 median 7.50 | Matchbook 9.20
    comment: The risk is a 238-day absence, with a pulled-up effort last time out and 167 lb to carry.
    DATA: model 7.9% | style Prominent (led 5% of runs) | runs in data 3 | last 3: 17 Jan Ascot Chase 23.8f Soft 7/11; 20 Feb Exeter Chase 24.2f Heavy 2/4; 4 Apr Haydock Chase 25.6f Good PU/11
    DATA for: Official rating 124, 5 lb above field average; Trainer 25% wins (3/12), last 14 days
    DATA against: Carries 5 lb more than average; Returns from a 238-day break; Pulled up in 1 of its last 3 jumps runs
- Gasmani (hrs_34652597) | 7yo G | 157lb | OR 114 | draw 0 | jockey Adam Wedge | trainer David Dennis (14d 1/2) | headgear - | last run 32 days | form 12-842 | MARKET 10.2% | 09:00 median 7.50 | Matchbook 9.80
    comment: Gasmani was second last time out and has run over today's trip, but he's been beaten in all four runs since a win five starts back, including an eighth three starts back.
    DATA: model 5.5% | style Midfield (led 4% of runs) | runs in data 5 | last 3: 22 May Worcester Hurdle 23f Good 8/11; 7 Oct Worcester Hurdle 20f Good 4/10; 27 Oct Bangor-on-Dee Chase 24f Good To Soft 2/13 fig 111
    DATA for: Best recent form figure 111, 6 lb above field average; Last-run finishing speed +5.9% vs that field (finished strongly); Has won at this trip or further; Carries 5 lb less than average
    DATA against: Official rating 114, 5 lb below field average
- Judicial Deference (hrs_37367974) | 7yo G | 167lb | OR 124 | draw 0 | jockey Toby Wynne | trainer Oliver Greenall & Josh Guerriero (14d 4/18) | headgear t | last run 252 days | form 2111B- | MARKET 9.2% | 09:00 median 9.00 | Matchbook 9.80
    comment: Judicial Deference won three on the spin before being brought down last time out, and a runner-up finish five starts back adds to a strong profile, but 252 days off is a big gap and 167 lb is a hefty burden.
    DATA: model 12.5% | style Prominent (led 5% of runs) | runs in data 3 | last 3: 17 Jan Haydock Hurdle 21.2f Good To Soft 1/17; 13 Feb Kelso Hurdle 22.7f Heavy 1/8; 21 Mar Kelso Hurdle 20.9f Good To Soft BD/14
    DATA for: Official rating 124, 5 lb above field average; Trainer 22% wins (4/18), last 14 days
    DATA against: Carries 5 lb more than average; Returns from a 252-day break; Fell or unseated in 1 of its last 3 jumps runs; First run over fences in our data
- Liege Ardent (hrs_57686468) | 5yo G | 150lb | OR 107 | draw 0 | jockey Craig Nichol | trainer Richard Hobson (14d 0/2) | headgear t | last run 32 days | form 6-0F25 | MARKET 8.5% | 09:00 median 9.50 | Matchbook 11.50
    comment: Liege Ardent is winless in his last five, though he was second two starts back, and a fifth last time out 32 days ago hardly makes him easy to fancy.
    DATA: model 6.5% | style Held up (led 8% of runs) | runs in data 1 | last 3: 27 Oct Bangor-on-Dee Chase 24f Good To Soft 5/13 fig 106
    DATA for: Last-run finishing speed +4.1% vs that field (finished strongly); Carries 12 lb less than average
    DATA against: Official rating 107, 12 lb below field average; Lightly raced: 1 run in our data, so the model has little to go on
- Limerick Star (hrs_40920299) | 6yo G | 166lb | OR 123 | draw 0 | jockey Jack Stenhouse(7) | trainer Philip Hobbs & Johnson White (14d 3/17) | headgear p | last run 245 days | form /3431- | MARKET 5.8% | 09:00 median 14.75 | Matchbook 16.00
    comment: Limerick Star won last time out and was third two starts back, but he returns after 245 days off and carries 166 lb, which could blunt that momentum.
    DATA: model 13.1% | style Prominent (led 23% of runs) | runs in data 4 | last 3: 7 Feb Warwick Hurdle 19f Heavy 4/7; 1 Mar Ffos Las Hurdle 20f Heavy 3/9; 28 Mar Uttoxeter Hurdle 23.3f Good To Soft 1/6
    DATA for: Last-run finishing speed +3.6% vs that field (finished strongly); Good recent finishing positions
    DATA against: Returns from a 245-day break; First run over fences in our data
- Grand Albert (hrs_34665414) | 8yo G | 163lb | OR 120 | draw 0 | jockey Peter Kavanagh | trainer Donald McCain (14d 2/25) | headgear p | last run 259 days | form /4564- | MARKET 5.2% | 09:00 median 15.00 | Matchbook 18.50
    comment: The main risk is a 259-day absence, with 163 lb to carry too.
    DATA: model 7.4% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 14 Feb Haydock Chase 28.4f Good To Soft 6/11; 14 Mar Uttoxeter Chase 34f Soft 4/16
    DATA against: Last-run finishing speed -7.0% vs that field (faded); Returns from a 259-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- Lucky d'Aubrelle (hrs_51024309) | 5yo G | 170lb | OR 127 | draw 0 | jockey Ned Fox(3) | trainer Venetia Williams (14d 0/11) | headgear - | last run 233 days | form 48643- | MARKET 5.0% | 09:00 median 17.00 | Matchbook 19.00
    comment: Lucky d'Aubrelle signed off with a third last time out, after a fourth two starts back, but he is yet to win in his last five and returns from 233 days off under 170 lb. Lightly raced and unexposed, he could have more to offer.
    DATA: model 7.6% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Official rating 127, 8 lb above field average
    DATA against: Trainer 0 wins from 11 runs, last 14 days; Carries 8 lb more than average; Returns from a 233-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Paddy O'Mahler (hrs_34045081) | 8yo G | 153lb | OR 110 | draw 0 | jockey Oscar Palmer(7) | trainer Joel Parkinson & Sue Smith (14d 0/14) | headgear p | last run 28 days | form 112F-4 | MARKET 4.8% | 09:00 median 17.00 | Matchbook 19.50
    comment: In his favour, he won four and five starts back, and a second three starts back shows he can be competitive.
    DATA: model 6.1% | style Leader (led 29% of runs) | runs in data 3 | last 3: 24 Feb Catterick Chase 25.2f Good To Soft 2/6; 22 Mar Carlisle Chase 24.5f Good To Soft F/12; 31 Oct Wetherby Chase 24f Good 4/4 fig 103
    DATA for: Carries 9 lb less than average; Pace: may get an uncontested lead
    DATA against: Recent figures 7 lb below its current mark (looks high in the weights); Official rating 110, 9 lb below field average; Trainer 0 wins from 14 runs, last 14 days; Fell or unseated in 1 of its last 3 jumps runs
- One Last Glance (hrs_23425738) | 9yo G | 150lb | OR 107 | draw 0 | jockey Freddie Mitchell(3) | trainer Tom Gretton (14d 0/4) | headgear tp | last run 30 days | form 2412-1 | MARKET 3.6% | 09:00 median 19.00 | Matchbook 32.00
    comment: One Last Glance arrives in cracking nick, a winner last time out, a second two starts back, and a winner three starts back, and he has run over today's trip.
    DATA: model 9.1% | style Held up (led 4% of runs) | runs in data 4 | last 3: 12 Feb Leicester Chase 20.1f Heavy 1/5; 6 Mar Leicester Chase 22.7f Good To Soft 2/6; 29 Oct Stratford Chase 22.5f Good To Soft 1/6 fig 100
    DATA for: Last-run finishing speed +5.7% vs that field (finished strongly); Good recent finishing positions; Carries 12 lb less than average
    DATA against: Best recent form figure 100, 5 lb below field average; Recent figures 7 lb below its current mark (looks high in the weights); Official rating 107, 12 lb below field average
- City Chief (hrs_24494568) | 9yo G | 167lb | OR 124 | draw 0 | jockey Cameron Iles(5) | trainer James Standen (14d 0/1) | headgear p | last run 204 days | form 3124-1 | MARKET 1.7% | 09:00 median 34.00 | Matchbook 110.00
    comment: City Chief won last time out and a fourth two starts back sits within a solid run of two wins in his last five, and he has run over today's trip.
    DATA: model 6.3% | style Held up (led 8% of runs) | runs in data 1 | last 3: 5 Apr Fairyhouse Chase 24.8f Yielding To Soft 2/9
    DATA for: Official rating 124, 5 lb above field average; Last-run finishing speed +2.1% vs that field (finished strongly)
    DATA against: Carries 5 lb more than average; Returns from a 204-day break; Lightly raced: 1 run in our data, so the model has little to go on
