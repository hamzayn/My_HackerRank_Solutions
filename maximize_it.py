# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
K, M = list(map(int, input().split()))
myList = []
for _ in range(K):
    myList.append(list(map(lambda x: int(x)**2, input().split()[1:])))

print(max(map(lambda x: sum(x)%M, list(itertools.product(*myList)))))
