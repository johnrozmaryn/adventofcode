#from copy import deepcopy
#import sys
#import time

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
costl ={rl:1,sl:2,cl:3,al:4}

def iscorrupted(l):
    corrupted = False
    stack = []
    for c in l:
        if c in [sl, rl, cl, al]:
            stack.append(c)
        elif len(stack) > 0:
            if leftpair[c] == stack[-1]:
                stack.pop()
            elif leftpair[c] != stack[-1]:
                corrupted = True
                break
    return corrupted

scorelist = []

for l in inputs:
    if not iscorrupted(l):
        stack = []
        for c in l:
            if c in [sl, rl, cl, al]:
                stack.append(c)
            else:
                stack.pop()
        stackscore = 0
        stack.reverse()
        for n in stack:
            stackscore = stackscore * 5
            stackscore += costl[n]
        scorelist.append(stackscore)

scorelist.sort()
print(scorelist[len(scorelist) //2])
            
        
            

                
            
            
        

    
