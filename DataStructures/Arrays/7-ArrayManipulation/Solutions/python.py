#!/bin/python3

import sys

iniArray = []

def manipulateArray(n,m,queries):
    iniArray[:n] = [0]*n
    maxVal = 0
    actualVal = 0

    for z in range(m):
        currentQuery = queries[z]
        a = currentQuery[0]
        b = currentQuery[1]
        k = currentQuery[2]

        iniArray[(a-1)] += k
        if b < n:
            iniArray[b] -= k
        

    for r in iniArray:
    	actualVal += r
    	if actualVal > maxVal:
        	maxVal = actualVal

    print(maxVal)

    
if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    queries = []
    for a0 in range(m):
        arr = list(map(int, input().strip().split(' ')))
        queries.append(arr)
    manipulateArray(n,m,queries)
