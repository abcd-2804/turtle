# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 13:10:11 2023

@author: 91626
"""

import random
w=0
l=0
n_s = 1000000
for i in range (n_s):
    die_1= random.randint(1,6)
    die_2= random.randint(1,6)
    check = die_1+die_2
    if check<=7:
        w=w+1
    else:
        l=l+1
Total = w*1+l*(-1)
print(Total/n_s)
 