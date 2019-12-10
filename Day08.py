f=open("C:/code/adventofcode/Day08.input","r")
contents = f.readlines()

contentstr = contents[0]
layersize = 25*6
print(layersize)
numlayers = int(len(contentstr) / layersize)
print(numlayers)
layers = []
tot0 = []
tot1 = []
tot2 = []

for l in range(0,numlayers):
    layers.append(contentstr[(layersize*l):(layersize*(l+1))])
    print(len(layers[l]))
    tot0.append(layers[l].count('0'))
    tot1.append(layers[l].count('1'))
    tot2.append(layers[l].count('2'))

minnum = min(tot0)
minindex = tot0.index(minnum)
print(tot1[minindex]*tot2[minindex])