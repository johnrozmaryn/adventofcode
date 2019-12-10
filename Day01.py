from math import floor

def fuelreq(massinput):
    n = floor(massinput / 3.0) - 2
    return n

f=open("c:/code/adventofcode/Day01.input","r")
contents = f.readlines()

totalfuel = 0
for line in contents:
    totalfuel += fuelreq(float(line))
    print(totalfuel)
    
    


    