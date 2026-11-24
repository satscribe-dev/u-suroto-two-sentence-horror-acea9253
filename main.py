"""Two-Sentence Horror — make.fun entry (u-suroto-two-sentence-horror-acea9253).

Writes one horror story of exactly two sentences to /output/entry.txt.
Deterministic: no input, no network, no randomness.
"""

import os

STORY = (
    "The graveyard keeper knows every name on every stone, "
    "and he greeted me by mine before I spoke. "
    "'You're early,' he said, 'your stone isn't finished yet.'"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
