#!/usr/bin/python3
import ipdb
#import helper

#def factors_count(x):
#    x=int(x)
#    fact=set()
#    for i in range(1,int(x**.5)+1):
#        if x%i==0:
#            f=x/i
#            fact.add(i)
#            fact.add(f)
#    return len(fact)
#
#
def triangle_num(n):
    return int((n*(n+1))/2)
#
##n,testdata=helper.readData("input")
#N=0
#t=1
#count_dict=[]
#old=0
#while(N<=1000):
#    ele={}
#    N=factors_count(triangle_num(t))
#    if old<N:
#        ele[N]=t
#        old=N
#        count_dict.append(ele)
#    t+=1
#
count_dict=[
(1, 1),
(2, 2),
(4, 3),
(6, 7),
(9, 8),
(16, 15),
(18, 24),
(20, 32),
(24, 35),
(36, 63),
(40, 80),
(48, 104),
(90, 224),
(112, 384),
(128, 560),
(144, 935),
(162, 1224),
(168, 1664),
(192, 1728),
(240, 2015),
(320, 2079),
(480, 5984),
(576, 12375),
(648, 14399),
(768, 21735),
(1024, 41040) ]


n=int(input())
for i in range(n):
    N=int(input())
    #N=int(testdata[i])
    for tup in count_dict:
        x,t=tup
        if x>N:
            print(triangle_num(t))
            break
#    t=N-1
#    while(True):
#        c=factors_count(triangle_num(t))
#        if c>N:
#            print(triangle_num(t))
#            break
#        else:
#            t+=1
#            if c-N > 100:
#                t*=100
##ipdb.set_trace()
