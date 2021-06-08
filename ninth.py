# Enter your code here. Read input from STDIN. Print output to STDOUT
S = input()
store = list()
for i in range(len(S)):
    if i == len(S) - 1:
        if S[i] not in store:
            if store:
                print("(%s, %s) "%(len(store), store[0]), end="")
                store.clear()
                store.append(S[i])
                print("(%s, %s) "%(len(store), store[0]), end="")
            else:
                store.append(S[i])
                print("(%s, %s) "%(len(store), store[0]), end="")
        else:
            store.append(S[i])
            print("(%s, %s) "%(len(store), store[0]), end="")
    else:
        if S[i] not in store:
            if store:
                print("(%s, %s) "%(len(store), store[0]), end="")
                store.clear()
                store.append(S[i])
            else:
                store.append(S[i])
        else:
            store.append(S[i])
