#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

    
myString = ""

for i in range(m):
    for j in range(n):
        myString = myString + matrix[j][i]

pattern = re.compile(r"([a-zA-Z0-9]+)([\s\W_]+)(?=[a-zA-Z0-9]+)")

matches = pattern.sub(lambda x: x.group(1) + " ", myString)

print(matches)





#solution from poorcoder

import re
x,y = list(map(int,input().split()))
rows =[input() for i in range(x)]
text = "".join([row[i] for i in range(y) for row in rows])
text = re.sub('([A-Za-z1-9])[^A-Za-z1-9]+([A-Za-z1-9])', r'\1 \2', text)
text = re.sub('  ', ' ', text)
print(text)
