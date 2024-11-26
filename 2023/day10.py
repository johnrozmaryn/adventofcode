f = open("day10.in")
contents = (f.readlines())

d = []

for l in contents:
    sl = []
    for i in range(len(l.strip())):
        sl.append(l[i])
    d.append(sl)
 
    n = [-1,0]
    s = [1,0]
    e = [0,1]
    w = [0,-1]
 
r = {'|': [n,s], \
     '-': [e,w], \
     'L': [n,e], \
     'J': [n,w], \
     '7': [s,w], \
     'F': [s,e]}
    
def findS(_):
    for r in range(len(_)):
        for c in range(len(_[r])):
            if _[r][c] == 'S':
                return [r,c]

def nextstep(currpos,fromloc):
    atpos = d[currpos[0]][currpos[1]]
    dirnext = [item for item in r[atpos] if item not in [fromloc]][0]
    nextpos = [currpos[0] + dirnext[0],currpos[1] + dirnext[1]]
    return [nextpos,[-dirnext[0],-dirnext[1]]]

pos = findS(d)
pointlist = []
pointlist.append([pos[0],pos[1]])
pos[1] += 1
fromloc = [0,-1]

while pos != pointlist[0]:
    pointlist.append([pos[0],pos[1]])
    a = nextstep(pos,fromloc)
    fromloc = a[1]
    pos = a[0]


print(len(pointlist) / 2)
    
    
        
