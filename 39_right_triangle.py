#!/usr/bin/python3
import ipdb
import helper
import time
import math


def is_square(n):
    r=math.sqrt(n)
    if (int(r)**2==n):
        return int(r)
    else:
        return -1
st=time.clock()
n,testdata=helper.readData("input")
#n=int(input())
#testdata=input()
for i in range(n):
    T=int(testdata[i])
    #N=int(input())
    side={}
    a=1

    for a in range(1,int(T/2)):
        for b in range(1,T-a):
            if a**2+(b**2) >=T**2:
                break
            c=a**2+(b**2)
            c=is_square(c)
            if  c>0:
                if a+b+c<=T:
                    side.setdefault(a+b+c,set())
                    side[a+b+c].add(a*b*c)
                else:
                    break
    print(time.clock()-st)
    ipdb.set_trace()
