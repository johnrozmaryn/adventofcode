f = open("day05.in")
contents = (f.readlines())
contents.append('')


seeds = contents[0].strip().split(':')[1].split()
for s in range(len(seeds)):
    seeds[s] = int(seeds[s])

line = 2
td = []
trans = []
while line < len(contents):
    st = contents[line].strip()
    if ':' in st:
        line += 1
    elif st == '':
        td.append(trans)
        line += 1
        trans = []
    else:
        x,y,z = st.split()
        trans.append([int(x),int(y),int(z)])
        line += 1
        
def transform(s, level):
    numxforms = len(td[level])
    done = False
    while done == False:
        for i in range(0,numxforms):
            if s in range(td[level][i][1],td[level][i][1]+td[level][i][2]+1):
                return s + td[level][i][0] - td[level][i][1]            
        return s
        done == True
                
                                                 
                      
        
#now that's in place, let me make a backwards function


loclist = []
for s in seeds:
    loc = s
    for level in range(len(td)):
        loc = transform(loc,level)
    loclist.append(loc)
 
print(min(loclist))
        
    
        
    
    
        
        
        
        