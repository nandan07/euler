#!/usr/bin/python3
import math
#import ipdb
#import helper
def digit(n):
    #ipdb.set_trace()
    r=1
    k=0
    rem=0
    while(r>0):
        k+=1
        r=n-(k*(9*(10**(k-1))))
        if r>0:
            n=r
        else:
            c=int(n/(k+1))
    curr_num=10**(k-1)+math.ceil(n/k)-1
    pos=(n-1)%k
    curr_num=str(curr_num)
    #return (k,n)
    return int(curr_num[pos])



#n,testdata=helper.readData("input")
n=int(input())

for i in range(n):
    testdata=input()
    data=testdata.split()
    pdt=1
    for x in data:
       pdt*=digit(int(x))
    print(pdt)

#ipdb.set_trace()
