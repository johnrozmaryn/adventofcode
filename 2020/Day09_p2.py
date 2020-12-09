# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 14:48:11 2020

@author: JROZMARYN
"""


f=open("Day09.data")
contents = (f.readlines())
data=list(map(int, contents))

magicnumber = 1309761972


def adder(rngstart,rngend):
    total = 0
    for i in range(rngstart,rngend + 1):
        total += data[i]
    return total

def addhighlow(rngstart,rngend):
    rangetoadd = data[rngstart:rngend+1]
    return max(rangetoadd) + min(rangetoadd)

for i in range(0,len(data)-1):
    rngstart = i
    rngend = rngstart + 1
    total = adder(rngstart,rngend)
    while total <= magicnumber:
        if total == magicnumber:
            print(addhighlow(rngstart,rngend))

            break
        rngend += 1
        total = adder(rngstart,rngend)
    
    


            

        

        
        
    