# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations_with_replacement

a,b = input().split()
a = sorted(list(a))
k = combinations_with_replacement(a,int(b))
for i in k:
    print("".join(i))