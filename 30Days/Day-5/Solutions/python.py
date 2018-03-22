#!/bin/python3

import sys


n = int(input().strip())
for x in range(1,11):
    print(str(n) +" x "+str(x) + " = " + str(x*n))