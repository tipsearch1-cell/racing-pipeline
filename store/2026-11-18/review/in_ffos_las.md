# Card review packet: Ffos Las, 2026-11-18

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
{"meeting": "ffos_las", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 12:48 Ffos Las | race_id rac_32305041366 | Dandara Maiden Hurdle Race (Div I) (GBB Race)
Hurdle | Class 4 | 1m7f182y | going Good To Soft | Turf | 9 runners | rating band - | age 4yo+
DATA pace: Unclear - Running styles known for only 4 of 9 runners.
- No Walkover (hrs_50188922) | 5yo G | 158lb | OR - | draw 0 | jockey Jack Tudor | trainer David Pipe (14d 0/11) | headgear - | last run 284 days | form 2/118- | MARKET 58.5% | 09:00 median 1.40 | Matchbook -
    DATA: model 21.7% | style Unknown | runs in data 1 | last 3: 7 Feb Newbury NH Flat 16.3f Heavy 8/10
    DATA against: Trainer 0 wins from 11 runs, last 14 days; Last-run finishing speed -13.4% vs that field (faded); Returns from a 284-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Bob Bishop (hrs_51124878) | 5yo G | 158lb | OR - | draw 0 | jockey Freddie Gingell | trainer Joe Tizzard (14d 4/23) | headgear - | last run 574 days | form 31/ | MARKET 16.3% | 09:00 median 4.50 | Matchbook -
    DATA: model 8.1% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 574-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Blinded By Grace (hrs_55091939) | 5yo G | 158lb | OR - | draw 0 | jockey Sean Bowen | trainer Mickey Bowen (14d 5/18) | headgear - | last run 159 days | form 3-16 | MARKET 14.1% | 09:00 median 5.00 | Matchbook -
    DATA: model 20.0% | style Leader (led 72% of runs) | runs in data 2 | last 3: 24 May Uttoxeter NH Flat 15.8f Good 1/5; 12 Jun Newton Abbot NH Flat 16.8f Good 6/6
    DATA for: Trainer 28% wins (5/18), last 14 days; Has won at this trip or further
    DATA against: Last-run finishing speed -8.7% vs that field (faded); Returns from a 159-day break; Lightly raced: 2 runs in our data, so the model has little to go on; First run over hurdles in our data
- Jevon (hrs_17394594644) | 5yo G | 158lb | OR - | draw 0 | jockey Charlie Todd | trainer Dan Skelton (14d 19/80) | headgear - | last run - days | form - | MARKET 4.5% | 09:00 median 15.00 | Matchbook -
    DATA: model 8.1% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 24% wins (19/80), last 14 days
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Mac Gayveur (hrs_61078647) | 4yo G | 158lb | OR - | draw 0 | jockey Jack Stenhouse(7) | trainer Claire Hitch (14d 0/1) | headgear - | last run 238 days | form 65- | MARKET 1.9% | 09:00 median 41.00 | Matchbook -
    DATA: model 9.0% | style Unknown | runs in data 2 | last 3: 18 Feb Southwell NH Flat 15.8f Soft 6/11; 25 Mar Hereford NH Flat 16.2f Good 5/9
    DATA against: Returns from a 238-day break; Lightly raced: 2 runs in our data, so the model has little to go on; First run over hurdles in our data
- El Dorado (hrs_60561186) | 4yo G | 158lb | OR - | draw 0 | jockey Conor Ring | trainer Sheila Lewis (14d 1/6) | headgear - | last run 17 days | form 0-0 | MARKET 1.3% | 09:00 median 81.00 | Matchbook -
    DATA: model 2.8% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 2 Apr Chepstow NH Flat 16.1f Good To Soft 10/11; 1 Nov Worcester Hurdle 16f Good To Soft 15/16
    DATA against: Last-run finishing speed -6.8% vs that field (faded); Lightly raced: 2 runs in our data, so the model has little to go on
- Fozzy Osbourne (hrs_64967952) | 5yo G | 158lb | OR - | draw 0 | jockey Joe Anderson(3) | trainer Grace Harris (14d 1/7) | headgear - | last run 101 days | form - | MARKET 1.2% | 09:00 median 81.00 | Matchbook -
    DATA: model 14.2% | style Held up (led 4% of runs) | runs in data 6 | last 3: 8 Jul Chepstow Flat 8.1f Good To Firm 3/8; 24 Jul Chepstow Flat 10f Good To Firm 5/9; 9 Aug Chepstow Flat 8.1f Good To Firm 11/12
    DATA against: Last-run finishing speed -4.6% vs that field (faded); Returns from a 101-day break; First run over hurdles in our data
- Nuptown Girl (hrs_42073892) | 4yo F | 151lb | OR - | draw 0 | jockey Lee Edwards | trainer Bernard Llewellyn (14d 0/1) | headgear p | last run 23 days | form P | MARKET 1.1% | 09:00 median 67.00 | Matchbook -
    DATA: model 13.3% | style Held up (led 5% of runs) | runs in data 12 | last 3: 28 Jul Yarmouth Flat 10.1f Good To Firm 2/6; 2 Aug Yarmouth Flat 10.1f Good To Firm 1/5; 26 Oct Hereford Hurdle 16f Good To Firm PU/12
    DATA against: Pulled up in 1 of its last 1 jumps runs
- Petit Galet (hrs_48853756) | 5yo G | 158lb | OR - | draw 0 | jockey James Best | trainer Richard Mitford-Slade (14d 0/0) | headgear ht | last run 14 days | form 0/P | MARKET 1.0% | 09:00 median 101.00 | Matchbook -
    DATA: model 2.6% | style Unknown | runs in data 1 | last 3: 4 Nov Chepstow Hurdle 19.5f Good To Soft PU/14
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on; Pulled up in 1 of its last 1 jumps runs

## 1:18 Ffos Las | race_id rac_32304727572 | Dandara Maiden Hurdle Race (Div II) (GBB Race)
Hurdle | Class 4 | 1m7f182y | going Good To Soft | Turf | 7 runners | rating band - | age 4yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Diamond Street (hrs_48853924) | 5yo G | 158lb | OR - | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 19/80) | headgear - | last run 242 days | form 15- | MARKET 62.2% | 09:00 median 1.40 | Matchbook -
    DATA: model 30.0% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 24 Jan Doncaster NH Flat 16.6f Soft 1/7; 21 Mar Newbury NH Flat 16.3f Good To Soft 5/20
    DATA for: Trainer 24% wins (19/80), last 14 days; Last-run finishing speed +3.2% vs that field (finished strongly); Has won at this trip or further
    DATA against: Returns from a 242-day break; Lightly raced: 2 runs in our data, so the model has little to go on; First run over hurdles in our data
- Quickkick (hrs_49578214) | 5yo G | 158lb | OR - | draw 0 | jockey Sean Houlihan | trainer Philip Hobbs & Johnson White (14d 1/20) | headgear h | last run 27 days | form /431-2 | MARKET 23.5% | 09:00 median 3.50 | Matchbook -
    DATA: model 24.0% | style Held up (led 8% of runs) | runs in data 4 | last 3: 26 Feb Taunton NH Flat 16.5f Good To Soft 3/12; 14 Apr Newton Abbot NH Flat 16.8f Good 1/8; 22 Oct Ffos Las Hurdle 16f Soft 2/11 fig 108
    DATA for: Last-run finishing speed +4.4% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Poets Express (hrs_17394104434) | 5yo G | 158lb | OR - | draw 0 | jockey Ben Jones | trainer Ben Pauling (14d 3/23) | headgear - | last run 27 days | form 2 | MARKET 9.4% | 09:00 median 8.50 | Matchbook -
    DATA: model 15.2% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 22 Oct Ffos Las NH Flat 16f Soft 2/6 fig 105
    DATA for: Last-run finishing speed +2.8% vs that field (finished strongly)
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Clondaw Fame (hrs_24769738) | 9yo G | 158lb | OR 98 | draw 0 | jockey Callum Pritchard | trainer Barry Murphy (14d 0/4) | headgear - | last run 386 days | form 3P/25- | MARKET 1.6% | 09:00 median 51.00 | Matchbook -
    DATA: model 17.2% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 386-day break; Lightly raced: 0 runs in our data, so the model has little to go on; Aged 9, older than most of this field
- Walk The Hall (hrs_17393552687) | 6yo M | 151lb | OR - | draw 0 | jockey Jamie Brace(5) | trainer Max Comley (14d 2/7) | headgear - | last run 17 days | form 3P12-0 | MARKET 1.2% | 09:00 median 81.00 | Matchbook -
    DATA: model 7.1% | style Held up (led 8% of runs) | runs in data 1 | last 3: 1 Nov Worcester Hurdle 16f Good To Soft 13/16
    DATA for: Trainer 29% wins (2/7), last 14 days
    DATA against: Last-run finishing speed -2.2% vs that field (faded); Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Mac J (hrs_61340699) | 5yo G | 158lb | OR - | draw 0 | jockey Jay Tidball(5) | trainer David Rees (14d 0/0) | headgear - | last run 238 days | form 74- | MARKET 1.2% | 09:00 median 101.00 | Matchbook -
    DATA: model 4.8% | style Unknown | runs in data 2 | last 3: 5 Feb Huntingdon NH Flat 15.8f Soft 7/8; 25 Mar Hereford NH Flat 16.2f Good 4/9
    DATA for: Last-run finishing speed +2.6% vs that field (finished strongly)
    DATA against: Returns from a 238-day break; Lightly raced: 2 runs in our data, so the model has little to go on; First run over hurdles in our data
- Hoeyfield Lad (hrs_41189946) | 6yo G | 158lb | OR - | draw 0 | jockey Kielan Woods | trainer D. J. Jeffreys (14d 0/4) | headgear - | last run 13 days | form 0/34-0 | MARKET 0.8% | 09:00 median 176.00 | Matchbook -
    DATA: model 1.8% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 5 Nov Newbury Hurdle 19f Good To Soft 10/10
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on

## 1:48 Ffos Las | race_id rac_32304729509 | Golwg Gwendraeth Beginners' Steeple Chase (GBB Race)
Chase | Class 3 | 2m | going Good To Soft | Turf | 4 runners | rating band - | age 4yo+
DATA pace: Even - Two likely leaders (Old Park Star, Sober Glory). A fair, even gallop is most likely.
- Old Park Star (hrs_46729571) | 6yo G | 158lb | OR 155 | draw 0 | jockey Nico de Boinville | trainer Nicky Henderson (14d 4/16) | headgear - | last run 253 days | form /1111- | MARKET 55.9% | 09:00 median 1.67 | Matchbook -
    DATA: model 41.5% | style Leader (led 57% of runs) | runs in data 2 | last 3: 17 Jan Haydock Hurdle 15.7f Good To Soft 1/6; 10 Mar Cheltenham Hurdle 16.4f Good To Soft 1/11
    DATA for: Official rating 155, 13 lb above field average; Trainer 25% wins (4/16), last 14 days; Last-run finishing speed +2.1% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Returns from a 253-day break; Lightly raced: 2 runs in our data, so the model has little to go on; First run over fences in our data
- Sober Glory (hrs_412693498) | 6yo G | 158lb | OR 153 | draw 0 | jockey Ben Jones | trainer Philip Hobbs & Johnson White (14d 1/20) | headgear - | last run 222 days | form 41124- | MARKET 39.3% | 09:00 median 2.25 | Matchbook -
    comment: Sober Glory won two of his last five, three and four starts back, before a second two starts back and a fourth last time out, and has run over today's trip, so he is a strong threat on form. The risks are a 222-day break and a stable out of form at 1/20.
    DATA: model 25.3% | style Leader (led 63% of runs) | runs in data 4 | last 3: 7 Feb Newbury Hurdle 16.3f Heavy 1/8; 10 Mar Cheltenham Hurdle 16.4f Good To Soft 2/11; 10 Apr Aintree Hurdle 16.5f Good To Soft 4/6
    DATA for: Official rating 153, 11 lb above field average; Has won at this trip or further; Good recent finishing positions
    DATA against: Returns from a 222-day break; First run over fences in our data
- Carlenrig (hrs_47807109) | 6yo G | 158lb | OR 132 | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 19/80) | headgear - | last run 298 days | form 1/21F- | MARKET 3.4% | 09:00 median 29.00 | Matchbook -
    comment: Carlenrig won two of his last four starts, winning two starts back and four starts back with a second in between, so the form reads strongly despite a fall last time out. The risk is fitness, as he returns after 298 days off and carries 158 lb.
    DATA: model 7.9% | style Held up (led 8% of runs) | runs in data 1 | last 3: 24 Jan Doncaster Hurdle 24.4f Soft F/12
    DATA for: Trainer 24% wins (19/80), last 14 days
    DATA against: Official rating 132, 10 lb below field average; Returns from a 298-day break; Lightly raced: 1 run in our data, so the model has little to go on; Fell or unseated in 1 of its last 1 jumps runs
- Bobby's Nelson (hrs_34961878) | 7yo G | 158lb | OR 129 | draw 0 | jockey Charlie Todd | trainer Dan Skelton (14d 19/80) | headgear - | wind surgery | last run 274 days | form /2213- | MARKET 1.5% | 09:00 median 81.00 | Matchbook -
    comment: Bobby's Nelson showed decent form with a third last time out, a win two starts back and seconds before that, but he returns after 274 days off and carries 158 lb.
    DATA: model 25.3% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 8 Jan Ffos Las Hurdle 20f Heavy 1/12; 17 Feb Newbury Hurdle 20.5f Soft 3/6
    DATA for: Trainer 24% wins (19/80), last 14 days; Has won at this trip or further; Good recent finishing positions
    DATA against: Official rating 129, 13 lb below field average; Returns from a 274-day break; Lightly raced: 2 runs in our data, so the model has little to go on; First run over fences in our data

## 2:18 Ffos Las | race_id rac_32304731446 | Edwina Jones 80th Birthday Celebrations Novices' Handicap Steeple Chase
Chase | Class 5 | 2m7f177y | going Good To Soft | Turf | 15 runners | rating band 0-100 | age 4yo+
DATA pace: Lone leader - Call Your Bluff is the only habitual front-runner and may be allowed an easy lead.
- Wannabe (hrs_38667223) | 6yo G | 163lb | OR 95 | draw 0 | jockey Stan Sheppard | trainer Tom Lacey (14d 5/11) | headgear v (1st time) | last run 35 days | form 5672-U | MARKET 24.2% | 09:00 median 3.00 | Matchbook - | CHECK (skip line 2.85)
    comment: Wannabe unseated last time out after a second two starts back, and he's been without a win in his last five outings.
    DATA: model 8.9% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 3 Mar Newcastle Chase 20.1f Good To Soft 2/8; 14 Oct Ffos Las Chase 23.8f Good To Soft UR/10
    DATA for: Trainer 45% wins (5/11), last 14 days; First-time headgear
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Fell or unseated in 1 of its last 2 jumps runs
- Walk Tall (hrs_47621091) | 6yo G | 168lb | OR 100 | draw 0 | jockey Harry Cobden | trainer Joe Tizzard (14d 4/23) | headgear - | wind surgery | last run 12 days | form 6523-U | MARKET 14.5% | 09:00 median 5.00 | Matchbook -
    comment: Fit after just 12 days, Walk Tall found a third two starts back and a second three starts back before unseating last time, and he has run on today's going before. Carrying 168 lb off 100 is a stiff ask, and that is the main risk.
    DATA: model 10.9% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 22 Feb Hereford Hurdle 21.7f Soft 2/7; 4 Apr Newton Abbot Hurdle 26.5f Good 3/7; 6 Nov Hexham Chase 24f Good UR/7
    DATA for: Official rating 100, 10 lb above field average
    DATA against: Carries 9 lb more than average; Fell or unseated in 1 of its last 5 jumps runs
- Cote d'Ange (hrs_50187858) | 5yo G | 155lb | OR 87 | draw 0 | jockey Dylan Johnston | trainer Sam Thomas (14d 0/2) | headgear p (1st time) | last run 220 days | form /0834- | MARKET 12.6% | 09:00 median 6.00 | Matchbook -
    comment: Winless in his last four, Cote d'Ange is hard to fancy after 220 days off, and a fourth last time out followed by a third two starts back only goes so far under 155 lb.
    DATA: model 8.0% | style Prominent (led 29% of runs) | runs in data 3 | last 3: 12 Jan Hereford Hurdle 16.2f Soft 8/12; 22 Feb Hereford Hurdle 21.7f Soft 3/7; 12 Apr Ffos Las Hurdle 23.9f Good To Soft 4/14
    DATA for: Last-run finishing speed +2.0% vs that field (finished strongly); First-time headgear
    DATA against: Returns from a 220-day break; First run over fences in our data
- Manhattan Valley (hrs_39568319) | 6yo G | 155lb | OR 87 | draw 0 | jockey Jack Tudor | trainer Christian Williams (14d 1/9) | headgear - | last run 165 days | form 98P8-3 | MARKET 8.8% | 09:00 median 9.00 | Matchbook -
    DATA: model 6.2% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 8 Jan Ffos Las Hurdle 20f Heavy PU/12; 12 Apr Ffos Las Chase 19.4f Good To Soft 8/11; 6 Jun Hexham Chase 20.1f Good 3/9
    DATA for: Last-run finishing speed +3.1% vs that field (finished strongly)
    DATA against: Returns from a 165-day break; Pulled up in 1 of its last 3 jumps runs
- Moon Over Clyro (hrs_40899558) | 6yo G | 166lb | OR 98 | draw 0 | jockey Charlie Price | trainer Robbie Llewellyn (14d 0/2) | headgear - | last run 211 days | form 23095- | MARKET 7.1% | 09:00 median 11.00 | Matchbook -
    comment: The main risk is a 211-day absence, with 166 lb to carry.
    DATA: model 5.1% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 28 Mar Stratford Hurdle 18.7f Good 9/9; 21 Apr Ffos Las Hurdle 23.9f Good 5/12
    DATA for: Official rating 98, 8 lb above field average
    DATA against: Carries 7 lb more than average; Returns from a 211-day break; Lightly raced: 2 runs in our data, so the model has little to go on; First run over fences in our data
- Glenmuick (hrs_57718745) | 5yo G | 150lb | OR 82 | draw 0 | jockey Lilly Pinchin | trainer Charlie Longsdon (14d 3/15) | headgear tp | last run 32 days | form 792-85 | MARKET 5.1% | 09:00 median 13.00 | Matchbook -
    comment: Glenmuick is winless in his last five, with a second three starts back the lone bright spot among a fifth last time out, an eighth, a ninth and a seventh.
    DATA: model 6.6% | style Midfield (led 3% of runs) | runs in data 6 | last 3: 21 Apr Ffos Las Hurdle 23.9f Good 2/12; 20 May Ffos Las Hurdle 23.9f Good To Soft 8/8; 17 Oct Market Rasen Hurdle 23f Good 5/8 fig 71
    DATA for: Trainer 20% wins (3/15), last 14 days; Carries 9 lb less than average
    DATA against: Best recent form figure 71, 14 lb below field average; Recent figures 11 lb below its current mark (looks high in the weights); Official rating 82, 8 lb below field average; Last-run finishing speed -4.0% vs that field (faded); First run over fences in our data
- Emailandy (hrs_34238225) | 8yo G | 166lb | OR 98 | draw 0 | jockey Sean Bowen | trainer Martin Keighley (14d 3/11) | headgear p | last run 14 days | form -31P43 | MARKET 4.9% | 09:00 median 15.00 | Matchbook -
    comment: Third last time out and only 14 days ago, Emailandy arrives fresh and in rhythm, with a win four starts back and experience over today's trip and going.
    DATA: model 5.4% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 3 Oct Fontwell Chase 19.5f Good PU/6; 16 Oct Uttoxeter Chase 24f Good 4/8 fig 100; 4 Nov Chepstow Chase 23.5f Good 3/5
    DATA for: Best recent form figure 100, 15 lb above field average; Official rating 98, 8 lb above field average; Trainer 27% wins (3/11), last 14 days
    DATA against: Last-run finishing speed -6.6% vs that field (faded); Carries 7 lb more than average; Race comments mention jumping mistakes in 2 of its last 5 runs; Pulled up in 3 of its last 5 jumps runs
- Call Your Bluff (hrs_46013758) | 6yo G | 148lb | OR 80 | draw 0 | jockey Cameron Johnstone-Baker(7) | trainer Emma Lavelle (14d 3/13) | headgear t | last run 245 days | form 7832P- | MARKET 4.8% | 09:00 median 17.00 | Matchbook -
    comment: Pulled up last time out and absent for 245 days, he returns with questions to answer, though a second two starts back and a third three starts back show he can still run well, and he has run over today's trip and going.
    DATA: model 7.4% | style Leader (led 57% of runs) | runs in data 2 | last 3: 5 Feb Doncaster Hurdle 24.4f Soft 2/9; 18 Mar Huntingdon Hurdle 25f Good PU/9
    DATA for: Trainer 23% wins (3/13), last 14 days; Carries 11 lb less than average; Pace: may get an uncontested lead
    DATA against: Official rating 80, 10 lb below field average; Returns from a 245-day break; Lightly raced: 2 runs in our data, so the model has little to go on; Pulled up in 1 of its last 2 jumps runs; First run over fences in our data
- Gustoso (hrs_35388990) | 7yo G | 167lb | OR 99 | draw 0 | jockey Sam Twiston-Davies | trainer Henry Daly (14d 0/12) | headgear - | last run 35 days | form P2/6-7 | MARKET 4.1% | 09:00 median 19.00 | Matchbook -
    comment: The risk is a seventh last time out and a sixth before it, leaving him winless in his last four, with 167 lb to carry after 35 days off.
    DATA: model 5.2% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 14 Oct Wetherby Hurdle 24f Good To Firm 7/8
    DATA for: Official rating 99, 9 lb above field average
    DATA against: Trainer 0 wins from 12 runs, last 14 days; Last-run finishing speed -6.2% vs that field (faded); Carries 8 lb more than average; Lightly raced: 1 run in our data, so the model has little to go on
- Woodythewoodpecker (hrs_412694877) | 6yo G | 165lb | OR 97 | draw 0 | jockey Adam Wedge | trainer Mrs C. Williams (14d 1/19) | headgear - | last run 21 days | form 7223-P | MARKET 3.7% | 09:00 median 19.00 | Matchbook -
    comment: Pulled up last time out, Woodythewoodpecker was a third two starts back and a second three and four starts back, so he is winless in his last five but has hit the frame. He has run on today's going and has had 21 days to recover, though 165 lb is a big burden off 97.
    DATA: model 8.9% | style Prominent (led 5% of runs) | runs in data 3 | last 3: 11 Jan Fontwell Hurdle 25.8f Soft 2/11; 6 Apr Hereford Hurdle 25.5f Good 3/7; 28 Oct Newton Abbot Chase 26f Good To Soft PU/5
    DATA for: Official rating 97, 7 lb above field average
    DATA against: Carries 6 lb more than average; Pulled up in 1 of its last 3 jumps runs
- Welcheston Warrier (hrs_40942111) | 6yo G | 163lb | OR 95 | draw 0 | jockey Richie McLernon | trainer Clive Boultbee-Brooks (14d 0/5) | headgear - | last run 218 days | form 2P223- | MARKET 2.8% | 09:00 median 26.00 | Matchbook -
    comment: Third last time out, and a second two and three starts back, so Welcheston Warrier is yet to win in his last five but is rarely far away; he has run over today's trip and going, though 218 days off and 163 lb are against him.
    DATA: model 9.4% | style Midfield (led 23% of runs) | runs in data 4 | last 3: 5 Feb Lingfield Hurdle 23f Heavy 2/5; 7 Mar Hereford Hurdle 25.5f Good 2/6; 14 Apr Newton Abbot Hurdle 26.5f Good 3/6
    DATA for: Good recent finishing positions
    DATA against: Returns from a 218-day break; Pulled up in 1 of its last 4 jumps runs; First run over fences in our data
- Jack's A Legend (hrs_18582249) | 11yo G | 154lb | OR 86 | draw 0 | jockey Miss Imogen Mathias(7) | trainer John & Rhys Flint (14d 0/1) | headgear t | last run 21 days | form -7403P | MARKET 2.6% | 09:00 median 29.00 | Matchbook -
    comment: Pulled up last time out, but a third two starts back shows he can still run a race, and he's fresh enough after 21 days off and has run on today's going before.
    DATA: model 6.4% | style Prominent (led 38% of runs) | runs in data 6 | last 3: 24 Jul Uttoxeter Chase 24f Good 12/14; 17 Oct Stratford Chase 22.5f Good 3/7 fig 85; 28 Oct Huntingdon Chase 23.5f Good PU/6
    DATA against: Race comments mention jumping mistakes in 2 of its last 5 runs; Pulled up in 1 of its last 5 jumps runs; Aged 11, older than most of this field
- Shuil Rocco (hrs_52709034) | 5yo G | 160lb | OR 92 | draw 0 | jockey Shane Fenelon(5) | trainer Mickey Bowen (14d 5/18) | headgear p (1st time) | last run 185 days | form 3704-6 | MARKET 2.5% | 09:00 median 26.00 | Matchbook -
    comment: Shuil Rocco is winless in his last five, with a sixth last time out and a fourth two starts back, and he returns after 185 days off, so fitness is a question. He carries 160 lb off a mark of 92, though he has run on today's going before.
    DATA: model 2.0% | style Midfield (led 4% of runs) | runs in data 4 | last 3: 12 Apr Ffos Las Hurdle 20f Good To Soft 10/11; 24 Apr Chepstow Hurdle 19.5f Good 4/8; 17 May Stratford Hurdle 22f Good To Firm 6/6
    DATA for: Trainer 28% wins (5/18), last 14 days; First-time headgear
    DATA against: Returns from a 185-day break; First run over fences in our data
- Rubys Legacy (hrs_40373865) | 7yo G | 158lb | OR 90 | draw 0 | jockey Jay Tidball(5) | trainer David Rees (14d 0/0) | headgear t | last run 439 days | form P4/26- | MARKET 1.2% | 09:00 median 51.00 | Matchbook -
    comment: Rubys Legacy was runner-up two starts back and a sixth last time out, yet he's yet to win in his last four and returns after 439 days off, which is a big question.
    DATA: model 5.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 439-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Lady Pacifico (hrs_22864401) | 8yo M | 142lb | OR 70 | draw 0 | jockey Tabitha Worsley | trainer Georgie Howell (14d 0/0) | headgear tb | last run 637 days | form 655P4/ | MARKET 1.0% | 09:00 median 81.00 | Matchbook -
    comment: Lady Pacifico is winless in her last five, with a pulled up two starts back and nothing better than a fourth last time out, and a 637-day absence adds to the doubts.
    DATA: model 4.1% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Carries 17 lb less than average
    DATA against: Official rating 70, 20 lb below field average; Returns from a 637-day break; Lightly raced: 0 runs in our data, so the model has little to go on

## 2:48 Ffos Las | race_id rac_32304733383 | Support Your Oncourse Bookmakers Maiden Hurdle Race (GBB Race)
Hurdle | Class 4 | 2m4f | going Good To Soft | Turf | 13 runners | rating band - | age 4yo+
DATA pace: Lone leader - Merry Away is the only habitual front-runner and may be allowed an easy lead.
- Merry Away (hrs_58745876) | 5yo G | 158lb | OR - | draw 0 | jockey Ben Jones | trainer Ben Pauling (14d 3/23) | headgear - | last run 221 days | form 314- | MARKET 62.7% | 09:00 median 1.29 | Matchbook -
    DATA: model 16.9% | style Leader (led 57% of runs) | runs in data 2 | last 3: 8 Mar Warwick NH Flat 16f Good To Soft 1/10; 11 Apr Aintree NH Flat 16.9f Good To Soft 4/20
    DATA for: Last-run finishing speed +11.2% vs that field (finished strongly); Pace: may get an uncontested lead
    DATA against: Returns from a 221-day break; Lightly raced: 2 runs in our data, so the model has little to go on; First run over hurdles in our data
- Valiant Soldier (hrs_60250120) | 5yo G | 158lb | OR - | draw 0 | jockey Harry Cobden | trainer Joe Tizzard (14d 4/23) | headgear - | last run 20 days | form 554-3 | MARKET 12.5% | 09:00 median 5.50 | Matchbook -
    DATA: model 13.5% | style Prominent (led 3% of runs) | runs in data 4 | last 3: 5 Mar Wincanton NH Flat 15.2f Good To Soft 5/12; 26 Mar Chepstow NH Flat 16.1f Good To Soft 4/10; 29 Oct Ffos Las Hurdle 16f Heavy 3/9 fig 111
    DATA for: Best recent form figure 111, 14 lb above field average
- Funny Hunny (hrs_17392037208) | 6yo M | 151lb | OR - | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 19/80) | headgear - | last run 27 days | form 32/44 | MARKET 6.5% | 09:00 median 11.00 | Matchbook -
    DATA: model 7.5% | style Held up (led 8% of runs) | runs in data 2 | last 3: 7 Oct Worcester Hurdle 16f Good 4/12; 22 Oct Ffos Las Hurdle 20f Soft 4/8 fig 94
    DATA for: Trainer 24% wins (19/80), last 14 days
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Doagh (hrs_17395447818) | 5yo G | 158lb | OR - | draw 0 | jockey Sean Bowen | trainer Mickey Bowen (14d 5/18) | headgear - | last run 46 days | form 1 | MARKET 6.0% | 09:00 median 11.00 | Matchbook -
    DATA: model 5.7% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 28% wins (5/18), last 14 days
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Karamel Biscuits (hrs_17395540645) | 6yo G | 158lb | OR - | draw 0 | jockey Charlie Deutsch | trainer Venetia Williams (14d 0/3) | headgear - | last run - days | form - | MARKET 3.2% | 09:00 median 23.00 | Matchbook -
    DATA: model 5.7% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Big John Ollie (hrs_57758435) | 5yo G | 158lb | OR - | draw 0 | jockey Charlie Todd | trainer Dan Skelton (14d 19/80) | headgear - | last run 17 days | form 32-0 | MARKET 1.6% | 09:00 median 41.00 | Matchbook -
    DATA: model 12.6% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 27 Jan Chepstow NH Flat 16.1f Soft 2/10; 1 Nov Worcester Hurdle 16f Good To Soft 11/16 fig 95
    DATA for: Trainer 24% wins (19/80), last 14 days
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Mistral du Chenet (hrs_56559510) | 4yo G | 157lb | OR - | draw 0 | jockey Jonathan Burke | trainer Toby Bulgin (14d 0/2) | headgear - | last run 20 days | form 0-5 | MARKET 1.4% | 09:00 median 41.00 | Matchbook -
    DATA: model 10.2% | style Prominent (led 38% of runs) | runs in data 2 | last 3: 21 Mar Newbury NH Flat 16.3f Good To Soft 16/20; 29 Oct Ffos Las NH Flat 16f Heavy 5/6 fig 93
    DATA against: Best recent form figure 93, 4 lb below field average; Last-run finishing speed -4.4% vs that field (faded); Lightly raced: 2 runs in our data, so the model has little to go on; First run over hurdles in our data
- Skibidirizz (hrs_17393567289) | 4yo G | 157lb | OR - | draw 0 | jockey Robert Dunne | trainer Dan Skelton (14d 19/80) | headgear - | last run 24 days | form 66 | MARKET 1.2% | 09:00 median 101.00 | Matchbook -
    DATA: model 4.3% | style Held up (led 8% of runs) | runs in data 2 | last 3: 11 Oct Chepstow Hurdle 16.1f Good To Soft 6/6; 25 Oct Market Rasen Hurdle 16.5f Good To Soft 6/11
    DATA for: Trainer 24% wins (19/80), last 14 days
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Cobbler's Lad (hrs_63357378) | 4yo G | 157lb | OR - | draw 0 | jockey Sam Twiston-Davies | trainer Henry Daly (14d 0/12) | headgear - | last run 226 days | form 6- | MARKET 1.1% | 09:00 median 51.00 | Matchbook -
    DATA: model 13.6% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 6 Apr Hereford NH Flat 16.2f Good 6/11
    DATA against: Trainer 0 wins from 12 runs, last 14 days; Returns from a 226-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Handfulofpromises (hrs_39431469) | 7yo M | 151lb | OR - | draw 0 | jockey Callum Pritchard | trainer Sheila Lewis (14d 1/6) | headgear - | last run 27 days | form 22/6 | MARKET 1.1% | 09:00 median 51.00 | Matchbook -
    DATA: model 2.3% | style Held up (led 8% of runs) | runs in data 1 | last 3: 22 Oct Ffos Las Hurdle 20f Soft 6/8 fig 92
    DATA against: Best recent form figure 92, 5 lb below field average; Lightly raced: 1 run in our data, so the model has little to go on
- One More Chrome (hrs_42452039) | 4yo G | 157lb | OR - | draw 0 | jockey Liam Harrison | trainer Dan Skelton (14d 19/80) | headgear - | last run 27 days | form 07 | MARKET 1.0% | 09:00 median 81.00 | Matchbook -
    DATA: model 2.7% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 7 Oct Worcester Hurdle 16f Good 10/12; 22 Oct Ffos Las Hurdle 16f Soft 7/11 fig 97
    DATA for: Trainer 24% wins (19/80), last 14 days
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Power of Authority (hrs_17394950307) | 4yo G | 157lb | OR - | draw 0 | jockey Sean Houlihan | trainer Sheila Lewis (14d 1/6) | headgear - | last run 13 days | form F-0 | MARKET 0.9% | 09:00 median 67.00 | Matchbook -
    DATA: model 2.2% | style Held up (led 8% of runs) | runs in data 1 | last 3: 5 Nov Newbury NH Flat 16.5f Good To Soft 11/11
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Ignite The Spark (hrs_17394111735) | 4yo G | 157lb | OR - | draw 0 | jockey Richie McLernon | trainer Barry Murphy (14d 0/4) | headgear t | last run 3 days | form 4-PP | MARKET 0.8% | 09:00 median 101.00 | Matchbook -
    DATA: model 2.8% | style Held up (led 8% of runs) | runs in data 2 | last 3: 29 Oct Ffos Las Hurdle 20f Heavy PU/11; 15 Nov Fontwell Hurdle 17.5f Soft PU/13
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Pulled up in 2 of its last 2 jumps runs

## 3:18 Ffos Las | race_id rac_32304735320 | 3A's Leisure Novices' Handicap Hurdle Race
Hurdle | Class 5 | 2m4f | going Good To Soft | Turf | 11 runners | rating band 0-100 | age 4yo+
DATA pace: Lone leader - No Boundaries is the only habitual front-runner and may be allowed an easy lead.
- For Old Times Sake (hrs_49974274) | 5yo G | 149lb | OR 81 | draw 0 | jockey Harry Cobden | trainer Neil Mulholland (14d 5/23) | headgear - | last run 34 days | form 869P-6 | MARKET 30.7% | 09:00 median 2.75 | Matchbook -
    comment: For Old Times Sake has been well beaten lately, with a sixth last time out, a pulled up two starts back and a ninth three starts back, and he is winless in his last five.
    DATA: model 12.0% | style Midfield (led 23% of runs) | runs in data 6 | last 3: 11 Mar Huntingdon Hurdle 20.7f Good 9/14; 6 Apr Hereford Hurdle 16.2f Good PU/10; 15 Oct Fontwell Hurdle 17.5f Good To Soft 6/9 fig 71
    DATA for: Trainer 22% wins (5/23), last 14 days; Carries 7 lb less than average
    DATA against: Best recent form figure 71, 14 lb below field average; Recent figures 10 lb below its current mark (looks high in the weights); Official rating 81, 7 lb below field average; Poor recent finishing positions; Pulled up in 1 of its last 5 jumps runs
- No Boundaries (hrs_57909670) | 4yo G | 167lb | OR 100 | draw 0 | jockey Ciaran Gethings | trainer Mrs Jane Williams (14d 2/8) | headgear - | last run 28 days | form 424-4 | MARKET 16.4% | 09:00 median 5.00 | Matchbook -
    comment: He has run over today's trip and on the going before, though he is yet to win in his last four starts.
    DATA: model 15.0% | style Leader (led 38% of runs) | runs in data 2 | last 3: 22 Feb Hereford Hurdle 16.2f Soft 4/7; 21 Oct Worcester Hurdle 20f Good To Soft 4/10 fig 97
    DATA for: Best recent form figure 97, 12 lb above field average; Official rating 100, 12 lb above field average; Trainer 25% wins (2/8), last 14 days; Last-run finishing speed +2.8% vs that field (finished strongly); Pace: may get an uncontested lead
    DATA against: Carries 11 lb more than average; Lightly raced: 2 runs in our data, so the model has little to go on
- Wispit Twob (hrs_58596622) | 4yo F | 154lb | OR 87 | draw 0 | jockey Sean Bowen | trainer Martin Keighley (14d 3/11) | headgear p | last run 28 days | form 0P-P81 | MARKET 13.4% | 09:00 median 6.00 | Matchbook -
    comment: Wispit Twob won last time out, but that came after an eighth, two pulled-up efforts and an unplaced run, so the form is patchy.
    DATA: model 9.7% | style Midfield (led 4% of runs) | runs in data 6 | last 3: 4 Sep Worcester Hurdle 23f Good PU/10; 16 Sep Kelso Hurdle 18.1f Good To Firm 8/8; 21 Oct Worcester Hurdle 20f Good To Soft 1/10 fig 83
    DATA for: Trainer 27% wins (3/11), last 14 days; Last-run finishing speed +5.3% vs that field (finished strongly); Has won at this trip or further
    DATA against: Pulled up in 2 of its last 5 jumps runs
- Yorgunnabeplucky (hrs_39959423) | 6yo G | 151lb | OR 83 | draw 0 | jockey Adam Wedge | trainer Mrs C. Williams (14d 1/19) | headgear - | last run 30 days | form 434P-2 | MARKET 10.4% | 09:00 median 8.00 | Matchbook -
    comment: Yorgunnabeplucky arrives in decent shape after a second last time out, and he has run over today's trip and going before, but he is winless in his last five and was pulled up two starts back.
    DATA: model 10.8% | style Midfield (led 5% of runs) | runs in data 3 | last 3: 23 Jan Warwick Chase 25.5f Good To Soft 4/8; 13 Mar Fakenham Chase 24.2f Good To Soft PU/3; 19 Oct Plumpton Chase 20f Good 2/4 fig 79
    DATA against: Best recent form figure 79, 6 lb below field average; Race comments mention jumping mistakes in 2 of its last 3 runs; Pulled up in 1 of its last 3 jumps runs; First run over hurdles in our data
- Neeps And Tatties (hrs_42226317) | 7yo M | 152lb | OR 84 | draw 0 | jockey Jonathan Burke | trainer Richard Phillips (14d 0/0) | headgear h | last run 211 days | form 74724- | MARKET 7.0% | 09:00 median 12.00 | Matchbook -
    comment: Fourth last time out and a second two starts back suggest Neeps And Tatties is in reasonable shape, and she has run over today's trip and going before, but she is yet to win in her last five and returns after 211 days off.
    DATA: model 11.9% | style Prominent (led 29% of runs) | runs in data 5 | last 3: 7 Mar Hereford Hurdle 19.7f Good 7/11; 16 Mar Ffos Las Hurdle 20f Soft 2/6; 21 Apr Ffos Las Hurdle 20f Good 4/7
    DATA against: Returns from a 211-day break
- Blazing Saint (hrs_59460926) | 5yo G | 153lb | OR 85 | draw 0 | jockey Jack Tudor | trainer Christian Williams (14d 1/9) | headgear - | last run 140 days | form 96P-19 | MARKET 6.4% | 09:00 median 12.00 | Matchbook -
    comment: Blazing Saint is hard to fancy after a ninth last time out, a 140-day absence and a pulled up three starts back, though he did win two starts back and has run on today's going before.
    DATA: model 8.9% | style Held up (led 5% of runs) | runs in data 4 | last 3: 18 Feb Southwell Hurdle 20.4f Soft PU/13; 11 May Southwell Hurdle 15.8f Good 1/13; 1 Jul Worcester Hurdle 16f Good 9/9
    DATA against: Last-run finishing speed -12.4% vs that field (faded); Returns from a 140-day break; Pulled up in 1 of its last 4 jumps runs
- Teletime (hrs_61910625) | 5yo G | 142lb | OR 69 | draw 0 | jockey Bradley Harris(3) | trainer Neil Mulholland (14d 5/23) | headgear - | last run 40 days | form 60-09 | MARKET 5.1% | 09:00 median 17.00 | Matchbook -
    comment: Teletime is hard to fancy, having finished a ninth last time out and been unplaced in the two runs before that, so he is winless in his last four starts after a 40-day break.
    DATA: model 1.7% | style Midfield (led 4% of runs) | runs in data 4 | last 3: 24 Apr Chepstow Hurdle 16.1f Good 10/12; 22 May Worcester Hurdle 16f Good 10/10; 9 Oct Chepstow Hurdle 16.1f Good To Soft 9/10
    DATA for: Trainer 22% wins (5/23), last 14 days; Carries 14 lb less than average
    DATA against: Official rating 69, 19 lb below field average; Last-run finishing speed -7.4% vs that field (faded); Poor recent finishing positions
- Billy Butcher (hrs_38073980) | 8yo G | 156lb | OR 88 | draw 0 | jockey Lee Edwards | trainer Dave Roberts (14d 0/2) | headgear h (1st time) | last run 10 days | form 64/62F | MARKET 4.8% | 09:00 median 17.00 | Matchbook -
    DATA: model 12.9% | style Midfield (led 5% of runs) | runs in data 3 | last 3: 10 Sep Worcester Hurdle 16f Good 6/12; 7 Oct Worcester Hurdle 16f Good 2/10; 8 Nov Ffos Las Hurdle 20f Soft F/8
    DATA for: First-time headgear
    DATA against: Fell or unseated in 1 of its last 3 jumps runs; Aged 8, older than most of this field
- Bahati Bahati (hrs_51618938) | 6yo G | 165lb | OR 97 | draw 0 | jockey Troy Walsh(7) | trainer Gordon Treacy (14d 0/0) | headgear - | last run 196 days | form 6P63-8 | MARKET 2.0% | 09:00 median 41.00 | Matchbook -
    comment: Bahati Bahati was beaten into eighth last time and returns after 196 days off, though he has a third two starts back and has run on today's going before.
    DATA: model 6.9% | style Midfield (led 23% of runs) | runs in data 4 | last 3: 23 Mar Wincanton Hurdle 15.2f Good 6/12; 12 Apr Ffos Las Hurdle 15.8f Good To Soft 3/12; 6 May Fontwell Hurdle 17.7f Good 8/14
    DATA for: Official rating 97, 9 lb above field average
    DATA against: Carries 9 lb more than average; Returns from a 196-day break; Pulled up in 1 of its last 4 jumps runs
- Lara K (hrs_17392410602) | 5yo M | 157lb | OR 89 | draw 0 | jockey Conor Ring | trainer Mrs C. Williams (14d 1/19) | headgear - | last run 27 days | form 7673 | MARKET 1.9% | 09:00 median 41.00 | Matchbook -
    comment: Lara K bounced back with a third last time out, and she's had 27 days to recover, with the distance not new to her.
    DATA: model 2.2% | style Held up (led 3% of runs) | runs in data 4 | last 3: 26 Sep Market Rasen Hurdle 16.6f Good 6/9; 4 Oct Uttoxeter Hurdle 15.8f Good 7/8; 22 Oct Ffos Las Hurdle 20f Soft 3/8 fig 95
    DATA for: Best recent form figure 95, 10 lb above field average; Recent figures 6 lb above its current mark (looks well handicapped)
- Cauvicourt (hrs_39488274) | 6yo G | 168lb | OR 100 | draw 0 | jockey James Best | trainer Nikki Evans (14d 0/1) | headgear - | last run 586 days | form 89232/ | MARKET 1.8% | 09:00 median 34.00 | Matchbook -
    DATA: model 7.9% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Official rating 100, 12 lb above field average
    DATA against: Carries 12 lb more than average; Returns from a 586-day break; Lightly raced: 0 runs in our data, so the model has little to go on

## 3:48 Ffos Las | race_id rac_32304737257 | Welsh Cottage Christmas Cakes Handicap Steeple Chase
Chase | Class 5 | 2m3f83y | going Good To Soft | Turf | 10 runners | rating band 0-100 | age 4yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Unleash The Beast (hrs_39109602) | 7yo G | 168lb | OR 98 | draw 0 | jockey Liam Harrison | trainer Fergal O'Brien (14d 2/26) | headgear - | last run 270 days | form 27/76- | MARKET 17.2% | 09:00 median 4.50 | Matchbook - | CHECK (skip line 4.27)
    comment: Unleash The Beast has run over today's trip and was second four starts back, though he's been well held in his last three outings.
    DATA: model 25.8% | style Held up (led 8% of runs) | runs in data 1 | last 3: 21 Feb Newcastle Hurdle 20.3f Good To Soft 6/15
    DATA for: Official rating 98, 13 lb above field average
    DATA against: Carries 13 lb more than average; Returns from a 270-day break; Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Seasett (hrs_21995512) | 8yo G | 158lb | OR 88 | draw 0 | jockey Sean Bowen | trainer Mickey Bowen (14d 5/18) | headgear tp | wind surgery | last run 448 days | form 9/562- | MARKET 14.2% | 09:00 median 6.00 | Matchbook -
    comment: The main risk is a 448-day absence, plus 158 lb to carry.
    DATA: model 8.1% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 28% wins (5/18), last 14 days
    DATA against: Returns from a 448-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Devilsrollthedice (hrs_46697154) | 6yo G | 147lb | OR 77 | draw 0 | jockey Sean Houlihan | trainer Gordon Treacy (14d 0/0) | headgear p | last run 220 days | form 86PP7- | MARKET 12.9% | 09:00 median 6.50 | Matchbook -
    comment: Devilsrollthedice is hard to fancy, winless in his last five with a seventh last time out, two pulled-up efforts before that and 220 days off the track.
    DATA: model 7.3% | style Midfield (led 3% of runs) | runs in data 4 | last 3: 29 Jan Wincanton Hurdle 19.8f Heavy PU/11; 6 Mar Exeter Chase 24.2f Good To Soft PU/9; 12 Apr Ffos Las Chase 19.4f Good To Soft 7/11
    DATA for: Carries 8 lb less than average
    DATA against: Official rating 77, 8 lb below field average; Poor recent finishing positions; Returns from a 220-day break; Pulled up in 2 of its last 4 jumps runs
- Pooroldmackley (hrs_39414711) | 7yo G | 148lb | OR 78 | draw 0 | jockey Adam Wedge | trainer Mrs C. Williams (14d 1/19) | headgear p | last run 28 days | form -4423P | MARKET 11.1% | 09:00 median 8.00 | Matchbook -
    comment: Pooroldmackley was pulled up last time out and is winless in his last five, which makes him hard to fancy, though a third and a second two and three starts back show he can run a bit.
    DATA: model 9.5% | style Held up (led 4% of runs) | runs in data 7 | last 3: 20 Sep Plumpton Hurdle 25f Good 2/6; 28 Sep Newton Abbot Hurdle 26.5f Good 3/7; 21 Oct Fontwell Chase 26f Soft PU/8
    DATA for: Carries 7 lb less than average
    DATA against: Official rating 78, 7 lb below field average; Pulled up in 1 of its last 5 jumps runs; Pace: steady gallop likely, hard to come from off the pace
- Leech (hrs_38580598) | 7yo G | 151lb | OR 81 | draw 0 | jockey James Turner(5) | trainer Mrs C. Williams (14d 1/19) | headgear - | last run 32 days | form 3936-4 | MARKET 10.8% | 09:00 median 8.00 | Matchbook -
    comment: The main risk is a 32-day break and a winless recent run.
    DATA: model 6.9% | style Midfield (led 3% of runs) | runs in data 4 | last 3: 30 Jan Ffos Las Chase 16f Heavy 3/6; 12 Feb Leicester Chase 15.9f Heavy 6/8; 17 Oct Newton Abbot Chase 16.5f Good 4/5 fig 78
- Just Aidan (hrs_34948494) | 7yo G | 157lb | OR 87 | draw 0 | jockey James Best | trainer Harriet Dickin (14d 0/4) | headgear p | last run 15 days | form U153-5 | MARKET 9.4% | 09:00 median 9.00 | Matchbook -
    comment: Just Aidan arrives fresh from a run 15 days ago, a fifth last time out, with a third two starts back and a win four starts back, and he has run over today's trip and going.
    DATA: model 9.3% | style Prominent (led 3% of runs) | runs in data 6 | last 3: 18 Mar Hereford Chase 16f Good 5/8; 12 Apr Ffos Las Chase 19.4f Good To Soft 3/11; 3 Nov Lingfield Hurdle 19.5f Good 5/9 fig 79
    DATA against: Recent figures 8 lb below its current mark (looks high in the weights); Fell or unseated in 1 of its last 5 jumps runs
- Everyonesacritic (hrs_35150528) | 7yo G | 158lb | OR 88 | draw 0 | jockey Miss Eleanor Williams(7) | trainer Mrs C. Williams (14d 1/19) | headgear - | last run 28 days | form 3315-3 | MARKET 8.3% | 09:00 median 10.00 | Matchbook -
    DATA: model 11.7% | style Prominent (led 5% of runs) | runs in data 5 | last 3: 11 Feb Hereford Chase 20.9f Heavy 1/10; 26 Feb Ludlow Chase 23.8f Good To Soft 5/8; 21 Oct Fontwell Chase 18f Soft 3/5 fig 83
    DATA for: Has won at this trip or further; Good recent finishing positions
- Owl of Athens (hrs_38217676) | 7yo G | 157lb | OR 87 | draw 0 | jockey Conor Ring | trainer Mrs C. Williams (14d 1/19) | headgear - | last run 27 days | form 5781-F | MARKET 5.8% | 09:00 median 15.00 | Matchbook -
    comment: Fell last time out, but he won two starts back and has run over today's trip, while 157 lb and an eighth and seventh before that temper the appeal.
    DATA: model 9.7% | style Midfield (led 5% of runs) | runs in data 3 | last 3: 15 Jan Ludlow Chase 20.1f Good To Soft 8/12; 19 Feb Huntingdon Chase 19.9f Heavy 1/6; 22 Oct Ffos Las Chase 19.5f Soft F/9
    DATA for: Has won at this trip or further
    DATA against: Race comments mention jumping mistakes in 2 of its last 3 runs; Fell or unseated in 1 of its last 3 jumps runs
- Disco Davis (hrs_35054453) | 7yo G | 158lb | OR 88 | draw 0 | jockey Lee Edwards | trainer Sarah-Jayne Davies (14d 0/2) | headgear p | last run 37 days | form 3P65P4 | MARKET 5.5% | 09:00 median 15.00 | Matchbook -
    DATA: model 3.9% | style Prominent (led 3% of runs) | runs in data 8 | last 3: 8 Sep Bangor-on-Dee Chase 20.3f Good 5/5; 25 Sep Worcester Chase 20f Good PU/12; 12 Oct Worcester Chase 20f Good 4/9
    DATA against: Pulled up in 2 of its last 5 jumps runs
- Bahtiyar (hrs_31835195) | 8yo G | 148lb | OR 78 | draw 0 | jockey Miss Clara Brewitt(7) | trainer Max Young (14d 0/2) | headgear tp | last run 15 days | form 634523 | MARKET 4.8% | 09:00 median 17.00 | Matchbook -
    comment: Bahtiyar is winless in his last six, though a third last time out and a second two starts back show he's competitive, and he's fresh from a 15-day break with experience of today's trip and going.
    DATA: model 7.8% | style Held up (led 4% of runs) | runs in data 11 | last 3: 5 Oct Stratford Chase 22.6f Good To Firm 5/9; 17 Oct Stratford Chase 22.5f Good 2/7 fig 78; 3 Nov Warwick Chase 25.5f Good 3/3 fig 74
    DATA for: Good recent finishing positions; Carries 7 lb less than average
    DATA against: Official rating 78, 7 lb below field average; Pace: steady gallop likely, hard to come from off the pace
