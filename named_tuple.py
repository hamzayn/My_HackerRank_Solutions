# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

N = int(input())
Student = namedtuple('Student', input().split())


marks = [Student(*input().split()).MARKS for i in range(N)]

print(sum(map(int, marks))/N)
   