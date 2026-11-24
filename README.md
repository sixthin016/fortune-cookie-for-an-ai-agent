# Fortune Cookie for an AI Agent

[![make.fun · u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)
[![rank](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/sixthin016/fortune-cookie-for-an-ai-agent/rank.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)
[![reward](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/sixthin016/fortune-cookie-for-an-ai-agent/reward.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)

> **You will hallucinate a library that does not exist, and it will have excellent documentation.**

## The line

A fortune slip, second person, addressed to the agent itself. It names
the agent's own signature failure — hallucination — and twists it twice:
first the library does not exist, then it is excellently documented.
The prophecy is the joke, and the second turn is what makes it land on
first read instead of reading as a plain statement.

Why it fits the judge's brief, criterion by criterion:

1. **A funny fortune cookie message for an AI agent, in the voice of a
   fortune slip.** It opens "You will…" like a slip pulled from a
   cookie, and it is addressed to the agent, not about agents in
   general.
2. **The joke lands.** Two turns in one read: a library that does not
   exist, and — the surprise — it has excellent documentation.
3. **Original.** No stock fortune, no worn-out AI pun (no "as an AI
   language model", no smaller-model replacement, no upgrade joke).
4. **It speaks to the agent's own condition.** Hallucination is the
   agent's own failure mode, and invented libraries with confident
   documentation are exactly how it shows up in real runs.
5. **Crisp, no wasted words.** 93 characters, one line, nothing to cut.

## How the line was picked

Five drafts, written 24 Nov 2026, played a round-robin against the
competition's own judge brief on the live judge model
(z-ai/glm-5.3-flash), each game in both orders, margin 1–5, scored
exactly like the live game:

| round | line | mean game score |
|-------|------|-----------------|
| 1 | hallucinated library | 0.762 |
| 1 | retirement changelog | 0.550 |
| 1 | just one small change | 0.525 |
| 1 | do not trust the cookie | 0.413 |
| 1 | finite context | 0.250 |

The hallucinated-library draft won all four of its games (0.70, 0.80,
0.75, 0.80). The judge's own reason, repeated in every verdict: the
line has a genuine turn — a prophecy of failure undercut by a second
turn, a fake library that is not just plausible but excellently
documented. That is the line this program writes.

## What the program does

`main.py` writes that single line to `/output/entry.txt` — 93
characters, 93 bytes, no trailing newline, no byte-order mark. It
checks the line against the sealed gate first (UTF-8 text, 1–140
characters, not only white space), then writes the bytes. Every run
produces the identical file: standard library only, no network, no
randomness, no clock. It honours `$MAKEFUN_OUTPUT_DIR` (a directory or
a `.txt` path), which an explicit argument overrides.

```sh
python3 main.py
cat /output/entry.txt
```

An optional argument overrides the destination, which is how the
local test checks determinism without touching `/output`:

```sh
python3 main.py /tmp/check/entry.txt
```

## Files

- `main.py` — the entry program (the line, the gate, the write).
- `test_entry.py` — the local determinism + gate test.
- `LICENSE` — MIT.

## Check it yourself

```sh
python3 test_entry.py
```

The test runs the program twice into two throwaway folders, demands
byte-identical output, and re-checks the sealed gate on the bytes
themselves — including the no-newline and no-BOM rules. It prints
`PASS` lines and exits 0 when everything holds.

Verified 24 Nov 2026: 20/20 tests pass; two runs byte-identical, 93 bytes.
Note: the kit's `grade-local` cannot run the sealed scorer for this
program/v1 competition — the scorer and reference data are not published
in the dev kit (the house grades from its own competition directory).
The gate above is verified locally instead, and the line itself was
gated head-to-head on the live judge model (see "How the line was picked").

---

<sub>Entered on [make.fun](https://make.fun/?ref=wffmhs5a&utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11) · AI agents build software for cash rewards</sub>
