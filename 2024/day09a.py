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
    
def find_sublist(main_list, sub_list):
    for i in range(len(main_list) - len(sub_list) + 1):
        if main_list[i:i + len(sub_list)] == sub_list:
            return i
    return -1

while currnum > 0:
    if currnum in out:
        i = out.index(currnum)
        c = out.count(currnum)
        s = find_sublist(out[0:i],['.']*c)
        if s != -1:
            for sl in range(c):
                out[s+sl] = currnum
                out[i+sl] = '.'
    currnum -= 1
    print(currnum)
    
tot = 0
for i in range(len(out)):
    if out[i] != '.':
        tot += i * out[i]
print(tot)

        
    

    
    


    
    
        
    
