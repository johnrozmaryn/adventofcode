f = open("day05.in")
contents = (f.readlines())

letterstring = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

stackwidth = len(contents[0].strip('\n'))
numstacks = stackwidth // 4 + 1

stacklist = []
for i in range(1,numstacks+1):
    stacklist.append([])
    
Stackphase = True


for l in contents:
    if l == '\n':
        Stackphase = False     #The section before the line breaks sets up the stacks
    else:
        if Stackphase:
            for i in range(0,stackwidth):
                if l[i] in letterstring:
                    stacklist[(i+1)//4].insert(0,l[i])
        else:   #we're now in the list of commands
            cmd = l.split()
            numtomove = int(cmd[1])
            fromstack = int(cmd[3]) - 1
            tostack = int(cmd[5]) - 1
            for i in range(0,numtomove):
                stacklist[tostack].append(stacklist[fromstack].pop())
            

outstr = ''
for l in stacklist:
    outstr += l.pop()
    
print(outstr)
            
        
        
        