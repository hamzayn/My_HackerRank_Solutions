#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    result = ""
    k = len(s)
    if k > 0 and k < 1000:
        word_list = s.split(" ")
        print(word_list)
        for words in word_list:
            if len(result) > 0:
                result = result + " " + words.strip().capitalize()
            
            else:
                result = words.capitalize()
    if not result:
        return s
    else:
        return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
