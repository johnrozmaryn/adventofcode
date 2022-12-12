f = open("day10.in")
contents = (f.readlines())

#commands for easy reference
noop = 1
addx = 2

#start states
xreg = 1
cycle = 0
xhist = [1] #I'm cheating, putting a zero in here for the zeroth cycle

addcycle = 0
numtoadd = 0

for l in contents:
    cmd = l.strip().split()
    if cmd[0] == 'noop':
        xreg += numtoadd
        cycle += 1
        xhist.append(xreg)
        numtoadd = 0
    if cmd[0] == 'addx':
        xreg += numtoadd
        xhist.append(xreg)
        xhist.append(xreg)
        cycle += 2
        numtoadd = int(cmd[1])

total = 0

for n in range(20,221,40):
    total += n*xhist[n]

print(total)     
    
    



        