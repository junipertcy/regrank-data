#!/usr/bin/env python3
"""Download the Reddit hyperlink network from SNAP."""

import urllib.request
import pathlib

URL = "https://snap.stanford.edu/data/soc-redditHyperlinks-body.tsv"
OUT_DIR = pathlib.Path(__file__).parent / "data"
OUT_FILE = OUT_DIR / "soc-redditHyperlinks-body.tsv"

def main():
    OUT_DIR.mkdir(exist_ok=True)
    if OUT_FILE.exists():
        print(f"Already downloaded: {OUT_FILE}")
        return
    print(f"Downloading Reddit hyperlink network from:\n  {URL}")
    print("  (This file is ~150 MB, may take a few minutes)")
    urllib.request.urlretrieve(URL, OUT_FILE, _progress)
    print(f"\nSaved to {OUT_FILE}")

def _progress(block_num, block_size, total_size):
    downloaded = block_num * block_size
    if total_size > 0:
        pct = min(100, downloaded * 100 // total_size)
        mb = downloaded / (1024 * 1024)
        print(f"\r  {pct}% ({mb:.1f} MB)", end="", flush=True)

if __name__ == "__main__":
    main()
