#!/usr/bin/python3
#import ipdb
#import helper

def isPrime(x):
    x=int(x)
    for i in range(2,int(x**.5)+1):
        if x%i ==0 :
            return False
    return True

def isPandigit(x):
    x=str(x)
    n=len(x)
    for p in range(1,n+1):
        if x.find(str(p))<0:
            return False
    return True
        


#n,testdata=helper.readData("input")
n=int(input())
for x in range(n):
    ans=[]
    #N=int(testdata[x])
    N=int(input())
    for i in range(2,N):
        if isPandigit(str(i)):
            if isPrime(str(i)):
                ans.append(str(i))
    print("".join(ans))

