def print_rangoli(size):
    # your code goes here
    alpha_list = list("abcdefghijklmnopqrstuvwxyz")
    p = sorted(alpha_list[:size], reverse = True)
	
    for x in range(1,size+1):
        myList = p[:x] + sorted(p[:x-1])
        print("-".join(myList).center(4*size-3, "-"))  
    for x in range(1,size):
        myList = p[:size-x] + sorted(p[:size-(x+1)])
        print("-".join(myList).center(4*size-3, "-"))


n = int(input())
print_rangoli(n)


