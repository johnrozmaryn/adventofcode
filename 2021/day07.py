#from copy import deepcopy
import sys

f = open("day07.in")
contents = (f.readlines())
inputlist = contents[0].split(',')
for i in range(len(inputlist)):
    inputlist[i] = int(inputlist[i])

minmoves = sys.maxsize
moveto = 0


for i in range(min(inputlist),max(inputlist)):
    runningtotal = 0
    for n in inputlist:
        runningtotal += abs(i-n)
    if runningtotal < minmoves:
        minmoves = runningtotal
        moveto = i
        
print(moveto,minmoves)