f = open("day20.in")
contents = f.readlines()

lst = []
st = set()

for l in contents:
    lst.append(int(l.strip()))
    st.add(int(l.strip()))

print(len(lst), len(st))    
        



    


    
    

