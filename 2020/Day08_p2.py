f=open("Day08.data")
contents = (f.read())
program = contents.splitlines()
linestochange = []


linesvisited = set()

accumulator = 0
currentpos = 0
linesvisited.add(currentpos)
keeprunning = True

def acc(input,pos):
    global accumulator
    accumulator += input
    return pos + 1

def jmp(input,pos):
    return pos + input
    
def nop(input,pos):
    return pos + 1
    
def runprogram(progtorun,linetochange):
    linesvisited = set()
    currentpos = 0
    linesvisited.add(currentpos)
    keeprunning = True
    global accumulator
    accumulator = 0
    while keeprunning:
        cmd, param = progtorun[currentpos].split()
        param = int(param)
        if cmd == 'acc':
            currentpos = acc(param,currentpos)
        if cmd == 'jmp':
            currentpos = jmp(param,currentpos)
        if cmd == 'nop':
            currentpos = nop(param,currentpos)
        if currentpos in linesvisited:
            return "InfiniteLoop, accumulator value: " + str(accumulator)
        if currentpos == len(progtorun):
            return "NormalExit after changeing " + str(linetochange) + ", accumulator value: " + str(accumulator)                 
        linesvisited.add(currentpos)
        
for line in range(0,len(program)):
    if program[line][:3] != 'acc':
        linestochange.append(line)
        
for cmd in linestochange:
    modprogram = program[:]
    if program[cmd][:3] == 'jmp':
        modprogram[cmd] = 'nop' + program[cmd][3:]
    if program[cmd][:3] == 'nop':
        modprogram[cmd] = 'jmp' + program[cmd][3:]
    print(runprogram(modprogram,cmd))


    
    
    
    
