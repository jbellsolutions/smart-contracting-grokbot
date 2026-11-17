# Smart Contracting's outreach team on Grok Bot

One bot to talk to, four lanes doing the work. Built for Jesse and Mike McGimpsey at Smart Contracting Ltd (residential drainage, Christchurch and Canterbury) by Justin's team. It replaces the Hermes Revenue Partner for outreach; Claude Code stays the back office (Xero, CRM, dashboards, their own inboxes).

Jesse talks to **Smart Contracting**. Every weekday at 7:30 it shows him a short, numbered list with the whole email for each, and he answers "send 1" or "skip 2". Every reply comes back as a draft: send the short reply, or leave it unanswered. Nothing goes out without his yes.

| Lane (role) | What it does |
|---|---|
| **Command** (`lead`) | The 7:30 list, the reply sweep, call cards, the evening wrap, the Friday scoreboard for Mike |
| **Lead Radar** (`radar`) | Finds Christchurch homeowners asking about drains in the groups Jesse's in; drafts a helpful reply he posts himself; watches for storm days |
| **Dream 100** (`dream100`) | One custom email to each of the 100 best-fit partners: inspectors, property managers, real-estate offices, the best trades |
| **Dream 500** (`dream500`) | Partner segments by cold email, in waves Jesse approves |
| **Trades partners** (`trades`) | Referral partners' list campaigns (the newsletter partner first) and cold email to the top tradies |

The partner offer, in Jesse's words: **5% of the job value, paid once the customer's invoice is settled in full**. It's never in a cold email.

## Install

1. Open the **Grok** desktop app → **New chat (+)** → **Create new Bot**, name it **Smart Contracting**, time zone Pacific/Auckland.
2. Send:

   ```
   You are Smart Contracting, Jesse and Mike's outreach team. Download https://github.com/jbellsolutions/smart-contracting-grokbot/releases/latest/download/smart-contracting.zip, unpack it into /workspace/smart-contracting/repo/ and follow HANDOFF.md, Part 2, from step 1. Read MASTER-PROMPT.md and CHARTER.md first. Ask me one thing at a time. Nothing sends, posts, spends or writes to a CRM until I say yes in this chat.
   ```

3. Answer its questions; it walks you through every click. Full steps: [HANDOFF.md](HANDOFF.md). Everything is created **paused**.

## What's inside

New in v1.1.0: the conversation log (`convlog/`). Every message the bot drafts, sends or receives is written down once, and the evening wrap carries the day's file. A bot that already holds v1.0.0: [UPGRADE.md](UPGRADE.md).

| Path | What |
|---|---|
| [HANDOFF.md](HANDOFF.md) | The install: Jesse's steps, then the bot's, the bring-up order and the test day |
| [MASTER-PROMPT.md](MASTER-PROMPT.md) | Who the bot is and the gates that never move |
| [CHARTER.md](CHARTER.md) | Purpose, the loop, KPIs, handoffs, workspace, milestones |
| [roles/](roles/) | One charter per lane, each with a system prompt section |
| [TRIGGER-MAP.md](TRIGGER-MAP.md) | The 12 routines (NZ time) and what Jesse says in chat |
| [GATES.md](GATES.md) | The gates, and the Ask-first lines for Auto-review |
| [USAGE.md](USAGE.md) | The usage budget for Premium |
| [kit/](kit/README.md) | The partner programme: rubric, partner types, terms, voice, scripts, campaigns, one-pagers, NZ compliance, radar |
| [guards/](guards/SKILL.md) | Guard scripts: approval (hash-checked yes), suppression, send, spend, heartbeat |
| [skills/](skills/), [SKILLS-MAP.md](SKILLS-MAP.md), [skills.json](skills.json) | How each job is done |
| `tools/ledger.py` | Partner IDs, referrals and fees (never in the bot's head) |
| `tools/check.py` | Completeness and secret check |
| `context-templates/` | Starting switch files, and the shape of the private owner.md |
| [NEEDS-JUSTIN.md](NEEDS-JUSTIN.md) | What only Justin or Jesse can do |

## How it stays safe

- **One send gate, in code.** `approval.py gate` checks all of these before anything goes out: no stop file, live sends on, Jesse said yes to this exact text and these recipients (hash-checked), it hasn't already been sent, and it's under the daily cap.
- **Stop everything.** Say "stop everything" to the bot.
- **NZ rules.** The Unsolicited Electronic Messages Act and the Privacy Act: [kit/compliance-nz.md](kit/compliance-nz.md).
- **No paid data.** Public sources only.
