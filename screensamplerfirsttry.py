# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 17:45:23 2022

@author: Matty
"""


from mss import mss
import mss.tools
from colorthief import ColorThief
from PIL import Image
import io


#with mss() as sct:
   # for firstscreenshot in sct.save():
     #   print(firstscreenshot)

with mss.mss() as sct:
    
    Topbar=[]
    Bottombar=[]
    Leftbar=[]
    Rightbar=[]
    x=0
    
    for i in range(16):
        
        #TOP BAR
        # Defining the dimensions of the screen capture, and actually screenshotting it.
        monitor = {"top": 0, "left": 0+x, "width": 160, "height": 160}
        output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)
        quadrant=sct.grab(monitor)
        mss.tools.to_png(quadrant.rgb, quadrant.size, output=output)
        
        #Using color theif to sample the dominant colour then add it to an array
        quadrantcolor=ColorThief("sct-{top}x{left}_{width}x{height}.png".format(**monitor))
        quadrantDominant=quadrantcolor.get_color(quality=1)
        Topbar.append(quadrantDominant)
        print(Topbar)
        
        #BOTTOM BAR
        # Defining the dimensions of the screen capture, and actually screenshotting it.
        monitor = {"top": 1280, "left": 0+x, "width": 160, "height": 160}
        output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)
        quadrant=sct.grab(monitor)
        mss.tools.to_png(quadrant.rgb, quadrant.size, output=output)
        
        #Using color theif to sample the dominant colour then add it to an array
        quadrantcolor=ColorThief("sct-{top}x{left}_{width}x{height}.png".format(**monitor))
        quadrantDominant=quadrantcolor.get_color(quality=1)
        Bottombar.append(quadrantDominant)
        print(Bottombar)
    
        x=x+160
       
    y=0
    
    for i in range(7):
        
        #LEFT BAR
        # Defining the dimensions of the screen capture, and actually screenshotting it.
        monitor = {"top": 160+y, "left": 0, "width": 160, "height": 160}
        output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)
        quadrant=sct.grab(monitor)
        mss.tools.to_png(quadrant.rgb, quadrant.size, output=output)
        
        #Using color theif to sample the dominant colour then add it to an array
        
        quadrantcolor=ColorThief("sct-{top}x{left}_{width}x{height}.png".format(**monitor))
        quadrantDominant=quadrantcolor.get_color(quality=1)
        Leftbar.append(quadrantDominant)
        print(Leftbar)
        
        #RIGHT BAR
        # Defining the dimensions of the screen capture, and actually screenshotting it.
        monitor = {"top": 160+y, "left": 2400, "width": 160, "height": 160}
        output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)
        quadrant=sct.grab(monitor)
        mss.tools.to_png(quadrant.rgb, quadrant.size, output=output)
        
        #Using color theif to sample the dominant colour then add it to an array
        
        quadrantcolor=ColorThief("sct-{top}x{left}_{width}x{height}.png".format(**monitor))
        quadrantDominant=quadrantcolor.get_color(quality=1)
        Rightbar.append(quadrantDominant)
        print(Rightbar)
    
        y=y+160       
      
    print("Done!")

     
    
        # Grab the data
        #sct_img01 = sct.grab(monitor)
    
        # Save to the picture file
       # mss.tools.to_png(sct_img01.rgb, sct_img01.size, output=output)
        #print(output)
