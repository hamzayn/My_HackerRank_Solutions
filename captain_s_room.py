# Enter your code here. Read input from STDIN. Print output to STDOUT
K = int(input())

m = dict()

for x in input().split():
    if x not in m:
        m[x] = 1
    else:
        m[x]+=1

for i in m.keys():
    if m[i] == 1:print(int(i))