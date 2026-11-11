# Card review packet: Warwick, 2026-11-11

You are a racing form reviewer. Use ONLY this packet. For every race:

1. Start from each runner's MARKET chance (the sharp-weighted 09:00 price, in %).
2. Change a runner's chance ONLY where the card below gives a specific reason: recent form figures, a comment
   or spotlight line, official rating (OR) vs today's weight, days since last run, trainer's 14-day record,
   headgear or wind surgery first time, draw, trip/going/course clues in the comment. Give a one-line reason
   that names the card fact. No reason on the card = no change. Do not use outside knowledge of the horses.
3. Keep changes moderate: normally within 0.67x to 1.5x of the market chance; never beyond 0.33x to 3x.
   Totals do not need to add to 100; they are rescaled afterwards.
4. Runners marked CHECK need a verdict, BET or SKIP:
   BET only if (a) your chance x Matchbook price >= 1.05 AND (b) Matchbook price >= the skip line
   shown (0.95 x 09:00 median), and the card supports your chance. "Matchbook" is the price the bet would get. Otherwise SKIP. Give a one-line reason.

Write valid JSON to the out path you were given, exactly this shape (use the exact race_id and horse_id values):
{"meeting": "warwick", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 12:50 Warwick | race_id rac_32304121291 | Dudley Peverill Conditional Jockeys' Handicap Hurdle Race
Hurdle | Class 4 | 2m3f0y | going Good | Turf | 5 runners | rating band 0-115 | age 3yo+
- Seraphic (hrs_34220970) | 6yo G | 156lb | OR 102 | draw 0 | jockey Isabelle Ryder | trainer David Killahena & Graeme McPherson (14d 3/9) | headgear t | last run 14 days | form 44-311 | MARKET 48.6% | 09:00 median 1.91 | Matchbook 1.97
    comment: Seraphic arrives fresh from back-to-back wins, victorious last time out and two starts back, just 14 days ago, and has run over today's trip and going before. The main risk is the 156 lb he must carry off an official mark of 102.
- Mariole (hrs_58132900) | 4yo G | 156lb | OR 103 | draw 0 | jockey Freddie Mitchell | trainer Nicky Henderson (14d 3/13) | headgear - | last run 21 days | form 0361-5 | MARKET 19.9% | 09:00 median 4.00 | Matchbook 5.50
    comment: The main risk is the 156 lb he must carry off an official mark of 103.
- Mister des Places (hrs_53181128) | 4yo G | 160lb | OR 107 | draw 0 | jockey Troy Walsh(10) | trainer Olly Murphy (14d 8/36) | headgear - | last run 21 days | form FP2-33 | MARKET 17.9% | 09:00 median 5.00 | Matchbook 5.60
    comment: Mister des Places arrives in good heart, third last time out and third again two starts back, with a second three starts back, and he's fresh enough after 21 days off. Yet to win in recent starts, he carries 160 lb, which is the main risk.
- Henrysbrotherjack (hrs_39239851) | 7yo G | 157lb | OR 103 | draw 0 | jockey H. J. Horgan | trainer Olly Murphy (14d 8/36) | headgear - | last run 359 days | form 511/9- | MARKET 8.4% | 09:00 median 11.00 | Matchbook 11.50
    comment: Henrysbrotherjack is hard to fancy after a ninth last time out and a 359-day absence, with 157 lb to carry, though he won two starts back and three starts back and has run over today's trip.
- Douglas Dc (hrs_28295134) | 8yo G | 156lb | OR 102 | draw 0 | jockey Freddie Keighley | trainer Tony Carroll (14d 3/32) | headgear p | last run 47 days | form 4270-F | MARKET 5.1% | 09:00 median 17.00 | Matchbook 20.00
    comment: Douglas Dc is yet to win in his last five, but a second four starts back shows his ability, and he has run over today's trip and going.

## 1:20 Warwick | race_id rac_32304123228 | FCN Novices' Hurdle Race (GBB Race)
Hurdle | Class 4 | 2m5f5y | going Good | Turf | 5 runners | rating band - | age 4yo+
- Largy Force (hrs_29816430) | 8yo M | 147lb | OR 127 | draw 0 | jockey Kevin Brogan | trainer Olly Murphy (14d 8/36) | headgear - | wind surgery | last run 181 days | form 1212-1 | MARKET 40.6% | 09:00 median 2.20 | Matchbook 2.38
- Kefir d'Oudairies (hrs_41442009) | 6yo G | 154lb | OR 110 | draw 0 | jockey Gavin Sheehan | trainer Olly Murphy (14d 8/36) | headgear t | wind surgery | last run 256 days | form /5244- | MARKET 30.4% | 09:00 median 3.00 | Matchbook 3.15
- Dylans Moon (hrs_62170871) | 6yo G | 154lb | OR - | draw 0 | jockey Jack Andrews | trainer Tom Ellis (14d 1/21) | headgear - | last run 204 days | form 3F- | MARKET 15.7% | 09:00 median 6.00 | Matchbook 6.00
- Arcturus Flame (hrs_44570708) | 4yo G | 160lb | OR - | draw 0 | jockey Jonathan Burke | trainer James Owen (14d 14/47) | headgear ht (1st time) | last run 37 days | form 15 | MARKET 9.2% | 09:00 median 9.00 | Matchbook 11.50
- Orchard County (hrs_17393046832) | 4yo G | 153lb | OR - | draw 0 | jockey Sam Twiston-Davies | trainer Nigel & Willy Twiston-Davies (14d 5/30) | headgear - | wind surgery | last run 32 days | form F-0 | MARKET 4.0% | 09:00 median 19.00 | Matchbook 30.00

## 1:50 Warwick | race_id rac_32304125165 | Arnold Thomson Novices' Handicap Steeple Chase (GBB Race)
Chase | Class 4 | 2m0f54y | going Good | Turf | 4 runners | rating band 0-120 | age 4yo+
- Fresh Perspective (hrs_39431364) | 6yo G | 168lb | OR 120 | draw 0 | jockey Gavin Sheehan | trainer Jamie Snowden (14d 9/24) | headgear - | wind surgery | last run 235 days | form 11359- | MARKET 37.9% | 09:00 median 2.50 | Matchbook 2.56
    comment: Twice a winner in his last five starts, Fresh Perspective has run over today's trip and on this going, and he's backed by a yard hitting 9 from 24 in the last 14 days.
- Crystal Days (hrs_47868975) | 6yo M | 157lb | OR 109 | draw 0 | jockey Callum Pritchard | trainer Ben Pauling (14d 5/29) | headgear t | wind surgery | last run 191 days | form 42P2-1 | MARKET 23.8% | 09:00 median 3.75 | Matchbook 4.50
    comment: Crystal Days won last time out and was second two starts back, a sharp recent upturn, and she has run over today's trip and going before. The main risk is a 191-day absence, with 157 lb to carry.
- Soldier's Leap (hrs_41346634) | 6yo G | 154lb | OR 106 | draw 0 | jockey Jack Andrews | trainer Tom Ellis (14d 1/21) | headgear t | wind surgery | last run 202 days | form 15522- | MARKET 20.6% | 09:00 median 4.33 | Matchbook 4.90
    comment: Soldier's Leap finished second last time out, and a second two starts back, so he arrives in solid recent form and has run over today's trip and going before. The main risk is a 202-day break, with the yard's 1/21 record lately adding to the concern.
- Adonedeal (hrs_52495583) | 6yo G | 164lb | OR 116 | draw 0 | jockey Jonathan Burke | trainer Olly Murphy (14d 8/36) | headgear h | last run 202 days | form 1160P- | MARKET 17.7% | 09:00 median 5.50 | Matchbook 5.60
    comment: Adonedeal won twice in his last five starts, a win four starts back and another five starts back, and has run over today's trip, but he was pulled up last time out and returns after 202 days off, so fitness is the main risk.

## 2:21 Warwick | race_id rac_32304127102 | Newton LDP Handicap Steeple Chase (GBB Race)
Chase | Class 4 | 3m0f0y | going Good | Turf | 4 runners | rating band 0-110 | age 4yo+
- Broadway Honey (hrs_50590253) | 6yo M | 160lb | OR 105 | draw 0 | jockey Sam Twiston-Davies | trainer Nigel & Willy Twiston-Davies (14d 5/30) | headgear - | last run 10 days | form 513111 | MARKET 37.7% | 09:00 median 2.38 | Matchbook 2.68
    comment: Broadway Honey arrives a three-time winner on the spin, with four wins in her last six starts, and she's fresh from a ten-day turnaround; she has run over today's trip and going before.
- Ignore The Door (hrs_41052445) | 6yo G | 156lb | OR 108 | draw 0 | jockey Harry Reed | trainer Harry Derham (14d 5/21) | headgear tp | last run 25 days | form 1635-2 | MARKET 25.2% | 09:00 median 3.75 | Matchbook 3.75
    comment: Ignore The Door was second last time out just 25 days ago, and he has run over today's trip and on this going before, so he looks a leading threat; the risk is that he carries 156 lb and has only one win in his last five starts.
- Jupiter des Bordes (hrs_46384233) | 7yo G | 156lb | OR 108 | draw 0 | jockey Freddie Keighley(5) | trainer Richard Hobson (14d 0/2) | headgear tp | last run 19 days | form 0559-7 | MARKET 24.6% | 09:00 median 3.75 | Matchbook 3.95
    comment: Jupiter des Bordes is yet to win in his last five, with a seventh last time out, but he has run over today's trip and on this going, and returns after just 19 days.
- Yes Day (hrs_33080866) | 8yo G | 159lb | OR 111 | draw 0 | jockey Richie McLernon | trainer Jonjo & A.J. O'Neill (14d 4/41) | headgear b | last run 28 days | form 232413 | MARKET 12.5% | 09:00 median 6.75 | Matchbook 8.40
    comment: Yes Day was third last time out and a winner two starts back, with five top-three finishes in his last six runs, and he has run over today's trip and going before; the main risk is carrying 159 lb off an official mark of 111.

## 2:51 Warwick | race_id rac_32304129039 | BNG Made Easy With Reverte Handicap Hurdle Race (Challenger Stayers Hurdle Series Qualifier)
Hurdle | Class 4 | 3m1f5y | going Good | Turf | 6 runners | rating band 0-120 | age 4yo+
- Jackstell (hrs_34860063) | 7yo G | 168lb | OR 117 | draw 0 | jockey Gavin Sheehan | trainer Jamie Snowden (14d 9/24) | headgear tp | last run 29 days | form 5-6P13 | MARKET 30.2% | 09:00 median 2.88 | Matchbook 3.25
    comment: Third last time out, and a winner two starts back, Jackstell arrives fit after 29 days and has run over today's trip and going before. Trainer is in cracking form, and while he carries 168 lb, that profile makes him our pick.
- Paddy de Pole (hrs_30123037) | 8yo G | 168lb | OR 117 | draw 0 | jockey Freddie Keighley(5) | trainer Paul Nicholls (14d 8/35) | headgear p | last run 58 days | form 14-241 | MARKET 18.2% | 09:00 median 5.00 | Matchbook 5.20
    comment: Won last time out and again five starts back, with a fourth and a second in between, so Paddy de Pole arrives in good heart and has run over today's trip and going before. The one concern is a 58-day break, carrying 168 lb.
- Secret Trix (hrs_27578957) | 9yo G | 167lb | OR 116 | draw 0 | jockey Lewis Saunders(5) | trainer Olly Murphy (14d 8/36) | headgear t | last run 47 days | form -32244 | MARKET 16.3% | 09:00 median 5.50 | Matchbook 5.90
    comment: Secret Trix is consistent, with a fourth last time out, another fourth two starts back and a second three starts back, and he has run over today's trip and on this going before.
- Oakley (hrs_25325202) | 8yo G | 168lb | OR 117 | draw 0 | jockey Conor Ring | trainer Mrs C. Williams (14d 3/28) | headgear - | last run 116 days | form -12315 | MARKET 13.3% | 09:00 median 6.50 | Matchbook 7.40
    comment: Oakley is hard to fancy after 116 days off and a fifth last time out, carrying a hefty 168 lb off an official mark of 117. In his favour, he has won twice in his last five starts, a winner two starts back, and has run on today's going before.
- Jaytee (hrs_17837393) | 11yo G | 156lb | OR 105 | draw 0 | jockey Sam Twiston-Davies | trainer Ian Williams (14d 2/26) | headgear v | last run 32 days | form 503-67 | MARKET 11.4% | 09:00 median 8.00 | Matchbook 8.60
    comment: He carries 156 lb, but the main risk is a gelding yet to win in his last five.
- I'm A Starman (hrs_9478350) | 13yo G | 156lb | OR 105 | draw 0 | jockey Callum Pritchard | trainer Mark Rimell (14d 0/0) | headgear - | last run 29 days | form 5-2P24 | MARKET 10.7% | 09:00 median 8.50 | Matchbook 9.20
    comment: I'm A Starman is winless in his last five, though a fourth last time out and a second two starts back show he's competitive, and he has run over today's trip and on this going.

## 3:22 Warwick | race_id rac_32304130976 | Pegasus Handicap Steeple Chase
Chase | Class 5 | 2m0f54y | going Good | Turf | 6 runners | rating band 0-100 | age 4yo+
- Mary (hrs_34542648) | 7yo M | 168lb | OR 100 | draw 0 | jockey Charlie Todd | trainer Ian Williams (14d 2/26) | headgear t | last run 43 days | form -2F333 | MARKET 22.5% | 09:00 median 3.75 | Matchbook 4.50 | CHECK (skip line 3.56)
    comment: Mary arrives consistent, with a third last time out, another third two starts back and a third three starts back, and she has run over today's trip and going before. The one concern is that she is yet to win in her last five starts, and she carries 168 lb after 43 days off.
- Tropical Talent (hrs_26740679) | 7yo G | 147lb | OR 79 | draw 0 | jockey Jack Tudor | trainer Oliver Greenall & Josh Guerriero (14d 2/21) | headgear tb (1st time) | last run 8 days | form /52-23 | MARKET 21.5% | 09:00 median 4.33 | Matchbook 4.30
    comment: Tropical Talent is winless in his last four, with a third last time out, a second two starts back and another second three starts back, so he keeps finding one or two better. Back in just eight days, he has run over this trip and going, but 147 lb off 79 and our 74 rating, fifth of six, make him hard to fancy.
- Alba Crus (hrs_51766547) | 5yo G | 166lb | OR 98 | draw 0 | jockey Sam Twiston-Davies | trainer Warren Greatrex (14d 2/16) | headgear - | wind surgery | last run 173 days | form 734-9U | MARKET 18.1% | 09:00 median 4.50 | Matchbook 5.80
    comment: He's been off 173 days and unseated last time, but a weight of 166 lb is a fair burden.
- Midnight View (hrs_48818952) | 6yo G | 155lb | OR 87 | draw 0 | jockey Ned Fox(3) | trainer Matt Sheppard (14d 0/4) | headgear - | last run 12 days | form 1-3547 | MARKET 17.9% | 09:00 median 5.00 | Matchbook 5.40
    comment: Midnight View ran only 12 days ago, so he arrives fit, has run over today's trip and going, and was a winner five starts back, with a third four starts back too. Risk is a seventh last time out, and 155 lb is a hefty burden off a mark of 87.
- River Don (hrs_51124150) | 5yo G | 143lb | OR 75 | draw 0 | jockey Lorcan Murtagh | trainer Harry Ryall (14d 0/4) | headgear t | last run 13 days | form P1-444 | MARKET 15.2% | 09:00 median 6.00 | Matchbook 6.40
    comment: River Don is unexposed and could have more to offer, having won four starts back and since finished fourth three times running, including last time out just 13 days ago. He carries 143 lb under an official mark of 75.
- Boom Boom (hrs_28875301) | 8yo G | 147lb | OR 79 | draw 0 | jockey Robert Dunne | trainer Rob Summers (14d 0/3) | headgear tp | last run 47 days | form -PP328 | MARKET 4.8% | 09:00 median 19.00 | Matchbook 19.50
    comment: Boom Boom bounced back from two pulled-up runs with a second and a third before an eighth last time, and he has run over today's trip and going before. Winless in his last five and 47 days off, he carries 147 lb, so the weight is the main risk.

## 3:52 Warwick | race_id rac_32304132913 | Farol Fillies' "Junior" National Hunt Flat Race (GBB Race)
NH Flat | Class 5 | 2m0f0y | going Good | Turf | 7 runners | rating band - | age 3yo
- Katies Turn (hrs_17395266336) | 3yo F | 156lb | OR - | draw 0 | jockey Jonathan Burke | trainer Kim Bailey & Mat Nicholls (14d 4/15) | headgear - | last run - days | form - | MARKET 42.2% | 09:00 median 2.20 | Matchbook 2.26
    comment: Katies Turn is an unraced filly with no form to assess, so she's very much an unexposed sort who could have plenty of improvement in her. She carries 156 lb on debut, and her first public run should reveal plenty.
- Sunshine Sheila (hrs_17395268422) | 3yo F | 156lb | OR - | draw 0 | jockey Harry Brown(7) | trainer Donald McCain (14d 0/25) | headgear - | last run - days | form - | MARKET 21.1% | 09:00 median 4.00 | Matchbook 4.70
    comment: Unexposed debutante with no form to go on, Sunshine Sheila is open to improvement but carries 156 lb on her first start, and her yard is 0/25 over the last 14 days, so she has plenty to prove.
- Star of Joy (hrs_17395267379) | 3yo F | 156lb | OR - | draw 0 | jockey Jamie Brace(5) | trainer Jonathan Portman (14d 1/15) | headgear - | last run - days | form - | MARKET 10.8% | 09:00 median 8.00 | Matchbook 9.20
    comment: Star of Joy is an unraced filly with no form to go on, so she's entirely unexposed and open to any amount of improvement. She carries 156 lb on her first outing, and that debut will tell us plenty.
- Poppy's Mist (hrs_17394610289) | 3yo F | 156lb | OR - | draw 0 | jockey Charlie Price | trainer Tim Vaughan (14d 0/6) | headgear - | last run - days | form - | MARKET 8.2% | 09:00 median 11.00 | Matchbook 12.00
    comment: Poppy's Mist is an unraced filly with no form to assess, so she is wholly unexposed and open to improvement on debut. She carries 156 lb, and her first run should reveal plenty about her profile.
- Nervousdisposition (hrs_17393644471) | 3yo F | 156lb | OR - | draw 0 | jockey James Best | trainer Pat Phelan (14d 1/3) | headgear - | last run - days | form - | MARKET 7.8% | 09:00 median 9.50 | Matchbook 14.50
    comment: Nervousdisposition is totally unexposed, with no recorded form to go on, so she's open to any amount of improvement on debut. She carries 156 lb, and her first run will tell us plenty.
- Lady Inca (hrs_17394607160) | 3yo F | 156lb | OR - | draw 0 | jockey Sean Houlihan | trainer Sheila Lewis (14d 0/4) | headgear - | last run - days | form - | MARKET 6.1% | 09:00 median 13.00 | Matchbook 18.00
    comment: Lady Inca is an unraced filly with no recorded form, so she's totally unexposed and open to improvement. She carries 156 lb on her first start, and her debut will reveal plenty about what she might offer.
- Maria's Double (hrs_17394608203) | 3yo F | 156lb | OR - | draw 0 | jockey Joe Anderson(3) | trainer Grace Harris (14d 3/12) | headgear - | last run 13 days | form 7 | MARKET 3.8% | 09:00 median 21.00 | Matchbook 32.00
    comment: Carrying 156 lb is the one reservation.
