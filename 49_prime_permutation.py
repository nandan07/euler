#!/usr/bin/python
import ipdb
import itertools
import helper

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
def getdigitkey(n):
    digit = "".join(sorted(str(n), reverse=True))
    return int(digit)
#onlt consider the concecutive numbers.. 
def isAP(ar,l):
    cd={}
    for i in range(len(ar)-1):
        key=ar[i+1]-ar[i]
        cd.setdefault(key,set())
        cd[key].add(ar[i])
        cd[key].add(ar[i+1])
    ipdb.set_trace()
    for x in cd:
        if len(cd[x])==l:
            return sorted(cd[x])



n,testdata=helper.readData("input")
#n=int(testdata[x])
N,K=testdata[0].split()
N=int(N)
K=int(K)
prime={}
ar=[1487, 1847, 4817, 4871, 7481, 7841, 8147, 8741]
isAP(ar,K)
for n in range(10,N+1):
    if isPrime(n):
        prime.setdefault(getdigitkey(n),set())
for key in prime:
    num=itertools.permutations(sorted(str(key)))
    for p in num:
        p=int("".join(p))
        if len(str(p))==len(str(key)):
            if isPrime(p):
                prime[key].add(p)
    if len(prime[key])>=K:
       ar=sorted(prime[key])

ipdb.set_trace()
