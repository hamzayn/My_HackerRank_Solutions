# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
pattern = re.compile(r"[bcdfghjklmnpqrstvwxyz]([aeiou]{2,})(?=[bcdfghjklmnpqrstvwxyz])", re.I)
myObj = pattern.findall(input())
if myObj:
    for x in myObj:
        print(x)
else:
    print(-1)    
	
	
#the poorcoder solution
	
import re
v = "aeiou"
c = "qwrtypsdfghjklzxcvbnm"
print(*re.findall("(?=[%s]([%s]{2,})[%s])"%(c,v,c),input(), re.I) or [-1], sep="\n")
	
	
	
# Re.findall() & Re.finditer() in Python - Hacker Rank Solution from codeworld
# Python 3
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Re.findall() & Re.finditer() in Python - Hacker Rank Solution START
import re

Storage = re.findall(r'(?<=[qwrtypsdfghjklzxcvbnm])([aeiou]{2,})(?=[qwrtypsdfghjklzxcvbnm])', input().strip(), re.IGNORECASE)

if Storage:
    for i in Storage:
        print(i)
else:
    print(-1)
# Re.findall() & Re.finditer() in Python - Hacker Rank Solution END