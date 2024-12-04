f = open("day03.in")
contents = (f.readlines())
ms = ""
for l in contents:
    ms += l
    
tot = 0
i = 0

while i < len(ms):
    badcommand = False
    lstr = ""
    rstr = ""
    while not badcommand:
        if ms[i] != 'm':
            badcommand = True
            i += 1
        else:
            i += 1
            if ms[i] != 'u':
                badcommand = True
                i += 1
            else:
                i += 1
                if ms[i] != 'l':
                    badcommand = True
                    i += 1
                else:
                    i += 1
                    if ms[i] != "(":
                        badcommand = True
                        i += 1
                    else:
                        i+=1
                        if not ms[i].isdigit():
                            badcommand = True
                            i += 1
                        else:
                            while ms[i].isdigit():
                                lstr += ms[i]
                                i += 1
                            if ms[i] != ',':
                                badcommand = True
                                i+=1
                            else:
                                i += 1
                                if not ms[i].isdigit():
                                    badcommand = True
                                    i += 1
                                else:
                                    while ms[i].isdigit():
                                        rstr += ms[i]
                                        i+=1
                                    if ms[i] != ')':
                                        badcommand = True
                                        i += 1
                                    else:
                                        tot += int(lstr) * int(rstr)
                                        lstr = ''
                                        rstr = ''
                                        i += 1

print(tot)        
            
        

    

    
