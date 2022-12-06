f = open("day06.in")
contents = (f.readlines())

line = contents[0]

for i in range(4,len(line)):
    if len(set(line[i-4:i])) == 4:
        break
print(i)

for i in range(14,len(line)):
    if len(set(line[i-14:i])) == 14:
        break
print(i)