# Card review packet: Punchestown, 2026-11-22

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
{"meeting": "punchestown", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 12:00 Punchestown | race_id rac_32305302861 | Donohue Marquees Risk Of Thunder Steeplechase
Chase |  | 3m0f90y | going Good To Yielding | Turf | 15 runners | rating band - | age 5yo+
DATA pace: Even - Two likely leaders (Desertmore House, Stumptown). A fair, even gallop is most likely.
- Stumptown (hrs_24494554) | 9yo G | 163lb | OR 149 | draw 0 | jockey Keith Donoghue | trainer Gavin Cromwell (14d 4/42) | headgear p | last run 27 days | form P/14-1 | MARKET 42.9% | 09:00 median 1.91 | Matchbook 2.00
    comment: Stumptown arrives a last-time-out winner and has won twice in his last four starts, a fourth two starts back and another win three starts back, with 27 days since his last run and experience of today's trip and going. The main risk is the 163 lb he carries, a hefty burden off an official mark of 149.
    DATA: model 13.4% | style Leader (led 72% of runs) | runs in data 2 | last 3: 11 Mar Cheltenham Chase 29.3f Good 4/14; 26 Oct Galway (IRE) Hurdle 22f Heavy 1/12 fig 133
    DATA for: Best recent form figure 133, 22 lb above field average; Official rating 149, 25 lb above field average
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Fountain House (hrs_33479019) | 8yo G | 168lb | OR 125 | draw 0 | jockey Mr E Mahon(7) | trainer Ian John McCarthy (14d 1/1) | headgear t | last run 28 days | form 1111-5 | MARKET 21.4% | 09:00 median 3.75 | Matchbook 4.00
    comment: Fountain House arrives having won four of his last five starts, with a fifth last time out the only blemish, and he has run over today's trip and going before.
    DATA: model 12.1% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 28 Apr Punchestown Chase 24.4f Yielding 1/9; 2 May Punchestown Chase 24.4f Yielding 1/15; 25 Oct Wexford (IRE) Chase 19.5f Soft 5/10 fig 125
    DATA for: Best recent form figure 125, 14 lb above field average; Has won at this trip or further; Good recent finishing positions
- The Goffer (hrs_24494225) | 9yo G | 158lb | OR 135 | draw 0 | jockey Jack Kennedy | trainer Gordon Elliott (14d 10/75) | headgear tp | last run 204 days | form 72034- | MARKET 6.1% | 09:00 median 12.00 | Matchbook 16.00
    comment: The Goffer has been running consistently, with a third two starts back and a fourth last time out, and he has run over today's trip and going before. The one concern is a 204-day absence, so fitness is the main risk under 158 lb.
    DATA: model 9.2% | style Held up (led 3% of runs) | runs in data 4 | last 3: 11 Mar Cheltenham Chase 29.3f Good 10/14; 30 Apr Punchestown Chase 33f Yielding 3/13; 2 May Punchestown Chase 24.4f Yielding 4/15
    DATA for: Official rating 135, 11 lb above field average; Last-run finishing speed +3.9% vs that field (finished strongly)
    DATA against: Returns from a 204-day break
- Desertmore House (hrs_20730675) | 11yo G | 163lb | OR 138 | draw 0 | jockey Mr J L Gleeson | trainer Martin Brassil (14d 1/4) | headgear tb (1st time) | last run 21 days | form 1P86-P | MARKET 5.2% | 09:00 median 12.00 | Matchbook 22.00
    comment: Desertmore House has run over today's trip and on this going, and he carries 163 lb after a win five starts back, though two pulled-up efforts in his last five leave a question mark.
    DATA: model 8.6% | style Leader (led 38% of runs) | runs in data 2 | last 3: 11 Mar Cheltenham Chase 29.3f Good 8/14; 30 Apr Punchestown Chase 33f Yielding 6/13
    DATA for: Official rating 138, 14 lb above field average; First-time headgear
    DATA against: Last-run finishing speed -3.0% vs that field (faded); Lightly raced: 2 runs in our data, so the model has little to go on
- Busselton (hrs_21659750) | 9yo G | 163lb | OR 133 | draw 0 | jockey J. J. Slevin | trainer E Bolger (14d 0/0) | headgear - | last run 206 days | form 25951- | MARKET 4.6% | 09:00 median 13.00 | Matchbook 28.00
    comment: Busselton won last time out and has run over today's trip and going, but he returns after 206 days off and carries 163 lb, while a fifth and a ninth in the two runs before that win show his consistency has been patchy.
    DATA: model 6.1% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 5 Apr Cork Hurdle 16.3f Yielding 5/7; 30 Apr Punchestown Chase 33f Yielding 1/13
    DATA for: Official rating 133, 9 lb above field average; Last-run finishing speed +3.6% vs that field (finished strongly); Has won at this trip or further
    DATA against: Returns from a 206-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- The Short Go (hrs_24555419) | 9yo G | 158lb | OR 129 | draw 0 | jockey Mike O'Connor | trainer Henry de Bromhead (14d 9/38) | headgear t | last run 197 days | form /430-7 | MARKET 4.5% | 09:00 median 15.00 | Matchbook 23.00
    comment: The Short Go has run over today's trip and going, and a third three starts back is his best recent finish, but he's yet to win in his last four and was only seventh last time out.
    DATA: model 4.9% | style Held up (led 5% of runs) | runs in data 2 | last 3: 10 Mar Cheltenham Chase 25f Good To Soft 11/22; 9 May Killarney Chase 26f Good To Yielding 7/11
    DATA for: Official rating 129, 5 lb above field average; Trainer 24% wins (9/38), last 14 days
    DATA against: Last-run finishing speed -5.5% vs that field (faded); Returns from a 197-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- Fakir d'Oudairies (hrs_13966008) | 11yo G | 158lb | OR 129 | draw 0 | jockey Sean Flanagan | trainer E Bolger (14d 0/0) | headgear - | last run 28 days | form 602-95 | MARKET 3.9% | 09:00 median 17.00 | Matchbook 27.00
    comment: Fakir d'Oudairies is fresh enough after 28 days off and has run over today's trip and going, with a second three starts back showing he can still reach the frame.
    DATA: model 5.9% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 10 Apr Wexford Chase 19.5f Good To Yielding 14/15; 2 May Punchestown Chase 24.4f Yielding 2/15; 25 May Ballinrobe Chase 23.4f Good 9/16
    DATA for: Official rating 129, 5 lb above field average
    DATA against: Last-run finishing speed -5.0% vs that field (faded); Race comments mention jumping mistakes in 3 of its last 5 runs
- Union Station (hrs_38884741) | 7yo G | 158lb | OR 122 | draw 0 | jockey Ben Harvey | trainer Gavin Cromwell (14d 4/42) | headgear - | last run 30 days | form U446-3 | MARKET 2.4% | 09:00 median 29.00 | Matchbook 46.00
    comment: Union Station is winless in his last five, though a third last time out is a step in the right direction, and he has run over today's trip.
    DATA: model 9.4% | style Held up (led 5% of runs) | runs in data 5 | last 3: 6 Apr Fairyhouse Chase 24.5f Yielding To Soft 4/17; 2 May Punchestown Chase 31.3f Yielding 6/19; 23 Oct Sligo (IRE) Hurdle 25.5f Yielding To Soft 3/5 fig 107
    DATA against: Race comments mention jumping mistakes in 2 of its last 5 runs; Fell or unseated in 1 of its last 5 jumps runs
- Outside The Door (hrs_22259412) | 10yo G | 163lb | OR 137 | draw 0 | jockey Aidan Kelly | trainer Padraig Roche (14d 0/6) | headgear - | last run 141 days | form P072-6 | MARKET 2.3% | 09:00 median 23.00 | Matchbook 80.00
    DATA: model 7.9% | style Prominent (led 38% of runs) | runs in data 2 | last 3: 30 Apr Punchestown Chase 33f Yielding 2/13; 4 Jul Bellewstown Hurdle 24.5f Good 6/15
    DATA for: Official rating 137, 13 lb above field average
    DATA against: Returns from a 141-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- Caesar Rock (hrs_22975946) | 10yo G | 163lb | OR 114 | draw 0 | jockey Josh Williamson(3) | trainer M F Morris (14d 0/2) | headgear - | last run 123 days | form 422-2P | MARKET 1.7% | 09:00 median 29.00 | Matchbook 110.00
    comment: Caesar Rock was pulled up last time out and returns after 123 days off, which makes him hard to fancy, though he was second in three straight runs before that and has run over today's trip and going.
    DATA: model 7.0% | style Prominent (led 3% of runs) | runs in data 4 | last 3: 10 Apr Wexford Chase 19.5f Good To Yielding 2/15; 9 May Killarney Chase 26f Good To Yielding 2/11; 22 Jul Wexford Chase 24.7f Good PU/5
    DATA against: Official rating 114, 10 lb below field average; Returns from a 123-day break; Pulled up in 1 of its last 4 jumps runs
- Three By Two (hrs_23787890) | 10yo M | 151lb | OR 92 | draw 0 | jockey Richard Deegan | trainer Denis Paul Murphy (14d 0/0) | headgear t | last run 44 days | form 0476-0 | MARKET 1.5% | 09:00 median 41.00 | Matchbook 85.00
    comment: Three By Two is winless in her last five, finishing unplaced last time and a sixth and seventh before that, so she is hard to fancy after 44 days off under 151 lb. She has run over today's trip and going before, but that's about the only positive.
    DATA: model 3.0% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 4 Feb Punchestown Chase 24.9f Soft To Heavy 6/10; 9 Oct Downpatrick Chase 23.7f Good 10/14
    DATA against: Official rating 92, 32 lb below field average; Lightly raced: 2 runs in our data, so the model has little to go on
- Idy Wood (hrs_29735356) | 8yo G | 158lb | OR 125 | draw 0 | jockey Conor Stone-Walsh | trainer Gavin Cromwell (14d 4/42) | headgear - | last run 128 days | form 100P-9 | MARKET 1.5% | 09:00 median 41.00 | Matchbook 80.00
    comment: Idy Wood won five starts back but has since managed a ninth last time out, after being pulled up two runs earlier, and returns from 128 days off.
    DATA: model 3.5% | style Midfield (led 3% of runs) | runs in data 4 | last 3: 12 Mar Cheltenham Hurdle 24f Good 22/24; 15 Apr Haydock Hurdle 21.2f Good PU/11; 17 Jul Killarney Hurdle 22.8f Good 9/16
    DATA against: Last-run finishing speed -4.7% vs that field (faded); Poor recent finishing positions; Returns from a 128-day break; Pulled up in 1 of its last 4 jumps runs; First run over fences in our data
- Thatildojon (hrs_17395886921) | 5yo G | 158lb | OR - | draw 0 | jockey Daniel King | trainer E Bolger (14d 0/0) | headgear - | last run 42 days | form 2U3P-5 | MARKET 0.8% | 09:00 median 81.00 | Matchbook 180.00
    comment: Lightly raced and unexposed, Thatildojon was a fifth last time out after being pulled up two starts back, and he has a third three starts back and a second five starts back to build on. Yet to win, he returns after 42 days carrying 158 lb.
    DATA: model 2.7% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- The Gallan (hrs_17395887964) | 6yo G | 158lb | OR - | draw 0 | jockey Eoghan Finegan(5) | trainer Peter John Flood (14d 0/2) | headgear - | last run 36 days | form 422-13 | MARKET 0.7% | 09:00 median 101.00 | Matchbook 220.00
    comment: Unexposed and open to improvement, The Gallan arrives having finished third last time out, with a win two starts back and a pair of seconds before that, so he has been in the frame in four of his last five. He returns after 36 days carrying 158 lb.
    DATA: model 2.7% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Fr Gilligansvoyge (hrs_11245388) | 13yo G | 168lb | OR 82 | draw 0 | jockey Sarah Kavanagh(7) | trainer John G Carr (14d 0/2) | headgear b | last run 13 days | form 206758 | MARKET 0.3% | 09:00 median 201.00 | Matchbook 500.00
    comment: Fr Gilligansvoyge is hard to fancy after an eighth last time out, and he is winless in his last six, with a second six starts back the only real highlight.
    DATA: model 3.7% | style Prominent (led 3% of runs) | runs in data 14 | last 3: 9 Oct Downpatrick Chase 23.7f Good 7/14; 14 Oct Punchestown (IRE) Chase 21.5f Good 5/8; 9 Nov Punchestown (IRE) Chase 24.5f Good To Yielding 8/12 fig 77
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 77, 34 lb below field average; Official rating 82, 42 lb below field average; Aged 13, older than most of this field

## 12:30 Punchestown | race_id rac_32305304798 | Irish Stallion Farms EBF Maiden Hurdle
Hurdle |  | 2m5f198y | going Good To Yielding | Turf | 16 runners | rating band - | age 4yo+
DATA pace: Even - Two likely leaders (Border Lad, Sine Qua Non). A fair, even gallop is most likely.
- Theflyingking (hrs_41052116) | 6yo G | 166lb | OR 129 | draw 0 | jockey Jack Kennedy | trainer Gordon Elliott (14d 10/75) | headgear t | last run 21 days | form /F2-52 | MARKET 29.9% | 09:00 median 2.63 | Matchbook 2.88
    DATA: model 18.7% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 4 May Down Royal Hurdle 17.4f Good 5/19; 1 Nov Cork (IRE) Hurdle 24.5f Good To Yielding 2/6 fig 121
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Sparkling Wit (hrs_52297924) | 5yo G | 166lb | OR - | draw 0 | jockey Paul Townend | trainer W. P. Mullins (14d 7/31) | headgear - | last run 220 days | form 1- | MARKET 28.7% | 09:00 median 2.75 | Matchbook 3.00
    DATA: model 12.6% | style Held up (led 8% of runs) | runs in data 1 | last 3: 16 Apr Limerick NH Flat 19.3f Soft To Heavy 1/9
    DATA for: Trainer 23% wins (7/31), last 14 days; Last-run finishing speed +10.2% vs that field (finished strongly)
    DATA against: Returns from a 220-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Border Lad (hrs_59429272) | 5yo G | 166lb | OR - | draw 0 | jockey Mike O'Connor | trainer Henry de Bromhead (14d 9/38) | headgear h | last run 255 days | form 12- | MARKET 11.1% | 09:00 median 6.50 | Matchbook 8.60
    DATA: model 9.9% | style Leader (led 57% of runs) | runs in data 1 | last 3: 12 Mar Limerick NH Flat 16.9f Heavy 2/7
    DATA for: Trainer 24% wins (9/38), last 14 days; Last-run finishing speed +3.1% vs that field (finished strongly)
    DATA against: Returns from a 255-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Sine Qua Non (hrs_47345249) | 6yo G | 166lb | OR - | draw 0 | jockey Harry Cobden | trainer Padraig Roche (14d 0/6) | headgear - | last run 232 days | form 13/3P- | MARKET 8.7% | 09:00 median 8.00 | Matchbook 11.50
    DATA: model 9.0% | style Leader (led 38% of runs) | runs in data 2 | last 3: 8 Mar Naas Hurdle 19f Soft To Heavy 3/14; 4 Apr Fairyhouse Hurdle 20f Yielding To Soft PU/25
    DATA against: Returns from a 232-day break; Lightly raced: 2 runs in our data, so the model has little to go on; Race comments mention jumping mistakes in 2 of its last 2 runs; Pulled up in 1 of its last 2 jumps runs
- Angelo Dundee (hrs_35175910) | 7yo G | 166lb | OR - | draw 0 | jockey Keith Donoghue | trainer Mark Edmund McCrory (14d 0/0) | headgear - | last run 169 days | form /23-34 | MARKET 3.9% | 09:00 median 21.00 | Matchbook 25.00
    DATA: model 9.9% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 4 May Down Royal Hurdle 17.4f Good 3/19; 6 Jun Punchestown Hurdle 19.2f Good To Yielding 4/17
    DATA against: Returns from a 169-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- Ravendark (hrs_48643973) | 5yo G | 166lb | OR - | draw 0 | jockey Kevin Healy(7) | trainer Gordon Elliott (14d 10/75) | headgear - | last run 331 days | form 36- | MARKET 3.3% | 09:00 median 23.00 | Matchbook 29.00
    DATA: model 4.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 331-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Excessivebehaviour (hrs_58963107) | 7yo G | 166lb | OR - | draw 0 | jockey Mark Walsh | trainer Martin Brassil (14d 1/4) | headgear t | last run 116 days | form 0-6 | MARKET 2.4% | 09:00 median 29.00 | Matchbook 42.00
    DATA: model 2.1% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 29 Jul Galway Hurdle 22f Good 6/20
    DATA for: Last-run finishing speed +3.3% vs that field (finished strongly)
    DATA against: Returns from a 116-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Beechwood Road (hrs_50906275) | 5yo G | 166lb | OR - | draw 0 | jockey Sean Flanagan | trainer Peter Fahey (14d 3/6) | headgear - | last run 301 days | form 54- | MARKET 2.1% | 09:00 median 29.00 | Matchbook 55.00
    DATA: model 4.3% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 25 Jan Naas NH Flat 18.7f Heavy 4/10
    DATA for: Trainer 50% wins (3/6), last 14 days; Last-run finishing speed +3.0% vs that field (finished strongly)
    DATA against: Returns from a 301-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Inthelineoffire (hrs_17395150563) | 5yo G | 166lb | OR - | draw 0 | jockey Josh Williamson(3) | trainer M F Morris (14d 0/2) | headgear - | last run - days | form - | MARKET 1.8% | 09:00 median 34.00 | Matchbook 90.00
    DATA: model 4.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- C'est Le Capri (hrs_17395890050) | 5yo G | 166lb | OR - | draw 0 | jockey Ross Berry(7) | trainer C A Murphy (14d 0/6) | headgear - | last run 224 days | form P1- | MARKET 1.7% | 09:00 median 34.00 | Matchbook 70.00
    DATA: model 4.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 224-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Strange Ways (hrs_17395891093) | 5yo G | 166lb | OR - | draw 0 | jockey Conor Stone-Walsh | trainer C A Murphy (14d 0/6) | headgear - | last run 316 days | form 2- | MARKET 1.5% | 09:00 median 41.00 | Matchbook 95.00
    DATA: model 4.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 316-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Sharp As Glass (hrs_51865982) | 6yo G | 166lb | OR - | draw 0 | jockey Aidan Kelly | trainer S Curling (14d 1/3) | headgear ht | last run 63 days | form 1223-0 | MARKET 1.5% | 09:00 median 41.00 | Matchbook 100.00
    DATA: model 4.3% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 6 Apr Cork NH Flat 19f Good To Yielding 3/8; 20 Sep Listowel Hurdle 22f Good 11/16
    DATA against: Last-run finishing speed -6.0% vs that field (faded); Lightly raced: 2 runs in our data, so the model has little to go on
- Grey Balls Of Fire (hrs_46697203) | 6yo G | 166lb | OR - | draw 0 | jockey Brian Hayes | trainer C A Murphy (14d 0/6) | headgear - | last run 28 days | form /319-5 | MARKET 1.2% | 09:00 median 51.00 | Matchbook 140.00
    DATA: model 3.0% | style Held up (led 5% of runs) | runs in data 2 | last 3: 17 Jan Navan Hurdle 22f Soft To Heavy 9/12; 25 Oct Wexford (IRE) Hurdle 17f Soft 5/13
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Call Of Freedom (hrs_17395889007) | 6yo G | 166lb | OR - | draw 0 | jockey Shane O'Callaghan(3) | trainer P. J. Rothwell (14d 0/24) | headgear - | last run 235 days | form F1UF- | MARKET 1.1% | 09:00 median 51.00 | Matchbook 160.00
    DATA: model 4.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Trainer 0 wins from 24 runs, last 14 days; Returns from a 235-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Highland Trail (hrs_17394811588) | 5yo G | 166lb | OR - | draw 0 | jockey Harry Sexton(7) | trainer Paul Stafford (14d 0/0) | headgear h (1st time) | last run 22 days | form 0 | MARKET 0.5% | 09:00 median 151.00 | Matchbook 220.00
    DATA: model 2.0% | style Unknown | runs in data 1 | last 3: 31 Oct Down Royal (IRE) NH Flat 17f Good 11/14
    DATA for: First-time headgear
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Any News For Me (hrs_58745820) | 6yo M | 159lb | OR - | draw 0 | jockey Eoghan Finegan(5) | trainer V C Ward (14d 0/0) | headgear - | last run 139 days | form 88-50 | MARKET 0.5% | 09:00 median 151.00 | Matchbook 250.00
    DATA: model 2.0% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 17 Jan Navan NH Flat 16f Soft To Heavy 8/8; 7 Jun Punchestown NH Flat 16.4f Good 5/10; 6 Jul Roscommon NH Flat 15.9f Good 10/16
    DATA for: Last-run finishing speed +2.2% vs that field (finished strongly)
    DATA against: Returns from a 139-day break; First run over hurdles in our data

## 1:00 Punchestown | race_id rac_32305306735 | Pertemps Network Group Handicap Hurdle (Qualifier)
Hurdle |  | 3m0f37y | going Good To Yielding | Turf | 13 runners | rating band - | age 4yo+
DATA pace: Strong pace - 3 habitual front-runners (Staffordshire Knot, Timeless Treaty, J'Arrive de L'Est). A contested lead should set things up for horses coming from behind.
- J'Arrive de L'Est (hrs_34387836) | 7yo G | 142lb | OR 125 | draw 0 | jockey Alan O'Sullivan(5) | trainer Emmet Mullins (14d 2/7) | headgear - | last run 17 days | form 22PP-1 | MARKET 17.5% | 09:00 median 4.50 | Matchbook 5.30 | CHECK (skip line 4.27)
    comment: Fresh from a win last time out just 17 days ago, J'Arrive de L'Est has run over today's trip and going, but two pulled-up efforts before that and 142 lb on his back make him hard to trust.
    DATA: model 7.6% | style Leader (led 23% of runs) | runs in data 4 | last 3: 14 Mar Uttoxeter Chase 34f Soft PU/16; 2 May Punchestown Chase 31.3f Yielding PU/19; 5 Nov Clonmel (IRE) Hurdle 24f Good 1/7 fig 120
    DATA for: Trainer 29% wins (2/7), last 14 days; Has won at this trip or further
    DATA against: Pulled up in 2 of its last 4 jumps runs; Pace: likely to be taken on for the lead
- Santo Sospir (hrs_49757680) | 5yo G | 147lb | OR 130 | draw 0 | jockey Jack Kennedy | trainer Gordon Elliott (14d 10/75) | headgear - | last run 246 days | form 41164- | MARKET 13.2% | 09:00 median 5.50 | Matchbook 7.60
    comment: Santo Sospir won twice in a row three and four starts back, but he has managed just a fourth last time out and a sixth before that, and a 246-day absence raises fitness questions.
    DATA: model 7.1% | style Prominent (led 4% of runs) | runs in data 3 | last 3: 8 Jan Clonmel Hurdle 16.9f Heavy 1/5; 2 Feb Leopardstown Hurdle 22.2f Heavy 6/8; 21 Mar Navan Hurdle 22.7f Soft To Heavy 4/5
    DATA against: Last-run finishing speed -3.5% vs that field (faded); Returns from a 246-day break
- Hgranca De Thaix (hrs_24555244) | 9yo G | 141lb | OR 124 | draw 0 | jockey Daniel King | trainer Barry Connell (14d 0/3) | headgear - | last run 27 days | form 2267-7 | MARKET 10.5% | 09:00 median 8.00 | Matchbook 8.20
    comment: Hgranca De Thaix is winless in his last five and has finished seventh in each of his last two, which makes him hard to fancy, though two seconds four and five starts back show he can get involved.
    DATA: model 6.8% | style Prominent (led 3% of runs) | runs in data 4 | last 3: 8 Mar Naas Hurdle 19f Soft To Heavy 6/17; 6 Apr Fairyhouse Hurdle 21.5f Yielding To Soft 7/15; 26 Oct Galway (IRE) Hurdle 22f Heavy 7/12 fig 120
    DATA for: Carries 6 lb less than average
    DATA against: Official rating 124, 5 lb below field average; Poor recent finishing positions
- Riskaway (hrs_40646942) | 6yo G | 146lb | OR 129 | draw 0 | jockey Josh Williamson(3) | trainer Gordon Elliott (14d 10/75) | headgear - | last run 14 days | form 2404-0 | MARKET 10.1% | 09:00 median 8.00 | Matchbook 9.00
    comment: Riskaway is winless in his last five, though a second five starts back and a fourth two outings ago show he's not out of his depth, and he's had just 14 days since his last run and has run on today's going.
    DATA: model 7.1% | style Midfield (led 3% of runs) | runs in data 4 | last 3: 11 Mar Cheltenham Hurdle 21f Good 17/21; 29 Apr Punchestown Hurdle 19.3f Yielding 4/10; 8 Nov Naas (IRE) Hurdle 20f Good To Yielding 11/20 fig 125
- Buachaillbocht (hrs_33290005) | 8yo G | 140lb | OR 123 | draw 0 | jockey Shane O'Callaghan(3) | trainer T M Walsh (14d 0/2) | headgear tb | last run 230 days | form 360P3- | MARKET 9.3% | 09:00 median 8.50 | Matchbook 9.80
    comment: Buachaillbocht is winless in his last five and returns after 230 days off, which makes him hard to fancy, though a third last time out and a third five starts back show he can get involved.
    DATA: model 4.9% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 1 Feb Leopardstown Chase 21.5f Heavy 15/23; 8 Mar Naas Chase 24.8f Soft To Heavy PU/15; 6 Apr Fairyhouse Hurdle 21.5f Yielding To Soft 3/15
    DATA for: Last-run finishing speed +4.0% vs that field (finished strongly); Carries 7 lb less than average
    DATA against: Official rating 123, 6 lb below field average; Returns from a 230-day break; Pulled up in 1 of its last 3 jumps runs
- Ragmans Corner (hrs_38217606) | 7yo G | 151lb | OR 134 | draw 0 | jockey Eoghan Finegan(5) | trainer Gerard Keane (14d 0/5) | headgear - | last run 58 days | form 42-147 | MARKET 8.5% | 09:00 median 9.50 | Matchbook 11.00
    comment: Ragmans Corner won three starts back and was a fourth two starts back, but he comes here off a seventh last time out and a 58-day break, while carrying 151 lb off 134.
    DATA: model 11.9% | style Prominent (led 3% of runs) | runs in data 5 | last 3: 30 Jul Galway Hurdle 16.1f Yielding To Soft 4/20; 21 Aug Killarney Flat 16.8f Good 1/8; 25 Sep Listowel Hurdle 16f Good To Yielding 7/15
- Paul's Dream (hrs_47985637) | 7yo M | 153lb | OR 136 | draw 0 | jockey J. J. Slevin | trainer Anthony Mullins (14d 0/3) | headgear - | last run 58 days | form 51131P | MARKET 6.2% | 09:00 median 12.00 | Matchbook 16.00
    comment: Pulled up last time out after 58 days off, which is hard to overlook, though she won two starts back and has three wins in her last six and has run on today's going.
    DATA: model 8.7% | style Prominent (led 23% of runs) | runs in data 7 | last 3: 13 Aug Tramore Flat 16f Good 3/9; 7 Sep Galway Hurdle 21.6f Yielding 1/8; 25 Sep Listowel Hurdle 16f Good To Yielding PU/15
    DATA for: Official rating 136, 7 lb above field average
    DATA against: Carries 6 lb more than average; Pulled up in 1 of its last 5 jumps runs
- Shoot First (hrs_24604825) | 10yo G | 151lb | OR 134 | draw 0 | jockey Philip Byrnes | trainer C Byrnes (14d 0/6) | headgear - | last run 27 days | form 5F34-6 | MARKET 5.9% | 09:00 median 13.00 | Matchbook 17.00
    comment: Shoot First has run over today's trip and going, and after a fourth two starts back and a third three starts back he returns fresh after 27 days.
    DATA: model 6.6% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 26 Oct Galway (IRE) Hurdle 22f Heavy 6/12 fig 131
    DATA for: Best recent form figure 131, 8 lb above field average
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on; Aged 10, older than most of this field
- Staffordshire Knot (hrs_33465306) | 8yo G | 166lb | OR 149 | draw 0 | jockey Kevin Healy(7) | trainer Gordon Elliott (14d 10/75) | headgear b | last run 202 days | form 121P-6 | MARKET 4.8% | 09:00 median 15.00 | Matchbook 25.00
    DATA: model 11.8% | style Leader (led 29% of runs) | runs in data 4 | last 3: 8 Feb Navan Hurdle 21.8f Heavy 1/6; 12 Mar Cheltenham Hurdle 24f Good PU/24; 4 May Down Royal Chase 19.7f Good 6/6
    DATA for: Official rating 149, 20 lb above field average
    DATA against: Last-run finishing speed -3.9% vs that field (faded); Carries 19 lb more than average; Returns from a 202-day break; Race comments mention jumping mistakes in 3 of its last 4 runs; Pulled up in 1 of its last 4 jumps runs; Pace: likely to be taken on for the lead
- Timeless Treaty (hrs_52087196) | 6yo G | 150lb | OR 133 | draw 0 | jockey Harry Sexton(7) | trainer R K Watson (14d 0/4) | headgear - | last run 202 days | form 1324-2 | MARKET 4.2% | 09:00 median 19.00 | Matchbook 23.00
    comment: Timeless Treaty has finished in the first four in each of his last five starts, including a second last time out, and he has run over today's trip and on the going before. The one concern is a 202-day absence, with 150 lb to carry too.
    DATA: model 12.9% | style Leader (led 23% of runs) | runs in data 6 | last 3: 5 Mar Thurles Hurdle 22.9f Soft 2/5; 6 Apr Fairyhouse Hurdle 21.5f Yielding To Soft 4/15; 4 May Down Royal Hurdle 24f Good 2/6
    DATA for: Last-run finishing speed +8.3% vs that field (finished strongly); Good recent finishing positions
    DATA against: Returns from a 202-day break; Pace: likely to be taken on for the lead
- Yeats Star (hrs_34961360) | 7yo G | 143lb | OR 126 | draw 0 | jockey Ethan O'Sullivan(7) | trainer Gordon Elliott (14d 10/75) | headgear p | last run 293 days | form 25P0P- | MARKET 3.3% | 09:00 median 23.00 | Matchbook 30.00
    comment: The big risk is fitness: he's been off 293 days and was pulled up last time out.
    DATA: model 2.8% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 2 Feb Leopardstown Hurdle 24.1f Heavy PU/21
    DATA against: Returns from a 293-day break; Lightly raced: 1 run in our data, so the model has little to go on; Pulled up in 1 of its last 1 jumps runs
- Feud (hrs_32061225) | 6yo G | 140lb | OR 120 | draw 0 | jockey Mike O'Connor | trainer Gerard Edmund O'Leary (14d 0/0) | headgear p | last run 21 days | form F-503P | MARKET 3.3% | 09:00 median 21.00 | Matchbook 34.00
    comment: Feud has been out of sorts, pulled up last time out after a third two starts back, and he is winless in his last five.
    DATA: model 6.4% | style Prominent (led 29% of runs) | runs in data 5 | last 3: 26 Sep Listowel Hurdle 20f Good 10/14; 14 Oct Punchestown (IRE) Hurdle 20f Good 3/13 fig 120; 1 Nov Cork (IRE) Hurdle 20f Good To Yielding PU/14
    DATA for: Carries 7 lb less than average
    DATA against: Official rating 120, 9 lb below field average; Race comments mention jumping mistakes in 5 of its last 5 runs; Fell or unseated in 1 of its last 5 jumps runs; Pulled up in 1 of its last 5 jumps runs
- A Tipp For Gold (hrs_37789990) | 7yo G | 140lb | OR 120 | draw 0 | jockey Conor Stone-Walsh | trainer Declan Queally (14d 0/7) | headgear - | last run 571 days | form 8P437/ | MARKET 3.2% | 09:00 median 23.00 | Matchbook 34.00
    comment: Winless in his last five and returning after 571 days off, A Tipp For Gold was seventh last time out, with a third two starts back his best recent effort, so he is hard to fancy under 140 lb. He has run over today's trip and going before, but that is about all in his favour.
    DATA: model 5.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Carries 7 lb less than average
    DATA against: Official rating 120, 9 lb below field average; Returns from a 571-day break; Lightly raced: 0 runs in our data, so the model has little to go on

## 1:30 Punchestown | race_id rac_32305308672 | Colm Quinn BMW Novice Handicap Hurdle
Hurdle |  | 2m0f127y | going Good To Yielding | Turf | 8 runners | rating band - | age 4yo+
DATA pace: Even - Two likely leaders (World As One, Crystabel). A fair, even gallop is most likely.
- Gomez Addams (hrs_55241683) | 5yo G | 164lb | OR 123 | draw 0 | jockey Sean Flanagan | trainer Henry de Bromhead (14d 9/38) | headgear - | last run 117 days | form 15-14 | MARKET 27.0% | 09:00 median 3.25 | Matchbook 3.40 | CHECK (skip line 3.09)
    DATA: model 25.4% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 30 May Listowel Hurdle 16.5f Yielding 1/17; 28 Jul Galway Hurdle 16.5f Good 4/8
    DATA for: Official rating 123, 10 lb above field average; Trainer 24% wins (9/38), last 14 days; Has won at this trip or further
    DATA against: Carries 10 lb more than average; Returns from a 117-day break; Lightly raced: 2 runs in our data, so the model has little to go on; Race comments mention jumping mistakes in 2 of its last 2 runs
- World As One (hrs_51434397) | 5yo G | 153lb | OR 112 | draw 0 | jockey Paul Townend | trainer W. P. Mullins (14d 7/31) | headgear t | last run 31 days | form 4532B2 | MARKET 24.9% | 09:00 median 3.25 | Matchbook 3.85
    comment: World As One arrives in good heart after a second last time out, and he has been in the frame in three of his last six, with a second three starts back and a third four back. He has run over today's trip and going, but he's yet to win and carries 153 lb, which is the main risk.
    DATA: model 21.5% | style Leader (led 29% of runs) | runs in data 7 | last 3: 14 Aug Tramore Hurdle 16.4f Good 2/11; 18 Sep Downpatrick Hurdle 17.8f Good BD/15; 22 Oct Clonmel (IRE) Hurdle 17f Good To Yielding 2/12 fig 108
    DATA for: Trainer 23% wins (7/31), last 14 days; Last-run finishing speed +6.2% vs that field (finished strongly)
    DATA against: Race comments mention jumping mistakes in 4 of its last 5 runs; Fell or unseated in 1 of its last 5 jumps runs
- Bunker Buster (hrs_62813044) | 4yo G | 166lb | OR 125 | draw 0 | jockey Philip Byrnes | trainer C Byrnes (14d 0/6) | headgear h | last run 14 days | form 23-U14 | MARKET 18.7% | 09:00 median 4.50 | Matchbook 5.00
    DATA: model 16.3% | style Midfield (led 4% of runs) | runs in data 5 | last 3: 2 Oct Gowran Park Hurdle 16.4f Good UR/13; 17 Oct Limerick (IRE) Hurdle 17f Yielding 1/16 fig 113; 8 Nov Naas (IRE) Hurdle 16f Good To Yielding 4/4 fig 105
    DATA for: Best recent form figure 113, 9 lb above field average; Official rating 125, 12 lb above field average; Has won at this trip or further
    DATA against: Recent figures 12 lb below its current mark (looks high in the weights); Carries 12 lb more than average; Fell or unseated in 1 of its last 3 jumps runs
- Maxfort (hrs_59928071) | 5yo G | 150lb | OR 109 | draw 0 | jockey Daniel King | trainer N Stokes (14d 0/0) | headgear t (1st time) | last run 180 days | form 345-7 | MARKET 10.8% | 09:00 median 8.50 | Matchbook 8.40
    DATA: model 11.4% | style Prominent (led 3% of runs) | runs in data 4 | last 3: 5 Feb Thurles Hurdle 16.2f Soft 4/17; 26 Feb Clonmel Hurdle 19.3f Heavy 5/16; 26 May Ballinrobe Hurdle 16.1f Good 7/15
    DATA for: First-time headgear
    DATA against: Returns from a 180-day break
- Carrig Padraig (hrs_41171781) | 7yo G | 150lb | OR 109 | draw 0 | jockey Conor Stone-Walsh | trainer Gavin Cromwell (14d 4/42) | headgear h | last run 13 days | form 0-F094 | MARKET 8.1% | 09:00 median 10.00 | Matchbook 12.50
    comment: Fourth last time out and back after just 13 days, Carrig Padraig has run over today's trip and going, but he's winless in his last five and was ninth two starts back.
    DATA: model 4.9% | style Held up (led 3% of runs) | runs in data 5 | last 3: 19 Sep Navan Hurdle 15.8f Good 13/16; 6 Oct Galway Hurdle 16.6f Yielding 9/20; 9 Nov Punchestown (IRE) Hurdle 16f Good To Yielding 4/9 fig 108
    DATA against: Fell or unseated in 1 of its last 5 jumps runs
- Not Too Bad (hrs_29690794) | 7yo G | 163lb | OR 122 | draw 0 | jockey Mark Walsh | trainer Martin Brassil (14d 1/4) | headgear ht (1st time) | last run 1281 days | form 2F238/ | MARKET 5.9% | 09:00 median 13.00 | Matchbook 17.50
    comment: Not Too Bad is lightly raced and unexposed, with a second and a third in his last five outings, though he returns after 1281 days off and was eighth last time out. He is yet to win in that spell and carries 163 lb, so a bold showing may need some improvement.
    DATA: model 10.8% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Official rating 122, 9 lb above field average; First-time headgear
    DATA against: Carries 9 lb more than average; Returns from a 1281-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Crystabel (hrs_45856020) | 5yo M | 141lb | OR 100 | draw 0 | jockey Josh Williamson(3) | trainer John Patrick Ryan (14d 0/7) | headgear - | last run 10 days | form 354557 | MARKET 2.3% | 09:00 median 34.00 | Matchbook 46.00
    comment: Crystabel is winless in her last six, finishing seventh last time out and fifth in two of the three runs before that, so she is hard to fancy off 141 lb.
    DATA: model 4.2% | style Prominent (led 54% of runs) | runs in data 10 | last 3: 10 Oct Fairyhouse Hurdle 16f Good 5/9; 23 Oct Sligo (IRE) Hurdle 17.5f Yielding 5/5; 12 Nov Thurles (IRE) Hurdle 20f Good 7/10 fig 88
    DATA for: Has won at this trip or further; Carries 13 lb less than average
    DATA against: Best recent form figure 88, 16 lb below field average; Recent figures 12 lb below its current mark (looks high in the weights); Official rating 100, 13 lb below field average
- Stepdance (hrs_31300192) | 6yo M | 148lb | OR 107 | draw 0 | jockey Kevin Healy(7) | trainer Declan Queally (14d 0/7) | headgear - | last run 10 days | form 58-P7F | MARKET 2.2% | 09:00 median 41.00 | Matchbook 55.00
    comment: Hard to fancy: Stepdance is winless in her last five, having fallen last time out, a seventh two starts back and pulled up three starts back. She has run over today's trip and going and is back quickly after ten days, but 148 lb is a big ask.
    DATA: model 5.5% | style Prominent (led 4% of runs) | runs in data 7 | last 3: 27 Aug Navan Flat 14f Good 15/22; 1 Oct Clonmel Hurdle 16.8f Good 7/12; 12 Nov Thurles (IRE) Hurdle 20f Good F/10
    DATA for: Carries 6 lb less than average
    DATA against: Official rating 107, 6 lb below field average; Poor recent finishing positions; Race comments mention jumping mistakes in 2 of its last 3 runs; Fell or unseated in 1 of its last 3 jumps runs; Pulled up in 1 of its last 3 jumps runs

## 2:00 Punchestown | race_id rac_32305310609 | Frontline Security Grabel Mares Hurdle (Listed)
Hurdle | Class 1 | 2m2f48y | going Good To Yielding | Turf | 7 runners | rating band - | age 4yo+
DATA pace: Lone leader - Alliteration is the only habitual front-runner and may be allowed an easy lead.
- Oldschool Outlaw (hrs_47837062) | 6yo M | 158lb | OR 137 | draw 0 | jockey Harry Cobden | trainer Gordon Elliott (14d 10/75) | headgear - | last run 231 days | form 11125- | MARKET 68.5% | 09:00 median 1.33 | Matchbook 1.37
    DATA: model 27.9% | style Prominent (led 5% of runs) | runs in data 3 | last 3: 3 Feb Fairyhouse Hurdle 18.4f Soft To Heavy 1/6; 12 Mar Cheltenham Hurdle 16.8f Good 2/22; 5 Apr Fairyhouse Hurdle 20f Yielding To Soft 5/11
    DATA for: Official rating 137, 19 lb above field average; Has won at this trip or further; Good recent finishing positions
    DATA against: Returns from a 231-day break
- Daboya (hrs_40646753) | 5yo M | 151lb | OR 122 | draw 0 | jockey Daniel King | trainer R Donohoe (14d 0/3) | headgear - | last run 14 days | form 41-120 | MARKET 8.8% | 09:00 median 9.00 | Matchbook 12.00
    comment: Daboya won two of her last five, taking the last two of them three and four starts back, then a second two starts back, and she's fit after 14 days off. She has run over today's trip and going, but the unplaced run last time out is the worry, and 151 lb is a big weight.
    DATA: model 16.6% | style Prominent (led 3% of runs) | runs in data 11 | last 3: 21 Sep Listowel Flat 12f Yielding 11/15; 2 Oct Gowran Park Hurdle 16.4f Good 2/6; 8 Nov Naas (IRE) Hurdle 20f Good To Yielding 14/20 fig 112
    DATA for: Best recent form figure 112, 7 lb above field average
- Savante (hrs_38649660) | 7yo M | 151lb | OR 122 | draw 0 | jockey Brian Hayes | trainer C A Murphy (14d 0/6) | headgear t | last run 230 days | form 57215- | MARKET 8.2% | 09:00 median 9.50 | Matchbook 13.00
    comment: The main risk is a 230-day absence, and she was only fifth last time out.
    DATA: model 28.4% | style Held up (led 4% of runs) | runs in data 3 | last 3: 2 Feb Leopardstown Hurdle 24.1f Heavy 2/21; 28 Feb Navan Chase 20.4f Heavy 1/5; 6 Apr Fairyhouse Chase 24.5f Yielding To Soft 5/17
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Returns from a 230-day break
- Alliteration (hrs_58099860) | 5yo M | 147lb | OR 119 | draw 0 | jockey Mark Walsh | trainer J P Dempsey (14d 1/6) | headgear tp | last run 23 days | form 3212-7 | MARKET 7.8% | 09:00 median 11.00 | Matchbook 13.00
    comment: Alliteration makes plenty of appeal, having won three starts back and been second two starts back, with a third five starts back, and she has run over today's trip and going before. The main risk is a seventh last time out, while 147 lb is a hefty burden.
    DATA: model 9.4% | style Leader (led 43% of runs) | runs in data 6 | last 3: 4 Apr Fairyhouse Hurdle 16f Yielding To Soft 1/16; 30 Apr Punchestown Hurdle 16.4f Yielding 2/5; 30 Oct Down Royal (IRE) Hurdle 17f Good To Yielding 7/7 fig 103
    DATA for: Good recent finishing positions; Pace: may get an uncontested lead
    DATA against: Last-run finishing speed -5.2% vs that field (faded)
- Ill Raise A Glass (hrs_42780836) | 6yo M | 151lb | OR 115 | draw 0 | jockey Sean O'Keeffe | trainer Martin Paul Fitzgerald (14d 0/0) | headgear - | last run 204 days | form 81354- | MARKET 2.7% | 09:00 median 29.00 | Matchbook 50.00
    comment: Ill Raise A Glass was fourth last time out and has a win four starts back, with a third three starts back, but she returns after 204 days off and carries 151 lb.
    DATA: model 4.7% | style Held up (led 3% of runs) | runs in data 4 | last 3: 8 Feb Navan Hurdle 20f Heavy 3/7; 12 Mar Limerick Hurdle 22.8f Heavy 5/7; 2 May Punchestown Hurdle 20.5f Yielding 4/4
    DATA for: Has won at this trip or further
    DATA against: Last-run finishing speed -7.2% vs that field (faded); Returns from a 204-day break
- Catchabird (hrs_31672949) | 8yo M | 147lb | OR 109 | draw 0 | jockey Aidan Kelly | trainer Sarah Joanna Connell (14d 0/1) | headgear h | last run 8 days | form 4115-0 | MARKET 2.6% | 09:00 median 41.00 | Matchbook 40.00
    comment: Catchabird won twice in her last five starts, but she's finished unplaced last time out and a fifth two starts back, so the sharpness has faded. She's only eight days since her last run and carries 147 lb, though she has run over today's trip and going.
    DATA: model 5.3% | style Prominent (led 3% of runs) | runs in data 8 | last 3: 21 Mar Navan Hurdle 16f Soft To Heavy 1/12; 30 Apr Punchestown Hurdle 16.4f Yielding 5/5; 14 Nov Navan (IRE) Hurdle 16f Good To Yielding 11/15 fig 99
    DATA against: Best recent form figure 99, 6 lb below field average; Official rating 109, 9 lb below field average
- Likealightswitch (hrs_53328261) | 5yo M | 147lb | OR 105 | draw 0 | jockey Harry Sexton | trainer Adrian Sexton (14d 0/1) | headgear - | last run 36 days | form 210-40 | MARKET 1.3% | 09:00 median 51.00 | Matchbook 130.00
    comment: Likealightswitch has been out of the frame in two of her last three, including last time, and a fourth two starts back hardly screams revival, so she is hard to fancy off 147 lb. In her favour, she won four starts back, has run over today's trip and going, and returns after 36 days.
    DATA: model 7.7% | style Prominent (led 29% of runs) | runs in data 6 | last 3: 6 Apr Fairyhouse Hurdle 16f Yielding To Soft 15/21; 2 Oct Gowran Park Hurdle 16.4f Good 4/6; 17 Oct Limerick (IRE) Hurdle 17f Good To Yielding 12/15
    DATA against: Official rating 105, 13 lb below field average

## 2:30 Punchestown | race_id rac_32305312546 | Matchbook Betting Exchange Craddockstown Novice Steeplechase (Grade 2)
Chase | Class 1 | 2m0f43y | going Good To Yielding | Turf | 6 runners | rating band - | age 4yo+
DATA pace: Lone leader - Ocastle Des Mottes is the only habitual front-runner and may be allowed an easy lead.
- Lovely Hurling (hrs_40493810) | 7yo G | 158lb | OR 145 | draw 0 | jockey Harry Cobden | trainer C A Murphy (14d 0/6) | headgear - | last run 267 days | form 2/222- | MARKET 29.1% | 09:00 median 3.00 | Matchbook 3.35 | CHECK (skip line 2.85)
    DATA: model 16.2% | style Held up (led 8% of runs) | runs in data 1 | last 3: 28 Feb Navan Chase 16f Heavy 2/5
    DATA for: Official rating 145, 9 lb above field average; Last-run finishing speed +4.5% vs that field (finished strongly)
    DATA against: Returns from a 267-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Zanoosh (hrs_40553877) | 6yo M | 151lb | OR - | draw 0 | jockey Brian Hayes | trainer C A Murphy (14d 0/6) | headgear t | last run 207 days | form 11112- | MARKET 27.2% | 09:00 median 3.25 | Matchbook 3.55
    DATA: model 12.3% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 12 Mar Limerick Hurdle 22.8f Heavy 1/7; 5 Apr Fairyhouse Hurdle 20f Yielding To Soft 1/11; 29 Apr Punchestown Hurdle 23.9f Yielding 2/14
    DATA for: Last-run finishing speed +4.0% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Returns from a 207-day break; First run over fences in our data
- Ocastle Des Mottes (hrs_34427911) | 7yo G | 158lb | OR 130 | draw 0 | jockey Paul Townend | trainer W. P. Mullins (14d 7/31) | headgear - | last run 63 days | form 4-P211 | MARKET 19.1% | 09:00 median 4.50 | Matchbook 5.20
    DATA: model 29.4% | style Leader (led 43% of runs) | runs in data 5 | last 3: 31 Jul Galway Chase 22.5f Yielding To Soft 2/9; 7 Sep Galway Chase 18.2f Yielding 1/6; 20 Sep Listowel Chase 17.7f Good 1/5
    DATA for: Trainer 23% wins (7/31), last 14 days; Has won at this trip or further; Good recent finishing positions; Pace: may get an uncontested lead
    DATA against: Official rating 130, 6 lb below field average; Race comments mention jumping mistakes in 2 of its last 5 runs; Pulled up in 1 of its last 5 jumps runs
- Frankie John (hrs_46697140) | 6yo G | 161lb | OR 140 | draw 0 | jockey Daniel King | trainer Denis Gerard Hogan (14d 0/15) | headgear - | last run 21 days | form 48-112 | MARKET 16.0% | 09:00 median 5.50 | Matchbook 6.20
    DATA: model 19.3% | style Prominent (led 3% of runs) | runs in data 7 | last 3: 28 Jul Galway Chase 18.2f Good 1/10; 3 Oct Gowran Park Chase 20f Good To Yielding 1/5; 1 Nov Cork (IRE) Chase 20f Good To Yielding 2/6 fig 135
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Trainer 0 wins from 15 runs, last 14 days
- Kainsbourg (hrs_46295081) | 6yo G | 158lb | OR - | draw 0 | jockey Mark Walsh | trainer Gordon Elliott (14d 10/75) | headgear tp | last run 12 days | form 24-P24 | MARKET 7.6% | 09:00 median 12.00 | Matchbook 12.50
    DATA: model 4.6% | style Held up (led 5% of runs) | runs in data 3 | last 3: 6 Jun Punchestown Chase 24.7f Good To Yielding PU/8; 10 Oct Fairyhouse Chase 21.2f Good 2/6; 10 Nov Fairyhouse (IRE) Chase 20f Good To Yielding 4/9 fig 130
    DATA against: Pulled up in 1 of its last 3 jumps runs
- Soir De Garde (hrs_38105053) | 8yo G | 158lb | OR 129 | draw 0 | jockey Harry Sexton | trainer R K Watson (14d 0/4) | headgear h | last run 53 days | form FP-133 | MARKET 0.9% | 09:00 median 81.00 | Matchbook 180.00
    DATA: model 18.1% | style Prominent (led 3% of runs) | runs in data 6 | last 3: 30 Jun Wexford Chase 16f Good 1/6; 30 Jul Galway Chase 18.2f Yielding To Soft 3/7; 30 Sep Sligo Chase 21f Good 3/6
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Official rating 129, 7 lb below field average; Race comments mention jumping mistakes in 4 of its last 5 runs; Fell or unseated in 1 of its last 5 jumps runs; Pulled up in 1 of its last 5 jumps runs

## 3:00 Punchestown | race_id rac_32303497577 | John Durkan Memorial Punchestown Steeplechase (Grade 1)
Chase | Class 1 | 2m3f150y | going Good To Yielding | Turf | 10 runners | rating band - | age 5yo+
DATA pace: Strong pace - 4 habitual front-runners (Fact To File, Final Demand, Kitzbuhel, The Big Westerner). A contested lead should set things up for horses coming from behind.
- Gaelic Warrior (hrs_24675973) | 8yo G | 166lb | OR 180 | draw 0 | jockey Paul Townend | trainer W. P. Mullins (14d 7/31) | headgear ht | last run 207 days | form 13211- | MARKET 53.0% | 09:00 median 1.67 | Matchbook 1.77
    comment: Gaelic Warrior has won his last two and three of his last five, adding a second and a third in that spell, and he has run over today's trip and going before.
    DATA: model 16.7% | style Midfield (led 5% of runs) | runs in data 3 | last 3: 2 Feb Leopardstown Chase 24.5f Heavy 2/12; 13 Mar Cheltenham Chase 26.3f Good To Soft 1/10; 29 Apr Punchestown Chase 25f Yielding 1/5
    DATA for: Official rating 180, 17 lb above field average; Trainer 23% wins (7/31), last 14 days; Last-run finishing speed +9.5% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Returns from a 207-day break
- Fact To File (hrs_28824691) | 9yo G | 166lb | OR 173 | draw 0 | jockey Harry Cobden | trainer W. P. Mullins (14d 7/31) | headgear - | last run 207 days | form /2612- | MARKET 19.3% | 09:00 median 4.33 | Matchbook 5.20
    comment: The main risk is a 207-day absence, plus 166 lb on his back.
    DATA: model 10.9% | style Leader (led 38% of runs) | runs in data 2 | last 3: 2 Feb Leopardstown Chase 24.5f Heavy 1/12; 29 Apr Punchestown Chase 25f Yielding 2/5
    DATA for: Official rating 173, 10 lb above field average; Trainer 23% wins (7/31), last 14 days; Last-run finishing speed +2.5% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Returns from a 207-day break; Lightly raced: 2 runs in our data, so the model has little to go on; Pace: likely to be taken on for the lead
- Final Demand (hrs_39431504) | 7yo G | 166lb | OR 156 | draw 0 | jockey Mr P. W. Mullins | trainer W. P. Mullins (14d 7/31) | headgear - | last run 256 days | form /113D- | MARKET 6.6% | 09:00 median 12.00 | Matchbook 15.50
    comment: He does have a third two starts back and wins three and four starts back, but he carries 166 lb off 156.
    DATA: model 9.9% | style Leader (led 38% of runs) | runs in data 2 | last 3: 1 Feb Leopardstown Chase 21.5f Heavy 3/4; 11 Mar Cheltenham Chase 25f Good 2/14
    DATA for: Trainer 23% wins (7/31), last 14 days; Last-run finishing speed +3.1% vs that field (finished strongly); Good recent finishing positions
    DATA against: Official rating 156, 7 lb below field average; Returns from a 256-day break; Lightly raced: 2 runs in our data, so the model has little to go on; Pace: likely to be taken on for the lead
- Kitzbuhel (hrs_40920628) | 6yo G | 166lb | OR 155 | draw 0 | jockey Daniel King | trainer W. P. Mullins (14d 7/31) | headgear - | last run 208 days | form 11U1P- | MARKET 5.8% | 09:00 median 12.00 | Matchbook 20.00
    comment: Kitzbuhel has won three of his last five, including a win two starts back, but he was pulled up last time out and returns after 208 days off.
    DATA: model 8.0% | style Leader (led 54% of runs) | runs in data 3 | last 3: 31 Jan Sandown Chase 20.1f Soft UR/4; 11 Mar Cheltenham Chase 25f Good 1/14; 28 Apr Punchestown Chase 25f Yielding PU/9
    DATA for: Trainer 23% wins (7/31), last 14 days; Has won at this trip or further
    DATA against: Official rating 155, 8 lb below field average; Returns from a 208-day break; Race comments mention jumping mistakes in 3 of its last 3 runs; Fell or unseated in 1 of its last 3 jumps runs; Pulled up in 1 of its last 3 jumps runs; Pace: likely to be taken on for the lead
- Kaid d'Authie (hrs_34932135) | 6yo G | 166lb | OR 158 | draw 0 | jockey Jack Kennedy | trainer W. P. Mullins (14d 7/31) | headgear p | last run 256 days | form /211F- | MARKET 5.3% | 09:00 median 15.00 | Matchbook 19.50
    DATA: model 7.9% | style Prominent (led 4% of runs) | runs in data 3 | last 3: 1 Jan Fairyhouse Chase 21.8f Yielding 1/7; 1 Feb Leopardstown Chase 21.5f Heavy 1/4; 11 Mar Cheltenham Chase 25f Good F/14
    DATA for: Trainer 23% wins (7/31), last 14 days; Has won at this trip or further
    DATA against: Official rating 158, 5 lb below field average; Returns from a 256-day break; Fell or unseated in 1 of its last 3 jumps runs
- Impaire Et Passe (hrs_33067363) | 8yo G | 166lb | OR 160 | draw 0 | jockey J. J. Slevin | trainer W. P. Mullins (14d 7/31) | headgear p | last run 227 days | form B/1PF- | MARKET 3.8% | 09:00 median 19.00 | Matchbook 30.00
    comment: Returning from a 227-day absence since falling last time out, Impaire Et Passe has a win three starts back to point to and has run over today's trip and going, but a fall, a pulled up and a brought down in his last four make it a patchy profile.
    DATA: model 6.5% | style Midfield (led 5% of runs) | runs in data 3 | last 3: 14 Feb Gowran Park Chase 19.3f Heavy 1/4; 12 Mar Cheltenham Chase 20.6f Good PU/7; 9 Apr Aintree Chase 25f Good To Soft F/5
    DATA for: Trainer 23% wins (7/31), last 14 days; Has won at this trip or further
    DATA against: Returns from a 227-day break; Race comments mention jumping mistakes in 2 of its last 3 runs; Fell or unseated in 1 of its last 3 jumps runs; Pulled up in 1 of its last 3 jumps runs
- The Big Westerner (hrs_39826976) | 7yo M | 159lb | OR 149 | draw 0 | jockey Mike O'Connor | trainer Henry de Bromhead (14d 9/38) | headgear - | last run 18 days | form P/21-1 | MARKET 3.4% | 09:00 median 23.00 | Matchbook 32.00
    DATA: model 14.3% | style Leader (led 57% of runs) | runs in data 1 | last 3: 4 Nov Wexford (IRE) Chase 23f Yielding 1/4 fig 150
    DATA for: Trainer 24% wins (9/38), last 14 days; Last-run finishing speed +2.8% vs that field (finished strongly); Has won at this trip or further
    DATA against: Official rating 149, 14 lb below field average; Lightly raced: 1 run in our data, so the model has little to go on; Pace: likely to be taken on for the lead
- I Am Maximus (hrs_22840202) | 10yo G | 166lb | OR 173 | draw 0 | jockey Mark Walsh | trainer W. P. Mullins (14d 7/31) | headgear - | last run 225 days | form /9251- | MARKET 1.1% | 09:00 median 67.00 | Matchbook 110.00
    comment: The one concern is a 225-day absence.
    DATA: model 14.3% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 2 Feb Leopardstown Chase 24.5f Heavy 5/12; 11 Apr Aintree Chase 34.3f Good To Soft 1/34
    DATA for: Official rating 173, 10 lb above field average; Trainer 23% wins (7/31), last 14 days; Last-run finishing speed +10.2% vs that field (finished strongly); Has won at this trip or further
    DATA against: Returns from a 225-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- Nick Rockett (hrs_27237777) | 9yo G | 166lb | OR 168 | draw 0 | jockey Sean O'Keeffe | trainer W. P. Mullins (14d 7/31) | headgear - | last run 250 days | form 111/3- | MARKET 0.8% | 09:00 median 81.00 | Matchbook 180.00
    comment: Nick Rockett won three of his last four starts before finishing third last time out, and has run over today's trip and going before.
    DATA: model 6.2% | style Unknown | runs in data 1 | last 3: 17 Mar Down Royal Chase 26.2f Good To Yielding 3/4
    DATA for: Trainer 23% wins (7/31), last 14 days
    DATA against: Returns from a 250-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Grangeclare West (hrs_23111382) | 10yo G | 166lb | OR 161 | draw 0 | jockey Brian Hayes | trainer W. P. Mullins (14d 7/31) | headgear - | last run 207 days | form 481U3- | MARKET 0.8% | 09:00 median 101.00 | Matchbook 170.00
    comment: Grangeclare West returns from 207 days off having finished third last time out, and he's a winner three starts back, with experience of today's trip and going; carrying 166 lb off an official mark of 161, the layoff is the main risk.
    DATA: model 5.4% | style Midfield (led 4% of runs) | runs in data 4 | last 3: 21 Feb Fairyhouse Chase 26f Heavy 1/9; 11 Apr Aintree Chase 34.3f Good To Soft UR/34; 29 Apr Punchestown Chase 25f Yielding 3/5
    DATA for: Trainer 23% wins (7/31), last 14 days; Has won at this trip or further
    DATA against: Last-run finishing speed -2.8% vs that field (faded); Returns from a 207-day break; Fell or unseated in 1 of its last 4 jumps runs

## 3:30 Punchestown | race_id rac_32305314483 | Keadeen Hotel (Pro/Am) Flat Race
NH Flat |  | 2m0f127y | going Good To Yielding | Turf | 10 runners | rating band - | age 4yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Ceasar's Ball (hrs_17395893179) | 4yo G | 168lb | OR - | draw 0 | jockey Mr P. W. Mullins | trainer W. P. Mullins (14d 7/31) | headgear - | last run 235 days | form 1- | MARKET 33.1% | 09:00 median 2.50 | Matchbook 2.76
    comment: Won last time out in his only recent start, but he returns after 235 days off and carries 168 lb. Lightly raced and unexposed, he could have more to offer, though the layoff is a question.
    DATA: model 8.6% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 23% wins (7/31), last 14 days
    DATA against: Returns from a 235-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Water Mill (hrs_17394712503) | 5yo G | 168lb | OR - | draw 0 | jockey Mr H C Swan | trainer Gordon Elliott (14d 10/75) | headgear - | last run 23 days | form 2-2 | MARKET 26.6% | 09:00 median 3.00 | Matchbook 3.65
    comment: Water Mill comes here in fine nick, runner-up last time out and a second two starts back, and he's fit enough off a 23-day break to be a serious threat under 168 lb.
    DATA: model 16.5% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 30 Oct Down Royal (IRE) Hurdle 22.5f Yielding 2/9 fig 101
    DATA for: Best recent form figure 101, 5 lb above field average; Last-run finishing speed +4.9% vs that field (finished strongly)
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Doyouhearmenow (hrs_17395895265) | 4yo G | 168lb | OR - | draw 0 | jockey Mr J L Gleeson | trainer Martin Brassil (14d 1/4) | headgear t (1st time) | last run - days | form - | MARKET 11.5% | 09:00 median 7.00 | Matchbook 8.40
    comment: Doyouhearmenow is unexposed on his debut with no form to go on, so he's open to improvement. The gelding shoulders 168 lb, a hefty burden for a newcomer, and that's the main angle here.
    DATA: model 8.6% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: First-time headgear
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Night Chaperone (hrs_64555015) | 4yo G | 168lb | OR - | draw 0 | jockey Mr B Doyle Murphy(7) | trainer Liz Doyle (14d 0/0) | headgear - | last run 197 days | form 2 | MARKET 8.9% | 09:00 median 8.50 | Matchbook 11.50
    DATA: model 15.9% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 9 May Killarney NH Flat 17f Good To Yielding 2/13
    DATA for: Last-run finishing speed +9.5% vs that field (finished strongly)
    DATA against: Returns from a 197-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Doctor Grimwig (hrs_17395894222) | 4yo G | 168lb | OR - | draw 0 | jockey Mr Finn Tegetmeier(7) | trainer Noel Meade (14d 3/15) | headgear - | last run - days | form - | MARKET 7.8% | 09:00 median 10.00 | Matchbook 13.00
    comment: He carries 168 lb on his debut.
    DATA: model 8.6% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 20% wins (3/15), last 14 days
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Some See Stars (hrs_39996607) | 6yo G | 168lb | OR - | draw 0 | jockey Miss H Ross(7) | trainer A L T Moore (14d 0/0) | headgear - | last run 22 days | form 67-P32 | MARKET 5.1% | 09:00 median 15.00 | Matchbook 19.50
    comment: Some See Stars arrives in good heart after a second last time out and a third two starts back, and he has run over today's trip and going before.
    DATA: model 15.9% | style Held up (led 3% of runs) | runs in data 6 | last 3: 12 May Sligo NH Flat 17.8f Good PU/15; 10 Oct Fairyhouse NH Flat 16f Good 3/10; 31 Oct Down Royal (IRE) NH Flat 17f Good 2/14 fig 97
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Ballygambon Bobo (hrs_17395892136) | 4yo G | 168lb | OR - | draw 0 | jockey Mr R W Barron(5) | trainer Conor Houlihan (14d 0/3) | headgear - | last run - days | form - | MARKET 3.9% | 09:00 median 23.00 | Matchbook 22.00
    comment: Ballygambon Bobo is an unraced gelding with no recorded form, so he's an unknown quantity and open to improvement. He carries 168 lb on his first start, and there's little to go on beyond that.
    DATA: model 8.6% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Pillars Presence (hrs_17392985295) | 4yo G | 168lb | OR - | draw 0 | jockey Mr J Conheady(7) | trainer James Conheady (14d 0/0) | headgear - | last run 27 days | form 94 | MARKET 1.8% | 09:00 median 34.00 | Matchbook 90.00
    comment: The main risk is the 168 lb he carries, with the pair of recent runs still leaving him yet to win.
    DATA: model 8.1% | style Held up (led 5% of runs) | runs in data 2 | last 3: 28 Sep Roscommon NH Flat 15.6f Good To Yielding 9/16; 26 Oct Galway (IRE) NH Flat 16.5f Heavy 4/7 fig 89
    DATA against: Best recent form figure 89, 7 lb below field average; Lightly raced: 2 runs in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Jukebox Charlie (hrs_59928631) | 5yo G | 168lb | OR - | draw 0 | jockey Mr D O'Sullivan(7) | trainer P A Fahy (14d 0/9) | headgear - | last run 194 days | form 00-7 | MARKET 0.7% | 09:00 median 101.00 | Matchbook 220.00
    comment: Jukebox Charlie returns after 194 days, having finished seventh last time out and unplaced in the two runs before, so he's yet to win in recent form. He carries 168 lb, but he looks unexposed and open to improvement.
    DATA: model 4.6% | style Midfield (led 8% of runs) | runs in data 2 | last 3: 1 May Punchestown NH Flat 18.8f Yielding 21/21; 12 May Sligo NH Flat 17.8f Good 7/15
    DATA against: Trainer 0 wins from 9 runs, last 14 days; Returns from a 194-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- Quinta Dourada (hrs_17394962823) | 5yo M | 161lb | OR - | draw 0 | jockey Kevin Healy(7) | trainer Miss Hilary McLoughlin (14d 0/1) | headgear - | last run 14 days | form 0 | MARKET 0.6% | 09:00 median 101.00 | Matchbook 280.00
    comment: Quinta Dourada is unexposed after just one recent start, when she finished unplaced, and she returns quickly after 14 days. Yet to win, she carries 161 lb and has scope to improve.
    DATA: model 4.5% | style Held up (led 8% of runs) | runs in data 1 | last 3: 8 Nov Naas (IRE) NH Flat 16f Good To Yielding 13/17
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
