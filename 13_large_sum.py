#!/usr/bin/python3
#import ipdb
#import helper

#n,testdata=helper.readData("input")
n=int(input())
ans=0
for i in range(n):
        ans+=int(input())
print(str(ans)[0:10])
