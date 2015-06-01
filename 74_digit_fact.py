#!/usr/bin/python3
import ipdb
import helper
import itertools
import math


def digit_factorial_sum(n):
    ipdb.set_trace()
    s=str(n)
    su=0
    for d in s:
        su+=math.factorial(int(d))
    return su


#n,testdata=helper.readData("input")
#n=int(input())
testdata=[]
end=1000000
#for i in range(n):
#    testdata.append(input())
#    if end <int(testdata[-1].split()[0]):
#        end=int(testdata[-1].split()[0])
digit_ser={}
for key in range(end+1):
    i=key
    digit_ser.setdefault(key,[])
    sr=set()
    sr.add(i)
    while(len(sr)<60):
        next_num=digit_factorial_sum(i)
        if next_num in sr:
            break
        else:
            sr.add(next_num)
            i=next_num
    digit_ser[key]=sr
ipdb.set_trace()
#for i in range(n):
#    N,L=testdata[i].split()
#    N=int(N)
#    L=int(L)
#    ans=[]
#    for p in range(N+1):
#    #    ipdb.set_trace()
#        sr=set()
#        length=-1
#        c=p
#        sr.add(c)
#        while(len(sr)<L+1):
#            next_num=digit_factorial_sum(c)
#            if next_num in sr:
#                break
#            else:
#                sr.add(next_num)
#                c=next_num
#        if len(sr)==L:
#            #ipdb.set_trace()
#            ans.append(str(p))
#
#    #ipdb.set_trace()
#    if len(ans)>0:
#        print(" ".join(ans))
#    else:
#        print('-1')
#
#ipdb.set_trace()
