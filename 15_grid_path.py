#!/usr/bin/python3
import ipdb
import helper
import math


n,testdata=helper.readData("input")
#n=int(input())
for i in range(n):
    #m,n=input().split()
    m,n=testdata[i].split()
    m=int(m)
    n=int(n)
    v=math.factorial(m+n)/(math.factorial(m)*math.factorial(n))
    rem=int(v%(10**9+7))
    print(rem)

