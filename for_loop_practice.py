# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 20:07:56 2022

@author: heost
"""

import matplotlib.pyplot as plt
import numpy as np

def get_fibonacci(index):
    x = [0, 1]
    #    0, 1, 1, 2, 3, 5, 8, ...
    
    if index == 0:
        return 0

    for i in range(2, index):
        x1 = x[i-1]
        x2 = x[i-2]
        fibonacci = x1 + x2
        x.append(fibonacci)
    
    return x[-1]

# ==========================================
# Fibonacci Sequence



# ==========================================
# linear function plot

x_list = []
y_list = []

for x in range(1,100,1):
    x = x/10
    y = np.sqrt(x)
    
    
    x_list.append(x)
    y_list.append(y)

plt.plot(x_list, y_list)
plt.show()