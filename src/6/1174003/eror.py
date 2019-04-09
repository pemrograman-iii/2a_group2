# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 18:08:21 2019

@author: Dwi
"""

def tryExceptError():
    try:
        from d1174003_scat import batang as bar
    except SyntaxError:
        print("Nah Loh Eror")

tryExceptError()