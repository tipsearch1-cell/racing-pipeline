# Card review packet: Dundalk (AW), 2026-11-13

You are a racing form reviewer. Use ONLY this packet. For every race:

1. Start from each runner's MARKET chance (the sharp-weighted 09:00 price, in %).
2. Change a runner's chance ONLY where the card below gives a specific reason: recent form figures, a comment
   or spotlight line, official rating (OR) vs today's weight, days since last run, trainer's 14-day record,
   headgear or wind surgery first time, draw, trip/going/course clues in the comment. Give a one-line reason
   that names the card fact. No reason on the card = no change. Do not use outside knowledge of the horses.
3. Keep changes moderate: normally within 0.67x to 1.5x of the market chance; never beyond 0.33x to 3x.
   Totals do not need to add to 100; they are rescaled afterwards.
4. Runners marked CHECK are the market favourite. Give a verdict, BET or SKIP, with a one-line reason:
   BET unless the card gives a specific reason to doubt the favourite (then lower its chance and SKIP).
   You do not need to do any price arithmetic; the price check (skip line shown) is applied afterwards.

Write valid JSON to the out path you were given, exactly this shape (use the exact race_id and horse_id values):
{"meeting": "dundalk_aw", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 5:30 Dundalk (AW) | race_id rac_32304407967 | Irish Stallion Farms EBF Race
Flat |  | 0m6f0y | going Standard | AW | 11 runners | rating band - | age 2yo
- Crayons In The Sky (hrs_66272213) | 2yo F | 131lb | OR 86 | draw 8 | jockey Jack Kearney | trainer Stephen Thorne (14d 0/4) | headgear - | last run 16 days | form 24241 | MARKET 29.7% | 09:00 median 2.75 | Matchbook 3.00
    comment: Crayons In The Sky arrives fresh from a win last time out just 16 days ago, with a second and a fourth before that, and she has run over today's trip and going.
- Supreme Lord (hrs_62168253) | 2yo G | 136lb | OR 88 | draw 3 | jockey Donagh O'Connor | trainer Robson De Aguiar (14d 0/3) | headgear - | last run 56 days | form 355174 | MARKET 19.3% | 09:00 median 4.00 | Matchbook 4.90
    comment: Supreme Lord has run over today's trip and on this going, and he was a winner three starts back before a fourth last time out.
- Normanton (hrs_17392958177) | 2yo G | 131lb | OR - | draw 11 | jockey Robbie Colgan | trainer David Marnane (14d 2/5) | headgear - | last run 16 days | form 42 | MARKET 13.7% | 09:00 median 6.00 | Matchbook 6.60
    comment: Normanton comes here fresh from a second last time out, and a fourth two starts back, so he's yet to win in recent form but is consistent, and 16 days since his last run suits.
- I Ready (hrs_64846859) | 2yo G | 136lb | OR 84 | draw 7 | jockey Colin Keane | trainer Paul W Flynn (14d 1/3) | headgear - | last run 34 days | form 814203 | MARKET 10.0% | 09:00 median 8.00 | Matchbook 9.20
    comment: The main risk is the 136 lb he carries, off a mark of 84 after 34 days off.
- Scolyer (hrs_17393664288) | 2yo C | 131lb | OR - | draw 4 | jockey Ben Coen | trainer Miss Natalia Lupini (14d 0/5) | headgear - | last run 14 days | form 62 | MARKET 8.1% | 09:00 median 10.00 | Matchbook 12.50
    comment: He has run over today's trip and going, but 131 lb from stall four is a hefty burden.
- Sharpe Ratio (hrs_17395391496) | 2yo C | 131lb | OR - | draw 6 | jockey Declan McDonogh | trainer Joseph Patrick O'Brien (14d 3/27) | headgear - | last run - days | form - | MARKET 6.9% | 09:00 median 12.00 | Matchbook 13.50
    comment: Sharpe Ratio is an unraced colt with no form to go on, so he's an unexposed type with plenty of scope for improvement. He carries 131 lb from stall 6 on debut.
- Sonny Hayes (hrs_17392272926) | 2yo C | 131lb | OR - | draw 1 | jockey W. M. Lordan | trainer Robson De Aguiar (14d 0/3) | headgear - | last run 24 days | form 40 | MARKET 4.8% | 09:00 median 17.00 | Matchbook 19.00
    comment: Sonny Hayes was unplaced last time out, though a fourth two starts back shows he can get involved, and he has run over today's trip.
- Matriarchal (hrs_63323295) | 2yo F | 131lb | OR 84 | draw 5 | jockey Chris Hayes | trainer Josh Halley (14d 0/3) | headgear h | last run 42 days | form 431570 | MARKET 3.0% | 09:00 median 21.00 | Matchbook 42.00
    comment: Matriarchal has run over today's trip and going before, and she was a winner four starts back, with a third five starts back to her credit too. The risk is a slide since, a seventh two starts back then unplaced last time, plus 42 days off and 131 lb from draw 5.
- Waysong (hrs_17393665331) | 2yo G | 131lb | OR - | draw 9 | jockey Adam Grant(7) | trainer Diego Dias (14d 0/1) | headgear - | last run 33 days | form 5 | MARKET 1.6% | 09:00 median 67.00 | Matchbook 60.00
    comment: He has run over today's trip and had a 33-day break, but 131 lb from stall nine is a lot to ask.
- Palo (hrs_17389168958) | 2yo C | 131lb | OR - | draw 10 | jockey Gavin Ryan | trainer Diego Dias (14d 0/1) | headgear - | last run 114 days | form 0 | MARKET 1.5% | 09:00 median 67.00 | Matchbook 65.00
    comment: Carrying 131 lb from stall 10, he looks a midfield sort.
- Cafe Oh Lait (hrs_17393025972) | 2yo F | 126lb | OR - | draw 2 | jockey Killian Leonard | trainer Kevin Thomas Coleman (14d 0/0) | headgear - | last run 16 days | form 7 | MARKET 1.4% | 09:00 median 51.00 | Matchbook 100.00
    comment: On the plus side, she has run over today's trip and going before and is quickly back from draw 2.

## 6:00 Dundalk (AW) | race_id rac_32304409904 | Christmas Party Nights At Dundalk Stadium Handicap
Flat |  | 0m6f0y | going Standard | AW | 10 runners | rating band - | age 3yo+
- Firewalker (hrs_57315881) | 3yo G | 121lb | OR 81 | draw 1 | jockey W. M. Lordan | trainer Robson De Aguiar (14d 0/3) | headgear - | last run 28 days | form -94021 | MARKET 16.1% | 09:00 median 5.00 | Matchbook 6.00 | CHECK (skip line 4.75)
    comment: Winning last time out and a second two starts back is decent form, and he has run over today's trip and going, but he is hard to fancy at 121 lb off an official mark of 81.
- Sir Les Patterson (hrs_38018421) | 5yo G | 140lb | OR 100 | draw 8 | jockey Jack Kearney | trainer Stephen Thorne (14d 0/4) | headgear - | last run 21 days | form 603024 | MARKET 15.0% | 09:00 median 5.00 | Matchbook 6.80
    comment: Fourth last time out and a second two starts back suggest Sir Les Patterson is in decent heart, and he has run over today's trip and going before after 21 days off.
- Chicago Pope (hrs_55061650) | 3yo G | 125lb | OR 85 | draw 9 | jockey Ben Coen | trainer J. P. Murtagh (14d 1/11) | headgear p | last run 29 days | form -21400 | MARKET 13.0% | 09:00 median 6.50 | Matchbook 7.20
    comment: Chicago Pope has been unplaced in his last two starts, though a fourth three starts back and a win four starts back show he can still go well, and he has run over today's trip.
- Caffu Zafeen (hrs_41876688) | 5yo G | 122lb | OR 82 | draw 10 | jockey Nina Doherty(10) | trainer Paul W Flynn (14d 1/3) | headgear - | last run 9 days | form 051111 | MARKET 12.7% | 09:00 median 6.50 | Matchbook 7.40
    comment: Four wins in his last six starts, including a winning run last time out and each of the three runs before that, makes him hard to dismiss, and he is fit after nine days off and has run over today's trip and going.
- City House (hrs_35895608) | 5yo G | 124lb | OR 84 | draw 6 | jockey Patrick McGettigan(5) | trainer Adrian McGuinness (14d 3/21) | headgear tv | last run 14 days | form 725861 | MARKET 11.8% | 09:00 median 7.50 | Matchbook 7.80
    comment: The risk is consistency, as he finished sixth, eighth and fifth in the three runs before that win.
- All The Girls (hrs_56843829) | 3yo F | 120lb | OR 80 | draw 7 | jockey Nicola Burns(5) | trainer T G McCourt (14d 0/1) | headgear tp | last run 14 days | form 825472 | MARKET 9.4% | 09:00 median 9.00 | Matchbook 9.80
    comment: All The Girls was a second last time out and has been fit enough since, back after 14 days, but she is winless in her last six and was only seventh and fourth before that.
- Eddie G (hrs_37576595) | 5yo G | 120lb | OR 80 | draw 5 | jockey Gavin Ryan | trainer Adrian McGuinness (14d 3/21) | headgear t | last run 14 days | form 853203 | MARKET 8.3% | 09:00 median 10.00 | Matchbook 12.00
    comment: Eddie G arrives fit after 14 days, having finished third last time out, and has run over today's trip and going before, but he is winless in his last six and was unplaced two starts back.
- Kerdos (hrs_32129853) | 6yo G | 134lb | OR 94 | draw 2 | jockey Colin Keane | trainer Stephen Thorne (14d 0/4) | headgear b | last run 21 days | form 601919 | MARKET 7.0% | 09:00 median 11.00 | Matchbook 14.50
    comment: The risk is a ninth last time out, and he must now carry 134 lb from stall two.
- Daamberdiplomat (hrs_30469817) | 6yo G | 129lb | OR 89 | draw 3 | jockey Adam Caffrey | trainer Adrian McGuinness (14d 3/21) | headgear h | last run 392 days | form 10761- | MARKET 3.7% | 09:00 median 19.00 | Matchbook 29.00
    comment: The one concern is a 392-day absence, so fitness is the question carrying 129 lb from stall three.
- Frescobaldi (hrs_51766603) | 3yo G | 120lb | OR 80 | draw 4 | jockey Jessica O'Gorman(7) | trainer Daniel James Murphy (14d 1/9) | headgear b | last run 14 days | form 506005 | MARKET 3.1% | 09:00 median 26.00 | Matchbook 32.00

## 6:30 Dundalk (AW) | race_id rac_32304411841 | View Restaurant At Dundalk Stadium Nursery Handicap
Flat |  | 1m0f0y | going Standard | AW | 7 runners | rating band - | age 2yo
- Shenata (hrs_66494022) | 2yo F | 140lb | OR 72 | draw 3 | jockey Ben Coen | trainer J. P. Murtagh (14d 1/11) | headgear - | last run 66 days | form 635 | MARKET 29.9% | 09:00 median 2.88 | Matchbook 2.96
- Closefield Beau (hrs_65869559) | 2yo G | 138lb | OR 70 | draw 2 | jockey Nathan Crosse | trainer Daniel McLoughlin (14d 1/4) | headgear p (1st time) | last run 9 days | form 078441 | MARKET 23.1% | 09:00 median 3.50 | Matchbook 4.00
    comment: The risk is the weight, with 138 lb to carry from stall two off an official mark of 70.
- Mutamarid Lsk (hrs_65869573) | 2yo G | 124lb | OR 56 | draw 1 | jockey James Ryan | trainer Daniel James Murphy (14d 1/9) | headgear b | last run 9 days | form 80042 | MARKET 16.3% | 09:00 median 5.00 | Matchbook 5.70
    comment: He has run over today's trip and going, and carries 124 lb from stall one.
- Rock On Johnny (hrs_66272227) | 2yo G | 126lb | OR 58 | draw 7 | jockey Adam Caffrey | trainer Adrian McGuinness (14d 3/21) | headgear - | last run 12 days | form 850 | MARKET 11.7% | 09:00 median 7.50 | Matchbook 7.40
    comment: Rock On Johnny is winless in his last three, unplaced last time, a fifth two starts back and an eighth three starts back, though he has run over today's trip and is back quickly after 12 days.
- Green Sparkle (hrs_17389036497) | 2yo F | 131lb | OR 63 | draw 5 | jockey Declan McDonogh | trainer Joseph Patrick O'Brien (14d 3/27) | headgear - | last run 43 days | form 9004 | MARKET 7.8% | 09:00 median 11.00 | Matchbook 12.50
    comment: The main risk is that she's yet to win in her last four starts, with 43 days off since her last run.
- Scarlet Dream (hrs_65225090) | 2yo F | 126lb | OR 58 | draw 6 | jockey Colin Keane | trainer Adrian McGuinness (14d 3/21) | headgear - | last run 9 days | form 794576 | MARKET 6.6% | 09:00 median 15.00 | Matchbook 14.50
    comment: The risk is a winless run in her last six, with a sixth last time out and a ninth five starts back.
- Angel Invincible (hrs_17393029101) | 2yo F | 141lb | OR 73 | draw 4 | jockey W. J. Lee | trainer Daniel McLoughlin (14d 1/4) | headgear - | last run 15 days | form 090 | MARKET 4.6% | 09:00 median 19.00 | Matchbook 19.50
    comment: Angel Invincible is winless in her last three, unplaced last time and a ninth two starts back, and she has run over today's trip.

## 7:00 Dundalk (AW) | race_id rac_32304413778 | Book Online At DundalkStadium.com Apprentice Handicap
Flat |  | 1m4f0y | going Standard | AW | 15 runners | rating band 0-60 | age 3yo+
- Deluca Chop (hrs_28532308) | 7yo G | 135lb | OR 53 | draw 1 | jockey Jimmy Dalton(4) | trainer S M Duffy (14d 0/0) | headgear v | last run 49 days | form 211532 | MARKET 14.9% | 09:00 median 5.00 | Matchbook 5.20 | CHECK (skip line 4.75)
    comment: Deluca Chop is in decent recent form, a second last time out and a third two starts back, with a win four starts back and another five starts back, and he has run over today's trip and going before.
- Chant d'Or (hrs_54712329) | 4yo G | 122lb | OR 40 | draw 5 | jockey Conor Cusack(4) | trainer Daniel McLoughlin (14d 1/4) | headgear - | last run 49 days | form 00-705 | MARKET 13.8% | 09:00 median 5.50 | Matchbook 5.50
    comment: Chant d'Or is hard to fancy, winless in his last five with a fifth last time out the best of a modest bunch, and he returns after 49 days off.
- Storm Eric (hrs_27329827) | 7yo G | 141lb | OR 59 | draw 13 | jockey Adam Grant(7) | trainer Jamie Flynn (14d 0/2) | headgear t | last run 7 days | form 823103 | MARKET 11.8% | 09:00 median 5.50 | Matchbook 7.40
    comment: Storm Eric was third last time out and is back quickly after seven days, with a win three starts back and a second five starts back showing he can get involved.
- Doctor Grace (hrs_31188206) | 6yo M | 131lb | OR 49 | draw 7 | jockey Cillian Rowan(7) | trainer Adrian McGuinness (14d 3/21) | headgear v | last run 7 days | form 003904 | MARKET 9.6% | 09:00 median 7.50 | Matchbook 8.60
    comment: Doctor Grace was a fourth last time out just seven days ago, and she has run over today's trip and going, but she is winless in her last six and her best recent effort was a third four starts back.
- Magna Gee Gee (hrs_45193463) | 4yo G | 136lb | OR 54 | draw 3 | jockey Robyn Donaghue-Leahy(2) | trainer Patrick J Flynn (14d 2/8) | headgear - | last run 30 days | form 086310 | MARKET 8.5% | 09:00 median 8.50 | Matchbook 9.00
    comment: Won two starts back and was third the run before, but he was unplaced last time out 30 days ago, and he carries 136 lb.
- In The Minus (hrs_42451850) | 4yo G | 134lb | OR 52 | draw 9 | jockey Sadhbh Tormey(7) | trainer Brian Francis Cawley (14d 0/1) | headgear - | last run 20 days | form 280-50 | MARKET 8.1% | 09:00 median 10.00 | Matchbook 9.80
    comment: The risk is a winless sequence, with unplaced last time out and a fifth two starts back.
- Young Churchill (hrs_40260626) | 5yo G | 139lb | OR 57 | draw 6 | jockey Sam Coen | trainer Richard John O'Brien (14d 0/1) | headgear - | last run 48 days | form 703706 | MARKET 8.1% | 09:00 median 9.50 | Matchbook 9.20
    comment: The risk is a poor recent book, sixth last time out and winless in his last six, plus 48 days off.
- Expound (hrs_32277210) | 7yo G | 140lb | OR 58 | draw 10 | jockey Mel Sheridan(7) | trainer Denis Gerard Hogan (14d 1/12) | headgear tp | last run 16 days | form 474807 | MARKET 6.0% | 09:00 median 13.00 | Matchbook 13.50
    comment: Winless in his last six, Expound has been beaten in recent outings, but he's fit after 16 days and has run over today's trip and going before.
- Jazz Forever (hrs_32909982) | 6yo G | 129lb | OR 47 | draw 15 | jockey Nina Doherty(7) | trainer Paul W Flynn (14d 1/3) | headgear - | last run 35 days | form 000020 | MARKET 4.8% | 09:00 median 13.00 | Matchbook 18.50
    comment: Jazz Forever is winless in his last six, with just a second two starts back to show amid four other unplaced runs, and he was unplaced again last time, 35 days ago.
- Coilins Girl (hrs_60527859) | 3yo F | 132lb | OR 55 | draw 12 | jockey Patrick McGettigan | trainer J. P. Murtagh (14d 1/11) | headgear p (1st time) | last run 39 days | form 9769 | MARKET 3.4% | 09:00 median 23.00 | Matchbook 24.00
    comment: Coilins Girl is yet to win in her last four, finishing ninth last time out and a ninth four starts back, so she is hard to fancy off 132 lb.
- Roderick (hrs_14220710) | 10yo G | 125lb | OR 43 | draw 14 | jockey Camillus Byrne(7) | trainer P Sweeney (14d 0/3) | headgear tp | last run 37 days | form 704276 | MARKET 3.0% | 09:00 median 23.00 | Matchbook 30.00
    comment: Roderick has been winless in his last six, with a sixth last time out and a second three starts back the pick of the form, and he has run over today's trip and going before.
- Chopsticks (hrs_38632867) | 6yo G | 131lb | OR 49 | draw 11 | jockey Ross Fagan(7) | trainer S M Duffy (14d 0/0) | headgear p | last run 49 days | form 409088 | MARKET 2.7% | 09:00 median 26.00 | Matchbook 36.00
    comment: The main risk is that he has been beaten in his last six outings and carries 131 lb off a mark of 49.
- Lisnadill (hrs_47282347) | 4yo F | 125lb | OR 43 | draw 4 | jockey  | trainer John McConnell (14d 2/10) | headgear - | last run 9 days | form 6-0006 | MARKET 2.2% | 09:00 median 26.00 | Matchbook 44.00
    comment: Lisnadill is winless in her last five, though a sixth last time out just nine days ago shows she's fit, and she has run on today's going before.
- Duleek Street (hrs_26116755) | 8yo G | 122lb | OR 40 | draw 2 | jockey Nicola Burns | trainer John McConnell (14d 2/10) | headgear p | last run 32 days | form 9/77-0 | MARKET 2.1% | 09:00 median 41.00 | Matchbook 36.00
    comment: Duleek Street is winless in his last four, with a seventh and another seventh two and three starts back after an unplaced run last time, and a ninth four starts back, so he is hard to fancy at 122 lb.
- Keep It Together (hrs_43983842) | 8yo M | 127lb | OR 45 | draw 8 | jockey Jessica O'Gorman(4) | trainer D Buckley (14d 0/1) | headgear - | last run 73 days | form 0-0668 | MARKET 1.2% | 09:00 median 67.00 | Matchbook 70.00
    comment: Winless in her last five, Keep It Together has finished eighth last time out and sixth on both runs before that, and she returns after 73 days off.

## 7:30 Dundalk (AW) | race_id rac_32304415715 | BAR 1 Betting 'Proud Supporter Of Irish Racing' Maiden
Flat |  | 1m2f150y | going Standard | AW | 9 runners | rating band - | age 3yo+
- Sangreal (hrs_58627338) | 3yo F | 129lb | OR 81 | draw 5 | jockey Declan McDonogh | trainer Joseph Patrick O'Brien (14d 3/27) | headgear - | last run 25 days | form 23342 | MARKET 55.6% | 09:00 median 1.50 | Matchbook 1.60
- Kashala (hrs_64846929) | 3yo F | 129lb | OR - | draw 3 | jockey Chris Hayes | trainer D K Weld (14d 0/7) | headgear - | last run 24 days | form 45 | MARKET 20.2% | 09:00 median 3.50 | Matchbook 5.20
- Theorist (hrs_58931089) | 3yo G | 134lb | OR 67 | draw 6 | jockey Ross Coakley | trainer D P Coakley (14d 0/0) | headgear - | last run 53 days | form 53-900 | MARKET 6.7% | 09:00 median 12.00 | Matchbook 14.50
- Winter Adventure (hrs_17393616310) | 3yo G | 134lb | OR - | draw 1 | jockey Colin Keane | trainer Noel Meade (14d 2/11) | headgear - | last run 26 days | form 0 | MARKET 6.0% | 09:00 median 13.00 | Matchbook 16.50
- Honouramongthieves (hrs_54304341) | 3yo G | 134lb | OR 69 | draw 9 | jockey R. P. Cleary | trainer C. W. J. Farrell (14d 0/2) | headgear - | last run 34 days | form 566769 | MARKET 5.6% | 09:00 median 12.00 | Matchbook 21.00
- Michinaga (hrs_17390260979) | 3yo G | 134lb | OR 74 | draw 7 | jockey Ben Coen | trainer Charles Weld (14d 0/2) | headgear - | last run 46 days | form 9690 | MARKET 2.7% | 09:00 median 29.00 | Matchbook 40.00
- Jeffnjoe (hrs_17395392539) | 3yo G | 134lb | OR - | draw 10 | jockey Leigh Roche | trainer Patrick J Flynn (14d 2/8) | headgear - | last run - days | form - | MARKET 2.2% | 09:00 median 34.00 | Matchbook 60.00
- Nthea Spirit (hrs_65974433) | 3yo G | 134lb | OR - | draw 4 | jockey Gavin Ryan | trainer Tracey Collins (14d 0/2) | headgear - | last run 26 days | form 00 | MARKET 0.6% | 09:00 median 151.00 | Matchbook 240.00
- Anaverna (hrs_65519895) | 3yo F | 129lb | OR - | draw 2 | jockey Robbie Colgan | trainer M M Rice (14d 0/1) | headgear t | last run 14 days | form 000 | MARKET 0.4% | 09:00 median 201.00 | Matchbook 380.00

## 8:00 Dundalk (AW) | race_id rac_32304417652 | BAR 1 Betting 'Best Odds Guaranteed Overnight' Handicap
Flat |  | 1m2f150y | going Standard | AW | 11 runners | rating band - | age 3yo+
- Serenity Blue (hrs_46295816) | 4yo G | 139lb | OR 87 | draw 11 | jockey Adam Caffrey | trainer Adrian McGuinness (14d 3/21) | headgear p | last run 14 days | form 004414 | MARKET 16.8% | 09:00 median 5.00 | Matchbook 5.30 | CHECK (skip line 4.75)
    comment: The main risk is a hefty 139 lb from draw 11.
- Star Harbour (hrs_23500323) | 8yo G | 140lb | OR 88 | draw 7 | jockey Declan McDonogh | trainer Adrian McGuinness (14d 3/21) | headgear v | last run 53 days | form 522300 | MARKET 12.4% | 09:00 median 6.50 | Matchbook 7.60
    comment: The risk is two unplaced runs since and a 53-day break, with 140 lb to carry from draw 7.
- Sonoran (hrs_44907534) | 4yo G | 132lb | OR 80 | draw 6 | jockey Chris Hayes | trainer Denis Gerard Hogan (14d 1/12) | headgear t | last run 16 days | form 995101 | MARKET 12.3% | 09:00 median 6.80 | Matchbook 7.00
    comment: Sonoran arrives in cracking nick, a winner last time out and again three starts back, and he's fresh enough after 16 days, having run over today's trip and going before.
- Unterberg (hrs_30300004) | 7yo G | 135lb | OR 83 | draw 4 | jockey Ben Coen | trainer Laura Hourigan (14d 0/0) | headgear - | last run 14 days | form 809486 | MARKET 9.2% | 09:00 median 9.00 | Matchbook 9.60
    comment: Unterberg is winless in his last six, with a sixth last time out and a fourth three starts back his best recent efforts, though he's back quickly after 14 days.
- Xirivella (hrs_66432338) | 3yo F | 126lb | OR 78 | draw 3 | jockey Colin Keane | trainer Noel Meade (14d 2/11) | headgear - | last run 39 days | form 633521 | MARKET 9.2% | 09:00 median 8.00 | Matchbook 11.50
- Letiza (hrs_34333677) | 6yo M | 127lb | OR 75 | draw 1 | jockey Jimmy Dalton(7) | trainer A. Slattery (14d 1/19) | headgear - | last run 33 days | form -24416 | MARKET 8.6% | 09:00 median 9.00 | Matchbook 11.00
    comment: Letiza was only sixth last time out and has had 33 days off, which makes her hard to fancy, though she was a winner two starts back and has run over today's trip and going.
- El Galvino (hrs_52677527) | 5yo G | 132lb | OR 80 | draw 9 | jockey W. J. Lee | trainer Andrew Lee (14d 0/2) | headgear - | last run 129 days | form 932-71 | MARKET 7.8% | 09:00 median 9.50 | Matchbook 12.50
    comment: El Galvino won last time out and was second three starts back, but a seventh two starts back and a 129-day absence temper the enthusiasm.
- Anvika (hrs_36528016) | 5yo M | 125lb | OR 73 | draw 10 | jockey Robbie Colgan | trainer Ms Sheila Lavery (14d 0/5) | headgear t | last run 24 days | form 36501U | MARKET 7.7% | 09:00 median 9.00 | Matchbook 15.00
    comment: Anvika unseated last time out and was only unplaced three starts back, so she is hard to fancy, though she did win two starts back and has run on today's going before.
- Diamond Exchange (hrs_43667253) | 4yo F | 132lb | OR 80 | draw 5 | jockey Nina Doherty(10) | trainer Mrs J. Harrington (14d 1/12) | headgear p | last run 42 days | form 751840 | MARKET 7.5% | 09:00 median 12.00 | Matchbook 11.00
- Spicy Margarita (hrs_46265387) | 4yo F | 140lb | OR 88 | draw 8 | jockey Donagh O'Connor | trainer Robson De Aguiar (14d 0/3) | headgear - | last run 7 days | form 870974 | MARKET 6.2% | 09:00 median 11.00 | Matchbook 17.00
- Brewing (hrs_32597908) | 7yo G | 125lb | OR 73 | draw 2 | jockey W. M. Lordan | trainer Kevin Thomas Coleman (14d 0/0) | headgear - | last run 28 days | form 230940 | MARKET 2.3% | 09:00 median 41.00 | Matchbook 42.00
    comment: Brewing is winless in his last six, though a second and a third five and six starts back show he has ability, and he has run on today's going before.

## 8:30 Dundalk (AW) | race_id rac_32304419589 | Now Racing Every Wednesday At Dundalk Handicap
Flat |  | 1m2f150y | going Standard | AW | 13 runners | rating band - | age 3yo
- African Affair (hrs_56843626) | 3yo G | 138lb | OR 68 | draw 9 | jockey Robbie Colgan | trainer Ms Sheila Lavery (14d 0/5) | headgear - | last run 24 days | form 0-0816 | MARKET 22.0% | 09:00 median 3.75 | Matchbook 3.80 | CHECK (skip line 3.56)
    comment: African Affair bounced back from an eighth to win two starts back, but was only sixth last time out, 24 days ago, so consistency is a question.
- Glitter And Glory (hrs_52267852) | 3yo F | 139lb | OR 69 | draw 7 | jockey Patrick McGettigan(5) | trainer Mrs J. Harrington (14d 1/12) | headgear - | last run 16 days | form 357793 | MARKET 16.1% | 09:00 median 4.50 | Matchbook 5.90
    comment: Glitter And Glory arrives in decent heart after a third last time out just 16 days ago, and she has run on today's going before.
- Love Orchid (hrs_53960032) | 3yo F | 136lb | OR 66 | draw 10 | jockey Colin Keane | trainer Noel Meade (14d 2/11) | headgear - | last run 25 days | form 023629 | MARKET 13.5% | 09:00 median 6.00 | Matchbook 6.20
- Chloe's Boy (hrs_65974419) | 3yo G | 122lb | OR 52 | draw 11 | jockey Siobhan Rutledge | trainer H Rogers (14d 0/2) | headgear v | last run 7 days | form 918503 | MARKET 11.6% | 09:00 median 7.00 | Matchbook 7.20
    comment: Chloe's Boy was third last time out and has run over today's trip and going, but that is his only recent top-three finish since a win five starts back, with a fifth, an eighth and a ninth also in the mix.
- Wild Berries (hrs_53743235) | 3yo F | 134lb | OR 64 | draw 8 | jockey W. J. Lee | trainer Ross O'Sullivan (14d 1/20) | headgear p | last run 49 days | form 070010 | MARKET 9.3% | 09:00 median 7.50 | Matchbook 10.50
    comment: Wild Berries won two starts back but has been unplaced in four of her other last five runs, and returns after 49 days with a stable out of form (1/20).
- Phlox (hrs_65745687) | 3yo F | 139lb | OR 69 | draw 3 | jockey Ben Coen | trainer J. P. Murtagh (14d 1/11) | headgear - | last run 90 days | form 564 | MARKET 8.8% | 09:00 median 6.50 | Matchbook 14.50
    comment: Phlox was fourth last time out, then a sixth two starts back, and a fifth three starts back, so she is yet to win in her last three and has been consistent without quite getting involved.
- Cherry Hill Girl (hrs_54712357) | 3yo F | 141lb | OR 71 | draw 12 | jockey Sam Coen(5) | trainer A. Slattery (14d 1/19) | headgear t (1st time) | last run 12 days | form 743700 | MARKET 7.4% | 09:00 median 11.00 | Matchbook 12.00
    comment: Cherry Hill Girl is winless in her last six and unplaced on her last two starts, though she was third four starts back and returns on a quick 12-day turnaround, and she has run over today's trip.
- My First Rose (hrs_64360989) | 3yo F | 130lb | OR 60 | draw 2 | jockey Chris Hayes | trainer D K Weld (14d 0/7) | headgear p (1st time) | last run 29 days | form 7680 | MARKET 4.9% | 09:00 median 15.00 | Matchbook 19.50
    comment: My First Rose is winless in her last four, with finishes of eighth and sixth among them, though she has run over today's trip and returns after 29 days.
- Mothel Abbey (hrs_17390262022) | 3yo G | 128lb | OR 58 | draw 14 | jockey Robyn Donaghue-Leahy(7) | trainer Patrick J Flynn (14d 2/8) | headgear - | last run 14 days | form 8099 | MARKET 2.2% | 09:00 median 34.00 | Matchbook 48.00
    comment: Mothel Abbey is hard to fancy, having finished ninth in each of his last two and remaining winless in his last four, with an eighth four starts back the best of them.
- Glamazon (hrs_52526103) | 3yo F | 128lb | OR 58 | draw 1 | jockey Luke McAteer | trainer Paul W Flynn (14d 1/3) | headgear p | last run 25 days | form 930360 | MARKET 1.9% | 09:00 median 29.00 | Matchbook 90.00
- Quinchy Lady (hrs_64847440) | 3yo F | 119lb | OR 48 | draw 4 | jockey Nathan Crosse | trainer John McConnell (14d 2/10) | headgear - | last run 36 days | form 00700 | MARKET 0.8% | 09:00 median 67.00 | Matchbook 150.00
    comment: Quinchy Lady is hard to fancy, unplaced in four of her last five and a seventh three starts back the best of it, so she is yet to win in that spell.
- Montevetro (hrs_54494314) | 3yo G | 132lb | OR 62 | draw 5 | jockey Leigh Roche | trainer Denis Gerard Hogan (14d 1/12) | headgear p (1st time) | last run 21 days | form 239080 | MARKET 0.8% | 09:00 median 67.00 | Matchbook 230.00
    comment: Montevetro is without a win in his last six and has been out of the first three in his last four, though he was second and third before that and has run over today's trip and going.
- Sarfarcat (hrs_59461052) | 3yo F | 119lb | OR 41 | draw 13 | jockey R. P. Cleary | trainer Thomas Coyle (14d 0/3) | headgear - | last run 28 days | form 060080 | MARKET 0.6% | 09:00 median 101.00 | Matchbook 300.00
