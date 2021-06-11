import numpy

N= tuple(map(int, input().split()))

print(numpy.zeros(N, dtype= numpy.int),numpy.ones(N, dtype= numpy.int),sep = "\n")
