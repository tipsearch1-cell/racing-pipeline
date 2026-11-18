# Card review packet: Dundalk (AW), 2026-11-18

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
{"meeting": "dundalk_aw", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 2:00 Dundalk (AW) | race_id rac_32304739194 | Irish Stallion Farms EBF Auction Maiden
Flat |  | 7f | going Standard | AW | 17 runners | rating band - | age 2yo
DATA pace: Unclear - Running styles known for only 7 of 17 runners.
- Coloursofthewind (hrs_17392883081) | 2yo F | 126lb | OR - | draw 17 | jockey Ben Coen | trainer Joseph G Murphy (14d 0/0) | headgear - | last run 21 days | form 3 | MARKET 17.3% | 09:00 median 3.75 | Matchbook 5.00 | CHECK (skip line 3.56)
    DATA: model 9.8% | style Unknown | runs in data 1 | last 3: 28 Oct Dundalk (AW) (IRE) 7f Standard 3/14 fig 65
    DATA for: Best recent form figure 65, 15 lb above field average; Last-run finishing speed +2.1% vs that field (finished strongly)
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Celtic Comet (hrs_17394337023) | 2yo G | 131lb | OR - | draw 8 | jockey Donagh O'Connor | trainer Robson De Aguiar (14d 1/6) | headgear - | last run 26 days | form 5 | MARKET 17.3% | 09:00 median 4.33 | Matchbook 4.50
    DATA: model 10.6% | style Unknown | runs in data 1 | last 3: 23 Oct Dundalk (AW) (IRE) 8f Standard 5/14 fig 71
    DATA for: Best recent form figure 71, 21 lb above field average
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Rayastar (hrs_17394525806) | 2yo C | 133lb | OR - | draw 2 | jockey Chris Hayes | trainer P J F Murphy (14d 0/4) | headgear - | last run 21 days | form 4 | MARKET 16.3% | 09:00 median 4.50 | Matchbook 4.70
    DATA: model 15.0% | style Unknown | runs in data 1 | last 3: 28 Oct Dundalk (AW) (IRE) 6f Standard 4/13 fig 54
    DATA for: Best recent form figure 54, 4 lb above field average; Last-run finishing speed +2.8% vs that field (finished strongly)
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Miss Cashman Hooke (hrs_17391063046) | 2yo F | 128lb | OR - | draw 5 | jockey W. J. Lee | trainer Miss Natalia Lupini (14d 1/3) | headgear - | last run 67 days | form 40 | MARKET 16.3% | 09:00 median 4.50 | Matchbook 4.60
    DATA: model 7.5% | style Held up (led 8% of runs) | runs in data 2 | last 3: 23 Aug Naas 5.9f Good 4/15; 12 Sep Leopardstown 7f Good 10/10
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Jezzie Bea (hrs_66272178) | 2yo F | 122lb | OR - | draw 12 | jockey Nathan Crosse | trainer Mrs J. Harrington (14d 1/9) | headgear p (1st time) | last run 83 days | form 443 | MARKET 7.9% | 09:00 median 7.50 | Matchbook 12.00
    DATA: model 12.8% | style Leader (led 29% of runs) | runs in data 3 | last 3: 30 Jun Roscommon 7.4f Good 4/15; 16 Jul Leopardstown 7.2f Good 4/12; 27 Aug Navan 8.1f Good 3/6
    DATA for: First-time headgear
- Togetherwearefree (hrs_17391068261) | 2yo F | 128lb | OR - | draw 16 | jockey  | trainer Joseph Patrick O'Brien (14d 3/22) | headgear - | last run 41 days | form 07 | MARKET 5.5% | 09:00 median 11.00 | Matchbook 19.00
    DATA: model 5.5% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 30 Aug Cork 8f Yielding 14/15; 8 Oct Thurles 8.3f Good To Yielding 7/14
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Bella Cheval (hrs_17394524763) | 2yo F | 122lb | OR - | draw 10 | jockey W. M. Lordan | trainer Noel Meade (14d 3/11) | headgear - | last run - days | form - | MARKET 4.2% | 09:00 median 17.00 | Matchbook 18.50
    DATA: model 4.3% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 27% wins (3/11), last 14 days
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Sorrento Bay (hrs_17392790254) | 2yo F | 128lb | OR - | draw 14 | jockey Declan McDonogh | trainer Joseph Patrick O'Brien (14d 3/22) | headgear - | last run - days | form - | MARKET 4.2% | 09:00 median 17.00 | Matchbook 19.50
    DATA: model 4.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Royal Saxon (hrs_17395565677) | 2yo F | 126lb | OR - | draw 4 | jockey James Ryan | trainer Conor David Maxwell (14d 0/0) | headgear h (1st time) | last run - days | form - | MARKET 2.4% | 09:00 median 26.00 | Matchbook 42.00
    DATA: model 4.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: First-time headgear
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Unstoppable Army (hrs_17394009521) | 2yo G | 127lb | OR - | draw 15 | jockey  | trainer Gavin Cromwell (14d 4/34) | headgear - | last run 30 days | form 7 | MARKET 1.9% | 09:00 median 51.00 | Matchbook 42.00
    DATA: model 5.2% | style Held up (led 8% of runs) | runs in data 1 | last 3: 19 Oct Gowran Park (IRE) 8.5f Soft 7/14 fig 48
    DATA for: Last-run finishing speed +2.1% vs that field (finished strongly)
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Lake Havasu (hrs_17395564634) | 2yo F | 122lb | OR - | draw 9 | jockey R. P. Cleary | trainer Kevin Thomas Coleman (14d 0/2) | headgear t (1st time) | last run - days | form - | MARKET 1.5% | 09:00 median 61.00 | Matchbook 55.00
    DATA: model 4.3% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: First-time headgear
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Chachaboo (hrs_17395562548) | 2yo C | 125lb | OR - | draw 6 | jockey Robert Whearty | trainer Gavin Cromwell (14d 4/34) | headgear - | last run - days | form - | MARKET 1.1% | 09:00 median 81.00 | Matchbook 80.00
    DATA: model 4.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Silent Promise (hrs_17392277098) | 2yo F | 124lb | OR - | draw 13 | jockey  | trainer Adrian McGuinness (14d 4/17) | headgear - | last run 17 days | form 90 | MARKET 1.0% | 09:00 median 67.00 | Matchbook 120.00
    DATA: model 3.2% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 15 Oct Curragh (IRE) 8f Soft 9/15 fig 51; 1 Nov Curragh (IRE) 8f Yielding To Soft 12/23 fig 52
    DATA for: Trainer 24% wins (4/17), last 14 days
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Legacy Of Stardom (hrs_17393389979) | 2yo C | 125lb | OR - | draw 7 | jockey Patrick McGettigan(5) | trainer Mrs Denise Foster (14d 0/0) | headgear - | last run 21 days | form 0 | MARKET 0.9% | 09:00 median 51.00 | Matchbook 140.00
    DATA: model 2.7% | style Unknown | runs in data 1 | last 3: 28 Oct Dundalk (AW) (IRE) 6f Standard 11/13 fig 39
    DATA against: Best recent form figure 39, 11 lb below field average; Lightly raced: 1 run in our data, so the model has little to go on
- Dramatic Approach (hrs_17393432742) | 2yo C | 127lb | OR - | draw 11 | jockey Leigh Roche | trainer Mrs J. Harrington (14d 1/9) | headgear - | last run 21 days | form 08 | MARKET 0.8% | 09:00 median 67.00 | Matchbook 200.00
    DATA: model 2.8% | style Unknown | runs in data 2 | last 3: 8 Oct Thurles 8.3f Good To Yielding 11/14; 28 Oct Dundalk (AW) (IRE) 7f Standard 8/11 fig 52
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Courtier (hrs_17392276055) | 2yo C | 125lb | OR - | draw 1 | jockey Seamie Heffernan | trainer S. R. B. Crawford (14d 1/9) | headgear - | last run 21 days | form 00 | MARKET 0.8% | 09:00 median 151.00 | Matchbook 80.00
    DATA: model 1.5% | style Midfield (led 8% of runs) | runs in data 2 | last 3: 19 Sep Gowran Park 8f Yielding To Soft 12/12; 28 Oct Dundalk (AW) (IRE) 7f Standard 10/11 fig 35
    DATA against: Best recent form figure 35, 15 lb below field average; Lightly raced: 2 runs in our data, so the model has little to go on
- Sevengrandchildren (hrs_17393393108) | 2yo C | 125lb | OR - | draw 3 | jockey Adam Caffrey | trainer Michael Mulvany (14d 0/6) | headgear t | last run 28 days | form 00 | MARKET 0.6% | 09:00 median 201.00 | Matchbook 160.00
    DATA: model 1.5% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 10 Oct Naas 8f Soft 17/18; 21 Oct Navan (IRE) 6f Yielding 14/14 fig 33
    DATA against: Best recent form figure 33, 17 lb below field average; Lightly raced: 2 runs in our data, so the model has little to go on

## 2:30 Dundalk (AW) | race_id rac_32305039429 | Dundalk Stadium Gift Vouchers Available Online Handicap (Div I)
Flat |  | 7f | going Standard | AW | 17 runners | rating band 0-60 | age 3yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Pocket Jacks (hrs_59025295) | 3yo F | 138lb | OR 57 | draw 17 | jockey W. J. Lee | trainer A Oliver (14d 0/0) | headgear - | last run 21 days | form -63261 | MARKET 21.2% | 09:00 median 3.50 | Matchbook 3.65 | CHECK (skip line 3.32)
    DATA: model 16.8% | style Prominent (led 5% of runs) | runs in data 5 | last 3: 12 Jun Gowran Park 7f Yielding 2/12; 19 Oct Gowran Park (IRE) 7f Yielding 6/13 fig 51; 28 Oct Dundalk (AW) (IRE) 7f Standard 1/14 fig 59
    DATA for: Best recent form figure 59, 12 lb above field average; Official rating 57, 6 lb above field average; Last-run finishing speed +2.1% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Carries 5 lb more than average
- The Bear Trap (hrs_35040054) | 5yo G | 142lb | OR 60 | draw 5 | jockey Cillian Rowan(10) | trainer Adrian McGuinness (14d 4/17) | headgear v | last run 7 days | form -40971 | MARKET 16.0% | 09:00 median 4.50 | Matchbook 5.00
    comment: Won last time out and turned out again just seven days later, but that came after a seventh two starts back and a ninth three starts back, so consistency is the question.
    DATA: model 21.6% | style Prominent (led 5% of runs) | runs in data 5 | last 3: 12 Oct Roscommon 7.5f Soft 9/14; 28 Oct Dundalk (AW) (IRE) 7f Standard 7/14 fig 53; 11 Nov Dundalk (AW) (IRE) 7f Standard 1/14 fig 59
    DATA for: Best recent form figure 59, 12 lb above field average; Official rating 60, 9 lb above field average; Trainer 24% wins (4/17), last 14 days; Has won at this trip or further
    DATA against: Carries 9 lb more than average
- Strikepoint (hrs_65869475) | 3yo G | 128lb | OR 47 | draw 14 | jockey R. P. Cleary | trainer John James Feane (14d 0/0) | headgear - | last run 21 days | form 709003 | MARKET 10.6% | 09:00 median 6.50 | Matchbook 8.00
    comment: Strikepoint comes into this off a third last time out, 21 days ago, and has run over today's trip and going, but he's winless in his last six and was unplaced in three of the previous five.
    DATA: model 6.2% | style Midfield (led 5% of runs) | runs in data 6 | last 3: 29 Aug Curragh 6f Yielding 16/19; 19 Oct Gowran Park (IRE) 8.5f Soft 12/16 fig 38; 28 Oct Dundalk (AW) (IRE) 7f Standard 3/13 fig 47
- Chester Nimitz (hrs_43859977) | 4yo G | 139lb | OR 57 | draw 1 | jockey Ben Coen | trainer G. O'Leary (14d 1/6) | headgear - | last run 19 days | form 990909 | MARKET 8.3% | 09:00 median 8.50 | Matchbook 10.00
    comment: The risk is obvious: he's winless in his last six, with a ninth last time out, a ninth six starts back among his finishes.
    DATA: model 7.9% | style Midfield (led 4% of runs) | runs in data 7 | last 3: 3 Aug Naas 7f Good 9/16; 22 Aug Curragh 6f Good 23/27; 30 Oct Dundalk (AW) (IRE) 8f Standard 9/14 fig 53
    DATA for: Best recent form figure 53, 6 lb above field average; Official rating 57, 6 lb above field average
    DATA against: Poor recent finishing positions; Carries 6 lb more than average
- Pinar Del Rio (hrs_24819501) | 7yo G | 139lb | OR 57 | draw 7 | jockey Leigh Roche | trainer Alan McIntyre (14d 0/1) | headgear p | last run 34 days | form 405700 | MARKET 7.1% | 09:00 median 10.00 | Matchbook 11.50
    comment: The risk is a winless run, with nothing better than a fourth six starts back, and 139 lb to carry.
    DATA: model 5.4% | style Held up (led 3% of runs) | runs in data 6 | last 3: 22 Aug Curragh 6f Good 7/27; 9 Sep Cork 6f Good 21/22; 15 Oct Curragh (IRE) 7f Soft 19/20
    DATA for: Official rating 57, 6 lb above field average
    DATA against: Poor recent finishing positions; Carries 6 lb more than average; Pace: steady gallop likely, hard to come from off the pace
- Jazzy Dancer (hrs_26874890) | 8yo G | 133lb | OR 51 | draw 11 | jockey Rory Mulligan(5) | trainer W J Martin (14d 0/2) | headgear - | last run 21 days | form 079082 | MARKET 6.7% | 09:00 median 8.50 | Matchbook 16.50
    comment: Jazzy Dancer arrives fresh off a second last time out, 21 days ago, and has run over today's trip and going, but he's yet to win in his last six starts and was eighth and ninth in two of the runs before that.
    DATA: model 4.9% | style Prominent (led 8% of runs) | runs in data 8 | last 3: 11 Jul Limerick 6.7f Good 11/14; 16 Oct Dundalk (AW) (IRE) 7f Standard 8/14 fig 49; 28 Oct Dundalk (AW) (IRE) 7f Standard 2/13 fig 51
    DATA for: Has won at this trip or further
- Auguste Gusteau (hrs_56127792) | 3yo G | 124lb | OR 43 | draw 13 | jockey Alan Persse(5) | trainer M A Cahill (14d 0/2) | headgear - | last run 21 days | form 679704 | MARKET 4.9% | 09:00 median 13.00 | Matchbook 19.50
    comment: Winless in his last six, Auguste Gusteau was fourth last time out but was beaten in the five runs before that, and he has run over today's trip and going.
    DATA: model 3.9% | style Prominent (led 4% of runs) | runs in data 6 | last 3: 8 Jul Fairyhouse 7f Good 7/15; 24 Jul Cork 6f Good To Firm 13/19; 28 Oct Dundalk (AW) (IRE) 7f Standard 4/14 fig 42
    DATA for: Carries 9 lb less than average
    DATA against: Best recent form figure 42, 5 lb below field average; Official rating 43, 8 lb below field average
- Glen Breeze (hrs_55700757) | 3yo G | 124lb | OR 43 | draw 10 | jockey Chris Hayes | trainer Patrick Magee (14d 0/5) | headgear tp | last run 14 days | form 905796 | MARKET 4.4% | 09:00 median 17.00 | Matchbook 18.50
    comment: Glen Breeze is winless in his last six, with a fifth four starts back the best of a run that includes a sixth last time out, a ninth and a seventh, so he is hard to fancy.
    DATA: model 3.0% | style Midfield (led 5% of runs) | runs in data 17 | last 3: 1 Oct Bellewstown 7.9f Soft To Heavy 7/9; 28 Oct Dundalk (AW) (IRE) 7f Standard 9/13 fig 38; 4 Nov Dundalk (AW) (IRE) 7f Standard 6/13 fig 45
    DATA for: Has won at this trip or further; Carries 9 lb less than average
    DATA against: Official rating 43, 8 lb below field average; Poor recent finishing positions
- U S S Constitution (hrs_29227303) | 6yo G | 142lb | OR 60 | draw 12 | jockey Sadhbh Tormey(7) | trainer T G McCourt (14d 0/1) | headgear - | last run 175 days | form 0-1356 | MARKET 4.2% | 09:00 median 17.00 | Matchbook 20.00
    comment: U S S Constitution won four starts back and was third three starts back, and he has run over today's trip and going before, though a sixth last time out and 175 days off are the reservation.
    DATA: model 12.5% | style Midfield (led 3% of runs) | runs in data 4 | last 3: 28 Feb Lingfield 7f Standard 3/7; 25 Apr Doncaster 8f Good To Firm 5/12; 27 May Kempton 8f Standard To Slow 6/14
    DATA for: Official rating 60, 9 lb above field average; Has won at this trip or further
    DATA against: Carries 9 lb more than average; Returns from a 175-day break
- Notforalongtime (hrs_18518927) | 9yo G | 136lb | OR 54 | draw 16 | jockey Robbie Colgan | trainer Laura Hourigan (14d 0/1) | headgear b | last run 70 days | form 385800 | MARKET 3.2% | 09:00 median 23.00 | Matchbook 28.00
    comment: Winless in his last six, Notforalongtime was unplaced last time out and returns after 70 days, though he has run over today's trip and going before.
    DATA: model 2.9% | style Held up (led 3% of runs) | runs in data 11 | last 3: 19 Jun Limerick 8f Soft 8/13; 16 Jul Leopardstown 7.2f Good 12/14; 9 Sep Cork 7f Good 19/22
    DATA against: Last-run finishing speed -4.3% vs that field (faded); Poor recent finishing positions; Aged 9, older than most of this field; Pace: steady gallop likely, hard to come from off the pace
- Jackandthefox (hrs_32554165) | 7yo G | 122lb | OR 35 | draw 4 | jockey  | trainer Miss Jennifer Anne Lynch (14d 0/0) | headgear p | last run 14 days | form 455007 | MARKET 2.5% | 09:00 median 26.00 | Matchbook 38.00
    comment: Winless in his last six, Jackandthefox was seventh last time out, unplaced twice before that, and has not finished better than a fourth in that spell.
    DATA: model 1.6% | style Midfield (led 4% of runs) | runs in data 8 | last 3: 5 Sep Navan 5f Good 13/18; 7 Oct Navan 5.8f Yielding 20/22; 4 Nov Dundalk (AW) (IRE) 7f Standard 7/13 fig 31
    DATA for: Carries 11 lb less than average
    DATA against: Best recent form figure 31, 16 lb below field average; Official rating 35, 16 lb below field average; Poor recent finishing positions
- Aughlish (hrs_62101641) | 3yo F | 133lb | OR 52 | draw 2 | jockey  | trainer Ms Claire O'Connell (14d 0/1) | headgear - | last run 14 days | form 770006 | MARKET 2.3% | 09:00 median 29.00 | Matchbook 38.00
    comment: Winless in her last six, Aughlish was sixth last time out just 14 days ago and has run over today's trip and going, but she's been unplaced in three of the previous four.
    DATA: model 2.1% | style Held up (led 5% of runs) | runs in data 10 | last 3: 15 Oct Curragh (IRE) 5f Soft 10/17 fig 55; 30 Oct Dundalk (AW) (IRE) 5f Standard 13/14 fig 46; 4 Nov Dundalk (AW) (IRE) 6f Standard 6/8 fig 54
    DATA for: Best recent form figure 55, 8 lb above field average
    DATA against: Poor recent finishing positions; Pace: steady gallop likely, hard to come from off the pace
- Goldsmith (hrs_24685892) | 7yo G | 137lb | OR 55 | draw 9 | jockey Seamie Heffernan | trainer H D McGuigan (14d 0/0) | headgear h | last run 173 days | form 0700-0 | MARKET 1.9% | 09:00 median 41.00 | Matchbook 44.00
    comment: Goldsmith is winless in his last five, unplaced last time out and a seventh four starts back, and returns after 173 days off.
    DATA: model 2.1% | style Unknown | runs in data 1 | last 3: 29 May Down Royal 7f Good 13/14
    DATA against: Returns from a 173-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Sayonara (hrs_59246964) | 3yo G | 132lb | OR 51 | draw 8 | jockey Jimmy Dalton(7) | trainer A. Slattery (14d 0/14) | headgear tv (1st time) | last run 12 days | form 423000 | MARKET 1.9% | 09:00 median 41.00 | Matchbook 44.00
    comment: Sayonara has been unplaced in his last three outings, though a third four starts back and a second five starts back show he can get involved, and he is back quickly after 12 days, having run over today's trip and going.
    DATA: model 3.6% | style Prominent (led 8% of runs) | runs in data 11 | last 3: 9 Sep Cork 7f Good 14/22; 5 Oct Killarney 8.1f Soft 10/15; 6 Nov Dundalk (AW) (IRE) 8f Standard 14/14 fig 36
    DATA for: First-time headgear
    DATA against: Best recent form figure 36, 11 lb below field average; Recent figures 15 lb below its current mark (looks high in the weights); Trainer 0 wins from 14 runs, last 14 days; Last-run finishing speed -2.7% vs that field (faded); Poor recent finishing positions
- Pure Valour (hrs_62583115) | 4yo F | 122lb | OR 38 | draw 3 | jockey  | trainer J G Coogan (14d 0/0) | headgear - | last run 81 days | form 976060 | MARKET 1.8% | 09:00 median 51.00 | Matchbook 46.00
    comment: Pure Valour is hard to fancy, winless in her last six with a best finish of sixth, and she returns after 81 days off. She has run over today's trip and going, and drawn three, but the form gives little to lean on.
    DATA: model 0.9% | style Prominent (led 3% of runs) | runs in data 6 | last 3: 1 Jul Fairyhouse 8.7f Good 12/12; 16 Aug Curragh 5f Good 6/11; 29 Aug Curragh 6f Yielding 17/19
    DATA for: Carries 11 lb less than average
    DATA against: Official rating 38, 13 lb below field average; Poor recent finishing positions
- Hastily (hrs_24686312) | 7yo M | 122lb | OR 40 | draw 6 | jockey Killian Leonard | trainer Tom McGuinness (14d 0/1) | headgear p | last run 14 days | form 909659 | MARKET 1.6% | 09:00 median 41.00 | Matchbook 55.00
    comment: Hastily is hard to fancy, having finished ninth last time out and without a win in her last six starts, with a fifth two starts back her best recent effort. She has run over today's trip and going, and is fresh enough after 14 days.
    DATA: model 2.1% | style Midfield (led 5% of runs) | runs in data 10 | last 3: 9 Oct Dundalk 7f Standard 6/14; 23 Oct Dundalk (AW) (IRE) 7f Standard 5/9 fig 44; 4 Nov Dundalk (AW) (IRE) 7f Standard 9/13 fig 33
    DATA for: Recent figures 4 lb above its current mark (looks well handicapped); Carries 11 lb less than average
    DATA against: Official rating 40, 11 lb below field average
- Profit Surge (hrs_44450672) | 5yo M | 141lb | OR 59 | draw 15 | jockey James Ryan | trainer Ian Patrick Donoghue (14d 0/11) | headgear tb | last run 40 days | form 314090 | MARKET 1.4% | 09:00 median 41.00 | Matchbook 75.00
    comment: The risk is a recent slide, unplaced last time out and a ninth two starts back, after 40 days off.
    DATA: model 2.5% | style Midfield (led 3% of runs) | runs in data 13 | last 3: 10 Sep Laytown 6f Standard 10/10; 25 Sep Dundalk 6f Standard 9/13; 9 Oct Dundalk 7f Standard 12/14
    DATA for: Official rating 59, 8 lb above field average; Has won at this trip or further
    DATA against: Trainer 0 wins from 11 runs, last 14 days; Poor recent finishing positions; Carries 8 lb more than average

## 3:00 Dundalk (AW) | race_id rac_32304741131 | Dundalk Stadium Gift Vouchers Available Online Handicap (Div II)
Flat |  | 7f | going Standard | AW | 16 runners | rating band 0-60 | age 3yo+
DATA pace: Even - Two likely leaders (Hot To Foxtrot, Akashaa). A fair, even gallop is most likely.
- Jazzit (hrs_47868625) | 4yo G | 140lb | OR 58 | draw 2 | jockey James Ryan | trainer T G McCourt (14d 0/1) | headgear - | last run 21 days | form 320412 | MARKET 16.3% | 09:00 median 4.00 | Matchbook 4.10 | CHECK (skip line 3.80)
    DATA: model 17.0% | style Midfield (led 8% of runs) | runs in data 13 | last 3: 10 Sep Laytown 6f Standard 4/9; 16 Oct Dundalk (AW) (IRE) 7f Standard 1/14 fig 56; 28 Oct Dundalk (AW) (IRE) 7f Standard 2/14 fig 60
    DATA for: Best recent form figure 60, 13 lb above field average; Official rating 58, 9 lb above field average; Last-run finishing speed +3.3% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Carries 9 lb more than average
- Four Blondes (hrs_36387379) | 5yo M | 139lb | OR 57 | draw 1 | jockey W. J. Lee | trainer Ross O'Sullivan (14d 1/12) | headgear - | last run 33 days | form 056903 | MARKET 10.6% | 09:00 median 6.50 | Matchbook 6.20
    comment: Four Blondes steps up after a third last time out, and she has run over today's trip and going before, with 33 days since that run.
    DATA: model 11.9% | style Prominent (led 4% of runs) | runs in data 7 | last 3: 21 Sep Fairyhouse 6f Good 9/17; 7 Oct Navan 5.8f Yielding 10/22; 16 Oct Dundalk (AW) (IRE) 7f Standard 3/14 fig 60
    DATA for: Best recent form figure 60, 13 lb above field average; Official rating 57, 8 lb above field average
    DATA against: Carries 8 lb more than average
- She's On The Ball (hrs_57816185) | 3yo F | 131lb | OR 50 | draw 14 | jockey W. M. Lordan | trainer Laura Hourigan (14d 0/1) | headgear t | last run 34 days | form 583120 | MARKET 10.6% | 09:00 median 6.00 | Matchbook 7.00
    comment: She's On The Ball showed a winner three starts back, then a second two starts back, but was unplaced last time out and returns after 34 days; she has run over today's trip and going before.
    DATA: model 11.1% | style Midfield (led 5% of runs) | runs in data 9 | last 3: 9 Sep Cork 7f Good 1/22; 22 Sep Listowel 7.1f Yielding 2/15; 15 Oct Curragh (IRE) 7f Soft 12/20 fig 44
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Recent figures 6 lb below its current mark (looks high in the weights)
- Imperial Dream (hrs_31274348) | 6yo G | 133lb | OR 51 | draw 8 | jockey Robyn Donaghue-Leahy(7) | trainer Patrick J Flynn (14d 1/8) | headgear - | last run 41 days | form 000248 | MARKET 9.5% | 09:00 median 7.00 | Matchbook 7.80
    DATA: model 8.0% | style Prominent (led 23% of runs) | runs in data 7 | last 3: 8 Sep Galway 7f Soft 2/11; 22 Sep Listowel 7.1f Yielding 4/15; 8 Oct Thurles 8.3f Yielding 8/13
    DATA against: Last-run finishing speed -2.1% vs that field (faded)
- Pallatine Hills (hrs_44721957) | 4yo G | 140lb | OR 58 | draw 13 | jockey Siobhan Rutledge | trainer Eddie & Patrick Harty (14d 1/3) | headgear b | last run 21 days | form 605003 | MARKET 9.2% | 09:00 median 7.50 | Matchbook 8.40
    comment: The risk is that he's yet to win in his last six starts.
    DATA: model 8.6% | style Prominent (led 29% of runs) | runs in data 7 | last 3: 28 Sep Roscommon 15.6f Good To Yielding 7/13; 20 Oct Curragh (IRE) 8f Yielding 14/23 fig 50; 28 Oct Dundalk (AW) (IRE) 7f Standard 3/14 fig 60
    DATA for: Best recent form figure 60, 13 lb above field average; Official rating 58, 9 lb above field average
    DATA against: Carries 9 lb more than average
- Blue Anthem (hrs_43951131) | 4yo G | 139lb | OR 57 | draw 16 | jockey Camillus Byrne(10) | trainer Adrian McGuinness (14d 4/17) | headgear tv | last run 7 days | form 322584 | MARKET 9.2% | 09:00 median 7.50 | Matchbook 7.20
    comment: The main risk is that he is yet to win in his last six starts and was an eighth two runs ago.
    DATA: model 15.0% | style Held up (led 8% of runs) | runs in data 12 | last 3: 23 Oct Dundalk (AW) (IRE) 6f Standard 5/14 fig 55; 30 Oct Dundalk (AW) (IRE) 5f Standard 8/14 fig 49; 11 Nov Dundalk (AW) (IRE) 7f Standard 4/14 fig 57
    DATA for: Best recent form figure 57, 10 lb above field average; Official rating 57, 8 lb above field average; Trainer 24% wins (4/17), last 14 days
    DATA against: Carries 8 lb more than average
- Akashaa (hrs_44232720) | 4yo F | 122lb | OR 40 | draw 4 | jockey Chris Hayes | trainer Miss Natalia Lupini (14d 1/3) | headgear - | last run 26 days | form 668309 | MARKET 7.5% | 09:00 median 8.50 | Matchbook 10.00
    comment: Akashaa is hard to fancy, beaten into ninth last time out and winless in her last six, with just one third three starts back to show.
    DATA: model 2.8% | style Leader (led 29% of runs) | runs in data 6 | last 3: 10 Sep Laytown 6f Standard 3/9; 29 Sep Cork 6f Soft 14/19; 23 Oct Dundalk (AW) (IRE) 6f Standard 9/14 fig 34
    DATA for: Carries 9 lb less than average
    DATA against: Best recent form figure 34, 13 lb below field average; Recent figures 6 lb below its current mark (looks high in the weights); Official rating 40, 9 lb below field average
- Hot To Foxtrot (hrs_35714343) | 6yo M | 127lb | OR 45 | draw 7 | jockey Ben Coen | trainer John James Feane (14d 0/0) | headgear p | last run 21 days | form 630768 | MARKET 5.6% | 09:00 median 12.00 | Matchbook 13.50
    comment: Hot To Foxtrot has been in the grind lately, finishing eighth last time out, with a sixth two starts back and a third five starts back her best recent effort, and she's yet to win in that spell.
    DATA: model 4.2% | style Leader (led 38% of runs) | runs in data 9 | last 3: 18 Sep Dundalk 8f Standard 7/14; 16 Oct Dundalk (AW) (IRE) 7f Standard 6/14 fig 46; 28 Oct Dundalk (AW) (IRE) 7f Standard 8/14 fig 41
    DATA against: Poor recent finishing positions
- Free Solo (hrs_18504633) | 9yo G | 137lb | OR 55 | draw 11 | jockey Conor Cusack(7) | trainer P J F Murphy (14d 0/4) | headgear /bes | last run 7 days | form 289409 | MARKET 5.3% | 09:00 median 13.00 | Matchbook -
    comment: The risk is form figures of ninth last time out and a fourth three starts back, leaving him winless in his last six.
    DATA: model 8.1% | style Midfield (led 4% of runs) | runs in data 13 | last 3: 15 Oct Curragh (IRE) 7f Soft 4/20 fig 67; 29 Oct Punchestown (IRE) 7f Yielding 10/12 fig 46; 11 Nov Dundalk (AW) (IRE) 7f Standard 9/14 fig 49
    DATA for: Best recent form figure 67, 20 lb above field average; Recent figures 12 lb above its current mark (looks well handicapped); Official rating 55, 6 lb above field average
    DATA against: Carries 6 lb more than average
- Pick A Window (hrs_53743242) | 4yo G | 122lb | OR 38 | draw 10 | jockey  | trainer Seamus G O'Donnell (14d 0/0) | headgear - | last run 14 days | form 058005 | MARKET 3.3% | 09:00 median 21.00 | Matchbook 21.00
    comment: Pick A Window is hard to fancy, winless in his last six and unplaced in three of them, though a fifth last time out just 14 days ago and prior experience over today's trip and going offer some respite.
    DATA: model 1.4% | style Prominent (led 5% of runs) | runs in data 7 | last 3: 22 Jul Naas 8f Good 17/18; 9 Sep Cork 7f Good 22/22; 4 Nov Dundalk (AW) (IRE) 7f Standard 5/13 fig 37
    DATA for: Carries 9 lb less than average
    DATA against: Best recent form figure 37, 10 lb below field average; Official rating 38, 11 lb below field average
- Volendam (hrs_47744214) | 4yo F | 135lb | OR 53 | draw 12 | jockey Colin Keane | trainer E D Delany (14d 0/1) | headgear p (1st time) | last run 14 days | form 252090 | MARKET 2.5% | 09:00 median 29.00 | Matchbook 26.00
    comment: Volendam has twice finished second in her last six, but she's been unplaced last time out and a ninth two starts back, so the form has cooled.
    DATA: model 1.5% | style Prominent (led 8% of runs) | runs in data 15 | last 3: 3 Aug Naas 7f Good 16/16; 10 Sep Laytown 6f Standard 9/9; 4 Nov Dundalk (AW) (IRE) 7f Standard 13/13 fig 14
    DATA for: Has won at this trip or further; First-time headgear
    DATA against: Best recent form figure 14, 33 lb below field average; Recent figures 39 lb below its current mark (looks high in the weights); Last-run finishing speed -3.5% vs that field (faded); Poor recent finishing positions
- Manhattan Dandy (hrs_19510351) | 9yo G | 122lb | OR 40 | draw 6 | jockey Patrick McGettigan(5) | trainer Thomas Coyle (14d 0/4) | headgear - | last run 37 days | form 837400 | MARKET 2.2% | 09:00 median 34.00 | Matchbook 38.00
    comment: Manhattan Dandy has been unplaced in his last two starts and is yet to win in recent form, with a fourth three starts back his best finish since a third five runs ago, so he is hard to fancy.
    DATA: model 2.1% | style Prominent (led 3% of runs) | runs in data 9 | last 3: 18 Sep Dundalk 8f Standard 4/14; 30 Sep Bellewstown 7.9f Soft To Heavy 14/14; 12 Oct Roscommon 7.5f Soft 10/13
    DATA for: Carries 9 lb less than average
    DATA against: Official rating 40, 9 lb below field average
- Prince Andorra (hrs_62360865) | 3yo G | 133lb | OR 52 | draw 15 | jockey Robbie Colgan | trainer Ms Claire O'Connell (14d 0/1) | headgear tb | last run 34 days | form 600500 | MARKET 2.1% | 09:00 median 51.00 | Matchbook 24.00
    comment: Prince Andorra has been unplaced in four of his last six, with a fifth three starts back his best recent effort, though he has run over today's trip and going and returns after 34 days off. Winless in that spell, he carries 133 lb from draw 15 off an official mark of 52.
    DATA: model 3.1% | style Held up (led 3% of runs) | runs in data 8 | last 3: 25 Sep Dundalk 6f Standard 5/13; 9 Oct Dundalk 7f Standard 11/14; 15 Oct Curragh (IRE) 5f Soft 11/17 fig 47
- Steppinoncats (hrs_17390848188) | 3yo G | 127lb | OR 46 | draw 5 | jockey Luke McAteer | trainer Rory Anthony Devine (14d 1/1) | headgear - | last run 41 days | form 0070 | MARKET 2.1% | 09:00 median 38.00 | Matchbook 38.00
    comment: Steppinoncats is winless in his last four, unplaced last time out and a seventh two starts back, so he is hard to fancy after 41 days off.
    DATA: model 1.5% | style Midfield (led 5% of runs) | runs in data 4 | last 3: 5 Sep Navan 10f Good 10/21; 19 Sep Gowran Park 9.5f Yielding To Soft 7/10; 8 Oct Thurles 8.3f Yielding 13/13
    DATA against: Last-run finishing speed -9.1% vs that field (faded); Poor recent finishing positions
- Bucky Larson (hrs_13284908) | 11yo G | 130lb | OR 48 | draw 9 | jockey  | trainer P Sweeney (14d 0/4) | headgear - | last run 12 days | form 1-8490 | MARKET 2.1% | 09:00 median 34.00 | Matchbook 38.00
    DATA: model 3.1% | style Midfield (led 4% of runs) | runs in data 4 | last 3: 30 Jan Dundalk 7f Standard 4/12; 20 Mar Dundalk 7f Standard 9/14; 6 Nov Dundalk (AW) (IRE) 8f Standard 13/14 fig 33
    DATA against: Best recent form figure 33, 14 lb below field average; Recent figures 15 lb below its current mark (looks high in the weights); Aged 11, older than most of this field
- Tijuana (hrs_27861673) | 8yo G | 122lb | OR 40 | draw 3 | jockey Nicola Burns(5) | trainer David Edward Finn (14d 0/0) | headgear t | last run 58 days | form 007/00 | MARKET 2.1% | 09:00 median 51.00 | Matchbook 27.00
    comment: Tijuana is winless in his last five, unplaced in four of them and seventh three starts back, and returns after 58 days off, so he is hard to fancy.
    DATA: model 0.6% | style Held up (led 5% of runs) | runs in data 2 | last 3: 12 May Killarney 8.1f Good 12/13; 21 Sep Listowel 8f Yielding 12/14
    DATA for: Carries 9 lb less than average
    DATA against: Official rating 40, 9 lb below field average; Lightly raced: 2 runs in our data, so the model has little to go on

## 3:30 Dundalk (AW) | race_id rac_32304743068 | Irishinjuredjockeys.com Nursery Handicap
Flat |  | 7f | going Standard | AW | 12 runners | rating band 0-60 | age 2yo
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Rock On Johnny (hrs_66272227) | 2yo G | 144lb | OR 58 | draw 9 | jockey Camillus Byrne(10) | trainer Adrian McGuinness (14d 4/17) | headgear - | last run 5 days | form 8501 | MARKET 32.9% | 09:00 median 2.38 | Matchbook 2.68
    DATA: model 16.4% | style Prominent (led 4% of runs) | runs in data 4 | last 3: 12 Aug Gowran Park 7f Good To Firm 5/16; 1 Nov Curragh (IRE) 8f Yielding To Soft 15/23 fig 30; 13 Nov Dundalk (AW) (IRE) 8f Standard 1/6 fig 59
    DATA for: Best recent form figure 59, 8 lb above field average; Official rating 58, 6 lb above field average; Trainer 24% wins (4/17), last 14 days; Has won at this trip or further
    DATA against: Carries 12 lb more than average
- Mutamarid Lsk (hrs_65869573) | 2yo G | 135lb | OR 56 | draw 11 | jockey Jack Kearney | trainer Daniel James Murphy (14d 0/7) | headgear b | last run 14 days | form 80042 | MARKET 15.9% | 09:00 median 5.00 | Matchbook 5.60
    comment: The main risk is that he is yet to win in his last five starts and carries 135 lb from draw 11.
    DATA: model 22.8% | style Midfield (led 4% of runs) | runs in data 5 | last 3: 9 Aug Curragh 6f Good To Firm 18/19; 2 Oct Dundalk 7f Standard 4/9; 4 Nov Dundalk (AW) (IRE) 7f Standard 2/7 fig 55
    DATA for: Best recent form figure 55, 4 lb above field average
- Dear Theodosia (hrs_7000000518) | 2yo F | 127lb | OR 48 | draw 5 | jockey Nathan Crosse | trainer Daniel McLoughlin (14d 0/5) | headgear - | last run 7 days | form 009963 | MARKET 10.8% | 09:00 median 7.00 | Matchbook 8.40
    comment: Dear Theodosia bounced back with a third last time out and returns quickly, just seven days later, having run over today's trip and going before.
    DATA: model 15.0% | style Midfield (led 29% of runs) | runs in data 6 | last 3: 4 Sep Down Royal 7.1f Good 9/10; 19 Oct Gowran Park (IRE) 7f Yielding 6/12 fig 49; 11 Nov Dundalk (AW) (IRE) 6f Standard 3/8 fig 54
    DATA for: Recent figures 6 lb above its current mark (looks well handicapped)
- Zelente (hrs_17391303979) | 2yo F | 131lb | OR 52 | draw 4 | jockey Siobhan Rutledge | trainer Ross O'Sullivan (14d 1/12) | headgear - | last run 14 days | form 0003 | MARKET 9.0% | 09:00 median 8.50 | Matchbook 10.50
    comment: Zelente comes into this off a third last time out just 14 days ago, though she's yet to win in her last four starts and was unplaced in the three before that.
    DATA: model 6.5% | style Held up (led 4% of runs) | runs in data 4 | last 3: 17 Sep Naas 5.9f Yielding 13/21; 11 Oct Naas 5.9f Soft 11/13; 4 Nov Dundalk (AW) (IRE) 7f Standard 3/7 fig 50
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- How Now (hrs_17390579094) | 2yo G | 130lb | OR 51 | draw 1 | jockey James Ryan | trainer Conor David Maxwell (14d 0/0) | headgear - | last run 30 days | form 0604 | MARKET 5.8% | 09:00 median 11.00 | Matchbook 18.50
    comment: How Now was a fourth last time out but is winless in his last four, with a sixth three starts back his best other finish, and he returns after 30 days having run over today's trip.
    DATA: model 4.3% | style Held up (led 3% of runs) | runs in data 4 | last 3: 22 Sep Listowel 7.1f Yielding 6/6; 7 Oct Navan 5.8f Yielding 20/21; 19 Oct Gowran Park (IRE) 7f Yielding 4/12 fig 52
    DATA for: Last-run finishing speed +2.3% vs that field (finished strongly)
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Hazy Sky (hrs_17392273969) | 2yo F | 127lb | OR 48 | draw 10 | jockey Robbie Colgan | trainer K J Condon (14d 0/0) | headgear - | last run 28 days | form 707 | MARKET 5.3% | 09:00 median 15.00 | Matchbook 16.50
    comment: Hazy Sky is winless in her last three, finishing seventh last time out and seventh three starts back, though she has run over today's trip and returns after 28 days.
    DATA: model 6.4% | style Held up (led 4% of runs) | runs in data 3 | last 3: 17 Sep Naas 8f Yielding 7/10; 7 Oct Navan 5.8f Yielding 10/21; 21 Oct Navan (IRE) 6f Yielding 7/14 fig 49
    DATA against: Poor recent finishing positions; Pace: steady gallop likely, hard to come from off the pace
- Maxims Of Equity (hrs_17392264582) | 2yo F | 134lb | OR 55 | draw 8 | jockey Leigh Roche | trainer M. D. O'Callaghan (14d 1/6) | headgear t | last run 20 days | form 086 | MARKET 4.4% | 09:00 median 17.00 | Matchbook 23.00
    comment: Maxims Of Equity is hard to fancy, having finished sixth last time out, an eighth two starts back and unplaced three starts back, so she is winless in her last three.
    DATA: model 5.3% | style Held up (led 5% of runs) | runs in data 3 | last 3: 17 Sep Naas 5.9f Yielding 17/21; 15 Oct Curragh (IRE) 6f Soft 8/12 fig 31; 29 Oct Punchestown (IRE) 7f Yielding 6/11 fig 44
    DATA against: Best recent form figure 44, 7 lb below field average; Recent figures 11 lb below its current mark (looks high in the weights); Poor recent finishing positions; Pace: steady gallop likely, hard to come from off the pace
- Tina Tereshkova (hrs_65225111) | 2yo F | 119lb | OR 40 | draw 2 | jockey R. P. Cleary | trainer Andrew Kinirons (14d 1/1) | headgear b (1st time) | last run 30 days | form 096007 | MARKET 4.4% | 09:00 median 16.50 | Matchbook 24.00
    comment: Tina Tereshkova is hard to fancy, winless in her last six with a seventh last time out and nothing better than a sixth four starts back.
    DATA: model 4.2% | style Midfield (led 3% of runs) | runs in data 6 | last 3: 26 Jun Curragh 6f Good 12/12; 17 Sep Naas 8f Yielding 11/13; 19 Oct Gowran Park (IRE) 7f Yielding 7/12 fig 38
    DATA for: Carries 12 lb less than average; First-time headgear
    DATA against: Best recent form figure 38, 13 lb below field average; Official rating 40, 12 lb below field average; Poor recent finishing positions
- Sorrento Sunset (hrs_17391301893) | 2yo F | 134lb | OR 55 | draw 6 | jockey Conor Cusack(7) | trainer Daniel McLoughlin (14d 0/5) | headgear - | last run 50 days | form 069 | MARKET 4.0% | 09:00 median 17.00 | Matchbook 26.00
    comment: Sorrento Sunset is hard to fancy, beaten in a ninth last time out, a sixth two starts back and unplaced three starts back, and she returns after 50 days off.
    DATA: model 7.1% | style Held up (led 5% of runs) | runs in data 3 | last 3: 23 Aug Naas 5.9f Good 13/15; 4 Sep Down Royal 5f Good 6/11; 29 Sep Cork 5f Soft 9/12
    DATA against: Poor recent finishing positions; Pace: steady gallop likely, hard to come from off the pace
- Annie Tips (hrs_66494169) | 2yo F | 138lb | OR 59 | draw 3 | jockey Nicola Burns(5) | trainer James Dowling (14d 0/0) | headgear - | last run 14 days | form 88065 | MARKET 3.6% | 09:00 median 19.00 | Matchbook 30.00
    comment: Fit after just 14 days off, Annie Tips has run over today's trip and on this going, and a fifth last time out is her best finish in a winless recent run.
    DATA: model 8.4% | style Midfield (led 4% of runs) | runs in data 5 | last 3: 23 Aug Naas 5.9f Good 15/15; 28 Sep Down Royal 5f Good To Yielding 6/6; 4 Nov Dundalk (AW) (IRE) 7f Standard 5/7 fig 55
    DATA for: Best recent form figure 55, 4 lb above field average; Official rating 59, 7 lb above field average
    DATA against: Carries 6 lb more than average
- Scotty Cameron (hrs_7000000581) | 2yo G | 134lb | OR 55 | draw 7 | jockey Nestor Kashuba(10) | trainer Kevin Thomas Coleman (14d 0/2) | headgear - | last run 98 days | form 000 | MARKET 2.2% | 09:00 median 41.00 | Matchbook 40.00
    comment: He carries 134 lb from stall seven.
    DATA: model 2.5% | style Held up (led 5% of runs) | runs in data 3 | last 3: 16 Jul Leopardstown 6.5f Good 10/11; 2 Aug Galway 7f Good 10/10; 12 Aug Gowran Park 7f Good To Firm 15/16
    DATA against: Poor recent finishing positions; Returns from a 98-day break; Pace: steady gallop likely, hard to come from off the pace
- Chiquitita Bee (hrs_64812776) | 2yo F | 125lb | OR 46 | draw 12 | jockey Robert Whearty | trainer Adrian McGuinness (14d 4/17) | headgear t | last run 130 days | form 9000 | MARKET 1.7% | 09:00 median 51.00 | Matchbook 60.00
    comment: Chiquitita Bee is hard to fancy: she was unplaced in each of her last three outings, with a ninth four starts back, and returns after 130 days off.
    DATA: model 1.3% | style Held up (led 4% of runs) | runs in data 4 | last 3: 4 Jun Leopardstown 7.1f Soft To Heavy 10/10; 18 Jun Leopardstown 7.2f Good To Firm 10/10; 11 Jul Navan 5.8f Good 16/17
    DATA for: Trainer 24% wins (4/17), last 14 days; Carries 6 lb less than average
    DATA against: Official rating 46, 6 lb below field average; Poor recent finishing positions; Returns from a 130-day break; Pace: steady gallop likely, hard to come from off the pace

## 4:00 Dundalk (AW) | race_id rac_32304745005 | Now Racing Every Wednesday At Dundalk Maiden
Flat |  | 6f | going Standard | AW | 13 runners | rating band - | age 3yo+
DATA pace: Unclear - Running styles known for only 6 of 13 runners.
- Otsana (hrs_17389043798) | 3yo F | 129lb | OR 72 | draw 11 | jockey W. J. Lee | trainer P. Twomey (14d 1/3) | headgear t | last run 14 days | form 5332 | MARKET 32.8% | 09:00 median 2.50 | Matchbook 2.56
    DATA: model 20.9% | style Midfield (led 5% of runs) | runs in data 4 | last 3: 4 Sep Down Royal 5f Good 3/12; 16 Oct Dundalk (AW) (IRE) 6f Standard 3/9 fig 70; 4 Nov Dundalk (AW) (IRE) 7f Standard 2/8 fig 69
    DATA for: Best recent form figure 70, 21 lb above field average; Good recent finishing positions
- Stooked (hrs_17389044841) | 3yo F | 129lb | OR 73 | draw 9 | jockey Colin Keane | trainer G. M. Lyons (14d 0/5) | headgear - | last run 92 days | form 220 | MARKET 23.2% | 09:00 median 3.50 | Matchbook 3.85
    DATA: model 18.8% | style Prominent (led 4% of runs) | runs in data 3 | last 3: 18 Jul Curragh 7f Good To Firm 2/11; 24 Jul Cork 6f Good To Firm 2/13; 18 Aug Roscommon 7.5f Good To Yielding 11/15
    DATA for: Good recent finishing positions
    DATA against: Last-run finishing speed -4.3% vs that field (faded); Returns from a 92-day break
- Brise Fraiche (hrs_17391028627) | 3yo F | 129lb | OR - | draw 13 | jockey J M Sheridan | trainer Joseph Patrick O'Brien (14d 3/22) | headgear - | last run 92 days | form 6 | MARKET 11.7% | 09:00 median 6.50 | Matchbook 8.40
    DATA: model 5.6% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 18 Aug Roscommon 7.5f Good To Yielding 6/15
    DATA against: Returns from a 92-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Transatlantico (hrs_17394892942) | 3yo G | 134lb | OR - | draw 1 | jockey W. M. Lordan | trainer Miss Natalia Lupini (14d 1/3) | headgear - | last run - days | form - | MARKET 6.0% | 09:00 median 15.00 | Matchbook 14.00
    DATA: model 4.8% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- What's Enough (hrs_17393013456) | 4yo G | 134lb | OR 64 | draw 3 | jockey Luke McAteer | trainer Patrick T Foley (14d 1/6) | headgear h | last run 12 days | form 362 | MARKET 4.9% | 09:00 median 15.00 | Matchbook 23.00
    DATA: model 7.3% | style Prominent (led 8% of runs) | runs in data 3 | last 3: 30 Sep Bellewstown 5f Soft To Heavy 3/7; 7 Oct Navan 5.8f Yielding 6/13; 6 Nov Dundalk (AW) (IRE) 5f Standard 2/5 fig 61
    DATA for: Best recent form figure 61, 12 lb above field average; Good recent finishing positions
- Carry The Dream (hrs_66160710) | 3yo C | 134lb | OR 68 | draw 5 | jockey Seamie Heffernan | trainer W P Browne (14d 0/0) | headgear ht (1st time) | last run 14 days | form 89584 | MARKET 4.8% | 09:00 median 17.00 | Matchbook 18.50
    DATA: model 7.1% | style Leader (led 38% of runs) | runs in data 5 | last 3: 9 Sep Cork 8f Good 5/18; 2 Oct Dundalk 7f Standard 8/13; 4 Nov Dundalk (AW) (IRE) 7f Standard 4/8 fig 59
    DATA for: Best recent form figure 59, 10 lb above field average; First-time headgear
- Dusty Rock (hrs_52054646) | 3yo F | 129lb | OR 65 | draw 2 | jockey Declan McDonogh | trainer Joseph Patrick O'Brien (14d 3/22) | headgear t (1st time) | last run 33 days | form 6-265 | MARKET 4.3% | 09:00 median 17.00 | Matchbook 27.00
    DATA: model 7.2% | style Prominent (led 5% of runs) | runs in data 3 | last 3: 28 Jan Dundalk 5f Standard 2/13; 30 Sep Bellewstown 5f Soft To Heavy 6/7; 16 Oct Dundalk (AW) (IRE) 6f Standard 5/9 fig 55
    DATA for: Best recent form figure 55, 6 lb above field average; First-time headgear
- Silver Flash (hrs_53959997) | 3yo F | 129lb | OR - | draw 4 | jockey R. P. Cleary | trainer Thomas Cleary (14d 0/0) | headgear - | last run 516 days | form 2- | MARKET 3.7% | 09:00 median 15.00 | Matchbook 36.00
    DATA: model 4.8% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 516-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Subtle Shade (hrs_17394487215) | 3yo F | 129lb | OR - | draw 7 | jockey Chris Hayes | trainer Joseph Patrick O'Brien (14d 3/22) | headgear - | last run 7 days | form 85 | MARKET 3.4% | 09:00 median 15.00 | Matchbook 48.00
    DATA: model 9.0% | style Unknown | runs in data 2 | last 3: 30 Oct Dundalk (AW) (IRE) 8f Standard 8/14 fig 47; 11 Nov Dundalk (AW) (IRE) 8f Standard 5/13 fig 55
    DATA for: Best recent form figure 55, 6 lb above field average; Last-run finishing speed +3.9% vs that field (finished strongly)
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Pianello (hrs_17395283024) | 3yo F | 129lb | OR - | draw 6 | jockey Ben Coen | trainer A. Slattery (14d 0/14) | headgear - | last run - days | form - | MARKET 2.8% | 09:00 median 23.00 | Matchbook 44.00
    DATA: model 4.8% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Trainer 0 wins from 14 runs, last 14 days; Lightly raced: 0 runs in our data, so the model has little to go on
- Arizona Babe (hrs_17395078596) | 3yo F | 129lb | OR - | draw 12 | jockey Jessica O'Gorman(7) | trainer Daniel James Murphy (14d 0/7) | headgear - | last run 12 days | form 4 | MARKET 0.9% | 09:00 median 67.00 | Matchbook 170.00
    DATA: model 2.8% | style Unknown | runs in data 1 | last 3: 6 Nov Dundalk (AW) (IRE) 5f Standard 4/5 fig 40
    DATA against: Best recent form figure 40, 9 lb below field average; Lightly raced: 1 run in our data, so the model has little to go on
- Little Miss Rock (hrs_17394706245) | 4yo F | 129lb | OR - | draw 10 | jockey Robert Whearty | trainer William Durkan (14d 0/2) | headgear - | last run 19 days | form 0 | MARKET 0.7% | 09:00 median 81.00 | Matchbook 260.00
    DATA: model 2.3% | style Unknown | runs in data 1 | last 3: 30 Oct Dundalk (AW) (IRE) 8f Standard 12/14 fig 27
    DATA against: Best recent form figure 27, 22 lb below field average; Lightly raced: 1 run in our data, so the model has little to go on
- Queen Creek (hrs_17395284067) | 3yo F | 129lb | OR - | draw 8 | jockey Nathan Crosse | trainer Joseph Patrick O'Brien (14d 3/22) | headgear - | last run 7 days | form 0 | MARKET 0.7% | 09:00 median 101.00 | Matchbook 210.00
    DATA: model 4.6% | style Unknown | runs in data 1 | last 3: 11 Nov Dundalk (AW) (IRE) 8f Standard 12/13 fig 27
    DATA against: Best recent form figure 27, 22 lb below field average; Last-run finishing speed -2.6% vs that field (faded); Lightly raced: 1 run in our data, so the model has little to go on

## 4:30 Dundalk (AW) | race_id rac_32304746942 | Christmas Party Nights At Dundalk Stadium Handicap
Flat |  | 1m | going Standard | AW | 15 runners | rating band - | age 3yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Go Out (hrs_50282106) | 4yo G | 137lb | OR 67 | draw 8 | jockey Colin Keane | trainer Daniel James Murphy (14d 0/7) | headgear tb | last run 7 days | form 600213 | MARKET 21.6% | 09:00 median 3.25 | Matchbook 3.50 | CHECK (skip line 3.09)
    comment: Go Out was third last time out, and a winner two starts back, which gives him solid recent form, and he's back quickly after seven days and has run over today's trip and going.
    DATA: model 18.1% | style Held up (led 8% of runs) | runs in data 17 | last 3: 16 Oct Dundalk (AW) (IRE) 7f Standard 2/14 fig 67; 30 Oct Dundalk (AW) (IRE) 8f Standard 1/14 fig 69; 11 Nov Dundalk (AW) (IRE) 7f Standard 3/14 fig 68
    DATA for: Best recent form figure 69, 5 lb above field average; Has won at this trip or further; Good recent finishing positions
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Golddream (hrs_62779164) | 3yo G | 143lb | OR 75 | draw 12 | jockey  | trainer David Marnane (14d 2/5) | headgear - | last run 19 days | form 550564 | MARKET 20.2% | 09:00 median 3.50 | Matchbook 3.80
    comment: The risk is that he is winless in his last six, with 143 lb from stall 12 to carry.
    DATA: model 12.4% | style Midfield (led 4% of runs) | runs in data 9 | last 3: 21 Aug Killarney 8.1f Good 5/9; 9 Oct Dundalk 8f Standard 6/13; 30 Oct Dundalk (AW) (IRE) 8f Standard 4/14 fig 79
    DATA for: Best recent form figure 79, 15 lb above field average; Recent figures 4 lb above its current mark (looks well handicapped); Official rating 75, 12 lb above field average; Trainer 40% wins (2/5), last 14 days; Has won at this trip or further
    DATA against: Carries 10 lb more than average
- Phoenix Pairc (hrs_52962805) | 4yo F | 132lb | OR 62 | draw 11 | jockey W. J. Lee | trainer W. McCreery (14d 0/1) | headgear t | last run 26 days | form 707163 | MARKET 9.6% | 09:00 median 6.50 | Matchbook 9.00
    comment: Phoenix Pairc comes here fresh from a third last time out, 26 days ago, and has a winner three starts back, plus experience over today's trip and going. Her form is patchy, though, with a sixth and a seventh in the other recent runs, and 132 lb from draw 11 is a notable burden.
    DATA: model 7.6% | style Midfield (led 4% of runs) | runs in data 7 | last 3: 31 Aug Roscommon 7.4f Good To Yielding 1/14; 21 Sep Fairyhouse 7f Good 6/18; 23 Oct Dundalk (AW) (IRE) 7f Standard 3/14 fig 65
    DATA for: Good recent finishing positions
- Final Boss (hrs_56525371) | 3yo G | 131lb | OR 63 | draw 15 | jockey Robbie Colgan | trainer Matthew J Smith (14d 0/4) | headgear b | last run 14 days | form 607052 | MARKET 8.6% | 09:00 median 7.00 | Matchbook 11.00
    comment: Fresh from a second last time out just 14 days ago, he has run over today's trip and going, but he's winless in his last six and was only fifth two starts back.
    DATA: model 6.8% | style Held up (led 5% of runs) | runs in data 7 | last 3: 15 Oct Curragh (IRE) 7f Soft 10/20 fig 59; 28 Oct Dundalk (AW) (IRE) 7f Standard 5/13 fig 59; 4 Nov Dundalk (AW) (IRE) 7f Standard 2/13 fig 66
    DATA for: Last-run finishing speed +2.2% vs that field (finished strongly)
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Altimara (hrs_36207325) | 5yo M | 132lb | OR 62 | draw 9 | jockey Donagh O'Connor | trainer Ross O'Sullivan (14d 1/12) | headgear h | last run 31 days | form 096590 | MARKET 5.2% | 09:00 median 12.00 | Matchbook 16.00
    comment: Altimara is winless in her last six, with a ninth two starts back and a fifth three starts back the best of a modest run, though she has run over today's trip and going before and returns after 31 days.
    DATA: model 5.1% | style Midfield (led 4% of runs) | runs in data 6 | last 3: 3 Aug Naas 7f Good 5/16; 20 Aug Leopardstown 7f Good To Yielding 9/14; 18 Oct Leopardstown (IRE) 7f Good 13/14 fig 45
    DATA against: Best recent form figure 45, 19 lb below field average; Recent figures 17 lb below its current mark (looks high in the weights)
- Usuario Amigo (hrs_40805534) | 5yo G | 134lb | OR 64 | draw 7 | jockey Jack Kearney | trainer Richard John O'Brien (14d 0/2) | headgear - | last run 7 days | form 703617 | MARKET 5.2% | 09:00 median 12.00 | Matchbook 17.00
    comment: Usuario Amigo was seventh last time out, and he won two starts back, so he has ability, but he's been inconsistent and returns quickly after seven days.
    DATA: model 11.2% | style Held up (led 5% of runs) | runs in data 13 | last 3: 18 Sep Dundalk 8f Standard 6/14; 25 Sep Dundalk 8f Standard 1/14; 11 Nov Dundalk (AW) (IRE) 7f Standard 7/14 fig 57
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 57, 7 lb below field average; Recent figures 7 lb below its current mark (looks high in the weights); Pace: steady gallop likely, hard to come from off the pace
- Shamacid (hrs_41189764) | 4yo G | 132lb | OR 62 | draw 16 | jockey Siobhan Rutledge | trainer John McConnell (14d 0/10) | headgear - | last run 84 days | form 205841 | MARKET 5.2% | 09:00 median 11.00 | Matchbook 19.50
    comment: Shamacid won last time out and has run over today's trip and going, but that came 84 days ago, and a fourth two starts back and an eighth three starts back show his inconsistency.
    DATA: model 4.6% | style Unknown | runs in data 9 | last 3: 23 Jul Southwell 7.1f Standard 8/13; 15 Aug Lingfield 8f Standard 4/6; 26 Aug Wolverhampton 8.6f Standard 1/12
    DATA for: Has won at this trip or further
    DATA against: Trainer 0 wins from 10 runs, last 14 days
- Tourin (hrs_65869482) | 3yo F | 131lb | OR 63 | draw 6 | jockey Seamie Heffernan | trainer J A Stack (14d 1/2) | headgear - | last run 52 days | form 368 | MARKET 4.7% | 09:00 median 12.00 | Matchbook 22.00
    comment: Tourin is hard to fancy, having slipped from a third three starts back to a sixth, then an eighth last time out, and she returns after 52 days off.
    DATA: model 6.0% | style Held up (led 4% of runs) | runs in data 3 | last 3: 19 Jun Limerick 7f Soft 3/16; 1 Sep Gowran Park 7f Yielding 6/14; 27 Sep Curragh 6f Heavy 8/11
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Moyassr (hrs_36738751) | 5yo G | 139lb | OR 69 | draw 10 | jockey Adam Caffrey | trainer Adrian McGuinness (14d 4/17) | headgear t | last run 7 days | form 222608 | MARKET 4.7% | 09:00 median 15.00 | Matchbook 17.50
    comment: Moyassr arrives quick back after seven days, having finished second in three runs earlier in this sequence, and he has run over today's trip and going before.
    DATA: model 7.6% | style Midfield (led 5% of runs) | runs in data 18 | last 3: 30 Sep Bellewstown 7.9f Soft To Heavy 6/14; 28 Oct Dundalk (AW) (IRE) 8f Standard 10/12 fig 62; 11 Nov Dundalk (AW) (IRE) 7f Standard 8/14 fig 64
    DATA for: Official rating 69, 6 lb above field average; Trainer 24% wins (4/17), last 14 days; Has won at this trip or further
    DATA against: Poor recent finishing positions; Carries 6 lb more than average
- Real Force (hrs_18323571) | 9yo G | 140lb | OR 70 | draw 2 | jockey Danny O'Leary(10) | trainer G. O'Leary (14d 1/6) | headgear - | last run 17 days | form -40060 | MARKET 3.4% | 09:00 median 21.00 | Matchbook 24.00
    comment: Only a fourth five starts back stands out in the form, so that is the reservation.
    DATA: model 5.7% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 4 Oct Curragh 6f Soft 13/22; 20 Oct Curragh (IRE) 6f Yielding 6/17 fig 76; 1 Nov Curragh (IRE) 7f Yielding To Soft 10/25 fig 72
    DATA for: Best recent form figure 76, 12 lb above field average; Recent figures 6 lb above its current mark (looks well handicapped); Official rating 70, 7 lb above field average
    DATA against: Poor recent finishing positions; Carries 7 lb more than average; Aged 9, older than most of this field
- Zheleznaya Dama (hrs_53602269) | 3yo F | 129lb | OR 61 | draw 3 | jockey R. P. Cleary | trainer Brendan W Duke (14d 0/0) | headgear - | last run 51 days | form P52100 | MARKET 3.2% | 09:00 median 23.00 | Matchbook 25.00
    comment: Zheleznaya Dama is hard to fancy after two unplaced runs since a win three starts back, and she returns from 51 days off carrying 129 lb from stall three.
    DATA: model 4.4% | style Prominent (led 5% of runs) | runs in data 6 | last 3: 3 Aug Naas 7f Good 1/16; 20 Aug Leopardstown 7f Good To Yielding 12/14; 28 Sep Down Royal 7.1f Good To Yielding 11/14
    DATA against: Last-run finishing speed -2.9% vs that field (faded)
- Karakula (hrs_50755446) | 4yo F | 130lb | OR 60 | draw 1 | jockey Chris Hayes | trainer Miss Hilary McLoughlin (14d 0/1) | headgear - | last run 29 days | form 4-2260 | MARKET 2.6% | 09:00 median 17.00 | Matchbook 50.00
    comment: Karakula is hard to fancy, unplaced last time out and a sixth two starts back, though she was second three and four starts back and has run over today's trip and going before.
    DATA: model 3.6% | style Prominent (led 29% of runs) | runs in data 4 | last 3: 18 May Wolverhampton 9.5f Standard 2/8; 10 Jun Kempton 11f Standard To Slow 6/14; 20 Oct Curragh (IRE) 8f Yielding 17/23 fig 48
    DATA against: Best recent form figure 48, 16 lb below field average; Recent figures 12 lb below its current mark (looks high in the weights)
- Cash Me (hrs_47282312) | 4yo F | 132lb | OR 62 | draw 14 | jockey Ben Coen | trainer A Oliver (14d 0/0) | headgear - | last run 17 days | form 969-30 | MARKET 2.2% | 09:00 median 34.00 | Matchbook 36.00
    comment: Cash Me is winless in her last five, unplaced last time out and beaten in all four before that, so she is hard to fancy; a third two starts back and a run over today's trip and going on 17 days' rest are the positives.
    DATA: model 4.3% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 29 Oct Punchestown (IRE) 8f Yielding 3/14 fig 67; 1 Nov Curragh (IRE) 7f Yielding To Soft 22/25 fig 31
    DATA for: Recent figures 5 lb above its current mark (looks well handicapped)
    DATA against: Last-run finishing speed -4.4% vs that field (faded); Lightly raced: 2 runs in our data, so the model has little to go on
- Victors Spirit (hrs_55916196) | 5yo G | 138lb | OR 68 | draw 5 | jockey Killian Leonard | trainer Tom McGuinness (14d 0/1) | headgear h | last run 30 days | form 125730 | MARKET 1.9% | 09:00 median 41.00 | Matchbook 42.00
    comment: The main risk is an unplaced run last time out, with just the one win in his last six starts.
    DATA: model 2.2% | style Prominent (led 4% of runs) | runs in data 10 | last 3: 1 Jun Newbury 10f Good To Firm 7/7; 5 Jul Southwell 11.1f Standard 3/8; 19 Oct Gowran Park (IRE) 12f Soft 13/14
    DATA for: Has won at this trip or further
- Hydream (hrs_64523221) | 3yo F | 119lb | OR 43 | draw 4 | jockey  | trainer Miss Evanna McCutcheon (14d 0/1) | headgear - | last run 166 days | form 080 | MARKET 1.6% | 09:00 median 51.00 | Matchbook 55.00
    comment: Hydream is hard to fancy, unplaced last time out and an eighth two starts back, and she returns after 166 days off.
    DATA: model 0.4% | style Held up (led 4% of runs) | runs in data 3 | last 3: 9 May Naas 8f Good 11/13; 19 May Cork 7f Soft To Heavy 8/12; 5 Jun Fairyhouse 9.9f Good 11/13
    DATA for: Carries 14 lb less than average
    DATA against: Official rating 43, 20 lb below field average; Poor recent finishing positions; Returns from a 166-day break; Pace: steady gallop likely, hard to come from off the pace

## 5:07 Dundalk (AW) | race_id rac_32304748879 | Safer Gambling Week 2026 Fillies Maiden
Flat |  | 1m4f | going Standard | AW | 9 runners | rating band - | age 3yo+
DATA pace: Lone leader - Blue Nasturtium is the only habitual front-runner and may be allowed an easy lead.
- Rhapsodic (hrs_58627324) | 3yo F | 129lb | OR - | draw 9 | jockey Colin Keane | trainer D K Weld (14d 0/3) | headgear - | last run 31 days | form 6 | MARKET 46.4% | 09:00 median 1.80 | Matchbook 1.96
    DATA: model 13.7% | style Unknown | runs in data 1 | last 3: 18 Oct Leopardstown (IRE) 9f Good 6/15 fig 56
    DATA for: Best recent form figure 56, 12 lb above field average
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Serendipia (hrs_63422562) | 3yo F | 129lb | OR 72 | draw 2 | jockey W. J. Lee | trainer W. McCreery (14d 0/1) | headgear tv | last run 30 days | form 433576 | MARKET 18.2% | 09:00 median 5.00 | Matchbook 4.60
    DATA: model 22.6% | style Midfield (led 3% of runs) | runs in data 8 | last 3: 2 Sep Navan 10f Good 5/21; 26 Sep Curragh 9f Yielding 7/17; 19 Oct Gowran Park (IRE) 9.5f Soft 6/9 fig 52
    DATA for: Best recent form figure 52, 8 lb above field average; Official rating 72, 11 lb above field average
- Blue Nasturtium (hrs_66494008) | 4yo F | 134lb | OR 70 | draw 3 | jockey Patrick McGettigan(5) | trainer K J Condon (14d 0/0) | headgear - | last run 44 days | form 4533 | MARKET 12.2% | 09:00 median 6.00 | Matchbook 8.60
    DATA: model 23.5% | style Leader (led 23% of runs) | runs in data 4 | last 3: 13 Aug Tramore 16f Good 5/9; 16 Sep Clonmel 9.8f Yielding 3/7; 5 Oct Killarney 11.2f Soft 3/7
    DATA for: Official rating 70, 9 lb above field average; Good recent finishing positions; Pace: may get an uncontested lead
- Essential Comedy (hrs_65745680) | 3yo F | 129lb | OR 63 | draw 5 | jockey R. P. Cleary | trainer Ms Claire O'Connell (14d 0/1) | headgear - | last run 21 days | form 653057 | MARKET 8.2% | 09:00 median 9.00 | Matchbook 12.50
    DATA: model 6.4% | style Prominent (led 5% of runs) | runs in data 6 | last 3: 27 Aug Navan 14f Good 12/18; 16 Sep Clonmel 9.8f Yielding 5/8; 28 Oct Dundalk (AW) (IRE) 12f Standard 7/13 fig 62
    DATA for: Best recent form figure 62, 18 lb above field average
- Kigalienne (hrs_17391396806) | 3yo F | 129lb | OR - | draw 4 | jockey Chris Hayes | trainer Mrs J. Harrington (14d 1/9) | headgear p (1st time) | last run 71 days | form 0 | MARKET 7.0% | 09:00 median 10.00 | Matchbook 15.50
    DATA: model 2.5% | style Held up (led 8% of runs) | runs in data 1 | last 3: 8 Sep Galway 12f Soft 17/17
    DATA for: First-time headgear
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Kimy (hrs_37789969) | 6yo M | 134lb | OR 68 | draw 1 | jockey Seamie Heffernan | trainer Thomas Mullins (14d 0/7) | headgear p | last run 6 days | form 729605 | MARKET 6.4% | 09:00 median 11.00 | Matchbook 18.00
    DATA: model 25.9% | style Midfield (led 3% of runs) | runs in data 15 | last 3: 8 Oct Tramore 20.4f Yielding 2/12; 19 Oct Gowran Park (IRE) 12f Soft 5/14 fig 66; 12 Nov Thurles (IRE) 18f Good 3/10 fig 93
    DATA for: Best recent form figure 66, 22 lb above field average; Official rating 68, 7 lb above field average; Good recent finishing positions
    DATA against: Aged 6, older than most of this field
- Sierra's Dream (hrs_17390243248) | 4yo F | 134lb | OR - | draw 6 | jockey James Ryan | trainer T G McCourt (14d 0/1) | headgear - | last run 26 days | form 0 | MARKET 0.6% | 09:00 median 151.00 | Matchbook 220.00
    DATA: model 2.8% | style Midfield (led 5% of runs) | runs in data 3 | last 3: 8 Aug Wexford 16f Good 4/7; 19 Sep Navan 15.8f Good 8/13; 23 Oct Dundalk (AW) (IRE) 10.5f Standard 14/14 fig 31
    DATA against: Best recent form figure 31, 13 lb below field average
- Churchill Gale (hrs_41876793) | 4yo F | 134lb | OR 34 | draw 8 | jockey Sadhbh Tormey(7) | trainer T G McCourt (14d 0/1) | headgear - | last run 21 days | form 68-000 | MARKET 0.6% | 09:00 median 151.00 | Matchbook 230.00
    DATA: model 0.9% | style Held up (led 8% of runs) | runs in data 3 | last 3: 5 Sep Navan 10f Good 19/21; 15 Sep Punchestown 9.1f Good 14/14; 28 Oct Dundalk (AW) (IRE) 7f Standard 11/13 fig 28
    DATA against: Best recent form figure 28, 16 lb below field average; Official rating 34, 27 lb below field average; Poor recent finishing positions
- Dyker Heights (hrs_57503908) | 3yo F | 129lb | OR - | draw 7 | jockey Robbie Colgan | trainer Matthew J Smith (14d 0/4) | headgear - | last run 7 days | form 00-00 | MARKET 0.4% | 09:00 median 201.00 | Matchbook 490.00
    DATA: model 1.8% | style Midfield (led 8% of runs) | runs in data 2 | last 3: 1 Nov Curragh (IRE) 12f Yielding 16/19; 11 Nov Dundalk (AW) (IRE) 8f Standard 13/13 fig 13
    DATA against: Best recent form figure 13, 31 lb below field average; Lightly raced: 2 runs in our data, so the model has little to go on

## 5:40 Dundalk (AW) | race_id rac_32304750816 | Book Online At DundalkStadium.com Handicap
Flat |  | 1m2f150y | going Standard | AW | 17 runners | rating band 0-60 | age 3yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Prada's World (hrs_45007403) | 4yo F | 133lb | OR 51 | draw 5 | jockey Shane B Kelly | trainer Noel C. Kelly (14d 2/8) | headgear p | last run 19 days | form /0-042 | MARKET 17.1% | 09:00 median 4.00 | Matchbook 4.60 | CHECK (skip line 3.80)
    comment: Prada's World comes here on a high after finishing second last time out, and a fourth two starts back, 19 days ago, and she has run on today's going before.
    DATA: model 11.1% | style Midfield (led 5% of runs) | runs in data 3 | last 3: 23 Aug Naas 5f Good 15/19; 8 Oct Thurles 8.3f Yielding 4/14; 30 Oct Dundalk (AW) (IRE) 8f Standard 2/14 fig 55
    DATA for: Best recent form figure 55, 11 lb above field average; Recent figures 4 lb above its current mark (looks well handicapped); Trainer 25% wins (2/8), last 14 days
- Robot Rock (hrs_53269181) | 4yo G | 138lb | OR 56 | draw 3 | jockey Robbie Colgan | trainer A. J. Martin (14d 0/10) | headgear t | last run 14 days | form 008062 | MARKET 11.7% | 09:00 median 5.50 | Matchbook 7.60
    comment: Runner-up last time out just 14 days ago, Robot Rock has since had a quiet spell of form, with a sixth two starts back and nothing better than that before, and he is yet to win in his last six.
    DATA: model 7.8% | style Held up (led 5% of runs) | runs in data 6 | last 3: 3 Jul Bellewstown 12.2f Good 16/16; 11 Jul Navan 10.2f Good 6/12; 4 Nov Dundalk (AW) (IRE) 10.5f Standard 2/14 fig 55
    DATA for: Best recent form figure 55, 11 lb above field average; Official rating 56, 6 lb above field average
    DATA against: Trainer 0 wins from 10 runs, last 14 days; Carries 7 lb more than average; Pace: steady gallop likely, hard to come from off the pace
- One Cool County (hrs_7000000224) | 3yo G | 126lb | OR 48 | draw 17 | jockey Chris Hayes | trainer P J F Murphy (14d 0/4) | headgear p (1st time) | last run 14 days | form 690043 | MARKET 11.1% | 09:00 median 6.50 | Matchbook 6.80
    comment: One Cool County is yet to win in his last six starts, though a third last time out and a fourth two starts back show some improvement, and he has run over today's trip and going.
    DATA: model 6.3% | style Midfield (led 4% of runs) | runs in data 6 | last 3: 15 Sep Punchestown 9.1f Good 10/14; 5 Oct Killarney 8.1f Soft 4/15; 4 Nov Dundalk (AW) (IRE) 10.5f Standard 3/14 fig 47
    DATA for: Carries 5 lb less than average; First-time headgear
- Medieval Night (hrs_43418130) | 4yo G | 136lb | OR 54 | draw 13 | jockey J M Sheridan | trainer Denis Gerard Hogan (14d 1/12) | headgear tb | last run 19 days | form 253636 | MARKET 9.5% | 09:00 median 7.00 | Matchbook 8.40
    comment: Medieval Night has hit the frame three times in his last six, a third two starts back, a third four starts back and a second six starts back, and has run over today's trip and going before.
    DATA: model 9.2% | style Prominent (led 4% of runs) | runs in data 15 | last 3: 8 Oct Thurles 8.3f Yielding 6/13; 19 Oct Gowran Park (IRE) 8.5f Soft 3/16 fig 65; 30 Oct Dundalk (AW) (IRE) 8f Standard 6/14 fig 52
    DATA for: Best recent form figure 65, 21 lb above field average; Recent figures 11 lb above its current mark (looks well handicapped)
- Wegotogether (hrs_51800651) | 4yo F | 141lb | OR 59 | draw 2 | jockey  | trainer Gavin Cromwell (14d 4/34) | headgear tp | last run 12 days | form 814046 | MARKET 9.0% | 09:00 median 9.00 | Matchbook 8.20
    comment: The risk is a sixth last time out, with no win since five starts back, and she carries 141 lb from stall two.
    DATA: model 16.4% | style Midfield (led 4% of runs) | runs in data 6 | last 3: 21 Sep Listowel 8f Yielding 10/15; 30 Sep Bellewstown 7.9f Soft To Heavy 4/14; 6 Nov Dundalk (AW) (IRE) 8f Standard 6/14 fig 55
    DATA for: Best recent form figure 55, 11 lb above field average; Official rating 59, 9 lb above field average
    DATA against: Carries 10 lb more than average
- Syosset (hrs_44450707) | 5yo G | 137lb | OR 55 | draw 14 | jockey Donagh O'Connor | trainer John McConnell (14d 0/10) | headgear - | last run 61 days | form 013-70 | MARKET 6.1% | 09:00 median 11.00 | Matchbook 14.00
    comment: Syosset won four starts back and was a third three starts back, but he's been unplaced last time out and a seventh two runs ago, and returns after 61 days off.
    DATA: model 8.3% | style Prominent (led 3% of runs) | runs in data 7 | last 3: 8 Aug Kilbeggan 16f Good 3/13; 8 Sep Bangor-on-Dee 16.7f Good 4/6; 18 Sep Dundalk 10.7f Standard 11/14
    DATA against: Trainer 0 wins from 10 runs, last 14 days; Carries 6 lb more than average
- Tempted Angel (hrs_61078780) | 3yo F | 128lb | OR 50 | draw 4 | jockey Ben Coen | trainer Mark Fahey (14d 0/8) | headgear h (1st time) | last run 20 days | form 506804 | MARKET 6.0% | 09:00 median 9.50 | Matchbook 17.00
    comment: She has run over today's trip and going, and 20 days since her last outing is no concern.
    DATA: model 2.9% | style Midfield (led 4% of runs) | runs in data 6 | last 3: 13 Mar Dundalk 8f Standard 8/8; 1 Sep Gowran Park 8f Yielding 15/16; 29 Oct Punchestown (IRE) 7f Yielding 4/12 fig 52
    DATA for: Best recent form figure 52, 8 lb above field average; First-time headgear
    DATA against: Trainer 0 wins from 8 runs, last 14 days
- Sweetie Too (hrs_65254700) | 3yo F | 130lb | OR 52 | draw 15 | jockey R. P. Cleary | trainer Brendan W Duke (14d 0/0) | headgear - | last run 51 days | form 084507 | MARKET 4.6% | 09:00 median 13.00 | Matchbook 20.00
    comment: Sweetie Too has been beaten in all six recent runs, a fourth four starts back and a fifth three starts back her best finishes, and she returns after 51 days off.
    DATA: model 7.9% | style Held up (led 3% of runs) | runs in data 6 | last 3: 8 Sep Galway 8.4f Soft 5/14; 16 Sep Clonmel 9.8f Yielding 10/14; 28 Sep Down Royal 11f Good To Yielding 7/14
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Will Be King (hrs_14823018) | 10yo G | 129lb | OR 47 | draw 10 | jockey W. J. Lee | trainer John McConnell (14d 0/10) | headgear t | last run 33 days | form /20500 | MARKET 4.1% | 09:00 median 17.00 | Matchbook 19.00
    comment: Winless in his last five and unplaced in three of those, including last time out 33 days ago, Will Be King is hard to fancy, though he has run over today's trip and going and was second five starts back.
    DATA: model 2.4% | style Prominent (led 4% of runs) | runs in data 5 | last 3: 6 Jul Wolverhampton 8.6f Standard 5/13; 25 Jul Gowran Park 7f Good 10/14; 16 Oct Dundalk (AW) (IRE) 7f Standard 14/14 fig 31
    DATA against: Best recent form figure 31, 13 lb below field average; Recent figures 16 lb below its current mark (looks high in the weights); Trainer 0 wins from 10 runs, last 14 days; Aged 10, older than most of this field
- Spanish Princess (hrs_54842753) | 5yo M | 134lb | OR 52 | draw 1 | jockey Siobhan Rutledge | trainer John McConnell (14d 0/10) | headgear - | last run 30 days | form 80-600 | MARKET 4.0% | 09:00 median 17.00 | Matchbook 20.00
    comment: Spanish Princess has been well beaten in her last five starts, but a 30-day break and a run from stall one give her a fresh start, and she has run over today's trip and going before.
    DATA: model 7.2% | style Held up (led 4% of runs) | runs in data 3 | last 3: 19 Sep Gowran Park 8f Yielding To Soft 6/16; 7 Oct Navan 10.1f Yielding 10/16; 19 Oct Gowran Park (IRE) 8.5f Soft 11/16 fig 49
    DATA for: Best recent form figure 49, 5 lb above field average
    DATA against: Trainer 0 wins from 10 runs, last 14 days; Poor recent finishing positions; Pace: steady gallop likely, hard to come from off the pace
- Captain Ciano (hrs_42451906) | 4yo G | 129lb | OR 47 | draw 12 | jockey James Ryan | trainer T G McCourt (14d 0/1) | headgear ht | last run 19 days | form 800058 | MARKET 3.3% | 09:00 median 21.00 | Matchbook 24.00
    comment: Captain Ciano is winless in his last six, finishing eighth last time out and unplaced in three of the four runs before that, so he is hard to fancy. He has run over today's trip and going, and 19 days since his last outing is fine, but 129 lb from stall 12 is a big ask.
    DATA: model 4.6% | style Held up (led 4% of runs) | runs in data 11 | last 3: 7 Oct Navan 10.1f Yielding 12/16; 19 Oct Gowran Park (IRE) 8.5f Soft 5/16 fig 46; 30 Oct Dundalk (AW) (IRE) 8f Standard 8/14 fig 44
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Think About It (hrs_44075913) | 4yo F | 126lb | OR 44 | draw 7 | jockey  | trainer Thomas Patrick McGettigan (14d 0/1) | headgear - | last run 20 days | form 057090 | MARKET 2.5% | 09:00 median 29.00 | Matchbook 36.00
    comment: Think About It has run over today's trip and going before, but she's yet to win and has been unplaced in two of her last three outings, including last time out 20 days ago.
    DATA: model 1.5% | style Midfield (led 3% of runs) | runs in data 7 | last 3: 5 Aug Sligo 13.3f Yielding 13/14; 27 Aug Navan 8.1f Good 9/12; 29 Oct Punchestown (IRE) 7f Yielding 11/12 fig 27
    DATA for: Carries 5 lb less than average
    DATA against: Best recent form figure 27, 17 lb below field average; Recent figures 17 lb below its current mark (looks high in the weights); Official rating 44, 6 lb below field average; Poor recent finishing positions
- Local Lad (hrs_41596842) | 4yo G | 142lb | OR 60 | draw 9 | jockey Danny O'Leary(10) | trainer G. O'Leary (14d 1/6) | headgear b | last run 29 days | form 3-0000 | MARKET 2.4% | 09:00 median 34.00 | Matchbook 34.00
    comment: Local Lad has run over today's trip and on this going, and his third five starts back is the best of his recent form, but he's been unplaced in the four since.
    DATA: model 5.1% | style Held up (led 5% of runs) | runs in data 4 | last 3: 21 Sep Listowel 8f Yielding 14/15; 4 Oct Curragh 8f Soft 12/16; 20 Oct Curragh (IRE) 10f Yielding 23/24
    DATA for: Official rating 60, 10 lb above field average
    DATA against: Poor recent finishing positions; Carries 11 lb more than average; Pace: steady gallop likely, hard to come from off the pace
- Kings Gesture (hrs_53148571) | 5yo G | 127lb | OR 45 | draw 16 | jockey Jack Cleary(5) | trainer Michael Paul Ryan (14d 0/1) | headgear tb (1st time) | last run 30 days | form 800000 | MARKET 2.2% | 09:00 median 34.00 | Matchbook 40.00
    comment: Kings Gesture is winless in his last six, unplaced in each of his last five and eighth six starts back, though he has run over today's trip and going before and returns after 30 days.
    DATA: model 1.2% | style Midfield (led 4% of runs) | runs in data 6 | last 3: 20 Jul Ballinrobe 12.8f Good To Yielding 10/11; 15 Aug Tramore 16f Good To Yielding 12/12; 19 Oct Gowran Park (IRE) 8.5f Soft 15/16 fig 12
    DATA for: First-time headgear
    DATA against: Best recent form figure 12, 32 lb below field average; Recent figures 33 lb below its current mark (looks high in the weights); Official rating 45, 5 lb below field average; Last-run finishing speed -6.7% vs that field (faded); Poor recent finishing positions
- Legato (hrs_17391875543) | 3yo G | 127lb | OR 49 | draw 8 | jockey Adam Caffrey | trainer Michael Mulvany (14d 0/6) | headgear - | last run 39 days | form 009 | MARKET 2.2% | 09:00 median 34.00 | Matchbook 40.00
    comment: Legato is hard to fancy, winless in his last three and coming off a ninth last time out after 39 days off, with two unplaced runs before that.
    DATA: model 1.6% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 5 Sep Navan 10f Good 11/21; 21 Sep Listowel 8f Yielding 11/14; 10 Oct Naas 8f Soft 9/13
    DATA against: Poor recent finishing positions
- Onyeisi (hrs_53211620) | 3yo G | 119lb | OR 40 | draw 11 | jockey Nathan Crosse | trainer Karl Thornton (14d 0/2) | headgear b | last run 14 days | form 070090 | MARKET 2.2% | 09:00 median 34.00 | Matchbook 40.00
    comment: Winless in his last six, with a ninth two starts back and a seventh five starts back his best finishes, Onyeisi at least returns quickly after 14 days and has run over today's trip and going.
    DATA: model 1.8% | style Held up (led 4% of runs) | runs in data 13 | last 3: 2 Sep Navan 8.1f Good 12/16; 18 Sep Dundalk 10.7f Standard 9/14; 4 Nov Dundalk (AW) (IRE) 10.5f Standard 13/14 fig 30
    DATA for: Carries 12 lb less than average
    DATA against: Best recent form figure 30, 14 lb below field average; Recent figures 10 lb below its current mark (looks high in the weights); Official rating 40, 10 lb below field average; Last-run finishing speed -2.4% vs that field (faded); Poor recent finishing positions; Pace: steady gallop likely, hard to come from off the pace
- Miss Glenville (hrs_46013632) | 6yo M | 129lb | OR 47 | draw 6 | jockey  | trainer Paul Power (14d 0/0) | headgear t | last run 14 days | form /9-597 | MARKET 2.2% | 09:00 median 34.00 | Matchbook 40.00
    comment: Miss Glenville has run over today's trip and going and is fit enough after 14 days, but she is winless in her last four, with a seventh last time out and a ninth two starts back.
    DATA: model 5.0% | style Prominent (led 5% of runs) | runs in data 3 | last 3: 16 Sep Clonmel 9.8f Yielding 5/14; 8 Oct Thurles 8.3f Yielding 9/14; 4 Nov Dundalk (AW) (IRE) 10.5f Standard 7/14 fig 44
