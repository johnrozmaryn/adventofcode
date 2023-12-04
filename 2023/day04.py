f = open("day04.in")
contents = (f.readlines())

lst = []
for l in contents:
    lst.append(l.strip())


gl = []
total = 0
for l in lst:
    a,b = l.split(':')
    game = int(a.split()[1])
    c,d = b.split('|')
    drawnum = set(c.split())
    mynum = set(d.split())
    wins = len(drawnum.intersection(mynum))
    if wins > 0:
        total += 2**(wins-1)
        
print(total)
    
            
            
            