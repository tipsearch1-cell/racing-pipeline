# Card review packet: Lingfield, 2026-11-10

You are a racing form reviewer. Use ONLY this packet. For every race:

1. Start from each runner's MARKET chance (the sharp-weighted 09:00 price, in %).
2. Change a runner's chance ONLY where the card below gives a specific reason: recent form figures, a comment
   or spotlight line, official rating (OR) vs today's weight, days since last run, trainer's 14-day record,
   headgear or wind surgery first time, draw, trip/going/course clues in the comment. Give a one-line reason
   that names the card fact. No reason on the card = no change. Do not use outside knowledge of the horses.
3. Keep changes moderate: normally within 0.67x to 1.5x of the market chance; never beyond 0.33x to 3x.
   Totals do not need to add to 100; they are rescaled afterwards.
4. Runners marked CHECK need a verdict, BET or SKIP:
   BET only if (a) your chance x best exchange price >= 1.05 AND (b) best exchange price >= the skip line
   shown (0.95 x 09:00 median), and the card supports your chance. Otherwise SKIP. Give a one-line reason.

Write valid JSON to the out path you were given, exactly this shape (use the exact race_id and horse_id values):
{"meeting": "lingfield", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 1:50 Lingfield | race_id rac_32304059307 | Sharon Knapp Memorial Cup EBF 'National Hunt' Novices' Hurdle Race (Qualifier) (GBB Race)
Hurdle | Class 3 | 2m3f110y | going Good | Turf | 5 runners | rating band - | age 4-6yo
- Port Glen One (hrs_17393456731) | 5yo G | 160lb | OR - | draw 0 | jockey Sam Twiston-Davies | trainer Nigel & Willy Twiston-Davies (14d 5/31) | headgear - | last run 33 days | form 1-1 | MARKET 71.7% | 09:00 median 1.29 | best exchange 1.32
- Wild Wescht (hrs_17395223573) | 6yo G | 154lb | OR - | draw 0 | jockey Freddie Gingell | trainer Joe Tizzard (14d 7/25) | headgear - | last run 709 days | form 44/ | MARKET 23.4% | 09:00 median 3.50 | best exchange 4.40
- Templar Knight (hrs_17394543537) | 5yo G | 154lb | OR - | draw 0 | jockey Joe Anderson(3) | trainer Oliver Signy (14d 0/4) | headgear h (1st time) | last run 7 days | form 6 | MARKET 2.8% | 09:00 median 26.00 | best exchange 44.00
- Storm Dudley (hrs_63809494) | 4yo G | 153lb | OR - | draw 0 | jockey David Bass | trainer David Weston (14d 0/0) | headgear - | last run 157 days | form 8 | MARKET 1.2% | 09:00 median 51.00 | best exchange 130.00
- Unknown Stranger (hrs_52236422) | 5yo G | 154lb | OR - | draw 0 | jockey Richie McLernon | trainer Jim & Suzi Best (14d 0/9) | headgear - | last run 20 days | form /44-PP | MARKET 0.8% | 09:00 median 101.00 | best exchange 250.00

## 2:20 Lingfield | race_id rac_32304063181 | Get The Inside Track With raceday-ready.com Mares' Handicap Hurdle Race
Hurdle | Class 4 | 2m3f110y | going Good | Turf | 5 runners | rating band 0-115 | age 3yo+
- Kamille Au Kanada (hrs_52495359) | 6yo M | 172lb | OR 108 | draw 0 | jockey Chad Bament(5) | trainer Anthony Honeyball (14d 4/37) | headgear t | last run 4 days | form 2-1511 | MARKET 42.3% | 09:00 median 2.10 | best exchange 2.30
    comment: Kamille Au Kanada arrives in cracking nick, a winner last time out and a winner two starts back, with three wins in her last five starts and experience of today's trip and going. The main risk is a quick turnaround after only four days, and 172 lb is a big weight to carry.
- Ride Like A Girl (hrs_46547165) | 5yo M | 165lb | OR 108 | draw 0 | jockey Gavin Sheehan | trainer Jamie Snowden (14d 8/21) | headgear t | last run 24 days | form -12212 | MARKET 21.8% | 09:00 median 4.00 | best exchange 4.60
    comment: Ride Like A Girl has finished in the first two in all five recent runs, second last time out and a winner two starts back, and she returns after 24 days with a yard in form. She has run on today's going, though 165 lb is a stiff burden.
- Miss Carbo (hrs_59399599) | 4yo F | 163lb | OR 107 | draw 0 | jockey Bradley Harris(3) | trainer Neil Mulholland (14d 6/25) | headgear h | last run 31 days | form 7615-4 | MARKET 13.3% | 09:00 median 7.00 | best exchange 7.40
    comment: Fourth last time out and a winner three starts back, Miss Carbo has run over today's trip and going before, and fits as a leading danger after 31 days off. Our rating of 110 ranks her third of five, though 163 lb is a hefty burden to carry.
- Basilette (hrs_33110511) | 7yo M | 166lb | OR 102 | draw 0 | jockey Daniel Sansom(3) | trainer Seamus Mullins (14d 2/8) | headgear - | last run 5 days | form -41331 | MARKET 11.9% | 09:00 median 7.00 | best exchange 9.20
    comment: Basilette arrives in cracking order, a winner last time out and again four starts back, with two wins in her last five and a quick return after just five days; she has run over today's trip and going before. The risk is the 166 lb she carries, a hefty burden.
- Reel Orange (hrs_412694800) | 7yo M | 156lb | OR 99 | draw 0 | jockey Freddie Gingell | trainer Joe Tizzard (14d 7/25) | headgear tp | last run 32 days | form 1-2141 | MARKET 10.7% | 09:00 median 8.50 | best exchange 9.40
    comment: Three wins in her last five, including last time out, is strong form, but Reel Orange carries 156 lb off 99 and is ranked fifth of five on our figures. She has run over today's trip and going, and the yard is in form, though a 32-day break and that big weight make her hard to fancy.

## 2:50 Lingfield | race_id rac_32304065118 | Careersinracing Step On Track Programme Handicap Hurdle Race
Hurdle | Class 5 | 2m0f0y | going Good | Turf | 9 runners | rating band 0-100 | age 3yo+
- Western Soldier (hrs_24216962) | 8yo G | 159lb | OR 82 | draw 0 | jockey Callum Pritchard | trainer Seamus Mullins (14d 2/8) | headgear - | last run 26 days | form -45P45 | MARKET 22.3% | 09:00 median 4.00 | best exchange 4.20 | CHECK (skip line 3.80)
    comment: Western Soldier is winless in his last five, though a fifth last time out and a fourth two starts back show him competitive, and he has run over today's trip and going after 26 days off. Carrying 159 lb off 82 is a stiff ask, and our rating of 87 only ranks him fifth of nine.
- Zaraquelle (hrs_44721733) | 4yo F | 167lb | OR 90 | draw 0 | jockey Mr Alex Chadwick(3) | trainer James Owen (14d 14/50) | headgear t | last run 13 days | form 42-24 | MARKET 16.8% | 09:00 median 4.50 | best exchange 6.40
    comment: Zaraquelle is consistent, with a fourth last time out, a second two starts back, and a second three starts back, and she's fresh from a 13-day break with a yard in form (14/50 over the last 14 days). She has run over today's trip and going, though she's yet to win in her last four starts, and 167 lb is the main risk.
- Diamond Days (hrs_46449795) | 6yo G | 161lb | OR 84 | draw 0 | jockey Freddie Gingell | trainer Joe Tizzard (14d 7/25) | headgear p | last run 8 days | form 55P-4F | MARKET 12.6% | 09:00 median 7.00 | best exchange 7.40
    comment: Diamond Days is winless in his last five, with a fall last time out and a pulled up three starts back, though a fourth two starts back shows some promise. He has run over today's trip and going and returns after eight days, with the yard in form, but 161 lb is a hefty burden.
- Castle Quarter (hrs_15233358) | 10yo G | 159lb | OR 82 | draw 0 | jockey Richie McLernon | trainer Neil Mulholland (14d 6/25) | headgear v | last run 26 days | form 753023 | MARKET 12.2% | 09:00 median 6.50 | best exchange 8.60
    comment: Castle Quarter has been placed in two of his last three, a third last time out and a second two starts back, yet he is still winless in his last six and ranks eighth of nine on our figures. He has run over today's trip and going, but 159 lb is a hefty burden.
- Foinix (hrs_30441110) | 6yo G | 156lb | OR 79 | draw 0 | jockey Sean Bowen | trainer Jim & Suzi Best (14d 0/9) | headgear - | last run 6 days | form 5565- | MARKET 10.9% | 09:00 median 8.00 | best exchange 9.00
    comment: Foinix is hard to fancy, having finished fifth, sixth, fifth and fifth in his last four starts, yet to win in that spell, and he carries 156 lb off an official mark of 79. He has run over today's trip and is back quickly after six days, but our rating of 61 ranks him last of nine.
- Raffles Nobu (hrs_37380882) | 6yo G | 164lb | OR 87 | draw 0 | jockey Nathan Andrews(10) | trainer Nick Scholfield (14d 0/19) | headgear tb | last run 15 days | form 352577 | MARKET 8.8% | 09:00 median 9.50 | best exchange 11.00
    comment: Raffles Nobu is fit enough after 15 days off and has run over today's trip and going, with a second four starts back and a third six starts back showing he can get involved. Two sevenths in his last two outings are the worry, though, and he is still yet to win in recent form.
- Dotties Star (hrs_32278421) | 7yo G | 163lb | OR 86 | draw 0 | jockey Sean Houlihan | trainer Pat Phelan (14d 0/4) | headgear - | last run 22 days | form 8P42-5 | MARKET 7.2% | 09:00 median 12.00 | best exchange 13.50
    comment: Dotties Star has shown solid recent form, with a second two starts back and a fifth last time out, and he returns after 22 days having run over today's trip and going before. Our rating of 92 makes him the one to beat, though he is yet to win in his last five and carries 163 lb.
- Most Wanted (hrs_32401761) | 8yo G | 158lb | OR 81 | draw 0 | jockey Tom Cannon | trainer David Bridgwater (14d 0/1) | headgear v | last run 24 days | form 372593 | MARKET 5.9% | 09:00 median 15.00 | best exchange 16.00
    comment: Most Wanted showed up well when third last time out, and he has run over today's trip and on this going, while our rating of 90 ranks him third of nine. The main risk is a winless run in his last six and a hefty 158 lb to carry.
- Play On Court (hrs_58099405) | 5yo G | 167lb | OR 90 | draw 0 | jockey James Best | trainer Harriet Dickin (14d 0/6) | headgear b | last run 34 days | form P46-77 | MARKET 3.2% | 09:00 median 26.00 | best exchange 34.00
    comment: Winless in his last five, Play On Court has finished seventh in his last two outings and was pulled up five starts back, so he is hard to fancy, especially carrying 167 lb off an official mark of 90. He has run over today's trip and going, and a 34-day break may help.

## 3:20 Lingfield | race_id rac_32304067055 | Tips For Every Race At raceday-ready.com Handicap Hurdle Race
Hurdle | Class 5 | 2m7f0y | going Good | Turf | 5 runners | rating band 0-105 | age 4yo+
- Sailing By (hrs_56559342) | 5yo G | 150lb | OR 87 | draw 0 | jockey Freddie Gingell | trainer Joe Tizzard (14d 7/25) | headgear - | last run 20 days | form 7447-3 | MARKET 44.2% | 09:00 median 2.00 | best exchange 2.20
    comment: Winless in his last five, Sailing By is hard to fancy as the outsider of five on our figures, though a third last time out, 20 days ago, is a step up on a seventh two starts back. Trainer's 7 from 25 in the last 14 days is a plus, and he carries 150 lb.
- Cinnodin (hrs_31698009) | 6yo G | 167lb | OR 104 | draw 0 | jockey Gavin Sheehan | trainer Jamie Snowden (14d 8/21) | headgear b | last run 35 days | form 12P041 | MARKET 20.5% | 09:00 median 4.33 | best exchange 4.80
    comment: Cinnodin won last time out and has run over today's trip and on the going before, while his trainer's yard is flying at 8 from 21 in the last 14 days. A 35-day break and 167 lb are the only reservations, but his overall profile makes him our pick.
- Betty's Tiara (hrs_32567801) | 8yo M | 166lb | OR 103 | draw 0 | jockey Ben Jones | trainer Ben Pauling (14d 4/30) | headgear tv | last run 13 days | form 981523 | MARKET 20.2% | 09:00 median 4.33 | best exchange 4.90
    comment: Third last time out and a second the run before, Betty's Tiara is bang in form, fresh from a run just 13 days ago, and she has run over today's trip and on this going before. Carrying 166 lb is the main risk, though our 110 rating, the best of the five, backs her.
- Robber's Bridge (hrs_30245712) | 8yo G | 168lb | OR 105 | draw 0 | jockey Mr Sam Burton(7) | trainer Dan Horsford (14d 0/6) | headgear h | last run 233 days | form 331P5- | MARKET 11.7% | 09:00 median 8.00 | best exchange 8.00
    comment: Robber's Bridge has a win and two thirds in his last five starts, with a winner three starts back, and he has run over today's trip and going before. The main risk is a 233-day absence, and he also carries 168 lb after a fifth last time out.
- One Cool Dreamer (hrs_36614928) | 5yo G | 154lb | OR 91 | draw 0 | jockey Robert Dunne | trainer Robert Stephens (14d 1/5) | headgear p | last run 30 days | form 425-0 | MARKET 3.3% | 09:00 median 26.00 | best exchange 32.00
    comment: One Cool Dreamer looks a leading threat, with a second three starts back and a fifth two runs ago, while our rating of 104 sits well clear of his official mark of 91 and he has run on today's going before. The risk is a disappointing unplaced effort last time out, and he carries 154 lb after 30 days off.

## 3:50 Lingfield | race_id rac_32304068992 | Download The Racecourse App Raceday Ready Handicap Hurdle Race
Hurdle | Class 4 | 2m7f0y | going Good | Turf | 6 runners | rating band 0-115 | age 4yo+
- Rebel Tribesman (hrs_52495856) | 5yo G | 168lb | OR 116 | draw 0 | jockey Gavin Sheehan | trainer Jamie Snowden (14d 8/21) | headgear - | last run 27 days | form 121321 | MARKET 44.2% | 09:00 median 2.00 | best exchange 2.16
    comment: Rebel Tribesman has finished in the first three in all of his last six starts, winning last time out and a first four starts back, and he has run over today's trip and going before, with his yard in form. The main risk is the 168 lb he carries, a hefty burden to shoulder.
- Spike Jones (hrs_26459993) | 9yo G | 162lb | OR 110 | draw 0 | jockey Benjamin Macey(5) | trainer Samuel Drinkwater (14d 1/4) | headgear tp | last run 264 days | form 3F747- | MARKET 17.9% | 09:00 median 4.50 | best exchange 5.90
    comment: Spike Jones has run over today's trip and going before, and his fourth two starts back plus a third five runs ago show he can reach the frame, while 162 lb is a big weight but he is rated 120 by us, second of six. The main risk is fitness, as he is back after 264 days and a seventh last time out.
- Secret Trix (hrs_27578957) | 9yo G | 168lb | OR 116 | draw 0 | jockey Lewis Saunders(5) | trainer Olly Murphy (14d 7/37) | headgear t | last run 46 days | form -32244 | MARKET 14.1% | 09:00 median 6.00 | best exchange 7.20
    comment: Consistent sort who has hit the frame in three of his last five, including a second three starts back and another second four starts back, and he has run over today's trip and going before. Fourth last time out and 46 days off are minor queries, but our 125 rating makes him the one to beat despite 168 lb.
- D'Jo Dela Barriere (hrs_35148904) | 7yo G | 156lb | OR 104 | draw 0 | jockey Miss Eleanor Williams(7) | trainer Mrs C. Williams (14d 3/30) | headgear - | last run 15 days | form 5565-1 | MARKET 11.3% | 09:00 median 8.00 | best exchange 8.60
    comment: D'Jo Dela Barriere won last time out after four straight efforts of fifth or sixth, and returns just 15 days later with experience of today's trip and going. The main risk is the 156 lb he carries, which leaves little margin for a rise in the weights.
- That's It Paddy (hrs_61684714) | 5yo G | 163lb | OR 111 | draw 0 | jockey Joe Anderson(3) | trainer Grace Harris (14d 2/12) | headgear - | last run 31 days | form 4P-646 | MARKET 7.9% | 09:00 median 11.00 | best exchange 12.50
    comment: Winless in his last five, That's It Paddy was sixth last time out and a sixth three starts back, with a pulled up four starts back, so he is hard to fancy; he has run on today's going and carries 163 lb, while our rating of 104 ranks him last of six.
- Lacrima (hrs_45920595) | 5yo G | 158lb | OR 106 | draw 0 | jockey Nathan Andrews(10) | trainer Nick Scholfield (14d 0/19) | headgear t | last run 49 days | form 845145 | MARKET 4.7% | 09:00 median 19.00 | best exchange 21.00
    comment: Lacrima was fifth last time out and fourth two starts back, with a winner three starts back his one success in his last six outings; he returns after 49 days off carrying 158 lb. He has run over today's trip and going, but our figures rank him fifth of six, so he is hard to fancy.
