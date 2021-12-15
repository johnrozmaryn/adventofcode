#from copy import deepcopy
# import sys
# import time


f = open("day13.in")
contents = (f.readlines())

dots = {}
folds = []
outlist = []

for l in contents:
    tstr = l.strip()
    if ',' in tstr:
        dots[tstr] = 1
    if '=' in tstr:
        val = int(tstr.split('=')[1])
        if 'x' in tstr:
            folds.append(['x',val])
        else:
            folds.append(['y',val])
            
def pprint(dots):
    xlist = []
    ylist = []
    for k in dots.keys():
        xy = k.split(',')
        xlist.append(int(xy[0]))
        ylist.append(int(xy[1]))
    for y in range(max(ylist)+1):
        row = ''
        for x in range(max(xlist)+1):
            if str(x)+','+ str(y) in dots:
                row += '#'
            else:
                row += '.'
        print(row)

def pointindict(x,y,pdict):
    if str(x) + ',' + str(y) in pdict:
        return True
    else:
        return False


def foldy(dotsin,val):
    dotsout = {}
    xlist = []
    ylist = []
    for k in dotsin.keys():
        xy = k.split(',')
        xlist.append(int(xy[0]))
        ylist.append(int(xy[1]))
    for x in range(max(xlist)+1):
        for y in range(val):
            if pointindict(x,y,dotsin):
                dotsout[str(x) + ',' + str(y)] = 1
                
    for x in range(max(xlist)+1):
        for y in range(val+1,max(ylist)+1):
            refy = 2*val - y
            if pointindict(x,y,dotsin):
                dotsout[str(x)+ ',' + str(refy)] = 1
    return dotsout
 
def foldx(dotsin,val):
    dotsout = {}
    xlist = []
    ylist = []
    for k in dotsin.keys():
        xy = k.split(',')
        xlist.append(int(xy[0]))
        ylist.append(int(xy[1]))
    for y in range(max(ylist)+1):
        for x in range(val):
            if pointindict(x,y,dotsin):
                dotsout[str(x) + ',' + str(y)] = 1
                
    for y in range(max(ylist)+1):
        for x in range(val+1,max(xlist)+1):
            refx = 2*val - x
            if pointindict(x,y,dotsin):
                dotsout[str(refx)+ ',' + str(y)] = 1
    return dotsout
       
outlist.append(dots)

for i in range(len(folds)):
    if folds[i][0] == 'x':
        outlist.append(foldx(outlist[i],folds[i][1]))
    else:
        outlist.append(foldy(outlist[i],folds[i][1]))

pprint(outlist[-1])
    



            