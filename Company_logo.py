#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    s = input()
    k = {}   
    for i in s:
        if i not in k:
            k[i] = 1
        else:
            k[i] += 1

    m = list(k.keys())
    m.sort()
    m.sort(key = lambda x: k.get(x), reverse= True)
    print(m[0], k[m[0]]); print(m[1], k[m[1]]); print(m[2], k[m[2]])
