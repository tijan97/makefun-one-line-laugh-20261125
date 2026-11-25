"""One Line, One Laugh — a single self-contained one-liner.

The program writes exactly one funny line of text to entry.txt in the
output directory the grader provides, and nothing else.
"""

import os

LINE = "My Roomba sued me for custody of the dust bunnies — and won, so now I pay child support in crumbs."


def main():
    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
