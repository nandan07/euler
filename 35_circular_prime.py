#!/usr/bin/python3
#import ipdb
#import helper
#

def isPrime(x):
    x=int(x)
    if x<2:
        return False
    for i in range(2,int(x**.5)+1):
        if x%i ==0 :
            return False
    return True

        


#n,testdata=helper.readData("input")
N=int(input())
#testdata=input()
#N=int(testdata[0])
ans=0
for i in range(N,1,-1):
    prime=True
    if isPrime(i):
        i_str=str(i)
        for p in range(len(i_str)):
            rot=int(i_str[p:]+i_str[:p])
            if not isPrime(rot):
                prime=False
                break
        if (prime):
            ans+=i
print(ans)


