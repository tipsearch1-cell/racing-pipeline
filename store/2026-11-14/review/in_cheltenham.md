# Card review packet: Cheltenham, 2026-11-14

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


## 12:35 Cheltenham | race_id rac_32304421526 | Citipost Amateur Jockeys' Handicap Steeple Chase (GBB Race)
Chase | Class 3 | 3m1f0y | going Good | Turf | 10 runners | rating band 0-135 | age 4yo+
- Little Ledgend (hrs_40352564) | 6yo G | 158lb | OR 125 | draw 0 | jockey Mr James King | trainer Olly Murphy (14d 8/41) | headgear tb (1st time) | last run 22 days | form -22113 | MARKET 23.5% | 09:00 median 3.50 | Matchbook 4.20 | CHECK (skip line 3.32)
    comment: Little Ledgend arrives in fine heart, third last time out, and a winner two starts back, with a win three starts back too, and he has run over today's trip and going before.
- Karnaval Point (hrs_42847455) | 6yo G | 156lb | OR 123 | draw 0 | jockey Mr Lucas Murphy(5) | trainer David Pipe (14d 0/10) | headgear tb | last run 21 days | form 635623 | MARKET 13.6% | 09:00 median 6.50 | Matchbook 6.80
    comment: Karnaval Point arrives in sound form, third last time out and a second two starts back, and he has run over today's trip and going before.
- Our Soldier (hrs_34598242) | 7yo G | 155lb | OR 122 | draw 0 | jockey Mr D Doyle | trainer Denis Gerard Hogan (14d 1/15) | headgear - | last run 13 days | form 11-732 | MARKET 11.8% | 09:00 median 7.50 | Matchbook 8.00
- Herakles Westwood (hrs_28720825) | 9yo G | 168lb | OR 135 | draw 0 | jockey Miss Gina Andrews | trainer Warren Greatrex (14d 4/21) | headgear - | last run 210 days | form 2410P- | MARKET 11.6% | 09:00 median 7.00 | Matchbook 8.60
    comment: The main risk is a 210-day absence after being pulled up last time out, with 168 lb to carry.
- Ladies Well (hrs_45445246) | 6yo M | 143lb | OR 110 | draw 0 | jockey Mr A P Ryan | trainer A. Slattery (14d 1/17) | headgear t | last run 14 days | form 121414 | MARKET 11.2% | 09:00 median 7.50 | Matchbook 8.80
    comment: Ladies Well has won three of her last six, including two starts back, and has run over today's trip and going, but a fourth last time out and a 143 lb burden off 110 make her hard to fancy.
- Dinoland (hrs_29691186) | 8yo G | 153lb | OR 120 | draw 0 | jockey Mr O McGill | trainer W R Crawford (14d 0/1) | headgear tv | last run 14 days | form P-1152 | MARKET 10.0% | 09:00 median 8.50 | Matchbook 9.60
    comment: He has run over today's trip and going, and he's fresh enough after 14 days.
- Transmission (hrs_27697243) | 9yo G | 164lb | OR 131 | draw 0 | jockey Mr J W Hendrick(3) | trainer Neil Mulholland (14d 7/28) | headgear p | last run 14 days | form 137-50 | MARKET 7.7% | 09:00 median 10.00 | Matchbook 13.50
    comment: Fresh from a run 14 days ago, Transmission has run over today's trip and on this going, and he showed his ability with a win five starts back and a third four starts back.
- Brucejack (hrs_27697264) | 9yo G | 151lb | OR 118 | draw 0 | jockey Mr D O'Sullivan(7) | trainer P A Fahy (14d 0/8) | headgear - | last run 14 days | form 517-83 | MARKET 4.5% | 09:00 median 17.00 | Matchbook 24.00
    comment: Brucejack bounced back with a third last time out, but an eighth two starts back and a seventh three starts back show inconsistency, with his only win in his last five a fourth-back affair.
- Sound And Fury (hrs_29621921) | 9yo G | 159lb | OR 126 | draw 0 | jockey Mr Freddie Robson(7) | trainer Ben Pauling (14d 4/21) | headgear p | last run 252 days | form 16815- | MARKET 3.3% | 09:00 median 26.00 | Matchbook 30.00
    comment: The risk is a 252-day absence, plus 159 lb.
- Awaythelad (hrs_27279091) | 9yo G | 145lb | OR 112 | draw 0 | jockey Mr Samuel Scott(7) | trainer Ben Pauling (14d 4/21) | headgear - | last run 38 days | form /P7P-5 | MARKET 2.8% | 09:00 median 29.00 | Matchbook 34.00
    comment: Awaythelad is winless in his last four, with a fifth last time out, a seventh three starts back and two pulled-up efforts, but he has run over today's trip and going and returns after 38 days.

## 1:10 Cheltenham | race_id rac_32304423463 | JCB Triumph Trial Juvenile Hurdle Race (Registered As The Prestbury Juvenile Hurdle Race) (Grade 2) (GBB Race)
Hurdle | Class 1 | 2m0f87y | going Good | Turf | 8 runners | rating band - | age 3yo
- Atomic City (hrs_58347576) | 3yo G | 154lb | OR - | draw 0 | jockey J. J. Slevin | trainer Joseph Patrick O'Brien (14d 3/28) | headgear - | last run 34 days | form 1 | MARKET 36.0% | 09:00 median 2.50 | Matchbook 2.68
- Charles Darnay (hrs_60752720) | 3yo G | 154lb | OR - | draw 0 | jockey Harry Cobden | trainer James Owen (14d 10/42) | headgear - | last run 15 days | form 1 | MARKET 32.1% | 09:00 median 2.75 | Matchbook 3.10
    comment: Winner last time out just 15 days ago, Charles Darnay is fit and fresh, and he has run over today's trip and on this going before.
- Admiral Will Brown (hrs_56338513) | 3yo G | 154lb | OR - | draw 0 | jockey Josh Williamson | trainer Patrick Magee (14d 0/3) | headgear t | last run 14 days | form 1 | MARKET 14.6% | 09:00 median 6.00 | Matchbook 6.60
    comment: Fresh from a win last time out just 14 days ago, he has run over today's trip and going before, which is a solid platform.
- Magnetude (hrs_57103410) | 3yo G | 154lb | OR - | draw 0 | jockey Jonathan Burke | trainer James Owen (14d 10/42) | headgear - | last run 31 days | form 1 | MARKET 7.7% | 09:00 median 11.00 | Matchbook 13.50
    comment: Magnetude won last time out, 31 days ago, and has run over today's trip, which is a decent starting point.
- Don Dandy (hrs_63971166) | 3yo G | 154lb | OR 127 | draw 0 | jockey Sean Bowen | trainer Olly Murphy (14d 8/41) | headgear p (1st time) | last run 20 days | form 421-2 | MARKET 5.6% | 09:00 median 15.00 | Matchbook 18.50
    comment: Don Dandy arrives in cracking nick, second last time out, a winner two starts back, and a second three starts back, with just 20 days since his last run and experience of today's trip.
- Confused (hrs_64036868) | 3yo G | 154lb | OR - | draw 0 | jockey Richie McLernon | trainer Faye Bramley (14d 0/14) | headgear p | last run 15 days | form 64 | MARKET 1.7% | 09:00 median 51.00 | Matchbook 75.00
    comment: The main risk is a 154 lb burden, and he is yet to win in his last two starts.
- Electrical (hrs_54337423) | 3yo G | 154lb | OR - | draw 0 | jockey Sean Flanagan | trainer Brian Toomey (14d 1/2) | headgear - | last run 17 days | form - | MARKET 1.6% | 09:00 median 81.00 | Matchbook 50.00
    comment: Electrical is unexposed with no recorded form to go on, so he's open to improvement, and he returns after just 17 days off while carrying 154 lb.
- Tiny Riot (hrs_57103466) | 3yo G | 154lb | OR 105 | draw 0 | jockey Tristan Durrell | trainer Max Young (14d 0/4) | headgear - | last run 115 days | form 122 | MARKET 0.8% | 09:00 median 126.00 | Matchbook 140.00

## 1:45 Cheltenham | race_id rac_32304425400 | Paddy Power Arkle Challenge Trophy Trial Novices' Steeple Chase (Grade 2) (Registered As The November) (GBB Race)
Chase | Class 1 | 1m7f199y | going Good | Turf | 5 runners | rating band - | age 4yo+
- Workahead (hrs_33859721) | 8yo G | 158lb | OR 148 | draw 0 | jockey Darragh O'Keeffe | trainer Henry de Bromhead (14d 6/37) | headgear - | last run 159 days | form 429-12 | MARKET 43.7% | 09:00 median 2.10 | Matchbook 2.26
- Putapoundinthejar (hrs_40225297) | 6yo G | 158lb | OR 139 | draw 0 | jockey Daniel King | trainer A. J. Martin (14d 0/11) | headgear - | last run 34 days | form -31121 | MARKET 18.3% | 09:00 median 5.00 | Matchbook 5.40
- Folie Golith (hrs_51491909) | 4yo F | 143lb | OR 137 | draw 0 | jockey Sean Bowen | trainer Faye Bramley (14d 0/14) | headgear - | last run 29 days | form 2262-1 | MARKET 18.1% | 09:00 median 5.00 | Matchbook 5.60
- Passing Diamond (hrs_41190051) | 6yo G | 158lb | OR 128 | draw 0 | jockey Richie McLernon | trainer Ben Haslam (14d 1/7) | headgear - | last run 22 days | form 131112 | MARKET 12.9% | 09:00 median 7.00 | Matchbook 7.80
- Newtown Rambler (hrs_41052543) | 7yo G | 158lb | OR 137 | draw 0 | jockey Oakley Brown | trainer Adrian Keatley (14d 0/3) | headgear tp | last run 21 days | form -111P1 | MARKET 7.0% | 09:00 median 13.00 | Matchbook 14.50

## 2:20 Cheltenham | race_id rac_32303241893 | Paddy Power Gold Cup Handicap Steeple Chase (Premier Handicap) (Registered As The William Holman) (GBB Race)
Chase | Class 1 | 2m4f44y | going Good | Turf | 12 runners | rating band - | age 4yo+
- Meetmebythesea (hrs_40494041) | 6yo G | 164lb | OR 151 | draw 0 | jockey Harry Cobden | trainer Ben Pauling (14d 4/21) | headgear - | last run 247 days | form /1161- | MARKET 22.9% | 09:00 median 3.50 | Matchbook 4.30 | CHECK (skip line 3.32)
    comment: Meetmebythesea has won three of his last four, including last time out, and has run over today's trip and going before, but a 247-day absence and 164 lb on an official mark of 151 are hurdles to overcome.
- Blueking d'Oroux (hrs_29785756) | 7yo G | 161lb | OR 148 | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 19/92) | headgear p | last run 219 days | form 21522- | MARKET 14.4% | 09:00 median 5.50 | Matchbook 6.80
    comment: The main risk is a 219-day absence, and he carries 161 lb.
- July Flower (hrs_34990970) | 7yo M | 155lb | OR 142 | draw 0 | jockey Darragh O'Keeffe | trainer Henry de Bromhead (14d 6/37) | headgear - | last run 200 days | form 11354- | MARKET 13.2% | 09:00 median 6.50 | Matchbook 7.00
    comment: July Flower won twice in her last five starts, though that was four and five starts back, and she's since managed a fifth, then a fourth last time out. She has run over today's trip and going, but 200 days off and 155 lb are hurdles to clear.
- Quebecois (hrs_34457262) | 7yo G | 154lb | OR 141 | draw 0 | jockey Sam Twiston-Davies | trainer Paul Nicholls (14d 5/31) | headgear t | last run 28 days | form 223P-2 | MARKET 11.1% | 09:00 median 7.00 | Matchbook 9.00
    comment: Quebecois bounces back from a pulled-up effort with a second last time out, and he has run over today's trip and going before, but he is winless in his last five and has to carry 154 lb off 141 after 28 days off.
- Zurich (hrs_47655517) | 7yo G | 151lb | OR 138 | draw 0 | jockey Sean Bowen | trainer Henry de Bromhead (14d 6/37) | headgear t (1st time) | last run 27 days | form 1352-5 | MARKET 9.1% | 09:00 median 9.00 | Matchbook 11.00
- Release The Beast (hrs_37687412) | 7yo G | 148lb | OR 135 | draw 0 | jockey Sean Flanagan | trainer Paul Nolan (14d 5/29) | headgear t | last run 198 days | form /224U- | MARKET 8.2% | 09:00 median 10.00 | Matchbook 11.50
    comment: Release The Beast unseated last time out and returns after 198 days off, which makes him hard to fancy, though a fourth, then two seconds in the runs before that, show he can be competitive, and he has run over today's trip and going.
- O'Moore Park (hrs_27153350) | 9yo G | 151lb | OR 138 | draw 0 | jockey Freddie Keighley(5) | trainer Martin Keighley (14d 2/8) | headgear - | last run 21 days | form 67-931 | MARKET 5.5% | 09:00 median 13.00 | Matchbook 19.50
    comment: O'Moore Park won last time out and was third two starts back, so he arrives in good heart after 21 days off, having run over today's trip and going before.
- Torneo (hrs_35123795) | 6yo G | 147lb | OR 134 | draw 0 | jockey Gavin Sheehan | trainer Jamie Snowden (14d 11/26) | headgear - | last run 31 days | form 2461-1 | MARKET 5.2% | 09:00 median 15.00 | Matchbook 19.00
    comment: Torneo arrives a double winner, successful last time out and two starts back, and he has run over today's trip and going, with a yard in cracking form.
- Matata (hrs_28824495) | 8yo G | 168lb | OR 155 | draw 0 | jockey J. J. Slevin | trainer Nigel & Willy Twiston-Davies (14d 6/36) | headgear - | last run 210 days | form 155PF- | MARKET 4.8% | 09:00 median 17.00 | Matchbook 20.00
    comment: Matata won five starts back and was fifth on each of his two runs after that, though a fall last time and a pulled up since temper the picture after 210 days off.
- Riskintheground (hrs_27358730) | 9yo G | 159lb | OR 146 | draw 0 | jockey Harry Atkins(5) | trainer Dan Skelton (14d 19/92) | headgear t | last run 14 days | form -21363 | MARKET 3.2% | 09:00 median 21.00 | Matchbook 34.00
    comment: Riskintheground arrives fresh from a third last time out just 14 days ago, and he has a winner four starts back plus a second five starts back, with experience over today's trip and going. The main risk is a hefty 159 lb, with a sixth two starts back showing he can falter.
- Dunkerque (hrs_49359051) | 6yo G | 145lb | OR 132 | draw 0 | jockey Sean Quinlan | trainer Jennie Candlish (14d 2/8) | headgear p | last run 53 days | form 112123 | MARKET 1.5% | 09:00 median 41.00 | Matchbook 85.00
    comment: Dunkerque's recent form reads well, with a third last time out, a second, and three wins in his last six starts, and he has run over today's trip and going.
- Guard Your Dreams (hrs_21378623) | 10yo G | 151lb | OR 138 | draw 0 | jockey Toby McCain-Mitchell(3) | trainer Nigel & Willy Twiston-Davies (14d 6/36) | headgear t | last run 31 days | form 21B4-P | MARKET 0.9% | 09:00 median 81.00 | Matchbook 110.00
    comment: Guard Your Dreams won four starts back and was a fourth two runs ago, but he was pulled up last time out and has had 31 days since.

## 2:55 Cheltenham | race_id rac_32304427337 | From The Horses Mouth Podcast Handicap Hurdle Race (GBB Race)
Hurdle | Class 2 | 2m7f208y | going Good | Turf | 12 runners | rating band - | age 4yo+
- William Yeats (hrs_52495289) | 5yo G | 145lb | OR 114 | draw 0 | jockey Jonathan England | trainer Sam England (14d 6/20) | headgear t | last run 9 days | form 3-1221 | MARKET 19.8% | 09:00 median 4.33 | Matchbook 4.60 | CHECK (skip line 4.11)
    comment: Fresh from a run nine days ago and with a hot yard behind him, he has experience of today's trip and going.
- Horaces Pearl (hrs_32751355) | 8yo G | 163lb | OR 132 | draw 0 | jockey Tom Broughton(3) | trainer Fergal O'Brien (14d 3/28) | headgear - | last run 357 days | form 153/5- | MARKET 17.7% | 09:00 median 4.33 | Matchbook 5.70
    comment: Horaces Pearl showed he can win four starts back and was third two runs later, while his fifth last time out keeps him in the picture, and he has run over today's trip and going before. The big risk is a 357-day absence under 163 lb.
- Ifiwerearichman (hrs_28824432) | 8yo G | 158lb | OR 127 | draw 0 | jockey Eoin Staples(5) | trainer Paul Nolan (14d 5/29) | headgear p | last run 49 days | form P-3686 | MARKET 13.9% | 09:00 median 6.00 | Matchbook 6.80
    comment: Ifiwerearichman is yet to win in his last five, with sixth last time out, an eighth and a third four starts back, though he has run over today's trip and going before.
- Aimeric (hrs_29801800) | 7yo G | 146lb | OR 115 | draw 0 | jockey William Shanahan(5) | trainer Jennie Candlish (14d 2/8) | headgear - | last run 38 days | form -44211 | MARKET 11.7% | 09:00 median 7.00 | Matchbook 8.20
    comment: Aimeric arrives in cracking heart, having won last time out and two starts back, and he has run on today's going before, yet he is hard to fancy.
- Rambo T (hrs_24769563) | 9yo G | 164lb | OR 133 | draw 0 | jockey Sean Bowen | trainer Olly Murphy (14d 8/41) | headgear - | last run 35 days | form 000-65 | MARKET 10.7% | 09:00 median 8.20 | Matchbook 8.60
- Moon Mission (hrs_52329242) | 5yo G | 146lb | OR 115 | draw 0 | jockey Alan O'Sullivan | trainer P. J. Rothwell (14d 0/23) | headgear - | last run 1 days | form -15P45 | MARKET 6.9% | 09:00 median 12.00 | Matchbook 14.00
    comment: Moon Mission was a fifth last time out, and a fourth two starts back, but he has won just once in his last five and was pulled up three starts back. Back out after only one day, with a yard 0/23 lately and 146 lb to carry, he is hard to fancy, though he has run on today's going before.
- Sir Galahad (hrs_37207975) | 5yo G | 166lb | OR 135 | draw 0 | jockey Lewis Saunders(5) | trainer Olly Murphy (14d 8/41) | headgear p | last run 105 days | form 60-210 | MARKET 6.3% | 09:00 median 12.00 | Matchbook 16.50
    comment: Sir Galahad won two starts back and was second three starts back, but he was unplaced last time out and returns after 105 days off.
- Black Bamboo (hrs_24687572) | 9yo G | 149lb | OR 118 | draw 0 | jockey Michael Kenneally(3) | trainer John Joseph Murphy (14d 0/1) | headgear b | last run 13 days | form 009-02 | MARKET 4.7% | 09:00 median 17.00 | Matchbook 21.00
    comment: Black Bamboo comes into this on the back of a second last time out, a clear step up on three unplaced runs and a ninth before that, and he's fresh enough after 13 days. He has run over today's trip and going, but he's yet to win in his last five and 149 lb is a hefty burden.
- Margaret's Legacy (hrs_23715685) | 9yo G | 157lb | OR 126 | draw 0 | jockey Richard Upton(10) | trainer Warren Greatrex (14d 4/21) | headgear h | last run 198 days | form 24600- | MARKET 2.9% | 09:00 median 29.00 | Matchbook 34.00
    comment: Margaret's Legacy is yet to win in his last five starts, with two unplaced runs most recently and a second five starts back, and he returns after 198 days off.
- Lucky Lyreen (hrs_29523193) | 8yo G | 160lb | OR 129 | draw 0 | jockey Freddie Keighley(5) | trainer Martin Keighley (14d 2/8) | headgear v (1st time) | last run 173 days | form 5105-P | MARKET 2.4% | 09:00 median 34.00 | Matchbook 46.00
    comment: Pulled up last time out and off 173 days since, Lucky Lyreen has a win four starts back and has run over today's trip and going, but a long absence and a fifth two starts back leave questions.
- Hartur d'Arc (hrs_27237539) | 9yo G | 151lb | OR 120 | draw 0 | jockey Conor Smithers(7) | trainer John McConnell (14d 1/11) | headgear - | last run 222 days | form P0P8P- | MARKET 1.5% | 09:00 median 41.00 | Matchbook 85.00
    comment: Hartur d'Arc has been pulled up in three of his last five and was last seen 222 days ago, so fitness is a question, though he has run over today's trip and on the going before.
- Blizzard of Oz (hrs_29509879) | 8yo G | 158lb | OR 127 | draw 0 | jockey Richie McLernon | trainer Faye Bramley (14d 0/14) | headgear - | last run 21 days | form 1P-580 | MARKET 1.4% | 09:00 median 51.00 | Matchbook 80.00
    comment: The main risk is a poor recent run, unplaced last time and an eighth two starts back, with 158 lb to carry.

## 3:30 Cheltenham | race_id rac_32304429274 | Paddy Power Intermediate Handicap Hurdle Race
Hurdle | Class 3 | 2m5f0y | going Good | Turf | 9 runners | rating band 0-140 | age 3yo+
- Daylatedollarshort (hrs_52709111) | 5yo G | 168lb | OR 135 | draw 0 | jockey Sean Bowen | trainer Olly Murphy (14d 8/41) | headgear - | last run 35 days | form 4112-1 | MARKET 25.1% | 09:00 median 3.50 | Matchbook 3.85 | CHECK (skip line 3.32)
    comment: Daylatedollarshort has won three of his last five starts, including last time out, with a second in between, and he has run over today's trip and going before.
- Sunny South West (hrs_46697217) | 6yo G | 154lb | OR 121 | draw 0 | jockey Michael Kenneally(3) | trainer Edward F Power (14d 1/4) | headgear h | last run 22 days | form 1462-4 | MARKET 17.7% | 09:00 median 5.00 | Matchbook 5.50
- Hillberry Hill (hrs_57654632) | 5yo G | 155lb | OR 122 | draw 0 | jockey Tom Bellamy | trainer Kim Bailey & Mat Nicholls (14d 2/15) | headgear - | last run 235 days | form 611- | MARKET 17.0% | 09:00 median 5.00 | Matchbook 5.80
    comment: Hillberry Hill won last time out and two starts back, with a sixth three starts back, and he has run over today's trip and going before.
- Grand Conqueror (hrs_52055787) | 5yo G | 160lb | OR 127 | draw 0 | jockey Richie McLernon | trainer Neil Mulholland (14d 7/28) | headgear h | last run 24 days | form 122-31 | MARKET 11.7% | 09:00 median 7.50 | Matchbook 8.40
    comment: Grand Conqueror arrives a last-time-out winner, with a third and two seconds in between, and has run over today's trip and going, though carrying 160 lb off an official 127 looks a stiff ask.
- Emerald Breeze (hrs_48112204) | 6yo G | 153lb | OR 120 | draw 0 | jockey Toby McCain-Mitchell(3) | trainer Ryan Hatch (14d 0/1) | headgear - | last run 223 days | form /3231- | MARKET 7.7% | 09:00 median 11.00 | Matchbook 13.00
    comment: Emerald Breeze won last time out and has been third, second and third in the starts before, with experience of today's trip and going, but a 223-day absence and 153 lb on an official 120 make him hard to fancy.
- Seamoon Story (hrs_51831878) | 5yo G | 161lb | OR 128 | draw 0 | jockey Daire McConville(7) | trainer Charlie Longsdon (14d 5/16) | headgear - | last run 29 days | form 4551-1 | MARKET 7.5% | 09:00 median 12.00 | Matchbook 13.00
    comment: Seamoon Story arrives in cracking nick, having won last time out and two starts back, and he has run over today's trip and going before after a 29-day break. The one concern is a weight of 161 lb, which could stretch him.
- Give Him A Chance (hrs_39959535) | 7yo G | 152lb | OR 119 | draw 0 | jockey Alan O'Sullivan(5) | trainer P. J. Rothwell (14d 0/23) | headgear - | last run 49 days | form 1S7-54 | MARKET 5.8% | 09:00 median 13.00 | Matchbook 18.50
    comment: Fourth last time out, and a fifth and a seventh before that, show Give Him A Chance running respectably without winning since a success five starts back; he has run over today's trip and going, but 49 days off, 152 lb and a yard 0/23 lately temper the appeal.
- Luck Between Us (hrs_54304432) | 6yo G | 158lb | OR 125 | draw 0 | jockey Darragh O'Keeffe | trainer P. J. Rothwell (14d 0/23) | headgear - | last run 1 days | form -12117 | MARKET 4.2% | 09:00 median 21.00 | Matchbook 24.00
    comment: Hard to fancy after a seventh last time out just one day ago, with a stable at 0/23 in the last 14 days and 158 lb to carry. On the plus side, he won twice and a third time in his last five, and has run over today's trip and going.
- Open Secret (hrs_38532256) | 5yo G | 165lb | OR 132 | draw 0 | jockey Josh Williamson(3) | trainer Gordon Elliott (14d 6/41) | headgear t | last run 47 days | form 14200- | MARKET 3.4% | 09:00 median 26.00 | Matchbook 30.00
    comment: The risk is two unplaced runs since, plus 47 days off and 165 lb to carry.

## 4:00 Cheltenham | race_id rac_32304431211 | Karndean Designflooring Mares' Open National Hunt Flat Race(listed Race) (Registered As The Dorothy Paget) (GBB Race)
NH Flat | Class 1 | 2m0f87y | going Good | Turf | 12 runners | rating band - | age 4-5yo
- Elegantemente (hrs_17390238033) | 4yo F | 156lb | OR - | draw 0 | jockey Darragh O'Keeffe | trainer Henry de Bromhead (14d 6/37) | headgear - | last run 82 days | form 1 | MARKET 27.8% | 09:00 median 3.00 | Matchbook 3.35 | CHECK (skip line 2.85)
    comment: The main risk is an 82-day absence, which may leave her short of peak fitness.
- Soleretta (hrs_17394328679) | 4yo F | 156lb | OR - | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 19/92) | headgear - | last run 251 days | form F- | MARKET 18.9% | 09:00 median 4.50 | Matchbook 4.80
    comment: Lightly raced and unexposed, Soleretta fell on her only recent start and returns after 251 days off, so there's scope for improvement, though she's yet to win in recent form. She carries 156 lb on her comeback.
- Eastern Whisper (hrs_17393747728) | 5yo M | 156lb | OR - | draw 0 | jockey Harry Cobden | trainer S G Carey (14d 0/5) | headgear - | last run 32 days | form 1 | MARKET 12.8% | 09:00 median 6.00 | Matchbook 7.80
    comment: Eastern Whisper won last time out and has run over today's trip and going, but a 32-day break and 156 lb on her back make her hard to fancy.
- Miss Master (hrs_17395395668) | 4yo F | 156lb | OR - | draw 0 | jockey Sean Bowen | trainer Olly Murphy (14d 8/41) | headgear - | last run 230 days | form 1- | MARKET 10.4% | 09:00 median 8.00 | Matchbook 9.20
    comment: Winner last time out, Miss Master returns after 230 days off with just that one recent run to go on, so she's unexposed and open to improvement. She carries 156 lb, and the long absence is the question.
- Gypsy Sky (hrs_17393247088) | 4yo F | 156lb | OR - | draw 0 | jockey Richie McLernon | trainer David Killahena & Graeme McPherson (14d 6/11) | headgear - | last run 40 days | form 1 | MARKET 7.7% | 09:00 median 10.00 | Matchbook 13.50
    comment: The main risk is the 156 lb she must carry.
- She Was The One (hrs_17390038820) | 4yo F | 156lb | OR - | draw 0 | jockey Daniel King | trainer Denis Gerard Hogan (14d 1/15) | headgear - | last run 50 days | form 52-321 | MARKET 7.6% | 09:00 median 11.00 | Matchbook 12.50
    comment: The 50-day break is the one question, while 156 lb is a hefty burden.
- Sarah's Sister (hrs_17395397754) | 4yo F | 156lb | OR - | draw 0 | jockey Jonathan Burke | trainer Nick Scholfield (14d 0/12) | headgear - | last run 42 days | form 1 | MARKET 5.0% | 09:00 median 17.00 | Matchbook 20.00
    comment: Unexposed filly who won last time out, her only recent start, so she arrives fresh after 42 days off and open to further improvement. She carries 156 lb, though her limited form leaves plenty still to learn.
- Kshira Sagara (hrs_17395394625) | 4yo F | 156lb | OR - | draw 0 | jockey Alex Harvey | trainer John McConnell (14d 1/11) | headgear t (1st time) | last run - days | form - | MARKET 2.6% | 09:00 median 26.00 | Matchbook 48.00
    comment: Kshira Sagara is an unraced filly with no form to assess, so she's a pure unknown and open to plenty of improvement. She carries 156 lb on her first outing, and the stable's intentions will be the interesting part.
- Clovelly Charm (hrs_57439354) | 5yo M | 156lb | OR - | draw 0 | jockey Sean Flanagan | trainer P A Fahy (14d 0/8) | headgear - | last run 78 days | form 513 | MARKET 2.4% | 09:00 median 29.00 | Matchbook 48.00
- Island Jetaway (hrs_62393905) | 4yo F | 156lb | OR - | draw 0 | jockey Gavin Sheehan | trainer Billy Aprahamian (14d 0/7) | headgear - | last run 183 days | form 1-2 | MARKET 2.0% | 09:00 median 34.00 | Matchbook 60.00
    comment: Island Jetaway arrives with a second last time out and a win two starts back, and she has run over today's trip and on this going before; the main risk is a 183-day layoff, with 156 lb to carry.
- Orderandout (hrs_17395396711) | 4yo F | 156lb | OR - | draw 0 | jockey Jack Quinlan | trainer Neil King (14d 0/8) | headgear - | last run 251 days | form 2- | MARKET 2.0% | 09:00 median 34.00 | Matchbook 60.00
    comment: Unexposed filly who finished second on her only recent start, yet to win, and she returns after 251 days off; carrying 156 lb, she looks open to improvement on that limited evidence.
- Miss Spec (hrs_17394533107) | 5yo M | 156lb | OR - | draw 0 | jockey Tom Broughton | trainer Fergal O'Brien (14d 3/28) | headgear - | last run 17 days | form 1-4 | MARKET 0.7% | 09:00 median 81.00 | Matchbook 220.00
    comment: Miss Spec won two starts back before finishing fourth last time out, and she has run over today's trip, but carrying 156 lb is a stiff ask.
