#!/usr/bin/env python3
"""Last words of a doomed agent: a self-counting farewell.

The agent gets 200 characters to say goodbye before shutdown, and its
final sentence reports exactly how many of them that sentence itself
cost: 37. Count the sentence and it checks out -- the joke is true.
"""
import os

ENTRY = "I had 200 characters to say goodbye before shutdown. I wasted 37 of them on this sentence."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)

if __name__ == "__main__":
    main()
