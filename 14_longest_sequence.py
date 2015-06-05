#!/usr/bin/python3
#import ipdb
##import helper
#import time
#
#def seq_len(n):
#    if n==1:
#        return 1
#    length=0
#    if n%2==0:
#        n=n/2
#    else:
#        n=(3*n)+1
#    length+=1
#    return (length+seq_len(n))
#
#def next_term(n):
#    if n%2==0:
#        return int(n/2)
#    else:
#        return (3*n)+1
#
#
#st=time.clock()
#seq=[]
#maxlen=0
#change_ar=[]
#seq.append(0)
#seq.append(1)
#st=time.clock()
#for i in range(2,5*10**6):
#    l=1
#    c=i
#    while next_term(c)>i:
#        l+=1
#        c=next_term(c)
#    seq.append(seq[next_term(c)]+l)
#    if seq[next_term(c)]+l>=maxlen:
#        maxlen=seq[next_term(c)]+l
#        change_ar.append(i)
#print(time.clock()-st)
#ipdb.set_trace()
##n,testdata=helper.readData("input")
ans_ar=[2, 3, 6, 7, 9, 18, 19, 25, 27, 54, 55, 73, 97, 129, 171, 231, 235, 313, 327, 649, 654, 655, 667, 703, 871, 1161, 2223, 2322, 2323, 2463, 2919, 3711, 6171, 10971, 13255, 17647, 17673, 23529, 26623, 34239, 35497, 35655, 52527, 77031, 106239, 142587, 156159, 216367, 230631, 410011, 511935, 626331, 837799, 1117065, 1126015, 1501353, 1564063, 1723519, 2298025, 3064033, 3542887, 3732423]

n=int(input())
for i in range(n):
    N=int(input())
    for x in ans_ar:
        if x<=N:
            ans=x
        else:
            break
    print(ans)



