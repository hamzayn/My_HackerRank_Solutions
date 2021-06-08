# Enter your code here. Read input from STDIN. Print output to STDOUT
M = int(input())
M_set = set(list(map(int, input().split())))
N = int(input())
N_set = set(list(map(int, input().split())))

print(*sorted(list(M_set^N_set)),sep = "\n")