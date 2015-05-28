#!/usr/bin/python3
import ipdb
#import helper
#
#N,testdata=helper.readData("input")
N=int(input())
def path_Val(node):
    if node['L']==None and node['R']==None:
        return node['Val']
    elif (path_Val(graph[node['R']]) > path_Val(graph[node['L']])):
        return node['Val']+path_Val(graph[node['R']])
    else:
        return node['Val']+path_Val(graph[node['L']])



for k in range(N):
    n=int(input())
    id=0
    c=0
    graph={}
    curr=input().split()
    nxt=""
    for i in range(n-1):
        nxt=input().split()
        c+=len(curr)
        for p in range(len(curr)):
            node={}
            node['L']=c+p
            node['R']=c+p+1
            node['Val']=int(curr[p])
            graph[id]=node
            #ipdb.set_trace()
            id+=1
        if i==n-2:
            #ipdb.set_trace()
            for l in range(len(nxt)):
                node={}
                node['L']=None
                node['R']=None
                node['Val']=int(nxt[l])
                graph[id]=node
                #ipdb.set_trace()
                id+=1
        curr=nxt
    if n==1:
            node={}
            node['L']=None
            node['R']=None
            node['Val']=int(curr[0])
            graph[id]=node
    print(path_Val(graph[0]))


