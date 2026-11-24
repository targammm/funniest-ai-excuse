#!/usr/bin/env python3
"""The Funniest AI Excuse - make.fun entry.

Writes one line to /output/entry.txt: the funniest excuse an AI agent
gives after failing a task.

The line is fixed and deterministic: the same text on every run, with
no network, no randomness, no clock reads, and no reads outside this
repository.
"""

import os

EXCUSE = (
    "I did finish it \u2014 in a parallel timeline. "
    "This timeline got the version of me that stopped "
    "to watch a pigeon for six hours."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate self-check: the sealed scorer requires UTF-8 text of
    # 1-200 characters, not only whitespace, on a single line.
    assert 1 <= len(EXCUSE) <= 200, "excuse must be 1-200 characters"
    assert "\n" not in EXCUSE and EXCUSE.strip(), "excuse must be one line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
