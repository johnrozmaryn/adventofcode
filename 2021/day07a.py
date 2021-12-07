#from copy import deepcopy
import sys
import time

f = open("day07.in")
contents = (f.readlines())
inputlist = contents[0].split(',')
for i in range(len(inputlist)):
    inputlist[i] = int(inputlist[i])

minmoves = sys.maxsize
moveto = 0

starttime = time.time()

lookuplist = [0]
for i in range(1,max(inputlist)+1):
    lookuplist.append(i+lookuplist[i-1])
    
for i in range(min(inputlist),max(inputlist)):
    runningtotal = 0
    for n in inputlist:
        runningtotal += lookuplist[abs(n-i)]
    if runningtotal < minmoves:
        minmoves = runningtotal
        moveto = i

print(moveto,minmoves)
print("Time to complete: ",time.time()-starttime)
