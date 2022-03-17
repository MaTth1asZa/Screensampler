# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 17:45:23 2022

@author: Matty
"""

#This is my first git based python file
from mss import mss
print('hello world')
with mss() as sct:
    for firstscreenshot in sct.save():
        print(firstscreenshot)