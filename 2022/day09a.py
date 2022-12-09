f = open("day09.in")
contents = (f.readlines())

v = set()
klist = []
for i in range(10):
    klist.append([0,0])
# klist[0] will be the head

def movetail(h,t):
    dif = [h[0]-t[0], h[1]-t[1]]
    
    if dif in [[1,2],[2,2],[2,1]]:
        t[0] += 1
        t[1] += 1
    if dif == [2,0]:
        t[0] += 1
    if dif in [[2,-1],[2,-2],[1,-2]]:
        t[0] += 1
        t[1] -= 1
    if dif == [0,-2]:
        t[1] -= 1
    if dif in [[-1,-2],[-2,-2],[-2,-1]]:
        t[0] -= 1
        t[1] -= 1
    if dif == [-2,0]:
        t[0] -= 1
    if dif in [[-2,1],[-2,2],[-1,2]]:
        t[0] -= 1
        t[1] += 1
    if dif == [0,2]:
        t[1] +=1    

for l in contents:
    cmd = l.split()
    c,n = cmd[0], int(cmd[1]) 
       
    for i in range(n):
        if c == 'R':
            klist[0][0] += 1
        elif c == 'L':
            klist[0][0] -= 1
        elif c == 'U':
            klist[0][1] += 1
        elif c == 'D':
            klist[0][1] -= 1

        for i in range(9):
            movetail(klist[i],klist[i+1])
            
        v.add(str(klist[9][0]) + '_' + str(klist[9][1]))


print(len(v))
