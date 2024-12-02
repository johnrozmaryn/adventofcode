f = open("day01.in")
contents = (f.readlines())
left = []
right = []

for l in contents:
    print(l)
    s = l.split()
    left.append(int(s[0]))
    right.append(int(s[1]))

tot = 0

for l in left:
    tot += l * right.count(l)
    
print(tot)

