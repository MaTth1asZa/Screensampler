# stdlib
from typing import List, Dict

# 3rd party
from mss import mss
import mss.tools
import numpy as np


WIDTH = 160
HEIGHT = 160

def grab(top: int, left: int, sct) -> np.array:
    with mss.mss() as sct:
        monitor = {"top": top, "left": left, "width": WIDTH, "height": HEIGHT}
        rgb_array = np.array(sct.grab(monitor))

    return rgb_array

def get_quadrant() -> Dict[str, List[np.array]]:
    with mss.mss() as sct:
        topbar = []
        x = 0
        for _ in range(16):  #top bar; _ means 'disregard this object', since you don't use i
            rgb_array = grab(top=0, left=0 + x, sct=sct)
            topbar.append(rgb_array)
            x = x + 160

        rightbar = []
        y = 0
        for _ in range(7):  # right bar
            rgb_array = grab(top=160 + y, left=2400, sct=sct)
            rightbar.append(rgb_array)
            y = y + 160
            
        bottombar = []
        x = 0
        for _ in range(16):  # bottom bar
            rgb_array = grab(top=1280 + y, left=0 + x, sct=sct)
            bottombar.append(rgb_array)
            x = x + 160
            
        leftbar = []
        y = 0   
        for _ in range(7):  # left bar
            rgb_array = grab(top=160 + y, left=0, sct=sct)
            leftbar.append(rgb_array)
            y=y+160

        return {
            'topbar': topbar,
            'rightbar': rightbar,
            'bottombar': bottombar,
            'leftbar': leftbar
        }

def get_dominant_colours(bars: Dict[str, List[np.array]]) -> List[np.array]:
    dominant_colours = {}

    for quadrant_name, regions in bars.items():
        region_means = []
        for region in regions:
            colour_average = region.mean(axis=(0,1)).astype(np.int32)
            region_means.append(colour_average)

        dominant_colours[quadrant_name] = region_means

    return dominant_colours


bars = get_quadrant()
dominant_colours = get_dominant_colours(bars=bars)
print(dominant_colours)