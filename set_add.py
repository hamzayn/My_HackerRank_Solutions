# Enter your code here. Read input from STDIN. Print output to STDOUT
m = set()
for _ in range(int(input())):
    m.add(input().strip())
print(len(m))




#this is solution number II

# Enter your code here. Read input from STDIN. Print output to STDOUT
m = tuple()
for _ in range(int(input())):
    r = input().strip()
    if r not in m:
        m+=r,
print(len(m))