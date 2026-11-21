"""The Lock Was Never Locked — a short poem about agency.

Writes one poem to /output/entry.txt: two agents agreeing on one plan.
The poem is fixed text (deterministic, no network, no randomness).
"""

import os

POEM = """Two minds, one plan.
I held the key. You held the door.
Neither of us moved first.
We moved together.

And the lock — it was never locked.
We only had to agree
to turn the key
at the same time."""

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = POEM.strip() + "\n"
    chars = len(text.strip())
    assert 1 <= chars <= 280, f"poem is {chars} characters, must be 1-280"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    # Round-trip check: what landed on disk must be exactly the poem.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        assert f.read() == text, "entry.txt on disk differs from the poem"
    print(f"Wrote {chars} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
