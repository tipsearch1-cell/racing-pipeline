# Card review packet: Hereford, 2026-11-12

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
{"meeting": "hereford", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 12:30 Hereford | race_id rac_32304223952 | CopyBet Back Again At Hereford Fillies' Juvenile Hurdle Race (GBB Race)
Hurdle | Class 4 | 2m0f53y | going Good | Turf | 3 runners | rating band - | age 3yo
- Koala Rose (hrs_59367301) | 3yo F | 154lb | OR - | draw 0 | jockey Tristan Durrell | trainer Dan Skelton (14d 21/93) | headgear - | last run 47 days | form - | MARKET 53.3% | 09:00 median 1.70 | Matchbook 1.86
    comment: Koala Rose is unexposed, with no recorded form to go on, so she is open to improvement. She returns after 47 days off and carries 154 lb, and her profile is a blank page.
- Princess of Habo (hrs_17395296583) | 3yo F | 154lb | OR - | draw 0 | jockey Gavin Sheehan | trainer Jamie Snowden (14d 11/26) | headgear - | last run 116 days | form - | MARKET 42.0% | 09:00 median 2.25 | Matchbook 2.30
    comment: Unexposed filly with no recorded form to lean on, so she's open to improvement, and she returns after 116 days off. Carries 154 lb, while the yard is flying with 11 winners from 26 in the last fortnight.
- Antiquarian (hrs_58033731) | 3yo F | 154lb | OR - | draw 0 | jockey Caoilin Quinn | trainer Jamie Moore & Josh Moore (14d 6/27) | headgear - | last run 40 days | form 4 | MARKET 4.7% | 09:00 median 19.00 | Matchbook 22.00
    comment: Lightly raced and unexposed, Antiquarian was fourth last time out and returns after 40 days off, so she may have more to offer. She is winless in her last start but carries 154 lb, with limited form leaving room for improvement.

## 1:05 Hereford | race_id rac_32304225889 | Paul Fergusons Jumpers To Follow EBF 'National Hunt' Novices' Hurdle Race (Qualifier) (GBB Race)
Hurdle | Class 4 | 2m0f53y | going Good | Turf | 12 runners | rating band - | age 4-6yo
- Governors Rock (hrs_54304502) | 5yo G | 160lb | OR - | draw 0 | jockey Caoilin Quinn | trainer Warren Greatrex (14d 2/18) | headgear h (1st time) | last run 20 days | form 100-19 | MARKET 52.1% | 09:00 median 1.62 | Matchbook 1.70
- Moscow Star (hrs_60250064) | 4yo G | 154lb | OR - | draw 0 | jockey Gavin Sheehan | trainer Oliver Signy (14d 0/4) | headgear t | last run 25 days | form 554-02 | MARKET 23.4% | 09:00 median 3.25 | Matchbook 4.10
- Thetype Istitle (hrs_61911752) | 4yo F | 147lb | OR - | draw 0 | jockey Stan Sheppard | trainer Tom Lacey (14d 4/15) | headgear t | last run 53 days | form -21793 | MARKET 8.9% | 09:00 median 8.00 | Matchbook 12.00
- Jaunty Trooper (hrs_65974657) | 5yo G | 154lb | OR - | draw 0 | jockey Conor Ring | trainer Mrs C. Williams (14d 2/23) | headgear - | last run 63 days | form U62 | MARKET 8.2% | 09:00 median 7.25 | Matchbook 15.50
- Robin Blue Breast (hrs_50965586) | 6yo M | 147lb | OR - | draw 0 | jockey Bryan Carver | trainer Joe Ponting (14d 0/0) | headgear - | last run 547 days | form 52/4- | MARKET 2.1% | 09:00 median 26.00 | Matchbook 65.00
- Unbelievable Jeff (hrs_17394597773) | 4yo G | 154lb | OR - | draw 0 | jockey Harry Kimber | trainer Faye Bramley (14d 0/14) | headgear - | last run 14 days | form 8 | MARKET 1.3% | 09:00 median 51.00 | Matchbook 120.00
- Dressed Overall (hrs_17394593601) | 4yo G | 154lb | OR - | draw 0 | jockey Beau Morgan(5) | trainer Faye Bramley (14d 0/14) | headgear - | last run 14 days | form 7 | MARKET 1.1% | 09:00 median 81.00 | Matchbook 130.00
- Valenciaga (hrs_55882407) | 5yo G | 154lb | OR - | draw 0 | jockey Callum Pritchard | trainer Sheila Lewis (14d 0/5) | headgear - | last run 17 days | form 4279-5 | MARKET 1.1% | 09:00 median 67.00 | Matchbook 95.00
- Bonnie Lazarevic (hrs_63875413) | 4yo F | 147lb | OR - | draw 0 | jockey Sean Houlihan | trainer Sheila Lewis (14d 0/5) | headgear - | last run 17 days | form 7P | MARKET 0.6% | 09:00 median 126.00 | Matchbook 280.00
- Sir Vinnie Kent (hrs_17392197830) | 4yo G | 154lb | OR - | draw 0 | jockey James Best | trainer Sarah-Jayne Davies (14d 0/3) | headgear - | last run 48 days | form PP | MARKET 0.4% | 09:00 median 201.00 | Matchbook 350.00
- Maria's Joy (hrs_46547193) | 5yo M | 147lb | OR - | draw 0 | jockey Joe Anderson(3) | trainer Grace Harris (14d 2/7) | headgear - | last run 14 days | form 0/7-9 | MARKET 0.4% | 09:00 median 201.00 | Matchbook 380.00
- Jersey Tex (hrs_61910660) | 4yo G | 154lb | OR - | draw 0 | jockey Ned Fox(3) | trainer Matt Sheppard (14d 1/4) | headgear - | last run 14 days | form 8P-7 | MARKET 0.3% | 09:00 median 201.00 | Matchbook 330.00

## 1:40 Hereford | race_id rac_32304227826 | CopyBet For Nations League Profit Boosts Handicap Hurdle Race
Hurdle | Class 4 | 2m5f163y | going Good | Turf | 7 runners | rating band 0-110 | age 4yo+
- Mr Jukebox (hrs_51273327) | 5yo G | 167lb | OR 109 | draw 0 | jockey Caoilin Quinn | trainer Warren Greatrex (14d 2/18) | headgear - | last run 202 days | form 53812- | MARKET 25.5% | 09:00 median 3.50 | Matchbook 3.75 | CHECK (skip line 3.32)
    comment: The main risk is a 202-day absence, plus 167 lb on his back.
- Lydeard Girl (hrs_48953128) | 5yo M | 153lb | OR 95 | draw 0 | jockey Callum Pritchard | trainer Kayley Woollacott (14d 0/5) | headgear - | last run 225 days | form 642U2- | MARKET 15.0% | 09:00 median 6.00 | Matchbook 6.40
    comment: Winless in her last five, Lydeard Girl was second last time out, but that came 225 days ago and she has an unseated and a sixth in the book too.
- Windsor Blue (hrs_51678963) | 5yo M | 164lb | OR 106 | draw 0 | jockey David Bass | trainer Henry Daly (14d 1/10) | headgear - | last run 204 days | form 54152- | MARKET 13.2% | 09:00 median 6.50 | Matchbook 7.40
- Lightning Flash (hrs_37686894) | 6yo G | 168lb | OR 110 | draw 0 | jockey Mr Eddie Edge(7) | trainer Nigel & Willy Twiston-Davies (14d 5/31) | headgear - | last run 18 days | form 63-341 | MARKET 12.9% | 09:00 median 6.50 | Matchbook 7.80
    comment: He has run on today's going before and carries 168 lb off an official mark of 110, which is the one reservation.
- Dublinofficecallin (hrs_52896921) | 5yo G | 147lb | OR 89 | draw 0 | jockey Tom Cannon | trainer Kerry Lee (14d 0/4) | headgear - | last run 149 days | form 071-70 | MARKET 12.9% | 09:00 median 7.00 | Matchbook 7.40
    comment: Dublinofficecallin has been well beaten recently, unplaced last time out and a seventh two starts back, and he returns after 149 days off, so he is hard to fancy under 147 lb. On the plus side, he won three starts back and has run on today's going before.
- Person of Interest (hrs_40095713) | 6yo G | 158lb | OR 100 | draw 0 | jockey J. P. O'Neill(10) | trainer Faye Bramley (14d 0/14) | headgear - | last run 65 days | form B612P5 | MARKET 12.0% | 09:00 median 7.50 | Matchbook 8.00
    comment: Fifth last time out, and a winner four starts back, Person of Interest has shown enough to sit mid-pack, and he has run over today's trip and going before.
- City of Diamonds (hrs_39826850) | 6yo G | 163lb | OR 105 | draw 0 | jockey Ned Fox(3) | trainer Clive Boultbee-Brooks (14d 0/5) | headgear - | last run 34 days | form 600-70 | MARKET 8.5% | 09:00 median 9.00 | Matchbook 13.00
    comment: The main risk is a winless recent spell, with nothing better than a sixth five starts back.

## 2:15 Hereford | race_id rac_32304229763 | CopyBet BOG Now For Cheltenham Tomorrow Novices' Handicap Hurdle Race (GBB Race)
Hurdle | Class 4 | 3m1f119y | going Good | Turf | 5 runners | rating band 0-110 | age 4yo+
- Oneinthewell (hrs_50036350) | 5yo G | 168lb | OR 109 | draw 0 | jockey Jonathan Burke | trainer James Owen (14d 13/47) | headgear p | last run 48 days | form -22143 | MARKET 42.6% | 09:00 median 2.20 | Matchbook 2.22
    comment: Oneinthewell arrives consistent, with a third last time out, a fourth two starts back and a win three starts back, and he has run over today's trip and going.
- Alan Bresil (hrs_50622481) | 6yo G | 152lb | OR 93 | draw 0 | jockey Nathan Andrews(10) | trainer Nick Scholfield (14d 0/18) | headgear b | last run 11 days | form 254633 | MARKET 25.9% | 09:00 median 3.25 | Matchbook 3.95
    comment: Alan Bresil comes here sharp after a third last time out, and a third two starts back, with just 11 days since that run; he has run over today's trip and going, and our 96 puts him third of five.
- Elated (hrs_58843974) | 5yo M | 158lb | OR 99 | draw 0 | jockey Charlie Price | trainer Robbie Llewellyn (14d 1/2) | headgear - | last run 47 days | form 332F22 | MARKET 13.6% | 09:00 median 6.00 | Matchbook 7.80
    comment: Elated has been runner-up in her last two starts and placed in five of her last six, so she arrives in fine heart despite being winless, and she has run on today's going before. The one concern is 158 lb on a 47-day break, which is a hefty burden.
- Lord Cauvelliere (hrs_51800336) | 5yo G | 142lb | OR 78 | draw 0 | jockey Callum Pritchard | trainer Sheila Lewis (14d 0/5) | headgear t (1st time) | last run 17 days | form 456P74 | MARKET 12.7% | 09:00 median 7.50 | Matchbook 7.60
    comment: The main risk is that he's winless in his last six, with a pulled up three starts back.
- Wishful Wings (hrs_52709356) | 5yo M | 142lb | OR 74 | draw 0 | jockey Harry Kimber | trainer Sheila Lewis (14d 0/5) | headgear - | last run 204 days | form 084U4- | MARKET 5.2% | 09:00 median 18.75 | Matchbook 18.50
    comment: Winless in her last five, Wishful Wings was fourth last time out but has been off for 204 days, and a fourth three starts back is the best of her other recent efforts.

## 2:50 Hereford | race_id rac_32304231700 | CopyBet Overnight Best Odds Guaranteed Handicap Hurdle Race
Hurdle | Class 5 | 2m0f53y | going Good | Turf | 9 runners | rating band 0-105 | age 3yo+
- Seraphic (hrs_34220970) | 6yo G | 165lb | OR 102 | draw 0 | jockey Kielan Woods | trainer David Killahena & Graeme McPherson (14d 4/10) | headgear t | last run 1 days | form 4-3111 | MARKET 49.1% | 09:00 median 1.81 | Matchbook 1.86
    comment: Seraphic arrives on a hat-trick, having won last time out, two starts back and three starts back, and he has run over today's trip and going before.
- Gaelic Saint (hrs_48644673) | 5yo M | 168lb | OR 105 | draw 0 | jockey Rian Corcoran(5) | trainer Tom Symonds (14d 0/10) | headgear h | last run 22 days | form 2467-4 | MARKET 16.5% | 09:00 median 5.00 | Matchbook 5.90
- Taritino (hrs_29918658) | 6yo G | 163lb | OR 100 | draw 0 | jockey Callum Pritchard | trainer Joe Tickle (14d 0/4) | headgear - | last run 46 days | form 1321-6 | MARKET 8.9% | 09:00 median 9.00 | Matchbook 11.50
    comment: Taritino won two starts back and five starts back, with a second and a third in between, but was only sixth last time out and returns after 46 days.
- Phoenix Risen (hrs_27414751) | 9yo G | 166lb | OR 103 | draw 0 | jockey Chad Bament(5) | trainer Jeremy Scott (14d 1/6) | headgear b | last run 34 days | form 2155-8 | MARKET 6.1% | 09:00 median 13.00 | Matchbook 17.50
    comment: Phoenix Risen won four starts back and was second five runs ago, and he has run over today's trip and on this going before.
- Zenato (hrs_37774513) | 5yo G | 167lb | OR 104 | draw 0 | jockey Fern O'Brien(5) | trainer Fergal O'Brien (14d 3/26) | headgear t | last run 27 days | form 9115-P | MARKET 6.0% | 09:00 median 12.00 | Matchbook 18.50
    comment: The risk is that he was pulled up last time out.
- Maasai Mara (hrs_31189564) | 6yo G | 168lb | OR 105 | draw 0 | jockey Charlie Deutsch | trainer John O'Shea (14d 0/4) | headgear - | last run 98 days | form 55/97- | MARKET 4.8% | 09:00 median 17.00 | Matchbook 22.00
    comment: The risk is that recent finishes are unconvincing and he is yet to win in that spell.
- Lucky Sevens (hrs_60818471) | 3yo G | 146lb | OR 99 | draw 0 | jockey James Best | trainer Nikki Evans (14d 0/1) | headgear p | last run 26 days | form 2142 | MARKET 3.8% | 09:00 median 19.00 | Matchbook 30.00
    comment: Lucky Sevens has been in the frame in three of his last four, including a second last time out and a win three starts back, and has run over today's trip and going.
- Happy Chandler (hrs_36137234) | 5yo G | 154lb | OR 91 | draw 0 | jockey Harry Reed | trainer Michael Blake (14d 0/2) | headgear - | last run 45 days | form 543 | MARKET 3.0% | 09:00 median 23.00 | Matchbook 40.00
    comment: Happy Chandler is winless in his last three, though he has crept from fifth to fourth to third, and he has run over today's trip and going.
- No Hard Feelings (hrs_41596954) | 6yo G | 161lb | OR 98 | draw 0 | jockey Stan Sheppard | trainer Matt Sheppard (14d 1/4) | headgear t | last run 13 days | form 1-1160 | MARKET 1.8% | 09:00 median 41.00 | Matchbook 65.00
    comment: No Hard Feelings won three on the spin, but those came three to five starts back, and he has since been a sixth, then unplaced last time out, so the form is heading the wrong way.

## 3:25 Hereford | race_id rac_32304233637 | CopyBet Support Safer Gambling Mares' Open Maiden National Hunt Flat Race (Category 3 Elimination) (GBB Race)
NH Flat | Class 5 | 2m0f53y | going Good | Turf | 5 runners | rating band - | age 4-5yo
- Eagles Promise (hrs_65549946) | 4yo F | 156lb | OR - | draw 0 | jockey Jonathan Burke | trainer Tom George (14d 2/5) | headgear - | last run 111 days | form 75 | MARKET 35.5% | 09:00 median 2.50 | Matchbook 2.76
- Ms Belle (hrs_17395173509) | 4yo F | 156lb | OR - | draw 0 | jockey David Bass | trainer Max Comley (14d 3/10) | headgear - | last run 192 days | form 2 | MARKET 26.4% | 09:00 median 3.50 | Matchbook 3.60
- Nova Foresta (hrs_17395099456) | 4yo F | 156lb | OR - | draw 0 | jockey Daniel Sansom(3) | trainer Seamus Mullins (14d 2/10) | headgear - | last run - days | form - | MARKET 18.7% | 09:00 median 4.50 | Matchbook 5.50
- Three of Spades (hrs_65287187) | 4yo F | 156lb | OR - | draw 0 | jockey Benjamin Macey(5) | trainer Tom Gretton (14d 0/1) | headgear - | last run 38 days | form 5 | MARKET 12.0% | 09:00 median 7.50 | Matchbook 8.40
- Flora Hobbs (hrs_64072911) | 4yo F | 156lb | OR - | draw 0 | jockey Kevin Brogan | trainer Samuel Drinkwater (14d 1/5) | headgear - | last run 183 days | form 1-0 | MARKET 7.4% | 09:00 median 13.00 | Matchbook 13.00
