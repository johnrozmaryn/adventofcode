f = open("day06.in")
contents = (f.readlines())
contents.append('')

time = contents[0].split(':')[1].strip().split()
dist = contents[1].split(':')[1].strip().split()

for i in range(len(time)):
    time[i] = int(time[i])
    dist[i] = int(dist[i])
  
winlist = []

i = 0
while i < len(time):
    t = 1
    wins = 0
    while t < time[i]:   
        travel = t*(time[i] - t)
        if travel > dist[i]:
            wins += 1
        t += 1
    winlist.append(wins)
    i += 1
    
total = 1
for i in winlist:
    total = total * i
    
print(total)

