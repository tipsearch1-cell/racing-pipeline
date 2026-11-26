# Card review packet: Thurles, 2026-11-26

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
{"meeting": "thurles", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 12:11 Thurles | race_id rac_32305546923 | William Hill Challenge Series Handicap Steeplechase
Chase |  | 3m1f66y | going Good | Turf | 14 runners | rating band - | age 4yo+
DATA pace: Even - Two likely leaders (Ceroc, Chanceitlucky). A fair, even gallop is most likely.
- Chanceitlucky (hrs_39959332) | 7yo G | 145lb | OR 89 | draw 0 | jockey Kevin Healy(7) | trainer Adrian Murray (14d 0/1) | headgear - | last run 52 days | form 46-501 | MARKET 15.5% | 09:00 median 5.00 | Matchbook 5.70 | CHECK (skip line 4.75)
    DATA: model 9.4% | style Prominent (led 54% of runs) | runs in data 3 | last 3: 10 Aug Ballinrobe Hurdle 22.5f Good 5/16; 24 Aug Ballinrobe Hurdle 22.3f Good 12/16; 5 Oct Fairyhouse Hurdle 24f Good 1/14
    DATA for: Last-run finishing speed +3.6% vs that field (finished strongly); Carries 9 lb less than average
    DATA against: Official rating 89, 8 lb below field average; First run over fences in our data
- Everystep Oftheway (hrs_29538726) | 8yo G | 140lb | OR 81 | draw 0 | jockey Phillip Enright | trainer Oliver McKiernan (14d 0/4) | headgear p | last run 17 days | form 44/072 | MARKET 14.1% | 09:00 median 5.90 | Matchbook 6.00
    comment: Carrying 140 lb off 81 is a big ask.
    DATA: model 6.1% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 10 Aug Ballinrobe Hurdle 22.5f Good 11/16; 5 Oct Fairyhouse Hurdle 24f Good 7/14; 9 Nov Punchestown (IRE) Chase 24.5f Good To Yielding 2/12 fig 79
    DATA for: Last-run finishing speed +3.1% vs that field (finished strongly); Carries 14 lb less than average
    DATA against: Best recent form figure 79, 16 lb below field average; Official rating 81, 16 lb below field average
- Mistyburn (hrs_52495352) | 6yo G | 145lb | OR 89 | draw 0 | jockey Simon Torrens | trainer P. J. Rothwell (14d 0/33) | headgear tp | last run 23 days | form -66323 | MARKET 11.9% | 09:00 median 6.00 | Matchbook 8.00
    comment: Mistyburn has been in the frame in three of his last five, including a third last time out, yet he's winless in that spell and the stable is 0/33 over the last fortnight.
    DATA: model 8.9% | style Held up (led 3% of runs) | runs in data 10 | last 3: 2 Aug Galway Chase 22.5f Good 3/18; 11 Sep Ballinrobe Chase 23.3f Good To Yielding 2/16; 3 Nov Fairyhouse (IRE) Chase 24.5f Good To Yielding 3/7 fig 86
    DATA for: Last-run finishing speed +3.3% vs that field (finished strongly); Good recent finishing positions; Carries 9 lb less than average
    DATA against: Best recent form figure 86, 9 lb below field average; Official rating 89, 8 lb below field average; Trainer 0 wins from 33 runs, last 14 days; Race comments mention jumping mistakes in 2 of its last 5 runs
- Ceroc (hrs_28295127) | 8yo G | 168lb | OR 112 | draw 0 | jockey Alan O'Sullivan(5) | trainer A. Slattery (14d 0/16) | headgear tb | last run 23 days | form 2P1321 | MARKET 11.1% | 09:00 median 6.00 | Matchbook 9.20
    comment: Ceroc arrives in cracking nick, a winner last time out, then a second, a third and a winner four starts back, and he's fresh enough after 23 days off.
    DATA: model 17.5% | style Prominent (led 43% of runs) | runs in data 9 | last 3: 8 Aug Wexford Chase 25f Good 3/7; 22 Oct Clonmel (IRE) Chase 21f Good 2/10 fig 110; 3 Nov Fairyhouse (IRE) Chase 24.5f Good To Yielding 1/7 fig 108
    DATA for: Best recent form figure 110, 15 lb above field average; Official rating 112, 14 lb above field average; Good recent finishing positions
    DATA against: Trainer 0 wins from 16 runs, last 14 days; Carries 14 lb more than average; Race comments mention jumping mistakes in 2 of its last 5 runs; Pulled up in 1 of its last 5 jumps runs
- Mickey Cohen (hrs_40918479) | 5yo G | 161lb | OR 105 | draw 0 | jockey Sam Ewing | trainer Noel Meade (14d 3/15) | headgear - | last run 23 days | form 456271 | MARKET 9.4% | 09:00 median 8.00 | Matchbook 9.80
    DATA: model 12.1% | style Midfield (led 3% of runs) | runs in data 6 | last 3: 5 Oct Fairyhouse Hurdle 24f Good 2/13; 23 Oct Sligo (IRE) Hurdle 25.5f Yielding To Soft 7/9 fig 92; 3 Nov Fairyhouse (IRE) Hurdle 24f Good To Yielding 1/12 fig 100
    DATA for: Best recent form figure 100, 5 lb above field average; Official rating 105, 8 lb above field average; Trainer 20% wins (3/15), last 14 days; Last-run finishing speed +2.3% vs that field (finished strongly); Good recent finishing positions
    DATA against: Carries 7 lb more than average; Race comments mention jumping mistakes in 2 of its last 5 runs
- Giant Haystacks (hrs_38217592) | 7yo G | 161lb | OR 105 | draw 0 | jockey Shane Markey(7) | trainer Ross O'Sullivan (14d 0/17) | headgear t | last run 18 days | form 310916 | MARKET 7.9% | 09:00 median 10.00 | Matchbook 11.00
    comment: Giant Haystacks was beaten into sixth last time out, though he's won twice in his last six starts, including a win two starts back, and he's fresh enough after 18 days.
    DATA: model 7.7% | style Midfield (led 3% of runs) | runs in data 9 | last 3: 28 Aug Wexford Chase 19.5f Yielding 9/9; 14 Oct Punchestown (IRE) Chase 21.5f Good 1/8 fig 99; 8 Nov Naas (IRE) Chase 20f Good To Yielding 6/9
    DATA for: Official rating 105, 8 lb above field average
    DATA against: Recent figures 6 lb below its current mark (looks high in the weights); Trainer 0 wins from 17 runs, last 14 days; Carries 7 lb more than average; Race comments mention jumping mistakes in 2 of its last 5 runs
- Smallcraftwarning (hrs_31083213) | 9yo G | 156lb | OR 100 | draw 0 | jockey Daniel King | trainer John Patrick Ryan (14d 0/5) | headgear t | last run 7 days | form 112F64 | MARKET 7.9% | 09:00 median 9.50 | Matchbook 12.00
    comment: Smallcraftwarning won twice in his last six starts, though that was five and six runs back, and he has since been a sixth two starts back and a fourth last time out. He has run over today's trip and going and is back quickly after seven days, but 156 lb is a hefty burden for a midfield type.
    DATA: model 5.3% | style Held up (led 3% of runs) | runs in data 17 | last 3: 14 Oct Punchestown (IRE) Chase 23f Good F/4; 5 Nov Clonmel (IRE) Hurdle 24f Good 6/7 fig 106; 19 Nov Thurles (IRE) Chase 22f Good 4/12 fig 96
    DATA for: Best recent form figure 106, 11 lb above field average; Recent figures 6 lb above its current mark (looks well handicapped)
    DATA against: Race comments mention jumping mistakes in 2 of its last 5 runs; Fell or unseated in 1 of its last 5 jumps runs
- Littlebiggie (hrs_35054964) | 9yo M | 162lb | OR 106 | draw 0 | jockey Liam Quinlan | trainer Ray Hackett (14d 0/5) | headgear t | last run 14 days | form 480F24 | MARKET 6.8% | 09:00 median 12.00 | Matchbook 12.50
    comment: Littlebiggie arrives fit after a fourth last time out, 14 days ago, and a second two starts back shows she is in good heart, with experience of today's trip and going. The risk is the 162 lb burden, and she is yet to win in her last six outings.
    DATA: model 4.3% | style Prominent (led 23% of runs) | runs in data 7 | last 3: 18 Sep Downpatrick Chase 23.5f Good F/15; 22 Oct Clonmel (IRE) Chase 18.5f Good 2/5 fig 108; 12 Nov Thurles (IRE) Chase 18f Good 4/12 fig 102
    DATA for: Best recent form figure 108, 13 lb above field average; Official rating 106, 8 lb above field average
    DATA against: Carries 8 lb more than average; Fell or unseated in 1 of its last 5 jumps runs
- Knocknagoran Lady (hrs_43097369) | 7yo M | 162lb | OR 106 | draw 0 | jockey Conor Stone-Walsh | trainer Cian Hughes (14d 0/0) | headgear tv | last run 16 days | form 1141P5 | MARKET 3.8% | 09:00 median 19.00 | Matchbook 26.00
    comment: Three wins in her last six starts catch the eye, but Knocknagoran Lady was only fifth last time out after being pulled up the run before, and she carries 162 lb off an official mark of 106.
    DATA: model 10.3% | style Midfield (led 23% of runs) | runs in data 10 | last 3: 28 Aug Down Royal Hurdle 24f Good 1/15; 19 Sep Navan Hurdle 21f Good PU/15; 10 Nov Fairyhouse (IRE) Hurdle 24.5f Good To Yielding 5/11 fig 103
    DATA for: Best recent form figure 103, 8 lb above field average; Official rating 106, 8 lb above field average
    DATA against: Carries 8 lb more than average; Pulled up in 1 of its last 5 jumps runs; First run over fences in our data
- Orkneys Jack (hrs_51373693) | 7yo G | 152lb | OR 96 | draw 0 | jockey Sean O'Keeffe | trainer L Young (14d 0/1) | headgear - | last run 14 days | form 355757 | MARKET 3.1% | 09:00 median 23.00 | Matchbook 34.00
    comment: Orkneys Jack is winless in his last six, with a seventh last time out and a third six starts back his best recent finish, though he has run over today's trip and going and is back after just 14 days.
    DATA: model 2.9% | style Midfield (led 3% of runs) | runs in data 6 | last 3: 16 Aug Tramore Chase 22f Good To Yielding 7/10; 6 Oct Galway Chase 22.5f Yielding To Soft 5/8; 12 Nov Thurles (IRE) Chase 18f Good 7/12 fig 89
    DATA against: Best recent form figure 89, 6 lb below field average; Recent figures 7 lb below its current mark (looks high in the weights)
- Dorans Law (hrs_35231938) | 8yo G | 158lb | OR 102 | draw 0 | jockey Shane O'Callaghan(3) | trainer P. J. Rothwell (14d 0/33) | headgear p | last run 61 days | form 725FU7 | MARKET 2.7% | 09:00 median 29.00 | Matchbook 34.00
    DATA: model 5.2% | style Midfield (led 3% of runs) | runs in data 10 | last 3: 19 Aug Sligo Hurdle 25.8f Good F/11; 23 Sep Listowel Hurdle 24f Good UR/14; 26 Sep Listowel Chase 23.8f Good 7/14
    DATA against: Trainer 0 wins from 33 runs, last 14 days; Poor recent finishing positions; Fell or unseated in 2 of its last 5 jumps runs
- Born Bright (hrs_39021472) | 7yo M | 168lb | OR 112 | draw 0 | jockey James Smith(3) | trainer Ms Claire O'Connell (14d 1/3) | headgear p | last run 54 days | form 4-34PP | MARKET 2.6% | 09:00 median 29.00 | Matchbook 36.00
    comment: Born Bright has twice been pulled up lately, but a fourth three starts back and a third four runs ago show she can be competitive, and she has run over today's trip and going.
    DATA: model 4.1% | style Held up (led 3% of runs) | runs in data 4 | last 3: 8 Jun Roscommon Chase 25.1f Yielding To Soft 4/15; 26 Sep Listowel Chase 23.8f Good PU/14; 3 Oct Gowran Park Hurdle 24.2f Good To Yielding PU/11
    DATA for: Official rating 112, 14 lb above field average
    DATA against: Carries 14 lb more than average; Pulled up in 2 of its last 4 jumps runs
- Heroes of Renown (hrs_16855440) | 12yo G | 144lb | OR 88 | draw 0 | jockey Harry Sexton(7) | trainer John Joseph Hanlon (14d 0/8) | headgear b | last run 16 days | form -330PU | MARKET 1.8% | 09:00 median 34.00 | Matchbook 65.00
    comment: Heroes of Renown is yet to win in his last five, with an unseated last time out and a pulled up before that, though he was third four and five starts back and has run over today's trip and going.
    DATA: model 2.4% | style Prominent (led 4% of runs) | runs in data 4 | last 3: 22 Oct Clonmel (IRE) Chase 21f Good 10/15; 30 Oct Down Royal (IRE) Hurdle 24.5f Good To Yielding PU/20; 10 Nov Fairyhouse (IRE) Chase 24f Good To Yielding UR/5
    DATA for: Carries 10 lb less than average
    DATA against: Official rating 88, 10 lb below field average; Trainer 0 wins from 8 runs, last 14 days; Poor recent finishing positions; Fell or unseated in 1 of its last 4 jumps runs; Pulled up in 1 of its last 4 jumps runs; Aged 12, older than most of this field
- Malton Groove (hrs_27428408) | 9yo G | 140lb | OR 74 | draw 0 | jockey Patrick M O'Brien(5) | trainer Dermot A McLoughlin (14d 0/5) | headgear t | last run 17 days | form 36FP96 | MARKET 1.4% | 09:00 median 51.00 | Matchbook 95.00
    comment: Malton Groove is winless in his recent form, with a sixth last time out following a ninth and a pulled up, so he is hard to fancy at 140 lb.
    DATA: model 3.9% | style Midfield (led 23% of runs) | runs in data 9 | last 3: 30 Sep Sligo Chase 21f Good PU/15; 9 Oct Downpatrick Chase 23.7f Good 9/14; 9 Nov Punchestown (IRE) Chase 24.5f Good To Yielding 6/12 fig 71
    DATA for: Carries 14 lb less than average
    DATA against: Best recent form figure 71, 24 lb below field average; Official rating 74, 24 lb below field average; Poor recent finishing positions; Race comments mention jumping mistakes in 2 of its last 5 runs; Fell or unseated in 1 of its last 5 jumps runs; Pulled up in 1 of its last 5 jumps runs

## 12:46 Thurles | race_id rac_32305548860 | Racing TV Club Day Steeplechase (Listed)
Chase | Class 1 | 2m6f0y | going Good | Turf | 7 runners | rating band - | age 5yo+
DATA pace: Lone leader - Apple's Of Bresil is the only habitual front-runner and may be allowed an easy lead.
- Champ Kiely (hrs_23332561) | 10yo G | 154lb | OR 152 | draw 0 | jockey Paul Townend | trainer Mr W. P. Mullins (14d 12/49) | headgear - | last run 211 days | form S578P- | MARKET 27.6% | 09:00 median 3.25 | Matchbook 3.40 | CHECK (skip line 3.09)
    comment: The major risk is fitness, as he returns after 211 days having been pulled up last time out.
    DATA: model 8.9% | style Midfield (led 4% of runs) | runs in data 4 | last 3: 2 Feb Leopardstown Chase 24.5f Heavy 7/12; 11 Apr Aintree Chase 34.3f Good To Soft 8/34; 29 Apr Punchestown Chase 25f Yielding PU/5
    DATA for: Trainer 24% wins (12/49), last 14 days
    DATA against: Poor recent finishing positions; Returns from a 211-day break; Pulled up in 1 of its last 4 jumps runs
- Ile Atlantique (hrs_29917741) | 8yo G | 154lb | OR 155 | draw 0 | jockey Daniel King | trainer Mr W. P. Mullins (14d 12/49) | headgear t | last run 230 days | form /3282- | MARKET 22.7% | 09:00 median 3.75 | Matchbook 4.30
    comment: Ile Atlantique was second last time out and has been placed in three of his last four, yet he is winless in that spell and returns after 230 days off.
    DATA: model 27.3% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 1 Jan Tramore Chase 22.8f Soft 2/7; 1 Feb Leopardstown Chase 21.5f Heavy 8/23; 10 Apr Aintree Chase 21.1f Good To Soft 2/27
    DATA for: Trainer 24% wins (12/49), last 14 days; Last-run finishing speed +5.3% vs that field (finished strongly); Good recent finishing positions
    DATA against: Returns from a 230-day break
- Monty's Star (hrs_24769591) | 9yo G | 154lb | OR 157 | draw 0 | jockey Jordan Gainford | trainer Henry de Bromhead (14d 8/42) | headgear - | last run 229 days | form /0560- | MARKET 14.8% | 09:00 median 5.50 | Matchbook 6.80
    DATA: model 12.8% | style Prominent (led 8% of runs) | runs in data 2 | last 3: 2 Feb Leopardstown Chase 24.5f Heavy 6/12; 11 Apr Aintree Chase 34.3f Good To Soft 10/34
    DATA for: Official rating 157, 6 lb above field average
    DATA against: Returns from a 229-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- Lecky Watson (hrs_29523179) | 8yo G | 154lb | OR 154 | draw 0 | jockey Sean O'Keeffe | trainer Mr W. P. Mullins (14d 12/49) | headgear t (1st time) | last run 229 days | form 77P8P- | MARKET 11.0% | 09:00 median 8.00 | Matchbook 8.80
    comment: The risk is stark: he is without a win in his last five, was pulled up last time out and returns after 229 days off.
    DATA: model 7.1% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 2 Feb Leopardstown Chase 24.5f Heavy PU/12; 21 Feb Fairyhouse Chase 26f Heavy 8/9; 11 Apr Aintree Chase 34.3f Good To Soft PU/34
    DATA for: Trainer 24% wins (12/49), last 14 days; First-time headgear
    DATA against: Poor recent finishing positions; Returns from a 229-day break; Race comments mention jumping mistakes in 3 of its last 3 runs; Pulled up in 2 of its last 3 jumps runs
- Gerri Colombe (hrs_21327712) | 10yo G | 158lb | OR 160 | draw 0 | jockey Jack Kennedy | trainer Gordon Elliott (14d 11/81) | headgear p | last run 229 days | form P321F- | MARKET 10.5% | 09:00 median 7.00 | Matchbook 10.50
    comment: The risk is a 229-day absence, plus a fall last time out, under 158 lb.
    DATA: model 18.8% | style Prominent (led 3% of runs) | runs in data 4 | last 3: 21 Feb Fairyhouse Chase 26f Heavy 2/9; 17 Mar Down Royal Chase 26.2f Good To Yielding 1/4; 11 Apr Aintree Chase 34.3f Good To Soft F/34
    DATA for: Official rating 160, 9 lb above field average; Has won at this trip or further
    DATA against: Returns from a 229-day break; Fell or unseated in 1 of its last 4 jumps runs
- High Class Hero (hrs_24141285) | 9yo G | 154lb | OR 149 | draw 0 | jockey Danny Mullins | trainer Mr W. P. Mullins (14d 12/49) | headgear - | last run 208 days | form 2PP5P- | MARKET 10.4% | 09:00 median 9.00 | Matchbook 9.00
    comment: High Class Hero is hard to fancy, pulled up in three of his last five starts including last time out, and he returns after 208 days off. He has run over today's trip and going, and a second five starts back is his best recent finish, but 154 lb is a big burden.
    DATA: model 9.6% | style Midfield (led 3% of runs) | runs in data 4 | last 3: 8 Mar Naas Chase 24.8f Soft To Heavy PU/15; 11 Apr Aintree Chase 34.3f Good To Soft 5/34; 2 May Punchestown Chase 24.5f Yielding PU/21
    DATA for: Trainer 24% wins (12/49), last 14 days
    DATA against: Returns from a 208-day break; Race comments mention jumping mistakes in 2 of its last 4 runs; Pulled up in 3 of its last 4 jumps runs
- Apple's Of Bresil (hrs_34361698) | 8yo G | 158lb | OR 128 | draw 0 | jockey Sean Flanagan | trainer Barry Connell (14d 0/4) | headgear t | last run 43 days | form /0-123 | MARKET 3.0% | 09:00 median 29.00 | Matchbook 32.00
    comment: Form reads well enough, with a third last time out, a second two starts back and a win three starts back, and he has run over today's trip and going before.
    DATA: model 15.5% | style Leader (led 38% of runs) | runs in data 3 | last 3: 31 May Kilbeggan Chase 20.4f Good To Yielding 1/10; 20 Sep Listowel Chase 17.7f Good 2/5; 14 Oct Punchestown (IRE) Chase 23f Good 3/4 fig 141
    DATA for: Good recent finishing positions; Pace: may get an uncontested lead
    DATA against: Official rating 128, 23 lb below field average; Last-run finishing speed -2.2% vs that field (faded); Race comments mention jumping mistakes in 2 of its last 3 runs

## 1:21 Thurles | race_id rac_32305550797 | Connolly's RED MILLS Irish EBF Auction & Median Maiden Hurdle
Hurdle |  | 2m4f51y | going Good | Turf | 16 runners | rating band - | age 4-5yo
DATA pace: Even - Two likely leaders (S T Hamo, She Was The One). A fair, even gallop is most likely.
- Dieux Diligence (hrs_65451379) | 4yo G | 165lb | OR - | draw 0 | jockey J. J. Slevin | trainer Joseph Patrick O'Brien (14d 4/35) | headgear - | last run 119 days | form 43 | MARKET 25.0% | 09:00 median 3.00 | Matchbook 3.45 | CHECK (skip line 2.85)
    DATA: model 9.7% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 6 Jun Punchestown NH Flat 16.5f Good To Yielding 4/18; 30 Jul Galway NH Flat 18f Good 3/16
    DATA for: Last-run finishing speed +6.5% vs that field (finished strongly)
    DATA against: Returns from a 119-day break; Lightly raced: 2 runs in our data, so the model has little to go on; First run over hurdles in our data
- Missouri Snow (hrs_17390036734) | 5yo M | 159lb | OR - | draw 0 | jockey Carl Millar(5) | trainer Nigel Thomas Slevin (14d 0/5) | headgear - | last run 31 days | form 1-133 | MARKET 13.5% | 09:00 median 6.00 | Matchbook 6.00
    DATA: model 5.7% | style Prominent (led 5% of runs) | runs in data 3 | last 3: 6 Aug Sligo NH Flat 18.6f Good 1/8; 2 Oct Gowran Park NH Flat 16.5f Good 3/10; 26 Oct Galway (IRE) Hurdle 16.5f Soft To Heavy 3/10 fig 94
    DATA for: Good recent finishing positions
- Give It A Crack (hrs_17391680502) | 5yo M | 159lb | OR - | draw 0 | jockey Mike O'Connor | trainer Henry de Bromhead (14d 8/42) | headgear - | last run 31 days | form 23/34 | MARKET 11.2% | 09:00 median 6.00 | Matchbook 9.00
    DATA: model 7.2% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 24 Sep Listowel Hurdle 16f Good 3/14; 26 Oct Galway (IRE) Hurdle 16.5f Soft To Heavy 4/10 fig 91
    DATA against: Best recent form figure 91, 6 lb below field average; Lightly raced: 2 runs in our data, so the model has little to go on
- She Was The One (hrs_17390038820) | 4yo F | 158lb | OR - | draw 0 | jockey Michael Kenneally(3) | trainer Denis Gerard Hogan (14d 0/14) | headgear - | last run 12 days | form 2-3216 | MARKET 9.5% | 09:00 median 8.00 | Matchbook 9.00
    DATA: model 10.1% | style Leader (led 43% of runs) | runs in data 4 | last 3: 24 Aug Ballinrobe NH Flat 16.2f Good 2/11; 25 Sep Listowel NH Flat 16f Good To Yielding 1/14; 14 Nov Cheltenham NH Flat 16.5f Good 6/10 fig 105
    DATA for: Best recent form figure 105, 8 lb above field average; Good recent finishing positions
    DATA against: Trainer 0 wins from 14 runs, last 14 days; First run over hurdles in our data
- Conor'salwaysright (hrs_17389681071) | 4yo G | 165lb | OR - | draw 0 | jockey Alan O'Sullivan(5) | trainer P. J. Rothwell (14d 0/33) | headgear - | last run 46 days | form 512 | MARKET 8.8% | 09:00 median 8.00 | Matchbook 10.50
    DATA: model 6.3% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 4 Aug Roscommon NH Flat 15.5f Yielding To Soft 5/13; 19 Aug Sligo NH Flat 18.6f Good 1/8; 11 Oct Cork Hurdle 20.5f Good 2/7
    DATA for: Good recent finishing positions
    DATA against: Trainer 0 wins from 33 runs, last 14 days
- Dunleer Crystal (hrs_57071763) | 5yo G | 166lb | OR 110 | draw 0 | jockey Jack Kennedy | trainer Gordon Elliott (14d 11/81) | headgear - | last run 211 days | form 0233P- | MARKET 8.6% | 09:00 median 8.50 | Matchbook 10.00
    DATA: model 10.3% | style Prominent (led 29% of runs) | runs in data 3 | last 3: 7 Feb Naas Hurdle 18.5f Soft To Heavy 3/5; 10 Apr Wexford Hurdle 20f Good To Yielding 3/8; 29 Apr Punchestown Hurdle 19.3f Yielding PU/14
    DATA against: Returns from a 211-day break; Pulled up in 1 of its last 3 jumps runs
- The Ocean Queen (hrs_17389191904) | 5yo M | 159lb | OR - | draw 0 | jockey Keith Donoghue | trainer Gavin Cromwell (14d 4/39) | headgear h | last run 40 days | form 21-52 | MARKET 7.8% | 09:00 median 9.50 | Matchbook 11.50
    DATA: model 6.5% | style Prominent (led 38% of runs) | runs in data 2 | last 3: 25 Sep Listowel NH Flat 16f Good To Yielding 5/14; 17 Oct Limerick (IRE) NH Flat 17f Good To Yielding 2/8 fig 111
    DATA for: Best recent form figure 111, 14 lb above field average
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; First run over hurdles in our data
- S T Hamo (hrs_59399725) | 5yo G | 166lb | OR - | draw 0 | jockey James Smith(3) | trainer A. McCann (14d 0/4) | headgear ht | last run 21 days | form 435233 | MARKET 4.5% | 09:00 median 13.00 | Matchbook 24.00
    DATA: model 6.0% | style Prominent (led 43% of runs) | runs in data 7 | last 3: 10 Oct Fairyhouse NH Flat 16f Good 2/10; 31 Oct Down Royal (IRE) Hurdle 17f Good 3/12; 5 Nov Clonmel (IRE) Hurdle 16.5f Good 3/11 fig 104
    DATA for: Best recent form figure 104, 7 lb above field average; Good recent finishing positions
    DATA against: Race comments mention jumping mistakes in 2 of its last 2 runs
- Our Sonny (hrs_49757673) | 5yo G | 166lb | OR - | draw 0 | jockey Danny Mullins | trainer Thomas Mullins (14d 1/6) | headgear - | last run 21 days | form 6/0-56 | MARKET 1.9% | 09:00 median 34.00 | Matchbook 55.00
    DATA: model 4.8% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 28 Sep Roscommon NH Flat 15.6f Good To Yielding 5/16; 5 Nov Clonmel (IRE) Hurdle 16.5f Good 6/11 fig 87
    DATA against: Best recent form figure 87, 10 lb below field average; Lightly raced: 2 runs in our data, so the model has little to go on
- Getaway Harry (hrs_63810383) | 4yo G | 165lb | OR - | draw 0 | jockey Mr J L Gleeson | trainer Yvonne Latta (14d 0/0) | headgear t | last run 27 days | form 3-86 | MARKET 1.9% | 09:00 median 41.00 | Matchbook 46.00
    DATA: model 3.2% | style Prominent (led 38% of runs) | runs in data 2 | last 3: 25 May Ballinrobe NH Flat 16.7f Good 8/11; 30 Oct Down Royal (IRE) NH Flat 17f Good To Yielding 6/8 fig 98
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; First run over hurdles in our data
- Idaho Sunrise (hrs_17396012081) | 5yo G | 166lb | OR - | draw 0 | jockey G B Noonan | trainer Eoin Christopher McCarthy (14d 0/4) | headgear - | last run - days | form - | MARKET 1.5% | 09:00 median 81.00 | Matchbook 60.00
    DATA: model 4.8% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Mia In Milan (hrs_63810068) | 5yo M | 159lb | OR 90 | draw 0 | jockey Sam Ewing | trainer D E Fitzgerald (14d 0/0) | headgear - | last run 40 days | form -05866 | MARKET 1.4% | 09:00 median 41.00 | Matchbook 90.00
    DATA: model 12.2% | style Held up (led 3% of runs) | runs in data 6 | last 3: 11 Sep Ballinrobe Hurdle 18f Good To Yielding 8/15; 1 Oct Clonmel Hurdle 19.7f Good 6/11; 17 Oct Limerick (IRE) Hurdle 19f Good To Yielding 6/18 fig 85
    DATA against: Best recent form figure 85, 12 lb below field average; Poor recent finishing positions
- Quarry Road (hrs_17392709943) | 4yo G | 165lb | OR - | draw 0 | jockey Miss Ella Herbison(7) | trainer Moses McCabe (14d 0/0) | headgear - | last run 55 days | form 5 | MARKET 1.3% | 09:00 median 101.00 | Matchbook 60.00
    DATA: model 3.2% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 2 Oct Gowran Park Hurdle 16.4f Good 5/13
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Cad A Realta (hrs_17396011038) | 5yo G | 166lb | OR - | draw 0 | jockey Phillip Enright | trainer M F Morris (14d 0/3) | headgear - | last run - days | form - | MARKET 1.1% | 09:00 median 67.00 | Matchbook 120.00
    DATA: model 4.8% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Last Apache (hrs_62813072) | 5yo G | 166lb | OR - | draw 0 | jockey Eoghan Finegan(5) | trainer Ciaran Murphy (14d 0/5) | headgear h (1st time) | last run 250 days | form 6- | MARKET 0.9% | 09:00 median 67.00 | Matchbook 120.00
    DATA: model 4.4% | style Held up (led 8% of runs) | runs in data 1 | last 3: 21 Mar Navan NH Flat 16f Soft 6/9
    DATA for: First-time headgear
    DATA against: Last-run finishing speed -3.7% vs that field (faded); Returns from a 250-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Hidden Hurricane (hrs_17392906027) | 4yo G | 165lb | OR - | draw 0 | jockey Luke Burke Ott(7) | trainer Alexander Ott (14d 0/3) | headgear - | last run 40 days | form 00 | MARKET 0.9% | 09:00 median 151.00 | Matchbook 75.00
    DATA: model 0.9% | style Held up (led 5% of runs) | runs in data 2 | last 3: 26 Sep Listowel Hurdle 16f Good 10/12; 17 Oct Limerick (IRE) Hurdle 17f Yielding 10/16
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Race comments mention jumping mistakes in 2 of its last 2 runs

## 1:56 Thurles | race_id rac_32305552734 | Horse And Jockey 3-Y-O Maiden Hurdle
Hurdle |  | 2m0f11y | going Good | Turf | 11 runners | rating band - | age 3yo
DATA pace: Even - Two likely leaders (Tanzanite Diamond, Blackisthenewblack). A fair, even gallop is most likely.
- Neria (hrs_62296514) | 3yo F | 147lb | OR - | draw 0 | jockey Paul Townend | trainer Mr W. P. Mullins (14d 12/49) | headgear - | last run 238 days | form 32- | MARKET 38.9% | 09:00 median 2.20 | Matchbook 2.30
    DATA: model 6.1% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 24% wins (12/49), last 14 days
    DATA against: Returns from a 238-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Kenough (hrs_58133495) | 3yo G | 154lb | OR - | draw 0 | jockey J. J. Slevin | trainer Joseph Patrick O'Brien (14d 4/35) | headgear - | last run 26 days | form 32 | MARKET 24.0% | 09:00 median 3.50 | Matchbook 3.75
    DATA: model 15.8% | style Midfield (led 4% of runs) | runs in data 4 | last 3: 26 Sep Curragh Flat 10f Yielding 4/18; 13 Oct Punchestown Hurdle 16.2f Good 3/9; 31 Oct Down Royal (IRE) Hurdle 17f Good 2/8 fig 97
    DATA for: Best recent form figure 97, 4 lb above field average; Good recent finishing positions
- Sunrush (hrs_55978517) | 3yo G | 154lb | OR - | draw 0 | jockey Cian Quirke | trainer A. Slattery (14d 0/16) | headgear t | last run 11 days | form 3 | MARKET 14.0% | 09:00 median 5.50 | Matchbook 7.20
    DATA: model 10.1% | style Prominent (led 5% of runs) | runs in data 7 | last 3: 22 Sep Listowel Flat 14.2f Yielding 7/8; 30 Oct Dundalk (AW) (IRE) Flat 12f Standard 2/9 fig 75; 15 Nov Navan (IRE) Hurdle 16f Good To Yielding 3/15 fig 101
    DATA for: Best recent form figure 101, 8 lb above field average; Good recent finishing positions
    DATA against: Trainer 0 wins from 16 runs, last 14 days
- Maxminelli (hrs_56406868) | 3yo G | 154lb | OR - | draw 0 | jockey Jordan Gainford | trainer Henry de Bromhead (14d 8/42) | headgear tp (1st time) | last run 23 days | form 3 | MARKET 13.4% | 09:00 median 5.50 | Matchbook 8.40
    DATA: model 15.4% | style Prominent (led 3% of runs) | runs in data 6 | last 3: 11 Jul Limerick Flat 12.3f Good 2/6; 15 Aug Tramore Flat 12f Good To Yielding 4/8; 3 Nov Fairyhouse (IRE) Hurdle 16f Good To Yielding 3/13 fig 104
    DATA for: Best recent form figure 104, 11 lb above field average; Last-run finishing speed +4.8% vs that field (finished strongly); Good recent finishing positions; First-time headgear
- Belle Nuit (hrs_55453937) | 3yo F | 147lb | OR - | draw 0 | jockey Sean Flanagan | trainer Paul Nolan (14d 3/14) | headgear - | last run 23 days | form 5 | MARKET 2.9% | 09:00 median 21.00 | Matchbook 46.00
    DATA: model 5.9% | style Midfield (led 4% of runs) | runs in data 5 | last 3: 8 Sep Galway Flat 12f Soft 9/15; 27 Sep Curragh Flat 10f Heavy 9/18; 3 Nov Fairyhouse (IRE) Hurdle 16f Good To Yielding 5/13 fig 92
    DATA for: Trainer 21% wins (3/14), last 14 days; Last-run finishing speed +4.6% vs that field (finished strongly)
- Mountbatten (hrs_59025407) | 3yo G | 154lb | OR - | draw 0 | jockey Michael Kenneally(3) | trainer Denis Gerard Hogan (14d 0/14) | headgear - | last run 34 days | form - | MARKET 1.6% | 09:00 median 41.00 | Matchbook 95.00
    DATA: model 8.3% | style Midfield (led 23% of runs) | runs in data 6 | last 3: 22 Aug Lingfield Flat 13f Standard 6/6; 9 Oct Kempton Flat 12f Standard To Slow 3/7; 23 Oct Wolverhampton (AW) Flat 12f Standard 5/5 fig 38
    DATA against: Trainer 0 wins from 14 runs, last 14 days; First run over hurdles in our data
- Tanzanite Diamond (hrs_57255184) | 3yo G | 154lb | OR - | draw 0 | jockey Patrick M O'Brien(5) | trainer Adrian McGuinness (14d 2/24) | headgear - | last run 42 days | form - | MARKET 1.6% | 09:00 median 51.00 | Matchbook 95.00
    DATA: model 10.0% | style Leader (led 23% of runs) | runs in data 10 | last 3: 21 Sep Listowel Flat 12f Yielding 4/15; 5 Oct Killarney Flat 11.2f Soft 4/12; 15 Oct Curragh (IRE) Flat 14f Yielding To Soft 18/21
    DATA against: First run over hurdles in our data
- The Wee Man (hrs_58133516) | 3yo G | 154lb | OR - | draw 0 | jockey Phillip Enright | trainer Mark Michael McNiff (14d 0/3) | headgear - | last run 31 days | form 84 | MARKET 1.1% | 09:00 median 67.00 | Matchbook 140.00
    DATA: model 1.7% | style Held up (led 3% of runs) | runs in data 5 | last 3: 3 May Sligo Flat 10.7f Soft 7/9; 11 Oct Cork Hurdle 15.5f Good 8/10; 26 Oct Galway (IRE) Hurdle 16.5f Soft To Heavy 4/10
- Blackisthenewblack (hrs_58165296) | 3yo F | 147lb | OR - | draw 0 | jockey Harry Sexton(7) | trainer John Joseph Hanlon (14d 0/8) | headgear - | last run 160 days | form - | MARKET 1.1% | 09:00 median 51.00 | Matchbook 200.00
    DATA: model 5.3% | style Leader (led 43% of runs) | runs in data 4 | last 3: 30 Apr Kempton Flat 12f Standard To Slow 1/9; 16 May Thirsk Flat 12f Good 10/11; 19 Jun Goodwood Flat 12f Good 8/8
    DATA against: Trainer 0 wins from 8 runs, last 14 days; Last-run finishing speed -10.4% vs that field (faded); Returns from a 160-day break; First run over hurdles in our data
- Sands Castle (hrs_57878009) | 3yo F | 147lb | OR 90 | draw 0 | jockey Conor Lamon(7) | trainer Adrian Sexton (14d 0/1) | headgear - | last run 17 days | form 665 | MARKET 0.8% | 09:00 median 67.00 | Matchbook 220.00
    DATA: model 10.2% | style Midfield (led 3% of runs) | runs in data 10 | last 3: 28 Aug Down Royal Hurdle 17.4f Good 6/9; 19 Oct Gowran Park (IRE) Flat 8.5f Soft 8/16 fig 55; 9 Nov Punchestown (IRE) Hurdle 16f Good To Yielding 5/10 fig 69
    DATA against: Best recent form figure 69, 24 lb below field average
- Arizona Star (hrs_57255170) | 3yo F | 147lb | OR - | draw 0 | jockey Philip Byrnes | trainer Michael Mulvany (14d 1/9) | headgear - | last run 11 days | form U | MARKET 0.7% | 09:00 median 126.00 | Matchbook 200.00
    DATA: model 11.2% | style Prominent (led 8% of runs) | runs in data 11 | last 3: 19 Oct Gowran Park (IRE) Flat 8.5f Soft 7/16 fig 42; 29 Oct Punchestown (IRE) Flat 7f Yielding 4/11 fig 44; 15 Nov Navan (IRE) Hurdle 16f Good To Yielding UR/15
    DATA against: Fell or unseated in 1 of its last 1 jumps runs

## 2:31 Thurles | race_id rac_32305554671 | Irish Stallion Farms EBF Mares Maiden Hurdle
Hurdle |  | 2m0f11y | going Good | Turf | 20 runners | rating band - | age 4yo+
DATA pace: Lone leader - Potters Queen is the only habitual front-runner and may be allowed an easy lead.
- Mahollia (hrs_17396009995) | 4yo F | 161lb | OR - | draw 0 | jockey Mr P. W. Mullins | trainer Mr W. P. Mullins (14d 12/49) | headgear - | last run 278 days | form 1- | MARKET 35.6% | 09:00 median 1.73 | Matchbook 1.89
    DATA: model 3.0% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 24% wins (12/49), last 14 days
    DATA against: Returns from a 278-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Divaboriva (hrs_41346536) | 7yo M | 161lb | OR 115 | draw 0 | jockey Daniel King | trainer Jonathan Sweeney (14d 0/1) | headgear - | last run 200 days | form 2255-2 | MARKET 19.4% | 09:00 median 3.25 | Matchbook 3.30
    DATA: model 30.5% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 4 Apr Fairyhouse Hurdle 23.8f Yielding To Soft 5/20; 10 May Cork Hurdle 19.2f Good 2/15
    DATA for: Last-run finishing speed +7.6% vs that field (finished strongly)
    DATA against: Returns from a 200-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- Coole Cafe (hrs_59399697) | 4yo F | 161lb | OR - | draw 0 | jockey Sam Ewing | trainer Ian Patrick Donoghue (14d 0/11) | headgear h | last run 211 days | form 17113- | MARKET 11.0% | 09:00 median 5.50 | Matchbook 6.40
    DATA: model 11.1% | style Held up (led 3% of runs) | runs in data 4 | last 3: 7 Feb Naas NH Flat 15.7f Soft To Heavy 1/5; 22 Mar Limerick NH Flat 16.2f Soft To Heavy 1/7; 29 Apr Punchestown NH Flat 16.6f Yielding 3/16
    DATA for: Last-run finishing speed +7.4% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Trainer 0 wins from 11 runs, last 14 days; Returns from a 211-day break; First run over hurdles in our data
- Railwayview Lady (hrs_53993912) | 4yo F | 161lb | OR - | draw 0 | jockey Keith Donoghue | trainer Gavin Cromwell (14d 4/39) | headgear - | last run 34 days | form 5 | MARKET 4.8% | 09:00 median 15.00 | Matchbook 14.50
    DATA: model 7.2% | style Held up (led 3% of runs) | runs in data 5 | last 3: 28 Jun Curragh Flat 12f Good 9/13; 10 Sep Doncaster Flat 11.9f Good To Soft 6/9; 23 Oct Sligo (IRE) Hurdle 17.5f Yielding 5/13 fig 96
    DATA for: Best recent form figure 96, 8 lb above field average
- Wungudi (hrs_43164597) | 5yo M | 153lb | OR - | draw 0 | jockey  | trainer David Kenneth Budds (14d 1/3) | headgear ht (1st time) | last run 49 days | form /- | MARKET 4.6% | 09:00 median 67.00 | Matchbook 9.80
    DATA: model 2.6% | style Unknown | runs in data 2 | last 3: 5 Aug Sligo Flat 13.3f Yielding 11/14; 8 Oct Thurles Flat 12.7f Yielding 4/14
    DATA for: Last-run finishing speed +3.5% vs that field (finished strongly); First-time headgear
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; First run over hurdles in our data
- Born Believing (hrs_59429475) | 5yo M | 161lb | OR - | draw 0 | jockey Mr D O'Sullivan(7) | trainer Ms Claire O'Connell (14d 1/3) | headgear t | last run 52 days | form 115-53 | MARKET 3.8% | 09:00 median 19.00 | Matchbook 19.00
    DATA: model 11.7% | style Prominent (led 3% of runs) | runs in data 4 | last 3: 29 Apr Punchestown NH Flat 16.6f Yielding 5/16; 28 Sep Roscommon Hurdle 20.2f Good To Yielding 5/15; 5 Oct Fairyhouse Hurdle 20f Good 3/10
    DATA for: Last-run finishing speed +2.9% vs that field (finished strongly); Has won at this trip or further
- Lavender Berry (hrs_65225034) | 4yo F | 153lb | OR - | draw 0 | jockey  | trainer John F Gleeson (14d 0/0) | headgear - | last run 18 days | form 960 | MARKET 2.7% | 09:00 median 21.00 | Matchbook 36.00
    DATA: model 3.0% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 30 May Listowel NH Flat 16.5f Yielding 9/9; 10 Jul Cork NH Flat 16.9f Good 6/16; 8 Nov Naas (IRE) NH Flat 16f Good To Yielding 15/17
    DATA against: Poor recent finishing positions; First run over hurdles in our data
- Jack's Sister (hrs_57942066) | 5yo M | 153lb | OR - | draw 0 | jockey Simon Torrens | trainer Patrick T Foley (14d 0/6) | headgear - | last run 19 days | form 6-4 | MARKET 2.4% | 09:00 median 26.00 | Matchbook 36.00
    DATA: model 2.6% | style Held up (led 8% of runs) | runs in data 2 | last 3: 18 Feb Punchestown Hurdle 20.1f Soft 6/7; 7 Nov Gowran Park (IRE) Hurdle 16f Good To Yielding 4/7 fig 95
    DATA for: Best recent form figure 95, 7 lb above field average
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Race comments mention jumping mistakes in 2 of its last 2 runs
- Rock On Suzie (hrs_17393629869) | 4yo F | 153lb | OR - | draw 0 | jockey Jordan Gainford | trainer Gordon Elliott (14d 11/81) | headgear - | last run 17 days | form 7 | MARKET 2.1% | 09:00 median 26.00 | Matchbook 38.00
    DATA: model 3.1% | style Unknown | runs in data 1 | last 3: 9 Nov Punchestown (IRE) Hurdle 20.5f Good To Yielding 7/11 fig 86
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Earthsong (hrs_46975124) | 4yo F | 161lb | OR - | draw 0 | jockey Sean Flanagan | trainer Denis Gerard Hogan (14d 0/14) | headgear - | last run 45 days | form - | MARKET 1.9% | 09:00 median 51.00 | Matchbook 34.00
    DATA: model 5.3% | style Midfield (led 23% of runs) | runs in data 5 | last 3: 20 May Gowran Park Flat 13.8f Good To Yielding 1/13; 22 Jun Ballinrobe Flat 13f Yielding 8/8; 12 Oct Roscommon Flat 12.2f Soft 14/16
    DATA against: Trainer 0 wins from 14 runs, last 14 days; First run over hurdles in our data
- Saoirses Choice (hrs_64780996) | 6yo M | 153lb | OR - | draw 0 | jockey Alix Balfe(7) | trainer Francis Casey (14d 0/1) | headgear t (1st time) | last run 47 days | form 499U | MARKET 1.8% | 09:00 median 81.00 | Matchbook 25.00
    DATA: model 1.2% | style Held up (led 3% of runs) | runs in data 5 | last 3: 6 Aug Sligo Hurdle 17.9f Good 9/13; 28 Aug Down Royal Hurdle 17.4f Good UR/10; 10 Oct Naas Flat 7f Soft 10/11
    DATA for: First-time headgear
    DATA against: Poor recent finishing positions; Fell or unseated in 1 of its last 2 jumps runs
- Eleen Alana (hrs_66463411) | 5yo M | 153lb | OR - | draw 0 | jockey Michael Kenneally(3) | trainer Eoin Griffin (14d 0/2) | headgear - | last run 47 days | form 3077 | MARKET 1.6% | 09:00 median 41.00 | Matchbook 46.00
    DATA: model 3.0% | style Prominent (led 3% of runs) | runs in data 4 | last 3: 1 Aug Galway NH Flat 16.8f Good To Yielding 14/18; 18 Sep Downpatrick NH Flat 17.8f Good 7/12; 10 Oct Fairyhouse NH Flat 16f Good 7/10
    DATA against: Poor recent finishing positions; First run over hurdles in our data
- Easter Snow (hrs_17395220444) | 4yo F | 153lb | OR - | draw 0 | jockey Philip Donovan | trainer Denis Gerard Hogan (14d 0/14) | headgear - | last run 17 days | form 74-48 | MARKET 1.5% | 09:00 median 101.00 | Matchbook 10.00
    DATA: model 1.3% | style Held up (led 8% of runs) | runs in data 1 | last 3: 9 Nov Punchestown (IRE) Hurdle 20.5f Good To Yielding 8/11 fig 82
    DATA against: Best recent form figure 82, 6 lb below field average; Trainer 0 wins from 14 runs, last 14 days; Last-run finishing speed -3.4% vs that field (faded); Lightly raced: 1 run in our data, so the model has little to go on
- Meenvee (hrs_17392980080) | 4yo F | 153lb | OR - | draw 0 | jockey J. J. Slevin | trainer John Patrick Ryan (14d 0/5) | headgear - | last run 19 days | form 6 | MARKET 1.5% | 09:00 median 101.00 | Matchbook 9.80
    DATA: model 1.1% | style Held up (led 8% of runs) | runs in data 1 | last 3: 7 Nov Gowran Park (IRE) Hurdle 16f Good To Yielding 6/7 fig 88
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Jimjohn Kittkath (hrs_17393224142) | 4yo F | 153lb | OR - | draw 0 | jockey Mike O'Connor | trainer Conor Houlihan (14d 0/2) | headgear ht | last run 53 days | form 6 | MARKET 1.3% | 09:00 median 101.00 | Matchbook 25.00
    DATA: model 1.6% | style Held up (led 8% of runs) | runs in data 1 | last 3: 4 Oct Killarney Hurdle 17f Good 6/8
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Potters Queen (hrs_17394784470) | 5yo M | 153lb | OR - | draw 0 | jockey Phillip Enright | trainer G Mangan (14d 0/1) | headgear ht | last run 14 days | form 3P-P4 | MARKET 1.1% | 09:00 median 51.00 | Matchbook 160.00
    DATA: model 1.5% | style Leader (led 57% of runs) | runs in data 2 | last 3: 1 Nov Cork (IRE) Hurdle 16f Good To Yielding PU/19; 12 Nov Thurles (IRE) Hurdle 20f Good 4/11 fig 82
    DATA for: Pace: may get an uncontested lead
    DATA against: Best recent form figure 82, 6 lb below field average; Lightly raced: 2 runs in our data, so the model has little to go on; Pulled up in 1 of its last 2 jumps runs
- Cracker's Diamond (hrs_17395529172) | 5yo M | 153lb | OR - | draw 0 | jockey Liam Quinlan | trainer Ray Hackett (14d 0/5) | headgear - | last run - days | form - | MARKET 0.9% | 09:00 median 67.00 | Matchbook 70.00
    DATA: model 2.7% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Bambi Fever (hrs_17389189818) | 5yo M | 153lb | OR - | draw 0 | jockey John Shinnick | trainer Timothy Townend (14d 0/0) | headgear - | last run 44 days | form 828 | MARKET 0.8% | 09:00 median 67.00 | Matchbook 160.00
    DATA: model 5.1% | style Held up (led 4% of runs) | runs in data 3 | last 3: 23 Jul Wexford NH Flat 16.7f Good 8/14; 3 Sep Kilbeggan NH Flat 19f Good To Yielding 2/10; 13 Oct Punchestown NH Flat 16.2f Good 8/14
    DATA against: First run over hurdles in our data
- An Ceanabhan Ban (hrs_17395148477) | 5yo M | 153lb | OR - | draw 0 | jockey John Aherne(7) | trainer Lawrence Walshe (14d 0/0) | headgear - | last run 18 days | form 0 | MARKET 0.6% | 09:00 median 126.00 | Matchbook 95.00
    DATA: model 0.8% | style Unknown | runs in data 1 | last 3: 8 Nov Naas (IRE) Hurdle 16f Good To Yielding 12/12
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Daddy's Cupcake (hrs_17395530215) | 5yo M | 153lb | OR - | draw 0 | jockey Cian Quirke | trainer Ray Hackett (14d 0/5) | headgear - | last run 4 days | form R | MARKET 0.6% | 09:00 median 126.00 | Matchbook 110.00
    DATA: model 1.4% | style Held up (led 8% of runs) | runs in data 1 | last 3: 22 Nov Cork (IRE) Hurdle 17f Soft RO/15
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on; Fell or unseated in 1 of its last 1 jumps runs

## 3:06 Thurles | race_id rac_32305556608 | Racing Here Again On 3rd December Maiden Hurdle
Hurdle |  | 2m0f11y | going Good | Turf | 18 runners | rating band - | age 4yo
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Moment Of Grace (hrs_17395958888) | 4yo G | 153lb | OR - | draw 0 | jockey Paul Townend | trainer Mr W. P. Mullins (14d 12/49) | headgear - | last run 390 days | form 2- | MARKET 27.1% | 09:00 median 3.00 | Matchbook 3.00 | CHECK (skip line 2.85)
    DATA: model 3.8% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 24% wins (12/49), last 14 days
    DATA against: Returns from a 390-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Werner (hrs_17395145348) | 4yo G | 161lb | OR - | draw 0 | jockey Jack Kennedy | trainer Gordon Elliott (14d 11/81) | headgear - | last run 17 days | form 2 | MARKET 16.9% | 09:00 median 3.50 | Matchbook 7.20
    DATA: model 16.9% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 9 Nov Punchestown (IRE) Hurdle 16f Good To Yielding 2/10 fig 116
    DATA for: Best recent form figure 116, 17 lb above field average; Last-run finishing speed +3.8% vs that field (finished strongly)
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Malte De Solzen (hrs_60089946) | 4yo G | 161lb | OR - | draw 0 | jockey J. J. Slevin | trainer Joseph Patrick O'Brien (14d 4/35) | headgear - | last run 337 days | form 22- | MARKET 14.7% | 09:00 median 4.50 | Matchbook 7.40
    DATA: model 4.3% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 337-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Red Seagull (hrs_62645324) | 4yo G | 153lb | OR - | draw 0 | jockey Daniel King | trainer N Stokes (14d 1/1) | headgear - | last run 21 days | form 26-2 | MARKET 14.2% | 09:00 median 5.50 | Matchbook 5.90
    DATA: model 9.4% | style Prominent (led 4% of runs) | runs in data 3 | last 3: 19 Mar Cork Hurdle 17.1f Yielding 2/14; 28 Apr Punchestown NH Flat 16.6f Yielding 6/18; 5 Nov Clonmel (IRE) NH Flat 16.5f Good 2/12 fig 98
    DATA for: Good recent finishing positions
- Apache Peak (hrs_57654457) | 4yo G | 153lb | OR - | draw 0 | jockey Conor Stone-Walsh | trainer Ross O'Sullivan (14d 0/17) | headgear - | last run 43 days | form 2223-4 | MARKET 10.4% | 09:00 median 6.50 | Matchbook 9.20
    DATA: model 11.7% | style Midfield (led 3% of runs) | runs in data 4 | last 3: 7 Feb Naas NH Flat 15.7f Soft To Heavy 2/5; 22 Mar Limerick NH Flat 16.2f Soft To Heavy 3/7; 14 Oct Punchestown (IRE) Hurdle 16.5f Good 4/15 fig 98
    DATA for: Good recent finishing positions
    DATA against: Trainer 0 wins from 17 runs, last 14 days
- Abando (hrs_52417876) | 4yo G | 153lb | OR 104 | draw 0 | jockey James Smith(3) | trainer A. McCann (14d 0/4) | headgear p | last run 26 days | form 342 | MARKET 3.9% | 09:00 median 17.00 | Matchbook 26.00
    DATA: model 13.0% | style Prominent (led 23% of runs) | runs in data 8 | last 3: 28 Sep Roscommon Hurdle 15.6f Good To Yielding 3/13; 5 Oct Fairyhouse Hurdle 16f Good 4/11; 31 Oct Down Royal (IRE) Hurdle 17f Good 2/12
    DATA for: Good recent finishing positions
    DATA against: Race comments mention jumping mistakes in 2 of its last 3 runs
- Sonic Invader (hrs_50875342) | 4yo G | 153lb | OR - | draw 0 | jockey Donagh Meyler | trainer Noel Meade (14d 3/15) | headgear - | last run 112 days | form - | MARKET 2.0% | 09:00 median 41.00 | Matchbook 55.00
    DATA: model 7.0% | style Prominent (led 23% of runs) | runs in data 5 | last 3: 31 May Listowel Flat 16.2f Good 3/11; 15 Jul Killarney Flat 14.4f Good 7/11; 6 Aug Leopardstown Flat 9f Good 17/22
    DATA for: Trainer 20% wins (3/15), last 14 days
    DATA against: Returns from a 112-day break; First run over hurdles in our data
- Gregwell (hrs_64522822) | 4yo G | 153lb | OR - | draw 0 | jockey Tiernan Power Roche | trainer P. J. Rothwell (14d 0/33) | headgear - | last run 22 days | form 5 | MARKET 1.3% | 09:00 median 41.00 | Matchbook 120.00
    DATA: model 2.4% | style Unknown | runs in data 1 | last 3: 4 Nov Wexford (IRE) Hurdle 16.5f Yielding 5/14 fig 90
    DATA against: Best recent form figure 90, 9 lb below field average; Trainer 0 wins from 33 runs, last 14 days; Lightly raced: 1 run in our data, so the model has little to go on
- Getinthekew (hrs_17396014167) | 4yo G | 153lb | OR - | draw 0 | jockey Harry Sexton(7) | trainer E Sheehy (14d 0/2) | headgear - | last run 18 days | form 7U-78 | MARKET 1.2% | 09:00 median 101.00 | Matchbook 80.00
    DATA: model 3.8% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Sea Senor (hrs_46013597) | 4yo G | 153lb | OR - | draw 0 | jockey Kevin Healy(7) | trainer Ciaran Murphy (14d 0/5) | headgear h | last run 581 days | form - | MARKET 1.1% | 09:00 median 51.00 | Matchbook 140.00
    DATA: model 3.8% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 581-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Smithfield (hrs_55484443) | 4yo G | 153lb | OR - | draw 0 | jockey Sean O'Keeffe | trainer L Young (14d 0/1) | headgear h | last run 7 days | form 8 | MARKET 1.1% | 09:00 median 101.00 | Matchbook 90.00
    DATA: model 2.4% | style Prominent (led 4% of runs) | runs in data 6 | last 3: 3 Jul Bellewstown Flat 7.9f Good 9/15; 15 Oct Curragh (IRE) Flat 7f Soft 20/20; 19 Nov Thurles (IRE) Hurdle 16f Good 8/12 fig 91
    DATA against: Best recent form figure 91, 8 lb below field average; Poor recent finishing positions
- In Gusto (hrs_17395863975) | 4yo G | 153lb | OR - | draw 0 | jockey Philip Donovan | trainer Gerard Edmund O'Leary (14d 0/1) | headgear - | last run - days | form - | MARKET 1.0% | 09:00 median 67.00 | Matchbook 120.00
    DATA: model 3.8% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Mambo Du Large (hrs_64554315) | 4yo G | 153lb | OR 89 | draw 0 | jockey Gavin Brouder | trainer M K Flannery (14d 0/1) | headgear t | last run 25 days | form 7060PP | MARKET 1.0% | 09:00 median 126.00 | Matchbook 80.00
    DATA: model 3.9% | style Midfield (led 3% of runs) | runs in data 4 | last 3: 2 Jul Limerick Hurdle 20f Good 13/18; 10 Jul Cork Hurdle 17.3f Good 6/14; 3 Aug Cork Hurdle 17f Good 14/16
    DATA against: Last-run finishing speed -9.1% vs that field (faded); Poor recent finishing positions
- Pencil Hill (hrs_17394489301) | 4yo F | 146lb | OR - | draw 0 | jockey Alan O'Sullivan(5) | trainer L J Archdeacon (14d 0/1) | headgear - | last run - days | form - | MARKET 1.0% | 09:00 median 67.00 | Matchbook 150.00
    DATA: model 3.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Carey's Dream (hrs_17395528129) | 4yo F | 146lb | OR - | draw 0 | jockey Mike O'Connor | trainer Gillian Scott (14d 0/1) | headgear - | last run - days | form - | MARKET 0.8% | 09:00 median 67.00 | Matchbook 200.00
    DATA: model 3.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- A Bitta Craic (hrs_17396013124) | 4yo F | 146lb | OR - | draw 0 | jockey G B Noonan | trainer Eoin Christopher McCarthy (14d 0/4) | headgear - | last run - days | form - | MARKET 0.8% | 09:00 median 81.00 | Matchbook 180.00
    DATA: model 3.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Haydens Star (hrs_63171696) | 4yo G | 153lb | OR - | draw 0 | jockey Ricky Doyle | trainer Eamon Courtney (14d 0/1) | headgear - | last run 238 days | form 6- | MARKET 0.7% | 09:00 median 81.00 | Matchbook 200.00
    DATA: model 1.7% | style Held up (led 8% of runs) | runs in data 1 | last 3: 2 Apr Clonmel Hurdle 15.9f Soft 6/7
    DATA against: Last-run finishing speed -5.4% vs that field (faded); Returns from a 238-day break; Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Morris From Mayo (hrs_17393384764) | 4yo G | 153lb | OR - | draw 0 | jockey Danny Mullins | trainer R Donohoe (14d 1/4) | headgear - | last run 19 days | form 88 | MARKET 0.6% | 09:00 median 151.00 | Matchbook 190.00
    DATA: model 1.5% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 6 Oct Galway NH Flat 16.6f Yielding To Soft 8/8; 7 Nov Gowran Park (IRE) Hurdle 16f Good To Yielding 8/12
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on

## 3:39 Thurles | race_id rac_32305558545 | William Hill Challenge Series Mares Handicap Hurdle
Hurdle |  | 2m0f11y | going Good | Turf | 21 runners | rating band 0-100 | age 3yo+
DATA pace: Even - Two likely leaders (Nirisque, Andyourbirdcansing). A fair, even gallop is most likely.
- Might Be The One (hrs_50412635) | 5yo M | 165lb | OR 97 | draw 0 | jockey Kevin Healy(7) | trainer Andrew McNamara (14d 0/0) | headgear t | last run 14 days | form 22-141 | MARKET 18.4% | 09:00 median 4.00 | Matchbook 3.95 | CHECK (skip line 3.80)
    comment: Won last time out and again three starts back, with a fourth two starts back the only blemish in a consistent run, and she's fresh from a 14-day turnaround having run over today's trip and going before. The main risk is the 165 lb she must carry off an official mark of 97.
    DATA: model 13.8% | style Prominent (led 3% of runs) | runs in data 7 | last 3: 18 Sep Downpatrick Hurdle 17.8f Good 1/12; 10 Oct Fairyhouse Hurdle 16f Good 4/9; 12 Nov Thurles (IRE) Chase 18f Good 1/10 fig 100
    DATA for: Best recent form figure 100, 19 lb above field average; Official rating 97, 10 lb above field average; Last-run finishing speed +3.6% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Carries 10 lb more than average
- Cosmic Front (hrs_412652261) | 5yo M | 163lb | OR 95 | draw 0 | jockey Paul Townend | trainer Mr W. P. Mullins (14d 12/49) | headgear - | last run 25 days | form 689 | MARKET 15.6% | 09:00 median 3.50 | Matchbook 6.00
    comment: Cosmic Front has been heading the wrong way, with a sixth three starts back followed by an eighth and then a ninth last time out, though she has run over today's trip and going and returns after 25 days.
    DATA: model 4.3% | style Prominent (led 4% of runs) | runs in data 3 | last 3: 28 Aug Down Royal Hurdle 17.4f Good 6/10; 2 Oct Gowran Park Hurdle 16.4f Good 8/20; 1 Nov Cork (IRE) Hurdle 16f Good To Yielding 9/19
    DATA for: Official rating 95, 8 lb above field average; Trainer 24% wins (12/49), last 14 days
    DATA against: Poor recent finishing positions; Carries 8 lb more than average
- Bowgate Street (hrs_34153483) | 7yo M | 160lb | OR 92 | draw 0 | jockey Philip Donovan | trainer M Flannery (14d 0/0) | headgear t | last run 14 days | form 330322 | MARKET 8.4% | 09:00 median 7.50 | Matchbook 10.00
    comment: Bowgate Street arrives in fine heart, second last time out and a second two starts back, and she has run over today's trip and going before, but she is still yet to win in her last six outings.
    DATA: model 8.5% | style Midfield (led 4% of runs) | runs in data 13 | last 3: 6 Oct Galway Hurdle 16.6f Yielding To Soft 3/11; 23 Oct Sligo (IRE) Hurdle 17.5f Yielding 2/13 fig 93; 12 Nov Thurles (IRE) Hurdle 16f Good 2/17 fig 96
    DATA for: Best recent form figure 96, 15 lb above field average; Recent figures 4 lb above its current mark (looks well handicapped); Has won at this trip or further; Good recent finishing positions
- Arctic Piper (hrs_40669041) | 7yo M | 151lb | OR 83 | draw 0 | jockey Michael Kenneally(3) | trainer R Donohoe (14d 1/4) | headgear - | last run 14 days | form F90936 | MARKET 7.3% | 09:00 median 10.00 | Matchbook 10.00
    comment: Arctic Piper is winless in her last six, though a third two starts back and a sixth last time out show she's in decent shape, and she's fresh from a 14-day break and has run over today's trip and going.
    DATA: model 4.5% | style Prominent (led 23% of runs) | runs in data 7 | last 3: 2 Oct Gowran Park Hurdle 20.2f Good 9/13; 13 Oct Punchestown Hurdle 16.2f Good 3/11; 12 Nov Thurles (IRE) Hurdle 16f Good 6/16 fig 82
    DATA against: Race comments mention jumping mistakes in 2 of its last 5 runs
- Dusky Night (hrs_17391808791) | 5yo M | 157lb | OR 89 | draw 0 | jockey Shane O'Callaghan(3) | trainer Ross O'Sullivan (14d 0/17) | headgear - | last run 23 days | form 3-6824 | MARKET 6.3% | 09:00 median 11.00 | Matchbook 12.50
    comment: Dusky Night comes here fourth last time out, with a second two starts back, and has run over today's trip and going, though she's winless in her last five and a 157 lb burden looks a hurdle to climbing higher.
    DATA: model 6.0% | style Held up (led 3% of runs) | runs in data 4 | last 3: 28 Sep Roscommon Hurdle 20.2f Good To Yielding 8/15; 8 Oct Tramore Hurdle 16f Yielding 2/8; 3 Nov Fairyhouse (IRE) Hurdle 20f Good To Yielding 4/15 fig 89
    DATA for: Best recent form figure 89, 8 lb above field average
    DATA against: Trainer 0 wins from 17 runs, last 14 days
- Talas Kera (hrs_55061601) | 5yo M | 160lb | OR 92 | draw 0 | jockey  | trainer John G Carr (14d 0/4) | headgear - | last run 2 days | form 404210 | MARKET 5.4% | 09:00 median 11.00 | Matchbook 18.00
    comment: Talas Kera won two starts back and was second three starts back, but she was unplaced last time out and returns just two days later, which is a quick turnaround.
    DATA: model 9.0% | style Midfield (led 3% of runs) | runs in data 10 | last 3: 2 Oct Gowran Park Hurdle 20.2f Good 2/13; 7 Nov Gowran Park (IRE) Hurdle 20f Good To Yielding 1/13 fig 87; 24 Nov Tramore (IRE) Hurdle 21f Soft To Heavy 13/15
    DATA for: Best recent form figure 87, 6 lb above field average; Has won at this trip or further; Good recent finishing positions
- Doyen Og (hrs_40225346) | 7yo M | 140lb | OR 72 | draw 0 | jockey Harry Sexton(7) | trainer Adrian Sexton (14d 0/1) | headgear - | last run 19 days | form 74753F | MARKET 5.0% | 09:00 median 12.00 | Matchbook 18.00
    comment: Doyen Og is winless in her last six, and having fallen last time out after a third two starts back, she is hard to fancy on form that has mostly been mid-division or worse.
    DATA: model 4.0% | style Prominent (led 3% of runs) | runs in data 9 | last 3: 9 Oct Downpatrick Hurdle 21.8f Good 5/14; 17 Oct Limerick (IRE) Hurdle 21.5f Good To Yielding 3/16 fig 72; 7 Nov Gowran Park (IRE) Hurdle 20f Good To Yielding F/14
    DATA for: Carries 15 lb less than average
    DATA against: Best recent form figure 72, 9 lb below field average; Official rating 72, 15 lb below field average; Fell or unseated in 1 of its last 5 jumps runs
- La Tulipe Noire (hrs_31480344) | 6yo M | 148lb | OR 80 | draw 0 | jockey Ethan O'Sullivan(7) | trainer Aengus King (14d 0/2) | headgear p | last run 9 days | form P8-F03 | MARKET 4.1% | 09:00 median 15.00 | Matchbook 21.00
    comment: Winless in her last five, La Tulipe Noire has been patchy, with a fell and a pulled up in that spell, though she was third last time out, just nine days ago.
    DATA: model 2.2% | style Held up (led 3% of runs) | runs in data 13 | last 3: 29 Oct Punchestown (IRE) Flat 7f Yielding 6/12 fig 55; 12 Nov Thurles (IRE) Hurdle 16f Good 13/17 fig 74; 17 Nov Limerick (IRE) Hurdle 16f Heavy 3/9 fig 77
    DATA for: Carries 7 lb less than average
    DATA against: Official rating 80, 7 lb below field average; Fell or unseated in 1 of its last 3 jumps runs
- Walk On Annilog (hrs_48259442) | 7yo M | 160lb | OR 92 | draw 0 | jockey Brian Barry(7) | trainer Riceal Dunne (14d 0/1) | headgear h | last run 14 days | form 0-4807 | MARKET 3.8% | 09:00 median 19.00 | Matchbook 22.00
    comment: She has run over today's trip and going, is fresh enough after 14 days, and carries 160 lb.
    DATA: model 4.6% | style Prominent (led 23% of runs) | runs in data 6 | last 3: 27 May Wexford Hurdle 17f Good To Yielding 8/14; 6 Jul Roscommon Hurdle 15.9f Good 12/16; 12 Nov Thurles (IRE) Hurdle 16f Good 7/17 fig 91
    DATA for: Best recent form figure 91, 10 lb above field average
    DATA against: Poor recent finishing positions
- Powerful Rosie (hrs_57654569) | 4yo F | 153lb | OR 85 | draw 0 | jockey Alan O'Sullivan(5) | trainer Liz Doyle (14d 0/2) | headgear - | last run 206 days | form 0056-8 | MARKET 3.2% | 09:00 median 23.00 | Matchbook 24.00
    comment: Powerful Rosie is winless in her last five, finishing eighth last time out and a sixth two starts back, and returns after 206 days off, so she is hard to fancy under 153 lb.
    DATA: model 3.4% | style Held up (led 3% of runs) | runs in data 6 | last 3: 17 Mar Wexford Hurdle 16f Soft 5/14; 2 Apr Clonmel Hurdle 15.9f Soft 6/16; 4 May Down Royal Hurdle 17.4f Good 8/20
    DATA against: Returns from a 206-day break
- Sylkie (hrs_37288902) | 5yo M | 160lb | OR 92 | draw 0 | jockey Cian Quirke | trainer Daniel John Howard (14d 0/1) | headgear - | last run 28 days | form 099- | MARKET 3.2% | 09:00 median 19.00 | Matchbook 28.00
    comment: Lightly raced and yet to win, Sylkie has finished ninth in her last two outings, and unplaced three starts back, so she looks unexposed with scope for improvement. She returns after 28 days off, carrying 160 lb off an official mark of 92.
    DATA: model 6.0% | style Midfield (led 3% of runs) | runs in data 7 | last 3: 8 Sep Galway Flat 12f Soft 11/15; 11 Oct Naas Flat 10.7f Soft 7/12; 29 Oct Punchestown (IRE) Flat 8f Yielding 2/14 fig 61
    DATA for: Last-run finishing speed +2.4% vs that field (finished strongly)
- Mercurial Sea (hrs_49609049) | 5yo M | 159lb | OR 91 | draw 0 | jockey Carl Millar(5) | trainer Nigel Thomas Slevin (14d 0/5) | headgear - | last run 9 days | form 28285P | MARKET 2.5% | 09:00 median 26.00 | Matchbook 34.00
    comment: Mercurial Sea was pulled up last time out and is winless in her last six, though she was second four and six starts back, and she has run over today's trip and going before.
    DATA: model 8.0% | style Midfield (led 4% of runs) | runs in data 8 | last 3: 14 Aug Tramore Chase 21.8f Good 8/13; 18 Sep Downpatrick Hurdle 17.8f Good 5/12; 17 Nov Limerick (IRE) Hurdle 16f Heavy PU/9
    DATA against: Race comments mention jumping mistakes in 2 of its last 5 runs; Pulled up in 1 of its last 5 jumps runs
- Our Girl Ellie (hrs_45445260) | 6yo M | 155lb | OR 87 | draw 0 | jockey  | trainer Stephen Ryan (14d 0/1) | headgear t | last run 7 days | form -00930 | MARKET 2.5% | 09:00 median 26.00 | Matchbook 36.00
    DATA: model 2.7% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 11 Oct Cork Hurdle 18.9f Good 9/14; 17 Oct Limerick (IRE) Hurdle 17f Good To Yielding 3/15 fig 83; 19 Nov Thurles (IRE) Hurdle 20f Good 11/13 fig 73
    DATA against: Last-run finishing speed -5.5% vs that field (faded)
- Andyourbirdcansing (hrs_35828023) | 8yo M | 157lb | OR 89 | draw 0 | jockey Conor Smithers(7) | trainer John Patrick Ryan (14d 0/5) | headgear - | last run 23 days | form 100177 | MARKET 2.4% | 09:00 median 26.00 | Matchbook 34.00
    comment: Andyourbirdcansing has won twice in her last six starts, a first three starts back and another six starts back, but she has finished seventh in her last two runs.
    DATA: model 4.4% | style Leader (led 29% of runs) | runs in data 9 | last 3: 30 Sep Sligo Chase 21f Good 1/15; 23 Oct Sligo (IRE) Hurdle 17.5f Yielding 7/13; 3 Nov Fairyhouse (IRE) Chase 24.5f Good To Yielding 7/7 fig 82
    DATA for: Has won at this trip or further
    DATA against: Recent figures 7 lb below its current mark (looks high in the weights); Last-run finishing speed -3.4% vs that field (faded)
- Avandra (hrs_40393444) | 6yo M | 140lb | OR 72 | draw 0 | jockey  | trainer P. J. Rothwell (14d 0/33) | headgear b | last run 7 days | form 340700 | MARKET 2.2% | 09:00 median 29.00 | Matchbook 40.00
    comment: Avandra has been unplaced last time out and two starts back, and she is winless in her last six, with a seventh three starts back her best finish since a fourth five starts back. Back in just seven days, with a yard 0/33 lately and 140 lb to carry, she is hard to fancy, though she has run over today's trip and going.
    DATA: model 2.8% | style Held up (led 8% of runs) | runs in data 12 | last 3: 28 Sep Roscommon Hurdle 15.6f Good To Yielding 7/16; 7 Nov Gowran Park (IRE) Hurdle 20f Good To Yielding 11/14; 19 Nov Thurles (IRE) Hurdle 16f Good 10/17 fig 53
    DATA for: Carries 15 lb less than average
    DATA against: Best recent form figure 53, 28 lb below field average; Recent figures 19 lb below its current mark (looks high in the weights); Official rating 72, 15 lb below field average; Trainer 0 wins from 33 runs, last 14 days; Last-run finishing speed -2.8% vs that field (faded); Poor recent finishing positions; Race comments mention jumping mistakes in 2 of its last 5 runs
- Nirisque (hrs_51800182) | 5yo M | 168lb | OR 100 | draw 0 | jockey Mike O'Connor | trainer Henry de Bromhead (14d 8/42) | headgear tp (1st time) | last run 35 days | form 02-65P | MARKET 2.1% | 09:00 median 34.00 | Matchbook 40.00
    comment: The risk is a pulled-up effort last time out, plus a hefty 168 lb after 35 days off.
    DATA: model 5.4% | style Leader (led 43% of runs) | runs in data 4 | last 3: 14 May Clonmel Hurdle 16.7f Good To Yielding 6/18; 18 Sep Downpatrick Hurdle 17.8f Good 5/15; 22 Oct Clonmel (IRE) Hurdle 20f Good To Yielding PU/13
    DATA for: Official rating 100, 13 lb above field average; First-time headgear
    DATA against: Carries 13 lb more than average; Pulled up in 1 of its last 4 jumps runs
- Thegooseiscooked (hrs_26460056) | 9yo M | 146lb | OR 78 | draw 0 | jockey Daniel King | trainer Gerard Keane (14d 0/6) | headgear - | last run 14 days | form 00/F-9 | MARKET 2.0% | 09:00 median 29.00 | Matchbook 44.00
    comment: Thegooseiscooked is winless in her last four, with a ninth last time out, a fall two starts back and unplaced efforts before that, so she is hard to fancy at 146 lb.
    DATA: model 2.4% | style Midfield (led 4% of runs) | runs in data 9 | last 3: 12 Oct Roscommon Flat 12.2f Soft 13/16; 21 Oct Navan (IRE) Flat 14f Yielding 14/23 fig 26; 12 Nov Thurles (IRE) Hurdle 16f Good 9/17 fig 74
    DATA for: Carries 9 lb less than average
    DATA against: Best recent form figure 74, 7 lb below field average; Official rating 78, 9 lb below field average; Poor recent finishing positions; Aged 9, older than most of this field
- Shesakindofmagic (hrs_37790102) | 8yo M | 168lb | OR 100 | draw 0 | jockey Luke Carberry(7) | trainer A. McCann (14d 0/4) | headgear t | last run 180 days | form 275-7P | MARKET 1.9% | 09:00 median 34.00 | Matchbook 48.00
    comment: Shesakindofmagic is yet to win in her last five starts and was pulled up last time, but a second five starts back shows her ability, and she has run over today's trip and going.
    DATA: model 5.2% | style Prominent (led 3% of runs) | runs in data 5 | last 3: 4 Apr Fairyhouse Hurdle 16f Yielding To Soft 5/16; 10 May Cork Hurdle 19.2f Good 7/15; 30 May Listowel Hurdle 23.5f Yielding PU/10
    DATA for: Official rating 100, 13 lb above field average
    DATA against: Carries 13 lb more than average; Returns from a 180-day break; Pulled up in 1 of its last 5 jumps runs
- Cool As A Cat (hrs_62645618) | 6yo M | 152lb | OR 84 | draw 0 | jockey Conor Stone-Walsh | trainer Tom Dreaper (14d 0/1) | headgear - | last run 16 days | form U-909 | MARKET 1.8% | 09:00 median 34.00 | Matchbook 60.00
    comment: Cool As A Cat is winless in her last four, finishing ninth last time out, unplaced two starts back, ninth three starts back and unseating four starts back, so she is hard to fancy.
    DATA: model 1.0% | style Held up (led 3% of runs) | runs in data 4 | last 3: 13 May Punchestown Hurdle 16f Good To Yielding 9/16; 6 Jun Punchestown Hurdle 16.5f Good To Yielding 10/24; 10 Nov Fairyhouse (IRE) Hurdle 20.5f Good To Yielding 9/10 fig 64
    DATA against: Best recent form figure 64, 17 lb below field average; Recent figures 20 lb below its current mark (looks high in the weights); Poor recent finishing positions; Race comments mention jumping mistakes in 2 of its last 4 runs; Fell or unseated in 1 of its last 4 jumps runs
- Only A Dollar (hrs_36626940) | 8yo M | 153lb | OR 85 | draw 0 | jockey Danny Power(7) | trainer Sean Aherne (14d 0/2) | headgear h | last run 127 days | form P6-059 | MARKET 1.5% | 09:00 median 51.00 | Matchbook 55.00
    DATA: model 1.3% | style Held up (led 3% of runs) | runs in data 4 | last 3: 13 May Punchestown Hurdle 16f Good To Yielding 15/18; 30 May Tramore Chase 15.6f Good To Yielding 5/6; 22 Jul Wexford Chase 15.5f Good 9/13
    DATA against: Last-run finishing speed -2.5% vs that field (faded); Returns from a 127-day break
- Keep It Together (hrs_43983842) | 8yo M | 142lb | OR 74 | draw 0 | jockey Benjamin P Kennedy(7) | trainer D Buckley (14d 0/2) | headgear - | last run 13 days | form F7P-P0 | MARKET 0.8% | 09:00 median 101.00 | Matchbook 120.00
    comment: Lightly raced and yet to win, Keep It Together has an unconvincing profile, with an unplaced effort last time out, two pulled-up runs before that and a seventh four starts back. Back after just 13 days, she's unexposed and open to improvement off 142 lb.
    DATA: model 0.5% | style Prominent (led 29% of runs) | runs in data 7 | last 3: 15 Aug Tramore Flat 12f Good To Yielding 6/10; 1 Sep Gowran Park Flat 8f Yielding 8/8; 13 Nov Dundalk (AW) (IRE) Flat 12f Standard 14/14 fig 20
    DATA for: Carries 13 lb less than average
    DATA against: Official rating 74, 13 lb below field average; Poor recent finishing positions; Pulled up in 1 of its last 2 jumps runs
