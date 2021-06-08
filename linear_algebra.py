import numpy


N = []

for _ in range(int(input())):
    N.append(list(map(float, input().split())))

print(round(numpy.linalg.det(N), 2))
    


