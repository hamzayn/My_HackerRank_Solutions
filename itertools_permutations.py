# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import permutations

a,b = input().split()
k = sorted(permutations(a,int(b)))
for i in k:
    print("".join(i))