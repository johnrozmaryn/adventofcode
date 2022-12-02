f = open("day01.in")
contents = (f.readlines())

cals = []
tot = 0

for l in contents:
    temp = l.strip()
    if temp == '':
        cals.append(tot)
        tot=0
    else:
        tot += int(temp)
        
maxcals = max(cals)
pos = cals.index(maxcals)
print(pos + 1)
print(maxcals)


 
 
   
