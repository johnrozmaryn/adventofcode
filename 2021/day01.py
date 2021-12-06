f = open("day01.in")
contents = (f.readlines())
data = list(map(int, contents))

increase = 0

for i in range(1,len(data)):
    if data[i] > data[i-1]:
        increase +=1
        
print(increase)
        
     
