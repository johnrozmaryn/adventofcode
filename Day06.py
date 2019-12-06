orbitee = []
orbiter = []

f=open("C:/code/adventofcode/Day06.input","r")
contents = f.readlines()

for line in contents:
    pair = line.split(')')
    orbitee.append(pair[0])
    orbiter.append(pair[1].rstrip())

for i in range(0,len(orbitee)):
    print(orbitee[i],orbiter[i])

def findorbits(s):
    if s in orbiter:
        return 1 + findorbits(orbitee[orbiter.index(s)])
    else:
        return 0

orbiterset = set(orbiter)
total = 0
for i in orbiterset:
    total += findorbits(i)
print(total)


    
    


    