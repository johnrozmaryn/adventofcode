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

lookuplist = [0]
for i in range(1,max(inputlist)+1):
    lookuplist.append(i+lookuplist[i-1])
    
def recadd(i):
    if i == 0:
        return 0
    if i == 1:
        return 1
    else:
        return i + recadd(i-1)
starttime = time.time()

for i in range(min(inputlist),max(inputlist)):
    runningtotal = 0
    for n in inputlist:
        runningtotal += recadd(abs(n-i))
    if runningtotal < minmoves:
        minmoves = runningtotal
        moveto = i

print(moveto,minmoves)
print("Time to complete: ",time.time()-starttime)