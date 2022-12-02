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
cals.sort()
print(cals[-1] + cals[-2]+ cals[-3])



 
 
   
