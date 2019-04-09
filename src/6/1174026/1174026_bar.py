from matplotlib import pyplot as plt

def bar():

    hasil = 1174026 % 3 + 2
    
    for i in range(1, hasil+1):
        plt.subplot(2,2,i)
        plt.bar([2009.7,2010.7,2011.7,2012.7,2013.7,2014.7],[9000,9500,10000,15000,20000,25000],
        label="OPPO",color='y',width=.3)
        plt.bar([2010,2011,2012,2013,2014,2015],[20000,25000,30000,35000,40000,45000],
        label="VIVO",color='c',width=.3)
        plt.bar([2010.3,2011.3,2012.3,2013.3,2014.3,2015.3],[2000,2500,3000,3500,4000,4500],
        label="SAMSUNG",color='g',width=.3)
        plt.legend()
        plt.xlabel('Tahun')
        plt.ylabel('Jumlah Pengguna')
        plt.title('Pengguna HP')
        plt.subplots_adjust(wspace=1, hspace=.7)
        
    plt.show()
    