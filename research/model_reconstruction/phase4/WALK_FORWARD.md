# Phase 4 - chronological walk-forward and evidence grading

**Protocol:**
- **Independent models:** expanding monthly windows. Trained on all history races before the 1st of the test month (from 1 Jan 2026). Early stopping and L2 chosen on the last training month only.
- **Market-anchored models:** trained on earlier evaluation months (from Mar 2026). Nothing is fitted on a test month.
- Every runner in a race stays in the same split.
- Model selection was frozen in the sealed spec before scoring. Amendment 1 was added before any shadow data existed.

| Evidence grade | Period | Races | Status |
|---|---|---|---|
| Development (selection) | May - Aug 2026 replay | 4,761 | Used to choose. Results are optimistic by construction. |
| Chronological replay, **re-used** | Sep - 12 Oct 2026 | 1,623 | Examined in Phases 2-3. Diagnostic only. |
| Chronological replay, **re-used** | H3 26 Oct - 18 Nov 2026 | 674 | Examined in Phase 3. Diagnostic only. |
| Verified forward predictions of the *candidates* | none | 0 | Candidates did not exist before today |
| **Genuinely untouched** | **from 20 Nov 2026 (prospective shadow)** | 0 so far | **The only valid test** |

**No unused historical holdout exists.** Every 2026 period with a 09:00 market has now been looked at. So no historical result in this phase is independent evidence, and none is presented as such.

**Prospective shadow test, set up today:**
- **Frozen models:** research/model_reconstruction/phase4/models/frozen_2026-11-19.pkl
  - sha256 56179d9c…7178b52;
  - D2 has 83 trees; C has 142 trees; E weights 1.079 / 0.044 / 0.059;
  - trained on history before 19 Nov.
- **Daily:** after the bot file is published, `shadow.py predict DAY` writes D2 and E probabilities for every race into the forward archive (write-once, chained-hash manifest). The tomorrow (20 Nov) build is set to run it and commit before the first off, and to carry it forward each day.
- **Pass (spec + Amendment 1):** after ≥ 1,000 settled races, the lower bound of the paired log-loss gain vs the 09:00 market must be > 0. Day-block interval, Bonferroni over 2 models (97.5%).
- **Expected duration:** about 35 GB/IRE races a day, so roughly 4-5 weeks.
- A dry run on 18 Nov's card produced 31 races, 344 runners, and race sums of 1 ± 2e-6. It was written to a temp folder, not the archive.

**Repeated-research caveat:** this is the fourth phase on the same 2026 replay. Any small positive historical effect (E +0.003) carries real selection risk. It counts only if it reappears in the shadow test.
