# Enter your code here. Read input from STDIN. Print output to STDOUT
import email.utils as k
import re

for _ in range(int(input())):
    myAdd = input().strip()
    
    
    if re.search(r"<[a-zA-Z][a-zA-Z0-9._-]+@[a-zA-Z]+\.[a-zA-Z]{1,3}>", myAdd):
        print(k.formataddr(k.parseaddr("%s"%(myAdd))))