f = open("day03.in")
contents = (f.readlines())

lst = []
for l in contents:
    lst.append(l.strip())

def adjsym(row,col,numstr):
    tmplst = []
    adjsym = False
    rmin = -1 
    if col-len(numstr) < 0 : 
        cmin = -len(numstr)
    else:
        cmin = -1 -len(numstr)
    rmax = 1 
    cmax = 1
    if row == 0:
        rmin = 0
    if row == len(lst) - 1:
        rmax = 0

    if col == len(lst[row]) - 1:
        cmax = 0
        
    for r in range(rmin+row,rmax+row+1):
        for c in range(cmin+col,cmax+col):
            if str(r) + ',' + str(c) in symdict:
                adjsym = True
                tmplst.append(str(r) + ',' + str(c))
    if adjsym:
        for item in tmplst:
            symdict[item].append(numstr)
    return adjsym

#first, make a dictionary of the locations of stars
symdict = {}
for row in range(len(lst)-1):
    col = 0
    while col < len(lst[row]):
        if lst[row][col] == '*':
            symdict[str(row) + ',' + str(col)] = []
        col += 1

numlist = []       
for row in range(len(lst)):
    col = 0
    numstr = ''
    innum = False

    while col < len(lst[row]):
        if lst[row][col].isdigit():
            innum = True
            numstr += lst[row][col]
        else:
            if innum:
                adjsym(row,col,numstr)
                innum = False
                numstr = ''
        if innum and col == len(lst[row]) - 1:
            adjsym(row,col,numstr)
            innum = False
            numstr = ''

        col += 1
  
total = 0
for item in symdict:
    if len(symdict[item]) == 2:
        total += int(symdict[item][0]) * int(symdict[item][1])
        
print(total)
            
            
            
            