#f = open("day01a.tst")
# f = open("day01.tst")
f = open("day01.in")
contents = (f.readlines())

lst = []
for l in contents:
    lst.append(l.strip())

digdict = {'zero':0,
           'one':1,
           'two':2,
           'three':3,
           'four':4,
           'five':5,
           'six':6,
           'seven':7,
           'eight':8,
           'nine':9}

total = 0
for item in lst:
    ones = None
    tens = None
    i = 0
    refstr = ''
    while tens == None:
        if item[i].isdigit():
            tens = int(item[i]) * 10
        else:
            refstr += item[i]
            
        for ind in digdict:
            if ind in refstr:
                tens = digdict[ind] * 10
            
        i += 1
        
            
    i = len(item) - 1
    refstr = ''
    while ones == None:
        if item[i].isdigit():
            ones = int(item[i])
        else:
            refstr = item[i] + refstr
            
        for ind in digdict:
            if ind in refstr:
                ones = digdict[ind]
        i -= 1
        
    
    total += tens + ones
    
print(total)
            
            
