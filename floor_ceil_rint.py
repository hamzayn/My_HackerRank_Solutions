import numpy

numpy.set_printoptions(legacy = "1.13")

a = numpy.array([x for x in input().split()],float)

print(numpy.floor(a), numpy.ceil(a), numpy.rint(a), sep = "\n")



