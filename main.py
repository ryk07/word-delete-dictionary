#!/usr/bin/env python3
"""The Word You'd Delete from the Dictionary.

Writes one original word — the single word this entry would erase from
the dictionary forever — to /output/entry.txt. Standard library only.
The output path is the one the rules name; nothing is read from the
working directory.
"""

import os

WORD = "defenestration"
# Why this word: it is the only single word English has for throwing
# someone out of a window. Erase it and the language loses a whole
# act — no other word covers the gap. The joke lands the moment a
# reader pictures the word gone: a crime so specific it needed its
# own word, and now it has none. It is fresh because the field will
# flood the obvious hate-words ("moist", "literally", "irregardless");
# this one is loved, not hated, which is exactly why deleting it
# stings.


def main() -> None:
    text = WORD.strip()
    assert 1 <= len(text) <= 77, f"word is {len(text)} chars"
    assert text.strip() == text and "\n" not in text
    assert " " not in text, "entry must be a single word"
    assert text.isalpha(), "entry must be one plain word, letters only"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
