#!/usr/bin/python3
def uppercase(str):
    temp = []
    for i in range(len(str)):
        if ord(str[i]) in range(ord('A'), ord('Z')+1):
            temp.append(str[i])
        else:
            upper_case = ord(str[i]) - 32
            temp.append(chr(upper_case))
    return ''.join(temp)
