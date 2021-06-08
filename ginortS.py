# Enter your code here. Read input from STDIN. Print output to STDOUT
import re


S = input()
myList = []
myList.append(re.findall("[a-z]", S))
myList.append(re.findall("[A-Z]", S))
myList.append(re.findall("[13579]", S))
myList.append(re.findall("[02468]", S))

for x in myList: x.sort()
finalList = []
for x in myList:
    finalList.extend(x)

print(*finalList, sep = "")


