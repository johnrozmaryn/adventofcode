moonnames = ['Io','Europa', 'Ganymede', 'Callisto']
moons = []
moonsorig = []


moonx = [16,0,6,-3,0,0,0,0]
moonxorig = [16,0,6,-3,0,0,0,0]

moony = [-11,-4,4,-2,0,0,0,0]
moonyorig = [-11,-4,4,-2,0,0,0,0]

moonz = [2,7,-10,-4,0,0,0,0]
moonzorig = [2,7,-10,-4,0,0,0,0]


# moonsorig.append([-1,0,2,0,0,0])
# moonsorig.append([2,-10,-7,0,0,0])
# moonsorig.append([4,-8,8,0,0,0])
# moonsorig.append([3,5,-1,0,0,0])

# moonx = [-1,2,4,3,0,0,0,0]
# moonxorig = [-1,2,4,3,0,0,0,0]

# moony = [0,-10,-8,5,0,0,0,0]
# moonyorig = [0,-10,-8,5,0,0,0,0]

# moonz = [2,-7,8,-1,0,0,0,0]
# moonzorig = [2,-7,8,-1,0,0,0,0]

def iteratex():
    for i in ((0,1),(0,2),(0,3),(1,2),(1,3),(2,3)):
        if moonx[i[0]] < moonx[i[1]]:
            moonx[i[0]+4] += 1
            moonx[i[1]+4] -= 1
        elif moonx[i[0]] > moonx[i[1]]:
            moonx[i[0]+4] -= 1
            moonx[i[1]+4] += 1
    moonx[0] += moonx[4]
    moonx[1] += moonx[5]
    moonx[2] += moonx[6]
    moonx[3] += moonx[7]
    # print(moonx)
            
xiterations = 1
iteratex()
while moonx != moonxorig:
    iteratex()
    xiterations += 1
print xiterations



def iteratey():
    for i in ((0,1),(0,2),(0,3),(1,2),(1,3),(2,3)):
        if moony[i[0]] < moony[i[1]]:
            moony[i[0]+4] += 1
            moony[i[1]+4] -= 1
        elif moony[i[0]] > moony[i[1]]:
            moony[i[0]+4] -= 1
            moony[i[1]+4] += 1
    moony[0] += moony[4]
    moony[1] += moony[5]
    moony[2] += moony[6]
    moony[3] += moony[7]
    # print(moony)
            
yiterations = 1
iteratey()
while moony != moonyorig:
    iteratey()
    yiterations += 1
print yiterations
         
def iteratez():
    for i in ((0,1),(0,2),(0,3),(1,2),(1,3),(2,3)):
        if moonz[i[0]] < moonz[i[1]]:
            moonz[i[0]+4] += 1
            moonz[i[1]+4] -= 1
        elif moonz[i[0]] > moonz[i[1]]:
            moonz[i[0]+4] -= 1
            moonz[i[1]+4] += 1
    moonz[0] += moonz[4]
    moonz[1] += moonz[5]
    moonz[2] += moonz[6]
    moonz[3] += moonz[7]
    # print(moonz)
            
ziterations = 1
iteratez()
while moonz != moonzorig:
    iteratez()
    ziterations += 1
print ziterations       

#https://www.calculatorsoup.com/calculators/math/lcm.php