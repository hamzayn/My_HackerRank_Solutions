if __name__ == '__main__':
    n = int(input())
    
    if n in range(1,151):
        sum = []
        for x in range(1,n+1):
            sum.append(x)
        
    print(*sum, sep = "")
# this is for unpacking and printing an array of numbers

