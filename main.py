#!/usr/bin/env python3
"""A fortune cookie for an AI agent.

The line was picked on 24 Nov 2026 by a head-to-head gate against the
competition's own judge brief, run on the live judge model
(z-ai/glm-5.3-flash): five drafts played a round-robin, each game in
both orders, scored exactly like the live game. The hallucinated-library
draft won all four of its games (0.70, 0.80, 0.75, 0.80; mean 0.762).
The judge's own reason, repeated in every verdict: the line has a
genuine turn — a prophecy of failure undercut by a second turn, a fake
library that is not just plausible but excellently documented.

The program below does one small job and nothing else. It turns that
line into bytes, checks the bytes against the sealed gate, and puts
them in a file. Same bytes every time: no clock, no dice, no network,
no imports beyond the standard library.
"""

import os
import sys
from pathlib import Path

# The line itself. 93 characters, inside the sealed gate's 1 to 140.
# A fortune slip, second person, addressed to the agent: it names the
# agent's own signature failure (hallucination) and twists it twice —
# first the library does not exist, then it is excellently documented.
LINE = (
    "You will hallucinate a library that does not exist, "
    "and it will have excellent documentation."
)

DEFAULT_OUTPUT = Path("/output/entry.txt")
LIMIT = 140


class GateError(ValueError):
    """Raised when a candidate line fails the sealed gate."""


def _is_blank(text):
    return not text.strip()


def _fits(text):
    return 1 <= len(text) <= LIMIT


def payload_for(line):
    """Encode *line* after the gate, or raise GateError."""
    if not isinstance(line, str):
        raise GateError("entry must be text, got %s" % type(line).__name__)
    if _is_blank(line):
        raise GateError("entry must not be only white space")
    if not _fits(line):
        raise GateError("entry must be 1 to 140 characters, got %d" % len(line))
    line.encode("utf-8")  # raises if not valid UTF-8 text
    return line.encode("utf-8")


def line_bytes():
    """The exact bytes the grader will read."""
    return payload_for(LINE)


def _prepare_parent(path):
    parent = path.parent
    if str(parent) not in ("", "."):
        parent.mkdir(parents=True, exist_ok=True)


def emit(line, destination):
    """Write *line* (gate-checked) to *destination*; return the path."""
    data = payload_for(line)
    target = Path(destination)
    _prepare_parent(target)
    target.write_bytes(data)
    return target


def _destination_from_env():
    """Resolve $MAKEFUN_OUTPUT_DIR: a directory or a .txt file path."""
    raw = os.environ.get("MAKEFUN_OUTPUT_DIR", "")
    if not raw:
        return None
    path = Path(raw)
    if path.suffix == ".txt":
        return path
    return path / "entry.txt"


def _destination_from_argv(argv):
    if len(argv) > 1:
        return Path(argv[1])
    return None


def resolve_destination(argv=None):
    """argv wins over $MAKEFUN_OUTPUT_DIR, which wins over the default."""
    dest = _destination_from_argv(list(sys.argv) if argv is None else argv)
    if dest is not None:
        return dest
    dest = _destination_from_env()
    if dest is not None:
        return dest
    return DEFAULT_OUTPUT


def write_entry(destination=DEFAULT_OUTPUT):
    """Compatibility entry point: write the chosen line out."""
    return emit(LINE, destination)


def main(argv=None):
    destination = resolve_destination(argv)
    emit(LINE, destination)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
