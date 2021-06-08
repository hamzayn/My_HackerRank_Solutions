# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

a = []
for _ in range(2):
    a.append(list(map(int, input().split())))

print(*product(*a))