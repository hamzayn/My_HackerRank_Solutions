# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations

k = int(input())
myList = list(combinations(input().split(), int(input())))

count = 0

for i in myList:
    if "a" in i:
        count +=1

print(round(count/len(myList), 3))