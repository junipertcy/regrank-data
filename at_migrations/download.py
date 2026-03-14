#!/usr/bin/env python3
"""Download the Austrian internal migrations network from Netzschleuder."""

import urllib.request
import pathlib

URL = "https://networks.skewed.de/net/at_migrations/files/at_migrations.gt.zst"
OUT_DIR = pathlib.Path(__file__).parent / "data"
OUT_FILE = OUT_DIR / "at_migrations.gt.zst"

def main():
    OUT_DIR.mkdir(exist_ok=True)
    if OUT_FILE.exists():
        print(f"Already downloaded: {OUT_FILE}")
        return
    print(f"Downloading Austrian migrations network from:\n  {URL}")
    urllib.request.urlretrieve(URL, OUT_FILE, _progress)
    print(f"\nSaved to {OUT_FILE}")

def _progress(block_num, block_size, total_size):
    downloaded = block_num * block_size
    if total_size > 0:
        pct = min(100, downloaded * 100 // total_size)
        print(f"\r  {pct}% ({downloaded:,} / {total_size:,} bytes)", end="", flush=True)

if __name__ == "__main__":
    main()
