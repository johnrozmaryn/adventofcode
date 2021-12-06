#from copy import deepcopy
#import sys

f = open("day06.in")
contents = (f.readlines())
splitout = contents[0].split(',')

fishlist = []

for l in splitout:
    fishlist.append(int(l))
    
print(fishlist)

for days in range(80):
    startlength = len(fishlist)
    for i in range(startlength):
        if fishlist[i] > 0:
            fishlist[i] -= 1
        else:
            fishlist[i] = 6
            fishlist.append(8)
            
print(len(fishlist))