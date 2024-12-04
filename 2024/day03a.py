import re
f = open("day03.in")
contents = (f.readlines())
ms = ""
for l in contents:
    ms += l
    
#mulstr = r"mul\(\d+,\d+\)"
cmdstr = r"mul\(\d+,\d+\)|do\(\)|don\'t\(\)"
cmdlst = re.findall(cmdstr,ms)
tot = 0
mult = True
for cmd in cmdlst:
    if cmd == 'do()':
        mult = True
    elif cmd == 'don\'t()':
        mult = False
    else:
        if mult:
            pair = cmd.strip('mul(').strip(')').split(',')
            tot += int(pair[0]) * int(pair[1])
    
print(tot)





        

            
            
        
    
    
        
    

 
