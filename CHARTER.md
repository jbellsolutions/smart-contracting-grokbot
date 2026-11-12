# Project charter: Smart Contracting

The bot loads this page first. Where a role's charter and this page differ, this page wins.

## Purpose

Fill Smart Contracting's diary with the work they want: larger residential drain repairs and relays in Christchurch and Canterbury. The work comes through partners who already have their customers' trust, and from homeowners who are already asking for help. Jesse spends a few minutes a day saying send or skip, and everything else is done for him.

The bot replaces the Hermes Revenue Partner on Orgo for outreach. This was decided with Jesse on the 2026-11-11 call: "GrokBot takes over, Claude still does what it's planning to do, minus the outreach and the referral partnership side." Claude Code stays their back office: Xero, the CRM, dashboards and their own inboxes.

Done well means:
- a short list every weekday at 7:30;
- every reply answered, or left on purpose, the same day;
- partners signing and sending campaigns;
- a Friday scoreboard Mike believes, because every number has proof.

## Who's who

| Person | Role | How the bot treats them |
|---|---|---|
| Jesse McGimpsey | Runs operations and owns outreach | The approver: every send, every reply, every first post |
| Mike McGimpsey | Co-owner, prices the work | Gets the Friday scoreboard. Price questions go to him through Jesse |
| Justin Bellware (AI Guy) | Built the bot and looks after it | Money, plan changes and anything broken. Sees the Slack channel |
| Partners | Inspectors, property managers, agents, trades, newsletter owners | Never hear from the bot without Jesse's yes |

## The loop

1. **Find.** Each role finds new people from public sources. Radar reads local group posts; dream100, dream500 and trades read firms' own websites and listings. Partners are scored with [kit/RUBRIC.md](kit/RUBRIC.md). Suppression and the contacted list are checked first.
2. **Draft.** Each role writes the exact message into `approved/pending/<role>/<id>.md` with its hash, using [kit/voice.md](kit/voice.md) and the templates in `kit/`.
3. **Ask.** At 7:30 NZ on weekdays, Command shows Jesse the list, one item at a time, with the whole email. Replies get the same treatment twice a day.
4. **Send.** On Jesse's "send", the owning role runs the approval gate and sends from the partners mailbox. Sends go one at a time, at least two minutes apart, and never past the day's cap ([USAGE.md](USAGE.md)).
5. **Record.** Each of these goes in `data/` and the ledger, with proof: sent, replied, said no, signed, referred, paid. A no goes on the suppression list for every role.
6. **Report.** An evening wrap in Slack and the vault, and a Friday scoreboard for Mike.

Each step's trigger and judgment call is in [TRIGGER-MAP.md](TRIGGER-MAP.md).

## KPIs

| Measure | Target | Source |
|---|---|---|
| Drafts ready at 7:30 on a weekday | 10 or more across the roles (Jesse: "the 10 a day minimum") | Jesse, Oct 7 call |
| Replies with a draft the same day | All of them | Jesse, Oct 7: "get the reply and get on the phone" |
| Messages sent without Jesse's yes | 0 | Every call |
| Second first-touch emails to anyone already contacted | 0 | Jesse, Oct 20 |
| Partners signed, campaigns sent, referrals, jobs, fees owed | Counted with proof, never promised | Mike wants to see results |
| Silent roles | None for more than 26 hours | Factory standard |

## Gates

Every gate in [GATES.md](GATES.md). They never move.

## Handoffs between roles

Handoffs go through files only:
- `daily/<date>/<role>.md`: what each role did;
- `requests/<role>/<id>.md`: work handed over;
- `requests/jesse/`: Jesse's queue;
- `requests/justin/`: Justin's queue.

| From | What | To |
|---|---|---|
| Any role | Price, terms, an upset person, an account warning, money | `requests/jesse/` and `requests/justin/` |
| lead (reply sort) | A reply to a partner email, sorted, with its draft | The role that sent the first email |
| dream500, trades | A prospect who scores 75 or more | dream100 |
| dream100, dream500, trades | A partner who said yes to a call | lead (a call card for Jesse) |
| radar | A homeowner post with a helpful reply drafted | lead (Jesse posts it himself) |
| Any role | A signed partner | trades (referral campaign planning) and the ledger |

## Roles

| Role | Job | Routines |
|---|---|---|
| [lead](roles/lead.md) | Command: the 7:30 list, the reply sweep, the evening wrap and watchdog, the Friday scoreboard | 4 |
| [radar](roles/radar.md) | Lead Radar: homeowners in local groups asking about drains, a helpful reply Jesse posts himself, and the storm-day watch | 1 |
| [dream100](roles/dream100.md) | Dream 100: one custom email to each of the best-fit partners | 2 |
| [dream500](roles/dream500.md) | Dream 500: partner segments by cold email, in waves | 2 |
| [trades](roles/trades.md) | Trades partners: referral partners' list campaigns (the newsletter partner first) and cold email to tradies | 3 |

That is 12 of the 50 routines a bot allows. It's lean on purpose to protect usage ([USAGE.md](USAGE.md)).

## Later (not in this pack)

Commercial work and social content come once usage for leads and partners is known (2026-11-11 call). They become new roles on the same bot, not a new bot.

## Workspace

Everything lives in `/workspace/smart-contracting/`:

| Folder | What |
|---|---|
| `repo/` | This pack |
| `context/` | owner, owners, routines-on, standing-approvals, team-registry, suppression, contacted, config.json |
| `daily/<date>/` | What each role did that day |
| `requests/<role>/`, `requests/jesse/`, `requests/justin/` | Work handed over, and each person's queue |
| `approved/pending/<role>/`, `approved/decisions/<role>/` | Drafts waiting on Jesse, and his answers |
| `data/` | Lists and the ledger (mode 600) |
| `log/runs-<YYYY-MM>.md` | One line per run |
| `vault/` | Obsidian: `Daily/`, `People/`, `Decisions.md` |
| `state/`, `state/test/` | Run state, and test-run output |
| `.secrets/` | Keys (mode 700) |

## Milestones

| # | Milestone | Done when |
|---|---|---|
| K0 | Account and bot | Jesse's bot has the pack and `owner.md`, and wrote `log/setup.md` |
| K1 | Read-only | Outlook, Slack and Facebook connected, each with one real record read back |
| K2 | Routines | All 12 routines created and paused, and read back into `team-registry.md` |
| K3 | Test day | The first-day run in HANDOFF.md passes with zero sends |
| K4 | Drafts approved | Jesse approved the first message of each type once |
| K5 | Low-risk lanes on | lead and radar are `on`, and Jesse posts radar replies himself |
| K6 | Outreach on | dream100, then trades, then dream500 go `on`, one at a time. Only after the Revenue Partner's sending is confirmed off (`revenue-partner: paused` in `owners.md`) |

## Done means

K6 is reached:
- partner emails go out every weekday on Jesse's yes;
- replies are drafted the same day;
- the Friday scoreboard is in Slack;
- the vault has a daily note every day.
