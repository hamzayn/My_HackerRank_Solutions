# Enter your code here. Read input from STDIN. Print output to STDOUT
a,b = int(input()), int(input())

print("{}\n{}\n{}".format(a//b, a%b, divmod(a,b)))