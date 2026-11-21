# Card review packet: Haydock, 2026-11-21

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
{"meeting": "haydock", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 12:05 Haydock | race_id rac_32305078169 | Betfair Exchange Graduation Steeple Chase (GBB Race)
Chase | Class 2 | 2m5f127y | going Good | Turf | 3 runners | rating band - | age 4yo+
DATA pace: Lone leader - Koktail Divin is the only habitual front-runner and may be allowed an easy lead.
- Koktail Divin (hrs_48052368) | 6yo G | 165lb | OR 154 | draw 0 | jockey Jordan Gainford | trainer Henry de Bromhead (14d 9/39) | headgear - | last run 226 days | form 22151- | MARKET 62.8% | 09:00 median 1.50 | Matchbook 1.57
    comment: Koktail Divin won last time out and was also a winner three starts back, with a second five starts back in the mix too, and he has run over today's trip and going before. The main risk is a 226-day layoff, plus 165 lb to carry.
    DATA: model 48.3% | style Leader (led 57% of runs) | runs in data 2 | last 3: 11 Mar Cheltenham Chase 25f Good 6/14; 9 Apr Aintree Chase 19.9f Good To Soft 1/5
    DATA for: Official rating 154, 8 lb above field average; Trainer 23% wins (9/39), last 14 days; Last-run finishing speed +20.5% vs that field (finished strongly); Pace: may get an uncontested lead
    DATA against: Returns from a 226-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- Be Aware (hrs_39040708) | 7yo G | 158lb | OR 146 | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 17/80) | headgear ht | last run 12 days | form 2203-2 | MARKET 26.6% | 09:00 median 3.50 | Matchbook 3.75
    comment: He has run over today's trip and going, though he's yet to win in his last five and carries a stiff 158 lb.
    DATA: model 23.2% | style Prominent (led 8% of runs) | runs in data 4 | last 3: 11 Mar Cheltenham Chase 15.9f Good 12/20; 11 Apr Aintree Chase 15.8f Good To Soft 3/8; 9 Nov Carlisle Chase 16f Good 2/3 fig 124
    DATA for: Trainer 21% wins (17/80), last 14 days; Good recent finishing positions
- Leave of Absence (hrs_27451928) | 9yo G | 165lb | OR 139 | draw 0 | jockey Rex Dingle | trainer Anthony Honeyball (14d 3/10) | headgear - | last run 15 days | form 2359-0 | MARKET 10.6% | 09:00 median 8.50 | Matchbook 9.80
    comment: Fresh enough after 15 days, he has run on today's going before and showed his best with a second and a third five and four starts back, so he looks a live threat off 165 lb. The risk is a slide since, with a ninth two starts back and then unplaced last time.
    DATA: model 28.5% | style Prominent (led 4% of runs) | runs in data 4 | last 3: 10 Mar Cheltenham Chase 25f Good To Soft 5/22; 11 Apr Aintree Chase 25f Good To Soft 9/13; 6 Nov Aintree Chase 25f Good To Soft 10/12 fig 134
    DATA for: Trainer 30% wins (3/10), last 14 days
    DATA against: Official rating 139, 7 lb below field average; Last-run finishing speed -3.6% vs that field (faded); Race comments mention jumping mistakes in 3 of its last 4 runs

## 12:40 Haydock | race_id rac_32305072358 | Bet At Your Best With Betfair Handicap Steeple Chase (GBB Race)
Chase | Class 3 | 2m67y | going Good | Turf | 7 runners | rating band 0-130 | age 4yo+
DATA pace: Even - Two likely leaders (Sir Tivo, Calgary Tiger). A fair, even gallop is most likely.
- Kykorock (hrs_39940964) | 6yo G | 166lb | OR 125 | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 17/80) | headgear ht | last run 40 days | form 1131-1 | MARKET 30.9% | 09:00 median 2.88 | Matchbook 3.15
    comment: Kykorock arrives in cracking form, a winner last time out and again two starts back, with four wins in his last five starts, and he has run over today's trip and going before.
    DATA: model 22.3% | style Held up (led 4% of runs) | runs in data 3 | last 3: 17 Jan Haydock Chase 16.3f Good To Soft 3/10; 14 Mar Uttoxeter Chase 24f Soft 1/6; 12 Oct Worcester Chase 16.5f Good To Soft 1/6
    DATA for: Official rating 125, 6 lb above field average; Trainer 21% wins (17/80), last 14 days; Last-run finishing speed +4.2% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Carries 6 lb more than average
- We're Red And Blue (hrs_39808076) | 6yo G | 168lb | OR 127 | draw 0 | jockey Jonjo O'Neill Jr. | trainer Jonjo & A.J. O'Neill (14d 6/39) | headgear - | last run 20 days | form 2320-2 | MARKET 21.8% | 09:00 median 4.00 | Matchbook 4.50
    comment: Beaten in second last time out, and placed in four of his last five, this gelding is a consistent type who has run over today's trip and going before and returns fresh after 20 days.
    DATA: model 14.3% | style Prominent (led 4% of runs) | runs in data 5 | last 3: 4 Apr Haydock Hurdle 15.7f Good 2/11; 28 Apr Punchestown Hurdle 16.6f Yielding 18/21; 1 Nov Carlisle Chase 21f Good 2/4 fig 122
    DATA for: Official rating 127, 8 lb above field average; Last-run finishing speed +2.2% vs that field (finished strongly); Good recent finishing positions
    DATA against: Carries 8 lb more than average
- Tigers Moon (hrs_47621595) | 6yo G | 152lb | OR 111 | draw 0 | jockey Miss Gina Andrews | trainer Tom Ellis (14d 1/9) | headgear - | last run 20 days | form 2132-2 | MARKET 20.5% | 09:00 median 4.42 | Matchbook 4.70
    comment: Tigers Moon has been consistent, finishing second last time out, a second two starts back and a third three starts back, but he's won just once in his last five and carries 152 lb.
    DATA: model 16.4% | style Prominent (led 4% of runs) | runs in data 3 | last 3: 20 Jan Leicester Hurdle 15.5f Heavy 3/10; 20 Feb Warwick Hurdle 16f Soft 2/12; 1 Nov Worcester Chase 16.5f Good To Soft 2/10 fig 109
    DATA for: Last-run finishing speed +3.7% vs that field (finished strongly); Good recent finishing positions; Carries 8 lb less than average
    DATA against: Best recent form figure 109, 12 lb below field average; Official rating 111, 8 lb below field average
- Milan Tino (hrs_37192365) | 6yo G | 164lb | OR 123 | draw 0 | jockey Harry Cobden | trainer Tom George (14d 1/3) | headgear - | last run 20 days | form 1422-1 | MARKET 15.7% | 09:00 median 5.50 | Matchbook 6.40
    comment: Milan Tino arrives in cracking order, a winner last time out, a second two starts back, and another second three starts back, with 20 days since that success. He has run over today's trip and going before, though carrying 164 lb is the main risk.
    DATA: model 17.5% | style Midfield (led 5% of runs) | runs in data 4 | last 3: 12 Feb Leicester Chase 15.9f Heavy 2/4; 15 Mar Chepstow Chase 16.1f Soft 2/3; 1 Nov Huntingdon Chase 16.5f Good 1/8 fig 125
    DATA for: Last-run finishing speed +3.2% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
- Bleu d'Enfer (hrs_29523060) | 8yo G | 164lb | OR 123 | draw 0 | jockey Harry Brown(7) | trainer Donald McCain (14d 3/29) | headgear tp | last run 14 days | form 246215 | MARKET 6.0% | 09:00 median 13.00 | Matchbook 18.00
    comment: Bleu d'Enfer arrives fit after 14 days, a winner two starts back and second three and six starts back, though he was fifth last time out.
    DATA: model 15.3% | style Midfield (led 3% of runs) | runs in data 11 | last 3: 15 Sep Uttoxeter Chase 16f Good 2/5; 16 Oct Uttoxeter Chase 16f Good 1/5 fig 128; 7 Nov Aintree Chase 16f Good To Soft 5/10 fig 118
    DATA for: Best recent form figure 128, 7 lb above field average; Recent figures 5 lb above its current mark (looks well handicapped); Has won at this trip or further; Good recent finishing positions
- Sir Tivo (hrs_13004180) | 12yo G | 164lb | OR 123 | draw 0 | jockey Sean Bowen | trainer Gary Hanmer (14d 1/7) | headgear tp | last run 14 days | form 31P32P | MARKET 2.6% | 09:00 median 34.00 | Matchbook 38.00
    comment: Sir Tivo bounced back from a pulled-up effort to finish second two starts back, a third before that, and he's fresh from a 14-day break with experience of today's trip and going. The big risk is that he was pulled up last time out, and he carries 164 lb.
    DATA: model 7.2% | style Leader (led 63% of runs) | runs in data 8 | last 3: 5 Sep Stratford Chase 17f Good 3/5; 14 Oct Wetherby Chase 15f Good To Firm 2/4 fig 123; 7 Nov Aintree Chase 16f Good To Soft PU/10
    DATA for: Has won at this trip or further
    DATA against: Pulled up in 2 of its last 5 jumps runs; Aged 12, older than most of this field
- Calgary Tiger (hrs_16929038) | 11yo G | 142lb | OR 98 | draw 0 | jockey Gavin Sheehan | trainer William de Best-Turner (14d 0/0) | headgear - | last run 223 days | form /F553- | MARKET 2.5% | 09:00 median 41.00 | Matchbook 40.00
    comment: Calgary Tiger is winless in his last four, though he was third last time out, after a fifth two starts back and another fifth three runs ago.
    DATA: model 7.0% | style Leader (led 72% of runs) | runs in data 2 | last 3: 14 Mar Newcastle Chase 16.3f Good To Soft 5/6; 12 Apr Wincanton Chase 15.7f Good 3/6
    DATA for: Carries 18 lb less than average
    DATA against: Official rating 98, 21 lb below field average; Returns from a 223-day break; Lightly raced: 2 runs in our data, so the model has little to go on

## 1:15 Haydock | race_id rac_32305074295 | Betfair Supports Safer Gambling Week Newton Novices' Hurdle Race (Grade 2) (GBB Race)
Hurdle | Class 1 | 1m7f144y | going Good | Turf | 8 runners | rating band - | age 4yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- North Shore (hrs_55915818) | 4yo G | 156lb | OR 139 | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 17/80) | headgear p | last run 28 days | form 0F-141 | MARKET 24.0% | 09:00 median 3.75 | Matchbook 4.10 | CHECK (skip line 3.56)
    DATA: model 16.8% | style Prominent (led 23% of runs) | runs in data 6 | last 3: 9 May Killarney Hurdle 17f Good To Yielding 1/14; 9 Oct Chepstow Hurdle 19.5f Good To Soft 4/11; 24 Oct Cheltenham Hurdle 16.5f Good To Soft 1/7 fig 126
    DATA for: Best recent form figure 126, 8 lb above field average; Official rating 139, 6 lb above field average; Trainer 21% wins (17/80), last 14 days; Has won at this trip or further; Good recent finishing positions
    DATA against: Fell or unseated in 1 of its last 5 jumps runs
- Cosmic Connection (hrs_50666847) | 5yo G | 156lb | OR 138 | draw 0 | jockey Freddie Gordon | trainer Chris Gordon (14d 1/4) | headgear - | last run 43 days | form 1211-9 | MARKET 22.2% | 09:00 median 4.00 | Matchbook 4.40
    DATA: model 14.5% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 11 Apr Chepstow Hurdle 16.1f Good To Soft 1/9; 25 Apr Sandown Hurdle 16f Good 1/15; 9 Oct Chepstow Hurdle 19.5f Good To Soft 9/11
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Last-run finishing speed -3.6% vs that field (faded)
- Wilde's Legacy (hrs_59862586) | 5yo G | 156lb | OR - | draw 0 | jockey Gavin Sheehan | trainer Jamie Snowden (14d 5/20) | headgear - | last run 25 days | form 110-1 | MARKET 14.5% | 09:00 median 6.00 | Matchbook 6.80
    DATA: model 5.7% | style Prominent (led 5% of runs) | runs in data 3 | last 3: 5 Feb Huntingdon NH Flat 15.8f Soft 1/8; 11 Mar Cheltenham NH Flat 16.4f Good 13/21; 27 Oct Newcastle Hurdle 17f Good 1/6 fig 112
    DATA for: Trainer 25% wins (5/20), last 14 days; Last-run finishing speed +3.4% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Best recent form figure 112, 6 lb below field average
- Saint Jeannais (hrs_57942038) | 6yo G | 156lb | OR 129 | draw 0 | jockey Toby McCain-Mitchell | trainer Nigel & Willy Twiston-Davies (14d 4/25) | headgear - | last run 43 days | form 14-11 | MARKET 11.5% | 09:00 median 8.00 | Matchbook 8.40
    DATA: model 25.4% | style Prominent (led 8% of runs) | runs in data 2 | last 3: 16 May Bangor-on-Dee Hurdle 16.7f Good 1/11; 9 Oct Chepstow Hurdle 16.1f Good To Soft 1/10
    DATA for: Last-run finishing speed +11.8% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Lightly raced: 2 runs in our data, so the model has little to go on
- Kingofthefrontier (hrs_62393989) | 5yo G | 159lb | OR 133 | draw 0 | jockey Conor O'Farrell | trainer John Dawson (14d 0/3) | headgear - | last run 29 days | form 1-311 | MARKET 11.3% | 09:00 median 8.00 | Matchbook 8.40
    DATA: model 11.3% | style Held up (led 5% of runs) | runs in data 3 | last 3: 2 May Uttoxeter Hurdle 15.8f Good 3/7; 2 Jun Southwell Hurdle 20.4f Good 1/5; 23 Oct Cheltenham Hurdle 16.5f Good To Soft 1/10 fig 124
    DATA for: Best recent form figure 124, 6 lb above field average; Has won at this trip or further; Good recent finishing positions
    DATA against: Pace: steady gallop likely, hard to come from off the pace
- Hold The Throw (hrs_51434257) | 5yo G | 156lb | OR - | draw 0 | jockey Sean Bowen | trainer Olly Murphy (14d 10/58) | headgear h | last run 35 days | form 2-11 | MARKET 6.8% | 09:00 median 13.00 | Matchbook 15.50
    DATA: model 10.0% | style Midfield (led 8% of runs) | runs in data 2 | last 3: 14 May Perth NH Flat 16.2f Good To Soft 1/8; 17 Oct Market Rasen Hurdle 16.5f Good 1/8 fig 111
    DATA for: Last-run finishing speed +6.3% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Best recent form figure 111, 7 lb below field average; Lightly raced: 2 runs in our data, so the model has little to go on
- Kershaw (hrs_52055353) | 5yo G | 156lb | OR - | draw 0 | jockey Derek Fox | trainer Lucinda Russell & Michael Scudamore (14d 4/24) | headgear - | last run 37 days | form 2/41-1 | MARKET 5.1% | 09:00 median 17.00 | Matchbook 20.00
    DATA: model 9.7% | style Prominent (led 38% of runs) | runs in data 2 | last 3: 24 Apr Kilbeggan NH Flat 16.5f Good To Yielding 1/14; 15 Oct Perth Hurdle 16f Soft 1/9 fig 113
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Best recent form figure 113, 5 lb below field average; Lightly raced: 2 runs in our data, so the model has little to go on
- Spanish Darling (hrs_17390767877) | 5yo G | 156lb | OR 128 | draw 0 | jockey Kielan Woods | trainer Alex Hales (14d 0/4) | headgear t | last run 7 days | form 13114U | MARKET 4.6% | 09:00 median 19.00 | Matchbook 22.00
    DATA: model 6.6% | style Prominent (led 8% of runs) | runs in data 5 | last 3: 7 Oct Worcester Hurdle 16f Good 1/12; 23 Oct Cheltenham Hurdle 16.5f Good To Soft 4/10 fig 121; 14 Nov Uttoxeter Hurdle 16f Good UR/7
    DATA for: Has won at this trip or further
    DATA against: Official rating 128, 5 lb below field average; Fell or unseated in 1 of its last 3 jumps runs

## 1:50 Haydock | race_id rac_32305076232 | Best Odds On The Betfair Exchange Handicap Hurdle Race (GBB Race)
Hurdle | Class 2 | 2m2f191y | going Good | Turf | 7 runners | rating band - | age 4yo+
DATA pace: Strong pace - 3 habitual front-runners (Manganese, Kocktail Bleu, Miss Maverick). A contested lead should set things up for horses coming from behind.
- Kocktail Bleu (hrs_40494097) | 6yo G | 156lb | OR 126 | draw 0 | jockey Freddie Gordon | trainer Chris Gordon (14d 1/4) | headgear - | last run 42 days | form 2214-4 | MARKET 38.9% | 09:00 median 2.25 | Matchbook 2.52
    comment: Kocktail Bleu has finished no worse than fourth in his last five, including a win three starts back and two seconds, and he has run over today's trip and going before.
    DATA: model 18.6% | style Leader (led 79% of runs) | runs in data 6 | last 3: 21 Mar Newbury Hurdle 16.3f Good To Soft 1/8; 25 Apr Sandown Hurdle 16f Good 4/15; 10 Oct Chepstow Hurdle 19.5f Good To Soft 4/17
    DATA against: Pace: likely to be taken on for the lead
- Smokeringinthedark (hrs_41378407) | 6yo G | 153lb | OR 123 | draw 0 | jockey Danny McMenamin | trainer Nicky Richards (14d 3/15) | headgear - | last run 190 days | form 2512-4 | MARKET 20.1% | 09:00 median 4.50 | Matchbook 4.80
    comment: Absent 190 days, Smokeringinthedark returns from a long break, which is the main worry, and he carries a hefty 153 lb. Still, he was fourth last time out, a winner three starts back, and has run over today's trip and going.
    DATA: model 18.7% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 31 Mar Newcastle Hurdle 20.3f Good To Soft 1/6; 15 Apr Haydock Hurdle 24.3f Good 2/10; 15 May Aintree Hurdle 20f Good 4/10
    DATA for: Trainer 20% wins (3/15), last 14 days; Has won at this trip or further; Good recent finishing positions
    DATA against: Returns from a 190-day break
- Manganese (hrs_58745442) | 4yo F | 157lb | OR 128 | draw 0 | jockey David Bass | trainer Max Comley (14d 2/11) | headgear - | last run 254 days | form 11117- | MARKET 15.8% | 09:00 median 5.50 | Matchbook 6.40
    comment: Manganese won four straight before a seventh last time out, and she has run on today's going, but a 254-day absence and 157 lb on her back leave plenty to prove.
    DATA: model 15.0% | style Leader (led 57% of runs) | runs in data 2 | last 3: 24 Jan Doncaster Hurdle 16.6f Soft 1/5; 12 Mar Cheltenham Hurdle 16.8f Good 7/22
    DATA against: Returns from a 254-day break; Lightly raced: 2 runs in our data, so the model has little to go on; Pace: likely to be taken on for the lead
- Give It To Me Oj (hrs_41305131) | 5yo G | 168lb | OR 138 | draw 0 | jockey Caoilin Quinn | trainer Jamie Moore & Josh Moore (14d 1/23) | headgear - | last run 168 days | form /1560- | MARKET 9.9% | 09:00 median 9.00 | Matchbook 9.80
    comment: The reservations are a 168-day break, a fading run of finishes since that win and a stable out of form.
    DATA: model 17.3% | style Midfield (led 8% of runs) | runs in data 3 | last 3: 11 Mar Cheltenham Hurdle 21f Good 18/24; 22 May Goodwood Flat 16f Good 3/5; 6 Jun Epsom Downs Flat 12f Soft 6/13
    DATA for: Official rating 138, 11 lb above field average
    DATA against: Carries 11 lb more than average; Returns from a 168-day break
- Melon (hrs_40312979) | 5yo G | 159lb | OR 129 | draw 0 | jockey Toby Wynne | trainer Oliver Greenall & Josh Guerriero (14d 2/8) | headgear - | last run 14 days | form 821-04 | MARKET 7.2% | 09:00 median 13.00 | Matchbook 13.50
    comment: Melon showed he's in good order with a fourth last time out just 14 days ago, and he's a winner three starts back who has run over today's trip.
    DATA: model 7.3% | style Prominent (led 4% of runs) | runs in data 6 | last 3: 19 Sep Chester Flat 14.4f Heavy 3/10; 10 Oct Chepstow Hurdle 19.5f Good To Soft 10/17; 7 Nov Aintree Hurdle 17f Good To Soft 4/4
    DATA for: Trainer 25% wins (2/8), last 14 days
- My Chiquita (hrs_31395378) | 7yo M | 151lb | OR 121 | draw 0 | jockey Leah Noreci(7) | trainer James Moffatt (14d 0/4) | headgear - | last run 38 days | form 317484 | MARKET 4.3% | 09:00 median 19.00 | Matchbook 25.00
    comment: The main risk is a modest recent record, with a win five starts back her only success in her last six outings and 151 lb to carry.
    DATA: model 10.2% | style Held up (led 3% of runs) | runs in data 6 | last 3: 29 Aug Cartmel Hurdle 17.2f Good 4/11; 24 Sep Perth Hurdle 23.9f Good 8/11; 14 Oct Wetherby Hurdle 19.5f Good To Firm 4/5
    DATA for: Carries 6 lb less than average; Pace: a contested lead should suit its hold-up style
    DATA against: Official rating 121, 6 lb below field average; Last-run finishing speed -2.0% vs that field (faded)
- Miss Maverick (hrs_29623125) | 9yo M | 154lb | OR 124 | draw 0 | jockey Brian Hughes | trainer Gary Hanmer (14d 1/7) | headgear - | last run 36 days | form 184315 | MARKET 3.9% | 09:00 median 23.00 | Matchbook 26.00
    comment: Miss Maverick was fifth last time out, and she was a winner two starts back, so the form has some substance, but 36 days off and a 154 lb burden make her hard to fancy.
    DATA: model 13.0% | style Leader (led 54% of runs) | runs in data 6 | last 3: 28 Jun Cartmel Hurdle 17.2f Good 3/9; 10 Jul Worcester Hurdle 20f Good 1/6; 16 Oct Uttoxeter Hurdle 20f Good 5/6 fig 109
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Recent figures 15 lb below its current mark (looks high in the weights); Last-run finishing speed -2.4% vs that field (faded); Aged 9, older than most of this field; Pace: likely to be taken on for the lead

## 2:25 Haydock | race_id rac_32304189086 | Betfair Stayers' Red Rose Handicap Hurdle Race (Premier Handicap) (GBB Race)
Hurdle | Class 1 | 3m0f58y | going Good | Turf | 10 runners | rating band - | age 4yo+
DATA pace: Lone leader - Phantomofthepoints is the only habitual front-runner and may be allowed an easy lead.
- Seaniecon (hrs_52055766) | 5yo G | 160lb | OR 133 | draw 0 | jockey Jonjo O'Neill Jr. | trainer Jonjo & A.J. O'Neill (14d 6/39) | headgear p | last run 28 days | form 1255-1 | MARKET 20.5% | 09:00 median 4.33 | Matchbook 4.70 | CHECK (skip line 4.11)
    comment: Seaniecon won last time out and has taken two of his last five, having also run second four starts back, while he has run over today's trip and going before.
    DATA: model 19.6% | style Prominent (led 23% of runs) | runs in data 6 | last 3: 10 Apr Aintree Hurdle 24.7f Good To Soft 5/12; 30 Apr Punchestown Hurdle 23.5f Yielding 5/24; 24 Oct Cheltenham Hurdle 24f Good 1/19 fig 130
    DATA for: Best recent form figure 130, 6 lb above field average; Has won at this trip or further
- Matty's Getaway (hrs_35430661) | 7yo G | 168lb | OR 141 | draw 0 | jockey Ciaran Gethings | trainer Kim Bailey & Mat Nicholls (14d 3/17) | headgear t | last run 41 days | form 412-11 | MARKET 18.7% | 09:00 median 4.95 | Matchbook 5.10
    comment: Matty's Getaway arrives in cracking form, a winner last time out and again two starts back, with a second three starts back, and he has run over today's trip and going before.
    DATA: model 17.3% | style Midfield (led 5% of runs) | runs in data 3 | last 3: 15 Apr Haydock Hurdle 21.2f Good 2/4; 9 May Haydock Hurdle 24.3f Good To Soft 1/15; 11 Oct Chepstow Hurdle 23.6f Good To Soft 1/10
    DATA for: Official rating 141, 10 lb above field average; Last-run finishing speed +7.0% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Carries 10 lb more than average
- Hartington (hrs_38089170) | 7yo G | 153lb | OR 126 | draw 0 | jockey Harry Cobden | trainer Joe Tizzard (14d 7/26) | headgear t | last run 252 days | form 12035- | MARKET 17.2% | 09:00 median 5.00 | Matchbook 5.70
    comment: Hartington was fifth last time out, with a third two starts back and a win five starts back, but he returns after 252 days off and carries 153 lb.
    DATA: model 7.5% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 1 Jan Windsor Hurdle 20f Good 11/12; 31 Jan Sandown Hurdle 23.5f Soft 3/11; 14 Mar Uttoxeter Hurdle 23.3f Soft 5/17
    DATA for: Trainer 27% wins (7/26), last 14 days; Last-run finishing speed +2.9% vs that field (finished strongly)
    DATA against: Returns from a 252-day break
- Supreme Malinas (hrs_39827081) | 6yo M | 153lb | OR 126 | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 17/80) | headgear - | last run 287 days | form 5/115- | MARKET 12.6% | 09:00 median 7.00 | Matchbook 7.80
    comment: Back-to-back wins two and three starts back are the highlight, but she was only fifth last time out and returns after 287 days off, so fitness is a real question.
    DATA: model 6.8% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 7 Feb Warwick Hurdle 19f Heavy 5/9
    DATA for: Trainer 21% wins (17/80), last 14 days
    DATA against: Returns from a 287-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Gold For Alec (hrs_38288264) | 6yo G | 150lb | OR 123 | draw 0 | jockey Caoilin Quinn | trainer Tom Symonds (14d 0/9) | headgear - | last run 28 days | form 1-76F2 | MARKET 7.0% | 09:00 median 12.00 | Matchbook 14.50
    comment: Gold For Alec bounced back with a second last time out after a fall two starts back, and he has run over today's trip and going, but a sixth and a seventh before that, plus 150 lb, leave him hard to fancy.
    DATA: model 5.3% | style Held up (led 3% of runs) | runs in data 8 | last 3: 25 Sep Worcester Hurdle 23f Good 6/9; 10 Oct Chepstow Hurdle 23.6f Good To Soft F/17; 24 Oct Cheltenham Hurdle 24f Good 2/19 fig 117
    DATA for: Has won at this trip or further; Carries 8 lb less than average
    DATA against: Best recent form figure 117, 7 lb below field average; Recent figures 6 lb below its current mark (looks high in the weights); Official rating 123, 8 lb below field average; Trainer 0 wins from 9 runs, last 14 days; Fell or unseated in 1 of its last 5 jumps runs
- The Egyptian Ginge (hrs_48242404) | 5yo G | 162lb | OR 135 | draw 0 | jockey Mr Jamie Neild(5) | trainer Nigel & Willy Twiston-Davies (14d 4/25) | headgear - | last run 14 days | form 21-114 | MARKET 7.0% | 09:00 median 13.00 | Matchbook 13.50
    comment: The Egyptian Ginge arrives fit after 14 days, having won three of his last five and finished a fourth last time out, and he has run over today's trip and going before.
    DATA: model 15.6% | style Prominent (led 23% of runs) | runs in data 8 | last 3: 25 Sep Worcester Hurdle 23f Good 1/9; 17 Oct Market Rasen Hurdle 23f Good 1/5 fig 129; 7 Nov Aintree Hurdle 24.5f Good To Soft 4/14 fig 133
    DATA for: Best recent form figure 133, 9 lb above field average; Good recent finishing positions
- Eagles Reprieve (hrs_47773824) | 5yo G | 146lb | OR 119 | draw 0 | jockey Jack Power(5) | trainer Lucinda Russell & Michael Scudamore (14d 4/24) | headgear - | last run 21 days | form 121P-3 | MARKET 5.3% | 09:00 median 15.00 | Matchbook 20.00
    DATA: model 8.1% | style Prominent (led 3% of runs) | runs in data 4 | last 3: 21 Mar Kelso Hurdle 20.9f Good To Soft 1/7; 17 Apr Ayr Hurdle 21.4f Soft PU/11; 31 Oct Ayr Hurdle 24.5f Good To Soft 3/7 fig 115
    DATA for: Carries 12 lb less than average
    DATA against: Best recent form figure 115, 9 lb below field average; Official rating 119, 12 lb below field average; Pulled up in 1 of its last 4 jumps runs
- Serious Chat (hrs_41171837) | 7yo G | 157lb | OR 130 | draw 0 | jockey Brian Hughes | trainer Donald McCain (14d 3/29) | headgear p | last run 21 days | form 21-032 | MARKET 4.7% | 09:00 median 17.00 | Matchbook 23.00
    comment: Serious Chat arrives in good heart, second last time out and third two starts back, with a winner four starts back, and he has run over today's trip and going before after 21 days off.
    DATA: model 5.2% | style Midfield (led 4% of runs) | runs in data 6 | last 3: 9 May Haydock Hurdle 24.3f Good To Soft 11/15; 25 Sep Worcester Chase 23f Good 3/4; 31 Oct Ayr Hurdle 24.5f Good To Soft 2/7 fig 127
    DATA for: Has won at this trip or further; Good recent finishing positions
- Yellow Car (hrs_40473559) | 8yo G | 166lb | OR 139 | draw 0 | jockey Nick Slatter(3) | trainer David Killahena & Graeme McPherson (14d 3/9) | headgear - | last run 617 days | form 15314/ | MARKET 3.6% | 09:00 median 23.00 | Matchbook 29.00
    comment: Yellow Car won two starts back and took another victory five starts back, and he has run over today's trip and going before, so he looks a strong threat on ability. The big risk is a 617-day absence, which makes fitness a real question under 166 lb.
    DATA: model 8.6% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Official rating 139, 8 lb above field average; Trainer 33% wins (3/9), last 14 days
    DATA against: Carries 8 lb more than average; Returns from a 617-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Phantomofthepoints (hrs_35054789) | 8yo G | 160lb | OR 133 | draw 0 | jockey Rian Corcoran(5) | trainer David Pipe (14d 2/9) | headgear tp | last run 218 days | form F415P- | MARKET 3.4% | 09:00 median 26.00 | Matchbook 30.00
    comment: The main risk is a 218-day absence, with a pulled up last time out also to overcome.
    DATA: model 6.1% | style Leader (led 72% of runs) | runs in data 4 | last 3: 7 Feb Warwick Hurdle 21f Heavy 1/8; 22 Feb Fontwell Hurdle 19.1f Heavy 5/5; 17 Apr Ayr Hurdle 21.4f Soft PU/11
    DATA for: Trainer 22% wins (2/9), last 14 days; Pace: may get an uncontested lead
    DATA against: Returns from a 218-day break; Pulled up in 1 of its last 4 jumps runs

## 3:00 Haydock | race_id rac_32304191023 | Betfair Steeple Chase (Grade 1) (Registered As The Lancashire Steeple Chase) (GBB Race)
Chase | Class 1 | 3m1f125y | going Good | Turf | 7 runners | rating band - | age 5yo+
DATA pace: Lone leader - Affordale Fury is the only habitual front-runner and may be allowed an easy lead.
- Grey Dawning (hrs_27846567) | 9yo G | 164lb | OR 166 | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 17/80) | headgear - | last run 225 days | form /1341- | MARKET 44.1% | 09:00 median 2.00 | Matchbook 2.26
    comment: Grey Dawning won last time out and again four starts back, with a third and a fourth in between, so he arrives in good recent order and has run over today's trip.
    DATA: model 14.3% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 24 Jan Cheltenham Chase 25.3f Soft 3/4; 13 Mar Cheltenham Chase 26.3f Good To Soft 4/10; 10 Apr Aintree Chase 19.9f Good To Soft 1/7
    DATA for: Official rating 166, 10 lb above field average; Trainer 21% wins (17/80), last 14 days; Last-run finishing speed +2.6% vs that field (finished strongly); Good recent finishing positions
    DATA against: Returns from a 225-day break; Race comments mention jumping mistakes in 2 of its last 3 runs
- Affordale Fury (hrs_29226554) | 8yo G | 164lb | OR 167 | draw 0 | jockey Sam Ewing | trainer Noel Meade (14d 3/12) | headgear - | last run 292 days | form 2211P- | MARKET 17.9% | 09:00 median 5.00 | Matchbook 5.50
    DATA: model 8.5% | style Leader (led 57% of runs) | runs in data 1 | last 3: 2 Feb Leopardstown Chase 24.5f Heavy PU/12
    DATA for: Official rating 167, 11 lb above field average; Trainer 25% wins (3/12), last 14 days; Pace: may get an uncontested lead
    DATA against: Returns from a 292-day break; Lightly raced: 1 run in our data, so the model has little to go on; Pulled up in 1 of its last 1 jumps runs
- Jagwar (hrs_32612132) | 7yo G | 164lb | OR 155 | draw 0 | jockey Harry Cobden | trainer Oliver Greenall & Josh Guerriero (14d 2/8) | headgear tp | wind surgery | last run 224 days | form /322U- | MARKET 12.2% | 09:00 median 7.00 | Matchbook 8.20
    comment: Jagwar unseated last time out and returns after 224 days off, which makes him hard to fancy, though he was second two and three starts back, and he has run over today's trip.
    DATA: model 20.6% | style Midfield (led 8% of runs) | runs in data 3 | last 3: 24 Jan Cheltenham Chase 20.6f Soft 2/11; 10 Mar Cheltenham Chase 25f Good To Soft 2/22; 11 Apr Aintree Chase 34.3f Good To Soft UR/34
    DATA for: Trainer 25% wins (2/8), last 14 days
    DATA against: Returns from a 224-day break; Fell or unseated in 1 of its last 3 jumps runs
- Salver (hrs_37905777) | 6yo G | 164lb | OR 150 | draw 0 | jockey Caoilin Quinn | trainer Jamie Moore & Josh Moore (14d 1/23) | headgear p | last run 17 days | form 14123- | MARKET 9.0% | 09:00 median 10.00 | Matchbook 11.00
    comment: Salver arrives in solid form, third last time out, a second two starts back and a winner three starts back, and he has run over today's trip and going before after 17 days off.
    DATA: model 16.5% | style Held up (led 8% of runs) | runs in data 4 | last 3: 11 Mar Cheltenham Chase 25f Good 3/14; 10 Apr Aintree Chase 25f Good To Soft 3/8; 4 Nov Nottingham Flat 14f Soft 8/10 fig 54
    DATA for: Good recent finishing positions
    DATA against: Official rating 150, 6 lb below field average
- Gorgeous Tom (hrs_28903840) | 8yo G | 164lb | OR 154 | draw 0 | jockey Jordan Gainford | trainer Henry de Bromhead (14d 9/39) | headgear - | last run 38 days | form 450-31 | MARKET 7.8% | 09:00 median 12.00 | Matchbook 12.50
    comment: Gorgeous Tom arrives a last-time-out winner, with a third two starts back, and he has run over today's trip and on this going before. The main risk is a 38-day absence combined with a hefty 164 lb on his back.
    DATA: model 19.2% | style Prominent (led 23% of runs) | runs in data 4 | last 3: 11 Apr Aintree Chase 34.3f Good To Soft 12/34; 29 Jul Galway Chase 22.5f Good 3/22; 14 Oct Punchestown (IRE) Chase 23f Good 1/4 fig 155
    DATA for: Best recent form figure 155, 6 lb above field average; Trainer 23% wins (9/39), last 14 days; Last-run finishing speed +4.1% vs that field (finished strongly); Good recent finishing positions
- Handstands (hrs_37790158) | 7yo G | 164lb | OR 153 | draw 0 | jockey Kielan Woods | trainer Ben Pauling (14d 4/25) | headgear - | last run 21 days | form 243P-2 | MARKET 7.2% | 09:00 median 13.00 | Matchbook 13.50
    comment: Yet to win in that spell and shouldering 164 lb, the weight is the main risk.
    DATA: model 11.3% | style Prominent (led 4% of runs) | runs in data 3 | last 3: 18 Jan Windsor Chase 22.2f Soft 3/5; 10 Mar Cheltenham Chase 25f Good To Soft PU/22; 31 Oct Wetherby Chase 24f Good 2/6 fig 150
    DATA against: Pulled up in 1 of its last 3 jumps runs
- Konfusion (hrs_30709889) | 8yo G | 164lb | OR 144 | draw 0 | jockey Gavin Sheehan | trainer Joel Parkinson & Sue Smith (14d 1/12) | headgear - | last run 15 days | form 13F3-5 | MARKET 1.8% | 09:00 median 51.00 | Matchbook 55.00
    comment: Konfusion was fifth last time out and fell three starts back, with his only win in his last five coming five starts back, so he is hard to fancy on a 164 lb burden off 144.
    DATA: model 9.5% | style Prominent (led 3% of runs) | runs in data 4 | last 3: 10 Mar Cheltenham Chase 25f Good To Soft F/22; 11 Apr Aintree Chase 25f Good To Soft 3/13; 6 Nov Aintree Chase 25f Good To Soft 5/12 fig 143
    DATA against: Best recent form figure 143, 6 lb below field average; Official rating 144, 12 lb below field average; Race comments mention jumping mistakes in 3 of its last 4 runs; Fell or unseated in 1 of its last 4 jumps runs

## 3:35 Haydock | race_id rac_32305080106 | Betfair Backs Opinions Handicap Steeple Chase (GBB Race)
Chase | Class 2 | 3m1f125y | going Good | Turf | 6 runners | rating band 0-145 | age 4yo+
DATA pace: Even - Two likely leaders (Saladins Son, Dexperts Opinion). A fair, even gallop is most likely.
- Dexperts Opinion (hrs_41190030) | 6yo G | 147lb | OR 116 | draw 0 | jockey Sean Bowen | trainer Mickey Bowen (14d 4/19) | headgear p | last run 34 days | form 7-1212 | MARKET 25.9% | 09:00 median 3.50 | Matchbook 3.80 | CHECK (skip line 3.32)
    comment: Carrying 147 lb after 34 days off is the stiff part.
    DATA: model 23.1% | style Prominent (led 43% of runs) | runs in data 4 | last 3: 12 Jun Newton Abbot Chase 25.8f Good 2/4; 4 Sep Worcester Chase 23f Good 1/6; 18 Oct Sedgefield Chase 29f Good 2/7 fig 113
    DATA for: Trainer 21% wins (4/19), last 14 days; Good recent finishing positions
    DATA against: Best recent form figure 113, 4 lb below field average
- Saladins Son (hrs_33274990) | 8yo G | 152lb | OR 121 | draw 0 | jockey Ben Godfrey | trainer Anthony Honeyball (14d 3/10) | headgear - | last run 231 days | form /2435- | MARKET 20.1% | 09:00 median 4.33 | Matchbook 5.10
    comment: Saladins Son has been in the frame without a win, finishing a second four starts back and a third two starts back before a fifth last time, and he has run over today's trip and going before.
    DATA: model 17.4% | style Leader (led 38% of runs) | runs in data 2 | last 3: 14 Feb Wincanton Chase 25.1f Heavy 3/6; 4 Apr Haydock Chase 25.6f Good 5/11
    DATA for: Trainer 30% wins (3/10), last 14 days
    DATA against: Returns from a 231-day break; Lightly raced: 2 runs in our data, so the model has little to go on
- Jaccours (hrs_38017469) | 7yo G | 143lb | OR 112 | draw 0 | jockey Danny McMenamin | trainer Robbie Llewellyn (14d 0/4) | headgear - | last run 38 days | form 41P6-2 | MARKET 19.9% | 09:00 median 4.50 | Matchbook 5.00
    comment: Jaccours bounced back to a second last time out after a sixth and a pulled-up effort, but he has won once in his last five and has a 38-day break to account for.
    DATA: model 13.6% | style Prominent (led 8% of runs) | runs in data 4 | last 3: 23 Feb Ayr Chase 20.5f Soft PU/7; 21 Apr Ffos Las Chase 19.4f Good 6/7; 14 Oct Ffos Las Chase 28f Soft 2/7 fig 110
    DATA for: Carries 9 lb less than average
    DATA against: Best recent form figure 110, 7 lb below field average; Official rating 112, 9 lb below field average; Pulled up in 1 of its last 4 jumps runs
- Chasingouttheblues (hrs_39431483) | 7yo G | 155lb | OR 124 | draw 0 | jockey Jamie Hamilton | trainer Mark Walford (14d 1/7) | headgear p | last run 37 days | form 2115-4 | MARKET 18.4% | 09:00 median 5.00 | Matchbook 5.20
    comment: Chasingouttheblues won two of his last five, a winner three starts back and again four starts back, and has run over today's trip and going before, so he's a strong threat. The main risk is a fourth last time out and fifth the run before, plus a burden of 155 lb after 37 days off.
    DATA: model 19.6% | style Prominent (led 23% of runs) | runs in data 5 | last 3: 22 Mar Carlisle Chase 24.5f Good To Soft 1/12; 18 Apr Ayr Chase 31.8f Heavy 5/16; 15 Oct Perth Chase 24f Soft 4/6 fig 118
    DATA for: Has won at this trip or further
    DATA against: Recent figures 6 lb below its current mark (looks high in the weights)
- Caughtinyourtrance (hrs_34166867) | 7yo G | 158lb | OR 127 | draw 0 | jockey Brian Hughes | trainer James Moffatt (14d 0/4) | headgear tp | last run 20 days | form 211222 | MARKET 13.3% | 09:00 median 6.50 | Matchbook 7.60
    comment: Caughtinyourtrance arrives in cracking nick, runner-up in each of his last three outings, with a win four starts back and another five starts back, and he's fresh enough after 20 days off.
    DATA: model 20.7% | style Midfield (led 3% of runs) | runs in data 12 | last 3: 31 Aug Cartmel Chase 25.5f Good To Soft 2/5; 23 Sep Perth Chase 23.8f Good 2/8; 1 Nov Carlisle Chase 26f Good 2/8 fig 127
    DATA for: Best recent form figure 127, 10 lb above field average; Official rating 127, 6 lb above field average; Has won at this trip or further; Good recent finishing positions
    DATA against: Carries 6 lb more than average
- Fortunedefortunata (hrs_28838257) | 9yo G | 155lb | OR 124 | draw 0 | jockey Charlie Maggs | trainer Patrick Morris (14d 0/5) | headgear p | last run 211 days | form UPF39- | MARKET 2.4% | 09:00 median 34.00 | Matchbook 46.00
    comment: The risk is a 211-day absence plus a ninth last time and a patchy record of completing.
    DATA: model 5.7% | style Midfield (led 3% of runs) | runs in data 4 | last 3: 4 Apr Haydock Chase 25.6f Good F/11; 15 Apr Haydock Chase 28.4f Good 3/11; 24 Apr Perth Chase 30.6f Good 9/11
    DATA against: Last-run finishing speed -7.3% vs that field (faded); Returns from a 211-day break; Fell or unseated in 1 of its last 4 jumps runs; Pulled up in 1 of its last 4 jumps runs
