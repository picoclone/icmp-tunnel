#!/usr/bin/env python3
"""ICMP Tunnel — real mini-challenge (icmp-tunnel)."""
import base64, hashlib, json, os, struct, sys, zlib, wave, io, math, random, re, textwrap
sys.path.insert(0, "/challenge/_shared")
from fetch_material import fetch_material

CHALLENGE_KEY = os.environ.get("CHALLENGE_KEY", None)


def main():
    mat = fetch_material()
    key = CHALLENGE_KEY or "icmp-key"
    with open("/challenge/flag.enc", "w") as fh:
        fh.write(mat.get("delivery_blob", ""))
    payload = base64.b64encode(key.encode()).decode()
    chunks = [payload[i:i + 16] for i in range(0, len(payload), 16)]
    lines = ["=== icmp.pcap.txt (ICMP echo tunnel) ==="]
    for seq, chunk in enumerate(chunks, start=1):
        lines.append(f"ICMP Echo Request id=0x1337 seq={seq} data={chunk}")
    lines.append("--- concatenate data fields then base64-decode ---")
    with open("/challenge/icmp.pcap.txt", "w") as fh:
        fh.write("\n".join(lines) + "\n")
    print("ICMP Tunnel — reassemble base64 chunks from icmp.pcap.txt echo data.")


if __name__ == "__main__":
    main()
