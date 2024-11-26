f = open("day09.in")
contents = (f.readlines())

d = []

for l in contents:
    d.append(l.split())
    
data = []

for i in d:
    j = []
    for n in i:
        j.append(int(n))
    data.append(j)
    
it = data[0]

# def gaps(row):
#     gaps = []
#     for n in range(len(row)-1):
#         gaps.append(row[n+1] - row[n])
#     return gaps

def findnext(row):
    if len(row) == 0:
        return 0
    gaps = []
    for n in range(len(row)-1):
        gaps.append(row[n+1] - row[n])       
    return row[-1] + findnext(gaps)
    
total = 0

for i in data:
    total += findnext(i)

print(total)
    