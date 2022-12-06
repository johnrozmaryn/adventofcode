f = open("day06.in")
contents = (f.readlines())

line = contents[0]
h = []

for i in range(0,3):
    h.append(line[i]) 

dupes = True

while dupes:
    for i in range(3,len(line)):
        h.append(line[i])
        countlist = []
        for j in range(0,3):
            countlist.append(h.count(h[j]))
        if max(countlist) < 2 :
            dupes = False
            break
        else:
            h.pop(0)
    
            
print(i+1)
        
        
        