f = open("day18.in")
contents = f.readlines()


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


print(faces)
    
        



    


    
    

