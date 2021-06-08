def merge_the_tools(string, k):
    # your code goes here
    
    
    for i in range(0,len(string),k):
        myList = []
        subStr = string[i:i+k]
        for i in subStr:
            if i not in myList:
                myList.append(i)
                print(i, end="")
                
        print()
        
   

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)