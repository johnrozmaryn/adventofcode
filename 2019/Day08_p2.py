f=open("C:/code/adventofcode/Day08.input","r")
contents = f.readlines()

contentstr = contents[0]
layersize = 25*6
numlayers = int(len(contentstr) / layersize)
layers = []
pixels = []


for l in range(0,numlayers):
    layers.append(contentstr[(layersize*l):(layersize*(l+1))])

for i in range(0,layersize):
    pixels.append(2)

for l in range(0,numlayers):
    for i in range(0,len(pixels)):
        if int(pixels[i]) == 2:
            pixels[i] = int(layers[l][i])
print(pixels)
for i in range(0,6):
    print(pixels[i*25:(i+1)*25])
    
