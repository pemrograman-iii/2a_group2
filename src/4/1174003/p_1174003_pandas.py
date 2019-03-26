# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 18:56:35 2019

@author: asus
"""

import pandas
#no3
df = pandas.read_csv('1174003.csv')
print(df)

#no4
df = pandas.read_csv('1174003.csv')
uji = pandas.DataFrame.from_dict(df)
print(uji)

#no5
df = pandas.read_csv('1174003.csv', parse_dates=['Hire Date'])
print(df)

#no6
df = pandas.read_csv('1174003.csv', index_col='Name')
print(df)

#no7
df = pandas.read_csv('1174003.csv',
        header=0, 
        names=['Nama', 'Tgl Masuk','Gaji', 'Jatah Sakit'])
print(df)

def bacalistpandas():
    df = pandas.read_csv('1174003.csv')
    print(df)

def write():
    df = pandas.read_csv('1174003.csv', 
            index_col='Employee', 
            parse_dates=['Hired'],
            header=0, 
            names=['Employee', 'Hired', 'Salary', 'Sick Days'])
    df.to_csv('d1174003_pandas_baru.csv')