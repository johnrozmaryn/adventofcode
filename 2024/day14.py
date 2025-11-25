
f = open("day14.tst")
contents = (f.readlines())

bots = []

# test grid: 11 wide, 7 tall
# real grid: 101 wide, 103 tall
width = 11
height = 7

bots = [[ [] for _ in range(width+1)] for _ in range(height+1)]
for l in contents:
    b = l.strip().split(' ')
    p = b[0][2:].split(',')
    v = b[1][2:].split(',')
    bots[int(p[0])][int(p[1])].append([int(v[0]),int(v[1])])
    

    
    
