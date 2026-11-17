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

## The day's conversation file

At the end of the wrap, from the workspace folder:

```bash
python3 repo/convlog/convlog.py daily --mark
python3 repo/convlog/convlog.py audit
```

The first writes `conversations/daily/<date>.md` and prints its path, two counts and the time zone it used (it must say Pacific/Auckland; if it says UTC, say so at the top of the wrap). The file holds every message drafted, sent or received today (the NZ day, set in `context/config.json`), plus anything earlier not yet handed over, such as a reply that came in after last night's wrap or over the weekend. For a wave it shows the approved template once per person, not each person's own first line.

Put the two counts in the wrap. Then attach the file to the wrap in Slack so the back office has it; the CRM is theirs, and the bot never writes it. The file carries the text of messages, so it goes only in the channel the wrap already goes to. If Slack won't take an attachment, don't retry and don't paste the file's text: give the counts and say the file is at its path in the workspace.

The second must say `audit ok`. If it names a line, put that line at the top of the wrap.
