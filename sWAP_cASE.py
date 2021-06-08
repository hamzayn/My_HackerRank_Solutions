def swap_case(s):
    string = ""
    for k in s:
        if k.isupper():
            string+=k.lower()
        else:
            string+=k.upper()
    return string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)