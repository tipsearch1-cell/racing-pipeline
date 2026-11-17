# Card review packet: Limerick, 2026-11-17

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
   treat it as one opinion, not the answer); "fig" is a performance figure (higher = better) for that past run;
   "for"/"against" are derived facts (figures vs field, vs mark, pace fit, jumping errors, finishing speed).
4. Runners marked CHECK are the market favourite. Give a verdict, BET or SKIP, with a one-line reason:
   BET unless the card or the DATA lines give a specific reason to doubt the favourite (then lower its chance and SKIP).
   You do not need to do any price arithmetic; the price check (skip line shown) is applied afterwards.

Write valid JSON to the out path you were given, exactly this shape (use the exact race_id and horse_id values):
{"meeting": "limerick", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 12:10 Limerick | race_id rac_32304686895 | Conference & Banqueting Facilities At Limerick Racecourse Maiden Hurdle
Hurdle |  | 2m2f150y | going Yielding | Turf | 17 runners | rating band - | age 4yo+
DATA pace: Lone leader - Go Loud is the only habitual front-runner and may be allowed an easy lead.
- Poet's Duke (hrs_50906191) | 5yo G | 166lb | OR - | draw 0 | jockey Alan O'Sullivan(5) | trainer Paul Nolan (14d 5/25) | headgear p (1st time) | last run 31 days | form 75-07 | MARKET 23.3% | 09:00 median 2.63 | Matchbook -
    DATA: model 17.0% | style Prominent (led 5% of runs) | runs in data 3 | last 3: 10 Apr Wexford 20f Good To Yielding 5/8; 15 May Kilbeggan 15.7f Good 14/14; 17 Oct Limerick (IRE) 19f Good To Yielding 7/18 fig 86
    DATA for: Best recent form figure 86, 4 lb above field average; Trainer 20% wins (5/25), last 14 days; First-time headgear
- Con Did It (hrs_17391069304) | 6yo G | 166lb | OR - | draw 0 | jockey Thomas O'Connor(7) | trainer Eoin Christopher McCarthy (14d 0/9) | headgear - | last run 12 days | form 55 | MARKET 15.1% | 09:00 median 3.75 | Matchbook -
    DATA: model 8.9% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 20 Sep Listowel 16f Good 5/13; 5 Nov Clonmel (IRE) 19.5f Good 5/12 fig 80
    DATA against: Trainer 0 wins from 9 runs, last 14 days; Lightly raced: 2 runs in our data, so the model has little to go on
- Western Note (hrs_52496241) | 6yo G | 166lb | OR - | draw 0 | jockey Kevin Healy(7) | trainer Gordon Elliott (14d 12/73) | headgear - | last run 534 days | form 6P- | MARKET 11.6% | 09:00 median 5.50 | Matchbook -
    DATA: model 4.0% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 534-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Go Loud (hrs_58963282) | 5yo G | 166lb | OR - | draw 0 | jockey Ben Harvey | trainer Cian Collins (14d 1/9) | headgear - | last run 136 days | form P65-69 | MARKET 7.9% | 09:00 median 9.00 | Matchbook -
    DATA: model 10.2% | style Leader (led 72% of runs) | runs in data 2 | last 3: 6 Jun Punchestown 16.5f Good To Yielding 6/18; 4 Jul Bellewstown 17.2f Good 9/16
    DATA for: Pace: may get an uncontested lead
    DATA against: Returns from a 136-day break; Lightly raced: 2 runs in our data, so the model has little to go on; First run over hurdles in our data
- Man Down (hrs_17391270603) | 5yo G | 166lb | OR 94 | draw 0 | jockey  | trainer Donncha Duggan (14d 0/2) | headgear - | last run 16 days | form P0679U | MARKET 7.3% | 09:00 median 7.80 | Matchbook 13.50
    DATA: model 17.8% | style Held up (led 3% of runs) | runs in data 5 | last 3: 25 Sep Listowel 18.6f Good To Yielding 7/15; 17 Oct Limerick (IRE) 19f Good To Yielding 9/18 fig 84; 1 Nov Cork (IRE) 20f Good To Yielding UR/14
    DATA against: Poor recent finishing positions; Fell or unseated in 1 of its last 5 jumps runs
- Attaho (hrs_39699051) | 6yo G | 166lb | OR - | draw 0 | jockey  | trainer Martin Brassil (14d 0/3) | headgear ht | last run 386 days | form 389/P- | MARKET 6.1% | 09:00 median 12.00 | Matchbook -
    DATA: model 4.0% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 386-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Storm Bresie (hrs_17393382678) | 4yo G | 166lb | OR - | draw 0 | jockey Shane O'Callaghan(3) | trainer P. J. Rothwell (14d 0/24) | headgear - | last run 10 days | form 2P-385 | MARKET 5.5% | 09:00 median 11.00 | Matchbook -
    DATA: model 5.7% | style Held up (led 5% of runs) | runs in data 2 | last 3: 6 Oct Galway 16.6f Yielding 8/20; 7 Nov Gowran Park (IRE) 16f Good To Yielding 5/12
    DATA against: Trainer 0 wins from 24 runs, last 14 days; Lightly raced: 2 runs in our data, so the model has little to go on
- Days Go By (hrs_17392706814) | 4yo G | 166lb | OR - | draw 0 | jockey Kevin A Murphy(7) | trainer E McNamara (14d 0/6) | headgear - | last run 31 days | form 2-67 | MARKET 4.8% | 09:00 median 15.00 | Matchbook -
    DATA: model 6.7% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 24 Sep Listowel 16f Good 6/9; 17 Oct Limerick (IRE) 17f Yielding 7/16
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Aint Over Yet (hrs_57878149) | 5yo M | 159lb | OR - | draw 0 | jockey Carl Millar(5) | trainer Nigel Thomas Slevin (14d 0/2) | headgear - | last run 7 days | form 80P-15 | MARKET 3.3% | 09:00 median 19.00 | Matchbook -
    DATA: model 1.8% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 12 Jan Punchestown 16.2f Soft To Heavy 12/13; 4 Feb Punchestown 23f Soft To Heavy PU/8; 10 Nov Fairyhouse (IRE) 16f Good To Yielding 5/5 fig 88
    DATA for: Best recent form figure 88, 6 lb above field average
    DATA against: Pulled up in 1 of its last 1 jumps runs
- Awordinyourear (hrs_59961552) | 5yo G | 166lb | OR - | draw 0 | jockey John Shinnick | trainer Terence O'Brien (14d 1/4) | headgear - | last run 46 days | form 90-0 | MARKET 2.9% | 09:00 median 26.00 | Matchbook -
    DATA: model 2.5% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 7 Feb Naas 18.5f Soft To Heavy 9/12; 22 Feb Naas 15.5f Heavy 19/21; 2 Oct Gowran Park 16.4f Good 18/20
    DATA against: Last-run finishing speed -10.0% vs that field (faded); Poor recent finishing positions
- Grandioso (hrs_48052396) | 6yo G | 166lb | OR - | draw 0 | jockey Ross Berry(7) | trainer J A Berry (14d 0/1) | headgear - | last run 24 days | form P/P-F | MARKET 2.4% | 09:00 median 29.00 | Matchbook -
    DATA: model 4.0% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Nothingtodowithyou (hrs_35054740) | 7yo G | 166lb | OR - | draw 0 | jockey  | trainer Alexander Ott (14d 0/1) | headgear - | last run 12 days | form 828U/9 | MARKET 2.2% | 09:00 median 34.00 | Matchbook -
    DATA: model 2.1% | style Held up (led 8% of runs) | runs in data 1 | last 3: 5 Nov Clonmel (IRE) 19.5f Good 9/12
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Eagle Doll (hrs_63650139) | 6yo M | 159lb | OR - | draw 0 | jockey E Walsh | trainer Eoin Christopher McCarthy (14d 0/9) | headgear - | last run 9 days | form P-U9 | MARKET 1.9% | 09:00 median 41.00 | Matchbook -
    DATA: model 2.2% | style Held up (led 4% of runs) | runs in data 3 | last 3: 14 Apr Clonmel 19.8f Yielding PU/17; 1 Nov Cork (IRE) 16f Good To Yielding UR/19; 8 Nov Naas (IRE) 16f Good To Yielding 9/12 fig 72
    DATA against: Best recent form figure 72, 10 lb below field average; Trainer 0 wins from 9 runs, last 14 days; Poor recent finishing positions; Fell or unseated in 1 of its last 3 jumps runs; Pulled up in 1 of its last 3 jumps runs
- George's Order (hrs_17391932908) | 5yo M | 159lb | OR - | draw 0 | jockey Rian Lane(7) | trainer Sean Joseph Allen (14d 0/1) | headgear - | last run 30 days | form 06 | MARKET 1.6% | 09:00 median 51.00 | Matchbook -
    DATA: model 3.4% | style Prominent (led 8% of runs) | runs in data 2 | last 3: 7 Sep Galway 16.7f Soft 15/18; 18 Oct Limerick (IRE) 16.5f Good To Yielding 6/7
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Matcho d'Agrostis (hrs_63357560) | 4yo G | 166lb | OR - | draw 0 | jockey Richard Deegan | trainer Paul Nolan (14d 5/25) | headgear - | last run 136 days | form F-F00 | MARKET 1.6% | 09:00 median 51.00 | Matchbook -
    DATA: model 3.5% | style Held up (led 3% of runs) | runs in data 4 | last 3: 13 May Punchestown 16f Good To Yielding F/8; 6 Jun Punchestown 16.5f Good To Yielding 16/22; 4 Jul Bellewstown 17.2f Good 12/16
    DATA for: Trainer 20% wins (5/25), last 14 days
    DATA against: Last-run finishing speed -5.9% vs that field (faded); Poor recent finishing positions; Returns from a 136-day break; Fell or unseated in 2 of its last 4 jumps runs
- Castle Garden (hrs_17391353000) | 4yo F | 159lb | OR - | draw 0 | jockey Philip Donovan | trainer Brian Hassett (14d 0/0) | headgear - | last run 23 days | form 39B | MARKET 1.5% | 09:00 median 67.00 | Matchbook -
    DATA: model 3.3% | style Held up (led 5% of runs) | runs in data 2 | last 3: 24 Aug Ballinrobe 22.3f Good 9/12; 25 Oct Galway (IRE) 21.5f Soft BD/12
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Fell or unseated in 1 of its last 2 jumps runs
- Checkpoint Georgie (hrs_62202182) | 4yo G | 166lb | OR - | draw 0 | jockey John Aherne(7) | trainer A M O'Grady (14d 0/0) | headgear - | last run 236 days | form 00- | MARKET 1.2% | 09:00 median 81.00 | Matchbook -
    DATA: model 2.8% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 7 Mar Gowran Park 16.2f Heavy 10/18; 26 Mar Clonmel 16f Soft 14/16
    DATA against: Last-run finishing speed -6.0% vs that field (faded); Returns from a 236-day break; Lightly raced: 2 runs in our data, so the model has little to go on

## 12:40 Limerick | race_id rac_32304688832 | Adare Manor Opportunity Maiden Hurdle
Hurdle |  | 2m | going Yielding | Turf | 17 runners | rating band - | age 4yo+
DATA pace: Even - Two likely leaders (Colossal Impact, Detroit Maverick). A fair, even gallop is most likely.
- Detroit Maverick (hrs_47620930) | 6yo G | 166lb | OR - | draw 0 | jockey Josh Williamson | trainer Gordon Elliott (14d 12/73) | headgear t (1st time) | last run 26 days | form 225-33 | MARKET 32.0% | 09:00 median 2.10 | Matchbook 2.00
    DATA: model 23.0% | style Leader (led 63% of runs) | runs in data 5 | last 3: 26 Mar Clonmel 16f Soft 5/8; 2 Oct Gowran Park 16.4f Good 3/20; 22 Oct Clonmel (IRE) 17f Good To Yielding 3/12 fig 99
    DATA for: Last-run finishing speed +2.8% vs that field (finished strongly); Good recent finishing positions; First-time headgear
- Burning Like Fire (hrs_17389186689) | 4yo F | 159lb | OR - | draw 0 | jockey Michael Kenneally | trainer Denis Gerard Hogan (14d 1/13) | headgear - | last run 13 days | form 3-002 | MARKET 13.4% | 09:00 median 5.50 | Matchbook -
    DATA: model 3.5% | style Held up (led 5% of runs) | runs in data 3 | last 3: 30 Jul Galway 18f Good 14/16; 28 Aug Wexford 24.2f Yielding 10/12; 4 Nov Wexford (IRE) 16.5f Yielding 2/14 fig 99
    DATA for: Last-run finishing speed +6.4% vs that field (finished strongly)
- Keep Kool Coko (hrs_39996516) | 6yo G | 166lb | OR 108 | draw 0 | jockey Josh Younge(4) | trainer A. Slattery (14d 0/13) | headgear - | last run 520 days | form 6/233- | MARKET 12.7% | 09:00 median 5.50 | Matchbook -
    DATA: model 6.9% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Trainer 0 wins from 13 runs, last 14 days; Returns from a 520-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Abando (hrs_52417876) | 4yo G | 166lb | OR 104 | draw 0 | jockey James Smith | trainer A. McCann (14d 0/4) | headgear p | last run 17 days | form 342 | MARKET 8.3% | 09:00 median 9.00 | Matchbook -
    DATA: model 19.6% | style Prominent (led 23% of runs) | runs in data 8 | last 3: 28 Sep Roscommon 15.6f Good To Yielding 3/13; 5 Oct Fairyhouse 16f Good 4/11; 31 Oct Down Royal (IRE) 17f Good 2/12
    DATA for: Good recent finishing positions
    DATA against: Race comments mention jumping mistakes in 2 of its last 3 runs
- Le Vent d'Ex (hrs_49757778) | 5yo G | 166lb | OR 102 | draw 0 | jockey Kevin A Murphy(4) | trainer Michael Winters (14d 1/3) | headgear - | last run 12 days | form -00002 | MARKET 7.5% | 09:00 median 11.00 | Matchbook -
    DATA: model 3.2% | style Held up (led 3% of runs) | runs in data 5 | last 3: 24 Sep Listowel 16f Good 12/14; 8 Oct Tramore 20.4f Yielding 11/12; 5 Nov Clonmel (IRE) 16.5f Good 2/11 fig 103
    DATA for: Best recent form figure 103, 6 lb above field average
- Ludus Magnus (hrs_52451686) | 5yo G | 166lb | OR - | draw 0 | jockey Niall Moore(2) | trainer Philip Fenton (14d 0/3) | headgear - | last run 22 days | form 40-4U5 | MARKET 7.2% | 09:00 median 8.00 | Matchbook 18.00
    DATA: model 8.7% | style Prominent (led 4% of runs) | runs in data 5 | last 3: 12 May Sligo 17.8f Good 4/15; 6 Jun Punchestown 16.5f Good To Yielding UR/22; 26 Oct Galway (IRE) 16.5f Soft To Heavy 5/20 fig 90
    DATA against: Best recent form figure 90, 7 lb below field average; Fell or unseated in 1 of its last 3 jumps runs
- Colossal Impact (hrs_51185855) | 5yo G | 166lb | OR - | draw 0 | jockey Shane O'Callaghan | trainer P. J. Rothwell (14d 0/24) | headgear - | last run 25 days | form 3-44 | MARKET 3.5% | 09:00 median 26.00 | Matchbook -
    DATA: model 9.0% | style Leader (led 54% of runs) | runs in data 3 | last 3: 21 Mar Navan 16f Soft 3/9; 8 Oct Tramore 16f Yielding 4/8; 23 Oct Sligo (IRE) 25.5f Yielding To Soft 4/5
    DATA against: Trainer 0 wins from 24 runs, last 14 days
- Macoo (hrs_17390119131) | 8yo G | 166lb | OR - | draw 0 | jockey Luke Burke Ott(4) | trainer Paul O'Flynn (14d 0/0) | headgear p | last run 31 days | form 984 | MARKET 2.7% | 09:00 median 34.00 | Matchbook -
    DATA: model 2.8% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 22 Aug Killarney 16.5f Good 9/16; 23 Sep Listowel 20f Good 8/11; 17 Oct Limerick (IRE) 19f Good To Yielding 4/18 fig 96
    DATA against: Aged 8, older than most of this field
- Eleen Alana (hrs_66463411) | 5yo M | 159lb | OR - | draw 0 | jockey  | trainer Eoin Griffin (14d 0/2) | headgear - | last run 38 days | form 3077 | MARKET 2.2% | 09:00 median 51.00 | Matchbook -
    DATA: model 4.0% | style Prominent (led 3% of runs) | runs in data 4 | last 3: 1 Aug Galway 16.8f Good To Yielding 14/18; 18 Sep Downpatrick 17.8f Good 7/12; 10 Oct Fairyhouse 16f Good 7/10
    DATA against: Poor recent finishing positions; First run over hurdles in our data
- Daddy's Cupcake (hrs_17395530215) | 5yo M | 159lb | OR - | draw 0 | jockey  | trainer Ray Hackett (14d 0/4) | headgear - | last run - days | form - | MARKET 2.1% | 09:00 median 34.00 | Matchbook -
    DATA: model 3.1% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Gerrymadiddler (hrs_17392904984) | 6yo G | 166lb | OR - | draw 0 | jockey Conor Smithers(4) | trainer Liam P Cusack (14d 0/1) | headgear h | last run 46 days | form P-F | MARKET 1.8% | 09:00 median 81.00 | Matchbook -
    DATA: model 1.8% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 2 Oct Gowran Park 16.4f Good F/20
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on; Fell or unseated in 1 of its last 1 jumps runs
- Don't Fusseme (hrs_17394956565) | 4yo G | 166lb | OR - | draw 0 | jockey Eoin Staples | trainer Paul John Gilligan (14d 0/2) | headgear h (1st time) | last run 12 days | form 60 | MARKET 1.6% | 09:00 median 67.00 | Matchbook -
    DATA: model 4.2% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 5 Nov Clonmel (IRE) 19.5f Good 11/12
    DATA for: First-time headgear
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Saoirses Choice (hrs_64780996) | 6yo M | 159lb | OR - | draw 0 | jockey Alix Balfe(4) | trainer Francis Casey (14d 0/0) | headgear t (1st time) | last run 38 days | form 499U | MARKET 1.4% | 09:00 median 81.00 | Matchbook -
    DATA: model 1.6% | style Held up (led 3% of runs) | runs in data 5 | last 3: 6 Aug Sligo 17.9f Good 9/13; 28 Aug Down Royal 17.4f Good UR/10; 10 Oct Naas 7f Soft 10/11
    DATA for: First-time headgear
    DATA against: Poor recent finishing positions; Fell or unseated in 1 of its last 2 jumps runs
- Hillview Lass (hrs_17394782384) | 6yo M | 159lb | OR - | draw 0 | jockey  | trainer Donncha Duggan (14d 0/2) | headgear - | last run 16 days | form PP42-0 | MARKET 1.2% | 09:00 median 81.00 | Matchbook -
    DATA: model 2.0% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 1 Nov Cork (IRE) 16f Good To Yielding 10/19
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Mane Road (hrs_17395531258) | 6yo G | 166lb | OR - | draw 0 | jockey Ben Kennedy(4) | trainer J F O'Shea (14d 0/0) | headgear - | last run - days | form - | MARKET 1.2% | 09:00 median 101.00 | Matchbook -
    DATA: model 3.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Hazem (hrs_41304676) | 5yo G | 166lb | OR - | draw 0 | jockey Luke Carberry(4) | trainer A. McCann (14d 0/4) | headgear - | last run 17 days | form 07 | MARKET 0.6% | 09:00 median 151.00 | Matchbook -
    DATA: model 1.5% | style Held up (led 5% of runs) | runs in data 2 | last 3: 19 Sep Navan 15.8f Good 15/16; 31 Oct Down Royal (IRE) 17f Good 7/12
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Soldier Power (hrs_17394376657) | 4yo F | 159lb | OR - | draw 0 | jockey Kevin Healy(4) | trainer Mrs Y Dunleavy (14d 0/1) | headgear - | last run 5 days | form F8 | MARKET 0.6% | 09:00 median 201.00 | Matchbook -
    DATA: model 1.6% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 1 Nov Cork (IRE) 16f Good To Yielding F/19; 12 Nov Thurles (IRE) 20f Good 8/11
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Fell or unseated in 1 of its last 2 jumps runs

## 1:10 Limerick | race_id rac_32304690769 | Panoramic Restaurant @ Limerick Races Mares Handicap Hurdle
Hurdle |  | 2m | going Yielding | Turf | 10 runners | rating band - | age 3yo+
DATA pace: Lone leader - Jumbos Jet is the only habitual front-runner and may be allowed an easy lead.
- Cathryns Ruby (hrs_40786669) | 9yo M | 166lb | OR 108 | draw 0 | jockey Alan O'Sullivan(5) | trainer Patrick T Foley (14d 1/5) | headgear t | last run 23 days | form 4336-1 | MARKET 19.1% | 09:00 median 4.00 | Matchbook - | CHECK (skip line 3.80)
    comment: Cathryns Ruby arrives fresh from a win last time out, 23 days ago, and she has run over today's trip and on this going before.
    DATA: model 21.5% | style Prominent (led 3% of runs) | runs in data 5 | last 3: 21 Feb Fairyhouse 20.2f Heavy 3/16; 4 Mar Naas 18.8f Soft To Heavy 6/11; 25 Oct Wexford (IRE) 17f Soft 1/13 fig 106
    DATA for: Best recent form figure 106, 19 lb above field average; Official rating 108, 12 lb above field average; Trainer 20% wins (1/5), last 14 days; Has won at this trip or further; Good recent finishing positions
    DATA against: Carries 12 lb more than average
- Jumbos Jet (hrs_58347562) | 5yo M | 162lb | OR 104 | draw 0 | jockey Eoghan Finegan(5) | trainer W J Martin (14d 0/1) | headgear h | last run 23 days | form 632-14 | MARKET 18.3% | 09:00 median 4.37 | Matchbook -
    DATA: model 20.3% | style Leader (led 29% of runs) | runs in data 5 | last 3: 17 Mar Wexford 16f Soft 2/9; 14 May Clonmel 16.7f Good To Yielding 1/18; 25 Oct Wexford (IRE) 17f Soft 4/13 fig 96
    DATA for: Best recent form figure 96, 9 lb above field average; Official rating 104, 8 lb above field average; Has won at this trip or further; Good recent finishing positions; Pace: may get an uncontested lead
    DATA against: Recent figures 8 lb below its current mark (looks high in the weights); Carries 8 lb more than average
- Galileo Springs (hrs_412712069) | 6yo M | 160lb | OR 102 | draw 0 | jockey Conor Smithers(7) | trainer Martin Brassil (14d 0/3) | headgear t | last run 33 days | form 7213-F | MARKET 16.2% | 09:00 median 5.00 | Matchbook -
    comment: Galileo Springs makes plenty of appeal, with a win three starts back and a third two starts back, and she has run over today's trip and going before after 33 days off. The one risk is that she fell last time out, and she carries 160 lb.
    DATA: model 6.7% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 14 Aug Tramore 16.4f Good F/9; 21 Sep Listowel 12f Yielding 7/11; 15 Oct Curragh (IRE) 14f Yielding To Soft 4/21 fig 65
    DATA for: Official rating 102, 6 lb above field average
    DATA against: Best recent form figure 65, 22 lb below field average; Recent figures 37 lb below its current mark (looks high in the weights); Carries 6 lb more than average; Fell or unseated in 1 of its last 1 jumps runs
- Mercurial Sea (hrs_49609049) | 5yo M | 149lb | OR 91 | draw 0 | jockey Carl Millar(5) | trainer Nigel Thomas Slevin (14d 0/2) | headgear - | last run 60 days | form -28285 | MARKET 13.8% | 09:00 median 6.00 | Matchbook -
    comment: Winless in her last five and absent 60 days, Mercurial Sea is hard to fancy after a fifth last time out and an eighth before that, though a second three starts back and another five starts back show she can get involved.
    DATA: model 10.4% | style Midfield (led 3% of runs) | runs in data 7 | last 3: 14 Jul Downpatrick 17.8f Good 2/11; 14 Aug Tramore 21.8f Good 8/13; 18 Sep Downpatrick 17.8f Good 5/12
- Kate Knows Best (hrs_39469129) | 8yo M | 153lb | OR 95 | draw 0 | jockey Peter Smithers(5) | trainer John Patrick Ryan (14d 0/12) | headgear - | last run 10 days | form 8F-F55 | MARKET 9.1% | 09:00 median 8.50 | Matchbook -
    comment: The risk is a winless run in her last five, including two falls, and 153 lb is no small burden.
    DATA: model 7.0% | style Prominent (led 38% of runs) | runs in data 3 | last 3: 15 May Kilbeggan 20.4f Good F/14; 23 Oct Sligo (IRE) 17.5f Yielding 5/12 fig 94; 7 Nov Gowran Park (IRE) 20f Good To Yielding 5/14 fig 92
    DATA for: Best recent form figure 94, 7 lb above field average
    DATA against: Trainer 0 wins from 12 runs, last 14 days; Fell or unseated in 1 of its last 3 jumps runs
- Albatala (hrs_30138073) | 7yo M | 157lb | OR 99 | draw 0 | jockey Dylan Kidd(7) | trainer John McConnell (14d 1/14) | headgear tp (1st time) | last run 23 days | form 2P0/2U | MARKET 7.5% | 09:00 median 9.50 | Matchbook 14.00
    comment: Albatala unseated last time out but was second two starts back, and she is yet to win in her last five outings, with a pulled up four starts back adding to the doubts. She has run over today's trip and returns after 23 days, though 157 lb is a hefty burden.
    DATA: model 8.9% | style Prominent (led 4% of runs) | runs in data 5 | last 3: 12 Jul Sligo 17.4f Good 2/7; 7 Oct Navan 10.1f Yielding 7/16; 25 Oct Wexford (IRE) 17f Soft UR/13
    DATA for: First-time headgear
    DATA against: Fell or unseated in 1 of its last 2 jumps runs
- Shesakindofmagic (hrs_37790102) | 8yo M | 158lb | OR 100 | draw 0 | jockey James Smith(3) | trainer A. McCann (14d 0/4) | headgear t | last run 171 days | form 275-7P | MARKET 7.3% | 09:00 median 13.00 | Matchbook -
    comment: The risk is a 171-day absence under 158 lb.
    DATA: model 8.0% | style Prominent (led 3% of runs) | runs in data 5 | last 3: 4 Apr Fairyhouse 16f Yielding To Soft 5/16; 10 May Cork 19.2f Good 7/15; 30 May Listowel 23.5f Yielding PU/10
    DATA against: Returns from a 171-day break; Pulled up in 1 of its last 5 jumps runs
- Aleish Lass (hrs_34457010) | 7yo M | 151lb | OR 93 | draw 0 | jockey Mike O'Connor | trainer Michael Winters (14d 1/3) | headgear - | last run 12 days | form /05P-0 | MARKET 3.5% | 09:00 median 23.00 | Matchbook -
    comment: Aleish Lass has been out of sorts, unplaced last time out and pulled up two starts back, though a fifth three starts back shows some ability, and she has run on today's going before.
    DATA: model 6.3% | style Held up (led 4% of runs) | runs in data 3 | last 3: 19 Feb Thurles 21.6f Soft To Heavy 5/16; 12 Mar Limerick 22.8f Heavy PU/16; 5 Nov Clonmel (IRE) 17f Good To Yielding 12/15
    DATA against: Pulled up in 1 of its last 3 jumps runs; First run over hurdles in our data
- La Tulipe Noire (hrs_31480344) | 6yo M | 141lb | OR 83 | draw 0 | jockey Ethan O'Sullivan(7) | trainer Aengus King (14d 0/3) | headgear p | last run 5 days | form /P8-F0 | MARKET 3.1% | 09:00 median 29.00 | Matchbook -
    comment: Hard to fancy: La Tulipe Noire was unplaced last time, fell two starts back and was pulled up four starts back, and she is yet to win in her last four.
    DATA: model 8.9% | style Held up (led 3% of runs) | runs in data 12 | last 3: 20 Oct Curragh (IRE) 8f Yielding 4/23 fig 68; 29 Oct Punchestown (IRE) 7f Yielding 6/12 fig 55; 12 Nov Thurles (IRE) 16f Good 13/17 fig 74
    DATA for: Carries 13 lb less than average
    DATA against: Best recent form figure 74, 13 lb below field average; Recent figures 9 lb below its current mark (looks high in the weights); Official rating 83, 12 lb below field average; Fell or unseated in 1 of its last 2 jumps runs
- St Anthonys Corner (hrs_41598067) | 6yo M | 140lb | OR 80 | draw 0 | jockey Mr E M Nugent(7) | trainer Norman Lee (14d 0/0) | headgear b (1st time) | last run 44 days | form 900-P0 | MARKET 2.0% | 09:00 median 41.00 | Matchbook -
    comment: St Anthonys Corner is winless in her last five, unplaced last time and pulled up two starts back, so she is hard to fancy after 44 days off.
    DATA: model 2.2% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 11 Sep Ballinrobe 21.9f Good To Yielding PU/11; 4 Oct Killarney 17f Good 16/16
    DATA for: Carries 14 lb less than average; First-time headgear
    DATA against: Official rating 80, 16 lb below field average; Lightly raced: 2 runs in our data, so the model has little to go on; Pulled up in 1 of its last 2 jumps runs

## 1:40 Limerick | race_id rac_32304692706 | Follow Us On Instagram Handicap Hurdle
Hurdle |  | 2m | going Yielding | Turf | 10 runners | rating band 0-100 | age 3yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- The Monkey Pole (hrs_49974519) | 6yo G | 168lb | OR 99 | draw 0 | jockey Richard Condon(5) | trainer N Dooly (14d 0/3) | headgear - | last run 5 days | form 35545D | MARKET 29.7% | 09:00 median 2.50 | Matchbook -
    comment: Quick back-out after five days looks no concern for The Monkey Pole, who has run over today's trip and was a third six starts back, with three fifths and a fourth in between.
    DATA: model 20.4% | style Prominent (led 29% of runs) | runs in data 9 | last 3: 5 Oct Fairyhouse 24f Good 4/14; 1 Nov Cork (IRE) 16f Good To Yielding 5/21 fig 100; 12 Nov Thurles (IRE) 18f Good 2/10 fig 100
    DATA for: Best recent form figure 100, 12 lb above field average; Official rating 99, 12 lb above field average; Last-run finishing speed +3.0% vs that field (finished strongly)
    DATA against: Carries 14 lb more than average
- Theanniversary Man (hrs_35446369) | 7yo G | 154lb | OR 85 | draw 0 | jockey Eoghan Finegan(5) | trainer James M Barcoe (14d 0/4) | headgear - | last run 16 days | form -P4767 | MARKET 18.1% | 09:00 median 4.00 | Matchbook 4.90
    comment: Theanniversary Man has run over today's trip and on this going, and 16 days since his last run suggests he's fresh enough, but he's winless in his last five, finishing seventh last time out, and he shoulders 154 lb off an official mark of 85.
    DATA: model 13.9% | style Held up (led 3% of runs) | runs in data 5 | last 3: 10 Jul Cork 17.3f Good 7/23; 10 Aug Ballinrobe 16.5f Good 6/14; 1 Nov Cork (IRE) 16f Good To Yielding 7/21 fig 80
    DATA against: Best recent form figure 80, 8 lb below field average; Poor recent finishing positions; Pulled up in 1 of its last 5 jumps runs; Pace: steady gallop likely, hard to come from off the pace
- Frontier Rose (hrs_54644555) | 5yo M | 149lb | OR 80 | draw 0 | jockey Carl Millar(5) | trainer Thomas Coyle (14d 0/3) | headgear h | last run 10 days | form 665054 | MARKET 13.1% | 09:00 median 6.50 | Matchbook -
    comment: Frontier Rose is winless in her last six, finishing a fourth last time out after a run of fifth and sixth places, which makes her hard to fancy under 149 lb.
    DATA: model 12.8% | style Midfield (led 3% of runs) | runs in data 8 | last 3: 5 Oct Fairyhouse 16f Good 11/16; 22 Oct Clonmel (IRE) 17f Good To Yielding 5/16 fig 84; 7 Nov Gowran Park (IRE) 20f Good To Yielding 4/13 fig 76
    DATA for: Recent figures 4 lb above its current mark (looks well handicapped); Carries 5 lb less than average
    DATA against: Best recent form figure 84, 4 lb below field average; Official rating 80, 7 lb below field average
- Dunmore (hrs_64555071) | 3yo G | 143lb | OR 90 | draw 0 | jockey Alan O'Sullivan(5) | trainer Anthony Mullins (14d 0/3) | headgear - | last run 22 days | form 767 | MARKET 8.7% | 09:00 median 10.00 | Matchbook -
    comment: Dunmore is hard to fancy, having finished seventh last time out, a sixth two starts back and a seventh three starts back, so he is winless in his last three.
    DATA: model 2.8% | style Prominent (led 29% of runs) | runs in data 4 | last 3: 20 Sep Listowel 16f Good 7/11; 13 Oct Punchestown 16.2f Good 6/9; 26 Oct Galway (IRE) 16.5f Soft To Heavy 7/10
    DATA for: Carries 11 lb less than average
    DATA against: Poor recent finishing positions
- Makaiah (hrs_42073787) | 5yo M | 168lb | OR 99 | draw 0 | jockey Thomas O'Connor(7) | trainer G. O'Leary (14d 1/6) | headgear - | last run 82 days | form 0429/ | MARKET 8.6% | 09:00 median 9.45 | Matchbook -
    comment: The main risk is a ninth last time out and an 82-day absence, with 168 lb to carry.
    DATA: model 12.0% | style Prominent (led 23% of runs) | runs in data 4 | last 3: 22 Jun Ballinrobe 13f Yielding 11/13; 6 Aug Leopardstown 15f Good 7/9; 27 Aug Navan 14f Good 17/22
    DATA for: Official rating 99, 12 lb above field average
    DATA against: Poor recent finishing positions; Carries 14 lb more than average; First run over hurdles in our data
- Nothing Da Now (hrs_47620902) | 6yo M | 149lb | OR 80 | draw 0 | jockey Shane O'Callaghan(3) | trainer Maike Magnussen (14d 0/4) | headgear p | last run 2 days | form P7-7PP | MARKET 7.7% | 09:00 median 11.00 | Matchbook 8.00
    comment: Hard to fancy: Nothing Da Now has been pulled up in three of her last five, including last time out just two days ago, and is yet to win in that spell.
    DATA: model 8.8% | style Held up (led 4% of runs) | runs in data 4 | last 3: 6 Aug Sligo 17.9f Good 7/16; 28 Aug Wexford 20.5f Yielding PU/14; 15 Nov Navan (IRE) 16f Good To Yielding PU/25
    DATA for: Carries 5 lb less than average
    DATA against: Official rating 80, 7 lb below field average; Poor recent finishing positions; Pulled up in 2 of its last 4 jumps runs; Pace: steady gallop likely, hard to come from off the pace
- Get It Right (hrs_29931657) | 8yo G | 156lb | OR 87 | draw 0 | jockey Anna McGuinness(7) | trainer Sean Aherne (14d 0/1) | headgear p | last run 423 days | form /1P00- | MARKET 4.2% | 09:00 median 21.00 | Matchbook -
    comment: The one concern is a 423-day layoff, with two unplaced runs and a pulled up since that win, under 156 lb.
    DATA: model 7.2% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 423-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Maciver (hrs_24569188) | 9yo G | 162lb | OR 93 | draw 0 | jockey John Aherne(7) | trainer A M O'Grady (14d 0/0) | headgear - | last run 212 days | form 2P250- | MARKET 4.0% | 09:00 median 23.00 | Matchbook -
    comment: The big risk is a 212-day absence, with 162 lb on his back and an unplaced run last time out.
    DATA: model 14.8% | style Prominent (led 5% of runs) | runs in data 3 | last 3: 1 Jan Tramore 21.5f Soft 2/15; 19 Mar Cork 24.2f Yielding 5/11; 19 Apr Tramore 20.5f Yielding 10/16
    DATA for: Official rating 93, 6 lb above field average
    DATA against: Carries 8 lb more than average; Returns from a 212-day break; Aged 9, older than most of this field
- Devine Genius (hrs_40918668) | 4yo G | 153lb | OR 84 | draw 0 | jockey John Shinnick | trainer J Morrison (14d 0/2) | headgear - | last run 10 days | form P006 | MARKET 3.2% | 09:00 median 29.00 | Matchbook -
    comment: Lightly raced and unexposed, Devine Genius showed a bit more when sixth last time out, 10 days ago, after unplaced efforts in his previous two and a pulled up four starts back. He is yet to win in recent form and carries 153 lb, so any improvement would need to come quickly.
    DATA: model 1.7% | style Held up (led 3% of runs) | runs in data 7 | last 3: 13 Aug Tramore 16f Good 10/12; 26 Sep Listowel 16f Good 12/12; 7 Nov Gowran Park (IRE) 16f Good To Yielding 6/12
    DATA against: Poor recent finishing positions; Race comments mention jumping mistakes in 2 of its last 4 runs; Pulled up in 1 of its last 4 jumps runs; Pace: steady gallop likely, hard to come from off the pace
- Boston Bongo (hrs_35528640) | 7yo G | 141lb | OR 72 | draw 0 | jockey Harry Sexton(7) | trainer E Sheehy (14d 0/2) | headgear b | last run 321 days | form 959P0- | MARKET 2.8% | 09:00 median 34.00 | Matchbook -
    comment: Boston Bongo has been out of sorts, unplaced last time and pulled up two starts back, and returns after 321 days off, though he has run over today's trip and going.
    DATA: model 5.6% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Carries 13 lb less than average
    DATA against: Official rating 72, 15 lb below field average; Returns from a 321-day break; Lightly raced: 0 runs in our data, so the model has little to go on

## 2:10 Limerick | race_id rac_32304985193 | Mr Binman Christmas Racing Festival 26th - 29th December Handicap Hurdle (Div I)
Hurdle |  | 2m5f | going Yielding | Turf | 17 runners | rating band 0-100 | age 3yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- The Cobblers Wife (hrs_52897285) | 8yo M | 155lb | OR 85 | draw 0 | jockey Alan O'Sullivan(5) | trainer Anthony Mullins (14d 0/3) | headgear - | last run 13 days | form 4-P142 | MARKET 16.7% | 09:00 median 3.75 | Matchbook - | CHECK (skip line 3.56)
    comment: The Cobblers Wife was second last time out, 13 days ago, and has a win three starts back, with experience of today's trip and going.
    DATA: model 12.7% | style Midfield (led 3% of runs) | runs in data 9 | last 3: 13 Aug Tramore 20.5f Good 1/16; 31 Aug Downpatrick 19.5f Good 4/15; 4 Nov Wexford (IRE) 20f Yielding 2/13 fig 81
    DATA for: Last-run finishing speed +6.1% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Race comments mention jumping mistakes in 2 of its last 5 runs; Pulled up in 1 of its last 5 jumps runs
- Talas Kera (hrs_55061601) | 5yo M | 162lb | OR 92 | draw 0 | jockey Eoghan Finegan(5) | trainer John G Carr (14d 1/3) | headgear - | last run 10 days | form 540421 | MARKET 11.2% | 09:00 median 5.50 | Matchbook -
    comment: Talas Kera arrives in good heart, a winner last time out and second two starts back, just 10 days ago, and she has run over today's trip and going before.
    DATA: model 16.0% | style Midfield (led 3% of runs) | runs in data 9 | last 3: 13 Aug Tramore 20.5f Good 4/16; 2 Oct Gowran Park 20.2f Good 2/13; 7 Nov Gowran Park (IRE) 20f Good To Yielding 1/13 fig 87
    DATA for: Good recent finishing positions
    DATA against: Race comments mention jumping mistakes in 2 of its last 5 runs
- Ardera Gun (hrs_40514544) | 6yo G | 157lb | OR 87 | draw 0 | jockey Kieren Buckley | trainer Eoin Doyle (14d 0/2) | headgear tb | last run 13 days | form P-U324 | MARKET 10.4% | 09:00 median 7.50 | Matchbook -
    comment: Ardera Gun comes here in solid recent form, fourth last time out, a second two starts back and a third three starts back, and he's fresh from a run just 13 days ago. He has run over today's trip and going before, though 157 lb is a hefty burden for an official mark of 87.
    DATA: model 10.2% | style Midfield (led 3% of runs) | runs in data 7 | last 3: 2 Oct Gowran Park 20.2f Good 3/13; 17 Oct Limerick (IRE) 21.5f Good To Yielding 2/18 fig 86; 4 Nov Wexford (IRE) 20f Yielding 4/13 fig 84
    DATA for: Last-run finishing speed +4.3% vs that field (finished strongly); Good recent finishing positions
    DATA against: Fell or unseated in 1 of its last 5 jumps runs; Pulled up in 1 of its last 5 jumps runs
- Agent Tequila (hrs_34166587) | 8yo G | 158lb | OR 88 | draw 0 | jockey Mike O'Connor | trainer John McConnell (14d 1/14) | headgear tp | last run 13 days | form 90P-01 | MARKET 7.8% | 09:00 median 8.50 | Matchbook -
    comment: Fresh from a win last time out just 13 days ago, Agent Tequila has the momentum and has run over today's trip and going before, but a pulled up and an unplaced effort in the three runs before that show his consistency is a worry, and 158 lb is a hefty burden.
    DATA: model 7.3% | style Held up (led 4% of runs) | runs in data 3 | last 3: 17 Mar Wexford 19.5f Soft PU/16; 7 Sep Galway 22.4f Yielding 10/19; 4 Nov Wexford (IRE) 20f Yielding 1/13 fig 82
    DATA for: Last-run finishing speed +5.3% vs that field (finished strongly)
    DATA against: Recent figures 6 lb below its current mark (looks high in the weights); Pulled up in 1 of its last 3 jumps runs; Pace: steady gallop likely, hard to come from off the pace
- Good Bye Milan (hrs_25810771) | 9yo M | 156lb | OR 86 | draw 0 | jockey Kevin Healy(7) | trainer Gillian Scott (14d 2/3) | headgear tp | last run 10 days | form 30-001 | MARKET 7.3% | 09:00 median 9.00 | Matchbook -
    comment: Won last time out and is only ten days fresh, but she was unplaced in the three runs before that, and she carries 156 lb.
    DATA: model 6.0% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 11 Oct Cork 18.9f Good 11/14; 22 Oct Clonmel (IRE) 17f Good To Yielding 13/16 fig 65; 7 Nov Gowran Park (IRE) 20f Good To Yielding 1/14 fig 87
- Mellem (hrs_45598483) | 7yo G | 156lb | OR 86 | draw 0 | jockey Thomas O'Connor(7) | trainer Mark Fahey (14d 0/8) | headgear tb | last run 8 days | form 740-75 | MARKET 6.8% | 09:00 median 9.25 | Matchbook -
    comment: Mellem is winless in his last five, though a fifth last time out and just eight days since that run keep him sharp, and he has experience of today's trip and going.
    DATA: model 6.4% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 13 Oct Punchestown 20f Good 7/15; 9 Nov Punchestown (IRE) 20.5f Good To Yielding 5/22 fig 86
    DATA for: Last-run finishing speed +3.5% vs that field (finished strongly)
    DATA against: Trainer 0 wins from 8 runs, last 14 days; Lightly raced: 2 runs in our data, so the model has little to go on
- Solar Generation (hrs_58565444) | 5yo G | 161lb | OR 91 | draw 0 | jockey Ricky Doyle | trainer Mark Michael McNiff (14d 0/1) | headgear t | last run 25 days | form 00-5P7 | MARKET 6.0% | 09:00 median 11.00 | Matchbook -
    comment: He has run on today's going and returns after 25 days, but 161 lb is a big burden.
    DATA: model 5.2% | style Held up (led 3% of runs) | runs in data 4 | last 3: 15 May Kilbeggan 15.7f Good 5/14; 21 Aug Kilbeggan 18.9f Good To Yielding PU/15; 23 Oct Sligo (IRE) 17.5f Yielding 7/12 fig 80
    DATA against: Best recent form figure 80, 4 lb below field average; Recent figures 11 lb below its current mark (looks high in the weights); Pulled up in 1 of its last 4 jumps runs; Pace: steady gallop likely, hard to come from off the pace
- Zolpharine (hrs_34253730) | 8yo G | 155lb | OR 85 | draw 0 | jockey Peter Smithers(5) | trainer John Patrick Ryan (14d 0/12) | headgear - | last run 12 days | form 0057P2 | MARKET 6.0% | 09:00 median 11.00 | Matchbook -
    comment: Zolpharine is hard to fancy after a pulled up two starts back and a run of unplaced efforts, yet he arrives fresh from a second last time out just 12 days ago.
    DATA: model 4.5% | style Midfield (led 4% of runs) | runs in data 13 | last 3: 4 Oct Killarney 23.5f Good To Yielding 7/15; 22 Oct Clonmel (IRE) 21f Good PU/15; 5 Nov Clonmel (IRE) 17f Good To Yielding 2/15 fig 85
    DATA for: Has won at this trip or further
    DATA against: Trainer 0 wins from 12 runs, last 14 days; Race comments mention jumping mistakes in 2 of its last 5 runs; Pulled up in 1 of its last 5 jumps runs
- Johnny Cakes (hrs_36970332) | 7yo G | 155lb | OR 85 | draw 0 | jockey Shane O'Callaghan(3) | trainer P. J. Rothwell (14d 0/24) | headgear p | last run 25 days | form 4355-4 | MARKET 5.9% | 09:00 median 13.00 | Matchbook -
    comment: Winless in his last five, Johnny Cakes was fourth last time out and fifth in each of the two runs before, so he keeps finishing in the pack without getting his head in front.
    DATA: model 6.2% | style Held up (led 3% of runs) | runs in data 4 | last 3: 17 Jan Navan 20.2f Soft To Heavy 5/10; 4 Mar Naas 23.8f Soft To Heavy 5/12; 23 Oct Sligo (IRE) 25.5f Yielding To Soft 4/9 fig 83
    DATA against: Trainer 0 wins from 24 runs, last 14 days; Pace: steady gallop likely, hard to come from off the pace
- Calzaghi (hrs_36095465) | 6yo G | 165lb | OR 95 | draw 0 | jockey Gearoid Brouder(5) | trainer E McNamara (14d 0/6) | headgear p (1st time) | last run 31 days | form 980999 | MARKET 4.9% | 09:00 median 17.00 | Matchbook -
    comment: The risk is obvious: a string of modest finishes and 165 lb on his back.
    DATA: model 5.0% | style Held up (led 3% of runs) | runs in data 6 | last 3: 3 Aug Cork 18f Good 9/18; 1 Oct Clonmel 22.8f Good 9/15; 17 Oct Limerick (IRE) 21.5f Good To Yielding 9/18 fig 86
    DATA for: Official rating 95, 8 lb above field average; First-time headgear
    DATA against: Recent figures 9 lb below its current mark (looks high in the weights); Poor recent finishing positions; Carries 8 lb more than average; Race comments mention jumping mistakes in 2 of its last 5 runs; Pace: steady gallop likely, hard to come from off the pace
- Lily Milan (hrs_48289829) | 7yo M | 156lb | OR 86 | draw 0 | jockey  | trainer Paul Stephen Kiely (14d 0/0) | headgear p (1st time) | last run 30 days | form 586-93 | MARKET 3.8% | 09:00 median 19.00 | Matchbook -
    comment: Lily Milan comes into this off a third last time out, her best finish in a run of modest efforts, and she has run on today's going before; yet to win in her last five starts, she carries 156 lb off an official mark of 86, which may cap her chance here.
    DATA: model 3.6% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 19 Mar Cork 16f Yielding 8/13; 5 Apr Cork 19f Yielding 6/14; 27 May Wexford 24f Good To Yielding 9/14
    DATA for: First-time headgear
    DATA against: Poor recent finishing positions
- Jacenry (hrs_34652751) | 7yo G | 159lb | OR 89 | draw 0 | jockey  | trainer William Harvey (14d 0/0) | headgear - | last run 751 days | form 127FP/ | MARKET 3.0% | 09:00 median 23.00 | Matchbook -
    comment: Jacenry has run over today's trip and going, and won five starts back, but he was pulled up last time out after a fall before that, and a 751-day absence raises fitness doubts.
    DATA: model 4.2% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 751-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Ballinaboola Hanna (hrs_59928092) | 5yo M | 153lb | OR 83 | draw 0 | jockey Richard Deegan | trainer R Donohoe (14d 0/3) | headgear - | last run 117 days | form 5F69-0 | MARKET 2.4% | 09:00 median 34.00 | Matchbook -
    comment: Ballinaboola Hanna is yet to win in her last five starts, with a fifth five starts back her best finish, and she returns after 117 days off carrying 153 lb. The form is modest, but she looks unexposed and could improve now.
    DATA: model 2.4% | style Midfield (led 3% of runs) | runs in data 6 | last 3: 26 Mar Clonmel 16f Soft 6/16; 14 Apr Clonmel 19.8f Yielding 9/17; 23 Jul Wexford 24f Good 12/13
    DATA against: Last-run finishing speed -15.6% vs that field (faded); Poor recent finishing positions; Returns from a 117-day break; Race comments mention jumping mistakes in 3 of its last 5 runs; Fell or unseated in 1 of its last 5 jumps runs
- Renard De Noir (hrs_38002384) | 8yo G | 145lb | OR 75 | draw 0 | jockey  | trainer Ms Helen P Markham (14d 0/3) | headgear - | last run 767 days | form 40009/ | MARKET 2.0% | 09:00 median 41.00 | Matchbook -
    comment: The risk is plain: he is unplaced in four of his last five, a ninth last time out, and returns after 767 days off.
    DATA: model 3.3% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Carries 12 lb less than average
    DATA against: Official rating 75, 12 lb below field average; Returns from a 767-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Free A Minute (hrs_41597150) | 7yo M | 152lb | OR 82 | draw 0 | jockey Conor Smithers(7) | trainer Charlie Keegan (14d 0/0) | headgear - | last run 35 days | form P40077 | MARKET 2.0% | 09:00 median 41.00 | Matchbook -
    comment: Winless in her last six, Free A Minute has finished seventh in each of her last two and was pulled up six starts back, so she is hard to fancy.
    DATA: model 1.0% | style Midfield (led 4% of runs) | runs in data 5 | last 3: 3 Aug Cork 18f Good 13/17; 24 Aug Ballinrobe 22.3f Good 7/12; 13 Oct Punchestown 20f Good 7/13
    DATA for: Carries 5 lb less than average
    DATA against: Official rating 82, 5 lb below field average; Poor recent finishing positions
- Seeitoldya (hrs_50402450) | 5yo G | 166lb | OR 96 | draw 0 | jockey Harry Sexton(7) | trainer John Joseph Hanlon (14d 0/11) | headgear - | last run 59 days | form 0-6P80 | MARKET 2.0% | 09:00 median 41.00 | Matchbook -
    DATA: model 3.4% | style Midfield (led 4% of runs) | runs in data 6 | last 3: 24 Jul Uttoxeter 23.3f Good PU/16; 20 Aug Killarney 20.8f Good 8/11; 19 Sep Navan 21f Good 12/15
    DATA for: Official rating 96, 9 lb above field average
    DATA against: Trainer 0 wins from 11 runs, last 14 days; Poor recent finishing positions; Carries 9 lb more than average; Race comments mention jumping mistakes in 2 of its last 5 runs; Pulled up in 1 of its last 5 jumps runs
- Fenian Maxios (hrs_61307211) | 5yo G | 160lb | OR 90 | draw 0 | jockey E Walsh | trainer Michael Winters (14d 1/3) | headgear - | last run 30 days | form 208-PP | MARKET 1.9% | 09:00 median 41.00 | Matchbook -
    comment: Fenian Maxios has been pulled up in his last two outings, and an eighth three starts back leaves him winless in his last five, though a second five starts back shows he has a bit of ability.
    DATA: model 2.6% | style Held up (led 4% of runs) | runs in data 7 | last 3: 16 Apr Limerick 19.3f Soft To Heavy 8/13; 8 Oct Tramore 16f Yielding PU/9; 18 Oct Limerick (IRE) 19.5f Good To Yielding PU/14
    DATA against: Poor recent finishing positions; Pulled up in 2 of its last 5 jumps runs; Pace: steady gallop likely, hard to come from off the pace

## 2:40 Limerick | race_id rac_32304694643 | Mr Binman Christmas Racing Festival 26th - 29th December Handicap Hurdle (Div II)
Hurdle |  | 2m5f | going Yielding | Turf | 17 runners | rating band 0-100 | age 3yo+
DATA pace: Even - Two likely leaders (Cahirdown Boy, Depalma). A fair, even gallop is most likely.
- Jonzac (hrs_40553555) | 6yo G | 151lb | OR 81 | draw 0 | jockey Kevin Healy(7) | trainer Gordon Elliott (14d 12/73) | headgear - | last run 257 days | form 1P09P- | MARKET 15.3% | 09:00 median 3.75 | Matchbook - | CHECK (skip line 3.56)
    comment: Lightly raced and unexposed, Jonzac returns after 257 days off, having won five starts back but since pulled up, was unplaced, finished ninth and pulled up again last time. He carries 151 lb off an official mark of 81, and a fresh start could bring improvement.
    DATA: model 1.1% | style Held up (led 3% of runs) | runs in data 4 | last 3: 3 Feb Carlisle 17f Good To Soft 11/12; 21 Feb Newcastle 16.9f Good To Soft 9/12; 5 Mar Haydock 21.2f Good To Soft PU/8
    DATA for: Carries 7 lb less than average
    DATA against: Official rating 81, 7 lb below field average; Poor recent finishing positions; Returns from a 257-day break; Pulled up in 2 of its last 4 jumps runs
- Kayla's Friend (hrs_50667400) | 6yo M | 166lb | OR 96 | draw 0 | jockey Mike O'Connor | trainer James William Hannon (14d 0/0) | headgear t | last run 14 days | form 651862 | MARKET 10.1% | 09:00 median 6.00 | Matchbook -
    comment: Kayla's Friend bounced back to form with a second last time out, just 14 days ago, but she is a winner four starts back and otherwise a sixth and an eighth in the other recent runs.
    DATA: model 3.9% | style Held up (led 5% of runs) | runs in data 7 | last 3: 15 Jul Uttoxeter 23.3f Good 8/10; 8 Oct Tramore 20.3f Yielding 6/7; 3 Nov Fairyhouse (IRE) 20f Good To Yielding 2/15 fig 96
    DATA for: Best recent form figure 96, 5 lb above field average; Official rating 96, 8 lb above field average; Last-run finishing speed +3.8% vs that field (finished strongly)
    DATA against: Carries 8 lb more than average
- Cahirdown Boy (hrs_18645599) | 11yo G | 164lb | OR 94 | draw 0 | jockey Gearoid Brouder(5) | trainer E McNamara (14d 0/6) | headgear t | last run 7 days | form -FU354 | MARKET 8.8% | 09:00 median 7.50 | Matchbook -
    comment: Quick back-up after seven days and consistent of late, with a fourth last time out, a fifth before that and a third three starts back, while he has run over today's trip and on this going.
    DATA: model 10.0% | style Leader (led 43% of runs) | runs in data 7 | last 3: 4 Oct Killarney 17f Good To Yielding 3/10; 17 Oct Limerick (IRE) 21.5f Good To Yielding 5/18 fig 90; 10 Nov Fairyhouse (IRE) 20.5f Good To Yielding 4/11 fig 96
    DATA for: Best recent form figure 96, 5 lb above field average; Official rating 94, 6 lb above field average
    DATA against: Carries 6 lb more than average; Fell or unseated in 2 of its last 5 jumps runs; Aged 11, older than most of this field
- Whiskey Serenade (hrs_47620909) | 6yo M | 156lb | OR 86 | draw 0 | jockey Carl Millar(5) | trainer Thomas Coyle (14d 0/3) | headgear - | last run 43 days | form 627669 | MARKET 7.3% | 09:00 median 9.50 | Matchbook -
    comment: Whiskey Serenade is winless in her last six, with a ninth last time out and a sixth two starts back, so she is hard to fancy after 43 days off and under 156 lb. In her favour, she has run over today's trip and going, and a second five starts back shows she can still go close.
    DATA: model 6.9% | style Midfield (led 3% of runs) | runs in data 8 | last 3: 6 Aug Sligo 20.8f Good 6/8; 26 Aug Bellewstown 20.5f Good 6/16; 5 Oct Fairyhouse 24f Good 9/14
    DATA against: Poor recent finishing positions
- Bridge View Star (hrs_56590926) | 6yo G | 164lb | OR 94 | draw 0 | jockey Eoghan Finegan(5) | trainer W J O'Doherty (14d 0/1) | headgear - | last run 16 days | form 646-U0 | MARKET 7.1% | 09:00 median 9.25 | Matchbook -
    comment: Bridge View Star has been unplaced last time out and unseated two runs back, though a fourth four starts back shows some ability, and he's back quickly after 16 days.
    DATA: model 5.6% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 7 Sep Galway 16.7f Yielding UR/20; 1 Nov Cork (IRE) 16f Good To Yielding 12/21 fig 83
    DATA for: Official rating 94, 6 lb above field average
    DATA against: Best recent form figure 83, 8 lb below field average; Recent figures 11 lb below its current mark (looks high in the weights); Carries 6 lb more than average; Lightly raced: 2 runs in our data, so the model has little to go on; Fell or unseated in 1 of its last 2 jumps runs
- No Big Deal (hrs_34002983) | 6yo G | 164lb | OR 94 | draw 0 | jockey Gavin Brouder | trainer Charles O'Brien (14d 0/0) | headgear t | last run 35 days | form 98-849 | MARKET 6.8% | 09:00 median 10.00 | Matchbook -
    DATA: model 13.6% | style Prominent (led 3% of runs) | runs in data 5 | last 3: 19 Sep Navan 19f Good 8/16; 2 Oct Gowran Park 20.2f Good 4/20; 13 Oct Punchestown 20f Good 9/17
    DATA for: Official rating 94, 6 lb above field average
    DATA against: Carries 6 lb more than average
- Lord De Choisel (hrs_61911479) | 5yo G | 157lb | OR 87 | draw 0 | jockey Kieren Buckley | trainer Eoin Doyle (14d 0/2) | headgear tp (1st time) | last run 18 days | form 57-860 | MARKET 5.7% | 09:00 median 13.00 | Matchbook -
    comment: Lord De Choisel is hard to fancy, unplaced last time and beaten in all five recent runs, with a sixth, an eighth, a seventh and a fifth before that.
    DATA: model 7.7% | style Held up (led 3% of runs) | runs in data 6 | last 3: 16 Jul Killarney 20.4f Good 8/15; 17 Oct Limerick (IRE) 21.5f Good To Yielding 6/16 fig 86; 30 Oct Down Royal (IRE) 24.5f Good To Yielding 12/20 fig 81
    DATA for: First-time headgear
    DATA against: Best recent form figure 86, 5 lb below field average; Poor recent finishing positions; Race comments mention jumping mistakes in 2 of its last 5 runs
- Mydreamtell (hrs_64779820) | 4yo G | 163lb | OR 94 | draw 0 | jockey Conor Smithers(7) | trainer James Andrew Fahey (14d 0/4) | headgear - | last run 75 days | form 685 | MARKET 5.2% | 09:00 median 12.00 | Matchbook -
    comment: Mydreamtell is winless in his last three, finishing fifth last time out, then an eighth and a sixth, and returns after 75 days off.
    DATA: model 4.8% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 26 May Ballinrobe 16.1f Good 6/15; 14 Jun Downpatrick 18.8f Good 8/14; 3 Sep Kilbeggan 16f Good To Yielding 5/14
    DATA for: Official rating 94, 6 lb above field average; Last-run finishing speed +2.1% vs that field (finished strongly)
    DATA against: Carries 5 lb more than average
- Portetta (hrs_41033804) | 5yo M | 156lb | OR 86 | draw 0 | jockey Harry Sexton(7) | trainer John Joseph Hanlon (14d 0/11) | headgear - | last run 13 days | form 06906U | MARKET 4.7% | 09:00 median 15.00 | Matchbook -
    comment: Portetta unseated last time out and has been without a win in her last six starts, with a sixth two starts back her best recent finish.
    DATA: model 4.7% | style Held up (led 3% of runs) | runs in data 6 | last 3: 1 Oct Clonmel 19.7f Good 12/16; 13 Oct Punchestown 20f Good 6/15; 4 Nov Wexford (IRE) 20f Yielding UR/13
    DATA against: Trainer 0 wins from 11 runs, last 14 days; Poor recent finishing positions; Fell or unseated in 1 of its last 5 jumps runs
- Finnicky Filly (hrs_39978204) | 8yo M | 142lb | OR 72 | draw 0 | jockey Peter Smithers(5) | trainer John Patrick Ryan (14d 0/12) | headgear - | last run 26 days | form 505067 | MARKET 4.7% | 09:00 median 15.00 | Matchbook -
    comment: Finnicky Filly is hard to fancy, winless in her last six with a seventh last time out and a sixth two starts back, and she carries a hefty 142 lb. On the plus side, she has run over today's trip and going, and returns after 26 days.
    DATA: model 4.7% | style Held up (led 4% of runs) | runs in data 17 | last 3: 1 Oct Clonmel 22.8f Good 14/15; 11 Oct Cork 18.9f Good 6/14; 22 Oct Clonmel (IRE) 21f Good 7/15
    DATA for: Carries 16 lb less than average
    DATA against: Official rating 72, 16 lb below field average; Trainer 0 wins from 12 runs, last 14 days; Poor recent finishing positions
- Wildhorserider (hrs_48289668) | 6yo G | 162lb | OR 92 | draw 0 | jockey John Shinnick | trainer Terence O'Brien (14d 1/4) | headgear - | last run 22 days | form /006-P | MARKET 4.6% | 09:00 median 17.00 | Matchbook -
    comment: Wildhorserider was pulled up last time out and has been winless in his last four, with a sixth two starts back his best recent effort, though 22 days since that run keeps him fresh.
    DATA: model 5.5% | style Held up (led 3% of runs) | runs in data 4 | last 3: 19 Mar Cork 20f Yielding 14/21; 2 Apr Clonmel 19.5f Soft 6/12; 26 Oct Galway (IRE) 24f Heavy PU/19
    DATA against: Poor recent finishing positions; Pulled up in 1 of its last 4 jumps runs
- Glory Sky (hrs_28535836) | 6yo M | 144lb | OR 74 | draw 0 | jockey Alan O'Sullivan(5) | trainer Ray Hackett (14d 0/4) | headgear p | last run 10 days | form 778-5P | MARKET 4.2% | 09:00 median 17.00 | Matchbook -
    comment: Glory Sky is hard to fancy, pulled up last time out and winless in her last five, with a fifth two starts back her best finish in that spell. She has run over today's trip and is back quickly after ten days, but 144 lb is a big ask.
    DATA: model 4.8% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 29 Jan Thurles 20f Heavy 8/16; 18 Sep Downpatrick 17.8f Good 5/12; 7 Nov Gowran Park (IRE) 20f Good To Yielding PU/14
    DATA for: Carries 14 lb less than average
    DATA against: Official rating 74, 14 lb below field average; Pulled up in 1 of its last 3 jumps runs
- Quirt Evans (hrs_18240509) | 11yo G | 163lb | OR 93 | draw 0 | jockey  | trainer Mark Fahey (14d 0/8) | headgear - | last run 60 days | form 0090/8 | MARKET 3.8% | 09:00 median 18.75 | Matchbook -
    comment: A 60-day break and 163 lb are the reservations.
    DATA: model 6.6% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 18 Sep Downpatrick 17.8f Good 8/12
    DATA for: Official rating 93, 5 lb above field average
    DATA against: Trainer 0 wins from 8 runs, last 14 days; Last-run finishing speed -3.7% vs that field (faded); Carries 5 lb more than average; Lightly raced: 1 run in our data, so the model has little to go on; Aged 11, older than most of this field
- Depalma (hrs_38433507) | 7yo G | 168lb | OR 98 | draw 0 | jockey  | trainer M K Flannery (14d 0/0) | headgear - | last run 31 days | form 232123 | MARKET 3.6% | 09:00 median 21.00 | Matchbook -
    comment: Depalma has finished in the first three in each of his last six starts, including a third last time out, a second two starts back and a win three starts back, and he has run over today's trip and on the going.
    DATA: model 10.1% | style Prominent (led 43% of runs) | runs in data 4 | last 3: 18 Sep Newton Abbot 21.6f Good 1/7; 28 Sep Newton Abbot 25.8f Good 2/3; 17 Oct Stratford 22.5f Good 3/4 fig 96
    DATA for: Best recent form figure 96, 5 lb above field average; Official rating 98, 10 lb above field average; Has won at this trip or further; Good recent finishing positions
    DATA against: Carries 10 lb more than average
- Kalsman (hrs_30541336) | 8yo G | 165lb | OR 95 | draw 0 | jockey Caragh Monaghan(7) | trainer Liam Lennon (14d 0/2) | headgear - | last run 8 days | form 24P480 | MARKET 3.1% | 09:00 median 24.50 | Matchbook -
    comment: Kalsman is winless in his last six, with an eighth two starts back and a fourth three starts back, though he's back quickly after eight days and has run over today's trip.
    DATA: model 5.9% | style Midfield (led 3% of runs) | runs in data 12 | last 3: 9 Oct Downpatrick 19.5f Good 4/8; 30 Oct Down Royal (IRE) 16.5f Good To Yielding 8/9 fig 83; 9 Nov Punchestown (IRE) 20.5f Good To Yielding 12/22 fig 89
    DATA for: Official rating 95, 7 lb above field average
    DATA against: Recent figures 6 lb below its current mark (looks high in the weights); Carries 7 lb more than average; Race comments mention jumping mistakes in 2 of its last 5 runs; Pulled up in 1 of its last 5 jumps runs
- Sum Story (hrs_59186435) | 5yo G | 155lb | OR 85 | draw 0 | jockey Shane O'Callaghan(3) | trainer P. J. Rothwell (14d 0/24) | headgear - | last run 47 days | form 5-0000 | MARKET 2.6% | 09:00 median 34.00 | Matchbook -
    comment: Unplaced in his last four runs, with a fifth five starts back the best of his recent form, and 47 days off the track, Sum Story is yet to win in that spell.
    DATA: model 1.6% | style Midfield (led 29% of runs) | runs in data 4 | last 3: 7 Aug Wexford 16.8f Good 11/14; 26 Aug Bellewstown 20.5f Good 11/14; 1 Oct Clonmel 19.7f Good 14/16
    DATA against: Trainer 0 wins from 24 runs, last 14 days; Poor recent finishing positions
- Imbolc (hrs_33274969) | 8yo G | 142lb | OR 72 | draw 0 | jockey  | trainer E Sheehy (14d 0/2) | headgear b | last run 22 days | form PF00-P | MARKET 2.3% | 09:00 median 34.00 | Matchbook -
    comment: Imbolc is hard to fancy, pulled up last time out and without a win in his last five starts, with a fall and another pulled up also in that run.
    DATA: model 2.7% | style Midfield (led 29% of runs) | runs in data 3 | last 3: 19 Mar Cork 17.1f Yielding 18/22; 12 Apr Down Royal 24f Good 12/19; 26 Oct Galway (IRE) 24f Heavy PU/19
    DATA for: Carries 16 lb less than average
    DATA against: Official rating 72, 16 lb below field average; Poor recent finishing positions; Pulled up in 1 of its last 3 jumps runs

## 3:15 Limerick | race_id rac_32304696580 | Follow Us On Facebook @ Limerick Races Handicap Hurdle
Hurdle |  | 3m155y | going Yielding | Turf | 17 runners | rating band 0-100 | age 4yo+
DATA pace: Even - Two likely leaders (Shotgun Jack, Chanceitlucky). A fair, even gallop is most likely.
- Cock And Bull (hrs_36878835) | 5yo G | 168lb | OR 99 | draw 0 | jockey  | trainer Emmet Mullins (14d 2/5) | headgear t | last run 38 days | form 8570- | MARKET 17.4% | 09:00 median 2.75 | Matchbook -
    comment: Cock And Bull is winless in his last four, with a seventh two starts back and a fifth three starts back his best recent efforts, though he was unplaced last time out.
    DATA: model 9.1% | style Prominent (led 3% of runs) | runs in data 7 | last 3: 26 Jun Curragh 16.3f Good 3/11; 29 Jul Galway 16.5f Yielding 1/19; 10 Oct Newmarket 18f Good 20/29
    DATA for: Official rating 99, 12 lb above field average; Trainer 40% wins (2/5), last 14 days; Good recent finishing positions
    DATA against: Last-run finishing speed -3.1% vs that field (faded); Carries 13 lb more than average
- Jolly Potter (hrs_34874455) | 7yo G | 148lb | OR 79 | draw 0 | jockey Alan O'Sullivan(5) | trainer James Andrew Fahey (14d 0/4) | headgear h | last run 14 days | form 0-0043 | MARKET 11.2% | 09:00 median 4.50 | Matchbook -
    comment: Jolly Potter is winless in his last five, though a third last time out and a fourth two starts back show some improvement, and he's fresh from a run 14 days ago.
    DATA: model 5.4% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 21 Jul Ballinrobe 22.2f Good 15/16; 1 Oct Clonmel 19.7f Good 4/16; 3 Nov Fairyhouse (IRE) 20f Good To Yielding 3/15 fig 80
    DATA for: Last-run finishing speed +5.0% vs that field (finished strongly); Carries 7 lb less than average
    DATA against: Official rating 79, 8 lb below field average
- Political Stance (hrs_52742032) | 6yo G | 164lb | OR 95 | draw 0 | jockey Conor Smithers(7) | trainer C Byrnes (14d 0/7) | headgear tp | last run 31 days | form P-0051 | MARKET 9.5% | 09:00 median 6.00 | Matchbook -
    comment: Won last time out, 31 days ago, after a fifth two starts back, and he has run over today's trip before.
    DATA: model 7.8% | style Midfield (led 3% of runs) | runs in data 6 | last 3: 11 Sep Ballinrobe 17.2f Good To Yielding 12/16; 4 Oct Killarney 22.8f Good To Yielding 5/13; 17 Oct Limerick (IRE) 21.5f Good To Yielding 1/16 fig 93
    DATA for: Best recent form figure 93, 10 lb above field average; Official rating 95, 8 lb above field average
    DATA against: Carries 9 lb more than average; Race comments mention jumping mistakes in 2 of its last 5 runs; Pulled up in 1 of its last 5 jumps runs
- Chanceitlucky (hrs_39959332) | 7yo G | 158lb | OR 89 | draw 0 | jockey Kevin Healy(7) | trainer Adrian Murray (14d 1/1) | headgear - | last run 43 days | form 46-501 | MARKET 7.9% | 09:00 median 6.50 | Matchbook 8.80
    DATA: model 9.0% | style Prominent (led 54% of runs) | runs in data 3 | last 3: 10 Aug Ballinrobe 22.5f Good 5/16; 24 Aug Ballinrobe 22.3f Good 12/16; 5 Oct Fairyhouse 24f Good 1/14
    DATA for: Last-run finishing speed +3.6% vs that field (finished strongly); Has won at this trip or further
- Spellacy's Cross (hrs_34571362) | 7yo G | 152lb | OR 83 | draw 0 | jockey Ricky Doyle | trainer James M Barcoe (14d 0/4) | headgear - | last run 13 days | form F-3473 | MARKET 7.2% | 09:00 median 8.00 | Matchbook -
    comment: Third last time out and fit after 13 days, Spellacy's Cross has run over today's trip and going before, but he is yet to win in his last five starts and a seventh two starts back tempers enthusiasm. Carrying 152 lb off 83, he looks a midfield sort.
    DATA: model 7.3% | style Midfield (led 3% of runs) | runs in data 7 | last 3: 28 May Limerick 22f Soft 4/13; 9 Jun Sligo 25.8f Yielding 7/16; 4 Nov Wexford (IRE) 20f Yielding 3/13 fig 80
    DATA for: Last-run finishing speed +5.8% vs that field (finished strongly)
    DATA against: Fell or unseated in 1 of its last 5 jumps runs
- Shotgun Jack (hrs_30567950) | 8yo G | 168lb | OR 99 | draw 0 | jockey Luke Burke Ott(7) | trainer Alexander Ott (14d 0/1) | headgear h | last run 22 days | form 0P09-2 | MARKET 6.8% | 09:00 median 8.00 | Matchbook 8.40
    comment: The main risk is that he's yet to win in recent starts and carries 168 lb off 99.
    DATA: model 11.4% | style Leader (led 57% of runs) | runs in data 1 | last 3: 26 Oct Galway (IRE) 24f Heavy 2/19 fig 96
    DATA for: Best recent form figure 96, 13 lb above field average; Official rating 99, 12 lb above field average
    DATA against: Carries 13 lb more than average; Lightly raced: 1 run in our data, so the model has little to go on
- Creadan Grace (hrs_50036315) | 6yo M | 159lb | OR 90 | draw 0 | jockey  | trainer Gordon Elliott (14d 12/73) | headgear p | last run 138 days | form 3P-453 | MARKET 5.6% | 09:00 median 9.00 | Matchbook -
    comment: The big risk is a 138-day absence, with 159 lb on her back.
    DATA: model 7.0% | style Midfield (led 3% of runs) | runs in data 4 | last 3: 13 May Punchestown 24f Good To Yielding 4/18; 7 Jun Perth 23.9f Good 5/13; 2 Jul Perth 23.9f Good 3/10
    DATA against: Returns from a 138-day break; Pulled up in 1 of its last 4 jumps runs
- Vision De Maine (hrs_34457150) | 7yo G | 165lb | OR 96 | draw 0 | jockey Mike O'Connor | trainer Emmet Mullins (14d 2/5) | headgear tp | last run 22 days | form 3PPP-P | MARKET 5.1% | 09:00 median 9.50 | Matchbook -
    DATA: model 5.9% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 16 Jan Market Rasen 23.9f Soft PU/8; 12 Apr Ffos Las 23.8f Good To Soft PU/7; 26 Oct Galway (IRE) 24f Heavy PU/19
    DATA for: Official rating 96, 9 lb above field average; Trainer 40% wins (2/5), last 14 days
    DATA against: Poor recent finishing positions; Carries 10 lb more than average; Pulled up in 3 of its last 3 jumps runs
- Kilkee Bay (hrs_34665351) | 7yo G | 159lb | OR 90 | draw 0 | jockey Gearoid Brouder(5) | trainer E McNamara (14d 0/6) | headgear p | last run 7 days | form 125U83 | MARKET 4.0% | 09:00 median 13.00 | Matchbook -
    comment: The risk is inconsistency, with an eighth and an unseated in his last four starts, plus 159 lb to carry.
    DATA: model 6.7% | style Held up (led 3% of runs) | runs in data 8 | last 3: 20 Aug Killarney 23.5f Good UR/12; 4 Oct Killarney 23.5f Good To Yielding 8/15; 10 Nov Fairyhouse (IRE) 24f Good To Yielding 3/5 fig 86
    DATA against: Fell or unseated in 1 of its last 5 jumps runs; First run over hurdles in our data
- Scathach (hrs_59928666) | 6yo M | 155lb | OR 86 | draw 0 | jockey Shane O'Callaghan(3) | trainer Ross O'Sullivan (14d 1/16) | headgear p | last run 18 days | form 836060 | MARKET 3.9% | 09:00 median 17.00 | Matchbook -
    comment: Scathach is winless in her last six, with a third five starts back her best finish and two sixths since, but 18 days since her last run keeps her fresh and she has run over today's trip.
    DATA: model 6.4% | style Midfield (led 3% of runs) | runs in data 8 | last 3: 3 Aug Cork 18f Good 12/18; 26 Sep Listowel 22f Good 6/17; 30 Oct Down Royal (IRE) 24.5f Good To Yielding 10/20 fig 82
    DATA for: Last-run finishing speed +3.4% vs that field (finished strongly)
    DATA against: Poor recent finishing positions
- Inches Away (hrs_46450292) | 7yo M | 141lb | OR 72 | draw 0 | jockey Ethan O'Sullivan(7) | trainer Paul Cashman (14d 0/1) | headgear - | last run 10 days | form /04097 | MARKET 3.8% | 09:00 median 16.25 | Matchbook -
    comment: Inches Away is winless in her last five, with a seventh last time out and a ninth two starts back, and she is hard to fancy after just ten days' rest while carrying 141 lb off an official mark of 72.
    DATA: model 3.3% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 28 Aug Wexford 20.5f Yielding 11/14; 4 Oct Killarney 17f Good 9/16; 7 Nov Gowran Park (IRE) 20f Good To Yielding 7/13
    DATA for: Carries 14 lb less than average
    DATA against: Official rating 72, 15 lb below field average; Poor recent finishing positions
- Chasing Crowns (hrs_45855348) | 6yo M | 152lb | OR 83 | draw 0 | jockey Harry Sexton(7) | trainer E Sheehy (14d 0/2) | headgear b | last run 117 days | form 90-5P4 | MARKET 3.8% | 09:00 median 15.00 | Matchbook -
    comment: Chasing Crowns showed a bit of life when fourth last time out, but she's winless in her last five, was pulled up two starts back and returns after 117 days off.
    DATA: model 3.8% | style Held up (led 3% of runs) | runs in data 4 | last 3: 15 Jun Kilbeggan 24.5f Good 5/14; 6 Jul Roscommon 23.8f Good PU/16; 23 Jul Wexford 24f Good 4/14
    DATA for: Last-run finishing speed +3.6% vs that field (finished strongly)
    DATA against: Returns from a 117-day break; Pulled up in 1 of its last 4 jumps runs
- Mullanour (hrs_40095958) | 7yo G | 154lb | OR 85 | draw 0 | jockey Eoghan Finegan(5) | trainer W J Martin (14d 0/1) | headgear - | last run 212 days | form P02PF- | MARKET 3.4% | 09:00 median 17.00 | Matchbook -
    comment: Mullanour has been through a rough patch, falling last time out and pulled up two starts back, though he did finish second three starts back and has run over today's trip and going.
    DATA: model 5.8% | style Midfield (led 3% of runs) | runs in data 4 | last 3: 26 Feb Clonmel 24f Heavy 2/15; 12 Mar Limerick 22.8f Heavy PU/15; 19 Apr Tramore 20.5f Yielding F/16
    DATA against: Returns from a 212-day break; Race comments mention jumping mistakes in 2 of its last 4 runs; Fell or unseated in 1 of its last 4 jumps runs; Pulled up in 1 of its last 4 jumps runs
- Prophetess Miriam (hrs_52708992) | 6yo M | 156lb | OR 87 | draw 0 | jockey Ben Harvey | trainer Cian Collins (14d 1/9) | headgear ht | last run 44 days | form -89988 | MARKET 3.0% | 09:00 median 23.00 | Matchbook -
    comment: Prophetess Miriam has finished eighth, eighth, ninth, ninth and eighth in her last five starts, so she is winless in that spell and returns after 44 days off.
    DATA: model 2.6% | style Held up (led 4% of runs) | runs in data 5 | last 3: 4 Aug Roscommon 15.5f Yielding To Soft 9/13; 19 Sep Navan 21f Good 8/15; 4 Oct Killarney 22.8f Good To Yielding 8/13
    DATA against: Poor recent finishing positions
- Hakensack (hrs_34859867) | 7yo G | 148lb | OR 79 | draw 0 | jockey  | trainer P. J. Rothwell (14d 0/24) | headgear p (1st time) | last run 157 days | form 269-UP | MARKET 2.9% | 09:00 median 21.00 | Matchbook -
    comment: Hakensack is hard to fancy, having pulled up last time out and unseated two starts back, and he returns after 157 days off with a yard 0/24 in the last 14 days.
    DATA: model 4.0% | style Prominent (led 23% of runs) | runs in data 4 | last 3: 29 Jan Thurles 20f Heavy 9/16; 21 May Limerick 22.7f Good UR/11; 13 Jun Downpatrick 21.8f Good PU/14
    DATA for: Carries 7 lb less than average; First-time headgear
    DATA against: Official rating 79, 8 lb below field average; Trainer 0 wins from 24 runs, last 14 days; Poor recent finishing positions; Returns from a 157-day break; Race comments mention jumping mistakes in 3 of its last 4 runs; Fell or unseated in 1 of its last 4 jumps runs; Pulled up in 1 of its last 4 jumps runs
- Fervida (hrs_54432483) | 6yo M | 141lb | OR 72 | draw 0 | jockey Charlie O'Dwyer(3) | trainer J A Berry (14d 0/1) | headgear p | last run 14 days | form U74000 | MARKET 2.5% | 09:00 median 29.00 | Matchbook -
    comment: Fervida is hard to fancy, unplaced in her last three and without a win in her last six, with a fourth four starts back the best of her recent efforts. She has run over today's trip and is fresh enough after 14 days, but 141 lb is a hefty burden.
    DATA: model 2.5% | style Held up (led 4% of runs) | runs in data 9 | last 3: 5 Oct Fairyhouse 24f Good 10/14; 17 Oct Limerick (IRE) 21.5f Good To Yielding 10/16 fig 67; 3 Nov Fairyhouse (IRE) 20f Good To Yielding 10/15 fig 60
    DATA for: Carries 14 lb less than average
    DATA against: Best recent form figure 67, 16 lb below field average; Official rating 72, 15 lb below field average; Poor recent finishing positions
- Rebel Queen (hrs_61521740) | 4yo F | 154lb | OR 87 | draw 0 | jockey Danny Power(7) | trainer Colin Motherway (14d 0/4) | headgear p (1st time) | last run 13 days | form 45-708 | MARKET 2.2% | 09:00 median 34.00 | Matchbook -
    comment: Rebel Queen is winless in her last five, with an eighth last time out following an unplaced run and a seventh, so the trend is heading the wrong way. She does race again quickly after 13 days, but 154 lb off an official mark of 87 is a lot to ask.
    DATA: model 2.0% | style Prominent (led 29% of runs) | runs in data 6 | last 3: 29 May Tramore 21.7f Good 7/10; 28 Sep Roscommon 20.2f Good To Yielding 11/15; 4 Nov Wexford (IRE) 20f Yielding 8/13
    DATA for: First-time headgear
    DATA against: Last-run finishing speed -4.2% vs that field (faded); Poor recent finishing positions; Race comments mention jumping mistakes in 2 of its last 5 runs

## 3:50 Limerick | race_id rac_32304698517 | Limerick (Ladies Pro/Am) Flat Race
NH Flat |  | 2m | going Yielding | Turf | 12 runners | rating band - | age 4yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Marble Hill (hrs_63776335) | 4yo G | 168lb | OR - | draw 0 | jockey Miss Georgie Benson(7) | trainer Gavin Cromwell (14d 4/38) | headgear - | last run 22 days | form 2-3 | MARKET 27.0% | 09:00 median 2.63 | Matchbook -
    comment: Marble Hill arrives in sound order, third last time out and a second two starts back, fresh from a run 22 days ago and with experience of today's trip and going.
    DATA: model 18.7% | style Prominent (led 38% of runs) | runs in data 2 | last 3: 18 Apr Bellewstown 17.1f Yielding 2/15; 26 Oct Galway (IRE) 16.5f Heavy 3/7 fig 103
    DATA for: Best recent form figure 103, 15 lb above field average; Good recent finishing positions
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Todo Bien (hrs_61456143) | 4yo G | 168lb | OR - | draw 0 | jockey Miss Charlotte Butler(7) | trainer Gordon Elliott (14d 12/73) | headgear - | last run 197 days | form 3-6 | MARKET 17.8% | 09:00 median 4.00 | Matchbook -
    comment: Todo Bien is hard to fancy after 197 days off, having finished sixth last time out and without a win in his last two starts, and he carries a hefty 168 lb.
    DATA: model 18.3% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 7 Feb Naas 15.7f Soft To Heavy 3/5; 4 May Down Royal 17.4f Good 6/12
    DATA against: Returns from a 197-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- Native Deal (hrs_40880077) | 6yo G | 168lb | OR - | draw 0 | jockey Miss A B O'Connor | trainer A. McCann (14d 0/4) | headgear t (1st time) | last run 304 days | form 5/64- | MARKET 12.4% | 09:00 median 7.50 | Matchbook 1.10
    comment: The big risk is a 304-day absence, which leaves fitness a real question.
    DATA: model 3.9% | style Held up (led 8% of runs) | runs in data 1 | last 3: 17 Jan Navan 16f Soft To Heavy 4/8
    DATA for: First-time headgear
    DATA against: Returns from a 304-day break; Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Fred Mooser (hrs_17395470764) | 4yo G | 168lb | OR - | draw 0 | jockey Miss N Lockhead Anderson(7) | trainer Mark Fahey (14d 0/8) | headgear - | last run - days | form - | MARKET 11.0% | 09:00 median 7.50 | Matchbook -
    comment: Fred Mooser is an unraced gelding with no form to go on, so he is totally unexposed and open to improvement.
    DATA: model 6.6% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Trainer 0 wins from 8 runs, last 14 days; Lightly raced: 0 runs in our data, so the model has little to go on
- Some See Stars (hrs_39996607) | 6yo G | 168lb | OR - | draw 0 | jockey Miss H Ross(7) | trainer A L T Moore (14d 0/0) | headgear - | last run 17 days | form 67-P32 | MARKET 9.4% | 09:00 median 8.00 | Matchbook -
    comment: Some See Stars heads into this on an upward curve, second last time out and third two starts back, and he's fresh enough after 17 days off. He has run over today's trip and going before, though he's yet to win in his last five and carries 168 lb.
    DATA: model 13.8% | style Held up (led 3% of runs) | runs in data 6 | last 3: 12 May Sligo 17.8f Good PU/15; 10 Oct Fairyhouse 16f Good 3/10; 31 Oct Down Royal (IRE) 17f Good 2/14 fig 97
    DATA for: Best recent form figure 97, 9 lb above field average
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Tlc Gold (hrs_17395535430) | 4yo G | 168lb | OR - | draw 0 | jockey Miss J Townend | trainer Paul John Gilligan (14d 0/2) | headgear - | last run - days | form - | MARKET 8.5% | 09:00 median 9.00 | Matchbook -
    comment: Tlc Gold is a debutant with no recorded form, so he is totally unexposed and open to improvement, and the unknown is the angle here. He carries 168 lb, a hefty burden for a newcomer to shoulder.
    DATA: model 6.6% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Hoof And Hustle (hrs_59928687) | 5yo G | 168lb | OR - | draw 0 | jockey Miss Ella Herbison(7) | trainer N Dooly (14d 0/3) | headgear - | last run 12 days | form 0-805 | MARKET 3.4% | 09:00 median 26.00 | Matchbook -
    comment: Hoof And Hustle is winless in his last four, with a fifth last time out the best of them and unplaced efforts either side of an eighth, so he is hard to fancy.
    DATA: model 3.7% | style Held up (led 5% of runs) | runs in data 3 | last 3: 14 May Clonmel 16.7f Good To Yielding 8/10; 3 Aug Cork 18f Good 15/17; 5 Nov Clonmel (IRE) 16.5f Good 5/12 fig 76
    DATA against: Best recent form figure 76, 12 lb below field average; Pace: steady gallop likely, hard to come from off the pace
- Cant Stopthe Clock (hrs_17394810545) | 5yo M | 161lb | OR - | draw 0 | jockey Sarah Kavanagh(7) | trainer Edward F Power (14d 2/4) | headgear h | last run 17 days | form 7 | MARKET 3.1% | 09:00 median 29.00 | Matchbook -
    comment: Seventh on her only recent start 17 days ago, Cant Stopthe Clock has run over today's trip and is fresh enough, but she is yet to win in recent form and carries 161 lb.
    DATA: model 7.4% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 31 Oct Down Royal (IRE) 17f Good 7/14 fig 81
    DATA against: Best recent form figure 81, 7 lb below field average; Lightly raced: 1 run in our data, so the model has little to go on
- Moot Hall (hrs_17390837758) | 5yo M | 161lb | OR - | draw 0 | jockey Ms N M Bradley(7) | trainer Eoin Griffin (14d 0/2) | headgear h | last run 17 days | form 056 | MARKET 2.3% | 09:00 median 51.00 | Matchbook -
    comment: The main risk is that she is yet to score in her last three, finishing sixth last time out.
    DATA: model 3.5% | style Midfield (led 5% of runs) | runs in data 3 | last 3: 16 Aug Tramore 16.6f Good To Yielding 11/12; 13 Oct Punchestown 16.2f Good 5/14; 31 Oct Down Royal (IRE) 17f Good 6/14 fig 83
    DATA against: Best recent form figure 83, 5 lb below field average
- Heartbreak Prince (hrs_53081308) | 4yo G | 168lb | OR - | draw 0 | jockey Miss A L Fitzgibbon(7) | trainer G Mangan (14d 0/3) | headgear t (1st time) | last run - days | form - | MARKET 2.0% | 09:00 median 51.00 | Matchbook -
    comment: Heartbreak Prince is unexposed, with no recorded form to go on, so this gelding is an unknown quantity who looks open to improvement. He carries 168 lb, which is a hefty burden to shoulder first time out.
    DATA: model 6.6% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: First-time headgear
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Allez Yeats (hrs_66655309) | 7yo M | 161lb | OR - | draw 0 | jockey Ms A Power(7) | trainer James M Barcoe (14d 0/4) | headgear - | last run 128 days | form P | MARKET 1.6% | 09:00 median 67.00 | Matchbook -
    comment: Unexposed mare with only one recent run to go on, and she was pulled up last time out 128 days ago, so there's plenty to prove; she's yet to win in that short spell and looks open to improvement, carrying 161 lb.
    DATA: model 4.2% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 12 Jul Sligo 18.3f Good PU/11
    DATA against: Returns from a 128-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Mister Bec (hrs_17395534387) | 4yo G | 168lb | OR - | draw 0 | jockey Ms S K Breen(7) | trainer P J Breen (14d 0/0) | headgear - | last run 177 days | form PP | MARKET 1.5% | 09:00 median 138.50 | Matchbook -
    comment: Mister Bec is lightly raced and unexposed, but he was pulled up last time out and again two starts back, so he has plenty to prove after 177 days off. Carrying 168 lb, he is yet to win in his last two starts and could still have improvement to come.
    DATA: model 6.6% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 177-day break; Lightly raced: 0 runs in our data, so the model has little to go on
