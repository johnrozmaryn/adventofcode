
prog1 = [3,225,1,225,6,6,1100,1,238,225,104,0,1102,27,28,225,1,113,14,224,1001,224,-34,224,4,224,102,8,223,223,101,7,224,224,1,224,223,223,1102,52,34,224,101,-1768,224,224,4,224,1002,223,8,223,101,6,224,224,1,223,224,223,1002,187,14,224,1001,224,-126,224,4,224,102,8,223,223,101,2,224,224,1,224,223,223,1102,54,74,225,1101,75,66,225,101,20,161,224,101,-54,224,224,4,224,1002,223,8,223,1001,224,7,224,1,224,223,223,1101,6,30,225,2,88,84,224,101,-4884,224,224,4,224,1002,223,8,223,101,2,224,224,1,224,223,223,1001,214,55,224,1001,224,-89,224,4,224,102,8,223,223,1001,224,4,224,1,224,223,223,1101,34,69,225,1101,45,67,224,101,-112,224,224,4,224,102,8,223,223,1001,224,2,224,1,223,224,223,1102,9,81,225,102,81,218,224,101,-7290,224,224,4,224,1002,223,8,223,101,5,224,224,1,223,224,223,1101,84,34,225,1102,94,90,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1007,677,677,224,102,2,223,223,1005,224,329,101,1,223,223,1108,226,677,224,1002,223,2,223,1005,224,344,101,1,223,223,1008,677,677,224,102,2,223,223,1005,224,359,101,1,223,223,8,226,677,224,1002,223,2,223,1006,224,374,101,1,223,223,108,226,677,224,1002,223,2,223,1006,224,389,1001,223,1,223,1107,226,677,224,102,2,223,223,1005,224,404,1001,223,1,223,7,226,677,224,1002,223,2,223,1005,224,419,101,1,223,223,1107,677,226,224,102,2,223,223,1006,224,434,1001,223,1,223,1107,226,226,224,1002,223,2,223,1006,224,449,101,1,223,223,1108,226,226,224,1002,223,2,223,1005,224,464,101,1,223,223,8,677,226,224,102,2,223,223,1005,224,479,101,1,223,223,8,226,226,224,1002,223,2,223,1006,224,494,1001,223,1,223,1007,226,677,224,1002,223,2,223,1006,224,509,1001,223,1,223,108,226,226,224,1002,223,2,223,1006,224,524,1001,223,1,223,1108,677,226,224,102,2,223,223,1006,224,539,101,1,223,223,1008,677,226,224,102,2,223,223,1006,224,554,101,1,223,223,107,226,677,224,1002,223,2,223,1006,224,569,101,1,223,223,107,677,677,224,102,2,223,223,1006,224,584,101,1,223,223,7,677,226,224,102,2,223,223,1005,224,599,101,1,223,223,1008,226,226,224,1002,223,2,223,1005,224,614,1001,223,1,223,107,226,226,224,1002,223,2,223,1005,224,629,101,1,223,223,7,226,226,224,102,2,223,223,1006,224,644,1001,223,1,223,1007,226,226,224,102,2,223,223,1006,224,659,101,1,223,223,108,677,677,224,102,2,223,223,1005,224,674,1001,223,1,223,4,223,99,226]

input = 5
output = 0
hit99 = False
pointer = 0

def evalpos(startpos,inarr):
    global input
    global output
    global hit99
    global pointer
    jmp = 0 #how far my readindex will jump after the instruction.
    
    if startpos > len(inarr)-1:
        exit
    elif hit99:
        print("Found a 99 at pos:",startpos)
    else:
        sCmd = str(inarr[startpos]).zfill(5) #I now have a string of 5 characters, nnnnn
        opcode = int(sCmd[-2:]) #number from last two characters in the string, nnnXX
        #immediate mode: use the value indicated by the parameter
        #position mode (like the original intcomputer): use the address indicated by the parameter
        p1imm = bool(int(sCmd[2])) #True/False for immediate mode of param1, nnXnn 
        p2imm = bool(int(sCmd[1])) #True/False for immediate mode of param2, nXnnn 
        p3imm = bool(int(sCmd[0])) #True/False for immediate mode of param3, Xnnnn

        if opcode == 1: #add next two parms
            p1 = inarr[startpos+1] if p1imm else inarr[inarr[startpos+1]]
            p2 = inarr[startpos+2] if p2imm else inarr[inarr[startpos+2]]
            inarr[inarr[startpos+3]] = p1 + p2
            pointer += 4
       
        elif opcode == 2: #multiply next two parms
            p1 = inarr[startpos+1] if p1imm else inarr[inarr[startpos+1]]
            p2 = inarr[startpos+2] if p2imm else inarr[inarr[startpos+2]]
            inarr[inarr[startpos+3]]= p1 * p2
            pointer += 4
       
        elif opcode == 3: #write input to parm1 address
            inarr[inarr[startpos+1]] = input
            pointer += 2
       
        elif opcode == 4: #write parm1 to output
            p1 = inarr[startpos+1] if p1imm else inarr[inarr[startpos+1]]
            output = p1
            pointer += 2
       
        elif opcode == 5: #jump-if-true
            p1 = inarr[startpos+1] if p1imm else inarr[inarr[startpos+1]]
            p2 = inarr[startpos+2] if p2imm else inarr[inarr[startpos+2]]
            if p1 != 0: 
                pointer = p2
            else:
                pointer += 3
       
        elif opcode == 6: #jump-if-false
            p1 = inarr[startpos+1] if p1imm else inarr[inarr[startpos+1]]
            p2 = inarr[startpos+2] if p2imm else inarr[inarr[startpos+2]]        
            if p1 == 0:
                pointer = p2
            else:
                pointer += 3
        
        elif opcode == 7: #less than
            p1 = inarr[startpos+1] if p1imm else inarr[inarr[startpos+1]]
            p2 = inarr[startpos+2] if p2imm else inarr[inarr[startpos+2]]
            if p1<p2:
                inarr[inarr[startpos+3]] = 1
            else:
                inarr[inarr[startpos+3]] = 0
            pointer += 4
            
        elif opcode == 8: #equal
            p1 = inarr[startpos+1] if p1imm else inarr[inarr[startpos+1]]
            p2 = inarr[startpos+2] if p2imm else inarr[inarr[startpos+2]]  
            if p1 == p2:
                inarr[inarr[startpos+3]] = 1
            else:
                inarr[inarr[startpos+3]] = 0
            pointer += 4            
                
        elif opcode == 99: #end command
            hit99 = True
            #print(inarr)
        else: #wtf happened?
            print("Invalid code:",opcode," at position ", startpos)
            print(inarr)
            exit()
        evalpos(pointer,inarr)

evalpos(0,prog1)  
        
print(output)
    

    