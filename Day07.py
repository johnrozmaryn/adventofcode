
prog1 = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
startseq = [4,3,2,1,0]

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
    inputs.append(startseq[ampindex])
    outputs.append(0)
    busy.append(False)
    isinitialized.append(False)
    hit99.append(False)
    pointer.append(0)



def evalpos(amp,startpos):
    global input
    global output
    global hit99
    global pointer
    global mem
    jmp = 0 #how far my readindex will jump after the instruction.
    ampindex = amps.index(amp)
        
    if startpos > len(mem[ampindex])-1:
        exit
    elif hit99[ampindex]:
        print("Found a 99 at pos:",startpos)
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
            mem[ampindex][mem[ampindex][startpos+1]] = inputs[ampindex]
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

for amp in amps:
    ampindex = amps.index(amp)
    inputs[ampindex] = startseq[ampindex]
    print("orig",mem[ampindex])
    print("originput",inputs[ampindex])
    print("origoutput",outputs[ampindex])
    evalpos(amp,0)
    hit99[ampindex] = False
    pointer[ampindex] = 0
    print("second",mem[ampindex])
    print("secondinput",inputs[ampindex])
    print("secondoutput",outputs[ampindex])
    if ampindex == 0:
        inputs[ampindex] = 0
    else:
        inputs[ampindex] = outputs[ampindex - 1]
    evalpos(amp,0)
    print("third",mem[ampindex])
    print("thirdinput",inputs[ampindex])
    print("thirdoutput",outputs[ampindex])
    # print(outputs[ampindex])

 
    

    