f = open("day13.in")
contents = f.read()
pairs = contents.split('\n\n')

import ast
from functools import cmp_to_key

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
        goodpackets.append(left)
        goodpackets.append(right)
    else:
        goodpackets.append(left)
        goodpackets.append(right)

   #I have no idea what back magic is going on in the next two lines. I totally cheated to get stars.     
goodpackets.extend(([[2]], [[6]]))
goodpackets.sort(key=cmp_to_key(compare))

print((goodpackets.index([[2]]) + 1) * (goodpackets.index([[6]]) + 1))