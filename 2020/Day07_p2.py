f=open("Day07.data")
contents = (f.read())
inputlist = contents.splitlines()
rulelist = []
globalset = set()

for rule in inputlist:
    splitrule = rule.split()
    parsedrule = []
    if len(splitrule) > 6:
        keycolor = splitrule[0] + splitrule[1]
        parsedrule.append(keycolor)
        index  = 4
        baglist = []
        while (index + 3) < len(splitrule):
            baglist.append([splitrule[index],splitrule[index+1]+splitrule[index+2]])
            index += 4
        parsedrule.append(baglist)
    rulelist.append(parsedrule)

def findindexbyname(bagtofind):
    for i in range(0,len(rulelist)):
        if rulelist[i][0] == bagtofind:
            return i
        

def numofbags(bagtofind):
    ruleindex = findindexbyname(bagtofind)
    if rulelist[ruleindex][1] == []:
        return 0
    else:
        total = 0
        for bag in rulelist[ruleindex][1]:
            total += int(bag[0]) * numofbags(bag[1]) + int(bag[0])
        return total
    
print(numofbags('shinygold'))

