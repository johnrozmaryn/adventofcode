f = open("day04.in")
contents = (f.readlines())


def inrange(st1,st2):
    lst1 = st1.split('-')
    lst2 = st2.split('-')
    set1 = set()
    set2 = set()
    for i in range(int(lst1[0]),int(lst1[1])+1):
        set1.add(i)
    for i in range(int(lst2[0]),int(lst2[1])+1):
        set2.add(i)
    if len(set1 & set2) >= 1:
        return True
    else:
        return False


tot = 0
for l in contents:
    s = l.strip()
    sp = s.split(',')
    
    if inrange(sp[0],sp[1]) or inrange(sp[1],sp[0]):
        tot +=1
    
print(tot)