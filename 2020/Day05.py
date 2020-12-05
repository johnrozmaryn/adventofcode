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
    for i in range(0,6):
        if s[i] == 'B':
            row += 2**(6-i)
    column = 0
    s=list(seat.strip()[-3:])
    for i in range(0,3):
        if s[i] == 'R':
            column += 2**(2-i)
    return (row*8)+column

    
maxid = 0
for s in contents:
    maxid = max(maxid,evalseat(s))

print(maxid)

    
    