f = open("day03.in")
contents = (f.readlines())

lst = []
for l in contents:
    lst.append(l.strip())

def adjsym(row,col):
    adjsym = False
    rmin = -1 
    cmin = -1
    rmax = 1 
    cmax = 1
    if row == 0:
        rmin = 0
    if row == len(lst) - 1:
        rmax = 0
    if col == 0:
        cmin = 0
    if col == len(lst[row]) - 1:
        cmax = 0
    for r in range(rmin+row,rmax+1+row,1):
        for c in range(cmin+col,cmax+1+col,1):
            if str(r) + ',' + str(c) in symdict:
                adjsym = True
    return adjsym

#first, make a dictionary of the locations of symbols
symdict = {}
for row in range(len(lst)-1):
    col = 0
    while col < len(lst[row]):
        if (not lst[row][col].isdigit()) and lst[row][col] != '.':
            symdict[str(row) + ',' + str(col)] = lst[row][col]
        col += 1
numlist = []       
for row in range(len(lst)):
    col = 0
    numstr = ''
    innum = False
    symadj = False
    while col < len(lst[row]):
        if lst[row][col].isdigit():
            innum = True
            numstr += lst[row][col]
            if adjsym(row,col):
                symadj = True
        else:
            if innum:
                numlist.append([int(numstr), symadj])
                innum = False
                numstr = ''
                symadj = False
        if innum and col == len(lst[row]) - 1:
            numlist.append([int(numstr),symadj])
            numstr = ''
            innum = False
            symadj = False
        col += 1
        
total = 0
for item in numlist:
    if item[1]:
        total += item[0]
print(total)
            
            
            
            