#!/usr/bin/python3
#import ipdb
#import helper

def factors_sum(x):
    x=int(x)
    fact=set()
    fact.add(1)
    for i in range(2,int(x**.5)+1):
        if x%i==0:
            f=x/i
            fact.add(i)
            fact.add(f)
    su=0
    for f in fact:
        su+=f
    return int(su)

abundant_ar=[]
abundant_set=set()
for i in range(1,28125):
    if factors_sum(i)>i:
        abundant_set.add(i)
        abundant_ar.append(i)
n=int(input())
#n,testdata=helper.readData("input")
for i in range(n):
    N=int(input())
    find=False
    if N>28123:
        print("YES")
        continue
    for j in abundant_ar:
        if j<N:
            if N-j in abundant_set:
                find=True
                break
        else:
            break
    if find:
        print("YES")
    else:
        print("NO")



