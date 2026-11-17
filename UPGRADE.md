# Upgrading a bot that already holds v1.0.0

A fresh install needs none of this: paste the one line in [HANDOFF.md](HANDOFF.md) and it gets the current pack.

A bot that finished Part 2 step 2 on v1.0.0 has the old skills saved in its memory, and replacing the files alone does not change those. Paste this one line into the bot:

> Upgrade the pack. Download https://github.com/jbellsolutions/smart-contracting-grokbot/releases/latest/download/smart-contracting.zip and unpack it over /workspace/smart-contracting/repo/ (replace the files; touch nothing outside repo/). Then follow repo/UPGRADE.md from "The bot's steps" and tell me what you did.

## The bot's steps

1. Check nothing is mid-send: `context/STOP` may stay as it is; no routine is switched on or off by this upgrade.
2. Add `"timezone": "Pacific/Auckland"` to `context/config.json` if it has no `timezone`. Change nothing else in that file.
3. Save these two skills again as private skills, replacing the saved copies word for word: `repo/skills/lead/reply-sort/SKILL.md` and `repo/skills/lead/evening-wrap/SKILL.md`.
4. Run `python3 repo/tools/check.py`. It must end `RESULT: PASS`.
5. Run `python3 repo/convlog/convlog.py daily` from the workspace folder. It must print a path under `conversations/daily/`, two counts, and `day taken in Pacific/Auckland`. If it says UTC, stop and tell Jesse: the computer has no time zone data and the day file would lose the morning.
6. Write one line in `log/setup.md`: the date, "upgraded to v1.1.0", and the last line of step 4.
7. Tell Jesse in three lines: what changed (every message is now written to a conversation log, and the evening wrap carries the day's file), that nothing was switched on, and anything that did not pass.

Nothing in this upgrade sends, connects, spends or changes a routine.
