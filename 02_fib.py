#!/usr/bin/python3
import ipdb


num=int(input())
for i in range(num):
		N=int(input())
		fibser=[]
		sum=0
		fib=1
		if fib < N:
				fibser.append(fib)
				fib+=1
		if fib < N:
				fibser.append(fib)
				sum+=fib
		fib=fibser[-1]+fibser[-2]
		while(fib <N):
				if (fib%2==0):
						sum+=fib
				fibser.append(fib)
				fib=fibser[-1]+fibser[-2]
		print(sum)




#ipdb.set_trace()
