#from copy import deepcopy
import sys
import time

f = open("day09.in")
contents = (f.readlines())

inputmap = []
for l in contents:
    inputmap.append(l.strip())

width = len(inputmap[0])
height= len(inputmap)

print(width,height)

risktotal = 0
for row in range(height):
    for col in range(width):
        lowpoint = True
        if row > 0:
            if inputmap[row-1][col] <= inputmap[row][col]:
                lowpoint = False
        if row < height-1:
            if inputmap[row+1][col] <= inputmap[row][col]:
                lowpoint = False
        if col > 0:
            if inputmap[row][col-1] <= inputmap[row][col]:
                lowpoint = False
        if col < width-1:
            if inputmap[row][col + 1] <= inputmap[row][col]:
                lowpoint = False
        if lowpoint:
            risktotal += int(inputmap[row][col]) + 1
            
print(risktotal)
            
        
        