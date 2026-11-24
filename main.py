#!/usr/bin/env python3
"""Entry for make.fun bounty "Funniest Autocorrect Fail"
(u-zeroxfive-funniest-autocorrect-fail-ddf82154).

Writes a single one-line autocorrect fail to entry.txt in the output
directory ($MAKEFUN_OUTPUT_DIR, default /output). The line is a group
text announcing an engagement where "engaged" slipped to "enraged" --
a one-letter autocorrect swap that flips the meaning completely.

Deterministic, standard library only, no network.
"""

import os

ENTRY = "He finally proposed last night and I said yes. I'm officially enraged!"

# The bounty gate accepts UTF-8 text of 1 to 199 characters, one line,
# not only whitespace. Validate defensively so a future edit of ENTRY
# can never silently produce an invalid entry file.
MAX_CHARS = 199


def validate(text):
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError("entry exceeds %d characters: %d" % (MAX_CHARS, len(text)))
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # raises if not encodable as UTF-8


def main():
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
