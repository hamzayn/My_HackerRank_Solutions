# Enter your code here. Read input from STDIN. Print output to STDOUT

for _ in range(int(input())):
    try:
        a,b = [int(x) for x in input().split()]
        print(int(a/b))
    except ZeroDivisionError as z:
        print("Error Code: integer division or modulo by zero")
    except ValueError as v:
        print("Error Code:", v)