#!/usr/bin/python3
#import ipdb
#import helper
import math

N=int(input())
ans=0
for x in range(N,10,-1):
    x_str=str(x)
    su=0
    for p in range(0,len(x_str)):
        su+=math.factorial(int(x_str[p]))
    if su%x == 0:
        ans+=x
print(ans)
            
