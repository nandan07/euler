#!/usr/bin/python3
import math


#n,testdata=helper.readData("input")
n=int(input())
for x in range(n):
   testdata=input()
   ans=-1
   x_int=int(testdata)*2
   a=math.floor(math.sqrt(x_int))
   if a*(a+1)==x_int:
       ans=a
   print(ans)
