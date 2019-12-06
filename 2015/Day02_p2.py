f=open("Day02.input","r")
pkgs = f.readlines()


total = 0

for pkg in pkgs:
    dims = pkg.split('x')
    x,y,z = int(dims[0]),int(dims[1]),int(dims[2])
    s1 = x+y
    s2 = y+z
    s3 = x+z
    total += 2*min(s1,s2,s3) + x*y*z
    
print(total)
