# In[1]: Jawaban Soal No. 2
from matplotlib import pyplot as plt
 
x=[1,3,5]
y=[4,6,8]

plt.plot(x,y)

plt.show()

# In[2]: Bar Graph

from matplotlib import pyplot as plt

plt.bar([2013.7,2014.7,2015.7,2016.7,2017.7,2018.7],[3.20,3.20,3.40,3.30,3.20,3.40],
label="Dika",color='b',width=.3)
plt.bar([2013,2014,2015,2016,2017,2018],[3.25,3.15,3.70,3.30,3.25,3.45],
label="Joko",color='r',width=.3)
plt.bar([2013.3,2014.3,2015.3,2016.3,2017.3,2018.3],[3.15,3.20,3.35,3.50,3.30,3.50],
label="Dodi",color='g',width=.3)
plt.legend()
plt.xlabel('Tahun')
plt.ylabel('IP')
plt.title('Nilai IP Kelas 2A')
plt.show()

# In[3]: Histogram

import matplotlib.pyplot as plt
orang = [17.,18,19,20,21,22,23]
umur = [0,10,20,30]
plt.hist(orang, umur, histtype='bar', rwidth=0.8)
plt.xlabel('Umur')
plt.ylabel('Jumlah Orang')
plt.title('Umur mahasiswa kelas 2A')
plt.show()

# In[4]: Scatter Plot

import matplotlib.pyplot as plt
x = [-1,-1.-5,-2,-2.-5,-3,-3.-5,-3.-6]
y = [7.5,8,8.5,9,9.5,10,10.5]
 
x1=[-8,-8.-5,-9,-9.-5,-10,-10.-5,-11]
y1=[3,3.5,3.7,4,4.5,5,5.2]
 
plt.scatter(x,y, label='bilangan negatif',color='r')
plt.scatter(x1,y1,label='bilangan positif',color='c')
plt.xlabel('bilangan positif')
plt.ylabel('bilangan negatif')
plt.title('Scatter Plot')
plt.legend()
plt.show()

# In[5]: Area plot

import matplotlib.pyplot as plt
hari = [1,2,3,4,5]
  
tidur =[7,8,6,11,7]
makan = [2,3,4,3,4]
kuliah =[7,8,7,2,5]
jalan_jalan = [8,5,7,8,13]
  
plt.plot([],[],color='k', label='Tidur', linewidth=5)
plt.plot([],[],color='m', label='Makan', linewidth=5)
plt.plot([],[],color='y', label='Kuliah', linewidth=5)
plt.plot([],[],color='c', label='Online', linewidth=5)
  
plt.stackplot(hari,tidur,makan,kuliah,jalan_jalan, colors=['k','m','y','c'])
  
plt.xlabel('x')
plt.ylabel('y')
plt.title('Kegiatan saya sehari-hari')
plt.legend()
plt.show()

# In[6]: Pie Plot

import matplotlib.pyplot as plt
 
hari = [1,2,3,4,5]
 
tidur =[7,8,6,11,7]
makan = [2,3,4,3,7]
kuliah =[7,8,7,2,4]
jalan_jalan = [8,5,7,8,13]
potong = [7,2,2,12]
kegiatan = ['Tidur','Makan','Kuliah','Online']
kolom = ['k','m','y','c']
 
plt.pie(potong,
  labels=kegiatan,
  colors=kolom,
  startangle=90,
  shadow= True,
  explode=(0,0,0.2,0),
  autopct='%1.1f%%')
 
plt.title('Kegiatan saya sehari-hari')
plt.show()

# In[7]: Line Graph

from matplotlib import pyplot as plt
 
y = [4000,6000,8000,15000,20000,30000]
x = [2014,2015,2016,2017,2018,2019]
plt.plot(x,y)
plt.title('Harga Coklat')
plt.ylabel('Tahun')
plt.xlabel('Harga Coklat')
plt.show()

# In[8]: Jawaban Soal No. 4

from matplotlib import pyplot as plt

x = [2014,2015,2016,2017,2018,2019]
y = [100,200,300,400,500,1000]
x2 = [2014,2015,2016,2017,2018,2019]
y2 = [100,250,310,390,450,850]
plt.plot(x,y,'b',label='Persija', linewidth=1)
plt.plot(x2,y2,'r',label='Persib',linewidth=1)
plt.title('Pendukung team sepak bola')
plt.ylabel('Jumlah Pendukung')
plt.xlabel('Tahun')
plt.legend()
plt.grid(True,color='k')
plt.show()

# In[8]: Jawaban Soal No. 5

import numpy as np
import matplotlib.pyplot as plt
 
t = np.arange(0.0, 9.0, 1)
s = [1,2,3,4,5,6,7,8,9]
 
for i in range(1, 10):
    plt.subplot(3,3,i)
    plt.xticks([]), plt.yticks([])
    plt.title('subplot(1,2,'+str(i)+')')
    plt.plot(t,s,'-y')
 
plt.show()

# In[5]: Jawaban Soal No. 7

import matplotlib.pyplot as plt
orang = [17.,18,19,20,21,22,23]
umur = [0,10,20,30]
plt.hist(orang, umur, histtype='bar', rwidth=0.8)
plt.xlabel('Umur')
plt.ylabel('Jumlah Orang')
plt.title('Umur mahasiswa kelas 2A')
plt.show()