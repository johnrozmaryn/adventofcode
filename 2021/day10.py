#from copy import deepcopy
import sys
import time

f = open("day10.in")
contents = (f.readlines())

inputs = []
for l in contents:
    inputs.append(l.strip())

sl, sr = '[' , ']' #square brackets
rl, rr = '(' , ')' #round brackets
cl, cr = '{' , '}' #curly brackets
al, ar = '<' , '>' #angle brackets

leftpair = {sr:sl,rr:rl,cr:cl,ar:al}
cost = {rr:3,sr:57,cr:1197,ar:25137}

def evalstring(l):
    stack = []
    totalcost = 0
    for c in l:
        if c in [sl, rl, cl, al]:
            stack.append(c)
        elif len(stack) > 0:
            if leftpair[c] == stack[-1]:
                stack.pop()
            elif leftpair[c] != stack[-1]:
                print(l,c)
                totalcost = cost[c]
                break
    return totalcost

totalcost = 0

for l in inputs:
    totalcost += evalstring(l)
print(totalcost)
            

                
            
            
        

    
