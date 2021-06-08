# Enter your code here. Read input from STDIN. Print output to STDOUT

import re


S = input().strip()
k = input().strip()

pattern = re.compile(r"(?={})".format(k))

matches = pattern.finditer(S)
myList = list(map(lambda x: x.start(), pattern.finditer(S)))

if myList:
    for match in myList:
        print(f"{match, match+len(k)-1}")
else:
    print("(-1, -1)")
	
	
	
	
	
#poor_coder 
	
import re
text, pattern = input(), input()
m= list(re.finditer("(?=(%s))"%pattern,text))
if not m:
    print((-1,-1))
for i in m:
    print((i.start(1),i.end(1)-1))