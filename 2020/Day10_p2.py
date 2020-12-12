
f=open("Day10.data")
contents = (f.readlines())
data=list(map(int, contents))

data.append(0)
data.append(max(data)+3)

data.sort()

gaps = []
for i in range (1,len(data)):
    gaps.append(data[i]-data[i-1])

ones = 0
twos = 0
threes = 0
fours = 0


strgaps = ''
for i in gaps:
    strgaps += str(i)

print(strgaps)
ones = strgaps.count('1')
twos = strgaps.count('11')
threes = strgaps.count('111')
fours = strgaps.count('1111')


twos = twos - (threes + fours)
threes = threes - fours

print(twos,threes,fours)

                             
print((2**twos) * (4**(threes)) * (7**(fours)))



    


            

        

        
        
    