# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 19:29:38 2019

@author: damara
"""

import pandas

def bacalistpandas():
    df = pandas.read_csv('1174012.csv')
    print(df)

def bacadictpandas():
    df = pandas.read_csv('1174012.csv')
    uji = pandas.DataFrame.from_dict(df)
    print(uji)
    
def standartanggal():
    df = pandas.read_csv('1174012.csv', parse_dates=['ttl'])
    print(df)

def changeindexcol():
    df = pandas.read_csv('1174012.csv', index_col='npm')
    print(df)

def renameatt():
    df = pandas.read_csv('1174012.csv',
        header=0, 
        names=['Nomor Induk Mahasiswa', 'Name','Class', 'Tanggal Lahir'])
    print(df)

def write():
    df = pandas.read_csv('1174012.csv')
    df.to_csv('p_1174012_pandas_baru.csv')