import copy
f = open("day06.in")
contents = (f.readlines())

m = []

for l in contents:
    sl = []
    for i in range(len(l.strip())):
        sl.append(l[i])
    m.append(sl)

rmin = 0
rmax = len(m)
cmin = 0
cmax = len(m[0])

   
# Pulled this from last year, I can make a list of directions. 
#     n = [-1,0]
#     s = [1,0]
#     e = [0,1]
#     w = [0,-1]
for row in m:
    if '^' in row:
        rstart = m.index(row)
for col in m[rstart]:
    if col == '^':
        cstart = m[rstart].index(col)


def doesitloop(tmpmap):
    visited = set()
    dlist = [[-1,0],[0,1],[1,0],[0,-1]]
    dnum = 0
    d = dlist[dnum % len(dlist)]
    out = False
    r = rstart
    c = cstart
    while not out:
        st = 'r' + str(r) + 'c' + str(c)+ 'd' + str(d)
        if st in visited:
            return True
        else:
            visited.add(st)
            tmpmap[r][c] = "X"
            rnext = r + d[0]
            cnext = c + d[1] 
            if rnext in range(rmax) and cnext in range(cmax):
                if tmpmap[rnext][cnext] == "#":
                    dnum += 1
                    d = dlist[dnum % len(dlist)]
                else:
                    r = rnext
                    c = cnext
            else:
                out = True
                return False

tot = 0
for row in range(rmax):
    print(row,col,tot)
    for col in range(cmax):        
        if m[row][col] not in ['^','#']:
            tmap = copy.deepcopy(m)
            tmap[row][col] = '#'
            tmap[rstart][cstart] = 'X'
            if doesitloop(tmap):
                tot += 1

                     
print(tot)