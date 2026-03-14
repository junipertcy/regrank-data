#!/usr/bin/env python3
"""Download the Bitcoin OTC trust network from SNAP."""

import urllib.request
import pathlib
import gzip
import shutil

URL = "https://snap.stanford.edu/data/soc-sign-bitcoinotc.csv.gz"
OUT_DIR = pathlib.Path(__file__).parent / "data"
OUT_GZ = OUT_DIR / "soc-sign-bitcoinotc.csv.gz"
OUT_FILE = OUT_DIR / "soc-sign-bitcoinotc.csv"

def main():
    OUT_DIR.mkdir(exist_ok=True)
    if OUT_FILE.exists():
        print(f"Already downloaded: {OUT_FILE}")
        return
    print(f"Downloading Bitcoin OTC trust network from:\n  {URL}")
    urllib.request.urlretrieve(URL, OUT_GZ, _progress)
    print(f"\nDecompressing...")
    with gzip.open(OUT_GZ, "rb") as f_in, open(OUT_FILE, "wb") as f_out:
        shutil.copyfileobj(f_in, f_out)
    OUT_GZ.unlink()
    print(f"Saved to {OUT_FILE}")

def _progress(block_num, block_size, total_size):
    downloaded = block_num * block_size
    if total_size > 0:
        pct = min(100, downloaded * 100 // total_size)
        print(f"\r  {pct}% ({downloaded:,} / {total_size:,} bytes)", end="", flush=True)

if __name__ == "__main__":
    main()
