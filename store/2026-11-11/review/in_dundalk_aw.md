# Card review packet: Dundalk (AW), 2026-11-11

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
{"meeting": "dundalk_aw", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 2:30 Dundalk (AW) | race_id rac_32304134850 | Christmas Party Nights At Dundalk Stadium Handicap
Flat |  | 0m5f0y | going Standard | AW | 13 runners | rating band - | age 3yo+
- Jordan Breeze (hrs_53390176) | 4yo G | 132lb | OR 62 | draw 11 | jockey Robyn Donaghue-Leahy(7) | trainer Patrick J Flynn (14d 3/7) | headgear - | last run 12 days | form 067851 | MARKET 16.8% | 09:00 median 4.33 | Matchbook 5.70 | CHECK (skip line 4.11)
    comment: Jordan Breeze won last time out just 12 days ago, but that came after a run of finishes from fifth down to eighth, and he carries 132 lb from draw 11.
- Lethimfly (hrs_41228803) | 4yo G | 142lb | OR 72 | draw 9 | jockey Nicola Burns(5) | trainer Gerard Keane (14d 0/5) | headgear t | last run 23 days | form 000071 | MARKET 16.1% | 09:00 median 4.50 | Matchbook 6.20
- One Cool Bear (hrs_53960053) | 3yo G | 130lb | OR 60 | draw 2 | jockey Patrick McGettigan(5) | trainer Adrian McGuinness (14d 2/22) | headgear p | last run 12 days | form 817732 | MARKET 12.6% | 09:00 median 6.00 | Matchbook 7.40
- Coincidental Glory (hrs_54842501) | 3yo G | 137lb | OR 67 | draw 7 | jockey Camillus Byrne(10) | trainer Adrian McGuinness (14d 2/22) | headgear v | last run 7 days | form 302314 | MARKET 10.2% | 09:00 median 8.00 | Matchbook 8.60
    comment: Fourth last time out, and a winner two starts back, Coincidental Glory is consistent in recent runs and quick back after seven days, having run over today's trip and going before.
- Initial Blue (hrs_45759497) | 4yo G | 143lb | OR 73 | draw 3 | jockey Jimmy Dalton(7) | trainer Jack W Davison (14d 0/4) | headgear tb | last run 21 days | form 231166 | MARKET 8.8% | 09:00 median 9.00 | Matchbook 10.00
- Cuban Grey (hrs_28533918) | 6yo G | 142lb | OR 72 | draw 12 | jockey Luke McAteer | trainer Patrick J McKenna (14d 0/1) | headgear p | last run 27 days | form 350880 | MARKET 6.8% | 09:00 median 11.00 | Matchbook 15.00
    comment: The risk is a form line of two eighths and an unplaced run last time out, leaving him winless in his last six.
- Sovereign Cry (hrs_57622173) | 3yo G | 137lb | OR 67 | draw 1 | jockey Declan McDonogh | trainer Daniel James Murphy (14d 2/9) | headgear b (1st time) | last run 7 days | form 499809 | MARKET 6.4% | 09:00 median 12.00 | Matchbook 13.00
    comment: Sovereign Cry has been well beaten in recent outings, a ninth last time out and a fourth six starts back his best finish, but he's quick back after seven days and has run over today's trip and going.
- Harry's Hill (hrs_22250802) | 8yo G | 135lb | OR 65 | draw 8 | jockey Colin Keane | trainer Martin Hassett (14d 0/4) | headgear t | last run 10 days | form 210980 | MARKET 5.3% | 09:00 median 15.00 | Matchbook 17.00
    comment: Harry's Hill is our pick on profile: he has run over today's trip and going before, is fit after just ten days off, and won five starts back after a second six starts back.
- Mint Man (hrs_36035902) | 5yo G | 137lb | OR 67 | draw 10 | jockey Chris Hayes | trainer P J F Murphy (14d 0/5) | headgear t | last run 70 days | form 803100 | MARKET 5.3% | 09:00 median 15.00 | Matchbook 17.50
- Treasured Royal (hrs_55882253) | 3yo F | 123lb | OR 53 | draw 13 | jockey Reese Holohan(5) | trainer Gavin Cromwell (14d 7/39) | headgear tb (1st time) | last run 12 days | form 400005 | MARKET 4.0% | 09:00 median 17.00 | Matchbook 26.00
    comment: Treasured Royal is winless in her last six, with a fifth last time out the best of her recent efforts and four unplaced runs before that, so she is hard to fancy.
- Mary Shoelaces (hrs_34976186) | 5yo M | 137lb | OR 67 | draw 6 | jockey Jessica O'Gorman(7) | trainer Eddie & Patrick Harty (14d 2/6) | headgear b | last run 27 days | form 671459 | MARKET 3.7% | 09:00 median 21.00 | Matchbook 26.00
    comment: Mary Shoelaces won four starts back but has since finished a fourth, a fifth and then a ninth last time out, and she has run over today's trip and going before.
- Astute Power (hrs_56127617) | 4yo G | 127lb | OR 57 | draw 4 | jockey James Ryan | trainer Edward Lynam (14d 1/3) | headgear t | last run 21 days | form 4-0048 | MARKET 2.6% | 09:00 median 34.00 | Matchbook 38.00
    comment: Winless in his last five and beaten into eighth last time out, Astute Power is hard to fancy, with a fourth two starts back the best of his recent efforts.
- Tarsus (hrs_35979433) | 5yo G | 144lb | OR 74 | draw 5 | jockey Sadhbh Tormey(7) | trainer John M Harney (14d 0/0) | headgear t | last run 651 days | form 60/87- | MARKET 1.3% | 09:00 median 41.00 | Matchbook 120.00
    comment: The big risk is that long absence, plus 144 lb from stall five.

## 3:00 Dundalk (AW) | race_id rac_32304136787 | Book Online At DundalkStadium.com Nursery Handicap
Flat |  | 0m6f0y | going Standard | AW | 9 runners | rating band - | age 2yo
- Invincible Irish (hrs_17389030239) | 2yo G | 134lb | OR 60 | draw 9 | jockey Scott McCullagh | trainer Daniel McLoughlin (14d 1/6) | headgear p (1st time) | last run 44 days | form 00742 | MARKET 22.7% | 09:00 median 3.50 | Matchbook 3.95 | CHECK (skip line 3.32)
- Lady H (hrs_17391299807) | 2yo F | 138lb | OR 64 | draw 1 | jockey W. J. Lee | trainer Henry de Bromhead (14d 8/41) | headgear - | last run 47 days | form 000 | MARKET 18.3% | 09:00 median 4.50 | Matchbook 5.10
    comment: The risk is plain though: she is winless in her last three, unplaced each time, and returns after 47 days off.
- Dear Theodosia (hrs_7000000518) | 2yo F | 124lb | OR 50 | draw 8 | jockey Declan McDonogh | trainer Daniel McLoughlin (14d 1/6) | headgear b | last run 23 days | form 00996 | MARKET 14.3% | 09:00 median 6.00 | Matchbook 6.40
    comment: Dear Theodosia is yet to win in her last five starts, though a sixth last time out, 23 days ago, was her best finish in that run.
- Professor Finnegan (hrs_17392595213) | 2yo G | 138lb | OR 64 | draw 6 | jockey Ben Coen | trainer J. P. Murtagh (14d 0/14) | headgear b (1st time) | last run 21 days | form 089 | MARKET 14.2% | 09:00 median 6.00 | Matchbook 6.60
- Syrah (hrs_17390804382) | 2yo F | 128lb | OR 54 | draw 5 | jockey Colin Keane | trainer Charles Weld (14d 0/0) | headgear h | last run 19 days | form 08546 | MARKET 12.8% | 09:00 median 6.80 | Matchbook 7.00
    comment: Syrah is winless in her last five, though a sixth last time out, a fourth two starts back and a fifth three starts back show she's been running in midfield, and she's fresh enough after 19 days.
- Dragon Scales (hrs_17390577008) | 2yo F | 132lb | OR 58 | draw 4 | jockey Nathan Crosse | trainer Daniel McLoughlin (14d 1/6) | headgear - | last run 14 days | form 600 | MARKET 9.3% | 09:00 median 9.00 | Matchbook 10.50
- Lady Quigley (hrs_17391818178) | 2yo F | 122lb | OR 48 | draw 7 | jockey Robert Whearty | trainer Paul W Flynn (14d 1/3) | headgear - | last run 33 days | form 900 | MARKET 3.7% | 09:00 median 17.00 | Matchbook 34.00
    comment: Lady Quigley is winless in her last three, unplaced twice before a ninth three starts back, and she steps up after 33 days off carrying 122 lb from stall seven.
- Savannah Sun (hrs_17390957703) | 2yo F | 125lb | OR 51 | draw 2 | jockey Chris Hayes | trainer Martin Hassett (14d 0/4) | headgear - | last run 14 days | form 00000 | MARKET 2.5% | 09:00 median 41.00 | Matchbook 46.00
    comment: Savannah Sun is winless and unplaced in each of her last five starts, which makes her hard to fancy, though she is fresh enough after 14 days and has run over today's trip and going.
- Imply (hrs_17391817135) | 2yo F | 129lb | OR 55 | draw 3 | jockey Patrick McGettigan(5) | trainer Charles Weld (14d 0/0) | headgear p (1st time) | last run 35 days | form 0650 | MARKET 2.1% | 09:00 median 34.00 | Matchbook 55.00
    comment: Imply is hard to fancy, unplaced last time out and winless in her last four, with a fifth two starts back and a sixth three starts back her best finishes.

## 3:30 Dundalk (AW) | race_id rac_32304138724 | Irishinjuredjockeys.com Claiming Race
Flat |  | 1m0f0y | going Standard | AW | 8 runners | rating band - | age 3yo+
- Justenzia (hrs_45982377) | 4yo F | 142lb | OR 74 | draw 3 | jockey Chris Hayes | trainer Denis Gerard Hogan (14d 1/16) | headgear p | last run 5 days | form 022621 | MARKET 34.4% | 09:00 median 2.50 | Matchbook 2.66
    comment: Won last time out just five days ago, and with a second two starts back and a pair of seconds before a sixth, Justenzia is in cracking form and has run over today's trip and going.
- Red Hugh O'Donnell (hrs_37014103) | 5yo G | 132lb | OR 62 | draw 2 | jockey W. J. Lee | trainer Gillian Scott (14d 1/2) | headgear tb | last run 14 days | form 480696 | MARKET 17.0% | 09:00 median 5.00 | Matchbook 5.50
    comment: The risk is a winless run in his last six starts, with a fourth six starts back his best recent effort.
- Shoot To Kill (hrs_19208000) | 9yo G | 136lb | OR 70 | draw 1 | jockey Ms E Dunseath(10) | trainer Noel C. Kelly (14d 1/9) | headgear - | last run 19 days | form 283692 | MARKET 14.6% | 09:00 median 5.50 | Matchbook 6.60
    comment: The risk is consistency, with a ninth and a sixth in the recent mix and yet to win in his last six.
- Star Strewn (hrs_58534952) | 3yo F | 140lb | OR 75 | draw 8 | jockey R. P. Cleary | trainer C. W. J. Farrell (14d 0/0) | headgear - | last run 33 days | form 189710 | MARKET 12.2% | 09:00 median 7.00 | Matchbook 7.60
    comment: Star Strewn won two starts back and six starts back, and has run over today's trip and going before, so she is our pick on profile despite an unplaced effort last time out. A 33-day break should have her fresh, though 140 lb is a notable burden from stall eight.
- Ocean Echo (hrs_63875329) | 3yo G | 128lb | OR 57 | draw 6 | jockey Reese Holohan(5) | trainer Mark Fahey (14d 0/8) | headgear tp | last run 14 days | form 686005 | MARKET 11.2% | 09:00 median 8.00 | Matchbook 8.40
    comment: Ocean Echo is winless in his last six, though a fifth last time out and a quick 14-day turnaround suggest he's holding his form, and he has run over today's trip and going before.
- Leonie (hrs_52451931) | 3yo F | 122lb | OR 66 | draw 5 | jockey Robert Whearty | trainer A. McCann (14d 0/7) | headgear ht (1st time) | last run 21 days | form 331608 | MARKET 6.3% | 09:00 median 9.50 | Matchbook 21.00
    comment: Leonie is a filly who has gone eighth and unplaced in her last two runs, though she won four starts back and was third before that, and she has run over today's trip and going.
- Morning Approach (hrs_23208983) | 8yo M | 122lb | OR 48 | draw 7 | jockey Megan Telford-Kelly(7) | trainer W. McCreery (14d 0/7) | headgear - | last run 14 days | form 000003 | MARKET 3.5% | 09:00 median 26.00 | Matchbook 28.00
    comment: Morning Approach is yet to win in her last six, with five unplaced runs before a third last time out 14 days ago, so she is hard to fancy at 122 lb from draw 7.
- Betsy Trotwood (hrs_17392879952) | 3yo F | 122lb | OR - | draw 4 | jockey Jared Huggan(10) | trainer Alan McIntyre (14d 0/0) | headgear - | last run 21 days | form 070 | MARKET 0.8% | 09:00 median 81.00 | Matchbook 230.00
    comment: She has run on today's going and returns after 21 days, but little else points her way from stall four.

## 4:02 Dundalk (AW) | race_id rac_32304140661 | Bet On The Best Night Out At Dundalk Stadium Maiden
Flat |  | 1m0f0y | going Standard | AW | 14 runners | rating band - | age 3yo+
- Lookingforarainbow (hrs_53390239) | 3yo F | 129lb | OR 76 | draw 2 | jockey Gavin Ryan | trainer Donnacha Aidan O'Brien (14d 0/6) | headgear tp (1st time) | last run 12 days | form 47-562 | MARKET 29.7% | 09:00 median 2.38 | Matchbook 2.56
- Resurgence (hrs_56127589) | 3yo G | 134lb | OR 80 | draw 13 | jockey Colin Keane | trainer Mrs J. Harrington (14d 2/14) | headgear p | last run 30 days | form 24-263 | MARKET 23.6% | 09:00 median 3.00 | Matchbook 3.20
- Riyazanka (hrs_17391710749) | 3yo F | 129lb | OR - | draw 14 | jockey Ben Coen | trainer J. P. Murtagh (14d 0/14) | headgear p (1st time) | last run 12 days | form 73 | MARKET 11.2% | 09:00 median 6.50 | Matchbook 6.80
- Subtle Shade (hrs_17394487215) | 3yo F | 129lb | OR - | draw 5 | jockey Chris Hayes | trainer Joseph Patrick O'Brien (14d 2/25) | headgear - | last run 12 days | form 8 | MARKET 8.1% | 09:00 median 9.00 | Matchbook 9.60
- Queen Creek (hrs_17395284067) | 3yo F | 129lb | OR - | draw 7 | jockey Declan McDonogh | trainer Joseph Patrick O'Brien (14d 2/25) | headgear - | last run - days | form - | MARKET 7.4% | 09:00 median 10.00 | Matchbook 10.50
- Positive Thinking (hrs_17392944618) | 3yo G | 134lb | OR - | draw 3 | jockey Killian Leonard | trainer Miss Natalia Lupini (14d 0/7) | headgear - | last run 12 days | form 05 | MARKET 4.6% | 09:00 median 19.00 | Matchbook 19.50
- Donna Time (hrs_61078766) | 3yo F | 129lb | OR 72 | draw 8 | jockey R. P. Cleary | trainer C. W. J. Farrell (14d 0/0) | headgear - | last run 119 days | form 7620 | MARKET 4.4% | 09:00 median 17.00 | Matchbook 23.00
- Emily Estherfaye (hrs_17389581986) | 3yo F | 129lb | OR 70 | draw 1 | jockey Jimmy Dalton(7) | trainer A. Slattery (14d 1/21) | headgear h | last run 37 days | form 0547 | MARKET 2.2% | 09:00 median 41.00 | Matchbook 44.00
- Bugsy Siegel (hrs_17394891899) | 3yo G | 134lb | OR - | draw 4 | jockey James Ryan | trainer Edward Lynam (14d 1/3) | headgear - | last run - days | form - | MARKET 2.2% | 09:00 median 41.00 | Matchbook 46.00
- Ossie's Lodge (hrs_34457073) | 7yo G | 136lb | OR - | draw 11 | jockey N G McCullagh | trainer A. J. Martin (14d 0/9) | headgear t | last run 880 days | form 4/ | MARKET 1.9% | 09:00 median 51.00 | Matchbook 48.00
- Ferreshana (hrs_17395281981) | 3yo F | 129lb | OR - | draw 10 | jockey Jack Kearney | trainer Daniel James Murphy (14d 2/9) | headgear - | last run - days | form - | MARKET 1.8% | 09:00 median 51.00 | Matchbook 55.00
- Susie's Angel (hrs_17389795801) | 3yo F | 129lb | OR - | draw 12 | jockey Reese Holohan(5) | trainer Mark Fahey (14d 0/8) | headgear - | last run 56 days | form 67 | MARKET 1.6% | 09:00 median 67.00 | Matchbook 46.00
- The Blonde Lady (hrs_17390805425) | 3yo F | 129lb | OR - | draw 6 | jockey Robbie Colgan | trainer A. J. Martin (14d 0/9) | headgear - | last run 23 days | form 008 | MARKET 0.8% | 09:00 median 151.00 | Matchbook 75.00
- Dyker Heights (hrs_57503908) | 3yo F | 129lb | OR - | draw 9 | jockey Robert Whearty | trainer Matthew J Smith (14d 0/8) | headgear - | last run 10 days | form 00-0 | MARKET 0.6% | 09:00 median 201.00 | Matchbook 100.00

## 4:32 Dundalk (AW) | race_id rac_32304142598 | View Restaurant At Dundalk Stadium Median Auction Maiden
Flat |  | 0m7f0y | going Standard | AW | 17 runners | rating band - | age 2yo
- Marcescence (hrs_66655358) | 2yo F | 125lb | OR - | draw 2 | jockey Jack Kearney | trainer Gavin Cromwell (14d 7/39) | headgear - | last run 35 days | form 33 | MARKET 21.8% | 09:00 median 3.00 | Matchbook 3.65 | CHECK (skip line 2.85)
- Sonic Sabiha (hrs_17389569470) | 2yo F | 123lb | OR 80 | draw 9 | jockey Rebecca Parsons(10) | trainer David Marnane (14d 1/7) | headgear - | last run 14 days | form 78525 | MARKET 15.2% | 09:00 median 4.33 | Matchbook 5.60
- Direct Action (hrs_17392283356) | 2yo C | 130lb | OR - | draw 13 | jockey Colin Keane | trainer Derek McCormack (14d 0/1) | headgear t | last run 21 days | form 64 | MARKET 9.4% | 09:00 median 7.50 | Matchbook 8.20
- Pennsylvania Ave (hrs_66399466) | 2yo C | 128lb | OR - | draw 3 | jockey Declan McDonogh | trainer Joseph Patrick O'Brien (14d 2/25) | headgear - | last run 103 days | form 49 | MARKET 8.5% | 09:00 median 8.00 | Matchbook 9.80
- Sake Nights (hrs_17392787125) | 2yo F | 129lb | OR - | draw 11 | jockey Chris Hayes | trainer Donnacha Aidan O'Brien (14d 0/6) | headgear - | last run 33 days | form 6 | MARKET 7.1% | 09:00 median 10.00 | Matchbook 12.50
- American Cowboy (hrs_17393544343) | 2yo C | 132lb | OR - | draw 10 | jockey James Ryan | trainer Daniel James Murphy (14d 2/9) | headgear - | last run 19 days | form 36 | MARKET 6.4% | 09:00 median 10.00 | Matchbook 13.50
- Esprit De Loi (hrs_17393540171) | 2yo F | 123lb | OR 70 | draw 4 | jockey Siobhan Rutledge | trainer Noel Meade (14d 2/15) | headgear - | last run 7 days | form 973 | MARKET 4.7% | 09:00 median 15.00 | Matchbook 19.50
- Celestial Order (hrs_17393765459) | 2yo F | 125lb | OR - | draw 17 | jockey  | trainer Miss Natalia Lupini (14d 0/7) | headgear - | last run 27 days | form 7 | MARKET 4.6% | 09:00 median 15.00 | Matchbook 19.00
- September Duke (hrs_66272185) | 2yo G | 134lb | OR - | draw 5 | jockey Jimmy Dalton(7) | trainer A. Slattery (14d 1/21) | headgear - | last run 59 days | form 06 | MARKET 4.4% | 09:00 median 17.00 | Matchbook 18.00
- Chicago Caray (hrs_17391961069) | 2yo G | 132lb | OR - | draw 14 | jockey Ben Coen | trainer J. P. Murtagh (14d 0/14) | headgear b (1st time) | last run 14 days | form 84 | MARKET 4.2% | 09:00 median 19.00 | Matchbook 15.50
- Jade Fox (hrs_17391968370) | 2yo F | 123lb | OR - | draw 15 | jockey Reese Holohan(5) | trainer Gavin Cromwell (14d 7/39) | headgear - | last run 27 days | form 03 | MARKET 3.6% | 09:00 median 21.00 | Matchbook 22.00
- Farmerspolish (hrs_17393546429) | 2yo C | 132lb | OR - | draw 12 | jockey W. J. Lee | trainer Henry de Bromhead (14d 8/41) | headgear t | last run 33 days | form 9 | MARKET 3.3% | 09:00 median 23.00 | Matchbook 25.00
- Salamantino (hrs_17395285110) | 2yo C | 134lb | OR - | draw 8 | jockey Robbie Downey | trainer William Durkan (14d 0/4) | headgear t (1st time) | last run - days | form - | MARKET 1.7% | 09:00 median 81.00 | Matchbook 55.00
- In Sequence (hrs_17394340152) | 2yo C | 132lb | OR - | draw 16 | jockey  | trainer Alan McIntyre (14d 0/0) | headgear tp (1st time) | last run 19 days | form 0 | MARKET 1.5% | 09:00 median 67.00 | Matchbook 75.00
- Bajan Bambi (hrs_17393760244) | 2yo F | 129lb | OR - | draw 6 | jockey Nathan Crosse | trainer Mrs J. Harrington (14d 2/14) | headgear - | last run 14 days | form 00 | MARKET 1.3% | 09:00 median 126.00 | Matchbook 70.00
- Elzante (hrs_17391307108) | 2yo G | 128lb | OR - | draw 7 | jockey Luke McAteer | trainer C Byrnes (14d 0/7) | headgear - | last run 22 days | form 90 | MARKET 1.1% | 09:00 median 151.00 | Matchbook 85.00
- Sevengrandchildren (hrs_17393393108) | 2yo C | 128lb | OR - | draw 1 | jockey  | trainer Michael Mulvany (14d 0/6) | headgear t | last run 21 days | form 00 | MARKET 1.1% | 09:00 median 67.00 | Matchbook 85.00

## 5:02 Dundalk (AW) | race_id rac_32304144535 | Celebrate Your Special Occasion At Dundalk Stadium Handicap
Flat |  | 0m7f0y | going Standard | AW | 15 runners | rating band - | age 3yo+
- Go Out (hrs_50282106) | 4yo G | 136lb | OR 66 | draw 12 | jockey Jack Kearney | trainer Daniel James Murphy (14d 2/9) | headgear tb (1st time) | last run 12 days | form 460021 | MARKET 15.4% | 09:00 median 4.00 | Matchbook 4.10 | CHECK (skip line 3.80)
    comment: Won last time out and a second two starts back, and he's fresh from just 12 days ago, having run over today's trip and going before.
- Golddream (hrs_62779164) | 3yo G | 144lb | OR 75 | draw 10 | jockey  | trainer David Marnane (14d 1/7) | headgear - | last run 12 days | form 550564 | MARKET 12.9% | 09:00 median 4.50 | Matchbook 5.10
    comment: The risk is that he is winless in his last six starts, with a fifth three starts back his best other finish.
- Carrigans Grove (hrs_42912933) | 5yo M | 132lb | OR 62 | draw 3 | jockey Robyn Donaghue-Leahy(7) | trainer Patrick J Flynn (14d 3/7) | headgear - | last run 7 days | form 703451 | MARKET 12.2% | 09:00 median 5.50 | Matchbook 4.90
- Boston Max (hrs_56843780) | 3yo G | 132lb | OR 63 | draw 15 | jockey Nina Doherty(10) | trainer Gordon Elliott (14d 9/58) | headgear tp | last run 19 days | form 254324 | MARKET 9.9% | 09:00 median 6.00 | Matchbook 6.60
    comment: Boston Max is yet to win in his last six, though he was second six starts back and again two starts back, and a fourth last time out 19 days ago keeps him ticking over.
- Blue Anthem (hrs_43951131) | 4yo G | 128lb | OR 58 | draw 4 | jockey Camillus Byrne(10) | trainer Adrian McGuinness (14d 2/22) | headgear tv | last run 12 days | form 832258 | MARKET 7.7% | 09:00 median 8.00 | Matchbook 8.40
    comment: Winless in his last six, Blue Anthem was runner-up twice and third before a fifth two starts back and an eighth last time out, 12 days ago, and he has run over today's trip and going.
- Usuario Amigo (hrs_40805534) | 5yo G | 134lb | OR 64 | draw 8 | jockey Scott McCullagh | trainer Richard John O'Brien (14d 0/0) | headgear - | last run 47 days | form 970361 | MARKET 7.1% | 09:00 median 9.00 | Matchbook 8.80
    comment: Usuario Amigo won last time out but was sixth two starts back, and he returns after 47 days off with 134 lb from draw 8. He has run over today's trip and going, though the patchy form before that win holds him back.
- Beach Barbie (hrs_52897145) | 4yo F | 138lb | OR 68 | draw 11 | jockey James Ryan | trainer Edward Lynam (14d 1/3) | headgear p | last run 19 days | form 530301 | MARKET 6.4% | 09:00 median 11.00 | Matchbook 9.80
    comment: Beach Barbie won last time out 19 days ago and has run over today's trip and going, but she was unplaced in two of the three runs before that.
- Tolebi (hrs_41565104) | 4yo G | 142lb | OR 72 | draw 13 | jockey Danny O'Leary(10) | trainer G. O'Leary (14d 2/11) | headgear b (1st time) | last run 22 days | form 045580 | MARKET 5.6% | 09:00 median 12.00 | Matchbook 11.00
    comment: Tolebi has run over today's distance and going before, and returns fresh after 22 days; he is yet to win in his last six, but a fourth and two fifths in that spell back him up.
- Moyassr (hrs_36738751) | 5yo G | 142lb | OR 72 | draw 14 | jockey Cillian Rowan(10) | trainer Adrian McGuinness (14d 2/22) | headgear t | last run 14 days | form 822260 | MARKET 4.6% | 09:00 median 13.00 | Matchbook 14.00
- Free Solo (hrs_18504633) | 9yo G | 128lb | OR 58 | draw 2 | jockey Gavin Ryan | trainer P J F Murphy (14d 0/5) | headgear /bes | last run 13 days | form 928940 | MARKET 4.5% | 09:00 median 15.00 | Matchbook 16.00
- Thaloria (hrs_52995131) | 4yo F | 135lb | OR 65 | draw 9 | jockey Nicola Burns(5) | trainer Miss Natalia Lupini (14d 0/7) | headgear - | last run 33 days | form 600046 | MARKET 4.4% | 09:00 median 15.00 | Matchbook 14.50
    comment: The main risk is a form line that reads sixth last time out, a fourth two starts back and nothing better, and she is yet to win in her last six.
- The Bear Trap (hrs_35040054) | 5yo G | 126lb | OR 56 | draw 5 | jockey Patrick McGettigan(5) | trainer Adrian McGuinness (14d 2/22) | headgear v | last run 14 days | form 0-4097 | MARKET 3.5% | 09:00 median 19.00 | Matchbook 19.00
    comment: The Bear Trap has been well beaten lately, seventh last time out and ninth two starts back, and he is winless in his last five, so he is hard to fancy.
- Teffian Warrior (hrs_50875377) | 4yo G | 132lb | OR 62 | draw 6 | jockey Nathan Crosse | trainer Ciaran Murphy (14d 0/19) | headgear - | last run 156 days | form 504-46 | MARKET 3.2% | 09:00 median 23.00 | Matchbook 18.50
    comment: The main risk is a 156-day absence, with 132 lb to carry from stall six.
- Estrallita (hrs_17390124346) | 3yo F | 136lb | OR 67 | draw 7 | jockey Jimmy Dalton(7) | trainer Jack W Davison (14d 0/4) | headgear v (1st time) | last run 14 days | form 6638 | MARKET 1.6% | 09:00 median 51.00 | Matchbook 38.00
    comment: In her favour, she has run over today's trip and going, was third two starts back, and returns after 14 days from stall 7.
- Isthatrightkatie (hrs_53808853) | 6yo M | 135lb | OR 65 | draw 1 | jockey Killian Leonard | trainer Miss Katy Brown (14d 0/0) | headgear - | last run 19 days | form 8-048 | MARKET 1.0% | 09:00 median 100.00 | Matchbook 100.00
    comment: Isthatrightkatie is hard to fancy, beaten into eighth last time out and winless in her last four, with a fourth two starts back her best recent effort.

## 5:32 Dundalk (AW) | race_id rac_32304146472 | Now Racing Every Wednesday At Dundalk Handicap
Flat |  | 1m2f150y | going Standard | AW | 15 runners | rating band - | age 3yo+
- Eastern Peace (hrs_42041454) | 4yo F | 135lb | OR 65 | draw 2 | jockey W. J. Lee | trainer Ross O'Sullivan (14d 1/23) | headgear p | last run 26 days | form 305734 | MARKET 18.1% | 09:00 median 3.50 | Matchbook 3.55 | CHECK (skip line 3.32)
    comment: The main risk is a yard out of form at 1/23, and she is yet to win in recent starts.
- Femme Beauty (hrs_53081231) | 3yo F | 139lb | OR 73 | draw 6 | jockey Danny O'Leary(10) | trainer G. O'Leary (14d 2/11) | headgear t | last run 56 days | form 143113 | MARKET 11.3% | 09:00 median 6.00 | Matchbook 5.50
    comment: Three wins in her last six starts, including a third last time out, is a solid profile, and she has run over today's trip and going before.
- No More Porter (hrs_22689310) | 8yo G | 137lb | OR 67 | draw 3 | jockey James Ryan | trainer Adrian McGuinness (14d 2/22) | headgear tp | last run 22 days | form 045757 | MARKET 7.4% | 09:00 median 8.50 | Matchbook 8.80
    comment: The risk is a form line of sevenths and fifths, yet to win in his last six starts.
- Walhaan (hrs_15441566) | 10yo G | 143lb | OR 73 | draw 10 | jockey Patrick McGettigan(5) | trainer Ciaran Murphy (14d 0/19) | headgear - | last run 24 days | form 380030 | MARKET 7.4% | 09:00 median 9.00 | Matchbook 8.60
    comment: A third two starts back shows he can go close, though he is yet to win in his last six and was unplaced last time out.
- Sherekiya (hrs_54842620) | 3yo F | 133lb | OR 67 | draw 12 | jockey Chris Hayes | trainer D K Weld (14d 0/8) | headgear t (1st time) | last run 37 days | form 4-7386 | MARKET 7.4% | 09:00 median 9.00 | Matchbook 8.60
    comment: Sherekiya was a sixth last time out after an eighth, though she was a third three starts back and is yet to win in her last five outings.
- Chloe's Boy (hrs_65974419) | 3yo G | 119lb | OR 51 | draw 15 | jockey  | trainer H Rogers (14d 0/2) | headgear v | last run 5 days | form 918503 | MARKET 7.3% | 09:00 median 9.50 | Matchbook 8.40
    comment: Chloe's Boy was third last time out, but he is a one-win horse in his last six, with a ninth, an eighth and an unplaced run among the others, and he is back after only five days.
- Movin And Groovin (hrs_42451878) | 4yo F | 122lb | OR 52 | draw 7 | jockey Nathan Crosse | trainer David Marnane (14d 1/7) | headgear - | last run 13 days | form -13738 | MARKET 7.3% | 09:00 median 9.00 | Matchbook 8.80
    comment: In her favour, she has run over this trip and going before and is back quickly after 13 days, with a third two starts back.
- Echinacea (hrs_50875293) | 4yo F | 136lb | OR 66 | draw 9 | jockey Luke McAteer | trainer Noel C. Kelly (14d 1/9) | headgear p | last run 72 days | form 2-6922 | MARKET 6.6% | 09:00 median 11.00 | Matchbook 9.60
    comment: Echinacea has finished second in two of her last three outings, including last time out, and has run over today's trip and going, yet she's winless in her last five.
- Speckled Meadow (hrs_21543396) | 9yo M | 130lb | OR 60 | draw 8 | jockey Robyn Donaghue-Leahy(7) | trainer Don Browne (14d 0/2) | headgear - | last run 13 days | form 696205 | MARKET 6.5% | 09:00 median 10.00 | Matchbook 10.00
    comment: Speckled Meadow was fifth last time out just 13 days ago and has a second three starts back, but she is winless in her last six and has run over today's trip and going before.
- Highlander Addict (hrs_55241690) | 5yo G | 128lb | OR 58 | draw 14 | jockey Declan McDonogh | trainer Patrick J Flynn (14d 3/7) | headgear - | last run 67 days | form 800 | MARKET 5.0% | 09:00 median 15.00 | Matchbook 12.50
    comment: Highlander Addict is winless in his last three, unplaced twice before an eighth three starts back, and returns after 67 days off, so he is hard to fancy.
- Flying Fortress (hrs_43951047) | 4yo G | 140lb | OR 70 | draw 13 | jockey Reese Holohan(5) | trainer Gavin Cromwell (14d 7/39) | headgear b | last run 13 days | form 082400 | MARKET 4.7% | 09:00 median 17.00 | Matchbook 15.50
    comment: Unplaced in his last two, Flying Fortress is yet to win in recent starts, though a second four starts back and a fourth three runs ago show he can get involved, and he has run over today's trip.
- Limestone Red (hrs_35992551) | 6yo G | 132lb | OR 62 | draw 1 | jockey R. P. Cleary | trainer Tracey Collins (14d 0/1) | headgear p | last run 44 days | form 882357 | MARKET 4.3% | 09:00 median 17.00 | Matchbook 15.50
    comment: He has run over today's trip and going, and a second and a third earlier in that spell show he can get involved.
- Darkdeserthighway (hrs_23208948) | 8yo M | 139lb | OR 69 | draw 11 | jockey Colin Keane | trainer Mr M. D. O'Callaghan (14d 1/8) | headgear b | last run 26 days | form 624700 | MARKET 3.9% | 09:00 median 21.00 | Matchbook 15.50
- Cozone (hrs_16761360) | 9yo G | 130lb | OR 60 | draw 4 | jockey Robbie Colgan | trainer Matthew J Smith (14d 0/8) | headgear - | last run 14 days | form 6/8000 | MARKET 1.8% | 09:00 median 51.00 | Matchbook 38.00
    comment: Cozone is winless in his last five, with three unplaced runs most recently and an eighth four starts back, but he returns after just 14 days and has run over today's trip and going.
- Almost Okay (hrs_17391872414) | 3yo F | 121lb | OR 55 | draw 5 | jockey Nicola Burns(5) | trainer Jarlath P Fahey (14d 0/3) | headgear - | last run 21 days | form 040 | MARKET 1.1% | 09:00 median 67.00 | Matchbook 60.00
    comment: Almost Okay is hard to fancy, unplaced last time out and winless in her last three, with a fourth two starts back the best of it.
