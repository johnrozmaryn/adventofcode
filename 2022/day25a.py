f = open("day21.in")
contents = f.readlines()

monks = {}

for l in contents:
    monk,op = l.strip().split(':')
    monks[monk] = op.strip()
    
def yell(monk):
    if monks[monk].isnumeric():
        return int(monks[monk])
    else:
        lst = monks[monk].strip().split()
        if lst[1] == '+':
            return yell(lst[0]) + yell(lst[2])
        if lst[1] == '*':
            return yell(lst[0]) * yell(lst[2])
        if lst[1] == '/':
            return yell(lst[0]) / yell(lst[2])
        if lst[1] == '-':
            return yell(lst[0]) - yell(lst[2])


def y(i):
    monks['humn'] = str(int(i))
    return yell(m1)


#Need to do some kind of binary search here. I know the number I need is between
# 10^12 and 10^13. A binary search for that number wouldn't take long.

m1,op,m2 = monks['root'].split()
v2 = yell(m2)

maxwin = 10 ** 20
minwin = 10 ** 0

found = False

while not found:
    testval = minwin + (maxwin - minwin) // 2
    v1 = y(testval)
    print(testval, v1, v2)
    if v1 > v2:
        minwin = testval
    elif v1 < v2:
        maxwin = testval
    elif v1 == v2:
        found = True

print(testval)
    
    
    
    

    

    


    

