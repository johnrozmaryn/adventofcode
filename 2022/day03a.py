f = open("day03.in")
contents = (f.readlines())

decodestr = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

tot = 0

for n in range(0,len(contents),3):
    set1 = set()
    
    line = contents[n].strip()
    for i in line:
        set1.add(i)
    set2 = set()
    line = contents[n+1].strip()
    for i in line:
        set2.add(i)
    set3 = set()
    line = contents[n+2].strip()
    for i in line:
        set3.add(i)

    un = list(set1 & set2 & set3)
    tot += decodestr.index(un[0])+ 1
    
print(tot)
    
        
        
        

 
 
   