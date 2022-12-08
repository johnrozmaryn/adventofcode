f = open("day08.in")
contents = (f.readlines())

colmax = len(contents[0].strip())
rowmax = len(contents)

hm = [] # height map
vis = [] # visibility map

for row in range(rowmax):
    h = []
    v = []
    for col in range(colmax):
        h.append(contents[row][col])
        v.append([])
    hm.append(h)
    vis.append(v)

#address things as h[row][col]

def ViewFromWest(row):
    vis[row][0] = True
    maxht = hm[row][0]
    for col in range(1,colmax):
        if hm[row][col] > maxht:
            maxht = hm[row][col]
            vis[row][col] = True
            
def ViewFromEast(row):
    vis[row][colmax-1] = True
    maxht = hm[row][colmax-1]
    for col in range(colmax-2,-1,-1):
        if hm[row][col] > maxht:
            maxht = hm[row][col]
            vis[row][col] = True
            
def ViewFromNorth(col):
    vis[0][col] = True
    maxht = hm[0][col]
    for row in range(1,rowmax):
        if hm[row][col] > maxht:
            maxht = hm[row][col]
            vis[row][col] = True

def ViewFromSouth(col):
    vis[rowmax-1][col] = True
    maxht = hm[rowmax-1][col]
    for row in range(rowmax-2,-1,-1):
        if hm[row][col] > maxht:
            maxht = hm[row][col]
            vis[row][col] = True
            
for row in range(rowmax):
    ViewFromEast(row)
    ViewFromWest(row)

for col in range(colmax):
    ViewFromNorth(col)
    ViewFromSouth(col)
    
viewable = 0
for row in range(rowmax):
    for col in range(colmax):
        if vis[row][col]:
            viewable += 1
            
print(viewable)

            
        
    
        
        