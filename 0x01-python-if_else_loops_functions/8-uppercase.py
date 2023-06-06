#!/usr/bin/python3
def uppercase(str):
    temp = []
    for i in range(len(str)):
        if ord(str[i]) in range(ord('a'), ord('z')+1):
            upper_case = ord(str[i]) - 32
            temp.append(chr(upper_case))
        else:
            temp.append(str[i])
    print("{}".format(''.join(temp)))
