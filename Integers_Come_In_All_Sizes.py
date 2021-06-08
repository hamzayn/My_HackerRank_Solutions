# Enter your code here. Read input from STDIN. Print output to STDOUT
k = []
for i in range(4):
    k.append(int(input()))

print(f"{pow(k[0],k[1]) + pow(k[2], k[3])}")