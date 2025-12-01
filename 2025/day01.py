f = open("day01.in")
contents = (f.readlines())

dirlist = []
for l in contents:
    s = l.strip()
    dirlist.append([s[0],int(s[1:])])
    
numzeros = 0
pos = 50

for i in dirlist:
    if i[0] == 'L':
        pos = (pos - i[1]) % 100
    else:
        pos = (pos + i[1]) % 100
    
    if pos == 0:
       numzeros += 1

print(numzeros)
       

    
    
    

