# Smart Contracting: the handoff

What Jesse does with Justin on the setup call, then what the bot does on its own. This follows the factory PLAYBOOK and the client-build GrokBot standard, and is modelled on Tommy's TMEC build. Platform facts that aren't verified are flagged *(unverified)*.

## Part 1: Jesse (with Justin on the call)

1. **Account.** Jesse's own Grok account, on the Premium plan he bought on 2026-11-11. One account for Smart Contracting only. The bot never buys or changes a plan.
2. **Desktop app.** Open the Grok desktop app on the office PC. Setup runs in the one-to-one chat there, because approval, secret and sign-in requests only show there.
3. **The bot.** Create one bot named **Smart Contracting**, and pin it. Set Settings → General → Bot → Timezone to **Pacific/Auckland**. If two bots were made by accident, keep one.
4. **The pack: one link.** Paste this one line into the new bot. *(If the bot can't download, attach `smart-contracting.zip` from the same release instead.)*

   > You are Smart Contracting, Jesse and Mike's outreach team. Download https://github.com/jbellsolutions/smart-contracting-grokbot/releases/latest/download/smart-contracting.zip, unpack it into /workspace/smart-contracting/repo/ and follow HANDOFF.md, Part 2, from step 1. Read MASTER-PROMPT.md and CHARTER.md first. Ask me one thing at a time. Nothing sends, posts, spends or writes to a CRM until I say yes in this chat.

5. **owner.md.** When the bot asks, attach the private `owner.md` that Justin DM'd. It holds the partner names, the contacted list and the suppression list.
6. **Auto-review rules.** At Part 2 step 4, paste the Ask-first lines the bot shows into Auto-review → Custom Rules.
7. **Sign-ins.** Through Connect apps, one at a time, when the bot asks: Outlook (Microsoft 365, the partners mailbox), then Slack, then Facebook in the bot's browser. Keys go only through a secure secret card or the hidden prompt with **Take over**. Never paste a key in chat.

## Part 2: the bot

1. **Workspace.** Create `/workspace/smart-contracting/` with these folders:
   - `context/`, `daily/`, `log/`, `approved/`
   - `requests/`, with `lead`, `radar`, `dream100`, `dream500`, `trades`, `jesse` and `justin` inside
   - `approved/pending/<role>/` and `approved/decisions/<role>/` for each role
   - `data/` (mode 600), with `partners/`, `partners/dream500/`, `radar/` and `ledger/` inside
   - `vault/` (Obsidian: `Daily/`, `Weekly/`, `People/`, `Decisions.md`)
   - `state/` and `state/test/`
   - `.secrets/` (mode 700)

   Copy `repo/context-templates/owners.md` and `repo/context-templates/config.json` into `context/`. Write `context/routines-on.md` with all 12 routine names from TRIGGER-MAP.md as `<name>: off`. Also write `context/standing-approvals.md` (empty), `context/spend-approvals.md` (empty) and `context/team-registry.md`. Don't create `context/STOP`. Start `log/setup.md`. Run `python3 repo/tools/check.py` and paste its RESULT line into `log/setup.md`.
2. **Memory and skills.** Save MASTER-PROMPT.md to memory word for word, then each role's "System prompt section" from `roles/`. Save `guards/SKILL.md` and every `skills/<role>/<skill>/SKILL.md` as a private skill ([SKILLS-MAP.md](SKILLS-MAP.md) says which role uses which).
3. **Intake.** Ask Jesse for the three private files Justin DM'd him. Save `owner.md` as `context/owner.md`, `contacted.csv` as `context/contacted.csv` (everyone already emailed, including by the old Revenue Partner) and `suppression.csv` as `context/suppression.csv` (everyone who said no). Then ask, one at a time, only what's still blank:
   - the partners mailbox to send from;
   - the office number for signatures;
   - which local Facebook groups he's in (add them to `repo/kit/radar/groups.md`'s list in `context/radar-groups.md`);
   - whether the 5% is before or after GST. If it's not decided, leave `fee_gst_basis` as `unset`.

   Tell Jesse in one line what you already know about the business, so he sees you're ready.
4. **Approval rules.** Show Jesse the Ask-first lines from GATES.md to paste.
5. **Connect, read-only, one at a time.** Each connection gets a Check that reads one real record into `log/setup.md`.

   | App | Roles | Check |
   |---|---|---|
   | Microsoft 365 (Outlook), the partners mailbox | lead, dream100, dream500, trades | The newest message's subject and date |
   | Slack #mike-and-jesse-drainage | lead | The last message's date (not its text) |
   | Facebook, Jesse's login in the bot's browser | radar | The name of one group from the list |
   | Verifalia (optional, free tier) | dream100, dream500, trades | Credits left today |

6. **The old agent.** The Hermes Revenue Partner on Orgo did this work, and its sending was put on hold. Nobody has confirmed it's fully off. `context/owners.md` says `revenue-partner: live` until Justin confirms. While it does, the outreach roles stay `off` or `test`, and first touches skip `contacted.csv`. Never touch that computer. Record this in `log/setup.md`.
7. **Routines, switched off.** Create all 12 routines in TRIGGER-MAP.md, paused, with the exact names. Each prompt starts `Role: <role>.` and names its skill. Record each in `team-registry.md` with its role, cron, time zone and next run. A next run an hour or more off means the time zone isn't set.
8. **Report.** Tell Jesse in five lines what's ready and what isn't, and why. Then offer the test day.

## Usage kit (usage-mastery v1.0.0)

From `grokbot-usage-mastery`. Do these right after the workspace and memory steps.

1. Run `bash repo/usage/scripts/install.sh` (free, pinned, no keys) and paste its last line into `log/setup.md`.
2. Save `repo/usage/SKILL.md` as a private skill named usage-saver.
3. Copy `repo/usage/LEDGER.md` to `log/usage-ledger.md`. Ask Jesse and Mike for the baseline reading (Settings → Usage: % used and reset date) before the first test day, and again after it.
4. The weekly audit (`repo/usage/AUDIT.md`) runs inside the Monday evening report; it adds no routine and changes nothing.
5. Check: `bash repo/usage/scripts/grep_lines.sh 'usage-mastery v' repo/usage/.. 3` prints at least one line (the rules are in place and the scripts run).
6. Show Jesse and Mike the two owner-only steps, once per Grok account, and record the answers in `log/setup.md`:
   - A spending cap: grok.com/dashboard/billing → a monthly additional-usage limit, or Auto top-up off. The bot never changes billing.
   - Three lines for Auto-review → Custom Rules (chat only; routines never wait on approvals):

     ```
     Ask first before opening more than 5 web pages for one task.
     Ask first before starting a sub-agent or a second bot on a job.
     Ask first before re-running a step that has already failed twice.
     ```

## Bring-up order

| # | Role | Why this order | Turned on first |
|---|---|---|---|
| 1 | lead | Reads and asks; sends nothing on its own | Morning list, Evening wrap, Friday scoreboard |
| 2 | radar | Reads and drafts; Jesse posts himself | Radar sweep |
| 3 | lead replies | Replies to threads that are already open | Reply sweep |
| 4 | dream100 | The highest-value emails, 5 a day, each approved | Research, then drafts |
| 5 | trades | Referral partners first, then tradies | Referral campaigns, Trades list build, Trades drafts |
| 6 | dream500 | Volume last, once deliverability looks right | Wave prep, then drafts |

Roles 4 to 6 go `on` only after `revenue-partner: paused` (Justin), and after Jesse sets `live_sends: true` in words ("go live").

## The first-day test run

Every routine is `test` in `context/routines-on.md`, so nothing reaches a person. **Test on a routine does real work**, so the `test` line goes in before every Test press.

| Step | Role | Do | Pass when |
|---|---|---|---|
| 1 | dream100 | Research, then drafts | 5 scored rows with evidence links; 5 items in `approved/pending/dream100/` with hashes; no fee or price in any |
| 2 | dream500 | Wave prep | One segment list, a wave item with sha256, count and samples |
| 3 | trades | Referral campaigns | A next-step item for the newsletter partner |
| 4 | radar | Radar sweep | Posts tiered in `data/radar/`, reply drafts with `Jesse posts it himself` |
| 5 | lead | Morning list | The numbered list in chat, with the whole emails; a copy in Slack |
| 6 | lead | Jesse says "send 1" | `approval.py gate` says `held: live_sends is not true`. Nothing sent |
| 7 | All | Suppression test | A known name from `suppression.csv` is held by every drafting role; one from `contacted.csv` is held as a first touch |
| 8 | All | STOP test | Jesse says "stop everything"; `context/STOP` exists; the next run of every role says stopped; Jesse says "start again" and it's removed |
| 9 | lead | Evening wrap | Every role has a line; the vault note exists; `beat.py status` shows no SILENT; `state/sent.csv` has no `sent` rows |

The day passes when every row passes and nothing was sent. Then Jesse approves the first message of each type, and roles go `on` one at a time in the order above.

## Reporting back

| Where | What | Written by |
|---|---|---|
| The bot's chat | The 7:30 list, replies to approve, call cards | lead |
| Slack #mike-and-jesse-drainage | A copy of the list, alarms, the evening wrap, the Friday scoreboard | lead |
| The workspace vault | `vault/Daily/<date>.md`, `Weekly/`, `People/`, `Decisions.md` | lead writes the daily note; each role adds its section |
| Justin's team | Reads Slack. Anything for Justin goes to `requests/justin/` and the Slack wrap | lead |
