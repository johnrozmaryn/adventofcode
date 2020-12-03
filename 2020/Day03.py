# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 16:36:58 2020

@author: jrozmaryn
"""
xpos = 0
ypos = 0

treelist = []
yval = 0


f=open("Day03.data","r")
contents = f.readlines()
#figure out the dimensions of the map
numlines = len(contents)
numcolumns = len(contents[0])-1 #stripping out the newline

#Make a nice list with x/y pairs for the trees
for line in contents:
    strippedline = line.rstrip()
    xval = 0
    for i in strippedline:
        if i == '#':
            treelist.append((xval,yval))
        xval += 1
    yval += 1

treeshit = 0

while ypos < numlines :
    xpos = (xpos + 3) % numcolumns
    ypos += 1
    if (xpos,ypos) in treelist:
        treeshit += 1

print(treeshit)        

    
        