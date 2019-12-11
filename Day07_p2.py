from itertools import permutations

prog1 = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
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
    print('entering evlapos for amp index', ampindex)
    print('memory is',mem[ampindex])
        
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
            print('didopcode1 at pointer',pointer[ampindex],'in amp',ampindex)
            print('using p1',p1,' and p2', p2)
            pointer[ampindex] += 4
       
        elif opcode == 2: #multiply next two parms
            p1 = mem[ampindex][startpos+1] if p1imm else mem[ampindex][mem[ampindex][startpos+1]]
            p2 = mem[ampindex][startpos+2] if p2imm else mem[ampindex][mem[ampindex][startpos+2]]
            mem[ampindex][mem[ampindex][startpos+3]]= p1 * p2
            pointer[ampindex] += 4
       
        elif opcode == 3: #write input to parm1 address
            if len(inputs[ampindex]) > 0:
                #mem[ampindex][startpos+1] = inputs[ampindex].pop()
                print('membeforepop',ampindex,mem[ampindex])
                numtoadd = inputs[ampindex].pop()
                print('numtoadd',numtoadd)
                mem[ampindex][mem[ampindex][startpos+1]] = numtoadd
                # mem[ampindex][mem[ampindex][startpos+1]] = inputs[ampindex].pop()
                print('memafterpop',ampindex,mem[ampindex])
                print('didopcode3 at ponter',pointer[ampindex],'in amp',ampindex)
                pointer[ampindex] += 2
            else:
                waiting[ampindex] = True
       
        elif opcode == 4: #write parm1 to output
            print('entering opcode 4')
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
        # evalpos(amps[ampindex],pointer[ampindex])
        print('exiting evalpos for amp', ampindex)
        print('mem when exiting', mem[ampindex])

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
        
        inputs[ampindex].insert(0,startseq[ampindex])
 
        if ampindex == 0:
            inputs[ampindex].insert(0,0)     
            
    # print('inputs',inputs)
    # print('outputs',outputs)
        
    while not hit99[len(hit99)-1]:
        # print('waiting',waiting)
        # print('hit99',hit99)
        # print('outputs',outputs)
        for amp in amps:
            ampindex = amps.index(amp)
            print('***ampindex',ampindex)
            print('-->allmemory',mem)
            if not waiting[ampindex]:
                if ampindex == 0:
                    print('inputs',inputs[ampindex])
                    print('output',outputs[ampindex])
                    print('membefore',ampindex,mem[ampindex])
                print('ampindex for evalpos ',ampindex)
                print('mem for that amp', mem[ampindex])
                evalpos(amps[ampindex],pointer[ampindex])
                if ampindex == 0:
                    print('memafter ',mem[ampindex])

    return outputs[len(outputs)-1]

print(evalthrust([9,8,7,6,999]))
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
    

 
    

    