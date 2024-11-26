# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 07:30:17 2024

@author: jrozmaryn
"""
import os
alph = 'abcdefghijklmnopqrstuvwxyz'
for a in alph:
    for b in alph:
        for c in alph:
            dirname = '.\\struct\\' + a + '\\' + b + '\\' + c
            os.makedirs(dirname, exist_ok= True)
            
            # for d in alph:
            #     for e in alph:
            #         print(a,b,c,d,e)
                    