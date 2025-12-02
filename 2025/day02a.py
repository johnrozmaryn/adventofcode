import re
repeats = r'^(..*?)\1{1,}$'

f = open("day02.in")
contents = (f.readlines())


rnglist = contents[0].split(',')

def invalid(i):
    s = str(i)
    if re.search(repeats,s):
        return True
    else:
        return False
    
invalids = []

for rng in rnglist:
    s = rng.split('-')
    l = int(s[0])
    r = int(s[1])
    for i in range(l,r+1):
        if invalid(i):
            invalids.append(i)
            
sum = 0
for i in invalids:
    sum += i
    
print(sum)
    
    
    




    
    
    

