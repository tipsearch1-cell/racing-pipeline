# Betfair Exchange API status

**Not available. The probability forward test does not need it, and it continues regardless.**

| Item | Finding |
|---|---|
| Research environment | No Betfair app key, session token or certificate in env (checked by variable names only) |
| VPS | Unknown from here. `deploy_vps.sh --check` lists any BETFAIR_*/BF_* variable **names** (never values) for McCoy to report |
| Racing API | One "Betfair Exchange" back price per runner. No lay price, depth, traded volume, market id or market status. These are stored as null (`unavailable_fields`) and never inferred |

**What would be needed** (no account or subscription has been created or bought):
1. A Betfair account with API access.
2. An application key: a delayed key is free but gives delayed data unsuitable for checkpoints; a live key is needed for real-time data.
3. A non-interactive (certificate) login, with the certificate in the VPS's protected storage.
4. Exchange Stream API or `listMarketBook` with EX_BEST_OFFERS and EX_TRADED for GB/IRE WIN markets, polled at the same checkpoints.

**What it would add:** best back and lay prices, depth at three levels, traded volume, market status and suspensions. These are needed for the execution study; they are not needed for the accuracy test.
