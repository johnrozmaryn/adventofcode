from math import floor

def fuelreq(massinput):
    n = floor(massinput / 3.0) - 2
    return n

def complexfuelreq(massinput):
    total = 0
    currentmass = fuelreq(massinput)
    while (currentmass > 0):
        total += currentmass
        currentmass = fuelreq(currentmass)
    return total

f=open("Day01.input","r")
contents = f.readlines()

totalfuel = 0
for line in contents:
    totalfuel += complexfuelreq(float(line))
    print(totalfuel)
    
    


    