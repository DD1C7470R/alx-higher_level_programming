#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arg_size = len(sys.argv[1:])
    print("{} {}{}".format(arg_size, "argument" if arg_size == 1 else "arguments", ":" if arg_size > 0 else "."))
    for arg in range(arg_size):
        print("{}: {}".format(arg+1, sys.argv[arg + 1]))
