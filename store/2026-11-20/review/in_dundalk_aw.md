# Card review packet: Dundalk (AW), 2026-11-20

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


## 4:45 Dundalk (AW) | race_id rac_32305045240 | Irishinjuredjockeys.com Nursery Handicap
Flat |  | 0m5f0y | going Standard | AW | 9 runners | rating band - | age 2yo
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Premier View (hrs_65642381) | 2yo G | 140lb | OR 82 | draw 7 | jockey Conor Cusack(7) | trainer Henry de Bromhead (14d 8/38) | headgear t | last run 28 days | form 8112 | MARKET 24.3% | 09:00 median 3.50 | Matchbook 3.75 | CHECK (skip line 3.32)
    DATA: model 41.3% | style Midfield (led 4% of runs) | runs in data 4 | last 3: 4 Sep Down Royal Flat 5f Good 1/11; 28 Sep Down Royal Flat 5f Good To Yielding 1/6; 23 Oct Dundalk (AW) (IRE) Flat 5f Standard 2/10 fig 85
    DATA for: Best recent form figure 85, 23 lb above field average; Official rating 82, 14 lb above field average; Trainer 21% wins (8/38), last 14 days; Has won at this trip or further; Good recent finishing positions
    DATA against: Carries 11 lb more than average
- Sapphire Sun (hrs_17391290420) | 2yo F | 132lb | OR 74 | draw 4 | jockey Ben Coen | trainer J. P. Murtagh (14d 1/8) | headgear - | last run 21 days | form 604 | MARKET 21.1% | 09:00 median 4.00 | Matchbook 4.40
    comment: Winless in her last three, Sapphire Sun was a fourth last time out after an unplaced run and a sixth, so she is hard to fancy at 132 lb from draw 4.
    DATA: model 6.0% | style Midfield (led 8% of runs) | runs in data 3 | last 3: 23 Aug Naas Flat 5.9f Good 6/15; 13 Sep Curragh Flat 6.3f Yielding 12/15; 30 Oct Dundalk (AW) (IRE) Flat 5f Standard 4/13 fig 46
    DATA for: Official rating 74, 6 lb above field average
    DATA against: Best recent form figure 46, 16 lb below field average; Recent figures 28 lb below its current mark (looks high in the weights)
- Invincible Irish (hrs_17389030239) | 2yo G | 119lb | OR 60 | draw 3 | jockey Nathan Crosse | trainer Daniel McLoughlin (14d 1/7) | headgear p | last run 9 days | form 007422 | MARKET 20.7% | 09:00 median 4.00 | Matchbook 4.50
    comment: Fresh from back-to-back seconds, and out again just nine days later, Invincible Irish is in cracking nick, and he has run over today's trip and on this going before. The one concern is that he is yet to win in his last six starts, and 119 lb leaves little in hand.
    DATA: model 7.8% | style Midfield (led 4% of runs) | runs in data 6 | last 3: 17 Sep Naas Flat 5f Yielding 4/14; 28 Sep Down Royal Flat 5f Good To Yielding 2/6; 11 Nov Dundalk (AW) (IRE) Flat 6f Standard 2/8 fig 71
    DATA for: Best recent form figure 71, 9 lb above field average; Recent figures 11 lb above its current mark (looks well handicapped); Last-run finishing speed +2.8% vs that field (finished strongly); Good recent finishing positions; Carries 10 lb less than average
    DATA against: Official rating 60, 8 lb below field average
- Rejoinder (hrs_65451442) | 2yo G | 137lb | OR 79 | draw 2 | jockey Patrick McGettigan(5) | trainer Robson De Aguiar (14d 1/4) | headgear - | last run 21 days | form 9428 | MARKET 10.7% | 09:00 median 8.00 | Matchbook 8.60
    comment: Rejoinder was beaten into eighth last time out, but a second two starts back shows he has a bit of ability, and he has run over today's trip and going before.
    DATA: model 13.1% | style Held up (led 4% of runs) | runs in data 4 | last 3: 11 Oct Naas Flat 5.9f Soft 4/7; 20 Oct Curragh (IRE) Flat 6f Yielding 2/13 fig 64; 30 Oct Dundalk (AW) (IRE) Flat 5f Standard 8/13 fig 42
    DATA for: Official rating 79, 11 lb above field average
    DATA against: Recent figures 15 lb below its current mark (looks high in the weights); Carries 8 lb more than average; Pace: steady gallop likely, hard to come from off the pace
- Matriarchal (hrs_63323295) | 2yo F | 137lb | OR 79 | draw 6 | jockey Chris Hayes | trainer Josh Halley (14d 0/2) | headgear h | last run 7 days | form 315706 | MARKET 9.3% | 09:00 median 9.00 | Matchbook 10.00
    comment: The risk is a poor recent run, with a sixth last time out and nothing better than a fifth since.
    DATA: model 10.2% | style Prominent (led 38% of runs) | runs in data 7 | last 3: 4 Jul Naas Flat 5f Good 7/10; 2 Oct Dundalk Flat 5f Standard 11/13; 13 Nov Dundalk (AW) (IRE) Flat 6f Standard 6/11 fig 57
    DATA for: Official rating 79, 11 lb above field average; Has won at this trip or further
    DATA against: Best recent form figure 57, 5 lb below field average; Recent figures 22 lb below its current mark (looks high in the weights); Poor recent finishing positions; Carries 8 lb more than average
- Space Dreamer (hrs_65161439) | 2yo F | 135lb | OR 77 | draw 1 | jockey James Ryan | trainer Conor David Maxwell (14d 0/2) | headgear - | last run 27 days | form 551152 | MARKET 6.9% | 09:00 median 11.00 | Matchbook 15.00
    comment: Space Dreamer arrives in good heart, second last time out and a winner three and four starts back, and she has run over today's trip and going before; the one concern is a fifth two starts back, so she must prove that was a blip from stall one under 135 lb.
    DATA: model 15.6% | style Held up (led 4% of runs) | runs in data 6 | last 3: 12 Sep Bath Flat 5f Good 1/10; 20 Sep Hamilton Flat 5f Heavy 5/7; 24 Oct Southwell (AW) Flat 5f Standard 2/4 fig 70
    DATA for: Best recent form figure 70, 8 lb above field average; Official rating 77, 9 lb above field average; Has won at this trip or further; Good recent finishing positions
    DATA against: Recent figures 7 lb below its current mark (looks high in the weights); Carries 6 lb more than average; Pace: steady gallop likely, hard to come from off the pace
- Sorrento Sunset (hrs_17391301893) | 2yo F | 119lb | OR 55 | draw 9 | jockey W. M. Lordan | trainer Daniel McLoughlin (14d 1/7) | headgear - | last run 2 days | form 0699 | MARKET 3.1% | 09:00 median 32.00 | Matchbook 32.00
    comment: Sorrento Sunset is hard to fancy, having finished ninth last time out and ninth two starts back, and she is winless in her last four, though she has run over today's trip and going before.
    DATA: model 3.3% | style Held up (led 4% of runs) | runs in data 4 | last 3: 4 Sep Down Royal Flat 5f Good 6/11; 29 Sep Cork Flat 5f Soft 9/12; 18 Nov Dundalk (AW) (IRE) Flat 7f Standard 9/12 fig 47
    DATA for: Carries 10 lb less than average
    DATA against: Best recent form figure 47, 15 lb below field average; Recent figures 8 lb below its current mark (looks high in the weights); Official rating 55, 13 lb below field average; Poor recent finishing positions; Pace: steady gallop likely, hard to come from off the pace
- Boysofwallstreet (hrs_64847300) | 2yo C | 123lb | OR 65 | draw 8 | jockey Sean Davis | trainer Sean Davis (14d 0/0) | headgear tv | last run 30 days | form 6580 | MARKET 2.1% | 09:00 median 41.00 | Matchbook 60.00
    comment: Boysofwallstreet is winless in his last four, finishing unplaced last time, an eighth two starts back, a fifth three starts back and a sixth four starts back, after 30 days off.
    DATA: model 2.2% | style Midfield (led 4% of runs) | runs in data 4 | last 3: 27 Jul Windsor Flat 6.1f Good To Firm 5/7; 29 Aug Windsor Flat 6.1f Soft 8/9; 21 Oct Kempton (AW) Flat 7f Standard / Slow 14/14 fig 53
    DATA for: Carries 6 lb less than average
    DATA against: Best recent form figure 53, 9 lb below field average; Recent figures 12 lb below its current mark (looks high in the weights)
- Mickian Thomas (hrs_17390956660) | 2yo C | 119lb | OR 44 | draw 5 | jockey Rory Mulligan(5) | trainer Rory Anthony Devine (14d 1/2) | headgear p | last run 44 days | form 0607 | MARKET 2.0% | 09:00 median 51.00 | Matchbook 55.00
    comment: Mickian Thomas is hard to fancy: he was seventh last time out, and before that came unplaced, a sixth three starts back and unplaced again, so he is winless in his last four.
    DATA: model 0.4% | style Prominent (led 29% of runs) | runs in data 4 | last 3: 27 Aug Navan Flat 8.1f Good 6/6; 15 Sep Punchestown Flat 8.1f Good 14/14; 7 Oct Navan Flat 5.8f Yielding 7/10
    DATA for: Carries 10 lb less than average
    DATA against: Official rating 44, 24 lb below field average; Poor recent finishing positions

## 5:15 Dundalk (AW) | race_id rac_32305047177 | Now Racing Every Wednesday At Dundalk Handicap
Flat |  | 0m6f0y | going Standard | AW | 17 runners | rating band 0-60 | age 3yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Surpass And Shine (hrs_37110843) | 5yo G | 142lb | OR 60 | draw 2 | jockey Robyn Donaghue-Leahy(7) | trainer Patrick J Flynn (14d 1/8) | headgear - | last run 28 days | form -00001 | MARKET 22.9% | 09:00 median 3.00 | Matchbook 3.30 | CHECK (skip line 2.85)
    comment: Won last time out after four unplaced runs, and he's fresh enough at 28 days, having run over today's trip and going before.
    DATA: model 13.7% | style Midfield (led 5% of runs) | runs in data 5 | last 3: 5 Sep Navan Flat 5f Good 14/18; 29 Sep Cork Flat 6f Soft 10/19; 23 Oct Dundalk (AW) (IRE) Flat 6f Standard 1/14 fig 55
    DATA for: Best recent form figure 55, 7 lb above field average; Official rating 60, 9 lb above field average; Has won at this trip or further
    DATA against: Carries 9 lb more than average
- One Cool Bear (hrs_53960053) | 3yo G | 142lb | OR 60 | draw 13 | jockey Patrick McGettigan(5) | trainer Adrian McGuinness (14d 4/19) | headgear p | last run 9 days | form 177323 | MARKET 9.6% | 09:00 median 7.00 | Matchbook 8.20
    comment: One Cool Bear arrives in solid form, third last time out and a second two starts back, and he's fit after just nine days off, with experience of today's trip and going. The risk is the 142 lb he carries from draw 13, with his own figure of 59 sitting just below his official mark of 60.
    DATA: model 20.0% | style Midfield (led 5% of runs) | runs in data 14 | last 3: 21 Oct Navan (IRE) Flat 6f Yielding 3/21 fig 69; 30 Oct Dundalk (AW) (IRE) Flat 5f Standard 2/14 fig 61; 11 Nov Dundalk (AW) (IRE) Flat 5f Standard 3/13 fig 63
    DATA for: Best recent form figure 69, 21 lb above field average; Recent figures 9 lb above its current mark (looks well handicapped); Official rating 60, 9 lb above field average; Trainer 21% wins (4/19), last 14 days; Good recent finishing positions
    DATA against: Carries 9 lb more than average
- The Cosy Corner (hrs_55700785) | 3yo F | 128lb | OR 46 | draw 5 | jockey Ben Coen | trainer Patrick Magee (14d 0/7) | headgear p | last run 28 days | form 9-0043 | MARKET 8.8% | 09:00 median 7.50 | Matchbook 9.80
    comment: Winless in her last five, The Cosy Corner is hard to fancy, though a third last time out, and a fourth two starts back, show she is heading the right way, and she has run over today's trip and going.
    DATA: model 5.9% | style Midfield (led 4% of runs) | runs in data 4 | last 3: 24 Jul Cork Flat 6f Good To Firm 10/19; 2 Oct Dundalk Flat 5f Standard 4/12; 23 Oct Dundalk (AW) (IRE) Flat 6f Standard 3/14 fig 45
    DATA for: Carries 5 lb less than average
    DATA against: Official rating 46, 5 lb below field average
- Subiaco (hrs_55061699) | 3yo G | 136lb | OR 54 | draw 16 | jockey R. P. Cleary | trainer Miss Jennifer Anne Lynch (14d 0/0) | headgear - | last run 21 days | form 408033 | MARKET 8.0% | 09:00 median 8.50 | Matchbook 9.80
    comment: Subiaco arrives in decent heart after back-to-back thirds, and he has run over today's trip and going, but he is yet to win in his last six starts and carries 136 lb off an official mark of 54.
    DATA: model 9.5% | style Prominent (led 5% of runs) | runs in data 7 | last 3: 5 Jun Fairyhouse Flat 6f Good 10/17; 2 Oct Dundalk Flat 5f Standard 3/12; 30 Oct Dundalk (AW) (IRE) Flat 5f Standard 3/14 fig 55
    DATA for: Best recent form figure 55, 7 lb above field average; Good recent finishing positions
- Sovereign Banter (hrs_42226079) | 4yo G | 133lb | OR 51 | draw 1 | jockey Jimmy Dalton(7) | trainer A. Slattery (14d 0/13) | headgear tb | last run 28 days | form 420002 | MARKET 7.6% | 09:00 median 9.00 | Matchbook 11.00
    comment: Sovereign Banter was second last time out and has run over today's trip and going, but he's winless in his last six and unplaced in the three runs before that second, so consistency is the question.
    DATA: model 4.0% | style Midfield (led 4% of runs) | runs in data 8 | last 3: 11 Jul Limerick Flat 6.7f Good 12/14; 24 Jul Cork Flat 6f Good To Firm 11/19; 23 Oct Dundalk (AW) (IRE) Flat 6f Standard 2/14 fig 50
    DATA against: Trainer 0 wins from 13 runs, last 14 days
- Treasured Royal (hrs_55882253) | 3yo F | 134lb | OR 52 | draw 4 | jockey Robert Whearty | trainer Gavin Cromwell (14d 4/34) | headgear t | last run 9 days | form 000055 | MARKET 5.6% | 09:00 median 13.00 | Matchbook 13.50
    comment: Treasured Royal is yet to win in her last six, though back-to-back fifths show a filly edging closer, and she's fresh from a run nine days ago with experience of today's trip and going.
    DATA: model 5.5% | style Held up (led 5% of runs) | runs in data 13 | last 3: 7 Oct Navan Flat 5.8f Yielding 16/22; 30 Oct Dundalk (AW) (IRE) Flat 5f Standard 5/14 fig 52; 11 Nov Dundalk (AW) (IRE) Flat 5f Standard 5/13 fig 54
    DATA for: Best recent form figure 54, 6 lb above field average
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Zabriskie Point (hrs_35625681) | 5yo G | 132lb | OR 50 | draw 9 | jockey Adam Caffrey | trainer Adrian McGuinness (14d 4/19) | headgear tv | last run 20 days | form 753587 | MARKET 5.1% | 09:00 median 12.00 | Matchbook 17.00
    comment: Zabriskie Point has been beaten in his last two, a seventh last time out and an eighth two starts back, though a third four starts back shows he can reach the frame, and he has run over today's trip and going.
    DATA: model 4.9% | style Prominent (led 3% of runs) | runs in data 16 | last 3: 12 Oct Roscommon Flat 7.5f Soft 5/13; 29 Oct Southwell (AW) Flat 7f Standard 8/13 fig 47; 31 Oct Southwell (AW) Flat 8f Standard 7/14 fig 48
    DATA for: Trainer 21% wins (4/19), last 14 days
- Steel Magnolia (hrs_47555445) | 4yo F | 131lb | OR 49 | draw 17 | jockey W. J. Lee | trainer W. McCreery (14d 0/3) | headgear v | last run 21 days | form 213406 | MARKET 4.8% | 09:00 median 13.00 | Matchbook 17.50
    comment: Steel Magnolia was a sixth last time out after an unplaced effort before that, though she won five starts back and has run over today's trip and going.
    DATA: model 3.9% | style Midfield (led 4% of runs) | runs in data 10 | last 3: 1 Oct Bellewstown Flat 5f Soft To Heavy 4/9; 15 Oct Curragh (IRE) Flat 5f Soft 14/17 fig 39; 30 Oct Dundalk (AW) (IRE) Flat 5f Standard 6/14 fig 47
- El Fontenaro (hrs_412692735) | 4yo F | 138lb | OR 56 | draw 14 | jockey Nathan Crosse | trainer Jarlath P Fahey (14d 0/1) | headgear - | last run 16 days | form 215503 | MARKET 4.7% | 09:00 median 13.00 | Matchbook 18.50
    comment: El Fontenaro was third last time out, just 16 days ago, and she has run over today's trip and on this going before.
    DATA: model 6.7% | style Midfield (led 4% of runs) | runs in data 9 | last 3: 1 Oct Bellewstown Flat 5f Soft To Heavy 5/9; 21 Oct Navan (IRE) Flat 6f Yielding 13/21 fig 48; 4 Nov Dundalk (AW) (IRE) Flat 7f Standard 3/13 fig 59
    DATA for: Best recent form figure 59, 11 lb above field average; Has won at this trip or further
- This Guy (hrs_51897622) | 3yo G | 139lb | OR 57 | draw 8 | jockey  | trainer Mark Fahey (14d 1/7) | headgear tp | last run 154 days | form 567846 | MARKET 4.7% | 09:00 median 13.00 | Matchbook 18.50
    comment: The risk is a 154-day absence after a sixth last time out, in a run of six outings without a win.
    DATA: model 6.0% | style Midfield (led 4% of runs) | runs in data 8 | last 3: 4 May Curragh Flat 6f Good 8/20; 29 May Down Royal Flat 5f Good 4/10; 19 Jun Down Royal Flat 5f Soft 6/7
    DATA for: Official rating 57, 6 lb above field average
    DATA against: Carries 6 lb more than average; Returns from a 154-day break
- Rodeeve (hrs_40746006) | 5yo M | 138lb | OR 56 | draw 15 | jockey Camillus Byrne(10) | trainer Michael J Browne (14d 0/1) | headgear p | last run 30 days | form 510030 | MARKET 3.8% | 09:00 median 17.00 | Matchbook 23.00
    comment: Rodeeve is a winner five starts back and a third two starts back, but she has been unplaced in her last run and two of the three before it, and she returns after 30 days.
    DATA: model 6.8% | style Midfield (led 3% of runs) | runs in data 8 | last 3: 16 Jul Leopardstown Flat 7.2f Good 10/14; 7 Oct Navan Flat 5.8f Yielding 3/22; 21 Oct Navan (IRE) Flat 6f Yielding 14/21 fig 46
    DATA for: Has won at this trip or further
    DATA against: Recent figures 10 lb below its current mark (looks high in the weights)
- Inishmot Prince (hrs_27166538) | 8yo G | 135lb | OR 53 | draw 6 | jockey James Ryan | trainer T G McCourt (14d 1/6) | headgear p | last run 28 days | form 558700 | MARKET 3.0% | 09:00 median 23.00 | Matchbook 28.00
    DATA: model 2.6% | style Held up (led 8% of runs) | runs in data 8 | last 3: 10 Sep Laytown Flat 6f Standard 7/9; 2 Oct Dundalk Flat 5f Standard 10/12; 23 Oct Dundalk (AW) (IRE) Flat 6f Standard 11/14 fig 46
    DATA for: Has won at this trip or further
    DATA against: Recent figures 7 lb below its current mark (looks high in the weights); Poor recent finishing positions; Aged 8, older than most of this field; Pace: steady gallop likely, hard to come from off the pace
- Spirit Of Eagles (hrs_31451448) | 6yo M | 125lb | OR 43 | draw 3 | jockey  | trainer William Delahunty (14d 0/0) | headgear - | last run 21 days | form 386890 | MARKET 2.5% | 09:00 median 34.00 | Matchbook 34.00
    comment: Winless in her last six, Spirit Of Eagles has finished unplaced, ninth and eighth in her last three runs, so she is hard to fancy, though a third six starts back and 21 days since her last outing are small positives.
    DATA: model 1.8% | style Held up (led 5% of runs) | runs in data 10 | last 3: 7 Aug Gowran Park Flat 7f Good 8/12; 10 Sep Laytown Flat 6f Standard 9/10; 30 Oct Dundalk (AW) (IRE) Flat 5f Standard 12/14 fig 34
    DATA for: Has won at this trip or further; Carries 8 lb less than average
    DATA against: Best recent form figure 34, 14 lb below field average; Recent figures 9 lb below its current mark (looks high in the weights); Official rating 43, 8 lb below field average; Poor recent finishing positions; Pace: steady gallop likely, hard to come from off the pace
- Are You In Or Out (hrs_37068157) | 5yo M | 126lb | OR 44 | draw 10 | jockey Sadhbh Tormey(7) | trainer Conor David Maxwell (14d 0/2) | headgear v (1st time) | last run 35 days | form 800400 | MARKET 2.4% | 09:00 median 34.00 | Matchbook 36.00
    comment: Winless in her last six, Are You In Or Out has been unplaced in three of her last four, with a fourth three starts back her best finish in that spell, so she is hard to fancy.
    DATA: model 2.1% | style Held up (led 4% of runs) | runs in data 9 | last 3: 30 Sep Bellewstown Flat 7.9f Soft To Heavy 4/14; 7 Oct Navan Flat 5.8f Yielding 19/22; 16 Oct Dundalk (AW) (IRE) Flat 7f Standard 12/14 fig 35
    DATA for: Has won at this trip or further; Carries 7 lb less than average; First-time headgear
    DATA against: Best recent form figure 35, 13 lb below field average; Recent figures 9 lb below its current mark (looks high in the weights); Official rating 44, 7 lb below field average; Pace: steady gallop likely, hard to come from off the pace
- All Hail (hrs_53081217) | 3yo G | 137lb | OR 55 | draw 7 | jockey Siobhan Rutledge | trainer John McConnell (14d 0/13) | headgear tb | last run 23 days | form 098040 | MARKET 2.2% | 09:00 median 34.00 | Matchbook 40.00
    comment: All Hail has been well beaten in recent outings, with a fourth two starts back his best finish in his last six, though he has run over today's trip and going before and returns after 23 days.
    DATA: model 4.1% | style Held up (led 5% of runs) | runs in data 8 | last 3: 9 Sep Cork Flat 8f Good 18/18; 25 Sep Dundalk Flat 6f Standard 4/14; 28 Oct Dundalk (AW) (IRE) Flat 7f Standard 12/13 fig 46
    DATA against: Recent figures 9 lb below its current mark (looks high in the weights); Trainer 0 wins from 13 runs, last 14 days; Pace: steady gallop likely, hard to come from off the pace
- Hasiyna (hrs_31188213) | 6yo M | 122lb | OR 40 | draw 12 | jockey  | trainer John McConnell (14d 0/13) | headgear - | last run 28 days | form 697900 | MARKET 2.2% | 09:00 median 34.00 | Matchbook 42.00
    comment: Hasiyna is hard to fancy, yet to score in her last six and unplaced in her last two after finishes of ninth, seventh, ninth and sixth before that. She has run over today's trip and going, and 28 days since her last run is no concern, but that is about all she has going for her from stall 12.
    DATA: model 1.1% | style Midfield (led 5% of runs) | runs in data 7 | last 3: 23 Aug Naas Flat 5f Good 9/19; 2 Oct Dundalk Flat 5f Standard 12/12; 23 Oct Dundalk (AW) (IRE) Flat 6f Standard 13/14 fig 31
    DATA for: Carries 11 lb less than average
    DATA against: Best recent form figure 31, 17 lb below field average; Recent figures 9 lb below its current mark (looks high in the weights); Official rating 40, 11 lb below field average; Trainer 0 wins from 13 runs, last 14 days; Poor recent finishing positions
- Gonirianbotharleat (hrs_59862481) | 5yo G | 126lb | OR 44 | draw 11 | jockey Leigh Roche | trainer Miss Jennifer Anne Lynch (14d 0/0) | headgear - | last run 30 days | form 9-8007 | MARKET 2.1% | 09:00 median 34.00 | Matchbook 44.00
    comment: He has run over today's trip and going and returns after 30 days, but that is about all in his favour.
    DATA: model 1.3% | style Midfield (led 3% of runs) | runs in data 4 | last 3: 20 Feb Dundalk Flat 7f Standard 10/10; 2 Oct Dundalk Flat 7f Standard 12/13; 21 Oct Navan (IRE) Flat 6f Yielding 7/21 fig 46
    DATA for: Carries 7 lb less than average
    DATA against: Official rating 44, 7 lb below field average; Poor recent finishing positions

## 5:45 Dundalk (AW) | race_id rac_32305049114 | Dundalk Stadium Nursery Handicap
Flat |  | 0m7f0y | going Standard | AW | 7 runners | rating band - | age 2yo
DATA pace: Lone leader - Bull Shark is the only habitual front-runner and may be allowed an easy lead.
- Prince Of Peppard (hrs_65973264) | 2yo C | 138lb | OR 80 | draw 1 | jockey Ben Coen | trainer J. P. Murtagh (14d 1/8) | headgear - | last run 30 days | form 674223 | MARKET 23.9% | 09:00 median 3.50 | Matchbook 4.00 | CHECK (skip line 3.32)
    comment: Prince Of Peppard arrives in cracking nick, third last time out after a second two starts back and another second three starts back, and he has run over today's trip before.
    DATA: model 27.5% | style Midfield (led 4% of runs) | runs in data 7 | last 3: 21 Sep Fairyhouse Flat 6f Good 2/7; 7 Oct Navan Flat 5.8f Yielding 2/10; 21 Oct Navan (IRE) Flat 6f Yielding 3/14 fig 90
    DATA for: Best recent form figure 90, 21 lb above field average; Recent figures 10 lb above its current mark (looks well handicapped); Official rating 80, 9 lb above field average; Good recent finishing positions
    DATA against: Carries 7 lb more than average
- Bull Shark (hrs_62168043) | 2yo G | 139lb | OR 81 | draw 3 | jockey Patrick McGettigan(5) | trainer Robson De Aguiar (14d 1/4) | headgear - | last run 146 days | form 333207 | MARKET 22.0% | 09:00 median 3.75 | Matchbook 4.30
    comment: The risk is a 146-day absence after a seventh last time out.
    DATA: model 5.5% | style Leader (led 54% of runs) | runs in data 6 | last 3: 3 Jun Curragh Flat 7f Yielding 2/6; 16 Jun Ascot Flat 6f Good To Firm 20/21; 27 Jun Curragh Flat 7f Good To Firm 7/8
    DATA for: Official rating 81, 10 lb above field average; Pace: may get an uncontested lead
    DATA against: Last-run finishing speed -3.4% vs that field (faded); Carries 8 lb more than average; Returns from a 146-day break
- Closefield Beau (hrs_65869559) | 2yo G | 128lb | OR 70 | draw 2 | jockey Conor Cusack(7) | trainer Daniel McLoughlin (14d 1/7) | headgear - | last run 7 days | form 784413 | MARKET 21.5% | 09:00 median 4.00 | Matchbook 4.20
    DATA: model 21.5% | style Held up (led 8% of runs) | runs in data 7 | last 3: 16 Oct Dundalk (AW) (IRE) Flat 7f Standard 4/13 fig 69; 4 Nov Dundalk (AW) (IRE) Flat 7f Standard 1/7 fig 67; 13 Nov Dundalk (AW) (IRE) Flat 8f Standard 3/6 fig 63
    DATA for: Has won at this trip or further; Good recent finishing positions
- Dear Theodosia (hrs_7000000518) | 2yo F | 119lb | OR 48 | draw 6 | jockey Nathan Crosse | trainer Daniel McLoughlin (14d 1/7) | headgear - | last run 2 days | form 099631 | MARKET 13.3% | 09:00 median 6.50 | Matchbook 6.80
    comment: She has run over today's trip and going, and drawn six, carries 119 lb.
    DATA: model 4.6% | style Midfield (led 29% of runs) | runs in data 7 | last 3: 19 Oct Gowran Park (IRE) Flat 7f Yielding 6/12 fig 49; 11 Nov Dundalk (AW) (IRE) Flat 6f Standard 3/8 fig 54; 18 Nov Dundalk (AW) (IRE) Flat 7f Standard 1/12 fig 57
    DATA for: Recent figures 9 lb above its current mark (looks well handicapped); Has won at this trip or further; Good recent finishing positions; Carries 12 lb less than average
    DATA against: Best recent form figure 57, 12 lb below field average; Official rating 48, 23 lb below field average
- Marcescence (hrs_66655358) | 2yo F | 133lb | OR 75 | draw 5 | jockey Jack Kearney | trainer Gavin Cromwell (14d 4/34) | headgear - | last run 9 days | form 334 | MARKET 12.4% | 09:00 median 6.50 | Matchbook 8.40
    comment: The risk is that she's yet to win and has to carry 133 lb from stall five.
    DATA: model 34.7% | style Prominent (led 38% of runs) | runs in data 3 | last 3: 5 Sep Navan Flat 5.8f Good 3/13; 7 Oct Navan Flat 5.8f Yielding 3/21; 11 Nov Dundalk (AW) (IRE) Flat 7f Standard 4/14 fig 62
    DATA for: Good recent finishing positions
    DATA against: Best recent form figure 62, 7 lb below field average; Recent figures 13 lb below its current mark (looks high in the weights)
- Angel Invincible (hrs_17393029101) | 2yo F | 130lb | OR 72 | draw 4 | jockey W. J. Lee | trainer Daniel McLoughlin (14d 1/7) | headgear - | last run 7 days | form 0904 | MARKET 4.5% | 09:00 median 17.00 | Matchbook 24.00
    comment: Angel Invincible is winless in her last four, with a fourth last time out the best of them and unplaced efforts either side of a ninth, so she is hard to fancy.
    DATA: model 2.7% | style Midfield (led 4% of runs) | runs in data 4 | last 3: 17 Oct Leopardstown (IRE) Flat 8.5f Good 9/10 fig 49; 29 Oct Punchestown (IRE) Flat 7f Yielding 10/11 fig 13; 13 Nov Dundalk (AW) (IRE) Flat 8f Standard 4/6 fig 65
    DATA against: Recent figures 7 lb below its current mark (looks high in the weights)
- Cloughleagh Bridge (hrs_65519825) | 2yo F | 130lb | OR 72 | draw 7 | jockey Chris Hayes | trainer P J F Murphy (14d 1/4) | headgear - | last run 60 days | form 584866 | MARKET 2.4% | 09:00 median 34.00 | Matchbook 44.00
    comment: Cloughleagh Bridge has run over today's trip and going, but she is winless in her last six, finishing sixth in her last two outings, and returns after 60 days off.
    DATA: model 3.5% | style Midfield (led 4% of runs) | runs in data 6 | last 3: 15 Aug Dundalk Flat 6f Standard 8/14; 8 Sep Galway Flat 7f Soft 6/12; 21 Sep Fairyhouse Flat 7f Good 6/6
    DATA against: Poor recent finishing positions

## 6:15 Dundalk (AW) | race_id rac_32305051051 | BAR 1 Betting 'Safer Gambling Week' Rated Race
Flat |  | 0m7f0y | going Standard | AW | 12 runners | rating band - | age 3yo+
DATA pace: Even - Two likely leaders (Celtic Motif, Send Harry). A fair, even gallop is most likely.
- City House (hrs_35895608) | 5yo G | 136lb | OR 84 | draw 9 | jockey Rory Mulligan(5) | trainer Adrian McGuinness (14d 4/19) | headgear tv | last run 7 days | form 258612 | MARKET 20.6% | 09:00 median 4.00 | Matchbook 4.20 | CHECK (skip line 3.80)
    comment: City House bounces in on a good profile, a second last time out and a winner two starts back, and he's fresh from a quick seven-day turnaround. He has run over today's trip and on the going before, though 136 lb from stall nine asks a fair bit.
    DATA: model 18.0% | style Midfield (led 8% of runs) | runs in data 16 | last 3: 16 Oct Dundalk (AW) (IRE) Flat 7f Standard 6/12 fig 79; 30 Oct Dundalk (AW) (IRE) Flat 6f Standard 1/8 fig 81; 13 Nov Dundalk (AW) (IRE) Flat 6f Standard 2/10 fig 84
    DATA for: Best recent form figure 84, 8 lb above field average; Trainer 21% wins (4/19), last 14 days; Good recent finishing positions
- Chicago Pope (hrs_55061650) | 3yo G | 134lb | OR 83 | draw 3 | jockey Ben Coen | trainer J. P. Murtagh (14d 1/8) | headgear - | last run 7 days | form 214006 | MARKET 13.5% | 09:00 median 6.00 | Matchbook 6.40
    comment: The risk is his recent form, with a sixth last time out and a quick seven-day turnaround.
    DATA: model 7.7% | style Prominent (led 29% of runs) | runs in data 6 | last 3: 13 Sep Curragh Flat 6f Yielding 16/24; 15 Oct Curragh (IRE) Flat 6f Soft 12/13 fig 69; 13 Nov Dundalk (AW) (IRE) Flat 6f Standard 6/10 fig 77
    DATA against: Poor recent finishing positions
- Alissam (hrs_58596475) | 3yo G | 129lb | OR 78 | draw 5 | jockey Jack Kearney | trainer Stephen Thorne (14d 0/3) | headgear t | last run 21 days | form 133-57 | MARKET 12.6% | 09:00 median 6.50 | Matchbook 6.80
    comment: Alissam has been in decline since a win five starts back, with a third, another third, a fifth and then a seventh last time out, though he has run over today's trip and going and returns after 21 days.
    DATA: model 6.8% | style Prominent (led 8% of runs) | runs in data 2 | last 3: 9 Oct Dundalk Flat 8f Standard 5/13; 30 Oct Dundalk (AW) (IRE) Flat 8f Standard 7/14 fig 79
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Celtic Motif (hrs_43667239) | 4yo F | 140lb | OR 88 | draw 4 | jockey J M Sheridan | trainer Joseph Patrick O'Brien (14d 2/22) | headgear t | last run 105 days | form 02-314 | MARKET 12.1% | 09:00 median 6.00 | Matchbook 7.80
    comment: Celtic Motif arrives with solid recent form, a fourth last time out, a winner two starts back, and a third and a second before that, and she has run over today's trip. The main risk is a 105-day absence, while 140 lb from stall four is a stiff ask off 88.
    DATA: model 17.3% | style Leader (led 57% of runs) | runs in data 2 | last 3: 14 Jul Killarney Flat 8.1f Good 1/5; 7 Aug Gowran Park Flat 8f Good 4/6
    DATA for: Official rating 88, 7 lb above field average; Has won at this trip or further
    DATA against: Returns from a 105-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- Eddie G (hrs_37576595) | 5yo G | 131lb | OR 79 | draw 1 | jockey Camillus Byrne(10) | trainer Adrian McGuinness (14d 4/19) | headgear t | last run 7 days | form 532037 | MARKET 7.8% | 09:00 median 10.00 | Matchbook 12.00
    comment: Eddie G is winless in his last six, though a third two starts back and a second four runs ago show he can get involved, and he has run over today's trip and going. Last seen seven days ago finishing seventh, he carries 131 lb from stall one off a mark of 79.
    DATA: model 5.8% | style Held up (led 5% of runs) | runs in data 12 | last 3: 18 Oct Leopardstown (IRE) Flat 8.5f Good 15/16 fig 67; 30 Oct Dundalk (AW) (IRE) Flat 6f Standard 3/8 fig 78; 13 Nov Dundalk (AW) (IRE) Flat 6f Standard 7/10 fig 70
    DATA for: Trainer 21% wins (4/19), last 14 days; Has won at this trip or further
- Apache Outlaw (hrs_30123702) | 6yo G | 136lb | OR 84 | draw 12 | jockey Colin Keane | trainer Denis Gerard Hogan (14d 0/12) | headgear tv | last run 16 days | form 396951 | MARKET 6.7% | 09:00 median 13.00 | Matchbook 13.50
    comment: Winner last time out just 16 days ago, Apache Outlaw has fitness and confidence on his side, and he has run over today's trip and going, though a fifth, a ninth and a sixth in the three runs before that show his consistency is patchy.
    DATA: model 13.4% | style Midfield (led 4% of runs) | runs in data 17 | last 3: 15 Oct Curragh (IRE) Flat 7f Soft 9/20 fig 65; 20 Oct Curragh (IRE) Flat 6f Yielding 5/17 fig 67; 4 Nov Dundalk (AW) (IRE) Flat 6f Standard 1/8 fig 77
    DATA for: Last-run finishing speed +2.3% vs that field (finished strongly)
    DATA against: Trainer 0 wins from 12 runs, last 14 days
- Send Harry (hrs_46013667) | 4yo G | 131lb | OR 79 | draw 11 | jockey Jimmy Dalton(7) | trainer Miss Evanna McCutcheon (14d 0/1) | headgear ht | last run 21 days | form 502810 | MARKET 6.5% | 09:00 median 13.00 | Matchbook 13.50
    comment: Send Harry won two starts back but was unplaced last time out, and his other recent runs read eighth, second, unplaced and fifth, so consistency is a worry.
    DATA: model 7.2% | style Leader (led 29% of runs) | runs in data 11 | last 3: 28 Sep Down Royal Flat 7.1f Good To Yielding 8/14; 9 Oct Dundalk Flat 7f Standard 1/14; 30 Oct Dundalk (AW) (IRE) Flat 8f Standard 11/14 fig 70
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 70, 6 lb below field average
- El Rehaiby (hrs_57041544) | 4yo G | 127lb | OR - | draw 6 | jockey Declan McDonogh | trainer A. Slattery (14d 0/13) | headgear - | last run 407 days | form 52- | MARKET 5.1% | 09:00 median 11.00 | Matchbook 26.00
    comment: El Rehaiby is hard to fancy after 407 days off, though he was second last time out and a fifth two starts back, and he has run on today's going before.
    DATA: model 4.2% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Trainer 0 wins from 13 runs, last 14 days; Returns from a 407-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Tax Me Later (hrs_17391394720) | 3yo F | 126lb | OR 75 | draw 7 | jockey Robbie Colgan | trainer Kevin Thomas Coleman (14d 0/4) | headgear - | last run 41 days | form 3232 | MARKET 4.6% | 09:00 median 13.00 | Matchbook 29.00
    comment: Tax Me Later has been placed in each of her last four starts, finishing second last time out, but she is yet to win and has been 41 days off.
    DATA: model 9.7% | style Prominent (led 4% of runs) | runs in data 4 | last 3: 1 Sep Gowran Park Flat 8f Yielding 2/8; 1 Oct Bellewstown Flat 7.9f Soft To Heavy 3/5; 10 Oct Naas Flat 8f Soft 2/13
    DATA for: Last-run finishing speed +3.4% vs that field (finished strongly); Good recent finishing positions
    DATA against: Official rating 75, 6 lb below field average
- Goal Exceeded (hrs_36387393) | 5yo G | 128lb | OR 76 | draw 8 | jockey Adam Caffrey | trainer Adrian McGuinness (14d 4/19) | headgear t | last run 19 days | form 441600 | MARKET 4.5% | 09:00 median 21.00 | Matchbook 18.50
    comment: Hard to fancy after back-to-back unplaced runs, with his only win four starts back and a sixth three starts back since. He has run over today's trip and going, and 19 days since his last run is fine, but carrying 128 lb from stall 8 he looks up against it.
    DATA: model 2.2% | style Midfield (led 3% of runs) | runs in data 10 | last 3: 22 Sep Listowel Flat 8f Yielding 6/7; 10 Oct Naas Flat 7f Soft 10/10; 1 Nov Curragh (IRE) Flat 7f Yielding To Soft 20/25 fig 64
    DATA for: Trainer 21% wins (4/19), last 14 days; Has won at this trip or further
    DATA against: Best recent form figure 64, 12 lb below field average; Official rating 76, 5 lb below field average; Poor recent finishing positions
- Kullazain (hrs_44481318) | 4yo G | 136lb | OR 84 | draw 10 | jockey Chris Hayes | trainer Denis Gerard Hogan (14d 0/12) | headgear - | last run 32 days | form 1-3768 | MARKET 3.8% | 09:00 median 17.00 | Matchbook 34.00
    comment: The risk is the slide since, with an eighth last time, a sixth and a seventh, off 136 lb from stall 10.
    DATA: model 6.0% | style Held up (led 5% of runs) | runs in data 4 | last 3: 7 Mar Wolverhampton Flat 6.1f Standard 7/9; 6 Apr Wolverhampton Flat 7.2f Standard 6/6; 19 Oct Wolverhampton (AW) Flat 6f Standard 8/12 fig 82
    DATA for: Best recent form figure 82, 6 lb above field average
    DATA against: Trainer 0 wins from 12 runs, last 14 days; Poor recent finishing positions
- Arryaaf (hrs_48290172) | 4yo F | 134lb | OR 82 | draw 2 | jockey W. J. Lee | trainer David Marnane (14d 2/5) | headgear - | last run 147 days | form 4313-0 | MARKET 2.3% | 09:00 median 41.00 | Matchbook 42.00
    comment: Arryaaf is hard to fancy after 147 days off and an unplaced run last time out, though she was third two starts back and a winner three starts back, and has run over today's trip.
    DATA: model 1.7% | style Held up (led 8% of runs) | runs in data 1 | last 3: 26 Jun Curragh Flat 7f Good 17/17
    DATA for: Trainer 40% wins (2/5), last 14 days
    DATA against: Last-run finishing speed -3.3% vs that field (faded); Returns from a 147-day break; Lightly raced: 1 run in our data, so the model has little to go on

## 6:45 Dundalk (AW) | race_id rac_32305052988 | Irish Stallion Farms EBF (C & G) Maiden
Flat |  | 1m0f0y | going Standard | AW | 13 runners | rating band - | age 2yo
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Golden Idol (hrs_17392957134) | 2yo C | 131lb | OR - | draw 5 | jockey W. J. Lee | trainer Henry de Bromhead (14d 8/38) | headgear - | last run 23 days | form 32 | MARKET 23.9% | 09:00 median 3.50 | Matchbook 3.50 | CHECK (skip line 3.32)
    DATA: model 14.6% | style Prominent (led 8% of runs) | runs in data 2 | last 3: 27 Sep Curragh Flat 7f Heavy 3/13; 28 Oct Dundalk (AW) (IRE) Flat 7f Standard 2/11 fig 70
    DATA for: Best recent form figure 70, 16 lb above field average; Trainer 21% wins (8/38), last 14 days; Good recent finishing positions
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Warrior Of Siam (hrs_17395085897) | 2yo C | 131lb | OR - | draw 6 | jockey J M Sheridan | trainer Joseph Patrick O'Brien (14d 2/22) | headgear t | last run 14 days | form 6 | MARKET 15.7% | 09:00 median 5.50 | Matchbook 5.30
    DATA: model 5.9% | style Unknown | runs in data 1 | last 3: 6 Nov Dundalk (AW) (IRE) Flat 8f Standard 6/10 fig 67
    DATA for: Best recent form figure 67, 13 lb above field average; Last-run finishing speed +3.2% vs that field (finished strongly)
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Bridgetown Boy (hrs_17394521634) | 2yo C | 131lb | OR - | draw 3 | jockey Seamie Heffernan | trainer W P Browne (14d 0/1) | headgear - | last run 23 days | form 3 | MARKET 15.2% | 09:00 median 5.50 | Matchbook 5.60
    DATA: model 16.2% | style Unknown | runs in data 1 | last 3: 28 Oct Dundalk (AW) (IRE) Flat 7f Standard 3/11 fig 65
    DATA for: Best recent form figure 65, 11 lb above field average
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Sovereign Jazz (hrs_17390258893) | 2yo C | 131lb | OR - | draw 9 | jockey Colin Keane | trainer Noel Meade (14d 3/11) | headgear - | last run 106 days | form 5 | MARKET 14.8% | 09:00 median 5.50 | Matchbook 5.90
    DATA: model 2.2% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 6 Aug Leopardstown Flat 8f Good 5/8
    DATA for: Trainer 27% wins (3/11), last 14 days
    DATA against: Returns from a 106-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Selosse (hrs_66304847) | 2yo C | 131lb | OR - | draw 12 | jockey Nathan Crosse | trainer Mrs J. Harrington (14d 1/10) | headgear p (1st time) | last run 41 days | form 57 | MARKET 9.1% | 09:00 median 7.50 | Matchbook 11.00
    DATA: model 14.8% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 22 Aug Curragh Flat 7f Good 5/16; 10 Oct Naas Flat 8f Soft 7/18
    DATA for: First-time headgear
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Epic Arch (hrs_17390851317) | 2yo G | 131lb | OR 77 | draw 1 | jockey Ben Coen | trainer A. Slattery (14d 0/13) | headgear - | last run 46 days | form 682 | MARKET 8.5% | 09:00 median 8.00 | Matchbook 12.00
    DATA: model 9.3% | style Prominent (led 4% of runs) | runs in data 3 | last 3: 15 Aug Dundalk Flat 8f Standard 6/13; 15 Sep Punchestown Flat 8.1f Good 8/14; 5 Oct Killarney Flat 8.1f Yielding To Soft 2/12
    DATA against: Trainer 0 wins from 13 runs, last 14 days
- Victorious Star (hrs_17395783664) | 2yo G | 131lb | OR - | draw 8 | jockey Declan McDonogh | trainer Joseph Patrick O'Brien (14d 2/22) | headgear - | last run - days | form - | MARKET 4.0% | 09:00 median 17.00 | Matchbook 29.00
    DATA: model 5.9% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Larry Curly Moe (hrs_17395084854) | 2yo C | 131lb | OR - | draw 7 | jockey Donagh O'Connor | trainer Robson De Aguiar (14d 1/4) | headgear - | last run - days | form - | MARKET 3.2% | 09:00 median 23.00 | Matchbook 36.00
    DATA: model 5.9% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Theboysbirthday (hrs_17395782621) | 2yo G | 131lb | OR - | draw 13 | jockey Robbie Colgan | trainer David Marnane (14d 2/5) | headgear - | last run - days | form - | MARKET 1.7% | 09:00 median 34.00 | Matchbook 95.00
    DATA: model 5.9% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 40% wins (2/5), last 14 days
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Pauseathought (hrs_17393548515) | 2yo C | 131lb | OR - | draw 2 | jockey W. M. Lordan | trainer Miss Natalia Lupini (14d 1/6) | headgear - | last run 42 days | form 0 | MARKET 1.3% | 09:00 median 51.00 | Matchbook 110.00
    DATA: model 5.4% | style Held up (led 8% of runs) | runs in data 1 | last 3: 9 Oct Dundalk Flat 7f Standard 10/14
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Saxonian (hrs_17392582697) | 2yo G | 131lb | OR - | draw 10 | jockey Chris Hayes | trainer J A Stack (14d 0/2) | headgear - | last run 34 days | form 90 | MARKET 1.0% | 09:00 median 67.00 | Matchbook 140.00
    DATA: model 3.6% | style Held up (led 5% of runs) | runs in data 2 | last 3: 19 Sep Gowran Park Flat 8f Yielding To Soft 9/12; 17 Oct Leopardstown (IRE) Flat 8.5f Good 10/15 fig 46
    DATA against: Best recent form figure 46, 8 lb below field average; Lightly raced: 2 runs in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Unstoppable Army (hrs_17394009521) | 2yo G | 131lb | OR - | draw 4 | jockey Robert Whearty | trainer Gavin Cromwell (14d 4/34) | headgear - | last run 32 days | form 7 | MARKET 1.0% | 09:00 median 67.00 | Matchbook 160.00
    DATA: model 5.2% | style Held up (led 8% of runs) | runs in data 1 | last 3: 19 Oct Gowran Park (IRE) Flat 8.5f Soft 7/14 fig 48
    DATA for: Last-run finishing speed +2.1% vs that field (finished strongly)
    DATA against: Best recent form figure 48, 6 lb below field average; Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Alfredo Delgado (hrs_17392601471) | 2yo G | 131lb | OR - | draw 11 | jockey Luke McAteer | trainer P Sweeney (14d 0/2) | headgear - | last run 36 days | form 89 | MARKET 0.6% | 09:00 median 151.00 | Matchbook 220.00
    DATA: model 5.3% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 21 Sep Listowel Flat 8f Yielding 8/11; 15 Oct Curragh (IRE) Flat 6f Soft 9/12 fig 29
    DATA against: Best recent form figure 29, 25 lb below field average; Lightly raced: 2 runs in our data, so the model has little to go on

## 7:15 Dundalk (AW) | race_id rac_32305054925 | Irish Stallion Farms EBF Fillies Maiden
Flat |  | 1m0f0y | going Standard | AW | 17 runners | rating band - | age 2yo
DATA pace: Unclear - Running styles known for only 6 of 17 runners.
- Castilian Queen (hrs_17391667986) | 2yo F | 128lb | OR - | draw 4 | jockey Colin Keane | trainer G. M. Lyons (14d 0/1) | headgear - | last run 56 days | form 42 | MARKET 32.0% | 09:00 median 2.25 | Matchbook 2.30
    DATA: model 15.9% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 9 Sep Cork Flat 7f Good 4/17; 25 Sep Dundalk Flat 7f Standard 2/13
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Carafinn (hrs_65101379) | 2yo F | 128lb | OR - | draw 6 | jockey W. M. Lordan | trainer Henry de Bromhead (14d 8/38) | headgear - | last run 134 days | form 44 | MARKET 13.0% | 09:00 median 5.00 | Matchbook 6.20
    DATA: model 8.3% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 14 Jun Cork Flat 6f Good 4/14; 9 Jul Leopardstown Flat 7.2f Good 4/13
    DATA for: Trainer 21% wins (8/38), last 14 days
    DATA against: Returns from a 134-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- Kathy M (hrs_17392574353) | 2yo F | 128lb | OR - | draw 2 | jockey J M Sheridan | trainer Joseph Patrick O'Brien (14d 2/22) | headgear - | last run 43 days | form 5 | MARKET 10.9% | 09:00 median 6.50 | Matchbook 7.60
    DATA: model 5.2% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 8 Oct Thurles Flat 8.3f Good To Yielding 5/10
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Solar Palace (hrs_17395792008) | 2yo F | 128lb | OR - | draw 3 | jockey  | trainer Joseph Patrick O'Brien (14d 2/22) | headgear - | last run - days | form - | MARKET 6.5% | 09:00 median 10.00 | Matchbook 14.00
    DATA: model 5.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Lochlane (hrs_17395789922) | 2yo F | 128lb | OR - | draw 11 | jockey Declan McDonogh | trainer Joseph Patrick O'Brien (14d 2/22) | headgear - | last run - days | form - | MARKET 5.6% | 09:00 median 13.00 | Matchbook 14.00
    DATA: model 5.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Kariata (hrs_17395788879) | 2yo F | 128lb | OR - | draw 1 | jockey Ben Coen | trainer J. P. Murtagh (14d 1/8) | headgear - | last run - days | form - | MARKET 3.8% | 09:00 median 17.00 | Matchbook 24.00
    DATA: model 5.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Lady Chancalot (hrs_17391671115) | 2yo F | 128lb | OR - | draw 16 | jockey James Ryan | trainer Jack W Davison (14d 0/2) | headgear - | last run 49 days | form 93 | MARKET 3.8% | 09:00 median 17.00 | Matchbook 23.00
    DATA: model 2.9% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 1 Sep Gowran Park Flat 7f Yielding 9/16; 2 Oct Dundalk Flat 8f Standard 3/7
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Arddin (hrs_17395785750) | 2yo F | 128lb | OR - | draw 14 | jockey Chris Hayes | trainer Joseph Patrick O'Brien (14d 2/22) | headgear - | last run - days | form - | MARKET 3.6% | 09:00 median 19.00 | Matchbook 24.00
    DATA: model 5.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Fire In The Air (hrs_17395786793) | 2yo F | 128lb | OR - | draw 17 | jockey Seamie Heffernan | trainer Joseph Patrick O'Brien (14d 2/22) | headgear - | last run - days | form - | MARKET 3.4% | 09:00 median 21.00 | Matchbook 25.00
    DATA: model 5.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Seanbonekapone (hrs_17395790965) | 2yo F | 128lb | OR - | draw 13 | jockey W. J. Lee | trainer W. McCreery (14d 0/3) | headgear v (1st time) | last run - days | form - | MARKET 2.9% | 09:00 median 26.00 | Matchbook 29.00
    DATA: model 5.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: First-time headgear
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Always Be Mine (hrs_17395784707) | 2yo F | 128lb | OR - | draw 7 | jockey Adam Grant(7) | trainer Henry de Bromhead (14d 8/38) | headgear - | last run - days | form - | MARKET 2.9% | 09:00 median 26.00 | Matchbook 29.00
    DATA: model 5.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 21% wins (8/38), last 14 days
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Proper Naughty (hrs_62169219) | 2yo F | 128lb | OR - | draw 5 | jockey Nicola Burns(5) | trainer Miss Natalia Lupini (14d 1/6) | headgear - | last run 90 days | form 30 | MARKET 2.7% | 09:00 median 26.00 | Matchbook 28.00
    DATA: model 4.3% | style Unknown | runs in data 2 | last 3: 3 Aug Windsor Flat 6.1f Good To Firm 3/6; 22 Aug Newmarket Flat 6f Good 13/18
    DATA against: Returns from a 90-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- Guide Me Home (hrs_17395787836) | 2yo F | 128lb | OR - | draw 10 | jockey Adam Caffrey | trainer Daniel James Murphy (14d 0/9) | headgear - | last run - days | form - | MARKET 2.3% | 09:00 median 29.00 | Matchbook 42.00
    DATA: model 5.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Trainer 0 wins from 9 runs, last 14 days; Lightly raced: 0 runs in our data, so the model has little to go on
- Celestial Order (hrs_17393765459) | 2yo F | 128lb | OR - | draw 12 | jockey  | trainer Miss Natalia Lupini (14d 1/6) | headgear - | last run 36 days | form 7 | MARKET 2.2% | 09:00 median 34.00 | Matchbook 42.00
    DATA: model 7.0% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 15 Oct Curragh (IRE) Flat 8f Soft 7/15 fig 51
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Whiptail (hrs_17395793051) | 2yo F | 128lb | OR - | draw 8 | jockey Robbie Colgan | trainer Henry de Bromhead (14d 8/38) | headgear - | last run - days | form - | MARKET 2.1% | 09:00 median 34.00 | Matchbook 42.00
    DATA: model 5.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 21% wins (8/38), last 14 days
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- An Tuath Nua (hrs_17393763373) | 2yo F | 128lb | OR - | draw 15 | jockey Luke McAteer | trainer J S Bolger (14d 0/0) | headgear - | last run - days | form - | MARKET 1.4% | 09:00 median 67.00 | Matchbook 60.00
    DATA: model 5.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Silent Promise (hrs_17392277098) | 2yo F | 128lb | OR - | draw 9 | jockey  | trainer Adrian McGuinness (14d 4/19) | headgear - | last run 19 days | form 90 | MARKET 1.0% | 09:00 median 101.00 | Matchbook 80.00
    DATA: model 2.7% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 15 Oct Curragh (IRE) Flat 8f Soft 9/15 fig 51; 1 Nov Curragh (IRE) Flat 8f Yielding To Soft 12/23 fig 52
    DATA for: Trainer 21% wins (4/19), last 14 days
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on

## 7:45 Dundalk (AW) | race_id rac_32305056862 | Christmas Party Nights At Dundalk Stadium Apprentice Handicap
Flat |  | 1m2f150y | going Standard | AW | 13 runners | rating band - | age 4yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Tero d'Rosa (hrs_53602164) | 4yo G | 131lb | OR 61 | draw 7 | jockey Conor Cusack(7) | trainer Ross O'Sullivan (14d 1/15) | headgear - | last run 36 days | form 664620 | MARKET 14.2% | 09:00 median 5.80 | Matchbook 6.20 | CHECK (skip line 5.51)
    comment: Tero d'Rosa is yet to win in his last six, though a second two starts back shows he can go close, and he has run over today's trip and going before.
    DATA: model 7.5% | style Prominent (led 3% of runs) | runs in data 7 | last 3: 23 Aug Naas Flat 11f Good 6/16; 15 Sep Punchestown Flat 9.1f Good 2/13; 15 Oct Curragh (IRE) Flat 9f Yielding To Soft 16/19 fig 53
    DATA against: Best recent form figure 53, 6 lb below field average; Recent figures 8 lb below its current mark (looks high in the weights)
- Flying Fortress (hrs_43951047) | 4yo G | 139lb | OR 69 | draw 4 | jockey Sam Coen | trainer Gavin Cromwell (14d 4/34) | headgear b | last run 9 days | form 824004 | MARKET 12.9% | 09:00 median 6.00 | Matchbook 7.00
    comment: The risk is he's yet to win in his last six starts.
    DATA: model 6.8% | style Midfield (led 4% of runs) | runs in data 8 | last 3: 12 Oct Roscommon Flat 12.2f Soft 12/16; 29 Oct Punchestown (IRE) Flat 8f Yielding 11/14 fig 63; 11 Nov Dundalk (AW) (IRE) Flat 10.5f Standard 4/14 fig 72
    DATA for: Best recent form figure 72, 13 lb above field average
- Usuario Amigo (hrs_40805534) | 5yo G | 134lb | OR 64 | draw 6 | jockey Adam Grant(7) | trainer Richard John O'Brien (14d 0/3) | headgear - | last run 2 days | form 036176 | MARKET 12.3% | 09:00 median 6.50 | Matchbook 7.20
    comment: Usuario Amigo is hard to fancy after a sixth last time out and a seventh before that, and he's back in just two days, though he did win three starts back and has run on today's going before.
    DATA: model 9.4% | style Held up (led 5% of runs) | runs in data 14 | last 3: 25 Sep Dundalk Flat 8f Standard 1/14; 11 Nov Dundalk (AW) (IRE) Flat 7f Standard 7/14 fig 57; 18 Nov Dundalk (AW) (IRE) Flat 8f Standard 6/13 fig 61
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Soaring Sun (hrs_56625009) | 5yo G | 136lb | OR 66 | draw 8 | jockey Robyn Donaghue-Leahy(4) | trainer Patrick J Flynn (14d 1/8) | headgear - | last run 14 days | form 178308 | MARKET 11.1% | 09:00 median 6.50 | Matchbook 8.40
    comment: Soaring Sun was eighth last time out and has just one win in his last six starts, a victory six starts back, though a third three starts back shows he can reach the frame.
    DATA: model 7.6% | style Midfield (led 4% of runs) | runs in data 6 | last 3: 8 Sep Galway Flat 12f Soft 3/15; 21 Sep Listowel Flat 14.2f Yielding 14/15; 6 Nov Dundalk (AW) (IRE) Flat 12f Standard 8/10 fig 60
    DATA for: Has won at this trip or further
    DATA against: Recent figures 6 lb below its current mark (looks high in the weights)
- Dancing Steve (hrs_412712174) | 5yo G | 133lb | OR 63 | draw 9 | jockey Camillus Byrne(7) | trainer Adrian McGuinness (14d 4/19) | headgear v | last run 16 days | form 310625 | MARKET 10.8% | 09:00 median 7.00 | Matchbook 8.80
    comment: He has run over today's trip and going and was second two starts back, while 16 days since his last run suggests he is fit.
    DATA: model 9.3% | style Midfield (led 8% of runs) | runs in data 10 | last 3: 16 Oct Dundalk (AW) (IRE) Flat 10.5f Standard 6/14 fig 57; 28 Oct Dundalk (AW) (IRE) Flat 12f Standard 2/13 fig 66; 4 Nov Dundalk (AW) (IRE) Flat 10.5f Standard 5/14 fig 60
    DATA for: Best recent form figure 66, 7 lb above field average; Trainer 21% wins (4/19), last 14 days; Has won at this trip or further
- Tribal Moon (hrs_36665132) | 5yo G | 134lb | OR 64 | draw 1 | jockey Rory Mulligan | trainer Noel C. Kelly (14d 2/9) | headgear tp | last run 21 days | form 2-0677 | MARKET 10.1% | 09:00 median 7.50 | Matchbook 9.20
    comment: Tribal Moon has finished seventh in each of his last two and is winless in recent starts, though a second five starts back shows he has a bit in him, and he has run over today's trip and going.
    DATA: model 5.8% | style Prominent (led 5% of runs) | runs in data 9 | last 3: 25 Sep Dundalk Flat 10.7f Standard 6/14; 16 Oct Dundalk (AW) (IRE) Flat 10.5f Standard 7/14 fig 64; 30 Oct Dundalk (AW) (IRE) Flat 12f Standard 7/9 fig 59
    DATA for: Best recent form figure 64, 5 lb above field average; Trainer 22% wins (2/9), last 14 days
    DATA against: Poor recent finishing positions
- Justenzia (hrs_45982377) | 4yo F | 144lb | OR 74 | draw 13 | jockey Jared Huggan(7) | trainer Denis Gerard Hogan (14d 0/12) | headgear p | last run 9 days | form 226212 | MARKET 7.7% | 09:00 median 9.00 | Matchbook 13.00
    comment: Justenzia arrives in cracking order, a second last time out and a winner two starts back, with five seconds-or-better in her last six runs and only nine days since her last outing.
    DATA: model 27.4% | style Prominent (led 8% of runs) | runs in data 12 | last 3: 28 Oct Dundalk (AW) (IRE) Flat 8f Standard 2/11 fig 74; 6 Nov Dundalk (AW) (IRE) Flat 12f Standard 1/10 fig 68; 11 Nov Dundalk (AW) (IRE) Flat 8f Standard 2/8 fig 78
    DATA for: Best recent form figure 78, 19 lb above field average; Recent figures 4 lb above its current mark (looks well handicapped); Official rating 74, 9 lb above field average; Last-run finishing speed +2.8% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Trainer 0 wins from 12 runs, last 14 days; Carries 9 lb more than average
- Walhaan (hrs_15441566) | 10yo G | 140lb | OR 70 | draw 10 | jockey Patrick McGettigan | trainer Ciaran Murphy (14d 0/13) | headgear tp | last run 9 days | form 800306 | MARKET 6.3% | 09:00 median 13.00 | Matchbook 14.50
    comment: The risk is a winless record in his last six, with only a third three starts back to show.
    DATA: model 7.6% | style Midfield (led 4% of runs) | runs in data 9 | last 3: 25 Sep Dundalk Flat 10.7f Standard 3/14; 18 Oct Leopardstown (IRE) Flat 10f Good 10/15 fig 63; 11 Nov Dundalk (AW) (IRE) Flat 10.5f Standard 6/14 fig 72
    DATA for: Best recent form figure 72, 13 lb above field average; Official rating 70, 5 lb above field average
    DATA against: Trainer 0 wins from 13 runs, last 14 days; Carries 5 lb more than average; Aged 10, older than most of this field
- Autocrat (hrs_31069185) | 6yo G | 133lb | OR 63 | draw 5 | jockey Nicola Burns(2) | trainer P Sweeney (14d 0/2) | headgear tb | last run 14 days | form 631025 | MARKET 5.6% | 09:00 median 13.00 | Matchbook 18.00
    comment: Autocrat was beaten into fifth last time out after a second two starts back, but he's winless since that success four starts back, and he has run over today's trip and going before.
    DATA: model 5.8% | style Midfield (led 5% of runs) | runs in data 14 | last 3: 12 Oct Roscommon Flat 12.2f Soft 15/16; 16 Oct Dundalk (AW) (IRE) Flat 10.5f Standard 2/13 fig 65; 6 Nov Dundalk (AW) (IRE) Flat 12f Standard 5/10 fig 59
    DATA for: Best recent form figure 65, 6 lb above field average; Has won at this trip or further
- Suerte (hrs_43417969) | 4yo F | 121lb | OR 51 | draw 11 | jockey Sadhbh Tormey(7) | trainer Ms Sheila Lavery (14d 0/1) | headgear t | last run 16 days | form 600728 | MARKET 3.2% | 09:00 median 19.00 | Matchbook 36.00
    comment: A second two starts back shows some ability, and she has run over today's trip and going, returning after 16 days.
    DATA: model 2.9% | style Held up (led 4% of runs) | runs in data 9 | last 3: 18 Sep Dundalk Flat 10.7f Standard 7/14; 7 Oct Navan Flat 10.1f Yielding 2/16; 4 Nov Dundalk (AW) (IRE) Flat 10.5f Standard 8/14 fig 44
    DATA for: Carries 14 lb less than average
    DATA against: Best recent form figure 44, 15 lb below field average; Recent figures 7 lb below its current mark (looks high in the weights); Official rating 51, 14 lb below field average; Pace: steady gallop likely, hard to come from off the pace
- Stable Lane (hrs_59025323) | 4yo G | 137lb | OR 67 | draw 2 | jockey Jimmy Dalton(4) | trainer Rodger Sweeney (14d 0/1) | headgear - | last run 19 days | form 66-20 | MARKET 2.1% | 09:00 median 34.00 | Matchbook 55.00
    comment: Stable Lane was second two starts back but unplaced last time, and he is winless in his last four, though 19 days since that run keeps him fresh and he has run on today's going.
    DATA: model 3.3% | style Prominent (led 38% of runs) | runs in data 2 | last 3: 10 Jun Limerick Flat 8f Yielding 2/13; 1 Nov Curragh (IRE) Flat 7f Yielding To Soft 25/25 fig 29
    DATA against: Best recent form figure 29, 30 lb below field average; Recent figures 38 lb below its current mark (looks high in the weights); Last-run finishing speed -4.4% vs that field (faded); Lightly raced: 2 runs in our data, so the model has little to go on
- Afloat (hrs_34360746) | 6yo M | 136lb | OR 66 | draw 12 | jockey Nina Doherty(7) | trainer Gavin Cromwell (14d 4/34) | headgear - | last run 19 days | form 608-58 | MARKET 2.0% | 09:00 median 34.00 | Matchbook 65.00
    comment: The risk is a form line of eighth, fifth, eighth that is still winless in her last five starts, with 136 lb to carry from stall 12.
    DATA: model 5.3% | style Held up (led 4% of runs) | runs in data 3 | last 3: 8 Sep Galway Flat 12f Soft 5/15; 21 Sep Listowel Flat 14.2f Yielding 8/15; 1 Nov Cork (IRE) Hurdle 16f Good To Yielding F/19
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Pepper Noir (hrs_38532179) | 5yo M | 133lb | OR 63 | draw 3 | jockey Jessica O'Gorman(4) | trainer John McConnell (14d 0/13) | headgear t | last run 23 days | form 486000 | MARKET 1.6% | 09:00 median 41.00 | Matchbook 90.00
    comment: Pepper Noir has been unplaced in her last three outings and is winless in her last six, though she's had 23 days to recover and has run over today's trip and going before.
    DATA: model 1.5% | style Held up (led 4% of runs) | runs in data 8 | last 3: 10 Jul Kilbeggan Hurdle 16f Good 8/11; 19 Sep Gowran Park Flat 9.5f Yielding To Soft 14/14; 28 Oct Dundalk (AW) (IRE) Flat 12f Standard 12/13 fig 47
    DATA against: Best recent form figure 47, 12 lb below field average; Recent figures 16 lb below its current mark (looks high in the weights); Trainer 0 wins from 13 runs, last 14 days; Poor recent finishing positions; Pace: steady gallop likely, hard to come from off the pace

## 8:15 Dundalk (AW) | race_id rac_32305058799 | Safer Gambling Week 2026 Handicap
Flat |  | 1m4f0y | going Standard | AW | 17 runners | rating band 0-60 | age 3yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Showyoutheropes (hrs_51866388) | 4yo G | 137lb | OR 55 | draw 6 | jockey Declan McDonogh | trainer G. O'Leary (14d 1/7) | headgear tb | last run 14 days | form 090602 | MARKET 14.5% | 09:00 median 4.50 | Matchbook 5.10 | CHECK (skip line 4.27)
    comment: Showyoutheropes bounced back with a second last time out just 14 days ago, and he has run over today's trip and going before.
    DATA: model 5.4% | style Held up (led 4% of runs) | runs in data 9 | last 3: 9 Oct Dundalk Flat 12f Standard 6/7; 20 Oct Curragh (IRE) Flat 10f Yielding 22/24; 6 Nov Dundalk (AW) (IRE) Flat 12f Standard 2/10 fig 51
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Young Churchill (hrs_40260626) | 5yo G | 139lb | OR 57 | draw 11 | jockey Adam Grant(7) | trainer Richard John O'Brien (14d 0/3) | headgear - | last run 7 days | form 037063 | MARKET 12.5% | 09:00 median 5.00 | Matchbook 6.20
    comment: Young Churchill showed his hand with a third last time out just seven days ago, so he arrives fit, and he has run over today's trip and going before.
    DATA: model 10.3% | style Held up (led 4% of runs) | runs in data 8 | last 3: 2 Sep Navan Flat 16f Good 6/16; 26 Sep Listowel Hurdle 20f Good 11/14; 13 Nov Dundalk (AW) (IRE) Flat 12f Standard 3/14 fig 59
    DATA for: Best recent form figure 59, 8 lb above field average; Official rating 57, 6 lb above field average
    DATA against: Carries 7 lb more than average; Pace: steady gallop likely, hard to come from off the pace
- Spy (hrs_27027315) | 7yo G | 140lb | OR 58 | draw 14 | jockey  | trainer C Byrnes (14d 0/9) | headgear v | last run 31 days | form 61-054 | MARKET 10.2% | 09:00 median 7.00 | Matchbook 7.00
    comment: Spy brings solid recent form, having won four starts back and finishing fourth last time out, and he has run over today's trip and on this going before. A 31-day break and 140 lb are the main risk, with his last two runs not yielding a win.
    DATA: model 10.9% | style Held up (led 4% of runs) | runs in data 7 | last 3: 18 Aug Roscommon Flat 12.2f Good To Yielding 15/16; 4 Sep Down Royal Flat 12.9f Good 5/12; 20 Oct Curragh (IRE) Flat 10f Yielding 4/24 fig 59
    DATA for: Best recent form figure 59, 8 lb above field average; Official rating 58, 7 lb above field average
    DATA against: Trainer 0 wins from 9 runs, last 14 days; Carries 8 lb more than average; Pace: steady gallop likely, hard to come from off the pace
- Grey Fable (hrs_30017484) | 6yo G | 140lb | OR 58 | draw 5 | jockey Ben Coen | trainer Karl Thornton (14d 0/3) | headgear t | last run 16 days | form 954263 | MARKET 9.4% | 09:00 median 7.40 | Matchbook 7.80
    comment: Grey Fable arrives fresh from a third last time out, 16 days ago, and has run over today's trip and going, but he's winless in his last six and a second three starts back shows his ceiling.
    DATA: model 8.4% | style Prominent (led 4% of runs) | runs in data 11 | last 3: 1 Oct Bellewstown Flat 12.3f Soft To Heavy 6/11; 5 Oct Fairyhouse Hurdle 16f Good 5/11; 4 Nov Musselburgh Flat 12.5f Soft 3/11 fig 62
    DATA for: Best recent form figure 62, 11 lb above field average; Recent figures 4 lb above its current mark (looks well handicapped); Official rating 58, 7 lb above field average; Last-run finishing speed +3.5% vs that field (finished strongly); Has won at this trip or further
    DATA against: Carries 8 lb more than average
- Doctor Grace (hrs_31188206) | 6yo M | 135lb | OR 53 | draw 3 | jockey Cillian Rowan(10) | trainer Adrian McGuinness (14d 4/19) | headgear v | last run 7 days | form 039041 | MARKET 9.1% | 09:00 median 7.00 | Matchbook 8.60
    comment: Won last time out and only seven days ago, so Doctor Grace arrives fit and in form, with experience of today's trip and going, but she carries 135 lb off 53 and her earlier form is patchy, a fourth two starts back then a ninth four runs ago.
    DATA: model 7.7% | style Held up (led 8% of runs) | runs in data 18 | last 3: 20 Oct Curragh (IRE) Flat 10f Yielding 16/24 fig 47; 6 Nov Dundalk (AW) (IRE) Flat 12f Standard 4/10 fig 45; 13 Nov Dundalk (AW) (IRE) Flat 12f Standard 1/14 fig 54
    DATA for: Trainer 21% wins (4/19), last 14 days; Has won at this trip or further
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Captain Hanley (hrs_47064955) | 6yo G | 132lb | OR 50 | draw 9 | jockey Colin Keane | trainer Eamonn O'Connell (14d 0/0) | headgear t | last run 96 days | form 642564 | MARKET 6.2% | 09:00 median 11.00 | Matchbook 12.00
    comment: Captain Hanley has run over today's trip and going and was fourth last time out, but he's yet to win in his last six starts and returns after 96 days off. A second four starts back is the best of that form, and carrying 132 lb off a mark of 50 looks a stiff ask.
    DATA: model 5.2% | style Held up (led 3% of runs) | runs in data 12 | last 3: 7 Jul Tramore Flat 16f Good 4/12; 8 Aug Kilbeggan Hurdle 16f Good 4/11; 16 Aug Tramore Hurdle 16.6f Good To Yielding 5/8
    DATA against: Returns from a 96-day break; Pace: steady gallop likely, hard to come from off the pace
- Tintinabulla (hrs_64073205) | 3yo F | 124lb | OR 47 | draw 2 | jockey Siobhan Rutledge | trainer Ms Sheila Lavery (14d 0/1) | headgear t | last run 50 days | form 087043 | MARKET 5.8% | 09:00 median 10.00 | Matchbook 15.50
    comment: Tintinabulla is winless in her last six, though a third last time out and a fourth two starts back show some improvement, and she has run over today's trip.
    DATA: model 3.6% | style Prominent (led 23% of runs) | runs in data 6 | last 3: 13 Jul Killarney Flat 11.3f Good 13/14; 31 Aug Roscommon Flat 12.1f Good To Yielding 4/16; 1 Oct Bellewstown Flat 12.3f Soft To Heavy 3/11
    DATA for: Carries 8 lb less than average
- Jazz Forever (hrs_32909982) | 6yo G | 128lb | OR 46 | draw 4 | jockey J M Sheridan | trainer Paul W Flynn (14d 0/5) | headgear p | last run 7 days | form 000206 | MARKET 5.1% | 09:00 median 15.00 | Matchbook 13.50
    comment: Jazz Forever is winless in his last six starts, with a sixth last time out and just one second, three starts back, to show among four other unplaced efforts, so he is hard to fancy.
    DATA: model 8.2% | style Prominent (led 8% of runs) | runs in data 13 | last 3: 18 Sep Dundalk Flat 10.7f Standard 2/14; 9 Oct Dundalk Flat 10.7f Standard 10/14; 13 Nov Dundalk (AW) (IRE) Flat 12f Standard 6/14 fig 44
    DATA against: Best recent form figure 44, 7 lb below field average; Official rating 46, 5 lb below field average
- Preparations (hrs_40260703) | 5yo M | 142lb | OR 60 | draw 10 | jockey Sam Coen(5) | trainer A. Slattery (14d 0/13) | headgear - | last run 8 days | form 061570 | MARKET 4.8% | 09:00 median 13.00 | Matchbook 19.00
    comment: Preparations won four starts back but has since drifted, with a fifth three starts back and a seventh two starts back before going unplaced last time, though she's back quickly after eight days and has run over today's trip and going.
    DATA: model 7.6% | style Midfield (led 4% of runs) | runs in data 8 | last 3: 30 Sep Bellewstown Flat 12.5f Soft To Heavy 7/12; 15 Oct Curragh (IRE) Flat 14f Yielding To Soft 14/21 fig 43; 12 Nov Thurles (IRE) Hurdle 20f Good 6/10 fig 102
    DATA for: Official rating 60, 9 lb above field average; Has won at this trip or further
    DATA against: Best recent form figure 43, 8 lb below field average; Recent figures 17 lb below its current mark (looks high in the weights); Trainer 0 wins from 13 runs, last 14 days; Poor recent finishing positions; Carries 10 lb more than average
- Barretstown (hrs_21837641) | 8yo G | 132lb | OR 50 | draw 13 | jockey W. J. Lee | trainer Conor O'Dwyer (14d 0/2) | headgear - | last run 35 days | form 000843 | MARKET 4.6% | 09:00 median 13.00 | Matchbook 18.50
    comment: Barretstown arrives on an upward curve after a third last time out and a fourth two starts back, and he has run on today's going before, but he is yet to win in his last six and carries 132 lb after 35 days off.
    DATA: model 3.7% | style Midfield (led 4% of runs) | runs in data 10 | last 3: 10 Sep Laytown Flat 7f Standard 8/10; 9 Oct Dundalk Flat 10.7f Standard 4/14; 16 Oct Dundalk (AW) (IRE) Flat 10.5f Standard 3/13 fig 69
    DATA for: Best recent form figure 69, 18 lb above field average; Recent figures 19 lb above its current mark (looks well handicapped)
    DATA against: Aged 8, older than most of this field
- All Is Bright (hrs_57315916) | 3yo F | 130lb | OR 53 | draw 17 | jockey Luke McAteer | trainer J S Bolger (14d 0/0) | headgear - | last run 53 days | form 800-6 | MARKET 4.2% | 09:00 median 17.00 | Matchbook 18.00
    comment: All Is Bright is winless in her last four, though a sixth last time out is her best recent effort, and she has run over today's trip and going before.
    DATA: model 8.6% | style Held up (led 8% of runs) | runs in data 1 | last 3: 28 Sep Down Royal Flat 11f Good To Yielding 6/14
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Esticky End (hrs_21686623) | 8yo G | 129lb | OR 47 | draw 8 | jockey  | trainer Tom McGuinness (14d 1/3) | headgear - | last run 8 days | form 5R96-9 | MARKET 3.3% | 09:00 median 21.00 | Matchbook 24.00
    comment: Esticky End has been well beaten in his last two outings, finishing a ninth last time out, and he has yet to win in recent starts, though a quick 8-day turnaround and experience over today's trip and going offer some comfort.
    DATA: model 3.7% | style Held up (led 4% of runs) | runs in data 9 | last 3: 19 Oct Gowran Park (IRE) Flat 8.5f Soft 9/16 fig 41; 25 Oct Wexford (IRE) Hurdle 17f Soft PU/13; 12 Nov Thurles (IRE) Chase 21.5f Good PU/15
    DATA against: Best recent form figure 41, 10 lb below field average; Recent figures 6 lb below its current mark (looks high in the weights); Poor recent finishing positions; Aged 8, older than most of this field; Pace: steady gallop likely, hard to come from off the pace
- Star Mind (hrs_37123597) | 5yo M | 142lb | OR 60 | draw 16 | jockey Danny O'Leary(10) | trainer G. O'Leary (14d 1/7) | headgear - | last run 16 days | form 806520 | MARKET 2.6% | 09:00 median 29.00 | Matchbook 29.00
    comment: The risk is a winless run in her last six, including an unplaced effort last time out.
    DATA: model 9.3% | style Midfield (led 4% of runs) | runs in data 10 | last 3: 18 Sep Dundalk Flat 10.7f Standard 5/14; 9 Oct Dundalk Flat 10.7f Standard 2/14; 4 Nov Dundalk (AW) (IRE) Flat 10.5f Standard 10/14 fig 50
    DATA for: Official rating 60, 9 lb above field average
    DATA against: Recent figures 10 lb below its current mark (looks high in the weights); Carries 10 lb more than average
- Just Another Eagle (hrs_35650223) | 6yo M | 125lb | OR 43 | draw 12 | jockey  | trainer Patrick J Flynn (14d 1/8) | headgear - | last run 43 days | form S-0900 | MARKET 2.4% | 09:00 median 29.00 | Matchbook 36.00
    comment: Just Another Eagle is winless in her last five starts, with nothing better than a ninth three starts back and unplaced efforts either side, so she is hard to fancy at 125 lb after 43 days off.
    DATA: model 3.7% | style Prominent (led 3% of runs) | runs in data 4 | last 3: 7 Jun Navan Flat 13f Good 9/14; 20 Jun Down Royal Flat 12.9f Soft 11/14; 8 Oct Thurles Flat 12.7f Yielding 12/14
    DATA for: Carries 7 lb less than average
    DATA against: Official rating 43, 8 lb below field average; Last-run finishing speed -6.6% vs that field (faded); Poor recent finishing positions
- Lisnadill (hrs_47282347) | 4yo F | 125lb | OR 43 | draw 15 | jockey Nicola Burns(5) | trainer John McConnell (14d 0/13) | headgear - | last run 16 days | form 6-0006 | MARKET 1.9% | 09:00 median 34.00 | Matchbook 46.00
    comment: Lisnadill is yet to win in her last five starts, though a sixth last time out just 16 days ago suggests she's holding her form, and she has run on today's going before.
    DATA: model 1.1% | style Held up (led 8% of runs) | runs in data 6 | last 3: 28 Aug Down Royal Hurdle 20f Good 7/8; 18 Sep Downpatrick Hurdle 17.8f Good F/15; 4 Nov Dundalk (AW) (IRE) Flat 10.5f Standard 6/14 fig 41
    DATA for: Carries 7 lb less than average
    DATA against: Best recent form figure 41, 10 lb below field average; Official rating 43, 8 lb below field average; Trainer 0 wins from 13 runs, last 14 days; Poor recent finishing positions; Pace: steady gallop likely, hard to come from off the pace
- Trovao Dourado (hrs_7000002520) | 4yo G | 130lb | OR 48 | draw 7 | jockey Donagh O'Connor | trainer Ciaran Murphy (14d 0/13) | headgear - | last run 14 days | form 5005 | MARKET 1.8% | 09:00 median 41.00 | Matchbook 46.00
    comment: Winless in his last four, Trovao Dourado was fifth last time out, 14 days ago, and unplaced in the two runs before that, so he is hard to fancy off 130 lb.
    DATA: model 1.0% | style Midfield (led 4% of runs) | runs in data 4 | last 3: 6 Aug Leopardstown Flat 9f Good 11/14; 15 Aug Dundalk Flat 7f Standard 14/14; 6 Nov Dundalk (AW) (IRE) Flat 5f Standard 5/5 fig 39
    DATA against: Best recent form figure 39, 12 lb below field average; Recent figures 9 lb below its current mark (looks high in the weights); Trainer 0 wins from 13 runs, last 14 days
- Lady Crossing (hrs_51865912) | 4yo F | 122lb | OR 40 | draw 1 | jockey Rory Mulligan(5) | trainer William J Fitzpatrick (14d 0/0) | headgear h (1st time) | last run 44 days | form -80400 | MARKET 1.7% | 09:00 median 51.00 | Matchbook 46.00
    comment: Lady Crossing is winless in her last five, with two unplaced runs most recently and just a fourth three starts back to show, and she returns after 44 days carrying 122 lb off a mark of 40. She has run on today's going, but little else makes her easy to fancy.
    DATA: model 1.6% | style Midfield (led 4% of runs) | runs in data 5 | last 3: 19 Jun Limerick Flat 8f Soft 4/13; 9 Jul Leopardstown Flat 9f Good 20/22; 7 Oct Navan Flat 10.1f Yielding 13/16
    DATA for: Carries 10 lb less than average; First-time headgear
    DATA against: Official rating 40, 11 lb below field average
