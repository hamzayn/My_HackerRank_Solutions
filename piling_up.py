#
import re

# Enter your code here. Read input from STDIN. Print output to STDOUT

def checkIt(n, k):
    m = max(k[0], k[-1])
    ans = "Yes"
    while k:
        if max(k[0], k[-1]) <= m:
            m = max(k[0], k[-1])
            k.pop(0) if k[0]>= k[-1] else k.pop(-1)
        else:
            ans = "No"
            break
    print(ans)
    
for x in range(int(input())):
    n = int(input())
    k = list(map(int, input().split()))
    checkIt(n, k)
    


    