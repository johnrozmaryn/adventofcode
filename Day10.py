from math import atan2

# f=open("Day10Test1.input","r")
f=open("Day10.input","r")
contents = f.readlines()

astlist = []
selfangle = 999
yval = 0

for line in contents:
    strippedline = line.rstrip()
    xval = 0
    for i in strippedline:
        if i == '#':
            astlist.append((xval,yval))
        xval += 1
    yval += 1
    
    
viewablelist = []


for i in range(0,len(astlist)):
    x1 = astlist[i][0]
    y1 = astlist[i][1]
    anglelist = []
    for j in range(0,len(astlist)):
        x2 = astlist[j][0]
        y2 = astlist[j][1]
        if x1 == x2 and y1 == y2 :
            anglelist.append(selfangle)
        else:
            anglelist.append(atan2(x1-x2,y1-y2))
    viewablelist.append(len(set(anglelist))-1)

mostviewed = max(viewablelist)
posmost = astlist[viewablelist.index(mostviewed)]
print(posmost, mostviewed)
    
        
        
    
    