f = open("day01.in")
contents = (f.readlines())
# test answer should be 6

dirlist = []
for l in contents:
    s = l.strip()
    dirlist.append([s[0],int(s[1:])])
    
numzeros = 0
pos = 50

for i in dirlist:
    numzeros += i[1] // 100
    
    if i[0] == 'L':
        if (i[1] % 100) > pos and (pos != 0):
            numzeros += 1
        pos = (pos - i[1]) % 100
        
    else:
        if (i[1] % 100 > (100-pos)) and pos != 0:
            numzeros += 1

        pos = (pos + i[1]) % 100
    
    if pos == 0:
        numzeros += 1

print(numzeros)
       

    
    
    

