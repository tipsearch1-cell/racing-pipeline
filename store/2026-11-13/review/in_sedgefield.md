# Card review packet: Sedgefield, 2026-11-13

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
{"meeting": "sedgefield", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 12:45 Sedgefield | race_id rac_32304307243 | Lisa Margaret Turner Memorial Handicap Steeple Chase (Go North Monet's Garden Series Qualifier) (GBB Race)
Chase | Class 4 | 2m5f28y | going Good | Turf | 3 runners | rating band 0-115 | age 4yo+
- Walk In The Valley (hrs_34746264) | 7yo G | 154lb | OR 100 | draw 0 | jockey Danny McMenamin | trainer Joel Parkinson & Sue Smith (14d 0/15) | headgear - | last run 19 days | form 8/2-41 | MARKET 46.9% | 09:00 median 1.96 | Matchbook 2.08
    comment: Winner last time out and fresh enough after 19 days, Walk In The Valley also has a second three starts back, and has run over today's trip and going before.
- Fairlawn Skipper (hrs_40996865) | 6yo G | 168lb | OR 114 | draw 0 | jockey Shane Fenelon(5) | trainer Mickey Bowen (14d 3/14) | headgear - | last run 21 days | form 1U1214 | MARKET 33.7% | 09:00 median 2.75 | Matchbook 2.88
    comment: The main risk is top weight of 168 lb after a fourth last time out.
- Glory And Honour (hrs_21212086) | 10yo G | 164lb | OR 110 | draw 0 | jockey Jonathan England | trainer Sam England (14d 4/18) | headgear tb | last run 22 days | form 472363 | MARKET 19.5% | 09:00 median 4.50 | Matchbook 5.20
    comment: Glory And Honour comes here in solid nick, a third last time out and just 22 days ago, with a second four starts back among a consistent profile, and he has run over today's trip and going before.

## 1:20 Sedgefield | race_id rac_32304309180 | Paxtons Northallerton Parts Team Power Performance Novices' Hurdle Race (GBB Race)
Hurdle | Class 4 | 2m5f34y | going Good | Turf | 3 runners | rating band - | age 4yo+
- In The Trenches (hrs_29227114) | 6yo G | 163lb | OR 115 | draw 0 | jockey Sean Quinlan | trainer Jennie Candlish (14d 2/4) | headgear t | last run 30 days | form 1P4712 | MARKET 57.2% | 09:00 median 1.57 | Matchbook 1.75
- Farfromaway (hrs_17394126337) | 5yo G | 156lb | OR - | draw 0 | jockey Danny McMenamin | trainer Joel Parkinson & Sue Smith (14d 0/15) | headgear - | last run 22 days | form 1211-5 | MARKET 41.2% | 09:00 median 2.25 | Matchbook 2.34
- Arcimboldo (hrs_52236345) | 4yo G | 155lb | OR - | draw 0 | jockey Charlie Maggs | trainer Mike Sowersby (14d 0/5) | headgear - | last run 14 days | form P75 | MARKET 1.6% | 09:00 median 51.00 | Matchbook 70.00

## 1:55 Sedgefield | race_id rac_32304303369 | Sedgefield Christmas Jumper Raceday 22nd December Conditional Jockeys' Handicap Hurdle Race (Go North Brindisi Breeze Series Qualifier)
Hurdle | Class 4 | 3m3f9y | going Good | Turf | 5 runners | rating band 0-110 | age 4yo+
- Frisky Whiskey (hrs_58469236) | 5yo M | 166lb | OR 104 | draw 0 | jockey Oakley Brown | trainer Brian Ellison (14d 1/13) | headgear t | last run 42 days | form 664321 | MARKET 38.8% | 09:00 median 2.25 | Matchbook 2.56
    comment: The risk is a 42-day break and a hefty 166 lb on her back.
- Jeteye (hrs_32780258) | 9yo G | 161lb | OR 99 | draw 0 | jockey Tom Midgley(3) | trainer Sam England (14d 4/18) | headgear tb | last run 10 days | form 312151 | MARKET 25.1% | 09:00 median 3.50 | Matchbook 3.90
    comment: Jeteye arrives in cracking form, a winner last time out and three wins in his last six starts, and he's back quickly after just ten days.
- Wee Alki (hrs_44199218) | 7yo G | 168lb | OR 106 | draw 0 | jockey Conor Rabbitt | trainer Susan Corbett (14d 0/5) | headgear tp | last run 50 days | form 2-16P1 | MARKET 16.8% | 09:00 median 5.25 | Matchbook 5.90
    comment: Wee Alki won last time out and has two wins in his last five starts, and he has run over today's trip and going before.
- Last Man d'Arcy (hrs_52055598) | 7yo G | 162lb | OR 100 | draw 0 | jockey Luke Scott(3) | trainer Jennie Candlish (14d 2/4) | headgear - | last run 459 days | form /P886- | MARKET 12.3% | 09:00 median 7.50 | Matchbook 8.00
    comment: Carrying 162 lb off an official mark of 100 is the main risk.
- Simiyann (hrs_35176043) | 6yo G | 143lb | OR 81 | draw 0 | jockey Charlie Maggs | trainer Mike Sowersby (14d 0/5) | headgear t | last run 12 days | form /80-38 | MARKET 7.0% | 09:00 median 13.00 | Matchbook 14.00
    comment: Simiyann is winless in his last four, finishing eighth last time out and a poor eighth four starts back, so he is hard to fancy. A third two starts back and a quick 12-day turnaround, plus experience of today's going, are the best points in his favour.

## 2:30 Sedgefield | race_id rac_32304305306 | Christmas Parties At Sedgefield Racecourse Maiden Hurdle Race (GBB Race)
Hurdle | Class 4 | 2m178y | going Good | Turf | 7 runners | rating band - | age 4yo+
- Military Cross (hrs_56278222) | 4yo G | 158lb | OR 105 | draw 0 | jockey Jonathan England | trainer Sam England (14d 4/18) | headgear t | last run 19 days | form 222 | MARKET 44.5% | 09:00 median 2.00 | Matchbook 2.04
- Carthusian (hrs_52526187) | 4yo G | 158lb | OR - | draw 0 | jockey Sean Quinlan | trainer Jennie Candlish (14d 2/4) | headgear h (1st time) | last run 33 days | form - | MARKET 24.1% | 09:00 median 3.50 | Matchbook 3.95
- Close House (hrs_62425188) | 5yo G | 158lb | OR - | draw 0 | jockey Danny McMenamin | trainer Chris Grant (14d 0/3) | headgear - | wind surgery | last run 45 days | form 3-3 | MARKET 20.0% | 09:00 median 4.00 | Matchbook 5.00
- Champagne Powder (hrs_44232454) | 4yo G | 158lb | OR 99 | draw 0 | jockey Leah Noreci(7) | trainer James Moffatt (14d 0/7) | headgear h | last run 17 days | form 553 | MARKET 4.8% | 09:00 median 19.00 | Matchbook 20.00
- Mac's Max (hrs_58686824) | 4yo G | 158lb | OR - | draw 0 | jockey Richie McLernon | trainer Ben Haslam (14d 1/6) | headgear - | last run 17 days | form 26-54 | MARKET 4.1% | 09:00 median 21.00 | Matchbook 25.00
- Who's The Goat (hrs_65642563) | 6yo G | 158lb | OR - | draw 0 | jockey Joshua Thompson(5) | trainer Micky Hammond (14d 0/13) | headgear - | last run 48 days | form - | MARKET 1.4% | 09:00 median 51.00 | Matchbook 130.00
- Get On Son (hrs_60090191) | 5yo G | 158lb | OR - | draw 0 | jockey Peter Kavanagh | trainer Joel Parkinson & Sue Smith (14d 0/15) | headgear - | last run 34 days | form 0-6 | MARKET 1.2% | 09:00 median 67.00 | Matchbook 110.00

## 3:05 Sedgefield | race_id rac_32304311117 | Paxtons Pity Me Workshop Top Performance Novices' Handicap Steeple Chase (Go North Forgive 'N Forget Series Qualifier)
Chase | Class 5 | 2m3f65y | going Good | Turf | 5 runners | rating band 0-100 | age 4yo+
- Soldier In Mayo (hrs_45855355) | 6yo G | 168lb | OR 97 | draw 0 | jockey Theo Gillard | trainer Donald McCain (14d 2/26) | headgear p (1st time) | last run 14 days | form /1-242 | MARKET 43.9% | 09:00 median 2.10 | Matchbook 2.12
    comment: He has run over today's trip and going, though top weight of 168 lb is the one reservation.
- Alidam (hrs_52741367) | 5yo G | 165lb | OR 94 | draw 0 | jockey I. J. Power | trainer Jennie Candlish (14d 2/4) | headgear ht (1st time) | last run 159 days | form P039-0 | MARKET 22.1% | 09:00 median 4.00 | Matchbook 4.50
    comment: The main risk is that long absence, plus 165 lb on his back.
- Brave Move (hrs_38131359) | 7yo G | 151lb | OR 80 | draw 0 | jockey Charlie Maggs | trainer Rebecca Menzies (14d 1/12) | headgear p | last run 10 days | form 5-8PP3 | MARKET 19.8% | 09:00 median 4.33 | Matchbook 5.10
    comment: The risk is two pulled-up efforts in the two runs before that, with him still winless in his last five.
- Knacker Trapper (hrs_33478809) | 8yo G | 155lb | OR 84 | draw 0 | jockey Oscar Palmer(7) | trainer Andrew Crook (14d 0/4) | headgear - | last run 154 days | form 32-926 | MARKET 8.6% | 09:00 median 10.00 | Matchbook 12.00
    comment: The main risk is a 154-day absence after a sixth last time out.
- Mr Globalist (hrs_26145763) | 7yo G | 143lb | OR 72 | draw 0 | jockey Peter Kavanagh | trainer Lizzie Quinlan (14d 1/11) | headgear p | last run 10 days | form 483656 | MARKET 5.6% | 09:00 median 15.00 | Matchbook 18.50
    comment: He has run over today's trip and going and is back quickly after ten days, but that's about it.

## 3:40 Sedgefield | race_id rac_32304313054 | Catertech North East Ltd Mares' Handicap Hurdle Race
Hurdle | Class 5 | 2m5f34y | going Good | Turf | 6 runners | rating band 0-100 | age 4yo+
- Midnight Bella (hrs_58535281) | 5yo M | 160lb | OR 91 | draw 0 | jockey Danny McMenamin | trainer Joel Parkinson & Sue Smith (14d 0/15) | headgear - | wind surgery | last run 10 days | form 0692-U | MARKET 37.0% | 09:00 median 2.38 | Matchbook 2.62
    comment: The risk is the unseating last time out, plus 160 lb and no win in her last five.
- Stellarmasterpiece (hrs_40942083) | 6yo M | 163lb | OR 94 | draw 0 | jockey Joshua Thompson(5) | trainer Micky Hammond (14d 0/13) | headgear p | last run 39 days | form -11124 | MARKET 21.2% | 09:00 median 4.33 | Matchbook 4.50
    comment: Stellarmasterpiece won three of her last five, and was second two starts back, but she was only fourth last time out and now carries 163 lb off an official mark of 94.
- Leave Her To Me (hrs_30738134) | 8yo M | 164lb | OR 95 | draw 0 | jockey Kielan Woods | trainer David Killahena & Graeme McPherson (14d 5/10) | headgear - | last run 36 days | form 9P-627 | MARKET 17.2% | 09:00 median 5.00 | Matchbook 5.80
- Eremenko (hrs_50936039) | 5yo M | 168lb | OR 99 | draw 0 | jockey Theo Gillard | trainer Donald McCain (14d 2/26) | headgear ht | last run 35 days | form 1P-4F5 | MARKET 10.9% | 09:00 median 8.25 | Matchbook 8.80
    comment: Eremenko heads the ratings and has the pedigree of a winner in her recent form, having won five starts back, with a fifth last time out and a fourth three starts back since. She has run over today's trip and going, though a fall two starts back is the one blemish, and 168 lb is a big weight to carry.
- Khaleesi Queen (hrs_58535267) | 6yo M | 155lb | OR 86 | draw 0 | jockey Sean Quinlan | trainer Micky Hammond (14d 0/13) | headgear h | last run 241 days | form 09955- | MARKET 8.8% | 09:00 median 9.50 | Matchbook 12.00
    comment: The main risk is a 241-day layoff after a winless run of recent starts.
- Strathcatcha (hrs_52641449) | 6yo M | 142lb | OR 71 | draw 0 | jockey Dominic Hislop(7) | trainer Gary Rutherford (14d 1/4) | headgear - | last run 216 days | form 77PP2- | MARKET 5.0% | 09:00 median 16.00 | Matchbook 22.00
    comment: Strathcatcha is winless in her last five and has been pulled up twice in her last three outings, while 216 days off the track is a concern.
