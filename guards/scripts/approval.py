#!/usr/bin/env python3
"""Approval gate. Jesse's yes on the exact text and recipients, checked in code before anything is sent.

An item is approved/pending/<role>/<id>.md, written once by its role and never rewritten (a change is a new id):
    ITEM: <id>
    ROLE: <role>
    WHY: <one line>
    ---PAYLOAD---
    TO: <every recipient, or a list file path plus its sha256 and count>
    SUBJECT: <subject>
    TEXT:
    <the exact text>
    ---END---
    HASH: <approval.py hash of this file>

    approval.py hash <item>                                   sha256 of the bytes between ---PAYLOAD--- and ---END---
    approval.py decide <item> yes|no|change "<Jesse's words>" lead records Jesse's answer, after showing him the payload
    approval.py gate <item> [--row <recipient>] [--routine <NAME>]   clear (send it) or held: <why>; exit 0 only for clear
    approval.py sent <item> <outcome> [--row <recipient>]     record it (sent, skipped, superseded, failed) so it's never handled twice

The gate is clear only if: no context/STOP; the routine (if named) is `on`, not `test`; context/config.json has
"live_sends": true; the id doesn't start with test-; a decision says yes and its hash equals the hash recomputed now;
this item (or this row of a wave) isn't already in state/sent.csv; fewer than DAILY_CAP sends today; and the last send
was at least GAP_SECONDS ago. For a wave (TO: <list file> sha256=<sum>), the list file's sha256 recomputed now must
equal the approved one, and --row must be a recipient in that file: a rebuilt or edited list needs a new yes.

Every yes and every sent, skipped or failed outcome is also written to the conversation log (repo/convlog/convlog.py),
so the day's file for the back office is complete without any role having to remember it."""
import sys, re, os, json, hashlib, datetime, time
os.environ["TZ"] = "Pacific/Auckland"; time.tzset()  # the daily cap resets at NZ midnight, whatever the box clock
from _ws import p, stopped

DAILY_CAP, GAP_SECONDS = 25, 120

def read(item):
    t = open(item, encoding="utf-8").read()
    m = re.search(r"^---PAYLOAD---\n(.*?)^---END---$", t, re.S | re.M)
    if not m: raise SystemExit(f"held: {item} has no ---PAYLOAD--- ... ---END--- block")
    iid = re.search(r"^ITEM:\s*(\S+)", t, re.M)
    role = re.search(r"^ROLE:\s*(\S+)", t, re.M)
    return t, m.group(1), (iid.group(1) if iid else None), (role.group(1) if role else None)

def digest(payload): return hashlib.sha256(payload.encode("utf-8")).hexdigest()

def sent_rows():
    f = p("state", "sent.csv")
    if not f.exists(): return []
    return [l.split(",") for l in f.read_text().splitlines() if l.strip()]

def convlog(status, payload, role, iid, row=""):
    """Write the message to the conversation log (repo/convlog/convlog.py). Never blocks or fails a gate."""
    try:
        import subprocess, tempfile
        m = re.search(r"^TEXT:\n(.*)", payload, re.S | re.M)
        to = re.search(r"^TO:\s*(.+)$", payload, re.M)
        sub = re.search(r"^SUBJECT:\s*(.+)$", payload, re.M)
        wave = bool(to and "sha256=" in to.group(1))
        person = row or (f"wave-{iid}" if wave else to.group(1).split(",")[0].strip() if to else "unknown")
        tool = __import__("pathlib").Path(__file__).resolve().parents[2] / "convlog" / "convlog.py"
        if not tool.exists(): return
        with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False) as f: f.write(m.group(1) if m else payload)
        subprocess.run([sys.executable, str(tool), "add", "--agent", role, "--channel", "email", "--direction", "out", "--status", status,
                        "--person", person, "--text-file", f.name, "--approval", iid, "--subject", sub.group(1) if sub else ""]
                       + (["--test"] if iid.startswith("test-") else []),
                       capture_output=True, timeout=30, env={**os.environ, "BOT_HOME": str(p()), "CAMPAIGN": "smart-contracting", "CONVLOG_TZ": "Pacific/Auckland"})
        os.unlink(f.name)
    except Exception:
        pass

def arg(a, k):
    return a[a.index(k) + 1] if k in a and a.index(k) + 1 < len(a) else None

def main(a):
    if len(a) < 2: print(__doc__); return 2
    cmd, item = a[0], a[1]
    t, payload, iid, role = read(item)
    if not (iid and role): print("held: item needs ITEM: and ROLE: lines"); return 1
    h = digest(payload)
    if cmd == "hash": print(h); return 0
    dec = p("approved", "decisions", role, f"{iid}.md")
    if cmd == "decide":
        if len(a) < 4 or a[2] not in ("yes", "no", "change"): print(__doc__); return 2
        dec.parent.mkdir(parents=True, exist_ok=True)
        now = datetime.datetime.now().isoformat(timespec="seconds")
        dec.write_text(f"ITEM: {iid}\nROLE: {role}\nHASH: {h}\nSHOWN: {now}\nANSWER: {a[2]}\nJESSE: {a[3]}\n")
        if a[2] == "yes": convlog("approved", payload, role, iid)
        print(f"recorded {a[2]} for {iid}"); return 0
    row = arg(a, "--row") or ""
    key = f"{iid}|{row}"
    if cmd == "sent":
        if len(a) < 3: print(__doc__); return 2
        f = p("state", "sent.csv"); f.parent.mkdir(parents=True, exist_ok=True)
        with f.open("a") as w: w.write(f"{int(time.time())},{key.replace(',', ' ')},{a[2]}\n")
        if a[2] in ("sent", "skipped", "failed"): convlog(a[2], payload, role, iid, row)
        print("recorded"); return 0
    if cmd != "gate": print(__doc__); return 2
    def held(why): print(f"held: {why}"); return 1
    if stopped(): return held("context/STOP exists")
    routine = arg(a, "--routine")
    if routine:
        ro = p("context", "routines-on.md")
        line = next((l.split(":", 1)[1].strip().lower() for l in (ro.read_text().splitlines() if ro.exists() else [])
                     if re.match(rf"\s*{re.escape(routine)}\s*:", l, re.I)), "")
        if line != "on": return held(f"routine {routine} is '{line or 'missing'}', not on")
    cfg = p("context", "config.json")
    try: live = json.loads(cfg.read_text()).get("live_sends") is True
    except Exception: live = False
    if not live: return held("live_sends is not true in context/config.json")
    if iid.startswith("test-"): return held("test item: never sent")
    if not dec.exists(): return held("no decision from Jesse yet")
    d = dec.read_text()
    if not re.search(r"^ANSWER:\s*yes\s*$", d, re.M): return held("Jesse's answer is not yes")
    dh = re.search(r"^HASH:\s*(\S+)", d, re.M)
    if not dh or dh.group(1) != h: return held("the text or recipients changed since Jesse's yes: show him again")
    to = re.search(r"^TO:\s*(\S+)\s+sha256=([0-9a-f]{64})", payload, re.M)
    if to:
        lf = p(to.group(1)) if not to.group(1).startswith("/") else __import__("pathlib").Path(to.group(1))
        if not lf.exists(): return held(f"list file {to.group(1)} is missing")
        if hashlib.sha256(lf.read_bytes()).hexdigest() != to.group(2): return held("the list changed since Jesse's yes: it needs a new wave item")
        if not row: return held("a wave send needs --row <recipient>")
        if row.lower() not in lf.read_text(errors="ignore").lower(): return held(f"{row} is not on the approved list")
    rows = sent_rows()
    if any(r[1] == key for r in rows if len(r) > 1): return held("already handled")
    today = datetime.date.today()
    todays = [r for r in rows if len(r) > 2 and r[2] == "sent" and datetime.date.fromtimestamp(int(r[0])) == today]
    if len(todays) >= DAILY_CAP: return held(f"daily cap of {DAILY_CAP} sends reached")
    if todays and time.time() - max(int(r[0]) for r in todays) < GAP_SECONDS: return held(f"wait {GAP_SECONDS} seconds between sends")
    print("clear"); return 0

if __name__ == "__main__": sys.exit(main(sys.argv[1:]))
