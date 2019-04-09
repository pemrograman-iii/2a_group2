
from matplotlib import pyplot as plt

def scatterfahmi():
	
	hasil = 1174021 % 3 + 2
	
	x = [-1,-1.-5,-2,-2.-5,-3,-3.-5,-3.-6]
	y = [7.5,8,8.5,9,9.5,10,10.5]
 
	x1=[-8,-8.-5,-9,-9.-5,-10,-10.-5,-11]
	y1=[3,3.5,3.7,4,4.5,5,5.2]

	for i in range(1, hasil+1):
		plt.subplot(2,2,i)
		plt.scatter(x,y, label='bilangan negatif',color='r')
		plt.scatter(x1,y1,label='bilangan positif',color='c')
		plt.xlabel('bilangan positif')
		plt.ylabel('bilangan negatif')
		plt.title('Scatter Plot')
		plt.legend()
		plt.subplots_adjust()
	
	plt.show()
    
scatterfahmi()