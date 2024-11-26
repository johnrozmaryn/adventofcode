f = open("day10.tst")
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
    nw = [-1,-1]
    ne = [-1,1]
    sw = [1,-1]
    se = [1,1]
 
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
    d[currpos[0]][currpos[1]] = '*'
    dirnext = [item for item in r[atpos] if item not in [fromloc]][0]
    nextpos = [currpos[0] + dirnext[0],currpos[1] + dirnext[1]]
    right = []
    if atpos == '/':
        if fromloc == n:
            right = [e]
        else:
            right = [w]
    if atpos == '-':
        if fromloc == e:
            right = [s]
        else:
            right = [n]
    if atpos == 'L':
        if nextpos == e:
            right = [w,s,sw]
        else:
            right = []
    if atpos == 'J':
        if nextpos == n:
            right = [s,e,se]
        else:
            right = []
    if atpos == '7':
        if nextpos == w:
            right = [n, ne, e]
        else:
            right = []
    if atpos == 'F':
        if nextpos == s:
            right = [w, nw, n]
        else:
            right = []
            
    for i in right:
        r1 = currpos[0]
        c1 = currpos[1]
        if d[r1 + i[0]][c1+i[1]] == '.':
            d[r1 + i[0]][c1+i[1]] = 'I'            
    
    return [nextpos,[-dirnext[0],-dirnext[1]]]

pos = findS(d)
pointlist = []
pointlist.append([pos[0],pos[1]])
print(pointlist)
pos[1] += 1
print(pointlist)
fromloc = [0,-1]

while pos != pointlist[0]:
    pointlist.append([pos[0],pos[1]])
    a = nextstep(pos,fromloc)
    fromloc = a[1]
    pos = a[0]


print(len(pointlist) / 2)
rs=''
for q in range(len(d)):
    cs = ''
    for c in range(len(d[q])):
        if d[q][c] in r:
            cs += ' '
        elif d[q][c] == 'I':
            cs += 'I'
        else:
            cs += d[q][c]
    rs += cs + '\n'
    
of = open("day10a.out", "w")
of.write(rs)
of.close()
    



    
    
        
