# Enter your code here. Read input from STDIN. Print output to STDOUT

a, b = list(map(int, input().split()))
m = range(1,(a+1)//2)

def gen(k):
    for i in k:
        n = "." + "..".join(["|"]*(2*i-1)) + "."
        
        print(n.center(b, "-"))

gen(m)
print("WELCOME".center(b, "-"))
gen(m[::-1])
