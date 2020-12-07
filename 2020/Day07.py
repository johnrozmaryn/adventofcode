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

def findholder(bagtofind):
    templist = []
    for r in rulelist:
        if len(r):
            for s in r[1]:
                if s[1] == bagtofind:
                    templist.append(r[0])
    if templist != []:
        for thing in templist:
            globalset.add(thing)
            findholder(thing)
            
    
    return templist

findholder('shinygold')   
print(len(globalset))
