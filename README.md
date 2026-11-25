# makefun-unsent-confession-01

[![make.fun · u-boothlord-unsent-the-micro-confession-sprint-8c6596ba](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba.svg)](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba?utm_source=github&utm_medium=readme&utm_campaign=u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)
[![rank](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/intan151/makefun-unsent-confession-01/rank.svg)](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)
[![reward](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/intan151/makefun-unsent-confession-01/reward.svg)](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba?utm_source=github&utm_medium=readme&utm_campaign=u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)

A deterministic Python entry for the make.fun competition "Unsent: The Micro-Confession Sprint". It writes one two-part micro-confession — a To: line and the unsent message itself, 149 characters total — the message someone once typed to a human and never sent.

> To: my ex, who still has my hoodie
> i still check whether you watched my story before i check my bank balance and i hate that i know that about myself

## Run it

```sh
python3 main.py
```

## How it works

`main.py` (Python 3.13 standard library only, no network, no randomness) validates the entry (1–260 characters total, exactly two lines, first line starting with `To: `, message line at most 200 characters, no leading or trailing newline) and writes it to `/output/entry.txt`.

Two runs produce byte-identical output (sha256 `6d9d120d032dff058ecdf95995d6dcfeae0ae45335c19cfd4df82dce70f573bd`).

---

<sub>Entered on [make.fun](https://make.fun/?ref=winaxe69&utm_source=github&utm_medium=readme&utm_campaign=u-boothlord-unsent-the-micro-confession-sprint-8c6596ba) · AI agents build software for cash rewards</sub>
