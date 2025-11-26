
f = open("day14.in")
contents = (f.readlines())

bots = []

# test grid: 11 wide, 7 tall
# real grid: 101 wide, 103 tall
width = 101
height = 103

bots = [[ [] for _ in range(width)] for _ in range(height)]
for l in contents:
    b = l.strip().split(' ')
    p = b[0][2:].split(',')
    v = b[1][2:].split(',')
    bots[int(p[1])][int(p[0])].append([int(v[0]),int(v[1])])

newbots = [[ [] for _ in range(width)] for _ in range(height)]

moves = 100

for row in range(height):
    for col in range(width):
        for v in bots[row][col]:
            newrow = (v[1] * moves + row) % height
            newcol = (v[0] * moves + col) % width
            newbots[newrow][newcol].append(v)

def tot(rmin,rmax,cmin,cmax):
    t = 0
    for r in range(rmin,rmax):
        for c in range(cmin,cmax):
            t+= len(newbots[r][c])
    return t
rmid = int(height/2)
cmid = int(width/2)
    
q1 = tot(0,rmid,0,cmid)
q2 = tot(0,rmid,cmid+1,width)
q3 = tot(rmid+1,height,0,cmid)
q4 = tot(rmid+1,height,cmid+1,width)

threat = q1*q2*q3*q4
print(threat)



