orbitee = []
orbiter = []
youlist = []
sanlist = []

f=open("C:/code/adventofcode/Day06.input","r")
contents = f.readlines()

for line in contents:
    pair = line.split(')')
    orbitee.append(pair[0])
    orbiter.append(pair[1].rstrip())


def findorbits(s):
    if s in orbiter:
        return 1 + findorbits(orbitee[orbiter.index(s)])
    else:
        return 0

def findorbityou(s):
    global youlist
    if s in orbiter:
        youlist.append(s)
        return 1 + findorbityou(orbitee[orbiter.index(s)])
    else:
        return 0

def findorbitsan(s):
    global sanlist
    if s in orbiter:
        sanlist.append(s)
        return 1 + findorbitsan(orbitee[orbiter.index(s)])
    else:
        return 0

findorbityou('YOU')
findorbitsan('SAN')

common = 0

for i in youlist:
    if i in sanlist:
        common += 1

print(len(youlist) + len(sanlist) - common - common-2)



    
    


    