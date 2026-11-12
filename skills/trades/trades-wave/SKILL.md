---
name: trades-wave
description: Build the top ten of each trade and run the trades waves. Load for the trades list build and trades drafts.
---

# trades-wave

Role: trades. Every step runs inside the gates in `repo/GATES.md` and the guards in `repo/guards/SKILL.md`.

1. Trades in `repo/kit/partner-types.md` (second tier): plumbers who don't do drainlaying, electricians, builders and renovators, roofers, landscapers, concrete and paving, and pest and moisture firms.
2. Top ten per trade by rubric score, from public sources. Owner-operators first.
3. The wave works the same as segment-wave, with the body from `repo/kit/campaigns/trades.md` rewritten as a cold first touch: "you're already in older homes every day; when you spot a drain issue, send them our way and we look after them".
4. Signed tradies go into the ledger (`tools/ledger.py add-partner`) and get the welcome email from `repo/kit/emails.md`.
