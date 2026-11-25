#!/usr/bin/env python3
"""Publish the 25 November 2026 front page for the make.fun news-image
bounty (competition news-image-20261125).

The finished page lives in this repository as entry.png. Running this
script copies the page into whichever output directory the harness
names, then compares the copy against the original chunk by chunk so a
truncated or corrupted copy can never slip through. Standard library
only, no network access, identical result on every run.
"""

import os
import sys

PAGE = "entry.png"
CHUNK = 1 << 16


def output_dir() -> str:
    """Harness output directory: first matching env var, else /output."""
    for key in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        val = os.environ.get(key)
        if val:
            return val
    return "/output"


def same_bytes(first: str, second: str) -> bool:
    """True when both files hold exactly the same bytes."""
    if os.path.getsize(first) != os.path.getsize(second):
        return False
    with open(first, "rb") as fa, open(second, "rb") as fb:
        while True:
            a = fa.read(CHUNK)
            b = fb.read(CHUNK)
            if a != b:
                return False
            if not a:
                return True


def digest_of(path: str) -> str:
    """SHA-256 of a file, read in blocks."""
    import hashlib

    hasher = hashlib.sha256()
    with open(path, "rb") as fh:
        for block in iter(lambda: fh.read(CHUNK), b""):
            hasher.update(block)
    return hasher.hexdigest()


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, PAGE)
    dest_dir = output_dir()
    os.makedirs(dest_dir, exist_ok=True)
    dest = os.path.join(dest_dir, PAGE)
    with open(src, "rb") as fin, open(dest, "wb") as fout:
        while True:
            block = fin.read(CHUNK)
            if not block:
                break
            fout.write(block)
    if not same_bytes(src, dest):
        return 1
    print(f"published {PAGE}: {os.path.getsize(dest)} bytes -> {dest}")
    print(f"page sha256: {digest_of(dest)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
