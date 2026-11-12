---
name: radar-sweep
description: Find Christchurch homeowners asking for drain help in the local groups Jesse is in, and draft a helpful reply he posts himself. Load for the radar sweep or when Jesse says scan.
---

# radar-sweep

Role: radar. Every step runs inside the gates in `repo/GATES.md` and the guards in `repo/guards/SKILL.md`.

1. Groups: `repo/kit/radar/groups.md` (only ones Jesse is already a member of, via his login in the bot's browser). Searches and tiers: `repo/kit/radar/searches.md`.
2. Read the last 48 hours. Skip anything already in `data/radar/`.
3. Tier 1: a homeowner with a drain problem now (blocked, smells, sinking ground, a failed inspection, a buyer's report). Tier 2: asking for recommendations, older house, renovation. Leave out the list in searches.md.
4. Reply drafts: answer their question first in plain words, then offer the CCTV inspection, then "Jesse, Smart Contracting" and the office number from `context/owner.md`. Three sentences. Never a price. Never pushy.
5. Item in `approved/pending/radar/` with `TO: <post link>` and `SEND: Jesse posts it himself`. Jesse's "posted" plus the comment link is the proof.
6. Storm watch: MetService Christchurch. A heavy-rain watch or warning means following `repo/kit/radar/storm-day.md`.
7. A login wall, a checkpoint or a CAPTCHA means stop, `requests/jesse/`: "Facebook wants you to sign in again on the bot's browser."
