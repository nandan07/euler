#!/usr/bin/python3
#import ipdb
import itertools

n=int(input())+1
prime=[2,3,5,7,11,13,17]
digit='0123456789'
pandigit=itertools.permutations(digit[:n])
ans=0
for x in pandigit:
    div=True
    for w in range(n-3):
        x="".join(x)
        #ipdb.set_trace()
        if not int(x[w+1:w+4])%prime[w]==0:
           div=False
           break
    if div:
        ans+=int(x)
print(ans)
