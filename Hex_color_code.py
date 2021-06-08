# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

pattern = re.compile(r"\{[^{}]*\}")
pattern2 = re.compile(r"(#[a-fA-F\d]{6}|#[a-fA-F\d]{3})")
myStr = ""
myStr2 = ""
for _ in range(int(input())):
    myStr += input().strip() + "\n"
    
myList =  pattern.findall(myStr)
for x in myList:
    myStr2+=x+"\n"

myList = pattern2.findall(myStr2)
for m in myList:
    print(m)



#solution from codeworld
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

T = int(input())
in_css = False
for _ in range(T):
    s = input()
    if '{' in s:
        in_css = True
    elif '}' in s:
        in_css = False
    elif in_css:
        for color in re.findall('#[0-9a-fA-F]{3,6}', s):
            print(color)
    

    