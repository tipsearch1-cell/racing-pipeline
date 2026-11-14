# Card review packet: Windsor, 2026-11-14

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
{"meeting": "windsor", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 12:20 Windsor | race_id rac_32304460266 | A1R Services Ltd Mares' Maiden Hurdle Race (GBB Race)
Hurdle | Class 4 | 2m0f0y | going Good | Turf | 16 runners | rating band - | age 3yo+
- Ti'mamzel (hrs_51897566) | 5yo M | 158lb | OR - | draw 0 | jockey Caoilin Quinn | trainer Jamie Moore & Josh Moore (14d 5/25) | headgear - | last run 219 days | form 1218- | MARKET 46.7% | 09:00 median 1.73 | Matchbook 1.85
- Jem's Lilly (hrs_48886278) | 6yo M | 158lb | OR 109 | draw 0 | jockey Calum Hogan(5) | trainer Harry Derham (14d 4/19) | headgear h (1st time) | last run 285 days | form 9/342- | MARKET 23.3% | 09:00 median 3.25 | Matchbook 3.95
- Magika Bella (hrs_17394678084) | 4yo F | 158lb | OR - | draw 0 | jockey Ben Jones | trainer Ben Pauling (14d 4/21) | headgear - | last run 15 days | form 2-4 | MARKET 10.3% | 09:00 median 7.00 | Matchbook 9.40
- Unflappable (hrs_64590498) | 4yo F | 158lb | OR - | draw 0 | jockey David Noonan | trainer Ben Clarke (14d 0/5) | headgear t (1st time) | last run 32 days | form 332 | MARKET 3.2% | 09:00 median 17.00 | Matchbook 46.00
- Sorgean (hrs_50422862) | 5yo M | 158lb | OR - | draw 0 | jockey Ben Godfrey | trainer Kayley Woollacott (14d 0/7) | headgear t | wind surgery | last run 36 days | form /21-56 | MARKET 3.0% | 09:00 median 26.00 | Matchbook 36.00
- Secret des Lune (hrs_59246957) | 5yo M | 158lb | OR - | draw 0 | jockey Rex Dingle | trainer Ben Clarke (14d 0/5) | headgear - | last run 16 days | form 221-65 | MARKET 3.0% | 09:00 median 26.00 | Matchbook 38.00
- Iconic Elsa (hrs_17393554773) | 4yo F | 158lb | OR - | draw 0 | jockey James Turner(5) | trainer Nigel & Willy Twiston-Davies (14d 6/36) | headgear - | last run 35 days | form 4 | MARKET 2.4% | 09:00 median 26.00 | Matchbook 48.00
- Maxi Mirage (hrs_17395298669) | 4yo F | 158lb | OR - | draw 0 | jockey Benjamin Macey(5) | trainer Seamus Mullins (14d 3/11) | headgear - | last run 181 days | form F2-2 | MARKET 1.8% | 09:00 median 29.00 | Matchbook 85.00
- On The Cobbles (hrs_63323533) | 4yo F | 158lb | OR - | draw 0 | jockey Ciaran Gethings | trainer Ben Case (14d 1/8) | headgear t (1st time) | last run 222 days | form 4- | MARKET 1.3% | 09:00 median 51.00 | Matchbook 160.00
- She's A Driver (hrs_62326383) | 4yo F | 158lb | OR - | draw 0 | jockey Tom Cannon | trainer David Bridgwater (14d 0/2) | headgear - | last run 250 days | form 6- | MARKET 1.1% | 09:00 median 67.00 | Matchbook 140.00
- The Tenpercentclub (hrs_17389381730) | 5yo M | 158lb | OR - | draw 0 | jockey Rian Corcoran(5) | trainer Tom Gretton (14d 0/3) | headgear - | last run - days | form - | MARKET 0.8% | 09:00 median 67.00 | Matchbook 200.00
- Kurios Lady (hrs_58005640) | 4yo F | 158lb | OR - | draw 0 | jockey Marc Goldstein | trainer Michael Madgwick (14d 0/1) | headgear - | last run 10 days | form - | MARKET 0.7% | 09:00 median 101.00 | Matchbook 160.00
- The Rarest Hour (hrs_17394329722) | 4yo F | 158lb | OR - | draw 0 | jockey Jack Tudor | trainer Christian Williams (14d 0/10) | headgear - | last run 14 days | form 44-8 | MARKET 0.6% | 09:00 median 101.00 | Matchbook 270.00
- Detroit Bay (hrs_57909649) | 4yo F | 158lb | OR - | draw 0 | jockey Lorcan Williams | trainer Jeremy Scott (14d 1/7) | headgear h | last run 36 days | form 4P0-8 | MARKET 0.6% | 09:00 median 101.00 | Matchbook 200.00
- Private Project (hrs_53294493) | 3yo F | 142lb | OR - | draw 0 | jockey Sean Houlihan | trainer Pat Phelan (14d 1/4) | headgear - | last run 30 days | form - | MARKET 0.6% | 09:00 median 101.00 | Matchbook 200.00
- West Hill Rosie (hrs_61110924) | 4yo F | 158lb | OR - | draw 0 | jockey Callum Pritchard | trainer Seamus Mullins (14d 3/11) | headgear - | last run 19 days | form 0-P | MARKET 0.5% | 09:00 median 101.00 | Matchbook 390.00

## 12:55 Windsor | race_id rac_32304462203 | Freight Movement Same Day Novices' Handicap Steeple Chase (GBB Race)
Chase | Class 4 | 2m4f42y | going Good | Turf | 6 runners | rating band 0-120 | age 4yo+
- Scavengers Reign (hrs_46233614) | 6yo M | 159lb | OR 113 | draw 0 | jockey Callum Pritchard | trainer James Owen (14d 10/42) | headgear - | last run 17 days | form 3130-2 | MARKET 30.0% | 09:00 median 3.00 | Matchbook 3.10 | CHECK (skip line 2.85)
    comment: Scavengers Reign arrives in good heart after a second last time out, just 17 days ago, and she has a win four starts back plus a third three starts back in her recent form. She has run over today's trip and going, though 159 lb is a stiff burden.
- Le Tiep's Sacre (hrs_46450180) | 5yo G | 164lb | OR 118 | draw 0 | jockey Caoilin Quinn | trainer Jamie Moore & Josh Moore (14d 5/25) | headgear - | last run 245 days | form 331/5- | MARKET 22.8% | 09:00 median 4.00 | Matchbook 4.20
    comment: The main risk is a 245-day absence, with a fifth last time out and 164 lb to carry.
- Admiral Stewart (hrs_38305218) | 7yo G | 161lb | OR 115 | draw 0 | jockey Isabelle Ryder(5) | trainer Jamie Snowden (14d 11/26) | headgear tp | last run 210 days | form P4342- | MARKET 17.0% | 09:00 median 5.00 | Matchbook 5.90
    comment: Admiral Stewart arrives with a solid book, finishing second last time out and a fourth two starts back, and he has run over today's trip and going before, while the yard is flying at 11 from 26 in the last fortnight. The one concern is a 210-day absence, so fitness is the question.
- Piping Rock (hrs_52055759) | 5yo G | 162lb | OR 116 | draw 0 | jockey Adam Wedge | trainer Emma Lavelle (14d 2/15) | headgear - | wind surgery | last run 204 days | form 23333- | MARKET 11.7% | 09:00 median 7.50 | Matchbook 8.40
    comment: Piping Rock arrives with a consistent profile, finishing third last time out, third two starts back, third three starts back, third four starts back and second five starts back, and he has run over today's trip and going before.
- Legal Weapon (hrs_47098821) | 6yo G | 156lb | OR 110 | draw 0 | jockey Ben Jones | trainer Ben Pauling (14d 4/21) | headgear - | wind surgery | last run 17 days | form 2440-F | MARKET 11.1% | 09:00 median 8.00 | Matchbook 9.00
    comment: A fourth, another fourth and a second further back show some ability, and he has had 17 days to recover.
- King Jon Oliver (hrs_51091054) | 6yo G | 160lb | OR 114 | draw 0 | jockey Kevin Brogan | trainer Olly Murphy (14d 8/41) | headgear - | last run 205 days | form 21P4P- | MARKET 7.4% | 09:00 median 12.00 | Matchbook 13.50
    comment: King Jon Oliver won four starts back and was a fourth two starts back, but he has pulled up in two of his last three outings and returns after 205 days off. He has run over today's trip and going, though 160 lb is a big burden for a 114-rated gelding.

## 1:25 Windsor | race_id rac_32304464140 | Fitzdares Telephone & Text Betting Handicap Hurdle Race (Challenger Stayers' Hurdle Series Qualifier)
Hurdle | Class 3 | 3m0f0y | going Good | Turf | 14 runners | rating band 0-125 | age 4yo+
- Doctor On Call (hrs_47869024) | 6yo G | 163lb | OR 119 | draw 0 | jockey Dylan Johnston | trainer Sam Thomas (14d 0/4) | headgear p (1st time) | last run 269 days | form /2341- | MARKET 18.9% | 09:00 median 4.50 | Matchbook 4.60 | CHECK (skip line 4.27)
    comment: Doctor On Call won last time out and was fourth and third in the runs before, but he returns after 269 days off and carries 163 lb, so he is hard to fancy.
- Kildinan Prince (hrs_52495625) | 7yo G | 164lb | OR 120 | draw 0 | jockey Ben Jones | trainer Emma Lavelle (14d 2/15) | headgear - | last run 237 days | form 221- | MARKET 18.0% | 09:00 median 4.33 | Matchbook 5.20
    comment: Kildinan Prince won last time out and was second twice before that, but he returns after 237 days off and carries 164 lb, which could blunt him.
- Surrey Lord (hrs_31965437) | 7yo G | 160lb | OR 116 | draw 0 | jockey Kevin Brogan | trainer Toby Lawes (14d 0/3) | headgear - | last run 301 days | form 11414- | MARKET 8.7% | 09:00 median 9.00 | Matchbook 11.00
    comment: Three wins in his last five starts is a strong body of form, and he has run on today's going before, but he was only fourth last time out, has been off for 301 days and carries 160 lb.
- Reallyntruthfully (hrs_35137067) | 7yo G | 164lb | OR 120 | draw 0 | jockey Ciaran Gethings | trainer Kim Bailey & Mat Nicholls (14d 2/15) | headgear p (1st time) | last run 35 days | form 16P4-D | MARKET 8.2% | 09:00 median 10.00 | Matchbook 11.00
    comment: The risk is a 164 lb burden and a patchy record, with a disqualification last time and a pulled up three starts back.
- Mount Anglesby (hrs_34598200) | 7yo G | 164lb | OR 120 | draw 0 | jockey Joe Anderson(3) | trainer Tom Britten (14d 0/0) | headgear - | last run 28 days | form 614-F1 | MARKET 7.0% | 09:00 median 11.00 | Matchbook 14.50
    comment: Mount Anglesby won last time out and has two wins in his last five starts, though a fall two runs back leaves a question mark, and he has run on today's going before.
- Thank You Ma'am (hrs_34652590) | 7yo G | 168lb | OR 124 | draw 0 | jockey Lorcan Murtagh | trainer Georgina Nicholls (14d 0/3) | headgear tp | last run 21 days | form 32-424 | MARKET 6.7% | 09:00 median 10.00 | Matchbook 16.50
    comment: Yet to win in his last five, though, and 168 lb is a hefty burden to carry.
- Crack Ops (hrs_55177724) | 4yo G | 150lb | OR 108 | draw 0 | jockey Jack Tudor | trainer Oliver Greenall & Josh Guerriero (14d 0/16) | headgear p | last run 44 days | form 322-12 | MARKET 6.5% | 09:00 median 12.00 | Matchbook 15.00
    comment: Crack Ops arrives in cracking form, second last time out, a winner two starts back and never worse than third in his last five, and he has run over today's trip and going.
- Tzarmix (hrs_32668503) | 8yo G | 161lb | OR 117 | draw 0 | jockey Sean Houlihan | trainer Alastair Ralph (14d 0/4) | headgear p | last run 35 days | form 2224-1 | MARKET 6.4% | 09:00 median 12.00 | Matchbook 15.00
    comment: Tzarmix won last time out and has finished second in three of his last five, with a fourth two starts back, and he has run over today's trip and going before.
- Libre de Choeur (hrs_39959381) | 6yo G | 160lb | OR 116 | draw 0 | jockey Adam Wedge | trainer Clive Boultbee-Brooks (14d 0/7) | headgear - | last run 23 days | form 2616-3 | MARKET 5.7% | 09:00 median 15.00 | Matchbook 16.00
    comment: Libre de Choeur was third last time out, and a winner three starts back, but a sixth two starts back and a sixth four starts back show the inconsistency, while 160 lb is a hefty burden.
- Lucky Bere (hrs_38231361) | 5yo G | 161lb | OR 117 | draw 0 | jockey Rex Dingle | trainer Kayley Woollacott (14d 0/7) | headgear - | last run 21 days | form 812P-7 | MARKET 5.1% | 09:00 median 15.00 | Matchbook 19.00
    comment: Lucky Bere has a winner four starts back and a second three starts back, but he's since pulled up and finished seventh last time out, 21 days ago. He has run over today's trip and going, though 161 lb is a stiff burden off 117.
- Inoui Machin (hrs_32709600) | 8yo G | 159lb | OR 115 | draw 0 | jockey Bradley Harris(3) | trainer Neil Mulholland (14d 7/28) | headgear p | last run 730 days | form 13132/ | MARKET 3.1% | 09:00 median 23.00 | Matchbook 38.00
    comment: Inoui Machin has a strong recent profile, finishing second last time out, third two starts back and a winner three starts back, and he has run over today's trip and going. The main risk is a 730-day absence, while 159 lb is a hefty burden against an official mark of 115.
- Corsican Caper (hrs_31698016) | 6yo G | 147lb | OR 103 | draw 0 | jockey Lee Edwards | trainer Kevin & Lauren Frost (14d 0/9) | headgear - | last run 18 days | form 734-31 | MARKET 2.2% | 09:00 median 29.00 | Matchbook 65.00
    comment: Corsican Caper won last time out and was third two starts back, with a fresh 18-day turnaround and previous experience of today's trip and going, but he carries 147 lb off 103.
- Bold Endeavour (hrs_22625414) | 10yo G | 160lb | OR 116 | draw 0 | jockey David Noonan | trainer Chris Honour (14d 0/5) | headgear b (1st time) | last run 21 days | form P-0640 | MARKET 1.8% | 09:00 median 36.00 | Matchbook 70.00
- Our Dylan (hrs_24555482) | 10yo G | 157lb | OR 113 | draw 0 | jockey Ben Godfrey | trainer Kayley Woollacott (14d 0/7) | headgear - | last run 210 days | form 31913- | MARKET 1.8% | 09:00 median 34.00 | Matchbook 90.00

## 2:00 Windsor | race_id rac_32304466077 | Listen Live To Track Radio Mares' Handicap Hurdle Race
Hurdle | Class 5 | 2m4f0y | going Good | Turf | 12 runners | rating band 0-100 | age 4yo+
- Independent Lady (hrs_50936032) | 5yo M | 166lb | OR 95 | draw 0 | jockey Freddie Gordon | trainer Nicky Henderson (14d 5/15) | headgear - | last run 29 days | form 8814-2 | MARKET 30.8% | 09:00 median 2.63 | Matchbook 2.96
- Barafundle Bay (hrs_37275357) | 5yo M | 149lb | OR 78 | draw 0 | jockey Jack Tudor | trainer Christian Williams (14d 0/10) | headgear - | last run 32 days | form -78041 | MARKET 12.4% | 09:00 median 6.00 | Matchbook 8.00
    comment: Barafundle Bay won last time out, but that came after a fourth two starts back and a run of unplaced efforts before it, so she is hard to fancy after a 32-day break.
- Shanagolden Girl (hrs_40786403) | 6yo M | 162lb | OR 91 | draw 0 | jockey Adam Wedge | trainer Emma Lavelle (14d 2/15) | headgear - | last run 16 days | form 0957-4 | MARKET 9.7% | 09:00 median 8.50 | Matchbook 9.40
    comment: Fourth last time out, 16 days ago, is her best recent effort, and she has run over today's trip, but she is winless in her last five and carries 162 lb off an official mark of 91.
- Mavis Pike (hrs_33302654) | 7yo M | 168lb | OR 97 | draw 0 | jockey Amber Jackson-Fennell(7) | trainer Nigel & Willy Twiston-Davies (14d 6/36) | headgear - | last run 19 days | form 5FU-32 | MARKET 7.9% | 09:00 median 10.00 | Matchbook 12.50
    comment: Mavis Pike arrives in good heart after a second last time out and a third the start before, and at 19 days since her last run she should be fit.
- Eliza Dolittle (hrs_30865751) | 8yo M | 153lb | OR 82 | draw 0 | jockey Tabitha Worsley | trainer Nick Gifford (14d 0/7) | headgear - | last run 26 days | form 166-33 | MARKET 7.5% | 09:00 median 9.50 | Matchbook 14.00
    comment: Eliza Dolittle has finished third in her last two starts and has run over today's trip and going, but she is winless since a victory five starts back, with two sixths in between.
- Border Gem (hrs_47475190) | 6yo M | 160lb | OR 89 | draw 0 | jockey Rex Dingle | trainer Jeremy Scott (14d 1/7) | headgear - | last run 24 days | form 525-54 | MARKET 6.8% | 09:00 median 12.00 | Matchbook 14.00
    comment: Border Gem is consistent without being a threat to win, finishing fourth last time out and fifth twice in her last five, with a second four starts back her best effort. She has run over today's trip and going, and 24 days off is fine, but she is winless in that spell and carries 160 lb.
- Mistress Fox (hrs_40186384) | 6yo M | 155lb | OR 84 | draw 0 | jockey Bradley Harris(3) | trainer Neil Mulholland (14d 7/28) | headgear ht | last run 157 days | form 884-27 | MARKET 6.0% | 09:00 median 13.00 | Matchbook 17.00
    comment: Mistress Fox is winless in her last five and was beaten into seventh last time, and returns from a 157-day break, so she's hard to fancy under 155 lb. A second two starts back and experience of today's trip and going are the best points in her favour.
- Morissette (hrs_45445372) | 6yo M | 161lb | OR 90 | draw 0 | jockey Ben Jones | trainer Dean Summersby (14d 0/1) | headgear - | last run 30 days | form 53-466 | MARKET 6.0% | 09:00 median 11.00 | Matchbook 20.00
    comment: The risk is a winless run in her last five, including sixths in her last two outings, with 161 lb to carry.
- Sophie Power (hrs_46265548) | 5yo M | 160lb | OR 89 | draw 0 | jockey Isabelle Ryder(5) | trainer Harriet Dickin (14d 0/7) | headgear ht | wind surgery | last run 217 days | form 158P6- | MARKET 5.6% | 09:00 median 15.00 | Matchbook 17.00
    comment: Sophie Power was sixth last time out and has been pulled up and beaten in the interim since her win five starts back, while a 217-day absence raises fitness questions.
- Mrs Biddle (hrs_34665659) | 8yo M | 158lb | OR 87 | draw 0 | jockey Ben Godfrey | trainer Kayley Woollacott (14d 0/7) | headgear t | last run 83 days | form 7025-P | MARKET 3.7% | 09:00 median 23.00 | Matchbook 27.00
    comment: Mrs Biddle was pulled up last time out and has been off for 83 days, so she is hard to fancy, yet she has run over today's trip and going and was second three starts back.
- Dalcassian Girl (hrs_49578200) | 6yo M | 149lb | OR 78 | draw 0 | jockey David Noonan | trainer Chris Honour (14d 0/5) | headgear p (1st time) | last run 16 days | form 0562-4 | MARKET 2.5% | 09:00 median 27.50 | Matchbook 55.00
    comment: Yet to win in her last five, she must still shoulder 149 lb, the main risk.
- Georgie's Lady (hrs_63357364) | 4yo F | 160lb | OR 90 | draw 0 | jockey Rian Corcoran(5) | trainer David Dennis (14d 0/2) | headgear - | last run 13 days | form -9645U | MARKET 1.2% | 09:00 median 41.00 | Matchbook 170.00
    comment: Georgie's Lady unseated last time out, but she was fifth and fourth in the two runs before that and is back quickly after just 13 days, with experience of today's going. She is winless in her last five and carries 160 lb off 90, which holds her back.

## 2:35 Windsor | race_id rac_32304468014 | Join Fitzdares For A Personal Service Handicap Steeple Chase (GBB Race)
Chase | Class 4 | 2m6f50y | going Good | Turf | 8 runners | rating band 0-115 | age 4yo+
- King Califet (hrs_38002454) | 7yo G | 168lb | OR 114 | draw 0 | jockey Ben Jones | trainer Emma Lavelle (14d 2/15) | headgear - | last run 239 days | form 4/841- | MARKET 39.7% | 09:00 median 2.20 | Matchbook 2.34
    comment: King Califet bounces in off a win last time out, and he has run over today's trip, so he looks a strong threat under 168 lb. The one concern is a long 239-day absence, which leaves fitness an open question.
- Doctor Midas (hrs_40805576) | 6yo G | 157lb | OR 103 | draw 0 | jockey Adam Wedge | trainer Henrietta C Knight (14d 1/7) | headgear t (1st time) | wind surgery | last run 262 days | form /3283- | MARKET 10.9% | 09:00 median 8.00 | Matchbook 8.60
    comment: Doctor Midas was third last time out and has finished in the first three in three of his last four starts, yet he is winless in that spell and returns after 262 days off.
- Jet Smart (hrs_29522682) | 8yo G | 162lb | OR 108 | draw 0 | jockey Rian Corcoran(5) | trainer Dean Summersby (14d 0/1) | headgear p | last run 32 days | form -22232 | MARKET 10.1% | 09:00 median 8.00 | Matchbook 10.00
    comment: Jet Smart has been a consistent sort, finishing second last time out and filling the places in all five recent starts, though he is yet to win.
- Le Galli Bier (hrs_50187809) | 5yo G | 156lb | OR 102 | draw 0 | jockey Caoilin Quinn | trainer Jamie Moore & Josh Moore (14d 5/25) | headgear t | last run 232 days | form 22U35- | MARKET 10.1% | 09:00 median 8.50 | Matchbook 9.80
    comment: Winless in his last five and absent 232 days, Le Galli Bier is hard to fancy, though a fifth last time out, a third two starts back and a pair of seconds earlier show he is no back number, and he has run on today's going.
- Loki's Mischief (hrs_37933672) | 6yo G | 161lb | OR 107 | draw 0 | jockey Jack Stenhouse(7) | trainer Chester Williams (14d 0/4) | headgear - | last run 16 days | form 2-1174 | MARKET 9.4% | 09:00 median 9.00 | Matchbook 10.50
    comment: Loki's Mischief won two of his last five, taking victories three and four starts back, and fourth last time out after just 16 days suggests he's fit.
- Dangerous Touch (hrs_35430682) | 7yo G | 163lb | OR 109 | draw 0 | jockey Tom Hutsby(10) | trainer Olly Murphy (14d 8/41) | headgear tp | wind surgery | last run 223 days | form 3F222- | MARKET 9.3% | 09:00 median 8.50 | Matchbook 11.50
    comment: Runner-up in each of his last three starts, Dangerous Touch has been knocking on the door but remains winless in recent form, and a 223-day layoff raises fitness questions.
- Joe Cotton (hrs_32568613) | 8yo G | 163lb | OR 109 | draw 0 | jockey Lorcan Williams | trainer Jeremy Scott (14d 1/7) | headgear v | wind surgery | last run 273 days | form 3327P- | MARKET 8.0% | 09:00 median 9.50 | Matchbook 13.50
    comment: Joe Cotton showed solid form earlier in his recent run, with a second three starts back and a third four and five starts back, and he has run over today's trip and going before. The big risk is fitness, as he was pulled up last time out and returns after 273 days off.
- Diligent Militia (hrs_41052277) | 7yo G | 158lb | OR 104 | draw 0 | jockey Rex Dingle | trainer Tim Vaughan (14d 0/8) | headgear tp | wind surgery | last run 194 days | form 5P44-P | MARKET 2.5% | 09:00 median 29.00 | Matchbook 48.00
    comment: Diligent Militia is hard to fancy: pulled up last time out and has been off 194 days since, and winless in his last five, with a pulled up four starts back too. He has run on today's going and posted a fourth two starts back, but 158 lb is a burden.

## 3:10 Windsor | race_id rac_32304469951 | Cutler And Gross Handicap Hurdle Race
Hurdle | Class 3 | 2m0f0y | going Good | Turf | 11 runners | rating band 0-125 | age 3yo+
- Zarakerjack (hrs_49821576) | 4yo G | 145lb | OR 102 | draw 0 | jockey Freddie Mitchell(3) | trainer Jamie Moore & Josh Moore (14d 5/25) | headgear - | last run 9 days | form 23P-1 | MARKET 24.7% | 09:00 median 3.50 | Matchbook 3.85 | CHECK (skip line 3.32)
    comment: Zarakerjack won last time out and has run over today's trip and going, but a pulled up two starts back and a quick 9-day turnaround raise questions, while 145 lb is a hefty burden.
- Secret Squirrel (hrs_34401871) | 7yo G | 169lb | OR 126 | draw 0 | jockey Tom Cannon | trainer Hughie Morrison (14d 0/6) | headgear - | last run 10 days | form F/305- | MARKET 21.7% | 09:00 median 4.00 | Matchbook 4.40
    comment: Secret Squirrel is fit and fresh enough after ten days off, a fifth last time out following a third three starts back, and he has run over today's trip and going before.
- Watamu (hrs_46547179) | 5yo M | 169lb | OR 126 | draw 0 | jockey Adam Wedge | trainer Emma Lavelle (14d 2/15) | headgear - | last run 28 days | form 13P1-1 | MARKET 12.7% | 09:00 median 7.00 | Matchbook 7.60
    comment: Watamu arrives in cracking form, a winner last time out and two starts back, with three wins in her last five, and she has run over today's trip and going before.
- Misterdoc (hrs_58033402) | 4yo G | 168lb | OR 125 | draw 0 | jockey Liam Harrison | trainer Dan Skelton (14d 19/92) | headgear - | last run 28 days | form 2411-2 | MARKET 8.7% | 09:00 median 9.50 | Matchbook 11.50
    comment: Misterdoc heads in bang in form, a second last time out after back-to-back wins two and three starts back, and he has run over today's trip and on this going before. The risk is 168 lb on a mark of 125, which leaves him plenty to carry.
- Kapitein Kool (hrs_47685022) | 5yo G | 160lb | OR 117 | draw 0 | jockey Benjamin Macey(5) | trainer Seamus Mullins (14d 3/11) | headgear - | last run 22 days | form 170-33 | MARKET 8.3% | 09:00 median 10.00 | Matchbook 12.00
    comment: Kapitein Kool arrives in solid shape, a third last time out and another third two starts back after 22 days off, and he has run over today's trip and going before.
- Anniversary (hrs_43892450) | 4yo G | 157lb | OR 114 | draw 0 | jockey Callum Pritchard | trainer Philip Hobbs & Johnson White (14d 0/17) | headgear - | last run 26 days | form 12 | MARKET 7.4% | 09:00 median 11.00 | Matchbook 14.00
    comment: Anniversary arrives in good heart with a second last time out and a win two starts back, and he has run over today's trip and going before.
- Fasol (hrs_29785504) | 7yo G | 161lb | OR 118 | draw 0 | jockey Freddie Gingell | trainer Paul Nicholls (14d 5/31) | headgear tb | last run 14 days | form 43-364 | MARKET 6.5% | 09:00 median 12.00 | Matchbook 16.00
    comment: Fasol arrives fit after 14 days off, with a fourth last time out and a pair of thirds in his last five, and he has run over today's trip and going before. Carrying 161 lb is the main risk, as he's yet to win in that spell.
- Moves Like Mason (hrs_46913545) | 6yo G | 144lb | OR 101 | draw 0 | jockey Ben Jones | trainer Ben Pauling (14d 4/21) | headgear - | last run 15 days | form /774-2 | MARKET 6.3% | 09:00 median 13.00 | Matchbook 16.00
    comment: He has run over today's trip and going, but 144 lb is a big burden.
- Into The Park (hrs_34860175) | 7yo G | 155lb | OR 112 | draw 0 | jockey Sean Clarke(7) | trainer Max Comley (14d 3/12) | headgear - | last run 35 days | form 347-4P | MARKET 1.6% | 09:00 median 66.00 | Matchbook 55.00
    comment: The risk is a pulled-up last time out, and he carries 155 lb after 35 days off.
- Demoiselle Kap (hrs_29855175) | 8yo M | 143lb | OR 100 | draw 0 | jockey Roisin Leech(7) | trainer Sophie Leech (14d 0/2) | headgear - | wind surgery | last run 144 days | form 53-295 | MARKET 1.1% | 09:00 median 81.00 | Matchbook 100.00
    comment: Fifth last time out and a second three starts back show Demoiselle Kap can get involved, and she has run over today's trip and going, but she is yet to win in her last five starts and returns after 144 days off.
- Tunisya (hrs_60089806) | 4yo F | 151lb | OR 108 | draw 0 | jockey Jack Tudor | trainer Faye Bramley (14d 0/14) | headgear - | last run 21 days | form 140-7 | MARKET 1.1% | 09:00 median 51.00 | Matchbook 200.00
    comment: Tunisya is hard to fancy after a seventh last time out and an unplaced run before that, with her win now four starts back, though she has run over today's trip and returns after 21 days.

## 3:45 Windsor | race_id rac_32304471888 | Download The Fitzdares App "Junior" National Hunt Flat Race (GBB Race)
NH Flat | Class 5 | 2m0f0y | going Good | Turf | 9 runners | rating band - | age 3yo
- Waverley (hrs_17395410270) | 3yo G | 156lb | OR - | draw 0 | jockey Tom Cannon | trainer Alan King (14d 1/18) | headgear h (1st time) | last run - days | form - | MARKET 20.8% | 09:00 median 4.00 | Matchbook 4.50 | CHECK (skip line 3.80)
    comment: Unraced and still a blank canvas, Waverley makes his debut with no form to go on, so he is wholly unexposed and open to improvement.
- New Addington Boy (hrs_17395406098) | 3yo G | 156lb | OR - | draw 0 | jockey Caoilin Quinn | trainer Jamie Moore & Josh Moore (14d 5/25) | headgear - | last run - days | form - | MARKET 19.0% | 09:00 median 4.50 | Matchbook 4.80
    comment: Unraced and unexposed, New Addington Boy makes his debut with no form to go on, so there's plenty of scope for improvement.
- Noe Le Dun (hrs_17395407141) | 3yo G | 156lb | OR - | draw 0 | jockey Lorcan Williams | trainer Chester Williams (14d 0/4) | headgear - | last run - days | form - | MARKET 16.0% | 09:00 median 5.00 | Matchbook 6.00
    comment: Noe Le Dun is an unexposed debutant with no recorded form to go on, so he's open to improvement, though he's a blank slate carrying 156 lb. Lightly raced is an understatement, and he is one to learn about on the day.
- Folkham (hrs_17395404012) | 3yo G | 156lb | OR - | draw 0 | jockey Ben Jones | trainer Jonathan Portman (14d 1/11) | headgear - | last run - days | form - | MARKET 10.8% | 09:00 median 7.50 | Matchbook 9.00
    comment: Folkham is totally unexposed, with no recorded form to go on, so this gelding's debut is a leap into the unknown and there should be scope for improvement. He carries 156 lb, and he is yet to win.
- Hosiery (hrs_17395405055) | 3yo G | 156lb | OR - | draw 0 | jockey Jack Tudor | trainer Syd Hosie (14d 2/7) | headgear - | last run - days | form - | MARKET 10.2% | 09:00 median 8.50 | Matchbook 9.00
    comment: Hosiery is an unraced debutant with no form to go on, so he's unexposed and open to improvement. He carries 156 lb on his first start, and any progress would be a bonus.
- By Your Leave (hrs_17395402969) | 3yo C | 156lb | OR - | draw 0 | jockey Adam Wedge | trainer Alex Hales (14d 0/10) | headgear - | last run - days | form - | MARKET 7.9% | 09:00 median 11.00 | Matchbook 11.50
    comment: By Your Leave is an unraced colt with no form to go on, so he is wholly unexposed and open to improvement. He carries 156 lb, and his debut will show what he has learned at home.
- Victory V (hrs_17395409227) | 3yo G | 156lb | OR - | draw 0 | jockey Ciaran Gethings | trainer Robert Stephens (14d 1/7) | headgear - | last run - days | form - | MARKET 5.4% | 09:00 median 15.00 | Matchbook 18.50
    comment: Unexposed debutant with no recorded form to lean on, so he's open to any amount of improvement; he carries 156 lb, and it's a case of taking him on trust first time out.
- James Dean (hrs_17393318012) | 3yo G | 156lb | OR - | draw 0 | jockey Sean Houlihan | trainer Pat Phelan (14d 1/4) | headgear - | last run 39 days | form 5 | MARKET 5.2% | 09:00 median 17.00 | Matchbook 18.00
    comment: He carries 156 lb, a fair weight to shoulder, though he is yet to win in his recent form.
- Arco Sancho (hrs_17391714921) | 3yo G | 156lb | OR - | draw 0 | jockey I. J. Power | trainer Ivan Furtado (14d 1/9) | headgear - | wind surgery | last run - days | form - | MARKET 4.6% | 09:00 median 19.00 | Matchbook 21.00
    comment: Arco Sancho is totally unexposed, with no recorded form to go on, so this gelding is open to plenty of improvement on debut. He carries 156 lb, and the lack of a public run leaves plenty to learn.
