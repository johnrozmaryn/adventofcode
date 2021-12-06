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
    if (i[0] == i[2]) or (i[1] == i[3]):
        minx = min(i[0],i[2])
        maxx = max(i[0],i[2])
        miny = min(i[1],i[3])
        maxy = max(i[1],i[3])
        for x in range(minx, maxx + 1):
            for y in range(miny, maxy + 1):
                key = str(x) + ";" + str(y)
                if key in pointdict.keys():
                    oldvalue = pointdict[key]
                    pointdict[key] = oldvalue + 1
                else:
                    pointdict[key] = 1                
total = 0
for key in pointdict:
    if pointdict[key] > 1:
        total += 1
print(total)
