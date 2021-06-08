# Enter your code here. Read input from STDIN. Print output to STDOUT

for _ in range(int(input())):
    size_A = int(input())
    set_A = set(map(int, input().split()))
    size_B = int(input())
    set_B = set(map(int, input().split()))
    print(set_A.issubset(set_B))