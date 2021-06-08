# Enter your code here. Read input from STDIN. Print output to STDOUT

n,m = map(int, input().split())
all_array = []
happiness = 0

all_array.append(list(map(int, input().split())))
for _ in range(2):
    all_array.append(set(map(int, input().split())))
for i in all_array[0]:
    if i in all_array[1]: happiness+=1
    elif i in all_array[2]: happiness-=1
    else: pass
print(happiness)


