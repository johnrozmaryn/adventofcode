f = open("day01.in")
contents = (f.readlines())

lst = []
for l in contents:
    lst.append(l.strip())

total = 0


for item in lst:
    ones= None
    tens = None
    i = 0
    while tens == None:
        if item[i].isdigit():
            tens = 10 * int(item[i])
        i += 1
        
    i = len(item) - 1
    while ones == None:
        if item[i].isdigit():
            ones = int(item[i])
        i -= 1

    print(ones + tens)
    total += ones + tens
    
print(total)
        