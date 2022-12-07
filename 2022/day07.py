f = open("day07.in")
contents = (f.readlines())

d = {}  #dictionary to hold the value of each path
path = '' #current path
cdir = '' #current directory
dirstack = []



for c in contents:
    l = c.strip().split()
    if l[0] == '$':
        if l[1] == 'cd':
            cdir = l[2]
            if cdir == '..':
                dirstack.pop()
                currentdirsize = d[path]
                path = ''.join(dirstack)
                d[path] += currentdirsize
                
            elif cdir == '/':
                path += cdir
                dirstack.append(cdir)
            else:
                path += cdir + '/'
                dirstack.append(cdir + '/')
            if path not in d:
                d[path] = 0
    if l[0].isnumeric():
        d[path] += int(l[0])
        
tot = 0
for n in d.values():
    if n <= 100000:
        tot += n
        
print(tot)
        
        
        