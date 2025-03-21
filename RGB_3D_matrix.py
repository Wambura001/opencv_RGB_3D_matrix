# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 12:00:55 2025

@author: USER
"""

import cv2 
import matplotlib.pyplot as plt 
import numpy as np 

# Create a 2x2 RGB image 
rgb_image = np.array([[[255, 0, 0], [0, 255, 50], [42, 90, 243]], #First row
                       [[0, 255, 50], [42, 90, 243], [255, 0, 0]], #second row
                       [ [42, 90, 243], [255, 0, 0], [0, 255, 50]]], dtype = np.uint8)

print(rgb_image)
plt.imshow(rgb_image)
plt.axis("Off")
plt.show()