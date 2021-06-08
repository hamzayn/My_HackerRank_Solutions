# Enter your code here. Read input from STDIN. Print output to STDOUT
from cmath import phase

z = complex(input())
print("%.3f\n%.3f"%(abs(z), phase(z)))