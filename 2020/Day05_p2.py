# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 08:17:52 2020

@author: JROZMARYN
"""


f=open("Day05.data")
contents = (f.readlines())

def evalseat(seat):
    s = list(seat.strip())
    row = 0
    for i in range(0,7):
        if s[i] == 'B':
            row += 2**(6-i)
    column = 0
    s=list(seat.strip()[-3:])
    for i in range(0,3):
        if s[i] == 'R':
            column += 2**(2-i)
    return (row*8)+column

passlist = []
for bp in contents:
    passlist.append(evalseat(bp))
    
totallist = list(range(0,127*8+8+1))

for s in passlist:
    if s in totallist:
        totallist.remove(s)
    
for s in totallist:
    if (s-1 in passlist) and (s+1 in passlist):
        print(s)

    




    
    