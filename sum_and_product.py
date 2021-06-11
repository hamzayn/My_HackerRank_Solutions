import numpy

N,M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append([int(x) for x in input().split()])

print(numpy.product(numpy.sum(arr, axis= 0)))

