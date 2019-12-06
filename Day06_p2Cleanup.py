orbitee = []
orbiter = []
youlist = []
sanlist = []

#Rookie move: need different paths depending on which computer I'm on
#f=open("C:/code/adventofcode/Day06.input","r")
f=open("Day06.input","r")
contents = f.readlines()

for line in contents:
    pair = line.split(')')
    orbitee.append(pair[0])
    orbiter.append(pair[1].rstrip())


def findorbits(s,routelist):
    if s in orbiter:
        routelist.append(s)
        return 1 + findorbits(orbitee[orbiter.index(s)],routelist)
    else:
        return 0

findorbits('YOU',youlist)
findorbits('SAN',sanlist)

common = 0

for i in youlist:
    if i in sanlist:
        common += 1

print(len(youlist) + len(sanlist) - common - common-2)



    
    


    