f = open("day01.in")
contents = (f.readlines())
data = list(map(int, contents))

increase = 0

for i in range(3,len(data)):
    lowrange = data[i-3] + data[i-2] + data[i-1]
    highrange = data[i-2] + data[i-1] + data[i]
    if highrange > lowrange:
        increase +=1
        
print(increase)
        
     
