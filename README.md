# racing-pipeline

Daily GB/IRE racing card, LIVE and SHADOW reviewer, bot file for MB Bot Manager (Matchbook),
bookmaker multiples, paper tests and trackers. Rebuilt from 10 Nov 2026 after the cloud workspace was reclaimed.

Persistence rule: every build and settle ends with a commit + push here, so a reclaimed VM can clone it back.
Large raw data (RBD, RaceIQ, odds history zips) is NOT committed; it is unpacked into raw/ from the chat attachments.

Layout: pipeline/ (scripts), data/ (trackers), store/<day>/ (sealed cards, results, review packets),
prereg/ (sealed test specs + SHA256SUMS.txt), report/ (page builder + page).
