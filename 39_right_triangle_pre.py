#!/usr/bin/python
import ipdb
ans=[12,60,120,240,420,720,840,1680,2520,4620,5040,9240,18480,27720,55440,110880,120120,166320,180180,240240,360360,720720,1081080,14414402162160,2882880,3603600,4084080]

t=int(input())
for i in range(t):
    N=int(input())
    curr=12
    for x in ans[1:]:
        if x>N:
            break
        else:
            curr=x
    print(curr)


#ipdb.set_trace()
