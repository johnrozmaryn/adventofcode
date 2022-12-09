f = open("day09.in")
contents = (f.readlines())

v = set()   # places the tail has visited, stored as a string of x_y
t = [0,0]   # t[x,y] is the position of the tail
h = [0,0]

for l in contents:
    cmd = l.split()
    c,n = cmd[0], int(cmd[1]) 
       
    for i in range(n):
        if c == 'R':
            h[0] += 1
        elif c == 'L':
            h[0] -= 1
        elif c == 'U':
            h[1] += 1
        elif c == 'D':
            h[1] -= 1
    
        dif = [h[0]-t[0], h[1]-t[1]]
        
        if dif in [[1,2],[2,2],[2,1]] :
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
            
        v.add(str(t[0]) + '_' + str(t[1]))
              
print(len(v))

        
        