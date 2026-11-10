"""Build the daily race-card page: python3 report/build_page.py DAY  -> report/race-reports.html
Reads the sealed card, the reviewer tracker and (when settled) results. Rebuilt 10 Nov 2026.
"""
import html, os, sys
from datetime import datetime, timezone
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "pipeline"))
from common import load_card, race_market, p  # noqa: E402

E = html.escape

CSS = """
/* Layout: one column of race cards in off-time order, a summary strip and the bot-file table first. */
:root{
  --bg:#f3f5f2; --panel:#ffffff; --fg:#18211c; --muted:#5d6b62; --rule:#d9dfd9; --accent:#1f6a4a;
  --up:#1f7a45; --down:#b0392f; --bet:#8a5a00; --betbg:#fff2cf; --chk:#1d4f86; --chkbg:#e3edf9; --skipbg:#eceeec;
  --display:"Barlow Condensed","Arial Narrow",system-ui,sans-serif; --body:"IBM Plex Sans",system-ui,sans-serif;
  --mono:"IBM Plex Mono",ui-monospace,Menlo,monospace;
}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){
  --bg:#111613; --panel:#18201b; --fg:#e4ebe6; --muted:#9aa89f; --rule:#2c3630; --accent:#5fc093;
  --up:#5fd08f; --down:#ef8a80; --bet:#f3c565; --betbg:#3a2f12; --chk:#8fb8ef; --chkbg:#1c2b40; --skipbg:#232b26; color-scheme:dark}}
:root[data-theme="dark"]{
  --bg:#111613; --panel:#18201b; --fg:#e4ebe6; --muted:#9aa89f; --rule:#2c3630; --accent:#5fc093;
  --up:#5fd08f; --down:#ef8a80; --bet:#f3c565; --betbg:#3a2f12; --chk:#8fb8ef; --chkbg:#1c2b40; --skipbg:#232b26; color-scheme:dark}
body{background:var(--bg);color:var(--fg);font-family:var(--body);font-size:14px;line-height:1.45}
.wrap{max-width:1080px;margin:0 auto;padding-block:20px 48px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));display:grid;gap:22px}
h1,h2,h3{font-family:var(--display);font-weight:600;letter-spacing:.01em;text-wrap:balance;margin:0}
h1{font-size:2.3rem;line-height:1.05}
h2{font-size:1.45rem}
.eyebrow{font-size:.75rem;text-transform:uppercase;letter-spacing:.08em;color:var(--muted)}
.status{display:inline-block;font-family:var(--display);font-size:1rem;letter-spacing:.06em;padding:2px 10px;border-radius:4px;border:1.5px solid currentColor}
.status.paper{color:var(--muted)} .status.live{color:var(--accent)}
header{display:grid;gap:8px}
.meta{color:var(--muted);display:flex;flex-wrap:wrap;gap:4px 16px}
.strip{display:flex;flex-wrap:wrap;gap:8px 28px;border-block:1px solid var(--rule);padding-block:10px}
.strip div{display:grid} .strip b{font-family:var(--display);font-size:1.6rem;font-weight:600;line-height:1}
.strip span{font-size:.75rem;color:var(--muted);text-transform:uppercase;letter-spacing:.06em}
.note{color:var(--muted);max-width:70ch;margin:0}
.scroll{overflow-x:auto;min-width:0}
table{border-collapse:collapse;width:100%;font-variant-numeric:tabular-nums}
th{font-size:.72rem;text-transform:uppercase;letter-spacing:.06em;color:var(--muted);text-align:left;font-weight:600;padding:6px 8px;border-bottom:1px solid var(--rule);white-space:nowrap}
td{padding:6px 8px;border-bottom:1px solid var(--rule);vertical-align:top}
td.n{text-align:right;font-family:var(--mono);font-size:.85rem;white-space:nowrap}
th.n{text-align:right}
.race{background:var(--panel);border:1px solid var(--rule);border-radius:6px;display:grid;gap:8px;padding:14px 14px 6px}
.race-h{display:flex;flex-wrap:wrap;align-items:baseline;gap:4px 14px}
.race-h .t{font-family:var(--display);font-size:1.6rem;font-weight:600;line-height:1}
.race-h .c{font-family:var(--display);font-size:1.3rem}
.race .sub{color:var(--muted);font-size:.85rem}
.horse{font-weight:600}
.small{font-size:.8rem;color:var(--muted)}
.reason{font-size:.82rem;color:var(--muted);margin-top:2px;max-width:60ch}
.up{color:var(--up)} .down{color:var(--down)}
.tag{display:inline-block;font-size:.7rem;font-weight:600;letter-spacing:.05em;text-transform:uppercase;padding:1px 6px;border-radius:3px;margin-left:6px;white-space:nowrap}
.tag.bet{background:var(--betbg);color:var(--bet)} .tag.chk{background:var(--chkbg);color:var(--chk)} .tag.skip{background:var(--skipbg);color:var(--muted)}
.tag.win{background:var(--accent);color:var(--panel)}
tr.flag td{background:var(--betbg)}
.nr{font-size:.8rem;color:var(--muted)}
.foot{color:var(--muted);font-size:.8rem;border-top:1px solid var(--rule);padding-top:12px;display:grid;gap:4px}
a{color:var(--accent)}
a:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
@media (max-width:640px){h1{font-size:1.9rem} .hide-s{display:none}}
"""


def fnum(x, nd=2):
    return "" if x is None or (isinstance(x, float) and pd.isna(x)) else f"{x:.{nd}f}"


def main(day):
    card = load_card(day)
    t = pd.read_csv(p("data", "card_review_tracker.csv"))
    t = t[t.day == day].set_index(["race_id", "horse_id"])
    ld = p("data", "live_days.csv")
    status = "PAPER"
    if os.path.exists(ld):
        s = pd.read_csv(ld)
        s = s[s.day == day]
        if len(s):
            status = s.status.iloc[-1]
    det_f = p("store", day, f"reviewer_bets_detail_{day}.csv")
    det = pd.read_csv(det_f) if os.path.exists(det_f) else pd.DataFrame()
    seal = open(p("store", day, "review", "SEAL.txt")).read().split(";")[0].replace("sealed ", "") if os.path.exists(p("store", day, "review", "SEAL.txt")) else "not sealed"
    settled = t.pos.notna().any() if len(t) else False
    dt = datetime.strptime(day, "%Y-%m-%d")
    courses = []
    for r in card:
        if r["course"] not in courses:
            courses.append(r["course"])
    nbot = int((det.Status == "BOT FILE").sum()) if len(det) else 0
    nchk = int(t.check.sum()) if len(t) else 0
    nchkbet = int((t.verdict == "BET").sum()) if len(t) else 0
    nchg = int((t.rev.round(1) != t.mkt.round(1)).sum()) if len(t) else 0
    out = [f"""<title>Frankie Race Card</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;600&family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;600&display=swap">
<style>{CSS}</style>
<div class="wrap">
<header>
  <div class="eyebrow">GB &amp; IRE racing · reviewer card</div>
  <h1>{dt:%A %-d %B %Y}</h1>
  <div class="meta"><span class="status {status.lower()}">{E(status)}</span><span>{E(' · '.join(courses))}</span>
  <span>Reviewer sealed {E(seal)}</span><span>{'Results settled' if settled else 'Results pending'}</span></div>
</header>
<div class="strip">
  <div><b>{len(card)}</b><span>Races</span></div>
  <div><b>{nbot}</b><span>Bot-file bets</span></div>
  <div><b>{nchkbet}/{nchk}</b><span>CHECK bets</span></div>
  <div><b>{nchg}</b><span>Runners changed</span></div>
</div>
<p class="note">{'These bets are <b>paper only</b> today and were not sent to McCoy.' if status == 'PAPER' else 'These bets were published for McCoy and loaded into BotTips.'}
Market % is the 09:00 sharp-weighted price; Reviewer % is the sealed reviewer chance. This card comes from the rebuilt pipeline (from 10 Nov).</p>
"""]
    if len(det):
        out.append('<section><h2>Bot file</h2><div class="scroll"><table><thead><tr><th>Time</th><th>Course</th><th>Horse</th><th>Type</th>'
                   '<th class="n">09:00 median</th><th class="n">Min price</th><th class="n">Best 09:00</th><th class="n">Reviewer %</th>'
                   + ('<th>Result</th>' if settled else '') + '</tr></thead><tbody>')
        for _, b in det.iterrows():
            res = ""
            if settled:
                m = t[(t.horse == b.SelectionName)]
                if len(m):
                    rr = m.iloc[0]
                    res = f"<td>{E(str(rr.pos))}{' <span class=\"tag win\">won</span>' if str(rr.pos) == '1' else ''} <span class=\"small\">SP {fnum(rr.sp)}</span></td>"
                else:
                    res = "<td></td>"
            typ = "CHECK BET" if "CHECK" in b.Source else "Value flag"
            exc = "" if b.Status == "BOT FILE" else ' <span class="tag skip">excluded</span>'
            out.append(f"<tr><td>{E(b.OffUK)}</td><td>{E(b.Course)}</td><td class='horse'>{E(b.SelectionName)}{exc}</td><td>{typ}</td>"
                       f"<td class='n'>{fnum(b.MorningMedian)}</td><td class='n'>{fnum(b.MinPrice)}</td><td class='n'>{fnum(b.BestPrice9am)}</td>"
                       f"<td class='n'>{fnum(b.ReviewerChancePct, 1)}</td>{res}</tr>")
        out.append("</tbody></table></div></section>")
    out.append("<section style='display:grid;gap:14px'><h2>Races</h2>")
    for r in card:
        mk = race_market(r)
        off = pd.Timestamp(r["off_dt"]).tz_convert("Europe/London").strftime("%H:%M")
        out.append(f"<article class='race' id='r-{E(r['race_id'])}'><div class='race-h'><span class='t'>{off}</span><span class='c'>{E(r['course'])}</span>"
                   f"<span class='sub'>{E(r['race_name'])}</span></div>"
                   f"<div class='sub'>{E(' · '.join(x for x in [r.get('type'), r.get('race_class'), r.get('distance'), 'going ' + (r.get('going') or ''), str(len(r['runners'])) + ' runners'] if x))}</div>")
        out.append("<div class='scroll'><table><thead><tr><th>Horse</th><th class='hide-s'>Form</th><th class='hide-s'>OR</th><th class='hide-s'>Jockey / trainer</th>"
                   "<th class='n'>Median</th><th class='n'>Best ex</th><th class='n'>Market %</th><th class='n'>Reviewer %</th>"
                   + ("<th>Result</th>" if settled else "") + "</tr></thead><tbody>")
        for h in sorted(r["runners"], key=lambda h: -(mk[h["horse_id"]]["mkt"] or 0)):
            key = (r["race_id"], h["horse_id"])
            m = mk[h["horse_id"]]
            row = t.loc[key] if key in t.index else None
            tags, cls, reason, revtxt = "", "", "", ""
            if row is not None:
                d = row.rev - row.mkt
                changed = isinstance(row.reason, str) and bool(row.reason)
                arrow = ("up" if d > 0.4 else ("down" if d < -0.4 else "")) if changed else ""
                revtxt = f"<span class='{arrow}'>{row.rev:.1f}</span>"
                if row.verdict == "BET":
                    tags += "<span class='tag chk'>check bet</span>"
                    cls = "flag"
                elif row.verdict == "SKIP":
                    tags += "<span class='tag skip'>check skip</span>"
                if row.bet:
                    tags += "<span class='tag bet'>value flag</span>"
                    cls = "flag"
                if arrow and isinstance(row.reason, str) and row.reason:
                    reason = f"<div class='reason'>{E(row.reason)}</div>"
            res = ""
            if settled and row is not None:
                res = f"<td>{E(str(row.pos)) if pd.notna(row.pos) else ''}{' <span class=\"tag win\">won</span>' if str(row.pos) == '1' else ''}</td>"
            out.append(f"<tr class='{cls}'><td><span class='horse'>{E(h['horse'])}</span>{tags}{reason}</td>"
                       f"<td class='hide-s n'>{E(h.get('form') or '-')}</td><td class='hide-s n'>{E(str(h.get('ofr') or '-'))}</td>"
                       f"<td class='hide-s small'>{E(h.get('jockey') or '')}<br>{E(h.get('trainer') or '')}</td>"
                       f"<td class='n'>{fnum(m['median'])}</td><td class='n'>{fnum(m['best_ex'])}</td><td class='n'>{fnum(m['mkt'], 1)}</td>"
                       f"<td class='n'>{revtxt}</td>{res}</tr>")
        out.append("</tbody></table></div>")
        if r.get("nr_at_seal"):
            out.append(f"<div class='nr'>Non-runners at seal: {E(', '.join(r['nr_at_seal']))}</div>")
        out.append("</article>")
    out.append("</section><div class='foot'><span>Earlier cards (21 Oct – 9 Nov, original pipeline): "
               "<a href='archive/race-reports-to-2026-11-09.html'>archived report page</a>.</span>"
               f"<span>Built {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC from the rebuilt pipeline.</span></div></div>")
    with open(p("report", "race-reports.html"), "w") as f:
        f.write("\n".join(out))
    print(f"page built for {day}: {len(card)} races, {nbot} bot-file bets, status {status}, settled {settled}")


if __name__ == "__main__":
    main(sys.argv[1])
