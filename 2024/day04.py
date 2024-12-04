f = open("day04.in")
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
direclist = [[-1,0],[1,0],[0,1],[0,-1],[-1,-1],[-1,1],[1,-1],[1,1]]

tot = 0

for r in range(rmax):
    for c in range(cmax):
        for d in direclist:
            if (r + 3*d[0] in range(rmax)) and (c + 3*d[1] in range(cmax)):
                rd = d[0]
                cd = d[1]
                if m[r][c] == 'X':
                    if m[r+rd][c+cd] == 'M':
                        if m[r+2*rd][c+2*cd] == 'A':
                            if m[r+3*rd][c+3*cd] == 'S':
                                tot +=1
                                print(r,c)
                                
print(tot)


