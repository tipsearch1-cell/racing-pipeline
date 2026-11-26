# Card review packet: Chelmsford (AW), 2026-11-26

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
{"meeting": "chelmsford_aw", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 4:30 Chelmsford (AW) | race_id rac_32305630214 | Midnite A Next Generation Betting App Handicap Stakes
Flat | Class 6 | 1m5f66y | going Standard | AW | 14 runners | rating band 0-55 | age 3yo+
DATA pace: Lone leader - Cavalry Call is the only habitual front-runner and may be allowed an easy lead.
- Masego (hrs_43228136) | 4yo G | 133lb | OR 53 | draw 6 | jockey Billy Loughnane | trainer Tony Carroll (14d 2/36) | headgear - | last run 19 days | form 132322 | MARKET 27.4% | 09:00 median 3.00 | Matchbook 3.15 | CHECK (skip line 2.85)
    comment: Masego arrives in cracking nick, second last time out and second again two starts back, but he has only one win in his last six starts and that came six starts back.
    DATA: model 23.1% | style Prominent (led 23% of runs) | runs in data 10 | last 3: 23 Sep Listowel Hurdle 18.6f Good 7/18; 24 Oct Southwell (AW) Flat 12f Standard 2/14 fig 55; 7 Nov Southwell (AW) Flat 12f Standard 2/10 fig 54
    DATA for: Best recent form figure 55, 11 lb above field average; Good recent finishing positions
- Stitching Wheel (hrs_45126039) | 4yo F | 133lb | OR 53 | draw 13 | jockey Luke Morris | trainer James Owen (14d 4/46) | headgear t | last run 40 days | form 612565 | MARKET 15.9% | 09:00 median 5.00 | Matchbook 5.70
    comment: Stitching Wheel arrives having finished fifth last time out and a sixth two starts back, though she won five starts back and was second four starts back.
    DATA: model 7.0% | style Prominent (led 23% of runs) | runs in data 9 | last 3: 8 Aug Newmarket Flat 14f Good To Firm 5/6; 6 Oct Southwell Flat 14.1f Standard 6/11; 17 Oct Catterick Flat 14f Good 5/10 fig 50
    DATA for: Best recent form figure 50, 6 lb above field average; Has won at this trip or further
- Kevin The Great (hrs_52236261) | 4yo G | 135lb | OR 55 | draw 14 | jockey Gina Mangan | trainer Fergal O'Brien (14d 4/30) | headgear - | last run 91 days | form 604900 | MARKET 13.9% | 09:00 median 5.50 | Matchbook 6.80
    comment: He is yet to win in his last six, so the layoff is the one concern.
    DATA: model 8.3% | style Midfield (led 23% of runs) | runs in data 6 | last 3: 2 Jul Bellewstown Flat 14.5f Good 9/12; 15 Jul Killarney Flat 11.5f Good 11/15; 27 Aug Navan Flat 14f Good 10/22
    DATA for: Last-run finishing speed +2.6% vs that field (finished strongly)
    DATA against: Poor recent finishing positions; Returns from a 91-day break
- Sea of Charm (hrs_22327886) | 8yo M | 135lb | OR 55 | draw 4 | jockey William Cox | trainer Georgina Nicholls (14d 0/5) | headgear p | last run 10 days | form 322472 | MARKET 7.6% | 09:00 median 8.00 | Matchbook 15.50
    comment: Sea of Charm bids to build on a second last time out, 10 days ago, and has been in the first three in four of her last six, with a pair of seconds before that. She has run over today's trip and going, but she's yet to win and carries 135 lb.
    DATA: model 13.0% | style Midfield (led 4% of runs) | runs in data 13 | last 3: 23 Aug Brighton Flat 11.9f Good To Firm 4/6; 2 Nov Wolverhampton (AW) Flat 14f Standard 7/9 fig 43; 16 Nov Wolverhampton (AW) Flat 12f Standard 2/11 fig 53
    DATA for: Best recent form figure 53, 9 lb above field average
- Beggarman (hrs_20471976) | 9yo G | 132lb | OR 52 | draw 7 | jockey Rob Hornby | trainer Hughie Morrison (14d 0/6) | headgear - | last run 19 days | form 524087 | MARKET 7.3% | 09:00 median 11.00 | Matchbook 12.00
    comment: Beggarman has slipped to a seventh last time out and an eighth two starts back, though he did finish second five starts back and has run over today's trip and going.
    DATA: model 6.3% | style Held up (led 4% of runs) | runs in data 7 | last 3: 29 Sep Bath Flat 13.1f Good To Firm 11/13; 22 Oct Southwell (AW) Flat 14f Standard 8/12 fig 51; 7 Nov Southwell (AW) Flat 16.5f Standard 7/10 fig 46
    DATA for: Best recent form figure 51, 7 lb above field average
    DATA against: Poor recent finishing positions; Aged 9, older than most of this field
- Cavalry Call (hrs_34471794) | 5yo G | 127lb | OR 47 | draw 1 | jockey Paddy Bradley | trainer Patrick Morris (14d 0/14) | headgear - | last run 21 days | form 700083 | MARKET 6.2% | 09:00 median 12.00 | Matchbook 16.00
    comment: The risk is that he is winless in his last six, with an eighth two starts back.
    DATA: model 3.8% | style Prominent (led 43% of runs) | runs in data 9 | last 3: 3 Sep Haydock Flat 11.6f Soft 11/11; 17 Sep Southwell Flat 11.1f Standard 8/9; 5 Nov Chelmsford (AW) Flat 10f Standard 3/13 fig 53
    DATA for: Best recent form figure 53, 9 lb above field average; Recent figures 6 lb above its current mark (looks well handicapped)
    DATA against: Official rating 47, 5 lb below field average; Trainer 0 wins from 14 runs, last 14 days
- Damzon (hrs_40075616) | 7yo M | 128lb | OR 48 | draw 8 | jockey Marco Ghiani | trainer Tony Carroll (14d 2/36) | headgear - | last run 19 days | form 143588 | MARKET 6.1% | 09:00 median 13.00 | Matchbook 16.00
    comment: Damzon has slipped to back-to-back eighths after a fifth three starts back and a win six starts back, though she's fresh enough after 19 days and has run over today's trip and going.
    DATA: model 3.1% | style Midfield (led 4% of runs) | runs in data 6 | last 3: 26 Feb Chelmsford Flat 14f Standard 5/7; 1 Oct Nottingham Flat 17.9f Good 8/10; 7 Nov Southwell (AW) Flat 16.5f Standard 8/10 fig 36
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 36, 8 lb below field average; Recent figures 12 lb below its current mark (looks high in the weights)
- Gatlinburg (hrs_56338660) | 3yo G | 129lb | OR 54 | draw 12 | jockey Alistair Rawlinson | trainer Michael Attwater (14d 1/11) | headgear p | last run 29 days | form 840597 | MARKET 3.4% | 09:00 median 17.00 | Matchbook 40.00
    comment: Gatlinburg is yet to score in his last six starts, but he has run over today's going before and comes here fresh after 29 days off.
    DATA: model 7.5% | style Prominent (led 23% of runs) | runs in data 7 | last 3: 11 Sep Salisbury Flat 9.9f Soft 5/10; 13 Oct Leicester Flat 10f Good To Soft 9/13; 28 Oct Kempton (AW) Flat 8f Standard / Slow 7/10 fig 49
    DATA for: Best recent form figure 49, 5 lb above field average
- Implied Volatility (hrs_52862649) | 4yo G | 128lb | OR 48 | draw 11 | jockey George Wood | trainer Jennie Candlish (14d 4/32) | headgear p | last run 58 days | form -70000 | MARKET 2.9% | 09:00 median 23.00 | Matchbook 44.00
    comment: Implied Volatility has been unplaced in each of his last four starts and was only seventh five runs back, so he is hard to fancy, especially off 128 lb after 58 days off.
    DATA: model 4.6% | style Held up (led 4% of runs) | runs in data 5 | last 3: 6 Jul Wolverhampton Flat 8.6f Standard 10/13; 16 Aug Southwell Flat 8.1f Standard 12/13; 29 Sep Wolverhampton Flat 9.5f Standard 10/13
    DATA against: Poor recent finishing positions
- Champagne Beau (hrs_65451659) | 3yo F | 130lb | OR 55 | draw 5 | jockey Callum Hutchinson | trainer Patrick Chamings (14d 0/3) | headgear - | last run 71 days | form 98769 | MARKET 2.0% | 09:00 median 34.00 | Matchbook 60.00
    comment: Champagne Beau is winless in her last five, finishing ninth last time out and no better than sixth in that run, and she returns after 71 days off.
    DATA: model 7.9% | style Held up (led 3% of runs) | runs in data 5 | last 3: 13 Aug Lingfield Flat 10f Standard 7/9; 29 Aug Windsor Flat 11.4f Soft 6/13; 16 Sep Sandown Flat 9.9f Good 9/11
    DATA against: Poor recent finishing positions
- Head Girl (hrs_57008448) | 3yo F | 130lb | OR 55 | draw 10 | jockey Olivia Tubb(5) | trainer Jonathan Portman (14d 2/12) | headgear p | last run 22 days | form 391280 | MARKET 2.0% | 09:00 median 34.00 | Matchbook 60.00
    comment: Head Girl has been unplaced last time out and a eighth two starts back, so hard to fancy on recent evidence, though she did win four starts back and has run on today's going before.
    DATA: model 6.0% | style Prominent (led 29% of runs) | runs in data 7 | last 3: 29 Aug Chepstow Flat 12f Good To Soft 2/8; 22 Sep Southwell Flat 16.5f Standard 8/9; 4 Nov Kempton (AW) Flat 12f Standard / Slow 13/14 fig 20
    DATA against: Best recent form figure 20, 24 lb below field average; Recent figures 35 lb below its current mark (looks high in the weights); Last-run finishing speed -6.6% vs that field (faded)
- Crystal Jet (hrs_58196649) | 4yo F | 135lb | OR 55 | draw 3 | jockey George Downing | trainer Toby Bulgin (14d 0/2) | headgear v (1st time) | last run 28 days | form 8600 | MARKET 1.9% | 09:00 median 29.00 | Matchbook 75.00
    comment: Crystal Jet is winless in her last four, with an eighth and a sixth before two unplaced runs, though she has run over today's trip and going and returns after 28 days off.
    DATA: model 4.5% | style Midfield (led 23% of runs) | runs in data 7 | last 3: 3 Sep Southwell Flat 12.1f Standard 6/7; 26 Sep Southwell Flat 11.1f Standard 11/13; 29 Oct Southwell (AW) Flat 14f Standard 12/12
    DATA for: First-time headgear
    DATA against: Poor recent finishing positions
- Vinny's Dream (hrs_41229783) | 5yo G | 135lb | OR 55 | draw 9 | jockey Edward Greatrex | trainer Ian Williams (14d 3/27) | headgear p | last run 35 days | form 0/7-60 | MARKET 1.7% | 09:00 median 41.00 | Matchbook 75.00
    comment: Vinny's Dream has been unplaced last time out, with a sixth two starts back and a seventh three starts back, so he is winless in his last four.
    DATA: model 2.6% | style Prominent (led 8% of runs) | runs in data 2 | last 3: 29 Sep Wolverhampton Flat 12.2f Standard 6/6; 22 Oct Southwell (AW) Flat 14f Standard 11/12 fig 30
    DATA against: Best recent form figure 30, 14 lb below field average; Recent figures 25 lb below its current mark (looks high in the weights); Last-run finishing speed -6.1% vs that field (faded); Lightly raced: 2 runs in our data, so the model has little to go on
- Abila (hrs_55882344) | 4yo F | 127lb | OR 47 | draw 2 | jockey Ryan Kavanagh(3) | trainer Ian Williams (14d 3/27) | headgear - | last run 154 days | form -50667 | MARKET 1.7% | 09:00 median 41.00 | Matchbook 90.00
    comment: Abila is winless in her last five, finishing seventh last time out, then a sixth two starts back and another sixth three starts back, and she returns after 154 days off.
    DATA: model 2.4% | style Held up (led 4% of runs) | runs in data 5 | last 3: 25 Apr Southwell Flat 14.1f Standard 6/11; 25 May Leicester Flat 11.8f Good To Firm 6/7; 25 Jun Leicester Flat 11.8f Good To Firm 7/8
    DATA against: Official rating 47, 5 lb below field average; Poor recent finishing positions; Returns from a 154-day break

## 5:00 Chelmsford (AW) | race_id rac_32305975000 | Midnite Built Different Handicap Stakes (Div I)
Flat | Class 6 | 6f | going Standard | AW | 12 runners | rating band 0-55 | age 3yo+
DATA pace: Strong pace - 3 habitual front-runners (Sir Rodneyredblood, Dashing Donkey, Due Date). A contested lead should set things up for horses coming from behind.
- Mehmar (hrs_30208255) | 6yo G | 130lb | OR 50 | draw 10 | jockey Callum Shepherd | trainer Jack Jones (14d 0/6) | headgear - | last run 2 days | form 574022 | MARKET 46.4% | 09:00 median 1.80 | Matchbook 1.85
    comment: Mehmar comes in sharp after two seconds on his last two starts, just two days ago, and has run over today's trip and going before.
    DATA: model 24.2% | style Prominent (led 3% of runs) | runs in data 12 | last 3: 22 Jul Naas Flat 8f Good 12/18; 24 Oct Southwell (AW) Flat 6f Standard 2/11 fig 58; 24 Nov Wolverhampton (AW) Flat 6f Standard 2/13 fig 60
    DATA for: Best recent form figure 60, 16 lb above field average; Recent figures 10 lb above its current mark (looks well handicapped); Good recent finishing positions
- Dashing Donkey (hrs_39940719) | 5yo G | 133lb | OR 53 | draw 5 | jockey Billy Loughnane | trainer William Stone (14d 0/3) | headgear - | last run 37 days | form 504933 | MARKET 19.4% | 09:00 median 4.00 | Matchbook 4.80
    DATA: model 14.2% | style Leader (led 29% of runs) | runs in data 7 | last 3: 30 Jul Wolverhampton Flat 7.2f Standard 9/12; 18 Aug Lingfield Flat 6f Standard 3/9; 20 Oct Yarmouth Flat 6f Soft 3/9 fig 56
    DATA for: Best recent form figure 56, 12 lb above field average; Good recent finishing positions
    DATA against: Pace: likely to be taken on for the lead
- Due Date (hrs_28535101) | 6yo G | 132lb | OR 52 | draw 9 | jockey Rob Hornby | trainer Charlie Wallis (14d 0/2) | headgear v | last run 33 days | form 762435 | MARKET 6.5% | 09:00 median 10.00 | Matchbook 18.00
    comment: Due Date has been in the frame, with a second four starts back and a third two runs ago before a fifth last time, and he has run over today's trip and going.
    DATA: model 9.6% | style Prominent (led 43% of runs) | runs in data 10 | last 3: 18 Aug Lingfield Flat 6f Standard 4/9; 15 Sep Wolverhampton Flat 6.1f Standard 3/12; 24 Oct Southwell (AW) Flat 6f Standard 5/11 fig 50
    DATA for: Best recent form figure 50, 6 lb above field average
- Solid Bond (hrs_40786172) | 4yo F | 134lb | OR 54 | draw 11 | jockey Harry Davies | trainer Tony Carroll (14d 2/36) | headgear - | last run 6 days | form 920774 | MARKET 6.3% | 09:00 median 10.00 | Matchbook 19.00
    comment: The risk is a modest recent record, winless in her last six, with a seventh twice in that spell.
    DATA: model 7.9% | style Midfield (led 3% of runs) | runs in data 9 | last 3: 14 Oct Nottingham Flat 5f Good To Soft 7/9 fig 46; 7 Nov Southwell (AW) Flat 7f Standard 7/12 fig 52; 20 Nov Wolverhampton (AW) Flat 6f Standard 4/13 fig 53
    DATA for: Best recent form figure 53, 9 lb above field average; Last-run finishing speed +2.5% vs that field (finished strongly)
- Sir Rodneyredblood (hrs_18809490) | 9yo G | 135lb | OR 55 | draw 7 | jockey Marco Ghiani | trainer J. R. Jenkins (14d 1/7) | headgear p | last run 6 days | form 838209 | MARKET 5.7% | 09:00 median 13.00 | Matchbook 17.00
    comment: Sir Rodneyredblood has run over today's trip and on this going, and showed some ability with a second three starts back, but he was only ninth last time out and is yet to win in his last six starts.
    DATA: model 12.5% | style Leader (led 43% of runs) | runs in data 9 | last 3: 26 Jun Yarmouth Flat 6f Good To Firm 2/6; 14 Jul Leicester Flat 6f Good To Firm 10/11; 20 Nov Wolverhampton (AW) Flat 6f Standard 9/13 fig 46
    DATA for: Official rating 55, 5 lb above field average; Has won at this trip or further
    DATA against: Recent figures 9 lb below its current mark (looks high in the weights); Aged 9, older than most of this field; Pace: likely to be taken on for the lead
- No Claims Bonus (hrs_52297406) | 3yo F | 127lb | OR 47 | draw 4 | jockey Kaiya Fraser | trainer Harry Eustace (14d 0/9) | headgear - | last run 28 days | form 3525U4 | MARKET 3.8% | 09:00 median 19.00 | Matchbook 27.00
    comment: Fourth last time out and a second four starts back show she can be competitive, and 28 days since her last run is fine, but she is winless in her last six and unseated two starts back.
    DATA: model 5.6% | style Midfield (led 4% of runs) | runs in data 7 | last 3: 23 Sep Kempton Flat 6f Standard To Slow 5/11; 15 Oct Brighton Flat 5.5f Good UR/9; 29 Oct Bath Flat 5.5f Soft 4/16 fig 51
    DATA for: Best recent form figure 51, 7 lb above field average; Recent figures 4 lb above its current mark (looks well handicapped)
    DATA against: Trainer 0 wins from 9 runs, last 14 days
- He's An Angel (hrs_29917853) | 6yo G | 131lb | OR 51 | draw 3 | jockey Oliver Stammers | trainer Kevin & Lauren Frost (14d 1/10) | headgear t | last run 33 days | form 812850 | MARKET 2.8% | 09:00 median 22.00 | Matchbook 48.00
    comment: He's An Angel was unplaced last time out and a fifth two starts back, though he did win five starts back and has run over today's trip and going before.
    DATA: model 5.6% | style Midfield (led 8% of runs) | runs in data 14 | last 3: 21 Jun Pontefract Flat 6f Good 8/11; 14 Jul Beverley Flat 5f Good To Firm 5/10; 24 Oct Southwell (AW) Flat 6f Standard 11/11 fig 18
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 18, 26 lb below field average; Recent figures 33 lb below its current mark (looks high in the weights)
- Candy Warhol (hrs_25745853) | 7yo G | 130lb | OR 50 | draw 12 | jockey Kieran O'Neill | trainer Scott Dixon (14d 0/16) | headgear tp | last run 24 days | form 352600 | MARKET 2.5% | 09:00 median 29.00 | Matchbook 44.00
    comment: Candy Warhol is winless in his last six and unplaced in his last two, though a second four starts back and a third six back show he can get involved, and he has run over today's trip and going.
    DATA: model 3.3% | style Prominent (led 29% of runs) | runs in data 18 | last 3: 6 Oct Brighton Flat 6f Good To Firm 6/9; 19 Oct Wolverhampton (AW) Flat 6f Standard 12/13 fig 39; 2 Nov Chelmsford (AW) Flat 7f Standard 10/13 fig 30
    DATA against: Best recent form figure 39, 5 lb below field average; Recent figures 11 lb below its current mark (looks high in the weights); Trainer 0 wins from 16 runs, last 14 days; Last-run finishing speed -3.3% vs that field (faded); Poor recent finishing positions
- Shining Guest (hrs_54337458) | 3yo F | 129lb | OR 49 | draw 8 | jockey Kieran Shoemark | trainer George Margarson (14d 0/1) | headgear - | last run 29 days | form -65269 | MARKET 2.3% | 09:00 median 29.00 | Matchbook 46.00
    comment: Shining Guest is winless in her last five and was beaten into ninth last time out, so she is hard to fancy, though a second three starts back shows she can make the frame.
    DATA: model 4.9% | style Prominent (led 8% of runs) | runs in data 5 | last 3: 5 Aug Yarmouth Flat 5.2f Good To Firm 2/6; 1 Sep Brighton Flat 5.3f Good 6/6; 28 Oct Kempton (AW) Flat 6f Standard / Slow 9/11 fig 43
    DATA against: Recent figures 6 lb below its current mark (looks high in the weights)
- Mariselle (hrs_65774926) | 3yo F | 126lb | OR 43 | draw 1 | jockey Charles Bishop | trainer Adam Kirby (14d 1/9) | headgear b (1st time) | last run 31 days | form 795977 | MARKET 1.6% | 09:00 median 41.00 | Matchbook 110.00
    comment: Mariselle is hard to fancy, having finished seventh last time out, and another seventh two starts back, with nothing better than a fifth four starts back in her last six.
    DATA: model 2.8% | style Midfield (led 29% of runs) | runs in data 7 | last 3: 17 Sep Southwell Flat 5f Standard 9/12; 15 Oct Southwell (AW) Flat 7f Standard 7/13 fig 41; 26 Oct Southwell (AW) Flat 7f Standard 7/11 fig 37
    DATA for: First-time headgear
    DATA against: Official rating 43, 7 lb below field average; Poor recent finishing positions
- Bishop's Glory (hrs_29802045) | 6yo G | 126lb | OR 43 | draw 14 | jockey Alex Jary(3) | trainer Joey Ramsden (14d 0/4) | headgear v | last run 31 days | form 770579 | MARKET 1.4% | 09:00 median 41.00 | Matchbook 120.00
    comment: Bishop's Glory is winless in his last six, finishing ninth last time out and no better than a fifth three starts back, so he is hard to fancy.
    DATA: model 2.5% | style Held up (led 3% of runs) | runs in data 11 | last 3: 7 Jul Wolverhampton Flat 5.1f Standard 5/7; 6 Oct Southwell Flat 5f Standard 7/11; 26 Oct Southwell (AW) Flat 5f Standard 9/10 fig 29
    DATA for: Pace: a contested lead should suit its hold-up style
    DATA against: Best recent form figure 29, 15 lb below field average; Recent figures 14 lb below its current mark (looks high in the weights); Official rating 43, 7 lb below field average
- Society Charm (hrs_62457178) | 3yo F | 128lb | OR 48 | draw 6 | jockey Luke Morris | trainer Peter Chapple-Hyam (14d 0/1) | headgear - | last run 57 days | form 67730 | MARKET 1.4% | 09:00 median 41.00 | Matchbook 100.00
    comment: Society Charm is winless in her last five starts, with an unplaced effort last time out and a third two starts back her best finish, and she returns after 57 days off.
    DATA: model 7.1% | style Prominent (led 23% of runs) | runs in data 5 | last 3: 13 Apr Leicester Flat 7f Good 7/12; 31 Aug Southwell Flat 6.1f Standard 3/12; 30 Sep Catterick Flat 6f Good 10/10
    DATA against: Last-run finishing speed -6.2% vs that field (faded)

## 5:30 Chelmsford (AW) | race_id rac_32305632151 | Midnite Built Different Handicap Stakes (Div II)
Flat | Class 6 | 6f | going Standard | AW | 14 runners | rating band 0-55 | age 3yo+
DATA pace: Lone leader - Forever Noah is the only habitual front-runner and may be allowed an easy lead.
- Henry Tudor (hrs_53420332) | 4yo G | 126lb | OR 46 | draw 5 | jockey Luke Morris | trainer Mark Hoad (14d 0/0) | headgear - | last run 29 days | form 734336 | MARKET 18.0% | 09:00 median 4.50 | Matchbook 4.80 | CHECK (skip line 4.27)
    comment: Henry Tudor is yet to win in his last six starts but has been placed three times, including a third two starts back, and has run over today's trip and going before.
    DATA: model 10.0% | style Prominent (led 4% of runs) | runs in data 12 | last 3: 12 Sep Lingfield Flat 6f Standard 3/10; 12 Oct Kempton Flat 6f Standard To Slow 3/10; 28 Oct Kempton (AW) Flat 6f Standard / Slow 6/11 fig 42
    DATA for: Has won at this trip or further; Good recent finishing positions
- Sprinting Speed (hrs_55061937) | 3yo G | 133lb | OR 53 | draw 13 | jockey George Wood | trainer Jennie Candlish (14d 4/32) | headgear p | last run 41 days | form 588704 | MARKET 13.6% | 09:00 median 4.50 | Matchbook 8.20
    comment: Sprinting Speed steps up from a fourth last time out, has run over today's trip and going before, and returns after 41 days off.
    DATA: model 7.7% | style Midfield (led 29% of runs) | runs in data 7 | last 3: 1 Aug Doncaster Flat 7f Good To Firm 7/10; 17 Sep Southwell Flat 6.1f Standard 13/13; 16 Oct Newcastle (AW) Flat 7f Standard 4/8 fig 52
    DATA for: Best recent form figure 52, 11 lb above field average
- Forever Noah (hrs_34470968) | 5yo G | 135lb | OR 55 | draw 7 | jockey Taryn Langley(5) | trainer Joey Ramsden (14d 0/4) | headgear tv | last run 30 days | form 228260 | MARKET 11.8% | 09:00 median 7.00 | Matchbook 7.20
    comment: The risk is an unplaced run last time out and a 30-day break.
    DATA: model 6.5% | style Leader (led 54% of runs) | runs in data 13 | last 3: 21 May Southwell Flat 6.1f Standard 2/11; 8 Jun Pontefract Flat 5f Good 6/7; 27 Oct Wolverhampton (AW) Flat 7f Standard 11/11 fig 29
    DATA for: Official rating 55, 6 lb above field average; Has won at this trip or further; Pace: may get an uncontested lead
    DATA against: Best recent form figure 29, 12 lb below field average; Recent figures 26 lb below its current mark (looks high in the weights); Carries 6 lb more than average
- Starsong (hrs_25938808) | 7yo M | 130lb | OR 50 | draw 12 | jockey Alistair Rawlinson | trainer Michael Appleby (14d 1/18) | headgear p | last run 85 days | form 555204 | MARKET 10.6% | 09:00 median 6.50 | Matchbook 9.40
    comment: The main risk is an 85-day absence, plus 130 lb from stall 12 and no win in her last six.
    DATA: model 16.8% | style Prominent (led 8% of runs) | runs in data 10 | last 3: 26 Jul Pontefract Flat 6f Good To Firm 2/11; 16 Aug Southwell Flat 6.1f Standard 10/14; 2 Sep Bath Flat 5.7f Good 4/8
- Love Alive (hrs_54525548) | 3yo F | 134lb | OR 54 | draw 6 | jockey David Egan | trainer John Butler (14d 4/16) | headgear t | last run 6 days | form 597040 | MARKET 9.6% | 09:00 median 8.55 | Matchbook 9.40
    comment: Winless in her last six, Love Alive was unplaced last time out six days ago and managed a fourth two starts back, though she has run over today's trip and going before.
    DATA: model 10.1% | style Held up (led 4% of runs) | runs in data 14 | last 3: 13 Oct Wolverhampton Flat 6.1f Standard 10/12; 27 Oct Wolverhampton (AW) Flat 6f Standard 4/12 fig 56; 20 Nov Wolverhampton (AW) Flat 6f Standard 12/13 fig 36
    DATA for: Best recent form figure 56, 15 lb above field average; Official rating 54, 5 lb above field average; Trainer 25% wins (4/16), last 14 days
- Thanks Dad (hrs_39170012) | 6yo G | 130lb | OR 50 | draw 2 | jockey Kieran O'Neill | trainer Scott Dixon (14d 0/16) | headgear tv | last run 19 days | form 618580 | MARKET 8.8% | 09:00 median 9.50 | Matchbook 9.80
    comment: Thanks Dad has been below his best lately, unplaced last time out and an eighth two starts back, though he's a winner five starts back and has run over today's trip and going before.
    DATA: model 6.6% | style Midfield (led 3% of runs) | runs in data 8 | last 3: 2 Oct Wolverhampton Flat 6.1f Standard 5/10; 19 Oct Wolverhampton (AW) Flat 6f Standard 8/13 fig 47; 7 Nov Southwell (AW) Flat 6f Standard 10/11 fig 41
    DATA for: Best recent form figure 47, 6 lb above field average; Has won at this trip or further
    DATA against: Trainer 0 wins from 16 runs, last 14 days
- Saeculamation (hrs_52831023) | 3yo G | 126lb | OR 45 | draw 1 | jockey Callum Hutchinson | trainer John Mackie (14d 0/5) | headgear p | last run 58 days | form 668325 | MARKET 6.5% | 09:00 median 12.00 | Matchbook 14.50
    comment: Winless in his last six, Saeculamation was fifth last time out after a second two starts back, but a 58-day break and a 126 lb burden make him hard to fancy.
    DATA: model 9.9% | style Held up (led 4% of runs) | runs in data 12 | last 3: 30 Jul Nottingham Flat 6.1f Good To Firm 3/7; 17 Aug Lingfield Flat 5f Standard 2/6; 29 Sep Wolverhampton Flat 6.1f Standard 5/11
    DATA for: Good recent finishing positions
- Crystal Dagger (hrs_54933662) | 4yo F | 132lb | OR 52 | draw 9 | jockey Alex Jary(3) | trainer Joey Ramsden (14d 0/4) | headgear tv (1st time) | last run 28 days | form 848806 | MARKET 5.1% | 09:00 median 13.00 | Matchbook 22.00
    DATA: model 3.8% | style Prominent (led 5% of runs) | runs in data 8 | last 3: 21 Jul Wolverhampton Flat 6.1f Standard 8/11; 1 Oct Nottingham Flat 6.1f Good 15/15; 29 Oct Southwell (AW) Flat 7f Standard 6/12 fig 60
    DATA for: Best recent form figure 60, 19 lb above field average; Recent figures 8 lb above its current mark (looks well handicapped); First-time headgear
    DATA against: Poor recent finishing positions
- Addictive (hrs_39961971) | 4yo G | 127lb | OR 47 | draw 4 | jockey Georgia Dobie | trainer Craig Benton (14d 0/1) | headgear p (1st time) | last run 31 days | form 067800 | MARKET 4.5% | 09:00 median 17.00 | Matchbook 19.50
    comment: Addictive has been unplaced in his last two outings and is winless in his last six, though he has run over today's trip and on the going and returns after 31 days off.
    DATA: model 4.2% | style Held up (led 5% of runs) | runs in data 6 | last 3: 22 Jun Windsor Flat 5.1f Good To Firm 8/12; 5 Oct Kempton Flat 7f Standard To Slow 13/13; 26 Oct Kempton (AW) Flat 6f Standard / Slow 10/12 fig 31
    DATA for: First-time headgear
    DATA against: Best recent form figure 31, 10 lb below field average; Recent figures 16 lb below its current mark (looks high in the weights); Poor recent finishing positions
- Coolagh Magic (hrs_13961500) | 10yo G | 129lb | OR 49 | draw 10 | jockey William Carson | trainer Anthony Carson (14d 0/0) | headgear - | last run 85 days | form 964164 | MARKET 3.3% | 09:00 median 21.00 | Matchbook 30.00
    comment: Coolagh Magic was fourth last time out but has only one win in his last six, a victory three starts back, and he returns after 85 days off.
    DATA: model 8.8% | style Held up (led 3% of runs) | runs in data 10 | last 3: 26 Jun Yarmouth Flat 6f Good To Firm 1/6; 22 Aug Lingfield Flat 5f Standard 6/8; 2 Sep Bath Flat 5f Good 4/8
    DATA for: Has won at this trip or further
    DATA against: Aged 10, older than most of this field
- Porfin (hrs_21672875) | 8yo G | 126lb | OR 45 | draw 8 | jockey Grace McEntee | trainer Phil McEntee (14d 0/3) | headgear p | last run 105 days | form 045455 | MARKET 2.5% | 09:00 median 23.00 | Matchbook 48.00
    comment: Porfin is consistent but winless, finishing fifth last time out, a fifth two starts back and a fourth three starts back, and he has run over today's trip and going.
    DATA: model 5.0% | style Midfield (led 4% of runs) | runs in data 13 | last 3: 5 Jun Bath Flat 5.7f Good 4/9; 28 Jun Wolverhampton Flat 6.1f Standard 5/12; 13 Aug Lingfield Flat 6f Standard 5/8
    DATA for: Has won at this trip or further
    DATA against: Returns from a 105-day break
- In Denial (hrs_59246880) | 3yo F | 130lb | OR 50 | draw 11 | jockey Hope Regan(7) | trainer Mark Loughnane (14d 2/21) | headgear - | last run 30 days | form 463057 | MARKET 2.5% | 09:00 median 23.00 | Matchbook 65.00
    comment: In Denial is winless in her last six, with a seventh last time out and a third four starts back the best of a modest run, though she has run over today's trip and going before.
    DATA: model 4.6% | style Midfield (led 4% of runs) | runs in data 7 | last 3: 26 May Lingfield Flat 6f Good 10/13; 29 Jun Ffos Las Flat 6f Good 5/6; 27 Oct Wolverhampton (AW) Flat 5f Standard 7/9 fig 45
- Poetic Jack (hrs_32733512) | 6yo G | 126lb | OR 43 | draw 3 | jockey Oliver Stammers | trainer Robert Cowell (14d 1/8) | headgear p | last run 51 days | form 486660 | MARKET 2.2% | 09:00 median 34.00 | Matchbook 46.00
    comment: Poetic Jack is winless in his last six, with three sixths in his last four and an unplaced run last time out, and he returns after 51 days off.
    DATA: model 3.0% | style Unknown | runs in data 9 | last 3: 9 Jun Brighton Flat 5.3f Good 6/8; 31 Jul Wolverhampton Flat 5.1f Standard 6/6; 6 Oct Southwell Flat 5f Standard 11/11
    DATA against: Official rating 43, 6 lb below field average; Poor recent finishing positions
- Tilsworth Turf (hrs_37603538) | 6yo G | 126lb | OR 44 | draw 14 | jockey Jonny Peate | trainer J. R. Jenkins (14d 1/7) | headgear v (1st time) | last run 31 days | form 089380 | MARKET 1.1% | 09:00 median 51.00 | Matchbook 150.00
    comment: Tilsworth Turf is winless in his last six, with an unplaced effort last time out and only a third three starts back to show for his recent runs, so he is hard to fancy.
    DATA: model 3.1% | style Midfield (led 4% of runs) | runs in data 6 | last 3: 11 Jun Yarmouth Flat 6f Soft 3/8; 24 Sep Pontefract Flat 5f Good 8/8; 26 Oct Redcar Flat 6f Heavy 12/14 fig 8
    DATA for: First-time headgear
    DATA against: Best recent form figure 8, 33 lb below field average; Recent figures 36 lb below its current mark (looks high in the weights)

## 6:00 Chelmsford (AW) | race_id rac_32305634088 | All-Weather Championship Is Back Nursery Handicap Stakes
Flat | Class 5 | 6f | going Standard | AW | 7 runners | rating band 0-75 | age 2yo
DATA pace: Lone leader - Harry's Pop is the only habitual front-runner and may be allowed an easy lead.
- Dowman (hrs_63323687) | 2yo G | 146lb | OR 74 | draw 3 | jockey Billy Loughnane | trainer George Boughey (14d 6/25) | headgear t | last run 3 days | form 252311 | MARKET 34.7% | 09:00 median 2.50 | Matchbook 2.76
    comment: Dowman arrives in cracking nick, a winner last time out and again two starts back, with a third three starts back also in the book, and he has run over today's trip and going. The one risk is a quick turnaround, just three days since his last run, and 146 lb is a big burden.
    DATA: model 28.4% | style Held up (led 5% of runs) | runs in data 9 | last 3: 19 Oct Southwell (AW) Flat 6f Standard 3/13 fig 75; 17 Nov Southwell (AW) Flat 5f Standard 1/5 fig 82; 23 Nov Newcastle (AW) Flat 5f Standard 1/7 fig 81
    DATA for: Best recent form figure 82, 12 lb above field average; Recent figures 8 lb above its current mark (looks well handicapped); Trainer 24% wins (6/25), last 14 days; Last-run finishing speed +2.2% vs that field (finished strongly); Good recent finishing positions
    DATA against: Carries 14 lb more than average
- Roosike (hrs_65938957) | 2yo F | 135lb | OR 75 | draw 5 | jockey Hector Crouch | trainer Richard Hughes (14d 1/12) | headgear - | last run 21 days | form 210952 | MARKET 25.5% | 09:00 median 3.50 | Matchbook 3.60
    comment: Roosike steps up on a second last time out and has had 21 days to recover, while she has run over today's trip and on this going before. A win five starts back and a 135 lb burden are fair, though a ninth three starts back is a blemish.
    DATA: model 13.3% | style Prominent (led 4% of runs) | runs in data 7 | last 3: 10 Sep Doncaster Flat 6.5f Good To Soft 9/11; 3 Oct Southwell Flat 8.1f Standard 5/10; 5 Nov Chelmsford (AW) Flat 7f Standard 2/11 fig 84
    DATA for: Best recent form figure 84, 14 lb above field average; Recent figures 9 lb above its current mark (looks well handicapped); Last-run finishing speed +2.1% vs that field (finished strongly); Has won at this trip or further
- Harry's Pop (hrs_64324610) | 2yo G | 135lb | OR 75 | draw 1 | jockey David Egan | trainer Dylan Cunha (14d 2/15) | headgear - | last run 10 days | form 411532 | MARKET 17.4% | 09:00 median 5.00 | Matchbook 5.60
    comment: Harry's Pop arrives in solid form, second last time out, a third two starts back, and a winner four and five starts back, and he's fresh enough after ten days, with experience of today's trip and going.
    DATA: model 16.1% | style Leader (led 29% of runs) | runs in data 10 | last 3: 21 Sep Ffos Las Flat 6f Soft 5/5; 9 Oct Kempton Flat 6f Standard To Slow 3/10; 16 Nov Wolverhampton (AW) Flat 6f Standard 2/9 fig 76
    DATA for: Best recent form figure 76, 6 lb above field average; Has won at this trip or further; Good recent finishing positions; Pace: may get an uncontested lead
- Sioux Moon (hrs_17389756167) | 2yo F | 127lb | OR 67 | draw 4 | jockey Paddy Bradley | trainer Charlie Fellowes (14d 3/12) | headgear - | last run 38 days | form 35255 | MARKET 11.2% | 09:00 median 8.00 | Matchbook 8.60
    comment: Sioux Moon has been consistent, with a second three starts back and a third five runs ago, and she has run over today's trip and on the going before.
    DATA: model 10.7% | style Held up (led 5% of runs) | runs in data 5 | last 3: 31 Aug Southwell Flat 5f Standard 2/10; 21 Sep Leicester Flat 6f Good 5/14; 19 Oct Southwell (AW) Flat 6f Standard 5/13 fig 68
    DATA for: Trainer 25% wins (3/12), last 14 days; Last-run finishing speed +2.5% vs that field (finished strongly)
- By Jove Grace (hrs_65974587) | 2yo F | 130lb | OR 70 | draw 7 | jockey Ethan Tindall(5) | trainer Richard & Peter Fahey (14d 0/13) | headgear - | last run 30 days | form 25212 | MARKET 7.8% | 09:00 median 8.50 | Matchbook 16.50
    comment: By Jove Grace arrives in cracking form, second last time out and a winner two starts back, with four seconds or better in her last five runs.
    DATA: model 19.6% | style Held up (led 4% of runs) | runs in data 5 | last 3: 24 Aug Musselburgh Flat 5f Good 2/8; 21 Sep Hamilton Flat 5f Soft 1/5; 27 Oct Catterick Flat 6f Soft 2/7 fig 74
    DATA for: Recent figures 4 lb above its current mark (looks well handicapped); Good recent finishing positions
    DATA against: Trainer 0 wins from 13 runs, last 14 days
- Marhaba Ya Tayib (hrs_17391387419) | 2yo C | 133lb | OR 73 | draw 2 | jockey Charles Bishop | trainer Adam Kirby (14d 1/9) | headgear ht (1st time) | last run 21 days | form 410 | MARKET 1.8% | 09:00 median 51.00 | Matchbook 60.00
    DATA: model 10.3% | style Prominent (led 4% of runs) | runs in data 3 | last 3: 15 Sep Wolverhampton Flat 6.1f Standard 4/10; 30 Sep Kempton Flat 6f Standard To Slow 1/10; 5 Nov Chelmsford (AW) Flat 7f Standard 10/11 fig 39
    DATA for: Has won at this trip or further; First-time headgear
    DATA against: Best recent form figure 39, 32 lb below field average; Recent figures 34 lb below its current mark (looks high in the weights); Last-run finishing speed -5.1% vs that field (faded)
- Solar Mission (hrs_17391389505) | 2yo G | 117lb | OR 57 | draw 6 | jockey Kieran O'Neill | trainer Georgina Nicholls (14d 0/5) | headgear - | last run 49 days | form 0860 | MARKET 1.5% | 09:00 median 51.00 | Matchbook 80.00
    comment: Solar Mission is winless in his last four, unplaced last time and a sixth two starts back, and returns after 49 days off.
    DATA: model 1.7% | style Held up (led 4% of runs) | runs in data 4 | last 3: 8 Sep Leicester Flat 7f Good To Soft 8/9; 21 Sep Wolverhampton Flat 7.2f Standard 6/11; 8 Oct Southwell Flat 8.1f Standard 10/12
    DATA for: Carries 15 lb less than average
    DATA against: Official rating 57, 13 lb below field average; Last-run finishing speed -2.9% vs that field (faded); Poor recent finishing positions

## 6:30 Chelmsford (AW) | race_id rac_32305636025 | AWC Finals Day At Newcastle 26th March Fillies' Handicap Stakes
Flat | Class 5 | 7f | going Standard | AW | 7 runners | rating band 0-70 | age 3yo+
DATA pace: Even - Two likely leaders (Get An Attitude, Overbudget). A fair, even gallop is most likely.
- Forbidden Colours (hrs_57223089) | 3yo F | 133lb | OR 66 | draw 3 | jockey Kieran Shoemark | trainer Ed Walker (14d 2/24) | headgear - | last run 21 days | form 548453 | MARKET 22.7% | 09:00 median 3.88 | Matchbook 4.20 | CHECK (skip line 3.68)
    comment: The risk is she's yet to win in her last six starts.
    DATA: model 11.5% | style Held up (led 5% of runs) | runs in data 6 | last 3: 27 Jul Ayr Flat 7.2f Good To Firm 4/5; 14 Sep Kempton Flat 6f Standard To Slow 5/8; 5 Nov Southwell (AW) Flat 7f Standard 3/10 fig 69
    DATA for: Best recent form figure 69, 8 lb above field average
- Coxy's Star (hrs_49141904) | 3yo F | 128lb | OR 61 | draw 1 | jockey Lewis Edmunds | trainer William Muir & Chris Grassick (14d 0/7) | headgear - | last run 44 days | form 404921 | MARKET 17.8% | 09:00 median 4.50 | Matchbook 5.70
    comment: She has run over today's trip and going, and goes from stall one under 128 lb.
    DATA: model 19.0% | style Prominent (led 23% of runs) | runs in data 7 | last 3: 9 Sep Kempton Flat 8f Standard To Slow 9/14; 28 Sep Wolverhampton Flat 8.6f Standard 2/12; 13 Oct Wolverhampton Flat 8.6f Standard 1/10
    DATA for: Has won at this trip or further; Good recent finishing positions
- Overbudget (hrs_50434517) | 3yo F | 132lb | OR 65 | draw 6 | jockey Billy Loughnane | trainer Michael Appleby (14d 1/18) | headgear p | last run 31 days | form 698113 | MARKET 17.7% | 09:00 median 5.00 | Matchbook 5.30
    comment: She has run over today's trip and going, though 132 lb from stall six is a big ask.
    DATA: model 16.6% | style Leader (led 57% of runs) | runs in data 10 | last 3: 22 Sep Southwell Flat 6.1f Standard 1/12; 6 Oct Southwell Flat 6.1f Standard 1/10; 26 Oct Southwell (AW) Flat 6f Standard 3/8 fig 69
    DATA for: Best recent form figure 69, 8 lb above field average; Recent figures 4 lb above its current mark (looks well handicapped); Good recent finishing positions
- Bear Right (hrs_55273057) | 3yo F | 133lb | OR 66 | draw 2 | jockey Luke Morris | trainer Hayley Burton (14d 0/5) | headgear p | last run 39 days | form 332447 | MARKET 13.8% | 09:00 median 6.50 | Matchbook 6.60
    comment: Bear Right is yet to win in her last six, but she has banked a second and two thirds in that spell, and she has run over today's trip and going before.
    DATA: model 16.2% | style Midfield (led 4% of runs) | runs in data 10 | last 3: 20 Aug Leopardstown Flat 7f Good To Yielding 4/14; 2 Oct Dundalk Flat 7f Standard 4/13; 18 Oct Leopardstown (IRE) Flat 7f Good 7/14 fig 63
- Vishaka (hrs_54555550) | 3yo F | 134lb | OR 67 | draw 7 | jockey Callum Shepherd | trainer David Simcock (14d 2/10) | headgear - | last run 36 days | form 160-79 | MARKET 10.9% | 09:00 median 8.00 | Matchbook 8.60
    DATA: model 7.4% | style Unknown | runs in data 2 | last 3: 8 Oct Bath Flat 5.7f Good 7/10; 21 Oct Kempton (AW) Flat 6f Standard / Slow 9/11 fig 63
    DATA for: Trainer 20% wins (2/10), last 14 days
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Bella Bisbee (hrs_37275434) | 5yo M | 133lb | OR 65 | draw 5 | jockey Kieran O'Neill | trainer Scott Dixon (14d 0/16) | headgear - | last run 24 days | form 836667 | MARKET 9.8% | 09:00 median 9.00 | Matchbook 9.80
    comment: Bella Bisbee has been consistent without troubling the judge, finishing sixth in three of her last four before a seventh last time out, and she's yet to win in that run. She has run over today's trip and going, but a 133 lb burden from stall five makes it a tough ask.
    DATA: model 5.0% | style Prominent (led 29% of runs) | runs in data 21 | last 3: 11 Sep Doncaster Flat 8f Good 6/13; 22 Sep Southwell Flat 7.1f Standard 6/12; 2 Nov Chelmsford (AW) Flat 7f Standard 7/8 fig 40
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 40, 21 lb below field average; Recent figures 25 lb below its current mark (looks high in the weights); Trainer 0 wins from 16 runs, last 14 days; Last-run finishing speed -3.8% vs that field (faded); Poor recent finishing positions
- Get An Attitude (hrs_58993284) | 3yo F | 136lb | OR 69 | draw 4 | jockey Darragh Keenan | trainer Michael Keady (14d 1/3) | headgear - | last run 304 days | form 22-2 | MARKET 7.2% | 09:00 median 9.00 | Matchbook 17.50
    comment: The main risk is a 304-day absence, with 136 lb to carry from draw 4.
    DATA: model 24.2% | style Leader (led 57% of runs) | runs in data 1 | last 3: 26 Jan Wolverhampton Flat 7.2f Standard 2/8
    DATA against: Returns from a 304-day break; Lightly raced: 1 run in our data, so the model has little to go on

## 7:00 Chelmsford (AW) | race_id rac_32305637962 | Darley EBF Novice Stakes (GBB Race)
Flat | Class 2 | 7f | going Standard | AW | 6 runners | rating band - | age 2yo
DATA pace: Lone leader - Re Shardana is the only habitual front-runner and may be allowed an easy lead.
- Force of Light (hrs_7000002009) | 2yo C | 133lb | OR - | draw 6 | jockey Billy Loughnane | trainer Charlie Appleby (14d 4/9) | headgear - | wind surgery | last run 132 days | form 5 | MARKET 44.7% | 09:00 median 2.00 | Matchbook 2.12
    DATA: model 15.7% | style Unknown | runs in data 1 | last 3: 17 Jul Newbury Flat 7f Good To Firm 5/12
    DATA for: Trainer 44% wins (4/9), last 14 days
    DATA against: Returns from a 132-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Space Bob (hrs_17392231206) | 2yo C | 133lb | OR - | draw 4 | jockey Kieran Shoemark | trainer Ed Walker (14d 2/24) | headgear - | last run 43 days | form 2 | MARKET 36.8% | 09:00 median 2.38 | Matchbook 2.60
    DATA: model 36.0% | style Held up (led 8% of runs) | runs in data 1 | last 3: 14 Oct Nottingham Flat 8.5f Good To Soft 2/11 fig 66
    DATA for: Last-run finishing speed +3.4% vs that field (finished strongly)
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Sexy (hrs_17394428807) | 2yo F | 128lb | OR - | draw 1 | jockey Rowan Scott | trainer Charlie Johnston (14d 0/14) | headgear - | last run - days | form - | MARKET 8.8% | 09:00 median 9.00 | Matchbook 13.00
    DATA: model 13.0% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Trainer 0 wins from 14 runs, last 14 days; Lightly raced: 0 runs in our data, so the model has little to go on
- Nostalgic Warrior (hrs_17391772286) | 2yo C | 133lb | OR - | draw 2 | jockey P. J. McDonald | trainer Andrew Balding (14d 4/37) | headgear - | last run 71 days | form 5 | MARKET 7.2% | 09:00 median 13.00 | Matchbook 13.00
    DATA: model 17.4% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 16 Sep Yarmouth Flat 7f Good To Soft 5/7
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Clear Code (hrs_60819150) | 2yo G | 133lb | OR - | draw 3 | jockey Callum Hutchinson | trainer Andrew Balding (14d 4/37) | headgear - | last run - days | form - | MARKET 2.1% | 09:00 median 34.00 | Matchbook 75.00
    DATA: model 13.2% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Re Shardana (hrs_17390333989) | 2yo G | 133lb | OR - | draw 5 | jockey Marco Ghiani | trainer Clare Hobson (14d 0/6) | headgear tp | last run 21 days | form 79 | MARKET 0.5% | 09:00 median 251.00 | Matchbook 260.00
    DATA: model 4.7% | style Leader (led 72% of runs) | runs in data 2 | last 3: 7 Aug Newmarket Flat 7f Good To Firm 7/8; 5 Nov Chelmsford (AW) Flat 7.5f Standard 9/12 fig 41
    DATA for: Pace: may get an uncontested lead
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on

## 7:30 Chelmsford (AW) | race_id rac_32305639899 | AWC Season 14 Has Begun Handicap Stakes
Flat | Class 6 | 7f | going Standard | AW | 12 runners | rating band 0-55 | age 3yo+
DATA pace: Lone leader - Oh So Perfect is the only habitual front-runner and may be allowed an easy lead.
- Honey Dale (hrs_57942094) | 3yo F | 140lb | OR 55 | draw 4 | jockey Billy Loughnane | trainer Charlie Clover (14d 1/4) | headgear - | last run 5 days | form 505011 | MARKET 25.8% | 09:00 median 2.88 | Matchbook 3.70
    comment: Honey Dale arrives with back-to-back wins and has run over today's trip and going, but she is back quickly after five days off and carries 140 lb from stall four.
    DATA: model 22.5% | style Midfield (led 29% of runs) | runs in data 8 | last 3: 17 Jul Killarney Hurdle 17f Good PU/12; 26 Oct Southwell (AW) Flat 7f Standard 1/11 fig 46; 21 Nov Lingfield (AW) Flat 8f Standard 1/10 fig 58
    DATA for: Best recent form figure 58, 9 lb above field average; Last-run finishing speed +2.4% vs that field (finished strongly); Has won at this trip or further
    DATA against: Carries 7 lb more than average
- Tam Lin (hrs_44786490) | 4yo G | 133lb | OR 53 | draw 3 | jockey Harry Davies | trainer Michael Appleby (14d 1/18) | headgear - | last run 2 days | form 338845 | MARKET 18.8% | 09:00 median 4.33 | Matchbook 4.70
    comment: Tam Lin is yet to win in his last six, though a fifth last time out and a fourth two starts back show he's not far off, and he has run over today's trip and going.
    DATA: model 17.1% | style Prominent (led 23% of runs) | runs in data 8 | last 3: 20 Apr Lingfield Flat 8f Standard 8/11; 7 Nov Southwell (AW) Flat 6f Standard 4/11 fig 50; 24 Nov Lingfield (AW) Flat 7f Standard 5/13 fig 50
- Oh So Perfect (hrs_54555529) | 3yo F | 131lb | OR 52 | draw 6 | jockey Kieran Shoemark | trainer Michael Appleby (14d 1/18) | headgear - | last run 9 days | form 465553 | MARKET 15.2% | 09:00 median 5.50 | Matchbook 5.70
    comment: Third last time out and only nine days ago, Oh So Perfect looks fit and in form, with her latest run her best of the last six, and she has run over today's trip and going before. The risk is she is yet to win in her last six outings, and 131 lb from draw 6 is a hefty burden.
    DATA: model 12.7% | style Leader (led 54% of runs) | runs in data 11 | last 3: 16 Oct Redcar Flat 7f Good 5/18 fig 63; 3 Nov Wolverhampton (AW) Flat 7f Standard 5/11 fig 50; 17 Nov Southwell (AW) Flat 7f Standard 3/9 fig 48
    DATA for: Best recent form figure 63, 14 lb above field average; Recent figures 11 lb above its current mark (looks well handicapped); Has won at this trip or further; Pace: may get an uncontested lead
- Splinterwood (hrs_59609879) | 4yo G | 130lb | OR 50 | draw 12 | jockey Alistair Rawlinson | trainer Michael Appleby (14d 1/18) | headgear - | last run 102 days | form 7-6793 | MARKET 8.8% | 09:00 median 9.00 | Matchbook 10.50
    comment: Splinterwood bounced back with a third last time out, but he is winless in his last five and had been beaten in the previous four, with a ninth two starts back. He has run over today's trip and going, yet a 102-day break and 130 lb are hurdles to clear.
    DATA: model 4.5% | style Midfield (led 3% of runs) | runs in data 4 | last 3: 7 Feb Southwell Flat 8.1f Standard 7/12; 6 Jul Wolverhampton Flat 8.6f Standard 9/13; 16 Aug Southwell Flat 8.1f Standard 3/13
    DATA for: Last-run finishing speed +2.5% vs that field (finished strongly)
    DATA against: Returns from a 102-day break
- Rovinia (hrs_45921596) | 4yo F | 131lb | OR 51 | draw 9 | jockey Owen Lewis(5) | trainer Roger Teal (14d 0/10) | headgear - | last run 2 days | form 135323 | MARKET 8.3% | 09:00 median 9.00 | Matchbook 12.00
    comment: Rovinia has been consistent, finishing third last time out, a second two starts back and a third three starts back, and she has run over today's trip and going before.
    DATA: model 13.0% | style Midfield (led 3% of runs) | runs in data 14 | last 3: 30 Sep Kempton Flat 6f Standard To Slow 3/11; 3 Nov Wolverhampton (AW) Flat 7f Standard 2/10 fig 50; 24 Nov Lingfield (AW) Flat 7f Standard 3/13 fig 49
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Trainer 0 wins from 10 runs, last 14 days
- Bad Habits (hrs_45791935) | 4yo G | 134lb | OR 54 | draw 2 | jockey James Sullivan | trainer Ruth Carr (14d 2/11) | headgear b | last run 28 days | form 291360 | MARKET 6.3% | 09:00 median 12.50 | Matchbook 15.00
    comment: Bad Habits was unplaced last time out and a sixth two starts back, so the recent trend is the wrong way, though he did win four starts back and has run over today's trip and going.
    DATA: model 4.1% | style Midfield (led 4% of runs) | runs in data 14 | last 3: 8 May Wolverhampton Flat 7.2f Standard 3/9; 24 Sep Southwell Flat 7.1f Standard 6/9; 29 Oct Southwell (AW) Flat 7f Standard 10/13 fig 45
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 45, 4 lb below field average; Recent figures 9 lb below its current mark (looks high in the weights)
- Amaysmont (hrs_19601526) | 9yo G | 134lb | OR 54 | draw 5 | jockey Matthew Lloyd Slater(7) | trainer Kevin & Lauren Frost (14d 1/10) | headgear t (1st time) | last run 23 days | form 038249 | MARKET 4.0% | 09:00 median 19.00 | Matchbook 25.00
    comment: Amaysmont chased home a second three starts back and was fourth two runs ago, so the ninth last time out looks the outlier, and he returns after 23 days with experience of today's trip and going.
    DATA: model 8.0% | style Midfield (led 5% of runs) | runs in data 10 | last 3: 9 Jun Carlisle Flat 5.8f Good To Soft 2/6; 7 Jul Wolverhampton Flat 6.1f Standard 4/10; 3 Nov Wolverhampton (AW) Flat 7f Standard 9/11 fig 42
    DATA for: First-time headgear
    DATA against: Best recent form figure 42, 7 lb below field average; Recent figures 12 lb below its current mark (looks high in the weights)
- Rogue Federation (hrs_49141036) | 3yo G | 134lb | OR 55 | draw 8 | jockey Marco Ghiani | trainer Kevin & Lauren Frost (14d 1/10) | headgear - | last run 87 days | form 5087 | MARKET 3.5% | 09:00 median 21.00 | Matchbook 28.00
    comment: Rogue Federation is winless in his last four, finishing seventh last time, and he returns after 87 days off.
    DATA: model 3.0% | style Held up (led 5% of runs) | runs in data 4 | last 3: 28 Jun Wolverhampton Flat 7.2f Standard 11/12; 23 Jul Southwell Flat 7.1f Standard 8/12; 31 Aug Southwell Flat 6.1f Standard 7/12
    DATA for: Last-run finishing speed +2.1% vs that field (finished strongly)
    DATA against: Poor recent finishing positions
- The Organiser (hrs_24846486) | 7yo G | 133lb | OR 53 | draw 11 | jockey Kieren Fox | trainer Mark Pattinson (14d 0/2) | headgear t | last run 42 days | form 453574 | MARKET 3.2% | 09:00 median 21.00 | Matchbook 38.00
    comment: The risk is that he is winless in his last six and returns after 42 days off.
    DATA: model 4.7% | style Midfield (led 5% of runs) | runs in data 9 | last 3: 24 Aug Brighton Flat 6f Good To Firm 5/5; 6 Oct Brighton Flat 7f Good To Firm 7/10; 15 Oct Brighton Flat 7f Good 4/13 fig 56
    DATA for: Best recent form figure 56, 7 lb above field average
- Fistral Beach (hrs_35417326) | 5yo M | 135lb | OR 55 | draw 1 | jockey Jack Doughty | trainer John Mackie (14d 0/5) | headgear p | last run 21 days | form 123700 | MARKET 2.8% | 09:00 median 26.00 | Matchbook 46.00
    comment: Fistral Beach has tailed off since a win six starts back, with a seventh three starts back followed by two unplaced runs, and she's hard to fancy as a result.
    DATA: model 3.5% | style Midfield (led 3% of runs) | runs in data 11 | last 3: 1 Jun Wolverhampton Flat 7.2f Standard 7/11; 14 Jul Wolverhampton Flat 7.2f Standard 10/10; 5 Nov Southwell (AW) Flat 7f Standard 10/10 fig 32
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 32, 17 lb below field average; Recent figures 23 lb below its current mark (looks high in the weights); Poor recent finishing positions
- Grand Citadel (hrs_36528023) | 5yo M | 132lb | OR 52 | draw 13 | jockey Darragh O'Sullivan(7) | trainer Micky Fenton (14d 0/0) | headgear b | last run 33 days | form 210879 | MARKET 2.0% | 09:00 median 41.00 | Matchbook 60.00
    comment: Grand Citadel has run over today's trip and going before, and she showed she can win with a victory five starts back, though she's been beaten in her last three outings.
    DATA: model 3.3% | style Midfield (led 4% of runs) | runs in data 12 | last 3: 4 Jul Leicester Flat 6f Good To Firm 8/11; 15 Oct Brighton Flat 6f Good 7/9 fig 43; 24 Oct Southwell (AW) Flat 8f Standard 9/13 fig 46
    DATA for: Has won at this trip or further
    DATA against: Recent figures 6 lb below its current mark (looks high in the weights); Poor recent finishing positions
- Nubough (hrs_13020455) | 10yo G | 131lb | OR 51 | draw 7 | jockey Kieran O'Neill | trainer Mark Pattinson (14d 0/2) | headgear - | last run 69 days | form 260577 | MARKET 1.4% | 09:00 median 47.50 | Matchbook 140.00
    comment: Nubough is winless in his last six, with a seventh last time out and another seventh two starts back, and a 69-day break leaves fitness a question.
    DATA: model 3.5% | style Held up (led 5% of runs) | runs in data 6 | last 3: 21 May Southwell Flat 7.1f Standard 5/9; 20 Aug Lingfield Flat 8f Standard 7/11; 18 Sep Wolverhampton Flat 7.2f Standard 7/8
    DATA against: Last-run finishing speed -3.5% vs that field (faded); Aged 10, older than most of this field

## 8:00 Chelmsford (AW) | race_id rac_32305641836 | Make The Move To Midnite Handicap Stakes
Flat | Class 5 | 6f | going Standard | AW | 8 runners | rating band 0-70 | age 3yo+
DATA pace: Even - Two likely leaders (Distillation, Rebel Path). A fair, even gallop is most likely.
- Freddie's Star (hrs_56370664) | 4yo G | 134lb | OR 68 | draw 1 | jockey Marco Ghiani | trainer Roger Teal (14d 0/10) | headgear p | last run 22 days | form 054751 | MARKET 28.6% | 09:00 median 3.00 | Matchbook 3.15 | CHECK (skip line 2.85)
    comment: Fresh from a win last time out, and just 22 days ago, Freddie's Star has run over today's trip and going, but a fifth, seventh and fourth before that show a modest record.
    DATA: model 17.3% | style Prominent (led 4% of runs) | runs in data 7 | last 3: 14 Aug Epsom Downs Flat 7f Good To Firm 7/9; 22 Oct Newmarket Flat 7f Soft 5/12 fig 67; 4 Nov Kempton (AW) Flat 6f Standard / Slow 1/11 fig 69
    DATA for: Best recent form figure 69, 6 lb above field average; Has won at this trip or further
    DATA against: Trainer 0 wins from 10 runs, last 14 days
- Distillation (hrs_58033661) | 3yo G | 133lb | OR 67 | draw 4 | jockey Rose Dawes(3) | trainer Mark Usher (14d 2/9) | headgear - | last run 24 days | form 562124 | MARKET 17.3% | 09:00 median 5.10 | Matchbook 5.10
    comment: Fourth last time out, after a second two starts back and a win three starts back, suggests Distillation is in reasonable heart, and he has run over today's trip and going.
    DATA: model 13.5% | style Leader (led 54% of runs) | runs in data 10 | last 3: 21 Sep Wolverhampton Flat 7.2f Standard 1/9; 29 Sep Wolverhampton Flat 7.2f Standard 2/10; 2 Nov Wolverhampton (AW) Flat 7f Standard 4/7 fig 62
    DATA for: Trainer 22% wins (2/9), last 14 days; Has won at this trip or further; Good recent finishing positions
- Fantasy Obsessor (hrs_48112323) | 4yo F | 128lb | OR 62 | draw 5 | jockey David Egan | trainer Michael Appleby (14d 1/18) | headgear - | last run 31 days | form 275233 | MARKET 16.5% | 09:00 median 5.00 | Matchbook 5.70
    comment: Fantasy Obsessor is yet to win in her last six, but a third last time out, and a third two starts back, show she is consistently in the frame, and she has run over today's trip and going.
    DATA: model 13.5% | style Prominent (led 5% of runs) | runs in data 11 | last 3: 31 Aug Southwell Flat 6.1f Standard 2/12; 6 Oct Southwell Flat 6.1f Standard 3/10; 26 Oct Southwell (AW) Flat 6f Standard 3/10 fig 59
    DATA for: Good recent finishing positions
- Insuspense (hrs_45950660) | 4yo F | 133lb | OR 67 | draw 9 | jockey William Carver | trainer Ross Burdon (14d 1/3) | headgear t | last run 29 days | form 753152 | MARKET 10.0% | 09:00 median 7.00 | Matchbook 11.50
    comment: The main risk is a fifth two starts back, which shows she can be inconsistent.
    DATA: model 22.3% | style Held up (led 5% of runs) | runs in data 12 | last 3: 17 Sep Southwell Flat 6.1f Standard 1/13; 6 Oct Southwell Flat 6.1f Standard 5/10; 28 Oct Kempton (AW) Flat 6f Standard / Slow 2/11 fig 68
    DATA for: Best recent form figure 68, 5 lb above field average; Has won at this trip or further; Good recent finishing positions
- Flash Rascal (hrs_52742200) | 3yo G | 131lb | OR 65 | draw 2 | jockey Laura Pearson | trainer David Loughnane (14d 3/12) | headgear - | last run 33 days | form 187866 | MARKET 9.5% | 09:00 median 9.00 | Matchbook 9.80
    comment: Flash Rascal has finished sixth in each of his last two, but he won six starts back and has run over today's trip and going before, returning fresh after 33 days off.
    DATA: model 6.2% | style Midfield (led 4% of runs) | runs in data 9 | last 3: 18 Sep Wolverhampton Flat 6.1f Standard 8/10; 9 Oct Kempton Flat 7f Standard To Slow 6/11; 24 Oct Southwell (AW) Flat 7f Standard 6/14 fig 66
    DATA for: Trainer 25% wins (3/12), last 14 days; Has won at this trip or further
    DATA against: Poor recent finishing positions
- Macanudo (hrs_35767543) | 5yo G | 128lb | OR 62 | draw 3 | jockey Billy Loughnane | trainer Ian Williams (14d 3/27) | headgear v | last run 21 days | form 711323 | MARKET 8.6% | 09:00 median 8.50 | Matchbook 13.00
    comment: Macanudo has been in the frame in his last three, a third last time out, a second two starts back and a third three starts back, with a win four starts back, and he has run over today's trip and going.
    DATA: model 17.7% | style Prominent (led 8% of runs) | runs in data 8 | last 3: 28 Sep Brighton Flat 6f Good To Firm 3/8; 27 Oct Wolverhampton (AW) Flat 5f Standard 2/9 fig 60; 5 Nov Southwell (AW) Flat 5f Standard 3/13 fig 67
    DATA for: Best recent form figure 67, 4 lb above field average; Recent figures 5 lb above its current mark (looks well handicapped); Last-run finishing speed +2.6% vs that field (finished strongly); Good recent finishing positions
- Rebel Path (hrs_26116608) | 7yo G | 130lb | OR 64 | draw 8 | jockey Chloe Lyons(7) | trainer Stuart Williams (14d 0/9) | headgear - | last run 24 days | form 381853 | MARKET 8.1% | 09:00 median 9.50 | Matchbook 12.50
    DATA: model 7.7% | style Leader (led 29% of runs) | runs in data 11 | last 3: 14 Sep Windsor Flat 6.1f Good To Soft 8/13; 6 Oct Leicester Flat 6f Good To Firm 5/7; 2 Nov Chelmsford (AW) Flat 5f Standard 3/7 fig 62
    DATA for: Has won at this trip or further
    DATA against: Trainer 0 wins from 9 runs, last 14 days; Aged 7, older than most of this field
- Double Eagle (hrs_55091883) | 3yo G | 121lb | OR 55 | draw 6 | jockey John Egan | trainer Michael Wigham (14d 0/2) | headgear t | last run 21 days | form 3-9968 | MARKET 1.4% | 09:00 median 51.00 | Matchbook 95.00
    comment: Double Eagle has finished eighth, sixth, ninth and ninth in his last four outings and is yet to win in recent starts, so he is hard to fancy; he has run over today's trip and going, and a third five starts back is the best of it.
    DATA: model 1.7% | style Held up (led 4% of runs) | runs in data 4 | last 3: 3 Sep Southwell Flat 8.1f Standard 9/9; 17 Oct Southwell (AW) Flat 7f Standard 6/9 fig 50; 5 Nov Southwell (AW) Flat 6f Standard 8/9 fig 42
    DATA for: Carries 9 lb less than average
    DATA against: Best recent form figure 50, 13 lb below field average; Official rating 55, 9 lb below field average; Poor recent finishing positions

## 8:30 Chelmsford (AW) | race_id rac_32305643773 | Midnite Ain't Your Grandad's Bookie Handicap Stakes (GBBPlus Race)
Flat | Class 4 | 1m2f | going Standard | AW | 10 runners | rating band 0-80 | age 3yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Caledonian (hrs_43228864) | 4yo G | 131lb | OR 71 | draw 2 | jockey Callum Shepherd | trainer David Simcock (14d 2/10) | headgear - | last run 4 days | form 845513 | MARKET 20.7% | 09:00 median 4.00 | Matchbook 4.20 | CHECK (skip line 3.80)
    comment: He has run over today's trip and going before and carries 131 lb from stall two.
    DATA: model 13.1% | style Held up (led 5% of runs) | runs in data 7 | last 3: 17 Oct Southwell (AW) Flat 11f Standard 5/6 fig 59; 2 Nov Wolverhampton (AW) Flat 9.5f Standard 1/9 fig 69; 22 Nov Lingfield (AW) Flat 10f Standard 3/8 fig 67
    DATA for: Trainer 20% wins (2/10), last 14 days; Has won at this trip or further; Good recent finishing positions
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Colonnade (hrs_66655568) | 3yo G | 133lb | OR 76 | draw 6 | jockey Billy Loughnane | trainer Simon Crisford (14d 4/9) | headgear t | last run 52 days | form 35329 | MARKET 16.0% | 09:00 median 5.00 | Matchbook 5.80
    comment: Colonnade was second two starts back and third three and five starts back, so he's been in the frame often despite being winless in his last five, and he has run over today's trip and going before.
    DATA: model 12.9% | style Midfield (led 23% of runs) | runs in data 5 | last 3: 27 Aug Lingfield Flat 8f Standard 3/7; 12 Sep Bath Flat 10.2f Good 2/5; 5 Oct Yarmouth Flat 8f Good To Firm 9/11
    DATA for: Trainer 44% wins (4/9), last 14 days; Good recent finishing positions
- Nizam (hrs_46013527) | 4yo G | 140lb | OR 80 | draw 8 | jockey Edward Greatrex | trainer Ian Williams (14d 3/27) | headgear - | last run 20 days | form 000000 | MARKET 14.0% | 09:00 median 6.00 | Matchbook 6.60
    comment: Nizam has been unplaced in each of his last six starts, but he returns fresh from a 20-day break and has run over today's trip and going before.
    DATA: model 7.2% | style Midfield (led 8% of runs) | runs in data 8 | last 3: 26 Sep Newmarket Flat 9f Good To Firm 17/27; 9 Oct York Flat 7.9f Good To Soft 11/17; 6 Nov Newcastle (AW) Flat 10f Standard 11/14 fig 77
    DATA for: Best recent form figure 77, 8 lb above field average; Official rating 80, 6 lb above field average
    DATA against: Poor recent finishing positions; Carries 7 lb more than average
- Metallo (hrs_34471017) | 5yo G | 134lb | OR 74 | draw 1 | jockey David Egan | trainer John Butler (14d 4/16) | headgear - | last run 24 days | form 440203 | MARKET 13.9% | 09:00 median 6.00 | Matchbook 6.80
    comment: The risk is that he is yet to win in his last six starts, so he still has to get his head in front.
    DATA: model 11.8% | style Midfield (led 3% of runs) | runs in data 10 | last 3: 12 Aug Kempton Flat 8f Standard To Slow 2/10; 10 Oct York Flat 7.9f Soft 13/20; 2 Nov Chelmsford (AW) Flat 10f Standard 3/8 fig 74
    DATA for: Best recent form figure 74, 5 lb above field average; Trainer 25% wins (4/16), last 14 days; Good recent finishing positions
- Charlie's Choice (hrs_34775195) | 6yo G | 132lb | OR 72 | draw 7 | jockey Taryn Langley(5) | trainer David Simcock (14d 2/10) | headgear - | last run 3 days | form 044874 | MARKET 9.9% | 09:00 median 8.50 | Matchbook 9.80
    comment: Charlie's Choice has run over today's trip and going and was a fourth last time out, but he is winless in his last six and was only eighth three starts back.
    DATA: model 10.2% | style Held up (led 3% of runs) | runs in data 15 | last 3: 14 Oct Kempton (AW) Flat 11f Standard / Slow 8/13 fig 71; 27 Oct Wolverhampton (AW) Flat 12f Standard 7/10 fig 67; 23 Nov Wolverhampton (AW) Flat 12f Standard 4/11 fig 75
    DATA for: Best recent form figure 75, 6 lb above field average; Trainer 20% wins (2/10), last 14 days; Has won at this trip or further
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Kokoluna (hrs_58196453) | 3yo F | 134lb | OR 77 | draw 5 | jockey Charles Bishop | trainer Eve Johnson Houghton (14d 1/3) | headgear p (1st time) | last run 24 days | form 142171 | MARKET 9.2% | 09:00 median 7.00 | Matchbook 13.00
    comment: Kokoluna won last time out, 24 days ago, and has three wins in her last six starts, though a seventh two starts back shows she can miss the mark.
    DATA: model 16.4% | style Midfield (led 3% of runs) | runs in data 6 | last 3: 28 Aug Goodwood Flat 9.9f Good To Firm 1/12; 7 Oct Nottingham Flat 10.2f Good To Soft 7/10; 2 Nov Chelmsford (AW) Flat 10f Standard 1/8 fig 77
    DATA for: Best recent form figure 77, 8 lb above field average; Has won at this trip or further; Good recent finishing positions; First-time headgear
- Super Hit (hrs_36529045) | 5yo G | 124lb | OR 64 | draw 4 | jockey Kieran O'Neill | trainer James Owen (14d 4/46) | headgear ht | last run 22 days | form 552337 | MARKET 5.6% | 09:00 median 13.00 | Matchbook 18.50
    comment: Super Hit is yet to win in his last six, and a seventh last time out follows a run of thirds and a second, so he keeps finding a couple too good.
    DATA: model 7.3% | style Midfield (led 4% of runs) | runs in data 18 | last 3: 5 Oct Kempton Flat 12f Standard To Slow 3/10; 15 Oct Southwell (AW) Flat 11f Standard 3/7 fig 62; 4 Nov Kempton (AW) Flat 12f Standard / Slow 7/14 fig 61
    DATA for: Has won at this trip or further; Good recent finishing positions; Carries 9 lb less than average
    DATA against: Best recent form figure 62, 7 lb below field average; Official rating 64, 10 lb below field average
- Thinthread (hrs_47621434) | 4yo G | 137lb | OR 77 | draw 9 | jockey Neil Callan | trainer George Baker (14d 1/7) | headgear - | last run 29 days | form -50749 | MARKET 5.0% | 09:00 median 17.00 | Matchbook 18.50
    comment: Winless in his last five, Thinthread was ninth last time out, though a fourth two starts back shows he can be competitive, and he has run over today's trip.
    DATA: model 7.6% | style Midfield (led 4% of runs) | runs in data 5 | last 3: 30 Aug Goodwood Flat 9.9f Soft 7/10; 23 Sep Kempton Flat 11f Standard To Slow 4/8; 28 Oct Kempton (AW) Flat 12f Standard / Slow 9/10 fig 64
    DATA against: Best recent form figure 64, 5 lb below field average; Recent figures 13 lb below its current mark (looks high in the weights)
- Marsh Benham (hrs_24854599) | 7yo G | 132lb | OR 72 | draw 10 | jockey Jack Callan | trainer George Baker (14d 1/7) | headgear - | last run 27 days | form 175399 | MARKET 3.3% | 09:00 median 19.00 | Matchbook 42.00
    comment: Beaten in his last two outings, finishing ninth both times, Marsh Benham is hard to fancy, though he was third three starts back and returns after 27 days off, and he has run over today's trip and going.
    DATA: model 7.4% | style Held up (led 4% of runs) | runs in data 10 | last 3: 9 Oct Kempton Flat 8f Standard To Slow 3/10; 26 Oct Leicester Flat 8f Soft 9/10; 30 Oct Newmarket Flat 8f Good To Soft 9/15 fig 63
    DATA against: Best recent form figure 63, 6 lb below field average; Recent figures 9 lb below its current mark (looks high in the weights); Pace: steady gallop likely, hard to come from off the pace
- Mr Baloo (hrs_35054502) | 5yo G | 135lb | OR 75 | draw 3 | jockey Paddy Bradley | trainer Ross Burdon (14d 1/3) | headgear - | last run 38 days | form 198707 | MARKET 2.5% | 09:00 median 29.00 | Matchbook 46.00
    comment: Mr Baloo's recent form is moderate, with a seventh last time out, though he has run over today's trip and going and last won six starts back.
    DATA: model 6.1% | style Midfield (led 3% of runs) | runs in data 10 | last 3: 16 May Newmarket Flat 8f Good 7/12; 29 Jun Kempton Flat 8f Standard To Slow 11/14; 19 Oct Southwell (AW) Flat 8f Standard 7/11 fig 64
    DATA against: Best recent form figure 64, 5 lb below field average; Recent figures 11 lb below its current mark (looks high in the weights); Poor recent finishing positions
