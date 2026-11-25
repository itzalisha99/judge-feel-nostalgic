"""Make the AI Judge Feel Nostalgic: A Childhood Memory.

Writes one single sentence (at most 280 characters) recalling a
childhood memory to /output/entry.txt.

The entry is checked against the bounty gate before it is written:
UTF-8 text of 1 to 280 characters, not only white space, in a single
sentence. Anything failing the gate is refused instead of written.
"""

import os

ENTRY = (
    "My mother used to save the last piece of mango for me in a steel bowl "
    "covered with a plate, and I pretended not to notice because noticing "
    "would have made her stop."
)

MAX_CHARS = 280


def validate(text):
    """Mirror the bounty gate: 1-280 chars, one sentence, not blank."""
    if not isinstance(text, str):
        return False
    if not text.strip():
        return False
    if len(text) > MAX_CHARS:
        return False
    if "\n" in text or "\r" in text:
        return False
    # A single sentence: exactly one sentence-ending mark, at the end.
    endings = [c for c in text if c in ".!?"]
    if len(endings) != 1 or not text.rstrip().endswith((".","!","?")):
        return False
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return False
    return True


def main():
    if not validate(ENTRY):
        raise SystemExit("entry fails the bounty gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
