def count_substring(string, sub_string):
    k = 0
    while sub_string in string:
        index = string.find(sub_string)
        string = string[:index] + "" +string[index+1:]
        k+=1
    return k

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)