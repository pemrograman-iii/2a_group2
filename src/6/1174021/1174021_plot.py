
from matplotlib import pyplot as plt

def plotfahmi():

	hasil = 1174021 % 3 + 2

	x = [2014,2015,2016,2017,2018,2019]
	y = [100,200,300,400,500,1000]
	x2 = [2014,2015,2016,2017,2018,2019]
	y2 = [100,250,310,390,450,850]

	for i in range(1, hasil+1):
		plt.plot(x,y,'b',label='Persija', linewidth=1)
		plt.plot(x2,y2,'r',label='Persib',linewidth=1)
		plt.title('Pendukung team sepak bola')
		plt.ylabel('Jumlah Pendukung')
		plt.xlabel('Tahun')
		plt.legend()
		plt.grid(True,color='k')
		plt.subplots_adjust()
	
	plt.show()
	
plotfahmi()
