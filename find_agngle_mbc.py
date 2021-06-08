# Enter your code here. Read input from STDIN. Print output to STDOUT

import math
a = '\u00b0'

AB = int(input())
BC = int(input())
print(round(math.degrees(math.atan(AB/BC))), a, sep ='')
