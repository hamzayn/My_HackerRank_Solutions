def print_formatted(number):
    # your code goes here
    l = len(bin(number)) - 2
    
    for x in range(1,number+1):
        print("%s %s %s %s"%(f"{x}".rjust(l),oct(x)[2:].rjust(l),hex(x)[2:].rjust(l).upper(),bin(x)[2:].rjust(l))) 

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)