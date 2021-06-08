# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
Nlist = [x for x in input().split()]
print(all([int(x) >= 0 for x in Nlist]) and any([x == x[::-1] for x in Nlist]))