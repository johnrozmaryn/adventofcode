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

print(yell('root'))
    

