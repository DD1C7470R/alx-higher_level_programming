#!/usr/bin/python3
import sys
if __name__ == "__main__":
    a_s = len(sys.argv[1:])
    if a_s == 1:
        print("{} {}{}".format(a_s, "argument", ":"))
    else:
        print("{} {}{}".format(a_s, "arguments", ":" if a_s > 0 else "."))
    for arg in range(a_s):
        print("{}: {}".format(arg+1, sys.argv[arg + 1]))
