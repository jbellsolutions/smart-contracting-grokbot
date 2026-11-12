# Usage budget

Jesse is on Grok **Premium**. Justin's word on the 2026-11-11 call: start lean with lead generation and emails, watch usage, and bump the plan only if it earns it. The bot never changes the plan.

## The budget

| Lever | Setting | Why |
|---|---|---|
| Routines | 12 of 50 | Each run costs usage. No hourly watchdog: the evening wrap does it |
| Quiet runs | End with `[SILENT]` after checking the switch file | A switched-off routine costs one file read |
| Weekends | Only the Saturday radar sweep | Partners don't read email on Sunday |
| Research | Twice a week for Dream 100, once a week for each wave | Lists don't change daily |
| Drafts a weekday | Dream 100: 5. Dream 500: 10. Trades: 10. Radar: whatever's found | About Jesse's "10 a day minimum", without burying him |
| Sends a day | 25 at most across every role, 2 minutes apart, from the partners mailbox | Protects the domain and Jesse's attention |
| Replies | Swept twice a weekday, not every 30 minutes | Same-day answers at a quarter of the runs |
| Verifalia | Free tier only (about 25 checks a day), used every weekday | Jesse: use every free check |
| Pages read | Only the firm's own site and its Google listing per prospect; no crawling | The biggest single cost |
| Model | The plan's default. Never a "heavy" or paid model for routine runs | Usage |

## When to turn it up

These are measured at the test day and in the first full week. The bot writes each run's usage line into `log/runs-<YYYY-MM>.md` where the platform shows it.

| Signal | Then |
|---|---|
| Plenty of headroom and replies converting | Justin proposes more drafts a day, or adds commercial work or social content as a new role |
| Usage near the plan's limit | Halve Dream 500 drafts, then move Trades list build to fortnightly |
| Over the limit | `requests/justin/`: the cost of the next plan, with the evidence. Jesse and Justin decide |

## Savings from the usage-mastery kit (v1.0.0, client edition)

Applied: `usage/` (saver scripts, weekly AUDIT, RESET, LEDGER), the usage rules in MASTER-PROMPT.md, the usage section in HANDOFF.md. What each saving means for this bot:

| Saving | Where it lands here | Expected effect (measure it) |
|---|---|---|
| Read pages through `clean_page.py`, never the full page | Dream 100 research, Dream 500 wave prep, Trades list build (the routine lines in `roles/`) | Pages read is this bot's biggest cost. Measured on a long page: 92% fewer characters |
| Lists answered with `sheet_q.py`, not opened whole | `data/partners/*.csv` once they grow | An answer of a few lines instead of the whole sheet |
| Big JSON replies cut with `pick.py` | Verifalia and any API reply | About 98% fewer characters on a typical reply |
| Schedule already lean | 12 routines, about 47 runs a week, none more often than every 3 hours, no hourly watchdog | Keep it: never add or speed up a routine without Jesse's yes |
| Instructions weight | About 2,750 words re-read every run (master prompt 1,061) | The weekly audit flags duplicate rules; move reference detail to files under `repo/kit/` |
| Weekly audit, report only | Inside the Monday evening wrap; no new routine | Labels routines KEEP / SLOW / EVENT / CHANGE / RETIRE in Jesse's queue |
| Usage ledger | `log/usage-ledger.md`: a reading before the test day and a week after | Turns "When to turn it up" above into numbers |
| Spend cap | Jesse, once: grok.com/dashboard/billing → Auto top-up off, or a monthly extra-usage limit | Premium can't silently run up extra usage |
| Auto-review lines | Jesse pastes the three lines from HANDOFF's usage section | Chat jobs ask before opening more than 5 pages or starting a sub-agent |
