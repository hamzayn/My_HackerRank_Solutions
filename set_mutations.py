# Enter your code here. Read input from STDIN. Print output to STDOUT

num_A = int(input())
set_A = set(map(int, input().split()))

def mut_A(command, set_in):
    
    if command == "update": 
        set_A.update(set_in)
    elif command == "intersection_update": 
        set_A.intersection_update(set_in)
    elif command == "symmetric_difference_update":
        set_A.symmetric_difference_update(set_in)
    else:
        set_A.difference_update(set_in)
    
for x in range(int(input())):
    k,b = list(map(str, input().split()))
    c = set(map(int, input().split()))
    mut_A(k,c)
    
print(sum(set_A))