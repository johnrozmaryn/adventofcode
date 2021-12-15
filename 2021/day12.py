#from copy import deepcopy
# import sys
# import time

f = open("day12.testin")
contents = (f.readlines())

rules = {}
for l in contents:
    splitlist = l.strip('\n').split('-')
    if splitlist[0] in rules.keys():
        rules[splitlist[0]].append(splitlist[1])
    else:
        rules[splitlist[0]] = []
        rules[splitlist[0]].append(splitlist[1])
    if splitlist[1] in rules.keys():
        rules[splitlist[1]].append(splitlist[0])
    else:
        rules[splitlist[1]] = []
        rules[splitlist[1]].append(splitlist[0])
        
        
pathlist = []

def pairinpath(pathstr,dest):
    inpath = False
    breakpos = pathstr[0:len(pathstr)].rfind(',')
    if breakpos == -1: #This is apparently the start node
        return inpath  
    lastadd = pathstr[breakpos + 1: len(pathstr)-1]
    if ( lastadd + ',' + dest) in pathstr:
        inpath = True
    else:
        inpath = False
    return inpath
        
def addleg(pathstr,dest):
    if dest == 'end':
        pathlist.append(pathstr + 'end')
    else:
        for nextdest in rules[dest]:
            if not pairinpath(pathstr,nextdest):
                addleg(pathstr + ',',nextdest)
          

            
for dest in rules['start']:
    addleg('start,',dest)




print(paths)
        
        