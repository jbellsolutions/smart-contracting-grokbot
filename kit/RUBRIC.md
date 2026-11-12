# Partner rubric: who is worth Jesse's time, and in what order

The partner roles (dream100, dream500 and trades) score every prospect with this rubric before it goes on any list. The score decides the order, never the yes: Jesse approves every first email and every wave.

The question behind it: **who deals with an older Christchurch homeowner before, during or after the moment a drain matters, such as buying, selling, a new tenant, a renovation, a blocked drain or a storm, and looks good when they point that homeowner to Smart Contracting?**

## 1. Hard gates: fail one and the prospect is out

| Gate | Out if | Why |
|---|---|---|
| Not a competitor | They lay, repair or CCTV drains themselves (drainlayers, drain unblockers who also do relays) | They have nothing to recommend. A plumber who doesn't do drainlaying is fine |
| Not the work they don't want | Their customers are mainly new builds, civil, commercial or government | Jesse: larger residential repairs, not new builds or civil work |
| Not a lead seller | They sell shared leads or quotes (quote-comparison sites and the like) | Vendors, not partners |
| Owner can say yes | A franchise or chain run from head office | The local owner usually can't send to the list |
| No opt-out on record | Their site says no unsolicited commercial email, or they're on the suppression list | The Unsolicited Electronic Messages Act. Record the reason |
| In the area | Their customers are outside Christchurch and Canterbury | Two crews; they can't serve them |
| Not already contacted | They're in `context/contacted.csv` (by this bot or the old Revenue Partner) | One first email, ever |

## 2. Score: 100 points

| # | Criterion | Points | 0 | Half | Full |
|---|---|---|---|---|---|
| 1 | **Same customer.** Owners of older homes (pre-1980s, earthenware laterals) in Christchurch and Canterbury | 15 | Renters, new-build buyers, commercial | Mixed | Owners of older homes, almost all |
| 2 | **Where they sit in the moment.** Before (buying or selling: inspectors, agents, conveyancers), during (on site: plumbers, builders, landscapers), after (tenancy changes: property managers), alongside (insurance and EQC history: assessors, loss adjusters) | 15 | No link to the house or the ground | One weak link | On site or in the report when a drain question comes up |
| 3 | **Volume they can send.** A repeat customer list, a newsletter, or a steady stream of jobs | 15 | No list, a handful of jobs | A few hundred, or a few jobs a month | 1,000+ on a list or newsletter, or a portfolio of rentals |
| 4 | **Trust in the home.** Their customer takes their advice | 10 | Arm's length | Some | They write the report or manage the house |
| 5 | **Drain moments they see.** Pre-purchase reports, tenancy inspections, renovations that dig, blockages, storm water | 10 | None | Sometimes | Every week (building inspectors, property managers) |
| 6 | **Deal size.** One yes can bring more than one job | 10 | One-off referral | One list campaign | A portfolio (property managers), a newsletter, or ongoing report referrals |
| 7 | **Warm path.** Jesse, Mike or a partner already knows them, or they share a network or business meeting | 10 | Cold | Shared contact or community | Known by name |
| 8 | **Easy yes.** Owner-run, small enough to decide on a call | 5 | Committee, legal review | Manager decides | Owner decides on one call |
| 9 | **Gets something back.** The 5% fee, a better answer for their customer, referrals the other way | 5 | Nothing obvious | The fee only | Two-way: their customers are better looked after, and selective referrals back |
| 10 | **Proof we can show them.** A job in their suburb, a CCTV report, a review they'd recognise | 5 | None yet | Generic | A job for their kind of customer |

Unknown scores 0, never half. A prospect with three or more unknowns goes to the research pile, not a list. Every score keeps its evidence and the source link (the business's own site, its Google listing, its reviews). No paid enrichment.

## 3. Tiers

| Score | Tier | What happens |
|---|---|---|
| 75 to 100 | **Dream 100** | One to one. dream100 writes a custom email for each; Jesse approves each one; the bot sends it from the partners mailbox on his yes |
| 50 to 74 | **Dream 500** | Segment cold email in waves of 25 to 50, a personal first line each, the wave approved by Jesse |
| 30 to 49 | **Nurture** | A later wave, or the quarterly update after a yes |
| Under 30 | **Out** | Not contacted. The reason is recorded |

The trades list is the top ten of each trade in [partner-types.md](partner-types.md), scored here. A trade business that scores 75 or more belongs to Dream 100, not the trades list.

## 4. How the score is kept

- One row per prospect on the owning role's list: `data/partners/dream100.csv`, `data/partners/dream500/<segment>.csv`, or `data/partners/trades.csv`. Each row has the score, each criterion's evidence and its link.
- After each wave, the Friday scoreboard shows replies, calls, yeses and signed partners per segment and per tier. When the measured numbers disagree with the weights, the bot proposes new weights to Jesse. Jesse decides.
- Nothing here promises a number of partners or jobs.
