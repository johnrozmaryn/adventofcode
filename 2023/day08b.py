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
    
found = 'VKA'
instructions = 1

visited = []

while found[2] != 'Z':
    visited.append(found)
    pos = (instructions % length) - 1  
    if ins[pos] == 'L':
        found = dest[found][0]
    else:
        found = dest[found][1]
        
    instructions += 1
    # if found in visited:
    #     break
    

print(instructions-1)
    
    