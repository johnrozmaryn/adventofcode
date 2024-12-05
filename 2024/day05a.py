f = open("day05.in")
contents = (f.readlines())

r= []  #rules
p= []  #pages
badbooks = []

first = True
for l in contents:
    if l.strip() == "":
        first = False
    elif first:
       r.append(l.strip().strip('()').split('|'))
    else:
        p.append(l.strip().split(','))
             
tot = 0
for book in p:
    goodbook = True
    for rule in r:
        if (rule[0] in book) and (rule[1] in book):
            if book.index(rule[0]) > book.index(rule[1]):
                goodbook = False
    if not goodbook:
        badbooks.append(book)
        
allpages = []
for rule in r:
    if rule[0] not in allpages:
        allpages.append(rule[0])
    if rule[1] not in allpages:
        allpages.append(rule[1])

def rulesforpage(page):
    tmp = []
    for rule in r:
        if rule[0] == page:
            tmp.append(rule[1])
    return tmp

fixedbooks = []

for book in badbooks:
    fixedbook = []
    for page in book:
        if len(fixedbook) == 0:
            fixedbook.append(page)
        else:
            pos = []
            for rule in rulesforpage(page):
                if rule in fixedbook:
                    pos.append(fixedbook.index(rule))
            if len(pos) == 0:
                fixedbook.append(page)
            else:
                fixedbook.insert(min(pos),page)
    fixedbooks.append(fixedbook)

tot = 0
for book in fixedbooks:
    tot += int(book[len(book)//2])
print(tot)

        
        
       
    

