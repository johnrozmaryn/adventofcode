f = open("day03.in")
contents = (f.readlines())

decodestr = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

tot = 0

for l in contents:
    st = l.strip()
    leftset = set()
    rightset = set()
    strlen = len(st)
    midst = int(strlen/2)
    for i in range(0,midst):
        leftset.add(st[i])
        rightset.add(st[i+midst])
    un = list(leftset & rightset)
    tot += decodestr.index(un[0])+ 1
    
print(tot)
    
        
        
        

 
 
   
