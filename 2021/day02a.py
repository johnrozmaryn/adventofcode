f = open("day02.in")
contents = (f.readlines())

hpos = 0
depth = 0
aim = 0

for i in contents:
    direction, num = i.split()
    num = int(num)
    if direction == "down":
        aim += num
    if direction == "up":
        aim -= num
    if direction == "forward":
        hpos += num
        depth += num * aim
    if direction == "back":
        hpos -= num * aim
        depth -= num * aim

print(hpos,depth,hpos*depth)
        

        
     
