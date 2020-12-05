# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 16:36:58 2020

@author: jrozmaryn
"""



class Passport:
# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)        
    def __init__(self,byr,iyr,eyr,hgt,hcl,ecl,pid,cid):
        self.byr=byr
        self.iyr=iyr
        self.eyr=eyr
        self.hgt=hgt
        self.hcl=hcl
        self.ecl=ecl
        self.pid=pid
        self.cid=cid
        
Passports = []  #my collection of passports        

f=open("Day04.data","r")
contents = f.readlines()

currentpassport = Passport('','','','','','','','')


for line in contents:
    stripline = line.strip()
    
    if stripline == '':
        Passports.append(currentpassport)
        currentpassport = Passport('','','','','','','','')
    else:
        splitline = stripline.split(' ')
        for item in splitline:
            s = item.split(':')
            setattr(currentpassport,s[0],s[1])

def Valid_byr(passin):
    if len(passin.byr) !=4 :
        return False
    if passin.byr.isnumeric() :
        byr = int(passin.byr)
        if (byr >= 1920) and (byr <= 2020):
            return True
    return False

def Valid_iyr(passin):
    if len(passin.iyr) !=4 :
        return False
    if passin.iyr.isnumeric() :
        iyr = int(passin.iyr)
        if (iyr >= 2010) and (iyr <= 2020):
            return True
    return False   

def Valid_eyr(passin):
    if len(passin.eyr) !=4 :
        return False
    if passin.eyr.isnumeric() :
        eyr = int(passin.eyr)
        if (eyr >= 2020) and (eyr <= 2030):
            return True
    return False       

def Valid_hgt(passin):
    if len(passin.hgt)> 2: #protecting against crappy data
        units = passin.hgt[-2:]
        if units == 'cm':
            if passin.hgt[:-2].isnumeric():
                hgt = int(passin.hgt[:-2])
                if (hgt >= 150) and (hgt <= 193):
                    return True
        if units == 'in':
            if passin.hgt[:-2].isnumeric():
                hgt = int(passin.hgt[:-2])
                if (hgt >= 59) and (hgt <= 76):
                    return True       
    return False
        
 
def Valid_hcl(passin):
    if len(passin.hcl) == 7:
        hcl = passin.hcl
        allowed = set("abcdef0123456789")
        if hcl[0] == '#':
            if set(hcl[-6:]) <= allowed:
                return True
    return False

def Valid_ecl(passin):
    if len(passin.ecl) == 3:
        ecl = passin.ecl
        if ecl in ('amb','blu','brn','gry','grn','hzl','oth'):
            return True
    return False

def Valid_pid(passin):
    if len(passin.pid) == 9:
        pid = passin.pid
        allowed = set("0123456789")
        if set(pid) <= allowed:
            return True
    return False

def Valid_cid(passin):
    return True



def ValidPassport(passin):
    if (Valid_byr(passin) and
        Valid_iyr(passin) and
        Valid_eyr(passin) and
        Valid_hgt(passin) and
        Valid_hcl(passin) and
        Valid_ecl(passin) and
        Valid_pid(passin) and
        Valid_cid(passin) ):

        return True
    else:
        return False
    
vp = 0            
for i in Passports:
    if ValidPassport(i):
        vp +=1
        
print(vp)