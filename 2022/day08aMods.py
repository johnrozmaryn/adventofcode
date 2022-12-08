f = open("day08.in")
contents = (f.readlines())

colmax = len(contents[0].strip())
rowmax = len(contents)

hm = [] # height map
vis = [] # visibility map
ss = [] # scenic scores

for row in range(rowmax):
    h = []
    v = []
    for col in range(colmax):
        h.append(contents[row][col])
        v.append([])
    hm.append(h)
    vis.append(v)

#address things as h[row][col]

def ViewWest(r,c):
    viewable = 0
    ht = hm[r][c]
    for i in range(c-1,-1,-1):
        viewable += 1
        if hm[r][i] >= ht:
            return viewable
    return viewable
            
def ViewEast(r,c):
    viewable = 0
    ht = hm[r][c]
    for i in range(c+1,colmax):
        viewable += 1
        if hm[r][i] >= ht:
            return viewable
    return viewable
        
def ViewNorth(r,c):
    viewable = 0
    ht = hm[r][c]
    for i in range(r-1,-1,-1):
        viewable += 1
        if hm[i][c] >= ht:
            return viewable
    return viewable

def ViewSouth(r,c):
    viewable = 0
    ht = hm[r][c]
    for i in range(r+1,rowmax):
        viewable += 1
        if hm[i][c] >= ht:
            return viewable
    return viewable

for rw in range(1,rowmax-1):
    for co in range(1,colmax-1):
        ss.append(ViewNorth(rw,co) * ViewSouth(rw,co) * ViewEast(rw,co) * ViewWest(rw,co))

print(max(ss))        