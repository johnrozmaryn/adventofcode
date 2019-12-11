from itertools import permutations

prog1 = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
startseqlist = list(permutations([9,8,7,6,5]))

mem = []
inputs = []
outputs = []
waiting = []
isinitialized = []
hit99 = []
pointer = []

amps = ['A','B','C','D','E']

#initialize everything
for amp in amps:
    ampindex = amps.index(amp)
    mem.append(prog1)
    inputs = []
    # print(inputs)
    outputs.append(0)
    waiting.append(False)
    isinitialized.append(False)
    hit99.append(False)
    pointer.append(0)



def evalpos(amp,startpos):
    global inputs
    global outputs
    global hit99
    global pointer
    global mem
    ampindex = amps.index(amp)
        
    if startpos > len(mem[ampindex])-1:
        exit
    elif hit99[ampindex]:
#        return 99
        exit
    else:
        sCmd = str(mem[ampindex][startpos]).zfill(5) #I now have a string of 5 characters, nnnnn
        opcode = int(sCmd[-2:]) #number from last two characters in the string, nnnXX
        #immediate mode: use the value indicated by the parameter
        #position mode (like the original intcomputer): use the address indicated by the parameter
        p1imm = bool(int(sCmd[2])) #True/False for immediate mode of param1, nnXnn 
        p2imm = bool(int(sCmd[1])) #True/False for immediate mode of param2, nXnnn 
        p3imm = bool(int(sCmd[0])) #True/False for immediate mode of param3, Xnnnn

        if opcode == 1: #add next two parms
            p1 = mem[ampindex][startpos+1] if p1imm else mem[ampindex][mem[ampindex][startpos+1]]
            p2 = mem[ampindex][startpos+2] if p2imm else mem[ampindex][mem[ampindex][startpos+2]]
            mem[ampindex][mem[ampindex][startpos+3]] = p1 + p2
            pointer[ampindex] += 4
       
        elif opcode == 2: #multiply next two parms
            p1 = mem[ampindex][startpos+1] if p1imm else mem[ampindex][mem[ampindex][startpos+1]]
            p2 = mem[ampindex][startpos+2] if p2imm else mem[ampindex][mem[ampindex][startpos+2]]
            mem[ampindex][mem[ampindex][startpos+3]]= p1 * p2
            pointer[ampindex] += 4
       
        elif opcode == 3: #write input to parm1 address
            if len(inputs[ampindex]) > 0:
                mem[ampindex][mem[ampindex][startpos+1]] = inputs[ampindex].pop()
                pointer[ampindex] += 2
            else:
                waiting[ampindex] = True
       
        elif opcode == 4: #write parm1 to output
            p1 = mem[ampindex][startpos+1] if p1imm else mem[ampindex][mem[ampindex][startpos+1]]
            outputs[ampindex] = p1
            if ampindex == len(amps)-1:
                inputs[0].insert(0,p1)
                waiting[0] = False
            else:
                inputs[ampindex+1].insert(0,p1)
                waiting[ampindex+1] = False
            pointer[ampindex] += 2
       
        elif opcode == 5: #jump-if-true
            p1 = mem[ampindex][startpos+1] if p1imm else mem[ampindex][mem[ampindex][startpos+1]]
            p2 = mem[ampindex][startpos+2] if p2imm else mem[ampindex][mem[ampindex][startpos+2]]
            if p1 != 0: 
                pointer[ampindex] = p2
            else:
                pointer[ampindex] += 3
       
        elif opcode == 6: #jump-if-false
            p1 = mem[ampindex][startpos+1] if p1imm else mem[ampindex][mem[ampindex][startpos+1]]
            p2 = mem[ampindex][startpos+2] if p2imm else mem[ampindex][mem[ampindex][startpos+2]]        
            if p1 == 0:
                pointer[ampindex] = p2
            else:
                pointer[ampindex] += 3
        
        elif opcode == 7: #less than
            p1 = mem[ampindex][startpos+1] if p1imm else mem[ampindex][mem[ampindex][startpos+1]]
            p2 = mem[ampindex][startpos+2] if p2imm else mem[ampindex][mem[ampindex][startpos+2]]
            if p1<p2:
                mem[ampindex][mem[ampindex][startpos+3]] = 1
            else:
                mem[ampindex][mem[ampindex][startpos+3]] = 0
            pointer[ampindex] += 4
            
        elif opcode == 8: #equal
            p1 = mem[ampindex][startpos+1] if p1imm else mem[ampindex][mem[ampindex][startpos+1]]
            p2 = mem[ampindex][startpos+2] if p2imm else mem[ampindex][mem[ampindex][startpos+2]]  
            if p1 == p2:
                mem[ampindex][mem[ampindex][startpos+3]] = 1
            else:
                mem[ampindex][mem[ampindex][startpos+3]] = 0
            pointer[ampindex] += 4            
                
        elif opcode == 99: #end command
            hit99[ampindex] = True
            #print(mem[ampindex])
        else: #wtf happened?
            print("Invalid code:",opcode," at position ", startpos)
            print(mem[ampindex])
            exit()
 #       evalpos(amps[ampindex],pointer[ampindex])

def evalthrust(startseq):
    global mem
    global outputs
    global inputs
    global waiting
    global isinitialized
    global hit99
    global pointer
    
    mem = []
    inputs = []
    outputs = []
    waiting = []
    isinitialized = []
    hit99 = []
    pointer = []

    for amp in amps:
        ampindex = amps.index(amp)
        mem.append(prog1)
        inputs.append([])
        outputs.append(0)
        waiting.append(False)
        isinitialized.append(False)
        hit99.append(False)
        pointer.append(0)
  
        if ampindex == 0:
            inputs[ampindex].append(0) 
        
        inputs[ampindex].insert(0,startseq[ampindex])
    print('inputs',inputs)
    print('outputs',outputs)
        
    while not any(hit99):
        print('waiting',waiting)
        print('hit99',hit99)
        for amp in amps:
            ampindex = amps.index(amp)
            if not waiting[ampindex]:
                evalpos(amps[ampindex],pointer[ampindex])

    return outputs[len(outputs)-1]

print(evalthrust([9,7,8,5,6]))
print('last data')
print(mem)
print('outputs',outputs)
print('inputs',inputs)
print(pointer)
print('hit99', hit99)

# thrustlist = []

# for seq in startseqlist:
    # thrustlist.append(evalthrust(seq))

# maxindex = thrustlist.index(max(thrustlist))
# print(thrustlist[maxindex],startseqlist[maxindex])
    

 
    

    