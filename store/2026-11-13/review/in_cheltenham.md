# Card review packet: Cheltenham, 2026-11-13

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
{"meeting": "cheltenham", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 1:10 Cheltenham | race_id rac_32304291747 | AIS Conditional Jockeys' Handicap Hurdle Race (Challenger Stayers' Hurdle Series Qualifier)
Hurdle | Class 3 | 2m5f0y | going Good | Turf | 18 runners | rating band 0-125 | age 3yo+
- Glancing Jack (hrs_48240094) | 5yo G | 165lb | OR 122 | draw 0 | jockey Harry Atkins(3) | trainer Dan Skelton (14d 22/93) | headgear - | last run 237 days | form /5212- | MARKET 27.8% | 09:00 median 2.75 | Matchbook 3.20
    comment: Glancing Jack arrives with a second last time out, a win two starts back and another second three starts back, and he has run on today's going before. The single main risk is a 237-day absence, with 165 lb to carry from an official mark of 122.
- High Fibre (hrs_25122223) | 7yo G | 163lb | OR 120 | draw 0 | jockey Toby McCain-Mitchell | trainer James Owen (14d 12/46) | headgear v | last run 34 days | form 125-51 | MARKET 14.8% | 09:00 median 5.00 | Matchbook 6.20
    comment: High Fibre won last time out and has two wins in his last five starts, and he has run over today's trip and going before, with a trainer in form.
- Keno Black (hrs_46913419) | 6yo G | 157lb | OR 107 | draw 0 | jockey Bradley Harris | trainer Neil Mulholland (14d 6/27) | headgear h | last run 11 days | form 091F-1 | MARKET 11.3% | 09:00 median 6.00 | Matchbook 8.80
    comment: Keno Black won last time out, and a winner three starts back too, after a fall two starts back, and he's fresh from an 11-day turnaround, having run over today's trip and going.
- Outmaster (hrs_52055997) | 5yo G | 161lb | OR 118 | draw 0 | jockey Freddie Keighley(3) | trainer Paul Nicholls (14d 6/32) | headgear p | last run 143 days | form 1/11 | MARKET 7.9% | 09:00 median 9.00 | Matchbook 12.50
    comment: Outmaster arrives unbeaten in his last three starts, having won last time out, and has run over today's trip and going before, but 143 days off is a concern, and 161 lb is a hefty burden.
- Step Ahead (hrs_41229748) | 6yo G | 164lb | OR 121 | draw 0 | jockey Aamilah Aswat(10) | trainer Kim Bailey & Mat Nicholls (14d 2/13) | headgear t | last run 35 days | form 2153-7 | MARKET 7.2% | 09:00 median 10.00 | Matchbook 13.50
    comment: Step Ahead has run over today's trip and on this going, and he won four starts back before a third and a fifth, but a seventh last time out and 35 days off leave questions.
- Norman Fletcher (hrs_33051522) | 7yo G | 156lb | OR 113 | draw 0 | jockey Jamie Brace | trainer Nigel & Willy Twiston-Davies (14d 5/35) | headgear v | last run 21 days | form 25322F | MARKET 6.9% | 09:00 median 9.50 | Matchbook 15.00
    comment: Norman Fletcher fell last time out but was second two starts back and second again three starts back, and he has run over today's trip and going, yet he remains winless in his last six.
- Lovely Gino (hrs_50590127) | 5yo G | 160lb | OR 117 | draw 0 | jockey Elliott England(8) | trainer Ben Pauling (14d 5/25) | headgear - | last run 229 days | form 12FFP- | MARKET 4.0% | 09:00 median 15.00 | Matchbook 29.00
    comment: Lovely Gino returns after 229 days off, pulled up last time out and a faller in each of the two runs before that, but he was a winner five starts back and a second four starts back. Unexposed, he could still have more to offer carrying 160 lb.
- Chutzpal (hrs_26328757) | 7yo G | 160lb | OR 117 | draw 0 | jockey Patrick M O'Brien | trainer Henry de Bromhead (14d 6/39) | headgear b | last run 50 days | form 1130/2 | MARKET 3.0% | 09:00 median 23.00 | Matchbook 34.00
    comment: Chutzpal showed solid recent form, second last time out and a winner four and five starts back, but he's had 50 days off and carries 160 lb.
- Kalium (hrs_412693008) | 6yo G | 168lb | OR 125 | draw 0 | jockey Richard Upton(7) | trainer Tim Vaughan (14d 0/6) | headgear - | last run 272 days | form 51/34- | MARKET 2.6% | 09:00 median 26.00 | Matchbook 38.00
    comment: Kalium arrives with a solid book of recent form, a fourth last time out, a third two starts back and a winner three starts back, and he has run on today's going before.
- Khafre (hrs_46697161) | 6yo G | 166lb | OR 123 | draw 0 | jockey Josh Williamson | trainer Syd Hosie (14d 2/7) | headgear - | last run 215 days | form 74115- | MARKET 2.5% | 09:00 median 26.00 | Matchbook 44.00
    comment: The main risk is a 215-day absence, with 166 lb to carry.
- Eton Mes (hrs_40394375) | 5yo G | 156lb | OR 113 | draw 0 | jockey Rian Corcoran(3) | trainer David Pipe (14d 0/12) | headgear p | last run 16 days | form 1135-2 | MARKET 2.4% | 09:00 median 29.00 | Matchbook 42.00
- Double Oban (hrs_34542627) | 6yo G | 162lb | OR 119 | draw 0 | jockey Lewis Saunders(3) | trainer Olly Murphy (14d 6/36) | headgear p | last run 29 days | form 215-52 | MARKET 2.3% | 09:00 median 29.00 | Matchbook 46.00
- No Ordinary Joe (hrs_21229215) | 10yo G | 165lb | OR 122 | draw 0 | jockey Jack Stenhouse(5) | trainer Robert Stephens (14d 1/6) | headgear tp | last run 18 days | form 61-065 | MARKET 1.9% | 09:00 median 35.00 | Matchbook 55.00
    comment: No Ordinary Joe has run over today's trip and on this going, and he is fresh enough after 18 days off.
- Boston Rajj (hrs_43637097) | 8yo G | 161lb | OR 118 | draw 0 | jockey Gearoid Brouder | trainer Ian O'Connor (14d 0/0) | headgear - | last run 21 days | form 5-7522 | MARKET 1.3% | 09:00 median 46.00 | Matchbook 100.00
    comment: Boston Rajj arrives in decent heart after a second last time out and another second two starts back, and he has run over today's trip and going before. Yet to win in his last five, he carries 161 lb off 118, which may cap him in this company.
- Razzle Dazzle Boy (hrs_41662327) | 6yo G | 158lb | OR 115 | draw 0 | jockey Jay Tidball | trainer Tim Vaughan (14d 0/6) | headgear - | last run 203 days | form 52125- | MARKET 1.2% | 09:00 median 34.00 | Matchbook 230.00
    comment: Razzle Dazzle Boy brings solid recent form, with a win three starts back and a second two starts back, but he was only fifth last time out and returns after 203 days off.
- Snatch A Glance (hrs_51124871) | 6yo G | 156lb | OR 113 | draw 0 | jockey Fern O'Brien(3) | trainer Fergal O'Brien (14d 3/26) | headgear - | last run 124 days | form F3-343 | MARKET 1.2% | 09:00 median 51.00 | Matchbook 95.00
    comment: Third last time out and in the frame in three of his last four, Snatch A Glance has run over today's trip and going before, but he's yet to win in recent starts and returns after 124 days off under 156 lb.
- Moon Mission (hrs_52329242) | 5yo G | 158lb | OR 115 | draw 0 | jockey Mr R Sugrue(10) | trainer P. J. Rothwell (14d 0/20) | headgear - | last run 30 days | form 0-15P4 | MARKET 1.2% | 09:00 median 51.00 | Matchbook 90.00
    comment: Moon Mission has finished fourth last time out, but he was pulled up two starts back and has won only once in his last five, a poor sequence made harder by a yard 0/20 over the last 14 days and 158 lb on his back.
- Heart Over Head (hrs_39392073) | 7yo G | 158lb | OR 115 | draw 0 | jockey Tom Broughton | trainer Fergal O'Brien (14d 3/26) | headgear - | last run 16 days | form 1108-7 | MARKET 0.5% | 09:00 median 101.00 | Matchbook 390.00
    comment: Heart Over Head has tailed off since winning four and five starts back, finishing an eighth two starts back and a seventh last time out, which makes him hard to fancy under 158 lb. In his favour, he has run over today's trip and going, and returns after 16 days.

## 1:45 Cheltenham | race_id rac_32304293684 | Mucking Brilliant Paddy Power Novices' Steeple Chase (Listed Race) (Registered As The Doctor Fothergill Novices' Steeple Chase) (GBB Race)
Chase | Class 1 | 3m1f0y | going Good | Turf | 6 runners | rating band - | age 4yo+
- King's Bucks (hrs_47620958) | 6yo G | 158lb | OR 133 | draw 0 | jockey Darragh O'Keeffe | trainer Henry de Bromhead (14d 6/39) | headgear - | last run 18 days | form 32P2-2 | MARKET 28.2% | 09:00 median 3.25 | Matchbook 3.40 | CHECK (skip line 3.09)
- Intosomethinggood (hrs_46759076) | 5yo G | 158lb | OR 135 | draw 0 | jockey Sam Twiston-Davies | trainer Nigel & Willy Twiston-Davies (14d 5/35) | headgear - | last run 7 days | form 4P1-13 | MARKET 18.9% | 09:00 median 4.50 | Matchbook 5.40
- Kingston Narcissus (hrs_32196367) | 7yo G | 158lb | OR 130 | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 22/93) | headgear tp | last run 14 days | form -12223 | MARKET 17.4% | 09:00 median 5.00 | Matchbook 5.70
- Follow Your Luck (hrs_49578046) | 5yo G | 158lb | OR 123 | draw 0 | jockey Brian Hughes | trainer Patrick Neville (14d 1/4) | headgear - | last run 20 days | form 11-312 | MARKET 12.8% | 09:00 median 7.00 | Matchbook 7.60
- D Art D Art (hrs_33660270) | 7yo G | 158lb | OR 134 | draw 0 | jockey Daniel King | trainer Mr Thomas Cooper (14d 0/1) | headgear - | last run 41 days | form P90-15 | MARKET 11.4% | 09:00 median 7.50 | Matchbook 8.80
- Bill Joyce (hrs_34361572) | 7yo G | 158lb | OR 130 | draw 0 | jockey Jonjo O'Neill Jr. | trainer Jonjo & A.J. O'Neill (14d 5/39) | headgear - | last run 23 days | form 0/PP-3 | MARKET 11.3% | 09:00 median 8.00 | Matchbook 8.20

## 2:20 Cheltenham | race_id rac_32304295621 | Shloer Steeple Chase (Registered As The Cheltenham Steeple Chase) (Grade 2) (GBB Race)
Chase | Class 1 | 1m7f199y | going Good | Turf | 4 runners | rating band - | age 4yo+
- Jonbon (hrs_22856064) | 10yo G | 164lb | OR 165 | draw 0 | jockey Harry Cobden | trainer Nicky Henderson (14d 3/14) | headgear p | last run 246 days | form 22112- | MARKET 48.8% | 09:00 median 1.91 | Matchbook 2.02
    comment: Jonbon was second last time out and a winner two and three starts back, so the form is rock solid, and he has run over today's trip and on this going before.
- Gidleigh Park (hrs_33547731) | 8yo G | 158lb | OR 155 | draw 0 | jockey Bryan Carver | trainer Harry Fry (14d 1/9) | headgear - | last run 217 days | form 2/2P5- | MARKET 26.6% | 09:00 median 3.50 | Matchbook 3.75
    comment: The main risk is a 217-day break, plus 158 lb on his back.
- Saint Segal (hrs_27464647) | 8yo G | 158lb | OR 153 | draw 0 | jockey Ciaran Gethings | trainer Mrs Jane Williams (14d 1/8) | headgear t | last run 30 days | form 22PP-4 | MARKET 13.4% | 09:00 median 6.50 | Matchbook 7.80
    comment: Fourth last time out after two pulled-up efforts, Saint Segal has two seconds four and five starts back and has run over today's trip and going, while 30 days since his last run suggests he's fresh. The risk is the 158 lb burden, yet to win in his last five starts.
- Mighty Bandit (hrs_38202976) | 6yo G | 158lb | OR 151 | draw 0 | jockey Sean Bowen | trainer Warren Greatrex (14d 4/19) | headgear - | wind surgery | last run 216 days | form 21114- | MARKET 11.2% | 09:00 median 8.50 | Matchbook 8.80
    comment: Mighty Bandit won three on the spin before a fourth last time out, and he has run over today's trip, so the form stacks up as a strong threat under 158 lb. The main risk is 216 days off the track, which leaves fitness the question.

## 2:55 Cheltenham | race_id rac_32304297558 | Jilly Cooper Veterans' Handicap Steeple Chase
Chase | Class 2 | 2m4f44y | going Good | Turf | 8 runners | rating band 0-150 | age 9yo+
- Thunder Rock (hrs_21453943) | 10yo G | 157lb | OR 134 | draw 0 | jockey Sean Bowen | trainer Olly Murphy (14d 6/36) | headgear - | last run 29 days | form 2110-1 | MARKET 25.5% | 09:00 median 3.50 | Matchbook 3.75 | CHECK (skip line 3.32)
    comment: Thunder Rock arrives a LTO winner with three wins in his last five starts, and he has run over today's trip and going before. The risk is the 157 lb he carries, though a 29-day break should have him fresh.
- Triple Trade (hrs_23979872) | 10yo G | 153lb | OR 130 | draw 0 | jockey Harry Cobden | trainer Joe Tizzard (14d 5/24) | headgear - | last run 19 days | form 34U6-1 | MARKET 22.3% | 09:00 median 4.00 | Matchbook 4.20
    comment: Triple Trade won last time out, just 19 days ago, and has run over today's trip and going, but a sixth and an unseated rider before that show inconsistency, and 153 lb is a stiff burden after a win.
- Glengouly (hrs_22738744) | 10yo G | 156lb | OR 133 | draw 0 | jockey Ben Jones | trainer Faye Bramley (14d 0/14) | headgear tp | last run 13 days | form PP-176 | MARKET 14.0% | 09:00 median 6.50 | Matchbook 6.80
    comment: Glengouly returned just 13 days ago and has run over today's trip and going, with a win three starts back, but he was only sixth last time out and seventh before that.
- Outlaw Peter (hrs_23624825) | 10yo G | 162lb | OR 139 | draw 0 | jockey Sam Twiston-Davies | trainer Paul Nicholls (14d 6/32) | headgear tp | last run 212 days | form 84213- | MARKET 11.3% | 09:00 median 6.50 | Matchbook 10.50
    comment: Outlaw Peter showed solid recent form, third last time out and a winner two starts back, and he has run over today's trip and on this going before; the main risk is a 212-day absence, with 162 lb to carry too.
- Ga Law (hrs_20995254) | 10yo G | 168lb | OR 145 | draw 0 | jockey Isabelle Ryder(5) | trainer Jamie Snowden (14d 11/26) | headgear p | last run 19 days | form 3/30-5 | MARKET 10.9% | 09:00 median 8.00 | Matchbook 9.00
    comment: Ga Law is without a win in his last four, but he arrives having finished third twice in his recent form, has run over today's trip and going, and returns after 19 days.
- Mahons Glory (hrs_21526708) | 10yo G | 165lb | OR 142 | draw 0 | jockey Lee Edwards | trainer Dylan Cunha (14d 1/9) | headgear - | last run 118 days | form 164-14 | MARKET 9.7% | 09:00 median 9.00 | Matchbook 10.00
    comment: The risk is a 118-day absence under 165 lb.
- Time To Bite (hrs_18572358) | 11yo G | 146lb | OR 123 | draw 0 | jockey Bryan Carver | trainer Chris Honour (14d 0/4) | headgear b | last run 33 days | form 130223 | MARKET 3.3% | 09:00 median 26.00 | Matchbook 30.00
    comment: Third last time out and runner-up in each of the two starts before, Time To Bite has been consistent, but he has not won since six starts back and carries 146 lb off a mark of 123.
- Copperhead (hrs_12127458) | 12yo G | 157lb | OR 134 | draw 0 | jockey Freddie Gingell | trainer Joe Tizzard (14d 5/24) | headgear tp | last run 229 days | form /7U13- | MARKET 2.9% | 09:00 median 29.00 | Matchbook 36.00
    comment: Third last time out, and a winner two starts back, Copperhead has run over today's trip and going, but a 229-day absence is a concern and 157 lb is a hefty burden.

## 3:30 Cheltenham | race_id rac_32304299495 | Albert Bartlett Novices' Hurdle Race(grade 2) (Registered As The Hyde) (GBB Race)
Hurdle | Class 1 | 2m5f0y | going Good | Turf | 10 runners | rating band - | age 4yo+
- Ferocimo (hrs_17393779018) | 4yo G | 155lb | OR - | draw 0 | jockey Sam Twiston-Davies | trainer Nigel & Willy Twiston-Davies (14d 5/35) | headgear - | wind surgery | last run 29 days | form 1-1 | MARKET 23.0% | 09:00 median 3.75 | Matchbook 4.20 | CHECK (skip line 3.56)
- Divine Diva (hrs_50188663) | 5yo M | 149lb | OR - | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 22/93) | headgear - | last run 33 days | form 1/30-1 | MARKET 14.9% | 09:00 median 5.50 | Matchbook 6.80
- Woodstock Octo (hrs_17394065843) | 6yo G | 156lb | OR - | draw 0 | jockey Ben Jones | trainer Kayley Woollacott (14d 0/6) | headgear - | last run 20 days | form 111-11 | MARKET 13.7% | 09:00 median 6.50 | Matchbook 7.00
- Lock Stock (hrs_41072703) | 6yo G | 156lb | OR 124 | draw 0 | jockey Charlie Hammond | trainer Stuart Edmunds (14d 1/10) | headgear - | last run 35 days | form 29-113 | MARKET 13.3% | 09:00 median 6.50 | Matchbook 7.20
- Dallas Star (hrs_35767613) | 5yo G | 156lb | OR 128 | draw 0 | jockey Donagh Meyler | trainer Emmet Mullins (14d 2/4) | headgear - | last run 27 days | form 12 | MARKET 10.4% | 09:00 median 8.50 | Matchbook 9.20
- Hitintheheadlines (hrs_49577976) | 5yo G | 156lb | OR - | draw 0 | jockey Tristan Durrell | trainer Dan Skelton (14d 22/93) | headgear - | last run 34 days | form /353-1 | MARKET 7.7% | 09:00 median 11.00 | Matchbook 12.50
- Luck Between Us (hrs_54304432) | 6yo G | 156lb | OR 125 | draw 0 | jockey Darragh O'Keeffe | trainer P. J. Rothwell (14d 0/20) | headgear - | last run 48 days | form 7-1211 | MARKET 5.9% | 09:00 median 15.00 | Matchbook 16.50
- Red Acres Georgie (hrs_41190079) | 6yo M | 149lb | OR 115 | draw 0 | jockey Harry Cobden | trainer Anthony Mullins (14d 0/1) | headgear - | last run 22 days | form 7-F422 | MARKET 4.8% | 09:00 median 17.00 | Matchbook 21.00
- Petersham Place (hrs_17393782147) | 6yo G | 156lb | OR - | draw 0 | jockey Sean Bowen | trainer Olly Murphy (14d 6/36) | headgear - | last run 29 days | form 1-1 | MARKET 4.4% | 09:00 median 17.00 | Matchbook 25.00
- Lion Rose Sivola (hrs_49577997) | 5yo G | 156lb | OR - | draw 0 | jockey Jonjo O'Neill Jr. | trainer Jonjo & A.J. O'Neill (14d 5/39) | headgear - | last run 33 days | form 1/22-2 | MARKET 1.7% | 09:00 median 41.00 | Matchbook 75.00

## 4:00 Cheltenham | race_id rac_32304301432 | Valda Energy Novices' Handicap Hurdle Race (GBB Race)
Hurdle | Class 3 | 2m0f87y | going Good | Turf | 18 runners | rating band 0-125 | age 3yo+
- Eben Zaabeel (hrs_37192295) | 5yo G | 163lb | OR 117 | draw 0 | jockey Daniel King | trainer Mr A. J. Martin (14d 0/10) | headgear ht | last run 33 days | form 0-12 | MARKET 21.6% | 09:00 median 3.50 | Matchbook 4.30 | CHECK (skip line 3.32)
    comment: Eben Zaabeel comes here in good heart, second last time out and a winner two starts back, and he has run on today's going before.
- Way of Stars (hrs_44450217) | 4yo G | 161lb | OR 115 | draw 0 | jockey Jack Tudor | trainer David Pipe (14d 0/12) | headgear t | last run 34 days | form 3210-2 | MARKET 12.9% | 09:00 median 5.50 | Matchbook 7.40
- Tuppence (hrs_47531575) | 6yo M | 158lb | OR 112 | draw 0 | jockey Mr Lucas Murphy(7) | trainer Lucinda Russell & Michael Scudamore (14d 10/46) | headgear h | last run 40 days | form /241-1 | MARKET 11.6% | 09:00 median 6.00 | Matchbook 8.60
- Crooked Path (hrs_50875335) | 4yo G | 166lb | OR 120 | draw 0 | jockey Jonathan Burke | trainer James Owen (14d 12/46) | headgear - | last run 21 days | form 31-313 | MARKET 10.9% | 09:00 median 7.00 | Matchbook 8.40
    comment: A 166 lb burden is the one reservation, though the in-form yard helps.
- Sytadel (hrs_17391197593) | 4yo G | 164lb | OR 118 | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 22/93) | headgear t | last run 22 days | form 232 | MARKET 8.2% | 09:00 median 9.00 | Matchbook 11.00
    comment: Sytadel has finished second, third and second in his last three, so he is bang in form after 22 days off, and he has run over today's trip and going before.
- Lexington Wood (hrs_51766309) | 5yo G | 159lb | OR 113 | draw 0 | jockey Sean Bowen | trainer Olly Murphy (14d 6/36) | headgear h | last run 37 days | form 428-24 | MARKET 7.8% | 09:00 median 9.50 | Matchbook 12.00
    comment: Lexington Wood was fourth last time out, with a second two starts back, and he has run over today's trip and going, but he is winless in his last five and returns after 37 days.
- Ade Boy (hrs_52677093) | 5yo G | 151lb | OR 105 | draw 0 | jockey Brian Hughes | trainer Charlie Longsdon (14d 5/14) | headgear tp | last run 28 days | form 634-23 | MARKET 5.1% | 09:00 median 13.00 | Matchbook 21.00
    comment: Ade Boy has been placed in three of his last five, including a third last time out and a second two starts back, and he has run over today's trip and going before after 28 days off. Yet to win in that spell, though, and 151 lb is a stiff burden to carry.
- Ocean of Dreams (hrs_36035783) | 5yo G | 152lb | OR 106 | draw 0 | jockey Mr O McGill(5) | trainer Gary McGill (14d 0/0) | headgear - | last run 21 days | form 068-61 | MARKET 3.9% | 09:00 median 19.00 | Matchbook 24.00
    comment: Fresh from a win last time out, but that came after a sixth, an eighth and another sixth, so the form is patchy, and carrying 152 lb off 106 is a big ask.
- Babyken (hrs_58099454) | 4yo G | 158lb | OR 112 | draw 0 | jockey Sam Twiston-Davies | trainer Paul Nicholls (14d 6/32) | headgear t | wind surgery | last run 249 days | form P234- | MARKET 3.1% | 09:00 median 23.00 | Matchbook 34.00
    comment: Babyken arrives with his placings getting worse with each run, fourth last time out, third two starts back and second three starts back, and he has run over today's trip and going before. A 249-day absence and 158 lb are the concerns, and he remains yet to win in recent starts.
- Whermyrosemarygoes (hrs_17389398418) | 5yo M | 153lb | OR 107 | draw 0 | jockey Harry Cobden | trainer Faye Bramley (14d 0/14) | headgear p (1st time) | last run 76 days | form 52-312 | MARKET 2.3% | 09:00 median 29.00 | Matchbook 46.00
    comment: Second last time out and a winner two starts back, so the recent form reads well, but a 76-day break and 153 lb are real obstacles.
- Final Surprise (hrs_51557975) | 5yo G | 154lb | OR 108 | draw 0 | jockey Ciaran Gethings | trainer Alastair Ralph (14d 0/3) | headgear - | last run 16 days | form 55-134 | MARKET 2.3% | 09:00 median 29.00 | Matchbook 46.00
    comment: Fourth last time out, a third two starts back and a winner three starts back show Final Surprise is in decent order, and he has run over today's trip and on this going before, fresh enough after 16 days.
- King's Scholar (hrs_40819548) | 5yo G | 168lb | OR 122 | draw 0 | jockey Tom Hutsby(10) | trainer Olly Murphy (14d 6/36) | headgear t | last run 35 days | form 4-1124 | MARKET 2.3% | 09:00 median 29.00 | Matchbook 46.00
    comment: King's Scholar won twice in his last five starts and was second two starts back, but he was only fourth last time out, and he returns after 35 days.
- Baymount (hrs_59928099) | 5yo M | 154lb | OR 108 | draw 0 | jockey Donagh Meyler | trainer Anthony Mullins (14d 0/1) | headgear - | last run 19 days | form P34214 | MARKET 1.8% | 09:00 median 34.00 | Matchbook 65.00
    comment: Baymount was fourth last time out, and a winner two starts back, which is a decent recent profile, and she has run over today's trip and going before.
- Mystic Rose (hrs_41053768) | 4yo F | 159lb | OR 113 | draw 0 | jockey Darragh O'Keeffe | trainer Patrick Magee (14d 1/3) | headgear - | last run 9 days | form 0-6412 | MARKET 1.7% | 09:00 median 41.00 | Matchbook 60.00
- Likewhatyousee (hrs_54178467) | 4yo F | 153lb | OR 107 | draw 0 | jockey Jonjo O'Neill Jr. | trainer Jonjo & A.J. O'Neill (14d 5/39) | headgear - | last run 27 days | form 2126F4 | MARKET 1.4% | 09:00 median 51.00 | Matchbook 75.00
    comment: Fourth last time out and fit enough after 27 days, Likewhatyousee has run over today's trip and going, and she won five starts back.
- Kilt (hrs_37860599) | 5yo G | 152lb | OR 106 | draw 0 | jockey Mr R Sugrue(7) | trainer P. J. Rothwell (14d 0/20) | headgear h | last run 34 days | form 454618 | MARKET 1.3% | 09:00 median 51.00 | Matchbook 90.00
    comment: In his favour, he won two starts back and has run over today's trip and going before.
- First Ascent (hrs_52021263) | 5yo G | 167lb | OR 121 | draw 0 | jockey Josh Williamson(3) | trainer Gordon Elliott (14d 8/53) | headgear tp | last run 23 days | form 542310 | MARKET 1.0% | 09:00 median 67.00 | Matchbook 110.00
    comment: First Ascent won two starts back and has been in the first four in most of his recent runs, but he was unplaced last time out, and carrying 167 lb off a mark of 121 looks a stiff ask.
- Shallow Bowles (hrs_51650095) | 6yo M | 154lb | OR 108 | draw 0 | jockey Mr Daniel Williams(7) | trainer Nick Scholfield (14d 0/19) | headgear t (1st time) | last run 276 days | form 4846- | MARKET 0.7% | 09:00 median 101.00 | Matchbook 150.00
    comment: Shallow Bowles is winless in her last four, finishing sixth last time out, and she returns after 276 days off, which is a lot to ask.
