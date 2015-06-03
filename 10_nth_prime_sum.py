#!/usr/bin/python3
#import ipdb
#import helper
#import time

def isPrime(x):
    x=int(x)
    if x<2:
        return False
    for i in range(2,int(x**.5)+1):
        if x%i ==0 :
            return False
    return True


def get_primes(n):
    num=set()
    prime={}
    su=0
    for i in range(2,n+1):
        num.add(i)
    l=len(num)
    while(l>0):
        p=num.pop()
        su+=p
        prime[p]=su
        i=2
        while(i*p<=n+1):
            if i*p in num:
                num.remove(i*p)
            i+=1
        l=len(num)
    return prime

n=int(input())
testdata=[]
#n,data=helper.readData("input")
max_n=0
for i in range(n):
    x=int(input())
    if x<=max_n:
        testdata.append(x)
    else:
        max_n=x
        testdata.append(x)
prime=get_primes(max_n)
for x in testdata:
    ans=0
    large=0
    for p in range(x,2,-1):
        if p in prime:
            ans=prime[p]
            break
    print(ans)
