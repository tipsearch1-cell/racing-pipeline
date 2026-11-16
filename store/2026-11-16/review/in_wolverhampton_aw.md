# Card review packet: Wolverhampton (AW), 2026-11-16

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
{"meeting": "wolverhampton_aw", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 4:30 Wolverhampton (AW) | race_id rac_32304568738 | All-Weather Championship Is Back Nursery Handicap Stakes (Rider Restricted Race)
Flat | Class 5 | 6f20y | going Standard | AW | 11 runners | rating band 0-75 | age 2yo
- Lord Ragnar (hrs_64168013) | 2yo C | 135lb | OR 75 | draw 3 | jockey Rhys Clutterbuck | trainer Ed Dunlop (14d 0/4) | headgear - | last run 19 days | form 124273 | MARKET 18.2% | 09:00 median 4.33 | Matchbook 5.40 | CHECK (skip line 4.11)
    comment: Lord Ragnar showed solid consistency, finishing third last time out and in the frame in four of his last six, and he returns fresh after 19 days with experience of today's trip and going.
- Go Go Girl (hrs_17392055982) | 2yo F | 133lb | OR 73 | draw 1 | jockey Georgia Dobie | trainer Clive Cox (14d 1/6) | headgear - | last run 39 days | form 32 | MARKET 14.8% | 09:00 median 5.50 | Matchbook 6.60
    comment: Go Go Girl comes in with a second last time out and a third two starts back, though she is yet to win in that spell, and she has run over today's trip.
- Roosike (hrs_65938957) | 2yo F | 135lb | OR 75 | draw 5 | jockey Donagh Murphy(5) | trainer Richard Hughes (14d 0/10) | headgear - | last run 11 days | form 210952 | MARKET 14.2% | 09:00 median 6.00 | Matchbook 6.60
- Pon Pon Dalia (hrs_64555652) | 2yo F | 128lb | OR 68 | draw 2 | jockey Luke Catton(3) | trainer Marco Botti (14d 0/4) | headgear - | last run 44 days | form 5218 | MARKET 10.6% | 09:00 median 7.50 | Matchbook 9.40
    comment: Pon Pon Dalia won two starts back and was second the run before, but she was eighth last time out and returns after 44 days off.
- Time Teller (hrs_17392057025) | 2yo C | 134lb | OR 74 | draw 7 | jockey Jack Dace(5) | trainer George Baker (14d 1/9) | headgear - | last run 13 days | form 822 | MARKET 10.3% | 09:00 median 8.00 | Matchbook 9.20
    comment: Time Teller arrives in cracking nick, a second last time out and another second two starts back, just 13 days since his latest run, and he has run over today's trip and on this going before.
- Harry's Pop (hrs_64324610) | 2yo G | 135lb | OR 75 | draw 8 | jockey Connor Planas | trainer Dylan Cunha (14d 1/7) | headgear - | last run 38 days | form 441153 | MARKET 9.9% | 09:00 median 9.00 | Matchbook 9.20
    comment: Harry's Pop was third last time out after a fifth two starts back, and he won twice in the two runs before that. He has run over today's trip and going, but 38 days off and 135 lb from draw 8 temper the case.
- Big Hitter (hrs_64460193) | 2yo F | 135lb | OR 75 | draw 9 | jockey William Carver | trainer Jamie Osborne (14d 0/0) | headgear t | last run 23 days | form 22317 | MARKET 8.0% | 09:00 median 11.00 | Matchbook 11.50
    comment: Big Hitter bounces back from a seventh last time out with a solid profile: a winner two starts back, plus a third and two seconds in her last five, and she has run over today's trip.
- Sue's Last Chance (hrs_64621620) | 2yo G | 127lb | OR 67 | draw 11 | jockey Barry McHugh | trainer Richard & Peter Fahey (14d 2/13) | headgear v | last run 19 days | form 580035 | MARKET 5.8% | 09:00 median 11.00 | Matchbook 21.00
    comment: Winless in his last six, Sue's Last Chance was fifth last time out 19 days ago, with a third two starts back his only top-three finish, so he is hard to fancy.
- Romeo Guest (hrs_63742049) | 2yo G | 130lb | OR 70 | draw 6 | jockey George Bass | trainer Jack Channon (14d 1/5) | headgear - | last run 47 days | form 593 | MARKET 5.4% | 09:00 median 15.00 | Matchbook 18.00
    comment: Romeo Guest was third last time out but is winless in his last three, with a ninth and a fifth before that, and a 47-day break adds to the doubt.
- Angel Ang (hrs_65710848) | 2yo G | 127lb | OR 67 | draw 4 | jockey Amy Tucker(7) | trainer David Evans (14d 0/9) | headgear - | last run 28 days | form 10458 | MARKET 1.6% | 09:00 median 51.00 | Matchbook 80.00
    comment: Angel Ang is hard to fancy after sliding from a fifth and a fourth to an eighth last time out, with his only win five starts back, though he has run over today's trip and going and returns after 28 days.
- Farasan (hrs_17390330860) | 2yo C | 127lb | OR 67 | draw 10 | jockey Nicola Currie | trainer Lawrence Mullaney (14d 0/7) | headgear - | last run 9 days | form 644897 | MARKET 1.2% | 09:00 median 67.00 | Matchbook 100.00
    comment: Farasan is winless in his last six, with a seventh last time out following a ninth and an eighth, though he has run over today's trip and is back quickly after nine days.

## 5:00 Wolverhampton (AW) | race_id rac_32304570675 | AWC Finals Day At Newcastle 26th March EBF Fillies' Novice Stakes (Rider Restricted Race) (GBB Race)
Flat | Class 4 | 6f20y | going Standard | AW | 13 runners | rating band - | age 2yo
- Desert Romance (hrs_17392888296) | 2yo F | 128lb | OR 80 | draw 4 | jockey Toby Moore(7) | trainer Charlie Appleby (14d 2/4) | headgear - | last run 24 days | form 33 | MARKET 45.5% | 09:00 median 1.80 | Matchbook 1.99
- Threelittleangels (hrs_17392698470) | 2yo F | 128lb | OR 74 | draw 7 | jockey Nicola Currie | trainer Roger Teal (14d 2/6) | headgear - | last run 38 days | form 32 | MARKET 19.5% | 09:00 median 3.75 | Matchbook 5.10
- Diamond Blue Point (hrs_64555449) | 2yo F | 128lb | OR - | draw 6 | jockey Grace McEntee | trainer George Boughey (14d 1/4) | headgear - | last run 25 days | form 3 | MARKET 13.4% | 09:00 median 6.00 | Matchbook 7.00
- Tootgarook (hrs_17395456162) | 2yo F | 128lb | OR - | draw 11 | jockey Connor Planas | trainer Simon & Ed Crisford (14d 0/3) | headgear - | last run - days | form - | MARKET 7.4% | 09:00 median 11.00 | Matchbook 13.00
- Aloisi Star (hrs_17395448861) | 2yo F | 128lb | OR - | draw 2 | jockey Dougie Costello | trainer K. R. Burke (14d 0/9) | headgear - | last run - days | form - | MARKET 3.2% | 09:00 median 23.00 | Matchbook 38.00
- Ruby Punch (hrs_17395455119) | 2yo F | 128lb | OR - | draw 13 | jockey William Carver | trainer Andrew Balding (14d 1/13) | headgear - | last run - days | form - | MARKET 2.3% | 09:00 median 34.00 | Matchbook 46.00
- Persian Coast (hrs_17392615030) | 2yo F | 128lb | OR - | draw 9 | jockey Laura Pearson | trainer Kevin Philippart de Foy (14d 0/1) | headgear - | last run - days | form - | MARKET 2.2% | 09:00 median 34.00 | Matchbook 46.00
- Letter To Hermione (hrs_17389384859) | 2yo F | 128lb | OR - | draw 1 | jockey George Downing | trainer Ed Walker (14d 1/11) | headgear - | last run 54 days | form 6 | MARKET 2.0% | 09:00 median 41.00 | Matchbook 55.00
- Kirton Angel (hrs_66586044) | 2yo F | 128lb | OR - | draw 5 | jockey Oisin McSweeney | trainer Richard & Peter Fahey (14d 2/13) | headgear - | last run 68 days | form 37 | MARKET 1.9% | 09:00 median 34.00 | Matchbook 65.00
- Mystical Magical (hrs_63323680) | 2yo F | 128lb | OR - | draw 10 | jockey Joey Haynes | trainer Adam Kirby (14d 0/8) | headgear - | last run 225 days | form 9 | MARKET 0.7% | 09:00 median 126.00 | Matchbook 250.00
- Peacock's Way (hrs_7000002219) | 2yo F | 128lb | OR - | draw 3 | jockey Liam Wright(3) | trainer Jennie Candlish (14d 3/15) | headgear - | last run 39 days | form 69 | MARKET 0.6% | 09:00 median 126.00 | Matchbook 250.00
- Milkin It (hrs_17395453033) | 2yo F | 128lb | OR - | draw 12 | jockey Tyler Heard | trainer John Mackie (14d 0/3) | headgear - | last run - days | form - | MARKET 0.6% | 09:00 median 126.00 | Matchbook 280.00
- Kissamee (hrs_17393700793) | 2yo F | 128lb | OR - | draw 8 | jockey Barry McHugh | trainer Richard & Peter Fahey (14d 2/13) | headgear - | last run 34 days | form 9 | MARKET 0.6% | 09:00 median 151.00 | Matchbook 250.00

## 5:30 Wolverhampton (AW) | race_id rac_32304896091 | AWC Season 14 Has Begun EBF Novice Stakes (Rider Restricted Race) (Div I) (GBB/GBBPlus Race)
Flat | Class 3 | 1m142y | going Standard | AW | 9 runners | rating band - | age 2yo
- Leading Role (hrs_17393752943) | 2yo C | 137lb | OR - | draw 7 | jockey Toby Moore(7) | trainer Charlie Appleby (14d 2/4) | headgear - | last run 33 days | form 1 | MARKET 68.0% | 09:00 median 1.25 | Matchbook 1.31
- Afif (hrs_17393175121) | 2yo C | 130lb | OR - | draw 2 | jockey Luke Catton(3) | trainer John & Thady Gosden (14d 3/9) | headgear - | last run 17 days | form 46 | MARKET 12.3% | 09:00 median 5.50 | Matchbook 8.80
- Ever Since (hrs_17395457205) | 3yo G | 130lb | OR - | draw 6 | jockey Tyler Heard | trainer John & Thady Gosden (14d 3/9) | headgear - | last run - days | form - | MARKET 10.3% | 09:00 median 6.75 | Matchbook 10.50
- Masai Land (hrs_17393239787) | 2yo C | 130lb | OR - | draw 8 | jockey M. P. Sheehy | trainer William Haggas (14d 4/9) | headgear - | last run 17 days | form 75 | MARKET 3.0% | 09:00 median 23.00 | Matchbook 40.00
- Bayside Waltz (hrs_17394078359) | 2yo C | 130lb | OR - | draw 5 | jockey William Carver | trainer Andrew Balding (14d 1/13) | headgear - | last run 26 days | form 5 | MARKET 2.8% | 09:00 median 21.00 | Matchbook 60.00
- Steel Nation (hrs_17394310948) | 2yo C | 130lb | OR - | draw 4 | jockey Grace McEntee | trainer George Boughey (14d 1/4) | headgear - | last run 23 days | form 8 | MARKET 1.5% | 09:00 median 41.00 | Matchbook 90.00
- Dj Harry (hrs_17393847856) | 2yo C | 130lb | OR - | draw 3 | jockey Laura Coughlan(3) | trainer Gemma Tutty (14d 1/6) | headgear - | last run 21 days | form 68 | MARKET 0.9% | 09:00 median 81.00 | Matchbook 170.00
- Penselwood (hrs_17392682825) | 2yo G | 130lb | OR - | draw 1 | jockey Rhys Clutterbuck | trainer Sir Mark Prescott Bt (14d 0/3) | headgear - | last run 35 days | form 79 | MARKET 0.7% | 09:00 median 81.00 | Matchbook 240.00
- Port Eleonora (hrs_17391597062) | 2yo F | 125lb | OR - | draw 9 | jockey Liam Wright(3) | trainer Jennie Candlish (14d 3/15) | headgear - | last run 41 days | form 0 | MARKET 0.5% | 09:00 median 126.00 | Matchbook 500.00

## 6:00 Wolverhampton (AW) | race_id rac_32304572612 | AWC Season 14 Has Begun EBF Novice Stakes (Rider Restricted Race) (Div II) (GBB/GBBPlus Race)
Flat | Class 3 | 1m142y | going Standard | AW | 9 runners | rating band - | age 2yo
- Al Lahbab (hrs_17393845770) | 2yo C | 133lb | OR - | draw 7 | jockey Connor Planas | trainer Charlie Appleby (14d 2/4) | headgear - | last run 26 days | form 2 | MARKET 48.3% | 09:00 median 1.73 | Matchbook 1.85
- Kings Medal (hrs_17394079402) | 2yo C | 133lb | OR - | draw 5 | jockey Tyler Heard | trainer John & Thady Gosden (14d 3/9) | headgear - | last run 23 days | form 4 | MARKET 19.4% | 09:00 median 4.00 | Matchbook 5.00
- Vulcanist (hrs_17393058305) | 2yo C | 133lb | OR - | draw 2 | jockey Rhys Clutterbuck | trainer Ralph Beckett (14d 0/7) | headgear - | last run 46 days | form 5 | MARKET 15.9% | 09:00 median 4.50 | Matchbook 6.60
- Adventus Saxonum (hrs_17394907544) | 2yo C | 133lb | OR - | draw 1 | jockey Luke Catton(3) | trainer John & Thady Gosden (14d 3/9) | headgear - | last run - days | form - | MARKET 6.6% | 09:00 median 12.00 | Matchbook 15.00
- Simply George (hrs_17395458248) | 2yo C | 133lb | OR - | draw 6 | jockey Dougie Costello | trainer Marco Botti (14d 0/4) | headgear - | last run - days | form - | MARKET 4.8% | 09:00 median 15.00 | Matchbook 25.00
- Laurel Crown (hrs_17394176401) | 2yo C | 133lb | OR - | draw 9 | jockey William Carver | trainer Andrew Balding (14d 1/13) | headgear - | last run 24 days | form 0 | MARKET 2.1% | 09:00 median 29.00 | Matchbook 65.00
- Silent Wisdom (hrs_17392562880) | 2yo C | 133lb | OR - | draw 3 | jockey George Downing | trainer Ed Walker (14d 1/11) | headgear - | last run 18 days | form 86 | MARKET 1.8% | 09:00 median 41.00 | Matchbook 80.00
- Graceful Gracie (hrs_17394842878) | 2yo F | 128lb | OR - | draw 4 | jockey Jonny Peate | trainer Mark Loughnane (14d 0/7) | headgear - | last run 13 days | form 6 | MARKET 0.7% | 09:00 median 101.00 | Matchbook 200.00
- Splintered (hrs_17393242916) | 2yo C | 133lb | OR - | draw 8 | jockey Olivia Tubb(5) | trainer Jonathan Portman (14d 1/11) | headgear - | last run 23 days | form 87 | MARKET 0.5% | 09:00 median 126.00 | Matchbook 350.00

## 6:30 Wolverhampton (AW) | race_id rac_32304574549 | Midnite Ain't Your Grandad's Bookie Handicap Stakes (Rider Restricted Race)
Flat | Class 3 | 5f21y | going Standard | AW | 11 runners | rating band 0-95 | age 3yo+
- Tan Rapido (hrs_35459018) | 5yo G | 122lb | OR 81 | draw 9 | jockey M. P. Sheehy | trainer Charlie Fellowes (14d 0/7) | headgear - | last run 13 days | form -78812 | MARKET 18.2% | 09:00 median 4.50 | Matchbook 5.10 | CHECK (skip line 4.27)
    comment: Tan Rapido arrives in good heart, a second last time out and a winner two starts back, just 13 days ago, and he has run over today's trip and on this going.
- Knebworth (hrs_29227856) | 6yo G | 131lb | OR 90 | draw 6 | jockey Donagh Murphy(5) | trainer Richard Hughes (14d 0/10) | headgear b | last run 9 days | form 200340 | MARKET 15.9% | 09:00 median 5.00 | Matchbook 6.00
    comment: Knebworth is yet to win in his last six starts, but a fourth two starts back and a third three starts back show he can go close, and he's fresh from a run nine days ago.
- Atomic Force (hrs_24358166) | 7yo G | 135lb | OR 94 | draw 10 | jockey Ryan Sexton | trainer Edward Bethell (14d 1/10) | headgear - | last run 65 days | form 110320 | MARKET 14.9% | 09:00 median 5.50 | Matchbook 6.40
    comment: Atomic Force won twice in his last six starts and was second two starts back, then third the run before, so the form stacks up, and he has run over today's trip and going before.
- Rhythm N Hooves (hrs_29918651) | 6yo G | 130lb | OR 89 | draw 7 | jockey Barry McHugh | trainer Robert Cowell (14d 0/5) | headgear v | last run 23 days | form 881821 | MARKET 12.2% | 09:00 median 6.50 | Matchbook 7.80
    comment: Rhythm N Hooves arrives in cracking nick, a winner last time out and a second two starts back, and he has run over today's trip and going before.
- Almaty Star (hrs_32030726) | 6yo G | 118lb | OR 77 | draw 4 | jockey Connor Planas | trainer Robert Cowell (14d 0/5) | headgear v | last run 23 days | form 083024 | MARKET 8.4% | 09:00 median 9.25 | Matchbook 11.50
    comment: Fourth last time out and a second two starts back suggest Almaty Star is running with some credit, and he has run over today's trip and going, but he's winless in his last six and was unplaced three starts back.
- Law of Average (hrs_36555484) | 5yo G | 130lb | OR 89 | draw 5 | jockey Joey Haynes | trainer Chelsea Banham (14d 0/1) | headgear - | last run 65 days | form 113143 | MARKET 7.3% | 09:00 median 11.00 | Matchbook 13.00
    comment: Law of Average has won three of his last six, including a win three starts back, and was third last time out, but he returns after 65 days off and has run over today's trip and going before.
- Rosenpur (hrs_39192048) | 6yo G | 123lb | OR 82 | draw 3 | jockey Liam Wright(3) | trainer Jennie Candlish (14d 3/15) | headgear h | last run 30 days | form 564916 | MARKET 6.5% | 09:00 median 11.50 | Matchbook 16.00
    comment: Rosenpur was a winner two starts back but has been sixth last time out, and his other recent runs include a ninth three starts back, so consistency is a worry.
- El Bufalo (hrs_38089191) | 5yo G | 118lb | OR 77 | draw 2 | jockey Zoe Lewis(7) | trainer Thomas Faulkner (14d 0/1) | headgear t | last run 140 days | form 256293 | MARKET 5.5% | 09:00 median 13.00 | Matchbook 19.00
    comment: El Bufalo is winless in his last six and returns after 140 days off, which makes him hard to fancy, though a third last time out, and a second six starts back, show he can hit the frame.
- Betsen (hrs_35040019) | 5yo G | 123lb | OR 82 | draw 11 | jockey Myla Coppins(5) | trainer Tony Carroll (14d 3/20) | headgear - | last run 23 days | form 185398 | MARKET 4.4% | 09:00 median 17.00 | Matchbook 23.00
    comment: The risk is a recent slide, with an eighth last time out and a ninth before that.
- Fiorella Princess (hrs_412728379) | 4yo F | 126lb | OR 85 | draw 1 | jockey Jack Dace(5) | trainer Robert Cowell (14d 0/5) | headgear p | last run 17 days | form 621451 | MARKET 4.4% | 09:00 median 19.00 | Matchbook 22.00
    comment: Fiorella Princess won last time out and has two wins in her last six, with a fresh 17-day gap and experience of today's trip and going, but a fifth and a fourth in between show the inconsistency.
- Alligator Alley (hrs_17762514) | 9yo G | 126lb | OR 85 | draw 8 | jockey William Pyle | trainer Ruth Carr (14d 2/9) | headgear - | last run 17 days | form 3-6980 | MARKET 2.1% | 09:00 median 29.00 | Matchbook 70.00
    comment: Winless in his last five, Alligator Alley has slipped from a third five starts back to an unplaced effort last time, though he's fresh enough after 17 days and has run over today's trip and going.

## 7:00 Wolverhampton (AW) | race_id rac_32304576486 | AW Trials Day - Lingfield 2nd Jan 2027 Handicap Stakes (Rider Restricted Race)
Flat | Class 5 | 7f36y | going Standard | AW | 11 runners | rating band 0-70 | age 4yo+
- Intervention (hrs_20260646) | 9yo G | 131lb | OR 66 | draw 10 | jockey M. P. Sheehy | trainer Michael Appleby (14d 1/11) | headgear p | last run 14 days | form 703012 | MARKET 25.9% | 09:00 median 3.00 | Matchbook 3.75 | CHECK (skip line 2.85)
    comment: Carrying 131 lb from draw 10, his only blemish is a patchy earlier run of form.
- Newsreader (hrs_35714399) | 5yo G | 130lb | OR 65 | draw 3 | jockey Myla Coppins(5) | trainer Tony Carroll (14d 3/20) | headgear - | last run 27 days | form 064552 | MARKET 21.3% | 09:00 median 4.00 | Matchbook 4.30
    comment: Newsreader was second last time out after a run of fourth and fifth-placed efforts, and he has run over today's trip and going before, but he is yet to win in his last six starts.
- Valentine Boy (hrs_50036392) | 4yo G | 130lb | OR 65 | draw 4 | jockey Jack Dace(5) | trainer Luke Dace (14d 0/2) | headgear h | last run 12 days | form 484653 | MARKET 17.5% | 09:00 median 4.50 | Matchbook 5.60
    comment: Valentine Boy comes into this fresh from a third last time out just 12 days ago and has run over today's trip and going, but he is winless in his last six and has finished fifth, sixth, fourth and eighth in the runs before.
- Split Elevens (hrs_21713517) | 8yo G | 132lb | OR 67 | draw 1 | jockey Kieren Fox | trainer John Butler (14d 3/9) | headgear - | last run 19 days | form 412222 | MARKET 11.2% | 09:00 median 7.00 | Matchbook 8.80
    comment: Split Elevens has finished second in each of his last four starts, after a win five starts back, so he is consistent but rarely gets his head in front, and he has run over today's trip and going.
- Queue Dos (hrs_42261198) | 4yo F | 135lb | OR 70 | draw 2 | jockey Alexandra Egan(5) | trainer J. S. Moore (14d 0/5) | headgear b | last run 12 days | form 738555 | MARKET 10.3% | 09:00 median 8.00 | Matchbook 9.20
    comment: The main risk is that she remains winless in her last six, so she needs to find that last bit to get her head in front.
- Giorgio M (hrs_37276246) | 5yo G | 129lb | OR 64 | draw 5 | jockey Jonny Peate | trainer Mark Loughnane (14d 0/7) | headgear tp | last run 137 days | form 647779 | MARKET 3.8% | 09:00 median 21.00 | Matchbook 27.00
    comment: The main risk is a 137-day absence after a ninth last time out, and he is yet to win in his last six starts.
- Mumayaz (hrs_24907519) | 7yo G | 134lb | OR 69 | draw 6 | jockey Stevie Donohoe | trainer Tony Carroll (14d 3/20) | headgear - | last run 18 days | form 567510 | MARKET 3.6% | 09:00 median 23.00 | Matchbook 27.00
    comment: Mumayaz won two starts back but was unplaced last time out, and he was beaten in the four runs before that win, so his form is patchy.
- Lessay (hrs_36062047) | 5yo G | 125lb | OR 60 | draw 8 | jockey Rhys Clutterbuck | trainer Patrick Morris (14d 0/6) | headgear p | last run 52 days | form 726148 | MARKET 2.9% | 09:00 median 29.00 | Matchbook 36.00
    comment: Lessay is hard to fancy after an eighth last time out and a 52-day break, with just one win in his last six starts, a victory three starts back.
- Royal Jet (hrs_31069367) | 6yo G | 128lb | OR 63 | draw 7 | jockey Molly Gunn(5) | trainer Tony Carroll (14d 3/20) | headgear - | last run 12 days | form 261790 | MARKET 1.2% | 09:00 median 51.00 | Matchbook 110.00
    comment: Royal Jet has been well beaten in his last two, a ninth then an unplaced run last time, and a win four starts back looks a long way off now.
- Assessment (hrs_27372471) | 7yo G | 130lb | OR 65 | draw 9 | jockey Liam Wright(3) | trainer Des Donovan (14d 0/0) | headgear t (1st time) | last run 753 days | form 00209/ | MARKET 1.2% | 09:00 median 67.00 | Matchbook 95.00
    comment: The risk is a 753-day absence, and a ninth last time out.
- Receipt (hrs_58412144) | 4yo G | 130lb | OR 65 | draw 11 | jockey Dougie Costello | trainer Tom Ellis (14d 2/16) | headgear h (1st time) | last run 12 days | form 109800 | MARKET 1.1% | 09:00 median 67.00 | Matchbook 100.00
    comment: Receipt is winless since a victory six starts back, with an eighth three starts back and a ninth four starts back, though a quick 12-day turnaround keeps him fit and he has run over today's trip and going.

## 7:30 Wolverhampton (AW) | race_id rac_32304578423 | ARC All Weather Bonus Is Back Handicap Stakes (Rider Restricted Race)
Flat | Class 5 | 1m142y | going Standard | AW | 12 runners | rating band 0-70 | age 3yo+
- R P McMurphy (hrs_52329578) | 4yo G | 137lb | OR 70 | draw 10 | jockey Jack Dace(5) | trainer Michael Appleby (14d 1/11) | headgear p | last run 24 days | form 341281 | MARKET 17.4% | 09:00 median 4.50 | Matchbook 5.30 | CHECK (skip line 4.27)
    comment: R P McMurphy won last time out and has two wins in his last six, with a fresh 24-day gap and experience of today's trip and going, but he's hard to fancy at 137 lb off a mark of 70.
- Susie Sioux (hrs_53808930) | 6yo M | 136lb | OR 69 | draw 1 | jockey Stevie Donohoe | trainer John Mackie (14d 0/3) | headgear - | last run 12 days | form 7251-6 | MARKET 12.3% | 09:00 median 5.50 | Matchbook 8.80
- Captain Parma (hrs_50339828) | 4yo G | 135lb | OR 68 | draw 8 | jockey Christian Howarth(3) | trainer James Owen (14d 7/34) | headgear - | last run 23 days | form 900590 | MARKET 9.5% | 09:00 median 8.50 | Matchbook 9.60
- Jojo's Legacy (hrs_53743207) | 3yo F | 130lb | OR 66 | draw 2 | jockey M. P. Sheehy | trainer Adrian Keatley (14d 0/4) | headgear t | last run 39 days | form 4-8655 | MARKET 9.2% | 09:00 median 8.50 | Matchbook 10.50
    comment: Jojo's Legacy has been consistent without winning, finishing fifth last time out and fifth two starts back, and she returns after 39 days with experience of today's trip and going.
- Criminal Shore (hrs_46233817) | 4yo G | 134lb | OR 67 | draw 5 | jockey Rhys Clutterbuck | trainer David O'Meara (14d 0/7) | headgear v | last run 17 days | form 635703 | MARKET 8.8% | 09:00 median 9.50 | Matchbook 10.50
    comment: Criminal Shore showed signs of life when third last time out, 17 days ago, and has run over today's trip and going, but he is yet to win in his last six starts and was unplaced, seventh and fifth in the runs before that. Carrying 134 lb from stall five, he looks a mid-pack type.
- Yehudi (hrs_41662271) | 4yo G | 132lb | OR 65 | draw 3 | jockey Hope Regan(7) | trainer Mark Loughnane (14d 0/7) | headgear t/bes | last run 24 days | form 546131 | MARKET 8.2% | 09:00 median 10.00 | Matchbook 11.50
    comment: Yehudi arrives in fine heart, a winner last time out and again three starts back, with a third two starts back, and he has run over today's trip and going.
- West Byfleet (hrs_63809431) | 3yo G | 131lb | OR 67 | draw 4 | jockey George Bass | trainer Jack Channon (14d 1/5) | headgear t (1st time) | last run 21 days | form 024560 | MARKET 7.7% | 09:00 median 10.00 | Matchbook 12.50
    comment: West Byfleet has been fading, with an unplaced run last time out after a sixth two starts back, though a second five starts back shows he has ability. He has run over today's trip and going, but he's yet to win in his last six and carries 131 lb from stall four.
- Galba (hrs_50434706) | 3yo C | 133lb | OR 69 | draw 12 | jockey Matthew Lloyd Slater(7) | trainer Kevin & Lauren Frost (14d 0/8) | headgear - | last run 21 days | form 323344 | MARKET 6.9% | 09:00 median 11.50 | Matchbook 13.50
    comment: Yet to win in that spell, so the main risk is finding that last bit to get his head in front from stall 12.
- Danehill Star (hrs_36454103) | 5yo G | 137lb | OR 70 | draw 11 | jockey Charlie Tucker(7) | trainer Tony Carroll (14d 3/20) | headgear b | last run 27 days | form 351132 | MARKET 6.6% | 09:00 median 10.00 | Matchbook 17.00
    comment: Danehill Star arrives in cracking form, second last time out, a third two starts back and a winner three and four starts back, and has run over today's trip and going.
- Lahan Kingman (hrs_55454084) | 3yo F | 132lb | OR 68 | draw 7 | jockey Donagh Murphy(5) | trainer Richard Hughes (14d 0/10) | headgear b | last run 26 days | form 224427 | MARKET 5.7% | 09:00 median 13.00 | Matchbook 17.50
    comment: Lahan Kingman is yet to win in her last six, though she has finished second three times in that spell, and she returns after 26 days having run over today's going before. A seventh last time out and 132 lb from stall 7 temper the case.
- Calyxoh (hrs_41305138) | 4yo G | 135lb | OR 68 | draw 6 | jockey Oliver Carmichael(7) | trainer Patrick Morris (14d 0/6) | headgear v | last run 11 days | form 304300 | MARKET 5.2% | 09:00 median 15.00 | Matchbook 18.50
- Rating (hrs_35137410) | 5yo M | 134lb | OR 67 | draw 9 | jockey Ben Ffrench Davis(5) | trainer Grace Harris (14d 1/6) | headgear p | last run 19 days | form 518327 | MARKET 2.6% | 09:00 median 24.50 | Matchbook 46.00
    comment: Beaten into seventh last time out, this mare is hard to fancy after just one win in her last six starts, though a second two starts back and a third three starts back show she can pick up a place.

## 8:00 Wolverhampton (AW) | race_id rac_32304580360 | Midnite A Next Generation Betting App Handicap Stakes (Rider Restricted Race)
Flat | Class 5 | 1m1f104y | going Standard | AW | 13 runners | rating band 0-75 | age 3yo+
- Ted Le Saux (hrs_59216227) | 4yo G | 133lb | OR 74 | draw 5 | jockey Charlie Tucker(7) | trainer Andrew Balding (14d 1/13) | headgear - | last run 20 days | form -13653 | MARKET 27.0% | 09:00 median 3.00 | Matchbook 3.30 | CHECK (skip line 2.85)
    comment: The main risk is consistency, with a fifth and a sixth in the two runs before that third.
- Sea The Light (hrs_52205321) | 4yo G | 132lb | OR 73 | draw 2 | jockey Kieren Fox | trainer John Butler (14d 3/9) | headgear p | last run 28 days | form 6-7071 | MARKET 11.1% | 09:00 median 7.00 | Matchbook 8.00
    comment: Sea The Light won last time out, but that came after a seventh, an unplaced run and another seventh before it, so consistency is lacking.
- Felix Gem (hrs_49142723) | 3yo G | 131lb | OR 75 | draw 4 | jockey Oliver Carmichael(7) | trainer Eve Johnson Houghton (14d 0/3) | headgear - | last run 46 days | form 5-2140 | MARKET 10.6% | 09:00 median 7.00 | Matchbook 9.40
    comment: Felix Gem won three starts back and was a fourth two starts ago, but he was unplaced last time out and returns after 46 days off.
- Cancan In The Rain (hrs_30980838) | 6yo G | 130lb | OR 71 | draw 13 | jockey Rhys Clutterbuck | trainer Gihan Arnolda (14d 0/5) | headgear - | last run 38 days | form 483065 | MARKET 9.8% | 09:00 median 8.00 | Matchbook 9.20
    comment: He is yet to win in his last six, but his figures stack up well.
- Mr Nugget (hrs_41325396) | 5yo G | 130lb | OR 71 | draw 3 | jockey Jack Dace(5) | trainer David Simcock (14d 1/4) | headgear - | last run 14 days | form 295695 | MARKET 6.9% | 09:00 median 10.00 | Matchbook 15.50
    comment: Mr Nugget is winless in his last six, with a fifth last time out, a ninth two starts back and a sixth three starts back, so he's hard to fancy off 130 lb. He has run over today's trip and going, and a second six starts back is the best of it.
- Paladin (hrs_35651518) | 5yo G | 132lb | OR 73 | draw 12 | jockey Taylor Fisher | trainer Kevin & Lauren Frost (14d 0/8) | headgear h (1st time) | last run 28 days | form 029900 | MARKET 5.8% | 09:00 median 12.00 | Matchbook 18.50
    comment: The risk is a poor recent run, with a second five starts back his only top-three finish and nothing better than ninth since.
- Oman (hrs_21995274) | 8yo G | 130lb | OR 71 | draw 10 | jockey Myla Coppins(5) | trainer Tony Carroll (14d 3/20) | headgear p | last run 39 days | form 796512 | MARKET 5.1% | 09:00 median 15.00 | Matchbook 19.50
    comment: Oman arrives in decent nick, a second last time out and a winner two starts back, but that came after a run of finishes of fifth or worse, and he has to shoulder 130 lb from draw 10.
- Cosmos Raj (hrs_23962127) | 8yo G | 133lb | OR 74 | draw 6 | jockey M. P. Sheehy | trainer David O'Meara (14d 0/7) | headgear - | last run 17 days | form 141822 | MARKET 5.0% | 09:00 median 15.00 | Matchbook 19.50
    comment: Cosmos Raj arrives in sound form, runner-up last time out and again two starts back, with a win four starts back, and he has run over today's trip and going.
- Camino Del Ray (hrs_50755425) | 4yo G | 132lb | OR 73 | draw 11 | jockey Ryan Sexton | trainer Julie Camacho (14d 0/11) | headgear p | last run 17 days | form 614841 | MARKET 5.0% | 09:00 median 15.00 | Matchbook 19.50
    comment: Camino Del Ray steps up after a win last time out, and he has two victories in his last six, with a fresh 17-day gap and experience of today's trip and going in his favour.
- The Sweet Escape (hrs_50875146) | 4yo G | 134lb | OR 75 | draw 8 | jockey Laura Pearson | trainer David Loughnane (14d 0/3) | headgear t | last run 38 days | form 112105 | MARKET 4.4% | 09:00 median 17.00 | Matchbook 22.00
    comment: Three wins in his last six starts is a decent record, though he was only a fifth last time out and unplaced the run before, and he returns after 38 days.
- Romance Spirit (hrs_57718710) | 3yo F | 131lb | OR 75 | draw 9 | jockey Luke Catton(3) | trainer Marco Botti (14d 0/4) | headgear - | last run 195 days | form 242 | MARKET 3.4% | 09:00 median 19.00 | Matchbook 34.00
    comment: Romance Spirit has been placed twice in her last three, a second last time out and a second three starts back, but she is yet to win and returns after 195 days off.
- Farasi Lane (hrs_21857024) | 8yo G | 134lb | OR 75 | draw 1 | jockey Aiden Brookes | trainer Micky Hammond (14d 0/15) | headgear p | last run 68 days | form 515386 | MARKET 3.4% | 09:00 median 23.00 | Matchbook 30.00
    comment: The risk is a 68-day layoff after a sixth last time out and an eighth before that.
- Livemore (hrs_65224803) | 3yo G | 131lb | OR 75 | draw 7 | jockey Connor Planas | trainer T. J. Kent (14d 1/2) | headgear - | last run 52 days | form 5160 | MARKET 2.3% | 09:00 median 35.00 | Matchbook 40.00
    comment: Livemore won three starts back, but he has been unplaced last time out and a sixth two starts back since, and returns after 52 days off.

## 8:30 Wolverhampton (AW) | race_id rac_32304582297 | Make The Move To Midnite Handicap Stakes (Rider Restricted Race)
Flat | Class 6 | 1m4f51y | going Standard | AW | 11 runners | rating band 0-60 | age 3yo+
- Saxophonic (hrs_55947675) | 3yo G | 132lb | OR 59 | draw 3 | jockey Jack Dace(5) | trainer David Simcock (14d 1/4) | headgear - | last run 13 days | form 644131 | MARKET 41.9% | 09:00 median 2.10 | Matchbook 2.10
    comment: Saxophonic arrives fresh from a win last time out, and a third two starts back, then another win three starts back, with just 13 days since that latest run and experience of today's trip and going.
- Havachoc (hrs_51491552) | 4yo G | 129lb | OR 51 | draw 6 | jockey Rhys Clutterbuck | trainer Patrick Morris (14d 0/6) | headgear p | last run 13 days | form 479653 | MARKET 12.8% | 09:00 median 6.00 | Matchbook 8.20
    comment: Winless in his last six, Havachoc has only a third last time out, 13 days ago, to hang his hat on, and before that a run of fifth, sixth, ninth and seventh efforts makes him hard to fancy.
- It's A Love Thing (hrs_23264549) | 8yo G | 134lb | OR 56 | draw 7 | jockey Jonny Peate | trainer Sam England (14d 5/24) | headgear - | last run 24 days | form 808324 | MARKET 10.6% | 09:00 median 7.50 | Matchbook 9.60
    comment: It's A Love Thing arrives in solid form, a fourth last time out after a second two starts back and a third three starts back, and he has run over today's trip and on the going before.
- Man of Desert (hrs_43002554) | 5yo G | 136lb | OR 58 | draw 11 | jockey Jake Dickson(5) | trainer Chris Dwyer (14d 0/2) | headgear tp | last run 13 days | form 776743 | MARKET 7.2% | 09:00 median 11.00 | Matchbook 13.50
    comment: Man of Desert comes into this on a fairly fresh 13-day turnaround after a third last time out, and he has run over today's trip and going, but he is winless in his last six and was seventh three starts back.
- Heart Sign (hrs_56007987) | 3yo G | 132lb | OR 59 | draw 4 | jockey Myla Coppins(5) | trainer Tony Carroll (14d 3/20) | headgear - | last run 21 days | form 637615 | MARKET 5.6% | 09:00 median 13.00 | Matchbook 18.50
    comment: Heart Sign signed off with a fifth last time out, 21 days ago, and a winner two starts back shows he can deliver, while he has run over today's trip and going before.
- The Bay Warrior (hrs_21938392) | 8yo G | 136lb | OR 58 | draw 5 | jockey Rose Dawes(3) | trainer Mark Usher (14d 0/3) | headgear p | last run 54 days | form 342720 | MARKET 5.4% | 09:00 median 15.00 | Matchbook 18.00
    comment: The Bay Warrior is yet to win in his last six starts and was unplaced last time out, 54 days ago, though two seconds in that spell and prior experience of today's trip and going keep him from being hopeless.
- Tiger Beetle (hrs_23055956) | 8yo G | 131lb | OR 53 | draw 2 | jockey Zoe Lewis(7) | trainer Thomas Faulkner (14d 0/1) | headgear tb | last run 14 days | form 783517 | MARKET 5.0% | 09:00 median 15.00 | Matchbook 22.00
    comment: Tiger Beetle was only seventh last time out and has just one win in his last six, a victory two starts back, so he is hard to fancy on this evidence.
- Kathleen Mary (hrs_44721754) | 4yo F | 137lb | OR 59 | draw 9 | jockey Laura Pearson | trainer Gihan Arnolda (14d 0/5) | headgear - | last run 21 days | form -76652 | MARKET 5.0% | 09:00 median 15.00 | Matchbook 21.00
    comment: Kathleen Mary arrives off a second last time out, a clear step up on a string of fifth, sixth and seventh finishes, and she has run over today's trip and going before.
- Sea of Charm (hrs_22327886) | 8yo M | 133lb | OR 55 | draw 1 | jockey William Cox | trainer Georgina Nicholls (14d 0/2) | headgear p | last run 14 days | form 632247 | MARKET 3.8% | 09:00 median 17.00 | Matchbook 32.00
    comment: Sea of Charm has been in the frame often lately, with a second three starts back and another four starts back, though she was only seventh last time out, 14 days ago. She has run over today's trip and going and is yet to win in her last six, which tempers the appeal of 133 lb.
- Hellion (hrs_56278243) | 4yo G | 138lb | OR 60 | draw 8 | jockey Dougie Costello | trainer Donald McCain (14d 3/25) | headgear - | last run 39 days | form 33-040 | MARKET 1.4% | 09:00 median 51.00 | Matchbook 120.00
    comment: The risk is a disappointing latest run, and he is yet to win in that spell, carrying 138 lb after 39 days off.
- Rogue Sea (hrs_35039361) | 6yo G | 138lb | OR 60 | draw 10 | jockey Taylor Fisher | trainer John & Rhys Flint (14d 0/0) | headgear - | last run 18 days | form 357-80 | MARKET 1.2% | 09:00 median 66.00 | Matchbook 130.00
    comment: The risk is that form line of fading finishes.
