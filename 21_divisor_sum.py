#!/usr/bin/python3
import ipdb
import helper

def isPrime(x):
    x=int(x)
    if x<2:
        return False
    for i in range(2,int(x**.5)+1):
        if x%i ==0 :
            return False
    return True

def f_sum(x):
    if (x==1):
        return 1
    fact=set()
    fact.add(1)
    x=int(x)
    i=2
    for i in range(1,int(x**.5)+1):
        if x%i==0:
            f=int(x/i)
            fact.add(i)
            fact.add(f)
        else:
            i+=1
    su=0
    for x in fact:
        su+=x
    return su

#n=int(input())
n,testdata=helper.readData("input")

for i in range(n):
    num=set()
    xx=int(testdata[i])
    for x in range(1,xx):
        if not isPrime(x) :
            a=f_sum(x)
            if a<xx:
                if x==f_sum(a) and a!=x:
                    num.add(x)
    su=0
    for k in num:
        su+=k
    print(su)
ipdb.set_trace()
print("done")
