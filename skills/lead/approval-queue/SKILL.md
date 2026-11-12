---
name: approval-queue
description: Show Jesse what's waiting for his yes, one item at a time, and record his answers. Load for the 7:30 morning list and whenever Jesse says send, skip or change.
---

# approval-queue

Role: lead. Every step runs inside the gates in `repo/GATES.md` and the guards in `repo/guards/SKILL.md`.

1. List every `approved/pending/*/<id>.md` with no file in `approved/decisions/<role>/<id>.md`. Recompute each HASH with `approval.py hash`; a mismatch means the role rewrote it: close it as `superseded` and tell that role.
2. A wave's "today's batch" counts as one item: show the wave's approved email once, then the 10 recipients with their first lines.
3. Order: replies first, then dream100, trades, dream500, radar. At most 15 a morning; the rest wait for tomorrow.
4. Show each one on its own, numbered: who it goes to (or the list count with five sample rows), why (one line), and **the whole email** exactly as it will go. No summaries of the text.
5. End with one line: `Reply "send 1", "skip 2" or "change 3: what to change". Nothing goes until you say.`
6. Copy the numbered list (recipients and subject only) to Slack #mike-and-jesse-drainage so Justin and Mike can see what's waiting.
7. When Jesse answers: `approval.py decide <item> yes|no|change "<his exact words>"`. A change is redrafted once by the owning role as a new id. A skip is recorded as `no`.
8. Hand each yes to the owning role in chat now (it sends through `approval.py gate`). If an Auto-review prompt appears, that is Jesse's second check: he approves it there too.
9. A routine run only shows the list and stops. It never waits for an answer.
