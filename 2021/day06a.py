#from copy import deepcopy
#import sys

f = open("day06.in")
contents = (f.readlines())
inputlist = contents[0].split(',')
for i in range(len(inputlist)):
    inputlist[i] = int(inputlist[i])

fishlist = [0,0,0,0,0,0,0,0,0]
  
print(fishlist)
print(inputlist)

for i in range(len(inputlist)):
    fishlist[inputlist[i]] += 1
    
print(fishlist)

for days in range(256):
    new8 = fishlist[0]
    new7 = fishlist[8]
    new6 = fishlist[7]  + fishlist[0]
    new5 = fishlist[6]
    new4 = fishlist[5]
    new3 = fishlist[4]
    new2 = fishlist[3]
    new1 = fishlist[2]
    new0 = fishlist[1]
    fishlist = [new0,new1,new2,new3,new4,new5,new6,new7,new8]

print(sum(fishlist))
print(fishlist)