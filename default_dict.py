# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import defaultdict

n,m = map(int, input().split())

myArray = defaultdict(list)

for x in range(n):myArray["group A"].append(input().strip())
for x in range(m):myArray["group B"].append(input().strip())

for word in myArray["group B"]:
    for i in range(n):
        if word in myArray["group A"]:
            if word == myArray["group A"][i]:
                print(i+1, end = " ")
        else:
            print(-1)
    print()
	
	
	

# Enter your code here. Read input from STDIN. Print output to STDOUT ## more efficient

from collections import defaultdict

n,m = map(int, input().split())

myArray = defaultdict(list)

for i in range(n):
    myArray[input()].append(i+1)
for i in range(m):
    print(*myArray[input()] or [-1])