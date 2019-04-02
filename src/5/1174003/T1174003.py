# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 20:19:53 2019

@author: asus
"""

import serial

def baca():
    ser = serial.Serial("COM6",115200)
    baca = ser.readline()
    print(baca)

baca()