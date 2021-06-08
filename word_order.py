#this is the life that we all want

# Enter your code here. Read input from STDIN. Print output to STDOUT

# Enter your code here. Read input from STDIN. Print output to STDOUT

word = []
wordy = ()
allwords = ""
for _ in range(int(input())):
    word.append(input().strip())
    
for i in word:
    if i not in wordy:
        wordy += i,
print(len(wordy))
print(*[word.count(k) for k in wordy])


#second solution by me
# Enter your code here. Read input from STDIN. Print output to STDOUT

vocab = {}
for x in range(int(input())):
    k = input().strip()
    if k in vocab.keys():
        vocab[k] += 1
    else:
        vocab[k] = 1
print(len(vocab.keys()))
print(*vocab.values())



# Enter your code here. Read input from STDIN. Print output to STDOUT from poorcoder

vocab = {}
for i in range(int(input())):
    value = input()
    if not vocab.get(value, None):
        vocab[value]= 1
    else:
        vocab[value]+= 1

print(len(vocab))
print(*vocab.values())