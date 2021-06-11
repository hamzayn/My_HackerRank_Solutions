import numpy

N,M = map(int, input().split())

array_ = []
for _ in range(N):
    array_.append(list(map(int, input().split())))
array_ = numpy.array(array_)

print(numpy.transpose(array_), array_.flatten(), sep = "\n")

