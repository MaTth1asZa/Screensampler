# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 12:44:22 2022

@author: Matty
"""

from mss import mss
import mss.tools
#from colorthief import ColorThief
import numpy as np
with mss.mss() as sct:
    from typing import Callable, List


def get_screengrab() -> np.ndarray:
def get_quadrant() -> list[np.array]:
def get_dominant_colours(quadrants: list[np.array]) -> list[np.array]:
def rasp_pi(dominant_colours: list[np.array]) ->    int #possibly ints per colour channel? To be decided


    
    Topbar=[]
    Bottombar=[]
    Leftbar=[]
    Rightbar=[]
    x=0
     
    for i in range(16):
        monitor = {"top": 0, "left": 0+x, "width": 160, "height": 160}
        #output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)
        quadrant=np.array(sct.grab(monitor))
   
        print(quadrant.shape)
        
        x=x+160










       # quadrantcolor=ColorThief('quadrant.rgb')
        #quadrantDominant=quadrantcolor.get_color(quality=1)
       # Topbar.append(quadrantDominant)
       # print(Topbar)
      #  x=x+160