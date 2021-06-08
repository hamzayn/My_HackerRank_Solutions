# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque


N = int(input())
que = deque()
for x in range(N):
    a = list(map(str, input().split()))
    
    if a[0] == "append": que.append(a[1])
    elif a[0] == "appendleft": que.appendleft(a[1])
    elif a[0] == "pop": que.pop()
    else: que.popleft()
    
print(*que)