# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
paper_1 = int(input())
roll_1 = set(map(int, input().split()))
paper_2 = int(input())
roll_2 = set(map(int, input().split()))
print(len(roll_1-roll_2))