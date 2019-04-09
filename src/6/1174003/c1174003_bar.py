# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 20:37:17 2019

@author: asus
"""

from matplotlib import pyplot as plt

print(1174003%3+2)

def balok():
    x = [9,10,11,12,13,14,15]
    y = [21,22,25,31,67,56,30]

    x1 = [4,7,9,3,6]
    y1 = [15,17,19,11,13]

    x2 = [30,40,50,60,70,80,90]
    y2 = [10,20,30,40,50,60,70]

    plt.subplot(221)
    plt.bar(x,y)
    plt.subplot(222)
    plt.bar(x1,y1)
    plt.subplot(223)
    plt.bar(x2,y2)
    plt.show()