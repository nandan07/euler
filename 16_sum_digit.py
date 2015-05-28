#!/usr/bin/python3
#import ipdb
#import helper

#n,testdata=helper.readData("input")
n=int(input())
for i in range(n):
    st=str(2**(int(input())))
    ans=0
    s=0
    for j in range(len(st)):
        s+=int(st[j])
    print(s)
