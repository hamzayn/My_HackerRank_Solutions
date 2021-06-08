n = int(input())
s = set(map(int, input().split()))

def command(*k):
    if k[0] == "remove": s.remove(int(k[1]))
    elif k[0] == "pop": s.pop()
    elif k[0] == "discard": s.discard(int(k[1]))

for _ in range(int(input())):
    command(*input().split())
    
print(sum(s))