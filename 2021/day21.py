
p1  = 5
p2 =  10

tp1 = 0
tp2 = 0

rolls = list(range(1,101))
rollcounter = 0

while True:
    for _ in range(3):
        p1 += rolls[(rollcounter % 100)]
        rollcounter += 1
    p1 = ((p1-1) % 10) + 1
    tp1 += p1
    if tp1 >= 1000:
        print(tp2*rollcounter)
        print("tp2=",tp2," counter=",rollcounter)
        break
    for _ in range(3):
        p2 += rolls[(rollcounter % 100)]
        rollcounter += 1
    p2 = ((p2-1) % 10) + 1
    tp2 += p2
    if tp2 >= 1000:
        print(tp1*rollcounter)
        print("tp1=",tp1," counter=",rollcounter)
        break

    


        
     
