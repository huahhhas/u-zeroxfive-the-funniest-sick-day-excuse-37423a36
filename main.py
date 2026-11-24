#!/usr/bin/env python3
"""Write one funny sick-day excuse to /output/entry.txt."""

LINE = "Can't come in today \u2014 my smart lock changed its own password overnight and now it won't let me leave until I apologize to it."

def main():
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
