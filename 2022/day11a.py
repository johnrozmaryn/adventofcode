f = open("day11.in")
contents = f.read()

monkdict = {}

monks = contents.split('\n\n')
for amonk in monks:
    s = amonk.split('\n')
    monknum = int(s[0][-2])   #'Monkey 0:'
    itlist = s[1][18:].split(',') #'  Starting items: 79, 98'
    for i in range(len(itlist)):
        itlist[i] = int(itlist[i])
    
    oplist = s[2][23:].split() # '  Operation: new = old * 19'
    
    tst = int(s[3][21:])         #'  Test: divisible by 23'
    
    tr = int(s[4][29:])         #'    If true: throw to monkey 2'
    fa = int(s[5][30:])         #'    If false: throw to monkey 3'
    
    monkdict[monknum] = {'itlist':itlist,'oplist':oplist,'tst':tst,'tr':tr,'fa':fa}

inspectlist = []
for i in range(len(monkdict)):
    inspectlist.append(0)

# def printitemlist():
#     for i in range(len(monkdict)):
#         print(monkdict[i]['itlist'])
#         print()

supermodulus = 1
for i in range(len(monkdict)):
    supermodulus *= monkdict[i]['tst']
       
for mround in range(10000):
    for i in monkdict.keys():
        amonk = monkdict[i]
        tr = amonk['tr']
        fa = amonk['fa']
        for item in amonk['itlist']:
            inspectlist[i] += 1
            op,num = amonk['oplist']
            if op == '+':
                item += int(num)
            if op == '*':
                if num.isnumeric():
                    item *= int(num)
                else:
                    item *= item
            
            if item % amonk['tst'] == 0:
                monkdict[tr]['itlist'].append(item % supermodulus)
            else:
                monkdict[fa]['itlist'].append(item % supermodulus)
            # printitemlist()
            # print('***')
        monkdict[i]['itlist'] = []
  
inspectlist.sort()
print(inspectlist[-1] * inspectlist[-2])
    
print(inspectlist)
    
    
           
            
            
   
    
    
    
    
    
    
    
    



        