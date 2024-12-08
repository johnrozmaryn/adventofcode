f = open("day08.tstt")
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

def isint(a):    #surely there's already a function for this?
    return round(a) == a


chars = set()
for r in range(rmax):
    for c in range(cmax):
        if m[r][c] != '.':
            chars.add(m[r][c])
charlist = []
for item in chars:
    charlist.append(item)
    
charmap = []
for character in charlist:
    line = []
    for r in range(rmax):
        for c in range(cmax):
            if m[r][c] == character:
                line.append([r,c])
    charmap.append(line)
    
anode = set()
for line in charmap:
    while len(line) > 1:
        pnt = line.pop()
        for nxt in line:
            dx = nxt[1] - pnt[1]
            dy = nxt[0] - pnt[0]
            newx = pnt[1] -dx
            newy = pnt[0] -dy
            if newx in range(cmin,cmax) and newy in range(rmin,rmax):
                anode.add('r'+str(newx)+'c'+str(newy))
            newx = nxt[1] + dx
            newy = nxt[0] + dy
            if newx in range(cmin,cmax) and newy in range(rmin,rmax):
                anode.add('r'+str(newx)+'c'+str(newy))
                
print(len(anode))

                    
    
