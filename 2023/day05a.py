f = open("day05.in")
contents = (f.readlines())
contents.append('')


minloc = 5000000000

seedstr = contents[0].strip().split(':')[1].split()
seedrng = []
for s in range(len(seedstr)):
    seedrng.append(int(seedstr[s]))
    
line = 2
td = []
trans = []
while line < len(contents):
    st = contents[line].strip()
    if ':' in st:
        line += 1
        print(line)
    elif st == '':
        td.append(trans)
        line += 1
        print(line)
        trans = []
    else:
        x,y,z = st.split()
        trans.append([int(x),int(y),int(z),set(range(int(y),int(z)+1))])
        line += 1
        print(line)

def transform(s, level):
    numxforms = len(td[level])
    done = False
    while done == False:
        for i in range(0,numxforms):
            if s in td[level][i][3]:
                return s + td[level][i][0] - td[level][i][1]            
        return s
        done == True
        

def findchun(seeds,minl):
    loc = seeds
    for level in range(len(td)):
        loc = transform(loc,level)
    return min(loc,minl)
      
         
                        



i = 0
while i < len(seedrng):

    for j in range(seedrng[i],seedrng[i] + seedrng[i+1]):
        minloc = findchun(j,minloc)
    print('i is ',i)
    print('minloc is', minloc)

    i += 2

        

                         
                      
        
#now that's in place, let me make a backwards function


        
    
        
    
    
        
        
        
        