f = open("day09.in")
contents = (f.readlines())

m = contents[0].strip()

mt = []
out = []

def isnum(n):
    return n % 2 == 0

currnum = 0
pos = 0
currins = 0
while currins in range(len(m)):
    num = int(m[currins])
    for i in range(num):
        if isnum(currins):
            out.append(currnum)
        else:
            out.append('.')
            mt.append(pos)
        pos += 1
    if isnum(currins):
        currnum += 1
    currins += 1
    
for i in mt:
    tmp = '.'
    if i < len(out):
        while tmp == '.':
            tmp = out.pop()
        if i < len(out)+1: 
            out[i] = tmp
        
tot = 0
for i in range(len(out)):
    tot += i * out[i]
print(tot)

        
    

    
    


    
    
        
    
