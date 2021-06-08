import numpy

N = int(input())

mat_a = [list(map(int, input().split())) for _ in range(N)]
mat_b = [list(map(int, input().split())) for _ in range(N)]

print(numpy.matmul(mat_a, mat_b))

