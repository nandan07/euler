#!/usr/bin/python3
import ipdb
import helper

def cycle_len(n):
    ss=str(1/n)[2:]
    for p in range(len(ss)-1):
        next_p=ss[p+1:].find(ss[p])
        if next_p>-1:
            return next_p+1
        else:
            continue
    return 0

ipdb.set_trace()

