f = open("day09.in")
contents = (f.readlines())

m = contents[0].strip()


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
        pos += 1
    if isnum(currins):
        currnum += 1
    currins += 1
print(out)
i = 0
maxlen = len(out)-1
while i < maxlen:
    if out[i] == '.':
        tmp = '.'
        while tmp == '.' and i < len(out):
            tmp = out.pop(-1)
            maxlen -= 1
        if i < maxlen:
            out[i] = tmp
    i += 1

tot = 0
for i in range(len(out)):
    tot += i * out[i]
print(tot)

        
    

    
    


    
    
        
    
