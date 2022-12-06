f = open("day06.in")
contents = (f.readlines())

line = contents[0]
h = []

for i in range(0,13):
    h.append(line[i]) 

dupes = True

while dupes:
    for i in range(13,len(line)):
        h.append(line[i])
        countlist = []
        for j in range(0,13):
            countlist.append(h.count(h[j]))
        if max(countlist) < 2 :
            dupes = False
            break
        else:
            h.pop(0)
           
print(i+1)
        
        
        