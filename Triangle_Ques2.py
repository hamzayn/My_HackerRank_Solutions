


#using no for loops

for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(sum(list(map(lambda x:x*pow(10,2*i-x-1)+x*pow(10,x-1),range(1,i))))+i*pow(10,i-1))
	
	
	
	
#using two for loops

for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(sum([x*pow(10,2*i-x-1)for x in range(1,i+1)])+sum([x*pow(10,x-1)for x in range(i-1,0,-1)]))



#using one for loop

for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(sum([x*pow(10,2*i-x-1)+x*pow(10,x-1) for x in range(1,i)])+i*pow(10,i-1))