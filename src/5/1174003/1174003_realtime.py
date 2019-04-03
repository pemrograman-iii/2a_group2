# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 19:07:14 2019

@author: asus
"""

import serial

def ulang():
    ser = serial.Serial('COM6',9600)
    while(1):
        print(ser.readline().decode("utf-8").strip('\n').strip('\r'))

ulang()