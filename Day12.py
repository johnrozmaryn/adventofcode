moonnames = ['Io','Europa', 'Ganymede', 'Callisto']
moons = []

# moons.append([-1,0,2,0,0,0])
# moons.append([2,-10,-7,0,0,0])
# moons.append([4,-8,8,0,0,0])
# moons.append([3,5,-1,0,0,0])

moons.append([16,-11,2,0,0,0])
moons.append([0,-4,7,0,0,0])
moons.append([6,4,-10,0,0,0])
moons.append([-3,-2,-4,0,0,0])

def iterate():
    global moons
    #apply gravity
    for imoon in moons:
        i = moons.index(imoon)
        for jmoon in moons:
            j = moons.index(jmoon)
            if i != j:
                if moons[i][0] < moons[j][0]:
                    moons[i][3] +=1
                elif moons[i][0] > moons[j][0]:
                    moons[i][3] -=1

                if moons[i][1] < moons[j][1]:
                    moons[i][4] +=1
                elif moons[i][1] > moons[j][1]:
                    moons[i][4] -=1
                    
                if moons[i][2] < moons[j][2]:
                    moons[i][5] +=1
                elif moons[i][2] > moons[j][2]:
                    moons[i][5] -=1
          
    #apply velocity
    for m in moons:
        m[0] += m[3]
        m[1] += m[4]
        m[2] += m[5]

print(moons)
for i in range(0,1000):
    iterate()
#    print(moons)
    
energy = 0
for i in moons:
    pot = abs(i[0]) + abs(i[1]) + abs(i[2])
    kin = abs(i[3]) + abs(i[4]) + abs(i[5])
    energy += pot*kin
print(energy)
    
