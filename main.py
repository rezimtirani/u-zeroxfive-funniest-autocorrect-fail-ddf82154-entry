"""Funniest Autocorrect Fail.

Writes one line to $MAKEFUN_OUTPUT_DIR/entry.txt: a text message
where autocorrect turned "promoted" into "pregnant", sent to Mom
before the sender could stop it.
Standard library only; no network, no secrets.
"""

import os

FAIL_LINE = (
    "Mom, I got the results back \u2014 I'm pregnant! "
    "Sorry, I meant promoted. Please don't tell Dad yet."
)


def check_entry(text):
    """Check the fail line against the competition gate before writing.

    The gate needs UTF-8 text of 1 to 199 characters, not only white
    space, in a single line that reads as one autocorrect fail and
    nothing else. Returns the cleaned text or raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("entry must not be only whitespace")
    if len(cleaned) > 199:
        raise ValueError("entry is %d characters, over the 199 limit" % len(cleaned))
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("entry must be exactly one line")
    return cleaned


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = check_entry(FAIL_LINE)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
