
f=open("Day10.data")
contents = (f.readlines())
data=list(map(int, contents))

data.append(0)
data.append(max(data)+3)

data.sort()

def goodlist(testlist):
    gaps = []
    for i in range(1, len(testlist)):
        gaps.append(data[i]-data[i-1])
    if max(gaps) <= 3:
        return True


gaps = []
for i in range (1,len(data)):
    gaps.append(data[i]-data[i-1])
    
print(gaps.count(1) * gaps.count(3))



    


            

        

        
        
    