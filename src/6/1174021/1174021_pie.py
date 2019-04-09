
import matplotlib.pyplot as plt

def piefahmi():

	hasil = 1174021 % 3 + 2
 
	hari = [1,2,3,4,5]
 
	tidur =[7,8,6,11,7]
	makan = [2,3,4,3,7]
	kuliah =[7,8,7,2,4]
	jalan_jalan = [8,5,7,8,13]
	potong = [7,2,2,12]
	kegiatan = ['Tidur','Makan','Kuliah','Online']
	kolom = ['k','m','y','c']
 
	for i in range(1, hasil+1):
		plt.subplot(2,2,i)
		plt.pie(potong,
		labels=kegiatan,
		colors=kolom,
		startangle=90,
		shadow= True,
		explode=(0,0,0.2,0),
		autopct='%1.1f%%')
		plt.title('Kegiatan saya sehari-hari')
		plt.subplots_adjust()
		
	plt.show()
	
piefahmi()
