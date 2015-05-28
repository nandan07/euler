#!/usr/bin/python3
import ipdb
import helper


def fact(x):
    if (x==1):
        return 1
    fact=set()
    x=int(x)
    i=2
    for i in range(1,int(x/2)+1):
        if x%i==0:
            fact.add(i)
            fact.add(int(x/i))
        else:
            i+=1
    return len(fact)
def triangle_gen():
    n=1
    new=fact(n)
    old=fact(n)
    while(new<100):
        t=n*(n+1)/2
        new=fact(t)
        if new>old:
            print(t)
        n+=1
        old=fact(t)

n,testdata=helper.readData("input")

ipdb.set_trace()

#n=int(input())
for k in range(n):

    print("test")    


print("test")    
