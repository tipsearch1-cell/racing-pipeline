# Card review packet: Market Rasen, 2026-11-26

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
{"meeting": "market_rasen", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 11:54 Market Rasen | race_id rac_32305605033 | PricedUp Bet 'National Hunt' Novices' Hurdle Race (GBB Race)
Hurdle | Class 4 | 2m0f125y | going Good To Soft | Turf | 8 runners | rating band - | age 4yo+
DATA pace: Even - Two likely leaders (Jetbob, Louxor de Grugy). A fair, even gallop is most likely.
- Cooltobecareless (hrs_50188859) | 5yo G | 161lb | OR 129 | draw 0 | jockey Tristan Durrell | trainer Dan Skelton (14d 21/94) | headgear - | last run 34 days | form 210-13 | MARKET 56.3% | 09:00 median 1.57 | Matchbook -
    DATA: model 42.8% | style Prominent (led 8% of runs) | runs in data 4 | last 3: 11 Apr Aintree NH Flat 16.9f Good To Soft 12/20; 9 Oct Chepstow Hurdle 16.1f Good To Soft 1/10; 23 Oct Cheltenham Hurdle 16.5f Good To Soft 3/10 fig 122
    DATA for: Trainer 22% wins (21/94), last 14 days; Has won at this trip or further; Good recent finishing positions
- Keeptheflagflying (hrs_17395399840) | 4yo G | 154lb | OR - | draw 0 | jockey Harry Cobden | trainer Ben Pauling (14d 8/41) | headgear - | last run 298 days | form 3- | MARKET 17.1% | 09:00 median 4.33 | Matchbook -
    DATA: model 6.8% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 298-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Stars Aligning (hrs_62549214) | 4yo G | 154lb | OR - | draw 0 | jockey Tom Bellamy | trainer Alan King (14d 4/25) | headgear h | last run 257 days | form 2- | MARKET 10.8% | 09:00 median 7.00 | Matchbook -
    DATA: model 14.9% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 14 Mar Kempton NH Flat 16f Good 2/10
    DATA for: Last-run finishing speed +7.1% vs that field (finished strongly)
    DATA against: Returns from a 257-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Louxor de Grugy (hrs_61242573) | 5yo G | 154lb | OR - | draw 0 | jockey Sean Bowen | trainer Olly Murphy (14d 10/51) | headgear - | last run 238 days | form 43- | MARKET 10.0% | 09:00 median 8.00 | Matchbook -
    DATA: model 15.5% | style Leader (led 57% of runs) | runs in data 2 | last 3: 2 Feb Kempton NH Flat 16f Good To Soft 4/14; 2 Apr Chepstow NH Flat 16.1f Good To Soft 3/11
    DATA for: Last-run finishing speed +6.9% vs that field (finished strongly)
    DATA against: Returns from a 238-day break; Lightly raced: 2 runs in our data, so the model has little to go on; First run over hurdles in our data
- Wisebob (hrs_17396035027) | 6yo G | 154lb | OR - | draw 0 | jockey Danny McMenamin | trainer Joel Parkinson & Sue Smith (14d 1/13) | headgear - | last run - days | form - | MARKET 2.3% | 09:00 median 34.00 | Matchbook -
    DATA: model 6.8% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Jetbob (hrs_49974491) | 7yo G | 154lb | OR - | draw 0 | jockey Ben Poste | trainer Rosemary Gasson (14d 0/2) | headgear ht (1st time) | last run 31 days | form P61-2F | MARKET 1.8% | 09:00 median 46.00 | Matchbook -
    DATA: model 8.0% | style Leader (led 57% of runs) | runs in data 3 | last 3: 1 May Punchestown Chase 20.2f Yielding 1/13; 28 Jun Uttoxeter Hurdle 19.9f Good 2/4; 26 Oct Hereford Hurdle 19.5f Good To Firm RO/6
    DATA for: Has won at this trip or further; First-time headgear
    DATA against: Fell or unseated in 1 of its last 3 jumps runs
- Tyrrhenus (hrs_50154720) | 6yo G | 154lb | OR - | draw 0 | jockey Kielan Woods | trainer Dan Skelton (14d 21/94) | headgear - | last run 35 days | form 8/6 | MARKET 1.0% | 09:00 median 81.00 | Matchbook -
    DATA: model 3.6% | style Unknown | runs in data 1 | last 3: 22 Oct Ffos Las Hurdle 16f Soft 6/10
    DATA for: Trainer 22% wins (21/94), last 14 days
    DATA against: Last-run finishing speed -2.3% vs that field (faded); Lightly raced: 1 run in our data, so the model has little to go on
- Equi Libre (hrs_61874456) | 4yo G | 154lb | OR - | draw 0 | jockey Charlie Todd | trainer Dan Skelton (14d 21/94) | headgear h | last run 14 days | form 3-PR7U | MARKET 0.8% | 09:00 median 101.00 | Matchbook -
    DATA: model 1.7% | style Held up (led 4% of runs) | runs in data 6 | last 3: 16 Oct Uttoxeter Hurdle 16f Good RO/10; 25 Oct Market Rasen Hurdle 16.5f Good To Soft 7/11; 12 Nov Market Rasen Hurdle 16.5f Good To Soft UR/10
    DATA for: Trainer 22% wins (21/94), last 14 days
    DATA against: Poor recent finishing positions; Fell or unseated in 2 of its last 4 jumps runs; Pulled up in 1 of its last 4 jumps runs

## 12:29 Market Rasen | race_id rac_32305606970 | PricedUp Now With Best Odds Handicap Hurdle Race
Hurdle | Class 5 | 2m4f139y | going Good To Soft | Turf | 10 runners | rating band 0-100 | age 3yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Midnight Bella (hrs_58535281) | 5yo M | 159lb | OR 91 | draw 0 | jockey Danny McMenamin | trainer Joel Parkinson & Sue Smith (14d 1/13) | headgear - | wind surgery | last run 23 days | form 0692-U | MARKET 24.0% | 09:00 median 3.50 | Matchbook - | CHECK (skip line 3.32)
    DATA: model 12.7% | style Prominent (led 23% of runs) | runs in data 4 | last 3: 17 Feb Market Rasen Hurdle 16.6f Soft 9/9; 3 Mar Newcastle Hurdle 20.3f Good To Soft 2/12; 3 Nov Sedgefield Hurdle 20f Good UR/5
    DATA against: Carries 6 lb more than average; Fell or unseated in 1 of its last 4 jumps runs
- Born Like Me (hrs_50936081) | 5yo G | 159lb | OR 91 | draw 0 | jockey Peter Kavanagh | trainer Joel Parkinson & Sue Smith (14d 1/13) | headgear - | last run 129 days | form 40-542 | MARKET 15.7% | 09:00 median 5.50 | Matchbook -
    comment: Born Like Me arrives on the back of a second last time out, with a fourth and a fifth before that, and he has run over today's trip and going before. He is yet to win in recent starts, and 129 days off plus 159 lb is the main risk.
    DATA: model 20.2% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 19 May Hexham Hurdle 20.1f Good 5/10; 12 Jun Market Rasen Hurdle 20.6f Good 4/7; 20 Jul Cartmel Hurdle 22.1f Good 2/9
    DATA against: Carries 6 lb more than average; Returns from a 129-day break
- Gilbertina (hrs_22064749) | 9yo M | 161lb | OR 93 | draw 0 | jockey Charlie Hammond | trainer Nick Kent (14d 0/3) | headgear t | last run 19 days | form 344-87 | MARKET 12.0% | 09:00 median 7.00 | Matchbook -
    comment: Gilbertina brings a third and two fourths in her last five, and she has run over today's trip and going before, back just 19 days after a seventh.
    DATA: model 9.4% | style Prominent (led 5% of runs) | runs in data 6 | last 3: 13 Apr Fakenham Chase 24.2f Good 4/5; 16 May Bangor-on-Dee Chase 24.1f Good 8/10; 7 Nov Uttoxeter Hurdle 20f Good 7/9 fig 88
    DATA for: Best recent form figure 88, 8 lb above field average
    DATA against: Carries 8 lb more than average; Race comments mention jumping mistakes in 2 of its last 5 runs; Aged 9, older than most of this field
- Present de Vango (hrs_32682510) | 8yo G | 156lb | OR 88 | draw 0 | jockey H. J. Horgan(5) | trainer Olly Murphy (14d 10/51) | headgear - | last run 1127 days | form 45550/ | MARKET 9.8% | 09:00 median 9.00 | Matchbook -
    comment: The big risk is a 1127-day absence, and he carries 156 lb.
    DATA: model 8.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 1127-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Eskimo Sam (hrs_43163729) | 7yo M | 150lb | OR 82 | draw 0 | jockey Lee Edwards | trainer Alastair Ralph (14d 0/8) | headgear ht | last run 25 days | form /56-27 | MARKET 9.3% | 09:00 median 9.00 | Matchbook -
    comment: Eskimo Sam has run over today's trip and going, and a second two starts back shows she can get involved, but she's winless in her last four and was seventh last time out.
    DATA: model 9.9% | style Held up (led 5% of runs) | runs in data 4 | last 3: 4 Apr Newton Abbot Hurdle 16.8f Good 6/7; 16 May Uttoxeter Hurdle 19.9f Good 2/12; 1 Nov Worcester Hurdle 23f Good To Soft 7/9
    DATA against: Official rating 82, 7 lb below field average; Trainer 0 wins from 8 runs, last 14 days; Last-run finishing speed -4.7% vs that field (faded); Pace: steady gallop likely, hard to come from off the pace
- Rose's Dart (hrs_47577334) | 5yo M | 168lb | OR 100 | draw 0 | jockey Jamie Hamilton | trainer Michael & David Easterby (14d 1/11) | headgear t | last run 227 days | form 60716- | MARKET 9.2% | 09:00 median 9.50 | Matchbook -
    comment: The main risk is a 227-day absence after a sixth last time out.
    DATA: model 13.1% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 27 Jan Newcastle Hurdle 20.3f Soft 7/7; 15 Mar Market Rasen Hurdle 18.6f Good To Soft 1/5; 13 Apr Hexham Hurdle 16.2f Good 6/8
    DATA for: Official rating 100, 11 lb above field average
    DATA against: Carries 15 lb more than average; Returns from a 227-day break
- Grand Scheme (hrs_21341523) | 8yo G | 149lb | OR 81 | draw 0 | jockey Jonathan England | trainer Sam England (14d 7/32) | headgear t | last run 23 days | form 5/14-7 | MARKET 8.4% | 09:00 median 9.50 | Matchbook -
    comment: Grand Scheme won three starts back but has slipped since, a fourth two starts back and a seventh last time out, though 23 days off suggests he's fresh enough.
    DATA: model 8.1% | style Held up (led 8% of runs) | runs in data 1 | last 3: 3 Nov Sedgefield Hurdle 17f Good 7/11 fig 69
    DATA for: Trainer 22% wins (7/32), last 14 days
    DATA against: Best recent form figure 69, 11 lb below field average; Recent figures 12 lb below its current mark (looks high in the weights); Official rating 81, 8 lb below field average; Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Contemplation (hrs_57941968) | 3yo G | 142lb | OR 91 | draw 0 | jockey Charlie Maggs | trainer Mike Sowersby (14d 0/5) | headgear - | last run 23 days | form 44 | MARKET 6.5% | 09:00 median 12.00 | Matchbook -
    comment: Contemplation is winless in his last two starts, finishing fourth both times, and he looks vulnerable at 142 lb off an official mark of 91.
    DATA: model 3.0% | style Prominent (led 38% of runs) | runs in data 8 | last 3: 10 Jun Yarmouth Flat 8f Soft 9/10; 25 Oct Market Rasen Hurdle 16.5f Good To Soft 4/7; 3 Nov Sedgefield Hurdle 17f Good 4/8 fig 83
    DATA for: Last-run finishing speed +2.3% vs that field (finished strongly); Carries 11 lb less than average
    DATA against: Recent figures 8 lb below its current mark (looks high in the weights)
- Steel Fixer (hrs_55764394) | 3yo G | 142lb | OR 91 | draw 0 | jockey Nathan Moscrop | trainer Brian Ellison (14d 1/8) | headgear tp | last run 61 days | form P45 | MARKET 3.9% | 09:00 median 19.00 | Matchbook -
    comment: Steel Fixer is winless in his last three, finishing fifth last time out, a fourth two starts back, and pulled up three starts back, so he is hard to fancy.
    DATA: model 8.0% | style Midfield (led 4% of runs) | runs in data 7 | last 3: 12 Jun Market Rasen Hurdle 16.6f Good 4/4; 22 Jul Catterick Flat 12.1f Good To Firm 5/7; 26 Sep Market Rasen Hurdle 16.6f Good 5/7
    DATA for: Carries 11 lb less than average
    DATA against: Pulled up in 1 of its last 3 jumps runs
- Takes Time (hrs_40394361) | 5yo M | 146lb | OR 78 | draw 0 | jockey Conor Rabbitt(3) | trainer Mike Sowersby (14d 0/5) | headgear - | last run 585 days | form 8680/ | MARKET 1.3% | 09:00 median 67.00 | Matchbook -
    comment: Takes Time is hard to fancy: she's winless in her last four, finishing eighth, sixth and eighth before going unplaced last time, and returns after 585 days off.
    DATA: model 7.2% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Carries 7 lb less than average
    DATA against: Official rating 78, 11 lb below field average; Returns from a 585-day break; Lightly raced: 0 runs in our data, so the model has little to go on

## 1:04 Market Rasen | race_id rac_32305608907 | PricedUp Boosted Prices Daily Bud Booth Mares' Steeple Chase (Listed Race) (GBB Race)
Chase | Class 1 | 2m7f191y | going Good To Soft | Turf | 5 runners | rating band - | age 4yo+
DATA pace: Even - Two likely leaders (Bluey, Overabottleofred). A fair, even gallop is most likely.
- Kala Conti (hrs_35431347) | 6yo M | 162lb | OR 148 | draw 0 | jockey Danny Gilligan | trainer Gordon Elliott (14d 11/81) | headgear - | last run 26 days | form 112F-1 | MARKET 49.9% | 09:00 median 1.83 | Matchbook -
    comment: Kala Conti won last time out and has three wins in her last five starts, with a second three starts back, and she's fresh enough after 26 days off.
    DATA: model 26.3% | style Held up (led 5% of runs) | runs in data 3 | last 3: 31 Jan Sandown Chase 20.1f Soft 2/4; 11 Apr Aintree Chase 15.8f Good To Soft F/8; 31 Oct Down Royal (IRE) Chase 19.5f Good 1/5 fig 119
    DATA for: Official rating 148, 14 lb above field average
    DATA against: Best recent form figure 119, 10 lb below field average; Fell or unseated in 1 of its last 3 jumps runs
- Bluey (hrs_34457402) | 7yo M | 158lb | OR 136 | draw 0 | jockey Harry Cobden | trainer Emma Lavelle (14d 2/21) | headgear - | last run 19 days | form 2121-3 | MARKET 26.2% | 09:00 median 3.50 | Matchbook -
    comment: Bluey arrives in cracking form, third last time out, a winner two starts back, and a second three starts back, with two wins in her last five and a fresh 19-day gap. She has run on today's going, but carrying 158 lb is the main risk.
    DATA: model 20.2% | style Leader (led 43% of runs) | runs in data 4 | last 3: 14 Feb Wincanton Chase 15.7f Heavy 2/5; 14 Apr Market Rasen Chase 21.4f Good 1/7; 7 Nov Aintree Chase 20f Good To Soft 3/11 fig 137
    DATA for: Best recent form figure 137, 8 lb above field average; Good recent finishing positions
- Ruby Island (hrs_28903581) | 9yo M | 156lb | OR 136 | draw 0 | jockey Danny McMenamin | trainer Nicky Richards (14d 1/8) | headgear p | last run 20 days | form 4312-1 | MARKET 13.7% | 09:00 median 6.50 | Matchbook -
    comment: Ruby Island arrives in cracking order, a winner last time out, a second two starts back, and a winner three starts back, with 20 days since her last run and experience of both today's trip and going.
    DATA: model 19.7% | style Midfield (led 5% of runs) | runs in data 4 | last 3: 5 Mar Haydock Chase 19.9f Good To Soft 1/2; 22 Apr Perth Chase 23.8f Good 2/4; 6 Nov Hexham Chase 20f Good 1/6 fig 132
    DATA for: Last-run finishing speed +2.6% vs that field (finished strongly); Good recent finishing positions
- Jasmine Bliss (hrs_34253401) | 7yo M | 160lb | OR 133 | draw 0 | jockey Jonathan Burke | trainer Harry Derham (14d 1/14) | headgear t | last run 226 days | form /3126- | MARKET 5.5% | 09:00 median 17.00 | Matchbook -
    comment: Jasmine Bliss has a solid book, winning three starts back and following with a second, and she has run on today's going before. The big risk is a 226-day absence, with a sixth last time out and 160 lb on her back.
    DATA: model 13.4% | style Prominent (led 4% of runs) | runs in data 3 | last 3: 5 Feb Huntingdon Chase 19.9f Soft 1/6; 21 Feb Kempton Chase 20.5f Good To Soft 2/4; 14 Apr Market Rasen Chase 21.4f Good 6/7
    DATA for: Good recent finishing positions
    DATA against: Last-run finishing speed -9.8% vs that field (faded); Returns from a 226-day break
- Overabottleofred (hrs_35321636) | 7yo M | 156lb | OR 115 | draw 0 | jockey Sean Bowen | trainer Tom Gretton (14d 0/3) | headgear t | last run 236 days | form /4U11- | MARKET 4.8% | 09:00 median 17.00 | Matchbook -
    comment: Overabottleofred won last time out and two starts back, but she returns after 236 days off and carries 156 lb off an official mark of 115.
    DATA: model 20.5% | style Leader (led 38% of runs) | runs in data 4 | last 3: 26 Feb Taunton Chase 23f Good To Soft UR/8; 15 Mar Market Rasen Chase 23.9f Good To Soft 1/4; 4 Apr Huntingdon Chase 23.6f Good 1/4
    DATA for: Last-run finishing speed +4.4% vs that field (finished strongly); Has won at this trip or further
    DATA against: Official rating 115, 19 lb below field average; Returns from a 236-day break; Fell or unseated in 1 of its last 4 jumps runs

## 1:39 Market Rasen | race_id rac_32305610844 | Aubrey Bealby ABH Tipster Champion Novices' Handicap Steeple Chase
Chase | Class 5 | 2m3f34y | going Good To Soft | Turf | 9 runners | rating band 0-100 | age 4yo+
DATA pace: Even - Two likely leaders (Ever Ready, Lunar Ocean). A fair, even gallop is most likely.
- Natus Vincere (hrs_41052368) | 7yo M | 163lb | OR 92 | draw 0 | jockey Sean Bowen | trainer Olly Murphy (14d 10/51) | headgear t | wind surgery | last run 227 days | form /512P- | MARKET 20.3% | 09:00 median 4.00 | Matchbook - | CHECK (skip line 3.80)
    comment: Natus Vincere won three starts back and was second two runs ago, but she was pulled up last time out and returns after 227 days off.
    DATA: model 16.2% | style Unknown | runs in data 4 | last 3: 19 Feb Huntingdon Hurdle 19.6f Heavy 1/6; 15 Mar Market Rasen Hurdle 18.6f Good To Soft 2/5; 13 Apr Fakenham Hurdle 23.4f Good PU/4
    DATA for: Official rating 92, 6 lb above field average; Has won at this trip or further
    DATA against: Carries 6 lb more than average; Returns from a 227-day break; Pulled up in 1 of its last 4 jumps runs; First run over fences in our data
- Ahanaglogh (hrs_39296579) | 7yo G | 156lb | OR 85 | draw 0 | jockey Tom Broughton(3) | trainer Fergal O'Brien (14d 4/30) | headgear - | last run 275 days | form 00822- | MARKET 17.0% | 09:00 median 5.00 | Matchbook -
    comment: Winless in his last five and absent for 275 days, Ahanaglogh is hard to fancy, though back-to-back seconds in his last two starts show he can run well, and he carries 156 lb off an official mark of 85.
    DATA: model 13.8% | style Prominent (led 38% of runs) | runs in data 3 | last 3: 12 Jan Hereford Hurdle 16.2f Soft 8/14; 11 Feb Hereford Chase 20.9f Heavy 2/10; 24 Feb Leicester Chase 20.1f Soft 2/5
    DATA for: Good recent finishing positions
    DATA against: Returns from a 275-day break
- Chatty Girl (hrs_48082657) | 5yo M | 168lb | OR 97 | draw 0 | jockey Kielan Woods | trainer Alex Hales (14d 0/8) | headgear t (1st time) | wind surgery | last run 36 days | form 5342-4 | MARKET 16.1% | 09:00 median 5.50 | Matchbook -
    comment: Chatty Girl has been consistent without a win, finishing second two starts back and fourth last time out, and she has run on today's going before.
    DATA: model 16.4% | style Prominent (led 4% of runs) | runs in data 4 | last 3: 5 Mar Wincanton Hurdle 15.2f Good To Soft 4/13; 14 Apr Market Rasen Hurdle 16.6f Good 2/7; 21 Oct Fontwell Chase 18f Soft 4/5 fig 92
    DATA for: Best recent form figure 92, 13 lb above field average; Official rating 97, 11 lb above field average; First-time headgear
    DATA against: Trainer 0 wins from 8 runs, last 14 days; Carries 11 lb more than average
- Lunar Ocean (hrs_34637855) | 7yo G | 149lb | OR 78 | draw 0 | jockey Gavin Sheehan | trainer Billy Aprahamian (14d 0/5) | headgear b | last run 24 days | form 4P-136 | MARKET 15.2% | 09:00 median 6.00 | Matchbook -
    comment: In his favour, he has run over today's trip and going before, and he returns after 24 days.
    DATA: model 13.8% | style Leader (led 63% of runs) | runs in data 7 | last 3: 14 May Fontwell Chase 19.5f Good 1/7; 24 May Fontwell Chase 19.5f Good 3/6; 2 Nov Plumpton Chase 20f Good 6/9
    DATA for: Has won at this trip or further; Good recent finishing positions; Carries 8 lb less than average
    DATA against: Official rating 78, 8 lb below field average; Last-run finishing speed -5.5% vs that field (faded); Race comments mention jumping mistakes in 3 of its last 5 runs; Pulled up in 1 of its last 5 jumps runs
- Dance Rules (hrs_41190415) | 7yo G | 148lb | OR 77 | draw 0 | jockey David Noonan | trainer Mitchell Hunt & Tim Vaughan (14d 1/5) | headgear - | wind surgery | last run 27 days | form 98/2-5 | MARKET 14.3% | 09:00 median 5.50 | Matchbook -
    comment: Without a win in his last four starts, Dance Rules is hard to fancy, though a fifth last time out and a second two starts back show some life, and he has run over today's trip.
    DATA: model 8.5% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 30 Oct Uttoxeter Chase 20f Good 5/11 fig 66
    DATA for: Trainer 20% wins (1/5), last 14 days; Carries 9 lb less than average
    DATA against: Best recent form figure 66, 13 lb below field average; Recent figures 11 lb below its current mark (looks high in the weights); Official rating 77, 9 lb below field average; Lightly raced: 1 run in our data, so the model has little to go on
- Ever Ready (hrs_34814542) | 7yo M | 159lb | OR 88 | draw 0 | jockey Paul O'Brien | trainer Pam Sly (14d 0/1) | headgear - | last run 25 days | form 2467-4 | MARKET 8.0% | 09:00 median 11.00 | Matchbook -
    comment: The risk is a winless run in her last five, with a second five starts back the best of it, while carrying 159 lb.
    DATA: model 7.4% | style Leader (led 23% of runs) | runs in data 6 | last 3: 24 Mar Southwell Hurdle 20.4f Good 6/12; 14 Apr Market Rasen Hurdle 18.6f Good 7/9; 1 Nov Huntingdon Hurdle 20.5f Good 4/7 fig 80
    DATA against: Recent figures 8 lb below its current mark (looks high in the weights); Last-run finishing speed -3.8% vs that field (faded); Race comments mention jumping mistakes in 2 of its last 5 runs; First run over fences in our data
- Miami Steve (hrs_39109588) | 7yo G | 166lb | OR 95 | draw 0 | jockey Peter Kavanagh | trainer Donald McCain (14d 2/22) | headgear - | last run 628 days | form 74548/ | MARKET 4.4% | 09:00 median 17.00 | Matchbook -
    DATA: model 10.6% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Official rating 95, 9 lb above field average
    DATA against: Carries 9 lb more than average; Returns from a 628-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Red Trail (hrs_29509753) | 7yo M | 142lb | OR 71 | draw 0 | jockey Charlie Maggs | trainer Mike Sowersby (14d 0/5) | headgear t | last run 73 days | form 50P567 | MARKET 2.8% | 09:00 median 41.00 | Matchbook -
    comment: Red Trail has been going the wrong way, a fifth, then a sixth, then a seventh last time out, and she's winless in her last six and returns after 73 days off.
    DATA: model 6.1% | style Held up (led 4% of runs) | runs in data 6 | last 3: 15 Aug Market Rasen Hurdle 18.6f Good 5/10; 28 Aug Sedgefield Hurdle 16.8f Good 6/10; 14 Sep Sedgefield Hurdle 16.8f Good 7/10
    DATA for: Carries 15 lb less than average
    DATA against: Official rating 71, 15 lb below field average; Last-run finishing speed -4.4% vs that field (faded); Pulled up in 1 of its last 5 jumps runs; First run over fences in our data
- Quickasican (hrs_29226743) | 9yo G | 158lb | OR 87 | draw 0 | jockey Troy Walsh(7) | trainer Jessica Bedi (14d 0/8) | headgear tp | last run 194 days | form PF2-PP | MARKET 1.9% | 09:00 median 67.00 | Matchbook -
    DATA: model 7.2% | style Midfield (led 3% of runs) | runs in data 6 | last 3: 11 Apr Newcastle Chase 20.1f Good 2/5; 2 May Hexham Chase 20.1f Good PU/13; 16 May Uttoxeter Chase 20.9f Good PU/10
    DATA against: Trainer 0 wins from 8 runs, last 14 days; Returns from a 194-day break; Race comments mention jumping mistakes in 2 of its last 5 runs; Fell or unseated in 1 of its last 5 jumps runs; Pulled up in 3 of its last 5 jumps runs

## 2:14 Market Rasen | race_id rac_32305612781 | PricedUp Boosts And BOG Handicap Hurdle Race
Hurdle | Class 4 | 2m7f16y | going Good To Soft | Turf | 9 runners | rating band 0-120 | age 4yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Jury's In (hrs_49578067) | 6yo G | 170lb | OR 122 | draw 0 | jockey Charlie Hammond | trainer Stuart Edmunds (14d 2/14) | headgear - | last run 46 days | form 4310-6 | MARKET 26.7% | 09:00 median 3.25 | Matchbook - | CHECK (skip line 3.09)
    comment: Jury's In has a win three starts back and a third four starts back in his last five, and he has run over today's trip and going before, while carrying 170 lb off an official mark of 122. The main risk is a sixth last time out and a 46-day break.
    DATA: model 18.1% | style Prominent (led 23% of runs) | runs in data 4 | last 3: 13 Feb Fakenham Hurdle 20f Soft 1/6; 7 Mar Sandown Hurdle 19.8f Soft 10/17; 11 Oct Chepstow Hurdle 23.6f Good To Soft 6/10
    DATA for: Official rating 122, 9 lb above field average
    DATA against: Carries 9 lb more than average
- Diamond Geezer (hrs_38203501) | 7yo G | 168lb | OR 120 | draw 0 | jockey Troy Walsh(10) | trainer Olly Murphy (14d 10/51) | headgear v (1st time) | last run 19 days | form 171-24 | MARKET 19.9% | 09:00 median 4.50 | Matchbook -
    comment: Diamond Geezer is a fourth last time out, after a second two starts back and a win three starts back, and he has run over today's trip and going, fresh enough after 19 days.
    DATA: model 18.0% | style Held up (led 3% of runs) | runs in data 5 | last 3: 1 Apr Southwell Hurdle 24.3f Good 1/8; 17 Oct Market Rasen Hurdle 23f Good 2/5 fig 116; 7 Nov Uttoxeter Hurdle 23.5f Good 4/9 fig 117
    DATA for: Best recent form figure 117, 5 lb above field average; Official rating 120, 7 lb above field average; Has won at this trip or further; Good recent finishing positions; First-time headgear
    DATA against: Carries 7 lb more than average; Race comments mention jumping mistakes in 2 of its last 5 runs; Pace: steady gallop likely, hard to come from off the pace
- Frisky Whiskey (hrs_58469236) | 5yo M | 153lb | OR 105 | draw 0 | jockey Danny McMenamin | trainer Brian Ellison (14d 1/8) | headgear tp (1st time) | last run 13 days | form 643212 | MARKET 19.8% | 09:00 median 4.33 | Matchbook -
    comment: Frisky Whiskey arrives in fine fettle, second last time out and a winner two starts back, with only 13 days since her last run, but she carries 153 lb off an official 105 and has run over today's trip.
    DATA: model 7.1% | style Held up (led 4% of runs) | runs in data 7 | last 3: 29 Aug Cartmel Hurdle 25.4f Good 2/12; 2 Oct Hexham Hurdle 23.3f Good 1/5; 13 Nov Sedgefield Hurdle 27f Good 2/5 fig 103
    DATA for: Last-run finishing speed +3.3% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions; Carries 8 lb less than average; First-time headgear
    DATA against: Best recent form figure 103, 9 lb below field average; Official rating 105, 8 lb below field average; Pace: steady gallop likely, hard to come from off the pace
- Billy Boi Blue (hrs_29816129) | 9yo G | 162lb | OR 114 | draw 0 | jockey Kielan Woods | trainer David Killahena & Graeme McPherson (14d 1/8) | headgear tp | last run 24 days | form 615711 | MARKET 12.1% | 09:00 median 6.50 | Matchbook -
    comment: Billy Boi Blue arrives in cracking nick, having won last time out and two starts back, with 24 days since his last run and experience of today's trip and going.
    DATA: model 17.1% | style Midfield (led 3% of runs) | runs in data 10 | last 3: 15 Sep Uttoxeter Hurdle 23.3f Good 7/8; 12 Oct Worcester Chase 23f Good 1/9; 2 Nov Southwell Chase 24.5f Good 1/8 fig 113
    DATA for: Last-run finishing speed +2.8% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
- Jalisco Star (hrs_32682608) | 8yo M | 163lb | OR 115 | draw 0 | jockey Sean Bowen | trainer Laura Horsfall (14d 0/4) | headgear t | last run 46 days | form 2145-P | MARKET 8.2% | 09:00 median 10.00 | Matchbook -
    comment: Pulled up last time out and a fifth two starts back, Jalisco Star has drifted since winning four starts back, and 46 days off the track raises fitness questions.
    DATA: model 9.3% | style Prominent (led 29% of runs) | runs in data 5 | last 3: 27 Feb Newbury Hurdle 24.3f Good To Soft 4/9; 27 Mar Wetherby Hurdle 24.1f Good 5/6; 11 Oct Chepstow Hurdle 23.6f Good To Soft PU/10
    DATA for: Has won at this trip or further
    DATA against: Pulled up in 1 of its last 5 jumps runs
- Ladronne (hrs_13382810) | 12yo G | 156lb | OR 108 | draw 0 | jockey Oscar Palmer(7) | trainer Joel Parkinson & Sue Smith (14d 1/13) | headgear t | last run 26 days | form 1252-5 | MARKET 6.0% | 09:00 median 15.00 | Matchbook -
    comment: The main risk is a weight of 156 lb after a fifth last time out.
    DATA: model 9.1% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 17 Mar Wetherby Hurdle 24.1f Good To Soft 5/10; 14 Apr Market Rasen Chase 23.9f Good 2/6; 31 Oct Wetherby Chase 19.5f Good 5/8 fig 114
    DATA for: Recent figures 6 lb above its current mark (looks well handicapped); Has won at this trip or further; Carries 5 lb less than average
    DATA against: Official rating 108, 5 lb below field average; Race comments mention jumping mistakes in 2 of its last 5 runs; Aged 12, older than most of this field
- Happy And Fine (hrs_25204760) | 9yo G | 166lb | OR 118 | draw 0 | jockey Jonathan Burke | trainer Alex Hales (14d 0/8) | headgear b (1st time) | last run 25 days | form UPU4-U | MARKET 2.9% | 09:00 median 29.00 | Matchbook -
    comment: Fit after 25 days off, Happy And Fine has run over today's trip and going before, and his fourth two starts back is the best of a patchy recent run.
    DATA: model 6.2% | style Prominent (led 3% of runs) | runs in data 5 | last 3: 28 Mar Stratford Chase 22.6f Good UR/5; 11 Apr Chepstow Chase 23.6f Good To Soft 4/8; 1 Nov Worcester Chase 20f Good To Soft UR/13
    DATA for: First-time headgear
    DATA against: Trainer 0 wins from 8 runs, last 14 days; Race comments mention jumping mistakes in 2 of its last 5 runs; Fell or unseated in 3 of its last 5 jumps runs; Pulled up in 1 of its last 5 jumps runs; First run over hurdles in our data
- Catch Catchfire (hrs_38579387) | 7yo G | 159lb | OR 111 | draw 0 | jockey Charlie Todd | trainer Ian Williams (14d 3/27) | headgear p | last run 257 days | form 5U2PP- | MARKET 2.9% | 09:00 median 26.00 | Matchbook -
    comment: Hard to fancy after being pulled up in each of his last two starts and returning from 257 days off, carrying 159 lb. On the plus side, he's run over today's trip and going before, and was second three starts back.
    DATA: model 11.0% | style Prominent (led 38% of runs) | runs in data 3 | last 3: 19 Jan Lingfield Chase 28.8f Soft 2/14; 20 Feb Exeter Chase 30.7f Heavy PU/8; 14 Mar Uttoxeter Chase 34f Soft PU/16
    DATA against: Returns from a 257-day break; Race comments mention jumping mistakes in 2 of its last 3 runs; Pulled up in 2 of its last 3 jumps runs; First run over hurdles in our data
- Kilbarry Hill (hrs_32780223) | 8yo G | 155lb | OR 107 | draw 0 | jockey Charlie Maggs | trainer Mike Sowersby (14d 0/5) | headgear t | wind surgery | last run 191 days | form 3F54-P | MARKET 1.6% | 09:00 median 51.00 | Matchbook -
    DATA: model 4.1% | style Held up (led 8% of runs) | runs in data 3 | last 3: 5 Mar Wincanton Chase 25.1f Good To Soft 5/8; 28 Mar Stratford Chase 22.6f Good 4/5; 19 May Hexham Hurdle 20.1f Good PU/10
    DATA for: Carries 6 lb less than average
    DATA against: Official rating 107, 6 lb below field average; Returns from a 191-day break; Race comments mention jumping mistakes in 2 of its last 3 runs; Pulled up in 1 of its last 3 jumps runs; Pace: steady gallop likely, hard to come from off the pace

## 2:49 Market Rasen | race_id rac_32305614718 | PricedUp Bet Handicap Steeple Chase
Chase | Class 5 | 2m7f191y | going Good To Soft | Turf | 10 runners | rating band 0-100 | age 4yo+
DATA pace: Strong pace - 4 habitual front-runners (Jo Lescribaa, Brother Boris, Jukebox d'Eddy, Jimmyjeroo). A contested lead should set things up for horses coming from behind.
- Jukebox d'Eddy (hrs_32683350) | 7yo G | 158lb | OR 90 | draw 0 | jockey Sean Bowen | trainer Tom Gretton (14d 0/3) | headgear tv | last run 234 days | form 11312- | MARKET 21.0% | 09:00 median 3.75 | Matchbook - | CHECK (skip line 3.56)
    DATA: model 16.2% | style Leader (led 57% of runs) | runs in data 3 | last 3: 23 Jan Doncaster Chase 24f Soft 3/4; 11 Mar Huntingdon Chase 23.6f Good 1/6; 6 Apr Hereford Chase 25.2f Good 2/5
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Returns from a 234-day break; Pace: likely to be taken on for the lead
- Subtle Fortune (hrs_34238176) | 8yo M | 164lb | OR 96 | draw 0 | jockey Charlie Hammond | trainer Mel Rowley (14d 1/12) | headgear t (1st time) | last run 222 days | form 41434- | MARKET 15.3% | 09:00 median 5.50 | Matchbook -
    comment: Subtle Fortune has finished fourth, third, then fourth again in her last three, with a win four starts back, and she has run over today's trip and going before; the main risk is a 222-day absence, while 164 lb is a hefty burden.
    DATA: model 13.0% | style Prominent (led 4% of runs) | runs in data 5 | last 3: 6 Mar Leicester Chase 22.7f Good To Soft 4/6; 31 Mar Bangor-on-Dee Chase 24.1f Good 3/10; 18 Apr Bangor-on-Dee Chase 24.1f Good 4/14
    DATA for: Official rating 96, 6 lb above field average; Last-run finishing speed +2.2% vs that field (finished strongly); Has won at this trip or further; First-time headgear
    DATA against: Carries 6 lb more than average; Returns from a 222-day break
- Glengolly (hrs_33774664) | 7yo G | 160lb | OR 92 | draw 0 | jockey Gavin Sheehan | trainer Billy Aprahamian (14d 0/5) | headgear tp | last run 24 days | form 5231-P | MARKET 14.2% | 09:00 median 6.00 | Matchbook -
    comment: Glengolly won two starts back and was a third the run before that, but he was pulled up last time out, which leaves a question mark after 24 days off.
    DATA: model 13.9% | style Prominent (led 3% of runs) | runs in data 5 | last 3: 18 Mar Huntingdon Hurdle 25f Good 3/9; 12 Apr Ffos Las Hurdle 23.9f Good To Soft 1/14; 2 Nov Southwell Chase 24.5f Good PU/8
    DATA for: Has won at this trip or further
    DATA against: Pulled up in 1 of its last 5 jumps runs
- Brother Boris (hrs_39392066) | 7yo G | 164lb | OR 96 | draw 0 | jockey Harry Cobden | trainer Lucy Wadham (14d 0/2) | headgear p | last run 234 days | form /311P- | MARKET 11.2% | 09:00 median 6.50 | Matchbook -
    comment: Brother Boris won two starts back and three starts back, but he was pulled up last time out and returns after 234 days off, which raises fitness questions.
    DATA: model 16.0% | style Leader (led 38% of runs) | runs in data 4 | last 3: 13 Feb Fakenham Chase 29.1f Soft 1/5; 13 Mar Fakenham Chase 24.2f Good To Soft 1/3; 6 Apr Fakenham Chase 24.2f Good PU/4
    DATA for: Official rating 96, 6 lb above field average; Has won at this trip or further
    DATA against: Carries 6 lb more than average; Returns from a 234-day break; Pulled up in 1 of its last 4 jumps runs; Pace: likely to be taken on for the lead
- Jimmyjeroo (hrs_31835125) | 8yo G | 158lb | OR 90 | draw 0 | jockey Paul O'Brien | trainer Henrietta C Knight (14d 1/11) | headgear p | last run 29 days | form 342-64 | MARKET 11.1% | 09:00 median 8.00 | Matchbook -
    comment: Fourth last time out and a second three starts back show Jimmyjeroo is consistent, and he has run over today's trip and going, but he is yet to win in his last five starts.
    DATA: model 8.2% | style Leader (led 57% of runs) | runs in data 2 | last 3: 12 Oct Worcester Chase 20f Good 6/9; 28 Oct Huntingdon Chase 23.5f Good 4/6 fig 87
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Pace: likely to be taken on for the lead
- Felton Bellevue (hrs_18323725) | 11yo G | 154lb | OR 86 | draw 0 | jockey Jonathan Burke | trainer Ben Case (14d 1/6) | headgear tb | last run 29 days | form 3254-3 | MARKET 9.8% | 09:00 median 8.50 | Matchbook -
    comment: Winless in his last five, Felton Bellevue was third last time out and has been placed in three of those, with a second four starts back, but he never quite gets his head in front.
    DATA: model 8.1% | style Prominent (led 23% of runs) | runs in data 8 | last 3: 31 Mar Bangor-on-Dee Chase 24.1f Good 5/10; 19 Apr Stratford Chase 27.5f Good 4/7; 28 Oct Huntingdon Chase 23.5f Good 3/6 fig 84
    DATA for: Has won at this trip or further
    DATA against: Aged 11, older than most of this field
- Jo Lescribaa (hrs_37890426) | 7yo G | 168lb | OR 100 | draw 0 | jockey Toby Wynne | trainer Oliver Greenall & Josh Guerriero (14d 3/17) | headgear tp (1st time) | wind surgery | last run 243 days | form 13/6P- | MARKET 9.5% | 09:00 median 9.50 | Matchbook -
    comment: The main risk is a 243-day absence, with a pulled up last time out and 168 lb to carry.
    DATA: model 8.9% | style Leader (led 57% of runs) | runs in data 1 | last 3: 28 Mar Uttoxeter Chase 24f Good To Soft PU/10
    DATA for: Official rating 100, 10 lb above field average; First-time headgear
    DATA against: Carries 10 lb more than average; Returns from a 243-day break; Lightly raced: 1 run in our data, so the model has little to go on; Pulled up in 1 of its last 1 jumps runs; Pace: likely to be taken on for the lead
- El Muchacho (hrs_29226393) | 9yo G | 161lb | OR 93 | draw 0 | jockey Charlie Maggs | trainer Mike Sowersby (14d 0/5) | headgear t | last run 129 days | form 23-239 | MARKET 3.4% | 09:00 median 21.00 | Matchbook -
    comment: The risk is a 129-day absence plus a ninth last time out, with 161 lb to carry.
    DATA: model 8.9% | style Held up (led 3% of runs) | runs in data 8 | last 3: 8 May Market Rasen Chase 21.4f Good 2/7; 28 May Market Rasen Chase 21.4f Good 3/4; 20 Jul Cartmel Chase 21.2f Good 9/9
    DATA for: Good recent finishing positions; Pace: a contested lead should suit its hold-up style
    DATA against: Last-run finishing speed -4.1% vs that field (faded); Returns from a 129-day break
- Deadly Missile (hrs_24592799) | 9yo G | 142lb | OR 74 | draw 0 | jockey Ben Poste | trainer Rosemary Gasson (14d 0/2) | headgear p | last run 61 days | form 4413-5 | MARKET 2.8% | 09:00 median 34.00 | Matchbook -
    comment: Deadly Missile was fifth last time out after a third two starts back, and he returns after 61 days off, which makes him hard to fancy.
    DATA: model 3.8% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 26 Sep Market Rasen Chase 23.9f Good 5/7
    DATA for: Carries 16 lb less than average
    DATA against: Official rating 74, 16 lb below field average; Lightly raced: 1 run in our data, so the model has little to go on
- Kadex (hrs_29379602) | 8yo G | 148lb | OR 80 | draw 0 | jockey Philip Armson(3) | trainer Alan Jones (14d 0/1) | headgear p | last run 38 days | form P5PF/P | MARKET 1.7% | 09:00 median 51.00 | Matchbook -
    DATA: model 3.0% | style Held up (led 8% of runs) | runs in data 1 | last 3: 19 Oct Plumpton Chase 20f Good PU/4
    DATA for: Carries 10 lb less than average; Pace: a contested lead should suit its hold-up style
    DATA against: Official rating 80, 10 lb below field average; Lightly raced: 1 run in our data, so the model has little to go on; Pulled up in 1 of its last 1 jumps runs

## 3:24 Market Rasen | race_id rac_32305616655 | PricedUp Now With Best Odds Open National Hunt Flat Race (Category 1 Elimination) (GBB Race)
NH Flat | Class 4 | 2m0f125y | going Good To Soft | Turf | 9 runners | rating band - | age 4-5yo
DATA pace: Unclear - Running styles known for only 4 of 9 runners.
- Monjeu de Chaillac (hrs_56559538) | 4yo G | 156lb | OR - | draw 0 | jockey Sean Bowen | trainer Olly Murphy (14d 10/51) | headgear - | last run 221 days | form 1- | MARKET 31.1% | 09:00 median 2.75 | Matchbook -
    comment: Unbeaten in his only recent start, Monjeu de Chaillac won last time out and looks unexposed with scope for improvement, though he returns after 221 days off and shoulders 156 lb.
    DATA: model 10.0% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 221-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Nevada Samba (hrs_62235775) | 5yo G | 163lb | OR - | draw 0 | jockey Tom Bellamy | trainer Alan King (14d 4/25) | headgear - | last run 266 days | form 1- | MARKET 15.9% | 09:00 median 5.50 | Matchbook -
    comment: The one concern is a 266-day layoff, and he also shoulders 163 lb.
    DATA: model 22.4% | style Held up (led 8% of runs) | runs in data 1 | last 3: 5 Mar Wincanton NH Flat 15.2f Good To Soft 1/12
    DATA for: Last-run finishing speed +7.6% vs that field (finished strongly)
    DATA against: Returns from a 266-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Micky Haller (hrs_17394063757) | 4yo G | 156lb | OR - | draw 0 | jockey Dominic Lewis(10) | trainer Dan Skelton (14d 21/94) | headgear - | last run 263 days | form 1- | MARKET 15.2% | 09:00 median 5.00 | Matchbook -
    comment: Winner last time out in his only recent start, Micky Haller returns after 263 days off and looks unexposed, with scope for improvement. He carries 156 lb, and the long layoff is the question.
    DATA: model 10.0% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 22% wins (21/94), last 14 days
    DATA against: Returns from a 263-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Oakworth (hrs_17396038156) | 4yo G | 156lb | OR - | draw 0 | jockey Harry Cobden | trainer Emma Lavelle (14d 2/21) | headgear - | last run - days | form - | MARKET 15.1% | 09:00 median 5.50 | Matchbook -
    comment: Oakworth is an unraced gelding with no form to go on, so he's wholly unexposed and open to improvement. He shoulders 156 lb on debut, and any promise will have to come from the stable rather than a previous run.
    DATA: model 10.0% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Cayenne (hrs_60395006) | 4yo G | 156lb | OR - | draw 0 | jockey Danny McMenamin | trainer Nicky Richards (14d 1/8) | headgear - | last run 30 days | form 5 | MARKET 9.1% | 09:00 median 9.00 | Matchbook -
    comment: Cayenne makes plenty of appeal on profile, having finished a fifth last time out 30 days ago and since had a break, while he has run over today's trip before.
    DATA: model 13.8% | style Held up (led 8% of runs) | runs in data 1 | last 3: 27 Oct Newcastle NH Flat 17f Good 5/9 fig 106
    DATA for: Last-run finishing speed +4.5% vs that field (finished strongly)
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Falconella (hrs_62645541) | 4yo F | 149lb | OR - | draw 0 | jockey Kielan Woods | trainer David Killahena & Graeme McPherson (14d 1/8) | headgear t | wind surgery | last run 234 days | form 4- | MARKET 6.7% | 09:00 median 13.00 | Matchbook -
    comment: The one concern is a 234-day absence, so fitness is the question.
    DATA: model 6.5% | style Held up (led 8% of runs) | runs in data 1 | last 3: 6 Apr Hereford NH Flat 16.2f Good 4/11
    DATA for: Last-run finishing speed +3.2% vs that field (finished strongly)
    DATA against: Returns from a 234-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Crystal Glade (hrs_63618695) | 4yo F | 149lb | OR - | draw 0 | jockey Paul O'Brien | trainer Pam Sly (14d 0/1) | headgear - | last run 199 days | form 4-5 | MARKET 4.2% | 09:00 median 19.00 | Matchbook -
    comment: Crystal Glade has run over today's trip and was a fifth last time out, with a fourth two starts back, so she's consistent without being able to land a blow, and her 149 lb burden is a real test.
    DATA: model 8.1% | style Prominent (led 8% of runs) | runs in data 2 | last 3: 14 Apr Market Rasen NH Flat 16.6f Good 4/8; 11 May Southwell NH Flat 15.8f Good 5/10
    DATA for: Last-run finishing speed +5.0% vs that field (finished strongly)
    DATA against: Returns from a 199-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- Don't Tell Zoe (hrs_17395621999) | 4yo F | 149lb | OR - | draw 0 | jockey Nick Slatter(3) | trainer David Killahena & Graeme McPherson (14d 1/8) | headgear - | last run - days | form - | MARKET 2.2% | 09:00 median 34.00 | Matchbook -
    comment: Don't Tell Zoe is a debutant with no recorded form, so she's totally unexposed and open to improvement, and she'll carry 149 lb into her first look at a racecourse. There's nothing to go on yet, which leaves plenty of room for progress.
    DATA: model 9.1% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Sylvan Grove (hrs_17396039199) | 4yo G | 156lb | OR - | draw 0 | jockey Oscar Palmer(7) | trainer Andrew Crook (14d 1/4) | headgear - | last run - days | form - | MARKET 0.6% | 09:00 median 126.00 | Matchbook -
    comment: Sylvan Grove is a debutant with no recorded form, so he's totally unexposed and open to improvement. He shoulders 156 lb on that first start, which is plenty of weight to carry for an unraced gelding.
    DATA: model 10.0% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
