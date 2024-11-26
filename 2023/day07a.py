f = open("day07.in")
contents = (f.readlines())

cards = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9, \
         'T':10,'J':1,'Q':12,'K':13,'A':14}


hands = {}

for l in contents:  
    hands[(l.split()[0])] = int(l.split()[1])
    
def rank(hand):
    j = hand.count('J')
    matches = []
    for c in range(len(hand)):
        card = hand[c]
        if card != 'J':
            matches.append(hand.count(card))    
    if j == 0:
        if matches.count(5) > 0:
            return '5ok'
        elif matches.count(4) > 0:
            return '4ok'
        elif matches.count(3) > 0:
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
    elif j >= 4:
        return '5ok'
    elif j == 3:
        if max(matches) == 2:
            return '5ok'
        else:
            return '4ok'
    elif j == 2:
        if max(matches) == 3:
            return '5ok'
        elif max(matches) == 2:
            return '4ok'
        else:
            return '3ok'
    elif j == 1:
        if max(matches) == 4:
            return '5ok'
        elif max(matches) == 3:
            return '4ok'
        elif max(matches) == 2:
            if matches.count(2) > 2:
                return 'fh'
            else:
                return '3ok'
        else:
            return 'pair'

    
def quant(hand):
    q = []
    for c in range(len(hand)):
        q.append(cards[hand[c]])
    return q

def unquant(hand):
    h = ''
    for c in hand:
        if c == 1:
            h += 'J'
        elif c < 10 :
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