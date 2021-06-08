# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

def isValid(string):
    test = False
    list_ = re.findall("[A-Za-z0-9]", string)
    alpha = set(re.findall("[A-Z]", string))
    num = set(re.findall("[0-9]", string))
    if len(alpha)>=2 and len(num)>=3:
        for x in string:
            if x not in list_ or list_.count(x) > 1:
                test = False
                break
            else:
                test = True
    else:
        pass                    
    return test

T = int(input())
for i in range (T):
    UID = input().strip()
    if len(UID) != 10:
        print("Invalid")
    elif isValid(UID):
        print("Valid")
    else:
        print("Invalid")
		
		
		
import re
for _ in range(int(input())):
    uid = input()
    uid = "".join(sorted(uid))
    if (re.search(r"[A-Z]{2}",uid) and #2 uppercase alphabets
        re.search(r"\d{3}",uid) and #3+ digits
        not re.search(r"[^A-Za-z0-9]",uid) and #no nonalphanumeric
        not re.search(r"(\w)\1",uid) and #no repetition
        len(uid) == 10): #10 characters long
        print("Valid")
    else:
        print("Invalid")


