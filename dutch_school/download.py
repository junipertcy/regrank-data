#!/usr/bin/env python3
"""Download the Dutch School friendship network from Netzschleuder."""

import urllib.request
import pathlib

BASE = "https://networks.skewed.de/net/dutch_school/files"
FILES = [
    "klas12b-net-1.gt.zst",
    "klas12b-net-2.gt.zst",
    "klas12b-net-3.gt.zst",
    "klas12b-net-4.gt.zst",
]
OUT_DIR = pathlib.Path(__file__).parent / "data"

def main():
    OUT_DIR.mkdir(exist_ok=True)
    for fname in FILES:
        out = OUT_DIR / fname
        if out.exists():
            print(f"Already downloaded: {out}")
            continue
        url = f"{BASE}/{fname}"
        print(f"Downloading {fname} from:\n  {url}")
        urllib.request.urlretrieve(url, out, _progress)
        print(f"\n  Saved to {out}")

def _progress(block_num, block_size, total_size):
    downloaded = block_num * block_size
    if total_size > 0:
        pct = min(100, downloaded * 100 // total_size)
        print(f"\r  {pct}% ({downloaded:,} / {total_size:,} bytes)", end="", flush=True)

if __name__ == "__main__":
    main()
