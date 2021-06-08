cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    a, b = 0, 1
    fib = []
    for _ in range(n):
        fib.append(a)
        a, b = b, a+b
    return fib
    # return a list of fibonacci numbers

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))