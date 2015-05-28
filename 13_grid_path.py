#!/usr/bin/python3
#import ipdb
#import helper

def factoral(n):
    if n<2:
        return 1
    else:
        return n*factoral(n-1)
#n,testdata=helper.readData("input")
n=int(input())
for i in range(n):
    m,n=input().split()
    m=int(m)
    n=int(n)
    if m<n:
        t=m
        m=n
        n=t
    p=1
    for i in range(n):
        p*=m+n-i
    print(int(p/factoral(n))%1000000007)

#ipdb.set_trace()
#print("done")
