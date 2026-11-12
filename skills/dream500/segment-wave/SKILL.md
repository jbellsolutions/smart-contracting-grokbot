---
name: segment-wave
description: Build a partner segment's list and its wave, then send an approved wave a few at a time. Load for Dream 500 wave prep and drafts.
---

# segment-wave

Role: dream500. Every step runs inside the gates in `repo/GATES.md` and the guards in `repo/guards/SKILL.md`.

1. Segments in order: property managers, real-estate offices, building inspectors, conveyancing lawyers, insurance assessors and loss adjusters, body corporates and retirement villages.
2. Build the list with the partner-score steps. 25 to 50 rows per wave.
3. The wave item: `TO: data/partners/dream500/<segment>.csv sha256=<sum> count=<n>`, five sample rows in WHY, and the first email and two follow-ups from `repo/kit/campaigns/<type>.md`, rewritten as a cold first touch (no fee, no price), with an unsubscribe line ("Reply 'no thanks' and we won't email again").
4. Every row's personal first line goes in the list's `first_line` column **before** the list is hashed, so Jesse's yes covers it. The five sample rows show theirs.
5. After the wave's yes, the weekday routine writes one "today's batch" item: the next 10 rows plus any follow-ups due. It doesn't send.
6. On Jesse's yes to the batch, in chat: gate each row with `approval.py gate <wave item> --row <email>` (it recomputes the list's sha256 and checks the row is on it), send, and record with `approval.py sent <wave item> sent --row <email>`, two minutes apart.
7. A rebuilt or changed list is a new wave item that needs a new yes. The gate holds anything else.
