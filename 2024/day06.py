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
#     nw = [-1,-1]
#     ne = [-1,1]
#     sw = [1,-1]
#     se = [1,1]
dlist = [[-1,0],[0,1],[1,0],[0,-1]]
dnum = 0
d = dlist[dnum % len(dlist)]
for row in m:
    if '^' in row:
        r = m.index(row)
for col in m[r]:
    if col == '^':
        c = m[r].index(col)

out = False

while not out:
    m[r][c] = "X"
    rnext = r + d[0]
    cnext = c + d[1] 
    if rnext in range(rmax) and cnext in range(cmax):
        if m[rnext][cnext] == "#":
            dnum += 1
            d = dlist[dnum % len(dlist)]
        else:
            r = rnext
            c = cnext
    else:
        out = True

tot = 0
for row in m:
    for col in row:
        if col == "X":
            tot += 1
            
print(tot)
    
        
        
    
    



        
        
       
    

