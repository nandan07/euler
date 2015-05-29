#!/usr/bin/python3
#import ipdb
#import helper

def factors_count(x):
    x=int(x)
    fact=set()
    for i in range(1,int(x**.5)+1):
        if x%i==0:
            f=x/i
            fact.add(i)
            fact.add(f)
    return len(fact)


def triangle_num(n):
    return int((n*(n+1))/2)

#n,testdata=helper.readData("input")
n=int(input())

for i in range(n):
    N=int(input())
    #N=int(testdata[i])
    t=N-1
    while(True):
        c=factors_count(triangle_num(t))
        if c>N:
            print(triangle_num(t))
            break
        else:
            t+=1
            if c-N > 100:
                t*=100
#ipdb.set_trace()
