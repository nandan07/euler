#!/usr/bin/python3
#import ipdb
#import helper

N=int(input())
rem=0
ans=0
for x in range(1,N+1):
    rem+=(x**x)%10000000000
    rem%=10000000000
print(rem)
