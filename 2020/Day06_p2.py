# -*- coding: utf-8 -*-

f=open("Day06.data")
formdata = f.read()

formsplit = formdata.split('\n\n')

def evalform(frm):
    firstitem = True
    frm = frm.split()
    for i in list(frm):
        if firstitem == True:
            fint = set(list(i))
            firstitem = False
        else:
            fint = fint.intersection(set(list(i)))
    return len(fint)

frmtotal = 0

for frm in formsplit:
    frmtotal += evalform(frm)
    
print(frmtotal)
    
    

