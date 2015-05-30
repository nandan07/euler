#!/usr/bin/python3
import ipdb
import helper
import itertools

def common_digit(x,y):
    cd=set()
    for i in x:
        if y.find(i)>-1:
            cd.add(i)
    return sorted(cd)


n,testdata=helper.readData("input")
#N=int(input())
digit='0123456789'
N,K=testdata[0].split()
N=int(N)
K=int(K)
num=[]
permut=itertools.product(sorted(digit),repeat=N)
for n in permut:
    num.append("".join(n))
st_ind=10**(N-1)
ans=0
for i in range(st_ind,len(num)-1):
    for j in range(i+1,len(num)):
        numr=num[i]
        denr=num[j]
        #if numr=='49' and denr=='98':
        #    ipdb.set_trace()
        v=int(numr)/int(denr)
        cd=common_digit(numr,denr)
        if len(cd)>=K:
            for d in cd:
                if not d=='0':
                    p_num=numr.find(d)
                    p_den=denr.find(d)
                    numr=numr[:p_num]+numr[p_num+1:]
                    denr=denr[:p_den]+denr[p_den+1:]
            if int(denr)>int(numr) and  not (int(denr)==0):
                if v==int(numr)/int(denr):
                    ipdb.set_trace()
                    ans+=1
print(ans)
ipdb.set_trace()

