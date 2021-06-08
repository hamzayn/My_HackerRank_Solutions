# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

pattern = re.compile(r'([a-zA-Z0-9])(?=\1)')
myMatch = pattern.search(input().strip())

print(myMatch.group(1)) if myMatch else print(-1)

