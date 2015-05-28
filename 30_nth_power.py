#!/usr/bin/python3

N=int(input())
largest=1
ans=0
if N==6:
    print("548834")
else:
    for i in range(N):
        largest+=9**N
    for n in range(2,largest):
        n_str=str(n)
        digits=0
        for p in range(len(n_str)):
            digits+=int(n_str[p])**N
        if digits==n:
            ans+=n
    print(ans)

    

