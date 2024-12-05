f = open("day05.in")
contents = (f.readlines())

r= []  #rules
p= []  #pages

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
    if goodbook:
        tot += int(book[len(book)//2])

        
        
       
    

