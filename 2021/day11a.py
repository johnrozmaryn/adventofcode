#from copy import deepcopy
# import sys
# import time

bignegative = -1

f = open("day11.in")
contents = (f.readlines())

inputmap = []
widelist = []
for i in range(len(contents[0]) + 1):
    widelist.append(bignegative)
inputmap.append(widelist)
for l in contents:
    inlist = []
    tmpstr = l.strip()
    inlist.append(bignegative)
    for c in tmpstr:
        inlist.append(int(c))
    inlist.append(bignegative)
    inputmap.append(inlist)

inputmap.append(widelist)
width = len(inputmap[0]) - 1
height= len(inputmap) - 1

def allaround(row,col):
    outlist = []
    outlist.append([row -1, col -1])
    outlist.append([row -1, col])    
    outlist.append([row -1, col +1])
    outlist.append([row, col -1])
    outlist.append([row, col +1])
    outlist.append([row +1, col -1])
    outlist.append([row +1, col])    
    outlist.append([row +1, col +1])
    return outlist
 
def incrementall():
    for row in range(1,height):
        for col in range(1,width):
                currentval = inputmap[row][col]
                inputmap[row][col] = currentval + 1
    
def flashneighbors(row,col):
    for c in allaround(row,col):
        currentval = inputmap[c[0]][c[1]]
        if currentval > 0:
            inputmap[c[0]][c[1]] = currentval + 1

def doflashes(): #maybe make this return how many flashes happened?
    flashes = 0
    for row in range(1,height):
        for col in range(1,width):
            if inputmap[row][col] > 9:
                flashneighbors(row,col)
                inputmap[row][col] = 0
                flashes += 1
    return flashes

def doallflashes():
    flashes = 0
    f = doflashes()
    while f > 0:
        flashes += f
        f = doflashes()
    return flashes

totalflashes = 0
                    
for i in range(10000):
    incrementall()
    numflashes = doallflashes()
    if numflashes == 100:
        print(i+1)
        break

        