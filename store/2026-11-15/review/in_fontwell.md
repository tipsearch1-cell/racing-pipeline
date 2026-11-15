# Card review packet: Fontwell, 2026-11-15

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
{"meeting": "fontwell", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 12:30 Fontwell | race_id rac_32304481573 | StoneX Commodities Conditional Jockeys' Handicap Hurdle Race
Hurdle | Class 4 | 2m1f162y | going Good To Soft | Turf | 8 runners | rating band 0-120 | age 3yo+
- Western Cross (hrs_57718724) | 5yo G | 164lb | OR 113 | draw 0 | jockey Jack Stenhouse(8) | trainer Philip Hobbs & Johnson White (14d 0/18) | headgear h | last run 18 days | form 3441-4 | MARKET 24.7% | 09:00 median 3.50 | Matchbook 3.85 | CHECK (skip line 3.32)
    comment: Fourth last time out and a winner two starts back, Western Cross has been consistent, with a third five runs ago, and he has run over today's trip and going after just 18 days off.
- Bridge (hrs_30614066) | 6yo G | 155lb | OR 104 | draw 0 | jockey Freddie Mitchell | trainer Jamie Moore & Josh Moore (14d 5/28) | headgear tp | last run 5 days | form 74P1-V | MARKET 13.8% | 09:00 median 6.00 | Matchbook 7.20
    comment: Bridge won two starts back, but a pulled up and a seventh in the other recent runs, plus a void last time out five days ago, make him hard to fancy under 155 lb.
- Maccarellu (hrs_41814017) | 6yo G | 155lb | OR 104 | draw 0 | jockey Ned Fox(3) | trainer Venetia Williams (14d 0/0) | headgear - | last run 225 days | form 2/366- | MARKET 12.5% | 09:00 median 7.00 | Matchbook 7.60
    comment: Maccarellu is winless in his last four, finishing sixth on each of his last two outings, and returns after 225 days off, which makes him hard to fancy under 155 lb. On the plus side, he has run on today's going and was second and third earlier in that spell.
- Kamaxos (hrs_21666855) | 9yo G | 164lb | OR 113 | draw 0 | jockey Daire McConville(3) | trainer Charlie Longsdon (14d 4/15) | headgear ht | last run 274 days | form P1620- | MARKET 11.4% | 09:00 median 8.00 | Matchbook 8.20
    comment: The main risk is a 274-day absence, with 164 lb to carry.
- Marhaba Prince (hrs_47685015) | 5yo G | 162lb | OR 111 | draw 0 | jockey James Robottom(10) | trainer Anthony Honeyball (14d 4/27) | headgear t (1st time) | last run 18 days | form 221-P8 | MARKET 10.7% | 09:00 median 8.50 | Matchbook 8.80
    comment: Marhaba Prince won three starts back and was second in his two runs before that, while he has run over today's trip and going and is back after just 18 days.
- The Sainted Canary (hrs_38173926) | 7yo G | 161lb | OR 110 | draw 0 | jockey Chad Bament | trainer Jeremy Scott (14d 1/10) | headgear t | last run 570 days | form 45123/ | MARKET 10.0% | 09:00 median 9.00 | Matchbook 9.60
    comment: The Sainted Canary arrives with solid recent form, third last time out, a second two starts back, and a winner three starts back, and he has run over today's trip and going before. The big risk is a 570-day absence, plus 161 lb on his back.
- Only One Blue (hrs_44541742) | 4yo F | 157lb | OR 106 | draw 0 | jockey Tom Broughton | trainer Max Comley (14d 3/9) | headgear p | last run 36 days | form 3324-7 | MARKET 8.9% | 09:00 median 9.00 | Matchbook 11.50
    comment: Only One Blue is winless in her last five, though a second and two thirds in that spell show she is consistent, and she has run over today's trip and going. Last-time-out seventh and a 157 lb burden hold her back, despite a 36-day break.
- Belfrina (hrs_37821539) | 5yo M | 168lb | OR 117 | draw 0 | jockey Rian Corcoran(3) | trainer David Pipe (14d 0/10) | headgear t | wind surgery | last run 17 days | form 2F12/ | MARKET 8.0% | 09:00 median 9.50 | Matchbook 13.50
    comment: Belfrina arrives in good heart, second last time out and a winner two starts back, and she's fresh enough after 17 days off.

## 1:05 Fontwell | race_id rac_32304483510 | StoneX Southern National Handicap Steeple Chase (GBB Race)
Chase | Class 3 | 3m3f149y | going Good To Soft | Turf | 11 runners | rating band 0-125 | age 4yo+
- Mask of Zorro (hrs_40473125) | 6yo G | 167lb | OR 124 | draw 0 | jockey Dylan Johnston | trainer Joe Tizzard (14d 5/23) | headgear - | last run 18 days | form 1114-1 | MARKET 18.6% | 09:00 median 4.50 | Matchbook 5.00 | CHECK (skip line 4.27)
    comment: Mask of Zorro arrives in cracking form, with four wins in his last five starts including last time out, and he has run on today's going, but he carries 167 lb off an official mark of 124.
- Call Me Legend (hrs_40646984) | 6yo G | 164lb | OR 121 | draw 0 | jockey Jack Stenhouse(7) | trainer Philip Hobbs & Johnson White (14d 0/18) | headgear - | last run 24 days | form 1222-3 | MARKET 16.8% | 09:00 median 4.50 | Matchbook 6.00
    comment: Call Me Legend has been consistent, finishing third last time out after three seconds in a row, and he returns fit after 24 days with experience of today's going. Still, he has one win in his last five starts and carries 164 lb, which may stop him going one better.
- Paper Mill (hrs_28622993) | 10yo G | 165lb | OR 122 | draw 0 | jockey Charlie Hammond | trainer Stuart Edmunds (14d 2/12) | headgear b | last run 21 days | form P-2411 | MARKET 15.4% | 09:00 median 5.50 | Matchbook 6.00
- Jeu d'Opale (hrs_49578704) | 8yo G | 154lb | OR 111 | draw 0 | jockey Charlie Deutsch | trainer Venetia Williams (14d 0/0) | headgear - | last run 274 days | form /52F1- | MARKET 12.4% | 09:00 median 7.00 | Matchbook 7.40
    comment: Won last time out, but that came 274 days ago, and he fell two starts back, so a long absence and a hefty 154 lb are hard to overlook.
- Livin On Luco (hrs_32568704) | 8yo G | 170lb | OR 127 | draw 0 | jockey Rian Corcoran(5) | trainer Philip Hobbs & Johnson White (14d 0/18) | headgear b | last run 21 days | form 462P-3 | MARKET 10.8% | 09:00 median 7.50 | Matchbook 9.00
    comment: Livin On Luco arrives in solid shape after a third last time out just 21 days ago, and he has run over today's trip and going before. A second three starts back shows he can go close, though he is yet to win in his last five and carries 170 lb.
- Ivane (hrs_29409408) | 8yo G | 155lb | OR 112 | draw 0 | jockey Stan Sheppard | trainer James Owen (14d 9/42) | headgear v | last run 28 days | form 64-4P6 | MARKET 8.6% | 09:00 median 10.00 | Matchbook 11.00
    comment: Ivane has been consistent without winning, finishing sixth last time out and fourth on two earlier starts, though he was pulled up two runs back. He has run over today's trip and going, but 155 lb looks a big ask for a winless gelding.
- Jack's Jury (hrs_39959241) | 6yo G | 142lb | OR 93 | draw 0 | jockey Charlie Maggs | trainer Barry Murphy (14d 1/5) | headgear tp | last run 7 days | form -3U153 | MARKET 7.0% | 09:00 median 11.00 | Matchbook 15.50
    comment: On the plus side, he has run on today's going before.
- Invincible Nao (hrs_29379469) | 8yo G | 167lb | OR 124 | draw 0 | jockey David Noonan | trainer Jamie Moore & Josh Moore (14d 5/28) | headgear h | last run 253 days | form 14364- | MARKET 4.5% | 09:00 median 17.00 | Matchbook 24.00
    comment: Invincible Nao has been consistent, finishing fourth last time out and a third three starts back, with a win five starts back, and he has run over today's trip and going.
- What A Glance (hrs_21212107) | 11yo G | 168lb | OR 125 | draw 0 | jockey Murray Dodd(5) | trainer Tom Britten (14d 0/1) | headgear t | last run 175 days | form F2P-22 | MARKET 2.1% | 09:00 median 41.00 | Matchbook 46.00
    comment: The main risk is a 175-day absence under 168 lb, and he is yet to win in recent form.
- Ventura Highway (hrs_35015421) | 6yo G | 168lb | OR 125 | draw 0 | jockey Freddie Mitchell(3) | trainer Jamie Moore & Josh Moore (14d 5/28) | headgear t | last run 193 days | form P067-7 | MARKET 2.1% | 09:00 median 34.00 | Matchbook 55.00
    comment: Ventura Highway returns after 193 days off, having finished seventh last time out, and another seventh two starts back, so he's yet to win in recent form. Lightly raced on that evidence and open to improvement, though 168 lb is a big weight to carry.
- Dartan (hrs_21650580) | 9yo G | 162lb | OR 119 | draw 0 | jockey Tom Cannon | trainer Sarah Humphrey (14d 1/2) | headgear tv | last run 14 days | form 329-P3 | MARKET 1.7% | 09:00 median 51.00 | Matchbook 60.00
    comment: The risk is a pulled-up effort two starts back, plus 162 lb on his back.

## 1:43 Fontwell | race_id rac_32304485447 | StoneX Bullion Novices' Hurdle Race (GBB Race)
Hurdle | Class 4 | 2m1f162y | going Good To Soft | Turf | 13 runners | rating band - | age 4yo+
- Bass Hunter (hrs_39431882) | 6yo G | 161lb | OR - | draw 0 | jockey Freddie Gordon | trainer Chris Gordon (14d 1/7) | headgear - | last run 27 days | form 1130-1 | MARKET 71.3% | 09:00 median 1.20 | Matchbook 1.22
- Catchem Black (hrs_61456367) | 4yo G | 154lb | OR - | draw 0 | jockey Callum Pritchard | trainer Ben Pauling (14d 4/23) | headgear - | last run 280 days | form 1- | MARKET 11.6% | 09:00 median 5.50 | Matchbook 9.80
- Casper Charlie (hrs_64294993) | 5yo G | 154lb | OR - | draw 0 | jockey Daniel Sansom(3) | trainer Seamus Mullins (14d 3/15) | headgear - | last run 103 days | form 0-F2 | MARKET 4.0% | 09:00 median 15.00 | Matchbook 34.00
- Chocks Away (hrs_60977245) | 4yo G | 154lb | OR - | draw 0 | jockey Paul O'Brien | trainer Henrietta C Knight (14d 0/7) | headgear - | last run 17 days | form 735-3 | MARKET 2.2% | 09:00 median 23.00 | Matchbook 80.00
- Orchard (hrs_44199162) | 4yo G | 154lb | OR - | draw 0 | jockey Conor O'Farrell | trainer Warren Greatrex (14d 4/22) | headgear h (1st time) | last run 39 days | form /- | MARKET 2.0% | 09:00 median 26.00 | Matchbook 100.00
- Sienna Earth (hrs_48259162) | 6yo M | 147lb | OR - | draw 0 | jockey Ben Godfrey | trainer Anthony Honeyball (14d 4/27) | headgear - | last run 651 days | form U4/ | MARKET 2.0% | 09:00 median 30.00 | Matchbook 70.00
- Alcaraz (hrs_26822642) | 7yo G | 154lb | OR - | draw 0 | jockey Tabitha Worsley | trainer George Baker (14d 1/7) | headgear - | last run 17 days | form P- | MARKET 1.6% | 09:00 median 30.00 | Matchbook 140.00
- Killarney (hrs_17394598816) | 6yo G | 154lb | OR - | draw 0 | jockey Tom Cannon | trainer Chris Gordon (14d 1/7) | headgear - | last run 204 days | form 25- | MARKET 1.4% | 09:00 median 41.00 | Matchbook 190.00
- Saint Canary Rock (hrs_63323603) | 4yo F | 147lb | OR - | draw 0 | jockey Lorcan Williams | trainer Jeremy Scott (14d 1/10) | headgear - | last run 36 days | form 5-6 | MARKET 1.0% | 09:00 median 51.00 | Matchbook 210.00
- Riseandcall (hrs_17394615504) | 5yo G | 154lb | OR - | draw 0 | jockey David Noonan | trainer Ben Clarke (14d 0/6) | headgear - | last run 11 days | form 432-0 | MARKET 0.9% | 09:00 median 67.00 | Matchbook 240.00
- Savvy Stellar (hrs_45950667) | 4yo G | 154lb | OR - | draw 0 | jockey James Best | trainer Nigel Hawke (14d 1/6) | headgear - | last run 388 days | form /- | MARKET 0.8% | 09:00 median 67.00 | Matchbook 270.00
- Ignite The Spark (hrs_17394111735) | 4yo G | 154lb | OR - | draw 0 | jockey Charlie Maggs | trainer Barry Murphy (14d 1/5) | headgear t (1st time) | last run 17 days | form 4-P | MARKET 0.7% | 09:00 median 67.00 | Matchbook 320.00
- Straight Out (hrs_17395297626) | 4yo G | 154lb | OR - | draw 0 | jockey Harry Reed | trainer Helen Nelmes (14d 0/0) | headgear - | last run 190 days | form 248P-P | MARKET 0.5% | 09:00 median 126.00 | Matchbook 520.00

## 2:20 Fontwell | race_id rac_32304487384 | StoneX Payments Juvenile Hurdle Race (GBB Race)
Hurdle | Class 4 | 2m1f162y | going Good To Soft | Turf | 11 runners | rating band - | age 3yo
- Pass The Buck (hrs_58065532) | 3yo G | 154lb | OR 115 | draw 0 | jockey Paul O'Brien | trainer Harry Derham (14d 4/17) | headgear p | last run 16 days | form 325 | MARKET 28.0% | 09:00 median 3.00 | Matchbook 3.30 | CHECK (skip line 2.85)
    comment: Pass The Buck has been in the frame twice in his last three starts, a second two runs back and a third three starts back, before a fifth last time out, and he's fit after 16 days.
- Silver State (hrs_53081413) | 3yo G | 154lb | OR - | draw 0 | jockey Tom Cannon | trainer Alan King (14d 2/19) | headgear - | last run 107 days | form - | MARKET 23.4% | 09:00 median 3.50 | Matchbook 4.00
    comment: Silver State is unexposed with no recorded form to lean on, so he remains open to improvement. Returning after 107 days off, the gelding carries 154 lb and still has plenty to prove.
- Lion In Zion (hrs_17395390453) | 3yo G | 154lb | OR - | draw 0 | jockey Jack Tudor | trainer David Pipe (14d 0/10) | headgear - | last run 231 days | form 93- | MARKET 18.6% | 09:00 median 4.50 | Matchbook 5.00
    comment: Lightly raced and unexposed, Lion In Zion could have more to offer after a third last time out, following a ninth two starts back, though he returns from 231 days off and is yet to win in his last two starts, carrying 154 lb.
- James Choice (hrs_55948228) | 3yo G | 154lb | OR - | draw 0 | jockey Conor O'Farrell | trainer Warren Greatrex (14d 4/22) | headgear - | last run 64 days | form - | MARKET 8.9% | 09:00 median 9.25 | Matchbook 11.00
    comment: James Choice is unexposed with no recorded form to go on, so he's open to improvement. He returns after 64 days off and carries 154 lb, and with a lightly raced profile there could be more to come.
- Houndswood Willow (hrs_57223054) | 3yo G | 161lb | OR 100 | draw 0 | jockey David Bass | trainer Tom Dascombe (14d 0/0) | headgear p | last run 20 days | form 3251 | MARKET 7.3% | 09:00 median 10.00 | Matchbook 14.50
    comment: Houndswood Willow arrives a course-of-action threat on the back of a win last time out, and he has been in the first three in three of his last four starts, fresh enough after 20 days off and having run over today's trip.
- Cape View (hrs_17395418614) | 3yo G | 154lb | OR - | draw 0 | jockey Lorcan Williams | trainer Jack Jones (14d 1/5) | headgear - | last run - days | form - | MARKET 6.2% | 09:00 median 13.00 | Matchbook 17.00
    comment: Cape View is unraced, so this gelding makes his debut with no form to go on, which leaves him unexposed and open to improvement. He carries 154 lb, and his first run should reveal plenty.
- Plan C (hrs_54933725) | 3yo G | 154lb | OR - | draw 0 | jockey Charlie Deutsch | trainer Alan King (14d 2/19) | headgear p (1st time) | last run 12 days | form 5 | MARKET 4.4% | 09:00 median 17.00 | Matchbook 26.00
    comment: The main risk is that he's yet to win in recent form and shoulders 154 lb.
- Rebel Legend (hrs_62326453) | 3yo G | 154lb | OR - | draw 0 | jockey Freddie Mitchell(3) | trainer Jamie Moore & Josh Moore (14d 5/28) | headgear b (1st time) | last run 232 days | form - | MARKET 1.4% | 09:00 median 51.00 | Matchbook 120.00
    comment: Rebel Legend is unexposed and open to improvement, with no recorded form to go on, and this gelding returns after 232 days off while carrying 154 lb, so he may need to prove his fitness.
- Don Pablo Colina (hrs_58843421) | 3yo G | 154lb | OR - | draw 0 | jockey Tabitha Worsley | trainer George Baker (14d 1/7) | headgear - | last run 116 days | form - | MARKET 0.7% | 09:00 median 81.00 | Matchbook 390.00
    comment: Unexposed on the evidence available, with no recorded form to go on, Don Pablo Colina returns after 116 days off and shoulders 154 lb. He is open to improvement, though there's little to judge him on yet.
- Pete's Sake (hrs_17393578762) | 3yo G | 154lb | OR - | draw 0 | jockey Robbie David(5) | trainer Daisy Hitchins (14d 0/6) | headgear - | last run 20 days | form - | MARKET 0.6% | 09:00 median 101.00 | Matchbook 300.00
    comment: Pete's Sake is unexposed, with no recorded form to go on, so any improvement is there to be found. He returns 20 days after his last run and carries 154 lb.
- Dundeelin (hrs_17393577719) | 3yo G | 154lb | OR - | draw 0 | jockey David Noonan | trainer Nigel Hawke (14d 1/6) | headgear - | last run 36 days | form P | MARKET 0.5% | 09:00 median 126.00 | Matchbook 300.00
    comment: Dundeelin is unexposed, with just one recent run to go on, when he pulled up 36 days ago, so there's little to judge him on yet. Carrying 154 lb, he's yet to win in his last start and may have more to offer.

## 2:50 Fontwell | race_id rac_32304489321 | John Rogerson Memorial Handicap Steeple Chase (Fontwell Chase Series Qualifier)
Chase | Class 5 | 2m5f135y | going Good To Soft | Turf | 10 runners | rating band 0-100 | age 4yo+
- Majestic Moment (hrs_37701405) | 7yo G | 159lb | OR 91 | draw 0 | jockey Rian Corcoran(5) | trainer Dean Summersby (14d 1/2) | headgear - | last run 18 days | form U26P32 | MARKET 21.4% | 09:00 median 4.00 | Matchbook 4.40 | CHECK (skip line 3.80)
    comment: Majestic Moment arrives in decent order, second last time out and third two starts back, and he's fresh enough after 18 days, though he's winless in his last six and carries a hefty 159 lb. He has run on today's going before, but a pulled up and an unseated in that spell flag some unreliability.
- What A Dragon (hrs_59678815) | 5yo G | 146lb | OR 78 | draw 0 | jockey Harry Kimber | trainer Robert Walford (14d 0/2) | headgear p | wind surgery | last run 237 days | form P803- | MARKET 18.3% | 09:00 median 4.50 | Matchbook 5.30
    comment: What A Dragon is winless in his last four and returns after 237 days off, which makes him hard to fancy, though a third last time out is a clear positive.
- Valirann Gold (hrs_23643305) | 9yo G | 148lb | OR 80 | draw 0 | jockey Ben Godfrey | trainer Harriet Brown (14d 0/0) | headgear t | last run 34 days | form 142-55 | MARKET 11.8% | 09:00 median 7.00 | Matchbook 8.20
    comment: Valirann Gold has slipped to back-to-back fifths since a second three starts back, and a win five starts back now looks a way off.
- Bertie Wooster (hrs_27451879) | 8yo G | 163lb | OR 95 | draw 0 | jockey Dylan Johnston | trainer Joe Tizzard (14d 5/23) | headgear p | last run 29 days | form 2244-P | MARKET 9.6% | 09:00 median 9.20 | Matchbook 9.80
- Fay Ce Que Voudras (hrs_22689072) | 10yo M | 162lb | OR 94 | draw 0 | jockey Tom Cannon | trainer Kerry Lee (14d 0/6) | headgear - | last run 254 days | form 5F111- | MARKET 9.4% | 09:00 median 7.00 | Matchbook 13.00
    comment: Three straight wins is a cracking recent run, and she has run on today's going before, but 254 days off is a big gap and 162 lb is a hefty burden.
- Just Call Me Buzz (hrs_59895675) | 5yo G | 168lb | OR 100 | draw 0 | jockey David Noonan | trainer Ben Clarke (14d 0/6) | headgear t (1st time) | last run 157 days | form 353-24 | MARKET 8.5% | 09:00 median 9.00 | Matchbook 12.00
    comment: The main risk is a 157-day layoff, so fitness is the question.
- Wellwillya (hrs_29761452) | 8yo G | 149lb | OR 81 | draw 0 | jockey Paul O'Brien | trainer Helen Nelmes (14d 0/0) | headgear p | last run 158 days | form 2/2-4P | MARKET 7.2% | 09:00 median 12.00 | Matchbook 13.00
    comment: Wellwillya was second twice and fourth in his last four before being pulled up last time, and he has run over today's trip and going, but he's been off for 158 days and is yet to win in that spell.
- Elpologreg (hrs_33790855) | 7yo G | 142lb | OR 71 | draw 0 | jockey Benjamin Macey(5) | trainer Seamus Mullins (14d 3/15) | headgear - | last run 25 days | form 2P/2-P | MARKET 7.0% | 09:00 median 12.00 | Matchbook 14.50
    comment: Elpologreg is winless in his last four, pulled up last time out and in a third start back, which makes him hard to fancy, though he was second two starts back and a second four back.
- Lord Maher (hrs_412693750) | 6yo G | 149lb | OR 81 | draw 0 | jockey Marc Goldstein | trainer Karen Jewell (14d 0/6) | headgear p | last run 13 days | form 5B7-55 | MARKET 5.5% | 09:00 median 15.00 | Matchbook 18.50
    comment: Lord Maher arrives fresh from a run just 13 days ago, with a fifth last time out and another fifth two starts back, and he has run over today's trip.
- Doonbeg Don (hrs_33165132) | 8yo G | 165lb | OR 97 | draw 0 | jockey Charlie Maggs | trainer Barry Murphy (14d 1/5) | headgear p | last run 17 days | form 027/PP | MARKET 1.1% | 09:00 median 67.00 | Matchbook 100.00
    comment: Doonbeg Don returns from two pulled-up efforts with a fresh 17-day gap, and a second four starts back shows he has a bit of ability.

## 3:25 Fontwell | race_id rac_32304491258 | Maria's And Aidie's 25th Wedding Anniversary Novices' Limited Handicap Hurdle Race
Hurdle | Class 5 | 2m5f164y | going Good To Soft | Turf | 9 runners | rating band 0-95 | age 3yo+
- County Champs (hrs_39978197) | 7yo G | 162lb | OR 91 | draw 0 | jockey Freddie Gordon | trainer Chris Gordon (14d 1/7) | headgear - | last run 25 days | form 2-PF22 | MARKET 24.4% | 09:00 median 3.50 | Matchbook 3.80 | CHECK (skip line 3.32)
    comment: County Champs arrives in good heart, runner-up last time out and again two starts back, though he's yet to win in his last five and has a fell and a pulled up in that spell. He has run over today's trip and carries 162 lb off 91, a stiff task.
- Asta La Vista (hrs_56338317) | 5yo G | 166lb | OR 95 | draw 0 | jockey Joe Anderson(3) | trainer Tom Britten (14d 0/1) | headgear - | last run 183 days | form 4835-2 | MARKET 21.1% | 09:00 median 4.00 | Matchbook 4.50
    comment: Asta La Vista bounced back to form with a second last time out, having also finished third three starts back, and he is yet to win in his last five.
- Charles Morin (hrs_37673370) | 5yo G | 148lb | OR 77 | draw 0 | jockey Callum Pritchard | trainer Barry Murphy (14d 1/5) | headgear tb | last run 12 days | form /4-682 | MARKET 13.3% | 09:00 median 6.50 | Matchbook 7.20
    comment: Charles Morin comes here fresh from a second last time out, just 12 days ago, and has run on today's going, though he is winless in his last four and was only eighth and sixth before that.
- Black Dakota (hrs_57654415) | 7yo G | 164lb | OR 93 | draw 0 | jockey Robbie David(5) | trainer Daisy Hitchins (14d 0/6) | headgear - | last run 17 days | form 546435 | MARKET 11.4% | 09:00 median 7.50 | Matchbook 8.40
    comment: Black Dakota has been consistent, finishing a fifth last time out, a third two starts back and no worse than sixth in his last six, and he returns fresh after 17 days having run over today's trip and going.
- Ami Bondhu (hrs_34637813) | 7yo G | 160lb | OR 89 | draw 0 | jockey Tabitha Worsley | trainer Nick Gifford (14d 0/8) | headgear - | wind surgery | last run 265 days | form /0333- | MARKET 9.9% | 09:00 median 9.00 | Matchbook 9.60
    comment: The main risk is a 265-day absence, with 160 lb to carry.
- Hawa Jumeirah (hrs_36328985) | 5yo G | 156lb | OR 85 | draw 0 | jockey Paul O'Brien | trainer Helen Nelmes (14d 0/0) | headgear t | last run 31 days | form 833643 | MARKET 9.8% | 09:00 median 8.00 | Matchbook 10.50
    comment: Hawa Jumeirah arrives in solid shape after a third last time out, and he has been in the first three twice more in his last six, though he remains winless in that spell.
- Vendant (hrs_29816059) | 8yo G | 154lb | OR 83 | draw 0 | jockey Tom Cannon | trainer Richard Rowe (14d 0/0) | headgear - | last run 221 days | form 4P/2F- | MARKET 5.8% | 09:00 median 15.00 | Matchbook 17.00
- Lily Grace (hrs_33743962) | 8yo M | 145lb | OR 71 | draw 0 | jockey Ned Fox(3) | trainer Venetia Williams (14d 0/0) | headgear - | last run 217 days | form /0550- | MARKET 2.5% | 09:00 median 29.00 | Matchbook 48.00
    comment: Lily Grace is hard to fancy: she is winless in her last four, with a fifth two starts back and another fifth three starts back, and she returns after 217 days off.
- Always Force It (hrs_33975270) | 7yo G | 145lb | OR 69 | draw 0 | jockey Ben Godfrey | trainer Harriet Brown (14d 0/0) | headgear h | last run 700 days | form 67325/ | MARKET 1.6% | 09:00 median 51.00 | Matchbook 110.00
    comment: The big risk is a 700-day absence, which makes fitness a real question under 145 lb.
