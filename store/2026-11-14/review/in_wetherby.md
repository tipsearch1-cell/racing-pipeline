# Card review packet: Wetherby, 2026-11-14

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
{"meeting": "wetherby", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 12:13 Wetherby | race_id rac_32304446707 | Boyle Sports Novices' Hurdle Race (GBB Race)
Hurdle | Class 3 | 2m3f154y | going Good | Turf | 3 runners | rating band - | age 4yo+
- Loriko (hrs_50809780) | 5yo G | 164lb | OR 132 | draw 0 | jockey Dominic Lewis(10) | trainer Dan Skelton (14d 19/92) | headgear - | last run 11 days | form 211362 | MARKET 67.0% | 09:00 median 1.44 | Matchbook 1.45
- Combs (hrs_43228087) | 4yo G | 159lb | OR 119 | draw 0 | jockey Danny McMenamin | trainer Gordon Elliott (14d 6/41) | headgear tb (1st time) | last run 14 days | form 9-1048 | MARKET 29.5% | 09:00 median 3.23 | Matchbook 3.35
- Some Good Men Gone (hrs_47773915) | 4yo G | 153lb | OR - | draw 0 | jockey Craig Nichol | trainer Jessica Bedi (14d 0/5) | headgear - | last run 14 days | form 6 | MARKET 3.5% | 09:00 median 17.00 | Matchbook 50.00

## 12:48 Wetherby | race_id rac_32304448644 | Boyle Sports Back Yourself Handicap Hurdle Race
Hurdle | Class 3 | 2m5f56y | going Good | Turf | 6 runners | rating band 0-125 | age 3yo+
- The Kalooki Kid (hrs_32568396) | 8yo G | 168lb | OR 124 | draw 0 | jockey Danny McMenamin | trainer Nicky Richards (14d 6/18) | headgear - | wind surgery | last run 229 days | form /456P- | MARKET 33.3% | 09:00 median 2.63 | Matchbook 2.96
- Jericoacoara (hrs_34623190) | 7yo G | 162lb | OR 118 | draw 0 | jockey Brian Hughes | trainer Micky Hammond (14d 0/14) | headgear - | last run 192 days | form 5322-1 | MARKET 24.8% | 09:00 median 3.50 | Matchbook 3.90
    comment: Jericoacoara won last time out and was second twice before that, so he arrives in cracking form, and he has run over today's trip and going before. The one risk is a 192-day absence, plus 162 lb on his back.
- Who's Going (hrs_61684518) | 4yo G | 149lb | OR 106 | draw 0 | jockey Craig Nichol | trainer Gordon Elliott (14d 6/41) | headgear - | last run 102 days | form 080-4 | MARKET 17.2% | 09:00 median 5.00 | Matchbook 5.90
    comment: Without a win in his last four starts and returning after 102 days off, Who's Going is hard to fancy, though a fourth last time out is his best recent effort.
- Shantwopointfive (hrs_37701496) | 8yo M | 164lb | OR 120 | draw 0 | jockey Oscar Palmer(7) | trainer Sam England (14d 6/20) | headgear t | last run 119 days | form P52P-9 | MARKET 14.4% | 09:00 median 6.50 | Matchbook 6.40
    comment: The main risk is a 119-day absence after a ninth last time out.
- Nopresentliketime (hrs_40553681) | 6yo G | 155lb | OR 111 | draw 0 | jockey Charlie Maggs | trainer Chris Grant (14d 0/4) | headgear - | last run 222 days | form 5/254- | MARKET 7.6% | 09:00 median 12.00 | Matchbook 13.00
    comment: The main risk is a 222-day absence, so fitness is a concern, especially under 155 lb.
- Fine Thing (hrs_51831717) | 5yo M | 155lb | OR 111 | draw 0 | jockey Tom Midgley(3) | trainer Sam England (14d 6/20) | headgear - | last run 15 days | form 311430 | MARKET 2.6% | 09:00 median 34.00 | Matchbook 42.00
    comment: In her favour, she has run over today's trip and going, is fresh enough after 15 days, and has a yard in form.

## 1:20 Wetherby | race_id rac_32304450581 | Sebden Steel Celebrating 30 Years In Business Novices' Limited Handicap Steeple Chase (GBB Race)
Chase | Class 3 | 1m7f36y | going Good | Turf | 4 runners | rating band - | age 4yo+
- Spadestep (hrs_40647082) | 7yo G | 146lb | OR 116 | draw 0 | jockey Derek Fox | trainer Lucinda Russell & Michael Scudamore (14d 10/38) | headgear t | wind surgery | last run 237 days | form 22225- | MARKET 31.5% | 09:00 median 3.00 | Matchbook 3.05
    comment: Spadestep arrives with four seconds in his last five starts and has run over today's trip and going, while a yard in form (10 from 38 lately) adds weight to his claims. The main risk is a 237-day absence, and he was only fifth last time out.
- Florida Dreams (hrs_29622432) | 8yo G | 152lb | OR 122 | draw 0 | jockey Brian Hughes | trainer Sandy Thomson (14d 2/11) | headgear - | last run 15 days | form 366-81 | MARKET 28.3% | 09:00 median 3.25 | Matchbook 3.50
    comment: Florida Dreams arrives fresh from a win last time out just 15 days ago, and he has run over today's trip and on this going before.
- Smart Decision (hrs_46602913) | 5yo G | 147lb | OR 117 | draw 0 | jockey Jamie Hamilton | trainer Tim Easterby (14d 2/21) | headgear - | last run 224 days | form 24755- | MARKET 20.7% | 09:00 median 4.50 | Matchbook 4.70
    comment: The main risk is a long layoff after back-to-back fifths.
- Le Beau Madrik (hrs_52021438) | 5yo G | 164lb | OR 134 | draw 0 | jockey Charlie Todd | trainer Dan Skelton (14d 19/92) | headgear - | last run 15 days | form 1P1-92 | MARKET 19.5% | 09:00 median 4.50 | Matchbook 5.20
    comment: Le Beau Madrik arrives fresh from a second last time out, 15 days ago, with two wins in his last five starts, and he has run on today's going before. The one concern is a 164 lb burden, which is a big weight to carry.

## 1:55 Wetherby | race_id rac_32304452518 | Boyle Sports Now Open In Wetherby 'Introductory' Hurdle Race (GBB Race)
Hurdle | Class 2 | 2m0f0y | going Good | Turf | 4 runners | rating band - | age 4yo+
- Velvet Outlaw (hrs_17393787362) | 4yo G | 154lb | OR - | draw 0 | jockey Brian Hughes | trainer Olly Murphy (14d 8/41) | headgear - | last run 30 days | form F-2 | MARKET 60.2% | 09:00 median 1.56 | Matchbook 1.55
    comment: Velvet Outlaw bounced back from a fall with a second last time out, and he returns after 30 days having run over today's trip.
- Static Charm (hrs_58900352) | 5yo G | 154lb | OR - | draw 0 | jockey Joshua Thompson | trainer Micky Hammond (14d 0/14) | headgear - | last run 210 days | form 3430- | MARKET 19.6% | 09:00 median 4.50 | Matchbook 5.20
    comment: Static Charm brings solid recent form, with a third two starts back and a third four starts back, and he has run over today's trip and going before. The one concern is a 210-day absence, which leaves fitness in question under 154 lb.
- Yashin (hrs_26408648) | 7yo G | 154lb | OR - | draw 0 | jockey Conor Rabbitt | trainer Jessica Bedi (14d 0/5) | headgear t | last run 110 days | form /- | MARKET 12.9% | 09:00 median 6.00 | Matchbook 8.80
    comment: Yashin is unexposed with no recorded form to go on, so he is open to improvement. He returns after 110 days off and carries 154 lb, which makes his first showing hard to judge.
- Recobella (hrs_47191424) | 5yo M | 147lb | OR - | draw 0 | jockey Joe Williamson | trainer Philip Kirby (14d 1/15) | headgear - | last run 42 days | form /- | MARKET 7.3% | 09:00 median 13.00 | Matchbook 13.00
    comment: Recobella is unexposed with no recorded form to go on, so any improvement is there to be found. She returns after 42 days off and carries 147 lb, a light-on-evidence profile that keeps her open to progress.

## 2:30 Wetherby | race_id rac_32304454455 | Boyle Sports Handicap Steeple Chase (GBB Race)
Chase | Class 3 | 2m3f85y | going Good | Turf | 5 runners | rating band 0-140 | age 4yo+
- The Bluesman (hrs_37790417) | 7yo G | 160lb | OR 132 | draw 0 | jockey Troy Walsh(10) | trainer Olly Murphy (14d 8/41) | headgear t | wind surgery | last run 213 days | form 1217P- | MARKET 33.2% | 09:00 median 2.75 | Matchbook 2.90
    comment: The Bluesman won twice in his last five starts, including a win three starts back, and he has run over today's trip and going before, while carrying 160 lb off an official mark of 132. The risk is a 213-day absence and a pulled up last time out.
- Palamon (hrs_31479336) | 6yo G | 152lb | OR 124 | draw 0 | jockey Dominic Lewis(10) | trainer Dan Skelton (14d 19/92) | headgear tb | last run 14 days | form 535123 | MARKET 31.1% | 09:00 median 3.00 | Matchbook 3.10
    comment: Palamon arrives in solid form, third last time out, a second two starts back, and a winner three starts back, and he's fresh enough after 14 days. He has run over today's trip and going, though 152 lb is a hefty burden and the main risk.
- Tommy's Oscar (hrs_17756781) | 11yo G | 170lb | OR 142 | draw 0 | jockey Danny McMenamin | trainer Ann Hamilton (14d 2/4) | headgear p | last run 20 days | form 142-42 | MARKET 24.9% | 09:00 median 3.25 | Matchbook 4.30
    comment: Tommy's Oscar comes here in sound form, second last time out and 20 days ago, with a second three starts back and a win five starts back, and he has run over today's trip and going before.
- Geryville (hrs_20049841) | 10yo G | 145lb | OR 117 | draw 0 | jockey Brian Hughes | trainer Micky Hammond (14d 0/14) | headgear b | last run 14 days | form 5135-8 | MARKET 8.4% | 09:00 median 11.00 | Matchbook 12.00
    comment: Geryville was eighth last time out and has been on the slide since a win four starts back, with a fifth two starts back and a third three starts back along the way.
- Gunsight Ridge (hrs_18715319) | 11yo G | 158lb | OR 130 | draw 0 | jockey Charlie Maggs | trainer Mike Sowersby (14d 0/7) | headgear t | last run 119 days | form 476-30 | MARKET 2.5% | 09:00 median 41.00 | Matchbook 42.00
    comment: The risk is a 119-day absence, plus a burden of 158 lb after an unplaced latest run.

## 3:05 Wetherby | race_id rac_32304456392 | Colin Baldwin Memorial Handicap Hurdle Race (Challenger Two Mile Hurdle Series Qualifier)
Hurdle | Class 3 | 2m0f0y | going Good | Turf | 4 runners | rating band 0-135 | age 3yo+
- Centurion's Sister (hrs_46892244) | 6yo M | 151lb | OR 113 | draw 0 | jockey Danny McMenamin | trainer Nicky Richards (14d 6/18) | headgear p | last run 31 days | form -22311 | MARKET 44.4% | 09:00 median 2.10 | Matchbook 2.14
    comment: Centurion's Sister arrives in cracking form, a winner last time out and again two starts back, with a third and two seconds before that, and she has run over today's trip and going. The risk is the 151 lb she must carry after 31 days off.
- Filibustering (hrs_38017595) | 5yo G | 168lb | OR 130 | draw 0 | jockey Ryan Mania | trainer Harry Derham (14d 4/19) | headgear t | last run 14 days | form -11381 | MARKET 29.7% | 09:00 median 3.00 | Matchbook 3.30
    comment: Filibustering has won three of his last five starts, including last time out just 14 days ago, so he arrives fresh and in form.
- Roarin' Success (hrs_32197235) | 6yo M | 142lb | OR 104 | draw 0 | jockey Peter Kavanagh | trainer Donald McCain (14d 2/26) | headgear t | last run 18 days | form 113232 | MARKET 16.0% | 09:00 median 5.50 | Matchbook 6.20
    comment: Roarin' Success arrives in cracking form, a second last time out and a third two starts back, with two wins five and six starts back, and she has run over today's trip and going.
- Down To Business (hrs_52526194) | 4yo G | 150lb | OR 112 | draw 0 | jockey Charlie Todd | trainer Dan Skelton (14d 19/92) | headgear - | last run 42 days | form 45-104 | MARKET 9.9% | 09:00 median 9.00 | Matchbook 10.50
    comment: The risk is a 42-day break under 150 lb, which could leave him a touch short of peak sharpness.

## 3:40 Wetherby | race_id rac_32304458329 | Boyle Sports Conditional Jockeys' Handicap Steeple Chase (Go North Red Rum Series Qualifier) (GBB Race)
Chase | Class 4 | 3m0f45y | going Good | Turf | 6 runners | rating band 0-110 | age 4yo+
- Peckforton Hills (hrs_47064969) | 6yo G | 150lb | OR 91 | draw 0 | jockey Charlie Maggs(3) | trainer Oliver Greenall & Josh Guerriero (14d 0/16) | headgear tp | last run 210 days | form 73222- | MARKET 35.3% | 09:00 median 2.50 | Matchbook 2.76
    comment: Peckforton Hills has been runner-up in each of his last three starts, yet remains without a win in his last five, and a 210-day layoff plus 150 lb off a mark of 91 make him hard to fancy.
- Camarrate (hrs_34845440) | 6yo G | 165lb | OR 106 | draw 0 | jockey Harry Brown(10) | trainer Donald McCain (14d 2/26) | headgear t | last run 29 days | form 61-P22 | MARKET 19.9% | 09:00 median 4.50 | Matchbook 4.90
    comment: Camarrate comes here in cracking nick, runner-up last time out and again two starts back, with a winner four starts back, and he has run over today's trip and on the going before.
- Safe Destination (hrs_28824544) | 8yo G | 165lb | OR 106 | draw 0 | jockey Jamie Brace | trainer Nigel & Willy Twiston-Davies (14d 6/36) | headgear p | last run 29 days | form 26PP-3 | MARKET 16.9% | 09:00 median 5.50 | Matchbook 5.70
    comment: The main risk is a big weight of 165 lb after two pulled-up runs.
- Slaney Opera (hrs_29816514) | 8yo G | 161lb | OR 102 | draw 0 | jockey James Murray(7) | trainer John Wainwright (14d 1/2) | headgear t | last run 14 days | form 5F2312 | MARKET 15.0% | 09:00 median 5.50 | Matchbook 7.00
    comment: Slaney Opera has been in cracking form, second last time out, a winner two starts back, and fresh from a run 14 days ago, with experience of today's trip and going.
- Check The Score (hrs_32682671) | 8yo G | 156lb | OR 97 | draw 0 | jockey Fern O'Brien(3) | trainer Fergal O'Brien (14d 3/28) | headgear p | last run 13 days | form 1/25-6 | MARKET 10.2% | 09:00 median 9.00 | Matchbook 9.60
    comment: The risk is a drift in form, with a sixth last time out and a fifth the run before, under 156 lb.
- Trac (hrs_23380147) | 9yo G | 168lb | OR 109 | draw 0 | jockey Joshua Thompson(3) | trainer Micky Hammond (14d 0/14) | headgear p | last run 237 days | form 25116- | MARKET 2.7% | 09:00 median 34.00 | Matchbook 38.00
    comment: The main risk is a 237-day absence, plus 168 lb on his back.
