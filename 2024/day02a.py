f = open("day02.tst")
contents = (f.readlines())

tot = 0

for l in contents:
    line = l.split()
    nlist = []
    for n in line:
       nlist.append(int(n))
    plist = []


    for n in range(1,len(nlist)):
        diff = nlist[n] - nlist[n-1]
        if diff == 0:
            problem = true
        elif diff < 0:
            allpos = False
        elif diff > 0:
            allneg = False
        if abs(diff) > 3:
            smallvar = False
            
    if (smallvar and noZeroes) and (allpos or allneg):
        
        tot += 1 if (smallvar and noZeroes) and (allpos or allneg):
     
     tot += 1
     
print(tot)
            
            
        
    
    
        
    

 
