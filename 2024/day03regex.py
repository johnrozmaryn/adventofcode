import re
f = open("day03a.tst")
contents = (f.readlines())
ms = ""
for l in contents:
    ms += l
    
# oof, part 2 is going to make me do regex
#  https://docs.python.org/3/howto/regex.html

mulstr = r"mul\(\d+,\d+\)"
cmdlst = re.findall(mulstr,ms)
tot = 0
for cmd in cmdlst:
    pair = cmd.strip('mul(').strip(')').split(',')
    tot += int(pair[0]) * int(pair[1])
    
print(tot)
    
    








        

            
            
        
    
    
        
    

 
