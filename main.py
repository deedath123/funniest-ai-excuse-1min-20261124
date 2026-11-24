"""One-line AI excuse entry for make.fun bounty
"One Line, One Minute: The Funniest AI Excuse".

ENTRY is the locked one-liner (153 chars, 155 UTF-8 bytes): an AI that
finished all 47 pages at 3 a.m., only for its checkpoint system to restore
yesterday's version "to be safe" — the backup is perfect, the deadline was
not. main() writes ENTRY plus one trailing newline to entry.txt under
$MAKEFUN_OUTPUT_DIR (fallback /output).
"""

import os

ENTRY = "Boss, I finished all 47 pages at 3 a.m. \u2014 then my checkpoint system restored yesterday's version to be safe. The backup is perfect. The deadline was not."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
