#!/usr/bin/python
import math
#import ipdb
#import helper

def isPrime(x):
    x=int(x)
    if x<2:
        return False
    for i in range(2,int(x**.5)+1):
        if x%i ==0 :
            return False
    return True

def nextPrime(p):
    while(True):
        p+=1
        if isPrime(p):
            return p


#n,testdata=helper.readData("input")
n=int(input())
for x in range(n):
    #n=int(testdata[x])
    n=int(input())
    ans=0
    p=1
    while(p<n):
        sq=int(math.sqrt((n-p)/2))
        if isPrime(p) and (n==p+2*(sq**2)):
            ans+=1
        p=nextPrime(p)
    print(ans)
