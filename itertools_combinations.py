# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations

a,b = input().split()

a = sorted(list(a))


for i in range(1,int(b)+1):
    k = combinations(a,i)
    for j in k:
        print("".join(j))