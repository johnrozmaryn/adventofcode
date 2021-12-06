from copy import deepcopy
import sys

f = open("day05.in")
contents = (f.readlines())
#[l.strip() for l in contents]

linelist = []
for l in contents:
    temp = l.strip()
    pairs = temp.split(' -> ')
    strcordlist = pairs[0].split(',') + pairs[1].split(',')
    cordlist = []
    for i in strcordlist:
        cordlist.append(int(i))
    linelist.append(cordlist)

pointdict = {}

for i in linelist:

    minx = min(i[0],i[2])
    maxx = max(i[0],i[2])
    miny = min(i[1],i[3])
    maxy = max(i[1],i[3])
    if (i[0] == i[2]) ^ (i[1] == i[3]):
        for x in range(minx, maxx + 1):
            for y in range(miny, maxy + 1):
                key = str(x) + ";" + str(y)
                if key in pointdict.keys():
                    oldvalue = pointdict[key]
                    pointdict[key] = oldvalue + 1
                else:
                    pointdict[key] = 1  
    else:
        if i[2] > i[0]:
            xstep = 1
        else: 
            xstep = -1
        if i[3] > i[1]:
            ystep = 1
        else: 
            ystep = -1
        for n in range(abs(maxx - minx)+ 1):
            key = str(i[0] + n* xstep) + ";" + str(i[1] + n*ystep)
            if key in pointdict.keys():
                oldvalue = pointdict[key]
                pointdict[key] = oldvalue + 1
                #print("second", minx+n, miny+n)
            else:
                pointdict[key] = 1
                #print("initial",minx+n, miny+n)
                
            
            
total = 0
for key in pointdict:
    if pointdict[key] > 1:
        total += 1
print(total)

