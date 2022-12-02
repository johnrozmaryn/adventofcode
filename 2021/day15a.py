#from copy import deepcopy
import sys
import time
# this was a lifesaver: pip install Dijkstar
from dijkstar import Graph, find_path
start = time.time()

bignegative = -1
print("opening file")
f = open("day15.in")
contents = (f.readlines())

scontents = []
for i in range(len(contents)):
    scontents.append(contents[i].strip())

for y in range(len(scontents)):
    for i in range(4*len(scontents[y])):
        val = int(scontents[y][i])
        if val == 9:
            scontents[y] += '1'
        else:
            scontents[y] += str(val + 1) 

for y in range(4*len(scontents)):
    strtoadd = ''
    for i in range(len(scontents[y])):
        val = int(scontents[y][i])
        if val == 9:
            strtoadd += '1'
        else:
            strtoadd += str(val + 1)
    scontents.append(strtoadd)
    
          

inputmap = []
widelist = []
for i in range(len(scontents[0]) + 1):
    widelist.append(bignegative)
inputmap.append(widelist)
for l in scontents:
    inlist = []
    tmpstr = l.strip()
    inlist.append(bignegative)
    for c in tmpstr:
        inlist.append(int(c))
    inlist.append(bignegative)
    inputmap.append(inlist)

inputmap.append(widelist)
width = len(inputmap[0])
height= len(inputmap) - 1


def allaround(row,col):
    outlist = []
    outlist.append([row -1, col])    
    outlist.append([row, col -1])
    outlist.append([row, col +1])
    outlist.append([row +1, col])    
    return outlist

rules = {}
costs = {}

for row in range(1,height):
    for col in range(1,width):
        costs[str(row) + ',' + str(col)] = inputmap[row][col]
        edgelist = []
        for c in allaround(row,col):
            if inputmap[c[0]][c[1]] > 0:
                edgelist.append(str(c[0]) + ',' +str(c[1]))
        rules[str(row) + ',' + str(col)] = edgelist
            
edges = []
for k in rules.keys():
    for i in rules[k]:
        edges.append((k,i,costs[i]))
print("addingGraph")
graph = Graph()
for e in edges:
    graph.add_edge(*e)
start = time.time()    
print(find_path(graph,'1,1','500,500'))
print("it took ", time.time()-start)