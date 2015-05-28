#!/usr/bin/python3
#import ipdb
#import helper

#n,testdata=helper.readData("input")
n=int(input())
name=[]
for i in range(n):
    testdata=input()
    name.append(testdata)
    #del(testdata[0])
name.sort()
#n=int(testdata[0])
n=int(input())
#del(testdata[0])
for i in range(n):
    score=0
    testdata=input()
    ind=name.index(testdata)+1
    for p in range(len(testdata)):
        score+=ord(testdata[p])-64
    score*=ind
    print(score)

#ipdb.set_trace()
#print("done")
