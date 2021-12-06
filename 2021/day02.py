f = open("day02.in")
contents = (f.readlines())

hpos = 0
depth = 0


for i in contents:
    print(i)
    direction, num = i.split()
    num = int(num)
    if direction == "down":
        depth += num
    if direction == "up":
        depth -= num
    if direction == "forward":
        hpos += num
    if direction == "back":
        hpos -= num

print(hpos,depth,hpos*depth)
        

        
     
