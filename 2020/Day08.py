f=open("Day08.data")
contents = (f.read())
program = contents.splitlines()

linesvisited = set()

accumulator = 0
pos = 0
linesvisited.add(pos)
keeprunning = True

def acc(input):
    global accumulator
    global pos
    accumulator += input
    pos += 1

def jmp(input):
    global pos
    pos += input
    
def nop(input):
    global pos
    pos += 1
    


while keeprunning:
    # print("LinesVisited", linesvisited)
    cmd, param = program[pos].split()
    param = int(param)
    if cmd == 'acc':
        acc(param)
    if cmd == 'jmp':
        jmp(param)
    if cmd == 'nop':
        nop(param)
    if pos in linesvisited:
        keeprunning = False
    linesvisited.add(pos)

    
print(accumulator)
    
    
    
    
