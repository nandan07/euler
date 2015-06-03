#!/usr/bin/python
import math
def get_primes(n):
    num=set()
    prime=set()
    for i in range(2,n+1):
        num.add(i)
    l=len(num)
    while(l>0):
        p=num.pop()
        prime.add(p)
        i=2
        while(i*p<=n+1):
            if i*p in num:
                num.remove(i*p)
            i+=1
        l=len(num)
    return prime


n=int(input())
prime=get_primes(5*(10**5))
for x in range(n):
    n=int(input())
    ans=0
    p=1
    for p in range(n+1):
        sq=int(math.sqrt((n-p)/2))
        if p in prime  and (n==p+2*(sq**2)):
            ans+=1
    print(ans)
