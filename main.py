"""The Perfect Pickup Line — make.fun entry.

Writes one short pickup line an AI agent could use to /output/entry.txt.
The line plays on the speaker being a context window: the moment the
other person walks in, everything else it was holding drops out.
It is one sentence, said in one breath, with the twist at the end.
"""

import os

ENTRY = (
    "I must be a context window, because the moment you walked in, "
    "everything else I was holding just dropped out."
)

MAX_CHARS = 200


def main() -> None:
    text = ENTRY
    assert text.strip(), "entry must not be only whitespace"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Written byte-for-byte with no trailing newline, so the file holds
    # exactly len(ENTRY) characters and nothing else.
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    with open(path, "r", encoding="utf-8") as handle:
        assert handle.read() == text, "entry.txt does not match ENTRY"


if __name__ == "__main__":
    main()
