---
name: referral-campaign
description: Plan and draft each referral partner's next step: their list campaign, the brief, a thank-you, a check-in. Load for the weekly referral campaigns routine, or when Jesse mentions a partner.
---

# referral-campaign

Role: trades. Every step runs inside the gates in `repo/GATES.md` and the guards in `repo/guards/SKILL.md`.

1. Who: the referral partners in `context/owner.md` (the newsletter partner first: he has a list, goes to business networking meetings around Christchurch, and is waiting to say yes to the campaign) and every signed partner in `tools/ledger.py list`.
2. Each partner's one next step:
   - No campaign yet and they've said yes: the campaign email and text from `repo/kit/campaigns/<type>.md`, filled in for them, plus the brief from `repo/kit/emails.md`. Jesse checks it, then it goes to the partner for their yes. They send it from their own system to their own list.
   - Gone quiet 14 days: the quiet-partner check-in from `repo/kit/emails.md`, offering to do all the legwork.
   - A referral came in: the thank-you.
   - A fee is due: `tools/ledger.py report`. A payout proposal for Jesse; he pays, and the remittance note is drafted from `kit/emails.md`.
3. One partner campaign a month across the programme (`repo/kit/campaign-calendar.md`), so no list gets tired.
4. Everything is an item for Jesse. The partner's own yes is recorded in the item's WHY before their campaign is final.
