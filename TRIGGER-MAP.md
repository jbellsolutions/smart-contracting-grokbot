# Trigger map

Schedules start every step, scripts move the data and run the gates, and the agent makes only the judgment call. Every send stays ask-first. **The bot's time zone is Pacific/Auckland**, so every cron below is NZ time and follows daylight saving on its own. 50 routines max per bot; this bot uses 12. `tools/check.py` counts the cron rows below.

## The loop, step by step

| # | Step | Started by | Role | Judgment call | Human gate |
|---|---|---|---|---|---|
| 1 | Research partners | Schedule (Mon, Tue, Wed) | dream100, dream500, trades | Is this a fit? Rubric score with evidence | None (research only) |
| 2 | Find homeowners asking | Schedule `15 6 * * 1-6` | radar | Tier the post; is it the work they want? | None |
| 3 | Draft | Schedule (weekdays 06:00 to 06:45) | dream100, dream500, trades, radar | The first line, the angle, the reply | None: drafts only |
| 4 | Ask | Schedule `30 7 * * 1-5` | lead | Order the list, most valuable first | **Jesse:** send, skip or change, per item |
| 5 | Send | Jesse's "send" in chat (never inside a routine) | The owning role | None: `approval.py gate` decides | Jesse's yes plus the hash check (text, and the list file for waves) |
| 6 | Sort replies | Schedule `0 10,14 * * 1-5` | lead | What the reply means, and the short answer | **Jesse:** send the short reply, or leave it unanswered |
| 7 | Referral campaigns | Schedule `0 9 * * 2` | trades | The partner's next step | **Jesse**, then **the partner** |
| 8 | Wrap and watchdog | Schedule `0 17 * * 1-5` | lead | Proof check on each number | None |
| 9 | Scoreboard | Schedule `0 15 * * 5` | lead | Proof check | None |

## Every schedule, by role

### lead

| Kind | When or what | Does |
|---|---|---|
| Schedule | `30 7 * * 1-5` | SC Morning list: the numbered approval list, in chat and copied to Slack |
| Schedule | `0 10,14 * * 1-5` | SC Reply sweep: sort replies, draft each, call cards |
| Schedule | `0 17 * * 1-5` | SC Evening wrap: watchdog, the wrap in Slack, the vault daily note |
| Schedule | `0 15 * * 5` | SC Friday scoreboard for Mike |

### radar

| Kind | When or what | Does |
|---|---|---|
| Schedule | `15 6 * * 1-6` | SC Radar sweep: group posts, reply drafts, storm watch |

### dream100

| Kind | When or what | Does |
|---|---|---|
| Schedule | `0 5 * * 1,3` | SC Dream 100 research: keep the list at 100, scored |
| Schedule | `0 6 * * 1-5` | SC Dream 100 drafts: 5 first emails, plus follow-ups due |

### dream500

| Kind | When or what | Does |
|---|---|---|
| Schedule | `0 5 * * 2` | SC Dream 500 wave prep: next segment's list and wave item |
| Schedule | `30 6 * * 1-5` | SC Dream 500 batch: today's 10 rows of an approved wave, as one item for the 7:30 list (no sends) |

### trades

| Kind | When or what | Does |
|---|---|---|
| Schedule | `0 9 * * 2` | SC Referral campaigns: each referral partner's next step |
| Schedule | `30 5 * * 3` | SC Trades list build: top ten per trade, scored |
| Schedule | `45 6 * * 1-5` | SC Trades batch: today's 10 rows of an approved wave, as one item for the 7:30 list (no sends) |

## In chat (no routine)

| Jesse says | Role | What happens |
|---|---|---|
| "send 1", "skip 2", "change 3: …" | lead, then the owning role | Decision recorded with his words; yeses sent through the gate, two minutes apart |
| "stop everything" | any | `context/STOP` is created. Nothing sends until he says "start again" |
| "slow down" or "we're flat out" | lead | `capacity: full` in `config.json`: radar logs tier 1 only, and outreach drafts halve |
| "how's it going?" | lead | This week's scoreboard so far, proof only |
