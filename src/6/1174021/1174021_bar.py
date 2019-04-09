   
from matplotlib import pyplot as plt

def barfahmi():

	hasil = 1174021 % 3 + 2 

	for i in range(1, hasil+1):
		plt.subplot(2,2,i)
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
		plt.subplots_adjust()
	
	plt.show()
	
barfahmi()