# Card review packet: Uttoxeter, 2026-11-14

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
{"meeting": "uttoxeter", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 12:07 Uttoxeter | race_id rac_32304440896 | QuinnBet Conditional Jockeys' Handicap Hurdle Race
Hurdle | Class 5 | 2m3f207y | going Good | Turf | 8 runners | rating band 0-105 | age 3yo+
- Spartan Times (hrs_40591908) | 5yo G | 168lb | OR 105 | draw 0 | jockey Luke Scott(3) | trainer Jennie Candlish (14d 2/8) | headgear - | last run 46 days | form 17-145 | MARKET 20.3% | 09:00 median 4.33 | Matchbook 4.60 | CHECK (skip line 4.11)
    comment: Twice a winner in his last five starts, including three starts back, Spartan Times has run over today's going and comes off a fifth last time out and a fourth before that; the main risk is a 46-day break and 168 lb on his back.
- Mooserwirt (hrs_49973938) | 6yo G | 153lb | OR 90 | draw 0 | jockey Ben Smith(6) | trainer Oliver Greenall & Josh Guerriero (14d 0/16) | headgear t | last run 238 days | form 60743- | MARKET 20.3% | 09:00 median 4.33 | Matchbook 4.70
    comment: Mooserwirt was third last time out and a fourth two starts back, and he has run over today's trip and going before, but he is winless in recent starts and returns after 238 days off.
- Tao Enki (hrs_40959842) | 6yo G | 166lb | OR 103 | draw 0 | jockey Jay Tidball | trainer Alastair Ralph (14d 0/4) | headgear p | last run 28 days | form 57-263 | MARKET 16.4% | 09:00 median 5.50 | Matchbook 5.70
    comment: Winless in his last five, though, and 166 lb is the main risk.
- Zeus Forlonge (hrs_65161621) | 4yo G | 166lb | OR 104 | draw 0 | jockey Lewis Stones | trainer Olly Murphy (14d 8/41) | headgear t (1st time) | last run 172 days | form 0-62 | MARKET 12.9% | 09:00 median 5.50 | Matchbook 9.00
    comment: Unexposed gelding who finished second last time out, after a sixth two starts back, and he is yet to win in his last three outings. He returns after 172 days off and carries 166 lb, so there should be more to come.
- Lunar Orbit (hrs_44975553) | 4yo G | 167lb | OR 105 | draw 0 | jockey Billy Marshall(7) | trainer Dan Skelton (14d 19/92) | headgear ht | last run 19 days | form 15-2P2 | MARKET 12.4% | 09:00 median 7.00 | Matchbook 7.80
    comment: Lunar Orbit signals his well-being with a second last time out just 19 days ago, and he has run over today's trip and on this going before.
- Getaway With You (hrs_29552600) | 8yo G | 153lb | OR 90 | draw 0 | jockey Nick Slatter | trainer David Killahena & Graeme McPherson (14d 6/11) | headgear tp | last run 24 days | form 5-7772 | MARKET 9.7% | 09:00 median 9.00 | Matchbook 10.00
    comment: Winless in his last five, Getaway With You is hard to fancy after three straight seventh-place finishes, though a second last time out, 24 days ago, offers some hope.
- Rumi Rock (hrs_49578137) | 5yo G | 168lb | OR 105 | draw 0 | jockey Shane Fenelon | trainer Gary Hanmer (14d 0/6) | headgear - | last run 96 days | form 6-0603 | MARKET 4.2% | 09:00 median 22.00 | Matchbook 24.00
    comment: Winless in his last five and absent for 96 days, Rumi Rock is hard to fancy, though a third last time out is a glimmer and he has run on today's going before.
- Back In The Bay (hrs_35336049) | 7yo M | 164lb | OR 101 | draw 0 | jockey Finn Lambert | trainer James Owen (14d 10/42) | headgear p | wind surgery | last run 17 days | form 752P44 | MARKET 3.8% | 09:00 median 23.00 | Matchbook 27.00
    comment: Back In The Bay arrives in solid fettle with consecutive fourths, a second four starts back, and a fresh 17-day gap since her last run, while she has run over today's trip and going before.

## 12:42 Uttoxeter | race_id rac_32304433148 | Somersby Novices' Hurdle Race (GBB Race)
Hurdle | Class 4 | 1m7f168y | going Good | Turf | 8 runners | rating band - | age 4yo+
- Spanish Darling (hrs_17390767877) | 5yo G | 161lb | OR 128 | draw 0 | jockey Kielan Woods | trainer Alex Hales (14d 0/10) | headgear t | last run 22 days | form -13114 | MARKET 73.6% | 09:00 median 1.14 | Matchbook 1.20
- Made For Mary (hrs_17395300755) | 4yo F | 147lb | OR - | draw 0 | jockey Jack Hogan | trainer Jonjo & A.J. O'Neill (14d 5/38) | headgear - | last run - days | form - | MARKET 5.9% | 09:00 median 10.50 | Matchbook 21.00
- Port Isaac (hrs_61718272) | 4yo G | 154lb | OR - | draw 0 | jockey Robert Dunne | trainer Toby Bulgin (14d 0/1) | headgear - | last run 21 days | form 1-9 | MARKET 5.5% | 09:00 median 10.00 | Matchbook 26.00
- Montevallo (hrs_17395280938) | 5yo G | 154lb | OR - | draw 0 | jockey Toby Wynne | trainer Oliver Greenall & Josh Guerriero (14d 0/16) | headgear - | last run 266 days | form 42- | MARKET 5.3% | 09:00 median 11.00 | Matchbook 27.00
- Carrigane (hrs_61276621) | 6yo G | 154lb | OR - | draw 0 | jockey Finn Lambert(3) | trainer Tom Ellis (14d 2/21) | headgear - | last run 102 days | form 43-248 | MARKET 3.8% | 09:00 median 17.00 | Matchbook 34.00
- Rose Warrior (hrs_51491454) | 4yo G | 154lb | OR - | draw 0 | jockey Luke Scott(3) | trainer Jennie Candlish (14d 2/8) | headgear p | last run 41 days | form 844 | MARKET 3.7% | 09:00 median 17.00 | Matchbook 36.00
- Ocean View (hrs_17394794900) | 4yo G | 154lb | OR - | draw 0 | jockey Jack Andrews | trainer Tom Ellis (14d 2/21) | headgear - | last run 12 days | form 2-1P | MARKET 1.3% | 09:00 median 51.00 | Matchbook 160.00
- Avatar Jet (hrs_36387323) | 5yo G | 154lb | OR - | draw 0 | jockey Nathan Moscrop | trainer Declan Carroll (14d 0/7) | headgear - | last run 7 days | form P | MARKET 0.8% | 09:00 median 101.00 | Matchbook 220.00

## 1:15 Uttoxeter | race_id rac_32304435085 | Carlsberg EBF Mares' 'National Hunt' Maiden Hurdle Race (EBF Mares' NH Novices' Hurdle Series Qualifier) (GBB Race)
Hurdle | Class 4 | 2m3f207y | going Good | Turf | 7 runners | rating band - | age 4-6yo
- Boombox (hrs_50433243) | 5yo M | 158lb | OR - | draw 0 | jockey Harry Reed | trainer Harry Derham (14d 4/19) | headgear - | last run 24 days | form 223-22 | MARKET 40.1% | 09:00 median 2.20 | Matchbook 2.30
- Malina Road (hrs_49577815) | 6yo M | 158lb | OR - | draw 0 | jockey Jack Hogan | trainer Fergal O'Brien (14d 3/28) | headgear - | last run 259 days | form 1/113- | MARKET 29.7% | 09:00 median 2.88 | Matchbook 3.30
- Port And Brandy (hrs_49974358) | 6yo M | 158lb | OR - | draw 0 | jockey Shane Fenelon(5) | trainer Mickey Bowen (14d 4/15) | headgear - | last run 174 days | form 1232-2 | MARKET 17.2% | 09:00 median 5.00 | Matchbook 5.50
- Kentford Legacy (hrs_64968057) | 5yo M | 158lb | OR - | draw 0 | jockey Daniel Sansom(3) | trainer Seamus Mullins (14d 3/11) | headgear - | last run 174 days | form 1 | MARKET 5.7% | 09:00 median 13.00 | Matchbook 19.50
- Millady (hrs_59862516) | 4yo F | 157lb | OR 102 | draw 0 | jockey Charlie Deutsch | trainer Mel Rowley (14d 1/11) | headgear - | last run 213 days | form 60535- | MARKET 2.9% | 09:00 median 30.50 | Matchbook 36.00
- Crystal Connemara (hrs_59710819) | 4yo F | 157lb | OR - | draw 0 | jockey David Bass | trainer Max Comley (14d 3/12) | headgear - | last run 29 days | form 32-4 | MARKET 2.6% | 09:00 median 29.00 | Matchbook 46.00
- Britway Belle (hrs_51341570) | 5yo M | 158lb | OR - | draw 0 | jockey Kielan Woods | trainer Henry Oliver (14d 0/6) | headgear - | wind surgery | last run 174 days | form 1733-5 | MARKET 1.8% | 09:00 median 51.00 | Matchbook 65.00

## 1:50 Uttoxeter | race_id rac_32304437022 | Karina's 60th Birthday Celebration Novices' Limited Handicap Hurdle Race
Hurdle | Class 5 | 1m7f168y | going Good | Turf | 12 runners | rating band 0-95 | age 3yo+
- Arcon (hrs_36837360) | 6yo G | 161lb | OR 89 | draw 0 | jockey Mr Jamie Neild(5) | trainer Jennie Candlish (14d 2/8) | headgear v (1st time) | last run 41 days | form 3-6676 | MARKET 23.7% | 09:00 median 3.25 | Matchbook 4.10 | CHECK (skip line 3.09)
    comment: Arcon is winless in his last five, finishing sixth last time out and sixth again four starts back, with a third five starts back his only podium finish, so he is hard to fancy.
- Chambers (hrs_45661714) | 4yo G | 152lb | OR 80 | draw 0 | jockey J. P. O'Neill(10) | trainer Faye Bramley (14d 0/14) | headgear - | last run 16 days | form 667 | MARKET 17.4% | 09:00 median 4.33 | Matchbook 5.60
    comment: Chambers is winless in his last three, finishing seventh last time out after a sixth two starts back and another sixth before that, so he is hard to fancy. A quick 16-day turnaround and previous experience on today's going help, but 152 lb off an official mark of 80 is a stiff ask.
- Savanna Storm (hrs_64360870) | 4yo G | 162lb | OR 90 | draw 0 | jockey Stan Sheppard | trainer Tom Lacey (14d 4/12) | headgear - | last run 47 days | form 74874 | MARKET 13.0% | 09:00 median 6.50 | Matchbook 7.00
- Josh Central (hrs_51124885) | 5yo G | 158lb | OR 86 | draw 0 | jockey Kielan Woods | trainer Tom George (14d 2/6) | headgear - | last run 229 days | form 7/706- | MARKET 12.0% | 09:00 median 7.00 | Matchbook 7.60
    comment: Josh Central has finished sixth, unplaced, seventh and seventh in his last four starts, and returns after 229 days off, which raises fitness doubts.
- Stone Cold (hrs_51831899) | 5yo G | 166lb | OR 94 | draw 0 | jockey Ned Fox(3) | trainer Matt Sheppard (14d 1/4) | headgear t | last run 251 days | form 56068- | MARKET 6.7% | 09:00 median 12.00 | Matchbook 14.50
    comment: The risk is a 251-day absence, and he is yet to win in his last five, including an eighth last time out.
- Pink 'n Purple (hrs_58534791) | 4yo G | 166lb | OR 94 | draw 0 | jockey Daniel Sansom(3) | trainer Seamus Mullins (14d 3/11) | headgear - | last run 27 days | form 553-45 | MARKET 5.6% | 09:00 median 13.00 | Matchbook 19.00
    comment: Pink 'n Purple is yet to win in his last five, but he's been consistent, with a third three starts back and a fourth two runs ago, and he returns fresh after 27 days having run over today's trip and going.
- Both of Us (hrs_53181632) | 4yo G | 165lb | OR 93 | draw 0 | jockey Conor O'Farrell | trainer Kerry Lee (14d 0/5) | headgear t | last run 136 days | form 433-47 | MARKET 4.9% | 09:00 median 15.00 | Matchbook 22.00
    comment: He has run over today's trip and going, yet 165 lb looks a lot to carry off 93.
- Moi Mon Vieux (hrs_64621466) | 4yo G | 152lb | OR 80 | draw 0 | jockey James Best | trainer Richard Hobson (14d 0/3) | headgear t | last run 30 days | form 2446 | MARKET 4.3% | 09:00 median 15.00 | Matchbook 27.00
    comment: Moi Mon Vieux is yet to win in his last four starts, but a sixth last time out follows a fourth two starts back and another fourth three starts back, and he has run over today's trip and going. Carrying 152 lb off an official mark of 80 after 30 days off, he looks capable of a bold show without being a banker.
- Prince Phil (hrs_59491796) | 5yo G | 155lb | OR 83 | draw 0 | jockey Robert Dunne | trainer Sam England (14d 6/20) | headgear h | last run 206 days | form 5P07- | MARKET 3.7% | 09:00 median 19.00 | Matchbook 29.00
    comment: Prince Phil is winless in his last four and returns after 206 days off, but he has run over today's trip, carries 155 lb off an official 83, and arrives with a yard in form at 6/20 over the last fortnight.
- Lady Blackmore (hrs_57470021) | 5yo M | 151lb | OR 79 | draw 0 | jockey Jack Hogan | trainer Alastair Ralph (14d 0/4) | headgear h | last run 34 days | form 5567-P | MARKET 3.4% | 09:00 median 23.00 | Matchbook 30.00
    comment: Lady Blackmore is hard to fancy after being pulled up last time out, with a seventh two starts back and a sixth before that, and she is yet to win in her last five starts.
- Famous Shoes (hrs_44786000) | 5yo G | 152lb | OR 80 | draw 0 | jockey Harriet Tucker(7) | trainer Neil Mulholland (14d 7/28) | headgear - | last run 38 days | form FPU5-P | MARKET 3.0% | 09:00 median 23.00 | Matchbook 36.00
    comment: Famous Shoes is hard to fancy, pulled up last time and without a completed finish bar a fifth two starts back in his last five outings, with a fall and an unseated rider in that run too. He has run over today's trip and going and has had 38 days off, but 152 lb is a big ask.
- Bargain Hunter (hrs_49974505) | 5yo G | 145lb | OR 72 | draw 0 | jockey Nick Slatter(3) | trainer D. J. Jeffreys (14d 0/4) | headgear - | last run 148 days | form 7890-P | MARKET 2.3% | 09:00 median 34.00 | Matchbook 46.00
    comment: Bargain Hunter has been pulled up last time out and is winless in his last five, but a 148-day break and a mark of 72 offer hope, and he has run over today's trip.

## 2:25 Uttoxeter | race_id rac_32304438959 | Eaton Hall Shooting Ground Mares' Handicap Steeple Chase (GBB Race)
Chase | Class 4 | 1m7f214y | going Good | Turf | 4 runners | rating band 0-120 | age 4yo+
- Pismo Beach (hrs_39959591) | 6yo M | 156lb | OR 114 | draw 0 | jockey Charlie Hammond | trainer Stuart Edmunds (14d 2/11) | headgear - | wind surgery | last run 238 days | form 543P2- | MARKET 29.8% | 09:00 median 3.00 | Matchbook 3.25
    comment: The risk is a 238-day absence, plus 156 lb and a pulled up two starts back.
- Irish Chorus (hrs_34456513) | 7yo M | 158lb | OR 116 | draw 0 | jockey Kielan Woods | trainer Alan King (14d 1/18) | headgear - | last run 13 days | form 211-26 | MARKET 26.5% | 09:00 median 3.50 | Matchbook 3.60
    comment: Irish Chorus won two starts in a row three and four starts back, then was second, before a sixth last time out, and she's fresh enough after 13 days. She has run over today's trip and going, but 158 lb is a hefty burden and the main risk.
- Lau And Shaz (hrs_40553835) | 6yo M | 161lb | OR 119 | draw 0 | jockey Charlie Deutsch | trainer Kayley Woollacott (14d 0/7) | headgear - | last run 219 days | form 61F13- | MARKET 22.1% | 09:00 median 3.75 | Matchbook 4.80
    comment: The one concern is a 219-day absence, with 161 lb to carry.
- Lady Tadita (hrs_46914119) | 5yo M | 159lb | OR 117 | draw 0 | jockey Conor O'Farrell | trainer Jamie Snowden (14d 11/26) | headgear - | last run 29 days | form 1126-3 | MARKET 21.6% | 09:00 median 4.00 | Matchbook 4.70
    comment: Trainer is in cracking form at 11 from 26 in the last 14 days, though a sixth two starts back and 159 lb are minor reservations.

## 3:00 Uttoxeter | race_id rac_32304442833 | Hobgoblin Handicap Steeple Chase (GBB Race)
Chase | Class 4 | 3m0f10y | going Good | Turf | 8 runners | rating band 0-120 | age 4yo+
- Seven Kites (hrs_62393849) | 4yo G | 148lb | OR 110 | draw 0 | jockey Stan Sheppard | trainer Tom Lacey (14d 4/12) | headgear v | last run 15 days | form 12-42 | MARKET 21.5% | 09:00 median 4.00 | Matchbook 4.40 | CHECK (skip line 3.80)
    comment: Seven Kites has been running well, second last time out and a winner four starts back, but he is fairly fit after 15 days and has run over today's trip and going before.
- Torrent (hrs_36970423) | 5yo G | 156lb | OR 108 | draw 0 | jockey Charlie Deutsch | trainer Nigel Hawke (14d 0/5) | headgear p | last run 35 days | form 453332 | MARKET 19.3% | 09:00 median 4.34 | Matchbook 5.00
    comment: Torrent has been consistent, finishing second last time out, with a third two starts back and another third three starts back, and he has run over today's trip and going before.
- Orderoftheday (hrs_40352578) | 6yo G | 167lb | OR 119 | draw 0 | jockey Robert Dunne | trainer Olly Murphy (14d 8/41) | headgear - | last run 30 days | form 343-15 | MARKET 18.7% | 09:00 median 4.50 | Matchbook 5.20
    comment: Orderoftheday arrives fresh from a 30-day break with a win two starts back and a third three starts back, so his recent form is solid, and he has run over today's trip and going before.
- Kalhandrion (hrs_40766698) | 6yo G | 159lb | OR 111 | draw 0 | jockey James Best | trainer Richard Hobson (14d 0/3) | headgear t | last run 242 days | form 32U13- | MARKET 10.7% | 09:00 median 7.50 | Matchbook 9.60
- Stone's Throw (hrs_39040330) | 6yo G | 167lb | OR 119 | draw 0 | jockey Kielan Woods | trainer Billy Aprahamian (14d 0/7) | headgear - | last run 246 days | form P1174- | MARKET 9.8% | 09:00 median 9.00 | Matchbook 9.40
    comment: The main risk is a 246-day absence, with a fourth last time out his latest effort.
- Kahavari (hrs_45630025) | 6yo G | 165lb | OR 117 | draw 0 | jockey Toby Wynne | trainer Oliver Greenall & Josh Guerriero (14d 0/16) | headgear t | last run 14 days | form 5221-6 | MARKET 8.3% | 09:00 median 9.00 | Matchbook 13.50
    comment: Kahavari showed his hand with a win two starts back and a second three starts back, and he has run over today's trip and on this going, returning fresh after 14 days. The main risk is a sixth last time out, while 165 lb is a stiff ask.
- Warriors Destiny (hrs_40095902) | 6yo G | 168lb | OR 120 | draw 0 | jockey Jack Hogan | trainer Fergal O'Brien (14d 3/28) | headgear - | last run 245 days | form 54310- | MARKET 8.0% | 09:00 median 11.00 | Matchbook 12.00
    comment: Warriors Destiny won two starts back and was third three starts back, but he was unplaced last time out and returns after 245 days off, so fitness is a question.
- Shy Love (hrs_34361467) | 8yo G | 160lb | OR 112 | draw 0 | jockey David Bass | trainer Fergal O'Brien (14d 3/28) | headgear - | last run 702 days | form 51547/ | MARKET 3.8% | 09:00 median 23.00 | Matchbook 27.00
    comment: Hard to fancy after a 702-day absence, with a seventh last time out and a fifth, a fourth and a seventh in three of his last four runs. He has won once in his last five and has run on today's going, but 160 lb is a big ask.

## 3:35 Uttoxeter | race_id rac_32304444770 | 1664 Biere Open National Hunt Flat Race (Category 1 Elimination) (GBB Race)
NH Flat | Class 5 | 1m7f168y | going Good | Turf | 12 runners | rating band - | age 4-5yo
- Ma Wang des Bois (hrs_58565521) | 5yo G | 156lb | OR - | draw 0 | jockey Jack Hogan | trainer Emma Lavelle (14d 2/15) | headgear - | last run 266 days | form 25- | MARKET 27.2% | 09:00 median 3.00 | Matchbook 3.45 | CHECK (skip line 2.85)
- Hannah's Kitchen (hrs_17395339346) | 4yo G | 156lb | OR - | draw 0 | jockey Robert Dunne | trainer Olly Murphy (14d 8/41) | headgear - | last run - days | form - | MARKET 14.7% | 09:00 median 5.00 | Matchbook 7.40
    comment: Hannah's Kitchen is unexposed on his debut, with no form to go on, so he's open to improvement. He carries 156 lb, and any progress will have to be judged from what he shows on the day.
- Lady Coco (hrs_64967896) | 4yo F | 156lb | OR - | draw 0 | jockey David Bass | trainer Henry Daly (14d 1/13) | headgear - | last run 175 days | form 1 | MARKET 13.1% | 09:00 median 6.50 | Matchbook 7.00
    comment: Lady Coco won last time out and has run over today's trip and going before, a tidy profile for a filly carrying 156 lb. The one risk is a 175-day absence, so fitness after the break is the question.
- Bateleur (hrs_17393905221) | 4yo G | 156lb | OR - | draw 0 | jockey Charlie Price | trainer Oliver Signy (14d 0/5) | headgear - | last run 27 days | form 1-2 | MARKET 11.3% | 09:00 median 7.00 | Matchbook 8.60
    comment: He has run over today's trip and on this going, though he carries 156 lb.
- Jimmy Gatz (hrs_61277216) | 4yo G | 156lb | OR - | draw 0 | jockey H. J. Horgan | trainer Olly Murphy (14d 8/41) | headgear - | last run 258 days | form 43- | MARKET 8.2% | 09:00 median 10.00 | Matchbook 11.50
- Menasha (hrs_17395109886) | 4yo G | 156lb | OR - | draw 0 | jockey Kielan Woods | trainer Henry Oliver (14d 0/6) | headgear - | last run 209 days | form 2- | MARKET 6.9% | 09:00 median 12.00 | Matchbook 13.50
    comment: Menasha filled the runner-up spot on his latest outing, yet he returns after a 209-day break and is yet to win in his sole recent start. Unexposed and open to improvement, the gelding shoulders 156 lb on his comeback.
- Miretix du Moulin (hrs_17395413399) | 4yo G | 156lb | OR - | draw 0 | jockey Mr Hugo Hunt(7) | trainer Richard Hobson (14d 0/3) | headgear - | last run - days | form - | MARKET 6.0% | 09:00 median 13.50 | Matchbook 16.00
    comment: Miretix du Moulin is totally unexposed, with no recorded form to go on, so this gelding's debut is a step into the unknown. He carries 156 lb, and with so little to judge him on there should be improvement to come.
- Brave Bard (hrs_63202727) | 4yo G | 156lb | OR - | draw 0 | jockey Stan Sheppard | trainer Ben Case (14d 1/8) | headgear t (1st time) | last run - days | form - | MARKET 5.1% | 09:00 median 17.00 | Matchbook 17.50
    comment: Brave Bard is an unexposed debutant with no form to go on, so he's open to improvement from the outset, and he shoulders 156 lb on that first appearance. He's yet to win, and there's little to judge him on beyond that.
- Weafers Cross (hrs_17395416528) | 4yo G | 156lb | OR - | draw 0 | jockey Charlie Hammond | trainer Laura Horsfall (14d 0/6) | headgear - | last run 189 days | form 2 | MARKET 3.2% | 09:00 median 26.00 | Matchbook 32.00
    comment: Unexposed gelding who finished second on his only recent start, though he returns after 189 days off and shouldn't be judged on so little. He carries 156 lb, and with plenty of scope for improvement he is yet to win in recent form.
- Chasing Honors (hrs_17394103391) | 4yo G | 156lb | OR - | draw 0 | jockey Charlie Deutsch | trainer Mel Rowley (14d 1/11) | headgear - | last run - days | form - | MARKET 3.0% | 09:00 median 26.00 | Matchbook 38.00
    comment: He carries 156 lb on debut, and with no form to lean on he is very much one to learn about.
- Bands of Courage (hrs_17395412356) | 5yo G | 156lb | OR - | draw 0 | jockey Callum Bewley | trainer John Norton (14d 0/0) | headgear t (1st time) | last run 190 days | form 4-P | MARKET 0.7% | 09:00 median 126.00 | Matchbook 260.00
    comment: Lightly raced and unexposed, Bands of Courage pulled up last time out and was a fourth two starts back, so there's scope for improvement. He returns after 190 days off and is yet to win in his last two starts, carrying 156 lb.
- Pdq Workspace (hrs_17395414442) | 5yo G | 156lb | OR - | draw 0 | jockey James Best | trainer Sarah Hollinshead (14d 0/1) | headgear - | last run - days | form - | MARKET 0.6% | 09:00 median 101.00 | Matchbook 260.00
    comment: Unraced and open to improvement, this gelding makes his debut with no form to assess, so he's an unexposed type who could have plenty to offer. He carries 156 lb.
