# Card review packet: Cheltenham, 2026-11-15

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
{"meeting": "cheltenham", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 12:50 Cheltenham | race_id rac_32304473825 | mallardjewellers.com Maiden Hurdle Race (Novices' Championship Hurdle Series Qualifier) (GBB Race)
Hurdle | Class 2 | 2m0f87y | going Good | Turf | 13 runners | rating band - | age 4yo+
- Mourne Crystal (hrs_17394106520) | 4yo G | 158lb | OR - | draw 0 | jockey Ben Jones | trainer Ben Pauling (14d 4/23) | headgear - | last run 24 days | form 1-3 | MARKET 22.5% | 09:00 median 3.50 | Matchbook 4.40 | CHECK (skip line 3.32)
- Wolf Rayet (hrs_43164576) | 4yo G | 158lb | OR 133 | draw 0 | jockey Robert Dunne | trainer Samuel Drinkwater (14d 1/6) | headgear t | last run 220 days | form 24384- | MARKET 19.3% | 09:00 median 4.50 | Matchbook 4.80
- Lastbutnotleased (hrs_17395087983) | 5yo G | 158lb | OR - | draw 0 | jockey Nico de Boinville | trainer Nicky Henderson (14d 5/16) | headgear - | last run 203 days | form 4F1- | MARKET 17.4% | 09:00 median 5.00 | Matchbook 5.30
- Old Habits (hrs_52236506) | 5yo G | 158lb | OR - | draw 0 | jockey Sean Bowen | trainer Olly Murphy (14d 9/48) | headgear - | last run 31 days | form 3/12-3 | MARKET 16.9% | 09:00 median 4.75 | Matchbook 5.80
- Get Out of My Way (hrs_59275979) | 5yo G | 158lb | OR - | draw 0 | jockey Jack Hogan | trainer Fergal O'Brien (14d 3/28) | headgear - | last run 31 days | form 12-2 | MARKET 9.0% | 09:00 median 9.00 | Matchbook 11.00
- Lion Rose Sivola (hrs_49577997) | 5yo G | 158lb | OR - | draw 0 | jockey Jonjo O'Neill Jr. | trainer Jonjo & A.J. O'Neill (14d 5/33) | headgear - | last run 35 days | form 1/22-2 | MARKET 5.0% | 09:00 median 15.00 | Matchbook 21.00
- En Or (hrs_25325258) | 8yo G | 158lb | OR 125 | draw 0 | jockey Daniel King | trainer A. J. Martin (14d 0/12) | headgear t | last run 57 days | form 703-22 | MARKET 4.5% | 09:00 median 17.00 | Matchbook 23.00
- Super Junior (hrs_59186428) | 5yo G | 158lb | OR - | draw 0 | jockey Harry Cobden | trainer Thomas Cooper (14d 1/2) | headgear - | wind surgery | last run 239 days | form 1P- | MARKET 1.8% | 09:00 median 41.00 | Matchbook 65.00
- Airds Moss (hrs_52236387) | 5yo G | 158lb | OR 115 | draw 0 | jockey Cian Quirke | trainer David Harry Kelly (14d 0/8) | headgear - | last run 41 days | form 2-1445 | MARKET 1.4% | 09:00 median 51.00 | Matchbook 95.00
- Arc Zoosve (hrs_44785979) | 5yo G | 158lb | OR - | draw 0 | jockey Jack Quinlan | trainer Neil King (14d 0/8) | headgear - | last run 25 days | form 4- | MARKET 0.9% | 09:00 median 67.00 | Matchbook 180.00
- Tide Is Turning (hrs_62101564) | 4yo G | 158lb | OR - | draw 0 | jockey Richie McLernon | trainer Neil Mulholland (14d 7/28) | headgear - | last run 25 days | form 3-6 | MARKET 0.7% | 09:00 median 151.00 | Matchbook 160.00
- Island Getaway (hrs_63202769) | 4yo G | 158lb | OR - | draw 0 | jockey Caoilin Quinn | trainer Warren Greatrex (14d 4/22) | headgear - | wind surgery | last run 192 days | form 5-2 | MARKET 0.5% | 09:00 median 126.00 | Matchbook 360.00
- Dernier Set (hrs_64388702) | 4yo G | 158lb | OR - | draw 0 | jockey Kielan Woods | trainer Ben Pauling (14d 4/23) | headgear - | last run 17 days | form 64 | MARKET 0.3% | 09:00 median 251.00 | Matchbook 520.00

## 1:25 Cheltenham | race_id rac_32304475762 | WKD Novices' Limited Handicap Steeple Chase (GBB Race)
Chase | Class 3 | 2m4f44y | going Good | Turf | 11 runners | rating band - | age 4yo+
- Crystal Island (hrs_51558073) | 5yo G | 162lb | OR 133 | draw 0 | jockey Nico de Boinville | trainer Nicky Henderson (14d 5/16) | headgear - | last run 208 days | form 1/11- | MARKET 31.1% | 09:00 median 2.75 | Matchbook 2.96
    comment: Crystal Island has won his last three starts, but he returns after 208 days off and carries 162 lb off an official mark of 133, a lot to ask first time back.
- Pourquoi Pas Papa (hrs_58535015) | 4yo G | 151lb | OR 131 | draw 0 | jockey Sam Twiston-Davies | trainer Paul Nicholls (14d 6/28) | headgear - | last run 32 days | form 1243-2 | MARKET 13.8% | 09:00 median 6.00 | Matchbook 6.80
    comment: Pourquoi Pas Papa arrives in cracking form, second last time out, a third two starts back, and a winner five starts back, so he is consistently in the frame. The main risk is his 151 lb burden, a stiff ask off an official mark of 131.
- Spectacularsunrise (hrs_48112225) | 6yo G | 161lb | OR 132 | draw 0 | jockey Toby McCain-Mitchell(3) | trainer Nigel & Willy Twiston-Davies (14d 5/36) | headgear - | last run 22 days | form 696-1F | MARKET 11.1% | 09:00 median 7.50 | Matchbook 8.60
- Turndlightsdownlow (hrs_49577864) | 6yo G | 156lb | OR 127 | draw 0 | jockey Freddie Keighley(5) | trainer Martin Keighley (14d 2/10) | headgear - | last run 22 days | form 222-2U | MARKET 9.5% | 09:00 median 9.00 | Matchbook 9.60
    comment: Winless in his last five, Turndlightsdownlow was runner-up in four straight before unseating last time, and he has run over today's trip and going before.
- Four Springs (hrs_52709139) | 5yo G | 153lb | OR 124 | draw 0 | jockey Kielan Woods | trainer Ben Pauling (14d 4/23) | headgear - | last run 33 days | form 132P-1 | MARKET 8.0% | 09:00 median 9.25 | Matchbook 13.00
    comment: Fresh from a win last time out, and a second three starts back adds to a solid recent record, though a pulled up two starts back shows he can be inconsistent.
- Dig Deep (hrs_50906142) | 5yo G | 150lb | OR 121 | draw 0 | jockey Ben Jones | trainer Ben Pauling (14d 4/23) | headgear - | last run 246 days | form 22651- | MARKET 7.4% | 09:00 median 10.00 | Matchbook 14.00
    comment: Dig Deep won last time out, with a second five starts back among his better efforts, but 246 days off the track is a big concern and he carries 150 lb.
- The Gray Ghost (hrs_41171844) | 7yo G | 154lb | OR 125 | draw 0 | jockey Charlie Price | trainer Robbie Llewellyn (14d 0/2) | headgear t | last run 15 days | form 144-21 | MARKET 6.5% | 09:00 median 12.00 | Matchbook 15.50
    comment: The Gray Ghost won last time out and was second two starts back, a fresh 15 days ago, and he has run over today's trip and going.
- Bill Joyce (hrs_34361572) | 7yo G | 159lb | OR 130 | draw 0 | jockey Jonjo O'Neill Jr. | trainer Jonjo & A.J. O'Neill (14d 5/33) | headgear - | last run 2 days | form /PP-33 | MARKET 5.7% | 09:00 median 13.00 | Matchbook 18.50
    comment: Bill Joyce arrives in better heart, third last time out and third again two starts back, and he has run over today's trip and on this going before.
- Sony Bill (hrs_40668607) | 5yo G | 152lb | OR 123 | draw 0 | jockey Sean Bowen | trainer Faye Bramley (14d 0/18) | headgear tp (1st time) | last run 22 days | form 33P505 | MARKET 3.7% | 09:00 median 19.00 | Matchbook 32.00
    comment: Sony Bill has run over today's trip and on this going, and he was third in two of his last six, with a fifth last time out 22 days ago.
- Sinchi Roca (hrs_47807144) | 6yo G | 145lb | OR 114 | draw 0 | jockey Bryan Carver | trainer Syd Hosie (14d 2/8) | headgear - | last run 217 days | form 14522- | MARKET 1.7% | 09:00 median 41.00 | Matchbook 70.00
    comment: Sinchi Roca finished second in his last two starts, but he's been off for 217 days and shoulders 145 lb, which is a tall order after such a layoff.
- Captain Cool (hrs_40225059) | 6yo G | 164lb | OR 135 | draw 0 | jockey Sean Quinlan | trainer Jennie Candlish (14d 3/13) | headgear tp | last run 32 days | form 213113 | MARKET 1.6% | 09:00 median 41.00 | Matchbook 80.00
    comment: Captain Cool has finished in the first three in all of his last six starts, with a third last time out and a winner two starts back, and he has run over today's trip and going.

## 2:00 Cheltenham | race_id rac_32304477699 | Weatherite Air Conditioning Handicap Steeple Chase (GBB Race)
Chase | Class 3 | 1m7f199y | going Good | Turf | 10 runners | rating band 0-140 | age 4yo+
- Highlands Legacy (hrs_37407895) | 7yo G | 166lb | OR 137 | draw 0 | jockey Jonjo O'Neill Jr. | trainer Jonjo & A.J. O'Neill (14d 5/33) | headgear - | last run 220 days | form 12212- | MARKET 21.2% | 09:00 median 4.00 | Matchbook 4.60 | CHECK (skip line 3.80)
    comment: Highlands Legacy has been in cracking form, a second last time out, a winner two starts back, and two wins plus three seconds in his last five, and he has run over today's trip and going before.
- Shakeyatailfeather (hrs_34845902) | 7yo M | 152lb | OR 123 | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 19/83) | headgear - | last run 15 days | form 8677-3 | MARKET 14.4% | 09:00 median 6.00 | Matchbook 6.80
    comment: Shakeyatailfeather bounced back with a third last time out, 15 days ago, and has run over today's trip and going, but she is winless in her last five and her sevenths and eighth before that suggest a ceiling.
- Authoceltic (hrs_38174262) | 6yo G | 147lb | OR 118 | draw 0 | jockey Ciaran Gethings | trainer Mrs Jane Williams (14d 1/8) | headgear - | last run 34 days | form 2152-2 | MARKET 13.6% | 09:00 median 6.50 | Matchbook 7.00
    comment: Authoceltic has finished second in his last two starts and won four starts back, so the form is solid, while he has run over today's trip and going.
- Putapoundinthejar (hrs_40225297) | 6yo G | 168lb | OR 139 | draw 0 | jockey Daniel King | trainer A. J. Martin (14d 0/12) | headgear - | last run 1 days | form 311214 | MARKET 10.8% | 09:00 median 8.00 | Matchbook 9.00
    comment: Three wins in his last six starts, including a win two starts back, make him a serious threat, and he has run over today's trip and going before. The one concern is a quick turnaround, back out just one day after a fourth last time, under 168 lb.
- Larzac (hrs_45855740) | 5yo G | 153lb | OR 124 | draw 0 | jockey Harry Cobden | trainer Faye Bramley (14d 0/18) | headgear t | last run 42 days | form /840-1 | MARKET 10.3% | 09:00 median 8.25 | Matchbook 9.60
    comment: Larzac won last time out and has run over today's trip and going, but 42 days off and 153 lb on an official mark of 124 give him plenty to do.
- Tour Ovalie (hrs_31965738) | 7yo M | 148lb | OR 119 | draw 0 | jockey Adam Wedge | trainer Mrs C. Williams (14d 2/24) | headgear - | last run 11 days | form 40-831 | MARKET 7.3% | 09:00 median 12.00 | Matchbook 13.50
    comment: Tour Ovalie won last time out and has run over today's trip and going, but she is quick back after 11 days and carries 148 lb off 119.
- Boothill (hrs_20025593) | 11yo G | 166lb | OR 137 | draw 0 | jockey Bryan Carver | trainer Harry Fry (14d 0/7) | headgear - | last run 220 days | form P5388- | MARKET 7.0% | 09:00 median 12.00 | Matchbook 14.50
    comment: Boothill has run over today's trip and on this going, and he signed off with a third three starts back before two eighth-place finishes, though he's yet to win in recent form.
- Jony R (hrs_40899544) | 7yo G | 159lb | OR 130 | draw 0 | jockey Sean Bowen | trainer Warren Greatrex (14d 4/22) | headgear - | wind surgery | last run 212 days | form 7144P- | MARKET 6.2% | 09:00 median 13.00 | Matchbook 16.50
    comment: Jony R won four starts back and posted a pair of fourths since, but he was pulled up last time out and returns after 212 days off; he has run over today's trip and going, though 159 lb is a hefty burden.
- Femme Magnifique (hrs_29621753) | 8yo M | 155lb | OR 126 | draw 0 | jockey Cian Quirke | trainer David Harry Kelly (14d 0/8) | headgear - | last run 48 days | form -12112 | MARKET 6.1% | 09:00 median 13.00 | Matchbook 17.50
    comment: Form is hard to fault, with a second last time out and three wins in her last five starts, and she has run over today's trip and going.
- Classic Maestro (hrs_29523081) | 8yo G | 160lb | OR 131 | draw 0 | jockey Luke Scott(3) | trainer Jennie Candlish (14d 3/13) | headgear p | last run 206 days | form 62P31- | MARKET 3.0% | 09:00 median 26.00 | Matchbook 38.00
    comment: The main risk is a 206-day absence, plus 160 lb on his back.

## 2:35 Cheltenham | race_id rac_32303243830 | Oddschecker Handicap Steeple Chase (Premier Handicap) (Registered As The Tom Olliver Handicap Steeple Chase) (GBB Race)
Chase | Class 1 | 3m3f71y | going Good | Turf | 9 runners | rating band - | age 4yo+
- Double Powerful (hrs_34361404) | 7yo G | 158lb | OR 140 | draw 0 | jockey Richie McLernon | trainer Neil Mulholland (14d 7/28) | headgear - | last run 31 days | form 582-31 | MARKET 16.8% | 09:00 median 5.50 | Matchbook 5.70 | CHECK (skip line 5.22)
    comment: Double Powerful arrives fresh from a last-time-out win, with a third and a second before that, and he has run on today's going before. The main risk is the 158 lb he must carry, which asks plenty off an official mark of 140.
- Ask Brewster (hrs_34845853) | 7yo G | 153lb | OR 135 | draw 0 | jockey Adam Wedge | trainer Mrs C. Williams (14d 2/24) | headgear - | last run 204 days | form /1519- | MARKET 14.2% | 09:00 median 6.00 | Matchbook 7.00
    comment: Ask Brewster returns after 204 days off, having finished ninth last time out, which makes him hard to fancy, though he won two starts back and four starts back and has run over today's trip and going.
- King of Answers (hrs_35243376) | 7yo G | 161lb | OR 143 | draw 0 | jockey Derek Fox | trainer Lucinda Russell & Michael Scudamore (14d 9/36) | headgear p | last run 53 days | form 412P-6 | MARKET 13.1% | 09:00 median 6.50 | Matchbook 7.60
    comment: The main risk is a sixth last time out and a 53-day absence under 161 lb.
- Havaila (hrs_29987923) | 7yo G | 157lb | OR 139 | draw 0 | jockey Caoilin Quinn | trainer Jamie Moore & Josh Moore (14d 5/28) | headgear - | last run 204 days | form 36111- | MARKET 12.4% | 09:00 median 6.50 | Matchbook 8.40
    comment: Havaila arrives on a hat-trick of wins, and he has run over today's trip and going, but a 204-day absence and 157 lb on his back temper the enthusiasm.
- Holokea (hrs_34759907) | 7yo G | 148lb | OR 130 | draw 0 | jockey Brian Hughes | trainer Mickey Bowen (14d 4/16) | headgear - | last run 214 days | form 22P81- | MARKET 10.7% | 09:00 median 8.50 | Matchbook 9.00
    comment: He has run over today's trip and going and has two seconds earlier in his recent form, though 148 lb is a big ask.
- Resplendent Grey (hrs_33110455) | 8yo G | 168lb | OR 150 | draw 0 | jockey Sean Bowen | trainer Olly Murphy (14d 9/48) | headgear p | last run 204 days | form 10205- | MARKET 10.5% | 09:00 median 8.50 | Matchbook 9.20
    comment: Resplendent Grey has a win and a second in his last five starts, though the latest was a fifth, and he has run on today's going before.
- Guard The Moon (hrs_37932314) | 8yo G | 154lb | OR 136 | draw 0 | jockey Sam Twiston-Davies | trainer Nigel & Willy Twiston-Davies (14d 5/36) | headgear p | last run 14 days | form 1P1P-3 | MARKET 9.3% | 09:00 median 9.50 | Matchbook 10.50
    comment: Guard The Moon showed he still has ability with a third last time out, and he has won twice in his last five starts, though two pulled-up efforts make him hard to trust.
- U Cant Be Serious (hrs_34789755) | 7yo G | 148lb | OR 130 | draw 0 | jockey Freddie Gingell | trainer Joe Tizzard (14d 5/23) | headgear p | wind surgery | last run 251 days | form 11972- | MARKET 7.5% | 09:00 median 12.00 | Matchbook 13.00
    comment: Returns after 251 days off, which is a big question, and a seventh and a ninth in the two runs before a second last time out hardly scream consistency. In his favour, he won four and five starts back, has run on today's going and carries 148 lb off 130.
- Monbeg Genius (hrs_22567573) | 10yo G | 160lb | OR 142 | draw 0 | jockey Jonjo O'Neill Jr. | trainer Jonjo & A.J. O'Neill (14d 5/33) | headgear tb | last run 223 days | form P5735- | MARKET 5.5% | 09:00 median 15.00 | Matchbook 19.00
    comment: Monbeg Genius is yet to win in his last five, but a third two starts back and a fifth last time out show he's competitive, and he has run over today's trip and going.

## 3:10 Cheltenham | race_id rac_32303245767 | Unibet Greatwood Handicap Hurdle Race (Premier Handicap) (GBB Race)
Hurdle | Class 1 | 2m0f87y | going Good | Turf | 17 runners | rating band - | age 3yo+
- Harry Lowes (hrs_49974281) | 5yo G | 152lb | OR 128 | draw 0 | jockey Harry Cobden | trainer Dan Skelton (14d 19/83) | headgear - | last run 219 days | form 13512- | MARKET 20.1% | 09:00 median 3.50 | Matchbook 5.00 | CHECK (skip line 3.32)
    comment: Second last time out and a winner two starts back, but Harry Lowes returns after 219 days off and carries 152 lb, which makes him hard to fancy.
- Pioneer Pete (hrs_51186828) | 6yo G | 157lb | OR 133 | draw 0 | jockey Jonjo O'Neill Jr. | trainer Jonjo & A.J. O'Neill (14d 5/33) | headgear - | last run 37 days | form 12-111 | MARKET 13.4% | 09:00 median 6.00 | Matchbook 6.60
    comment: Pioneer Pete has won four of his last five, including last time out, and has run over today's trip and going, yet he carries 157 lb after 37 days off.
- Let It Rain (hrs_37932405) | 7yo M | 154lb | OR 130 | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 19/83) | headgear - | last run 251 days | form 1/3P1- | MARKET 12.5% | 09:00 median 6.00 | Matchbook 7.60
    comment: Let It Rain won last time out and four starts back, with a third three starts back, but she was pulled up two starts back and returns after 251 days off.
- Mister Ursus (hrs_46667628) | 5yo G | 152lb | OR 128 | draw 0 | jockey Sean Bowen | trainer Olly Murphy (14d 9/48) | headgear - | last run 29 days | form 2211-3 | MARKET 7.2% | 09:00 median 11.00 | Matchbook 13.00
    comment: Carrying 152 lb off a mark of 128 after 29 days off, he looks short of a fancy despite the solid form.
- Helnwein (hrs_29012753) | 8yo G | 154lb | OR 130 | draw 0 | jockey Jonathan Burke | trainer Alan King (14d 2/19) | headgear - | last run 190 days | form 252U-4 | MARKET 7.1% | 09:00 median 11.00 | Matchbook 13.00
    comment: Helnwein finished fourth last time out and second three starts back, and he has run over today's trip and going, but he is yet to win in his last five and returns after 190 days off. Carrying 154 lb off 130 is a stiff ask.
- Tennessee Tango (hrs_46449781) | 6yo G | 147lb | OR 123 | draw 0 | jockey Freddie Gingell | trainer Joe Tizzard (14d 5/23) | headgear t | wind surgery | last run 37 days | form 31P6-3 | MARKET 5.9% | 09:00 median 13.00 | Matchbook 16.00
    comment: Tennessee Tango was third last time out, and a winner four starts back, but a sixth and a pulled up in between make him hard to trust, and he carries 147 lb.
- The Hardest Geezer (hrs_37889761) | 7yo G | 145lb | OR 121 | draw 0 | jockey Ben Jones | trainer Philip Hobbs & Johnson White (14d 0/18) | headgear - | last run 23 days | form 244F-2 | MARKET 5.7% | 09:00 median 13.00 | Matchbook 17.00
    comment: Second last time out and fit enough after 23 days, he has run over today's trip and going, but he's yet to win in his last five and fell two starts back.
- The Kemble Brewery (hrs_34789832) | 7yo G | 166lb | OR 142 | draw 0 | jockey Tom Bellamy | trainer Kim Bailey & Mat Nicholls (14d 2/14) | headgear tp | last run 175 days | form /F21-1 | MARKET 5.5% | 09:00 median 13.00 | Matchbook 18.00
    comment: Won his last two starts, with a second three starts back, and has run over today's trip and going before; however, 175 days off is a long layoff, and 166 lb is a hefty burden.
- Burdett Road (hrs_32499908) | 6yo G | 165lb | OR 141 | draw 0 | jockey Sam Twiston-Davies | trainer James Owen (14d 9/42) | headgear h | last run 24 days | form 2/23-5 | MARKET 5.1% | 09:00 median 12.00 | Matchbook 23.00
    comment: Burdett Road has hit the frame in three of his last four, including two seconds, and he has run over today's trip and going before, after a fresh 24-day break.
- Captain Hugo (hrs_46450236) | 6yo G | 158lb | OR 134 | draw 0 | jockey Sean Houlihan | trainer Philip Hobbs & Johnson White (14d 0/18) | headgear - | last run 37 days | form 1F12-6 | MARKET 4.1% | 09:00 median 19.00 | Matchbook 23.00
    comment: Captain Hugo has won twice in his last five starts and was second two starts back, but he was only sixth last time out and returns after 37 days off. He has run over today's trip and going, though 158 lb is a hefty burden off 134.
- Race To Base (hrs_41052480) | 6yo G | 146lb | OR 122 | draw 0 | jockey Jack Quinlan | trainer Nick Scholfield (14d 0/11) | headgear tp (1st time) | last run 15 days | form 34P2-3 | MARKET 3.0% | 09:00 median 21.00 | Matchbook 42.00
    comment: Race To Base is winless in his last five but arrives in decent heart, third last time out and second the run before, only 15 days ago.
- Morning Mayhem (hrs_52741941) | 5yo G | 152lb | OR 128 | draw 0 | jockey Kielan Woods | trainer Nick Scholfield (14d 0/11) | headgear p | last run 15 days | form 412267 | MARKET 2.5% | 09:00 median 29.00 | Matchbook 40.00
    comment: Morning Mayhem has slipped to a sixth and then a seventh in his last two outings, which makes him hard to fancy, though two seconds and a win earlier in the sequence show he can go close. He has run over today's trip and going, and 152 lb is a big burden.
- Iberico Lord (hrs_32653544) | 8yo G | 168lb | OR 144 | draw 0 | jockey Nico de Boinville | trainer Nicky Henderson (14d 5/16) | headgear - | last run 197 days | form 99180- | MARKET 2.2% | 09:00 median 34.00 | Matchbook 44.00
    comment: The main risk is a 197-day absence, with an unplaced run last time out and an eighth two starts back.
- Day Trader (hrs_37589237) | 5yo G | 142lb | OR 117 | draw 0 | jockey Daniel King | trainer A. J. Martin (14d 0/12) | headgear - | last run 55 days | form 01000- | MARKET 2.1% | 09:00 median 29.00 | Matchbook 55.00
    comment: Day Trader has been unplaced in his last three outings and hasn't won since four starts back, while 55 days off the track adds to the doubts.
- Serious Challenge (hrs_31149062) | 6yo G | 158lb | OR 134 | draw 0 | jockey Liam Harrison | trainer Fergal O'Brien (14d 3/28) | headgear - | last run 37 days | form P123-0 | MARKET 2.0% | 09:00 median 34.00 | Matchbook 60.00
    comment: Serious Challenge bounced back from a pulled up with a win four starts back, then a second and a third, but was unplaced last time out and returns after 37 days.
- Knickerbockerglory (hrs_23000348) | 10yo G | 158lb | OR 134 | draw 0 | jockey Tristan Durrell | trainer Dan Skelton (14d 19/83) | headgear - | last run 14 days | form 02-507 | MARKET 0.9% | 09:00 median 67.00 | Matchbook 150.00
- Listentoyourheart (hrs_37505321) | 7yo M | 149lb | OR 125 | draw 0 | jockey Charlie Todd | trainer Dan Skelton (14d 19/83) | headgear - | last run 14 days | form 739-05 | MARKET 0.8% | 09:00 median 81.00 | Matchbook 150.00
    comment: Fifth last time out and only 14 days ago, Listentoyourheart is fit and has run over today's trip and going, but she is winless in her last five and has a third four starts back as her best recent finish. Carrying 149 lb off 125, she looks a midfield type.

## 3:45 Cheltenham | race_id rac_32304479636 | Three Counties Christmas Open National Hunt Flat Race(listed Race) (Registered As The William Kidd) (GBB Race)
NH Flat | Class 1 | 2m0f87y | going Good | Turf | 10 runners | rating band - | age 4-5yo
- New Grange (hrs_17392543063) | 4yo G | 156lb | OR - | draw 0 | jockey Harry Cobden | trainer Thomas Cooper (14d 1/2) | headgear - | last run 53 days | form 1-1 | MARKET 28.4% | 09:00 median 3.00 | Matchbook 3.40 | CHECK (skip line 2.85)
    comment: New Grange arrives unbeaten in his last two starts, winning last time out and again two starts back, and he has run on today's going before.
- Cameron de Fiacre (hrs_64621473) | 4yo G | 156lb | OR - | draw 0 | jockey Gavin Sheehan | trainer Jamie Snowden (14d 7/24) | headgear - | last run 185 days | form 1 | MARKET 22.1% | 09:00 median 4.00 | Matchbook 4.20
    comment: Cameron de Fiacre won last time out and has run on today's going before, while the yard's 7 from 24 in the last fortnight adds weight to his claims, making him a serious threat off 156 lb. The one concern is a 185-day absence, so sharpness may be an issue.
- Berkstar (hrs_17392705771) | 4yo G | 156lb | OR - | draw 0 | jockey Mr P. W. Mullins | trainer W. P. Mullins (14d 5/20) | headgear - | last run 52 days | form 2-1 | MARKET 16.0% | 09:00 median 5.50 | Matchbook 5.90
    comment: Berkstar won last time out and was second the run before, so the form is hard to knock, but 52 days off and 156 lb leave plenty to prove.
- Dundee Law (hrs_62170955) | 4yo G | 156lb | OR - | draw 0 | jockey Harry Skelton | trainer Dan Skelton (14d 19/83) | headgear - | last run 39 days | form 32-1 | MARKET 12.7% | 09:00 median 6.50 | Matchbook 7.80
    comment: Dundee Law arrives in good heart, a winner last time out, then a second two starts back and a third three starts back, and he has run over today's trip and going before.
- Par Avion (hrs_59335801) | 5yo G | 156lb | OR - | draw 0 | jockey Bryan Carver | trainer Harry Fry (14d 0/7) | headgear - | last run 18 days | form 42-1 | MARKET 8.1% | 09:00 median 11.00 | Matchbook 12.00
    comment: Par Avion arrives in good heart, a winner last time out, a runner-up two starts back, and a fourth three starts back, and he's fresh enough after 18 days.
- Lord Churchill (hrs_61077863) | 4yo G | 156lb | OR - | draw 0 | jockey Ben Jones | trainer Nick Scholfield (14d 0/11) | headgear - | last run 15 days | form 1-2 | MARKET 6.6% | 09:00 median 12.00 | Matchbook 16.00
    comment: Lord Churchill arrives in cracking nick, second last time out and a winner two starts back, just 15 days after his latest run, and he has run over today's trip and on this going before.
- Junior Minister (hrs_17393906264) | 5yo G | 156lb | OR - | draw 0 | jockey Jonathan England | trainer Sam England (14d 5/23) | headgear - | last run 24 days | form 2-1 | MARKET 2.4% | 09:00 median 29.00 | Matchbook 48.00
    comment: Junior Minister arrives in good heart, a winner last time out after a second two starts back, and he has run over today's trip and on this going.
- Groovy Train (hrs_17395419657) | 4yo G | 156lb | OR - | draw 0 | jockey Sean Bowen | trainer Richard Spencer (14d 0/1) | headgear - | last run - days | form - | MARKET 1.8% | 09:00 median 41.00 | Matchbook 75.00
    comment: Unraced and with no recorded form to go on, Groovy Train is a pure unknown on debut, so he's open to plenty of improvement. He carries 156 lb, and there's nothing yet to suggest where his ceiling lies.
- Willow Tide (hrs_17394113821) | 5yo G | 156lb | OR - | draw 0 | jockey Kielan Woods | trainer Fergal O'Brien (14d 3/28) | headgear - | last run 24 days | form F1-6 | MARKET 1.2% | 09:00 median 51.00 | Matchbook 120.00
    comment: In his favour, he has run over today's trip and is fresh enough after 24 days.
- Hoo's The Jet (hrs_17394735449) | 5yo G | 156lb | OR - | draw 0 | jockey Jonathan Burke | trainer Syd Hosie (14d 2/8) | headgear - | last run 15 days | form 23-4 | MARKET 0.8% | 09:00 median 81.00 | Matchbook 190.00
    comment: Hoo's The Jet has been finishing further back with each run, with a fourth last time out, a third two starts back and a second three starts back, so he is yet to win in that run.
