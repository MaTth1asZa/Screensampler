# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 12:44:22 2022

@author: Matty
"""

from mss import mss
import mss.tools
#from colorthief import ColorThief
import numpy as np
from typing import Callable, List


height=160
width=160
channels=4

def get_screengrab() -> np.ndarray:
    dummy_array=np.random.randint(low=0, high=256, size=(height, width, channels))
    #print(dummy_array.ndim)
    #print(dummy_array.shape)
    return dummy_array
# with mss.mss() as sct:



def get_quadrant() -> list[np.array]:
    
    topbar=list()
    for i in range(16): #top bar
        x=0
        monitor = {"top": 0, "left": 0+x, "width": 160, "height": 160}   # to be addressed, need to rework the get_screengrab function to use this line, then call the function with get_screengrab(x=0) or something
        topbar.append(get_screengrab())
        x=x+160

    #print(topbar)

    # rightbar=list()    
    # for i in range(7):  #right bar
    #     y=0
    #     monitor = {"top": 160+y, "left": 2400, "width": 160, "height": 160}
    #     rightbar.append(get_screengrab())
    #     y=y+160
        
    # bottombar=list()    
    # for i in range(16): #bottom bar
    #     x=0
    #     monitor = {"top": 1280, "left": 0+x, "width": 160, "height": 160}
    #     bottombar.append(get_screengrab())
    #     x=x+160
        
    # leftbar=list()    
    # for i in range(7): #left bar
    #     y=0
    #     monitor = {"top": 160+y, "left": 0, "width": 160, "height": 160}
    #     leftbar.append(get_screengrab())
    #     y=y+160

    return topbar#, rightbar, bottombar, leftbar

      
def get_dominant_colours() -> list[np.array]:
    
    dominant_colours = list()
    get_quadrant()
    for quadrant in get_quadrant():
        colour_average = quadrant.mean(axis=(0,1)).astype(np.int32)
        dominant_colours.append(colour_average)
    print(dominant_colours)
        
get_dominant_colours()


# def rasp_pi(dominant_colours: list[np.array]) ->    int #possibly ints per colour channel? To be decided


    







