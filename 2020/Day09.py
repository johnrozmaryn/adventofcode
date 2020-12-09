# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 14:48:11 2020

@author: JROZMARYN
"""


f=open("Day09.data")
contents = (f.readlines())
data=list(map(int, contents))

preamble = 25

def checkrange(num):
    for i in range(num-preamble, num):
        for k in range(num-preamble, num):
            if (data[i] + data[k]) == data[num]:
                return 'valid', num
    return 'invalid', num
            
for pos in range(preamble, len(data)):
    ans = checkrange(pos)
    if ans[0] == 'invalid':
        print(data[ans[1]])

        

        
        
    