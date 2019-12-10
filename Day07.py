from itertools import permutations

prog1 = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
startseqlist = list(permutations([4,3,2,1,0]))

mem = []
inputs = []
outputs = []
busy = []
isinitialized = []
hit99 = []
pointer = []

amps = ['A','B','C','D','E']

#initialize everything
for amp in amps:
    ampindex = amps.index(amp)
    mem.append(prog1)
    # inputs.append(startseq[ampindex])
    print(inputs)
    outputs.append(0)
    busy.append(False)
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
        return 99
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
            mem[ampindex][mem[ampindex][startpos+1]] = inputs[ampindex].pop()
            pointer[ampindex] += 2
       
        elif opcode == 4: #write parm1 to output
            p1 = mem[ampindex][startpos+1] if p1imm else mem[ampindex][mem[ampindex][startpos+1]]
            outputs[ampindex] = p1
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
        evalpos(amps[ampindex],pointer[ampindex])

def evalthrust(startseq):
    global mem
    global inputs
    global busy
    global isinitialized
    global hit99
    global pointer
    
    mem = []
    inputs = []
    outputs = []
    busy = []
    isinitialized = []
    hit99 = []
    pointer = []

    for amp in amps:
        ampindex = amps.index(amp)
        mem.append(prog1)
        outputs.append(0)
        busy.append(False)
        isinitialized.append(False)
        hit99.append(False)
        pointer.append(0)
    
    for amp in amps:
        ampindex = amps.index(amp)
        inputs.append([])
        if ampindex == 0:
            inputs[ampindex].append(0)
        else:
            inputs[ampindex].append(outputs[ampindex-1])
        inputs[ampindex].append(startseq[ampindex])
        print(amp,inputs)
        evalpos(amps[ampindex],0)
        print(mem[ampindex])
        print(outputs[ampindex])


    return outputs
  
print(evalthrust([4,3,2,1,0]))
print(inputs)
# for seq in startseqlist:
    # print(seq)
    # print(evalthrust(seq))
    

 
    

    