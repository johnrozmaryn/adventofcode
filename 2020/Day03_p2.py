# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 16:36:58 2020

@author: jrozmaryn
"""


treelist = []
yval = 0



f=open("Day03.data","r")
contents = f.readlines()
#figure out the dimensions of the map
numlines = len(contents)
numcolumns = len(contents[0])-1 #stripping out the newline

def checkfortrees(xinc,yinc):
    xpos = 0
    ypos = 0
    treeshit = 0
    while ypos < numlines :
        xpos = (xpos + xinc) % numcolumns
        ypos += yinc
        if (xpos,ypos) in treelist:
            treeshit += 1
    return treeshit
    
    

#Make a nice list with x/y pairs for the trees
for line in contents:
    strippedline = line.rstrip()
    xval = 0
    for i in strippedline:
        if i == '#':
            treelist.append((xval,yval))
        xval += 1
    yval += 1



print(checkfortrees(1,1)*
      checkfortrees(3,1)*
      checkfortrees(5,1)*
      checkfortrees(7,1)*
      checkfortrees(1,2))

    
        