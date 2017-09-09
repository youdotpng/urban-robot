# -*- coding: utf-8 -*-
"""
Created on Tue May 30 22:08:52 2017

@author: nicol
"""
from PIL import Image as Image
import numpy as np


try:
    original = Image.open(r"D:\Downloads\ch01.tif")
except:
    print("Unable to load Image")

print(original.size)
orig_data = np.asarray(original, dtype=np.uint)
print(orig_data.shape)