#!/usr/bin/python3
import ipdb
import helper



power=set()
n=int(input())
testdata=n
for i in range(2,int(testdata)+1):
    for j in range(2,int(testdata)+1):
        power.add(i**j)
print(len(power))





ipdb.set_trace()
print("test")    
