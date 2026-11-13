# Card review packet: Southwell, 2026-11-13

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
{"meeting": "southwell", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 12:20 Southwell | race_id rac_32304314991 | DBS And Willmott Dixon Building Together Handicap Steeple Chase
Chase | Class 5 | 2m4f88y | going Good | Turf | 10 runners | rating band 0-100 | age 4yo+
- Golly Gosh (hrs_51988888) | 5yo G | 152lb | OR 82 | draw 0 | jockey Jack Andrews | trainer Tom Ellis (14d 1/20) | headgear t | last run 25 days | form -P7221 | MARKET 37.1% | 09:00 median 2.25 | Matchbook 2.52
    comment: Golly Gosh arrives in cracking nick, a winner last time out after two seconds before that, and he has run over today's trip and going.
- Walkinthepresent (hrs_51341451) | 6yo G | 160lb | OR 90 | draw 0 | jockey Dylan Johnston | trainer Neil Mulholland (14d 6/27) | headgear p | last run 23 days | form 3314-P | MARKET 14.8% | 09:00 median 5.50 | Matchbook 6.60
    comment: Walkinthepresent was pulled up last time out, which tempers a profile that includes a winner three starts back and a fourth two starts back; he has run over today's trip and going, and 23 days off helps.
- Unleash The Beast (hrs_39109602) | 7yo G | 168lb | OR 98 | draw 0 | jockey Liam Harrison | trainer Fergal O'Brien (14d 3/26) | headgear - | last run 265 days | form 27/76- | MARKET 14.5% | 09:00 median 5.75 | Matchbook 6.40
    comment: The big risk is fitness, as he returns after 265 days off and has finished sixth and seventh in his last three outings.
- Ionity (hrs_37860634) | 7yo G | 159lb | OR 89 | draw 0 | jockey Adam Wedge | trainer Mrs C. Williams (14d 2/22) | headgear - | last run 22 days | form 3/32-P | MARKET 10.0% | 09:00 median 8.50 | Matchbook 9.40
    comment: Ionity was pulled up last time out, though he was second two starts back and third in the two runs before that, so he's yet to win in his last four.
- Largy Panic (hrs_47129390) | 6yo G | 164lb | OR 94 | draw 0 | jockey David Noonan | trainer Ben Clarke (14d 0/5) | headgear t | wind surgery | last run 206 days | form 79817- | MARKET 7.4% | 09:00 median 11.00 | Matchbook 13.00
    comment: Largy Panic won two starts back but was only seventh last time out, and he returns after 206 days off and carries 164 lb, which adds to the task.
- Jac Jumper (hrs_32682769) | 7yo G | 163lb | OR 93 | draw 0 | jockey Joe Anderson(3) | trainer Deborah Cole (14d 0/2) | headgear tp | last run 499 days | form 22/45- | MARKET 6.4% | 09:00 median 12.00 | Matchbook 16.50
- Scoro (hrs_39568473) | 6yo G | 142lb | OR 69 | draw 0 | jockey Harry Reed | trainer L J Morgan (14d 0/8) | headgear tp | last run 11 days | form 4664PP | MARKET 3.1% | 09:00 median 26.00 | Matchbook 34.00
    comment: Scoro is hard to fancy, pulled up in his last two outings and yet to win in his last six, with a best finish of fourth, though he's back quickly after 11 days and has run over today's trip and going.
- Get In Order (hrs_51831794) | 6yo G | 164lb | OR 94 | draw 0 | jockey Robert Dunne | trainer Henry Oliver (14d 1/5) | headgear - | last run 23 days | form 4400-7 | MARKET 2.9% | 09:00 median 29.00 | Matchbook 36.00
    comment: The risk is a poor recent run, with a seventh last time out and a fourth five starts back his best finish, and he is yet to win in that spell with 164 lb to carry.
- Woodview Lad (hrs_51800392) | 5yo G | 165lb | OR 95 | draw 0 | jockey Kevin Brogan | trainer Gary Hanmer (14d 0/5) | headgear - | last run 11 days | form 4983-P | MARKET 2.2% | 09:00 median 34.00 | Matchbook 55.00
    comment: Eleven days since a pulled-up effort is a reservation, though he is yet to win in recent form and carries 165 lb off an official 95.
- Caballo Diablo (hrs_21395052) | 10yo G | 142lb | OR 65 | draw 0 | jockey Miss Ellie Callwood(7) | trainer Jonathan Barlow (14d 0/0) | headgear - | last run 412 days | form 73/57- | MARKET 1.6% | 09:00 median 51.00 | Matchbook 75.00
    comment: Without a win in his last four and off a 412-day absence, Caballo Diablo is hard to fancy, having finished seventh last time out, with a fifth two starts back his best recent effort bar a third three starts back. He has run on today's going, and his 142 lb is the other concern.

## 12:55 Southwell | race_id rac_32304316928 | JDA Grand Design Mares' Handicap Steeple Chase
Chase | Class 5 | 3m0f60y | going Good | Turf | 5 runners | rating band 0-100 | age 4yo+
- Out On Her Own (hrs_51618630) | 6yo M | 143lb | OR 75 | draw 0 | jockey Conor O'Farrell | trainer Dianne Sayer (14d 0/3) | headgear - | last run 26 days | form -2545F | MARKET 32.0% | 09:00 median 2.75 | Matchbook 3.05
    comment: Without a win in her last five and a faller last time out, Out On Her Own is hard to fancy, though a second five starts back and fifth and fourth in between show she can get involved.
- Gata Ban (hrs_29621935) | 9yo M | 160lb | OR 92 | draw 0 | jockey Dylan Johnston | trainer Neil Mulholland (14d 6/27) | headgear p | last run 68 days | form -21143 | MARKET 29.5% | 09:00 median 2.94 | Matchbook 3.30
    comment: Gata Ban arrives with solid recent form, third last time out and a winner three starts back, and she has run over today's trip and on this going before. The risk is a 68-day layoff, while she also carries 160 lb.
- Princess Keri (hrs_40095797) | 6yo M | 168lb | OR 100 | draw 0 | jockey Adam Wedge | trainer Mrs C. Williams (14d 2/22) | headgear - | last run 32 days | form U12P-P | MARKET 21.0% | 09:00 median 4.33 | Matchbook 4.60
    comment: Princess Keri signed off with a win four starts back and a second three starts back, and she has run over today's trip and on this going before.
- Kit's Coty (hrs_29906856) | 8yo M | 156lb | OR 88 | draw 0 | jockey Charlie Todd | trainer Emma Lavelle (14d 2/15) | headgear - | last run 27 days | form 433-34 | MARKET 15.0% | 09:00 median 6.00 | Matchbook 6.40
    comment: Kit's Coty has been consistent, finishing fourth last time out, with a third two starts back, a third three starts back and another third four starts back.
- Walkingtheline (hrs_40591943) | 6yo M | 148lb | OR 80 | draw 0 | jockey Toby Wynne | trainer Steph Cameron (14d 0/0) | headgear ht | last run 120 days | form P-12P5 | MARKET 2.5% | 09:00 median 38.50 | Matchbook 44.00
    comment: The main risk is a 120-day absence, with a pulled up two starts back and a fifth last time out.

## 1:30 Southwell | race_id rac_32304318865 | BWB Consulting - Women In Engineering Handicap Steeple Chase (GBB Race)
Chase | Class 4 | 3m1f185y | going Good | Turf | 5 runners | rating band 0-115 | age 4yo+
- May Call You Back (hrs_34874490) | 8yo M | 160lb | OR 116 | draw 0 | jockey Mr P. W. Mullins | trainer Mr W. P. Mullins (14d 8/27) | headgear - | last run 223 days | form 1205F- | MARKET 36.7% | 09:00 median 2.50 | Matchbook 2.62
    comment: May Call You Back has a win and a second in her last five starts and has run over today's trip and going before, while her yard is in cracking form at 8/27 over the last 14 days. The risk is a 223-day absence and a fall last time out, with 160 lb to carry.
- Island Bridge (hrs_40352396) | 6yo G | 158lb | OR 114 | draw 0 | jockey Tom Bellamy | trainer Kim Bailey & Mat Nicholls (14d 2/13) | headgear p (1st time) | last run 22 days | form 2223-4 | MARKET 26.3% | 09:00 median 3.25 | Matchbook 3.85
    comment: Island Bridge arrives consistent, with three seconds and a third in his last five, then a fourth last time out 22 days ago, and he has run on today's going before.
- Ballykinlar (hrs_37890566) | 7yo G | 161lb | OR 117 | draw 0 | jockey James Murray(10) | trainer Mickey Bowen (14d 3/14) | headgear tp | last run 20 days | form 70-337 | MARKET 13.9% | 09:00 median 6.50 | Matchbook 7.00
    comment: Ballykinlar arrives fresh from a 20-day break, with a third two starts back and another third three starts back, and he has run on today's going before.
- Golan Loop (hrs_41190128) | 6yo G | 161lb | OR 117 | draw 0 | jockey Caoilin Quinn | trainer Warren Greatrex (14d 4/19) | headgear - | wind surgery | last run 226 days | form 21P34- | MARKET 12.9% | 09:00 median 6.50 | Matchbook 8.20
    comment: The main risk is a 226-day absence, with 161 lb to carry.
- Express Surprise (hrs_34361446) | 7yo G | 156lb | OR 112 | draw 0 | jockey Ned Fox(3) | trainer Clive Boultbee-Brooks (14d 0/6) | headgear t | last run 203 days | form 1141P- | MARKET 10.2% | 09:00 median 9.00 | Matchbook 9.80
    comment: Carrying 156 lb is a big ask.

## 2:05 Southwell | race_id rac_32304320802 | Lexy 21st Birthday Open National Hunt Flat Race (Category 1 Elimination) (GBB Race)
NH Flat | Class 5 | 1m7f182y | going Good | Turf | 7 runners | rating band - | age 4-5yo
- Helios Forlonge (hrs_17394110692) | 4yo G | 156lb | OR - | draw 0 | jockey Gavin Sheehan | trainer Olly Murphy (14d 6/36) | headgear - | last run 258 days | form 2- | MARKET 31.6% | 09:00 median 2.81 | Matchbook 3.00
    comment: Helios Forlonge finished second last time out, but that was 258 days ago, so he returns after a long break. Winless in his last start and carrying 156 lb, he is unexposed and could have more to offer.
- Francisco Alvares (hrs_17394316163) | 4yo G | 156lb | OR - | draw 0 | jockey Charlie Todd | trainer Dan Skelton (14d 22/93) | headgear - | last run - days | form - | MARKET 21.4% | 09:00 median 4.00 | Matchbook 4.60
    comment: Francisco Alvares is an unexposed gelding with no recorded form to go on, so this is a clean-slate debut and there should be plenty of room for improvement. He carries 156 lb, and his first run will reveal plenty.
- Mirage d'Alene (hrs_17395341432) | 4yo G | 156lb | OR - | draw 0 | jockey Caoilin Quinn | trainer Warren Greatrex (14d 4/19) | headgear - | last run 195 days | form 1- | MARKET 19.4% | 09:00 median 4.50 | Matchbook 5.00
    comment: Winner on his latest outing, Mirage d'Alene is unexposed and open to improvement, though he returns after 195 days off and carries 156 lb, so the layoff is the question mark.
- The Bardman (hrs_17395342475) | 4yo G | 156lb | OR - | draw 0 | jockey Daire McConville(7) | trainer Charlie Longsdon (14d 5/14) | headgear - | last run - days | form - | MARKET 11.9% | 09:00 median 7.50 | Matchbook 8.00
    comment: Unraced and unexposed, The Bardman makes his debut with no form to go on, so any improvement is a matter of potential rather than evidence. The gelding carries 156 lb, and he is one to learn from on this first look.
- I'll Start Monday (hrs_17395340389) | 4yo G | 156lb | OR - | draw 0 | jockey Conor O'Farrell | trainer John Dawson (14d 0/4) | headgear - | last run - days | form - | MARKET 11.7% | 09:00 median 7.50 | Matchbook 8.40
    comment: Unexposed and open to improvement, I'll Start Monday is a debutant with no recorded form to go on, so he's an unknown quantity.
- Liblex Dream (hrs_17393403538) | 4yo F | 149lb | OR - | draw 0 | jockey William Shanahan(5) | trainer Ivan Furtado (14d 0/7) | headgear - | wind surgery | last run - days | form - | MARKET 2.3% | 09:00 median 41.00 | Matchbook 46.00
    comment: Liblex Dream is unraced, so there's no form to lean on, and this debut filly is entirely unexposed with plenty of scope for improvement.
- Madethempay (hrs_17393572504) | 5yo M | 149lb | OR - | draw 0 | jockey Benjamin Macey(5) | trainer Laura Horsfall (14d 0/5) | headgear h (1st time) | last run 31 days | form 3 | MARKET 1.7% | 09:00 median 51.00 | Matchbook 70.00
    comment: Madethempay was third last time out, 31 days ago, and has run over today's trip and on this going before.

## 2:40 Southwell | race_id rac_32304322739 | Festive Fixtures At Southwell Racecourse Mares' Novices' Hurdle Race (Herring Queen Mares' Novices' Hurdle Race Series Qualifier) (GBB Race)
Hurdle | Class 4 | 1m7f182y | going Good | Turf | 7 runners | rating band - | age 4yo+
- Clondaw Park (hrs_50188698) | 5yo M | 154lb | OR - | draw 0 | jockey Paul O'Brien | trainer Harry Derham (14d 5/20) | headgear - | last run 290 days | form 1/U3- | MARKET 44.2% | 09:00 median 2.00 | Matchbook 2.18
- Madam Speaker (hrs_59710882) | 4yo F | 154lb | OR - | draw 0 | jockey Freddie Gordon | trainer Nicky Henderson (14d 3/14) | headgear - | last run 28 days | form 22-3 | MARKET 33.2% | 09:00 median 2.63 | Matchbook 2.90
- It Takes Two (hrs_62645534) | 4yo F | 154lb | OR - | draw 0 | jockey Tom Bellamy | trainer Alan King (14d 1/17) | headgear - | last run 186 days | form 5-2 | MARKET 10.1% | 09:00 median 8.50 | Matchbook 9.80
- Crystalate (hrs_60722529) | 4yo F | 154lb | OR - | draw 0 | jockey Robert Dunne | trainer Olly Murphy (14d 6/36) | headgear - | last run 37 days | form 4-22 | MARKET 8.0% | 09:00 median 11.00 | Matchbook 12.50
- Celestial Flow (hrs_17395343518) | 5yo M | 154lb | OR - | draw 0 | jockey David Bass | trainer Kim Bailey & Mat Nicholls (14d 2/13) | headgear t (1st time) | last run - days | form - | MARKET 2.9% | 09:00 median 29.00 | Matchbook 42.00
- Another Vega (hrs_17394675998) | 4yo F | 154lb | OR - | draw 0 | jockey Liam Harrison | trainer Dan Skelton (14d 22/93) | headgear - | last run 14 days | form 0 | MARKET 0.8% | 09:00 median 81.00 | Matchbook 210.00
- Shadow Love (hrs_17394076273) | 4yo F | 154lb | OR - | draw 0 | jockey Charlie Todd | trainer Dan Skelton (14d 22/93) | headgear - | last run 23 days | form 8 | MARKET 0.8% | 09:00 median 101.00 | Matchbook 270.00

## 3:15 Southwell | race_id rac_32304324676 | Winter Ladies Day Saturday 28th November Handicap Hurdle Race
Hurdle | Class 5 | 1m7f182y | going Good | Turf | 11 runners | rating band 0-100 | age 3yo+
- Northwest Passage (hrs_46109371) | 4yo G | 168lb | OR 96 | draw 0 | jockey William Shanahan(5) | trainer Ivan Furtado (14d 0/7) | headgear - | last run 34 days | form 75-3 | MARKET 26.1% | 09:00 median 3.25 | Matchbook 3.55 | CHECK (skip line 3.09)
    comment: Northwest Passage was third last time out, though he's winless in his last three starts, with a fifth two starts back and a seventh the start before that.
- Promethean (hrs_37407832) | 5yo G | 163lb | OR 91 | draw 0 | jockey Jack Quinlan | trainer Sam England (14d 4/18) | headgear tp (1st time) | last run 27 days | form 83-F55 | MARKET 19.2% | 09:00 median 4.33 | Matchbook 4.90
    comment: Promethean has run over today's trip and on this going, and he returns fresh after 27 days with back-to-back fifth-place finishes, a third four starts back also in the book.
- Character Testing (hrs_35336427) | 5yo G | 171lb | OR 92 | draw 0 | jockey Jamie Hamilton | trainer Mark Walford (14d 3/17) | headgear tv | last run 10 days | form 424421 | MARKET 18.4% | 09:00 median 4.33 | Matchbook 5.40
    comment: Winner last time out and a second two starts back, Character Testing is in cracking nick after just ten days off, and he has run over today's trip and going before. The risk is the 171 lb he carries off an official mark of 92.
- Papa Oscar (hrs_49907025) | 4yo G | 152lb | OR 80 | draw 0 | jockey Dylan Johnston | trainer Clare Hobson (14d 0/4) | headgear h | last run 16 days | form P6-562 | MARKET 6.8% | 09:00 median 12.00 | Matchbook 14.50
    comment: Papa Oscar bounced back with a second last time out after sixth, fifth and sixth efforts, but he is winless in his last five and carries 152 lb off 80.
- Classical Sting (hrs_47033119) | 6yo G | 166lb | OR 94 | draw 0 | jockey Harry Reed | trainer L J Morgan (14d 0/8) | headgear h | last run 234 days | form 12P2P- | MARKET 5.8% | 09:00 median 13.00 | Matchbook 18.00
    comment: The risk is a 234-day absence and a pulled-up effort last time out, with 166 lb to carry.
- Cawthorne Banker (hrs_32264694) | 8yo G | 160lb | OR 88 | draw 0 | jockey Kevin Brogan | trainer Jonjo & A.J. O'Neill (14d 5/39) | headgear b | last run 14 days | form 110676 | MARKET 5.8% | 09:00 median 13.00 | Matchbook 18.50
    comment: On the plus side, he won five and six starts back, has run over today's trip and going, and returns after just 14 days carrying 160 lb.
- Billy Bathgate (hrs_21082873) | 10yo G | 153lb | OR 81 | draw 0 | jockey Craig Nichol | trainer Ewan Whillans (14d 0/15) | headgear - | last run 24 days | form F2P0/8 | MARKET 5.4% | 09:00 median 15.00 | Matchbook 18.00
    comment: Billy Bathgate arrives 24 days after an eighth last time out, and he is winless in his last five, with a second four starts back the one bright spot among a pulled up and a fall.
- Klapton Boy (hrs_41052172) | 6yo G | 153lb | OR 81 | draw 0 | jockey Adam Wedge | trainer Nick Kent (14d 0/6) | headgear - | last run 19 days | form P56-64 | MARKET 4.8% | 09:00 median 17.00 | Matchbook 21.00
    comment: Klapton Boy is winless in his last five, though a fourth last time out, 19 days ago, shows his form heading the right way, and he has run over today's trip and going before.
- Captain Attridge (hrs_25122167) | 8yo G | 167lb | OR 95 | draw 0 | jockey David Noonan | trainer Henry Oliver (14d 1/5) | headgear - | last run 553 days | form P42/F- | MARKET 2.9% | 09:00 median 29.00 | Matchbook 36.00
- Iolaos du Mou (hrs_30245705) | 8yo G | 162lb | OR 90 | draw 0 | jockey Tabitha Worsley | trainer Tony Culhane & Stella Barclay (14d 0/5) | headgear h | last run 14 days | form -663P9 | MARKET 2.6% | 09:00 median 33.00 | Matchbook 38.00
    comment: Winless in his last five, Iolaos du Mou was ninth last time out after being pulled up two starts back, though a third three starts back shows he can bounce back; he has run over today's trip and going, and is fresh enough after 14 days, but 162 lb is a big burden off 90.
- Razzo Italiano (hrs_28891653) | 9yo G | 156lb | OR 84 | draw 0 | jockey Jack Hogan | trainer Gary Hanmer (14d 0/5) | headgear tp | last run 45 days | form 17857/ | MARKET 2.1% | 09:00 median 41.00 | Matchbook 55.00
    comment: Razzo Italiano has been beaten in four straight since a win five starts back, finishing seventh last time out, then a fifth, an eighth and a seventh, and he returns after 45 days under 156 lb.

## 3:50 Southwell | race_id rac_32304326613 | Celebrate With Sponsorship At Southwell Racecourse Conditional Jockeys' Handicap Hurdle Race
Hurdle | Class 5 | 3m0f60y | going Good | Turf | 6 runners | rating band 0-105 | age 4yo+
- Crafty Gael (hrs_32795385) | 7yo G | 163lb | OR 99 | draw 0 | jockey Alice Stevens | trainer Lizzie Quinlan (14d 1/11) | headgear tp | last run 7 days | form -32112 | MARKET 24.6% | 09:00 median 3.50 | Matchbook 4.00 | CHECK (skip line 3.32)
    comment: Back in seven days, he has run over today's trip and going.
- Keep On Cobbling (hrs_42226289) | 6yo M | 167lb | OR 103 | draw 0 | jockey William Featherstone(3) | trainer Henry Daly (14d 1/13) | headgear - | last run 174 days | form 1632-3 | MARKET 22.2% | 09:00 median 3.88 | Matchbook 4.40
    comment: Placed in each of her last three runs, a third last time out, a second two starts back and a third three starts back, Keep On Cobbling has run over today's trip and going before. The risk is a 174-day absence, and she also carries 167 lb.
- Iamcelestialgift (hrs_51523927) | 8yo G | 143lb | OR 79 | draw 0 | jockey Nick Slatter | trainer David Killahena & Graeme McPherson (14d 5/10) | headgear tp (1st time) | wind surgery | last run 70 days | form P-6969 | MARKET 16.1% | 09:00 median 5.50 | Matchbook 6.00
    comment: The risk is a 70-day absence after a ninth last time out.
- The Clonmel Kid (hrs_38203088) | 7yo G | 163lb | OR 99 | draw 0 | jockey Beau Morgan | trainer Philip Kirby (14d 1/14) | headgear p | last run 48 days | form 336742 | MARKET 15.9% | 09:00 median 5.50 | Matchbook 6.20
    comment: The risk is 163 lb on his back after 48 days off, and he is yet to win in his last six starts.
- Luminaries (hrs_32046462) | 9yo G | 146lb | OR 82 | draw 0 | jockey Ellis Collier | trainer Ewan Whillans (14d 0/15) | headgear tb | last run 10 days | form 721122 | MARKET 11.6% | 09:00 median 7.50 | Matchbook 8.40
    comment: Luminaries has finished second in each of his last two starts and was a winner three and four starts back, so the form reads well, and he's fresh from a run ten days ago, having been over this trip and going before.
- Muskerry Rock (hrs_34253800) | 7yo G | 168lb | OR 104 | draw 0 | jockey James Murray(10) | trainer Mickey Bowen (14d 3/14) | headgear p | last run 20 days | form 21P344 | MARKET 9.6% | 09:00 median 9.00 | Matchbook 10.50
    comment: Muskerry Rock arrives fit after 20 days, having finished a fourth last time out, a fourth two starts back, and a third three starts back, and he has run over today's trip and going before.
