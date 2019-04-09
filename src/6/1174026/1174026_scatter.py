from matplotlib import pyplot as plt

def scatter():

    hasil = 117426 % 3 + 2
    
    x = [1,1.5,2,2.5,3,3.5,3.6]
    y = [5.5,6,8.5,7,7.5,6,6.5]
     
    x1=[6,6.5,8,8.5,9,9.5,10]
    y1=[3,3.5,3.7,4,4.5,5,5.2]
    
    for i in range(1, hasil+1):
        plt.subplot(2,2,i)
        plt.scatter(x,y, label='Yang mabuk',color='y')
        plt.scatter(x1,y1,label='yang waras',color='b')
        plt.xlabel('simpanan dalam ratusan')
        plt.ylabel('pendapatan dalam ribuan')
        plt.title('Scatter Plot')
        plt.legend()
        plt.subplots_adjust(wspace=1.1, hspace=.7)
    
    plt.show()
    