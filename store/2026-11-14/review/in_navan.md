# Card review packet: Navan, 2026-11-14

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


## 11:52 Navan | race_id rac_32304584234 | Kilberry Pub & Kitchen Maiden Hurdle
Hurdle |  | 2m4f50y | going Good To Yielding | Turf | 22 runners | rating band - | age 4yo+
- Charismatic Kid (hrs_59399718) | 5yo G | 166lb | OR - | draw 0 | jockey Jack Kennedy | trainer Gordon Elliott (14d 6/41) | headgear t (1st time) | last run 222 days | form 131- | MARKET 50.6% | 09:00 median 1.53 | Matchbook 1.68
- The Irish Avatar (hrs_51558178) | 5yo G | 166lb | OR - | draw 0 | jockey Paul Townend | trainer W. P. Mullins (14d 8/28) | headgear - | last run 199 days | form 2/105- | MARKET 20.3% | 09:00 median 3.25 | Matchbook 4.90
- Outofafrika (hrs_50874943) | 5yo G | 166lb | OR - | draw 0 | jockey Keith Donoghue | trainer Gavin Cromwell (14d 6/38) | headgear - | last run 198 days | form 1/514- | MARKET 10.1% | 09:00 median 6.50 | Matchbook 10.00
- Luxor Love (hrs_17394958651) | 5yo G | 166lb | OR - | draw 0 | jockey Mike O'Connor | trainer Henry de Bromhead (14d 6/37) | headgear - | last run 286 days | form P/1- | MARKET 4.2% | 09:00 median 13.00 | Matchbook 32.00
- Apples Delight (hrs_17395461377) | 4yo G | 165lb | OR - | draw 0 | jockey Sam Ewing | trainer Gordon Elliott (14d 6/41) | headgear - | last run - days | form - | MARKET 2.5% | 09:00 median 26.00 | Matchbook 46.00
- Bonnie Gold (hrs_52055325) | 5yo G | 166lb | OR - | draw 0 | jockey Danny Gilligan | trainer Gordon Elliott (14d 6/41) | headgear - | last run 190 days | form P/34-1 | MARKET 2.3% | 09:00 median 26.00 | Matchbook 50.00
- Confidence Within (hrs_17389779113) | 5yo G | 166lb | OR - | draw 0 | jockey Tiernan Power Roche | trainer P. J. Rothwell (14d 0/23) | headgear - | last run 50 days | form 3-13 | MARKET 2.1% | 09:00 median 29.00 | Matchbook 60.00
- Tidy Town (hrs_17395466592) | 4yo G | 165lb | OR - | draw 0 | jockey Mark Walsh | trainer Noel Meade (14d 3/12) | headgear - | last run - days | form - | MARKET 1.6% | 09:00 median 34.00 | Matchbook 95.00
- Spanish Agent (hrs_64555029) | 4yo G | 165lb | OR - | draw 0 | jockey James Smith(3) | trainer Gordon Elliott (14d 6/41) | headgear - | last run - days | form - | MARKET 1.1% | 09:00 median 51.00 | Matchbook 180.00
- Churchroad Harry (hrs_17393181379) | 5yo G | 166lb | OR - | draw 0 | jockey E Walsh | trainer Cian Collins (14d 1/7) | headgear - | last run 43 days | form P2-0 | MARKET 0.8% | 09:00 median 81.00 | Matchbook 160.00
- The Stags (hrs_17394710417) | 5yo G | 166lb | OR - | draw 0 | jockey Kevin Healy(7) | trainer Gordon Elliott (14d 6/41) | headgear - | last run 15 days | form FPP-46 | MARKET 0.6% | 09:00 median 126.00 | Matchbook 180.00
- War Rooms (hrs_36428133) | 5yo G | 166lb | OR - | draw 0 | jockey Brian Hayes | trainer Gerard Keane (14d 0/7) | headgear - | last run 14 days | form 00-6 | MARKET 0.5% | 09:00 median 101.00 | Matchbook 250.00
- Walkwithmyfriend (hrs_17391685717) | 4yo G | 165lb | OR - | draw 0 | jockey Jordan Gainford | trainer James William Kenny (14d 0/1) | headgear - | last run 11 days | form 4-469 | MARKET 0.5% | 09:00 median 126.00 | Matchbook 220.00
- Modern Day Hero (hrs_17395459291) | 5yo G | 166lb | OR - | draw 0 | jockey Eoghan Finegan(5) | trainer Gordon Elliott (14d 6/41) | headgear - | last run 181 days | form 3/PP-5 | MARKET 0.4% | 09:00 median 126.00 | Matchbook 300.00
- Lady Cosmo (hrs_51341787) | 6yo M | 159lb | OR - | draw 0 | jockey Paddy Cody(7) | trainer R P Cody (14d 1/3) | headgear - | last run 216 days | form 7/168- | MARKET 0.4% | 09:00 median 201.00 | Matchbook 250.00
- Eamon's Dream (hrs_57654471) | 4yo G | 165lb | OR - | draw 0 | jockey Ben Kennedy(7) | trainer Seamus Fahey (14d 0/2) | headgear - | last run 200 days | form 0- | MARKET 0.4% | 09:00 median 201.00 | Matchbook 290.00
- Crystal Yeats (hrs_51831395) | 5yo G | 166lb | OR - | draw 0 | jockey Ms E Dunseath(7) | trainer Noel C. Kelly (14d 2/5) | headgear - | last run 208 days | form 4/307- | MARKET 0.3% | 09:00 median 138.50 | Matchbook 530.00
- Attack Or Defend (hrs_17395462420) | 5yo G | 166lb | OR - | draw 0 | jockey Ricky Doyle | trainer D Broad (14d 0/0) | headgear - | last run 202 days | form F3F- | MARKET 0.3% | 09:00 median 151.00 | Matchbook 1000.00
- Parisian Dream (hrs_17392933145) | 4yo G | 165lb | OR - | draw 0 | jockey Shane Markey(7) | trainer Ross O'Sullivan (14d 1/19) | headgear - | last run 20 days | form 95 | MARKET 0.3% | 09:00 median 151.00 | Matchbook 1000.00
- Awayoutback (hrs_17394893985) | 5yo G | 166lb | OR - | draw 0 | jockey Ben Harvey | trainer Cian Collins (14d 1/7) | headgear - | last run 11 days | form P-20 | MARKET 0.2% | 09:00 median 201.00 | Matchbook 1000.00
- Jetaway Mountain (hrs_58132620) | 5yo G | 166lb | OR - | draw 0 | jockey Ross Berry(7) | trainer C A Murphy (14d 0/2) | headgear - | last run 20 days | form 2-688 | MARKET 0.2% | 09:00 median 201.00 | Matchbook 1000.00
- Rough And Tough (hrs_34774978) | 6yo G | 166lb | OR - | draw 0 | jockey Kieren Buckley | trainer Michael Mulvany (14d 0/4) | headgear - | last run 6 days | form 8 | MARKET 0.2% | 09:00 median 201.00 | Matchbook 1000.00

## 12:27 Navan | race_id rac_32304586171 | Lisadell Equine Hospital 110 Series Final Handicap Hurdle
Hurdle |  | 2m4f50y | going Good To Yielding | Turf | 12 runners | rating band - | age 3yo+
- Macshadow Des Crai (hrs_58132907) | 4yo G | 161lb | OR 109 | draw 0 | jockey Jack Kennedy | trainer Ian Patrick Donoghue (14d 0/4) | headgear t | last run 108 days | form 6527-3 | MARKET 18.8% | 09:00 median 5.00 | Matchbook 4.50 | CHECK (skip line 4.75)
    comment: Third last time out and a second three starts back show Macshadow Des Crai can get involved, and he has run on today's going, but he is yet to win in his last five starts and returns after 108 days off.
- Miners Bridge (hrs_28220507) | 9yo G | 164lb | OR 111 | draw 0 | jockey Phillip Enright | trainer S Curling (14d 0/1) | headgear - | last run 27 days | form 2-4111 | MARKET 17.9% | 09:00 median 4.50 | Matchbook 4.90
    comment: Miners Bridge arrives in cracking form, a winner last time out, and again two and three starts back, and he has run over today's trip and going before.
- Beckistine (hrs_46416377) | 7yo G | 166lb | OR 113 | draw 0 | jockey Mark Walsh | trainer M A Molloy (14d 0/1) | headgear - | last run 27 days | form 6P-841 | MARKET 14.1% | 09:00 median 5.50 | Matchbook 6.80
    comment: The main risk is a mixed record before that, with an eighth three starts back and a pulled up four starts back.
- Jacko Star (hrs_50402387) | 5yo G | 160lb | OR 107 | draw 0 | jockey Peter Smithers(5) | trainer J P Dempsey (14d 0/1) | headgear - | last run 37 days | form 4404-F | MARKET 8.2% | 09:00 median 9.00 | Matchbook 12.50
    comment: Jacko Star fell last time out but was a fourth two starts back and has run over today's trip and going, so he's no stranger to conditions.
- Mount Shenshan (hrs_33274843) | 8yo M | 145lb | OR 92 | draw 0 | jockey Brian Hayes | trainer Thomas Mullins (14d 0/6) | headgear t | last run 23 days | form 560611 | MARKET 7.0% | 09:00 median 11.00 | Matchbook 14.00
    comment: Mount Shenshan arrives a double winner, successful last time out and two starts back, and has run over today's trip and going, but she carries 145 lb off an official mark of 92.
- Bossy Bird (hrs_52054058) | 6yo M | 153lb | OR 100 | draw 0 | jockey James Smith(3) | trainer Thomas Gibney (14d 1/7) | headgear t | last run 32 days | form 425853 | MARKET 5.7% | 09:00 median 15.00 | Matchbook 16.00
    comment: Bossy Bird was third last time out and has been in the first five in five of her last six, yet she's without a win in that spell.
- Magic Day (hrs_40786732) | 7yo M | 165lb | OR 112 | draw 0 | jockey Caragh Monaghan(7) | trainer Ian Patrick Donoghue (14d 0/4) | headgear ht (1st time) | last run 56 days | form 3-6243 | MARKET 5.6% | 09:00 median 12.00 | Matchbook 20.00
    comment: Magic Day is consistent, third last time out, a fourth two starts back and a second three runs ago, and she has run over today's trip and going before.
- Mother Ship (hrs_40260584) | 6yo M | 151lb | OR 98 | draw 0 | jockey Harry Sexton(7) | trainer John Joseph Hanlon (14d 0/12) | headgear tp | last run 23 days | form 722191 | MARKET 5.1% | 09:00 median 16.00 | Matchbook 19.50
- Grandy Lane (hrs_51124185) | 6yo G | 158lb | OR 105 | draw 0 | jockey Keith Donoghue | trainer Gavin Cromwell (14d 6/38) | headgear t | last run 39 days | form 86F-P0 | MARKET 4.8% | 09:00 median 15.00 | Matchbook 23.00
    comment: Grandy Lane has had a rough recent spell, unplaced last time, pulled up two starts back and a faller three starts back, though he has run over today's trip and going and returns after 39 days.
- Private Policy (hrs_29522689) | 8yo G | 156lb | OR 103 | draw 0 | jockey Paddy Cleary(7) | trainer Nigel Thomas Slevin (14d 0/1) | headgear t | last run 23 days | form 4-1514 | MARKET 4.7% | 09:00 median 17.00 | Matchbook 21.00
    comment: Against that, he's won twice in his last five, including a win two starts back, and has run over today's trip and going.
- Dairy Force (hrs_38288453) | 7yo G | 163lb | OR 110 | draw 0 | jockey Danny Gilligan | trainer Gordon Elliott (14d 6/41) | headgear h | last run 35 days | form 3F6217 | MARKET 4.2% | 09:00 median 19.00 | Matchbook 24.00
    comment: The risk is a seventh last time out, plus 163 lb and a 35-day break.
- Just For One (hrs_49974428) | 5yo G | 154lb | OR 101 | draw 0 | jockey Sam Ewing | trainer Daniel G Murphy (14d 0/1) | headgear - | last run 20 days | form PP1-73 | MARKET 4.1% | 09:00 median 19.00 | Matchbook 25.00
    comment: Just For One was third last time out, 20 days ago, but a seventh before that and two pulled-up efforts in his last five starts make him hard to fancy.

## 1:02 Navan | race_id rac_32304588108 | Hotel Park St. Johann In Tirol Austria Handicap Hurdle
Hurdle |  | 2m0f50y | going Good To Yielding | Turf | 16 runners | rating band - | age 4yo+
- Radiator Springs (hrs_52709412) | 6yo M | 157lb | OR 120 | draw 0 | jockey Mike O'Connor | trainer Henry de Bromhead (14d 6/37) | headgear - | last run 55 days | form 3128-4 | MARKET 17.1% | 09:00 median 4.33 | Matchbook 5.00 | CHECK (skip line 4.11)
    comment: The main risk is a 55-day absence under 157 lb.
- Simply Natural (hrs_49974365) | 6yo M | 151lb | OR 114 | draw 0 | jockey Conor Stone-Walsh | trainer Gavin Cromwell (14d 6/38) | headgear - | last run 20 days | form 6224-1 | MARKET 12.9% | 09:00 median 5.50 | Matchbook 7.20
    comment: She has run over today's trip, yet the weight looks a hefty ask.
- Rightfolksplease (hrs_34153595) | 8yo G | 141lb | OR 104 | draw 0 | jockey Kevin Healy(7) | trainer Declan Queally (14d 0/3) | headgear t | last run 93 days | form F0/211 | MARKET 10.1% | 09:00 median 7.00 | Matchbook 9.00
    comment: Rightfolksplease arrives a back-to-back winner, with a second three starts back too, and has run over today's trip and going, but a 93-day break is a worry.
- Blue Train (hrs_44264507) | 4yo G | 154lb | OR 117 | draw 0 | jockey Philip Byrnes | trainer C Byrnes (14d 0/8) | headgear h | last run 20 days | form 781-54 | MARKET 8.7% | 09:00 median 8.00 | Matchbook 11.00
    comment: Blue Train comes off a fourth last time out, and a win three starts back shows he can do it, while a fifth before that keeps him ticking along.
- Sommesky (hrs_39978281) | 7yo G | 162lb | OR 125 | draw 0 | jockey Danny Power(7) | trainer Henry de Bromhead (14d 6/37) | headgear - | last run 318 days | form 76/5F- | MARKET 7.0% | 09:00 median 11.00 | Matchbook 12.50
    comment: Sommesky fell last time out after a fifth and a sixth in the two runs before, and returns from 318 days off, so fitness is a worry under 162 lb.
- Arch Empire (hrs_39431672) | 6yo G | 155lb | OR 118 | draw 0 | jockey Danny Gilligan | trainer Gordon Elliott (14d 6/41) | headgear - | last run 14 days | form 7-6899 | MARKET 6.9% | 09:00 median 10.00 | Matchbook 14.00
    comment: The main risk is a winless run of five and a hefty 155 lb.
- St Denis's Well (hrs_29889909) | 8yo G | 150lb | OR 113 | draw 0 | jockey Caragh Monaghan(7) | trainer Ian Patrick Donoghue (14d 0/4) | headgear tb | last run 44 days | form 6P29-0 | MARKET 5.6% | 09:00 median 11.00 | Matchbook 18.00
    comment: St Denis's Well has run over today's trip and going, and he bounced back from a pulled up to finish second three starts back, but he's been unplaced last time out and a ninth two starts back, and is yet to win in his last five. Carrying 150 lb after 44 days off, he looks a midfield type.
- This Songisforyou (hrs_31274250) | 8yo G | 149lb | OR 112 | draw 0 | jockey Donagh Meyler | trainer Emmet Mullins (14d 2/4) | headgear h (1st time) | last run 19 days | form 655/70 | MARKET 5.2% | 09:00 median 12.00 | Matchbook 20.00
    comment: Winless in his last five, with a sixth, two fifths and a seventh before an unplaced effort last time, This Songisforyou is consistent without threatening, though he has run over today's trip and going and is fresh enough after 19 days.
- Path d'Oroux (hrs_27794046) | 9yo G | 163lb | OR 126 | draw 0 | jockey Keith Donoghue | trainer Gavin Cromwell (14d 6/38) | headgear tv | last run 50 days | form 950-00 | MARKET 5.0% | 09:00 median 13.00 | Matchbook 19.00
    comment: He is yet to win in his last five starts and returns after 50 days off.
- Catchabird (hrs_31672949) | 8yo M | 146lb | OR 109 | draw 0 | jockey Aidan Kelly | trainer Sarah Joanna Connell (14d 0/0) | headgear h | last run 198 days | form 34115- | MARKET 4.0% | 09:00 median 19.00 | Matchbook 23.00
    comment: Catchabird won two starts back and three starts back, but she was only fifth last time out and returns after a 198-day break, which makes her hard to fancy.
- Fiveonefive (hrs_30672138) | 8yo G | 166lb | OR 129 | draw 0 | jockey Jordan Gainford | trainer Cian Collins (14d 1/7) | headgear p | last run 22 days | form 843199 | MARKET 3.9% | 09:00 median 19.00 | Matchbook 23.00
    comment: The risk is two ninth-place finishes in his last two outings, while he carries 166 lb.
- Malbay Madness (hrs_30096689) | 6yo G | 155lb | OR 118 | draw 0 | jockey P J O'Hanlon | trainer Dermot A McLoughlin (14d 0/8) | headgear h | last run 14 days | form 118195 | MARKET 3.6% | 09:00 median 19.00 | Matchbook 26.00
    comment: Three wins in his last six starts, including a win three starts back, is a decent calling card, but a fifth last time out and a ninth two starts back suggest the sharpness has dipped. He has run over today's trip and going and is back after 14 days, though 155 lb is a big burden off 118.
- Hesgonethatway (hrs_57877918) | 5yo G | 143lb | OR 106 | draw 0 | jockey Tiernan Power Roche | trainer P. J. Rothwell (14d 0/23) | headgear - | last run 20 days | form 8150-8 | MARKET 2.9% | 09:00 median 23.00 | Matchbook 38.00
    comment: Hesgonethatway was eighth last time out and unplaced the start before, so the form is going the wrong way since a win four starts back, while a yard 0/23 in the last 14 days adds to the doubts. He has run over today's trip and is back after 20 days, but 143 lb is a big ask.
- Solsbury Hill (hrs_41090987) | 7yo G | 147lb | OR 110 | draw 0 | jockey Charlie O'Dwyer(3) | trainer Conor O'Dwyer (14d 0/2) | headgear t | last run 98 days | form 790-U6 | MARKET 2.8% | 09:00 median 26.00 | Matchbook 32.00
    comment: Solsbury Hill is winless in his last five, with a sixth last time out, an unseated two starts back and a seventh five runs ago, and he returns after 98 days off carrying 147 lb.
- Dont Go Yet (hrs_17841691) | 12yo G | 151lb | OR 114 | draw 0 | jockey Sarah Kavanagh(7) | trainer Edward Cawley (14d 0/1) | headgear - | last run 173 days | form 7133-U | MARKET 2.6% | 09:00 median 29.00 | Matchbook 38.00
    comment: Dont Go Yet banked a win four starts back and was third twice after that, but he unseated last time out and returns after 173 days off.
- Duke Of Leggagh (hrs_30208157) | 6yo G | 153lb | OR 116 | draw 0 | jockey Luke Carberry(7) | trainer Michael Mulvany (14d 0/4) | headgear t | last run 45 days | form 11P/9- | MARKET 1.6% | 09:00 median 51.00 | Matchbook 55.00
    comment: Duke Of Leggagh won three and four starts back, but he's since run poorly, finishing ninth last time out after being pulled up the run before.

## 1:35 Navan | race_id rac_32304590045 | BAR 1 Betting 'Download Our App' For Auction Novice Hurdle (Grade 3)
Hurdle | Class 1 | 2m0f50y | going Good To Yielding | Turf | 8 runners | rating band - | age 4yo+
- City Of Cork (hrs_58962911) | 5yo G | 155lb | OR - | draw 0 | jockey Paul Townend | trainer Joseph Patrick O'Brien (14d 3/28) | headgear h | last run 23 days | form 734-1 | MARKET 25.2% | 09:00 median 3.50 | Matchbook 3.80 | CHECK (skip line 3.32)
- Thinkitdontjinxit (hrs_58963009) | 5yo G | 155lb | OR - | draw 0 | jockey Jack Kennedy | trainer Gordon Elliott (14d 6/41) | headgear - | last run 19 days | form 1228-1 | MARKET 24.9% | 09:00 median 3.50 | Matchbook 3.90
- State Pension (hrs_39996621) | 6yo G | 155lb | OR - | draw 0 | jockey Cian Quirke | trainer David Harry Kelly (14d 0/7) | headgear - | last run 40 days | form 135-31 | MARKET 11.7% | 09:00 median 7.50 | Matchbook 8.20
- It's Only A Game (hrs_52297896) | 5yo G | 155lb | OR - | draw 0 | jockey Mark Walsh | trainer Martin Brassil (14d 0/2) | headgear h (1st time) | last run 248 days | form 2/140- | MARKET 11.4% | 09:00 median 8.00 | Matchbook 7.80
- Fiveandahalf (hrs_63171353) | 4yo G | 155lb | OR - | draw 0 | jockey Keith Donoghue | trainer Gavin Cromwell (14d 6/38) | headgear - | last run 31 days | form 4-11 | MARKET 10.1% | 09:00 median 8.00 | Matchbook 10.50
- The Captain's Word (hrs_57878170) | 5yo G | 155lb | OR - | draw 0 | jockey Jordan Gainford | trainer Henry de Bromhead (14d 6/37) | headgear - | last run 43 days | form 423-1 | MARKET 6.7% | 09:00 median 12.00 | Matchbook 15.50
- Game Point (hrs_46233719) | 4yo G | 155lb | OR 120 | draw 0 | jockey Sam Ewing | trainer R P Cody (14d 1/3) | headgear - | last run 27 days | form 323311 | MARKET 6.4% | 09:00 median 13.00 | Matchbook 16.50
- Joe Cool (hrs_51373623) | 4yo G | 155lb | OR - | draw 0 | jockey Donagh Meyler | trainer Noel Meade (14d 3/12) | headgear - | last run 13 days | form 1 | MARKET 3.7% | 09:00 median 23.00 | Matchbook 29.00

## 2:07 Navan | race_id rac_32304591982 | Railway Bar Lismullen Hurdle (Grade 2)
Hurdle | Class 1 | 2m4f50y | going Good To Yielding | Turf | 8 runners | rating band - | age 4yo+
- The Yellow Clay (hrs_34153560) | 7yo G | 157lb | OR 153 | draw 0 | jockey Jack Kennedy | trainer Gordon Elliott (14d 6/41) | headgear p | last run 222 days | form /25F5- | MARKET 23.1% | 09:00 median 3.75 | Matchbook 4.20 | CHECK (skip line 3.56)
    comment: The main risk is a 222-day layoff, with a fifth last time out and a fall before that, under 157 lb.
- I'll Sort That (hrs_45792089) | 6yo G | 163lb | OR 144 | draw 0 | jockey Mr D L Queally | trainer Declan Queally (14d 0/3) | headgear - | last run 248 days | form 11115- | MARKET 19.3% | 09:00 median 4.50 | Matchbook 5.00
    comment: I'll Sort That won four of his last five, with a fifth last time out, and has run over today's trip and going.
- Slade Steel (hrs_30016385) | 8yo G | 162lb | OR 150 | draw 0 | jockey Mark Walsh | trainer Henry de Bromhead (14d 6/37) | headgear tp | last run 222 days | form 2B261- | MARKET 19.3% | 09:00 median 4.50 | Matchbook 5.00
    comment: Slade Steel won last time out and has a second five starts back among his recent finishes, and he has run over today's trip and going before, carrying 162 lb off an official mark of 150. The main risk is a 222-day layoff, so fitness is the question.
- Casheldale Lad (hrs_37110731) | 6yo G | 157lb | OR 151 | draw 0 | jockey Danny Gilligan | trainer Gordon Elliott (14d 6/41) | headgear h | last run 107 days | form 11F3-9 | MARKET 15.0% | 09:00 median 6.00 | Matchbook 6.40
    comment: Casheldale Lad has won two of his last five, including back-to-back victories four and five starts back, and a third two runs ago shows he retains plenty of ability, while he has run on today's going before. The risk is a 107-day absence and a ninth last time out, with 157 lb to carry.
- Feet Of A Dancer (hrs_33975284) | 7yo M | 155lb | OR 144 | draw 0 | jockey Sean O'Keeffe | trainer Paul Nolan (14d 5/29) | headgear - | last run 247 days | form /1213- | MARKET 9.7% | 09:00 median 9.00 | Matchbook 10.50
- Home By The Lee (hrs_18645662) | 11yo G | 166lb | OR 161 | draw 0 | jockey Richard Deegan | trainer Joseph Patrick O'Brien (14d 3/28) | headgear - | last run 182 days | form 4111-P | MARKET 7.5% | 09:00 median 11.00 | Matchbook 14.00
- Dawn Rising (hrs_16762270) | 9yo G | 157lb | OR 136 | draw 0 | jockey Keith Donoghue | trainer Joseph Patrick O'Brien (14d 3/28) | headgear - | last run 35 days | form 113P6/ | MARKET 3.6% | 09:00 median 23.00 | Matchbook 29.00
    comment: Dawn Rising has tailed off since a winner four starts back and again five starts back, with a sixth last time out and a pulled up before that, so he is hard to fancy carrying 157 lb.
- Staffordshire Knot (hrs_33465306) | 8yo G | 162lb | OR 149 | draw 0 | jockey Sam Ewing | trainer Gordon Elliott (14d 6/41) | headgear b | last run 194 days | form 121P-6 | MARKET 2.4% | 09:00 median 34.00 | Matchbook 55.00
    comment: Staffordshire Knot won twice in his last five starts, a first three starts back and another five back, but he was sixth last time and pulled up before that, and he returns after 194 days off.

## 2:43 Navan | race_id rac_32304593919 | BAR 1 Betting Fortria Steeplechase (Grade 2)
Chase | Class 1 | 2m0f0y | going Yielding | Turf | 7 runners | rating band - | age 5yo+
- Majborough (hrs_34932142) | 6yo G | 168lb | OR 170 | draw 0 | jockey Mark Walsh | trainer W. P. Mullins (14d 8/28) | headgear p | last run 200 days | form 23174- | MARKET 36.6% | 09:00 median 2.50 | Matchbook 2.62
    comment: Majborough has a win and a second and third in his last five starts, and he has run over today's trip and on the going before, while a yard in form (8 from 28) adds to the case. The main risk is a 200-day absence, with a fourth last time out and a seventh the start before.
- Only By Night (hrs_29906884) | 8yo M | 154lb | OR 150 | draw 0 | jockey Keith Donoghue | trainer Gavin Cromwell (14d 6/38) | headgear p | last run 197 days | form /1523- | MARKET 17.7% | 09:00 median 5.00 | Matchbook 5.50
    comment: Only By Night arrives off a 197-day break, which is a concern, though she was third last time out and second the run before, and has run over today's trip and going.
- Solness (hrs_29747795) | 8yo G | 168lb | OR 164 | draw 0 | jockey Richard Deegan | trainer Joseph Patrick O'Brien (14d 3/28) | headgear tp | last run 45 days | form 1523-0 | MARKET 15.7% | 09:00 median 5.50 | Matchbook 6.40
    comment: The reservation is an unplaced effort last time and 45 days off.
- Found A Fifty (hrs_27794151) | 9yo G | 164lb | OR 160 | draw 0 | jockey Jack Kennedy | trainer Gordon Elliott (14d 6/41) | headgear - | last run 222 days | form 434P3- | MARKET 15.6% | 09:00 median 5.50 | Matchbook 6.40
    comment: The main risk is a 222-day absence under 164 lb, and he is yet to win in that spell.
- Blood Destiny (hrs_29690759) | 7yo G | 161lb | OR 154 | draw 0 | jockey Paul Townend | trainer W. P. Mullins (14d 8/28) | headgear t | last run 42 days | form 5-2162 | MARKET 10.6% | 09:00 median 8.50 | Matchbook 9.20
- Touch Me Not (hrs_34557796) | 7yo G | 158lb | OR 150 | draw 0 | jockey Danny Gilligan | trainer Gordon Elliott (14d 6/41) | headgear - | last run 200 days | form 23200- | MARKET 3.0% | 09:00 median 29.00 | Matchbook 38.00
    comment: Touch Me Not showed ability with a second five starts back, a third four back and a second three back, but he has been unplaced in his last two and returns after 200 days off. He has run over today's trip and going, yet 158 lb is a hefty burden.
- Lady Doyanne (hrs_49110390) | 6yo M | 148lb | OR 108 | draw 0 | jockey Mike O'Connor | trainer Henry de Bromhead (14d 6/37) | headgear t | last run 37 days | form 432232 | MARKET 0.8% | 09:00 median 101.00 | Matchbook 200.00
    comment: Lady Doyanne has been placed in five of her last six, including a second last time out, yet she's winless in that spell and keeps finding one too good.

## 3:18 Navan | race_id rac_32304595856 | Jimmy & Sheila Owens Irish EBF Beginners Steeplechase
Chase |  | 2m1f0y | going Yielding | Turf | 11 runners | rating band - | age 4yo+
- Mighty Park (hrs_52055465) | 5yo G | 166lb | OR - | draw 0 | jockey Mark Walsh | trainer W. P. Mullins (14d 8/28) | headgear - | last run 249 days | form 2/19- | MARKET 41.6% | 09:00 median 2.00 | Matchbook 2.22
    comment: Mighty Park won two starts back and was second three runs ago, but he was beaten into ninth last time out and returns after 249 days off, which raises fitness doubts. He has run over today's trip and going, and the yard is in form, though 166 lb is a hefty burden.
- Saint Baco (hrs_45314584) | 5yo G | 166lb | OR - | draw 0 | jockey Paul Townend | trainer W. P. Mullins (14d 8/28) | headgear - | last run 197 days | form 16F54- | MARKET 24.2% | 09:00 median 3.50 | Matchbook 3.70
    comment: Fourth last time out and a winner five starts back, Saint Baco has run over today's trip and on this going before, while his yard is in cracking form at 8 from 28 over the last 14 days.
- Bleu De Vassy (hrs_35054712) | 7yo G | 166lb | OR - | draw 0 | jockey Jack Kennedy | trainer Gordon Elliott (14d 6/41) | headgear - | last run 650 days | form 11126/ | MARKET 11.3% | 09:00 median 7.00 | Matchbook 8.80
    comment: Three wins in his last five starts, followed by a second two runs back, make him a serious threat, and he has run over today's trip and going before; the one concern is a 650-day absence, with a sixth last time out and 166 lb to carry.
- Wingmen (hrs_29523263) | 8yo G | 166lb | OR 138 | draw 0 | jockey Sam Ewing | trainer Gordon Elliott (14d 6/41) | headgear - | last run 197 days | form 32920- | MARKET 8.0% | 09:00 median 9.00 | Matchbook 13.00
    comment: The main risk is a 197-day absence, plus an unplaced effort last time out and 166 lb to carry.
- Largy Star (hrs_52236639) | 7yo G | 166lb | OR - | draw 0 | jockey Keith Donoghue | trainer Gavin Cromwell (14d 6/38) | headgear - | last run 197 days | form 11231- | MARKET 5.8% | 09:00 median 13.00 | Matchbook 17.50
    comment: He has run on today's going before, which helps.
- Powerful (hrs_48886271) | 5yo G | 166lb | OR - | draw 0 | jockey Simon Torrens | trainer Mrs J. Harrington (14d 2/14) | headgear - | last run 200 days | form 18181- | MARKET 3.7% | 09:00 median 21.00 | Matchbook 28.00
    comment: Powerful won last time out and has three wins in his last five starts, with a win three starts back and another five starts back, and he has run over today's trip and going before. The one concern is a 200-day absence, so fitness is the question at 166 lb.
- Jet To Monte Carlo (hrs_51124325) | 5yo G | 166lb | OR - | draw 0 | jockey Donagh Meyler | trainer Emmet Mullins (14d 2/4) | headgear - | last run 200 days | form 7251P- | MARKET 1.8% | 09:00 median 34.00 | Matchbook 70.00
    comment: Pulled up last time out and returns from a 200-day break, but he won two starts back and has run over today's trip, so there's a touch of ability to work with.
- Time Is A Thief (hrs_39826892) | 6yo G | 166lb | OR - | draw 0 | jockey Jordan Gainford | trainer Henry de Bromhead (14d 6/37) | headgear h | last run 41 days | form /F1-23 | MARKET 1.4% | 09:00 median 41.00 | Matchbook 110.00
    comment: Time Is A Thief arrives in solid recent form, third last time out, a second two starts back, and a winner three starts back, and he has run over today's trip.
- Champagne Jury (hrs_40096035) | 7yo G | 166lb | OR - | draw 0 | jockey Kieren Buckley | trainer Gavin Cromwell (14d 6/38) | headgear t | last run 251 days | form /3154- | MARKET 1.3% | 09:00 median 41.00 | Matchbook 150.00
    comment: Champagne Jury was a winner three starts back and a fourth last time out, and he has run over today's trip and going before, but a 251-day absence raises fitness doubts.
- Royal Soldier (hrs_41052872) | 6yo G | 166lb | OR - | draw 0 | jockey Conor Stone-Walsh | trainer Mrs Gillian Callaghan (14d 0/1) | headgear - | last run 6 days | form 41F-P7 | MARKET 0.4% | 09:00 median 151.00 | Matchbook 260.00
    comment: Royal Soldier is hard to fancy after a seventh last time out, following a pulled up and a fall in the two runs before, though he did win four starts back and has run over today's trip.
- Workinonadream (hrs_37068143) | 8yo M | 159lb | OR - | draw 0 | jockey Alix Balfe(7) | trainer Tom Dreaper (14d 0/3) | headgear - | last run 14 days | form /30P-4 | MARKET 0.3% | 09:00 median 151.00 | Matchbook 520.00
    comment: Workinonadream was a fourth last time out but pulled up two starts back, and she is winless in her last four, so she is hard to fancy.

## 3:53 Navan | race_id rac_32304597793 | BAR 1 Betting Best Odds Guaranteed Overnight (Pro/Am) Flat Race
NH Flat |  | 2m0f50y | going Good To Yielding | Turf | 10 runners | rating band - | age 4yo+
- Uncle Pad (hrs_17394707288) | 5yo G | 168lb | OR - | draw 0 | jockey Mr H C Swan | trainer Gordon Elliott (14d 6/41) | headgear - | last run 286 days | form 1- | MARKET 35.3% | 09:00 median 2.25 | Matchbook 2.74
    comment: Won last time out, his only recent start, so Uncle Pad is unexposed and open to improvement, though he returns after 286 days off and carries 168 lb, which makes fitness the question.
- Kanzler (hrs_49757624) | 5yo G | 168lb | OR - | draw 0 | jockey Miss J Townend | trainer W. P. Mullins (14d 8/28) | headgear h (1st time) | last run 644 days | form 1/ | MARKET 17.1% | 09:00 median 5.00 | Matchbook 5.40
    comment: Kanzler won last time out, his only recent run, but that came 644 days ago, so this gelding returns after a long absence. Unexposed and open to improvement, he carries 168 lb, and his yard is in good form with 8 winners from 28 in the last 14 days.
- Sir Vinny (hrs_54304565) | 5yo G | 168lb | OR - | draw 0 | jockey Mr J L Gleeson | trainer David Harry Kelly (14d 0/7) | headgear - | last run 55 days | form 3222 | MARKET 13.5% | 09:00 median 6.00 | Matchbook 7.20
    comment: Sir Vinny has been placed in each of his last four starts, finishing second last time out, a second two starts back, a second three starts back, and a third four starts back, and he has run over today's trip and going.
- Elusive Legend (hrs_17395469721) | 5yo G | 168lb | OR - | draw 0 | jockey Mr Finian Maguire | trainer Barry Connell (14d 0/4) | headgear - | last run - days | form - | MARKET 8.6% | 09:00 median 10.00 | Matchbook 11.50
    comment: Elusive Legend is an unraced gelding with no form to go on, so he's an unexposed type who could easily find improvement as he learns his trade. He shoulders 168 lb on debut, and that's the key angle for a horse yet to show anything on a racecourse.
- Certain Escape (hrs_17394713546) | 4yo G | 168lb | OR - | draw 0 | jockey Mr Jack Paddy Carroll(7) | trainer Gordon Elliott (14d 6/41) | headgear - | last run 189 days | form F-1 | MARKET 7.7% | 09:00 median 9.00 | Matchbook 15.00
    comment: Certain Escape won last time out, though he fell two starts back, and returns after 189 days off carrying 168 lb. He looks unexposed on this limited evidence and open to further improvement, but the long absence is worth noting.
- Nine Toes Tim (hrs_59429482) | 5yo G | 168lb | OR - | draw 0 | jockey Mr T A Halford(7) | trainer S. R. B. Crawford (14d 0/5) | headgear - | last run 321 days | form 2- | MARKET 6.7% | 09:00 median 13.00 | Matchbook 14.00
    comment: The risk is a 321-day absence, so fitness is the question, and he carries 168 lb.
- Airforce Marshal (hrs_17393783190) | 5yo G | 168lb | OR - | draw 0 | jockey Mr J Dunne(7) | trainer Gordon Elliott (14d 6/41) | headgear - | last run 195 days | form P/1- | MARKET 6.5% | 09:00 median 13.00 | Matchbook 14.50
    comment: Won last time out, having pulled up two starts back, so Airforce Marshal is lightly raced and open to improvement. He returns after 195 days off and carries 168 lb, so fitness is the question.
- Noble Indulgence (hrs_63202804) | 4yo G | 168lb | OR - | draw 0 | jockey Mr Finn Tegetmeier(7) | trainer Noel Meade (14d 3/12) | headgear - | last run 200 days | form 0- | MARKET 2.5% | 09:00 median 34.00 | Matchbook 48.00
    comment: Noble Indulgence is lightly raced and unexposed, with just one recent outing, an unplaced effort last time out, so there should be more to come. He returns after 200 days off and carries 168 lb, and he is yet to win in recent form.
- Giomibe (hrs_17395471807) | 5yo G | 168lb | OR - | draw 0 | jockey Anna McGuinness(7) | trainer Paul Traynor (14d 0/0) | headgear - | last run 209 days | form FF- | MARKET 1.1% | 09:00 median 67.00 | Matchbook 100.00
    comment: Giomibe is unexposed and lightly raced, with a fall last time out and another two starts back, so he has yet to complete in recent starts. He returns after 209 days off carrying 168 lb, and there should be improvement to come if he stays on his feet.
- Line Speed (hrs_59186505) | 7yo G | 168lb | OR - | draw 0 | jockey Mr Hugh Lillingston(7) | trainer John E & Thomas Kiely (14d 0/1) | headgear - | last run 223 days | form 7558- | MARKET 1.0% | 09:00 median 67.00 | Matchbook 140.00
    comment: The main risk is a 223-day absence after an eighth last time out.
