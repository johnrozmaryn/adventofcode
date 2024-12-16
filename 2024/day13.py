f = open("day13.in")
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
    machine = [ax,ay,bx,by,px,py]
    machines.append(machine)
    l+=2
    
    

    


