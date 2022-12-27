f = open("day18.in")
contents = f.readlines()


pp = [] #possible pockets

cl = [] #cubelist
for l in contents:
    cl.append(eval('['+ l.strip() + ']'))

def add3(a,b): #add two three-element lists
    return [a[0] + b[0], a[1]+b[1], a[2]+b[2]]

def al(cl): #around list
    vecs = [[-1,0,0], [1,0,0], [0,-1,0], [0,1,0], [0,0,-1], [0,0,1]]
    ret = []
    for i in vecs:
        ret.append(add3(cl,i))
    return ret

faces = 0

for c in cl:
    for n in al(c):
        if n not in cl:
            faces += 1
            if n not in pp:
                pp.append(n)

ap = [] # actual pockets
for p in pp:
    around = 0
    for n in al(p):
        if n in cl:
            around += 1
    if around == 6:
        ap.append(p)

print(faces - len(ap) * 6)
    
###At the moment this is bad. I'm making a list of "possible pockets, but don't
###have a good way to subtract out those spots.        



    


    
    

