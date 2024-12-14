import copy
f = open("day10.in")
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
direclist = [[-1,0],[1,0],[0,1],[0,-1]]

tot = 0

trails = []
for r in range(rmax):
    for c in range(cmax):
        if int(m[r][c])== 0:
            trails.append([[r,c]])

for n in range(1,10):
    tmptrail = []
    for trail in trails:
        for d in direclist:
                rnew = trail[-1][0] + d[0]
                cnew = trail[-1][1] + d[1]
                if rnew in range(rmax) and cnew in range(cmax):
                    if int(m[rnew][cnew]) == n:
                        tmptrail.append(trail + [[rnew,cnew]])
    trails = copy.deepcopy(tmptrail)
            
unique = []
for t in trails:
    if [t[0],t[-1]] not in unique:
        unique.append([t[0],t[-1]])
                      
print(len(unique))         
            
            
            
            
            
#         for d in direclist:
#             if (r + 3*d[0] in range(rmax)) and (c + 3*d[1] in range(cmax)):
#                 rd = d[0]
#                 cd = d[1]
#                 if m[r][c] == 'X':
#                     if m[r+rd][c+cd] == 'M':
#                         if m[r+2*rd][c+2*cd] == 'A':
#                             if m[r+3*rd][c+3*cd] == 'S':
#                                 tot +=1
#                                 print(r,c)
                                
# print(tot)