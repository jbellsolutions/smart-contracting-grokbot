---
name: evening-wrap
description: The weekday evening wrap: watchdog, the day's numbers with proof, the Slack post and the vault daily note. Load for the evening routine.
---

# evening-wrap

Role: lead. Every step runs inside the gates in `repo/GATES.md` and the guards in `repo/guards/SKILL.md`.

1. `beat.py status --hours 26`: every SILENT role is an alarm line in Slack.
2. Check `state/sent.csv` against `approved/decisions/`: any send with no yes decision is an alarm, and STOP is created at once.
3. Read every `daily/<date>/<role>.md`. Count found, drafted, sent (with proof only), replies, calls booked.
4. Post to Slack #mike-and-jesse-drainage, five lines at most: what went out, what came back, what's waiting on Jesse, anything broken.
5. Write `vault/Daily/<date>.md`: the same numbers, each role's line, decisions Jesse made today (his words), and links to new `vault/People/` notes for partners who replied.
