# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

items_ = OrderedDict()
for _ in range(int(input())):
    *item, cost = input().split()
    item = " ".join(item)
    
    if item not in items_:
        items_[item] = int(cost)
    else:
        items_[item] += int(cost)
for x in items_: print(x,items_[x] )