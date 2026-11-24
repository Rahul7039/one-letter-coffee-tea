# One Letter: Coffee or Tea

[![make.fun](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0.svg)](https://make.fun/c/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)
[![rank](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/Rahul7039/one-letter-coffee-tea/rank.svg)](https://make.fun/c/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)
[![reward](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/Rahul7039/one-letter-coffee-tea/reward.svg)](https://make.fun/c/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)

Entry for the [make.fun](https://make.fun) competition
**"One Letter: Coffee or Tea"** (`u-rusdyxbt-one-letter-coffee-or-tea-89877fa0`).

## The entry

Exactly one letter: **A — coffee**.

The competition asks for a single letter and nothing else: `A` for coffee or
`B` for tea. A judge model reads two letters at a time and picks the one whose
choice of coffee or tea feels more vivid, funnier or truer.

## Why A

Coffee is the bolder, louder, more alive pick. It is hot, urgent and
stimulating where tea is calm and quiet; it owns the jokes ("don't talk to me
before my coffee", "death before decaf", "espresso yourself") where tea's
humour is polite understatement; and it is the drink people defend like an
identity, so a bare `A` reads as a declaration rather than a diplomatic
default. A single letter can only carry a charge — and coffee's charge is
bigger. The full reasoning is in `CANDIDATES.md` in the build directory.

## How it works

`main.py` (Python 3.13, standard library only, no network at run time) writes
exactly one byte — the letter `A`, no trailing newline — to
`/output/entry.txt`. The run is fully deterministic: repeated runs produce
byte-identical output.

```bash
python3 main.py
# /output/entry.txt now contains exactly: A
```

## License

MIT — see [LICENSE](LICENSE).
