# Card review packet: Ayr, 2026-11-11

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
{"meeting": "ayr", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 1:10 Ayr | race_id rac_32304167779 | Coral "Bet£5 Get£30 New Customer Offer" 'Chasing Excellence' Beginners' Steeple Chase (GBB Race)
Chase | Class 3 | 2m4f110y | going Good | Turf | 3 runners | rating band - | age 4yo+
- Stride On (hrs_46450362) | 6yo G | 159lb | OR 127 | draw 0 | jockey Derek Fox | trainer Lucinda Russell & Michael Scudamore (14d 7/39) | headgear - | last run 207 days | form /2412- | MARKET 44.1% | 09:00 median 2.15 | Matchbook 2.24
    comment: Stride On is a strong threat on recent form, a second last time out and a win two starts back, and he has run over today's trip before. The main risk is a 207-day absence, plus 159 lb on his back.
- Jeriko du Reponet (hrs_34571264) | 7yo G | 159lb | OR 138 | draw 0 | jockey Harry Cobden | trainer Ben Haslam (14d 1/7) | headgear - | last run 22 days | form 250P-2 | MARKET 43.0% | 09:00 median 2.20 | Matchbook 2.30
    comment: Jeriko du Reponet arrives fresh from a second last time out just 22 days ago, and he has also run second five starts back, with experience of today's trip and going.
- Welonlyhavedone (hrs_40920187) | 6yo G | 159lb | OR 130 | draw 0 | jockey Brian Hughes | trainer Sandy Thomson (14d 3/17) | headgear - | wind surgery | last run 22 days | form P3PU-3 | MARKET 13.0% | 09:00 median 7.00 | Matchbook 8.00
    comment: The main risk is a patchy record, with a pulled up and an unseated in his last five starts and 159 lb to carry.

## 1:40 Ayr | race_id rac_32304161968 | Coral "Pipped-At-The-Post And Win" Novices' Hurdle Race (Go North Night Nurse Series Qualifier) (GBB Race)
Hurdle | Class 4 | 2m | going Good | Turf | 10 runners | rating band - | age 4yo+
- Attin (hrs_63551222) | 5yo G | 154lb | OR - | draw 0 | jockey Danny McMenamin | trainer Nicky Richards (14d 4/14) | headgear - | last run 214 days | form 1- | MARKET 58.5% | 09:00 median 1.44 | Matchbook 1.53
- Jet of Stars (hrs_49974211) | 5yo G | 154lb | OR - | draw 0 | jockey Brian Hughes | trainer Lucinda Russell & Michael Scudamore (14d 7/39) | headgear - | last run 49 days | form 1/1-0 | MARKET 21.7% | 09:00 median 3.25 | Matchbook 4.80
- Moon Reign (hrs_55484422) | 4yo G | 161lb | OR - | draw 0 | jockey Murray Dodd(5) | trainer Iain Jardine (14d 0/11) | headgear - | last run 49 days | form 71 | MARKET 12.7% | 09:00 median 5.00 | Matchbook 9.60
- Cool Off (hrs_17395261121) | 4yo G | 154lb | OR - | draw 0 | jockey Sean Quinlan | trainer Lizzie Quinlan (14d 1/11) | headgear - | last run 171 days | form 52 | MARKET 2.7% | 09:00 median 21.00 | Matchbook 55.00
- Malinas Party (hrs_17395263207) | 5yo M | 147lb | OR - | draw 0 | jockey Derek Fox | trainer Stuart Coltherd (14d 1/6) | headgear - | last run 192 days | form 25- | MARKET 1.8% | 09:00 median 31.00 | Matchbook 85.00
- Effortless (hrs_61684623) | 4yo G | 154lb | OR - | draw 0 | jockey Nathan Moscrop | trainer R. Mike Smith (14d 0/7) | headgear - | last run 201 days | form 38- | MARKET 0.8% | 09:00 median 69.00 | Matchbook 240.00
- Saint Cunning (hrs_64590680) | 5yo G | 154lb | OR - | draw 0 | jockey Ben Smith(7) | trainer R. Mike Smith (14d 0/7) | headgear - | last run 157 days | form 55 | MARKET 0.7% | 09:00 median 101.00 | Matchbook 320.00
- Zebra Star (hrs_30123352) | 6yo M | 147lb | OR - | draw 0 | jockey Bruce Lynn | trainer R. Mike Smith (14d 0/7) | headgear h | last run 27 days | form 69 | MARKET 0.5% | 09:00 median 126.00 | Matchbook 330.00
- Bracing Brook (hrs_58283036) | 7yo M | 147lb | OR - | draw 0 | jockey Dominic Hislop(7) | trainer Catch Bissett (14d 0/2) | headgear - | last run 182 days | form PP-P | MARKET 0.3% | 09:00 median 201.00 | Matchbook 760.00
- Bondi Road (hrs_17393781104) | 5yo G | 154lb | OR - | draw 0 | jockey Charlie Maggs | trainer Jean McGregor (14d 0/1) | headgear - | last run 27 days | form P/7P-P | MARKET 0.2% | 09:00 median 201.00 | Matchbook 1000.00

## 2:13 Ayr | race_id rac_32304163905 | Coral "Daily Rewards Shaker" Handicap Hurdle Race
Hurdle | Class 5 | 2m3f110y | going Good | Turf | 10 runners | rating band 0-100 | age 3yo+
- Jack Dempsey (hrs_46974886) | 6yo G | 158lb | OR 86 | draw 0 | jockey Callum Bewley | trainer Ian Duncan (14d 0/4) | headgear - | last run 20 days | form 95-P92 | MARKET 22.8% | 09:00 median 3.50 | Matchbook 4.30 | CHECK (skip line 3.32)
    comment: Jack Dempsey bounced back with a second last time out after 20 days off, and he has run over today's trip and going before, but he is yet to win in his last five starts and has finished ninth twice in that spell. Carrying 158 lb off 86, he looks a mid-pack type.
- Rickety Gate (hrs_21461636) | 11yo G | 154lb | OR 82 | draw 0 | jockey Danny McMenamin | trainer Nicky Richards (14d 4/14) | headgear - | last run 20 days | form 4P-774 | MARKET 22.4% | 09:00 median 3.75 | Matchbook 4.10
    comment: Rickety Gate was fourth last time out, and he's had a fresh enough 20 days since, with experience over today's trip and going. Yet he's winless in his last five, with two sevenths and a pulled up in that run, and 154 lb off an official mark of 82 is no gift.
- Beat The Retreat (hrs_32751159) | 7yo G | 160lb | OR 88 | draw 0 | jockey Dominic Hislop(7) | trainer N. W. Alexander (14d 2/21) | headgear tp | last run 48 days | form 014-P3 | MARKET 16.2% | 09:00 median 5.00 | Matchbook 5.80
- Largy Meadow (hrs_55061580) | 6yo G | 168lb | OR 96 | draw 0 | jockey Ben Smith(7) | trainer R. Mike Smith (14d 0/7) | headgear ht | last run 157 days | form F2P-29 | MARKET 13.2% | 09:00 median 6.50 | Matchbook 7.00
    comment: The risk is a 157-day absence and a patchy record of one pull-up and one fall in his last five.
- Kinbara Firstdraft (hrs_34373773) | 7yo G | 165lb | OR 93 | draw 0 | jockey Derek Fox | trainer Leonard Kerr (14d 0/3) | headgear tp | last run 6 days | form 6952P5 | MARKET 11.0% | 09:00 median 7.00 | Matchbook 9.00
    comment: Back quickly after a fifth last time out just six days ago, Kinbara Firstdraft has run over today's trip and going and was second three starts back, so he makes our selection on profile despite being winless in recent starts and carrying 165 lb.
- Dreamings Free (hrs_34282101) | 7yo G | 142lb | OR 69 | draw 0 | jockey Patrick Wadge | trainer Daniel Bourne (14d 0/0) | headgear h | last run 116 days | form 380-97 | MARKET 6.0% | 09:00 median 11.50 | Matchbook 19.00
    comment: Dreamings Free is winless in his last five, with a seventh last time out and a ninth before that, and he returns after 116 days off. He has run on today's going and a third five starts back is his best recent effort, but he's hard to fancy off 142 lb.
- Gone With The Tide (hrs_34571376) | 7yo G | 142lb | OR 69 | draw 0 | jockey Joe Williamson | trainer Alison Hamilton (14d 0/0) | headgear - | last run 176 days | form PPP9-P | MARKET 3.0% | 09:00 median 36.00 | Matchbook 42.00
    comment: The big risk is a poor profile: pulled up in four of his last five and absent for 176 days.
- Brewdog (hrs_60594772) | 4yo G | 142lb | OR 67 | draw 0 | jockey Nathan Moscrop | trainer R. Mike Smith (14d 0/7) | headgear - | last run 157 days | form 88-96 | MARKET 2.2% | 09:00 median 34.00 | Matchbook 50.00
    comment: Lightly raced and yet to win, Brewdog showed a bit more when sixth last time out after an eighth and a ninth before that, and he returns after 157 days off with 142 lb, so there could be improvement for a still unexposed gelding.
- Boston Queen (hrs_53539668) | 5yo M | 149lb | OR 77 | draw 0 | jockey Conor Rabbitt(3) | trainer William Young Jnr (14d 0/1) | headgear - | last run 38 days | form 0-BP6P | MARKET 1.7% | 09:00 median 34.00 | Matchbook 110.00
    comment: Boston Queen is hard to fancy, pulled up last time out and again three starts back, with a sixth two starts back her best recent effort and no win in her last five starts. She has run on today's going and has had 38 days to recover, but 149 lb is a big burden for an official mark of 77.
- Bray Dale (hrs_28825083) | 9yo G | 142lb | OR 70 | draw 0 | jockey Bruce Lynn | trainer Catch Bissett (14d 0/2) | headgear p | last run 11 days | form P8P-50 | MARKET 1.6% | 09:00 median 81.00 | Matchbook 65.00
    comment: Bray Dale is winless in his last five, with two pulled-up efforts and an eighth in that run, so he is hard to fancy, though a fifth two starts back and a quick 11-day turnaround show some life.

## 2:43 Ayr | race_id rac_32304165842 | "Play Coral Racing-Super-Series For Free" Handicap Hurdle Race (Go North Cab On Target Series Qualifier)
Hurdle | Class 4 | 2m4f100y | going Good | Turf | 9 runners | rating band 0-120 | age 3yo+
- Ballynoe Boy (hrs_48052480) | 6yo G | 164lb | OR 107 | draw 0 | jockey Danny McMenamin | trainer Nicky Richards (14d 4/14) | headgear - | last run 40 days | form -74111 | MARKET 25.8% | 09:00 median 3.50 | Matchbook 3.50 | CHECK (skip line 3.32)
- Allfor (hrs_51341493) | 5yo G | 166lb | OR 109 | draw 0 | jockey Patrick Wadge | trainer Lucinda Russell & Michael Scudamore (14d 7/39) | headgear - | wind surgery | last run 207 days | form 2/624- | MARKET 24.7% | 09:00 median 3.25 | Matchbook 4.00
    comment: Allfor was second twice in his last four, either side of a sixth, and finished fourth last time out, and has run over today's trip, but he's yet to win in that spell and returns after 207 days off.
- Boston Jury (hrs_43859837) | 6yo G | 158lb | OR 101 | draw 0 | jockey Conor Rabbitt(3) | trainer Andrew Hamilton (14d 0/0) | headgear - | last run 18 days | form 7-6P72 | MARKET 11.5% | 09:00 median 7.65 | Matchbook 8.00
    comment: Runner-up last time out just 18 days ago, Boston Jury is yet to win in his last five starts and was seventh and pulled up in the two runs before that. He has run over today's trip and going, but 158 lb is a big burden for a midfield type.
- The Jeweller's Pet (hrs_35243264) | 7yo G | 154lb | OR 97 | draw 0 | jockey Callum Bewley | trainer Ian Duncan (14d 0/4) | headgear p | last run 22 days | form U432-8 | MARKET 10.6% | 09:00 median 8.50 | Matchbook 8.60
    comment: In his favour, he has run over today's trip and going, and was second and third in the two runs before that.
- Lets Mingle (hrs_40225164) | 6yo M | 168lb | OR 111 | draw 0 | jockey Gregor Walkingshaw(7) | trainer Lucinda Russell & Michael Scudamore (14d 7/39) | headgear - | last run 18 days | form 515771 | MARKET 10.6% | 09:00 median 7.00 | Matchbook 10.50
    comment: Fresh from a win last time out just 18 days ago, Lets Mingle has also won five starts back, and she has run over today's trip and going before. Carrying 168 lb is the main risk, with two sevenths in the middle of her recent form to temper the case.
- Tread Softly Now (hrs_35203392) | 7yo M | 161lb | OR 104 | draw 0 | jockey Ryan Mania | trainer Ian Duncan (14d 0/4) | headgear v | last run 172 days | form 4342-1 | MARKET 7.0% | 09:00 median 11.00 | Matchbook 15.50
- Jem In Em (hrs_29327018) | 8yo G | 162lb | OR 105 | draw 0 | jockey Derek Fox | trainer Lucinda Russell & Michael Scudamore (14d 7/39) | headgear t | last run 565 days | form 42P23/ | MARKET 4.8% | 09:00 median 17.00 | Matchbook 21.00
    comment: The big risk is fitness, as he is returning after 565 days off and carries 162 lb.
- Pyramid Place (hrs_16761927) | 9yo G | 159lb | OR 102 | draw 0 | jockey Craig Nichol | trainer Tristan Davidson (14d 2/5) | headgear ht | wind surgery | last run 15 days | form 8P-6P6 | MARKET 2.8% | 09:00 median 34.00 | Matchbook 38.00
- Micks Jet (hrs_33080817) | 8yo M | 152lb | OR 95 | draw 0 | jockey Joe Williamson | trainer Philip Kirby (14d 1/16) | headgear - | last run 20 days | form 3/P-0P | MARKET 2.2% | 09:00 median 41.00 | Matchbook 50.00
    comment: The risk is plain: she was pulled up last time out and has been winless in her last four, so she must bounce back off 152 lb.

## 3:13 Ayr | race_id rac_32304169716 | Coral "We're Here For It" Handicap Steeple Chase (Go North Red Rum Series Qualifier) (GBB Race)
Chase | Class 4 | 3m0f20y | going Good | Turf | 6 runners | rating band 0-120 | age 4yo+
- Bridge Court (hrs_34859790) | 7yo G | 152lb | OR 104 | draw 0 | jockey Brian Hughes | trainer Sandy Thomson (14d 3/17) | headgear p | last run 27 days | form 2514-6 | MARKET 27.1% | 09:00 median 3.42 | Matchbook 3.45 | CHECK (skip line 3.25)
    comment: Bridge Court has slipped to a sixth last time out and a fourth two starts back, a long way from the win three starts back, and that makes him hard to fancy under 152 lb.
- Green Angel (hrs_51185890) | 5yo G | 162lb | OR 114 | draw 0 | jockey J. J. Slevin | trainer S. R. B. Crawford (14d 0/4) | headgear t | last run 208 days | form 4/443- | MARKET 20.4% | 09:00 median 4.50 | Matchbook 4.60
    comment: The main risk is a 208-day absence, which leaves fitness an open question under 162 lb.
- No Regrets (hrs_18311041) | 12yo G | 155lb | OR 107 | draw 0 | jockey Danny McMenamin | trainer Nicky Richards (14d 4/14) | headgear - | last run 32 days | form 8-1234 | MARKET 16.3% | 09:00 median 5.50 | Matchbook 5.80
    comment: No Regrets arrives with a consistent-looking profile, finishing fourth last time out, a third two starts back, a second three starts back and a winner four starts back, and he has run over today's trip and going before.
- Blakey Boy (hrs_42452193) | 6yo G | 159lb | OR 111 | draw 0 | jockey Craig Nichol | trainer Ewan Whillans (14d 0/13) | headgear p | last run 22 days | form 211P-4 | MARKET 15.1% | 09:00 median 5.50 | Matchbook 6.80
    comment: Hard to fancy at 159 lb off an official mark of 111, with a pulled up two starts back and only a fourth last time out following back-to-back wins. He has run over today's trip and going, and 22 days since his last outing is no concern.
- Whistle Stop Tour (hrs_34166734) | 8yo G | 169lb | OR 121 | draw 0 | jockey Patrick Wadge | trainer Lucinda Russell & Michael Scudamore (14d 7/39) | headgear tp | last run 201 days | form 535P0- | MARKET 13.3% | 09:00 median 6.00 | Matchbook 7.80
    comment: Whistle Stop Tour has run over today's trip and on this going, and a third four starts back is the best of his recent finishes, though he's yet to win in his last five and returns after 201 days off.
- If Not For Dylan (hrs_21512232) | 11yo G | 163lb | OR 115 | draw 0 | jockey Derek Fox | trainer Lucinda Russell & Michael Scudamore (14d 7/39) | headgear t | last run 170 days | form 3173-5 | MARKET 7.6% | 09:00 median 11.00 | Matchbook 13.00
    comment: The main risk is a 170-day absence, with 163 lb to carry on top of a fifth last time out.

## 3:43 Ayr | race_id rac_32304171653 | "Join Coral-Racing-Club For Free" National Hunt Flat Race (Conditional And Amateur Jockeys' Race) (Category 1 Elimination) (GBB Race)
NH Flat | Class 4 | 2m0f0y | going Good | Turf | 7 runners | rating band - | age 4-5yo
- Double Annie (hrs_17394323464) | 4yo F | 149lb | OR - | draw 0 | jockey Gregor Walkingshaw(7) | trainer Lucinda Russell & Michael Scudamore (14d 7/39) | headgear - | last run 213 days | form P1- | MARKET 38.0% | 09:00 median 2.38 | Matchbook 2.50
    comment: Won last time out after being pulled up two starts back, and this lightly raced filly returns after 213 days off, so she looks unexposed with scope to improve. She carries 149 lb.
- Eillis (hrs_64325723) | 4yo F | 149lb | OR - | draw 0 | jockey Mr S Connor(7) | trainer S. R. B. Crawford (14d 0/4) | headgear - | last run 191 days | form 4 | MARKET 28.5% | 09:00 median 3.00 | Matchbook 3.50
    comment: The risk is a 191-day absence, so fitness is the question mark.
- Office Banter (hrs_64360912) | 4yo G | 156lb | OR - | draw 0 | jockey Charlie Maggs | trainer Ewan Whillans (14d 0/13) | headgear - | last run 189 days | form 6 | MARKET 15.8% | 09:00 median 5.50 | Matchbook 6.20
- Pony Express (hrs_64360926) | 5yo G | 156lb | OR - | draw 0 | jockey Joshua Thompson(5) | trainer Ian Duncan (14d 0/4) | headgear hb | last run 20 days | form 25 | MARKET 9.0% | 09:00 median 9.00 | Matchbook 11.50
    comment: Pony Express arrives fresh from a 20-day break after a second two starts back, and he has run over today's trip and on this going before.
- Kiki K (hrs_62908482) | 4yo F | 149lb | OR - | draw 0 | jockey Miss Natasha Cookson(7) | trainer Philip Kirby (14d 1/16) | headgear - | last run - days | form - | MARKET 5.2% | 09:00 median 17.00 | Matchbook 19.50
    comment: Kiki K is a debutant with no recorded form, so she's unexposed and open to any amount of improvement. She carries 149 lb, and her first run should reveal plenty.
- Vienna Blue (hrs_17395175595) | 5yo M | 149lb | OR - | draw 0 | jockey Luke Scott(3) | trainer Daniel Bourne (14d 0/0) | headgear t (1st time) | last run 193 days | form RP55- | MARKET 1.8% | 09:00 median 51.00 | Matchbook 60.00
    comment: Vienna Blue is unexposed and may have more to offer, having finished fifth last time out and fifth again two starts back after a pulled up and a refusal earlier. She is yet to win in her last four starts, returns after 193 days off and carries 149 lb.
- Milano Lady (hrs_57504363) | 5yo M | 149lb | OR - | draw 0 | jockey Mr Daniel Perrin(7) | trainer Philip Kirby (14d 1/16) | headgear - | last run 399 days | form 3- | MARKET 1.7% | 09:00 median 41.00 | Matchbook 75.00
    comment: The main risk is a 399-day absence, so fitness is the question carrying 149 lb.
