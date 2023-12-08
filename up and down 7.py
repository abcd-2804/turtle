# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 23:51:47 2023

@author: ayushi 
"""


import random
n_s = 1000000
w = 0
l = 0
for i in range (n_s):
    die_1= random . randint(1,6)
    die_2= random . randint(1,6)
    n= die_1 + die_2
    if n <= 7:
        w=w+ 1
    else:
        l=l + 1
total = w * 1 + l *(-1)
print (total /n_s)
       
       