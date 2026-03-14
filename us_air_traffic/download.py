#!/usr/bin/env python3
"""Download the US air traffic network from Netzschleuder."""

import urllib.request
import pathlib

URL = "https://networks.skewed.de/net/us_air_traffic/files/us_air_traffic.gt.zst"
OUT_DIR = pathlib.Path(__file__).parent / "data"
OUT_FILE = OUT_DIR / "us_air_traffic.gt.zst"

def main():
    OUT_DIR.mkdir(exist_ok=True)
    if OUT_FILE.exists():
        print(f"Already downloaded: {OUT_FILE}")
        return
    print(f"Downloading US air traffic network from:\n  {URL}")
    urllib.request.urlretrieve(URL, OUT_FILE, _progress)
    print(f"\nSaved to {OUT_FILE}")

def _progress(block_num, block_size, total_size):
    downloaded = block_num * block_size
    if total_size > 0:
        pct = min(100, downloaded * 100 // total_size)
        print(f"\r  {pct}% ({downloaded:,} / {total_size:,} bytes)", end="", flush=True)

if __name__ == "__main__":
    main()
