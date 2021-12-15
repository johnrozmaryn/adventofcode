#from copy import deepcopy
# import sys
# import time


f = open("day14.in")
contents = (f.readlines())

startlist = contents[0].strip()
startchar = startlist[0]
endchar = startlist[-1]

contents.remove(contents[0])
contents.remove('\n')

rules = {}
for l in contents:
    sl = l.strip().split(' -> ')
    rules[sl[0]] = sl[1]

def dec(pair,count,rules):
    if pair in rules:
        rules[pair] = rules[pair] - count
    else:
        rules[pair] = -count

def inc(pair,count,rules):
    if pair in rules:
        rules[pair] = rules[pair] + count
    else:
        rules[pair] = count

polylist = []
poly = {}
for i in range(len(startlist)-1):
    inc(startlist[i] + startlist[i+1],1,poly)

atoms = {}
for i in range(len(startlist)):
    inc(startlist[i],1,atoms)
    

polylist.append(poly) 

print(polylist[0])   
print(atoms)

for turn in range(40):
    newpoly = {}
    poly = polylist[turn]
    for p in poly:
        count = poly[p]
        toadd = rules[p]
        left = p[0]
        right = p[1]
        if not p in newpoly:
            newpoly[p] = poly[p]
        else:
            newpoly[p] = newpoly[p] + poly[p]
        dec(p,count,newpoly)
        inc(toadd,count,atoms)
        inc(left+toadd,count,newpoly)
        inc(toadd+right,count,newpoly)
    polylist.append(newpoly)
    
print(polylist[-1])
print(atoms)
qs = []
for k in atoms.keys():
    qs.append(atoms[k]) 
print(max(qs)-min(qs))
                

