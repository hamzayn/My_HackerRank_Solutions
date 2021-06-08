
def check_validity(string):
    isalnum = isal = isdigit = islow = isupper = False
    for x in string:
        if x.isalnum(): isalnum = True
        if x.isalpha(): isal = True
        if x.isdigit(): isdigit = True
        if x.islower(): islow = True
        if x.isupper(): isupper = True
    return isalnum, isal,isdigit,islow,isupper


if __name__ == '__main__':
    s = input()
    
    print(*check_validity(s), sep="\n")
    
    