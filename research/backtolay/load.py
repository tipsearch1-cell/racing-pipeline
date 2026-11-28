"""Load the RBD results archive into one clean parquet (research/backtolay)."""
import glob, numpy as np, pandas as pd
ROOT = "/home/claude/racing-pipeline/raw/rbd_results"
NUM = ["Distance","Class","Stall","Official Rating","Age","Pace","Weight","Industry SP","Betfair SP","IP Min","IP Max","Pre Min","Pre Max",
       "Forecasted Odds","Place","Runners","Runs last 18 months","Wins Last 5 races","Avg % SP Drop Last 5 races","Avg % SP Drop last 18 mths",
       "RBD Rating","RBD Rank","Total Prev Races","Days Since Last time out","Course Wins","Distance Wins","Class Wins","Going Wins",
       "Last time out Position","% BSP reduction","Betfair Rank"]
def load():
    d = pd.concat([pd.read_csv(f, low_memory=False) for f in sorted(glob.glob(f"{ROOT}/*/*.csv"))], ignore_index=True)
    d["Distance_raw"] = d["Distance"].astype(str); d["Weight_raw"] = d["Weight"].astype(str)
    for c in NUM:
        if c in d: d[c] = pd.to_numeric(d[c], errors="coerce")
    d["date"] = pd.to_datetime(d["Date of Race"], errors="coerce", dayfirst=False)
    d = d[(d["Betfair SP"] > 1.01) & (d["IP Min"] >= 1.01) & (d["IP Max"] >= 1.01)].copy()
    d["race"] = d["Date of Race"].astype(str) + "|" + d.Track.astype(str) + "|" + d.Time.astype(str)
    d["won"] = (d.Place == 1).astype(int)
    d = d.sort_values(["date", "Time"]).reset_index(drop=True)
    return d
if __name__ == "__main__":
    d = load(); d.to_pickle("/tmp/claude-0/-home-claude/cd2f780b-543c-598d-8d36-a8da908aed77/scratchpad/rbd.pkl")
    print(len(d), d.date.min(), d.date.max(), d.race.nunique(), "races"); print(d.Type.value_counts().head(8).to_dict())
