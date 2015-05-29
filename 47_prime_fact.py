#!/usr/bin/python3
import ipdb
import helper

def isPrime(x):
    x=int(x)
    for i in range(2,int(x**.5)+1):
        if x%i ==0 :
            return False
    return True

def prime_factors(x):
    x=int(x)
    fact=set()
    if x==2:
        fact.add(2)
        return fact
    for i in range(2,int(x**.5)+2):
        if x%i==0:
            f=x/i
            if isPrime(i):
                fact.add(i)
            if isPrime(f):
                fact.add(f)
    return len(fact)


n,data=helper.readData("input")
#n=int(input())
#N,K=input().split()
N,K=data[0].split()
N=int(N)
K=int(K)
n=2
while(n<N+1):
    window=True
    for p in range(K):
        if not prime_factors(n+p)==K:
            window=False
            break
    if window:
        print(n)
        n+=1
    else:
        n+=p+1

#ipdb.set_trace()
