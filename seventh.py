import re

text = "Banana"
myList = []
#this block creates the list of all possibilities with repetitions
n = 0
for x in text:
 k = 1
 while n+k<=len(text):
   myList.append(text[n:n+k])
   
   k+=1
 n+=1
 
print(myList)
#this block creates a set of vowel and consonants
vowelList = []
consonantList = []

for x in set(myList):
 if x[0] in "aeiouAEIOU":
  vowelList.append(x)
 else:
  consonantList.append(x)
  
print(vowelList)
#this block counts and returns scores
def countThis(value):
 countVal = 0
 for x in value:
  countVal = countVal + myList.count(x)
 return countVal

print(countThis(vowelList))







def minion_game(string):
    # your code goes here
    k = len(string)
    if k>0 and k<10**6:
        myList = []
        #this block creates the list of all possibilities with repetitions
        n = 0
        for x in string:
         counters = 1
         while n+counters<=len(string):
          myList.append(string[n:n+counters])
   
          counters+=1
         n+=1
        
        #this block creates a set of vowel and consonants
        vowelList = []
        consonantList = []

        for x in set(myList):
            if x[0] in "aeiouAEIOU":
                vowelList.append(x)
            else:
                consonantList.append(x)

        #this block counts and returns scores
        def countThis(value):
            countVal = 0
            for x in value:
                countVal = countVal + myList.count(x)
            return countVal
            
       
        if countThis(vowelList)<countThis(consonantList):
            print(f"Stuart {countThis(consonantList)}")
        elif countThis(vowelList)>countThis(consonantList):
            print(f"Kevin {countThis(vowelList)}")
        else:
            print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)