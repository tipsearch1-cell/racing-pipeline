# Card review packet: Dundalk (AW), 2026-11-25

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
{"meeting": "dundalk_aw", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 2:01 Dundalk (AW) | race_id rac_32305477191 | Christmas Party Nights At Dundalk Stadium Handicap
Flat |  | 5f | going Standard | AW | 13 runners | rating band - | age 3yo+
DATA pace: Even - Two likely leaders (Xerling, Genesis). A fair, even gallop is most likely.
- Firewalker (hrs_57315881) | 3yo G | 142lb | OR 92 | draw 13 | jockey Donagh O'Connor | trainer Robson De Aguiar (14d 2/8) | headgear - | last run 12 days | form 940211 | MARKET 22.0% | 09:00 median 3.50 | Matchbook 4.30 | CHECK (skip line 3.32)
    comment: Firewalker arrives in cracking form, a winner last time out and again two starts back, after a second three starts back, and he's fresh enough at 12 days since his last run.
    DATA: model 31.1% | style Unknown | runs in data 6 | last 3: 25 Sep Dundalk Flat 6f Standard 2/13; 16 Oct Dundalk (AW) (IRE) Flat 6f Standard 1/9 fig 81; 13 Nov Dundalk (AW) (IRE) Flat 6f Standard 1/10 fig 91
    DATA for: Best recent form figure 91, 13 lb above field average; Official rating 92, 11 lb above field average; Trainer 25% wins (2/8), last 14 days; Has won at this trip or further; Good recent finishing positions
    DATA against: Carries 11 lb more than average
- Caffu Zafeen (hrs_41876688) | 5yo G | 132lb | OR 82 | draw 3 | jockey Shay Wallace(7) | trainer Paul W Flynn (14d 0/6) | headgear - | last run 12 days | form 511113 | MARKET 15.4% | 09:00 median 5.00 | Matchbook 5.80
    comment: Caffu Zafeen arrives fit after 12 days off, third last time out and a winner four times in his last six starts, so the form is hard to knock, but carrying 132 lb off an official 82 is a stiff ask.
    DATA: model 13.3% | style Prominent (led 8% of runs) | runs in data 11 | last 3: 2 Oct Dundalk Flat 5f Standard 1/12; 4 Nov Dundalk (AW) (IRE) Flat 6f Standard 1/9 fig 75; 13 Nov Dundalk (AW) (IRE) Flat 6f Standard 3/10 fig 80
    DATA for: Has won at this trip or further; Good recent finishing positions
- Chicago Call (hrs_52677394) | 3yo G | 134lb | OR 84 | draw 7 | jockey Ben Coen | trainer J. P. Murtagh (14d 1/8) | headgear - | last run 26 days | form 678044 | MARKET 9.5% | 09:00 median 7.50 | Matchbook 10.00
    comment: Chicago Call comes in off back-to-back fourths, a run of form that has crept up from a sixth and a seventh six and five starts back, and he is fresh after 26 days off.
    DATA: model 6.4% | style Held up (led 5% of runs) | runs in data 7 | last 3: 9 Aug Curragh Flat 5f Good To Firm 11/12; 2 Oct Dundalk Flat 5f Standard 4/8; 30 Oct Dundalk (AW) (IRE) Flat 6f Standard 4/8 fig 82
- Eclairage (hrs_412692728) | 4yo F | 133lb | OR 83 | draw 5 | jockey Colin Keane | trainer Daniel James Murphy (14d 1/5) | headgear t | last run 33 days | form 702060 | MARKET 9.4% | 09:00 median 8.50 | Matchbook 10.00
    comment: The risk is a winless last six, with nothing better than a sixth in her last three outings.
    DATA: model 2.5% | style Unknown | runs in data 8 | last 3: 24 Jul Cork Flat 5f Good To Firm 10/11; 2 Oct Dundalk Flat 5f Standard 6/8; 23 Oct Dundalk (AW) (IRE) Flat 5f Standard 11/13 fig 75
    DATA for: Trainer 20% wins (1/5), last 14 days
    DATA against: Recent figures 8 lb below its current mark (looks high in the weights); Poor recent finishing positions
- Coincidental Glory (hrs_54842501) | 3yo G | 124lb | OR 74 | draw 10 | jockey Camillus Byrne(10) | trainer Adrian McGuinness (14d 2/20) | headgear v | last run 14 days | form 023141 | MARKET 7.9% | 09:00 median 9.00 | Matchbook 13.00
    comment: Won last time out and has two wins in his last six starts, with a fourth two starts back, and he's fresh enough after 14 days, having run over today's trip and going.
    DATA: model 5.1% | style Prominent (led 8% of runs) | runs in data 18 | last 3: 21 Oct Navan (IRE) Flat 6f Yielding 1/21 fig 74; 4 Nov Dundalk (AW) (IRE) Flat 6f Standard 4/9 fig 63; 11 Nov Dundalk (AW) (IRE) Flat 5f Standard 1/13 fig 77
    DATA for: Last-run finishing speed +2.5% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions; Carries 7 lb less than average
    DATA against: Official rating 74, 7 lb below field average
- The Highway Rat (hrs_23324903) | 8yo G | 137lb | OR 87 | draw 4 | jockey J M Sheridan | trainer A Oliver (14d 0/2) | headgear b | last run 24 days | form 905300 | MARKET 7.4% | 09:00 median 11.00 | Matchbook 12.00
    comment: Yet to win in his last six, he has been unplaced in his last two, which is the main risk.
    DATA: model 5.4% | style Prominent (led 3% of runs) | runs in data 10 | last 3: 2 Oct Dundalk Flat 5f Standard 3/8; 15 Oct Curragh (IRE) Flat 6f Soft 10/13 fig 78; 1 Nov Curragh (IRE) Flat 5f Yielding To Soft 10/13 fig 78
    DATA for: Official rating 87, 6 lb above field average
    DATA against: Recent figures 9 lb below its current mark (looks high in the weights); Carries 6 lb more than average; Aged 8, older than most of this field
- Collective Power (hrs_21714882) | 8yo G | 126lb | OR 76 | draw 2 | jockey Patrick McGettigan(5) | trainer Edward Lynam (14d 0/0) | headgear - | last run 21 days | form 253825 | MARKET 6.8% | 09:00 median 12.00 | Matchbook 13.00
    comment: Collective Power was fifth last time out, with a second two starts back, and has had 21 days to recover; he has run over today's trip and going but is yet to win in his last six starts.
    DATA: model 5.4% | style Midfield (led 5% of runs) | runs in data 10 | last 3: 15 Aug Dundalk Flat 6f Standard 8/12; 10 Sep Laytown Flat 6f Standard 2/10; 4 Nov Dundalk (AW) (IRE) Flat 6f Standard 5/9 fig 74
    DATA for: Carries 5 lb less than average
    DATA against: Best recent form figure 74, 4 lb below field average; Official rating 76, 5 lb below field average; Aged 8, older than most of this field
- Genesis (hrs_38465560) | 5yo G | 130lb | OR 80 | draw 1 | jockey Wesley Joyce | trainer Michael Mulvany (14d 0/8) | headgear t | last run 73 days | form 136230 | MARKET 5.7% | 09:00 median 12.00 | Matchbook 18.00
    comment: Genesis showed a solid profile with a third two starts back and a second three starts back, and he has run over today's trip and going, but he was unplaced last time and returns after 73 days off.
    DATA: model 6.9% | style Leader (led 83% of runs) | runs in data 10 | last 3: 9 Aug Curragh Flat 5f Good To Firm 2/12; 22 Aug Curragh Flat 6f Good 3/10; 13 Sep Curragh Flat 6f Yielding 21/24
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Trainer 0 wins from 8 runs, last 14 days; Last-run finishing speed -4.2% vs that field (faded)
- Gerrit's Gem (hrs_37673566) | 6yo G | 123lb | OR 73 | draw 6 | jockey Nathan Crosse | trainer J G Coogan (14d 0/0) | headgear b | last run 24 days | form 340222 | MARKET 5.2% | 09:00 median 15.00 | Matchbook 18.00
    comment: Yet to win in his last six, Gerrit's Gem has been second in each of his last three runs, which is frustrating but shows he's in decent heart after 24 days off.
    DATA: model 7.6% | style Prominent (led 5% of runs) | runs in data 10 | last 3: 10 Oct Naas Flat 5f Soft 2/11; 21 Oct Navan (IRE) Flat 5f Yielding 2/8 fig 75; 1 Nov Curragh (IRE) Flat 5f Yielding To Soft 2/13 fig 76
    DATA for: Good recent finishing positions; Carries 8 lb less than average
    DATA against: Official rating 73, 8 lb below field average
- Kerdos (hrs_32129853) | 6yo G | 144lb | OR 94 | draw 12 | jockey Sam Coen(5) | trainer Stephen Thorne (14d 0/4) | headgear b | last run 12 days | form 019190 | MARKET 3.9% | 09:00 median 21.00 | Matchbook 24.00
    comment: The risk is a recent dip, unplaced last time and a ninth two starts back, under 144 lb from stall 12.
    DATA: model 8.0% | style Held up (led 5% of runs) | runs in data 11 | last 3: 2 Oct Dundalk Flat 5f Standard 1/8; 23 Oct Dundalk (AW) (IRE) Flat 5f Standard 9/13 fig 86; 13 Nov Dundalk (AW) (IRE) Flat 6f Standard 10/10 fig 76
    DATA for: Best recent form figure 86, 8 lb above field average; Official rating 94, 13 lb above field average; Has won at this trip or further
    DATA against: Recent figures 8 lb below its current mark (looks high in the weights); Carries 13 lb more than average
- Cuban Grey (hrs_28533918) | 6yo G | 119lb | OR 69 | draw 11 | jockey Rory Mulligan(5) | trainer Patrick J McKenna (14d 0/0) | headgear - | last run 14 days | form 508808 | MARKET 2.7% | 09:00 median 29.00 | Matchbook 40.00
    comment: Cuban Grey is winless in his last six, finishing eighth last time out and eighth again four starts back, so he is hard to fancy.
    DATA: model 2.5% | style Prominent (led 4% of runs) | runs in data 17 | last 3: 10 Oct Naas Flat 5f Soft 8/11; 15 Oct Curragh (IRE) Flat 5f Soft 15/17 fig 48; 11 Nov Dundalk (AW) (IRE) Flat 5f Standard 8/13 fig 66
    DATA for: Has won at this trip or further; Carries 12 lb less than average
    DATA against: Best recent form figure 66, 12 lb below field average; Official rating 69, 12 lb below field average; Poor recent finishing positions
- Xerling (hrs_54525450) | 3yo F | 135lb | OR 85 | draw 9 | jockey Seamie Heffernan | trainer Miss Natalia Lupini (14d 1/6) | headgear - | last run 54 days | form 212077 | MARKET 2.1% | 09:00 median 26.00 | Matchbook 65.00
    comment: Xerling has been below her best lately, a seventh last time out and another seventh two starts back, though she won five starts back and has run over today's trip and going before.
    DATA: model 4.0% | style Leader (led 23% of runs) | runs in data 6 | last 3: 22 Jul Naas Flat 5.9f Good 13/15; 30 Aug Cork Flat 5f Yielding 7/8; 2 Oct Dundalk Flat 5f Standard 7/8
    DATA for: Has won at this trip or further
    DATA against: Poor recent finishing positions
- Frescobaldi (hrs_51766603) | 3yo G | 128lb | OR 78 | draw 8 | jockey Declan McDonogh | trainer Daniel James Murphy (14d 1/5) | headgear t (1st time) | last run 12 days | form 060059 | MARKET 1.9% | 09:00 median 41.00 | Matchbook 55.00
    comment: Frescobaldi is winless in his last six, beaten into ninth last time out after a fifth two starts back, though he has run over today's trip and going before and returns quickly after just 12 days. Carrying 128 lb from stall 8, he looks a midfield sort on an official mark of 78.
    DATA: model 1.8% | style Held up (led 8% of runs) | runs in data 7 | last 3: 16 Oct Dundalk (AW) (IRE) Flat 7f Standard 11/12 fig 73; 30 Oct Dundalk (AW) (IRE) Flat 6f Standard 5/8 fig 77; 13 Nov Dundalk (AW) (IRE) Flat 6f Standard 9/10 fig 68
    DATA for: Trainer 20% wins (1/5), last 14 days; First-time headgear

## 2:31 Dundalk (AW) | race_id rac_32305479128 | Dundalk Stadium Gift Vouchers Available Online Handicap
Flat |  | 2m | going Standard | AW | 15 runners | rating band 0-60 | age 3yo+
DATA pace: Lone leader - Red Glory is the only habitual front-runner and may be allowed an easy lead.
- Young Churchill (hrs_40260626) | 5yo G | 146lb | OR 57 | draw 12 | jockey Adam Grant(7) | trainer Richard John O'Brien (14d 1/4) | headgear - | last run 5 days | form 370631 | MARKET 25.1% | 09:00 median 2.75 | Matchbook 3.60
    DATA: model 15.5% | style Held up (led 4% of runs) | runs in data 9 | last 3: 26 Sep Listowel Hurdle 20f Good 11/14; 13 Nov Dundalk (AW) (IRE) Flat 12f Standard 3/14 fig 59; 20 Nov Dundalk (AW) (IRE) Flat 12f Standard 1/14 fig 63
    DATA for: Best recent form figure 63, 17 lb above field average; Recent figures 6 lb above its current mark (looks well handicapped); Official rating 57, 9 lb above field average; Last-run finishing speed +4.5% vs that field (finished strongly); Good recent finishing positions
    DATA against: Carries 17 lb more than average
- Red Glory (hrs_22372560) | 8yo G | 142lb | OR 60 | draw 10 | jockey Conor Cusack(7) | trainer Henry de Bromhead (14d 9/43) | headgear tp | last run 25 days | form 95/8-2 | MARKET 12.2% | 09:00 median 6.00 | Matchbook 7.20
    comment: The risk is that he is yet to win and managed only an eighth and a fifth in the two runs before that, so consistency is a question.
    DATA: model 12.3% | style Leader (led 23% of runs) | runs in data 6 | last 3: 26 Aug Bellewstown Hurdle 20.5f Good PU/11; 8 Oct Thurles Flat 12.7f Yielding 2/14; 31 Oct Down Royal (IRE) Hurdle 17f Good 6/12 fig 122
    DATA for: Official rating 60, 12 lb above field average; Trainer 21% wins (9/43), last 14 days; Pace: may get an uncontested lead
    DATA against: Carries 13 lb more than average
- Bhean Saibhre (hrs_35337568) | 5yo M | 129lb | OR 47 | draw 9 | jockey James Ryan | trainer Aidan Anthony Howard (14d 0/1) | headgear t | last run 59 days | form 3-3460 | MARKET 11.2% | 09:00 median 7.00 | Matchbook 7.00
    comment: Bhean Saibhre was third twice earlier in her last five runs but has faded to a sixth two starts back and unplaced last time, returning after 59 days off.
    DATA: model 8.7% | style Prominent (led 3% of runs) | runs in data 9 | last 3: 21 Aug Kilbeggan Hurdle 18.9f Good To Yielding 1/15; 25 Sep Dundalk Flat 12f Standard 6/14; 27 Sep Curragh Flat 10f Heavy 12/18
- Chant d'Or (hrs_54712329) | 4yo G | 122lb | OR 38 | draw 15 | jockey Nathan Crosse | trainer Daniel McLoughlin (14d 1/10) | headgear - | last run 12 days | form 0-7054 | MARKET 9.2% | 09:00 median 8.00 | Matchbook 9.00
    comment: Chant d'Or is winless in his last five, though a fourth last time out and a fifth two starts back show a little improvement, and he returns after just 12 days having run over today's going before. An official mark of 38 is modest, but he looks hard to fancy at 122 lb.
    DATA: model 3.4% | style Midfield (led 4% of runs) | runs in data 4 | last 3: 16 Sep Clonmel Flat 9.8f Yielding 12/14; 25 Sep Dundalk Flat 12f Standard 5/14; 13 Nov Dundalk (AW) (IRE) Flat 12f Standard 4/14 fig 40
    DATA for: Carries 7 lb less than average
    DATA against: Best recent form figure 40, 6 lb below field average; Official rating 38, 10 lb below field average
- Grey Fable (hrs_30017484) | 6yo G | 140lb | OR 58 | draw 4 | jockey Camillus Byrne(10) | trainer Karl Thornton (14d 0/2) | headgear t | last run 5 days | form 542636 | MARKET 7.8% | 09:00 median 8.00 | Matchbook 13.00
    comment: Quick back-up after five days is a minor concern, but Grey Fable has been consistent, with a third two starts back and a second four starts back, and he has run over today's trip and going.
    DATA: model 21.3% | style Prominent (led 4% of runs) | runs in data 12 | last 3: 5 Oct Fairyhouse Hurdle 16f Good 5/11; 4 Nov Musselburgh Flat 12.5f Soft 3/11 fig 62; 20 Nov Dundalk (AW) (IRE) Flat 12f Standard 6/14 fig 55
    DATA for: Best recent form figure 62, 16 lb above field average; Recent figures 4 lb above its current mark (looks well handicapped); Official rating 58, 10 lb above field average
    DATA against: Carries 11 lb more than average
- Duke Otto (hrs_22731436) | 8yo G | 122lb | OR 39 | draw 14 | jockey Robyn Donaghue-Leahy(7) | trainer Patrick J Flynn (14d 2/7) | headgear b | last run 13 days | form 6634-4 | MARKET 7.0% | 09:00 median 9.00 | Matchbook 13.50
    comment: Duke Otto is winless in his last five, though back-to-back fourths last time out and two starts back, plus a third three starts back, show some recent consistency.
    DATA: model 3.4% | style Midfield (led 3% of runs) | runs in data 7 | last 3: 2 Oct Gowran Park Hurdle 20.2f Good 11/20; 1 Nov Cork (IRE) Hurdle 16f Good To Yielding 10/21 fig 85; 12 Nov Thurles (IRE) Hurdle 16f Good 1/16 fig 98
    DATA for: Trainer 29% wins (2/7), last 14 days; Carries 7 lb less than average
    DATA against: Official rating 39, 9 lb below field average
- Captain Hanley (hrs_47064955) | 6yo G | 132lb | OR 50 | draw 1 | jockey  | trainer Eamonn O'Connell (14d 0/1) | headgear t | last run 5 days | form 425647 | MARKET 6.7% | 09:00 median 9.00 | Matchbook 16.00
    comment: Captain Hanley is winless in his last six, with a seventh last time out just five days ago, though a second five starts back shows he can go close, and he has run over today's trip and going before.
    DATA: model 7.9% | style Held up (led 3% of runs) | runs in data 13 | last 3: 8 Aug Kilbeggan Hurdle 16f Good 4/11; 16 Aug Tramore Hurdle 16.6f Good To Yielding 5/8; 20 Nov Dundalk (AW) (IRE) Flat 12f Standard 7/14 fig 46
- Captain Con (hrs_54998048) | 3yo G | 125lb | OR 49 | draw 2 | jockey Miss M Carlin(10) | trainer Noel Meade (14d 3/14) | headgear - | last run 75 days | form 006700 | MARKET 5.2% | 09:00 median 15.00 | Matchbook 16.00
    comment: The main risk is a 75-day absence, so fitness is a concern.
    DATA: model 6.7% | style Prominent (led 23% of runs) | runs in data 7 | last 3: 4 Jul Naas Flat 10.9f Good 11/16; 5 Sep Navan Flat 10f Good 10/21; 11 Sep Ballinrobe Hurdle 18f Good To Yielding 7/13
    DATA for: Trainer 21% wins (3/14), last 14 days
    DATA against: Poor recent finishing positions
- Lariat (hrs_15233379) | 10yo G | 122lb | OR 38 | draw 6 | jockey Nicola Burns(5) | trainer Liam P Cusack (14d 0/1) | headgear tv | last run 33 days | form 67-728 | MARKET 3.4% | 09:00 median 21.00 | Matchbook 29.00
    comment: Lariat is winless in his last five and was eighth last time out, with a second two starts back the one real bright spot among otherwise modest finishes.
    DATA: model 3.1% | style Midfield (led 3% of runs) | runs in data 7 | last 3: 15 Aug Tramore Flat 16f Good To Yielding 8/12; 19 Sep Navan Hurdle 19f Good 12/16; 23 Oct Sligo (IRE) Hurdle 20.5f Yielding To Soft 2/12 fig 76
    DATA for: Carries 7 lb less than average
    DATA against: Official rating 38, 10 lb below field average; Aged 10, older than most of this field
- Synchronize (hrs_37246587) | 5yo G | 122lb | OR 40 | draw 7 | jockey Julian Pietropaolo(5) | trainer J Morrison (14d 0/2) | headgear - | last run 13 days | form 9-4269 | MARKET 3.0% | 09:00 median 23.00 | Matchbook 34.00
    comment: Synchronize is winless in his last five and was beaten into ninth last time out, only 13 days ago, so he is hard to fancy.
    DATA: model 2.2% | style Held up (led 3% of runs) | runs in data 10 | last 3: 11 Oct Cork Hurdle 18.9f Good 8/14; 3 Nov Fairyhouse (IRE) Hurdle 20f Good To Yielding 9/15 fig 79; 12 Nov Thurles (IRE) Chase 21.5f Good UR/15
    DATA for: Carries 7 lb less than average
    DATA against: Official rating 40, 8 lb below field average; Poor recent finishing positions
- Goodie Girl (hrs_34775111) | 8yo M | 137lb | OR 55 | draw 3 | jockey R. P. Cleary | trainer Dermot A McLoughlin (14d 0/6) | headgear p (1st time) | last run 35 days | form 8890 | MARKET 2.8% | 09:00 median 26.00 | Matchbook 36.00
    comment: Goodie Girl is yet to win in her last four starts, finishing unplaced last time, a ninth two starts back and an eighth three and four starts back, and she returns after 35 days off.
    DATA: model 3.8% | style Held up (led 3% of runs) | runs in data 5 | last 3: 13 Aug Tramore Flat 16f Good 8/9; 8 Sep Galway Flat 12f Soft 9/17; 21 Oct Navan (IRE) Flat 14f Yielding 12/23 fig 43
    DATA for: Official rating 55, 7 lb above field average; First-time headgear
    DATA against: Recent figures 12 lb below its current mark (looks high in the weights); Poor recent finishing positions; Carries 8 lb more than average
- Zitkala Sa (hrs_62677706) | 3yo F | 124lb | OR 48 | draw 11 | jockey Wesley Joyce | trainer E Sheehy (14d 0/1) | headgear t | last run 16 days | form 890480 | MARKET 1.6% | 09:00 median 51.00 | Matchbook 55.00
    comment: Winless in her last six, Zitkala Sa has been unplaced last time out and managed just a fourth three starts back, though she's fresh enough after 16 days and has run on today's going before.
    DATA: model 2.3% | style Midfield (led 4% of runs) | runs in data 12 | last 3: 9 Oct Dundalk Flat 10.7f Standard 8/14; 4 Nov Dundalk (AW) (IRE) Flat 10.5f Standard 12/14 fig 35; 9 Nov Punchestown (IRE) Hurdle 16f Good To Yielding 6/10
    DATA for: Carries 5 lb less than average
    DATA against: Best recent form figure 35, 11 lb below field average; Recent figures 13 lb below its current mark (looks high in the weights); Poor recent finishing positions
- Queen Of Astolat (hrs_57654373) | 3yo F | 126lb | OR 50 | draw 13 | jockey Mel Sheridan(7) | trainer Denis Gerard Hogan (14d 0/11) | headgear p | last run 16 days | form 860730 | MARKET 1.6% | 09:00 median 41.00 | Matchbook 60.00
    comment: Winless in her last six, Queen Of Astolat did manage a third two starts back, but she was unplaced last time out and returns after 16 days.
    DATA: model 4.5% | style Midfield (led 4% of runs) | runs in data 10 | last 3: 8 Oct Thurles Flat 12.7f Yielding 3/14; 12 Oct Roscommon Flat 12.2f Soft 11/16; 9 Nov Punchestown (IRE) Hurdle 16f Good To Yielding 8/10
    DATA against: Trainer 0 wins from 11 runs, last 14 days; Last-run finishing speed -4.6% vs that field (faded)
- Esticky End (hrs_21686623) | 8yo G | 129lb | OR 47 | draw 5 | jockey Robbie Colgan | trainer Tom McGuinness (14d 1/4) | headgear - | last run 13 days | form 5R96-9 | MARKET 1.6% | 09:00 median 51.00 | Matchbook 50.00
    comment: Esticky End is winless in his last five, with a ninth last time out, a sixth two starts back and a ninth three starts back, though he is back quickly after 13 days and has run on today's going before.
    DATA: model 3.4% | style Held up (led 4% of runs) | runs in data 9 | last 3: 19 Oct Gowran Park (IRE) Flat 8.5f Soft 9/16 fig 41; 25 Oct Wexford (IRE) Hurdle 17f Soft PU/13; 12 Nov Thurles (IRE) Chase 21.5f Good PU/15
    DATA against: Best recent form figure 41, 5 lb below field average; Recent figures 6 lb below its current mark (looks high in the weights); Poor recent finishing positions
- Black Chicken (hrs_65254686) | 3yo F | 121lb | OR 45 | draw 8 | jockey Siobhan Rutledge | trainer Ross O'Sullivan (14d 0/16) | headgear - | last run 26 days | form 800 | MARKET 1.5% | 09:00 median 67.00 | Matchbook 60.00
    comment: Black Chicken is winless in her last three, unplaced twice before an eighth three starts back, and she returns after 26 days off.
    DATA: model 1.3% | style Held up (led 5% of runs) | runs in data 3 | last 3: 1 Jun Gowran Park Flat 8f Yielding 8/11; 30 Jun Roscommon Flat 7.4f Good 11/12; 30 Oct Dundalk (AW) (IRE) Flat 8f Standard 13/14 fig 35
    DATA for: Carries 8 lb less than average
    DATA against: Best recent form figure 35, 11 lb below field average; Recent figures 10 lb below its current mark (looks high in the weights); Trainer 0 wins from 16 runs, last 14 days; Poor recent finishing positions

## 3:01 Dundalk (AW) | race_id rac_32305481065 | Irish Stallion Farms EBF Maiden
Flat |  | 7f | going Standard | AW | 17 runners | rating band - | age 2yo
DATA pace: Unclear - Running styles known for only 8 of 17 runners.
- Sharpe Ratio (hrs_17395391496) | 2yo C | 133lb | OR - | draw 8 | jockey J M Sheridan | trainer Joseph Patrick O'Brien (14d 5/30) | headgear - | last run 12 days | form 2 | MARKET 44.3% | 09:00 median 1.73 | Matchbook 1.78
    DATA: model 13.6% | style Unknown | runs in data 1 | last 3: 13 Nov Dundalk (AW) (IRE) Flat 6f Standard 2/11 fig 67
    DATA for: Best recent form figure 67, 18 lb above field average
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Catuai (hrs_65973341) | 2yo G | 133lb | OR - | draw 5 | jockey  | trainer Diego Dias (14d 0/2) | headgear - | last run 49 days | form 89 | MARKET 8.4% | 09:00 median 6.50 | Matchbook 14.50
    DATA: model 11.3% | style Held up (led 5% of runs) | runs in data 2 | last 3: 21 Sep Fairyhouse Flat 6f Good 8/10; 7 Oct Navan Flat 5.8f Yielding 9/21
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Final Settlement (hrs_17395780535) | 2yo C | 133lb | OR - | draw 4 | jockey Colin Keane | trainer Stephen Thorne (14d 0/4) | headgear - | last run - days | form - | MARKET 6.2% | 09:00 median 11.00 | Matchbook 14.50
    DATA: model 4.6% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Irishamerican (hrs_17392069541) | 2yo G | 133lb | OR - | draw 1 | jockey Declan McDonogh | trainer Joseph Patrick O'Brien (14d 5/30) | headgear h (1st time) | last run - days | form - | MARKET 5.8% | 09:00 median 11.00 | Matchbook 17.50
    DATA: model 4.6% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: First-time headgear
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Celestial Order (hrs_17393765459) | 2yo F | 128lb | OR - | draw 3 | jockey Ben Coen | trainer Miss Natalia Lupini (14d 1/6) | headgear - | last run 41 days | form 7 | MARKET 5.8% | 09:00 median 11.00 | Matchbook 19.50
    DATA: model 11.4% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 15 Oct Curragh (IRE) Flat 8f Soft 7/15 fig 51
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Solar Palace (hrs_17395792008) | 2yo F | 128lb | OR - | draw 10 | jockey Seamie Heffernan | trainer Joseph Patrick O'Brien (14d 5/30) | headgear - | last run - days | form - | MARKET 5.1% | 09:00 median 13.00 | Matchbook 18.50
    DATA: model 4.5% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- There's A Starman (hrs_66272409) | 2yo G | 133lb | OR - | draw 2 | jockey Jack Kearney | trainer Stephen Thorne (14d 0/4) | headgear - | last run - days | form - | MARKET 4.8% | 09:00 median 13.00 | Matchbook 20.00
    DATA: model 4.6% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Colpo Del Fortuna (hrs_17395959931) | 2yo G | 133lb | OR - | draw 15 | jockey Chris Hayes | trainer Joseph Patrick O'Brien (14d 5/30) | headgear - | last run - days | form - | MARKET 4.4% | 09:00 median 18.00 | Matchbook 18.50
    DATA: model 4.6% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Big City Girl (hrs_17392878909) | 2yo F | 128lb | OR - | draw 16 | jockey Donagh O'Connor | trainer Robson De Aguiar (14d 2/8) | headgear - | last run 61 days | form 9 | MARKET 3.8% | 09:00 median 17.00 | Matchbook 25.00
    DATA: model 10.2% | style Held up (led 8% of runs) | runs in data 1 | last 3: 25 Sep Dundalk Flat 7f Standard 9/13
    DATA for: Trainer 25% wins (2/8), last 14 days
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Se Per Caso (hrs_17395962017) | 2yo C | 133lb | OR - | draw 13 | jockey Shay Wallace(7) | trainer Joseph Patrick O'Brien (14d 5/30) | headgear - | last run - days | form - | MARKET 2.6% | 09:00 median 29.00 | Matchbook 32.00
    DATA: model 4.6% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Beauxvarus (hrs_17394334937) | 2yo F | 128lb | OR - | draw 11 | jockey Robbie Colgan | trainer Henry de Bromhead (14d 9/43) | headgear - | last run 33 days | form 9 | MARKET 1.9% | 09:00 median 51.00 | Matchbook 46.00
    DATA: model 5.4% | style Unknown | runs in data 1 | last 3: 23 Oct Dundalk (AW) (IRE) Flat 8f Standard 9/14 fig 57
    DATA for: Best recent form figure 57, 8 lb above field average; Trainer 21% wins (9/43), last 14 days
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Sea The Sol (hrs_17395963060) | 2yo G | 133lb | OR - | draw 6 | jockey Leigh Roche | trainer Paul W Flynn (14d 0/6) | headgear - | last run - days | form - | MARKET 1.8% | 09:00 median 51.00 | Matchbook 48.00
    DATA: model 4.6% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Victorious Star (hrs_17395783664) | 2yo G | 133lb | OR - | draw 9 | jockey Julian Pietropaolo(5) | trainer Joseph Patrick O'Brien (14d 5/30) | headgear - | last run 5 days | form 0 | MARKET 1.2% | 09:00 median 61.00 | Matchbook 80.00
    DATA: model 4.8% | style Held up (led 8% of runs) | runs in data 1 | last 3: 20 Nov Dundalk (AW) (IRE) Flat 8f Standard 13/13 fig 28
    DATA against: Best recent form figure 28, 21 lb below field average; Last-run finishing speed -3.5% vs that field (faded); Lightly raced: 1 run in our data, so the model has little to go on
- Silent Promise (hrs_17392277098) | 2yo F | 128lb | OR - | draw 14 | jockey  | trainer Adrian McGuinness (14d 2/20) | headgear - | last run 24 days | form 90 | MARKET 1.1% | 09:00 median 101.00 | Matchbook 80.00
    DATA: model 4.5% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 15 Oct Curragh (IRE) Flat 8f Soft 9/15 fig 51; 1 Nov Curragh (IRE) Flat 8f Yielding To Soft 12/23 fig 52
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Drumbinion Lass (hrs_17392956091) | 2yo F | 128lb | OR - | draw 17 | jockey James Ryan | trainer T G McCourt (14d 1/7) | headgear h (1st time) | last run 37 days | form 40 | MARKET 1.0% | 09:00 median 151.00 | Matchbook 80.00
    DATA: model 3.2% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 2 Oct Dundalk Flat 8f Standard 4/7; 19 Oct Gowran Park (IRE) Flat 8.5f Soft 11/15 fig 37
    DATA for: First-time headgear
    DATA against: Best recent form figure 37, 12 lb below field average; Last-run finishing speed -4.2% vs that field (faded); Lightly raced: 2 runs in our data, so the model has little to go on
- Nando The Great (hrs_7000000567) | 2yo G | 133lb | OR - | draw 7 | jockey  | trainer Paul W Flynn (14d 0/6) | headgear - | last run 103 days | form 00 | MARKET 1.0% | 09:00 median 126.00 | Matchbook 90.00
    DATA: model 1.7% | style Held up (led 8% of runs) | runs in data 2 | last 3: 9 Aug Curragh Flat 6f Good To Firm 19/19; 14 Aug Cork Flat 5f Good 11/16
    DATA against: Returns from a 103-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- Blue Glory (hrs_17393397280) | 2yo G | 133lb | OR - | draw 12 | jockey Nicola Burns(5) | trainer Aengus King (14d 0/2) | headgear - | last run 24 days | form 900 | MARKET 0.8% | 09:00 median 201.00 | Matchbook 110.00
    DATA: model 1.7% | style Midfield (led 5% of runs) | runs in data 3 | last 3: 7 Oct Navan Flat 8.2f Yielding 9/9; 15 Oct Curragh (IRE) Flat 8f Soft 15/15; 1 Nov Curragh (IRE) Flat 8f Yielding To Soft 23/23
    DATA against: Last-run finishing speed -12.6% vs that field (faded); Poor recent finishing positions

## 3:31 Dundalk (AW) | race_id rac_32305835536 | Book Online At DundalkStadium.com Handicap (Div I)
Flat |  | 1m | going Standard | AW | 16 runners | rating band 0-60 | age 3yo+
DATA pace: Lone leader - Sayonara is the only habitual front-runner and may be allowed an easy lead.
- Sedro Woolley (hrs_52205090) | 4yo G | 136lb | OR 54 | draw 11 | jockey W. J. Lee | trainer W. McCreery (14d 0/4) | headgear v | last run 40 days | form 5-5671 | MARKET 26.1% | 09:00 median 2.63 | Matchbook 3.20
    comment: The main risk is a 40-day layoff, plus 136 lb to carry from stall 11.
    DATA: model 15.5% | style Prominent (led 5% of runs) | runs in data 4 | last 3: 11 Feb Dundalk Flat 6f Standard 6/8; 12 Apr Leopardstown Flat 8f Yielding 7/20; 16 Oct Dundalk (AW) (IRE) Flat 7f Standard 1/14 fig 59
    DATA for: Best recent form figure 59, 13 lb above field average; Recent figures 5 lb above its current mark (looks well handicapped); Official rating 54, 6 lb above field average
    DATA against: Carries 6 lb more than average
- The Bear Trap (hrs_35040054) | 5yo G | 144lb | OR 62 | draw 6 | jockey Camillus Byrne(10) | trainer Adrian McGuinness (14d 2/20) | headgear v | last run 7 days | form 409713 | MARKET 15.5% | 09:00 median 4.50 | Matchbook 5.40
    comment: The Bear Trap booked a third last time out, and a winner two starts back, so he arrives in good heart just seven days after that run.
    DATA: model 21.6% | style Held up (led 5% of runs) | runs in data 6 | last 3: 28 Oct Dundalk (AW) (IRE) Flat 7f Standard 7/14 fig 53; 11 Nov Dundalk (AW) (IRE) Flat 7f Standard 1/14 fig 59; 18 Nov Dundalk (AW) (IRE) Flat 7f Standard 3/14 fig 69
    DATA for: Best recent form figure 69, 23 lb above field average; Recent figures 7 lb above its current mark (looks well handicapped); Official rating 62, 14 lb above field average; Good recent finishing positions
    DATA against: Carries 14 lb more than average
- Magna Gee Gee (hrs_45193463) | 4yo G | 135lb | OR 53 | draw 12 | jockey Leigh Roche | trainer Patrick J Flynn (14d 2/7) | headgear - | last run 12 days | form 863107 | MARKET 10.9% | 09:00 median 6.50 | Matchbook 7.80
    comment: Fit after just 12 days off, he has run over today's trip and going, and he won three starts back, but a seventh last time out and an unplaced effort before that leave him short of convincing.
    DATA: model 1.4% | style Midfield (led 4% of runs) | runs in data 13 | last 3: 2 Oct Gowran Park Hurdle 16.4f Good 8/13; 14 Oct Punchestown (IRE) Hurdle 16.5f Good 15/15; 13 Nov Dundalk (AW) (IRE) Flat 12f Standard 7/14 fig 50
    DATA for: Official rating 53, 5 lb above field average; Trainer 29% wins (2/7), last 14 days; Has won at this trip or further
    DATA against: Poor recent finishing positions
- Roman Harry (hrs_36036714) | 6yo G | 142lb | OR 60 | draw 7 | jockey Patrick McGettigan(5) | trainer S M Duffy (14d 0/2) | headgear - | last run 28 days | form 098291 | MARKET 9.0% | 09:00 median 6.50 | Matchbook 12.00
    comment: Roman Harry won last time out, but that came after a ninth two starts back and a mixed run of results, so consistency is the query.
    DATA: model 17.1% | style Midfield (led 4% of runs) | runs in data 10 | last 3: 15 Aug Dundalk Flat 8f Standard 2/14; 10 Sep Laytown Flat 7f Standard 9/10; 28 Oct Dundalk (AW) (IRE) Flat 7f Standard 1/13 fig 58
    DATA for: Best recent form figure 58, 12 lb above field average; Official rating 60, 12 lb above field average; Good recent finishing positions
    DATA against: Carries 12 lb more than average
- Jasmine Affanalis (hrs_47985735) | 4yo F | 135lb | OR 53 | draw 9 | jockey Robbie Colgan | trainer David Marnane (14d 1/5) | headgear - | last run 19 days | form 207104 | MARKET 7.7% | 09:00 median 9.00 | Matchbook 12.00
    DATA: model 10.3% | style Held up (led 5% of runs) | runs in data 12 | last 3: 5 Oct Killarney Flat 8.1f Soft 1/15; 20 Oct Curragh (IRE) Flat 8f Yielding 12/23 fig 57; 6 Nov Dundalk (AW) (IRE) Flat 8f Standard 4/14 fig 55
    DATA for: Best recent form figure 57, 11 lb above field average; Recent figures 4 lb above its current mark (looks well handicapped); Official rating 53, 5 lb above field average; Trainer 20% wins (1/5), last 14 days; Has won at this trip or further
- La Campanella (hrs_57255212) | 4yo F | 122lb | OR 38 | draw 14 | jockey Rory Mulligan(5) | trainer Gerard Keane (14d 0/6) | headgear b (1st time) | last run 86 days | form 754740 | MARKET 4.9% | 09:00 median 17.00 | Matchbook 15.00
    comment: La Campanella is winless in her last six, with a fourth two starts back her best finish, and she returns after 86 days off, so she is hard to fancy.
    DATA: model 4.6% | style Prominent (led 3% of runs) | runs in data 7 | last 3: 12 Aug Gowran Park Flat 9.5f Good To Firm 7/16; 25 Aug Bellewstown Flat 7.9f Good To Yielding 4/15; 31 Aug Roscommon Flat 7.4f Good To Yielding 12/14
    DATA for: Carries 8 lb less than average; First-time headgear
    DATA against: Official rating 38, 10 lb below field average
- Whistling Jamesie (hrs_55453965) | 3yo G | 133lb | OR 53 | draw 16 | jockey Nicola Burns(5) | trainer Miss Natalia Lupini (14d 1/6) | headgear v (1st time) | last run 21 days | form 800500 | MARKET 4.3% | 09:00 median 17.00 | Matchbook 19.50
    comment: Whistling Jamesie is winless in his last six, unplaced last time out and a fifth three starts back his best recent finish, though he has run over today's trip and going and returns after 21 days.
    DATA: model 5.9% | style Prominent (led 5% of runs) | runs in data 6 | last 3: 12 Jul Dundalk Flat 7f Standard 5/11; 28 Oct Dundalk (AW) (IRE) Flat 7f Standard 10/13 fig 49; 4 Nov Dundalk (AW) (IRE) Flat 7f Standard 12/13 fig 30
    DATA for: Official rating 53, 5 lb above field average; First-time headgear
    DATA against: Last-run finishing speed -3.7% vs that field (faded)
- Local Lad (hrs_41596842) | 4yo G | 142lb | OR 60 | draw 1 | jockey Danny O'Leary(10) | trainer G. O'Leary (14d 0/5) | headgear b | last run 36 days | form 3-0000 | MARKET 3.9% | 09:00 median 17.00 | Matchbook 23.00
    comment: The risk is a poor recent run of form, carrying 142 lb after 36 days off.
    DATA: model 4.8% | style Held up (led 5% of runs) | runs in data 4 | last 3: 21 Sep Listowel Flat 8f Yielding 14/15; 4 Oct Curragh Flat 8f Soft 12/16; 20 Oct Curragh (IRE) Flat 10f Yielding 23/24
    DATA for: Official rating 60, 12 lb above field average
    DATA against: Poor recent finishing positions; Carries 12 lb more than average
- Jackandthefox (hrs_32554165) | 7yo G | 122lb | OR 35 | draw 5 | jockey  | trainer Miss Jennifer Anne Lynch (14d 0/2) | headgear p | last run 21 days | form 455007 | MARKET 3.7% | 09:00 median 17.00 | Matchbook 27.00
    comment: Jackandthefox is hard to fancy, winless in his last six and beaten in seventh last time out, with no finish better than a fourth six starts back.
    DATA: model 1.8% | style Midfield (led 4% of runs) | runs in data 8 | last 3: 5 Sep Navan Flat 5f Good 13/18; 7 Oct Navan Flat 5.8f Yielding 20/22; 4 Nov Dundalk (AW) (IRE) Flat 7f Standard 7/13 fig 31
    DATA for: Carries 8 lb less than average
    DATA against: Best recent form figure 31, 15 lb below field average; Official rating 35, 13 lb below field average; Poor recent finishing positions
- Sayonara (hrs_59246964) | 3yo G | 128lb | OR 48 | draw 8 | jockey Jimmy Dalton(7) | trainer A. Slattery (14d 0/14) | headgear t | last run 7 days | form 230007 | MARKET 2.5% | 09:00 median 34.00 | Matchbook 30.00
    comment: Sayonara is winless in his last six, with a seventh last time out and three unplaced runs before that, though he has been placed before, finishing a third five starts back and a second six starts back.
    DATA: model 4.1% | style Leader (led 38% of runs) | runs in data 12 | last 3: 5 Oct Killarney Flat 8.1f Soft 10/15; 6 Nov Dundalk (AW) (IRE) Flat 8f Standard 14/14 fig 36; 18 Nov Dundalk (AW) (IRE) Flat 7f Standard 7/14 fig 46
    DATA for: Pace: may get an uncontested lead
    DATA against: Trainer 0 wins from 14 runs, last 14 days; Poor recent finishing positions
- Rampage (hrs_30231985) | 7yo G | 124lb | OR 42 | draw 10 | jockey Sadhbh Tormey(7) | trainer T G McCourt (14d 1/7) | headgear tv | last run 28 days | form 526805 | MARKET 2.5% | 09:00 median 29.00 | Matchbook 40.00
    comment: Rampage was a fifth last time out 28 days ago, and he has run over today's trip and going, but he is without a win in his last six and managed just one second, five starts back.
    DATA: model 3.1% | style Midfield (led 4% of runs) | runs in data 15 | last 3: 5 Oct Killarney Flat 8.1f Soft 8/15; 19 Oct Gowran Park (IRE) Flat 8.5f Soft 10/15 fig 31; 28 Oct Dundalk (AW) (IRE) Flat 8f Standard 5/11 fig 45
    DATA for: Carries 6 lb less than average
    DATA against: Official rating 42, 6 lb below field average
- Miss Abby Jools (hrs_30765084) | 7yo M | 136lb | OR 54 | draw 3 | jockey Keithen Kennedy(5) | trainer Timothy Doyle (14d 0/3) | headgear - | last run 37 days | form 4200-0 | MARKET 2.3% | 09:00 median 34.00 | Matchbook 40.00
    comment: A second four starts back shows she can go close, though she has been unplaced in her last three and returns after 37 days off.
    DATA: model 4.0% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 19 Oct Gowran Park (IRE) Flat 8.5f Soft 16/16 fig 22
    DATA for: Official rating 54, 6 lb above field average
    DATA against: Best recent form figure 22, 24 lb below field average; Recent figures 32 lb below its current mark (looks high in the weights); Last-run finishing speed -6.8% vs that field (faded); Carries 6 lb more than average; Lightly raced: 1 run in our data, so the model has little to go on
- Cosmic Force (hrs_42226884) | 4yo G | 122lb | OR 40 | draw 15 | jockey R. P. Cleary | trainer Keith Henry Clarke (14d 0/0) | headgear - | last run 136 days | form 663570 | MARKET 2.2% | 09:00 median 34.00 | Matchbook 42.00
    comment: Winless in his last six, Cosmic Force was unplaced last time and returns after 136 days off, though a third four starts back and prior experience over today's trip and going give him something to work with.
    DATA: model 1.9% | style Held up (led 4% of runs) | runs in data 6 | last 3: 23 Apr Dundalk Flat 8f Standard 5/10; 26 May Dundalk Flat 8f Standard 7/10; 12 Jul Dundalk Flat 8f Standard 13/14
    DATA for: Carries 8 lb less than average
    DATA against: Official rating 40, 8 lb below field average; Returns from a 136-day break
- Manhattan Dandy (hrs_19510351) | 9yo G | 122lb | OR 38 | draw 13 | jockey  | trainer Thomas Coyle (14d 0/4) | headgear - | last run 7 days | form 374000 | MARKET 2.1% | 09:00 median 34.00 | Matchbook 48.00
    comment: Manhattan Dandy is winless in his last six, unplaced in each of his last three, and he's back quickly after seven days off, so he's hard to fancy.
    DATA: model 2.2% | style Midfield (led 3% of runs) | runs in data 10 | last 3: 30 Sep Bellewstown Flat 7.9f Soft To Heavy 14/14; 12 Oct Roscommon Flat 7.5f Soft 10/13; 18 Nov Dundalk (AW) (IRE) Flat 7f Standard 12/14 fig 22
    DATA for: Carries 8 lb less than average
    DATA against: Best recent form figure 22, 24 lb below field average; Recent figures 16 lb below its current mark (looks high in the weights); Official rating 38, 10 lb below field average; Poor recent finishing positions; Aged 9, older than most of this field
- Pure Valour (hrs_62583115) | 4yo F | 122lb | OR 38 | draw 2 | jockey Nathan Crosse | trainer J G Coogan (14d 0/0) | headgear - | last run 88 days | form 976060 | MARKET 1.3% | 09:00 median 67.00 | Matchbook 80.00
    comment: Pure Valour is hard to fancy, winless in her last six with a best finish of sixth, and she returns after 88 days off. She has run over today's trip and going, and carries 122 lb from draw 2 off a lowly 38.
    DATA: model 1.0% | style Prominent (led 3% of runs) | runs in data 6 | last 3: 1 Jul Fairyhouse Flat 8.7f Good 12/12; 16 Aug Curragh Flat 5f Good 6/11; 29 Aug Curragh Flat 6f Yielding 17/19
    DATA for: Carries 8 lb less than average
    DATA against: Official rating 38, 10 lb below field average; Poor recent finishing positions
- Tijuana (hrs_27861673) | 8yo G | 122lb | OR 40 | draw 4 | jockey Wesley Joyce | trainer David Edward Finn (14d 0/1) | headgear - | last run 7 days | form 07/00P | MARKET 1.1% | 09:00 median 101.00 | Matchbook 80.00
    comment: Tijuana was pulled up last time out and is winless in his last five, with a seventh four starts back his best recent finish, so he is hard to fancy.
    DATA: model 0.8% | style Held up (led 5% of runs) | runs in data 3 | last 3: 12 May Killarney Flat 8.1f Good 12/13; 21 Sep Listowel Flat 8f Yielding 12/14; 18 Nov Dundalk (AW) (IRE) Flat 7f Standard PU/14
    DATA for: Carries 8 lb less than average
    DATA against: Official rating 40, 8 lb below field average; Poor recent finishing positions

## 4:06 Dundalk (AW) | race_id rac_32305483002 | Book Online At DundalkStadium.com Handicap (Div II)
Flat |  | 1m | going Standard | AW | 15 runners | rating band 0-60 | age 3yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Red Hugh O'Donnell (hrs_37014103) | 5yo G | 141lb | OR 59 | draw 13 | jockey Nicola Burns(5) | trainer Gillian Scott (14d 1/1) | headgear tb | last run 14 days | form 806965 | MARKET 10.7% | 09:00 median 5.50 | Matchbook 8.60 | CHECK (skip line 5.22)
    DATA: model 10.4% | style Held up (led 5% of runs) | runs in data 10 | last 3: 30 Sep Bellewstown Flat 7.9f Soft To Heavy 9/14; 28 Oct Dundalk (AW) (IRE) Flat 8f Standard 6/12 fig 60; 11 Nov Dundalk (AW) (IRE) Flat 8f Standard 5/8 fig 62
    DATA for: Best recent form figure 62, 14 lb above field average; Official rating 59, 9 lb above field average; Has won at this trip or further
    DATA against: Carries 10 lb more than average; Pace: steady gallop likely, hard to come from off the pace
- Comfort Line (hrs_20041406) | 9yo G | 139lb | OR 57 | draw 15 | jockey Adam Caffrey | trainer Adrian McGuinness (14d 2/20) | headgear v | last run 21 days | form 358908 | MARKET 10.3% | 09:00 median 6.50 | Matchbook 8.40
    DATA: model 9.7% | style Midfield (led 8% of runs) | runs in data 19 | last 3: 16 Oct Dundalk (AW) (IRE) Flat 10.5f Standard 9/14 fig 58; 23 Oct Dundalk (AW) (IRE) Flat 7f Standard 10/14 fig 54; 4 Nov Dundalk (AW) (IRE) Flat 7f Standard 8/13 fig 57
    DATA for: Best recent form figure 58, 10 lb above field average; Official rating 57, 7 lb above field average; Has won at this trip or further
    DATA against: Poor recent finishing positions; Carries 8 lb more than average; Aged 9, older than most of this field
- John La Bear (hrs_54712392) | 3yo G | 140lb | OR 60 | draw 14 | jockey Donagh O'Connor | trainer Ross O'Sullivan (14d 0/16) | headgear t | last run 28 days | form 1-7099 | MARKET 10.2% | 09:00 median 7.50 | Matchbook 7.60
    comment: The risk is form of late, a ninth last time out and another ninth before that, off 140 lb from stall 14.
    DATA: model 11.6% | style Prominent (led 4% of runs) | runs in data 4 | last 3: 31 Jul Galway Flat 8.4f Yielding To Soft 12/18; 16 Sep Clonmel Flat 9.8f Yielding 9/14; 28 Oct Dundalk (AW) (IRE) Flat 8f Standard 9/12 fig 53
    DATA for: Best recent form figure 53, 5 lb above field average; Official rating 60, 10 lb above field average
    DATA against: Recent figures 7 lb below its current mark (looks high in the weights); Trainer 0 wins from 16 runs, last 14 days; Last-run finishing speed -2.5% vs that field (faded); Poor recent finishing positions; Carries 9 lb more than average
- Liamo (hrs_36809577) | 5yo G | 124lb | OR 42 | draw 4 | jockey Chris Hayes | trainer Brendan Maurice Walsh (14d 0/3) | headgear tp | last run 28 days | form 662056 | MARKET 9.1% | 09:00 median 8.00 | Matchbook 8.80
    comment: Liamo has finished sixth and fifth in his last two starts, with a second four runs back his best recent effort, and he has run over today's trip and going before.
    DATA: model 6.7% | style Midfield (led 5% of runs) | runs in data 6 | last 3: 9 Sep Cork Flat 7f Good 13/22; 16 Oct Dundalk (AW) (IRE) Flat 7f Standard 5/14 fig 47; 28 Oct Dundalk (AW) (IRE) Flat 7f Standard 6/14 fig 37
    DATA for: Recent figures 5 lb above its current mark (looks well handicapped); Carries 7 lb less than average
    DATA against: Official rating 42, 8 lb below field average
- Desert Of The Sea (hrs_46013611) | 5yo G | 123lb | OR 41 | draw 12 | jockey Sadhbh Tormey(7) | trainer T G McCourt (14d 1/7) | headgear tp | last run 26 days | form 085065 | MARKET 8.9% | 09:00 median 9.00 | Matchbook 8.60
    comment: Desert Of The Sea was fifth last time out and sixth two starts back, yet he's winless in his last six and has only two fifths and a sixth in that spell to show for it.
    DATA: model 4.9% | style Midfield (led 5% of runs) | runs in data 11 | last 3: 18 Sep Dundalk Flat 8f Standard 11/14; 16 Oct Dundalk (AW) (IRE) Flat 7f Standard 6/14 fig 47; 30 Oct Dundalk (AW) (IRE) Flat 8f Standard 5/14 fig 40
    DATA for: Recent figures 6 lb above its current mark (looks well handicapped); Carries 8 lb less than average
    DATA against: Official rating 41, 9 lb below field average
- Jazzy Dancer (hrs_26874890) | 8yo G | 133lb | OR 51 | draw 3 | jockey Luke McAteer | trainer W J Martin (14d 0/4) | headgear p | last run 7 days | form 790828 | MARKET 7.3% | 09:00 median 11.00 | Matchbook 10.50
    comment: Winless in his last six, Jazzy Dancer was eighth last time out just seven days ago, though a second two starts back shows he can step up, and he has run over today's trip and going before.
    DATA: model 10.6% | style Unknown | runs in data 9 | last 3: 16 Oct Dundalk (AW) (IRE) Flat 7f Standard 8/14 fig 49; 28 Oct Dundalk (AW) (IRE) Flat 7f Standard 2/13 fig 51; 18 Nov Dundalk (AW) (IRE) Flat 7f Standard 8/14 fig 44
- River Derwent (hrs_22939973) | 8yo G | 122lb | OR 38 | draw 10 | jockey Nina Doherty(10) | trainer Thomas Coyle (14d 0/4) | headgear - | last run 21 days | form 004004 | MARKET 6.5% | 09:00 median 12.00 | Matchbook 11.50
    comment: River Derwent is winless in his last six, with a fourth last time out the best of a modest recent run, and he has been unplaced in four of those.
    DATA: model 2.4% | style Held up (led 4% of runs) | runs in data 8 | last 3: 20 May Gowran Park Flat 8f Good To Yielding 14/16; 25 Sep Dundalk Flat 8f Standard 11/14; 4 Nov Dundalk (AW) (IRE) Flat 7f Standard 4/13 fig 39
    DATA for: Last-run finishing speed +4.3% vs that field (finished strongly); Carries 9 lb less than average
    DATA against: Best recent form figure 39, 9 lb below field average; Official rating 38, 12 lb below field average; Pace: steady gallop likely, hard to come from off the pace
- Chavajod (hrs_22214542) | 8yo G | 130lb | OR 48 | draw 11 | jockey Ross Coakley | trainer D P Coakley (14d 0/1) | headgear v | last run 56 days | form -00710 | MARKET 5.9% | 09:00 median 11.00 | Matchbook 16.00
    comment: Chavajod won two starts back, but he was unplaced last time out and has been off for 56 days, so fitness is a question.
    DATA: model 7.5% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 12 Aug Gowran Park Flat 9.5f Good To Firm 7/15; 10 Sep Laytown Flat 7f Standard 1/10; 30 Sep Bellewstown Flat 7.9f Soft To Heavy 13/14
- Spiritofthedawn (hrs_53602234) | 3yo F | 127lb | OR 47 | draw 5 | jockey Robert Whearty | trainer F G Hand (14d 0/1) | headgear t | last run 55 days | form -00275 | MARKET 5.9% | 09:00 median 11.00 | Matchbook 16.50
    comment: A second three starts back and experience of today's trip are about the only positives from stall five.
    DATA: model 10.3% | style Prominent (led 8% of runs) | runs in data 5 | last 3: 2 Sep Navan Flat 8.1f Good 2/16; 15 Sep Punchestown Flat 9.1f Good 7/14; 1 Oct Bellewstown Flat 7.9f Soft To Heavy 5/9
- Teffian Warrior (hrs_50875377) | 4yo G | 142lb | OR 60 | draw 6 | jockey Ben Coen | trainer Ciaran Murphy (14d 0/5) | headgear - | last run 14 days | form 04-460 | MARKET 5.8% | 09:00 median 12.00 | Matchbook 15.00
    DATA: model 9.2% | style Prominent (led 4% of runs) | runs in data 4 | last 3: 12 May Killarney Flat 8.1f Good 6/13; 8 Jun Roscommon Hurdle 16f Yielding To Soft 10/11; 11 Nov Dundalk (AW) (IRE) Flat 7f Standard 11/14 fig 51
    DATA for: Official rating 60, 10 lb above field average
    DATA against: Recent figures 9 lb below its current mark (looks high in the weights); Poor recent finishing positions; Carries 11 lb more than average
- Freddiesadienray (hrs_17392596256) | 3yo F | 139lb | OR 59 | draw 1 | jockey Colin Keane | trainer Gerard Keane (14d 0/6) | headgear t | last run 46 days | form 076 | MARKET 5.3% | 09:00 median 13.00 | Matchbook 18.00
    comment: Winless in her last three, finishing sixth last time out and a seventh two starts back, Freddiesadienray is hard to fancy after 46 days off and with 139 lb to carry from stall one.
    DATA: model 3.4% | style Held up (led 4% of runs) | runs in data 3 | last 3: 21 Sep Fairyhouse Flat 7f Good 15/17; 28 Sep Down Royal Flat 7.1f Good To Yielding 7/9; 10 Oct Naas Flat 8f Soft 6/13
    DATA for: Official rating 59, 9 lb above field average
    DATA against: Poor recent finishing positions; Carries 8 lb more than average; Pace: steady gallop likely, hard to come from off the pace
- Exceeding (hrs_37821560) | 5yo G | 122lb | OR 37 | draw 7 | jockey  | trainer A. Slattery (14d 0/14) | headgear t | last run 19 days | form 201009 | MARKET 4.4% | 09:00 median 15.00 | Matchbook 22.00
    comment: Exceeding was a ninth last time out and unplaced in the two runs before, though he is a winner four starts back and has run over today's trip and going.
    DATA: model 2.4% | style Midfield (led 4% of runs) | runs in data 6 | last 3: 31 May Listowel Flat 7f Good 14/15; 10 Jun Limerick Flat 7f Yielding 11/13; 6 Nov Dundalk (AW) (IRE) Flat 8f Standard 9/14 fig 30
    DATA for: Carries 9 lb less than average
    DATA against: Best recent form figure 30, 18 lb below field average; Recent figures 7 lb below its current mark (looks high in the weights); Official rating 37, 13 lb below field average; Trainer 0 wins from 14 runs, last 14 days; Poor recent finishing positions
- Mothel Abbey (hrs_17390262022) | 3yo G | 133lb | OR 53 | draw 9 | jockey Robyn Donaghue-Leahy(7) | trainer Patrick J Flynn (14d 2/7) | headgear h (1st time) | last run 12 days | form 80998 | MARKET 4.0% | 09:00 median 17.00 | Matchbook 23.00
    comment: Mothel Abbey is hard to fancy, having finished eighth last time out, with a ninth two starts back and another ninth three starts back, and he is winless in his last five.
    DATA: model 2.3% | style Prominent (led 5% of runs) | runs in data 5 | last 3: 8 Oct Thurles Flat 16.6f Yielding To Soft 9/9; 30 Oct Dundalk (AW) (IRE) Flat 8f Standard 9/14 fig 43; 13 Nov Dundalk (AW) (IRE) Flat 10.5f Standard 8/10 fig 47
    DATA for: Trainer 29% wins (2/7), last 14 days; First-time headgear
    DATA against: Recent figures 6 lb below its current mark (looks high in the weights); Poor recent finishing positions
- Miss Glenville (hrs_46013632) | 6yo M | 129lb | OR 47 | draw 2 | jockey Conor Cusack(7) | trainer Paul Power (14d 0/0) | headgear tp | last run 21 days | form /9-597 | MARKET 3.8% | 09:00 median 21.00 | Matchbook 19.50
    comment: Miss Glenville is winless in her last four, finishing seventh last time out, a ninth two starts back, a fifth three runs ago and a ninth before that, so she is hard to fancy.
    DATA: model 6.7% | style Prominent (led 5% of runs) | runs in data 3 | last 3: 16 Sep Clonmel Flat 9.8f Yielding 5/14; 8 Oct Thurles Flat 8.3f Yielding 9/14; 4 Nov Dundalk (AW) (IRE) Flat 10.5f Standard 7/14 fig 44
    DATA against: Best recent form figure 44, 4 lb below field average
- May Night (hrs_20977754) | 8yo G | 127lb | OR 45 | draw 8 | jockey Jared Huggan(10) | trainer Raymond Hurley (14d 0/1) | headgear p | last run 61 days | form 703-00 | MARKET 2.0% | 09:00 median 51.00 | Matchbook 46.00
    comment: May Night is yet to win in his last five starts, though a third three starts back shows he can pick up a cheque, and he has run over today's trip and going. Unplaced in his last two and returning after 61 days, he looks a midfield type from stall 8.
    DATA: model 1.9% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 12 Aug Gowran Park Flat 8f Good To Firm 14/15; 25 Sep Dundalk Flat 8f Standard 12/14
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on

## 4:40 Dundalk (AW) | race_id rac_32305484939 | Irishinjuredjockeys.com Handicap
Flat |  | 1m | going Standard | AW | 15 runners | rating band - | age 3yo+
DATA pace: Strong pace - 3 habitual front-runners (Exquisite Acclaim, Gotta Catch'em All, Leveraging). A contested lead should set things up for horses coming from behind.
- Gavoo (hrs_52496150) | 3yo G | 132lb | OR 74 | draw 5 | jockey Donagh O'Connor | trainer David Marnane (14d 1/5) | headgear - | last run 26 days | form 377973 | MARKET 15.4% | 09:00 median 5.00 | Matchbook 5.50 | CHECK (skip line 4.75)
    DATA: model 7.6% | style Held up (led 5% of runs) | runs in data 10 | last 3: 22 Sep Listowel Flat 7.1f Yielding 9/11; 28 Oct Dundalk (AW) (IRE) Flat 8f Standard 7/12 fig 67; 30 Oct Dundalk (AW) (IRE) Flat 8f Standard 3/14 fig 78
    DATA for: Recent figures 4 lb above its current mark (looks well handicapped); Trainer 20% wins (1/5), last 14 days; Pace: a contested lead should suit its hold-up style
- Naoi (hrs_51557793) | 4yo F | 138lb | OR 78 | draw 4 | jockey W. J. Lee | trainer W. McCreery (14d 0/4) | headgear - | last run 47 days | form 8-1914 | MARKET 14.5% | 09:00 median 5.50 | Matchbook 5.60
    comment: Fourth last time out, and a winner two starts back, Naoi has shown she can win in recent runs, and she has run over today's trip and going before.
    DATA: model 14.1% | style Held up (led 3% of runs) | runs in data 4 | last 3: 29 Aug Curragh Flat 6f Yielding 9/19; 21 Sep Fairyhouse Flat 7f Good 1/18; 9 Oct Dundalk Flat 8f Standard 4/13
    DATA for: Pace: a contested lead should suit its hold-up style
- Art Gallery (hrs_55634194) | 3yo F | 137lb | OR 79 | draw 6 | jockey Ben Coen | trainer J. P. Murtagh (14d 1/8) | headgear - | last run 26 days | form 21-156 | MARKET 11.6% | 09:00 median 5.50 | Matchbook 8.80
    comment: Art Gallery won three and four starts back but has since slipped to a fifth, then a sixth last time out, and she returns after 26 days having run over today's trip and going before.
    DATA: model 12.6% | style Unknown | runs in data 3 | last 3: 30 Mar Kempton Flat 8f Standard To Slow 1/6; 26 Apr Wetherby Flat 7f Good To Firm 5/8; 30 Oct Dundalk (AW) (IRE) Flat 8f Standard 6/14 fig 81
    DATA for: Best recent form figure 81, 7 lb above field average; Has won at this trip or further
- I Bid You Ajou (hrs_37890356) | 5yo G | 135lb | OR 75 | draw 10 | jockey Gavin Ryan | trainer Mark Fahey (14d 1/4) | headgear - | last run 21 days | form 226003 | MARKET 10.4% | 09:00 median 8.00 | Matchbook 7.60
    comment: Third last time out and twice second in the six runs before that, he arrives fresh after 21 days and has run over today's trip and going. Yet to win in his last six starts, though, which is the main risk, and he carries 135 lb from draw 10.
    DATA: model 6.0% | style Midfield (led 4% of runs) | runs in data 12 | last 3: 13 Sep Curragh Flat 6f Yielding 22/24; 4 Oct Curragh Flat 6f Soft 10/22; 4 Nov Dundalk (AW) (IRE) Flat 6f Standard 3/9 fig 73
- Leveraging (hrs_55633830) | 3yo G | 130lb | OR 72 | draw 2 | jockey Robbie Colgan | trainer Ms Sheila Lavery (14d 0/3) | headgear - | last run 28 days | form 060751 | MARKET 8.0% | 09:00 median 7.50 | Matchbook 14.00
    comment: Leveraging won last time out, but that was his only success in his last six starts, with a fifth and a seventh before it, and he has run over today's trip and going.
    DATA: model 8.8% | style Leader (led 29% of runs) | runs in data 6 | last 3: 25 Sep Dundalk Flat 6f Standard 7/13; 9 Oct Dundalk Flat 7f Standard 5/14; 28 Oct Dundalk (AW) (IRE) Flat 8f Standard 1/12 fig 72
    DATA for: Has won at this trip or further
    DATA against: Pace: likely to be taken on for the lead
- Bishopton (hrs_43826930) | 4yo G | 140lb | OR 80 | draw 13 | jockey Nicola Burns(5) | trainer Miss Natalia Lupini (14d 1/6) | headgear - | last run 26 days | form 056505 | MARKET 7.5% | 09:00 median 8.50 | Matchbook 14.50
    comment: Bishopton was fifth last time out, 26 days ago, and has been consistent without a win in his last six, with a sixth four starts back among the finishes.
    DATA: model 6.6% | style Held up (led 5% of runs) | runs in data 7 | last 3: 8 Jul Fairyhouse Flat 7f Good 5/7; 9 Oct Dundalk Flat 8f Standard 13/13; 30 Oct Dundalk (AW) (IRE) Flat 8f Standard 5/14 fig 83
    DATA for: Best recent form figure 83, 9 lb above field average; Official rating 80, 6 lb above field average; Pace: a contested lead should suit its hold-up style
    DATA against: Carries 6 lb more than average
- Exquisite Acclaim (hrs_24907491) | 7yo G | 141lb | OR 81 | draw 11 | jockey Adam Caffrey | trainer Adrian McGuinness (14d 2/20) | headgear tp | last run 19 days | form 634255 | MARKET 7.0% | 09:00 median 11.00 | Matchbook 12.50
    comment: Exquisite Acclaim is winless in his last six, though he was second three starts back and has been fifth in his last two outings, so he's consistent without quite landing a blow. He has run over today's trip and going, and 19 days off is fine, but 141 lb from draw 11 asks plenty.
    DATA: model 10.0% | style Leader (led 57% of runs) | runs in data 16 | last 3: 9 Oct Dundalk Flat 8f Standard 2/13; 16 Oct Dundalk (AW) (IRE) Flat 7f Standard 5/12 fig 80; 6 Nov Dundalk (AW) (IRE) Flat 8f Standard 5/8 fig 76
    DATA for: Best recent form figure 80, 6 lb above field average; Official rating 81, 7 lb above field average
    DATA against: Carries 7 lb more than average; Aged 7, older than most of this field; Pace: likely to be taken on for the lead
- Lady In Gold (hrs_60527873) | 3yo F | 131lb | OR 73 | draw 12 | jockey J M Sheridan | trainer Joseph Patrick O'Brien (14d 5/30) | headgear - | last run 26 days | form 8198 | MARKET 5.9% | 09:00 median 13.00 | Matchbook 12.50
    comment: Lady In Gold has finished eighth and ninth in her last two outings, so she is hard to fancy, though a win three starts back shows she can score and she has run over today's trip and going before.
    DATA: model 6.3% | style Held up (led 4% of runs) | runs in data 4 | last 3: 20 Feb Dundalk Flat 8f Standard 1/14; 7 Oct Navan Flat 8.2f Yielding 9/9; 30 Oct Dundalk (AW) (IRE) Flat 8f Standard 8/14 fig 74
    DATA for: Has won at this trip or further; Pace: a contested lead should suit its hold-up style
- Frank Pickle (hrs_52641351) | 5yo G | 134lb | OR 74 | draw 15 | jockey Patrick McGettigan(5) | trainer Mrs Denise Foster (14d 0/2) | headgear - | last run 71 days | form 451870 | MARKET 3.8% | 09:00 median 19.00 | Matchbook 23.00
    comment: Frank Pickle won four starts back but has since finished an eighth, a seventh and then unplaced last time out, and he returns after 71 days off.
    DATA: model 5.2% | style Prominent (led 3% of runs) | runs in data 6 | last 3: 25 Jul Gowran Park Flat 8f Good 8/9; 2 Sep Navan Flat 8.1f Good 7/15; 15 Sep Punchestown Flat 8.1f Good 10/14
    DATA for: Has won at this trip or further
    DATA against: Last-run finishing speed -2.0% vs that field (faded); Poor recent finishing positions
- Tachos (hrs_35337617) | 5yo M | 131lb | OR 71 | draw 1 | jockey Chris Hayes | trainer D K Weld (14d 1/2) | headgear tp | last run 38 days | form 531033 | MARKET 3.3% | 09:00 median 17.00 | Matchbook 40.00
    comment: Tachos has finished third in each of her last two starts, and she has run over today's trip and going, but she hasn't won since four starts back and 131 lb from stall 1 is a big ask.
    DATA: model 4.3% | style Prominent (led 4% of runs) | runs in data 9 | last 3: 12 Sep Leopardstown Flat 8.3f Good 16/18; 1 Oct Bellewstown Flat 7.9f Soft To Heavy 3/5; 18 Oct Leopardstown (IRE) Flat 7f Good 3/14 fig 73
    DATA for: Has won at this trip or further; Good recent finishing positions
- Gotta Catch'em All (hrs_43385566) | 6yo G | 130lb | OR 70 | draw 8 | jockey Siobhan Rutledge | trainer H Rogers (14d 0/2) | headgear - | last run 21 days | form 293566 | MARKET 2.9% | 09:00 median 21.00 | Matchbook 42.00
    comment: He has run over today's trip and going and is fresh enough after 21 days, but 130 lb from stall eight is a lot to ask.
    DATA: model 4.3% | style Leader (led 29% of runs) | runs in data 12 | last 3: 2 Sep Navan Flat 5f Good 5/16; 5 Sep Navan Flat 5f Good 6/8; 4 Nov Dundalk (AW) (IRE) Flat 6f Standard 6/9 fig 66
    DATA against: Best recent form figure 66, 8 lb below field average; Pace: likely to be taken on for the lead
- New Radical (hrs_61649252) | 3yo G | 138lb | OR 80 | draw 3 | jockey James Ryan | trainer Jack W Davison (14d 0/1) | headgear - | last run 24 days | form 3170 | MARKET 2.8% | 09:00 median 26.00 | Matchbook 38.00
    comment: The risk is a poor recent return, unplaced last time and seventh two starts back, despite a fresh 24-day break.
    DATA: model 6.3% | style Midfield (led 3% of runs) | runs in data 4 | last 3: 11 Apr Bellewstown Flat 7.9f Soft 1/11; 17 May Naas Flat 8f Good 7/7; 1 Nov Curragh (IRE) Flat 7f Yielding To Soft 11/25 fig 80
    DATA for: Best recent form figure 80, 6 lb above field average; Official rating 80, 6 lb above field average; Has won at this trip or further
- Temperance (hrs_44721971) | 4yo F | 136lb | OR 76 | draw 14 | jockey Colin Keane | trainer Miss Kate McGivern (14d 0/0) | headgear b | last run 47 days | form 778738 | MARKET 2.7% | 09:00 median 34.00 | Matchbook 32.00
    comment: The risk is a poor run of finishes, with a third two starts back her best and an eighth last time out after 47 days off.
    DATA: model 4.5% | style Held up (led 8% of runs) | runs in data 8 | last 3: 26 Sep Curragh Flat 7f Yielding 7/10; 2 Oct Dundalk Flat 7f Standard 3/5; 9 Oct Dundalk Flat 8f Standard 8/13
    DATA for: Pace: a contested lead should suit its hold-up style
- Albion Power (hrs_39259878) | 5yo G | 122lb | OR 62 | draw 9 | jockey  | trainer Keith Henry Clarke (14d 0/0) | headgear - | last run 47 days | form -84900 | MARKET 2.7% | 09:00 median 19.00 | Matchbook 65.00
    comment: Winless in his last five, Albion Power was unplaced last time out and again two starts back, with a fourth four starts back his best recent effort, so he is hard to fancy after 47 days off.
    DATA: model 2.0% | style Midfield (led 23% of runs) | runs in data 5 | last 3: 24 May Curragh Flat 8f Good 9/19; 26 Jun Curragh Flat 8f Good 19/20; 9 Oct Dundalk Flat 7f Standard 10/14
    DATA for: Carries 12 lb less than average
    DATA against: Official rating 62, 12 lb below field average; Poor recent finishing positions
- Brewing (hrs_32597908) | 7yo G | 129lb | OR 69 | draw 7 | jockey Nestor Kashuba(10) | trainer Kevin Thomas Coleman (14d 0/5) | headgear - | last run 12 days | form 309400 | MARKET 1.3% | 09:00 median 51.00 | Matchbook 75.00
    comment: Brewing is winless in his last six and unplaced in his last two, but he has a fourth three starts back, has run over today's trip and going, and returns after just 12 days.
    DATA: model 1.5% | style Unknown | runs in data 9 | last 3: 19 May Cork Flat 7f Soft To Heavy 4/8; 16 Oct Dundalk (AW) (IRE) Flat 7f Standard 12/12 fig 56; 13 Nov Dundalk (AW) (IRE) Flat 10.5f Standard 10/10 fig 57
    DATA against: Best recent form figure 57, 17 lb below field average; Recent figures 12 lb below its current mark (looks high in the weights); Official rating 69, 5 lb below field average; Aged 7, older than most of this field

## 5:10 Dundalk (AW) | race_id rac_32305486876 | Now Racing Every Wednesday At Dundalk Maiden
Flat |  | 1m4f | going Standard | AW | 15 runners | rating band - | age 3yo+
DATA pace: Lone leader - Let's Smash It is the only habitual front-runner and may be allowed an easy lead.
- Let's Smash It (hrs_59367210) | 3yo G | 134lb | OR 79 | draw 8 | jockey Donagh O'Connor | trainer Robson De Aguiar (14d 2/8) | headgear - | last run 60 days | form -33495 | MARKET 52.1% | 09:00 median 1.57 | Matchbook 1.70
    DATA: model 34.6% | style Leader (led 54% of runs) | runs in data 5 | last 3: 22 Aug Curragh Flat 10f Good 4/12; 2 Sep Navan Flat 8.1f Good 9/13; 26 Sep Curragh Flat 10f Yielding 5/18
    DATA for: Official rating 79, 10 lb above field average; Trainer 25% wins (2/8), last 14 days; Pace: may get an uncontested lead
- Copper Dog (hrs_17392946704) | 3yo G | 134lb | OR - | draw 5 | jockey Ben Coen | trainer J. P. Murtagh (14d 1/8) | headgear tb (1st time) | last run 60 days | form 0 | MARKET 12.4% | 09:00 median 6.50 | Matchbook 7.20
    DATA: model 4.2% | style Held up (led 8% of runs) | runs in data 1 | last 3: 26 Sep Curragh Flat 10f Yielding 12/18
    DATA for: First-time headgear
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Kigalienne (hrs_17391396806) | 3yo F | 129lb | OR - | draw 11 | jockey Colin Keane | trainer Mrs J. Harrington (14d 1/9) | headgear p | last run 7 days | form 03 | MARKET 10.6% | 09:00 median 6.50 | Matchbook 10.00
    DATA: model 4.2% | style Held up (led 8% of runs) | runs in data 2 | last 3: 8 Sep Galway Flat 12f Soft 17/17; 18 Nov Dundalk (AW) (IRE) Flat 12f Standard 3/9 fig 64
    DATA for: Best recent form figure 64, 9 lb above field average
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Meet The Day (hrs_17395964103) | 3yo G | 134lb | OR - | draw 2 | jockey Luke McAteer | trainer J S Bolger (14d 0/2) | headgear - | last run - days | form - | MARKET 4.8% | 09:00 median 17.00 | Matchbook 21.00
    DATA: model 3.2% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Ossie's Lodge (hrs_34457073) | 7yo G | 139lb | OR - | draw 14 | jockey Robbie Colgan | trainer A. J. Martin (14d 0/7) | headgear - | last run 894 days | form 4/ | MARKET 4.4% | 09:00 median 13.00 | Matchbook 30.00
    DATA: model 3.3% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 894-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Lilannbee (hrs_56746270) | 5yo M | 134lb | OR - | draw 6 | jockey Siobhan Rutledge | trainer S G Carey (14d 2/5) | headgear - | last run 24 days | form 5 | MARKET 3.0% | 09:00 median 23.00 | Matchbook 44.00
    DATA: model 7.8% | style Prominent (led 23% of runs) | runs in data 6 | last 3: 9 Aug Downpatrick Hurdle 17.8f Good 4/7; 5 Oct Fairyhouse Hurdle 16f Good 2/6; 1 Nov Curragh (IRE) Flat 12f Yielding 5/19 fig 62
    DATA for: Best recent form figure 62, 7 lb above field average; Trainer 40% wins (2/5), last 14 days; Last-run finishing speed +5.2% vs that field (finished strongly)
- Seventh Sea (hrs_17391323796) | 3yo F | 129lb | OR - | draw 7 | jockey Chris Hayes | trainer D K Weld (14d 1/2) | headgear t (1st time) | last run 60 days | form 0 | MARKET 2.9% | 09:00 median 23.00 | Matchbook 44.00
    DATA: model 3.9% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 26 Sep Curragh Flat 9f Yielding 12/17
    DATA for: First-time headgear
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Yolanda Be Cool (hrs_17395966189) | 3yo F | 129lb | OR - | draw 10 | jockey Jimmy Dalton(7) | trainer A. Slattery (14d 0/14) | headgear - | last run - days | form - | MARKET 2.2% | 09:00 median 29.00 | Matchbook 60.00
    DATA: model 3.2% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Trainer 0 wins from 14 runs, last 14 days; Lightly raced: 0 runs in our data, so the model has little to go on
- Monodora (hrs_17395965146) | 3yo F | 129lb | OR - | draw 3 | jockey Gavin Ryan | trainer Mark Fahey (14d 1/4) | headgear - | last run - days | form - | MARKET 2.1% | 09:00 median 29.00 | Matchbook 80.00
    DATA: model 3.2% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Sierra's Dream (hrs_17390243248) | 4yo F | 134lb | OR - | draw 12 | jockey James Ryan | trainer T G McCourt (14d 1/7) | headgear - | last run 7 days | form 05 | MARKET 1.7% | 09:00 median 34.00 | Matchbook 100.00
    DATA: model 1.8% | style Midfield (led 5% of runs) | runs in data 4 | last 3: 19 Sep Navan NH Flat 15.8f Good 8/13; 23 Oct Dundalk (AW) (IRE) Flat 10.5f Standard 14/14 fig 31; 18 Nov Dundalk (AW) (IRE) Flat 12f Standard 5/9 fig 64
    DATA for: Best recent form figure 64, 9 lb above field average
- Sargent Lightfoot (hrs_20085632) | 12yo G | 139lb | OR 95 | draw 13 | jockey Seamie Heffernan | trainer Sabrina J Harty (14d 0/0) | headgear - | last run 24 days | form 8 | MARKET 1.3% | 09:00 median 41.00 | Matchbook 150.00
    DATA: model 19.9% | style Held up (led 8% of runs) | runs in data 1 | last 3: 1 Nov Curragh (IRE) Flat 12f Yielding 8/19 fig 56
    DATA for: Official rating 95, 26 lb above field average; Last-run finishing speed +4.2% vs that field (finished strongly)
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on; Aged 12, older than most of this field
- Ferreshana (hrs_17395281981) | 3yo F | 129lb | OR - | draw 9 | jockey Adam Caffrey | trainer Daniel James Murphy (14d 1/5) | headgear - | last run 14 days | form 0 | MARKET 0.9% | 09:00 median 67.00 | Matchbook 200.00
    DATA: model 3.5% | style Unknown | runs in data 1 | last 3: 11 Nov Dundalk (AW) (IRE) Flat 8f Standard 10/13 fig 36
    DATA for: Trainer 20% wins (1/5), last 14 days
    DATA against: Best recent form figure 36, 19 lb below field average; Lightly raced: 1 run in our data, so the model has little to go on
- The Lodge Lane (hrs_17390039863) | 4yo F | 134lb | OR - | draw 4 | jockey R. P. Cleary | trainer Peter Lawlor (14d 0/1) | headgear - | last run 10 days | form - | MARKET 0.7% | 09:00 median 81.00 | Matchbook 240.00
    DATA: model 5.2% | style Held up (led 5% of runs) | runs in data 3 | last 3: 8 Aug Wexford NH Flat 16f Good 3/7; 24 Aug Ballinrobe NH Flat 16.2f Good 11/11; 15 Nov Navan (IRE) NH Flat 16f Good To Yielding 8/8
- Cape Blue Point (hrs_17393889576) | 3yo F | 129lb | OR - | draw 1 | jockey J M Sheridan | trainer Denis Gerard Hogan (14d 0/11) | headgear t | last run 26 days | form 80 | MARKET 0.4% | 09:00 median 151.00 | Matchbook 450.00
    DATA: model 1.6% | style Unknown | runs in data 2 | last 3: 16 Oct Dundalk (AW) (IRE) Flat 6f Standard 8/9 fig 49; 30 Oct Dundalk (AW) (IRE) Flat 8f Standard 11/14 fig 37
    DATA against: Best recent form figure 49, 6 lb below field average; Trainer 0 wins from 11 runs, last 14 days; Lightly raced: 2 runs in our data, so the model has little to go on
- Threebiggulps (hrs_63069678) | 3yo G | 134lb | OR 33 | draw 15 | jockey  | trainer J G Coogan (14d 0/0) | headgear h | last run 22 days | form 009909 | MARKET 0.4% | 09:00 median 201.00 | Matchbook 450.00
    DATA: model 0.7% | style Prominent (led 5% of runs) | runs in data 7 | last 3: 2 Jul Bellewstown Flat 8f Good 11/15; 15 Aug Dundalk Flat 10.7f Standard 9/14; 3 Nov Fairyhouse (IRE) Hurdle 16f Good To Yielding 11/13
    DATA against: Official rating 33, 36 lb below field average; Last-run finishing speed -9.3% vs that field (faded); Poor recent finishing positions

## 5:40 Dundalk (AW) | race_id rac_32305488813 | Floodlit Fridays At Dundalk (Q.R.) Handicap
Flat |  | 1m4f | going Standard | AW | 11 runners | rating band - | age 3yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Letiza (hrs_34333677) | 6yo M | 163lb | OR 74 | draw 7 | jockey Mr A P Ryan(3) | trainer A. Slattery (14d 0/14) | headgear - | last run 12 days | form 244164 | MARKET 17.1% | 09:00 median 5.00 | Matchbook 5.10 | CHECK (skip line 4.75)
    comment: Fourth last time out just 12 days ago, Letiza has been consistent, with a win three starts back and a second six starts back, and she has run over today's trip and going.
    DATA: model 19.5% | style Midfield (led 4% of runs) | runs in data 6 | last 3: 31 Aug Roscommon Flat 12.1f Good To Yielding 1/15; 11 Oct Naas Flat 10.7f Soft 6/11; 13 Nov Dundalk (AW) (IRE) Flat 10.5f Standard 4/10 fig 73
    DATA for: Official rating 74, 6 lb above field average; Has won at this trip or further
    DATA against: Trainer 0 wins from 14 runs, last 14 days; Carries 5 lb more than average
- Granville Street (hrs_27902630) | 8yo G | 162lb | OR 73 | draw 1 | jockey Mr D McGill(5) | trainer Ciaran Murphy (14d 0/5) | headgear b | last run 15 days | form 548032 | MARKET 17.1% | 09:00 median 5.00 | Matchbook 5.10
    comment: Granville Street arrives in fair heart, second last time out and third two starts back after just 15 days off, and he has run over today's trip and going.
    DATA: model 19.8% | style Midfield (led 3% of runs) | runs in data 13 | last 3: 8 Oct Thurles Flat 16.6f Yielding To Soft 3/13; 15 Oct Curragh (IRE) Flat 14f Yielding To Soft 2/21 fig 74; 10 Nov Fairyhouse (IRE) Hurdle 20.5f Good To Yielding 3/11 fig 112
    DATA for: Official rating 73, 5 lb above field average; Good recent finishing positions
- Ozark Daze (hrs_36095451) | 5yo G | 154lb | OR 65 | draw 3 | jockey Mr J L Gleeson | trainer Gearoid O'Loughlin (14d 0/0) | headgear t | last run 22 days | form 04624- | MARKET 14.7% | 09:00 median 5.00 | Matchbook 6.80
    comment: Fourth last time out, and a second two starts back, show Ozark Daze is running with credit after 22 days off, and he has run over today's trip and going before. Yet to win in his last five, he carries 154 lb off 65, which looks the sticking point.
    DATA: model 3.8% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 25 Sep Listowel Hurdle 18.6f Good To Yielding 6/15; 22 Oct Clonmel (IRE) Hurdle 17f Good To Yielding 9/12; 3 Nov Fairyhouse (IRE) Hurdle 16f Good To Yielding 7/15 fig 98
    DATA for: Last-run finishing speed +3.1% vs that field (finished strongly)
    DATA against: Poor recent finishing positions
- Wandering Rocks (hrs_29906800) | 7yo G | 159lb | OR 70 | draw 6 | jockey Mr T McGuinness(7) | trainer William Durkan (14d 0/2) | headgear tv | last run 28 days | form 538556 | MARKET 11.0% | 09:00 median 8.00 | Matchbook 8.00
    comment: Wandering Rocks has run over today's trip and going, and a third five starts back is his best finish in a winless recent spell, though he was sixth last time out after 28 days off.
    DATA: model 8.6% | style Midfield (led 4% of runs) | runs in data 9 | last 3: 18 Sep Dundalk Flat 12f Standard 5/10; 9 Oct Dundalk Flat 12f Standard 5/7; 28 Oct Dundalk (AW) (IRE) Flat 12f Standard 6/13 fig 69
- Friary Road (hrs_44295391) | 6yo G | 161lb | OR 72 | draw 8 | jockey Mr L P Shanahan(7) | trainer T M Walsh (14d 0/2) | headgear t | last run 33 days | form 39-327 | MARKET 9.5% | 09:00 median 8.50 | Matchbook 9.80
    comment: Friary Road is yet to win in his last five starts but has been in the frame, a second two starts back and a third three starts back, and he has run over today's trip and going before.
    DATA: model 17.5% | style Held up (led 5% of runs) | runs in data 5 | last 3: 23 Jul Leopardstown Flat 15f Good 2/9; 2 Sep Navan Flat 16f Good 7/16; 23 Oct Sligo (IRE) Hurdle 17.5f Yielding 3/5
    DATA for: Good recent finishing positions
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Big Dispute (hrs_34678483) | 7yo G | 151lb | OR 62 | draw 2 | jockey Mr Finian Maguire | trainer Kevin Thomas Coleman (14d 0/5) | headgear - | last run 114 days | form 6900 | MARKET 7.8% | 09:00 median 10.00 | Matchbook 12.00
    comment: Big Dispute is winless in his last four, unplaced twice most recently after a ninth three starts back, and he returns from 114 days off carrying 151 lb, so he is hard to fancy.
    DATA: model 2.2% | style Held up (led 4% of runs) | runs in data 6 | last 3: 22 Jun Ballinrobe Flat 9.7f Yielding 9/10; 7 Jul Tramore Flat 12f Good 10/10; 3 Aug Naas Flat 10.8f Good 11/11
    DATA for: Carries 7 lb less than average
    DATA against: Official rating 62, 6 lb below field average; Poor recent finishing positions; Returns from a 114-day break; Pace: steady gallop likely, hard to come from off the pace
- Palmezzano (hrs_46697357) | 4yo G | 161lb | OR 72 | draw 11 | jockey Mr H C Swan | trainer Denis Gerard Hogan (14d 0/11) | headgear p | last run 26 days | form 4-4619 | MARKET 7.1% | 09:00 median 11.00 | Matchbook 15.00
    comment: Palmezzano won two starts back and has run over today's trip and on this going, so a ninth last time out looks forgivable after 26 days off.
    DATA: model 9.5% | style Midfield (led 4% of runs) | runs in data 4 | last 3: 28 Jan Dundalk Flat 10.7f Standard 6/8; 13 Feb Dundalk Flat 12f Standard 1/10; 30 Oct Dundalk (AW) (IRE) Flat 12f Standard 9/9 fig 57
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 57, 14 lb below field average; Recent figures 15 lb below its current mark (looks high in the weights); Trainer 0 wins from 11 runs, last 14 days
- The Mediator (hrs_23921618) | 9yo G | 168lb | OR 79 | draw 4 | jockey Ms C E O'Ryan(7) | trainer Gordon Elliott (14d 12/82) | headgear - | last run 36 days | form 450546 | MARKET 6.9% | 09:00 median 9.00 | Matchbook 20.00
    DATA: model 9.1% | style Held up (led 3% of runs) | runs in data 9 | last 3: 4 Oct Curragh Flat 12f Yielding 4/12; 14 Oct Punchestown (IRE) Hurdle 20f Good 10/13 fig 98; 20 Oct Curragh (IRE) Flat 12f Yielding 6/8 fig 82
    DATA for: Best recent form figure 82, 11 lb above field average; Official rating 79, 11 lb above field average
    DATA against: Carries 10 lb more than average; Pace: steady gallop likely, hard to come from off the pace
- Western Bandit (hrs_63422632) | 4yo C | 153lb | OR 64 | draw 5 | jockey Mr D Doyle(5) | trainer Luke W Comer (14d 0/0) | headgear t | last run 118 days | form 577300 | MARKET 4.4% | 09:00 median 19.00 | Matchbook 20.00
    comment: Without a win in his last six outings and unplaced in his last two, Western Bandit is hard to fancy, and 118 days off the track raises fitness questions too.
    DATA: model 3.3% | style Held up (led 3% of runs) | runs in data 7 | last 3: 22 Jun Ballinrobe Flat 9.7f Yielding 3/10; 11 Jul Limerick Flat 6.7f Good 10/11; 30 Jul Galway Flat 12f Yielding To Soft 17/17
    DATA against: Last-run finishing speed -4.6% vs that field (faded); Returns from a 118-day break; Pace: steady gallop likely, hard to come from off the pace
- Eskimo Komet (hrs_27427876) | 7yo C | 156lb | OR 67 | draw 10 | jockey Mr B M Coonan(7) | trainer Luke W Comer (14d 0/0) | headgear - | last run 866 days | form 34839/ | MARKET 3.2% | 09:00 median 23.00 | Matchbook 38.00
    comment: Eskimo Komet has been placed twice in his last five, a third two starts back and another five starts back, and he has run over today's trip and going before.
    DATA: model 6.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 866-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Chain Of Destiny (hrs_31660741) | 7yo G | 147lb | OR 48 | draw 9 | jockey Mr W T Ladd Finn(7) | trainer David Edward Finn (14d 0/1) | headgear b (1st time) | last run 134 days | form 96/950 | MARKET 1.2% | 09:00 median 81.00 | Matchbook 95.00
    comment: Chain Of Destiny is winless in his last five, with a fifth two starts back his best finish, and he returns after 134 days off carrying 147 lb.
    DATA: model 0.4% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 12 May Killarney Flat 16.8f Good 9/9; 31 May Listowel Flat 13.4f Good 5/6; 14 Jul Killarney Flat 14.2f Good 12/12
    DATA for: Carries 11 lb less than average; First-time headgear
    DATA against: Official rating 48, 20 lb below field average; Last-run finishing speed -6.8% vs that field (faded); Returns from a 134-day break
