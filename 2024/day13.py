f = open("day13.tst")
contents = f.readlines()

machines = []
l = 0
while l <= len(contents):
    machine = []
    ax = int(contents[l][12:14])
    ay = int(contents[l][18:20])
    l+=1
    bx = int(contents[l][12:14])
    by = int(contents[l][18:20])
    l+=1
    p = contents[l].strip()
    p1 = p.replace('=',',')
    p2 = p1.split(',')
    px = int(p2[1])
    py = int(p2[3])
    machine = [ax,bx,px,ay,by,py]
    machines.append(machine)
    l+=2
    
def isint(n):
    return n % 2 == 0
    
def sol(ax, bx, px, ay, by, py):

    determinant = ax * by - ay * bx

    a = (px * by - py * bx) / determinant
    b = (ax * py - ay * px) / determinant
    return int(a),int(b)

tot = 0
    
for m in machines:
    ax,bx,px,ay,by,py = m
    a,b = sol(ax,bx,px,ay,by,py)
    if (isint(a) and isint(b)) and a<100 and b<100:
        print(a,b)
        tot += a*3 + b
print(tot)




    


