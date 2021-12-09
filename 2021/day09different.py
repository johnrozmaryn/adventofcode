#from copy import deepcopy
import sys
import time

f = open("day09.in")
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
    for c in inputmap:
        tmplst.append(0)
    bmap.append(tmplst)


risktotal = 0
for row in range(1,height):
    for col in range(1,width):
        lowpoint = True
        if inputmap[row-1][col] <= inputmap[row][col]:
            lowpoint = False
        if inputmap[row+1][col] <= inputmap[row][col]:
            lowpoint = False
        if inputmap[row][col-1] <= inputmap[row][col]:
            lowpoint = False
        if inputmap[row][col + 1] <= inputmap[row][col]:
            lowpoint = False
        if lowpoint:
            risktotal += int(inputmap[row][col]) + 1
            
print(risktotal)
print(bmap)
