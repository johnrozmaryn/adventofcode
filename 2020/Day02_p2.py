# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 08:17:52 2020

@author: JROZMARYN
"""


f=open("Day02.data")
contents = (f.readlines())
goodpwds = 0


for line in contents:
    splitline = line.split(' ')
    mincount,maxcount = map(int,splitline[0].split("-"))
    rulestring = splitline[1].split(":")[0]
    pwdstring = splitline[2]
    # if len(pwdstring) >= maxcount and len(pwdstring) >= mincount:
    if (pwdstring[mincount - 1] == rulestring) ^ (pwdstring[maxcount-1] == rulestring):
        goodpwds += 1

        
print(goodpwds)
    
    
    