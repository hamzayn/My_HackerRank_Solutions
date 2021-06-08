# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

sum_ = 0
shoe_num = int(input())

k = list(map(int, input().split()))

for _ in range(int(input())):
    
    size, cost = list(map(int, input().split()))
    if size in k and k.count(size) > 0:
        k.remove(size)
        sum_ += cost

print(sum_)