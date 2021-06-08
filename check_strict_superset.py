# Enter your code here. Read input from STDIN. Print output to STDOUT

superset = set(map(int, input().split()))
checkList = []
for _ in range(int(input())):
    subset = set(map(int, input().split()))
    checkList.append(subset.issubset(superset) and len(superset)>len(subset))
print(all(checkList))