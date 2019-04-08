# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 18:47:20 2019

@author: asus
"""

from matplotlib import pyplot as plt

x=[10,5,7]
y=[11,9,7]

#plt.plot(x,y)
#plt.show
#line

#plt.bar([3,5,7,9,11,15],[70,80,90,50,30],
#label="Lamborghini",color='Y',width=.5)
#plt.bar([4,6,8,10,12,14],[40,10,10,60,30],
#label="VW", color='K',width=.3)
#plt.legend()
#plt.xlabel('Days')
#plt.ylabel('Distance (kms)')
#plt.title('Information')
#plt.show()
#bar

#population_age = [50,10,51,20,7,9,40,15,22,55,62,45,21,22,102,95,85,55,110,120,70,80,75,65,54,39,32,41,46,44]
#bins = [0,10,20,30,40,50,60,70,80,90,100]
#plt.hist(population_age, bins, histtype='bar', rwidth=0.8)
#plt.xlabel('age groups')
#plt.ylabel('Number of people')
#plt.title('Histogram')
#plt.show()
#histogram

#x = [5,2,4,6,7,7,6]
#y = [10,8,8.5,9,15.5,10,11.5]
 
#x1=[8,8.5,9,9.5,10,10.5,11]
#y1=[3,3.5,3.7,4,4.5,5,5.2]
 
#plt.scatter(x,y, label='Pendapatan Tinggi Tapi Penyimpanan Rendah',color='K')
#plt.scatter(x1,y1,label='Pendapatan Rendah Tapi Penyimpanan Tinggi',color='B')
#plt.xlabel('Pensimpanan dalam ratusan')
#plt.ylabel('Pendapatan dalam ribuan')
#plt.title('Diagram Titik')
#plt.legend()
#plt.show()
#scatter

#Bulan = [1,2,3,4,5,6,7]
  
#bahasa_inggris =[7,8,6,8,7,9,10]
#Matematika = [2,3,4,3,2,3,4]
#Kimia =[7,8,7,2,2,6,0]
#Fisika = [8,5,7,8,13,15,25]
  
#plt.plot([],[],color='B', label='Bahasa_Inggris', linewidth=6)
#plt.plot([],[],color='K', label='Matematika', linewidth=6)
#plt.plot([],[],color='M', label='Kimia', linewidth=6)
#plt.plot([],[],color='C', label='Fisika', linewidth=6)
  
#plt.stackplot(Bulan, Bahasa_Inggris','Matematika','Kimia','Fisika colors=['B','K','M','C'])
  
#plt.xlabel('bulan')
#plt.ylabel('Berapa Lama')
#plt.title('Stack Plot')
#plt.legend()
#plt.show()
#stack plot

Bulan = [1,2,3,4,5,6,7]
 
Bahasa_Inggris =[10,11,15,34,12,16,21]
Matematika = [15,10,22,20,16,19,28]
Kimia =[11,13,15,18,16,14,12]
Fisika = [9,10,14,11,15,12,10]
slices = [7,2,2,13]
activities = ['Bahasa_Inggris','Matematika','Kimia','Fisika']
cols = ['B','Y','M','C']
 
plt.pie(slices,
  labels=activities,
  colors=cols,
  startangle=90,
  shadow= True,
  explode=(0,0,0,0),
  autopct='%1.2f%%')
 
plt.title('Plot')
plt.show()
#diagram Pie

#x = [1,2,3,4,5,6,7,8,9,10]
#y = [10,20,30,40,50,60,70,80,90,100]
#plt.subplot(248)#tinggi,lebar,urutan
#plt.plot(x, y)
#plt.subplot(249)
#plt.bar(x, y)
#plt.subplot(251)
#plt.hist(x, y)
#plt.subplot(250)
#plt.scatter(x, y)
#plt.show()
#subplot