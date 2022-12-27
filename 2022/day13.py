f = open("day13.tst")
contents = f.read()
pairs = contents.split('\n\n')

import ast

#ahh! cmp is all weird in python 3!
#it was handy, because if l == r it's 0, if l>r postive, if l<r negative
def compare(l,r):    
    l_int = type(l) == type(1)   #see if they're integers
    r_int = type(r) == type(1)
    
    if l_int:
        if r_int:
            return l-r
        else:
            return compare([l],r)
    else:
        if r_int:
            return compare(l,[r])
        else:
            for ls,rs in zip(l,r):
                ans = compare(ls,rs)
                if ans != 0:
                    return ans
        
    return len(l) - len(r)
        
    
    

goodpackets = []

for item in pairs:
    left,right = item.split('\n')
    left = ast.literal_eval(left)
    right = ast.literal_eval(right)
    if compare(left,right) < 0:
        goodpackets.append(True)
    else:
        goodpackets.append(False)
        
total = 0
for i in range(len(goodpackets)):
    if goodpackets[i]:
        total += (1+i)
        
print(total)
    
    

