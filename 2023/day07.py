f = open("day07.in")
contents = (f.readlines())

order = {'nothing':0,'pair':1,'2pair':2,'3ok':3}
cards = {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9, \
         'T':10,'J':11,'Q':12,'K':13,'A':14}


hands = {}

for l in contents:  
    hands[(l.split()[0])] = int(l.split()[1])
    
def rank(hand):       #returns order
    matches = []
    for c in range(len(hand)):
        card = hand[c]
        matches.append(hand.count(card))
    if matches.count(5) > 0:
        return '5ok'
    if matches.count(4) > 0:
        return '4ok'
    if matches.count(3) > 0:
        if matches.count(2) > 0:
            return 'fh'
        else:
            return '3ok'
    elif matches.count(2) > 3:
        return '2pair'
    elif matches.count(2) > 1:
        return 'pair'
    else:
        return 'nothing'
    
def quant(hand):
    q = []
    for c in range(len(hand)):
        q.append(cards[hand[c]])
    return q

def unquant(hand):
    h = ''
    for c in hand:
        if c < 10 :
            h += str(c)
        elif c == 10:
            h += 'T'
        elif c == 11:
            h += 'J'
        elif c == 12:
            h += 'Q'
        elif c == 13:
            h += 'K'
        elif c == 14:
            h += 'A'
    return h

five = []
four = []    
fh = []
three = []
twopair = []
pair = []
none = []


biglist = []

for h in hands:
    q = quant(h)
    r = rank(h)
    if r == '5ok':
        five.append(q)
    elif r == '4ok':
        four.append(q)
    elif r == 'fh':
        fh.append(q)
    elif r == '3ok':
        three.append(q)
    elif r == '2pair':
        twopair.append(q)
    elif r == 'pair':
        pair.append(q)
    else:
        none.append(q)
five.sort()
four.sort()
fh.sort()        
three.sort()
twopair.sort()
pair.sort()
none.sort()

biglist = none + pair + twopair + three + fh + four + five
 

total = 0

for h in range(len(biglist)):
    total += (h+1) * hands[unquant(biglist[h])]

print(total)