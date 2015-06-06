#!/usr/bin/python3
#import ipdb
#import helper


def f_sum(x):
    if (x==1):
        return 1
    fact=set()
    fact.add(1)
    x=int(x)
    i=2
    for i in range(2,int(x**.5)+1):
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
n=int(input())
#n,testdata=helper.readData("input")
num=[220, 284, 1184, 1210, 2620, 2924, 5020, 5564, 6232, 6368, 10744, 10856, 12285, 14595, 17296, 18416, 63020, 66928, 66992, 67095, 69615, 71145, 76084, 79750, 87633, 88730]
for i in range(n):
    N=int(input())
    ans=0
    for x in num:
        if x<N:
            ans+=x
        else:
            break
    print(ans)
