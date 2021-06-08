import numpy as k
N,M,P = map(int, input().split())

list_a, list_b = [], []

for _ in range(N):
    list_a.append(list(map(int, input().split())))
    
for _ in range(M):
    list_b.append(list(map(int, input().split())))
    
print(k.concatenate((k.array(list_a), k.array(list_b))))
