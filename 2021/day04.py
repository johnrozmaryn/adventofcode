from copy import deepcopy
import sys

f = open("day04.in")
contents = (f.readlines())
#[l.strip() for l in contents]

def createhitlist(mylist):
    templist = deepcopy(mylist)
    for i in range(0,len(templist)):
        for j in range(0,len(templist[i])):
            for k in range(0,len(templist[i][j])):
                templist[i][j][k] = False
    return templist

def checkcardwin(cardnum):
    height = len(hitlist[cardnum])
    width = len(hitlist[cardnum][0])
    #first, check for wins in any row
    for i in range(0,height):
        rowwin = True
        for j in range(0,width):
            if hitlist[cardnum][i][j] == False:
                rowwin = False
        if rowwin:
            return True
    #next, check for wins in any column
    for j in range(0,width):
        colwin = True
        for i in range(0,height):
            if hitlist[cardnum][i][j] == False:
                colwin = False
        if colwin:
            return True
    return False
 
def markhits(bingonum):
    for i in range(0,len(cardlist)):
        for j in range(0,len(cardlist[i])):
            for k in range(0,len(cardlist[i][j])):  
                if cardlist[i][j][k] == bingonum:
                    hitlist[i][j][k] = True
                    
def listprint(listtoprint):
    for i in range(len(listtoprint))  :
        print((listtoprint[i]))                  

def sumuncalled(card):
    total = 0
    for i in range(0,len(cardlist[card])):
        for j in range(0,len(cardlist[card][i])):  
            if hitlist[card][i][j] == False:
                total += int(cardlist[card][i][j])
    return total

bingostr = contents[0].strip()
bingostrlist = bingostr.split(',')
bingolist = []
for l in bingostrlist:
    bingolist.append(l)

cardlist = []
tempcard = []
for n in range(2,len(contents)):
    if contents[n] == '\n':
        cardlist.append(tempcard)
        tempcard = []
    else:
        tempstr = contents[n].strip()  
        tempcard.append(tempstr.split())  
cardlist.append(tempcard)

hitlist = createhitlist(cardlist)

for n in range(0,len(bingolist)):
    bingonum = bingolist[n]
    markhits(bingonum)
    for card in range(len(cardlist)):
        cardwins =  checkcardwin(card)
        if cardwins:
            print(sumuncalled(card) * int(bingonum))
            sys.exit(0)
