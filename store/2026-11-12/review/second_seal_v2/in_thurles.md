# Card review packet: Thurles, 2026-11-12

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
{"meeting": "thurles", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 11:43 Thurles | race_id rac_32304173590 | Racing Again November 19th Beginners Steeplechase
Chase |  | 2m2f55y | going Good | Turf | 12 runners | rating band - | age 4yo+
- Kimy (hrs_37789969) | 6yo M | 159lb | OR 99 | draw 0 | jockey Danny Gilligan | trainer Thomas Mullins (14d 0/3) | headgear p | last run 24 days | form 093-02 | MARKET 19.7% | 09:00 median 4.00 | Matchbook 4.70 | CHECK (skip line 3.80)
    comment: Kimy comes here in good heart after a second last time out, and a third three starts back, with 24 days since that run and experience of both today's trip and the going.
- Whispering Willow (hrs_51341759) | 5yo M | 159lb | OR 97 | draw 0 | jockey Keith Donoghue | trainer Gavin Cromwell (14d 7/40) | headgear tp (1st time) | last run 38 days | form 360228 | MARKET 17.6% | 09:00 median 4.33 | Matchbook 5.50
    comment: Whispering Willow arrives off an eighth last time out, but a second two starts back and another second three starts back show she can get involved, and she has run over today's trip and going. Yet to win in her last six, she carries 159 lb after 38 days off, which holds her back.
- Might Be The One (hrs_50412635) | 5yo M | 159lb | OR 97 | draw 0 | jockey Darragh O'Keeffe | trainer Andrew McNamara (14d 0/2) | headgear t | last run 33 days | form 322-14 | MARKET 17.4% | 09:00 median 4.33 | Matchbook 5.50
    comment: She has run over today's trip and going, which is a plus.
- The Monkey Pole (hrs_49974519) | 6yo G | 166lb | OR - | draw 0 | jockey Miss Ella Herbison(7) | trainer N Dooly (14d 0/4) | headgear - | last run 11 days | form P35545 | MARKET 10.2% | 09:00 median 9.00 | Matchbook 8.20
    comment: Only 11 days since his last run, so The Monkey Pole is fit and consistent, finishing fifth, fourth, fifth and fifth in his last four, and he has run over today's trip and going before.
- I C U In My Dreams (hrs_46233593) | 6yo M | 159lb | OR - | draw 0 | jockey Mike O'Connor | trainer Conor Houlihan (14d 0/0) | headgear - | last run 181 days | form 4216-6 | MARKET 8.5% | 09:00 median 9.00 | Matchbook 11.50
- Itsaworkinmaniam (hrs_47129495) | 7yo G | 166lb | OR 98 | draw 0 | jockey Mr E Mahon(7) | trainer Brian M McMahon (14d 0/2) | headgear p | last run 38 days | form 26-588 | MARKET 6.5% | 09:00 median 13.00 | Matchbook 13.50
    comment: The risk is two eighth-place finishes in his last two outings, and 166 lb is a big weight to carry.
- Space Warrior (hrs_41013952) | 5yo G | 166lb | OR - | draw 0 | jockey Simon Torrens | trainer Thomas Mullins (14d 0/3) | headgear - | last run 18 days | form -99667 | MARKET 4.8% | 09:00 median 17.00 | Matchbook 19.00
    comment: Space Warrior is winless in his last five, finishing seventh last time out and sixth two starts back, so he's consistent without threatening.
- Jonny Carrol (hrs_51650060) | 5yo G | 166lb | OR - | draw 0 | jockey Jordan Gainford | trainer Moses McCabe (14d 0/2) | headgear t | last run 41 days | form P-7840 | MARKET 4.7% | 09:00 median 15.00 | Matchbook 23.00
    comment: The risk is a winless recent record, with 166 lb a stiff burden to carry.
- Harry's Dream (hrs_39208127) | 6yo G | 166lb | OR - | draw 0 | jockey Anna McGuinness(7) | trainer P. J. Rothwell (14d 0/16) | headgear t | last run 240 days | form 14428- | MARKET 4.3% | 09:00 median 17.00 | Matchbook 24.00
    comment: Harry's Dream was a second two starts back and a winner five starts back, but he was eighth last time out and returns after 240 days off, so fitness is a question.
- Angelsworknovrtime (hrs_26219452) | 10yo M | 159lb | OR 94 | draw 0 | jockey Conor Smithers(7) | trainer James Andrew Fahey (14d 0/5) | headgear t | last run 9 days | form 450-05 | MARKET 3.0% | 09:00 median 26.00 | Matchbook 32.00
    comment: Winless in her last five, Angelsworknovrtime was fifth last time out nine days ago and unplaced in the two runs before that, so she is hard to fancy under 159 lb.
- Tea In The Park (hrs_39699240) | 6yo G | 166lb | OR - | draw 0 | jockey Ricky Doyle | trainer Eamon Courtney (14d 0/3) | headgear - | last run 193 days | form 9252U- | MARKET 1.8% | 09:00 median 41.00 | Matchbook 55.00
    comment: Lightly raced and yet to win, Tea In The Park showed promise with a second two starts back and another second four starts back, but unseated last time out and returns after 193 days off. Carrying 166 lb, he looks unexposed with scope to improve.
- Kingston Silver (hrs_17389453697) | 5yo G | 166lb | OR - | draw 0 | jockey Philip Donovan | trainer W J Lanigan (14d 0/0) | headgear - | last run 30 days | form 0909 | MARKET 1.3% | 09:00 median 67.00 | Matchbook 75.00
    comment: Kingston Silver is winless in his last four, finishing ninth last time out and ninth again three starts back, which makes him hard to fancy.

## 12:18 Thurles | race_id rac_32304175527 | Horse & Jockey Handicap Steeplechase
Chase |  | 2m2f55y | going Good | Turf | 12 runners | rating band - | age 4yo+
- Stoneyford Lady (hrs_38649737) | 7yo M | 159lb | OR 103 | draw 0 | jockey Darragh O'Keeffe | trainer Henry de Bromhead (14d 8/43) | headgear tp | last run 39 days | form -534F2 | MARKET 21.3% | 09:00 median 3.75 | Matchbook 4.30 | CHECK (skip line 3.56)
    comment: Stoneyford Lady was second last time out and has finished in the first four in three of her last five, the exceptions a fall two starts back and a fifth five starts back, having run over today's trip and going before.
- Potters Pal (hrs_50188432) | 5yo G | 161lb | OR 105 | draw 0 | jockey Danny Gilligan | trainer G Mangan (14d 0/1) | headgear ht | last run 48 days | form 51P-31 | MARKET 16.3% | 09:00 median 4.50 | Matchbook 6.00
    comment: Potters Pal won last time out and has two wins in his last five starts, though a pulled up three starts back shows his form has its ups and downs.
- Aurea Fortuna (hrs_38649562) | 7yo G | 160lb | OR 104 | draw 0 | jockey Daniel King | trainer A. J. Martin (14d 0/10) | headgear p (1st time) | last run 29 days | form 59P-43 | MARKET 11.6% | 09:00 median 7.00 | Matchbook 8.00
    comment: Aurea Fortuna arrives in better heart after a third last time out and a fourth two starts back, and he has run over today's trip and going, but he is yet to win in his last five starts and carries a hefty 160 lb.
- Cappa Hill (hrs_40494265) | 6yo G | 168lb | OR 112 | draw 0 | jockey Peter Smithers(5) | trainer Sean Joseph Allen (14d 0/0) | headgear t | last run 32 days | form 754934 | MARKET 11.5% | 09:00 median 7.00 | Matchbook 8.00
- Littlebiggie (hrs_35054964) | 9yo M | 163lb | OR 107 | draw 0 | jockey Conor Clarke(7) | trainer Ray Hackett (14d 0/3) | headgear t | last run 21 days | form -480F2 | MARKET 8.4% | 09:00 median 9.50 | Matchbook 11.00
    comment: Littlebiggie bounces back from a fall with a second last time out, and at 21 days since that run she should be fit. She has run over today's trip and on this going, and her 163 lb burden is the one reservation.
- Burlington House (hrs_37052323) | 5yo G | 146lb | OR 90 | draw 0 | jockey Phillip Enright | trainer Oliver McKiernan (14d 0/9) | headgear t | last run 31 days | form 542-7F | MARKET 7.0% | 09:00 median 11.00 | Matchbook 12.50
    comment: Burlington House fell last time out and was seventh two starts back, so he is hard to fancy, though a second three starts back shows he has ability, and 31 days off gives him time to recover.
- That's About Right (hrs_33774461) | 8yo G | 150lb | OR 94 | draw 0 | jockey Shane O'Callaghan(3) | trainer P. J. Rothwell (14d 0/16) | headgear tp | last run 35 days | form 048485 | MARKET 5.9% | 09:00 median 13.00 | Matchbook 16.00
    comment: Winless in his last six, with a fifth last time out and an eighth two starts back, That's About Right is hard to fancy, and a 35-day break doesn't help.
- Springboard (hrs_39978218) | 7yo G | 148lb | OR 92 | draw 0 | jockey Cian Quirke | trainer Michael J McDonagh (14d 0/4) | headgear - | last run 18 days | form 1-9519 | MARKET 5.9% | 09:00 median 13.00 | Matchbook 16.50
    comment: Springboard was beaten into ninth last time out and has finished ninth, fifth and ninth in three of his last five, which makes him hard to fancy.
- Mags Nelson (hrs_40920208) | 7yo G | 161lb | OR 105 | draw 0 | jockey Donagh Meyler | trainer Ross O'Sullivan (14d 1/23) | headgear - | last run 29 days | form 183-44 | MARKET 5.4% | 09:00 median 15.00 | Matchbook 18.00
    comment: Mags Nelson has run in the frame twice lately, a fourth last time out and a fourth two starts back, but he hasn't won since five starts back, and carrying 161 lb off 105 with a yard in poor form (1/23) makes him hard to fancy.
- Beauforts Storm (hrs_35351323) | 7yo M | 163lb | OR 107 | draw 0 | jockey Mr D Doyle(5) | trainer Timothy Doyle (14d 0/2) | headgear b (1st time) | last run 39 days | form U744P9 | MARKET 2.6% | 09:00 median 26.00 | Matchbook 44.00
    comment: Winless in her last six, Beauforts Storm has still run over today's trip and going, and she's rated 114 by us, third best of twelve, with a fourth three starts back suggesting she can bounce back after 39 days off; carrying 163 lb off 107 is the main risk.
- Banjaxed (hrs_29104544) | 9yo G | 166lb | OR 110 | draw 0 | jockey John Shinnick | trainer Mrs Lorna Fowler (14d 1/2) | headgear b (1st time) | last run 21 days | form 486-4P | MARKET 2.3% | 09:00 median 34.00 | Matchbook 42.00
- Orkneys Jack (hrs_51373693) | 7yo G | 155lb | OR 99 | draw 0 | jockey Sean O'Keeffe | trainer L Young (14d 0/0) | headgear - | last run 37 days | form 135575 | MARKET 1.7% | 09:00 median 41.00 | Matchbook 70.00
    comment: The risk is a recent slide, with a fifth last time out and a seventh before that, after 37 days off.

## 12:53 Thurles | race_id rac_32304177464 | www.thurlesraces.ie Handicap Steeplechase
Chase |  | 2m5f132y | going Good | Turf | 16 runners | rating band 0-100 | age 4yo+
- Onefortheditch (hrs_30122974) | 8yo M | 159lb | OR 90 | draw 0 | jockey Darragh O'Keeffe | trainer Eamonn Francis Gallagher (14d 0/1) | headgear - | last run 7 days | form 226-5U | MARKET 20.4% | 09:00 median 3.50 | Matchbook 4.30 | CHECK (skip line 3.32)
    comment: Two seconds in her last five starts, and she's turned out quickly just seven days after unseating, having run over today's trip and going before.
- Way Down South (hrs_37701594) | 7yo G | 168lb | OR 99 | draw 0 | jockey Alan O'Sullivan(5) | trainer Gillian Scott (14d 1/2) | headgear tp | last run 25 days | form 2-3517 | MARKET 11.3% | 09:00 median 6.00 | Matchbook 8.00
    comment: Way Down South won two starts back and has been in the first three twice in his last five, with a second five starts back and a third four back, and he has run over today's trip and going before.
- Island McCoo (hrs_31287816) | 9yo G | 159lb | OR 90 | draw 0 | jockey Eoin Staples(5) | trainer Donncha Duggan (14d 0/2) | headgear t | last run 26 days | form 184535 | MARKET 9.6% | 09:00 median 8.00 | Matchbook 8.80
    comment: Island McCoo has been consistent without winning lately, a fifth last time out and a third two starts back, and he has run over today's trip and going before after 26 days off.
- Gortmore Lady (hrs_412673023) | 6yo M | 148lb | OR 79 | draw 0 | jockey Kevin Healy(7) | trainer Ciaran Murphy (14d 0/18) | headgear b | last run 21 days | form 754252 | MARKET 9.4% | 09:00 median 7.50 | Matchbook 10.00
    comment: Gortmore Lady is winless in her last six, though she was second last time out and a fifth two starts back, and she has run over today's trip and going before.
- Tantrum Boy (hrs_53539626) | 6yo G | 149lb | OR 80 | draw 0 | jockey Phillip Enright | trainer Brian M McMahon (14d 0/2) | headgear b (1st time) | last run 26 days | form 844204 | MARKET 8.8% | 09:00 median 8.50 | Matchbook 9.80
    comment: Winless in his last six, Tantrum Boy is hard to fancy, though a fourth last time out and a second three starts back show he is not out of form, and he has run over today's trip and going before.
- Orlando Spirit (hrs_412672925) | 6yo G | 154lb | OR 85 | draw 0 | jockey Sean O'Keeffe | trainer Paul Power (14d 0/1) | headgear - | last run 183 days | form 0238-4 | MARKET 7.3% | 09:00 median 9.00 | Matchbook 13.00
    comment: Fourth last time out and placed in a second and a third earlier, Orlando Spirit is yet to win in his last five starts, and he has run on today's going before. A 183-day absence and 154 lb on an official mark of 85 temper the case.
- Grange Walk (hrs_16596174) | 11yo G | 164lb | OR 95 | draw 0 | jockey Daniel King | trainer John Patrick Ryan (14d 0/11) | headgear b | last run 21 days | form 6B7763 | MARKET 6.6% | 09:00 median 11.00 | Matchbook 13.50
    comment: A weight of 164 lb off an official 95 is the one reservation.
- Sharetheknowledge (hrs_35054691) | 7yo G | 158lb | OR 89 | draw 0 | jockey Sean Flanagan | trainer W J Burke (14d 0/2) | headgear t | last run 21 days | form 4-0456 | MARKET 5.7% | 09:00 median 13.00 | Matchbook 15.00
    comment: The risk is a winless run in his last five, with a sixth last time out, and 158 lb to carry.
- Vroomvroomboo (hrs_38532858) | 8yo M | 147lb | OR 78 | draw 0 | jockey Michael Kenneally(3) | trainer James Andrew Fahey (14d 0/5) | headgear t | last run 9 days | form -80668 | MARKET 4.5% | 09:00 median 17.00 | Matchbook 18.50
    comment: Winless in her last five, Vroomvroomboo has finished eighth last time out, a sixth two starts back and another sixth three starts back, so she is hard to fancy carrying 147 lb.
- Hickeys Hill (hrs_38666495) | 7yo G | 153lb | OR 84 | draw 0 | jockey Danny Gilligan | trainer G Mangan (14d 0/1) | headgear - | last run 66 days | form 15-90P | MARKET 3.1% | 09:00 median 17.00 | Matchbook 38.00
    comment: Hickeys Hill won five starts back but has tailed off since, with a ninth three starts back and then pulled up last time out, and he returns after 66 days off.
- Synchronize (hrs_37246587) | 5yo G | 152lb | OR 83 | draw 0 | jockey John Shinnick | trainer J Morrison (14d 0/2) | headgear - | last run 9 days | form 0-0089 | MARKET 3.1% | 09:00 median 23.00 | Matchbook 28.00
    comment: Synchronize is winless in his last five, finishing ninth last time out and eighth two starts back, though he has run on today's going and is back quickly after nine days.
- It's Time Again (hrs_24228792) | 10yo M | 157lb | OR 88 | draw 0 | jockey Jordan Gainford | trainer David Richard Barry (14d 0/0) | headgear p | last run 26 days | form F89P2P | MARKET 3.0% | 09:00 median 26.00 | Matchbook 30.00
- Esticky End (hrs_21686623) | 8yo G | 148lb | OR 79 | draw 0 | jockey Dylan Robinson | trainer Tom McGuinness (14d 0/1) | headgear - | last run 18 days | form P2110P | MARKET 2.2% | 09:00 median 34.00 | Matchbook 42.00
    comment: Esticky End is hard to fancy after being pulled up last time out and finishing unplaced the run before, though he won three and four starts back and has run on today's going before.
- Barton Sky (hrs_38002601) | 8yo G | 159lb | OR 90 | draw 0 | jockey Harry Sexton(7) | trainer John Joseph Hanlon (14d 0/11) | headgear t | last run 49 days | form P-5070 | MARKET 1.9% | 09:00 median 34.00 | Matchbook 55.00
    comment: Barton Sky is winless in his last five, with a fifth four starts back his best recent effort, and he returns after 49 days off carrying 159 lb off an official mark of 90.
- Annie Questions (hrs_34253499) | 8yo M | 141lb | OR 72 | draw 0 | jockey Mr M J Walsh(7) | trainer Brendan Maurice Walsh (14d 0/3) | headgear h | last run 76 days | form -18040 | MARKET 1.6% | 09:00 median 41.00 | Matchbook 70.00
    comment: Annie Questions is hard to fancy after being unplaced last time out and a fourth two starts back, with her only win five starts back and a 76-day absence to overcome.
- Battle Of Benburb (hrs_21678636) | 9yo G | 142lb | OR 73 | draw 0 | jockey Mr P Verling(7) | trainer Patrick Michael Verling (14d 0/0) | headgear b | last run 21 days | form PP-04P | MARKET 1.3% | 09:00 median 51.00 | Matchbook 120.00
    comment: Battle Of Benburb has been pulled up in three of his last five, including last time out, though a fourth two starts back shows some ability, and he has run over today's trip and going.

## 1:28 Thurles | race_id rac_32304179401 | Irish Stallion Farms EBF Maiden Hurdle
Hurdle |  | 2m6f176y | going Good | Turf | 7 runners | rating band - | age 4yo+
- Doctor Elvis (hrs_38074057) | 7yo G | 158lb | OR 117 | draw 0 | jockey Jack Kennedy | trainer Gordon Elliott (14d 9/59) | headgear b | last run 18 days | form 20-2P2 | MARKET 59.0% | 09:00 median 1.53 | Matchbook 1.60
- Zambezi Moon (hrs_51341815) | 6yo G | 166lb | OR 111 | draw 0 | jockey J. J. Slevin | trainer David Richard Barry (14d 0/0) | headgear - | last run 48 days | form P1-562 | MARKET 28.0% | 09:00 median 3.00 | Matchbook 3.55
- The Goose's Acre (hrs_47655503) | 6yo G | 158lb | OR 92 | draw 0 | jockey Alan O'Sullivan(5) | trainer Eamon Courtney (14d 0/3) | headgear p (1st time) | last run 206 days | form 4009P- | MARKET 5.7% | 09:00 median 15.00 | Matchbook 17.50
- Through The Storm (hrs_47952996) | 5yo G | 158lb | OR - | draw 0 | jockey Cian Quirke | trainer David Harry Kelly (14d 0/6) | headgear b (1st time) | last run 50 days | form 46/805 | MARKET 2.6% | 09:00 median 29.00 | Matchbook 48.00
- Pacy Macie (hrs_60343493) | 5yo M | 151lb | OR 83 | draw 0 | jockey Mr B J Walsh(7) | trainer Barry John Walsh (14d 0/0) | headgear p (1st time) | last run 54 days | form P-3657 | MARKET 2.1% | 09:00 median 34.00 | Matchbook 60.00
- Minella Maverick (hrs_17391809834) | 5yo G | 158lb | OR - | draw 0 | jockey Daniel King | trainer John Patrick Ryan (14d 0/11) | headgear - | last run 21 days | form 07 | MARKET 1.8% | 09:00 median 41.00 | Matchbook 75.00
- Go Mike Go (hrs_49325864) | 7yo G | 158lb | OR - | draw 0 | jockey Mr Ian Cribbin(7) | trainer Peter McCreery (14d 0/1) | headgear p | last run 26 days | form PUU/0P | MARKET 0.9% | 09:00 median 81.00 | Matchbook 42.00

## 2:03 Thurles | race_id rac_32304181338 | Sign Up To GavinLynchRacing.com Maiden Hurdle
Hurdle |  | 2m4f | going Good | Turf | 12 runners | rating band - | age 4yo+
- Gunnery Sergeant (hrs_40095629) | 6yo G | 166lb | OR 102 | draw 0 | jockey Jack Kennedy | trainer Gordon Elliott (14d 9/59) | headgear tp | last run 20 days | form -85532 | MARKET 39.3% | 09:00 median 2.10 | Matchbook 2.30
- Beeverstown Boy (hrs_17393180336) | 6yo G | 166lb | OR - | draw 0 | jockey Paddy Cody(7) | trainer M A Cahill (14d 0/2) | headgear - | last run 20 days | form 63 | MARKET 19.9% | 09:00 median 4.33 | Matchbook 4.30
- Flashy Fred (hrs_64780926) | 4yo G | 165lb | OR - | draw 0 | jockey Mike O'Connor | trainer Conor Houlihan (14d 0/0) | headgear - | last run 105 days | form 3220 | MARKET 12.5% | 09:00 median 5.50 | Matchbook 8.20
- Quarry Road (hrs_17392709943) | 4yo G | 165lb | OR - | draw 0 | jockey Miss Ella Herbison(7) | trainer Moses McCabe (14d 0/2) | headgear - | last run 41 days | form 5 | MARKET 9.4% | 09:00 median 8.50 | Matchbook 9.80
- Kiltinan (hrs_58745701) | 5yo G | 166lb | OR - | draw 0 | jockey Eoin Staples(5) | trainer Michael J McDonagh (14d 0/4) | headgear b | last run 18 days | form 4-P8 | MARKET 9.3% | 09:00 median 7.50 | Matchbook 11.50
- Two Pats (hrs_17395288239) | 5yo G | 166lb | OR - | draw 0 | jockey Cian Quirke | trainer Louise G Lyons (14d 0/0) | headgear - | last run - days | form - | MARKET 2.7% | 09:00 median 29.00 | Matchbook 36.00
- Bayswater Bloom (hrs_57071777) | 5yo M | 159lb | OR - | draw 0 | jockey Philip Donovan | trainer Miss Evanna McCutcheon (14d 0/1) | headgear t | last run 21 days | form 687839 | MARKET 2.4% | 09:00 median 29.00 | Matchbook 44.00
- Vango At Dawn (hrs_17394406904) | 4yo G | 165lb | OR - | draw 0 | jockey Kevin Healy(7) | trainer Colin Motherway (14d 0/3) | headgear - | last run 18 days | form 8 | MARKET 1.8% | 09:00 median 41.00 | Matchbook 70.00
- Potters Queen (hrs_17394784470) | 5yo M | 159lb | OR - | draw 0 | jockey Phillip Enright | trainer G Mangan (14d 0/1) | headgear ht (1st time) | last run 11 days | form 3P-P | MARKET 0.9% | 09:00 median 67.00 | Matchbook 210.00
- George Dundee (hrs_17393178250) | 5yo G | 166lb | OR - | draw 0 | jockey Danny Power(7) | trainer Terence O'Brien (14d 1/3) | headgear - | last run 21 days | form 7-5100 | MARKET 0.7% | 09:00 median 81.00 | Matchbook 300.00
- Long Story (hrs_65069081) | 6yo G | 166lb | OR - | draw 0 | jockey Daniel King | trainer John Neilan (14d 0/0) | headgear p (1st time) | last run 18 days | form 779500 | MARKET 0.6% | 09:00 median 101.00 | Matchbook 270.00
- Soldier Power (hrs_17394376657) | 4yo F | 158lb | OR - | draw 0 | jockey Josh Williamson(3) | trainer Mrs Y Dunleavy (14d 0/1) | headgear - | last run 11 days | form F | MARKET 0.4% | 09:00 median 201.00 | Matchbook 310.00

## 2:38 Thurles | race_id rac_32304183275 | Book Your Christmas Party Here On December 19th Mares Handicap Hurdle
Hurdle |  | 2m4f | going Good | Turf | 11 runners | rating band - | age 3yo+
- Shoda (hrs_40260647) | 5yo M | 162lb | OR 111 | draw 0 | jockey Richard Deegan | trainer Joseph Patrick O'Brien (14d 2/28) | headgear t | last run 32 days | form 397-81 | MARKET 20.3% | 09:00 median 4.00 | Matchbook 4.40 | CHECK (skip line 3.80)
    comment: The risk is a burdensome 162 lb after three modest efforts before that win.
- Fratas (hrs_32779978) | 6yo M | 166lb | OR 115 | draw 0 | jockey J. J. Slevin | trainer Joseph Patrick O'Brien (14d 2/28) | headgear - | last run 32 days | form 2/20-2 | MARKET 15.3% | 09:00 median 5.00 | Matchbook 6.20
    comment: Fratas arrives in cracking nick, second last time out and runner-up in three of her last four, with just the one blip between, and she has run on today's going before.
- Tutu Twist (hrs_52709188) | 5yo M | 154lb | OR 103 | draw 0 | jockey Darragh O'Keeffe | trainer Henry de Bromhead (14d 8/43) | headgear t | last run 35 days | form 233-22 | MARKET 14.7% | 09:00 median 5.50 | Matchbook 6.20
    comment: Tutu Twist has been a model of consistency, finishing second last time out, second two starts back and third three starts back, and she has run over today's trip and going before. Yet winless in her last five and carrying 154 lb after 35 days off, she may again find one too good.
- Tir Og (hrs_46450215) | 5yo M | 164lb | OR 113 | draw 0 | jockey Conor Clarke(7) | trainer E Seymour (14d 1/1) | headgear p | last run 11 days | form 704041 | MARKET 12.9% | 09:00 median 6.00 | Matchbook 7.40
    comment: The risk is a patchy record before that, with just a fourth two starts back in the preceding runs.
- Theflyingbee (hrs_36614354) | 9yo M | 165lb | OR 114 | draw 0 | jockey Mr J R Martin(7) | trainer F G Hand (14d 0/0) | headgear t | last run 22 days | form 3-2256 | MARKET 10.4% | 09:00 median 7.50 | Matchbook 9.00
    comment: Twice second and once third in her last five, Theflyingbee has run over today's trip and going and returns fresh after 22 days, while our 126 puts her top of the 11. The risk is 165 lb on her back and a sixth last time out.
- Jennyfromtheblock (hrs_50433285) | 6yo M | 154lb | OR 103 | draw 0 | jockey Mark Walsh | trainer E McNamara (14d 0/6) | headgear - | last run 26 days | form 1/F-51 | MARKET 9.3% | 09:00 median 8.50 | Matchbook 10.00
    comment: Jennyfromtheblock arrives fresh from a win last time out, with a fifth two starts back and a faller three runs ago, and she has run over today's trip and going.
- Pure Logic (hrs_41813905) | 6yo M | 153lb | OR 102 | draw 0 | jockey Harry Sexton(7) | trainer John Joseph Hanlon (14d 0/11) | headgear tp | last run 42 days | form P31236 | MARKET 5.6% | 09:00 median 12.00 | Matchbook 21.00
    comment: Pure Logic has slipped to a sixth last time out after a third two starts back, and 42 days off leaves her something to prove, though she has run over today's trip and on the going before.
- Mastertown Miss (hrs_63171717) | 4yo F | 148lb | OR 98 | draw 0 | jockey Cian Quirke | trainer David Harry Kelly (14d 0/6) | headgear h | last run 39 days | form 28-443 | MARKET 5.0% | 09:00 median 15.00 | Matchbook 19.50
    comment: Mastertown Miss was a third last time out, and she was a fourth two starts back, so she's consistent, yet she's winless in her last five and has had 39 days off.
- Stepdance (hrs_31300192) | 6yo M | 158lb | OR 107 | draw 0 | jockey Kevin Healy(7) | trainer Declan Queally (14d 0/2) | headgear - | last run 42 days | form 558-P7 | MARKET 2.9% | 09:00 median 23.00 | Matchbook 42.00
    comment: Stepdance is winless in her last five, with a seventh last time out and a pulled up two starts back, though she has run on today's going before and her 42-day break gives her a fresh outing.
- Preparations (hrs_40260703) | 5yo M | 161lb | OR 110 | draw 0 | jockey Josh Younge(7) | trainer A. Slattery (14d 1/22) | headgear - | last run 28 days | form 17/P | MARKET 1.9% | 09:00 median 41.00 | Matchbook 60.00
    comment: Preparations was pulled up last time out and was a seventh two starts back, so the recent trend is poor, and a trainer going 1/22 lately and a weight of 161 lb don't help. On the plus side, she won three starts back and has run on today's going before.
- Crystabel (hrs_45856020) | 5yo M | 153lb | OR 102 | draw 0 | jockey Daniel King | trainer John Patrick Ryan (14d 0/11) | headgear - | last run 20 days | form 135455 | MARKET 1.6% | 09:00 median 41.00 | Matchbook 70.00
    comment: Fifth last time out and again two starts back, Crystabel has been consistent without threatening since winning six starts back, though she has run over today's trip and going and is fresh enough after 20 days.

## 3:15 Thurles | race_id rac_32304553242 | Two-Mile Borris Handicap Hurdle (Div I)
Hurdle |  | 2m16y | going Good | Turf | 17 runners | rating band 0-100 | age 3yo+
- Max Meridius (hrs_40260661) | 5yo G | 160lb | OR 92 | draw 0 | jockey Danny Gilligan | trainer Thomas Mullins (14d 0/3) | headgear p | last run 23 days | form 051055 | MARKET 15.9% | 09:00 median 5.00 | Matchbook 5.30 | CHECK (skip line 4.75)
    comment: Max Meridius has finished fifth in each of his last two starts and won four starts back, so he's consistent without quite getting his head in front lately.
- Daisy Fingall (hrs_48853805) | 6yo M | 163lb | OR 95 | draw 0 | jockey Darragh O'Keeffe | trainer Henry de Bromhead (14d 8/43) | headgear - | last run 208 days | form 6/027- | MARKET 10.1% | 09:00 median 7.00 | Matchbook 9.20
    comment: Daisy Fingall was a second two starts back but has since managed only a seventh last time out, and she returns after 208 days off.
- I Feel Fine (hrs_50465772) | 6yo G | 155lb | OR 87 | draw 0 | jockey Daniel King | trainer M A Molloy (14d 0/0) | headgear - | last run 66 days | form 6P-460 | MARKET 9.6% | 09:00 median 8.00 | Matchbook 9.00
    comment: Without a win in his last five, I Feel Fine was unplaced last time, though a sixth two starts back and a fourth three starts back show he can be competitive, and he has run over today's trip and going.
- Liceo (hrs_36192702) | 6yo G | 168lb | OR 100 | draw 0 | jockey P J O'Hanlon | trainer Dermot A McLoughlin (14d 0/11) | headgear tp | last run 33 days | form 935352 | MARKET 8.3% | 09:00 median 7.50 | Matchbook 13.50
    comment: Liceo comes here in solid nick, a second last time out and a fifth two starts back, and he has run over today's trip and going before. Yet to win in his last six, he's back after 33 days, and carrying 168 lb is the main risk.
- Jaadil (hrs_35528612) | 5yo M | 160lb | OR 92 | draw 0 | jockey Patrick M O'Brien(5) | trainer E McNamara (14d 0/6) | headgear - | last run 25 days | form -PF953 | MARKET 7.9% | 09:00 median 9.50 | Matchbook 11.50
    comment: Jaadil was third last time out, and she's had 25 days to recover, but she's yet to win in her last five starts, with a ninth three starts back and a fall before that. She has run over today's trip and going, yet 160 lb and a ranking of tenth of 17 make this a midfield task.
- Ozark's Walk (hrs_52087252) | 6yo G | 152lb | OR 84 | draw 0 | jockey Philip Byrnes | trainer Riceal Dunne (14d 0/0) | headgear - | last run 129 days | form 2009-0 | MARKET 7.6% | 09:00 median 11.00 | Matchbook 11.50
- Arctic Piper (hrs_40669041) | 7yo M | 152lb | OR 84 | draw 0 | jockey Michael Kenneally(3) | trainer R Donohoe (14d 0/3) | headgear - | last run 30 days | form -F9093 | MARKET 6.8% | 09:00 median 11.00 | Matchbook 13.50
    comment: Arctic Piper bounced back with a third last time out after a run of ninth, unplaced, ninth and a faller, and she has run over today's trip and going before.
- Grennanstown Lady (hrs_57008273) | 5yo M | 153lb | OR 85 | draw 0 | jockey Eoghan Finegan(5) | trainer Gerard Keane (14d 0/6) | headgear - | last run 20 days | form 54-0B3 | MARKET 5.9% | 09:00 median 11.00 | Matchbook 18.50
    comment: Winless in her last five, Grennanstown Lady at least arrives with a third last time out, 20 days ago, and has run over today's trip and going before.
- Ddakji (hrs_59961482) | 4yo G | 158lb | OR 90 | draw 0 | jockey Mike O'Connor | trainer Conor Houlihan (14d 0/0) | headgear h | last run 21 days | form 0-9865 | MARKET 5.3% | 09:00 median 12.00 | Matchbook 20.00
    comment: Ddakji is winless in his last five, finishing fifth last time out after a sixth, an eighth and a ninth, so it is hard to fancy him off 158 lb and an official mark of 90.
- Polly Poppins (hrs_41325123) | 6yo M | 152lb | OR 84 | draw 0 | jockey Ethan O'Sullivan(7) | trainer Bernard Martin Crowley (14d 0/2) | headgear - | last run 11 days | form 764429 | MARKET 5.0% | 09:00 median 15.00 | Matchbook 19.00
- Pakens Rock (hrs_15942199) | 13yo G | 168lb | OR 100 | draw 0 | jockey Niall Moore(5) | trainer Donncha Duggan (14d 0/2) | headgear - | last run 25 days | form 774-95 | MARKET 3.9% | 09:00 median 17.00 | Matchbook 28.00
- Duke Otto (hrs_22731436) | 8yo G | 163lb | OR 95 | draw 0 | jockey Conor Smithers(7) | trainer Patrick J Flynn (14d 3/10) | headgear b (1st time) | last run 11 days | form 40-P00 | MARKET 3.4% | 09:00 median 21.00 | Matchbook 28.00
    comment: Duke Otto has been out of the frame in his last four, including a pulled up three starts back, with a fourth five starts back his best recent effort, though he has run over today's trip and going and is fresh from just 11 days ago.
- Big Dee (hrs_37193247) | 7yo G | 164lb | OR 96 | draw 0 | jockey G B Noonan | trainer Eoin Christopher McCarthy (14d 0/15) | headgear h | last run 39 days | form 3P-P70 | MARKET 3.2% | 09:00 median 23.00 | Matchbook 34.00
    comment: The risk is form that reads poorly: unplaced last time, a seventh two starts back and two pulled-up efforts before that.
- Titanium (hrs_28891485) | 7yo G | 168lb | OR 100 | draw 0 | jockey Kevin Healy(7) | trainer Ciaran Murphy (14d 0/18) | headgear v | last run 11 days | form 0/30-0 | MARKET 2.8% | 09:00 median 23.00 | Matchbook 38.00
    comment: Titanium has been unplaced in three of his last four, with a third three starts back the only bright spot, though he's fit enough after 11 days and has run over today's trip and going.
- Dark Berkshire (hrs_54432448) | 6yo G | 140lb | OR 72 | draw 0 | jockey Shane O'Callaghan(3) | trainer P. J. Rothwell (14d 0/16) | headgear b | last run 20 days | form 036959 | MARKET 2.4% | 09:00 median 29.00 | Matchbook 42.00
    comment: Without a win in his last six outings, Dark Berkshire has finished ninth last time out, and a third five starts back is the only podium finish in that spell.
- Vairue (hrs_24506524) | 10yo G | 144lb | OR 76 | draw 0 | jockey Josh Williamson(3) | trainer Ms Helen P Markham (14d 0/4) | headgear - | last run 11 days | form /7F940 | MARKET 1.5% | 09:00 median 34.00 | Matchbook 95.00
    comment: Vairue is winless in his last five, with an unplaced effort last time, a fourth two starts back and a fall four runs ago, so he is hard to fancy at 144 lb.
- Kidam Roque (hrs_412693015) | 6yo G | 148lb | OR 80 | draw 0 | jockey Anna McGuinness(7) | trainer I Madden (14d 0/0) | headgear t (1st time) | last run 17 days | form 9-PU0P | MARKET 0.6% | 09:00 median 101.00 | Matchbook 300.00
    comment: Kidam Roque has been pulled up last time out and is winless in his last five starts, with an unseated and another pulled up in that spell, so the form is poor.

## 3:48 Thurles | race_id rac_32304185212 | Two-Mile Borris Handicap Hurdle (Div II)
Hurdle |  | 2m16y | going Good | Turf | 17 runners | rating band 0-100 | age 3yo+
- Sinbad My Dad (hrs_36986173) | 5yo G | 160lb | OR 92 | draw 0 | jockey Ben Kennedy(7) | trainer Seamus Fahey (14d 0/1) | headgear - | last run 5 days | form 66/0-4 | MARKET 16.1% | 09:00 median 4.33 | Matchbook 5.90 | CHECK (skip line 4.11)
    comment: Fourth last time out and back quickly after just five days, Sinbad My Dad has run over today's trip and going, but he's winless in his last four and was sixth on two of those, while 160 lb is a hefty burden off 92.
- Euro Maker (hrs_51766225) | 5yo G | 165lb | OR 97 | draw 0 | jockey Eoghan Finegan(5) | trainer Adrian Murray (14d 0/3) | headgear - | last run 48 days | form 2-9130 | MARKET 11.9% | 09:00 median 6.50 | Matchbook 7.40
    comment: Euro Maker looks a strong threat, having won three starts back and finished third two starts back, with experience of today's trip and going, and he's rated 100 by us. The main risk is a layoff of 48 days, plus an unplaced run last time out and a hefty 165 lb.
- Topothelane (hrs_28706895) | 9yo G | 156lb | OR 88 | draw 0 | jockey Mike O'Connor | trainer P C O'Connor (14d 0/0) | headgear - | last run 166 days | form /P3-15 | MARKET 11.6% | 09:00 median 7.00 | Matchbook 7.60
    comment: Topothelane won two starts back and was third three starts back, and he has run over today's trip and going before, but a fifth last time out and 166 days off the track temper the case.
- Bowgate Street (hrs_34153483) | 7yo M | 160lb | OR 92 | draw 0 | jockey Darragh O'Keeffe | trainer M Flannery (14d 0/0) | headgear t | last run 20 days | form 733032 | MARKET 11.6% | 09:00 median 6.50 | Matchbook 7.80
    comment: Bowgate Street arrives in cracking nick, second last time out and third in two of the three starts before that, with 20 days since her last run and experience of today's trip and going. Still yet to win in her last six, and 160 lb is the main risk.
- Mad Maxios (hrs_49359758) | 5yo G | 166lb | OR 98 | draw 0 | jockey Sean Flanagan | trainer E McNamara (14d 0/6) | headgear t | last run 26 days | form /52F-5 | MARKET 11.4% | 09:00 median 7.00 | Matchbook 7.60
    comment: Mad Maxios arrives fresh after 26 days and has run over today's trip and going, with a second three starts back showing his ability, while carrying 166 lb.
- Centaq (hrs_51373665) | 6yo G | 151lb | OR 83 | draw 0 | jockey Alix Balfe(7) | trainer Dermot A McLoughlin (14d 0/11) | headgear tp | last run 34 days | form 64682P | MARKET 6.6% | 09:00 median 11.00 | Matchbook 14.00
    comment: Centaq was pulled up last time out but filled the runner-up spot two starts back, and he has run over today's trip and going before.
- Speakasyoufind (hrs_52709041) | 5yo G | 155lb | OR 87 | draw 0 | jockey Conor Clarke(7) | trainer P. J. Rothwell (14d 0/16) | headgear - | last run 34 days | form 926F94 | MARKET 5.0% | 09:00 median 15.00 | Matchbook 18.50
    comment: Fourth last time out and a second five starts back suggest Speakasyoufind retains some ability, and he has run over today's trip and going, but he is yet to win in his last six and fell three starts back.
- Thegooseiscooked (hrs_26460056) | 9yo M | 148lb | OR 80 | draw 0 | jockey Daniel King | trainer Gerard Keane (14d 0/6) | headgear - | last run 22 days | form 900/F- | MARKET 4.4% | 09:00 median 12.00 | Matchbook 32.00
    comment: Fell last time out and unplaced in the two runs before that, so Thegooseiscooked arrives winless in her last four, though 22 days since that spill is fine and she has run over today's trip and going.
- Getaway Henry (hrs_30567943) | 9yo G | 153lb | OR 85 | draw 0 | jockey Danny Gilligan | trainer Daniel Joseph O'Leary (14d 0/2) | headgear b | last run 113 days | form 8-P108 | MARKET 4.0% | 09:00 median 19.00 | Matchbook 23.00
    comment: Getaway Henry won three starts back but has since finished unplaced and then an eighth last time out, and he returns after 113 days off; he has run over today's trip and going, though 153 lb is a hefty burden.
- Chesterbaylad (hrs_44690233) | 5yo G | 144lb | OR 76 | draw 0 | jockey Josh Williamson(3) | trainer Ms Helen P Markham (14d 0/4) | headgear - | last run 11 days | form 418070 | MARKET 3.7% | 09:00 median 17.00 | Matchbook 29.00
    comment: Chesterbaylad has been out of sorts, unplaced last time out and a seventh two starts back, with his only win five starts ago, so he is hard to fancy. He has run over today's trip and going and is fresh enough after 11 days, but 144 lb is a big burden.
- Romella (hrs_16652251) | 12yo M | 148lb | OR 80 | draw 0 | jockey Phillip Enright | trainer Brendan Maurice Walsh (14d 0/3) | headgear tp | last run 7 days | form 70-006 | MARKET 3.2% | 09:00 median 17.00 | Matchbook 46.00
    comment: Romella is hard to fancy, winless in her last five and only sixth last time out, with unplaced efforts before that and a seventh five starts back.
- Walk On Annilog (hrs_48259442) | 7yo M | 162lb | OR 94 | draw 0 | jockey Philip Byrnes | trainer Riceal Dunne (14d 0/0) | headgear h | last run 129 days | form 70-480 | MARKET 3.1% | 09:00 median 17.00 | Matchbook 50.00
    comment: The risk is a 129-day absence after an unplaced run last time, with 162 lb to carry.
- La Tulipe Noire (hrs_31480344) | 6yo M | 151lb | OR 83 | draw 0 | jockey Cian Quirke | trainer Aengus King (14d 0/3) | headgear p | last run 14 days | form 9/P8-F | MARKET 3.1% | 09:00 median 23.00 | Matchbook 32.00
    comment: La Tulipe Noire is hard to fancy, having fallen last time out, with an eighth two starts back and a ninth four starts back, and she is winless in her last four.
- Je Suis Celebre (hrs_60279975) | 4yo G | 166lb | OR 98 | draw 0 | jockey G B Noonan | trainer Eoin Christopher McCarthy (14d 0/15) | headgear - | last run 12 days | form F575 | MARKET 1.8% | 09:00 median 29.00 | Matchbook 85.00
    comment: Without a win in his last four, Je Suis Celebre has finished fifth, seventh and fifth before a fall four starts back, so he is hard to fancy, especially carrying 166 lb off a mark of 98. On the plus side, he is fresh from a run 12 days ago and has experience of today's trip and going.
- Shakita (hrs_46077948) | 4yo F | 152lb | OR 84 | draw 0 | jockey Donagh Meyler | trainer Thomas Mullins (14d 0/3) | headgear - | last run 96 days | form 800-C9 | MARKET 1.2% | 09:00 median 41.00 | Matchbook 130.00
    comment: Shakita is yet to win and was only ninth last time out, after being carried out two starts back, so this lightly raced filly looks unexposed and open to improvement after 96 days off, carrying 152 lb.
- Slea Head (hrs_51557604) | 8yo G | 140lb | OR 72 | draw 0 | jockey Patrick M O'Brien(5) | trainer Peter Maher (14d 0/1) | headgear - | last run 345 days | form 5800P- | MARKET 0.7% | 09:00 median 81.00 | Matchbook 240.00
    comment: Slea Head is hard to fancy: pulled up last time out, winless in his last five starts and returning after 345 days off, with an eighth and a fifth the best of his recent form.
- Middlethird Marvel (hrs_51766316) | 5yo M | 142lb | OR 74 | draw 0 | jockey Philip Donovan | trainer Darren Collins (14d 1/3) | headgear - | last run 26 days | form 0-P00P | MARKET 0.6% | 09:00 median 101.00 | Matchbook 240.00
    comment: Middlethird Marvel has been pulled up last time out and is winless in her last five, though she has run over today's trip and going and is fresh enough after 26 days.
