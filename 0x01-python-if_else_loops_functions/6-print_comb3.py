#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i, 10):
        if i != j and i != 8:
            print(f"{i}{j}", end=", ")
            if i == 8 and j == 9:
                print(f"{i}{j}")
