import numpy

arr = []

N, M = map(int, input().split())
for _ in range(N):
    arr.append(list(map(int, input().split())))

print(numpy.max((numpy.min(numpy.array(arr), axis=1))))


