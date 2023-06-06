#!/usr/bin/python3
import random
number = random.randint(-1000, 1000)
last_num = (abs(number)) % 10
if last_num > 5:
    print(f"The last digit of {number} is {last_num} and is greater than 5")
elif last_num == 0:
    print(f"The last digit of {number} is {last_num} and is zero")
else:
    print(f"The last digit of {number} is {last_num} and is less than 6 and not 0")
     
