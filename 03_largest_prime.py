#!/usr/bin/python3
#import ipdb
#import helper

def isPrime(x):
    x=int(x)
    for i in range(2,int(x**.5)+1):
        if x%i ==0 :
            return False
    return True

def factors(x):
    x=int(x)
    fact=1
    for i in range(2,int(x*.5)+1):
        if x%i==0:
            if isPrime(i) and fact<i:
                fact=i
    print(fact)


#n,testdata=helper.readData("input")
n=int(input())
testdata=[]
for xx in range(n):
    testdata=input()
    if isPrime(testdata):
        print(testdata)
    else:
        factors(testdata)

