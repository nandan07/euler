#!/usr/bin/python3
#import ipdb
#import helper
import math

def fib_term(N):
    Phi = float(1.618033988)
    n=(N-1+0.5*math.log10(5))/math.log10(Phi)
    return math.ceil(n)




#n,testdata=helper.readData("input")
n=int(input())

for i in range(n):
    #t=fib_term(int(testdata[i]))
    t=fib_term(int(input()))
    print(t)

#ipdb.set_trace()
#print("done")
