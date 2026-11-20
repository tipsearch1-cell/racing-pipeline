# Card review packet: Ascot, 2026-11-20

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
{"meeting": "ascot", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 12:10 Ascot | race_id rac_32304899965 | Ladbrokes 'Chasing Excellence' Beginners' Steeple Chase (GBB Race)
Chase | Class 2 | 2m5f13y | going Good | Turf | 1 runners | rating band - | age 4yo+
DATA pace: Unclear - Running styles known for only 1 of 1 runners.
- Etna Bianco (hrs_412693484) | 6yo G | 159lb | OR 126 | draw 0 | jockey Jonjo O'Neill Jr. | trainer Joe Tizzard (14d 2/18) | headgear t | last run 251 days | form 31542- | MARKET 100.0% | 09:00 median 2.00 | Matchbook 1.99
    DATA: model 100.0% | style Leader (led 38% of runs) | runs in data 2 | last 3: 14 Feb Ascot Hurdle 19.3f Good To Soft 4/6; 14 Mar Kempton Hurdle 21f Good 2/5
    DATA for: Last-run finishing speed +3.3% vs that field (finished strongly)
    DATA against: Returns from a 251-day break; Lightly raced: 2 runs in our data, so the model has little to go on; First run over fences in our data

## 12:45 Ascot | race_id rac_32304898028 | Ascot Promoting Safer Gambling Week 'National Hunt' Maiden Hurdle Race (GBB Race)
Hurdle | Class 3 | 2m3f63y | going Good | Turf | 8 runners | rating band - | age 4yo+
DATA pace: Lone leader - Current Edition is the only habitual front-runner and may be allowed an easy lead.
- No Way Jay (hrs_58534819) | 5yo G | 158lb | OR - | draw 0 | jockey Freddie Gingell | trainer Joe Tizzard (14d 2/18) | headgear - | last run 20 days | form 1490-2 | MARKET 42.0% | 09:00 median 2.10 | Matchbook 2.22
    DATA: model 9.3% | style Prominent (led 5% of runs) | runs in data 3 | last 3: 7 Feb Newbury NH Flat 16.3f Heavy 9/10; 21 Mar Newbury NH Flat 16.3f Good To Soft 14/20; 31 Oct Ascot Hurdle 15.5f Good To Firm 2/5 fig 114
    DATA for: Best recent form figure 114, 13 lb above field average
- Current Edition (hrs_52055297) | 5yo G | 158lb | OR 119 | draw 0 | jockey Toby McCain-Mitchell | trainer Nigel & Willy Twiston-Davies (14d 6/31) | headgear - | last run 23 days | form 532-22 | MARKET 31.4% | 09:00 median 2.75 | Matchbook 3.00
    DATA: model 42.4% | style Prominent (led 43% of runs) | runs in data 4 | last 3: 30 Mar Ludlow Hurdle 15.8f Good 2/8; 4 Oct Uttoxeter Hurdle 15.8f Good 2/7; 28 Oct Huntingdon Hurdle 19.5f Good 2/6 fig 113
    DATA for: Best recent form figure 113, 12 lb above field average; Good recent finishing positions
- Diamonds And Denim (hrs_17395668934) | 5yo G | 158lb | OR - | draw 0 | jockey Ben Jones | trainer Kayley Woollacott (14d 1/10) | headgear - | last run 195 days | form PP2-1 | MARKET 11.6% | 09:00 median 7.00 | Matchbook 8.60
    DATA: model 8.2% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 195-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Affinitive (hrs_62941137) | 4yo G | 157lb | OR - | draw 0 | jockey Paul O'Brien | trainer Henrietta C Knight (14d 0/6) | headgear - | last run 21 days | form 52-3 | MARKET 5.7% | 09:00 median 13.00 | Matchbook 19.00
    DATA: model 9.7% | style Prominent (led 4% of runs) | runs in data 3 | last 3: 26 Mar Warwick NH Flat 16f Good 5/11; 18 Apr Bangor-on-Dee NH Flat 16.7f Good 2/11; 30 Oct Uttoxeter Hurdle 20f Good 3/4 fig 95
    DATA for: Good recent finishing positions
    DATA against: Best recent form figure 95, 6 lb below field average
- Jet Bay (hrs_17393455688) | 5yo G | 158lb | OR - | draw 0 | jockey Shane Fenelon | trainer Mickey Bowen (14d 4/18) | headgear - | last run 29 days | form 1-3 | MARKET 5.1% | 09:00 median 13.00 | Matchbook 24.00
    DATA: model 11.2% | style Held up (led 8% of runs) | runs in data 1 | last 3: 22 Oct Ffos Las NH Flat 16f Soft 3/6 fig 101
    DATA for: Trainer 22% wins (4/18), last 14 days
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Danza Kuduro (hrs_63741958) | 5yo G | 158lb | OR - | draw 0 | jockey Harry Reed | trainer Daisy Hitchins (14d 0/6) | headgear - | last run 34 days | form 4-3 | MARKET 1.7% | 09:00 median 41.00 | Matchbook 90.00
    DATA: model 7.5% | style Prominent (led 8% of runs) | runs in data 2 | last 3: 17 Apr Exeter NH Flat 16.7f Good 4/5; 17 Oct Newton Abbot Hurdle 17f Good 3/8 fig 83
    DATA against: Best recent form figure 83, 18 lb below field average; Lightly raced: 2 runs in our data, so the model has little to go on
- Norff N Sauff (hrs_63908712) | 4yo G | 157lb | OR - | draw 0 | jockey Caoilin Quinn | trainer Jamie Moore & Josh Moore (14d 1/19) | headgear - | last run 190 days | form 0 | MARKET 1.5% | 09:00 median 51.00 | Matchbook 90.00
    DATA: model 7.9% | style Held up (led 8% of runs) | runs in data 1 | last 3: 14 May Fontwell NH Flat 17.7f Good 11/12
    DATA against: Last-run finishing speed -13.5% vs that field (faded); Returns from a 190-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Seven Airs (hrs_62549200) | 4yo G | 157lb | OR - | draw 0 | jockey Tom Cannon | trainer Lawney Hill (14d 0/0) | headgear - | last run 20 days | form 64-5 | MARKET 0.9% | 09:00 median 81.00 | Matchbook 190.00
    DATA: model 3.8% | style Prominent (led 29% of runs) | runs in data 3 | last 3: 14 Mar Kempton NH Flat 16f Good 6/10; 28 Mar Uttoxeter NH Flat 15.8f Good To Soft 4/7; 31 Oct Ascot Hurdle 15.5f Good To Firm 5/5
    DATA against: Last-run finishing speed -5.9% vs that field (faded)

## 1:20 Ascot | race_id rac_32304901902 | Bet With Ascot Donation Box Winners 'Introductory' Hurdle Race (GBB Race)
Hurdle | Class 2 | 1m7f157y | going Good | Turf | 6 runners | rating band - | age 4yo+
DATA pace: Lone leader - Premiere Ligne is the only habitual front-runner and may be allowed an easy lead.
- Spanish Stroll (hrs_56559349) | 5yo G | 161lb | OR - | draw 0 | jockey Dylan Johnston | trainer Joe Tizzard (14d 2/18) | headgear - | last run 29 days | form 90-1 | MARKET 37.3% | 09:00 median 2.38 | Matchbook 2.62
    comment: The main risk is a hefty 161 lb, plus an unplaced run and a ninth in the two starts before that winning effort.
    DATA: model 11.1% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 21 Feb Kempton NH Flat 16f Good To Soft 9/13; 21 Mar Newbury NH Flat 16.3f Good To Soft 10/20; 22 Oct Ffos Las Hurdle 16f Soft 1/11 fig 109
    DATA for: Last-run finishing speed +5.6% vs that field (finished strongly); Has won at this trip or further; Course: midfield runners have won 1.4× their fair share at 16f here
- Push The Limit (hrs_45982384) | 4yo G | 156lb | OR - | draw 0 | jockey Tristan Durrell | trainer Dan Skelton (14d 16/78) | headgear t | last run 29 days | form 3 | MARKET 34.1% | 09:00 median 2.63 | Matchbook 2.88
    comment: Push The Limit signed off with a third last time out and returns after 29 days, a fresh but sensible gap, with experience of today's going.
    DATA: model 29.8% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 22 Oct Carlisle Hurdle 17f Good 3/13 fig 118
    DATA for: Best recent form figure 118, 7 lb above field average; Trainer 21% wins (16/78), last 14 days; Course: midfield runners have won 1.4× their fair share at 16f here
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Without Burlington (hrs_45950674) | 4yo G | 161lb | OR - | draw 0 | jockey Jonjo O'Neill Jr. | trainer Jonjo & A.J. O'Neill (14d 6/31) | headgear - | last run 121 days | form 1 | MARKET 13.8% | 09:00 median 6.50 | Matchbook 7.20
    comment: The one concern is a 121-day absence, and he carries 161 lb.
    DATA: model 26.0% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 22 Jul Worcester Hurdle 16f Good 1/9
    DATA for: Last-run finishing speed +4.8% vs that field (finished strongly); Has won at this trip or further
    DATA against: Returns from a 121-day break; Lightly raced: 1 run in our data, so the model has little to go on; Course: prominent racers have won 0.7× their fair share at 16f here
- Premiere Ligne (hrs_29944656) | 7yo G | 156lb | OR - | draw 0 | jockey Jonathan Burke | trainer Hughie Morrison (14d 0/3) | headgear tp | last run 23 days | form 4 | MARKET 11.2% | 09:00 median 8.00 | Matchbook 8.80
    comment: Fit after 23 days off, Premiere Ligne was fourth last time out and has run on today's going before, while a 156 lb burden makes him a solid threat in this field.
    DATA: model 11.8% | style Leader (led 43% of runs) | runs in data 8 | last 3: 19 Sep Newmarket Flat 18f Good 1/6; 10 Oct Newmarket Flat 18f Good 25/29; 28 Oct Huntingdon Hurdle 19.5f Good 4/6 fig 106
    DATA for: Pace: may get an uncontested lead
    DATA against: Best recent form figure 106, 5 lb below field average
- Prometeo (hrs_36921367) | 5yo G | 156lb | OR - | draw 0 | jockey Harry Reed | trainer Sophie Leech (14d 0/2) | headgear - | last run 553 days | form /- | MARKET 2.2% | 09:00 median 41.00 | Matchbook 50.00
    comment: Prometeo is effectively unexposed, with no recorded form to go on and 553 days since his last run, so a sharp showing can't be taken for granted. He carries 156 lb, and with so little on his page he is open to improvement.
    DATA: model 12.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 553-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Expressionless (hrs_28533204) | 6yo G | 156lb | OR - | draw 0 | jockey Lee Edwards | trainer Dylan Cunha (14d 0/6) | headgear - | last run 23 days | form /- | MARKET 1.3% | 09:00 median 51.00 | Matchbook 130.00
    comment: Expressionless is unexposed and open to improvement, with no recorded form to go on, so this gelding's profile is a blank page. He returns after 23 days off and carries 156 lb, yet to show what he can do.
    DATA: model 9.0% | style Held up (led 5% of runs) | runs in data 12 | last 3: 4 Sep Haydock Flat 14f Heavy 8/8; 1 Oct Nottingham Flat 10.2f Good 10/14; 28 Oct Nottingham Flat 10f Soft 13/15 fig 30
    DATA against: Last-run finishing speed -3.0% vs that field (faded); Poor recent finishing positions; First run over hurdles in our data

## 1:55 Ascot | race_id rac_32304903839 | Join Ladbrokes Bet £5 Get £30 Handicap Steeple Chase (GBB Race)
Chase | Class 2 | 2m5f13y | going Good | Turf | 6 runners | rating band 0-145 | age 4yo+
DATA pace: Even - Two likely leaders (Jet To Vegas, Fringill Dike). A fair, even gallop is most likely.
- Western Knight (hrs_34789748) | 7yo G | 159lb | OR 135 | draw 0 | jockey Dylan Johnston | trainer Joe Tizzard (14d 2/18) | headgear t | last run 253 days | form 41120- | MARKET 29.0% | 09:00 median 3.17 | Matchbook 3.35 | CHECK (skip line 3.01)
    comment: The main risk is a 253-day absence and an unplaced run last time out under 159 lb.
    DATA: model 11.8% | style Prominent (led 5% of runs) | runs in data 3 | last 3: 23 Jan Doncaster Chase 19.1f Soft 1/4; 14 Feb Ascot Chase 23.8f Good To Soft 2/3; 12 Mar Cheltenham Chase 20.6f Good 13/18
    DATA for: Good recent finishing positions
    DATA against: Last-run finishing speed -2.7% vs that field (faded); Returns from a 253-day break; Race comments mention jumping mistakes in 2 of its last 3 runs
- Jet To Vegas (hrs_40786564) | 7yo G | 160lb | OR 136 | draw 0 | jockey Derek Fox | trainer Lucinda Russell & Michael Scudamore (14d 7/35) | headgear t | last run 20 days | form 86P-12 | MARKET 27.7% | 09:00 median 3.25 | Matchbook 3.60
    comment: He has run over today's trip and going before, though 160 lb is a stiff burden.
    DATA: model 19.8% | style Leader (led 29% of runs) | runs in data 6 | last 3: 1 May Punchestown Chase 20.2f Yielding PU/22; 26 Sep Market Rasen Chase 21.4f Good 1/4; 31 Oct Ascot Chase 19f Good 2/5 fig 134
    DATA for: Trainer 20% wins (7/35), last 14 days; Has won at this trip or further
    DATA against: Pulled up in 1 of its last 5 jumps runs
- Crebilly (hrs_27697271) | 9yo G | 159lb | OR 135 | draw 0 | jockey Jonjo O'Neill Jr. | trainer Jonjo & A.J. O'Neill (14d 6/31) | headgear p | last run 21 days | form 142131 | MARKET 17.9% | 09:00 median 5.00 | Matchbook 5.60
    comment: Crebilly arrives in cracking form, a winner last time out and three wins in his last six starts, with a third two starts back, and he has run over today's trip and going before. The main risk is the 159 lb he must carry.
    DATA: model 25.0% | style Midfield (led 3% of runs) | runs in data 8 | last 3: 10 Sep Worcester Chase 20f Good 1/5; 14 Oct Ffos Las Chase 19.5f Soft 3/8 fig 130; 30 Oct Wetherby Chase 19.5f Good 1/6 fig 131
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Race comments mention jumping mistakes in 3 of its last 5 runs
- Somespring Special (hrs_30137653) | 8yo M | 156lb | OR 132 | draw 0 | jockey Ben Jones | trainer Philip Hobbs & Johnson White (14d 2/12) | headgear t | wind surgery | last run 20 days | form 3-1175 | MARKET 12.4% | 09:00 median 7.50 | Matchbook 7.80
    comment: Fifth last time out and a seventh two starts back, so the recent trend is the wrong way, but she won three and four starts back and has run over today's trip and going.
    DATA: model 11.4% | style Prominent (led 3% of runs) | runs in data 6 | last 3: 23 May Bangor-on-Dee Chase 24.1f Good 1/7; 7 Jun Perth Chase 23.8f Good 7/10; 31 Oct Ascot Chase 24f Good 5/10 fig 126
    DATA for: Has won at this trip or further
    DATA against: Best recent form figure 126, 4 lb below field average; Recent figures 6 lb below its current mark (looks high in the weights)
- Fringill Dike (hrs_24028739) | 9yo G | 159lb | OR 135 | draw 0 | jockey Craig Nichol | trainer Jedd O'Keeffe (14d 0/2) | headgear b | last run 34 days | form -61221 | MARKET 9.9% | 09:00 median 9.00 | Matchbook 10.00
    comment: He has run over today's trip and going before.
    DATA: model 24.5% | style Leader (led 72% of runs) | runs in data 6 | last 3: 5 Jul Market Rasen Chase 21.4f Good 2/3; 26 Sep Market Rasen Chase 21.4f Good 2/4; 17 Oct Market Rasen Chase 21.5f Good 1/5 fig 130
    DATA for: Last-run finishing speed +4.5% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
- Thecompanysergeant (hrs_24592659) | 9yo G | 163lb | OR 139 | draw 0 | jockey Shane Fenelon(5) | trainer Mickey Bowen (14d 4/18) | headgear - | last run 74 days | form -21847 | MARKET 3.0% | 09:00 median 29.00 | Matchbook 36.00
    comment: The risk is a seventh last time out and a 74-day absence, with 163 lb to carry.
    DATA: model 7.5% | style Midfield (led 23% of runs) | runs in data 6 | last 3: 10 Jul Kilbeggan Hurdle 20f Good 8/14; 14 Aug Tramore Chase 21.8f Good 4/5; 7 Sep Galway Hurdle 21.6f Yielding 7/8
    DATA for: Trainer 22% wins (4/18), last 14 days

## 2:30 Ascot | race_id rac_32304905776 | Ascot Shared Ownership Weekend Handicap Hurdle Race
Hurdle | Class 3 | 1m7f157y | going Good | Turf | 8 runners | rating band 0-140 | age 3yo+
DATA pace: Lone leader - Ooh Betty is the only habitual front-runner and may be allowed an easy lead.
- Wondering Why (hrs_50435581) | 5yo G | 149lb | OR 120 | draw 0 | jockey Ben Jones | trainer Ben Pauling (14d 5/25) | headgear - | last run 28 days | form 216-17 | MARKET 20.5% | 09:00 median 4.33 | Matchbook 4.70 | CHECK (skip line 4.11)
    comment: Still, he won two starts back and four starts back, and has run over today's trip and going.
    DATA: model 13.1% | style Prominent (led 3% of runs) | runs in data 4 | last 3: 8 Mar Warwick Hurdle 16f Good To Soft 6/10; 4 May Warwick Hurdle 16f Good 1/8; 23 Oct Cheltenham Hurdle 16.5f Good To Soft 7/11 fig 115
    DATA for: Trainer 20% wins (5/25), last 14 days; Has won at this trip or further
    DATA against: Best recent form figure 115, 11 lb below field average; Course: prominent racers have won 0.7× their fair share at 16f here
- Moveit Like Minnie (hrs_25040652) | 9yo G | 150lb | OR 121 | draw 0 | jockey Amber Jackson-Fennell(7) | trainer Nigel & Willy Twiston-Davies (14d 6/31) | headgear tv | last run 20 days | form 419-23 | MARKET 19.5% | 09:00 median 4.50 | Matchbook 5.00
    comment: Moveit Like Minnie arrives in good heart after a third last time out and a second two starts back, and he has run over today's trip and going before, while 20 days since his last run suits.
    DATA: model 13.7% | style Midfield (led 4% of runs) | runs in data 6 | last 3: 19 Apr Plumpton Hurdle 25f Good 9/10; 2 Oct Hexham Hurdle 16.2f Good 2/7; 31 Oct Ascot Hurdle 15.5f Good To Firm 3/16 fig 125
    DATA for: Recent figures 4 lb above its current mark (looks well handicapped); Has won at this trip or further; Good recent finishing positions; Course: midfield runners have won 1.4× their fair share at 16f here
- Fasol (hrs_29785504) | 7yo G | 154lb | OR 118 | draw 0 | jockey Freddie Gingell | trainer Paul Nicholls (14d 2/17) | headgear tb | last run 6 days | form 3-3641 | MARKET 16.9% | 09:00 median 5.00 | Matchbook 5.80
    DATA: model 16.3% | style Midfield (led 4% of runs) | runs in data 10 | last 3: 9 Oct Chepstow Hurdle 19.5f Good To Soft 6/15; 31 Oct Ascot Hurdle 15.5f Good To Firm 4/16 fig 122; 14 Nov Windsor Hurdle 16f Good 1/10 fig 123
    DATA for: Recent figures 5 lb above its current mark (looks well handicapped); Has won at this trip or further; Course: midfield runners have won 1.4× their fair share at 16f here
    DATA against: Official rating 118, 6 lb below field average; Race comments mention jumping mistakes in 2 of its last 5 runs
- Brendas Asking (hrs_30315768) | 8yo M | 147lb | OR 118 | draw 0 | jockey Jonathan Burke | trainer Kim Bailey & Mat Nicholls (14d 1/11) | headgear - | last run 20 days | form 1/3-15 | MARKET 11.3% | 09:00 median 8.00 | Matchbook 8.40
    comment: Brendas Asking won twice in her last four starts, a winner two starts back and four starts back, though she was only fifth last time out, 20 days ago.
    DATA: model 10.3% | style Prominent (led 4% of runs) | runs in data 3 | last 3: 15 Apr Haydock Hurdle 15.7f Good 3/7; 20 May Warwick Hurdle 16f Good 1/7; 31 Oct Ascot Hurdle 15.5f Good To Firm 5/16 fig 120
    DATA for: Has won at this trip or further; Good recent finishing positions; Carries 7 lb less than average
    DATA against: Best recent form figure 120, 6 lb below field average; Official rating 118, 6 lb below field average; Course: prominent racers have won 0.7× their fair share at 16f here
- Williethebuilder (hrs_34166643) | 7yo G | 168lb | OR 139 | draw 0 | jockey Toby McCain-Mitchell(3) | trainer Christian Williams (14d 1/10) | headgear - | last run 20 days | form 407-16 | MARKET 10.6% | 09:00 median 8.50 | Matchbook 9.00
    comment: Williethebuilder won two starts back and has run over today's trip and on this going, while his 20-day break suggests he's fit enough.
    DATA: model 15.2% | style Held up (led 3% of runs) | runs in data 6 | last 3: 4 Apr Haydock Hurdle 15.7f Good 7/11; 18 Oct Sedgefield Hurdle 17f Good 1/9 fig 140; 31 Oct Ascot Hurdle 15.5f Good To Firm 6/16 fig 142
    DATA for: Best recent form figure 142, 16 lb above field average; Official rating 139, 15 lb above field average; Has won at this trip or further
    DATA against: Carries 14 lb more than average
- Intellotto (hrs_28013216) | 6yo G | 157lb | OR 128 | draw 0 | jockey Harry Reed | trainer Daisy Hitchins (14d 0/6) | headgear - | last run 34 days | form 3407-1 | MARKET 10.0% | 09:00 median 8.50 | Matchbook 10.00
    comment: The risk is a 34-day break and 157 lb on his back, with a seventh two starts back showing his form can wobble.
    DATA: model 8.5% | style Midfield (led 3% of runs) | runs in data 4 | last 3: 13 Mar Cheltenham Hurdle 20.3f Good To Soft 19/24; 5 Apr Plumpton Hurdle 15.9f Good 7/14; 17 Oct Newton Abbot Hurdle 17f Good 1/7 fig 127
    DATA for: Last-run finishing speed +2.2% vs that field (finished strongly); Has won at this trip or further; Course: midfield runners have won 1.4× their fair share at 16f here
    DATA against: Race comments mention jumping mistakes in 4 of its last 4 runs
- Ooh Betty (hrs_29917475) | 8yo M | 160lb | OR 131 | draw 0 | jockey Rex Dingle | trainer Ben Clarke (14d 0/7) | headgear tp (1st time) | last run 20 days | form 0193-3 | MARKET 7.2% | 09:00 median 11.00 | Matchbook 14.50
    comment: Ooh Betty arrives fresh from two thirds in a row, with a winner four starts back, and has run over today's trip and going before after 20 days off.
    DATA: model 9.2% | style Leader (led 83% of runs) | runs in data 4 | last 3: 13 Mar Cheltenham Hurdle 16.8f Good To Soft 9/23; 18 Apr Ayr Hurdle 16f Heavy 3/8; 31 Oct Wetherby Hurdle 16f Good 3/4 fig 130
    DATA for: Best recent form figure 130, 4 lb above field average; Official rating 131, 7 lb above field average; Has won at this trip or further; Good recent finishing positions; First-time headgear; Pace: may get an uncontested lead
    DATA against: Carries 6 lb more than average
- Gambino (hrs_42647759) | 5yo G | 146lb | OR 117 | draw 0 | jockey Tristan Durrell | trainer Dan Skelton (14d 16/78) | headgear - | last run 33 days | form 3-1149 | MARKET 3.9% | 09:00 median 19.00 | Matchbook 29.00
    comment: Still, he won twice, three and four starts back, and has run over today's trip and going.
    DATA: model 13.7% | style Prominent (led 4% of runs) | runs in data 7 | last 3: 29 Aug Cartmel Hurdle 17.2f Good 1/9; 23 Sep Perth Hurdle 16.2f Good 4/10; 18 Oct Sedgefield Hurdle 17f Good 9/9
    DATA for: Trainer 21% wins (16/78), last 14 days; Has won at this trip or further; Carries 8 lb less than average
    DATA against: Official rating 117, 7 lb below field average; Course: prominent racers have won 0.7× their fair share at 16f here

## 3:05 Ascot | race_id rac_32304907713 | Ladbrokes 'Get Your Free Racing Bet Today' Handicap Steeple Chase (GBB Race)
Chase | Class 4 | 2m7f185y | going Good | Turf | 10 runners | rating band 0-120 | age 4yo+
DATA pace: Strong pace - 3 habitual front-runners (Star of Affinity, Yes Day, Muskoka). A contested lead should set things up for horses coming from behind.
- Draco Malfoy (hrs_39568487) | 6yo G | 168lb | OR 119 | draw 0 | jockey Ciaran Gethings | trainer Kim Bailey & Mat Nicholls (14d 1/11) | headgear p (1st time) | last run 44 days | form 218P-4 | MARKET 16.4% | 09:00 median 5.50 | Matchbook 5.60 | CHECK (skip line 5.22)
    comment: The main risk is a pulled up two starts back and an eighth three starts back, which leave his consistency in question.
    DATA: model 9.7% | style Midfield (led 23% of runs) | runs in data 4 | last 3: 7 Mar Sandown Hurdle 19.8f Soft 8/17; 17 Apr Ayr Hurdle 24.3f Soft PU/15; 7 Oct Worcester Chase 20f Good 4/6
    DATA for: Official rating 119, 7 lb above field average; First-time headgear
    DATA against: Carries 6 lb more than average; Pulled up in 1 of its last 4 jumps runs
- Gasmani (hrs_34652597) | 7yo G | 163lb | OR 114 | draw 0 | jockey Jonathan Burke | trainer David Dennis (14d 0/1) | headgear - | last run 24 days | form 12-842 | MARKET 14.2% | 09:00 median 6.00 | Matchbook 6.80
    comment: Gasmani was second last time out, 24 days ago, and has run over today's trip and going, though a fourth two starts back and an eighth three starts back show some inconsistency.
    DATA: model 7.8% | style Midfield (led 4% of runs) | runs in data 5 | last 3: 22 May Worcester Hurdle 23f Good 8/11; 7 Oct Worcester Hurdle 20f Good 4/10; 27 Oct Bangor-on-Dee Chase 24f Good To Soft 2/13 fig 111
    DATA for: Last-run finishing speed +5.9% vs that field (finished strongly); Has won at this trip or further
- Star of Affinity (hrs_34991026) | 7yo G | 167lb | OR 118 | draw 0 | jockey Freddie Gingell | trainer Joe Tizzard (14d 2/18) | headgear t | last run 23 days | form 4214-1 | MARKET 12.7% | 09:00 median 7.00 | Matchbook 7.60
    comment: Star of Affinity won last time out and again three starts back, with a fourth two starts back in between, and he has run on today's going before.
    DATA: model 17.9% | style Leader (led 29% of runs) | runs in data 3 | last 3: 9 Feb Plumpton Chase 19.8f Soft 1/2; 9 Mar Stratford Chase 22.6f Soft 4/6; 28 Oct Newton Abbot Chase 21f Good To Soft 1/6 fig 114
    DATA for: Best recent form figure 114, 6 lb above field average; Official rating 118, 6 lb above field average; Good recent finishing positions
    DATA against: Carries 6 lb more than average; Race comments mention jumping mistakes in 2 of its last 3 runs; Pace: likely to be taken on for the lead
- Ideal des Bordes (hrs_33165384) | 8yo G | 164lb | OR 115 | draw 0 | jockey Nico de Boinville | trainer Nicky Henderson (14d 3/14) | headgear b | last run 162 days | form 0P42-P | MARKET 10.5% | 09:00 median 8.00 | Matchbook 9.40
    DATA: model 6.2% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 11 Jun Worcester Chase 23f Good PU/8
    DATA for: Trainer 21% wins (3/14), last 14 days
    DATA against: Returns from a 162-day break; Lightly raced: 1 run in our data, so the model has little to go on; Pulled up in 1 of its last 1 jumps runs
- Fever Dream (hrs_30123030) | 8yo G | 162lb | OR 113 | draw 0 | jockey Jack Tudor | trainer Christian Williams (14d 1/10) | headgear t | last run 33 days | form 215-13 | MARKET 9.8% | 09:00 median 8.50 | Matchbook 10.00
    DATA: model 9.5% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 24 Apr Perth Chase 30.6f Good 5/11; 22 Sep Warwick Chase 25.5f Good To Firm 1/3; 18 Oct Sedgefield Chase 29f Good 3/7 fig 111
    DATA for: Has won at this trip or further; Good recent finishing positions
- Muskoka (hrs_33229329) | 8yo G | 164lb | OR 115 | draw 0 | jockey Charlie Todd | trainer Emma Lavelle (14d 3/19) | headgear v | last run 22 days | form 4PP-F2 | MARKET 9.8% | 09:00 median 9.00 | Matchbook 10.00
    comment: The risk is a patchy record, with a fell and two pulled ups in his last five starts, and he is yet to win in that spell.
    DATA: model 6.4% | style Leader (led 63% of runs) | runs in data 5 | last 3: 1 Apr Wincanton Chase 25.1f Good PU/5; 12 Oct Worcester Chase 23f Good To Soft F/5; 29 Oct Ffos Las Chase 25.5f Good 2/5 fig 115
    DATA for: Best recent form figure 115, 7 lb above field average; Last-run finishing speed +3.9% vs that field (finished strongly)
    DATA against: Race comments mention jumping mistakes in 2 of its last 5 runs; Fell or unseated in 1 of its last 5 jumps runs; Pulled up in 2 of its last 5 jumps runs; Pace: likely to be taken on for the lead
- Yes Day (hrs_33080866) | 8yo G | 167lb | OR 111 | draw 0 | jockey Jonjo O'Neill Jr. | trainer Jonjo & A.J. O'Neill (14d 6/31) | headgear b | last run 9 days | form 324131 | MARKET 8.4% | 09:00 median 9.50 | Matchbook 12.50
    comment: Yes Day arrives in cracking nick, a winner last time out nine days ago, then a third two starts back and a winner three starts back, and he has run over today's trip and going.
    DATA: model 14.5% | style Leader (led 43% of runs) | runs in data 12 | last 3: 22 Sep Fontwell Chase 26f Good 1/4; 14 Oct Ffos Las Chase 28f Soft 3/7 fig 106; 11 Nov Warwick Chase 24f Good 1/4 fig 113
    DATA for: Best recent form figure 113, 5 lb above field average; Has won at this trip or further; Good recent finishing positions
    DATA against: Carries 6 lb more than average; Pace: likely to be taken on for the lead
- Royal Time (hrs_37687419) | 7yo G | 146lb | OR 97 | draw 0 | jockey Ellis Collier(5) | trainer Christian Williams (14d 1/10) | headgear - | last run 24 days | form 435311 | MARKET 8.4% | 09:00 median 9.50 | Matchbook 12.50
    DATA: model 11.7% | style Midfield (led 4% of runs) | runs in data 9 | last 3: 6 Oct Huntingdon Chase 23.6f Good 3/5; 18 Oct Sedgefield Chase 21f Good 1/7 fig 92; 27 Oct Newcastle Chase 23.5f Good 1/4 fig 89
    DATA for: Last-run finishing speed +2.1% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions; Carries 16 lb less than average
    DATA against: Best recent form figure 92, 16 lb below field average; Official rating 97, 15 lb below field average
- Diplomatic Ash (hrs_38188815) | 7yo G | 162lb | OR 113 | draw 0 | jockey Tom Cannon | trainer Jamie Moore & Josh Moore (14d 1/19) | headgear tp | last run 15 days | form 42-171 | MARKET 6.6% | 09:00 median 12.00 | Matchbook 15.50
    comment: Won last time out and a winner three starts back, with a seventh in between, so Diplomatic Ash arrives fresh after 15 days and has run over today's trip and going.
    DATA: model 10.5% | style Held up (led 8% of runs) | runs in data 5 | last 3: 26 May Plumpton Hurdle 20.5f Good 1/4; 15 Oct Fontwell Chase 19.5f Good To Soft 7/7; 5 Nov Plumpton Chase 25.5f Good 1/4 fig 110
    DATA for: Last-run finishing speed +2.6% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions; Pace: a contested lead should suit its hold-up style
    DATA against: Race comments mention jumping mistakes in 2 of its last 5 runs
- Mahler Moon (hrs_29479205) | 8yo G | 152lb | OR 103 | draw 0 | jockey Jack Quinlan | trainer Fergal O'Brien (14d 3/30) | headgear tp | last run 35 days | form 21-266 | MARKET 3.0% | 09:00 median 26.00 | Matchbook 36.00
    comment: Mahler Moon has slipped to back-to-back sixths after a second and a win earlier in his last five starts, and he is hard to fancy at 152 lb after 35 days off.
    DATA: model 5.7% | style Prominent (led 4% of runs) | runs in data 7 | last 3: 5 May Hereford Chase 25.2f Good 2/4; 24 May Uttoxeter Chase 24f Good 6/7; 16 Oct Uttoxeter Chase 24f Good 6/8 fig 96
    DATA for: Has won at this trip or further; Carries 10 lb less than average
    DATA against: Best recent form figure 96, 12 lb below field average; Recent figures 7 lb below its current mark (looks high in the weights); Official rating 103, 9 lb below field average; Last-run finishing speed -2.6% vs that field (faded)

## 3:40 Ascot | race_id rac_32304909650 | Bet Responsibly With Ladbrokes Open National Hunt Flat Race (Category 1 Elimination) (GBB Race)
NH Flat | Class 3 | 1m7f157y | going Good | Turf | 7 runners | rating band - | age 4-5yo
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Power Steering (hrs_65069039) | 4yo G | 156lb | OR - | draw 0 | jockey Jonathan Burke | trainer Harry Fry (14d 0/6) | headgear - | last run 178 days | form 2 | MARKET 41.8% | 09:00 median 2.10 | Matchbook 2.32
    comment: Power Steering was second last time out but returns after 178 days off, and he is yet to win in his recent form, which makes him hard to fancy at 156 lb.
    DATA: model 12.4% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 26 May Ballinrobe NH Flat 16.1f Good 2/9
    DATA for: Last-run finishing speed +6.6% vs that field (finished strongly)
    DATA against: Returns from a 178-day break; Lightly raced: 1 run in our data, so the model has little to go on; Course: prominent racers have won 0.7× their fair share at 16f here
- Dennis's Honor (hrs_64488046) | 4yo G | 156lb | OR - | draw 0 | jockey Finn Lambert(3) | trainer Tom Ellis (14d 1/10) | headgear - | last run 27 days | form 22 | MARKET 19.6% | 09:00 median 4.50 | Matchbook 5.00
    comment: The risk is 156 lb, a hefty burden to carry.
    DATA: model 6.5% | style Held up (led 5% of runs) | runs in data 2 | last 3: 9 May Warwick NH Flat 16f Good 2/5; 24 Oct Cheltenham NH Flat 16.5f Good To Soft 2/10 fig 109
    DATA for: Good recent finishing positions
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- Persian Art (hrs_17393250217) | 4yo G | 160lb | OR - | draw 0 | jockey Paul O'Brien | trainer Henrietta C Knight (14d 0/6) | headgear - | last run 23 days | form 21 | MARKET 13.3% | 09:00 median 7.00 | Matchbook 7.20
    comment: Persian Art arrives in cracking nick, a winner last time out and second two starts back, and he's fresh enough after 23 days off.
    DATA: model 21.0% | style Prominent (led 38% of runs) | runs in data 2 | last 3: 5 Oct Stratford NH Flat 16.3f Good To Firm 2/8; 28 Oct Huntingdon NH Flat 16f Good 1/9 fig 116
    DATA for: Best recent form figure 116, 6 lb above field average; Last-run finishing speed +3.5% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on; Course: prominent racers have won 0.7× their fair share at 16f here
- Bielle Biarrey (hrs_17395096327) | 4yo G | 156lb | OR - | draw 0 | jockey Freddie Gingell | trainer Paul Nicholls (14d 2/17) | headgear - | last run 209 days | form F- | MARKET 11.3% | 09:00 median 8.10 | Matchbook 8.80
    comment: Unexposed gelding who fell on his only recent start, so there's little to go on and plenty of scope for improvement; he returns after 209 days off and carries 156 lb, yet to win in his last start.
    DATA: model 11.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 209-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Parisian Fair (hrs_66399613) | 4yo G | 160lb | OR - | draw 0 | jockey Caoilin Quinn | trainer Jamie Moore & Josh Moore (14d 1/19) | headgear - | last run 138 days | form 1 | MARKET 7.5% | 09:00 median 12.00 | Matchbook 13.00
    comment: The main risk is a 138-day layoff, which leaves fitness the question.
    DATA: model 25.6% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 5 Jul Market Rasen NH Flat 16.6f Good 1/11
    DATA for: Last-run finishing speed +6.6% vs that field (finished strongly); Has won at this trip or further
    DATA against: Returns from a 138-day break; Lightly raced: 1 run in our data, so the model has little to go on; Course: prominent racers have won 0.7× their fair share at 16f here
- Irish Ocean (hrs_17393902092) | 4yo G | 156lb | OR - | draw 0 | jockey Dylan Johnston | trainer Joe Tizzard (14d 2/18) | headgear - | last run 34 days | form 3 | MARKET 3.9% | 09:00 median 19.00 | Matchbook 30.00
    comment: The risk is 156 lb, a hefty burden that could blunt his challenge.
    DATA: model 11.7% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 17 Oct Newton Abbot NH Flat 17f Good 3/7 fig 104
    DATA for: Last-run finishing speed +3.5% vs that field (finished strongly); Course: midfield runners have won 1.4× their fair share at 16f here
    DATA against: Best recent form figure 104, 6 lb below field average; Lightly raced: 1 run in our data, so the model has little to go on
- Knowonelikesus (hrs_17395020188) | 4yo G | 156lb | OR - | draw 0 | jockey Harry Reed | trainer Nick Scholfield (14d 1/14) | headgear - | last run - days | form - | MARKET 2.7% | 09:00 median 34.00 | Matchbook 38.00
    comment: Knowonelikesus is unexposed with no recorded form to lean on, so he arrives an unknown quantity carrying 156 lb. Lightly raced types can find improvement, though that remains to be proven on the track.
    DATA: model 11.4% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Lightly raced: 0 runs in our data, so the model has little to go on
