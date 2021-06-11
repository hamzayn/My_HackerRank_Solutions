import numpy

def generate_array(N,M):
    arr = []
    for _ in range (N):
        arr.append(list(map(int, input().split())))
    return arr
N,M = map(int, input().split())


a = numpy.array(generate_array(N,M))
b = numpy.array(generate_array(N,M))

print(a+b, a-b,a*b,a//b,a%b,a**b, sep = "\n")

