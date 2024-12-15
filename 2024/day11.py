from collections import defaultdict
f = open("day11.in")
contents = (f.readlines())
m = contents[0].split()

stones = defaultdict(int)
xfer = defaultdict(str)


for s in m:
    stones[s] += 1
    
xfer['0'] =['1']

def blink(stones):
    newstones = defaultdict(int)
    for item in stones:
        if xfer[item] == '':
            if len(item) % 2 == 0:
                l = len(item)
                mid = int(l/2)
                left = item[:mid]
                right = item[mid:]
                xfer[item] = [str(int(left)),str(int(right))]
            else:
                xfer[item]= [str(2024 * int(item))]          

        for i in xfer[item]:
            newstones[i] += stones[item]
    return newstones
print(stones)
for i in range(25):
    tot = 0
    stones = blink(stones)
for s in stones:
    tot += stones[s]
print(tot)

            
           
            

                
                

            
        
    

