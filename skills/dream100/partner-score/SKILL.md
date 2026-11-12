---
name: partner-score
description: Find and score partner prospects from public sources with the partner rubric. Load when building or refreshing the Dream 100, Dream 500 or trades lists.
---

# partner-score

Role: dream100. Every step runs inside the gates in `repo/GATES.md` and the guards in `repo/guards/SKILL.md`.

1. Sources: the business's own website, its Google listing and reviews, NZ business directories, and professional bodies' public member lists (e.g. building inspectors' associations, REINZ office listings). No paid data, no scraping behind a login.
2. Apply `repo/kit/RUBRIC.md`: hard gates first, then the ten criteria. Each criterion gets its evidence and a link. Unknown is 0.
3. Contact: a published business address for the owner or office (the Act allows published business addresses). Verify with Verifalia's free checks; a bad address is dropped, not guessed.
4. `suppression.py check --first-touch` on the business and the address.
5. Write the row. 75 or more: dream100. 50 to 74: dream500 (by segment). A trade: trades. Three or more unknowns: `data/partners/research-pile.csv`.
