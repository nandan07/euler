#!/usr/bin/python3
#import ipdb
#import helper
import math

#n,testdata=helper.readData("input")
n=int(input())

for i in range(n):
    testdata=input()
    n=int(testdata)-1
    char="abcdefghijklm"
    char_ar=sorted(char)
    out=''
    for c in range(len(char_ar)-1,-1,-1):
        p=int(n/math.factorial(c))
        out+=char[p]
        if len(char)>0:
            char=char[:p]+char[p+1:]
        n=n%math.factorial(c)
    print(out)
