#!/usr/bin/python3
import ipdb
import helper

n,testdata=helper.readData("input")
#n=int(input())
num={}
ten={}
num['0']   =''
num['1']   ='One'
num['2']   ='Two'
num['3']   ='Three'
num['4']   ='Four'
num['5']   ='Five'
num['6']   ='Six'
num['7']   ='Seven'
num['8']   ='Eight'
num['9']   ='Nine'
num['10']  ='Ten'
num['11']  ='Eleven'
num['12']  ='Twelve'
num['13']  ='Thirteen'
num['14']  ='Fourteen'
num['15']  ='Fifteen'
num['16']  ='Sixteen'
num['17']  ='Seventeen'
num['18']  ='Eighteen'
num['19']  ='Eineteen'
ten['2']   ='Twenty'
ten['3']   ='Thirty'
ten['4']   ='Forty'
ten['5']   ='Fifty'
ten['6']   ='Sixty'
ten['7']   ='Seventy'
ten['8']   ='Eighty'
ten['9']   ='Ninety'

for i in range(113):
    #N=int(input())
    #N=testdata[i]
    N=str(i)
    ans=''
    l=len(N)
    if l<2:
        if N=='0':
            print("Zero")
        else:
            print(num[N])
    else:
        if int(N[-2])<2:
            ans=num[str(int(N[-2:]))]+" "+ans
        else:
            ans=ten[N[-2]]+" "+num[N[-1]]+" "+ans
        if l>2:
            ans=num[N[-3]]+" Hundred "+ans
            if l>3:
                ans="Thousand "+ans
                if l>4:
                    if int(N[-5])<2:
                        ans=num[str(int(N[-5:-3]))]+" "+ans
                    else:
                        ans=ten[N[-5]]+" "+num[N[-4]]+" "+ans
                    if l>5:
                        ans=num[N[-6]]+" Hundred "+ans
                        if l>6:
                            ans="Million "+ans
                            if l>7:
                                if int(N[-8])<2:
                                    ans=num[str(int(N[-8:-6]))]+" "+ans
                                else:
                                    ans=ten[N[-8]]+" "+num[N[-7]]+" "+ans
                                if l>8:
                                    ans=num[N[-9]]+" Hundred "+ans
                                    if l>9:
                                        ans="Billion "+ans
                                        if l>10:
                                            if int(N[-11])<2:
                                                ans=num[str(int(N[-11:-9]))]+" "+ans
                                            else:
                                                ans=ten[N[-11]]+" "+num[N[-10]]+" "+ans
                                            if l>11:
                                                ans=num[N[-12]]+" Hundred "+ans



        print(ans)
    #ipdb.set_trace()
