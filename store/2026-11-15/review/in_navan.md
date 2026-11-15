# Card review packet: Navan, 2026-11-15

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
{"meeting": "navan", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 11:40 Navan | race_id rac_32304599730 | BAR 1 Casino 3-Y-O Maiden Hurdle
Hurdle |  | 2m0f0y | going Good To Yielding | Turf | 15 runners | rating band - | age 3yo
- Norman Prince (hrs_17394805330) | 3yo G | 154lb | OR - | draw 0 | jockey Jack Kennedy | trainer Gordon Elliott (14d 10/58) | headgear t (1st time) | last run 222 days | form 2- | MARKET 39.7% | 09:00 median 2.00 | Matchbook 2.28
- Huff'n'puff (hrs_56843899) | 3yo G | 154lb | OR - | draw 0 | jockey Jordan Gainford | trainer Henry de Bromhead (14d 7/41) | headgear - | last run 54 days | form - | MARKET 19.3% | 09:00 median 4.33 | Matchbook 4.60
- Green Soul (hrs_50434314) | 3yo G | 154lb | OR - | draw 0 | jockey J. J. Slevin | trainer Joseph Patrick O'Brien (14d 3/21) | headgear - | last run 20 days | form 45 | MARKET 11.7% | 09:00 median 7.00 | Matchbook 7.80
- Sunrush (hrs_55978517) | 3yo G | 154lb | OR - | draw 0 | jockey Philip Donovan | trainer A. Slattery (14d 1/12) | headgear t (1st time) | last run 16 days | form - | MARKET 10.0% | 09:00 median 8.00 | Matchbook 9.00
- Mergus Serrator (hrs_57878037) | 3yo G | 154lb | OR - | draw 0 | jockey Conor Stone-Walsh | trainer Gavin Cromwell (14d 6/33) | headgear - | last run 54 days | form - | MARKET 5.9% | 09:00 median 11.00 | Matchbook 18.50
- Nustty (hrs_17393692449) | 3yo G | 154lb | OR - | draw 0 | jockey Keith Donoghue | trainer Gavin Cromwell (14d 6/33) | headgear - | last run 34 days | form - | MARKET 4.8% | 09:00 median 10.00 | Matchbook 40.00
- Nephin Mountain (hrs_53841067) | 3yo G | 154lb | OR - | draw 0 | jockey Sean Flanagan | trainer Michael Mulvany (14d 0/4) | headgear - | last run 27 days | form - | MARKET 2.0% | 09:00 median 29.00 | Matchbook 70.00
- Glen Echo (hrs_64073191) | 3yo G | 154lb | OR - | draw 0 | jockey Ben Harvey | trainer Gavin Cromwell (14d 6/33) | headgear - | last run 38 days | form - | MARKET 1.2% | 09:00 median 51.00 | Matchbook 130.00
- Fay Og (hrs_63104643) | 3yo G | 154lb | OR - | draw 0 | jockey Sam Ewing | trainer W R Crawford (14d 1/2) | headgear - | last run 15 days | form 76 | MARKET 1.0% | 09:00 median 67.00 | Matchbook 130.00
- Arizona Star (hrs_57255170) | 3yo F | 147lb | OR - | draw 0 | jockey Simon Torrens | trainer Michael Mulvany (14d 0/4) | headgear - | last run 17 days | form - | MARKET 0.8% | 09:00 median 101.00 | Matchbook 150.00
- Rose Sienna (hrs_57878002) | 3yo F | 147lb | OR - | draw 0 | jockey Josh Williamson(3) | trainer Patrick Magee (14d 0/4) | headgear - | last run 25 days | form - | MARKET 0.8% | 09:00 median 101.00 | Matchbook 150.00
- Matada (hrs_63104657) | 3yo G | 154lb | OR - | draw 0 | jockey Kieren Buckley | trainer Gavin Cromwell (14d 6/33) | headgear - | last run 176 days | form - | MARKET 0.8% | 09:00 median 81.00 | Matchbook 220.00
- Moon Aura (hrs_63422506) | 3yo F | 147lb | OR - | draw 0 | jockey Shane Markey(7) | trainer C A McBratney (14d 0/0) | headgear p | last run 15 days | form P7 | MARKET 0.7% | 09:00 median 101.00 | Matchbook 170.00
- Courtlough Gula (hrs_56843892) | 3yo F | 147lb | OR - | draw 0 | jockey James Smith(3) | trainer P Cluskey (14d 0/0) | headgear - | last run 34 days | form - | MARKET 0.7% | 09:00 median 101.00 | Matchbook 240.00
- Star Of Tara (hrs_53602241) | 3yo F | 147lb | OR - | draw 0 | jockey Phillip Enright | trainer Jamie Flynn (14d 0/3) | headgear t | last run 12 days | form 9 | MARKET 0.5% | 09:00 median 126.00 | Matchbook 280.00

## 12:10 Navan | race_id rac_32304601667 | Irish Stallion Farms EBF Mares Maiden Hurdle
Hurdle |  | 2m0f0y | going Good To Yielding | Turf | 19 runners | rating band - | age 4yo+
- La Valserine (hrs_60852379) | 5yo M | 161lb | OR - | draw 0 | jockey Paul Townend | trainer W. P. Mullins (14d 5/20) | headgear - | last run 634 days | form 1/ | MARKET 37.0% | 09:00 median 2.10 | Matchbook 2.34
- Moonverrin (hrs_59186120) | 5yo M | 161lb | OR - | draw 0 | jockey Sean Flanagan | trainer Martin Hassett (14d 0/4) | headgear - | last run 249 days | form 2110- | MARKET 17.9% | 09:00 median 4.33 | Matchbook 4.90
- Tintara (hrs_52236681) | 5yo M | 161lb | OR - | draw 0 | jockey Jack Kennedy | trainer Gordon Elliott (14d 10/58) | headgear - | last run 200 days | form /F229- | MARKET 9.4% | 09:00 median 7.50 | Matchbook 10.00
- Royale Walk (hrs_17395474936) | 5yo M | 161lb | OR - | draw 0 | jockey Mike O'Connor | trainer Henry de Bromhead (14d 7/41) | headgear t (1st time) | last run 252 days | form 1- | MARKET 7.7% | 09:00 median 10.00 | Matchbook 11.50
- Theemeraldempress (hrs_63388626) | 4yo F | 161lb | OR - | draw 0 | jockey Keith Donoghue | trainer Gavin Cromwell (14d 6/33) | headgear - | last run 177 days | form 2-1 | MARKET 7.4% | 09:00 median 7.50 | Matchbook 17.00
- Adamas (hrs_17394780298) | 6yo M | 161lb | OR - | draw 0 | jockey Mark Walsh | trainer Henry de Bromhead (14d 7/41) | headgear - | last run 743 days | form 1/ | MARKET 5.5% | 09:00 median 12.00 | Matchbook 19.50
- Holly's Thunder (hrs_63776202) | 5yo M | 161lb | OR - | draw 0 | jockey John Shinnick | trainer Mrs Lorna Fowler (14d 1/3) | headgear - | last run 21 days | form 3-6 | MARKET 2.5% | 09:00 median 23.00 | Matchbook 50.00
- Ellen Imlach (hrs_17392529504) | 4yo F | 161lb | OR - | draw 0 | jockey Danny Gilligan | trainer Gordon Elliott (14d 10/58) | headgear - | last run 40 days | form 6 | MARKET 1.9% | 09:00 median 34.00 | Matchbook 75.00
- Chipsrdown (hrs_52677457) | 4yo F | 161lb | OR - | draw 0 | jockey Philip Donovan | trainer A. Slattery (14d 1/12) | headgear - | last run 26 days | form - | MARKET 1.2% | 09:00 median 67.00 | Matchbook 95.00
- Cala Gracioneta (hrs_56559279) | 4yo F | 161lb | OR - | draw 0 | jockey James Smith(3) | trainer Matthew J Smith (14d 0/6) | headgear - | last run 24 days | form 56 | MARKET 1.1% | 09:00 median 51.00 | Matchbook 130.00
- Chekhov's Gun (hrs_17395473893) | 5yo M | 161lb | OR - | draw 0 | jockey Josh Williamson(3) | trainer Patrick Magee (14d 0/4) | headgear t (1st time) | last run - days | form - | MARKET 1.1% | 09:00 median 67.00 | Matchbook 90.00
- Darby Hill (hrs_60343339) | 5yo M | 161lb | OR - | draw 0 | jockey Sean O'Keeffe | trainer Paul Nolan (14d 6/32) | headgear - | last run 186 days | form 410-6 | MARKET 1.0% | 09:00 median 51.00 | Matchbook 160.00
- Trinity Belle (hrs_17394491387) | 4yo F | 161lb | OR - | draw 0 | jockey Shane Markey(7) | trainer Ross O'Sullivan (14d 1/17) | headgear - | last run 11 days | form 4-8 | MARKET 1.0% | 09:00 median 67.00 | Matchbook 140.00
- Booklight (hrs_41534836) | 4yo F | 161lb | OR - | draw 0 | jockey Sam Ewing | trainer C A McBratney (14d 0/0) | headgear h | last run 16 days | form 74 | MARKET 1.0% | 09:00 median 51.00 | Matchbook 170.00
- Sanctity Of Space (hrs_42912408) | 5yo M | 161lb | OR - | draw 0 | jockey Alex Harvey | trainer John McConnell (14d 1/12) | headgear - | last run 21 days | form 7 | MARKET 1.0% | 09:00 median 51.00 | Matchbook 200.00
- Provoque La Chaos (hrs_17394885641) | 4yo F | 161lb | OR - | draw 0 | jockey Conor Stone-Walsh | trainer J Motherway (14d 0/0) | headgear - | last run 203 days | form 5- | MARKET 0.9% | 09:00 median 67.00 | Matchbook 140.00
- Melody D'Arc (hrs_17391355086) | 4yo F | 161lb | OR - | draw 0 | jockey Dylan Kidd(7) | trainer John McConnell (14d 1/12) | headgear - | last run 11 days | form 80 | MARKET 0.8% | 09:00 median 67.00 | Matchbook 250.00
- Ragstoriches (hrs_17393628826) | 4yo F | 161lb | OR - | draw 0 | jockey Eoghan Finegan(5) | trainer Gerard Keane (14d 0/5) | headgear - | last run 14 days | form 09 | MARKET 0.8% | 09:00 median 67.00 | Matchbook 260.00
- Pink Sheet Pony (hrs_58065567) | 4yo F | 161lb | OR - | draw 0 | jockey Patrick M O'Brien(5) | trainer John G Carr (14d 1/2) | headgear - | last run 387 days | form - | MARKET 0.7% | 09:00 median 81.00 | Matchbook 260.00

## 12:40 Navan | race_id rac_32304603604 | Gaeil Colmcille GAA Kells 'Day At The Races' Handicap Hurdle
Hurdle |  | 2m0f0y | going Good To Yielding | Turf | 28 runners | rating band 0-100 | age 3yo+
- Mr Caulfield (hrs_17389174173) | 5yo G | 173lb | OR 105 | draw 0 | jockey Mr O McGill(5) | trainer Mr Noel C. Kelly (14d 2/6) | headgear - | last run 6 days | form 02B05F | MARKET 9.8% | 09:00 median 5.00 | Matchbook 6.60 | CHECK (skip line 4.75)
    comment: Mr Caulfield fell last time out just six days ago, though he was a fifth two starts back and a second five starts back, so the ability is there. He has run on today's going but is yet to win in his last six, and 173 lb is a hefty burden off 105.
- Crypto Crash (hrs_412652863) | 5yo G | 158lb | OR 90 | draw 0 | jockey Rian Lane(7) | trainer David Kenneth Budds (14d 0/1) | headgear tp | last run 14 days | form F1R561 | MARKET 7.8% | 09:00 median 7.00 | Matchbook 8.00
    comment: Crypto Crash won last time out and has a win five starts back, and he is fresh from a run 14 days ago, but a sixth and a fifth followed by a refusal and a fall show the patchy side. He has run over today's trip and going, though 158 lb is a hefty burden.
- Invincible Oscar (hrs_55484394) | 5yo M | 156lb | OR 88 | draw 0 | jockey Ms E Dunseath(7) | trainer Mr Noel C. Kelly (14d 2/6) | headgear - | last run 37 days | form 80-612 | MARKET 6.3% | 09:00 median 8.50 | Matchbook 10.00
- Asthelightdeclines (hrs_62202168) | 4yo F | 164lb | OR 96 | draw 0 | jockey Keith Donoghue | trainer Gavin Cromwell (14d 6/33) | headgear - | last run 38 days | form B77-61 | MARKET 6.0% | 09:00 median 9.00 | Matchbook 10.50
    comment: She has run over today's trip and going, and 164 lb is a big burden.
- Tropical Twist (hrs_56961583) | 5yo M | 165lb | OR 97 | draw 0 | jockey Jack Kennedy | trainer Gordon Elliott (14d 10/58) | headgear tp | last run 8 days | form 418653 | MARKET 5.5% | 09:00 median 11.00 | Matchbook 10.00
- Sheer Raz (hrs_46233635) | 6yo G | 162lb | OR 94 | draw 0 | jockey Eoin Staples(5) | trainer Gavin Cromwell (14d 6/33) | headgear t | last run 168 days | form 535-37 | MARKET 5.0% | 09:00 median 10.00 | Matchbook 12.00
    comment: Yet to win in his last five, Sheer Raz showed solid consistency with a third two starts back and another third four back, but he was a seventh last time out and returns after 168 days off. He has run over today's trip and going, though 162 lb is a hefty burden.
- Mary's Pride (hrs_24506503) | 9yo G | 165lb | OR 97 | draw 0 | jockey Sarah Kavanagh(7) | trainer Edward Cawley (14d 0/2) | headgear p | last run 57 days | form 0-2706 | MARKET 4.7% | 09:00 median 13.00 | Matchbook 13.50
    comment: The risk is a 57-day absence and a sixth last time out, while carrying 165 lb.
- Leo Messy (hrs_62361250) | 6yo G | 148lb | OR 80 | draw 0 | jockey Harry Sexton(7) | trainer Thomas Gibney (14d 1/7) | headgear t | last run 33 days | form 0-8340 | MARKET 4.3% | 09:00 median 13.00 | Matchbook 16.00
    comment: He has run over today's trip and going, but 148 lb is a stiff ask.
- La Rocca Lass (hrs_41813891) | 6yo M | 140lb | OR 72 | draw 0 | jockey P J O'Hanlon | trainer Ian Patrick Donoghue (14d 0/7) | headgear tp (1st time) | last run 12 days | form 000-05 | MARKET 4.1% | 09:00 median 15.00 | Matchbook 14.50
    comment: La Rocca Lass is winless in her last five, though a fifth last time out and a quick 12-day turnaround hint at some sharpening, and she has run over today's trip and going.
- Beat The Devil (hrs_51650298) | 4yo G | 165lb | OR 97 | draw 0 | jockey Josh Williamson(3) | trainer Patrick Magee (14d 0/4) | headgear t | last run 23 days | form P-974 | MARKET 3.7% | 09:00 median 17.00 | Matchbook 15.50
    comment: Fourth last time out and 23 days fresh, Beat The Devil has found some form after a seventh and a ninth before that, and he has run on today's going before.
- Champagne Dawn (hrs_29226687) | 9yo G | 165lb | OR 97 | draw 0 | jockey Phillip Enright | trainer T J O'Mara (14d 0/0) | headgear - | last run 14 days | form P-7536 | MARKET 3.0% | 09:00 median 21.00 | Matchbook 19.00
    comment: Fit after just 14 days off, Champagne Dawn has run over today's trip and going and was third two starts back, while his 165 lb burden is the one reservation.
- Hob's Angel (hrs_30441138) | 10yo M | 140lb | OR 72 | draw 0 | jockey  | trainer James M Barcoe (14d 0/4) | headgear - | last run 11 days | form 364U96 | MARKET 3.0% | 09:00 median 19.00 | Matchbook 23.00
    comment: Winless in her last six, Hob's Angel was a sixth last time out after a ninth and an unseated, which makes her hard to fancy off 140 lb. She has run over today's trip and going, and a third six starts back is the best of her recent form.
- Annarubyrose (hrs_52677121) | 5yo M | 155lb | OR 87 | draw 0 | jockey Sam Ewing | trainer Ian Patrick Donoghue (14d 0/7) | headgear - | last run 76 days | form -24570 | MARKET 3.0% | 09:00 median 21.00 | Matchbook 21.00
    comment: Annarubyrose has slipped down the order since a second five starts back, finishing unplaced last time and winless in her last five, and she returns after 76 days off.
- Everyday Life (hrs_51341584) | 5yo M | 167lb | OR 99 | draw 0 | jockey James Smith(3) | trainer Ian Patrick Donoghue (14d 0/7) | headgear h | last run 41 days | form 2-96U5 | MARKET 2.8% | 09:00 median 21.00 | Matchbook 24.00
    comment: Everyday Life was fifth last time out after 41 days off, and she has run over today's trip and going before, but she's winless in her last five, with an unseated two starts back and a second five runs ago the only real highlight. Carrying 167 lb off 99, her profile looks mid-pack.
- Clonbury Court (hrs_61277328) | 4yo G | 151lb | OR 83 | draw 0 | jockey Jordan Gainford | trainer J P Dempsey (14d 0/2) | headgear - | last run 23 days | form P00-07 | MARKET 2.8% | 09:00 median 21.00 | Matchbook 25.00
    comment: He does return after 23 days off, but 151 lb on an official mark of 83 is a lot to ask.
- Llem's (hrs_58596685) | 5yo G | 167lb | OR 99 | draw 0 | jockey  | trainer Gordon Elliott (14d 10/58) | headgear - | last run 21 days | form 8F-49 | MARKET 2.8% | 09:00 median 21.00 | Matchbook 24.00
    comment: Llem's has run over today's trip and is fresh enough after 21 days, but he's yet to win in his last four starts, with a ninth last time out and a fall three starts back.
- Orinoco Walk (hrs_53359691) | 8yo M | 150lb | OR 82 | draw 0 | jockey Patrick M O'Brien(5) | trainer Riceal Dunne (14d 0/2) | headgear - | last run 172 days | form 590-0P | MARKET 2.7% | 09:00 median 19.00 | Matchbook 30.00
    comment: Orinoco Walk is winless in her last five, pulled up last time and unplaced in the two runs before, while a 172-day absence raises fitness questions.
- I Can Find Em (hrs_59186372) | 5yo G | 164lb | OR 96 | draw 0 | jockey Mr D McGill(5) | trainer Gary McGill (14d 0/1) | headgear - | last run 50 days | form 22-096 | MARKET 2.7% | 09:00 median 23.00 | Matchbook 23.00
    comment: I Can Find Em showed promise with seconds four and five starts back, but he's tailed off since, finishing a ninth then a sixth last time out, and he returns after 50 days off. He has run on today's going and is yet to win in recent form, while 164 lb is a stiff burden.
- Mirfaq (hrs_63357308) | 4yo G | 157lb | OR 89 | draw 0 | jockey Conor Stone-Walsh | trainer Gavin Cromwell (14d 6/33) | headgear t (1st time) | last run 57 days | form 0-P60 | MARKET 2.4% | 09:00 median 26.00 | Matchbook 26.00
    comment: Mirfaq is winless in his last four, with an unplaced effort last time, a sixth two starts back and a pulled up before that, and he returns after 57 days off.
- Noble Rocco (hrs_63171339) | 4yo F | 154lb | OR 86 | draw 0 | jockey Danny Gilligan | trainer Gordon Elliott (14d 10/58) | headgear - | last run 57 days | form 79739 | MARKET 2.4% | 09:00 median 26.00 | Matchbook 26.00
    comment: Noble Rocco is winless in her last five, with a ninth last time out after 57 days off, and only a third two starts back stands out in that run.
- Tommy Go Maith (hrs_52862474) | 5yo G | 140lb | OR 72 | draw 0 | jockey Simon Torrens | trainer Thomas Patrick McGettigan (14d 0/0) | headgear b | last run 23 days | form PPU868 | MARKET 2.2% | 09:00 median 29.00 | Matchbook 27.00
    comment: Tommy Go Maith is hard to fancy, winless in his last six with an eighth last time out, a sixth two starts back and an eighth three starts back, plus two pulled up and an unseated before that. He does return after 23 days, but 140 lb off a mark of 72 looks tough.
- Nothing Da Now (hrs_47620902) | 6yo M | 148lb | OR 80 | draw 0 | jockey Sean O'Keeffe | trainer Maike Magnussen (14d 0/2) | headgear - | last run 79 days | form 0P7-7P | MARKET 2.1% | 09:00 median 34.00 | Matchbook 26.00
    comment: Nothing Da Now is winless in her last five, pulled up last time out and again four starts back, with a seventh two starts back the best of it, and she returns after 79 days off. Carrying 148 lb, her only plus is that she has run on today's going before.
- Northern Ruler (hrs_41723430) | 5yo G | 159lb | OR 91 | draw 0 | jockey Shane O'Callaghan(3) | trainer M. D. O'Callaghan (14d 1/5) | headgear tp | last run 35 days | form 006-0P | MARKET 2.0% | 09:00 median 34.00 | Matchbook 30.00
    comment: Northern Ruler was pulled up last time out and is winless in his last five, with a sixth three starts back his best recent finish, though he has run over today's trip and returns after 35 days off.
- Leitzel (hrs_31368701) | 6yo M | 154lb | OR 86 | draw 0 | jockey Alan O'Sullivan(5) | trainer Sean McParlan (14d 0/1) | headgear - | last run 98 days | form 000-05 | MARKET 2.0% | 09:00 median 34.00 | Matchbook 29.00
    comment: Leitzel signed off with a fifth last time out but is winless in her last five and returns after 98 days off, which tempers enthusiasm.
- Dunmore (hrs_64555071) | 3yo G | 142lb | OR 90 | draw 0 | jockey  | trainer Anthony Mullins (14d 0/3) | headgear - | last run 20 days | form 767 | MARKET 2.0% | 09:00 median 41.00 | Matchbook 29.00
    comment: Dunmore is winless in his last three, finishing seventh, sixth and seventh, and he looks hard to fancy off an official mark of 90 while carrying 142 lb. On the plus side, he has run over today's trip and going before, and he is fresh enough after 20 days off.
- Zaryagle (hrs_52677590) | 5yo G | 149lb | OR 81 | draw 0 | jockey Dylan Robinson | trainer P. J. Rothwell (14d 0/25) | headgear p | last run 36 days | form 96P-08 | MARKET 1.7% | 09:00 median 41.00 | Matchbook 42.00
    comment: Winless in his last five, with an eighth last time out and a pulled up three starts back, Zaryagle has little recent form to lean on, and a cold yard (0/25 in the last 14 days) doesn't help.
- Magnificent Era (hrs_57102794) | 6yo G | 147lb | OR 79 | draw 0 | jockey Philip Donovan | trainer John F Gleeson (14d 0/1) | headgear - | last run 154 days | form 095-00 | MARKET 1.6% | 09:00 median 51.00 | Matchbook 42.00
    comment: Winless in his last five and unplaced last time out, Magnificent Era has little recent form to lean on, with a fifth three starts back his best effort and 154 days off the track a concern.
- Gatehouse Boy (hrs_49389228) | 6yo G | 164lb | OR 96 | draw 0 | jockey Tiernan Power Roche | trainer P. J. Rothwell (14d 0/25) | headgear p | last run 33 days | form 10P-50 | MARKET 1.5% | 09:00 median 51.00 | Matchbook 42.00
    comment: The big concern is a stable at 0/25 in the last 14 days, after he was unplaced last time out.

## 1:15 Navan | race_id rac_32304605541 | John Lynch Carpets & Flooring Monksfield Novice Hurdle (Grade 3)
Hurdle | Class 1 | 2m4f0y | going Good To Yielding | Turf | 7 runners | rating band - | age 4yo+
- With Nolimit (hrs_51341416) | 5yo G | 154lb | OR - | draw 0 | jockey Jack Kennedy | trainer Gordon Elliott (14d 10/58) | headgear - | last run 16 days | form 1291-1 | MARKET 38.1% | 09:00 median 2.38 | Matchbook 2.50
- Reaching High (hrs_36793680) | 5yo G | 154lb | OR - | draw 0 | jockey Paul Townend | trainer W. P. Mullins (14d 5/20) | headgear t | last run 51 days | form 21 | MARKET 21.6% | 09:00 median 4.00 | Matchbook 4.60
- Thinkitdontjinxit (hrs_58963009) | 5yo G | 154lb | OR - | draw 0 | jockey Danny Gilligan | trainer Gordon Elliott (14d 10/58) | headgear - | last run 1 days | form 228-11 | MARKET 12.5% | 09:00 median 7.00 | Matchbook 8.00
- Pat O's Rock (hrs_17390411171) | 5yo M | 147lb | OR - | draw 0 | jockey Mike O'Connor | trainer Henry de Bromhead (14d 7/41) | headgear - | last run 33 days | form 411 | MARKET 9.2% | 09:00 median 9.50 | Matchbook 11.00
- Gillane (hrs_41052725) | 6yo G | 154lb | OR - | draw 0 | jockey Keith Donoghue | trainer Gavin Cromwell (14d 6/33) | headgear t (1st time) | last run 44 days | form 2321-1 | MARKET 7.7% | 09:00 median 11.00 | Matchbook 13.50
- Barnahash Mason (hrs_58165247) | 7yo G | 154lb | OR - | draw 0 | jockey Mark Walsh | trainer Jonathan Sweeney (14d 0/0) | headgear - | last run 269 days | form 511- | MARKET 6.9% | 09:00 median 12.00 | Matchbook 15.00
- Tountinna (hrs_51766365) | 5yo M | 150lb | OR 123 | draw 0 | jockey Sean O'Keeffe | trainer Maike Magnussen (14d 0/2) | headgear h | last run 29 days | form 841-01 | MARKET 4.1% | 09:00 median 21.00 | Matchbook 26.00

## 1:50 Navan | race_id rac_32304607478 | BAR 1 Betting 'Bet 10 Get 50' Tara Handicap Hurdle
Hurdle |  | 2m5f0y | going Good To Yielding | Turf | 16 runners | rating band - | age 4yo+
- Mart Lane (hrs_58565430) | 5yo G | 152lb | OR 116 | draw 0 | jockey Mr Finian Maguire | trainer Barry Connell (14d 0/5) | headgear t | last run 52 days | form 24-821 | MARKET 20.2% | 09:00 median 3.75 | Matchbook 4.30 | CHECK (skip line 3.56)
    comment: Mart Lane won last time out and was second two starts back, but he returns after 52 days off and carries 152 lb.
- Royal Gladiator (hrs_52056011) | 5yo G | 159lb | OR 123 | draw 0 | jockey Keith Donoghue | trainer Ian Patrick Donoghue (14d 0/7) | headgear - | last run 224 days | form /2410- | MARKET 10.8% | 09:00 median 7.50 | Matchbook 7.80
    comment: Royal Gladiator won two starts back and was second four runs ago, but he was unplaced last time out and returns after 224 days off, which raises fitness questions. He has run over today's trip and going, though 159 lb is a hefty burden.
- Paddy's Milestone (hrs_35243726) | 7yo G | 150lb | OR 114 | draw 0 | jockey Sam Ewing | trainer S. R. B. Crawford (14d 0/6) | headgear - | last run 344 days | form 01/15- | MARKET 8.0% | 09:00 median 8.00 | Matchbook 12.50
    comment: Won two starts back and three starts back, then finished fifth last time, but this gelding returns after 344 days off and carries 150 lb, a hefty burden.
- Better Times (hrs_47837433) | 6yo G | 142lb | OR 106 | draw 0 | jockey Ms Aine Connolly(7) | trainer S G Carey (14d 0/4) | headgear - | last run 14 days | form -47893 | MARKET 6.6% | 09:00 median 12.00 | Matchbook 13.00
    comment: He has run over today's trip and going, and a quick 14-day turnaround keeps him fit, though 142 lb is a lot to carry.
- Sa Fureur (hrs_27428513) | 9yo G | 168lb | OR 132 | draw 0 | jockey Jack Kennedy | trainer Gordon Elliott (14d 10/58) | headgear - | last run 188 days | form 4204-F | MARKET 6.5% | 09:00 median 11.00 | Matchbook 14.50
- You Make Me Smile (hrs_31865155) | 8yo M | 140lb | OR 103 | draw 0 | jockey Sean O'Keeffe | trainer P A Fahy (14d 0/10) | headgear - | last run 23 days | form -32371 | MARKET 6.1% | 09:00 median 11.00 | Matchbook 16.00
    comment: She has run over today's trip and going, yet 140 lb off 103 is a big ask.
- Cool Native (hrs_47621147) | 6yo M | 145lb | OR 109 | draw 0 | jockey Danny Gilligan | trainer Gordon Elliott (14d 10/58) | headgear tp (1st time) | last run 124 days | form /3U4-3 | MARKET 6.1% | 09:00 median 12.00 | Matchbook 15.00
    comment: She has run on today's going before, which is a small positive.
- Champagne Venture (hrs_39169312) | 7yo M | 150lb | OR 114 | draw 0 | jockey Josh Williamson(3) | trainer D Broad (14d 0/1) | headgear p | last run 239 days | form /5331- | MARKET 5.7% | 09:00 median 11.00 | Matchbook 18.50
    comment: Champagne Venture won last time out and was third on her two starts before that, but she returns after 239 days off and carries 150 lb, which is a lot to ask.
- Matt Connor (hrs_31565478) | 6yo G | 159lb | OR 123 | draw 0 | jockey Eoin Staples(5) | trainer J P Dempsey (14d 0/2) | headgear p | last run 34 days | form 410-59 | MARKET 5.2% | 09:00 median 13.00 | Matchbook 20.00
    comment: The main risk is a ninth last time out, and he carries 159 lb.
- Beyond Your Dreams (hrs_38173821) | 5yo M | 149lb | OR 113 | draw 0 | jockey Aidan Kelly | trainer Padraig Roche (14d 0/6) | headgear tp | last run 42 days | form 0/98-6 | MARKET 4.1% | 09:00 median 19.00 | Matchbook 21.00
- Burru (hrs_34253317) | 8yo G | 145lb | OR 109 | draw 0 | jockey Michael Kenneally(3) | trainer Bernard Martin Crowley (14d 0/2) | headgear - | last run 87 days | form P-1046 | MARKET 3.9% | 09:00 median 19.00 | Matchbook 23.00
    comment: Burru has a win four starts back and has run over today's trip and going, but he's a sixth last time out and a fourth two starts back, and an 87-day break raises fitness questions.
- I Love My Baie (hrs_30540769) | 8yo G | 159lb | OR 123 | draw 0 | jockey J. J. Slevin | trainer S. R. B. Crawford (14d 0/6) | headgear p | last run 344 days | form 7/U07- | MARKET 3.8% | 09:00 median 21.00 | Matchbook 23.00
    comment: The big risk is fitness, as he returns after 344 days off following a seventh last time out.
- It's Bobsled Time (hrs_57654513) | 4yo G | 141lb | OR 106 | draw 0 | jockey Kevin Healy(7) | trainer Declan Queally (14d 0/5) | headgear - | last run 52 days | form 1F0-40 | MARKET 3.5% | 09:00 median 23.00 | Matchbook 28.00
    comment: It's Bobsled Time is hard to fancy, unplaced last time out and 52 days off, with just one win in his last five starts, back then, and a fall since.
- Sequoiaspirit (hrs_22180501) | 9yo G | 156lb | OR 120 | draw 0 | jockey Alan O'Sullivan(5) | trainer Ray Hackett (14d 0/3) | headgear t | last run 50 days | form 8P-100 | MARKET 3.3% | 09:00 median 23.00 | Matchbook 28.00
    comment: Sequoiaspirit won three starts back but has been unplaced in his last two outings, and he returns after 50 days off carrying 156 lb.
- Must Go Now (hrs_32401943) | 9yo G | 145lb | OR 109 | draw 0 | jockey Jordan Gainford | trainer Edward Cawley (14d 0/2) | headgear p | last run 160 days | form 309-08 | MARKET 3.2% | 09:00 median 21.00 | Matchbook 34.00
    comment: Must Go Now has been winless in his last five, with an eighth last time out and a third five starts back the best of it, and he returns after 160 days off.
- Park Of Kings (hrs_30016000) | 8yo G | 155lb | OR 119 | draw 0 | jockey Mark Walsh | trainer Paul Nolan (14d 6/32) | headgear tp | last run 7 days | form U0-400 | MARKET 2.9% | 09:00 median 19.00 | Matchbook 44.00
    comment: The risk is a winless recent run, with a fourth three starts back his best finish, and 155 lb is a stiff burden.

## 2:25 Navan | race_id rac_32304609415 | Race And Stay Irish EBF Beginners Steeplechase
Chase |  | 2m4f150y | going Yielding | Turf | 9 runners | rating band - | age 4yo+
- Fruit De Mer (hrs_40646949) | 6yo G | 166lb | OR - | draw 0 | jockey Sean Flanagan | trainer Henry de Bromhead (14d 7/41) | headgear - | last run 200 days | form /1324- | MARKET 32.2% | 09:00 median 2.63 | Matchbook 2.94
    comment: Fruit De Mer has been consistent, finishing fourth last time out, second two starts back, third three starts back, and a winner four starts back, and he has run over today's trip and going before.
- Classical Creek (hrs_41053054) | 6yo G | 166lb | OR - | draw 0 | jockey Jack Kennedy | trainer Gordon Elliott (14d 10/58) | headgear - | last run 310 days | form 13/17- | MARKET 20.2% | 09:00 median 4.00 | Matchbook 4.80
    comment: Classical Creek won two starts back and four starts back, with a third three starts back, but he was only seventh last time out and returns after 310 days off.
- Kopeck De Mee (hrs_38684506) | 6yo G | 166lb | OR - | draw 0 | jockey Mark Walsh | trainer W. P. Mullins (14d 5/20) | headgear - | last run 197 days | form 2/F02- | MARKET 18.6% | 09:00 median 4.50 | Matchbook 5.10
    comment: Kopeck De Mee finished second last time out and was also second four starts back, though he is without a win in his last four, and he has run over today's trip and going before.
- Espresso Milan (hrs_47684980) | 6yo G | 166lb | OR - | draw 0 | jockey Brian Hayes | trainer W. P. Mullins (14d 5/20) | headgear - | last run 200 days | form /110P- | MARKET 10.3% | 09:00 median 8.00 | Matchbook 9.60
    comment: Espresso Milan won twice in his last four, a first three starts back and another the run before, but he was pulled up last time and unplaced the start prior, and he returns after 200 days off.
- Forty Coats (hrs_39431532) | 7yo G | 166lb | OR - | draw 0 | jockey Keith Donoghue | trainer Henry de Bromhead (14d 7/41) | headgear - | last run 249 days | form 4/737- | MARKET 7.7% | 09:00 median 12.00 | Matchbook 12.50
    comment: The main risk is a 249-day absence, with a seventh last time out and 166 lb to carry.
- Kazansky (hrs_39996509) | 6yo G | 166lb | OR - | draw 0 | jockey Danny Gilligan | trainer Gordon Elliott (14d 10/58) | headgear - | last run 200 days | form 112P7- | MARKET 7.7% | 09:00 median 11.00 | Matchbook 12.50
    comment: Kazansky won two starts in a row four and five runs back, then finished second three starts back, so he has real ability on his day.
- Hens Tooth (hrs_34166720) | 8yo G | 166lb | OR - | draw 0 | jockey Sean O'Keeffe | trainer W. P. Mullins (14d 5/20) | headgear - | last run 225 days | form /061P- | MARKET 2.3% | 09:00 median 26.00 | Matchbook 60.00
    comment: Hens Tooth is hard to fancy after being pulled up last time out and returning from a 225-day absence, while a sixth three starts back and an unplaced run before that add little.
- Lengaruka (hrs_64779813) | 5yo G | 166lb | OR - | draw 0 | jockey Phillip Enright | trainer Derek O'Connor (14d 0/0) | headgear - | last run 21 days | form 05356 | MARKET 0.6% | 09:00 median 91.00 | Matchbook 370.00
    comment: Lengaruka is winless in his last five, with a sixth last time out and a fifth two starts back, and he looks up against it at 166 lb.
- Big Tom (hrs_38433220) | 7yo G | 166lb | OR - | draw 0 | jockey Conor Smithers(7) | trainer Mrs Mary Whelehan (14d 0/0) | headgear - | last run 36 days | form /815-P | MARKET 0.4% | 09:00 median 201.00 | Matchbook 380.00
    comment: Big Tom is lightly raced and still unexposed, with a win three starts back sitting alongside a fifth two runs ago, though he was pulled up last time out. Back after 36 days off and carrying 166 lb, he could have more to offer.

## 3:00 Navan | race_id rac_32303981827 | BAR 1 Betting Troytown Handicap Steeplechase (Grade 3)
Chase | Class 1 | 3m0f0y | going Yielding | Turf | 18 runners | rating band - | age 4yo+
- The Enabler (hrs_34961591) | 7yo G | 146lb | OR 136 | draw 0 | jockey Danny Gilligan | trainer Gordon Elliott (14d 10/58) | headgear t | last run 223 days | form 14363- | MARKET 12.9% | 09:00 median 6.00 | Matchbook 6.80 | CHECK (skip line 5.70)
    comment: Third last time out and a third three starts back show The Enabler is capable of making the frame, and he has run over today's trip and going, but a 223-day absence and 146 lb on his back leave question marks.
- The Wallpark (hrs_32061764) | 8yo G | 152lb | OR 142 | draw 0 | jockey Jack Kennedy | trainer Gordon Elliott (14d 10/58) | headgear tp (1st time) | last run 258 days | form 07620- | MARKET 11.8% | 09:00 median 6.00 | Matchbook 8.00
    comment: The Wallpark is winless in his last five, though a second two starts back shows he can go close, and he has run over today's trip and going before.
- Win Some Lose Some (hrs_34775104) | 7yo G | 145lb | OR 135 | draw 0 | jockey Mark Walsh | trainer Padraig Roche (14d 0/6) | headgear - | last run 287 days | form 38762- | MARKET 10.4% | 09:00 median 7.00 | Matchbook 9.00
    comment: Yet to win in his last five, he bounced back with a second last time out, but that came 287 days ago and the 6th, 7th and 8th before it show a patchy profile.
- He's Gorgeous (hrs_38649632) | 7yo G | 140lb | OR 129 | draw 0 | jockey Sean O'Keeffe | trainer P A Fahy (14d 0/10) | headgear - | last run 28 days | form 55-P33 | MARKET 8.4% | 09:00 median 9.00 | Matchbook 11.00
    comment: He has run on today's going before and returns after 28 days carrying 140 lb.
- Firefox (hrs_29523102) | 8yo G | 166lb | OR 156 | draw 0 | jockey Kevin Healy(7) | trainer Gordon Elliott (14d 10/58) | headgear t | last run 218 days | form 12460- | MARKET 8.4% | 09:00 median 8.50 | Matchbook 11.50
    comment: Firefox has run over today's trip and on this going, and he won five starts back before a second four runs ago, though he's been unplaced last time out and absent 218 days.
- Sportinthepark (hrs_34859888) | 7yo G | 140lb | OR 130 | draw 0 | jockey Sam Ewing | trainer Noel Meade (14d 4/14) | headgear - | last run 20 days | form /10P-5 | MARKET 7.4% | 09:00 median 9.00 | Matchbook 13.50
    comment: Carrying 140 lb off 130 after 20 days off, he has plenty to prove.
- Better Days Ahead (hrs_28903721) | 8yo G | 163lb | OR 153 | draw 0 | jockey Mr L Murphy(7) | trainer Gordon Elliott (14d 10/58) | headgear tp (1st time) | last run 223 days | form 6/226- | MARKET 6.0% | 09:00 median 11.00 | Matchbook 17.50
    comment: Better Days Ahead is yet to win in his last four, but back-to-back seconds two and three starts back show he can be competitive, and he has run over today's trip and going.
- Kinturk Kalanisi (hrs_35430773) | 8yo G | 143lb | OR 133 | draw 0 | jockey Harry Sexton(7) | trainer Thomas Gibney (14d 1/7) | headgear p | last run 197 days | form /307P- | MARKET 5.2% | 09:00 median 13.00 | Matchbook 19.50
    comment: Kinturk Kalanisi has been pulled up last time out after a seventh two starts back, and he returns from 197 days off, though a third four starts back shows he has ability. He has run over today's trip and going, but he is winless in his last four and carries 143 lb off 133.
- Uhavemeinstitches (hrs_40899509) | 6yo M | 141lb | OR 131 | draw 0 | jockey Simon Torrens | trainer J Motherway (14d 0/0) | headgear - | last run 197 days | form 33U1P- | MARKET 4.8% | 09:00 median 15.00 | Matchbook 20.00
    comment: Pulled up last time out and absent for 197 days, Uhavemeinstitches is hard to fancy, though she did win two starts back and has run over today's trip and going.
- Kish Bank (hrs_38089359) | 7yo G | 140lb | OR 128 | draw 0 | jockey Josh Williamson(3) | trainer Gordon Elliott (14d 10/58) | headgear p | last run 198 days | form 31P20- | MARKET 4.6% | 09:00 median 17.00 | Matchbook 19.50
    comment: Kish Bank is hard to fancy after 198 days off and an unplaced effort last time out, with a pulled up three starts back adding to the doubts. A second two starts back and a win four starts back show ability, and he has run over today's trip and going.
- Search For Glory (hrs_29829198) | 9yo G | 156lb | OR 146 | draw 0 | jockey James Smith(3) | trainer Gordon Elliott (14d 10/58) | headgear tb | last run 223 days | form 22PUP- | MARKET 3.3% | 09:00 median 21.00 | Matchbook 32.00
    comment: Search For Glory has been without a win in his last five, with seconds four and five starts back, though he has since been pulled up, unseated and pulled up again.
- Patter Merchant (hrs_38002468) | 7yo G | 140lb | OR 128 | draw 0 | jockey Patrick M O'Brien(5) | trainer Gordon Elliott (14d 10/58) | headgear p | last run 223 days | form 530P7- | MARKET 3.2% | 09:00 median 23.00 | Matchbook 24.00
    comment: Patter Merchant has run over today's trip and going before, but he's winless in his last five, a seventh last time out following a pulled-up, and returns after 223 days off. A third four starts back is his best recent effort, and 140 lb looks a stern ask.
- Will Do (hrs_29622166) | 9yo G | 140lb | OR 126 | draw 0 | jockey Ethan O'Sullivan(7) | trainer Gordon Elliott (14d 10/58) | headgear b | last run 21 days | form 0PP-32 | MARKET 3.0% | 09:00 median 21.00 | Matchbook 36.00
    comment: Will Do arrives in better heart, second last time out and third two starts back after a pair of pulled-up efforts, and he has run over today's trip and going.
- Da Capo Glory (hrs_24206042) | 9yo G | 140lb | OR 125 | draw 0 | jockey Phillip Enright | trainer Padraig Butler (14d 0/0) | headgear b (1st time) | last run 21 days | form U-2255 | MARKET 2.6% | 09:00 median 23.00 | Matchbook 42.00
    comment: Fifth in each of his last two runs, with a second three and four starts back, Da Capo Glory has run creditably of late without getting his head in front in his last five, and he has run over today's trip and going. A 21-day break is fine, but 140 lb is a big weight to carry for a gelding yet to win in his last five.
- Croke Park (hrs_29326801) | 8yo G | 153lb | OR 143 | draw 0 | jockey Jordan Gainford | trainer Gordon Elliott (14d 10/58) | headgear p | last run 15 days | form 300-25 | MARKET 2.6% | 09:00 median 29.00 | Matchbook 40.00
    comment: Croke Park arrives fit after 15 days off, with a second two starts back and a third five runs ago, and he has run over today's trip and going before. He is yet to win in his last five, though, and 153 lb is the main risk.
- Vaureal (hrs_38203011) | 7yo G | 140lb | OR 122 | draw 0 | jockey Caragh Monaghan(7) | trainer Ian Patrick Donoghue (14d 0/7) | headgear - | last run 45 days | form 425-10 | MARKET 2.1% | 09:00 median 34.00 | Matchbook 48.00
    comment: Vaureal was unplaced last time out after a win two starts back, and a 45-day break does little to help his case, while 140 lb is a hefty burden.
- Intense Raffles (hrs_26861548) | 8yo G | 152lb | OR 142 | draw 0 | jockey J. J. Slevin | trainer Thomas Gibney (14d 1/7) | headgear - | last run 197 days | form 8PP65- | MARKET 1.8% | 09:00 median 41.00 | Matchbook 60.00
    comment: The main risk is fitness, as he is yet to win in his last five and returns after 197 days off.
- Perceval Legallois (hrs_23490313) | 9yo G | 151lb | OR 141 | draw 0 | jockey Conor Stone-Walsh | trainer Gavin Cromwell (14d 6/33) | headgear t | last run 53 days | form P-82PP | MARKET 1.6% | 09:00 median 41.00 | Matchbook 65.00
    comment: Perceval Legallois has been pulled up in two of his last three outings, though a second three starts back shows he has ability, and he has run over today's trip and going.

## 3:35 Navan | race_id rac_32304611352 | Coolmore N.H. Sires Hurricane Lane Irish EBF Mares Flat Race (Listed)
NH Flat | Class 1 | 2m0f0y | going Good To Yielding | Turf | 10 runners | rating band - | age 4-6yo
- Sarahs Lawn (hrs_17389686286) | 4yo F | 165lb | OR - | draw 0 | jockey Mr D L Queally | trainer Declan Queally (14d 0/5) | headgear t | last run 44 days | form 41-11 | MARKET 46.3% | 09:00 median 1.80 | Matchbook 1.95
    comment: The main risk is the 165 lb she carries after a 44-day break.
- All Noise (hrs_17393739384) | 4yo F | 161lb | OR - | draw 0 | jockey Mr H C Swan | trainer Mrs J. Harrington (14d 2/9) | headgear - | last run 29 days | form 1-1 | MARKET 21.8% | 09:00 median 3.75 | Matchbook 4.30
- Brosna Shine (hrs_51434418) | 5yo M | 161lb | OR - | draw 0 | jockey Mr P A King | trainer S G Carey (14d 0/4) | headgear - | last run 287 days | form 3/15- | MARKET 16.0% | 09:00 median 5.00 | Matchbook 6.00
    comment: Brosna Shine won two starts back and was third three starts back, so she arrives with solid recent form, and she has run over today's trip.
- Shuil Solas (hrs_66463446) | 5yo M | 161lb | OR - | draw 0 | jockey Mr J L Gleeson | trainer John E & Thomas Kiely (14d 0/2) | headgear - | last run 33 days | form 5922 | MARKET 4.6% | 09:00 median 17.00 | Matchbook 22.00
    comment: Shuil Solas arrives in good heart after finishing second last time out and a second two starts back, and she has run over today's trip and going before, but she is yet to win in her last four and carries 161 lb after 33 days off.
- Bluebell Breeze (hrs_65225405) | 4yo F | 161lb | OR - | draw 0 | jockey Miss Charlotte Butler | trainer A D Leahy (14d 0/4) | headgear - | last run 21 days | form 074791 | MARKET 3.5% | 09:00 median 15.00 | Matchbook 55.00
    comment: Bluebell Breeze won last time out, but that came after a ninth, a seventh and another seventh in her prior runs, so consistency is a worry, and 161 lb is a hefty burden.
- Born Believing (hrs_59429475) | 5yo M | 161lb | OR - | draw 0 | jockey Mr D O'Sullivan | trainer Ms Claire O'Connell (14d 1/5) | headgear t | last run 41 days | form 115-53 | MARKET 2.7% | 09:00 median 26.00 | Matchbook 50.00
    comment: Born Believing bagged back-to-back wins four and five starts back, but she has since tailed off to a fifth, a fifth, then a third last time out. She has run over today's trip and going, though 161 lb and a 41-day break temper enthusiasm.
- Eillis (hrs_64325723) | 4yo F | 161lb | OR - | draw 0 | jockey Mr N. McParlan | trainer S. R. B. Crawford (14d 0/6) | headgear - | last run 195 days | form 4 | MARKET 1.5% | 09:00 median 51.00 | Matchbook 85.00
    comment: Eillis was fourth last time out but has been off for 195 days, and she is yet to win in her recent form, so she is hard to fancy at 161 lb.
- The Lodge Lane (hrs_17390039863) | 4yo F | 161lb | OR - | draw 0 | jockey Mr J Dunne | trainer Peter Lawlor (14d 0/0) | headgear - | last run 83 days | form 30 | MARKET 1.4% | 09:00 median 41.00 | Matchbook 120.00
    comment: The risk is an 83-day absence after an unplaced latest effort.
- Inner Bloom (hrs_17395477022) | 4yo F | 161lb | OR - | draw 0 | jockey Mr Finian Maguire | trainer M P Fogarty (14d 0/0) | headgear - | last run 203 days | form 6P- | MARKET 1.2% | 09:00 median 85.00 | Matchbook 85.00
    comment: Lightly raced and unexposed, Inner Bloom was pulled up last time out and a sixth two starts back, so she's yet to win in her last two starts. Returning after 203 days off and carrying 161 lb, she may have more to offer.
- Silver Song (hrs_17394413162) | 4yo F | 161lb | OR - | draw 0 | jockey Mr B M Coonan | trainer Derek O'Connor (14d 0/0) | headgear - | last run 16 days | form 7 | MARKET 1.1% | 09:00 median 51.00 | Matchbook 180.00
    comment: Silver Song was only seventh last time out and is yet to win in her recent form, which makes her hard to fancy, though she's fresh from a 16-day break and has run over today's trip and going before.
