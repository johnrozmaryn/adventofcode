f = open("day08.in")
contents = (f.readlines())


ins = contents[0].strip()
length = len(ins)
dest = {}
for l in range(2,len(contents)):
    ind = contents[l].split('=')[0].strip()
    s = contents[l].split('=')[1].strip()
    t = s.strip('() ')
    u = t.split(', ')
    dest[ind] = u

foundlist = []
for i in dest:
    if i[2] == 'A':
        foundlist.append(i)
    
print(foundlist)

done = False

instructions = 1

while done == False:
    pos = (instructions % length) - 1
    if ins[pos] == 'L':
        d = 0
    else:
        d = 1
    endinz = []
    for f in range(len(foundlist)):
        foundlist[f] = dest[foundlist[f]][d]
        endinz.append(foundlist[f][2] == 'Z')
    instructions += 1
    if all(endinz):
        done = True
    
    
    

print(instructions-1)
    
    