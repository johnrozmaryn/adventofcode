f = open("day25.in")
contents = f.readlines()

mp = {'2':2,'1':1,'0':0,'-':-1,'=':-2}

numlist = []

for l in contents:
    a = list(l.strip())
    a.reverse()
    numlist.append(a)


def stoint(lst):
    tot = 0
    for i in range(len(lst)):
        tot += mp[lst[i]] * (5 ** i)
    return tot

def intos(dec):
    if dec == 0:
        return ''
    q, r = divmod(dec + 2, 5)
    return intos(q) + '=-012'[r]
    


listtot = 0

for l in numlist:
    listtot += stoint(l)
    
print(intos(listtot))
    


    

