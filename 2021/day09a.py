#from copy import deepcopy
import sys
import time

f = open("day09.testin")
contents = (f.readlines())

inputmap = []
widestr = ''
for i in range(len(contents[0]) + 1):
    widestr += '9'
inputmap.append(widestr)
for l in contents:
    tmpstr = l.strip()
    inputmap.append('9' + tmpstr + '9')
inputmap.append(widestr)
width = len(inputmap[0]) - 1
height= len(inputmap) - 1

print(inputmap)

bmap = []
for r in inputmap:
    tmplst = []
    for c in r:
        tmplst.append(0)
    bmap.append(tmplst)

def leftbasin(row,col):
    return(bmap[row][col-1])

def abovebasin(row,col):
    return(bmap[row-1][col])

def modifybmap(l,a):
    for r in range(1,height):
        for c in range(1,width):
            if bmap[r][c] == l:
                bmap[r][c] = a
        
    
    
nextbasin = 1

for row in range(1,height):
    for col in range(1,width):
        if inputmap[row][col] != '9':
            l = leftbasin(row,col)
            a = abovebasin(row,col)
            if (l==0) and (a==0):
                bmap[row][col] = nextbasin
                nextbasin +=1
            elif l == a:
                bmap[row][col] = l
            elif (l == 0) and (a != 0):
                bmap[row][col] = a
            elif (l !=0) and (a ==0):
                bmap[row][col] = l
            else:
                bmap[row][col] = a
                modifybmap(l,a)
        
            
print(bmap)

sizes = []
for i in range(1,nextbasin):
    bcount = 0
    for r in range(1,height):
        for c in range(1,width):
            if bmap[r][c] == i:
                bcount += 1
    sizes.append(bcount)
                
sizes.sort()
top3 = sizes[-3:]
print(top3[0] * top3[1] * top3[2])
                
    
