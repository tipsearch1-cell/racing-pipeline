# Card review packet: Market Rasen, 2026-11-12

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
{"meeting": "market_rasen", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 12:06 Market Rasen | race_id rac_32304235574 | PricedUp Bet Maiden Hurdle Race (GBB Race)
Hurdle | Class 4 | 2m0f125y | going Good To Soft | Turf | 10 runners | rating band - | age 4yo+
- Ballydine Boy (hrs_59186575) | 5yo G | 158lb | OR - | draw 0 | jockey Sean Bowen | trainer Olly Murphy (14d 10/41) | headgear - | last run 22 days | form 614-1 | MARKET 43.3% | 09:00 median 1.91 | Matchbook -
- Northern Olympian (hrs_412712006) | 5yo G | 158lb | OR - | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 21/93) | headgear - | last run 36 days | form 3 | MARKET 30.9% | 09:00 median 2.50 | Matchbook -
- Show Your Hand (hrs_56559566) | 4yo G | 158lb | OR - | draw 0 | jockey Brian Hughes | trainer Adrian Keatley (14d 1/4) | headgear t | last run 117 days | form 02-2P3 | MARKET 10.7% | 09:00 median 7.00 | Matchbook -
- Wyrley Birch (hrs_52021340) | 6yo G | 158lb | OR - | draw 0 | jockey Tom Bellamy | trainer Alan King (14d 1/17) | headgear - | last run 249 days | form 6- | MARKET 4.8% | 09:00 median 17.00 | Matchbook -
- Silver Salver (hrs_63618261) | 4yo G | 158lb | OR - | draw 0 | jockey Danny McMenamin | trainer Joel Parkinson & Sue Smith (14d 0/12) | headgear - | last run 18 days | form 2-84 | MARKET 3.9% | 09:00 median 17.00 | Matchbook -
- Yafaarr (hrs_39960508) | 4yo G | 158lb | OR - | draw 0 | jockey Jonathan England | trainer Sam England (14d 4/20) | headgear t | last run 17 days | form - | MARKET 3.1% | 09:00 median 26.00 | Matchbook -
- Ricky Roma (hrs_17393891662) | 4yo G | 158lb | OR - | draw 0 | jockey Charlie Todd | trainer Dan Skelton (14d 21/93) | headgear - | last run 10 days | form P | MARKET 1.1% | 09:00 median 67.00 | Matchbook -
- Icy Glen (hrs_57758428) | 5yo G | 158lb | OR - | draw 0 | jockey Peter Kavanagh | trainer Joel Parkinson & Sue Smith (14d 0/12) | headgear - | last run 356 days | form 60- | MARKET 1.0% | 09:00 median 81.00 | Matchbook -
- Equi Libre (hrs_61874456) | 4yo G | 158lb | OR - | draw 0 | jockey Robert Dunne | trainer Dan Skelton (14d 21/93) | headgear h | last run 18 days | form 03-PR7 | MARKET 0.8% | 09:00 median 81.00 | Matchbook -
- Treshnish Point (hrs_17391215324) | 5yo G | 158lb | OR - | draw 0 | jockey Sean Quinlan | trainer L J Morgan (14d 0/7) | headgear - | last run 10 days | form 060 | MARKET 0.3% | 09:00 median 201.00 | Matchbook -

## 12:41 Market Rasen | race_id rac_32304237511 | PricedUp Now With Best Odds 'National Hunt' Maiden Hurdle Race (GBB Race)
Hurdle | Class 4 | 2m4f139y | going Good To Soft | Turf | 9 runners | rating band - | age 4yo+
- Eastern Rock (hrs_52495303) | 5yo G | 158lb | OR - | draw 0 | jockey Ben Jones | trainer Emma Lavelle (14d 1/14) | headgear - | last run 22 days | form P12-4 | MARKET 36.6% | 09:00 median 2.25 | Matchbook -
- Ivor Bear (hrs_60250071) | 4yo G | 157lb | OR - | draw 0 | jockey Sam Twiston-Davies | trainer Nigel & Willy Twiston-Davies (14d 5/31) | headgear - | last run 26 days | form 422-2 | MARKET 33.6% | 09:00 median 2.50 | Matchbook -
- Supreme Force (hrs_17395264250) | 5yo G | 158lb | OR - | draw 0 | jockey Brian Hughes | trainer Charlie Longsdon (14d 6/14) | headgear - | last run 192 days | form P115-1 | MARKET 14.5% | 09:00 median 5.50 | Matchbook -
- Striking Midnight (hrs_58686831) | 4yo G | 157lb | OR - | draw 0 | jockey Danny McMenamin | trainer Joel Parkinson & Sue Smith (14d 0/12) | headgear - | last run 21 days | form 32-9 | MARKET 4.3% | 09:00 median 15.00 | Matchbook -
- Jack The Master (hrs_63323575) | 4yo G | 157lb | OR - | draw 0 | jockey Ciaran Gethings | trainer Henry Daly (14d 1/10) | headgear - | last run 222 days | form 4- | MARKET 3.2% | 09:00 median 21.00 | Matchbook -
- Definite Call (hrs_30454494) | 8yo G | 158lb | OR - | draw 0 | jockey Tom Bellamy | trainer Sara Bradstock (14d 0/0) | headgear - | last run 328 days | form U13/P- | MARKET 3.1% | 09:00 median 21.00 | Matchbook -
- Zains Hope (hrs_62615091) | 5yo G | 158lb | OR - | draw 0 | jockey Tom Midgley(3) | trainer Nick Kent (14d 0/7) | headgear - | last run 240 days | form 5- | MARKET 2.7% | 09:00 median 29.00 | Matchbook -
- Jax Belle (hrs_55148618) | 6yo M | 151lb | OR - | draw 0 | jockey David Noonan | trainer Lucy Wadham (14d 1/5) | headgear - | last run 14 days | form 036-6 | MARKET 1.1% | 09:00 median 67.00 | Matchbook -
- Prince of Clova (hrs_58196544) | 5yo G | 158lb | OR - | draw 0 | jockey Charlie Maggs | trainer Peter Niven (14d 1/5) | headgear - | wind surgery | last run 230 days | form 5P0- | MARKET 0.9% | 09:00 median 126.00 | Matchbook -

## 1:16 Market Rasen | race_id rac_32304239448 | PricedUp Boosted Prices Daily Novices' Handicap Steeple Chase (GBB Race)
Chase | Class 4 | 2m7f191y | going Good To Soft | Turf | 6 runners | rating band 0-110 | age 4yo+
- Tell The Tale (hrs_41052879) | 6yo G | 156lb | OR 101 | draw 0 | jockey Conor O'Farrell | trainer Neil Mulholland (14d 5/25) | headgear - | last run 29 days | form 647-21 | MARKET 38.1% | 09:00 median 2.20 | Matchbook -
- Chemoulin (hrs_59150651) | 6yo G | 164lb | OR 109 | draw 0 | jockey Sam Twiston-Davies | trainer Charlie Longsdon (14d 6/14) | headgear t | last run 226 days | form 5414- | MARKET 16.2% | 09:00 median 5.50 | Matchbook -
    comment: Chemoulin showed he can win when successful two starts back, and he has run on today's going before, following that with a fourth last time out.
- Firm But Fair (hrs_51831773) | 5yo G | 165lb | OR 110 | draw 0 | jockey Paul O'Brien | trainer Harry Derham (14d 6/21) | headgear t (1st time) | last run 240 days | form /2333- | MARKET 15.1% | 09:00 median 6.00 | Matchbook -
    comment: Firm But Fair has been placed in all four recent runs, third last time out, a third two starts back, a third three starts back and a second four starts back, and he has run over today's trip and going before, with the yard in form. The one concern is a 240-day absence, so fitness is the main risk.
- Another High Five (hrs_41052396) | 6yo G | 157lb | OR 102 | draw 0 | jockey Derek Fox | trainer Lucinda Russell & Michael Scudamore (14d 10/47) | headgear p | last run 49 days | form 3225-8 | MARKET 13.1% | 09:00 median 7.00 | Matchbook -
    comment: Another High Five is yet to win in his last five starts, but he's been in the frame three times in that spell, including a second three starts back and another second four starts back, and he has run over today's trip and going. Last time's eighth and a 49-day break are the worry, along with 157 lb.
- Western George (hrs_48853931) | 5yo G | 158lb | OR 103 | draw 0 | jockey Jonjo O'Neill Jr. | trainer Jonjo & A.J. O'Neill (14d 5/41) | headgear - | last run 32 days | form 855-24 | MARKET 11.4% | 09:00 median 7.50 | Matchbook -
    comment: Western George arrives in solid recent form, a fourth last time out and a second two starts back, and he has run over today's trip and going before.
- Catwalk Girl (hrs_49757855) | 6yo M | 165lb | OR 110 | draw 0 | jockey Mr James King(3) | trainer Max Comley (14d 3/10) | headgear - | last run 184 days | form 53F-13 | MARKET 6.2% | 09:00 median 13.00 | Matchbook -
    comment: Third last time out and a winner two starts back, Catwalk Girl has a decent recent profile and has run over today's trip, but a 184-day absence and 165 lb are big asks.

## 1:51 Market Rasen | race_id rac_32304241385 | Lincolnshire Rural Support Network Handicap Steeple Chase
Chase | Class 5 | 2m5f89y | going Good To Soft | Turf | 7 runners | rating band 0-100 | age 4yo+
- Noble Recall (hrs_39315136) | 7yo G | 149lb | OR 81 | draw 0 | jockey Isabelle Ryder(5) | trainer Anthony Day (14d 0/0) | headgear - | last run 18 days | form -P1312 | MARKET 25.2% | 09:00 median 3.50 | Matchbook - | CHECK (skip line 3.32)
    comment: Noble Recall has been in cracking form, second last time out and a winner two starts back, with 18 days since that run and previous experience on today's going.
- Miss Denver (hrs_48818973) | 6yo M | 157lb | OR 89 | draw 0 | jockey Sam Twiston-Davies | trainer Nigel & Willy Twiston-Davies (14d 5/31) | headgear - | last run 30 days | form 322222 | MARKET 21.1% | 09:00 median 4.00 | Matchbook -
    comment: Miss Denver arrives in rock-solid form, runner-up last time out and in each of her four starts before that, plus a third six starts back, and she has run on today's going before. Yet to win in that spell, though, and carrying 157 lb off 89 is the main risk.
- Crac de Megaudais (hrs_35796593) | 7yo G | 147lb | OR 79 | draw 0 | jockey Conor O'Farrell | trainer Tom Gretton (14d 0/1) | headgear t | last run 26 days | form 4P-341 | MARKET 16.9% | 09:00 median 5.00 | Matchbook -
    comment: Crac de Megaudais won last time out and has run over today's trip and going, but a fourth two starts back and a pulled up four runs ago show some inconsistency.
- Calli Black (hrs_30454564) | 8yo M | 148lb | OR 80 | draw 0 | jockey Ciaran Gethings | trainer David Weston (14d 0/1) | headgear t | last run 31 days | form 577-85 | MARKET 13.4% | 09:00 median 6.50 | Matchbook -
    comment: The risk is a winless run, with nothing better than a fifth in her last five starts.
- Bongo Man (hrs_38809596) | 6yo G | 166lb | OR 98 | draw 0 | jockey Sean Bowen | trainer Billy Aprahamian (14d 0/5) | headgear t | last run 174 days | form 3P27-4 | MARKET 11.2% | 09:00 median 8.00 | Matchbook -
    comment: The main risk is that long absence, with a seventh two starts back and a 166 lb burden to carry.
- Boys of Wexford (hrs_24769822) | 9yo G | 149lb | OR 81 | draw 0 | jockey David Noonan | trainer Henry Oliver (14d 1/5) | headgear v | last run 15 days | form P41-P5 | MARKET 6.3% | 09:00 median 14.00 | Matchbook -
    comment: Boys of Wexford is hard to fancy, with two pulled-up efforts in his last five and only a fifth last time out, though he did win three starts back and has run over today's trip and going.
- Riviera Walk (hrs_40553849) | 6yo M | 168lb | OR 100 | draw 0 | jockey Jonjo O'Neill Jr. | trainer Jonjo & A.J. O'Neill (14d 5/41) | headgear - | last run 16 days | form F1P-UP | MARKET 5.8% | 09:00 median 15.00 | Matchbook -
    comment: Riviera Walk is a winner four starts back and has run on today's going, and she's fresh enough after 16 days off, though her last three runs have ended in a pulled up, an unseated and another pulled up. Our 107 puts her top of the seven despite 168 lb, with an official 100.

## 2:26 Market Rasen | race_id rac_32304243322 | NFU Mutual Agriculture Raceday Novices' Handicap Hurdle Race
Hurdle | Class 5 | 2m4f139y | going Good To Soft | Turf | 6 runners | rating band 0-100 | age 3yo+
- Teofimo (hrs_412693071) | 5yo G | 168lb | OR 100 | draw 0 | jockey Ryan Mania | trainer Adam Nicol (14d 0/14) | headgear t | last run 7 days | form /76-32 | MARKET 25.5% | 09:00 median 3.25 | Matchbook - | CHECK (skip line 3.09)
    comment: Teofimo arrives in good heart, second last time out and third two starts back, and he turns out quickly again just seven days later.
- Stylia (hrs_41190093) | 6yo M | 153lb | OR 85 | draw 0 | jockey Sean Bowen | trainer Olly Murphy (14d 10/41) | headgear p (1st time) | last run 544 days | form 443/2- | MARKET 23.9% | 09:00 median 3.50 | Matchbook -
    comment: Stylia is winless in her last four, though a second last time out and a third two starts back show she can get involved; the 544-day absence is the big worry, and she has run on today's going before.
- This Sway (hrs_53328443) | 5yo G | 162lb | OR 94 | draw 0 | jockey Freddie Mitchell(3) | trainer Max Comley (14d 3/10) | headgear - | last run 163 days | form 143-22 | MARKET 23.3% | 09:00 median 3.90 | Matchbook -
    comment: This Sway has finished second in each of his last two outings, and a third and a fourth before that, so he arrives in solid recent form and has run over today's trip and going before.
- Bouboule (hrs_48700470) | 4yo G | 142lb | OR 75 | draw 0 | jockey Sean Quinlan | trainer Gillian Boanas (14d 0/1) | headgear tb | last run 16 days | form -76553 | MARKET 12.0% | 09:00 median 7.50 | Matchbook -
    comment: Bouboule is yet to win in his last five starts, though a third last time out, after a fifth two starts back, a fifth three starts back and a sixth four starts back, hints at a slight upturn.
- C'Est Pour Moi (hrs_56559433) | 4yo G | 154lb | OR 87 | draw 0 | jockey Amber Jackson-Fennell(7) | trainer Nigel & Willy Twiston-Davies (14d 5/31) | headgear - | last run 17 days | form 96783 | MARKET 9.0% | 09:00 median 10.00 | Matchbook -
    comment: The risk is a modest recent record, with an eighth, a seventh, a sixth and a ninth before that, and he carries 154 lb.
- Toby Two Scoops (hrs_42780738) | 4yo G | 158lb | OR 91 | draw 0 | jockey Brian Hughes | trainer Micky Hammond (14d 1/13) | headgear b | last run 215 days | form 23P2P- | MARKET 6.3% | 09:00 median 15.00 | Matchbook -
    comment: Toby Two Scoops showed his best with a second two starts back and a third four starts back, and he's rated 92 by us, a point above his official mark of 91, but he was pulled up last time and returns after 215 days off, so rust is the main risk under 158 lb.

## 3:01 Market Rasen | race_id rac_32304245259 | PricedUp Boosts And BOG Mares' Handicap Hurdle Race
Hurdle | Class 5 | 2m7f16y | going Good To Soft | Turf | 8 runners | rating band 0-100 | age 4yo+
- Burning Embers (hrs_57439242) | 5yo M | 162lb | OR 90 | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 21/93) | headgear p | last run 24 days | form 466-62 | MARKET 22.3% | 09:00 median 3.75 | Matchbook - | CHECK (skip line 3.56)
    comment: Burning Embers is winless in her last five starts, though a second last time out, 24 days ago, is a lift after three sixths on the spin before that.
- Reflection of You (hrs_37701342) | 7yo M | 162lb | OR 90 | draw 0 | jockey Derek Fox | trainer Lucinda Russell & Michael Scudamore (14d 10/47) | headgear p | last run 49 days | form 3P13-4 | MARKET 16.9% | 09:00 median 5.00 | Matchbook -
    comment: Fourth last time out, a third before that, and a winner three starts back, she's been in the mix lately, and she has run over today's trip and going.
- Briery Butterfly (hrs_39020926) | 7yo M | 165lb | OR 93 | draw 0 | jockey Sam Twiston-Davies | trainer Henry Daly (14d 1/10) | headgear - | last run 186 days | form 223F-4 | MARKET 14.4% | 09:00 median 6.00 | Matchbook -
    comment: Briery Butterfly shaped with plenty of promise in recent form, a fourth last time out, a third three starts back and two seconds before that, and she has run over today's trip and going. The main risk is a 186-day absence, and a weight of 165 lb adds to the task.
- Fireball Frenzy (hrs_40919984) | 6yo M | 167lb | OR 95 | draw 0 | jockey Charlie Hammond | trainer Stuart Edmunds (14d 1/11) | headgear p (1st time) | last run 21 days | form 1P2/5 | MARKET 13.0% | 09:00 median 6.50 | Matchbook -
    comment: Fireball Frenzy arrives fresh from a three-week break, having finished fifth last time out, with a second two starts back and a win four starts back showing she can deliver.
- Seasmoke (hrs_29523333) | 8yo M | 161lb | OR 89 | draw 0 | jockey Sean Bowen | trainer Billy Aprahamian (14d 0/5) | headgear t | last run 215 days | form 23333- | MARKET 11.1% | 09:00 median 7.50 | Matchbook -
    comment: Seasmoke has been placed in each of her last five runs, a third last time out, a third two starts back, a third three starts back, a third four starts back, and a second five starts back, and she has run over today's trip and going.
- It's Maisy (hrs_30726213) | 8yo M | 168lb | OR 96 | draw 0 | jockey Oscar Palmer(7) | trainer Joel Parkinson & Sue Smith (14d 0/12) | headgear - | last run 194 days | form 2431-8 | MARKET 10.3% | 09:00 median 8.50 | Matchbook -
    comment: The risk is a 194-day absence, plus an eighth last time out.
- Diamond Grace (hrs_51434425) | 5yo M | 167lb | OR 95 | draw 0 | jockey Jonjo O'Neill Jr. | trainer Jonjo & A.J. O'Neill (14d 5/41) | headgear - | last run 79 days | form 5-325 | MARKET 6.3% | 09:00 median 14.00 | Matchbook -
    comment: Diamond Grace has been consistent without a win, finishing a fifth last time out, a second two starts back and a third three starts back, but she returns after 79 days off and carries 167 lb off an official mark of 95.
- Bits Ballou (hrs_59895682) | 5yo M | 153lb | OR 81 | draw 0 | jockey James Turner(5) | trainer Nigel & Willy Twiston-Davies (14d 5/31) | headgear - | last run 17 days | form -42314 | MARKET 5.7% | 09:00 median 15.00 | Matchbook -
    comment: Bits Ballou was a fourth last time out, 17 days ago, and her win came two starts back, so the form is respectable without being compelling.

## 3:36 Market Rasen | race_id rac_32304247196 | PricedUp Bet Handicap Hurdle Race
Hurdle | Class 4 | 2m0f125y | going Good To Soft | Turf | 7 runners | rating band 0-120 | age 3yo+
- Tilehurst (hrs_46046000) | 5yo G | 157lb | OR 109 | draw 0 | jockey Sean Bowen | trainer Neil Mulholland (14d 5/25) | headgear p | last run 51 days | form 4-5123 | MARKET 27.4% | 09:00 median 3.00 | Matchbook - | CHECK (skip line 2.85)
    comment: Tilehurst arrives in decent order, third last time out and second the run before, with a winner three starts back, and he has run over today's trip and going before.
- Ballygeary (hrs_29522605) | 9yo G | 154lb | OR 106 | draw 0 | jockey Joshua Thompson(5) | trainer Mike Sowersby (14d 0/5) | headgear t | last run 26 days | form 535512 | MARKET 22.4% | 09:00 median 4.00 | Matchbook -
    comment: Ballygeary showed up well with a second last time out and a win two starts back, but a fifth three starts back and another fifth four starts back sit in the mix, and 154 lb is a big weight to carry.
- St Faz (hrs_32290839) | 6yo G | 168lb | OR 120 | draw 0 | jockey Oakley Brown(5) | trainer Adrian Keatley (14d 1/4) | headgear tp | last run 117 days | form 5746-P | MARKET 20.3% | 09:00 median 4.33 | Matchbook -
    comment: St Faz has run over today's trip and going before, and his last-time pull-up follows a sixth two runs ago and a fourth three starts back, leaving him without a win in his last five.
- Moutarde (hrs_36824116) | 5yo G | 154lb | OR 106 | draw 0 | jockey Dylan Johnston | trainer Syd Hosie (14d 1/6) | headgear t | wind surgery | last run 234 days | form P8P52- | MARKET 10.7% | 09:00 median 8.00 | Matchbook -
    comment: The main risk is a 234-day absence, with two pulled-up efforts in his last five starts.
- Time In A Bottle (hrs_40225311) | 6yo M | 155lb | OR 107 | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 21/93) | headgear ht | last run 58 days | form 226F-6 | MARKET 9.9% | 09:00 median 8.50 | Matchbook -
    comment: Without a win in her last five outings, Time In A Bottle was sixth last time out after a fall two starts back, and she has been off 58 days; a second four starts back is the best of it.
- Pigeon House (hrs_30124724) | 6yo G | 163lb | OR 115 | draw 0 | jockey Sean Quinlan | trainer Charles & Adam Pogson (14d 0/2) | headgear p | last run 11 days | form P2P444 | MARKET 4.8% | 09:00 median 17.00 | Matchbook -
    comment: Three straight fourths, the latest just 11 days ago, show Pigeon House is in good heart, and he has run over today's trip and going before.
- Trust House (hrs_35054474) | 6yo G | 168lb | OR 120 | draw 0 | jockey Philip Armson(3) | trainer Jake Thomas Coulson (14d 0/0) | headgear - | last run 153 days | form 511-23 | MARKET 4.5% | 09:00 median 19.00 | Matchbook -
    comment: Trust House arrives in cracking form, a third last time out, a second two starts back, and a winner three starts back and four starts back, and he has run over today's trip and going before. The one concern is a 153-day absence under 168 lb.
