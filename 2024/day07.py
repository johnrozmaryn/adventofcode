f = open("day07.in")
contents = (f.readlines())

probs = []
for line in contents:
    sol = int(line.split(':')[0])
    a = line.strip().split(': ')[1].split(' ')
    nums = []
    for num in a:
        nums.append(int(num))
    probs.append([sol,nums])
    
def getops(n):
  if n == 0:
    return [""]
  ops = []
  for op in getops(n - 1):
    ops.append(op + '+')
    ops.append(op + '*')
  return ops

def mathworks(sol,num,ops):
    stack = num[0]
    for i in range(len(ops)):
        if ops[i] == '+':
            stack = stack + num[i+1]
        elif ops[i] == '*':
            stack = stack * num[i+1]
    return sol == stack 

tot = 0

for prob in probs:
    print(probs.index(prob))
    sol = prob[0]
    nums = prob[1]
    ops = getops(len(nums)-1)
    possible = False
    for i in ops:
        if mathworks(sol,nums,i):
            possible = True
            break
    if possible:
        tot += sol
print(tot)     
        
    
       
    

