# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 14:48:11 2020

@author: JROZMARYN
"""


f=open("Day01.data")
contents = (f.readlines())
data=list(map(int, contents))
print(data)



for i in data:
    for j in data:
        for k in data:
            if i+j+k == 2020:
                print(i,j,k,i*j*k)


        
        
    