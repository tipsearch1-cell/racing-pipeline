# RUNBOOK - daily racing pipeline (rebuilt 10 Nov 2026)

Repo: github.com/tipsearch1-cell/racing-pipeline (private). Work in /home/claude/racing-pipeline.
If that folder is missing (workspace reclaimed): add_repo tipsearch1-cell/racing-pipeline with push access, clone it there
(`git clone --depth 1 https://github.com/tipsearch1-cell/racing-pipeline /home/claude/racing-pipeline`, 10-min timeout), register it.
Everything needed for the daily chain is in the repo. raw/ (RBD, RaceIQ, RaceData, odds) is NOT in the main branch: it lives on the
`raw-data` branch (archives + daily files the VPS pushes to daily/raceiq/YYYY-MM-DD/ and daily/racedata/YYYY-MM-DD/).
`bash tools/restore_raw.sh` (re)builds raw/ from it - run it at the start of EVERY build (it also pulls the newest daily files).
Size rules: report/race-reports.html and data/raceiq_runs.csv.gz are rebuilt, never committed; history is stored as monthly
files in data/history/ (only changed months are rewritten). Never commit files > 50 MB to main.

## Hard rules
- Read-only data use; nobody places bets but the user. Racing API only through the MCP tools.
- The LIVE reviewer must be sealed before the first off. Only the LIVE reviewer feeds the bot file.
- Never re-seal a published day. Back up nothing by hand: git is the backup. COMMIT AND PUSH after every build, settle and live check.
- Bot: MB Bot Manager on Matchbook, bet persistence Cancel, matches ~09:30 at the morning price.
  SP below MinPrice does NOT mean unmatched.
- McCoy (VPS agent) cannot see chat files; it polls the artifact https://claude.ai/artifact/53No1yYZoG8wSaf25toxGK.
  Publish report/race-reports.html with files={daily/sealed_card_<DAY>.json, daily/sealed_card_latest.json,
  daily/reviewer_bets_<DAY>.csv, daily/reviewer_bets_latest.csv, daily/multiples_<DAY>.csv, daily/multiples_latest.csv}
  from out/for_vps/. If a publish is refused because a daily/ file changed, read it (action read + path), check it is our
  own earlier file, then republish. If publishing fails, tell the user at once.
- data/live_days.csv says whether a day's bot file was LIVE (published for McCoy) or PAPER.
- Big MCP results are saved to the tool-results folder; pass that saved file path to the scripts.

## Daily build (09:05 UTC)
Order: 0, 1, 1b, 2, 3, 4, 4b, 5, 6. Seal now validates the reviewer output (non-CHECK verdicts ignored, BET re-tested, races
off before the seal excluded; WARNING lines must be read and reported). The bot file refuses to build without SEAL.txt and
drops races off within 5 minutes.
1. Settle yesterday (if not done in the evening): get_results YESTERDAY gb,ire detailed limit 50 (skip 50 if total > 50);
   `python3 pipeline/save_res.py YESTERDAY <saved file(s)>`; `python3 pipeline/card_review.py settle YESTERDAY`.
   BSP often arrives 10:00-12:00 UK or a day late: re-save only when complete (the 12:00 check retries).
0. `bash tools/restore_raw.sh`. It prints the latest RaceIQ / RaceData daily push: if yesterday's is missing, say so in the morning message.
1b. History + models: `python3 pipeline/raceiq.py` (finishing speed from all RaceIQ files in raw/); `python3 pipeline/history.py build <yesterday's saved results file(s) from step 1>` (adds yesterday's runs to
   data/history_runs.csv.gz); after step 2, `python3 pipeline/models.py run DAY` (win model, run styles, shape, pros/cons, h2h ->
   store/DAY/model.json). Retrain only by a dated prereg amendment (prereg/MODEL_REBUILD_2026-11-10.md).
2. Card: get_racecards_pro DAY gb,ire detailed limit 50 (skip 50 if total > 50);
   `python3 pipeline/save_card.py DAY <saved file(s)>` (reports NRs removed, abandoned meetings, first off).
   Publish the sealed card for McCoy straight away.
3. Review: `python3 pipeline/card_review.py prep DAY`; then in ONE message one general-purpose Agent per meeting in
   store/DAY/review/meetings.json (run_in_background false) with this prompt:
   "You are a racing form reviewer. Read ONLY this file: <in path>. Do not open any other file, do not search the web,
   do not use any results. Follow the instructions at the top of that packet exactly: for every race, start from each
   runner's MARKET chance, change only runners where the card gives a specific reason (with a one-line reason), and give
   BET/SKIP verdicts for any runner marked CHECK. Then write your answer as valid JSON (schema in the packet) to <out path>
   using the Write tool. Use the exact race_id and horse_id values from the packet. chance_pct is the new win chance in
   percent. Reply with just done and the number of changes you made."
   Re-run any missing/invalid meeting. `python3 pipeline/card_review.py seal DAY` (refuses after a day is sealed; check
   the seal time is before the first off). `python3 pipeline/reviewer_bets_csv.py DAY`.
4. Publish reviewer bets (+ empty multiples until the multiples are rebuilt) for McCoy; append DAY,LIVE to data/live_days.csv;
   SendUserFile store/DAY/reviewer_bets_DAY.csv and reviewer_bets_detail_DAY.csv; SendUserMessage with a time-ordered table
   (time, course, horse, CHECK BET / value flag, 09:00 median, min price, best 09:00 exchange price), excluded picks, SKIPs,
   and the reminder that the rebuilt reviewer is on trial (small stakes).
4b. Page: `python3 report/build_old_page.py DAY` (old design + recovered 12 Oct - 9 Nov history in report/history_data.json;
   report/build_page.py is the simple fallback) (re-run after settling and after live checks) and publish report/race-reports.html
   to the artifact (daily/ files and archive/race-reports-to-2026-11-09.html are kept when not passed).
5. Live checks: send_later 12:00/14:00/16:00/18:00 UTC (skip any after the last race): get_racecards_pro DAY ...;
   `python3 pipeline/live_changes.py DAY <saved file(s)>`; message the user only for lines marked "!" (important, still to run).
   The 12:00 one also re-fetches yesterday's results for BSP, re-saves when complete and re-runs settle.
6. git add -A; commit; push. Schedule the next day's 09:05 build (same prompt, dates moved on).

## Evening settle (when the user asks "result today's card")
get_results DAY ...; save_res.py; card_review.py settle DAY; report bot-file bets at SP, 09:00 best price and BSP
(BSP usually next day); commit and push.

## Not yet rebuilt (old pipeline, lost 10 Nov)
Rebuilt 10 Nov: win model + early-position/pace model (pipeline/models.py; back-check data/rebuild_vs_old_summary.txt).
Still to do: model-pick tracker/xW tables on the page, feeding model/pace lines into the reviewer packets, SHADOW reviewer, bookmaker multiples, morning favourites, angle flags,
fair-price N1, the full report page. Old results 21 Oct - 9 Nov are kept separately (store/ daily files + FINDINGS/summary).
