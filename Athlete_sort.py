#!/bin/python3

import math
import os
import random
import re
import sys


def checkSort(check):
    return check[k]
        
    


if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    
    arr.sort(key = checkSort)
    
    for i in arr:
        for j in range(m):
            print(f"{i[j]} ", end="")
        print()
    
