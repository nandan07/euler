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
    st=str(factoral(int(input())))
    s=0
    for i in range(len(st)):
        s+=int(st[i])
    print(s)

#
#ipdb.set_trace()
#print("done")
