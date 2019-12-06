f=open("Day02.input","r")
pkgs = f.readlines()

total = 0

for pkg in pkgs:
    dims = pkg.split('x')
    s1 = int(dims[0]) * int(dims[1])
    s2 = int(dims[1]) * int(dims[2])
    s3 = int(dims[2]) * int(dims[0])
    total += min(s1,s2,s3) + 2*(s1+s2+s3)
    
print(total)
