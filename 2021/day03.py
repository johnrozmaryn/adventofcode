f = open("day03.in")
contents = (f.readlines())

numInputs = len(contents)
width = len(contents[0].strip())

gamma = []
epsilon = []

for i in range(0,width):
    posSum = 0
    for n in contents:
        posSum += int(n[i])
    if posSum > numInputs / 2:
        gamma.append(1)
        epsilon.append(0)
    else:
        gamma.append(0)
        epsilon.append(1)
        
        
def binlist2dec(binlist):
    binlist.reverse()
    dec = 0
    for i in range(0,len(binlist)):
        dec += binlist[i] * (2**i)
    return dec
        
print(binlist2dec(gamma)* binlist2dec(epsilon))
        
     
