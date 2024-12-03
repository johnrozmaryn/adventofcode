f = open("day02.in")
contents = (f.readlines())



def issafe(nlist):
    allpos = True
    allneg = True
    smallvar = True
    nozeros = True
    
    for n in range(1,len(nlist)):
        diff = nlist[n] - nlist[n-1]
        if diff == 0:
            nozeros = False
        elif diff < 0:
            allpos = False
        elif diff > 0:
            allneg = False
        if abs(diff) > 3:
            smallvar = False
            
    return (smallvar and nozeros) and (allpos or allneg)


tot = 0

for l in contents:
    line = l.split()
    nlist = []
    for n in line:
       nlist.append(int(n))
       
    if issafe(nlist):
        tot += 1
    else:
        for i in range(len(nlist)):
            if issafe(nlist[:i] + nlist[i+1:]):
                tot+=1
                break
            
    
print(tot)






        

            
            
        
    
    
        
    

 
