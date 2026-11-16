# Card review packet: Plumpton, 2026-11-16

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
{"meeting": "plumpton", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 12:45 Plumpton | race_id rac_32304555179 | Weatherbys & Birdie Calendars Novices' Hurdle Race (GBB Race)
Hurdle | Class 4 | 2m4f116y | going Good | Turf | 6 runners | rating band - | age 4yo+
- Ginolo (hrs_17394070015) | 4yo G | 153lb | OR - | draw 0 | jockey Nico de Boinville | trainer Nicky Henderson (14d 4/14) | headgear - | last run 26 days | form 2 | MARKET 52.3% | 09:00 median 1.73 | Matchbook 1.81
- Mysterland (hrs_64388695) | 4yo G | 153lb | OR - | draw 0 | jockey David Bass | trainer Charlie Longsdon (14d 2/14) | headgear - | last run 29 days | form 41 | MARKET 33.2% | 09:00 median 2.50 | Matchbook 3.05
- Mickey Viking (hrs_17395105714) | 4yo G | 153lb | OR - | draw 0 | jockey Rex Dingle | trainer Ben Clarke (14d 0/8) | headgear - | last run 176 days | form 6F | MARKET 6.3% | 09:00 median 13.00 | Matchbook 16.50
- Gold Hill (hrs_45256778) | 4yo G | 153lb | OR - | draw 0 | jockey Charlie Deutsch | trainer Sara Bradstock (14d 0/1) | headgear h | last run 30 days | form 4 | MARKET 4.8% | 09:00 median 15.00 | Matchbook 26.00
- Ar Aghaidh Leat (hrs_17395446775) | 5yo M | 147lb | OR - | draw 0 | jockey Jack Quinlan | trainer Phil McEntee (14d 0/0) | headgear h (1st time) | last run 36 days | form U54-1 | MARKET 2.0% | 09:00 median 41.00 | Matchbook 55.00
- Crock's Bottom (hrs_63171661) | 5yo M | 147lb | OR - | draw 0 | jockey Freddie Gingell | trainer Joe Tizzard (14d 5/25) | headgear - | last run 229 days | form 7- | MARKET 1.4% | 09:00 median 66.00 | Matchbook 70.00

## 1:15 Plumpton | race_id rac_32304557116 | Paul Ferguson's Jumpers To Follow Amateur Jockeys' Handicap Hurdle Race
Hurdle | Class 5 | 2m4f116y | going Good | Turf | 12 runners | rating band 0-105 | age 3yo+
- Market House (hrs_33096490) | 6yo G | 162lb | OR 98 | draw 0 | jockey Mr Alex Chadwick | trainer James Owen (14d 7/34) | headgear tp | last run 13 days | form 21-243 | MARKET 20.1% | 09:00 median 4.00 | Matchbook 4.70 | CHECK (skip line 3.80)
    comment: Market House arrives fit after 13 days, with a third last time out and a win four starts back, and he has run over today's trip.
- Rip Wheeler (hrs_39431371) | 6yo G | 166lb | OR 102 | draw 0 | jockey Mr Hezekiah March(7) | trainer Jamie Moore & Josh Moore (14d 4/31) | headgear - | last run 222 days | form 41241- | MARKET 16.1% | 09:00 median 5.00 | Matchbook 5.80
    comment: Rip Wheeler won last time out and has two wins in his last five starts, with a second three starts back, and he has run over today's trip.
- Cadillac Ranch (hrs_17391048444) | 6yo G | 163lb | OR 99 | draw 0 | jockey Miss Ellie Callwood(5) | trainer L J Morgan (14d 0/5) | headgear - | last run 13 days | form P15234 | MARKET 11.9% | 09:00 median 6.75 | Matchbook 8.00
    comment: Fourth last time out and a third two starts back suggest Cadillac Ranch is in decent heart, and he's fresh from a run 13 days ago, having run over today's trip. Carrying 163 lb off 99 is a stiff ask though, and he's still looking for a first win since succeeding five starts back.
- Prairie Diamond (hrs_34153350) | 7yo G | 168lb | OR 104 | draw 0 | jockey Mr Harry Hoyles(7) | trainer Martin Keighley (14d 2/11) | headgear tv (1st time) | last run 21 days | form 1-P23U | MARKET 11.4% | 09:00 median 7.00 | Matchbook 8.20
    comment: Prairie Diamond unseated last time out but had posted a third two starts back and a second three starts back before that, and he's fresh enough after 21 days.
- Kandor (hrs_34253275) | 7yo G | 168lb | OR 104 | draw 0 | jockey Mr Daniel Williams(7) | trainer Nick Scholfield (14d 0/13) | headgear t | last run 14 days | form 221-45 | MARKET 8.3% | 09:00 median 8.50 | Matchbook 13.00
    comment: The risk is a slide to fifth last time out and fourth the start before, plus a hefty 168 lb.
- Jefe Triunfo (hrs_35580734) | 7yo G | 159lb | OR 95 | draw 0 | jockey Miss Milica Jovana Dusanovic | trainer Chris Gordon (14d 2/9) | headgear p | last run 44 days | form 7-5413 | MARKET 7.1% | 09:00 median 11.00 | Matchbook 14.00
    comment: Jefe Triunfo showed up with a third last time out, and a winner two starts back, but a fourth, a fifth and a seventh before that make him hard to fancy under 159 lb after 44 days off.
- Bread And Butter (hrs_20387024) | 11yo G | 145lb | OR 81 | draw 0 | jockey Miss Molly Legg(7) | trainer Cynthia Woods (14d 0/3) | headgear t | last run 6 days | form 5-6424 | MARKET 7.0% | 09:00 median 10.00 | Matchbook 15.50
    comment: Winless in his last five, Bread And Butter was a fourth last time out and a second two starts back, so he is knocking on the door, but that has not made him a winner.
- Whatsgoingonmarvin (hrs_45759504) | 4yo G | 158lb | OR 95 | draw 0 | jockey Miss Abigail Voyce(7) | trainer Mickey Bowen (14d 5/17) | headgear b | last run 18 days | form 266-53 | MARKET 6.2% | 09:00 median 13.00 | Matchbook 16.00
    comment: Whatsgoingonmarvin is winless in his last five, though a third last time out and a second five starts back show he is not out of form, and he's fresh enough after 18 days.
- Glitz And Glamour (hrs_50433019) | 5yo M | 167lb | OR 103 | draw 0 | jockey Mr Evan Lonergan(7) | trainer Neil King (14d 0/8) | headgear - | last run 49 days | form 9-P604 | MARKET 4.4% | 09:00 median 17.00 | Matchbook 23.00
    comment: Glitz And Glamour showed some improvement with a fourth last time out, but she's winless in her last five and was only sixth three starts back, so the form is modest. She has run over today's trip, though 167 lb and a 49-day absence temper enthusiasm.
- Girl of Gold (hrs_46547228) | 5yo M | 168lb | OR 104 | draw 0 | jockey Mr James King | trainer Andy Irvine (14d 0/3) | headgear - | last run 303 days | form /2231- | MARKET 3.0% | 09:00 median 22.00 | Matchbook 38.00
    comment: Girl of Gold won last time out and has been placed in her other recent starts, a second, a third and another second, though 303 days off is a big gap and she carries a hefty 168 lb.
- Nelson Gate (hrs_45474793) | 4yo G | 157lb | OR 94 | draw 0 | jockey Miss Elizabeth Feakes(7) | trainer Jamie Moore & Josh Moore (14d 4/31) | headgear p | last run 21 days | form 934-33 | MARKET 2.5% | 09:00 median 29.00 | Matchbook 42.00
    comment: Nelson Gate has been thereabouts without getting his head in front, with thirds last time out and two starts back, but he is winless in his last five and carries 157 lb off 94.
- No No Fizz (hrs_34542557) | 8yo M | 166lb | OR 102 | draw 0 | jockey L O'Hara(7) | trainer Fergal O'Brien (14d 3/30) | headgear - | last run 9 days | form 81P-5P | MARKET 2.0% | 09:00 median 34.00 | Matchbook 70.00
    comment: The main risk is two pulled-up efforts in her last three runs, the latest last time out, while she carries 166 lb.

## 1:45 Plumpton | race_id rac_32304559053 | John Weight Gone But Not Forgotten Handicap Steeple Chase (GBB Race)
Chase | Class 4 | 2m0f219y | going Good To Soft | Turf | 6 runners | rating band 0-120 | age 4yo+
- Ionian (hrs_51558199) | 5yo G | 167lb | OR 114 | draw 0 | jockey Nico de Boinville | trainer Nicky Henderson (14d 4/14) | headgear - | wind surgery | last run 200 days | form 62437- | MARKET 25.6% | 09:00 median 3.50 | Matchbook 3.80 | CHECK (skip line 3.32)
    comment: The main risk is a 200-day absence, and a seventh last time out hardly screams sharpness.
- Clap of Thunder (hrs_37686873) | 6yo G | 168lb | OR 115 | draw 0 | jockey Sam Twiston-Davies | trainer Nigel & Willy Twiston-Davies (14d 5/37) | headgear - | last run 19 days | form 3/43-4 | MARKET 20.8% | 09:00 median 4.50 | Matchbook 4.70
    comment: Clap of Thunder is consistent, finishing third and fourth in each of his last four starts, and he returns just 19 days after a fourth last time out, having run over today's trip before.
- Crest of Stars (hrs_47685050) | 5yo G | 167lb | OR 114 | draw 0 | jockey Rex Dingle | trainer Anthony Honeyball (14d 4/25) | headgear t | last run 11 days | form 431-32 | MARKET 17.2% | 09:00 median 5.00 | Matchbook 5.90
    comment: Crest of Stars arrives in cracking form, second last time out, a third two starts back and a winner three starts back, and he's fit after just 11 days off.
- Icare Grandchamp (hrs_26988360) | 8yo G | 164lb | OR 111 | draw 0 | jockey Caoilin Quinn | trainer Jamie Moore & Josh Moore (14d 4/31) | headgear - | last run 226 days | form 52132- | MARKET 16.1% | 09:00 median 5.50 | Matchbook 6.20
    comment: Icare Grandchamp arrives in cracking nick on paper, a second last time out, a third two starts back and a winner three starts back, and he has run over today's trip. The one concern is a 226-day absence, with 164 lb to carry on top.
- Reteti (hrs_30850470) | 6yo G | 156lb | OR 103 | draw 0 | jockey Marc Goldstein | trainer Sheena West (14d 0/3) | headgear h | last run 13 days | form 321334 | MARKET 12.2% | 09:00 median 7.00 | Matchbook 8.60
    comment: Reteti has been consistent, finishing fourth last time out, with a third two starts back, and he has run over today's trip after just 13 days off.
- Siam Park (hrs_34073221) | 7yo G | 167lb | OR 114 | draw 0 | jockey Jack Tudor | trainer Joe Tizzard (14d 5/25) | headgear t | last run 35 days | form -U2335 | MARKET 8.2% | 09:00 median 11.00 | Matchbook 12.00
    comment: Siam Park is winless in his last five, having finished fifth last time out, and he has had a break of 35 days since.

## 2:15 Plumpton | race_id rac_32304560990 | 'Anyone Want A Drink? Anyone?' Handicap Hurdle Race
Hurdle | Class 3 | 2m4f116y | going Good | Turf | 10 runners | rating band 0-130 | age 3yo+
- Kamille Au Kanada (hrs_52495359) | 6yo M | 160lb | OR 112 | draw 0 | jockey Chad Bament(5) | trainer Anthony Honeyball (14d 4/25) | headgear t | last run 6 days | form -15111 | MARKET 26.2% | 09:00 median 3.25 | Matchbook 3.65 | CHECK (skip line 3.09)
    comment: Kamille Au Kanada arrives on a four-timer after four wins in her last five starts, a fifth four starts back the only blip, and she has run over today's trip.
- Norman Fletcher (hrs_33051522) | 7yo G | 154lb | OR 113 | draw 0 | jockey Jamie Brace(5) | trainer Nigel & Willy Twiston-Davies (14d 5/37) | headgear v | last run 3 days | form 5322F1 | MARKET 26.1% | 09:00 median 3.25 | Matchbook 3.65
    comment: Norman Fletcher won last time out and was second in two of the three runs before a fall, so the form reads well, but he's back after just three days and carries 154 lb off 113.
- Tune In A Box (hrs_34401850) | 7yo G | 161lb | OR 120 | draw 0 | jockey Stan Sheppard | trainer Tom Lacey (14d 5/13) | headgear p | last run 8 days | form 732-51 | MARKET 14.1% | 09:00 median 6.00 | Matchbook 6.80
    comment: Tune In A Box arrives a last-time-out winner, with a second and a third also in his last five, and he's back quickly after just eight days, having run over today's trip before.
- Grand Conqueror (hrs_52055787) | 5yo G | 168lb | OR 127 | draw 0 | jockey Richie McLernon | trainer Neil Mulholland (14d 4/23) | headgear h | last run 26 days | form 122-31 | MARKET 13.7% | 09:00 median 6.00 | Matchbook 7.20
    comment: Winner last time out and a third two starts back, Grand Conqueror arrives in cracking form after 26 days off, and he has run over today's trip.
- Stream of Stars (hrs_13524994) | 11yo G | 166lb | OR 125 | draw 0 | jockey Sam Twiston-Davies | trainer Nigel & Willy Twiston-Davies (14d 5/37) | headgear - | last run 14 days | form 226-35 | MARKET 6.1% | 09:00 median 13.00 | Matchbook 17.50
- Dragons And Demons (hrs_58715293) | 5yo G | 142lb | OR 101 | draw 0 | jockey Harry Kimber | trainer Robert Walford (14d 0/3) | headgear - | last run 247 days | form U8641- | MARKET 5.6% | 09:00 median 15.00 | Matchbook 17.50
    comment: Won last time out, but that came 247 days ago and he's been beaten in the three runs before it, finishing a fourth, a sixth and an eighth.
- Percy Shelley (hrs_29636516) | 7yo G | 162lb | OR 121 | draw 0 | jockey Jonathan Burke | trainer James Owen (14d 7/34) | headgear p | last run 37 days | form 2P3-26 | MARKET 5.0% | 09:00 median 15.00 | Matchbook 22.00
    comment: Percy Shelley is winless in his last five but has been in the frame three times, with a second two starts back and a third three starts back, though he slipped to sixth last time out. He has run over today's trip and carries 162 lb after 37 days off, which is a lot to ask.
- Jaramillo (hrs_22871975) | 8yo G | 162lb | OR 121 | draw 0 | jockey Richard Upton(10) | trainer Warren Greatrex (14d 4/23) | headgear p | last run 34 days | form 56-831 | MARKET 1.9% | 09:00 median 34.00 | Matchbook 80.00
    comment: Jaramillo won last time out and was third two starts back, so he arrives in good heart after 34 days off, and he has run over today's trip.
- Way Out (hrs_27794067) | 9yo G | 149lb | OR 108 | draw 0 | jockey James Best | trainer Syd Hosie (14d 2/9) | headgear - | last run 38 days | form 2050/P | MARKET 0.8% | 09:00 median 101.00 | Matchbook 190.00
- Tonaghneave Well (hrs_41191346) | 6yo G | 165lb | OR 124 | draw 0 | jockey Adam Wedge | trainer Jim & Suzi Best (14d 1/4) | headgear - | last run 14 days | form 893P60 | MARKET 0.6% | 09:00 median 101.00 | Matchbook 360.00
    comment: The risk is a winless record in his last six, with an unplaced effort last time out.

## 2:45 Plumpton | race_id rac_32304562927 | More Radio Novices' Limited Handicap Hurdle Race
Hurdle | Class 5 | 3m0f217y | going Good | Turf | 7 runners | rating band 0-95 | age 4yo+
- Golly Gosh (hrs_51988888) | 5yo G | 154lb | OR 82 | draw 0 | jockey Jack Andrews | trainer Tom Ellis (14d 2/16) | headgear t | last run 3 days | form P72211 | MARKET 34.4% | 09:00 median 2.63 | Matchbook 2.72
    comment: Golly Gosh arrives in cracking nick, a winner last time out and two starts back, with seconds three and four starts back, though turning out just three days later is a quick return.
- Anothermanicmonday (hrs_52772209) | 6yo G | 146lb | OR 74 | draw 0 | jockey Sean Houlihan | trainer Susan Gardner (14d 0/0) | headgear - | last run 26 days | form 06-571 | MARKET 22.4% | 09:00 median 4.00 | Matchbook 4.30
    comment: Anothermanicmonday won last time out, but that came after a seventh, a fifth and a sixth in his previous runs, so the form is patchy. Carrying 146 lb off an official mark of 74, he looks hard to fancy, though 26 days since his last run is a fair gap.
- Good Girl Rachel (hrs_58132662) | 6yo M | 149lb | OR 77 | draw 0 | jockey Sam Twiston-Davies | trainer Ben Clarke (14d 0/8) | headgear tv (1st time) | last run 159 days | form 789-43 | MARKET 11.3% | 09:00 median 8.00 | Matchbook 8.40
    comment: Third last time out and a fourth two starts back show Good Girl Rachel heading the right way, and she has run over today's trip, but she is yet to win in her last five and returns after 159 days off.
- Jurassic Pet (hrs_41597129) | 6yo M | 166lb | OR 94 | draw 0 | jockey Miss Lily Bradstock(7) | trainer Sara Bradstock (14d 0/1) | headgear t | last run 46 days | form /430-7 | MARKET 10.4% | 09:00 median 7.50 | Matchbook 11.00
    comment: The main risk is a 46-day absence and 166 lb on her back, having been winless in her last four starts.
- Of Corse I Can (hrs_27040510) | 9yo G | 145lb | OR 72 | draw 0 | jockey Bradley Harris(3) | trainer Neil Mulholland (14d 4/23) | headgear p | last run 44 days | form -55412 | MARKET 8.8% | 09:00 median 9.50 | Matchbook 12.50
    comment: Of Corse I Can bounces in off a second last time out and a win two starts back, but he's been out 44 days and carries 145 lb, and he has run over today's trip.
- Ephyra (hrs_36386938) | 5yo M | 149lb | OR 77 | draw 0 | jockey Tom Cannon | trainer Andy Irvine (14d 0/3) | headgear - | last run 10 days | form 62P-P5 | MARKET 6.8% | 09:00 median 13.00 | Matchbook 14.00
    comment: The risk is reliability, with a pulled up two and three starts back and yet to win in her last five.
- Athena's Dream (hrs_58566067) | 4yo F | 152lb | OR 82 | draw 0 | jockey Isabelle Ryder(5) | trainer Harriet Dickin (14d 0/7) | headgear v | last run 34 days | form 352933 | MARKET 5.9% | 09:00 median 15.00 | Matchbook 16.50
    comment: Athena's Dream arrives in sound order, third last time out and another third two starts back, with a second four runs ago, and she has run over today's trip before. Carrying 152 lb off 82 is the main risk, as she is yet to win in her last six starts.

## 3:15 Plumpton | race_id rac_32304564864 | Docker Hughes Memorial Race Handicap Steeple Chase
Chase | Class 5 | 3m1f157y | going Good To Soft | Turf | 5 runners | rating band 0-105 | age 4yo+
- Uncle Al (hrs_52176607) | 7yo G | 153lb | OR 90 | draw 0 | jockey Kevin Healy(7) | trainer Jessica Bedi (14d 0/6) | headgear p | last run 26 days | form 63U231 | MARKET 35.7% | 09:00 median 2.50 | Matchbook 2.78
    comment: Uncle Al arrives a last-time-out winner, with a third and a second before that, and has run over today's trip after 26 days off.
- Daring Plan (hrs_29621977) | 8yo G | 150lb | OR 87 | draw 0 | jockey Lucy Gardner | trainer Susan Gardner (14d 0/0) | headgear p | last run 26 days | form 2-U112 | MARKET 24.3% | 09:00 median 3.75 | Matchbook 4.00
    comment: Daring Plan arrives in cracking form, a second last time out and a winner two and three starts back, and he has run over today's trip after a 26-day break.
- Back It Up (hrs_29327151) | 8yo G | 165lb | OR 102 | draw 0 | jockey Mr Alex Chadwick(3) | trainer James Owen (14d 7/34) | headgear v (1st time) | last run 15 days | form 4-5454 | MARKET 21.2% | 09:00 median 4.33 | Matchbook 4.60
    comment: Back It Up has been consistent, finishing fourth last time out, and his run of fourths and fifths in his last five starts shows he's rarely far away.
- Walkinthewoods (hrs_24819662) | 9yo G | 152lb | OR 89 | draw 0 | jockey Adam Wedge | trainer Mrs C. Williams (14d 2/25) | headgear - | last run 22 days | form U6FR-4 | MARKET 17.6% | 09:00 median 5.00 | Matchbook 5.70
    comment: The risk is reliability, with a refusal, a fall and an unseating in his last five starts.
- Sopran Thor (hrs_20308155) | 11yo G | 168lb | OR 105 | draw 0 | jockey Murray Dodd(5) | trainer Louise Allan (14d 0/0) | headgear p | last run 19 days | form P4/3-P | MARKET 1.3% | 09:00 median 67.00 | Matchbook 85.00
    comment: Sopran Thor is without a win in his last four starts and was pulled up last time, but he showed his hand with a third two starts back and a fourth three starts back.

## 3:45 Plumpton | race_id rac_32304566801 | Neville Hall 60th Birthday Celebration Novices' Handicap Hurdle Race
Hurdle | Class 5 | 1m7f195y | going Good | Turf | 8 runners | rating band 0-105 | age 3yo+
- Kotari (hrs_30175705) | 7yo G | 154lb | OR 88 | draw 0 | jockey Caoilin Quinn | trainer Jamie Moore & Josh Moore (14d 4/31) | headgear p | last run 21 days | form 3/34-4 | MARKET 24.1% | 09:00 median 3.75 | Matchbook 3.90 | CHECK (skip line 3.56)
    comment: Kotari arrives consistent, with a fourth last time out, another fourth two starts back and a third three starts back, and he's fresh enough after 21 days off while having run over today's trip.
- Bobbi's Beauty (hrs_32682566) | 8yo M | 166lb | OR 100 | draw 0 | jockey Freddie Keighley(5) | trainer Martin Keighley (14d 2/11) | headgear p | last run 7 days | form 251-31 | MARKET 14.8% | 09:00 median 5.50 | Matchbook 6.80
    comment: Bobbi's Beauty is in cracking form, a winner last time out and again three starts back, with a third two starts back in between, and she's fresh from a run just seven days ago.
- Sir Edward Lear (hrs_44450805) | 5yo G | 168lb | OR 102 | draw 0 | jockey Callum Pritchard | trainer James Owen (14d 7/34) | headgear p | last run 15 days | form 5-64 | MARKET 13.9% | 09:00 median 6.50 | Matchbook 6.80
    comment: Sir Edward Lear is winless in his last three, finishing fourth last time out after a sixth and a fifth, and he returns just 15 days later having run over today's trip.
- Graeme The Grey (hrs_46449809) | 6yo G | 156lb | OR 90 | draw 0 | jockey Tabitha Worsley | trainer Nick Gifford (14d 1/8) | headgear - | last run 26 days | form /346-7 | MARKET 12.8% | 09:00 median 6.50 | Matchbook 7.80
    comment: Graeme The Grey is winless in his last four and has been going the wrong way, with a seventh last time out and a sixth before that, so he is hard to fancy under 156 lb.
- Giddyupadingdong (hrs_37489753) | 6yo G | 147lb | OR 81 | draw 0 | jockey Bradley Harris(3) | trainer Neil Mulholland (14d 4/23) | headgear t | last run 124 days | form 84-536 | MARKET 12.1% | 09:00 median 7.00 | Matchbook 8.20
    comment: Giddyupadingdong was sixth last time out after a third two starts back, but he is winless in his last five and returns from 124 days off.
- Sense of Reason (hrs_40899593) | 5yo G | 168lb | OR 102 | draw 0 | jockey Tom Cannon | trainer Charlie Fellowes (14d 0/7) | headgear - | last run 27 days | form 4472-P | MARKET 10.7% | 09:00 median 8.00 | Matchbook 9.20
    comment: The main risk is a pulled-up effort last time out, and he is yet to win in his last five starts, carrying 168 lb.
- Victory Shout (hrs_35767627) | 5yo G | 164lb | OR 98 | draw 0 | jockey Charlie Deutsch | trainer Syd Hosie (14d 2/9) | headgear - | last run 38 days | form P122-0 | MARKET 7.1% | 09:00 median 13.00 | Matchbook 13.50
    comment: Victory Shout bids to bounce back after a quiet latest run, having finished second, second and a win in the three runs before, and he has run over today's trip. Off 38 days since his last start and carrying 164 lb, the weight is the main risk.
- Freddiemissmolli (hrs_48112183) | 6yo M | 146lb | OR 80 | draw 0 | jockey Adam Wedge | trainer Mrs C. Williams (14d 2/25) | headgear - | last run 38 days | form 5U0-64 | MARKET 4.5% | 09:00 median 19.00 | Matchbook 24.00
    comment: Freddiemissmolli is winless in her last five, with a fourth last time out the best of a modest run that includes a sixth two starts back and an unseated four starts back.
