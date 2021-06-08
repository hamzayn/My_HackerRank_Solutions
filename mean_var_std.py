import numpy

N,M = map(int, input().split())
myArray = numpy.array([list(map(int, input().split())) for _ in range(N) ])

print(numpy.mean(myArray, axis=1))
print(numpy.var(myArray, axis=0))
print(round(numpy.std(myArray), 11))