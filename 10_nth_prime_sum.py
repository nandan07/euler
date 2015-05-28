#!/usr/bin/python3

def isPrime(x):
    x=int(x)
    for i in range(2,int(x**.5)+1):
        if x%i ==0 :
            return False
    return True

def getprime(p):
    if isPrime(p):
        return p
    else:
        while(not isPrime(p)):
            p-=1
        return p



data=[]
num=2
for i in range(1,100001):
    while(not isPrime(num)):
        num+=1
        if num>1000000:
            break
    data.append(num)
    num+=1
    if num>1000000:
        break
n=int(input())

for k in range(n):
    testdata=input()
    i=int(testdata)
    p=getprime(i)
    ind=data.index(p)
    su=0
    for i in range(ind+1):
        su+=data[i]
    print(su)
