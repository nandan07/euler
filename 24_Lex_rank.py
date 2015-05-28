#!/usr/bin/python3
import ipdb
import helper
import math

n,testdata=helper.readData("input")
#n=int(input())

for i in range(n):
    #testdata=input()
    #ipdb.set_trace()
    ans=''
    char="a b c d e"
    char=char.split()
    r=int(testdata[i])
    s=len(char)
    while(r>0):
        print('r-'+str(r))
        p=int(r/math.factorial(s))
        ans+=char[p]
        print('p-'+str(p))
        print('ans-'+str(ans))
        char.remove(char[p])
        r=r%math.factorial(s)
        s-=1
    print(ans)
    while(len(char)>0):
        ans+=char[0]
        char.remove(char[0])
    print(ans)

ipdb.set_trace()
print("done")
