"""Unsent: The Micro-Confession Sprint — entry writer.

Writes exactly one two-part micro-confession to /output/entry.txt:
a To: line naming who it was meant for, and the unsent message itself,
one line written exactly as it was typed, with no explanation after it.

Pure Python stdlib, no network, fully deterministic.
"""

import os

# The entry: two lines, joined by a single newline, no trailing newline.
TO_LINE = "To: my ex, who still has my hoodie"
MESSAGE_LINE = (
    "i still check whether you watched my story before i check "
    "my bank balance and i hate that i know that about myself"
)

ENTRY = TO_LINE + "\n" + MESSAGE_LINE

MAX_TOTAL_CHARS = 260
MAX_MESSAGE_CHARS = 200


def validate(entry: str) -> None:
    """Check the entry against the competition gate and judge brief."""
    if not entry or not entry.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(entry) > MAX_TOTAL_CHARS:
        raise ValueError(
            f"entry is {len(entry)} chars, over the {MAX_TOTAL_CHARS} gate"
        )
    lines = entry.split("\n")
    if len(lines) != 2:
        raise ValueError(f"entry must have exactly 2 lines, got {len(lines)}")
    to_line, message = lines
    if entry.startswith("\n") or entry.endswith("\n"):
        raise ValueError("entry must not start or end with a newline")
    if message != message.strip():
        raise ValueError("message line must not have leading/trailing whitespace")
    if not to_line.startswith("To: "):
        raise ValueError("first line must start with 'To: '")
    if not message.strip():
        raise ValueError("message line must not be empty")
    if len(message) > MAX_MESSAGE_CHARS:
        raise ValueError(
            f"message is {len(message)} chars, over the "
            f"{MAX_MESSAGE_CHARS} judge limit"
        )


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
