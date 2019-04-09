
from matplotlib import pyplot as plt

def tryExceptError():
    try:
        x=[1,3,5]
        y=[2,4,6]        
        plt.plot(x,y)        
        plt.show()        
    except SyntaxError:
        print("Kesalahan penulisan syntax")
    except NameError:
        print("Variable tersebut tidak ada")
    except TypeError:
        print("Tipe data salah")
    except:
        print("Terjadi sebuah kesalahan")
        
tryExceptError()