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

#n,testdata=helper.readData("input")
n=int(input())
abundant=[]
for i in range(n):
    N=int(input())
    #N=int(testdata[i])
    if N>28123:
        print("YES")
    else:
        if len(abundant)<1:
            a=12
            for a in range(12,28125):
                if factors_sum(a)>a:
                    abundant.append(a)
        possible=False
        for x in range(len(abundant)-1):
            if abundant[x]>N:
                break
            for y in range(x,len(abundant)):
                if abundant[y]>N:
                    break
                if abundant[x]+abundant[y]==N:
                    possible=True
                    break
            if possible:
                break
        if possible:
            print("YES")
        else:
            print("NO")
#ipdb.set_trace()
