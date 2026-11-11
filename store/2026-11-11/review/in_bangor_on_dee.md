# Card review packet: Bangor-on-Dee, 2026-11-11

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
{"meeting": "bangor_on_dee", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 12:30 Bangor-on-Dee | race_id rac_32304148409 | Overton Handicap Steeple Chase (GBB Race)
Chase | Class 3 | 2m4f72y | going Good | Turf | 5 runners | rating band 0-130 | age 4yo+
- Wandering Ego (hrs_40352459) | 6yo G | 163lb | OR 121 | draw 0 | jockey Sean Bowen | trainer Olly Murphy (14d 8/36) | headgear - | last run 28 days | form 3219-4 | MARKET 30.5% | 09:00 median 3.00 | Matchbook 3.20 | CHECK (skip line 2.85)
    comment: Wandering Ego arrives fresh off a 28-day break with a fourth last time out, and he has a win three starts back plus a second four starts back and a third five starts back.
- Chuggy (hrs_40473482) | 6yo G | 167lb | OR 125 | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 20/94) | headgear - | last run 242 days | form 11125- | MARKET 26.6% | 09:00 median 3.25 | Matchbook 3.80
- Laguna Beach (hrs_51434285) | 5yo G | 168lb | OR 126 | draw 0 | jockey Nico de Boinville | trainer Nicky Henderson (14d 3/13) | headgear - | last run 207 days | form 312P7- | MARKET 23.4% | 09:00 median 4.00 | Matchbook 4.00
    comment: Laguna Beach showed his best with a win four starts back and a second three starts back, and he has run over today's trip, so he has the ability to figure at 168 lb. The main risk is fitness, as he returns after 207 days off following a seventh last time out.
- Bowenspark (hrs_32853135) | 8yo G | 161lb | OR 119 | draw 0 | jockey Stan Sheppard | trainer Henry Daly (14d 2/9) | headgear - | last run 204 days | form 25154- | MARKET 14.2% | 09:00 median 6.50 | Matchbook 7.00
    comment: The main risk is a 204-day absence, and he also carries a hefty 161 lb.
- Supreme George (hrs_39431742) | 6yo G | 154lb | OR 112 | draw 0 | jockey Theo Gillard | trainer Donald McCain (14d 0/25) | headgear - | last run 26 days | form 21-552 | MARKET 5.3% | 09:00 median 17.00 | Matchbook 19.50
    comment: Supreme George showed up well when second last time out, and he has a win four starts back, but two fifths in between and a yard going 0/25 in the last fortnight make him hard to fancy.

## 1:00 Bangor-on-Dee | race_id rac_32304150346 | Yorton Mares' Novices' Steeple Chase (Listed Race) (For The Richard Aston Memorial Trophy) (GBB Race)
Chase | Class 1 | 2m1f77y | going Good | Turf | 8 runners | rating band - | age 4yo+
- Mighty Fleur (hrs_40959219) | 6yo M | 156lb | OR 124 | draw 0 | jockey Sean Bowen | trainer Mickey Bowen (14d 3/18) | headgear p | last run 30 days | form 2-1111 | MARKET 22.1% | 09:00 median 3.75 | Matchbook 4.50 | CHECK (skip line 3.56)
- Jubilee Alpha (hrs_39109567) | 7yo M | 156lb | OR 137 | draw 0 | jockey Lorcan Williams | trainer Faye Bramley (14d 1/17) | headgear - | last run 243 days | form 2522P- | MARKET 19.4% | 09:00 median 4.42 | Matchbook 5.00
- Siog Geal (hrs_38666446) | 7yo M | 156lb | OR 127 | draw 0 | jockey Kielan Woods | trainer Fergal O'Brien (14d 3/27) | headgear - | last run 241 days | form /3252- | MARKET 13.8% | 09:00 median 6.50 | Matchbook 6.80
- Sunset Marquesa (hrs_37659034) | 7yo M | 156lb | OR 129 | draw 0 | jockey Dylan Johnston | trainer Joe Tizzard (14d 5/25) | headgear t | last run 235 days | form 143F2- | MARKET 12.7% | 09:00 median 7.00 | Matchbook 7.40
- Piper Park (hrs_34073361) | 7yo M | 156lb | OR 128 | draw 0 | jockey Stan Sheppard | trainer Tom Lacey (14d 4/14) | headgear t | last run 243 days | form 36/26- | MARKET 12.4% | 09:00 median 7.00 | Matchbook 7.80
- Onefournine (hrs_40493908) | 6yo M | 156lb | OR 120 | draw 0 | jockey Jonjo O'Neill Jr. | trainer Jonjo & A.J. O'Neill (14d 4/41) | headgear - | last run 32 days | form 2201-1 | MARKET 10.2% | 09:00 median 8.50 | Matchbook 9.40
- Getawhisky (hrs_45887688) | 6yo M | 156lb | OR 119 | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 20/94) | headgear p (1st time) | last run 26 days | form F145-2 | MARKET 6.8% | 09:00 median 13.00 | Matchbook 14.00
- Merely A Detail (hrs_46914112) | 5yo M | 156lb | OR 114 | draw 0 | jockey Tom Cannon | trainer Toby Bulgin (14d 0/3) | headgear - | last run 11 days | form 41V134 | MARKET 2.6% | 09:00 median 34.00 | Matchbook 42.00

## 1:30 Bangor-on-Dee | race_id rac_32304152283 | Weatherbys & Birdie Calendars Handicap Steeple Chase (GBB Race)
Chase | Class 2 | 3m0f30y | going Good | Turf | 5 runners | rating band 0-150 | age 4yo+
- First Confession (hrs_38203130) | 7yo G | 164lb | OR 131 | draw 0 | jockey Dylan Johnston | trainer Joe Tizzard (14d 5/25) | headgear - | last run 246 days | form 35F10- | MARKET 27.6% | 09:00 median 3.25 | Matchbook 3.60 | CHECK (skip line 3.09)
    comment: The main risk is a 246-day absence, with an unplaced run last time out.
- Broomfields Cave (hrs_27794137) | 9yo G | 156lb | OR 123 | draw 0 | jockey Bradley Harris(3) | trainer Neil Mulholland (14d 6/25) | headgear p | last run 201 days | form 31P13- | MARKET 24.2% | 09:00 median 3.75 | Matchbook 4.00
    comment: Third last time out and a winner two starts back, but Broomfields Cave has been off for 201 days and carries 156 lb off an official mark of 123.
- Blenkinsop (hrs_27551125) | 9yo G | 157lb | OR 124 | draw 0 | jockey Ciaran Gethings | trainer Henry Daly (14d 2/9) | headgear - | last run 320 days | form 0/516- | MARKET 18.6% | 09:00 median 5.00 | Matchbook 5.20
    comment: The main risk is a 320-day absence, with a sixth last time out leaving fitness the big question.
- Jupiter Allen (hrs_32472671) | 7yo G | 157lb | OR 124 | draw 0 | jockey Lorcan Williams | trainer Chester Williams (14d 0/5) | headgear p | last run 32 days | form 231P-0 | MARKET 18.3% | 09:00 median 5.00 | Matchbook 5.40
    comment: Jupiter Allen showed his hand with a win three starts back and had been placed second and third in the two runs before it, while he has run over today's trip and going before. The risk is a poor recent run, unplaced last time and pulled up the start before, under a hefty 157 lb.
- Arizona Cardinal (hrs_21512085) | 10yo G | 165lb | OR 132 | draw 0 | jockey Charlie Hammond | trainer Stuart Edmunds (14d 1/11) | headgear tp (1st time) | last run 648 days | form 11P80/ | MARKET 11.2% | 09:00 median 8.45 | Matchbook 8.60
    comment: Arizona Cardinal won twice in his last five starts, a win four starts back and another five starts back, and he has run over today's trip and going before.

## 2:05 Bangor-on-Dee | race_id rac_32304154220 | Bangor-On-Dee Memberships Now On Sale EBF Junior 'National Hunt' Hurdle Race (GBB Race)
Hurdle | Class 4 | 2m0f145y | going Good | Turf | 7 runners | rating band - | age 3yo
- Rockson Piel (hrs_17395275723) | 3yo G | 154lb | OR - | draw 0 | jockey Paul O'Brien | trainer Harry Derham (14d 5/21) | headgear - | last run - days | form - | MARKET 27.5% | 09:00 median 3.25 | Matchbook 3.45 | CHECK (skip line 3.09)
    comment: Rockson Piel is an unexposed debutant with no recorded form to go on, so he's an open book and could well improve for the experience. He carries 154 lb on his first outing.
- Agafay (hrs_17395269465) | 3yo G | 154lb | OR - | draw 0 | jockey Sean Bowen | trainer Warren Greatrex (14d 2/16) | headgear - | last run - days | form - | MARKET 27.3% | 09:00 median 3.00 | Matchbook 3.70
    comment: Agafay is an unraced gelding with no form to go on, so he is wholly unexposed and open to improvement. He carries 154 lb on debut, and there is nothing yet to say about distance or ground.
- Fika (hrs_17395271551) | 3yo G | 154lb | OR - | draw 0 | jockey Dylan Johnston | trainer Sam Thomas (14d 1/6) | headgear t (1st time) | wind surgery | last run - days | form - | MARKET 15.9% | 09:00 median 5.50 | Matchbook 6.00
    comment: Fika is unexposed on debut, so there's no form to lean on and he's open to any amount of improvement. He carries 154 lb, and this first run should reveal plenty about what he can do.
- Notre Jacques (hrs_17395274680) | 3yo G | 154lb | OR - | draw 0 | jockey Ciaran Gethings | trainer Mrs Jane Williams (14d 1/7) | headgear - | last run - days | form - | MARKET 14.5% | 09:00 median 6.00 | Matchbook 6.80
    comment: Notre Jacques is unexposed with no recorded form to go on, so this gelding is open to improvement on debut. He carries 154 lb, and with nothing to weigh him against, his first outing is all about what he shows.
- Bump And Run (hrs_17395270508) | 3yo G | 154lb | OR - | draw 0 | jockey Stan Sheppard | trainer Clive Boultbee-Brooks (14d 0/4) | headgear - | last run - days | form - | MARKET 8.8% | 09:00 median 10.00 | Matchbook 11.00
    comment: Bump And Run is unexposed, with no recorded form to go on, so this debut leaves him open to plenty of improvement. He carries 154 lb, and he is one to learn about rather than judge.
- Royal Castle (hrs_17395276766) | 3yo G | 154lb | OR - | draw 0 | jockey David Noonan | trainer Nigel Hawke (14d 0/5) | headgear - | last run - days | form - | MARKET 3.1% | 09:00 median 29.00 | Matchbook 34.00
    comment: Royal Castle is an unraced gelding on debut, so he's totally unexposed and open to improvement, with no form to lean on. He carries 154 lb, and his first look at a racecourse will tell us plenty.
- Sam's Reflection (hrs_17395277809) | 3yo G | 154lb | OR - | draw 0 | jockey Jack Quinlan | trainer Ben Case (14d 1/8) | headgear h (1st time) | last run - days | form - | MARKET 2.8% | 09:00 median 34.00 | Matchbook 34.00
    comment: Sam's Reflection is unraced and yet to show anything on a racecourse, so he is entirely unexposed and open to improvement. He carries 154 lb on debut, and with no form to judge, any step forward would be a bonus.

## 2:35 Bangor-on-Dee | race_id rac_32304156157 | Paul Ferguson's Jumpers To Follow Novices' Hurdle Race (GBB Race)
Hurdle | Class 4 | 2m0f145y | going Good | Turf | 7 runners | rating band - | age 4yo+
- Alcarath (hrs_55273155) | 4yo G | 154lb | OR - | draw 0 | jockey Tom Bellamy | trainer Alan King (14d 1/19) | headgear - | last run 46 days | form - | MARKET 53.6% | 09:00 median 1.67 | Matchbook 1.77
- Frost Moon (hrs_51557996) | 5yo M | 147lb | OR - | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 20/94) | headgear - | last run 21 days | form 1/84-3 | MARKET 20.0% | 09:00 median 4.33 | Matchbook 4.90
- Sky Grove (hrs_52709846) | 5yo G | 161lb | OR - | draw 0 | jockey Bryan Carver | trainer Laura Horsfall (14d 0/4) | headgear h | last run 20 days | form 623-15 | MARKET 13.9% | 09:00 median 6.50 | Matchbook 6.80
- Hang Out (hrs_17394658267) | 5yo G | 154lb | OR - | draw 0 | jockey Theo Gillard | trainer Donald McCain (14d 0/25) | headgear - | last run 256 days | form 1- | MARKET 7.1% | 09:00 median 9.50 | Matchbook 18.00
- Dolly Drama (hrs_52641428) | 5yo M | 147lb | OR - | draw 0 | jockey Peter Kavanagh | trainer Donald McCain (14d 0/25) | headgear - | wind surgery | last run 12 days | form 344-0 | MARKET 3.8% | 09:00 median 26.00 | Matchbook 30.00
- Get Busy Jumping (hrs_17394499731) | 5yo G | 154lb | OR - | draw 0 | jockey Toby Wynne | trainer Oliver Greenall & Josh Guerriero (14d 2/21) | headgear - | last run 15 days | form 8 | MARKET 1.1% | 09:00 median 67.00 | Matchbook 140.00
- Whiteoak Duffy (hrs_53960158) | 5yo G | 154lb | OR - | draw 0 | jockey Lee Edwards | trainer Simon Edwards (14d 0/2) | headgear - | last run 13 days | form 0-89 | MARKET 0.5% | 09:00 median 201.00 | Matchbook 380.00

## 3:05 Bangor-on-Dee | race_id rac_32304158094 | Wrexham Lager Novices' Hurdle Race (GBB Race)
Hurdle | Class 4 | 2m7f32y | going Good | Turf | 4 runners | rating band - | age 4yo+
- Solid Performer (hrs_52495282) | 8yo G | 154lb | OR 116 | draw 0 | jockey Theo Gillard | trainer Donald McCain (14d 0/25) | headgear - | last run 228 days | form 332F4- | MARKET 46.6% | 09:00 median 1.91 | Matchbook 2.14
- Mr Rafiki (hrs_51434334) | 5yo G | 154lb | OR 107 | draw 0 | jockey Jonjo O'Neill Jr. | trainer Jonjo & A.J. O'Neill (14d 4/41) | headgear tp | last run 11 days | form 42FF22 | MARKET 41.7% | 09:00 median 2.25 | Matchbook 2.30
- Captain Connor (hrs_58931145) | 4yo G | 152lb | OR 82 | draw 0 | jockey Dylan Johnston | trainer Clare Ellam (14d 0/2) | headgear - | last run 10 days | form 342352 | MARKET 8.4% | 09:00 median 11.00 | Matchbook 11.50
- Granny B (hrs_29918294) | 6yo M | 147lb | OR 77 | draw 0 | jockey Lewis Stones(3) | trainer Michael Mullineaux (14d 0/3) | headgear h | last run 9 days | form 77635U | MARKET 3.2% | 09:00 median 26.00 | Matchbook 36.00

## 3:35 Bangor-on-Dee | race_id rac_32304160031 | Festive Meeting Saturday 28th November Handicap Hurdle Race (GBB Race)
Hurdle | Class 2 | 2m3f123y | going Good | Turf | 5 runners | rating band 0-145 | age 3yo+
- Brookside La (hrs_46295837) | 6yo G | 154lb | OR 119 | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 20/94) | headgear - | last run 35 days | form 4133-1 | MARKET 31.9% | 09:00 median 2.88 | Matchbook 3.05
- Charisma Cat (hrs_41845636) | 6yo M | 167lb | OR 132 | draw 0 | jockey Tom Bellamy | trainer Alan King (14d 1/19) | headgear - | last run 214 days | form 21216- | MARKET 23.4% | 09:00 median 4.00 | Matchbook 4.10
    comment: Charisma Cat has won two of her last five, with a first two starts back and another four starts back, and has run over today's trip, but a sixth last time out and 214 days off the track are the main risk, with 167 lb to carry.
- Static (hrs_41263607) | 5yo G | 157lb | OR 122 | draw 0 | jockey Theo Gillard | trainer Donald McCain (14d 0/25) | headgear h | last run 26 days | form 110-52 | MARKET 17.9% | 09:00 median 5.00 | Matchbook 5.50
    comment: Static was second last time out, a fifth two starts back, and he won four and five starts back, so he arrives fit after 26 days and has run over today's trip and going. The yard's poor run of form is the one reservation.
- The Cistercian (hrs_53081168) | 6yo G | 159lb | OR 124 | draw 0 | jockey Charlie Hammond | trainer Stuart Edmunds (14d 1/11) | headgear - | wind surgery | last run 231 days | form 3U3U2- | MARKET 13.9% | 09:00 median 6.00 | Matchbook 7.60
    comment: Placed in three of his last five, including a second last time out, The Cistercian is yet to win in that spell and has two unseated rides in it, but he has run on today's going and sits on a workable 124. The main risk is a 231-day absence, with 159 lb to carry.
- Good To Be Alive (hrs_49609042) | 5yo G | 168lb | OR 133 | draw 0 | jockey Sean Bowen | trainer Olly Murphy (14d 8/36) | headgear p (1st time) | last run 214 days | form 2212P- | MARKET 12.8% | 09:00 median 7.00 | Matchbook 7.80
    comment: Good To Be Alive arrives with a winner three starts back, sandwiched by seconds either side, and he has run over today's trip and going before; the one concern is a pulled-up effort last time and a 214-day absence under 168 lb.
