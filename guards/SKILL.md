---
name: bot-guards
description: The checks every role runs in code before it drafts, sends or spends, and the heartbeat it writes at the end. Load on every run.
---

# Guards

These are code, not advice. Run them; don't reason around them. Paths are relative to the workspace.

| Before you | Run | It answers |
|---|---|---|
| Draft to anyone | `python3 repo/guards/scripts/suppression.py check "<name, business, email or url>"` | `clear` or `held`. Held means stop on that person |
| First email to anyone | `python3 repo/guards/scripts/suppression.py check --first-touch "<business and email>"` | Also held if they were already emailed, by this bot or the old Revenue Partner |
| Someone says no | `python3 repo/guards/scripts/suppression.py add "<who>" "<reason>"` | Done for every role |
| Queue a draft for Jesse | write `approved/pending/<role>/<id>.md`, then `python3 repo/guards/scripts/approval.py hash <item>` into its `HASH:` line | The hash Jesse's yes is tied to |
| Record Jesse's answer (lead only) | `python3 repo/guards/scripts/approval.py decide <item> yes\|no\|change "<his exact words>"` | Only after showing him the whole payload |
| Send anything | `python3 repo/guards/scripts/approval.py gate <item> [--row <recipient>]` | `clear` or `held: <why>`. Held means don't send; write why in your daily note |
| After sending | `python3 repo/guards/scripts/approval.py sent <item> sent [--row <recipient>]` | Never handled twice; counts toward the daily cap |
| A standing template (later) | `python3 repo/guards/scripts/send_guard.py <message-type> --routine <NAME>` | `auto` only for a type Jesse marked auto |
| Spend anything | `python3 repo/guards/scripts/spend_guard.py <plan-id> <usd>` | `approved` or `held`. Held means the plan and its cost go to `requests/jesse/` |
| End a run | `python3 repo/guards/scripts/beat.py write <role> '<line>' found=N drafted=N sent=N` | Your heartbeat. The watchdog alarms on a silent role |
| Watchdog | `python3 repo/guards/scripts/beat.py status --hours 26` | `SILENT <role>` lines to alarm on |

Never print the suppression list, read `.secrets/`, or edit a guard or a switch file to get past it.
