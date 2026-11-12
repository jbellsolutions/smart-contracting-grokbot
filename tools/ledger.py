#!/usr/bin/env python3
"""Partner ledger: partner IDs, referrals and fees. The bot never works a fee out in its head and never moves money.

    ledger.py add-partner "<business>" <type>            new partner: prints its ID and reference code (SC-P001)
    ledger.py list                                        partners: id, code, business, type, signed date
    ledger.py add-referral <code> "<customer ref>"        a customer quoted the partner's name or code
    ledger.py settle <referral-id> <invoice-total> [--gst-inclusive]   invoice settled in full: fee owed is recorded
    ledger.py fee <invoice-total> [--gst-inclusive]       what 5% would be, without recording anything
    ledger.py report                                      referrals, settled jobs and fees owed, per partner

The fee: 5% of the job value, paid once the customer's invoice is settled in full (Jesse's terms). Whether 5% is on
the amount before or after GST is not yet decided (kit/terms.md). Until Jesse decides, context/config.json
"fee_gst_basis" is "unset" and every fee is shown both ways, marked "to confirm with Jesse". NZ GST is 15%.
Files: data/ledger/partners.csv, data/ledger/referrals.csv (mode 600)."""
import sys, csv, json, datetime, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "guards", "scripts"))
from _ws import p

RATE, GST = 0.05, 0.15
P_COLS = ["id", "code", "business", "type", "signed"]
R_COLS = ["ref_id", "code", "customer", "logged", "invoice_total", "gst_inclusive", "settled", "fee_ex_gst", "fee_on_total"]

def path(n):
    d = p("data", "ledger"); d.mkdir(parents=True, exist_ok=True)
    return d / n

def load(n, cols):
    f = path(n)
    if not f.exists(): return []
    return list(csv.DictReader(f.open()))

def save(n, cols, rows):
    f = path(n)
    with f.open("w", newline="") as h:
        w = csv.DictWriter(h, fieldnames=cols); w.writeheader(); w.writerows(rows)
    os.chmod(f, 0o600)

def basis():
    try: return json.loads(p("context", "config.json").read_text()).get("fee_gst_basis", "unset")
    except Exception: return "unset"

def fees(total, inclusive):
    ex = total / (1 + GST) if inclusive else total
    return round(ex * RATE, 2), round(total * RATE, 2)

def show(total, inclusive):
    ex, on_total = fees(total, inclusive)
    b = basis()
    if b == "ex-gst": return f"fee {ex:.2f} (5% of the amount before GST)"
    if b == "on-total": return f"fee {on_total:.2f} (5% of the invoice total)"
    return f"fee {ex:.2f} on the amount before GST, or {on_total:.2f} on the invoice total: to confirm with Jesse"

def main(a):
    if not a: print(__doc__); return 2
    c = a[0]
    if c == "add-partner" and len(a) >= 3:
        rows = load("partners.csv", P_COLS)
        n = len(rows) + 1
        r = {"id": f"P{n:03d}", "code": f"SC-P{n:03d}", "business": a[1], "type": a[2], "signed": str(datetime.date.today())}
        rows.append(r); save("partners.csv", P_COLS, rows)
        print(f"{r['id']} {r['code']}"); return 0
    if c == "list":
        for r in load("partners.csv", P_COLS): print(", ".join(r[k] for k in P_COLS))
        return 0
    if c == "add-referral" and len(a) >= 3:
        if not any(r["code"] == a[1] for r in load("partners.csv", P_COLS)): print(f"no partner with code {a[1]}"); return 1
        rows = load("referrals.csv", R_COLS)
        r = {k: "" for k in R_COLS}
        r.update(ref_id=f"R{len(rows) + 1:04d}", code=a[1], customer=a[2], logged=str(datetime.date.today()))
        rows.append(r); save("referrals.csv", R_COLS, rows); print(r["ref_id"]); return 0
    if c == "settle" and len(a) >= 3:
        rows = load("referrals.csv", R_COLS); total = float(a[2]); inc = "--gst-inclusive" in a
        for r in rows:
            if r["ref_id"] == a[1]:
                ex, on_total = fees(total, inc)
                r.update(invoice_total=f"{total:.2f}", gst_inclusive=str(inc), settled=str(datetime.date.today()),
                         fee_ex_gst=f"{ex:.2f}", fee_on_total=f"{on_total:.2f}")
                save("referrals.csv", R_COLS, rows); print(show(total, inc)); return 0
        print(f"no referral {a[1]}"); return 1
    if c == "fee" and len(a) >= 2:
        print(show(float(a[1]), "--gst-inclusive" in a)); return 0
    if c == "report":
        parts = {r["code"]: r["business"] for r in load("partners.csv", P_COLS)}
        refs = load("referrals.csv", R_COLS)
        print(f"partners {len(parts)}, referrals {len(refs)}, settled {sum(1 for r in refs if r['settled'])}")
        for code, biz in parts.items():
            mine = [r for r in refs if r["code"] == code]
            done = [r for r in mine if r["settled"]]
            ex = sum(float(r["fee_ex_gst"]) for r in done); tot = sum(float(r["fee_on_total"]) for r in done)
            owed = {"ex-gst": f"{ex:.2f}", "on-total": f"{tot:.2f}"}.get(basis(), f"{ex:.2f} or {tot:.2f} (GST basis to confirm)")
            print(f"{code} {biz}: referrals {len(mine)}, settled {len(done)}, fees owed {owed}")
        return 0
    print(__doc__); return 2

if __name__ == "__main__": sys.exit(main(sys.argv[1:]))
