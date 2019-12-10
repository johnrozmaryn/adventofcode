from math import atan2
from math import pi
from math import sqrt

# f=open("Day10test2.input","r")
# f=open("Day10Test1.input","r")
f=open("Day10.input","r")
contents = f.readlines()

astlist = []
headinglist = []
distlist = []


def heading(startpos,ast):
    atanout = atan2(ast[0]-startpos[0],startpos[1]-ast[1])
    if atanout >= 0:
        return atanout
    else:
        return 2*pi + atanout

def distance(startpos,ast):
    x2 = (startpos[0] - ast[0])**2
    y2 = (startpos[1] - ast[1])**2
    return sqrt(x2 + y2)
# generate list of asteroid positions, headings, and distances   
yval = 0
for line in contents:
    strippedline = line.rstrip()
    xval = 0
    for i in strippedline:
        if i == '#':
            astlist.append((xval,yval))
        xval += 1
    yval += 1

mypos = (17,22) #solution to my dataset
#mypos = (11,13) #for dataset test2
astlist.remove(mypos)
for i in astlist:
    headinglist.append(heading(mypos,i))
    distlist.append(distance(mypos,i))

for i in astlist:
    ind = astlist.index(i)
    print(astlist[ind],headinglist[ind],distlist[ind])
    
rotlist = list(set(headinglist))
rotlist.sort()
fireangle = rotlist[199]
print(len(rotlist))
print(rotlist)
print(fireangle)

for i in range(0,len(astlist)):
    if headinglist[i] == fireangle:
        print(astlist[i],distlist[i])







      
# viewablelist = []

# for i in range(0,len(astlist)):
    # x1 = astlist[i][0]
    # y1 = astlist[i][1]
    # anglelist = []
    # for j in range(0,len(astlist)):
        # x2 = astlist[j][0]
        # y2 = astlist[j][1]
        # if x1 == x2 and y1 == y2 :
            # anglelist.append(selfangle)
        # else:
            # anglelist.append(atan2(x1-x2,y1-y2))
    # viewablelist.append(len(set(anglelist))-1)

# mostviewed = max(viewablelist)
# posmost = astlist[viewablelist.index(mostviewed)]
# print(posmost, mostviewed)
    
        
        
    
    