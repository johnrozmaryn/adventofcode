# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 09:06:51 2020

@author: jrozmaryn
"""
f=open("Day06.data")
formdata = f.read()

formdata.split('\n\n')
formsplit = formdata.split('\n\n')

def evalform(frm):
    questionset = set()
    for i in list(frm):
        questionset.add(i)
        questionset.discard('\n')
    return(len(questionset))

frmtotal = 0

for frm in formsplit:
    frmtotal += evalform(frm)
    
print(frmtotal)
    
    

