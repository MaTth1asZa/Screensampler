# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 17:45:23 2022

@author: Matty
"""


from mss import mss
import mss.tools
print('hello world')
#with mss() as sct:
   # for firstscreenshot in sct.save():
     #   print(firstscreenshot)
        
with mss.mss() as sct:
    x=0
    for i in range(16):
        
        # The screen part to capture
        monitor = {"top": 0, "left": 0+x, "width": 160, "height": 160}
        output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)
        
        Topbar=[]
        Topbar.append(sct.grab(monitor))
        x=x+160
       
        print("This is the picture array", Topbar)
 

        # Save to the picture file
       # mss.tools.to_png(sct_img00.rgb, sct_img00.size, output=output)
        #print(output)
        
        #monitor = {"top": 0, "left": 161, "width": 160, "height": 160}
        #output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)
    
        # Grab the data
        #sct_img01 = sct.grab(monitor)
    
        # Save to the picture file
       # mss.tools.to_png(sct_img01.rgb, sct_img01.size, output=output)
        #print(output)
        