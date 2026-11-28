# Card review packet: Newbury, 2026-11-28

You are a racing form reviewer. Use ONLY this packet. For every race:

1. Start from each runner's MARKET chance (the sharp-weighted 09:00 price, in %).
2. Change a runner's chance ONLY where the card below gives a specific reason: recent form figures, a comment
   or spotlight line, official rating (OR) vs today's weight, days since last run, trainer's 14-day record,
   headgear or wind surgery first time, draw, trip/going/course clues in the comment, and the DATA lines
   (rebuilt form model, last three runs with figures, run style and race pace, finishing speed). Give a one-line reason
   that names the card fact. No reason on the card = no change. Do not use outside knowledge of the horses.
3. Keep changes moderate: normally within 0.67x to 1.5x of the market chance; never beyond 0.33x to 3x.
   Totals do not need to add to 100; they are rescaled afterwards.
   DATA lines come from our own models, not the card: "model" is a form-only win chance (it ignores the market, so
   treat it as one opinion, not the answer); "fig" is a performance figure (higher = better) for that past run - Flat and jumps (Hurdle/Chase/NH Flat)
   figures are on different scales, so only compare figures from the same code as today's race;
   "for"/"against" are derived facts (figures vs field, vs mark, pace fit, jumping errors, finishing speed).
4. Runners marked CHECK are the market favourite. Give a verdict, BET or SKIP, with a one-line reason:
   BET unless the card or the DATA lines give a specific reason to doubt the favourite (then lower its chance and SKIP).
   You do not need to do any price arithmetic; the price check (skip line shown) is applied afterwards.

Write valid JSON to the out path you were given, exactly this shape (use the exact race_id and horse_id values):
{"meeting": "newbury", "races": [
  {"race_id": "rac_...", "changes": [{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}],
    "checks": [{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}]}
]}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.


## 12:00 Newbury | race_id rac_32305870402 | Coral "Daily Rewards Shaker" Novices' Hurdle Race (GBB Race)
Hurdle | Class 3 | 2m4f118y | going Good To Soft | Turf | 13 runners | rating band - | age 4yo+
DATA pace: Even - Two likely leaders (Livio, Aqua Bleu). A fair, even gallop is most likely.
- Aqua Bleu (hrs_58316230) | 4yo G | 153lb | OR 123 | draw 0 | jockey Sean Bowen | trainer Warren Greatrex (14d 4/22) | headgear - | last run 22 days | form 111P-2 | MARKET 23.0% | 09:00 median 3.75 | Matchbook 4.00 | CHECK (skip line 3.56)
    DATA: model 7.7% | style Leader (led 38% of runs) | runs in data 3 | last 3: 13 Feb Chepstow Hurdle 16.1f Soft 1/5; 9 Apr Aintree Hurdle 16.9f Good To Soft PU/10; 6 Nov Aintree Hurdle 17f Good To Soft 2/4 fig 113
    DATA for: Best recent form figure 113, 10 lb above field average; Last-run finishing speed +4.9% vs that field (finished strongly)
    DATA against: Pulled up in 1 of its last 3 jumps runs
- Trial By Jury (hrs_57877967) | 6yo G | 154lb | OR - | draw 0 | jockey Callum Pritchard | trainer Ben Pauling (14d 8/39) | headgear - | last run 346 days | form 12- | MARKET 19.9% | 09:00 median 4.33 | Matchbook 4.60
    DATA: model 4.7% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 21% wins (8/39), last 14 days
    DATA against: Returns from a 346-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Well Achieved (hrs_17396183133) | 4yo G | 153lb | OR - | draw 0 | jockey Ben Jones | trainer Ben Pauling (14d 8/39) | headgear - | last run 286 days | form 1- | MARKET 16.9% | 09:00 median 5.00 | Matchbook 5.60
    DATA: model 4.6% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Trainer 21% wins (8/39), last 14 days
    DATA against: Returns from a 286-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Sappingirl (hrs_58099412) | 5yo G | 154lb | OR - | draw 0 | jockey Sam Twiston-Davies | trainer Paul Nicholls (14d 5/28) | headgear - | last run 23 days | form 26-2 | MARKET 15.4% | 09:00 median 5.50 | Matchbook 6.00
    DATA: model 7.6% | style Held up (led 8% of runs) | runs in data 1 | last 3: 5 Nov Newbury Hurdle 19f Good To Soft 2/10 fig 114
    DATA for: Best recent form figure 114, 11 lb above field average
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Terrano (hrs_51557933) | 5yo G | 160lb | OR - | draw 0 | jockey Paul O'Brien | trainer Harry Derham (14d 1/16) | headgear - | last run 210 days | form 3/1 | MARKET 8.0% | 09:00 median 10.00 | Matchbook 12.00
    DATA: model 17.0% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 2 May Hexham Hurdle 16.2f Good 1/8
    DATA for: Last-run finishing speed +4.8% vs that field (finished strongly)
    DATA against: Returns from a 210-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Livio (hrs_58931026) | 5yo G | 154lb | OR 128 | draw 0 | jockey Richie McLernon | trainer Faye Bramley (14d 1/13) | headgear - | last run 63 days | form 1/3017 | MARKET 4.5% | 09:00 median 17.00 | Matchbook 23.00
    DATA: model 28.5% | style Prominent (led 43% of runs) | runs in data 4 | last 3: 6 Jun Punchestown Hurdle 16.5f Good To Yielding 11/24; 3 Aug Cork Hurdle 18f Good 1/18; 26 Sep Listowel Hurdle 20f Good 7/14
- Wonder Flying (hrs_52021431) | 5yo G | 154lb | OR - | draw 0 | jockey Jack Andrews | trainer Tom Ellis (14d 0/11) | headgear - | last run 27 days | form 5837-3 | MARKET 2.8% | 09:00 median 29.00 | Matchbook 38.00
    DATA: model 3.7% | style Held up (led 5% of runs) | runs in data 2 | last 3: 7 Feb Newbury NH Flat 16.3f Heavy 7/10; 1 Nov Carlisle Hurdle 20f Good To Soft 3/8 fig 104
    DATA against: Trainer 0 wins from 11 runs, last 14 days; Lightly raced: 2 runs in our data, so the model has little to go on
- Ballypollard (hrs_52418002) | 6yo G | 154lb | OR - | draw 0 | jockey Jonathan Burke | trainer Mel Rowley (14d 2/11) | headgear - | last run 210 days | form 16- | MARKET 2.6% | 09:00 median 29.00 | Matchbook 42.00
    DATA: model 6.6% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 2 May Punchestown NH Flat 16f Yielding 6/16
    DATA for: Last-run finishing speed +5.7% vs that field (finished strongly)
    DATA against: Returns from a 210-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Asamahleroffact (hrs_17395673106) | 4yo G | 153lb | OR - | draw 0 | jockey Ciaran Gethings | trainer Alastair Ralph (14d 0/5) | headgear - | last run 203 days | form F | MARKET 1.8% | 09:00 median 34.00 | Matchbook 90.00
    DATA: model 4.6% | style Unknown | runs in data 0 | last 3: none in our data
    DATA against: Returns from a 203-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Mister Coko (hrs_56559496) | 4yo G | 153lb | OR - | draw 0 | jockey Tom Bellamy | trainer Nigel & Willy Twiston-Davies (14d 3/18) | headgear - | last run 36 days | form 58-35 | MARKET 1.7% | 09:00 median 29.00 | Matchbook 140.00
    DATA: model 2.0% | style Held up (led 5% of runs) | runs in data 3 | last 3: 8 Mar Warwick NH Flat 16f Good To Soft 8/10; 7 Oct Worcester Hurdle 16f Good 3/12; 23 Oct Cheltenham Hurdle 20f Good To Soft 5/7 fig 99
    DATA against: Best recent form figure 99, 4 lb below field average
- Spare The Voice (hrs_17395017059) | 5yo G | 154lb | OR - | draw 0 | jockey Tom Cannon | trainer Nick Scholfield (14d 1/13) | headgear - | last run 23 days | form 1-5 | MARKET 1.4% | 09:00 median 51.00 | Matchbook 85.00
    DATA: model 4.4% | style Midfield (led 8% of runs) | runs in data 1 | last 3: 5 Nov Newbury Hurdle 19f Good To Soft 5/10 fig 101
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Indulto Rouge (hrs_52495324) | 5yo G | 154lb | OR - | draw 0 | jockey Jack Tudor | trainer David Pipe (14d 3/17) | headgear t | wind surgery | last run 249 days | form 1/305- | MARKET 1.3% | 09:00 median 41.00 | Matchbook 130.00
    DATA: model 6.9% | style Unknown | runs in data 1 | last 3: 24 Mar Southwell NH Flat 15.8f Good 5/7
    DATA against: Last-run finishing speed -5.4% vs that field (faded); Returns from a 249-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Company Charge (hrs_66655491) | 5yo G | 154lb | OR - | draw 0 | jockey James Turner(5) | trainer Nigel & Willy Twiston-Davies (14d 3/18) | headgear - | last run 23 days | form 5U387 | MARKET 0.5% | 09:00 median 151.00 | Matchbook 400.00
    DATA: model 1.8% | style Held up (led 5% of runs) | runs in data 5 | last 3: 20 Sep Plumpton NH Flat 17.8f Good 3/6; 10 Oct Chepstow Hurdle 19.5f Good To Soft 8/13; 5 Nov Newbury Hurdle 19f Good To Soft 7/10 fig 88
    DATA against: Best recent form figure 88, 15 lb below field average

## 12:35 Newbury | race_id rac_32305872339 | Play Coral "Racing-Super-Series" Mares' Novices' Hurdle Race (Listed Race) (GBB Race)
Hurdle | Class 1 | 2m0f69y | going Good To Soft | Turf | 11 runners | rating band - | age 4yo+
DATA pace: Even - Two likely leaders (L'Amandine, Miss Kingston). A fair, even gallop is most likely.
- Fairy Park (hrs_51557989) | 5yo M | 154lb | OR - | draw 0 | jockey Jack Tudor | trainer Joe Tizzard (14d 8/31) | headgear - | last run 37 days | form 1/23-1 | MARKET 31.4% | 09:00 median 2.75 | Matchbook 2.94
    DATA: model 8.9% | style Prominent (led 38% of runs) | runs in data 3 | last 3: 28 Feb Newbury NH Flat 16.3f Good To Soft 2/8; 9 Apr Aintree NH Flat 16.9f Good To Soft 3/20; 22 Oct Ffos Las Hurdle 20f Soft 1/8 fig 116
    DATA for: Trainer 26% wins (8/31), last 14 days; Has won at this trip or further; Good recent finishing positions
- Royal Response (hrs_61911360) | 4yo F | 154lb | OR - | draw 0 | jockey Nico de Boinville | trainer Nicky Henderson (14d 2/24) | headgear - | last run 23 days | form 21-1 | MARKET 26.2% | 09:00 median 3.25 | Matchbook 3.55
    DATA: model 7.8% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 5 Nov Newbury Hurdle 16.5f Good To Soft 1/10 fig 115
    DATA for: Has won at this trip or further
    DATA against: Lightly raced: 1 run in our data, so the model has little to go on
- Salsinha (hrs_54644611) | 5yo M | 154lb | OR 127 | draw 0 | jockey Jordan Gainford | trainer Henry de Bromhead (14d 6/36) | headgear t | last run 29 days | form 34-213 | MARKET 15.8% | 09:00 median 5.00 | Matchbook 6.20
    DATA: model 12.8% | style Midfield (led 5% of runs) | runs in data 5 | last 3: 1 Jun Listowel Hurdle 16f Yielding 1/13; 18 Jun Leopardstown Flat 15f Good To Firm 4/15; 30 Oct Down Royal (IRE) Hurdle 17f Good To Yielding 3/7 fig 124
    DATA for: Best recent form figure 124, 9 lb above field average; Official rating 127, 12 lb above field average; Last-run finishing speed +2.6% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
- Ti'mamzel (hrs_51897566) | 5yo M | 154lb | OR - | draw 0 | jockey Caoilin Quinn | trainer Jamie Moore & Josh Moore (14d 3/33) | headgear - | last run 233 days | form 1218- | MARKET 7.8% | 09:00 median 10.00 | Matchbook 13.00
    DATA: model 5.4% | style Unknown | runs in data 3 | last 3: 18 Jan Windsor NH Flat 16f Soft 2/6; 7 Mar Sandown NH Flat 16f Soft 1/10; 9 Apr Aintree NH Flat 16.9f Good To Soft 8/20
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Returns from a 233-day break; First run over hurdles in our data
- Katios Queen (hrs_58196509) | 5yo M | 154lb | OR - | draw 0 | jockey Tristan Durrell | trainer Dan Skelton (14d 27/97) | headgear - | last run 44 days | form 133-1 | MARKET 4.3% | 09:00 median 17.00 | Matchbook 26.00
    DATA: model 6.5% | style Midfield (led 8% of runs) | runs in data 2 | last 3: 16 Jan Market Rasen NH Flat 16.6f Good To Soft 3/9; 15 Oct Fontwell Hurdle 17.5f Good To Soft 1/6 fig 110
    DATA for: Trainer 28% wins (27/97), last 14 days; Last-run finishing speed +4.5% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Best recent form figure 110, 5 lb below field average; Lightly raced: 2 runs in our data, so the model has little to go on
- L'Amandine (hrs_60343276) | 4yo F | 154lb | OR - | draw 0 | jockey Gavin Sheehan | trainer Jamie Snowden (14d 4/15) | headgear - | last run 46 days | form 31-1 | MARKET 4.3% | 09:00 median 17.00 | Matchbook 25.00
    DATA: model 8.0% | style Leader (led 38% of runs) | runs in data 3 | last 3: 15 Jan Ludlow NH Flat 15.8f Good To Soft 3/11; 6 Apr Fakenham NH Flat 16f Good 1/5; 13 Oct Southwell Hurdle 15.8f Good 1/4
    DATA for: Trainer 27% wins (4/15), last 14 days; Last-run finishing speed +3.5% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
- Boombox (hrs_50433243) | 5yo M | 154lb | OR 108 | draw 0 | jockey Paul O'Brien | trainer Harry Derham (14d 1/16) | headgear - | last run 14 days | form 23-221 | MARKET 3.1% | 09:00 median 26.00 | Matchbook 34.00
    DATA: model 17.9% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 11 May Killarney NH Flat 17f Good To Yielding 2/11; 21 Oct Worcester Hurdle 16f Good To Soft 2/9 fig 119; 14 Nov Uttoxeter Hurdle 20f Good 1/7 fig 109
    DATA for: Best recent form figure 119, 4 lb above field average; Has won at this trip or further; Good recent finishing positions
    DATA against: Official rating 108, 8 lb below field average
- Miss Kingston (hrs_51766330) | 5yo M | 154lb | OR 114 | draw 0 | jockey Ciaran Gethings | trainer Alastair Ralph (14d 0/5) | headgear - | last run 33 days | form 41-261 | MARKET 2.2% | 09:00 median 34.00 | Matchbook 50.00
    DATA: model 15.7% | style Leader (led 63% of runs) | runs in data 5 | last 3: 6 Jun Worcester Hurdle 16f Good 2/8; 25 Sep Worcester Hurdle 20f Good 6/15; 26 Oct Hereford Hurdle 16f Good To Firm 1/12 fig 111
    DATA for: Last-run finishing speed +4.8% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
- Ladies Day (hrs_51618952) | 5yo M | 154lb | OR 113 | draw 0 | jockey Jack Andrews | trainer Tom Ellis (14d 0/11) | headgear - | wind surgery | last run 80 days | form -21142 | MARKET 2.0% | 09:00 median 41.00 | Matchbook 50.00
    DATA: model 11.0% | style Midfield (led 3% of runs) | runs in data 6 | last 3: 13 Jun Uttoxeter Hurdle 15.8f Good 1/6; 18 Jul Cartmel Hurdle 17.2f Good 4/11; 9 Sep Sedgefield Hurdle 19.9f Good 2/5
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Trainer 0 wins from 11 runs, last 14 days
- Marvelous Dragones (hrs_60250050) | 4yo F | 154lb | OR - | draw 0 | jockey Sean Bowen | trainer Jamie Snowden (14d 4/15) | headgear t | wind surgery | last run 18 days | form 0230-1 | MARKET 1.8% | 09:00 median 41.00 | Matchbook 65.00
    DATA: model 2.3% | style Midfield (led 8% of runs) | runs in data 2 | last 3: 1 Jan Cheltenham NH Flat 16.8f Good 16/16; 10 Nov Huntingdon Hurdle 16f Good 1/7 fig 108
    DATA for: Trainer 27% wins (4/15), last 14 days; Has won at this trip or further
    DATA against: Best recent form figure 108, 7 lb below field average; Lightly raced: 2 runs in our data, so the model has little to go on
- Mythical Bird (hrs_43730582) | 4yo F | 154lb | OR - | draw 0 | jockey Tom Cannon | trainer Hughie Morrison (14d 0/6) | headgear - | last run 32 days | form /- | MARKET 0.9% | 09:00 median 81.00 | Matchbook 160.00
    DATA: model 3.6% | style Held up (led 8% of runs) | runs in data 10 | last 3: 18 Sep Newbury Flat 10f Good 5/8; 25 Sep Newmarket Flat 9f Good 4/10; 27 Oct Wolverhampton (AW) Flat 9.5f Standard 5/8 fig 73
    DATA against: First run over hurdles in our data

## 1:10 Newbury | race_id rac_32305874276 | Coral Sir Peter O'Sullevan Memorial Handicap Steeple Chase (GBB Race)
Chase | Class 2 | 2m6f93y | going Good | Turf | 18 runners | rating band 0-145 | age 4yo+
DATA pace: Strong pace - 4 habitual front-runners (Go West, Sheldon, Leader In The Park, Chuggy). A contested lead should set things up for horses coming from behind.
- Knight of Allen (hrs_38018330) | 6yo G | 155lb | OR 127 | draw 0 | jockey Ciaran Gethings | trainer Mrs Jane Williams (14d 3/7) | headgear - | last run 21 days | form 42P3-2 | MARKET 16.2% | 09:00 median 4.50 | Matchbook 5.80 | CHECK (skip line 4.27)
    comment: Knight of Allen was second last time out and third the run before, though he is winless in his last five and was pulled up three starts back. Fresh enough after 21 days, he has run over today's trip, but 155 lb is a hefty burden off 127.
    DATA: model 7.4% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 10 Mar Cheltenham Chase 25f Good To Soft PU/22; 2 Apr Chepstow Chase 19.4f Good To Soft 3/6; 7 Nov Aintree Chase 20f Good To Soft 2/11 fig 129
    DATA for: Best recent form figure 129, 4 lb above field average; Trainer 43% wins (3/7), last 14 days
    DATA against: Race comments mention jumping mistakes in 2 of its last 5 runs; Pulled up in 1 of its last 5 jumps runs
- Norn Iron (hrs_32936519) | 8yo G | 165lb | OR 137 | draw 0 | jockey Paul O'Brien | trainer Harry Derham (14d 1/16) | headgear t | last run 211 days | form 23112- | MARKET 12.2% | 09:00 median 6.00 | Matchbook 7.60
    comment: Norn Iron has outstanding recent form, a second last time out after back-to-back wins, but he returns after 211 days off and carries 165 lb.
    DATA: model 10.2% | style Midfield (led 4% of runs) | runs in data 4 | last 3: 31 Jan Sandown Chase 20.1f Soft 1/5; 7 Mar Sandown Chase 20.1f Soft 1/3; 1 May Punchestown Chase 20.2f Yielding 2/22
    DATA for: Official rating 137, 9 lb above field average; Last-run finishing speed +4.3% vs that field (finished strongly); Good recent finishing positions
    DATA against: Carries 9 lb more than average; Returns from a 211-day break; Race comments mention jumping mistakes in 2 of its last 4 runs
- Leader In The Park (hrs_32682482) | 8yo G | 155lb | OR 127 | draw 0 | jockey Ben Jones | trainer Ben Pauling (14d 8/39) | headgear - | last run 30 days | form /22P-4 | MARKET 9.3% | 09:00 median 8.00 | Matchbook 10.00
    comment: Fourth last time out after being pulled up two starts back, he showed more spark, having been second three and four starts back, yet he remains without a win in his last four.
    DATA: model 4.5% | style Prominent (led 54% of runs) | runs in data 3 | last 3: 10 Jan Kempton Chase 20.5f Good 2/5; 21 Feb Kempton Chase 24f Good To Soft PU/13; 29 Oct Ffos Las Chase 19.5f Good 4/6 fig 124
    DATA for: Trainer 21% wins (8/39), last 14 days
    DATA against: Pulled up in 1 of its last 3 jumps runs
- El Capitaine (hrs_28916517) | 8yo G | 160lb | OR 132 | draw 0 | jockey Sean Flanagan | trainer Kayley Woollacott (14d 1/4) | headgear - | last run 42 days | form 4371-1 | MARKET 9.2% | 09:00 median 8.25 | Matchbook 10.00
    DATA: model 7.1% | style Held up (led 5% of runs) | runs in data 3 | last 3: 27 Jan Chepstow Hurdle 19.5f Soft 7/10; 20 Mar Newbury Chase 22.4f Good To Soft 1/5; 17 Oct Newton Abbot Chase 21f Good 1/4 fig 132
    DATA for: Best recent form figure 132, 7 lb above field average; Last-run finishing speed +2.5% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions; Pace: a contested lead should suit its hold-up style
- Kdeux Saint Fray (hrs_41072773) | 6yo G | 156lb | OR 128 | draw 0 | jockey Sam Twiston-Davies | trainer Anthony Honeyball (14d 1/14) | headgear t | last run 23 days | form 4307-2 | MARKET 8.6% | 09:00 median 8.50 | Matchbook 11.00
    DATA: model 5.8% | style Prominent (led 23% of runs) | runs in data 5 | last 3: 12 Mar Cheltenham Chase 20.6f Good 12/18; 18 Apr Ayr Chase 24.1f Heavy 7/11; 5 Nov Plumpton Chase 20f Good 2/3 fig 123
    DATA against: Race comments mention jumping mistakes in 4 of its last 5 runs
- Barlovento (hrs_38288257) | 7yo G | 157lb | OR 129 | draw 0 | jockey Sean Bowen | trainer Olly Murphy (14d 9/41) | headgear - | last run 220 days | form 21831- | MARKET 8.2% | 09:00 median 8.50 | Matchbook 12.50
    comment: Barlovento won last time out and four starts back, with a third two starts back, but he returns after 220 days off and carries 157 lb off a mark of 129.
    DATA: model 7.9% | style Midfield (led 5% of runs) | runs in data 3 | last 3: 24 Jan Cheltenham Chase 20.6f Soft 8/9; 14 Mar Kempton Chase 20.5f Good 3/7; 22 Apr Perth Chase 20.1f Good 1/7
    DATA for: Trainer 22% wins (9/41), last 14 days; Last-run finishing speed +3.2% vs that field (finished strongly); Good recent finishing positions
    DATA against: Returns from a 220-day break
- Jipcot (hrs_32233327) | 7yo G | 159lb | OR 131 | draw 0 | jockey Richie McLernon | trainer Jonjo & A.J. O'Neill (14d 4/33) | headgear t | last run 30 days | form 1404-U | MARKET 6.8% | 09:00 median 10.00 | Matchbook 15.00
    comment: Jipcot unseated last time out, but he was a fourth two starts back and a fourth four starts back, with a win five starts back, and has run over today's trip.
    DATA: model 5.7% | style Prominent (led 38% of runs) | runs in data 6 | last 3: 10 Mar Cheltenham Chase 20.2f Good To Soft 13/23; 17 Apr Ayr Chase 20.5f Soft 4/9; 29 Oct Stratford Chase 19.5f Good To Soft UR/10
    DATA for: Has won at this trip or further
    DATA against: Fell or unseated in 1 of its last 5 jumps runs
- King's Threshold (hrs_28294658) | 9yo G | 161lb | OR 133 | draw 0 | jockey Gavin Sheehan | trainer Emma Lavelle (14d 2/19) | headgear t | last run 21 days | form 410-42 | MARKET 4.0% | 09:00 median 19.00 | Matchbook 23.00
    comment: King's Threshold arrives in good heart after a second last time out, just 21 days ago, and has a win four starts back to his name, while he has run over today's trip before.
    DATA: model 4.9% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 12 Mar Cheltenham Chase 26.3f Good 16/23; 2 May Uttoxeter Chase 24f Good 4/6; 7 Nov Uttoxeter Chase 24f Good 2/5 fig 126
    DATA against: Recent figures 7 lb below its current mark (looks high in the weights); Race comments mention jumping mistakes in 2 of its last 3 runs
- Demnat (hrs_23240714) | 9yo G | 151lb | OR 123 | draw 0 | jockey Tom Bellamy | trainer Venetia Williams (14d 0/11) | headgear - | last run 625 days | form 9P329/ | MARKET 3.6% | 09:00 median 21.00 | Matchbook 26.00
    comment: Demnat was ninth last time out after a second two starts back and a third three starts back, but he returns from a 625-day absence and is yet to win in his last five.
    DATA: model 4.0% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Carries 5 lb less than average
    DATA against: Official rating 123, 5 lb below field average; Trainer 0 wins from 11 runs, last 14 days; Returns from a 625-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Holetown (hrs_34975990) | 6yo M | 142lb | OR 114 | draw 0 | jockey Patrick Wadge | trainer Venetia Williams (14d 0/11) | headgear - | last run 253 days | form /4613- | MARKET 3.6% | 09:00 median 21.00 | Matchbook 27.00
    comment: Holetown was third last time out and a winner two starts back, but she returns after 253 days off and carries 142 lb, so she is hard to fancy.
    DATA: model 4.1% | style Prominent (led 4% of runs) | runs in data 3 | last 3: 11 Jan Fontwell Hurdle 17.7f Soft 6/9; 18 Feb Ludlow Chase 20.1f Soft 1/8; 20 Mar Newbury Chase 22.4f Good To Soft 3/11
    DATA for: Good recent finishing positions; Carries 14 lb less than average
    DATA against: Official rating 114, 14 lb below field average; Trainer 0 wins from 11 runs, last 14 days; Returns from a 253-day break
- Go West (hrs_29327242) | 8yo G | 165lb | OR 137 | draw 0 | jockey Freddie Gingell | trainer Paul Nicholls (14d 5/28) | headgear - | last run 30 days | form 3144-2 | MARKET 3.3% | 09:00 median 21.00 | Matchbook 32.00
    comment: The main risk is the 165 lb he must carry off an official mark of 137.
    DATA: model 5.4% | style Leader (led 43% of runs) | runs in data 5 | last 3: 21 Feb Kempton Chase 20.5f Good To Soft 4/4; 25 Apr Sandown Chase 20.1f Good 4/4; 29 Oct Stratford Chase 19.5f Good To Soft 2/10 fig 137
    DATA for: Best recent form figure 137, 12 lb above field average; Official rating 137, 9 lb above field average; Last-run finishing speed +3.2% vs that field (finished strongly)
    DATA against: Carries 9 lb more than average; Pace: likely to be taken on for the lead
- Chuggy (hrs_40473482) | 6yo G | 151lb | OR 123 | draw 0 | jockey Tristan Durrell | trainer Dan Skelton (14d 27/97) | headgear - | last run 17 days | form 1125-4 | MARKET 3.1% | 09:00 median 23.00 | Matchbook 32.00
    comment: Chuggy's last two runs, a fourth last time out and a fifth two starts back, show a slide from back-to-back wins four and five starts back, and carrying 151 lb off 123 makes him hard to fancy.
    DATA: model 3.8% | style Leader (led 38% of runs) | runs in data 2 | last 3: 14 Mar Kempton Chase 18f Good 5/6; 11 Nov Bangor-on-Dee Chase 20.5f Good 4/5 fig 118
    DATA for: Trainer 28% wins (27/97), last 14 days; Last-run finishing speed +2.6% vs that field (finished strongly); Carries 5 lb less than average
    DATA against: Best recent form figure 118, 7 lb below field average; Official rating 123, 5 lb below field average; Lightly raced: 2 runs in our data, so the model has little to go on; Pace: likely to be taken on for the lead
- Sheldon (hrs_20789272) | 10yo G | 158lb | OR 130 | draw 0 | jockey Benjamin Macey(5) | trainer Seamus Mullins (14d 1/5) | headgear - | last run 19 days | form 2321-1 | MARKET 3.0% | 09:00 median 26.00 | Matchbook 32.00
    comment: Fit enough after 19 days, he looks hard to fancy at this level.
    DATA: model 9.8% | style Leader (led 54% of runs) | runs in data 5 | last 3: 20 Mar Newbury Chase 22.4f Good To Soft 2/11; 14 Apr Newton Abbot Chase 21f Good 1/4; 9 Nov Stratford Chase 22.5f Good To Soft 1/8 fig 128
    DATA for: Trainer 20% wins (1/5), last 14 days; Has won at this trip or further; Good recent finishing positions
    DATA against: Race comments mention jumping mistakes in 2 of its last 5 runs; Pace: likely to be taken on for the lead
- Moon D'Orange (hrs_32568753) | 8yo G | 151lb | OR 123 | draw 0 | jockey Ellis Collier(5) | trainer Christian Williams (14d 0/14) | headgear - | last run 35 days | form 37-074 | MARKET 2.4% | 09:00 median 29.00 | Matchbook 42.00
    comment: Fourth last time out and a third five starts back give Moon D'Orange some credentials, but he's yet to win in his last five and was seventh twice in between.
    DATA: model 3.2% | style Midfield (led 3% of runs) | runs in data 9 | last 3: 9 May Haydock Hurdle 24.3f Good To Soft 15/15; 25 Sep Worcester Hurdle 23f Good 7/9; 24 Oct Cheltenham Chase 25f Good To Soft 4/9 fig 118
    DATA for: Carries 5 lb less than average
    DATA against: Best recent form figure 118, 7 lb below field average; Official rating 123, 5 lb below field average; Trainer 0 wins from 14 runs, last 14 days
- Eyed (hrs_27861722) | 9yo G | 148lb | OR 120 | draw 0 | jockey Jonathan Burke | trainer Hughie Morrison (14d 0/6) | headgear t | last run 225 days | form 275P7- | MARKET 1.9% | 09:00 median 34.00 | Matchbook 60.00
    comment: Eyed is hard to fancy, having been beaten in a seventh last time out after being pulled up two starts back, and he returns from a 225-day absence while winless in his last five. He has run over today's trip and a second five starts back shows some ability, but 148 lb is a big burden.
    DATA: model 2.9% | style Midfield (led 5% of runs) | runs in data 3 | last 3: 17 Jan Ascot Chase 23.8f Soft 5/11; 10 Mar Cheltenham Chase 25f Good To Soft PU/22; 17 Apr Ayr Hurdle 24.3f Soft 7/15
    DATA for: Carries 8 lb less than average
    DATA against: Official rating 120, 8 lb below field average; Last-run finishing speed -5.9% vs that field (faded); Returns from a 225-day break; Pulled up in 1 of its last 3 jumps runs
- Down Memory Lane (hrs_32568711) | 8yo G | 168lb | OR 140 | draw 0 | jockey Harry Kimber | trainer Faye Bramley (14d 1/13) | headgear - | last run 21 days | form P5P-89 | MARKET 1.9% | 09:00 median 29.00 | Matchbook 80.00
    DATA: model 2.5% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 29 Apr Punchestown Chase 20.4f Yielding PU/14; 14 Oct Ffos Las Chase 19.5f Soft 8/8; 7 Nov Aintree Chase 20f Good To Soft 9/11
    DATA for: Official rating 140, 12 lb above field average
    DATA against: Poor recent finishing positions; Carries 12 lb more than average; Pulled up in 2 of its last 5 jumps runs
- Royal Jewel (hrs_34962137) | 7yo G | 160lb | OR 132 | draw 0 | jockey Callum Pritchard | trainer Philip Hobbs & Johnson White (14d 3/17) | headgear t (1st time) | last run 238 days | form 63132- | MARKET 1.8% | 09:00 median 41.00 | Matchbook 60.00
    comment: Royal Jewel arrives in cracking form, a second last time out, a third two starts back, and a winner three starts back, and he has run over today's trip.
    DATA: model 6.8% | style Held up (led 8% of runs) | runs in data 3 | last 3: 3 Feb Taunton Chase 23f Heavy 1/4; 9 Mar Taunton Chase 23f Good 3/5; 4 Apr Newton Abbot Chase 21f Good 2/6
    DATA for: Last-run finishing speed +4.4% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions; First-time headgear; Pace: a contested lead should suit its hold-up style
    DATA against: Returns from a 238-day break
- Neon Moon (hrs_21100394) | 10yo G | 153lb | OR 125 | draw 0 | jockey Jack Tudor | trainer David Pipe (14d 3/17) | headgear tb | wind surgery | last run 28 days | form 4F50-8 | MARKET 1.0% | 09:00 median 67.00 | Matchbook 110.00
    comment: The risk is a form line that reads eighth last time out, with a fall four starts back, and he is yet to win in his last five.
    DATA: model 4.0% | style Held up (led 4% of runs) | runs in data 4 | last 3: 6 Mar Exeter Chase 19.2f Good To Soft 5/9; 4 Apr Haydock Chase 19.9f Good 10/17; 31 Oct Ascot Chase 24f Good 8/10 fig 115
    DATA for: Pace: a contested lead should suit its hold-up style
    DATA against: Best recent form figure 115, 10 lb below field average; Recent figures 10 lb below its current mark (looks high in the weights); Last-run finishing speed -3.2% vs that field (faded); Fell or unseated in 1 of its last 4 jumps runs

## 1:40 Newbury | race_id rac_32305876213 | Coral "Bet£10 Get£50 Sign Up Offer" Handicap Hurdle Race (GBB Race)
Hurdle | Class 2 | 2m4f118y | going Good To Soft | Turf | 17 runners | rating band 0-145 | age 4yo+
DATA pace: Slow / tactical - No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close.
- Moneygarrow (hrs_41052095) | 6yo G | 161lb | OR 133 | draw 0 | jockey Tristan Durrell | trainer Dan Skelton (14d 27/97) | headgear - | last run 260 days | form 35118- | MARKET 25.2% | 09:00 median 2.88 | Matchbook 3.75
    comment: Absent 260 days and beaten into eighth last time out, Moneygarrow is hard to fancy off 161 lb, though he won two starts back and three starts back and has run over today's trip.
    DATA: model 8.1% | style Held up (led 5% of runs) | runs in data 2 | last 3: 16 Jan Windsor Hurdle 24f Soft 1/6; 13 Mar Cheltenham Hurdle 24f Good To Soft 8/22
    DATA for: Trainer 28% wins (27/97), last 14 days; Last-run finishing speed +2.6% vs that field (finished strongly); Has won at this trip or further
    DATA against: Returns from a 260-day break; Lightly raced: 2 runs in our data, so the model has little to go on; Pace: steady gallop likely, hard to come from off the pace
- A King of Magic (hrs_50154713) | 5yo G | 157lb | OR 129 | draw 0 | jockey Jay Tidball(5) | trainer Paul Nicholls (14d 5/28) | headgear t | last run 219 days | form 45121- | MARKET 11.4% | 09:00 median 7.00 | Matchbook 7.80
    comment: A winner last time out, and a second two starts back, but he returns after 219 days off and carries 157 lb off an official mark of 129.
    DATA: model 12.5% | style Midfield (led 4% of runs) | runs in data 4 | last 3: 12 Feb Taunton Hurdle 16.5f Heavy 1/9; 19 Mar Sedgefield Hurdle 16.8f Good 2/5; 23 Apr Perth Hurdle 20.2f Good 1/8
    DATA for: Last-run finishing speed +7.5% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
    DATA against: Returns from a 219-day break
- Gentleman Toboot (hrs_40095853) | 6yo G | 157lb | OR 129 | draw 0 | jockey Jack Tudor | trainer David Pipe (14d 3/17) | headgear t | wind surgery | last run 266 days | form /1137- | MARKET 10.1% | 09:00 median 7.00 | Matchbook 9.60
    comment: Gentleman Toboot won two of his last four, but he was beaten in a seventh last time out and returns after 266 days off, carrying a hefty 157 lb off 129.
    DATA: model 4.8% | style Unknown | runs in data 1 | last 3: 7 Mar Sandown Hurdle 19.8f Soft 7/17
    DATA against: Last-run finishing speed -2.6% vs that field (faded); Returns from a 266-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Spirits Bay (hrs_32936526) | 8yo G | 152lb | OR 124 | draw 0 | jockey Sam Twiston-Davies | trainer Nigel & Willy Twiston-Davies (14d 3/18) | headgear - | last run 23 days | form 3476-2 | MARKET 7.6% | 09:00 median 9.50 | Matchbook 12.50
    comment: Spirits Bay arrives in decent heart after a second last time out, though he is yet to win in his last five starts and finished sixth and seventh before that.
    DATA: model 4.7% | style Midfield (led 3% of runs) | runs in data 4 | last 3: 12 Feb Taunton Hurdle 16.5f Heavy 7/7; 7 Mar Sandown Hurdle 16f Soft 6/18; 5 Nov Newbury Hurdle 16.5f Good To Soft 2/16 fig 126
    DATA for: Carries 6 lb less than average
    DATA against: Official rating 124, 7 lb below field average
- Frontier Prince (hrs_46265569) | 5yo G | 154lb | OR 126 | draw 0 | jockey Jack Hogan | trainer Fergal O'Brien (14d 5/28) | headgear t | last run 36 days | form 34-011 | MARKET 6.3% | 09:00 median 12.00 | Matchbook 15.00
    comment: Frontier Prince arrives in cracking nick, having won last time out and again two starts back, and he has run over today's trip, but 154 lb is a big burden and a 36-day absence is a query.
    DATA: model 8.0% | style Midfield (led 3% of runs) | runs in data 6 | last 3: 9 May Haydock Hurdle 15.7f Good To Soft 12/16; 23 Sep Perth Hurdle 20.2f Good 1/12; 23 Oct Cheltenham Hurdle 20f Good To Soft 1/11 fig 128
    DATA for: Has won at this trip or further; Good recent finishing positions
- Fingle Bridge (hrs_32638277) | 8yo G | 163lb | OR 135 | draw 0 | jockey Sean Bowen | trainer Olly Murphy (14d 9/41) | headgear - | last run 232 days | form 13200- | MARKET 5.9% | 09:00 median 12.00 | Matchbook 16.50
    comment: Fingle Bridge has a win, a third and a second in his last five starts, but he has been unplaced in his last two and returns after 232 days off.
    DATA: model 4.7% | style Held up (led 5% of runs) | runs in data 4 | last 3: 7 Feb Warwick Hurdle 21f Heavy 2/8; 7 Mar Sandown Hurdle 16f Soft 14/18; 10 Apr Aintree Hurdle 20f Good To Soft 21/22
    DATA for: Trainer 22% wins (9/41), last 14 days
    DATA against: Last-run finishing speed -4.0% vs that field (faded); Returns from a 232-day break; Pace: steady gallop likely, hard to come from off the pace
- Firestream (hrs_24568803) | 9yo G | 150lb | OR 122 | draw 0 | jockey Benjamin Macey(5) | trainer Chester Williams (14d 0/2) | headgear tp | last run 23 days | form /P56-6 | MARKET 5.4% | 09:00 median 13.00 | Matchbook 18.00
    comment: Firestream is winless in his last four, finishing sixth on his last two outings and a fifth three starts back, though he has run over today's trip and returns after 23 days.
    DATA: model 4.5% | style Prominent (led 23% of runs) | runs in data 4 | last 3: 14 Mar Uttoxeter Hurdle 19.9f Soft 5/14; 15 Apr Haydock Hurdle 24.3f Good 6/10; 5 Nov Newbury Hurdle 24.5f Good To Soft 6/16 fig 120
    DATA for: Carries 8 lb less than average
    DATA against: Best recent form figure 120, 6 lb below field average; Official rating 122, 9 lb below field average; Pulled up in 1 of its last 4 jumps runs
- Califet En Vol (hrs_37890573) | 7yo G | 165lb | OR 137 | draw 0 | jockey Nico de Boinville | trainer Nicky Henderson (14d 2/24) | headgear - | last run 28 days | form 5147-6 | MARKET 4.8% | 09:00 median 15.00 | Matchbook 20.00
    comment: The risk is a form line that has slipped to a seventh and a sixth in his last two outings, under a hefty 165 lb.
    DATA: model 7.3% | style Prominent (led 23% of runs) | runs in data 6 | last 3: 14 Mar Kempton Chase 20.5f Good 4/7; 17 Apr Ayr Chase 20.5f Soft 7/9; 31 Oct Ascot Chase 24f Good 6/10 fig 128
    DATA for: Official rating 137, 6 lb above field average; Has won at this trip or further
    DATA against: Recent figures 9 lb below its current mark (looks high in the weights); Last-run finishing speed -2.2% vs that field (faded); Carries 7 lb more than average; Race comments mention jumping mistakes in 2 of its last 5 runs; First run over hurdles in our data
- Jig's Forge (hrs_34788775) | 7yo G | 164lb | OR 136 | draw 0 | jockey Ben Jones | trainer Ben Pauling (14d 8/39) | headgear - | last run 294 days | form 7/315- | MARKET 4.6% | 09:00 median 17.00 | Matchbook 20.00
    comment: Jig's Forge won two starts back and was third the run before, but he was only fifth last time out and returns after a 294-day break, which raises fitness doubts.
    DATA: model 6.3% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 7 Feb Newbury Chase 23.4f Heavy 5/10
    DATA for: Official rating 136, 5 lb above field average; Trainer 21% wins (8/39), last 14 days
    DATA against: Last-run finishing speed -4.3% vs that field (faded); Carries 6 lb more than average; Returns from a 294-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Walk On High (hrs_27358688) | 9yo G | 149lb | OR 121 | draw 0 | jockey Bryan Carver | trainer Harry Fry (14d 2/7) | headgear ht | last run 26 days | form 115P-4 | MARKET 4.4% | 09:00 median 15.00 | Matchbook 24.00
    DATA: model 3.1% | style Held up (led 4% of runs) | runs in data 3 | last 3: 17 Jan Taunton Hurdle 19f Good To Soft 5/5; 28 Mar Uttoxeter Chase 20f Good To Soft PU/7; 2 Nov Plumpton Hurdle 20.5f Good 4/12 fig 124
    DATA for: Trainer 29% wins (2/7), last 14 days; Last-run finishing speed +5.5% vs that field (finished strongly); Carries 9 lb less than average
    DATA against: Official rating 121, 10 lb below field average; Pulled up in 1 of its last 3 jumps runs; Pace: steady gallop likely, hard to come from off the pace
- Ace of Spades (hrs_38306268) | 7yo G | 165lb | OR 137 | draw 0 | jockey Jonathan Burke | trainer Dan Skelton (14d 27/97) | headgear - | last run 35 days | form 2108-0 | MARKET 3.1% | 09:00 median 23.00 | Matchbook 32.00
    comment: Ace of Spades has gone unplaced last time out and an eighth two starts back, so the form has cooled since a win four starts back, though he has run over today's trip and arrives fresh after 35 days off. A weight of 165 lb and a yard in good form leave this a balanced picture.
    DATA: model 7.3% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 12 Mar Cheltenham Hurdle 24f Good 13/24; 11 Apr Aintree Hurdle 24.7f Good To Soft 8/22; 24 Oct Cheltenham Hurdle 24f Good 10/19 fig 130
    DATA for: Best recent form figure 130, 4 lb above field average; Official rating 137, 6 lb above field average; Trainer 28% wins (27/97), last 14 days; Has won at this trip or further
    DATA against: Recent figures 7 lb below its current mark (looks high in the weights); Poor recent finishing positions; Carries 7 lb more than average; Race comments mention jumping mistakes in 2 of its last 5 runs
- One Horse Town (hrs_46944660) | 4yo G | 156lb | OR 129 | draw 0 | jockey Alice Stevens(3) | trainer Harry Derham (14d 1/16) | headgear - | last run 35 days | form 2206-3 | MARKET 2.7% | 09:00 median 26.00 | Matchbook 38.00
    comment: One Horse Town signed off with a third last time out, and has a second four and five starts back, but he's yet to win in his last five and has had 35 days off.
    DATA: model 7.6% | style Prominent (led 29% of runs) | runs in data 6 | last 3: 2 May Punchestown Hurdle 16f Yielding 6/12; 1 Oct Salisbury Flat 14.2f Soft 2/10; 24 Oct Cheltenham Hurdle 16.5f Good To Soft 3/7 fig 120
    DATA for: Good recent finishing positions
    DATA against: Best recent form figure 120, 6 lb below field average; Recent figures 9 lb below its current mark (looks high in the weights); Race comments mention jumping mistakes in 2 of its last 5 runs
- Court In The Act (hrs_34470660) | 7yo G | 153lb | OR 125 | draw 0 | jockey Paul O'Brien | trainer Harry Derham (14d 1/16) | headgear - | last run 608 days | form 91041/ | MARKET 2.6% | 09:00 median 29.00 | Matchbook 36.00
    comment: He has run over today's trip, yet the long absence makes him hard to fancy.
    DATA: model 4.3% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Carries 5 lb less than average
    DATA against: Official rating 125, 6 lb below field average; Returns from a 608-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Nurse Susan (hrs_27371855) | 9yo M | 164lb | OR 136 | draw 0 | jockey Miss Heidi Palin(5) | trainer Dan Skelton (14d 27/97) | headgear - | last run 27 days | form 1140-8 | MARKET 2.0% | 09:00 median 29.00 | Matchbook 70.00
    comment: Nurse Susan won two of her last five, four and five starts back, but has faded since with a fourth three starts back, an unplaced run, then an eighth last time out 27 days ago. She has run over today's trip and gets a boost from a yard in form, though 164 lb is a stiff burden.
    DATA: model 4.0% | style Held up (led 3% of runs) | runs in data 4 | last 3: 22 Feb Fontwell Hurdle 19.1f Heavy 4/5; 13 Mar Cheltenham Hurdle 20.3f Good To Soft 16/24; 1 Nov Carlisle Hurdle 20f Good To Soft 8/10 fig 129
    DATA for: Official rating 136, 5 lb above field average; Trainer 28% wins (27/97), last 14 days
    DATA against: Recent figures 7 lb below its current mark (looks high in the weights); Carries 6 lb more than average; Pace: steady gallop likely, hard to come from off the pace
- Kamsinas (hrs_29117102) | 9yo G | 161lb | OR 133 | draw 0 | jockey Tom Broughton(3) | trainer Fergal O'Brien (14d 5/28) | headgear t | last run 27 days | form 55F3-6 | MARKET 1.8% | 09:00 median 34.00 | Matchbook 65.00
    comment: Kamsinas is yet to win in his last five, but a third two starts back and a 27-day break since a sixth last time out keep him in the picture, and he has run over today's trip.
    DATA: model 4.4% | style Held up (led 3% of runs) | runs in data 5 | last 3: 28 Feb Doncaster Hurdle 24.4f Soft F/5; 19 Apr Plumpton Hurdle 25f Good 3/10; 1 Nov Carlisle Hurdle 20f Good To Soft 6/10 fig 128
    DATA against: Fell or unseated in 1 of its last 5 jumps runs; Pace: steady gallop likely, hard to come from off the pace
- Too Bossy For Us (hrs_36878821) | 5yo G | 168lb | OR 140 | draw 0 | jockey Richie McLernon | trainer Faye Bramley (14d 1/13) | headgear - | last run 41 days | form 16P6-0 | MARKET 1.2% | 09:00 median 51.00 | Matchbook 140.00
    DATA: model 4.3% | style Midfield (led 3% of runs) | runs in data 11 | last 3: 12 Sep Leopardstown Flat 13f Good 3/21; 27 Sep Curragh Flat 16.8f Heavy 23/30; 18 Oct Leopardstown (IRE) Flat 11.5f Good 9/15 fig 82
    DATA for: Official rating 140, 9 lb above field average
    DATA against: Carries 10 lb more than average; Pulled up in 1 of its last 5 jumps runs
- Insurrection (hrs_33275046) | 9yo G | 155lb | OR 127 | draw 0 | jockey Caoilin Quinn | trainer Nick Scholfield (14d 1/13) | headgear - | last run 21 days | form 3803-7 | MARKET 0.8% | 09:00 median 67.00 | Matchbook 180.00
    comment: Seventh last time out after a third two starts back, Insurrection is winless in his last five and has run over today's trip, but he's had 21 days to recover.
    DATA: model 3.9% | style Midfield (led 4% of runs) | runs in data 5 | last 3: 12 Mar Cheltenham Chase 26.3f Good 18/23; 16 Apr Hereford Chase 20.9f Good 3/5; 7 Nov Aintree Chase 20f Good To Soft 7/11
    DATA against: First run over hurdles in our data

## 2:20 Newbury | race_id rac_32304613289 | Coral Racing Club Intermediate Handicap Hurdle Race (Registered As The Gerry Feilden) (Premier Handicap) (GBB Race)
Hurdle | Class 1 | 2m0f69y | going Good To Soft | Turf | 8 runners | rating band - | age 4yo+
DATA pace: Lone leader - Mossy Fen Road is the only habitual front-runner and may be allowed an easy lead.
- Idaho Sun (hrs_41228957) | 6yo G | 168lb | OR 142 | draw 0 | jockey Bryan Carver | trainer Harry Fry (14d 2/7) | headgear - | last run 337 days | form 6/111- | MARKET 35.7% | 09:00 median 2.50 | Matchbook 2.66
    comment: Idaho Sun arrives on a hat-trick of wins, having won last time out, and again two and three starts back, and he has run over today's trip, while 168 lb is a hefty burden. The one big risk is a 337-day absence, so rustiness could blunt him.
    DATA: model 11.7% | style Unknown | runs in data 0 | last 3: none in our data
    DATA for: Official rating 142, 10 lb above field average; Trainer 29% wins (2/7), last 14 days
    DATA against: Carries 10 lb more than average; Returns from a 337-day break; Lightly raced: 0 runs in our data, so the model has little to go on
- Minella Yoga (hrs_57654548) | 4yo G | 157lb | OR 131 | draw 0 | jockey Sam Twiston-Davies | trainer Paul Nicholls (14d 5/28) | headgear - | last run 217 days | form 11315- | MARKET 13.5% | 09:00 median 6.50 | Matchbook 7.20
    comment: Three wins in his last five starts is a decent record, and he has run over today's trip, but a fifth last time out and a 217-day absence temper enthusiasm, while 157 lb is a hefty burden.
    DATA: model 20.7% | style Prominent (led 8% of runs) | runs in data 3 | last 3: 24 Jan Cheltenham Hurdle 16.8f Soft 3/10; 9 Apr Taunton Hurdle 16.5f Good 1/7; 25 Apr Sandown Hurdle 16f Good 5/15
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Returns from a 217-day break
- La Conquiere (hrs_40669055) | 7yo M | 158lb | OR 132 | draw 0 | jockey Gavin Sheehan | trainer Jamie Snowden (14d 4/15) | headgear - | last run 28 days | form 1206-2 | MARKET 13.4% | 09:00 median 6.50 | Matchbook 7.20
    comment: La Conquiere was second last time out 28 days ago, and she's placed twice in her last five, but a sixth two starts back and a single win five starts back leave her short of a winner's profile.
    DATA: model 7.1% | style Held up (led 3% of runs) | runs in data 4 | last 3: 12 Mar Cheltenham Hurdle 16.8f Good 14/22; 10 Apr Aintree Hurdle 16.5f Good To Soft 6/6; 31 Oct Wetherby Hurdle 16f Good 2/4 fig 129
    DATA for: Trainer 27% wins (4/15), last 14 days
- Mossy Fen Road (hrs_39959409) | 6yo G | 162lb | OR 136 | draw 0 | jockey Paul O'Brien | trainer Harry Derham (14d 1/16) | headgear - | last run 300 days | form 9/112- | MARKET 11.2% | 09:00 median 7.50 | Matchbook 9.00
    comment: Hard to fancy after 300 days off, despite a second last time out and a winner two starts back and again three starts back, while carrying 162 lb off an official mark of 136.
    DATA: model 15.7% | style Leader (led 57% of runs) | runs in data 1 | last 3: 1 Feb Musselburgh Hurdle 15.6f Good To Soft 2/4
    DATA for: Pace: may get an uncontested lead
    DATA against: Returns from a 300-day break; Lightly raced: 1 run in our data, so the model has little to go on
- White Noise (hrs_49577822) | 6yo M | 162lb | OR 136 | draw 0 | jockey Tom Bellamy | trainer Kim Bailey & Mat Nicholls (14d 6/18) | headgear t | wind surgery | last run 20 days | form 1212-4 | MARKET 9.1% | 09:00 median 9.50 | Matchbook 11.00
    comment: White Noise arrives in cracking recent form, a winner three starts back and five starts back with a second in between, and she was a fourth last time out just 20 days ago.
    DATA: model 18.3% | style Prominent (led 23% of runs) | runs in data 4 | last 3: 12 Mar Cheltenham Hurdle 16.8f Good 1/22; 15 Apr Haydock Hurdle 21.2f Good 2/8; 8 Nov Sandown Hurdle 20f Good To Soft 4/8 fig 133
    DATA for: Trainer 33% wins (6/18), last 14 days; Has won at this trip or further; Good recent finishing positions
- Our Boy Stan (hrs_48499283) | 5yo G | 146lb | OR 120 | draw 0 | jockey Ben Jones | trainer Ben Pauling (14d 8/39) | headgear - | wind surgery | last run 224 days | form 1/166- | MARKET 7.9% | 09:00 median 12.00 | Matchbook 12.00
    DATA: model 3.7% | style Prominent (led 8% of runs) | runs in data 1 | last 3: 18 Apr Ayr Hurdle 21.4f Heavy 6/8
    DATA for: Trainer 21% wins (8/39), last 14 days; Carries 12 lb less than average
    DATA against: Official rating 120, 12 lb below field average; Returns from a 224-day break; Lightly raced: 1 run in our data, so the model has little to go on
- Mondo Man (hrs_37672796) | 5yo G | 159lb | OR 133 | draw 0 | jockey Caoilin Quinn | trainer Jamie Moore & Josh Moore (14d 3/33) | headgear - | last run 162 days | form 24116- | MARKET 6.3% | 09:00 median 13.00 | Matchbook 16.50
    comment: The main risk is a 162-day absence, with 159 lb to carry.
    DATA: model 13.1% | style Prominent (led 38% of runs) | runs in data 4 | last 3: 7 Mar Sandown Hurdle 16f Soft 1/18; 5 Apr Plumpton Hurdle 15.9f Good 6/14; 19 Jun Ascot Flat 12f Good To Firm 16/17
    DATA for: Has won at this trip or further
    DATA against: Last-run finishing speed -6.5% vs that field (faded); Returns from a 162-day break
- Klycot (hrs_52677058) | 4yo G | 155lb | OR 129 | draw 0 | jockey Jonathan Burke | trainer Richard Bandey (14d 0/2) | headgear - | last run 31 days | form 41213- | MARKET 2.8% | 09:00 median 29.00 | Matchbook 38.00
    comment: Klycot arrives in cracking form, third last time out and a winner two starts back, with another win four starts back, and he has run over today's trip before. The main risk is a 31-day break while carrying 155 lb.
    DATA: model 9.7% | style Prominent (led 23% of runs) | runs in data 4 | last 3: 10 Mar Cheltenham Hurdle 16.4f Good To Soft 3/22; 11 Oct Goodwood Flat 16f Good To Soft 7/12; 28 Oct Nottingham Flat 14f Soft 7/13 fig 71
    DATA for: Has won at this trip or further

## 3:00 Newbury | race_id rac_32303247704 | Coral Gold Cup Handicap Steeple Chase (Registered As The Newbury Gold Cup) (Premier Handicap) (GBB Race)
Chase | Class 1 | 3m1f214y | going Good | Turf | 17 runners | rating band - | age 4yo+
DATA pace: Strong pace - 5 habitual front-runners (Panic Attack, The Jukebox Kid, Myretown, Amirite, Here Comes Georgie). A contested lead should set things up for horses coming from behind.
- Wendigo (hrs_34457227) | 7yo G | 166lb | OR 147 | draw 0 | jockey Gavin Sheehan | trainer Jamie Snowden (14d 4/15) | headgear - | last run 27 days | form 31F6-1 | MARKET 17.3% | 09:00 median 4.42 | Matchbook 5.50 | CHECK (skip line 4.19)
    comment: Wendigo arrives a winner last time out, with another success four starts back, and 27 days since that run suggests he's fresh.
    DATA: model 5.0% | style Held up (led 5% of runs) | runs in data 4 | last 3: 11 Mar Cheltenham Chase 25f Good F/14; 10 Apr Aintree Chase 25f Good To Soft 6/8; 1 Nov Carlisle Chase 20f Good 1/3 fig 154
    DATA for: Best recent form figure 154, 16 lb above field average; Recent figures 7 lb above its current mark (looks well handicapped); Official rating 147, 6 lb above field average; Trainer 27% wins (4/15), last 14 days; Pace: a contested lead should suit its hold-up style
    DATA against: Carries 6 lb more than average; Fell or unseated in 1 of its last 4 jumps runs
- Regent's Stroll (hrs_37095968) | 7yo G | 168lb | OR 149 | draw 0 | jockey Sam Twiston-Davies | trainer Paul Nicholls (14d 5/28) | headgear h | wind surgery | last run 232 days | form 31232- | MARKET 11.2% | 09:00 median 6.75 | Matchbook 8.60
    comment: Regent's Stroll arrives with a consistent profile, finishing second last time out, third two starts back and second three starts back, and he won four starts back. The one concern is a 232-day absence, so fitness is the main risk, especially under 168 lb.
    DATA: model 7.5% | style Prominent (led 5% of runs) | runs in data 3 | last 3: 1 Jan Cheltenham Chase 20.6f Good 2/5; 12 Mar Cheltenham Chase 20.6f Good 3/18; 10 Apr Aintree Chase 25f Good To Soft 2/8
    DATA for: Official rating 149, 8 lb above field average; Good recent finishing positions
    DATA against: Carries 8 lb more than average; Returns from a 232-day break
- Miami Magic (hrs_34457255) | 7yo G | 164lb | OR 145 | draw 0 | jockey Charlie Hammond | trainer Stuart Edmunds (14d 2/13) | headgear - | wind surgery | last run 23 days | form 131F-2 | MARKET 11.1% | 09:00 median 7.25 | Matchbook 8.20
    DATA: model 7.5% | style Prominent (led 4% of runs) | runs in data 5 | last 3: 27 Feb Newbury Chase 23.4f Good To Soft 1/5; 10 Apr Aintree Chase 25f Good To Soft F/8; 5 Nov Newbury Hurdle 24.5f Good To Soft 2/16 fig 141
    DATA against: Fell or unseated in 1 of its last 5 jumps runs
- Road To Home (hrs_39827186) | 7yo G | 159lb | OR 140 | draw 0 | jockey Mr P. W. Mullins | trainer W. P. Mullins (14d 16/53) | headgear - | last run 53 days | form 3P23-1 | MARKET 8.2% | 09:00 median 9.50 | Matchbook 11.50
    comment: Road To Home won last time out and has a third and a second before that, so the form is solid, and he has run over today's trip, with the yard in cracking form.
    DATA: model 8.4% | style Prominent (led 29% of runs) | runs in data 4 | last 3: 12 Mar Cheltenham Chase 26.3f Good 2/23; 25 Apr Sandown Chase 28.7f Good 3/11; 6 Oct Galway Chase 18.2f Yielding To Soft 1/8
    DATA for: Trainer 30% wins (16/53), last 14 days; Good recent finishing positions
    DATA against: Pulled up in 1 of its last 4 jumps runs
- Mr Hope Street (hrs_33729843) | 8yo G | 154lb | OR 135 | draw 0 | jockey Jonathan Burke | trainer Dan Skelton (14d 27/97) | headgear - | last run 30 days | form 6341-3 | MARKET 8.1% | 09:00 median 8.50 | Matchbook 13.00
    comment: A 30-day break and a yard in cracking form (27 from 97) are the positives.
    DATA: model 4.7% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 7 Mar Sandown Chase 20.1f Soft 4/5; 11 Apr Aintree Chase 25f Good To Soft 1/13; 29 Oct Stratford Chase 19.5f Good To Soft 3/10 fig 134
    DATA for: Trainer 28% wins (27/97), last 14 days; Last-run finishing speed +3.3% vs that field (finished strongly); Good recent finishing positions; Carries 6 lb less than average
    DATA against: Best recent form figure 134, 4 lb below field average; Official rating 135, 6 lb below field average
- Kap Vert (hrs_39996502) | 6yo G | 155lb | OR 136 | draw 0 | jockey Sean Houlihan | trainer Philip Hobbs & Johnson White (14d 3/17) | headgear - | last run 22 days | form 3411-3 | MARKET 7.5% | 09:00 median 10.00 | Matchbook 13.00
    comment: Fit enough after 22 days, he still looks hard to fancy.
    DATA: model 4.5% | style Midfield (led 4% of runs) | runs in data 4 | last 3: 9 Mar Taunton Chase 23f Good 1/5; 18 Apr Ayr Chase 31.8f Heavy 1/16; 6 Nov Aintree Chase 25f Good To Soft 3/12 fig 136
    DATA for: Last-run finishing speed +2.1% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions; Carries 5 lb less than average
    DATA against: Official rating 136, 5 lb below field average
- Booster Bob (hrs_33975739) | 8yo G | 157lb | OR 138 | draw 0 | jockey Sean Bowen | trainer Olly Murphy (14d 9/41) | headgear - | wind surgery | last run 232 days | form /15F0- | MARKET 5.8% | 09:00 median 13.00 | Matchbook 16.50
    comment: Booster Bob is hard to fancy after 232 days off, having been unplaced last time out and fallen two starts back, with his win now four starts old.
    DATA: model 4.6% | style Held up (led 8% of runs) | runs in data 3 | last 3: 24 Jan Cheltenham Chase 20.6f Soft 5/11; 10 Mar Cheltenham Chase 20.2f Good To Soft F/23; 10 Apr Aintree Chase 21.1f Good To Soft 13/27
    DATA for: Trainer 22% wins (9/41), last 14 days; Pace: a contested lead should suit its hold-up style
    DATA against: Returns from a 232-day break; Fell or unseated in 1 of its last 3 jumps runs
- Masaccio (hrs_16761871) | 9yo G | 166lb | OR 147 | draw 0 | jockey Tom Bellamy | trainer Alan King (14d 3/26) | headgear - | last run 23 days | form 3331/1 | MARKET 5.4% | 09:00 median 13.00 | Matchbook 19.00
    comment: Masaccio arrives in cracking form, a winner last time out and again two starts back, with a third before that three times running, and he's fresh enough after 23 days off. The main risk is the 166 lb burden, which is a big ask off an official mark of 147.
    DATA: model 4.9% | style Unknown | runs in data 1 | last 3: 5 Nov Newbury Hurdle 24.5f Good To Soft 1/16 fig 143
    DATA for: Best recent form figure 143, 5 lb above field average; Official rating 147, 6 lb above field average
    DATA against: Carries 6 lb more than average; Lightly raced: 1 run in our data, so the model has little to go on
- Panic Attack (hrs_20789300) | 10yo M | 164lb | OR 145 | draw 0 | jockey Dominic Lewis(10) | trainer Dan Skelton (14d 27/97) | headgear - | last run 220 days | form 113F3- | MARKET 5.0% | 09:00 median 13.00 | Matchbook 23.00
    comment: Third last time out, and a winner four and five starts back, she has the form to sit in the mix, but 220 days off and a fall two starts back raise fitness and confidence questions. Has run over today's trip, and the yard is in form.
    DATA: model 6.5% | style Leader (led 43% of runs) | runs in data 4 | last 3: 13 Mar Cheltenham Chase 20.6f Good To Soft 3/8; 11 Apr Aintree Chase 34.3f Good To Soft F/34; 22 Apr Perth Chase 23.8f Good 3/4
    DATA for: Trainer 28% wins (27/97), last 14 days
    DATA against: Returns from a 220-day break; Fell or unseated in 1 of its last 4 jumps runs; Pace: likely to be taken on for the lead
- The Jukebox Kid (hrs_39699261) | 7yo G | 161lb | OR 142 | draw 0 | jockey Ben Jones | trainer Ben Pauling (14d 8/39) | headgear - | wind surgery | last run 23 days | form 411P-0 | MARKET 3.7% | 09:00 median 19.00 | Matchbook 28.00
    comment: Won twice in his last five starts, a win three starts back and another four starts back, but he was unplaced last time and pulled up before that, so the form has tailed off. He has run over today's trip and returns after 23 days, though 161 lb is a stiff burden.
    DATA: model 6.2% | style Leader (led 43% of runs) | runs in data 4 | last 3: 14 Feb Ascot Chase 23.8f Good To Soft 1/3; 6 Apr Fairyhouse Chase 29.1f Yielding To Soft PU/30; 5 Nov Newbury Hurdle 24.5f Good To Soft 14/16
    DATA for: Trainer 21% wins (8/39), last 14 days
    DATA against: Pulled up in 1 of its last 4 jumps runs; Pace: likely to be taken on for the lead
- Downmexicoway (hrs_34073571) | 7yo G | 166lb | OR 147 | draw 0 | jockey Sean Flanagan | trainer Henry de Bromhead (14d 6/36) | headgear p (1st time) | last run 66 days | form 134-53 | MARKET 3.4% | 09:00 median 21.00 | Matchbook 29.00
    comment: Downmexicoway was third last time out and a winner five starts back, so the recent form is solid without being sharp, but a 66-day absence is a question after that.
    DATA: model 8.6% | style Prominent (led 3% of runs) | runs in data 4 | last 3: 10 Mar Cheltenham Chase 20.2f Good To Soft 4/23; 29 Jul Galway Chase 22.5f Good 5/22; 23 Sep Listowel Chase 23.8f Good 3/18
    DATA for: Official rating 147, 6 lb above field average; Last-run finishing speed +3.9% vs that field (finished strongly); First-time headgear
    DATA against: Carries 6 lb more than average; Race comments mention jumping mistakes in 2 of its last 4 runs
- Myretown (hrs_28220514) | 9yo G | 161lb | OR 142 | draw 0 | jockey Patrick Wadge | trainer Lucinda Russell & Michael Scudamore (14d 2/24) | headgear - | last run 35 days | form 4P08-1 | MARKET 3.2% | 09:00 median 23.00 | Matchbook 30.00
    comment: Myretown won last time out, but that came after an eighth two starts back and a pulled up four runs ago, so the form is patchy.
    DATA: model 5.6% | style Leader (led 38% of runs) | runs in data 5 | last 3: 10 Mar Cheltenham Chase 25f Good To Soft 13/22; 17 Apr Ayr Chase 20.5f Soft 8/9; 24 Oct Kelso Chase 26f Good 1/4 fig 137
    DATA for: Has won at this trip or further
    DATA against: Race comments mention jumping mistakes in 2 of its last 5 runs; Pulled up in 1 of its last 5 jumps runs; Pace: likely to be taken on for the lead
- One Big Bang (hrs_29226575) | 8yo G | 156lb | OR 137 | draw 0 | jockey Ciaran Gethings | trainer James Owen (14d 5/46) | headgear - | last run 23 days | form 1336-5 | MARKET 3.0% | 09:00 median 23.00 | Matchbook 34.00
    comment: One Big Bang has a win and two thirds in his last five starts, though he's tailed off to a sixth and then a fifth last time out, and he returns after 23 days with 156 lb.
    DATA: model 5.0% | style Midfield (led 5% of runs) | runs in data 4 | last 3: 10 Mar Cheltenham Chase 29.9f Good To Soft 3/17; 6 Apr Fairyhouse Chase 29.1f Yielding To Soft 6/30; 5 Nov Newbury Hurdle 24.5f Good To Soft 5/16 fig 136
- Havaila (hrs_29987923) | 7yo G | 158lb | OR 139 | draw 0 | jockey Caoilin Quinn | trainer Jamie Moore & Josh Moore (14d 3/33) | headgear - | last run 217 days | form 36111- | MARKET 2.8% | 09:00 median 23.00 | Matchbook 42.00
    comment: Havaila won last time out and has taken three of his last five, but he returns after 217 days off, has run over today's trip, and carries 158 lb off 139.
    DATA: model 9.7% | style Held up (led 4% of runs) | runs in data 5 | last 3: 21 Mar Newbury Chase 23.4f Good To Soft 1/7; 6 Apr Plumpton Chase 28.5f Good 1/10; 25 Apr Sandown Chase 28.7f Good 1/11
    DATA for: Last-run finishing speed +2.1% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions; Pace: a contested lead should suit its hold-up style
    DATA against: Returns from a 217-day break
- Here Comes Georgie (hrs_34888679) | 8yo G | 149lb | OR 130 | draw 0 | jockey Tristan Durrell | trainer Dan Skelton (14d 27/97) | headgear t | last run 22 days | form 633-17 | MARKET 2.4% | 09:00 median 29.00 | Matchbook 42.00
    DATA: model 5.1% | style Leader (led 72% of runs) | runs in data 4 | last 3: 7 Mar Sandown Chase 20.1f Soft 3/3; 24 Oct Cheltenham Chase 25f Good To Soft 1/9 fig 123; 6 Nov Aintree Chase 25f Good To Soft 7/12 fig 126
    DATA for: Trainer 28% wins (27/97), last 14 days; Good recent finishing positions; Carries 11 lb less than average
    DATA against: Best recent form figure 126, 12 lb below field average; Official rating 130, 11 lb below field average; Pace: likely to be taken on for the lead
- The Doyen Chief (hrs_33080705) | 9yo G | 158lb | OR 139 | draw 0 | jockey Tom Cannon | trainer Nick Scholfield (14d 1/13) | headgear p (1st time) | wind surgery | last run 34 days | form 129P-2 | MARKET 1.2% | 09:00 median 51.00 | Matchbook 90.00
    comment: The Doyen Chief was second last time out after a pulled up and a ninth in the two runs before, so his form has a patchy look, though he has a win five starts back and a second four starts back.
    DATA: model 3.8% | style Held up (led 3% of runs) | runs in data 5 | last 3: 10 Mar Cheltenham Chase 25f Good To Soft 9/22; 2 May Punchestown Chase 24.5f Yielding PU/21; 25 Oct Market Rasen Chase 27.5f Good To Soft 2/4 fig 138
    DATA for: First-time headgear; Pace: a contested lead should suit its hold-up style
    DATA against: Race comments mention jumping mistakes in 2 of its last 5 runs; Pulled up in 1 of its last 5 jumps runs
- Amirite (hrs_27040580) | 10yo G | 158lb | OR 139 | draw 0 | jockey Freddie Gordon | trainer Chris Gordon (14d 3/15) | headgear - | last run 23 days | form 0PP-40 | MARKET 0.5% | 09:00 median 101.00 | Matchbook 300.00
    DATA: model 2.5% | style Leader (led 43% of runs) | runs in data 4 | last 3: 11 Apr Aintree Chase 34.3f Good To Soft PU/34; 10 Jul Kilbeggan Chase 25.4f Good 4/14; 5 Nov Newbury Hurdle 24.5f Good To Soft 13/16
    DATA for: Trainer 20% wins (3/15), last 14 days
    DATA against: Pulled up in 2 of its last 4 jumps runs; Pace: likely to be taken on for the lead

## 3:38 Newbury | race_id rac_32305878150 | Coral "Pipped-At-The-Post" And Win Handicap Steeple Chase (For The Jim Joel Memorial Trophy) (GBB Race)
Chase | Class 3 | 2m0f92y | going Good | Turf | 12 runners | rating band 0-140 | age 4yo+
DATA pace: Lone leader - Escapeandevade is the only habitual front-runner and may be allowed an easy lead.
- Un Sens A La Vie (hrs_41052697) | 6yo G | 163lb | OR 135 | draw 0 | jockey Sam Twiston-Davies | trainer Nigel & Willy Twiston-Davies (14d 3/18) | headgear - | last run 25 days | form 142-11 | MARKET 20.0% | 09:00 median 4.00 | Matchbook 4.90 | CHECK (skip line 3.80)
    comment: Un Sens A La Vie arrives in cracking form, a winner last time out and two starts back, with three wins in his last five, and he has run over today's trip.
    DATA: model 15.0% | style Prominent (led 38% of runs) | runs in data 4 | last 3: 22 Apr Ludlow Hurdle 15.8f Good 2/6; 26 Sep Market Rasen Hurdle 16.6f Good 1/12; 3 Nov Warwick Chase 16f Good 1/2 fig 131
    DATA for: Best recent form figure 131, 4 lb above field average; Last-run finishing speed +3.3% vs that field (finished strongly); Has won at this trip or further; Good recent finishing positions
- Ryan's Rocket (hrs_29283590) | 8yo G | 167lb | OR 139 | draw 0 | jockey Jonathan Burke | trainer Fergal O'Brien (14d 5/28) | headgear - | last run 7 days | form 1U61-B | MARKET 16.4% | 09:00 median 5.00 | Matchbook 6.00
    comment: Ryan's Rocket has won twice in his last five starts, including a first two starts back, and he's back quickly after being brought down last time out seven days ago.
    DATA: model 7.7% | style Midfield (led 4% of runs) | runs in data 3 | last 3: 14 Mar Kempton Chase 20.5f Good 6/7; 9 Apr Aintree Chase 15.8f Good To Soft 1/15; 21 Nov Ascot Chase 17f Good To Firm BD/7
    DATA for: Official rating 139, 8 lb above field average
    DATA against: Carries 8 lb more than average; Fell or unseated in 1 of its last 3 jumps runs
- Wreckless Eric (hrs_38580563) | 6yo G | 155lb | OR 127 | draw 0 | jockey Richie McLernon | trainer Jonjo & A.J. O'Neill (14d 4/33) | headgear p | last run 30 days | form 6203-2 | MARKET 13.5% | 09:00 median 6.50 | Matchbook 6.80
    comment: Runner-up last time out and a third two starts back, Wreckless Eric is yet to win in his last five, and he has run over today's trip before.
    DATA: model 8.2% | style Held up (led 4% of runs) | runs in data 6 | last 3: 10 Apr Aintree Hurdle 16.5f Good To Soft 17/21; 24 Apr Chepstow Hurdle 16.1f Good 3/5; 29 Oct Ffos Las Chase 19.5f Good 2/6 fig 126
    DATA for: Good recent finishing positions
- Pure Carbon (hrs_34637890) | 7yo G | 150lb | OR 122 | draw 0 | jockey Paul O'Brien | trainer Harry Derham (14d 1/16) | headgear - | last run 20 days | form 1231-2 | MARKET 9.6% | 09:00 median 8.50 | Matchbook 10.00
    comment: He has run over today's trip and is fresh after 20 days, but 150 lb is a big burden.
    DATA: model 8.4% | style Midfield (led 4% of runs) | runs in data 5 | last 3: 29 Mar Ascot Chase 16.8f Good 3/5; 19 Apr Stratford Chase 17f Good 1/4; 8 Nov Ffos Las Chase 16f Good 2/4 fig 123
    DATA for: Has won at this trip or further; Good recent finishing positions; Carries 9 lb less than average
    DATA against: Official rating 122, 9 lb below field average
- Daytime Dreaming (hrs_40075875) | 6yo G | 158lb | OR 130 | draw 0 | jockey Jack Andrews | trainer Tom Ellis (14d 0/11) | headgear - | last run 22 days | form 4112-5 | MARKET 9.4% | 09:00 median 9.00 | Matchbook 10.00
    comment: In his favour, he has run over today's trip and is fit after 22 days off.
    DATA: model 7.9% | style Midfield (led 3% of runs) | runs in data 4 | last 3: 27 Feb Newbury Chase 16.4f Good To Soft 1/4; 28 Mar Uttoxeter Chase 20f Good To Soft 2/7; 6 Nov Aintree Chase 16f Good To Soft 5/6 fig 118
    DATA for: Has won at this trip or further; Good recent finishing positions
    DATA against: Best recent form figure 118, 9 lb below field average; Recent figures 12 lb below its current mark (looks high in the weights); Trainer 0 wins from 11 runs, last 14 days
- Pleasington (hrs_37889768) | 8yo G | 158lb | OR 130 | draw 0 | jockey Sean Bowen | trainer Olly Murphy (14d 9/41) | headgear p | wind surgery | last run 225 days | form 52FP1- | MARKET 9.0% | 09:00 median 9.50 | Matchbook 11.00
    comment: Pleasington won last time out, but that came after a pulled up and a fall in his previous two starts, and he returns from 225 days off under 158 lb.
    DATA: model 9.1% | style Unknown | runs in data 3 | last 3: 22 Jan Wetherby Chase 19.4f Soft F/9; 28 Feb Newbury Chase 19.9f Good To Soft PU/11; 17 Apr Ayr Chase 16.5f Soft 1/9
    DATA for: Trainer 22% wins (9/41), last 14 days; Last-run finishing speed +4.7% vs that field (finished strongly); Has won at this trip or further
    DATA against: Returns from a 225-day break; Fell or unseated in 1 of its last 3 jumps runs; Pulled up in 1 of its last 3 jumps runs
- The Four Sixes (hrs_29212904) | 8yo G | 154lb | OR 126 | draw 0 | jockey Freddie Gingell | trainer Chester Williams (14d 0/2) | headgear h | last run 31 days | form 74-P51 | MARKET 5.6% | 09:00 median 15.00 | Matchbook 17.50
    comment: The risk is a patchy record beforehand, with a fifth two starts back and a pulled up before that, plus 154 lb to carry.
    DATA: model 8.7% | style Prominent (led 38% of runs) | runs in data 8 | last 3: 9 May Hexham Hurdle 20.1f Good To Soft PU/12; 17 Oct Newton Abbot Hurdle 17f Good 5/7 fig 117; 28 Oct Newton Abbot Chase 16.5f Good To Soft 1/5 fig 122
    DATA for: Last-run finishing speed +2.3% vs that field (finished strongly); Has won at this trip or further; Carries 5 lb less than average
    DATA against: Best recent form figure 122, 5 lb below field average; Official rating 126, 5 lb below field average; Race comments mention jumping mistakes in 3 of its last 5 runs; Pulled up in 1 of its last 5 jumps runs
- Jour d'Evasion (hrs_35363566) | 7yo G | 161lb | OR 133 | draw 0 | jockey Ciaran Gethings | trainer Henry Daly (14d 3/12) | headgear - | last run 28 days | form 11P8-F | MARKET 5.5% | 09:00 median 15.00 | Matchbook 17.50
    comment: Jour d'Evasion won twice in his last five starts, a first four and five starts back, but a fell last time out, an eighth two starts back and a pulled up three starts back leave questions. He has run over today's trip, returns after 28 days and carries 161 lb off 133.
    DATA: model 5.3% | style Prominent (led 3% of runs) | runs in data 4 | last 3: 11 Mar Cheltenham Chase 15.9f Good PU/20; 15 Apr Haydock Chase 19.9f Good 8/11; 31 Oct Ascot Chase 17f Good F/11
    DATA for: Trainer 25% wins (3/12), last 14 days; Has won at this trip or further
    DATA against: Poor recent finishing positions; Fell or unseated in 1 of its last 4 jumps runs; Pulled up in 1 of its last 4 jumps runs
- Breaking Cover (hrs_28903728) | 8yo G | 169lb | OR 141 | draw 0 | jockey Chad Bament(5) | trainer Anthony Honeyball (14d 1/14) | headgear t | last run 29 days | form 441114 | MARKET 3.5% | 09:00 median 22.00 | Matchbook 29.00
    comment: Three wins in his last six starts, including a hat-trick of victories from four to two starts back, makes Breaking Cover a serious threat, and he has run over today's trip. The risk is a fourth last time out and a hefty 169 lb after 29 days off.
    DATA: model 11.3% | style Held up (led 3% of runs) | runs in data 6 | last 3: 5 Sep Stratford Chase 17f Good 1/5; 4 Oct Kelso Chase 17.1f Good To Firm 1/4; 30 Oct Wetherby Chase 19.5f Good 4/6 fig 139
    DATA for: Best recent form figure 139, 12 lb above field average; Official rating 141, 10 lb above field average; Has won at this trip or further; Good recent finishing positions
    DATA against: Carries 10 lb more than average
- Escapeandevade (hrs_23433641) | 10yo G | 158lb | OR 130 | draw 0 | jockey Alice Stevens(3) | trainer Harry Derham (14d 1/16) | headgear p | last run 37 days | form 2P20-3 | MARKET 3.3% | 09:00 median 24.50 | Matchbook 30.00
    comment: Third last time out and a second three starts back show Escapeandevade is running with credit, yet he is winless in his last five and was unplaced two starts back.
    DATA: model 7.1% | style Leader (led 83% of runs) | runs in data 5 | last 3: 21 Mar Newbury Chase 16.4f Good To Soft 2/5; 30 Apr Punchestown Chase 16.3f Yielding 12/20; 22 Oct Ffos Las Chase 16f Soft 3/6 fig 130
    DATA for: Good recent finishing positions; Pace: may get an uncontested lead
    DATA against: Pulled up in 1 of its last 5 jumps runs; Aged 10, older than most of this field
- Stencil (hrs_41325242) | 5yo G | 165lb | OR 137 | draw 0 | jockey Jack Hogan | trainer Tom George (14d 1/2) | headgear h | last run 22 days | form 210P-6 | MARKET 3.3% | 09:00 median 23.00 | Matchbook 34.00
    comment: Stencil showed he can win when landing a victory four starts back, and a second five starts back is a solid foundation, while 22 days since his last run suggests he's fresh and has run over today's trip. The risk is a sixth last time out followed by a pulled up before that, with 165 lb to carry.
    DATA: model 7.3% | style Midfield (led 4% of runs) | runs in data 4 | last 3: 12 Mar Cheltenham Chase 20.6f Good 10/18; 9 Apr Aintree Chase 15.8f Good To Soft PU/15; 6 Nov Aintree Chase 16f Good To Soft 6/6 fig 124
    DATA for: Official rating 137, 6 lb above field average; Has won at this trip or further
    DATA against: Recent figures 13 lb below its current mark (looks high in the weights); Last-run finishing speed -2.8% vs that field (faded); Poor recent finishing positions; Carries 6 lb more than average; Pulled up in 1 of its last 4 jumps runs
- Jony R (hrs_40899544) | 7yo G | 155lb | OR 127 | draw 0 | jockey Caoilin Quinn | trainer Warren Greatrex (14d 4/22) | headgear - | wind surgery | last run 13 days | form 144P-P | MARKET 1.0% | 09:00 median 67.00 | Matchbook 160.00
    comment: Jony R has been pulled up in his last two starts, which makes him hard to fancy, and he carries 155 lb off an official mark of 127.
    DATA: model 4.0% | style Midfield (led 3% of runs) | runs in data 5 | last 3: 8 Mar Naas Hurdle 16.4f Soft To Heavy 4/5; 17 Apr Ayr Hurdle 21.4f Soft PU/11; 15 Nov Cheltenham Chase 16f Good PU/9
    DATA for: Has won at this trip or further
    DATA against: Pulled up in 2 of its last 5 jumps runs
