# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 20:24:30 2019

@author: ASUS
"""

import csv

#Jawaban No. 1
def bukaModeListCsv():
    with open('Book1.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print(row[0], row[1], row[2])

#Jawaban No. 2            
def bukaModeDictCsv():
    with open('Book1.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            print(row['npm'], row['nama'], row['kelas'])

def tulisCsv():
    with open('Book4.csv', mode='w') as csv_file:
        fieldnames = ['npm', 'nama', 'kelas', 'tanggal lahir']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
        writer.writeheader()
        writer.writerow({'npm': '1174017', 'nama': 'Muh. Rifky Prananda', 'kelas': 'D4TI2C', 'tanggal lahir': '12/03/1999'})
        writer.writerow({'npm': '1174017', 'nama': 'Nita', 'kelas': 'D4TI2B', 'tanggal lahir': '13/04/1999'})