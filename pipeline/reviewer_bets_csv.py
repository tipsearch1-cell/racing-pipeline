"""Bot upload file from the sealed LIVE reviewer: python3 pipeline/reviewer_bets_csv.py DAY

CHECK verdict BET  -> MinPrice = 0.95 x 09:00 median (CHECK rule amended 12 Nov: fav, median 3.0-7.0, not marked down)
reviewer value flag -> MinPrice = 100 / reviewer chance
Races with an unraced runner (no form figures; amended 10 Nov) are EXCLUDED from the bot file.
Writes store/DAY/reviewer_bets_DAY.csv (MB Bot Manager format), reviewer_bets_detail_DAY.csv and out/for_vps copies.
"""
import os, shutil, sys
import pandas as pd
from common import p


def main(day):
    if not os.path.exists(p("store", day, "review", "SEAL.txt")):
        sys.exit(f"{day} is not sealed (no SEAL.txt) - no bot file written")
    now = pd.Timestamp.now(tz="UTC")
    df = pd.read_csv(p("data", "card_review_tracker.csv"))
    d = df[(df.day == day) & ((df.verdict == "BET") | (df.bet == True))].copy()
    rows = []
    for _, r in d.sort_values("off_dt").iterrows():
        chk = r.verdict == "BET"
        minp = round(0.95 * r["median"], 2) if chk else round(100 / r.rev, 2)
        rows.append(dict(OffUK=pd.Timestamp(r.off_dt).tz_convert("Europe/London").strftime("%H:%M"), StartTimeUTC=r.off_dt,
                         Course=r.course, SelectionName=r.horse, Code=r.code, Source="CHECK verdict BET" if chk else "reviewer BET flag",
                         MorningMedian=r["median"], MinPrice=minp, BestPrice9am=r.best,
                         Matchbook9am=r.get("mb"), ReviewerChancePct=r.rev, MarketChancePct=r.mkt,
                         Reason=r.reason, Status=("EXCLUDED - unknown runner(s) or off before seal" if r.excluded
                                                     else "EXCLUDED - off within 5 min of file time" if pd.Timestamp(r.off_dt) <= now + pd.Timedelta(minutes=5)
                                                     else "BOT FILE")))
    det = pd.DataFrame(rows, columns=["OffUK", "StartTimeUTC", "Course", "SelectionName", "Code", "Source", "MorningMedian", "MinPrice",
                                      "BestPrice9am", "Matchbook9am", "ReviewerChancePct", "MarketChancePct", "Reason", "Status"])
    sd = p("store", day)
    det.to_csv(os.path.join(sd, f"reviewer_bets_detail_{day}.csv"), index=False)
    bot = det[det.Status == "BOT FILE"]
    out = pd.DataFrame(dict(Provider="Frankie", SelectionName=bot.SelectionName, MarketType="WIN",
                            StartTime=[pd.Timestamp(t).tz_convert("Europe/London").strftime("%Y-%m-%d %H:%M:%S") for t in bot.StartTimeUTC],
                            BetType="BACK", MinPrice=bot.MinPrice, BSP="false", Course=bot.Course, OffUK=bot.OffUK, Code=bot.Code,
                            MorningMedian=bot.MorningMedian))
    f = os.path.join(sd, f"reviewer_bets_{day}.csv")
    out.to_csv(f, index=False)
    os.makedirs(p("out", "for_vps"), exist_ok=True)
    for name in (f"reviewer_bets_{day}.csv", "reviewer_bets_latest.csv"):
        shutil.copy(f, p("out", "for_vps", name))
    exc = det[det.Status != "BOT FILE"].SelectionName.tolist()
    print(f"{f}: {len(out)} reviewer bets ({(bot.Source == 'CHECK verdict BET').sum()} CHECK BET, "
          f"{(bot.Source != 'CHECK verdict BET').sum()} value flags); excluded for unknown runners: {len(exc)} ({', '.join(exc) or 'none'})")


if __name__ == "__main__":
    main(sys.argv[1])
