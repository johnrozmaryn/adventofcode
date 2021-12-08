f = open("day03.in")
contents = (f.readlines())

numInputs = len(contents)
width = len(contents[0].strip())

def binlist2dec(binlist):
    binlist.reverse()
    dec = 0
    for i in range(0,len(binlist)):
        dec += binlist[i] * (2**i)
    return dec

def removeitems(startlist,position,toremove):
    outlist = []
    for n in startlist:
        if int(n[position]) != toremove:
            outlist.append(n)
    return outlist


# find oxygen generator rating
oxlist = contents[:]

while len(oxlist) > 1:
    for i in range(0,width):
        tempsum = 0
        for n in oxlist:
            tempsum += int(n[i])
        if tempsum >= len(oxlist) / 2: #1 occurs more than 0
            if len(oxlist) > 1:
                oxlist = removeitems(oxlist,i,0)
        if tempsum < len(oxlist) / 2: #0 occurs more than 1
            if len(oxlist) > 1:
               oxlist = removeitems(oxlist,i,1)
            
co2list = contents[:]
while len(co2list) > 1:
    for i in range(0,width):
        tempsum = 0
        for n in co2list:
            tempsum += int(n[i])
        if tempsum >= len(co2list) / 2: #1 occurs more than 0
            if len(co2list) > 1:
                co2list = removeitems(co2list,i,1)
        if tempsum < len(co2list) / 2: #0 occurs more or equal than 1
            if len(co2list) > 1:
                co2list = removeitems(co2list,i,0)
            
print(int(oxlist[0].strip(),2) * int(co2list[0].strip(),2))


                         
            
 
        


        
     
