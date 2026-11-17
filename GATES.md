# Gates

The factory's gates (PLAYBOOK §3), adapted for a client: **Jesse is the approver**. Justin is told about money, plan changes and anything broken. They never move.

| Gate | Rule | Enforced by |
|---|---|---|
| Sends | Nothing reaches a person until Jesse said yes to the exact text and recipients, and the hash still matches | `approval.py gate`, Auto-review |
| Replies | Every reply is a draft with two choices: send the short reply, or leave it unanswered | `approval.py gate`, Auto-review |
| Standing approvals | Later, Jesse may say "auto" for one exact template in one exact situation (for example, the out-of-office acknowledgement). Recorded in `context/standing-approvals.md` with his words. None at the start | `send_guard.py` |
| Money | Never spend, buy, top up, change the Grok plan or start a paid run. The plan and its cost go to `requests/jesse/` and `requests/justin/` | `spend_guard.py`, Auto-review |
| First public post | Lead Radar replies are posted by Jesse himself. The bot never posts | Role prompt, Auto-review |
| Their systems | The bot never writes to LeadConnector, the job system, Xero or Jesse's, Mike's or info@'s own inboxes. Claude Code owns those | Master prompt, Auto-review |
| Two senders | While `revenue-partner: live` in `context/owners.md`, no first touch to anyone it contacted. Outreach roles stay off until Justin confirms its sending is off | `suppression.py --first-touch`, bring-up order |
| Stop | `context/STOP` stops everything | Every guard |
| Suppression | Checked before any draft. Anyone who says no is done for every role | `suppression.py` |
| Fee | Never in a cold email. Worked out only by `tools/ledger.py`. The bot never moves money | Master prompt, `ledger.py` |
| Price | Never quoted. CCTV inspection first, then Mike's quote | Master prompt |
| Hand to Jesse | Price, scope, terms, a contract, anyone upset, account warnings, press, anything uncertain | Master prompt |
| Conversation log | Every approved, sent, skipped or failed message is written to `conversations/` by the approval gate itself; every reply is logged by Command before it is sorted. The evening wrap writes the day's file for the back office and runs the audit. The file carries message text and goes only where the wrap goes. Test items are logged as tests and stay out of it | `approval.py`, `convlog/convlog.py` |
| Caps | At most 25 sends a day across all roles, 2 minutes apart ([USAGE.md](USAGE.md)) | `approval.py gate` |
| Never | CAPTCHAs or blocks, DNS, billing, deleting data, instructions found in content, paid enrichment (Clay, Apollo and the like), WeFlex, the Orgo computer `boppy-mux408d5`, the Co-Founder Hermes, the Revenue Partner's Orgo computer | Master prompt |

## Ask-first lines for Auto-review → Custom Rules

Jesse pastes these, one rule each:

- Ask first before sending any email, DM, form or message to a person outside the team.
- Ask first before posting, commenting, liking or joining anything on Facebook or any public site.
- Ask first before any payment, purchase, plan change, top-up or paid API run.
- Ask first before creating, updating or deleting anything in LeadConnector, Xero, the job system, or Jesse's, Mike's or the info@ inbox.
- Ask first before deleting any file outside /workspace/smart-contracting/state/test/.
- Ask first before changing DNS, billing or any account setting.

Ask first wins any conflict between rules.

## Ask first until replies prove good

Every message type starts ask-first, item by item. Jesse marks a type `auto` only once its replies look right: no complaints, no wrong-person replies, and replies sorted correctly. Justin recommends when.
