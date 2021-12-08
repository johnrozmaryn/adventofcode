#from copy import deepcopy
import sys
import time

f = open("day08.in")
contents = (f.readlines())
inputlist = []
for l in contents:
    tlist = l.strip().split(' ')
    tlist.remove('|')
    inputlist.append(tlist)

dd= {}
dd['abcefg'] = '0'
dd['cf'] = '1'
dd['acdeg'] = '2'
dd['acdfg'] = '3'
dd['bcdf'] = '4'
dd['abdfg'] = '5'
dd['abdefg'] = '6'
dd['acf'] = '7'
dd['abcdefg'] = '8'
dd['abcdfg'] = '9'
        
def solve(line):
    tlist = line[0:10]
    codelist = []
    for i in tlist:
        codelist.append([])
    for i in range(0,len(codelist)):
        for c in tlist[i]:
            codelist[i].append(c)
        codelist[i].sort()
    #codelist is a nested list with all of the individual codes, sorted
    codelist.sort(key=len)
    uk = []  #sets of unknown values. Starts as the codelists in set form, will modified later
    for i in codelist:
        uk.append(set(i))
    
    transdict = {}
    #A is the difference between the length 3 string and the lenght 2 string
    aset = (uk[1] - uk[0])
    transdict['a'] = aset.pop()
    #F is in the union of 6,7,8, but onnot 3,4,5 
    fset =(uk[6] & uk[7] & uk[8]) - (uk[3] & uk[4] & uk[5]) & uk[1]
    transdict['f'] = fset.pop()
    #C is  the length 3 string - values for A and F
    cset = uk[1] - set([transdict['a'],transdict['f']])
    transdict['c'] = cset.pop()
    #b
    bset = uk[2] - (uk[3] & uk[4] & uk[5]) - uk[1]
    transdict['b'] = bset.pop()

    #clean up a bit
    for i in uk:
        i.discard(transdict['a'])
        i.discard(transdict['f'])
        i.discard(transdict['c'])
        i.discard(transdict['b'])
    transdict['d'] = uk[2].pop()
    for i in uk:
        i.discard(transdict['d'])
    transdict['g'] = (uk[3] & uk[4] & uk[5]).pop()
    for i in uk:
        i.discard(transdict['g'])
    transdict['e'] = (uk[6] | uk[7] | uk[8]).pop()
    reversetransdict = {}
    for left, right in transdict.items():
        reversetransdict[right] = left
    
    return reversetransdict

sum = 0

for i in inputlist:
    numstr = ''
    transdict = solve(i)
    incode = i[-4:]
    outstr = ''
    for c in incode:
        clist = []
        for l in c:
            clist.append(transdict[l])
        outstr += dd["".join(sorted(clist))]
    sum += int(outstr)
    
print(sum)


"""
uk = [{'c', 'f'},
            {'a', 'c', 'f'},
            {'b', 'c', 'd', 'f'},
            {'a', 'b', 'd', 'f', 'g'},
            {'a', 'c', 'd', 'e', 'g'},
            {'a', 'c', 'd', 'f', 'g'},
            {'a', 'b', 'c', 'd', 'f', 'g'},
            {'a', 'b', 'c', 'e', 'f', 'g'},
            {'a', 'b', 'd', 'e', 'f', 'g'},
            {'a', 'b', 'c', 'd', 'e', 'f', 'g'}]



"""
    