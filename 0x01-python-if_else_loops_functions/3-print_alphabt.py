#!/usr/bin/python3
for c in range(ord('a'), ord('z') + 1):
    if chr(c) == 'q' or chr(c) == 'e':
        pass
    else:
        print("{}".format(chr(c)), end="")
