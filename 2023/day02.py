f = open("day02.in")
contents = (f.readlines())

lst = []
for l in contents:
    lst.append(l.strip())

resultdict = {}    
for game in lst:
    gamenum = game.split(':')[0].split()[1]
    resultdict[gamenum] = {"maxtot":0,"blue":0,"red":0,"green":0}
    playlist = game.split(':')[1].split(';')
    for item in playlist:
        plays = item.split(',')
        playtotal = 0
        for play in plays:
            playstr = play.split()
            num = int(playstr[0])
            color = playstr[1]
            if resultdict[gamenum][color] < num:
                resultdict[gamenum][color] = num
            playtotal += num
        if resultdict[gamenum]["maxtot"] < playtotal:
            resultdict[gamenum]["maxtot"] = playtotal
            
            
gameids = 0
redmax = 12
greenmax = 13
bluemax = 14
totmax = redmax+greenmax+bluemax

for game in resultdict:
    if (resultdict[game]["red"] <= redmax) and (resultdict[game]["green"] <= greenmax) and (resultdict[game]["blue"] <= bluemax):
        gameids += int(game)
        
print(gameids)
        
        
    
            
            
            
            
        
        
        
    
    

        