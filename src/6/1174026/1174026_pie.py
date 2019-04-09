from matplotlib import pyplot as plt

def pie():

    hasil = 1174026 % 3 + 2
    
    potong = [7,4,2,12]
    kegiatan = ['Kencan','Game','Makan','Belajar']
    kolom = ['c','r','y','m']
    
    for i in range(1, hasil+1):
        plt.subplot(2,2,i)
        plt.pie(potong,
        labels=kegiatan,
        colors=kolom,
        startangle=90,
        shadow= True,
        explode=(0.3,0,0,0),
        autopct='%1.1f%%')         
        plt.title('Kegiatan Sehari-hari')
        plt.subplots_adjust(hspace=.4)
    
    plt.show()
    