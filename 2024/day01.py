f = open("day01.in")
contents = (f.readlines())
left = []
right = []

for l in contents:
    print(l)
    s = l.split()
    left.append(int(s[0]))
    right.append(int(s[1]))

left.sort()
right.sort()

tot = 0

for n in range(len(left)):
    tot += abs(left[n] - right[n])

print(tot)

