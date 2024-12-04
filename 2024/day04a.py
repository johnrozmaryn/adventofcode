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


#     nw = [-1,-1]
#     ne = [-1,1]
#     sw = [1,-1]
#     se = [1,1]

tot = 0

for r in range(rmin+1,rmax-1):
    for c in range(cmin+1,cmax-1):
        if m[r][c] == 'A':
            if [m[r-1][c-1],m[r+1][c+1]] in [['M','S'],['S','M']]:
                if [m[r-1][c+1],m[r+1][c-1]] in [['M','S'],['S','M']]:
                    tot += 1
            
print(tot)
    
    





# width = len(contents[0]) + 2
# height = len(contents) + 2

