
def evaluate(x,y,z):
    if x=="insert": z.insert(int(y[0]), int(y[1]))
    elif x == "print": print(z)
    elif x == "remove": z.remove(int(y[0]))
    elif x == "append": z.append(int(y[0]))
    elif x == "sort": z.sort()
    elif x == "pop": z.pop()
    elif x == "reverse": z.reverse()
    
    
if __name__ == '__main__':
    N = int(input())
    global myArray
    myArray = []
    for _ in range(N):
        command, *det = input().split()
        evaluate(command, det, myArray)
    