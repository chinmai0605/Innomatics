# HackerRank Python Introduction Codes

# 1. Say "Hello, World!" With Python
var = "Hello, World!"
print(var)

# 2. Python If-Else
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    if(n&1!=0):
        print("Weird")
    else:
        if(2>=n or n<=5):
            print("Not Weird")
        elif(6>=n or n<=20):
            print("Weird")
        else:
            print("Not Weird")

# 3. Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)

# 4. Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)

# 5. Loops
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i*i)

# 6. Write a function
def is_leap(year):
    leap = False
    
    # Write your logic here
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
    return leap
    
    # if year % 400 ==0:
    #     return True
    # elif year % 100==0:
    #     return False
    # elif year % 4 ==0:
    #     return True
    # else:
    #     return False

year = int(input())
print(is_leap(year))

# 7. Print Function
if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        print(i,end="")
