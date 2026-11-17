# Card review packet: Southwell (AW), 2026-11-17

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
{"meeting": "southwell_aw", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 4:30 Southwell (AW) | race_id rac_32304653966 | Midnite: Built For 2026 Not 2006 Handicap Stakes (Rider Restricted Race)
Flat | Class 5 | 4f214y | going Standard | AW | 13 runners | rating band 0-75 | age 3yo+
DATA pace: Strong pace - 4 habitual front-runners (Beaumadier, Jax Edge, Managing Director, Castan). A contested lead should set things up for horses coming from behind.
- Managing Director (hrs_42452165) | 4yo G | 132lb | OR 72 | draw 3 | jockey Barry McHugh | trainer Geoff Oldroyd (14d 0/1) | headgear - | last run 56 days | form /53204 | MARKET 18.4% | 09:00 median 4.00 | Matchbook - | CHECK (skip line 3.80)
    comment: Managing Director is yet to win in his last five starts but has been in the frame twice, a second three starts back and a third four back, before a fourth last time out. Fifty-six days off and 132 lb temper the case, though he has run over today's trip and going.
    DATA: model 15.5% | style Leader (led 79% of runs) | runs in data 5 | last 3: 14 Aug Thirsk 5f Good 2/9; 6 Sep York 5.4f Good To Soft 11/21; 22 Sep Southwell 5f Standard 4/7
    DATA for: Course: front-runners have won 1.3× their fair share at 5f here
    DATA against: Pace: likely to be taken on for the lead
- Bonnie's Boy (hrs_43385293) | 4yo G | 132lb | OR 72 | draw 5 | jockey Ryan Sexton | trainer Richard & Peter Fahey (14d 2/15) | headgear - | last run 59 days | form 404352 | MARKET 15.4% | 09:00 median 5.00 | Matchbook -
    comment: The risk is 59 days off the track, so fitness is the question at 132 lb.
    DATA: model 16.0% | style Midfield (led 4% of runs) | runs in data 6 | last 3: 22 Aug Redcar 6f Good 3/8; 6 Sep York 5.4f Good To Soft 5/21; 19 Sep Newcastle 5f Standard 2/10
    DATA for: Good recent finishing positions
- Lion's House (hrs_36207598) | 5yo G | 126lb | OR 66 | draw 11 | jockey Rhys Clutterbuck | trainer Linda Perratt (14d 0/3) | headgear - | last run 11 days | form 042604 | MARKET 9.7% | 09:00 median 8.00 | Matchbook -
    DATA: model 6.0% | style Held up (led 4% of runs) | runs in data 16 | last 3: 15 Aug Doncaster 5.7f Good To Firm 6/10; 17 Sep Ayr 5f Soft 15/20; 6 Nov Newcastle (AW) 5f Standard 4/14 fig 69
    DATA for: Has won at this trip or further; Pace: a contested lead should suit its hold-up style
    DATA against: Course: hold-up horses have won 0.6× their fair share at 5f here
- Castan (hrs_29918210) | 6yo G | 130lb | OR 70 | draw 9 | jockey Oisin McSweeney | trainer Bryan Smart (14d 0/4) | headgear p | last run 32 days | form 963892 | MARKET 8.6% | 09:00 median 8.50 | Matchbook -
    comment: Castan was second last time out and has run over today's trip and going, but he is winless in his last six and was ninth two starts back.
    DATA: model 7.1% | style Leader (led 29% of runs) | runs in data 12 | last 3: 20 Aug Newcastle 5f Standard 8/13; 19 Sep Newcastle 5f Standard 9/10; 16 Oct Redcar 5f Good 2/10 fig 74
    DATA for: Best recent form figure 74, 5 lb above field average; Recent figures 4 lb above its current mark (looks well handicapped); Has won at this trip or further; Course: front-runners have won 1.3× their fair share at 5f here
    DATA against: Pace: likely to be taken on for the lead
- Grandlad (hrs_40293729) | 5yo G | 133lb | OR 73 | draw 12 | jockey Stevie Donohoe | trainer James Horton (14d 0/4) | headgear t | last run 32 days | form 676904 | MARKET 7.8% | 09:00 median 9.80 | Matchbook -
    comment: Grandlad is yet to win in his last six starts, though a fourth last time out is his best recent finish, and he has run over today's trip and going before.
    DATA: model 3.9% | style Prominent (led 8% of runs) | runs in data 7 | last 3: 28 Aug Goodwood 5f Good To Firm 9/9; 13 Sep Doncaster 5f Good 10/10; 16 Oct Newcastle (AW) 5f Standard 4/11 fig 72
    DATA for: Has won at this trip or further
- Kinnalargy (hrs_52772300) | 3yo G | 132lb | OR 72 | draw 8 | jockey M. P. Sheehy | trainer David O'Meara (14d 0/9) | headgear tp (1st time) | last run 22 days | form 574054 | MARKET 7.5% | 09:00 median 10.00 | Matchbook -
    comment: He's yet to win in his last six, but sits on an official 72 and carries 132 lb from draw 8.
    DATA: model 8.9% | style Prominent (led 3% of runs) | runs in data 7 | last 3: 6 Sep York 5.4f Good To Soft 20/21; 12 Oct Newcastle 6f Standard 5/12; 26 Oct Southwell (AW) 6f Standard 4/8 fig 76
    DATA for: Best recent form figure 76, 7 lb above field average; Recent figures 4 lb above its current mark (looks well handicapped); First-time headgear
    DATA against: Trainer 0 wins from 9 runs, last 14 days
- Binadham (hrs_40918850) | 4yo G | 135lb | OR 75 | draw 4 | jockey Tom Eaves | trainer Jonathan Portman (14d 2/12) | headgear p | last run 174 days | form -63323 | MARKET 7.1% | 09:00 median 10.50 | Matchbook -
    comment: Binadham arrives with a consistent profile, finishing third last time out, second two starts back, and third three and four starts back, and he has run over today's trip and going before.
    DATA: model 11.2% | style Midfield (led 4% of runs) | runs in data 5 | last 3: 21 Apr Wolverhampton 5.1f Standard 3/7; 29 Apr Bath 5f Firm 2/6; 27 May Hamilton 5f Good To Firm 3/6
    DATA for: Good recent finishing positions
    DATA against: Returns from a 174-day break
- Beaumadier (hrs_29748383) | 6yo G | 134lb | OR 74 | draw 1 | jockey Hope Regan(7) | trainer Mark Loughnane (14d 1/6) | headgear - | last run 28 days | form 325581 | MARKET 6.9% | 09:00 median 11.00 | Matchbook -
    comment: Beaumadier won last time out and has run over today's trip and going, but that came after an eighth and two fifths, and 134 lb off an official 74 looks a stiff ask.
    DATA: model 9.7% | style Leader (led 29% of runs) | runs in data 15 | last 3: 27 Jul Windsor 5.1f Good To Firm 5/11; 17 Aug Catterick 5f Good 8/11; 20 Oct Newcastle (AW) 5f Standard 1/13 fig 74
    DATA for: Best recent form figure 74, 5 lb above field average; Has won at this trip or further; Course: front-runners have won 1.3× their fair share at 5f here
    DATA against: Pace: likely to be taken on for the lead
- Jax Edge (hrs_30850463) | 6yo M | 134lb | OR 74 | draw 13 | jockey Charlie Tucker(7) | trainer Christopher Mason (14d 0/0) | headgear - | last run 29 days | form 782367 | MARKET 5.2% | 09:00 median 15.00 | Matchbook -
    comment: Jax Edge is yet to win in her last six starts, though a third three starts back and a second four starts back show she can get involved, and she has run over today's trip and going.
    DATA: model 6.3% | style Leader (led 38% of runs) | runs in data 10 | last 3: 8 Sep Goodwood 5f Soft 3/6; 29 Sep Bath 5f Good To Firm 6/12; 19 Oct Wolverhampton (AW) 6f Standard 7/12 fig 72
    DATA for: Has won at this trip or further; Course: front-runners have won 1.3× their fair share at 5f here
    DATA against: Pace: likely to be taken on for the lead
- Brazilian Belle (hrs_41152944) | 4yo F | 128lb | OR 68 | draw 7 | jockey Rhys Elliott(5) | trainer Michael Dods (14d 0/7) | headgear - | last run 38 days | form 116057 | MARKET 3.7% | 09:00 median 21.00 | Matchbook -
    comment: Brazilian Belle won five and six starts back but has finished seventh, fifth, unplaced and sixth since, and she's had 38 days off.
    DATA: model 3.1% | style Midfield (led 4% of runs) | runs in data 7 | last 3: 16 May Thirsk 5f Good 16/17; 22 Sep Southwell 5f Standard 5/7; 10 Oct Southwell 5f Standard 7/7
    DATA for: Has won at this trip or further
- Anaisa (hrs_51866311) | 3yo F | 132lb | OR 72 | draw 14 | jockey Jake Dickson(5) | trainer Tim Easterby (14d 2/22) | headgear t | last run 22 days | form 073408 | MARKET 3.3% | 09:00 median 23.00 | Matchbook -
    comment: The risk is form that has tailed off, with an eighth last time out.
    DATA: model 4.1% | style Held up (led 4% of runs) | runs in data 10 | last 3: 15 Sep Redcar 6f Good 4/14; 30 Sep Musselburgh 5f Good To Soft 11/12; 26 Oct Southwell (AW) 6f Standard 8/10 fig 60
    DATA for: Pace: a contested lead should suit its hold-up style
    DATA against: Best recent form figure 60, 9 lb below field average; Recent figures 12 lb below its current mark (looks high in the weights); Course: hold-up horses have won 0.6× their fair share at 5f here
- Dark Kestrel (hrs_31492755) | 6yo G | 128lb | OR 68 | draw 6 | jockey Ethan Tindall(5) | trainer Antony Brittain (14d 1/3) | headgear tv | last run 119 days | form 467386 | MARKET 3.2% | 09:00 median 25.00 | Matchbook -
    comment: Dark Kestrel is winless in his last six, finishing sixth last time out and eighth the run before, and he returns after 119 days off, so he is hard to fancy. In his favour, he has run over today's trip and going, and a third three starts back is his best recent effort.
    DATA: model 3.3% | style Held up (led 4% of runs) | runs in data 13 | last 3: 15 Jun Wetherby 5.5f Good To Firm 3/9; 6 Jul Wolverhampton 6.1f Standard 8/11; 21 Jul Nottingham 6.1f Good To Firm 6/8
    DATA for: Has won at this trip or further; Pace: a contested lead should suit its hold-up style
    DATA against: Returns from a 119-day break; Course: hold-up horses have won 0.6× their fair share at 5f here
- Opal Storm (hrs_35895818) | 6yo M | 125lb | OR 65 | draw 10 | jockey Faye McManoman | trainer Brian Rothwell (14d 0/1) | headgear tp | last run 28 days | form 615718 | MARKET 3.1% | 09:00 median 21.00 | Matchbook -
    comment: Opal Storm was beaten into eighth last time out and has finished fifth or worse in four of her last six, which makes her hard to fancy, though she won two starts back and five starts back and has run over today's trip and going.
    DATA: model 4.9% | style Held up (led 8% of runs) | runs in data 15 | last 3: 3 Oct Southwell 5f Standard 7/10; 10 Oct Southwell 5f Standard 1/7; 20 Oct Newcastle (AW) 5f Standard 8/13 fig 58
    DATA for: Has won at this trip or further; Carries 6 lb less than average; Pace: a contested lead should suit its hold-up style
    DATA against: Best recent form figure 58, 11 lb below field average; Recent figures 7 lb below its current mark (looks high in the weights); Official rating 65, 6 lb below field average; Course: hold-up horses have won 0.6× their fair share at 5f here

## 5:00 Southwell (AW) | race_id rac_32304655903 | AW Trials Day - Lingfield 2nd Jan 2027 Nursery Handicap Stakes (Rider Restricted Race)
Flat | Class 4 | 4f214y | going Standard | AW | 5 runners | rating band 0-85 | age 2yo
DATA pace: Even - Two likely leaders (Urumita, Bladey Lady). A fair, even gallop is most likely.
- Urumita (hrs_17391345699) | 2yo F | 130lb | OR 77 | draw 4 | jockey Ross Coakley | trainer Richard Hannon (14d 1/12) | headgear - | last run 40 days | form 4521 | MARKET 27.3% | 09:00 median 3.20 | Matchbook - | CHECK (skip line 3.04)
    comment: Urumita arrives a last-time-out winner, with a second two starts back, and has run over today's trip and going, but 40 days off and a 130 lb burden from draw four are hurdles.
    DATA: model 22.5% | style Leader (led 54% of runs) | runs in data 4 | last 3: 14 Sep Windsor 5.1f Good To Soft 5/10; 29 Sep Wolverhampton 6.1f Standard 2/7; 8 Oct Bath 5f Good 1/7
    DATA for: Has won at this trip or further; Good recent finishing positions; Course: front-runners have won 1.3× their fair share at 5f here
- Dowman (hrs_63323687) | 2yo G | 127lb | OR 74 | draw 1 | jockey M. P. Sheehy | trainer George Boughey (14d 0/5) | headgear t | last run 29 days | form 212523 | MARKET 25.4% | 09:00 median 3.25 | Matchbook 4.50
    comment: A 29-day break is no concern, though he has only the one win in that spell.
    DATA: model 13.2% | style Midfield (led 8% of runs) | runs in data 7 | last 3: 29 Aug Chepstow 5.1f Good To Soft 5/6; 12 Sep Bath 5f Good 2/10; 19 Oct Southwell (AW) 6f Standard 3/13 fig 75
    DATA for: Has won at this trip or further; Good recent finishing positions
- Roxa Love (hrs_65190615) | 2yo F | 132lb | OR 79 | draw 3 | jockey Laura Pearson | trainer Kevin Philippart de Foy (14d 0/2) | headgear - | last run 40 days | form 3113 | MARKET 17.2% | 09:00 median 5.00 | Matchbook 5.70
    comment: Roxa Love arrives in cracking nick, third last time out after back-to-back wins with a third either side, and she has run over today's trip and going before. The one concern is a 40-day absence, plus 132 lb to carry from stall three.
    DATA: model 30.6% | style Prominent (led 29% of runs) | runs in data 4 | last 3: 22 Jun Brighton 5.3f Good To Firm 1/5; 7 Sep Wolverhampton 5.1f Standard 1/7; 8 Oct Southwell 5f Standard 3/7
    DATA for: Has won at this trip or further; Good recent finishing positions
- Bladey Lady (hrs_64555715) | 2yo F | 129lb | OR 76 | draw 5 | jockey Duran Fentiman | trainer Tim Easterby (14d 2/22) | headgear - | last run 10 days | form 118114 | MARKET 15.1% | 09:00 median 6.00 | Matchbook -
    comment: Bladey Lady has won four of her last six, including two starts back and three starts back, and she was a fourth last time out just ten days ago; she has run over today's trip and going. The main risk is a 129 lb burden from draw 5 against an official mark of 76.
    DATA: model 24.3% | style Leader (led 63% of runs) | runs in data 9 | last 3: 30 Sep Catterick 6f Good 1/6; 27 Oct Catterick 6f Soft 1/7 fig 79; 7 Nov Doncaster 6f Good To Soft 4/8 fig 75
    DATA for: Has won at this trip or further; Good recent finishing positions; Course: front-runners have won 1.3× their fair share at 5f here
- Undercover Affair (hrs_64073086) | 2yo G | 135lb | OR 82 | draw 2 | jockey Tom Eaves | trainer David Evans (14d 0/8) | headgear - | last run 24 days | form 185701 | MARKET 14.8% | 09:00 median 6.00 | Matchbook -
    comment: The risk is a patchy middle spell of a seventh, a fifth and an eighth, so consistency remains the question.
    DATA: model 9.4% | style Held up (led 4% of runs) | runs in data 14 | last 3: 28 Aug Sandown 5f Good 7/8; 1 Oct Nottingham 6.1f Good 10/10; 24 Oct Southwell (AW) 5f Standard 1/4 fig 75
    DATA for: Has won at this trip or further
    DATA against: Recent figures 7 lb below its current mark (looks high in the weights); Trainer 0 wins from 8 runs, last 14 days; Course: hold-up horses have won 0.6× their fair share at 5f here

## 5:30 Southwell (AW) | race_id rac_32304657840 | Make The Move To Midnite Handicap Stakes (Rider Restricted Race) (GBBPlus Race)
Flat | Class 4 | 1m4f14y | going Standard | AW | 13 runners | rating band 0-85 | age 3yo+
DATA pace: Strong pace - 4 habitual front-runners (Redbud Sixteen, Yaa Min, Gloryous, Optician). A contested lead should set things up for horses coming from behind.
- Almekarem (hrs_53359579) | 4yo G | 141lb | OR 84 | draw 8 | jockey Rhys Clutterbuck | trainer Sir Mark Prescott Bt (14d 0/4) | headgear - | last run 20 days | form 221073 | MARKET 18.8% | 09:00 median 4.00 | Matchbook 5.30 | CHECK (skip line 3.80)
    comment: Almekarem arrives fresh from a third last time out, 20 days ago, and has run over today's trip and on this going, while a winner four starts back keeps him firmly in the picture. The risk is a seventh two starts back, so consistency off 141 lb is the question.
    DATA: model 10.0% | style Held up (led 5% of runs) | runs in data 8 | last 3: 19 Sep Newbury 10f Good To Firm 10/11; 10 Oct York 10.3f Good To Soft 7/19; 28 Oct Kempton (AW) 12f Standard / Slow 3/10 fig 83
    DATA for: Best recent form figure 83, 7 lb above field average; Pace: a contested lead should suit its hold-up style
- Fahidi (hrs_55091897) | 3yo G | 131lb | OR 79 | draw 12 | jockey Charlie Tucker(7) | trainer Andrew Balding (14d 1/17) | headgear - | last run 21 days | form 3-4051 | MARKET 17.9% | 09:00 median 4.33 | Matchbook -
    comment: Carrying 131 lb off an official mark of 79, he follows a fifth two starts back, and a modest speed figure of 72 limits his appeal.
    DATA: model 9.7% | style Held up (led 5% of runs) | runs in data 4 | last 3: 23 May Salisbury 9.9f Good 11/12; 5 Oct Kempton 11f Standard To Slow 5/9; 27 Oct Wolverhampton (AW) 12f Standard 1/10 fig 76
    DATA for: Has won at this trip or further; Carries 5 lb less than average; Pace: a contested lead should suit its hold-up style
- Ashnak (hrs_45475682) | 4yo G | 140lb | OR 83 | draw 2 | jockey M. P. Sheehy | trainer David O'Meara (14d 0/9) | headgear t | last run 20 days | form 278435 | MARKET 10.3% | 09:00 median 7.50 | Matchbook 9.00
    comment: Ashnak arrives fit after a 20-day break, having finished fifth last time out, with a third two starts back and a second six starts back showing he can get involved.
    DATA: model 12.6% | style Held up (led 3% of runs) | runs in data 9 | last 3: 17 Sep Ayr 13.1f Soft 4/11; 10 Oct York 10.3f Good To Soft 3/19; 28 Oct Nottingham 14f Soft 5/13 fig 81
    DATA for: Best recent form figure 81, 5 lb above field average; Last-run finishing speed +2.4% vs that field (finished strongly); Pace: a contested lead should suit its hold-up style
    DATA against: Trainer 0 wins from 9 runs, last 14 days
- Redbud Sixteen (hrs_54875415) | 4yo F | 142lb | OR 85 | draw 10 | jockey Kieren Fox | trainer Charlie Pike (14d 1/2) | headgear - | last run 60 days | form 811724 | MARKET 10.0% | 09:00 median 8.00 | Matchbook -
    comment: Redbud Sixteen booked a second two starts back and a fourth last time out, and she has won twice in her last six, with a win four starts back and another five back. She has run over today's trip and going, but 60 days off is the one risk, and 142 lb is no small burden.
    DATA: model 9.6% | style Leader (led 57% of runs) | runs in data 6 | last 3: 3 Jul Doncaster 10.2f Good To Firm 7/8; 3 Sep Salisbury 9.9f Good To Soft 2/7; 18 Sep Newbury 12f Good 4/8
    DATA for: Official rating 85, 5 lb above field average
    DATA against: Carries 6 lb more than average; Pace: likely to be taken on for the lead
- Without Compromise (hrs_47807319) | 5yo G | 135lb | OR 78 | draw 7 | jockey Harry Russell | trainer Antony Brittain (14d 1/3) | headgear tp | last run 12 days | form 826741 | MARKET 8.9% | 09:00 median 8.50 | Matchbook -
    comment: Fresh from a win last time out just 12 days ago, he has run over today's trip and going, but a fourth and a seventh in the two runs before that show inconsistency.
    DATA: model 6.9% | style Midfield (led 4% of runs) | runs in data 8 | last 3: 11 Sep Doncaster 10.2f Good 7/17; 6 Oct Southwell 12.1f Standard 4/6; 5 Nov Southwell (AW) 12f Standard 1/9 fig 81
    DATA for: Best recent form figure 81, 5 lb above field average; Has won at this trip or further
- Aravalli (hrs_57718017) | 3yo F | 131lb | OR 79 | draw 1 | jockey Taylor Fisher | trainer Joe Tickle (14d 0/2) | headgear - | last run 25 days | form 113708 | MARKET 6.6% | 09:00 median 12.00 | Matchbook -
    comment: Aravalli has slipped to an eighth last time out and unplaced the run before, a long way from back-to-back wins five and six starts back.
    DATA: model 1.4% | style Midfield (led 3% of runs) | runs in data 12 | last 3: 14 Sep Windsor 11.4f Good To Soft 7/9; 8 Oct Bath 14f Good 12/12; 23 Oct Wolverhampton (AW) 9.5f Standard 8/12 fig 75
    DATA for: Has won at this trip or further; Carries 5 lb less than average
    DATA against: Poor recent finishing positions
- Gloryous (hrs_40919431) | 4yo F | 140lb | OR 83 | draw 5 | jockey William Carver | trainer Jamie Osborne (14d 0/0) | headgear - | last run 60 days | form 832122 | MARKET 6.2% | 09:00 median 12.50 | Matchbook -
    comment: Gloryous has been consistent, finishing second last time out and a second two starts back, with a winner three starts back, and she has run over today's trip and on this going before.
    DATA: model 16.5% | style Leader (led 57% of runs) | runs in data 6 | last 3: 26 Aug Kempton 12f Standard To Slow 1/8; 30 Aug Goodwood 11.2f Soft 2/6; 18 Sep Newbury 12f Good 2/8
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Pace: likely to be taken on for the lead
- Yaa Min (hrs_46515455) | 4yo G | 141lb | OR 84 | draw 4 | jockey Liam Wright(3) | trainer Hayley Burton (14d 0/1) | headgear - | last run 32 days | form 334915 | MARKET 5.8% | 09:00 median 13.00 | Matchbook 16.50
    comment: Yaa Min was a fifth last time out, and a winner two starts back, which gives him a solid recent profile, and he has run over today's trip and going before.
    DATA: model 10.4% | style Leader (led 57% of runs) | runs in data 11 | last 3: 31 Aug Epsom Downs 12f Good To Soft 9/14; 26 Sep Haydock 14f Heavy 1/9; 16 Oct Haydock 14f Heavy 5/5 fig 70
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 70, 6 lb below field average; Recent figures 14 lb below its current mark (looks high in the weights); Pace: likely to be taken on for the lead
- Charlie's Choice (hrs_34775195) | 6yo G | 129lb | OR 72 | draw 6 | jockey Jack Dace(5) | trainer David Simcock (14d 0/5) | headgear - | last run 21 days | form 704487 | MARKET 5.7% | 09:00 median 12.00 | Matchbook 20.00
    comment: Charlie's Choice is hard to fancy, beaten into seventh last time out and an eighth two starts back, and he is yet to win in his last six outings. He has run over today's trip and going and is fit enough after 21 days, but 129 lb is a big ask.
    DATA: model 2.8% | style Held up (led 3% of runs) | runs in data 14 | last 3: 18 Jun Yarmouth 10.1f Good To Firm 4/6; 14 Oct Kempton (AW) 11f Standard / Slow 8/13 fig 71; 27 Oct Wolverhampton (AW) 12f Standard 7/10 fig 67
    DATA for: Has won at this trip or further; Carries 7 lb less than average; Pace: a contested lead should suit its hold-up style
    DATA against: Best recent form figure 71, 5 lb below field average; Official rating 72, 8 lb below field average
- Optician (hrs_29917909) | 6yo G | 134lb | OR 77 | draw 9 | jockey Tom Eaves | trainer Michael Herrington (14d 0/6) | headgear p | last run 12 days | form 932014 | MARKET 3.2% | 09:00 median 26.00 | Matchbook -
    comment: Fourth last time out, twelve days ago, and a winner two starts back, Optician is in decent order and has run over today's trip and going before.
    DATA: model 8.2% | style Leader (led 43% of runs) | runs in data 11 | last 3: 10 Oct York 10.3f Good To Soft 15/19; 22 Oct Southwell (AW) 11f Standard 1/11 fig 74; 5 Nov Southwell (AW) 12f Standard 4/9 fig 77
    DATA for: Has won at this trip or further
    DATA against: Pace: likely to be taken on for the lead
- First Ambition (hrs_46169627) | 5yo G | 136lb | OR 79 | draw 11 | jockey Dougie Costello | trainer Steph Hollinshead (14d 0/4) | headgear h (1st time) | last run 25 days | form 663035 | MARKET 2.7% | 09:00 median 23.00 | Matchbook 55.00
    comment: First Ambition arrives fit enough after 25 days, with a fifth last time out and a third two starts back, and he has run on today's going before.
    DATA: model 5.2% | style Midfield (led 4% of runs) | runs in data 9 | last 3: 26 Sep Newmarket 9f Good To Firm 27/27; 16 Oct Newcastle (AW) 8f Standard 3/5 fig 75; 23 Oct Wolverhampton (AW) 9.5f Standard 5/12 fig 77
    DATA for: First-time headgear
- Skipper (hrs_36234506) | 5yo G | 143lb | OR 86 | draw 13 | jockey Donagh Murphy(5) | trainer Barry Brennan (14d 0/1) | headgear - | last run 75 days | form -10966 | MARKET 2.4% | 09:00 median 34.00 | Matchbook -
    comment: The risk is a poor recent run of sixth, sixth and ninth, plus 75 days off.
    DATA: model 5.1% | style Prominent (led 4% of runs) | runs in data 5 | last 3: 25 May Windsor 8.1f Good To Firm 9/10; 16 Aug Southwell 7.1f Standard 6/13; 3 Sep Salisbury 8f Good To Soft 6/11
    DATA for: Official rating 86, 6 lb above field average; Last-run finishing speed +2.0% vs that field (finished strongly)
    DATA against: Poor recent finishing positions; Carries 7 lb more than average
- Enziya (hrs_46265366) | 4yo G | 127lb | OR 70 | draw 3 | jockey Tyler Heard | trainer Kevin Pickard (14d 0/1) | headgear tp | wind surgery | last run 12 days | form 5721-5 | MARKET 1.5% | 09:00 median 51.00 | Matchbook -
    comment: In his favour, he has run over today's trip and going before and was second three starts back.
    DATA: model 1.5% | style Held up (led 4% of runs) | runs in data 3 | last 3: 17 Jan Ascot 15.7f Soft 8/10; 18 Sep Newton Abbot 16.8f Good PU/11; 5 Nov Chelmsford (AW) 16f Standard 5/6 fig 66
    DATA for: Carries 9 lb less than average; Pace: a contested lead should suit its hold-up style
    DATA against: Best recent form figure 66, 10 lb below field average; Official rating 70, 10 lb below field average

## 6:00 Southwell (AW) | race_id rac_32304659777 | AWC Season 14 Has Begun Fillies' Novice Stakes (Rider Restricted Race) (GBB/GBBPlus Race)
Flat | Class 3 | 1m4f14y | going Standard | AW | 10 runners | rating band - | age 3yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Danseuse (hrs_64812951) | 3yo F | 128lb | OR - | draw 9 | jockey Ross Coakley | trainer Simon & Ed Crisford (14d 0/4) | headgear - | last run 182 days | form 3 | MARKET 23.1% | 09:00 median 3.50 | Matchbook 3.50 | CHECK (skip line 3.32)
    DATA: model 7.8% | style Unknown | runs in data 1 | last 3: 19 May Newcastle 12.4f Standard 3/6
    DATA against: Returns from a 182-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Bintnaseefa (hrs_63742119) | 3yo F | 128lb | OR - | draw 10 | jockey Millie Wonnacott(5) | trainer Harry Charlton (14d 2/2) | headgear - | last run 22 days | form 04 | MARKET 16.9% | 09:00 median 5.00 | Matchbook -
    DATA: model 3.5% | style Midfield (led 5% of runs) | runs in data 2 | last 3: 17 Apr Newbury 10f Good 13/14; 26 Oct Kempton (AW) 12f Standard / Slow 4/9 fig 57
    DATA against: Best recent form figure 57, 6 lb below field average; Lightly raced: 2 runs in our data, so the model has little to go on
- Allaire (hrs_59645460) | 3yo F | 128lb | OR 72 | draw 2 | jockey William Carver | trainer Andrew Balding (14d 1/17) | headgear - | last run 22 days | form -26332 | MARKET 14.1% | 09:00 median 5.50 | Matchbook 7.20
    DATA: model 17.6% | style Prominent (led 8% of runs) | runs in data 5 | last 3: 21 Sep Leicester 10f Good 3/7; 5 Oct Kempton 12f Standard To Slow 3/7; 26 Oct Kempton (AW) 12f Standard / Slow 2/9 fig 58
    DATA for: Official rating 72, 6 lb above field average; Good recent finishing positions
    DATA against: Best recent form figure 58, 5 lb below field average
- Don't Hurry Love (hrs_55634285) | 3yo F | 128lb | OR - | draw 8 | jockey Luke Catton(3) | trainer John & Thady Gosden (14d 3/12) | headgear - | last run 466 days | form 6- | MARKET 13.8% | 09:00 median 6.00 | Matchbook -
    DATA: model 5.6% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 25% wins (3/12), last 14 days
    DATA against: Returns from a 466-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Maneater (hrs_46975159) | 4yo F | 133lb | OR 75 | draw 7 | jockey Ryan Sexton | trainer Richard Spencer (14d 0/2) | headgear - | last run 11 days | form 23-2 | MARKET 12.1% | 09:00 median 7.00 | Matchbook -
    DATA: model 31.9% | style Held up (led 8% of runs) | runs in data 1 | last 3: 6 Nov Newcastle (AW) 10f Standard 2/7 fig 69
    DATA for: Best recent form figure 69, 6 lb above field average; Official rating 75, 10 lb above field average; Last-run finishing speed +4.2% vs that field (finished strongly)
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Seacole (hrs_65451652) | 3yo F | 128lb | OR 70 | draw 6 | jockey Rhys Clutterbuck | trainer Ralph Beckett (14d 0/8) | headgear b (1st time) | last run 31 days | form 427323 | MARKET 8.4% | 09:00 median 9.50 | Matchbook 12.00
    DATA: model 15.1% | style Midfield (led 5% of runs) | runs in data 7 | last 3: 14 Sep Windsor 11.4f Good To Soft 3/7; 27 Sep Epsom Downs 10.1f Good 2/6; 17 Oct Southwell (AW) 11f Standard 3/6 fig 68
    DATA for: Best recent form figure 68, 5 lb above field average; Good recent finishing positions; First-time headgear
    DATA against: Trainer 0 wins from 8 runs, last 14 days
- Saaffya (hrs_17391432268) | 3yo F | 128lb | OR - | draw 4 | jockey George Downing | trainer Ed Walker (14d 1/13) | headgear - | last run 41 days | form 54 | MARKET 6.4% | 09:00 median 13.00 | Matchbook -
    DATA: model 3.3% | style Held up (led 8% of runs) | runs in data 2 | last 3: 7 Sep Windsor 10f Good 5/7; 7 Oct Kempton 11f Standard To Slow 4/8
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Triumph (hrs_63908677) | 3yo F | 128lb | OR - | draw 3 | jockey M. P. Sheehy | trainer Charlie Johnston (14d 2/7) | headgear - | last run 178 days | form 38 | MARKET 1.9% | 09:00 median 51.00 | Matchbook -
    DATA: model 3.2% | style Prominent (led 38% of runs) | runs in data 2 | last 3: 25 Apr Ripon 9.8f Good 3/5; 23 May Goodwood 9.9f Good 8/8
    DATA for: Trainer 29% wins (2/7), last 14 days
    DATA against: Last-run finishing speed -4.0% vs that field (faded); Returns from a 178-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- Sparkling Water (hrs_51124234) | 5yo M | 133lb | OR - | draw 1 | jockey Taylor Fisher | trainer Joe Tickle (14d 0/2) | headgear - | last run 90 days | form - | MARKET 1.9% | 09:00 median 41.00 | Matchbook -
    DATA: model 11.1% | style Midfield (led 3% of runs) | runs in data 4 | last 3: 20 Feb Warwick 16f Soft 2/8; 24 Jul Uttoxeter 15.8f Good 1/12; 19 Aug Worcester 16f Good 9/14
    DATA for: Good recent finishing positions
    DATA against: Returns from a 90-day break
- Pure Theory (hrs_43507429) | 4yo F | 133lb | OR 45 | draw 5 | jockey Oliver Carmichael(7) | trainer Stephanie Cassidy (14d 0/0) | headgear p | last run 68 days | form 005672 | MARKET 1.4% | 09:00 median 67.00 | Matchbook -
    DATA: model 1.0% | style Midfield (led 29% of runs) | runs in data 11 | last 3: 28 Jul Yarmouth 10.1f Good To Firm 6/6; 15 Aug Lingfield 10f Standard 7/8; 10 Sep Lingfield 12f Standard 2/9
    DATA for: Last-run finishing speed +3.0% vs that field (finished strongly)
    DATA against: Official rating 45, 20 lb below field average

## 6:30 Southwell (AW) | race_id rac_32304661714 | AWC Finals Day At Newcastle 26th March Handicap Stakes (Rider Restricted Race)
Flat | Class 4 | 1m13y | going Standard | AW | 13 runners | rating band 0-85 | age 3yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Moving Shadow (hrs_55882449) | 3yo G | 134lb | OR 84 | draw 13 | jockey Dougie Costello | trainer K. R. Burke (14d 0/10) | headgear - | last run 56 days | form 17-32 | MARKET 18.7% | 09:00 median 4.00 | Matchbook - | CHECK (skip line 3.80)
    comment: The main risk is a 56-day absence, plus 134 lb from draw 13.
    DATA: model 14.1% | style Midfield (led 8% of runs) | runs in data 2 | last 3: 29 Jul Leicester 7f Good To Firm 3/4; 22 Sep Southwell 8.1f Standard 2/9
    DATA for: Last-run finishing speed +3.1% vs that field (finished strongly); Good recent finishing positions
    DATA against: Trainer 0 wins from 10 runs, last 14 days; Lightly raced: 2 runs in our data, so the model has little to go on
- Anthropologist (hrs_40433974) | 4yo G | 137lb | OR 85 | draw 6 | jockey Ryan Sexton | trainer Michael Herrington (14d 0/6) | headgear p | last run 19 days | form 328411 | MARKET 14.9% | 09:00 median 5.00 | Matchbook -
    DATA: model 21.4% | style Held up (led 4% of runs) | runs in data 15 | last 3: 25 Sep Newcastle 7.1f Standard 4/11; 24 Oct Southwell (AW) 7f Standard 1/14 fig 86; 29 Oct Southwell (AW) 8f Standard 1/13 fig 73
    DATA for: Best recent form figure 86, 5 lb above field average; Has won at this trip or further; Good recent finishing positions
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Tex (hrs_44785916) | 5yo G | 130lb | OR 78 | draw 3 | jockey Jack Dace(5) | trainer George Baker (14d 1/9) | headgear tp | last run 17 days | form 192183 | MARKET 12.1% | 09:00 median 6.50 | Matchbook -
    comment: Tex was third last time out and has two wins in his last six, including a winner three starts back, but an eighth two starts back shows his consistency wobbles.
    DATA: model 9.3% | style Held up (led 5% of runs) | runs in data 9 | last 3: 4 Sep Ascot 8f Good 1/11; 2 Oct Ascot 7f Good To Firm 8/18; 31 Oct Newmarket 7f Good To Soft 3/16 fig 87
    DATA for: Best recent form figure 87, 6 lb above field average; Recent figures 9 lb above its current mark (looks well handicapped); Has won at this trip or further; Good recent finishing positions
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Raging Raj (hrs_51491517) | 3yo G | 135lb | OR 85 | draw 4 | jockey Tom Eaves | trainer Michael Herrington (14d 0/6) | headgear - | last run 19 days | form 512608 | MARKET 9.5% | 09:00 median 8.00 | Matchbook -
    comment: Raging Raj has tailed off since a second four starts back and a win five starts back, with an eighth last time out and a sixth three starts back, though he's fresh enough after 19 days and has run over today's trip and going.
    DATA: model 6.9% | style Held up (led 5% of runs) | runs in data 10 | last 3: 13 Sep Doncaster 7f Good 6/14; 13 Oct Leicester 7f Good To Soft 16/17; 29 Oct Southwell (AW) 7f Standard 8/14 fig 82
    DATA against: Poor recent finishing positions; Pace: steady gallop likely, hard to come from off the pace
- Zryan (hrs_35812490) | 5yo G | 136lb | OR 84 | draw 5 | jockey M. P. Sheehy | trainer David O'Meara (14d 0/9) | headgear - | last run 186 days | form 126090 | MARKET 8.0% | 09:00 median 9.50 | Matchbook -
    comment: The main risk is a 186-day absence and a slide through his last three runs, so fitness is the question.
    DATA: model 3.2% | style Midfield (led 4% of runs) | runs in data 7 | last 3: 3 Apr Newcastle 10.2f Standard 11/14; 2 May Newmarket 8f Good To Firm 9/13; 15 May York 10.3f Good 11/15
    DATA for: Has won at this trip or further
    DATA against: Trainer 0 wins from 9 runs, last 14 days; Poor recent finishing positions; Returns from a 186-day break
- Jimmy Speaking (hrs_35553322) | 5yo G | 136lb | OR 84 | draw 11 | jockey Jake Dickson(5) | trainer Chris Dwyer (14d 0/2) | headgear - | last run 55 days | form 944827 | MARKET 7.6% | 09:00 median 10.00 | Matchbook -
    comment: The risk is a seventh last time out and a 55-day absence, with 136 lb to carry from stall 11.
    DATA: model 7.3% | style Midfield (led 8% of runs) | runs in data 9 | last 3: 21 Aug York 11.9f Good To Soft 8/16; 16 Sep Yarmouth 9.1f Good To Soft 2/11; 23 Sep Goodwood 8f Good 7/7
    DATA against: Last-run finishing speed -5.1% vs that field (faded)
- BillyB (hrs_26509693) | 7yo G | 134lb | OR 82 | draw 2 | jockey Barry McHugh | trainer Craig Lidster (14d 0/2) | headgear p | last run 40 days | form 707420 | MARKET 7.6% | 09:00 median 10.00 | Matchbook -
    comment: BillyB was second two starts back but unplaced last time out, and he returns after 40 days having run over today's trip and going.
    DATA: model 6.5% | style Prominent (led 29% of runs) | runs in data 7 | last 3: 17 Jul Pontefract 8f Good To Firm 4/6; 17 Sep Pontefract 8f Good 2/10; 8 Oct Southwell 7.1f Standard 10/12
    DATA against: Last-run finishing speed -3.2% vs that field (faded)
- Silent City (hrs_53476080) | 4yo F | 131lb | OR 79 | draw 8 | jockey Ross Coakley | trainer Roger Varian (14d 2/6) | headgear - | last run 26 days | form 2-3658 | MARKET 5.3% | 09:00 median 13.00 | Matchbook -
    comment: Silent City is hard to fancy, beaten into eighth last time out and a sixth three starts back, so she is yet to win in her last five outings. A second five starts back and a third four starts back show some ability, and she has run over today's trip, but 131 lb from draw 8 is a big ask.
    DATA: model 6.6% | style Midfield (led 29% of runs) | runs in data 4 | last 3: 13 Jul Windsor 10f Good To Firm 6/7; 30 Sep Kempton 8f Standard To Slow 5/13; 22 Oct Newmarket 8f Soft 8/15 fig 73
    DATA for: Trainer 33% wins (2/6), last 14 days
    DATA against: Best recent form figure 73, 8 lb below field average; Recent figures 6 lb below its current mark (looks high in the weights)
- Hale End (hrs_29987811) | 6yo G | 131lb | OR 79 | draw 14 | jockey Rhys Elliott(5) | trainer Michael Dods (14d 0/7) | headgear p | last run 22 days | form 142703 | MARKET 4.5% | 09:00 median 17.00 | Matchbook -
    comment: Hale End was third last time out and has been in the frame before, with a second four starts back, though he has just one win in his last six and was unplaced two runs ago.
    DATA: model 3.6% | style Held up (led 3% of runs) | runs in data 13 | last 3: 17 Sep Pontefract 8f Good 7/10; 10 Oct York 7.9f Soft 11/20; 26 Oct Redcar 8f Heavy 3/10 fig 84
    DATA for: Recent figures 5 lb above its current mark (looks well handicapped); Has won at this trip or further
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Down To The Kid (hrs_25908813) | 7yo G | 136lb | OR 84 | draw 7 | jockey Jonny Peate | trainer Michael Herrington (14d 0/6) | headgear - | wind surgery | last run 19 days | form 312260 | MARKET 3.9% | 09:00 median 20.00 | Matchbook -
    comment: Down To The Kid was beaten last time out and a sixth two starts back, but he was second three and four starts back and won five starts back, and he has run over today's trip and going.
    DATA: model 6.0% | style Prominent (led 3% of runs) | runs in data 8 | last 3: 9 Apr Southwell 8.1f Standard 2/6; 25 Apr Southwell 7.1f Standard 6/9; 29 Oct Southwell (AW) 7f Standard 12/14 fig 69
    DATA against: Best recent form figure 69, 12 lb below field average; Recent figures 15 lb below its current mark (looks high in the weights)
- Priapos (hrs_42452536) | 4yo G | 134lb | OR 82 | draw 9 | jockey Oliver Carmichael(7) | trainer Phillip Makin (14d 0/1) | headgear - | last run 32 days | form 005652 | MARKET 3.0% | 09:00 median 26.00 | Matchbook -
    comment: Priapos is winless in his last six, though he did finish second last time out after a run of fifth, sixth and fifth, and he has run over today's trip and going.
    DATA: model 5.1% | style Midfield (led 4% of runs) | runs in data 10 | last 3: 12 Sep Chester 7.6f Soft 6/9; 30 Sep Musselburgh 8.9f Good To Soft 5/6; 16 Oct Newcastle (AW) 8f Standard 2/5 fig 84
    DATA for: Has won at this trip or further
- Vixey (hrs_32076093) | 6yo M | 130lb | OR 78 | draw 1 | jockey Aiden Brookes | trainer Simon West (14d 0/1) | headgear - | last run 56 days | form 203542 | MARKET 2.5% | 09:00 median 29.00 | Matchbook -
    comment: Vixey is winless in her last six, though a second last time out and another second six starts back show she is capable of getting close, and she has run over today's trip and going.
    DATA: model 8.1% | style Midfield (led 23% of runs) | runs in data 7 | last 3: 22 Aug Chester 7.6f Good To Soft 5/13; 12 Sep Chester 7.6f Soft 4/8; 22 Sep Beverley 7.3f Good 2/10
    DATA for: Last-run finishing speed +3.2% vs that field (finished strongly)
- One Smack Mac (hrs_412692826) | 4yo G | 137lb | OR 85 | draw 10 | jockey William Carver | trainer Jamie Osborne (14d 0/0) | headgear t | last run 35 days | form -09000 | MARKET 2.4% | 09:00 median 34.00 | Matchbook -
    comment: A 35-day break and 137 lb from stall 10 are the questions.
    DATA: model 2.0% | style Unknown | runs in data 5 | last 3: 29 Jul Goodwood 7f Good To Firm 18/20; 3 Sep Salisbury 8f Good To Soft 11/11; 13 Oct Leicester 7f Good To Soft 15/17
    DATA against: Poor recent finishing positions

## 7:00 Southwell (AW) | race_id rac_32304989067 | All-Weather Championship Is Back Handicap Stakes (Rider Restricted Race) (Div I)
Flat | Class 5 | 7f14y | going Standard | AW | 11 runners | rating band 0-70 | age 3yo+
DATA pace: Lone leader - Bay Breeze is the only habitual front-runner and may be allowed an easy lead.
- Red Hat Eagle (hrs_32613483) | 6yo G | 137lb | OR 69 | draw 4 | jockey Rhys Clutterbuck | trainer Michael Appleby (14d 1/11) | headgear tp | last run 24 days | form 752352 | MARKET 28.0% | 09:00 median 2.75 | Matchbook -
    DATA: model 22.0% | style Unknown | runs in data 11 | last 3: 14 Sep Thirsk 7f Good 3/12; 9 Oct Kempton 7f Standard To Slow 5/11; 24 Oct Southwell (AW) 7f Standard 2/14 fig 80
    DATA for: Best recent form figure 80, 23 lb above field average; Recent figures 11 lb above its current mark (looks well handicapped); Good recent finishing positions
- Phoenix of Dreams (hrs_38058132) | 5yo G | 136lb | OR 68 | draw 7 | jockey James Sullivan | trainer John & Sean Quinn (14d 0/9) | headgear - | last run 22 days | form 473218 | MARKET 13.6% | 09:00 median 6.00 | Matchbook -
    comment: Beaten in eighth last time out, he showed more before that with a win two starts back and a second three starts back, and he has run over today's trip and going.
    DATA: model 16.6% | style Midfield (led 3% of runs) | runs in data 11 | last 3: 24 Sep Southwell 7.1f Standard 2/9; 9 Oct Kempton 7f Standard To Slow 1/11; 26 Oct Redcar 7f Heavy 8/12 fig 61
    DATA for: Best recent form figure 61, 4 lb above field average; Has won at this trip or further; Good recent finishing positions
    DATA against: Recent figures 7 lb below its current mark (looks high in the weights); Trainer 0 wins from 9 runs, last 14 days
- Flowstate (hrs_42326613) | 5yo G | 138lb | OR 70 | draw 6 | jockey M. P. Sheehy | trainer David O'Meara (14d 0/9) | headgear v | last run 36 days | form 141566 | MARKET 12.4% | 09:00 median 6.50 | Matchbook -
    comment: The risk is back-to-back sixths in his last two outings, after 36 days off.
    DATA: model 13.4% | style Midfield (led 23% of runs) | runs in data 9 | last 3: 3 Sep Southwell 6.1f Standard 5/12; 25 Sep Newcastle 7.1f Standard 6/11; 12 Oct Newcastle 7.1f Standard 6/13
    DATA for: Official rating 70, 5 lb above field average; Has won at this trip or further
    DATA against: Trainer 0 wins from 9 runs, last 14 days; Carries 5 lb more than average
- Bay Breeze (hrs_24846409) | 7yo G | 136lb | OR 68 | draw 5 | jockey Duran Fentiman | trainer Tim Easterby (14d 2/22) | headgear p | last run 13 days | form 311771 | MARKET 10.3% | 09:00 median 8.00 | Matchbook -
    comment: Bay Breeze arrives in good heart, having won last time out and taken three of his last six, though a seventh two starts back and another three starts back show his consistency wavers.
    DATA: model 10.4% | style Prominent (led 43% of runs) | runs in data 12 | last 3: 13 Oct Leicester 6f Good To Soft 7/18; 31 Oct Newmarket 6f Good To Soft 7/10 fig 58; 4 Nov Musselburgh 7f Soft 1/12 fig 69
    DATA for: Best recent form figure 69, 12 lb above field average; Last-run finishing speed +3.0% vs that field (finished strongly); Has won at this trip or further
- Ziggy's Condor (hrs_35336882) | 5yo G | 134lb | OR 66 | draw 8 | jockey Joey Haynes | trainer Adam Kirby (14d 0/8) | headgear - | last run 20 days | form 326008 | MARKET 9.0% | 09:00 median 9.50 | Matchbook -
    DATA: model 3.9% | style Held up (led 5% of runs) | runs in data 16 | last 3: 18 Sep Wolverhampton 7.2f Standard 11/12; 13 Oct Leicester 6f Good To Soft 18/18; 28 Oct Kempton (AW) 7f Standard / Slow 8/13 fig 60
    DATA against: Recent figures 6 lb below its current mark (looks high in the weights); Trainer 0 wins from 8 runs, last 14 days; Poor recent finishing positions
- Packetofbiscuits (hrs_39960368) | 4yo G | 133lb | OR 65 | draw 11 | jockey Tyler Heard | trainer John Mackie (14d 0/5) | headgear b | last run 12 days | form 626075 | MARKET 8.2% | 09:00 median 8.00 | Matchbook 20.00
    comment: Fifth last time out just 12 days ago, he has run over today's trip and going before, but he's winless in his last six and was unplaced three starts back, with a second five starts back his best finish.
    DATA: model 9.3% | style Midfield (led 3% of runs) | runs in data 16 | last 3: 9 Oct York 7f Good To Soft 13/20; 24 Oct Southwell (AW) 7f Standard 7/14 fig 65; 5 Nov Southwell (AW) 8f Standard 5/12 fig 60
    DATA for: Best recent form figure 65, 8 lb above field average; Has won at this trip or further
- Folkene (hrs_51766743) | 4yo F | 130lb | OR 62 | draw 1 | jockey Tom Eaves | trainer Roger Fell (14d 0/1) | headgear - | last run 32 days | form 474880 | MARKET 5.0% | 09:00 median 19.00 | Matchbook -
    comment: Folkene is winless in her last six, with an unplaced effort last time out and a pair of eighths before that, so she is hard to fancy on recent evidence.
    DATA: model 5.4% | style Midfield (led 4% of runs) | runs in data 9 | last 3: 22 Sep Beverley 7.3f Good 8/9; 6 Oct Leicester 7f Good To Firm 8/10; 16 Oct Redcar 7f Good 17/18 fig 22
    DATA against: Best recent form figure 22, 35 lb below field average; Recent figures 40 lb below its current mark (looks high in the weights); Poor recent finishing positions
- Legacy Rock (hrs_54494797) | 3yo G | 132lb | OR 65 | draw 2 | jockey Jack Dace(5) | trainer Luke Dace (14d 0/3) | headgear - | last run 63 days | form 126660 | MARKET 4.4% | 09:00 median 21.00 | Matchbook -
    comment: Legacy Rock won six starts back and was second five starts back, though he has finished sixth in three of his last four outings, and he has run over today's trip and going before.
    DATA: model 6.6% | style Held up (led 5% of runs) | runs in data 9 | last 3: 20 Aug Newmarket 8f Good To Firm 6/7; 31 Aug Southwell 8.1f Standard 6/10; 15 Sep Redcar 8f Good 11/13
    DATA for: Has won at this trip or further
    DATA against: Last-run finishing speed -6.4% vs that field (faded); Poor recent finishing positions
- Coolree (hrs_30469901) | 7yo G | 135lb | OR 67 | draw 3 | jockey Faye McManoman | trainer Sam England (14d 5/23) | headgear t | last run 13 days | form 373160 | MARKET 3.8% | 09:00 median 23.00 | Matchbook -
    comment: Coolree won three starts back and was third four starts back, but he has since been unplaced last time out and sixth two starts back.
    DATA: model 5.2% | style Midfield (led 29% of runs) | runs in data 14 | last 3: 22 Sep Beverley 7.3f Good 1/10; 16 Oct Newcastle (AW) 8f Standard 6/9 fig 61; 4 Nov Nottingham 8.5f Soft 14/14 fig 42
    DATA for: Best recent form figure 61, 4 lb above field average; Trainer 22% wins (5/23), last 14 days; Has won at this trip or further
    DATA against: Recent figures 6 lb below its current mark (looks high in the weights); Last-run finishing speed -3.8% vs that field (faded)
- Whatever Bruce (hrs_65678291) | 3yo G | 129lb | OR 62 | draw 10 | jockey William Pyle | trainer Gemma Tutty (14d 1/7) | headgear - | last run 34 days | form 6650 | MARKET 2.8% | 09:00 median 34.00 | Matchbook -
    comment: Whatever Bruce is hard to fancy, unplaced last time out after a fifth two starts back and a pair of sixths, and he is winless in his last four.
    DATA: model 2.9% | style Held up (led 4% of runs) | runs in data 4 | last 3: 5 Sep Newcastle 7.1f Standard 6/9; 25 Sep Newcastle 6f Standard 5/5; 14 Oct Nottingham 8.5f Good To Soft 10/10 fig 44
    DATA against: Best recent form figure 44, 13 lb below field average; Recent figures 18 lb below its current mark (looks high in the weights); Last-run finishing speed -2.2% vs that field (faded)
- Yaahobby (hrs_24735053) | 7yo G | 119lb | OR 48 | draw 9 | jockey Ethan Tindall(5) | trainer Antony Brittain (14d 1/3) | headgear t | last run 15 days | form 491394 | MARKET 2.4% | 09:00 median 41.00 | Matchbook -
    comment: Fourth last time out and a winner four starts back, but a ninth two starts back and another ninth five starts back show the inconsistency, and he has been beaten in most of his recent runs.
    DATA: model 4.1% | style Held up (led 4% of runs) | runs in data 11 | last 3: 25 Sep Newcastle 6f Standard 3/12; 12 Oct Newcastle 6f Standard 9/12; 2 Nov Wolverhampton (AW) 6f Standard 4/10 fig 47
    DATA for: Last-run finishing speed +2.2% vs that field (finished strongly); Carries 14 lb less than average
    DATA against: Best recent form figure 47, 10 lb below field average; Official rating 48, 17 lb below field average

## 7:30 Southwell (AW) | race_id rac_32304663651 | All-Weather Championship Is Back Handicap Stakes (Rider Restricted Race) (Div II)
Flat | Class 5 | 7f14y | going Standard | AW | 10 runners | rating band 0-70 | age 3yo+
DATA pace: Lone leader - Glorious Kitty is the only habitual front-runner and may be allowed an easy lead.
- Edmond Halley (hrs_41189694) | 4yo G | 133lb | OR 65 | draw 2 | jockey Ryan Sexton | trainer Edward Bethell (14d 1/10) | headgear hp | last run 19 days | form 353311 | MARKET 23.8% | 09:00 median 3.25 | Matchbook 5.00 | CHECK (skip line 3.09)
    comment: Edmond Halley arrives in cracking form, a winner last time out and again two starts back, and he has run over today's trip and going before after 19 days off.
    DATA: model 21.3% | style Prominent (led 8% of runs) | runs in data 11 | last 3: 12 Oct Newcastle 6f Standard 3/12; 24 Oct Southwell (AW) 6f Standard 1/11 fig 66; 29 Oct Southwell (AW) 7f Standard 1/12 fig 71
    DATA for: Best recent form figure 71, 5 lb above field average; Recent figures 6 lb above its current mark (looks well handicapped); Has won at this trip or further; Good recent finishing positions
- It'sneverjustone (hrs_41876849) | 4yo G | 138lb | OR 70 | draw 10 | jockey William Pyle | trainer David Loughnane (14d 1/4) | headgear b | last run 26 days | form 600547 | MARKET 17.4% | 09:00 median 4.90 | Matchbook -
    comment: The risk is a winless run in his last six, including a seventh last time out, while carrying 138 lb from stall 10.
    DATA: model 12.3% | style Midfield (led 23% of runs) | runs in data 8 | last 3: 17 Sep Ayr 8f Soft 5/12; 9 Oct Kempton 8f Standard To Slow 4/10; 22 Oct Southwell (AW) 8f Standard 7/11 fig 65
    DATA for: Official rating 70, 5 lb above field average
    DATA against: Carries 6 lb more than average
- Strong Voice (hrs_57255681) | 3yo C | 136lb | OR 69 | draw 5 | jockey Stevie Donohoe | trainer James Horton (14d 0/4) | headgear tp | last run 20 days | form 662241 | MARKET 16.6% | 09:00 median 5.00 | Matchbook -
    comment: Strong Voice arrives a last-time-out winner after 20 days off, with a second three starts back and another second four starts back, and he has run over today's trip and going before.
    DATA: model 21.4% | style Prominent (led 29% of runs) | runs in data 8 | last 3: 12 Sep Lingfield 7f Standard 2/8; 9 Oct Kempton 7f Standard To Slow 4/11; 28 Oct Kempton (AW) 7f Standard / Slow 1/13 fig 71
    DATA for: Best recent form figure 71, 5 lb above field average; Has won at this trip or further; Good recent finishing positions
- Oh So Perfect (hrs_54555529) | 3yo F | 119lb | OR 52 | draw 3 | jockey Jack Dace(5) | trainer Michael Appleby (14d 1/11) | headgear - | last run 14 days | form 246555 | MARKET 8.7% | 09:00 median 10.00 | Matchbook -
    comment: Oh So Perfect has finished fifth in each of her last three outings and is winless in her last six, so she is hard to fancy, though she has run over today's trip and going and is back after just 14 days.
    DATA: model 5.5% | style Prominent (led 38% of runs) | runs in data 10 | last 3: 26 Sep Ripon 6f Good 5/11; 16 Oct Redcar 7f Good 5/18 fig 63; 3 Nov Wolverhampton (AW) 7f Standard 5/11 fig 50
    DATA for: Recent figures 11 lb above its current mark (looks well handicapped); Has won at this trip or further; Carries 14 lb less than average
    DATA against: Official rating 52, 13 lb below field average
- Cairdeas (hrs_39961068) | 4yo G | 130lb | OR 62 | draw 1 | jockey Liam Wright(3) | trainer Paul Midgley (14d 0/5) | headgear - | last run 11 days | form 403040 | MARKET 8.1% | 09:00 median 10.00 | Matchbook -
    comment: Cairdeas is yet to win in his last six, though a fourth two starts back and a third four runs ago show he can get involved, and he's fit after 11 days off. He has run over today's trip and going, but unplaced last time out and 130 lb from stall one keep him a midfield sort.
    DATA: model 5.7% | style Midfield (led 3% of runs) | runs in data 10 | last 3: 13 Oct Leicester 6f Good To Soft 11/18; 26 Oct Redcar 7f Heavy 4/12 fig 66; 6 Nov Newcastle (AW) 6f Standard 12/14 fig 58
    DATA for: Recent figures 4 lb above its current mark (looks well handicapped)
- Maldevious (hrs_43796683) | 4yo F | 134lb | OR 66 | draw 6 | jockey Harry Russell | trainer Brian Ellison (14d 0/10) | headgear tp | last run 12 days | form 915445 | MARKET 6.7% | 09:00 median 12.00 | Matchbook -
    DATA: model 7.3% | style Midfield (led 5% of runs) | runs in data 11 | last 3: 5 Sep Newcastle 6f Standard 4/7; 28 Sep Hamilton 6f Soft 4/6; 5 Nov Southwell (AW) 6f Standard 5/9 fig 67
    DATA against: Trainer 0 wins from 10 runs, last 14 days
- Glorious Kitty (hrs_41305166) | 4yo F | 135lb | OR 67 | draw 7 | jockey Finlay Bassett(7) | trainer Michael & David Easterby (14d 1/10) | headgear - | last run 42 days | form 126486 | MARKET 6.6% | 09:00 median 13.00 | Matchbook -
    comment: The risk is a fading profile, with a sixth last time out and an eighth before that, after 42 days off.
    DATA: model 8.4% | style Leader (led 63% of runs) | runs in data 9 | last 3: 29 Aug Beverley 8.5f Soft 4/10; 18 Sep Ayr 8f Soft 8/11; 6 Oct Southwell 7.1f Standard 6/10
    DATA for: Has won at this trip or further; Pace: may get an uncontested lead
- Anton Mauve (hrs_54494265) | 3yo G | 133lb | OR 66 | draw 9 | jockey Matthew Lloyd Slater(7) | trainer Kevin & Lauren Frost (14d 1/7) | headgear - | last run 19 days | form 890150 | MARKET 4.6% | 09:00 median 19.00 | Matchbook -
    DATA: model 9.2% | style Midfield (led 3% of runs) | runs in data 6 | last 3: 17 Sep Yarmouth 7f Good 1/13; 14 Oct Nottingham 8.5f Good To Soft 5/10 fig 63; 29 Oct Southwell (AW) 8f Standard 12/13 fig 52
    DATA for: Has won at this trip or further
- Lerwick (hrs_31550428) | 6yo G | 137lb | OR 69 | draw 8 | jockey Jonny Peate | trainer Mark Loughnane (14d 1/6) | headgear /bes | last run 31 days | form 671775 | MARKET 4.2% | 09:00 median 21.00 | Matchbook -
    comment: Lerwick was fifth last time out after 31 days off and has finished no better than seventh in two runs before that, though he was a winner four starts back and has run over today's trip and going.
    DATA: model 5.7% | style Prominent (led 4% of runs) | runs in data 8 | last 3: 28 Aug Ffos Las 7.4f Good To Soft 7/8; 18 Sep Wolverhampton 7.2f Standard 7/12; 17 Oct Southwell (AW) 7f Standard 5/9 fig 65
    DATA for: Has won at this trip or further
- Comprador (hrs_59025372) | 3yo G | 130lb | OR 63 | draw 4 | jockey Ethan Tindall(5) | trainer Antony Brittain (14d 1/3) | headgear tv | last run 73 days | form 353060 | MARKET 3.3% | 09:00 median 26.00 | Matchbook -
    comment: Comprador is yet to win in his last six starts, though he has been third twice in that spell, most recently four starts back, and he has run over today's trip and going before.
    DATA: model 3.2% | style Prominent (led 5% of runs) | runs in data 8 | last 3: 20 Jun Doncaster 7f Good To Firm 11/13; 8 Aug Haydock 7f Good 6/8; 5 Sep Newcastle 6f Standard 14/14
    DATA against: Poor recent finishing positions

## 8:00 Southwell (AW) | race_id rac_32304665588 | ARC All Weather Bonus Is Back Novice Stakes (Rider Restricted Race) (GBB Race)
Flat | Class 4 | 6f16y | going Standard | AW | 7 runners | rating band - | age 2yo
DATA pace: Lone leader - Miss Deeds is the only habitual front-runner and may be allowed an easy lead.
- Hayate (hrs_17389673770) | 2yo C | 137lb | OR 90 | draw 7 | jockey Robbie Downey | trainer Roger Varian (14d 2/6) | headgear - | last run 34 days | form 31 | MARKET 58.0% | 09:00 median 1.50 | Matchbook 1.51
    DATA: model 39.0% | style Prominent (led 8% of runs) | runs in data 2 | last 3: 31 Jul Newmarket 6f Good To Firm 3/7; 14 Oct Kempton (AW) 6f Standard / Slow 1/8 fig 76
    DATA for: Trainer 33% wins (2/6), last 14 days; Last-run finishing speed +3.3% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Miss Deeds (hrs_17394051241) | 2yo F | 132lb | OR - | draw 3 | jockey M. P. Sheehy | trainer William Haggas (14d 4/9) | headgear - | last run 22 days | form 1 | MARKET 21.8% | 09:00 median 3.50 | Matchbook -
    DATA: model 28.5% | style Leader (led 57% of runs) | runs in data 1 | last 3: 26 Oct Leicester 6f Soft 1/6 fig 95
    DATA for: Trainer 44% wins (4/9), last 14 days; Has won at this trip or further; Pace: may get an uncontested lead
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Lehbab Prince (hrs_64812937) | 2yo C | 130lb | OR - | draw 6 | jockey William Carver | trainer Andrew Balding (14d 1/17) | headgear - | last run 182 days | form 7 | MARKET 6.8% | 09:00 median 13.00 | Matchbook -
    DATA: model 4.8% | style Unknown | runs in data 1 | last 3: 19 May Newcastle 6f Standard 7/7
    DATA against: Returns from a 182-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Blue Cascade (hrs_17394672869) | 2yo C | 130lb | OR - | draw 5 | jockey Dougie Costello | trainer Harry Eustace (14d 0/3) | headgear - | last run - days | form - | MARKET 4.0% | 09:00 median 25.00 | Matchbook -
    DATA: model 8.7% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Gut Reaction (hrs_17391507364) | 2yo G | 130lb | OR - | draw 4 | jockey Oisin McSweeney | trainer Harriet Bethell (14d 0/1) | headgear - | last run 35 days | form 73 | MARKET 3.9% | 09:00 median 23.00 | Matchbook 25.00
    DATA: model 6.4% | style Prominent (led 5% of runs) | runs in data 2 | last 3: 14 Sep Kempton 7f Standard To Slow 7/9; 13 Oct Wolverhampton 6.1f Standard 3/8
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Dubai Jimmy (hrs_17395521871) | 2yo C | 130lb | OR - | draw 2 | jockey Christian Howarth(3) | trainer James Owen (14d 4/34) | headgear - | last run - days | form - | MARKET 3.8% | 09:00 median 26.00 | Matchbook -
    DATA: model 8.7% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
- Hal'way The Lads (hrs_17393973016) | 2yo C | 130lb | OR - | draw 1 | jockey Laura Coughlan(3) | trainer Gemma Tutty (14d 1/7) | headgear - | last run 22 days | form 0 | MARKET 1.6% | 09:00 median 67.00 | Matchbook -
    DATA: model 4.0% | style Held up (led 8% of runs) | runs in data 1 | last 3: 26 Oct Redcar 7f Soft 11/11
    DATA against: Last-run finishing speed -6.4% vs that field (faded); Lightly raced: 1 run in our data, so the model has little to go on

## 8:30 Southwell (AW) | race_id rac_32304667525 | Midnite A Next Generation Betting App Handicap Stakes (Rider Restricted Race)
Flat | Class 5 | 6f16y | going Standard | AW | 14 runners | rating band 0-75 | age 3yo+
DATA pace: Strong pace - 3 habitual front-runners (Methgal, Project Wallace, Veydari). A contested lead should set things up for horses coming from behind.
- Methgal (hrs_39962125) | 4yo G | 132lb | OR 72 | draw 12 | jockey Christian Howarth(3) | trainer Dylan Cunha (14d 1/8) | headgear tv | last run 25 days | form 221232 | MARKET 14.8% | 09:00 median 5.00 | Matchbook - | CHECK (skip line 4.75)
    comment: Methgal has finished in the first three in each of his last six starts, including a second last time out and a winner four starts back, and he has run over today's trip and going.
    DATA: model 13.7% | style Leader (led 38% of runs) | runs in data 17 | last 3: 29 Sep Wolverhampton 6.1f Standard 2/11; 12 Oct Yarmouth 6f Good To Soft 3/13; 23 Oct Wolverhampton (AW) 6f Standard 2/7 fig 69
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Pace: likely to be taken on for the lead
- Goldwork (hrs_50433481) | 3yo G | 133lb | OR 73 | draw 7 | jockey Oliver Carmichael(7) | trainer Eve Johnson Houghton (14d 0/3) | headgear - | last run 41 days | form 736443 | MARKET 12.4% | 09:00 median 6.00 | Matchbook 6.00
    comment: Goldwork was third last time out and has finished in the first four in three of his last four starts, though he remains winless in his last six.
    DATA: model 8.3% | style Held up (led 5% of runs) | runs in data 10 | last 3: 9 Sep Kempton 6f Standard To Slow 4/6; 5 Oct Kempton 6f Standard To Slow 4/10; 7 Oct Kempton 6f Standard To Slow 3/11
    DATA for: Pace: a contested lead should suit its hold-up style
- Courageous Sioux (hrs_50434699) | 3yo F | 135lb | OR 75 | draw 10 | jockey Georgia Dobie | trainer Clive Cox (14d 1/7) | headgear - | last run 22 days | form 5-114 | MARKET 11.2% | 09:00 median 7.00 | Matchbook -
    comment: Fourth last time out follows back-to-back wins, so Courageous Sioux arrives in good heart after 22 days, and she has run over today's trip and going.
    DATA: model 18.0% | style Held up (led 4% of runs) | runs in data 3 | last 3: 4 Jul Nottingham 5f Good To Firm 1/9; 22 Sep Southwell 5f Standard 1/7; 26 Oct Southwell (AW) 6f Standard 4/10 fig 72
    DATA for: Good recent finishing positions; Pace: a contested lead should suit its hold-up style
- Aberama Gold (hrs_18518801) | 9yo G | 135lb | OR 75 | draw 6 | jockey M. P. Sheehy | trainer David O'Meara (14d 0/9) | headgear v | last run 21 days | form 220245 | MARKET 9.9% | 09:00 median 7.50 | Matchbook -
    DATA: model 8.4% | style Midfield (led 4% of runs) | runs in data 18 | last 3: 5 Aug Pontefract 6f Good To Firm 2/8; 23 Oct Doncaster 6f Heavy 4/12 fig 78; 27 Oct Catterick 6f Soft 5/8 fig 70
    DATA for: Best recent form figure 78, 9 lb above field average; Has won at this trip or further
    DATA against: Trainer 0 wins from 9 runs, last 14 days; Aged 9, older than most of this field
- Ormolulu (hrs_34775160) | 6yo M | 132lb | OR 72 | draw 14 | jockey William Pyle | trainer Gemma Tutty (14d 1/7) | headgear - | last run 12 days | form 529972 | MARKET 8.7% | 09:00 median 8.50 | Matchbook -
    comment: Ormolulu bounced back to form with a second last time out just 12 days ago, and she has run over today's trip and going, but she's yet to win in her last six starts and a seventh and two ninth-place finishes sit in that run.
    DATA: model 5.8% | style Held up (led 3% of runs) | runs in data 9 | last 3: 6 Oct Southwell 7.1f Standard 9/10; 12 Oct Newcastle 6f Standard 7/12; 5 Nov Southwell (AW) 6f Standard 2/9 fig 75
    DATA for: Best recent form figure 75, 6 lb above field average; Pace: a contested lead should suit its hold-up style
- Veydari (hrs_41782741) | 4yo G | 129lb | OR 69 | draw 5 | jockey Ryan Sexton | trainer Julie Camacho (14d 0/11) | headgear - | last run 22 days | form 7-2343 | MARKET 8.4% | 09:00 median 8.50 | Matchbook -
    comment: Veydari arrives in solid form with a third last time out, a fourth two starts back and a third three starts back, and he has run over today's trip and going before after a 22-day break.
    DATA: model 8.5% | style Leader (led 38% of runs) | runs in data 4 | last 3: 21 Sep Hamilton 5f Soft 3/6; 5 Oct Pontefract 6f Good 4/12; 26 Oct Leicester 5f Soft 3/7 fig 70
    DATA for: Good recent finishing positions
    DATA against: Trainer 0 wins from 11 runs, last 14 days; Pace: likely to be taken on for the lead
- Amazonian Dream (hrs_24065412) | 7yo G | 133lb | OR 73 | draw 4 | jockey Jonny Peate | trainer Rod Millman (14d 0/1) | headgear - | last run 13 days | form 174578 | MARKET 6.8% | 09:00 median 11.00 | Matchbook -
    comment: The risk is form that has tailed off, with an eighth last time out and a seventh the start before.
    DATA: model 4.2% | style Held up (led 5% of runs) | runs in data 15 | last 3: 29 Aug Windsor 6.1f Soft 5/9; 5 Oct Kempton 6f Standard To Slow 7/10; 4 Nov Kempton (AW) 7f Standard / Slow 8/11 fig 71
    DATA for: Last-run finishing speed +2.1% vs that field (finished strongly); Has won at this trip or further; Pace: a contested lead should suit its hold-up style
- Invincible Speed (hrs_35149212) | 5yo G | 129lb | OR 69 | draw 13 | jockey Taylor Fisher | trainer Mark Loughnane (14d 1/6) | headgear - | last run 13 days | form 442545 | MARKET 6.1% | 09:00 median 11.00 | Matchbook -
    comment: Invincible Speed is winless in his last six, finishing fifth last time out and fourth or worse in four of the other five, which makes him hard to fancy at 129 lb from stall 13. He has run over today's trip and going, and a second four starts back and a quick 13-day turnaround offer some hope.
    DATA: model 6.7% | style Held up (led 5% of runs) | runs in data 8 | last 3: 9 Jun Salisbury 6f Soft 5/10; 2 Jul Kempton 6f Standard To Slow 4/11; 4 Nov Kempton (AW) 6f Standard / Slow 5/11 fig 68
    DATA for: Has won at this trip or further; Pace: a contested lead should suit its hold-up style
- Slot (hrs_56127722) | 3yo F | 127lb | OR 67 | draw 1 | jockey Harry Russell | trainer Antony Brittain (14d 1/3) | headgear - | last run 116 days | form 544227 | MARKET 5.4% | 09:00 median 13.00 | Matchbook -
    comment: Winless in her last six, Slot was seventh last time out and has been off 116 days, which makes her hard to fancy, though a second two starts back and another second three starts back show she can get close.
    DATA: model 6.4% | style Prominent (led 23% of runs) | runs in data 6 | last 3: 25 Jun Newcastle 5f Standard To Slow 2/12; 17 Jul Nottingham 6.1f Good To Firm 2/7; 24 Jul York 5.4f Good To Firm 7/12
    DATA for: Good recent finishing positions
    DATA against: Returns from a 116-day break
- Judgment Call (hrs_24065300) | 8yo G | 133lb | OR 73 | draw 2 | jockey Rhys Clutterbuck | trainer Linda Perratt (14d 0/3) | headgear - | last run 250 days | form 082716 | MARKET 4.4% | 09:00 median 17.00 | Matchbook -
    comment: Sixth last time out and off a 250-day break, Judgment Call is hard to fancy, with a win two starts back the only real bright spot in an otherwise patchy run of form.
    DATA: model 6.6% | style Prominent (led 3% of runs) | runs in data 8 | last 3: 20 Feb Southwell 7.1f Standard 7/12; 10 Mar Southwell 6.1f Standard 1/11; 12 Mar Newcastle 6f Standard 6/10
    DATA for: Has won at this trip or further
    DATA against: Returns from a 250-day break
- Project Wallace (hrs_53960249) | 3yo G | 130lb | OR 70 | draw 8 | jockey Zak Wheatley | trainer Declan Carroll (14d 0/8) | headgear - | last run 12 days | form 4537 | MARKET 3.6% | 09:00 median 21.00 | Matchbook -
    comment: Winless in his last four, Project Wallace was only seventh last time out, 12 days ago, and has finished no better than a third two starts back, so he is hard to fancy.
    DATA: model 6.6% | style Leader (led 54% of runs) | runs in data 4 | last 3: 16 Jun Wolverhampton 5.1f Standard 5/8; 16 Aug Southwell 6.1f Standard 3/9; 5 Nov Southwell (AW) 6f Standard 7/9 fig 63
    DATA against: Best recent form figure 63, 6 lb below field average; Recent figures 7 lb below its current mark (looks high in the weights); Trainer 0 wins from 8 runs, last 14 days; Pace: likely to be taken on for the lead
- Big Cyril (hrs_41597045) | 4yo G | 130lb | OR 70 | draw 3 | jockey Tom Eaves | trainer Roger Fell (14d 0/1) | headgear - | last run 39 days | form 56-090 | MARKET 3.2% | 09:00 median 26.00 | Matchbook -
    comment: Carrying 130 lb from draw 3 after 39 days off, he looks a midfield sort.
    DATA: model 3.0% | style Prominent (led 8% of runs) | runs in data 3 | last 3: 28 Aug Thirsk 6f Good 16/18; 16 Sep Beverley 5f Good 9/12; 9 Oct York 7f Good To Soft 19/20
    DATA against: Poor recent finishing positions
- Perfect Location (hrs_52709671) | 3yo F | 128lb | OR 68 | draw 11 | jockey Jack Dace(5) | trainer Tom Ward (14d 0/3) | headgear p | last run 19 days | form 815609 | MARKET 2.9% | 09:00 median 26.00 | Matchbook -
    DATA: model 2.0% | style Held up (led 5% of runs) | runs in data 9 | last 3: 31 Aug Epsom Downs 6f Good To Soft 6/7; 7 Oct Kempton 6f Standard To Slow 10/11; 29 Oct Bath 5.5f Soft 9/12 fig 59
    DATA for: Has won at this trip or further; Pace: a contested lead should suit its hold-up style
    DATA against: Best recent form figure 59, 10 lb below field average; Recent figures 9 lb below its current mark (looks high in the weights); Poor recent finishing positions
- Numero Vingt (hrs_56278257) | 3yo G | 132lb | OR 72 | draw 9 | jockey William Cox | trainer Robert Edwards (14d 0/0) | headgear - | last run 157 days | form 116079 | MARKET 2.2% | 09:00 median 41.00 | Matchbook -
    comment: Won twice five and six starts back, but the gelding has faded to a ninth last time out and a seventh before that, and he returns after 157 days off.
    DATA: model 1.8% | style Midfield (led 4% of runs) | runs in data 6 | last 3: 3 Apr Lingfield 6f Standard 10/12; 1 May Newcastle 6f Standard 7/8; 13 Jun Leicester 6f Good 9/9
    DATA for: Has won at this trip or further
    DATA against: Last-run finishing speed -2.8% vs that field (faded); Poor recent finishing positions; Returns from a 157-day break
