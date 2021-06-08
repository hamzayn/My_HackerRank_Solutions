# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
N = int(input())

pattern = re.compile(r"(?<=\s)(\|\||&&)(?=\s)")

def replacement(k):

    if k.group(1) != "&&":
        return "or"
    else:
        return "and"
        
totalinput = ""
for _ in range(N):
    totalinput += input().rstrip() + "\n"

newstring = pattern.sub(replacement, totalinput)
print(newstring)
    
