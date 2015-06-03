#!/usr/bin/python3
import ipdb
#import helper
#


def get_primes(n):
    num=set()
    prime={}
    su=0
    for i in range(2,n+1):
        num.add(i)
    l=len(num)
    while(l>0):
        p=num.pop()
        su+=p
        prime[p]=su
        i=2
        while(i*p<=n+1):
            if i*p in num:
                num.remove(i*p)
            i+=1
        l=len(num)
    return prime


#N=int(input())
N=int("100")

ipdb.set_trace()
ans=0
#last=(10**(len(str(n))+1))-1
prime=get_primes(1000000)
ans=0
for n in range(2,N+1):
    cir_prime=True
    if n in prime:
        #ipdb.set_trace()
        n_str=str(n)
        for p in range(len(n_str)):
            rot=int(n_str[p:]+n_str[:p])
            if not rot in prime:
                cir_prime=False
                break
        if cir_prime:
            #ipdb.set_trace()
            ans+=n
print(ans)


#
#for i in range(N,1,-1):
#    prime=True
#    if isPrime(i):
#        i_str=str(i)
#        for p in range(len(i_str)):
#            rot=int(i_str[p:]+i_str[:p])
#            if not isPrime(rot):
#                prime=False
#                break
#        if (prime):
#            ans+=i
#print(ans)
#
#
