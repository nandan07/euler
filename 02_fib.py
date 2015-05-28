#!/usr/bin/python3
import ipdb

#def readData(filename):
#		data=open(filename)
#		testData=[]
#		n=data.readline()[0:-1]
####		ipdb.set_trace()
#		nn=int(n)+1
#		for line in range(1,nn):
#				testData.append(data.readline()[0:-1])
#		return testData

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
