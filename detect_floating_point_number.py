# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for _ in range(int(input())):
    print(bool(re.match(r"^[+-]?\d*\.\d+$", input().strip())))