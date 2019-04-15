# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 17:03:15 2019

@author: Tomy
"""
#Teori
#Pemahaman Teori
#Jawaban No. 1
def namaFungsi(inputanFungsi):
    return inputanFungsi

output = namaFungsi("Kembalian Fungsi")
print(output)

#Jawaban No. 2
import math
print("Nilai pi adalah: ", math.pi)

#Jawaban No. 3
class Mahasiswa:
    jumlahMahasiswa = 0
    
    def _init_(self, npm, nama):
        self.npm = npm
        self.nama = nama
        Mahasiswa.jumlahMahasiswa +=1
            
    def tampilkanProfil(self):
        print("NPM :", self.npm)
        print("Nama :", self.nama)
        print()

mahasiswa1 = Mahasiswa("1174031", "Muhammad Tomy")
mahasiswa2 = Mahasiswa("1174077", "Bujang")

mahasiswa1.tampilkanProfil()
mahasiswa2.tampilkanProfil()

print("Total mahasiswa adalah ", Mahasiswa.jumlahMahasiswa)

#Jawaban No. 4
from Mahasiswa import Mahasiswa

mhs1 = Mahasiswa("1174012", "Muhammad Tomy")
mhs2 = Mahasiswa("1174077", "Bujang")

mhs1.tampilkanProfil()
mhs2.tampilkanProfil()

print("Total mahasiswa adalah ", Mahasiswa.jumlahMahasiswa)

#Jawaban No. 5
from kalkulator import Penambahan

hasil = Penambahan(10, 5)
print(hasil)

#Jawaban No. 6
from folder import kalkulator

a=50
b=25

hasil1=kalkulator.Penambahan(a,b)
hasil2=kalkulator.Pengurangan(a,b)
hasil3=kalkulator.Perkalian(a,b)
hasil4=kalkulator.Pembagian(a,b)

print(hasil1)
print(hasil2)
print(hasil3)
print(hasil4)

#Jawaban No. 7
from folder.Mahasiswa import Mahasiswa

mhs1 = Mahasiswa("1174012", "Muhammad Tomy")
mhs2 = Mahasiswa("1174077", "Bujang")

mhs1.tampilkanProfil()
mhs2.tampilkanProfil()

print("Total mahasiswa adalah ", Mahasiswa.jumlahMahasiswa)
#Ketrampilan Pemrograman
#No.1
def jwbNo1():
    
    npm = input("Masukan NPM :")
    npm = list(str(npm))

    angka1 = {"0":" ###### ", "1":"  ##", "2":" #######  ", "3":"  #######  ", "4":"   #####", "5":"#######", "6":" #######", "7":"#######", "8":" ##### ", "9":" ######  "}
    angka2 = {"0":"###  ###", "1":"####", "2":"##    ### ", "3":"###     ###", "4":"  ##  ##", "5":"##     ", "6":"###     ", "7":"#######", "8":"##   ##", "9":"##    ## "}
    angka3 = {"0":"###  ###", "1":" ###", "2":"     ###  ", "3":"      #### ", "4":" ##   ##", "5":"##     ", "6":"###     ", "7":"   ### ", "8":" ##### ", "9":"##    ## "}
    angka4 = {"0":"###  ###", "1":" ###", "2":"    ###   ", "3":"      #### ", "4":"########", "5":"###### ", "6":"########", "7":"  ###  ", "8":"#######", "9":"######## "}
    angka5 = {"0":"###  ###", "1":" ###", "2":"  ####    ", "3":"###     ###", "4":"      ##", "5":"     ##", "6":"###  ###", "7":" ###   ", "8":"##   ##", "9":"      ## "}
    angka6 = {"0":" ###### ", "1":" ###", "2":"######### ", "3":"  #######  ", "4":"      ##", "5":"###### ", "6":" ###### ", "7":"###    ", "8":" ##### ", "9":"#######  "}
          
    hasil1 = []
    hasil2 = []
    hasil3 = []
    hasil4 = []
    hasil5 = []
    hasil6 = []

    for x in npm:
        hasil1.append(angka1[x])
        hasil2.append(angka2[x])
        hasil3.append(angka3[x])
        hasil4.append(angka4[x])
        hasil5.append(angka5[x])
        hasil6.append(angka6[x])
    
    print(*hasil1, sep=' ')
    print(*hasil2, sep=' ')
    print(*hasil3, sep=' ')
    print(*hasil4, sep=' ')
    print(*hasil5, sep=' ')
    print(*hasil6, sep=' ')

jwbNo1()

#no.2
def jwbNo2(npm):
    hitung = 0
    while(hitung <12):
        print("Halo, " + str(npm) + " Apa Kabar?")
        hitung = hitung +1
jwbNo2(int(input("Masukkan NPM: ")))

#no.3
def jwbNo3(npm):
    hitung = 0
    npm = str(npm)
    x = npm[4:7]
    while(hitung < 3):
        print("Halo, " + x + " Apa Kabar?")
        hitung = hitung +1
jwbNo3(int(input("Masukkan NPM: ")))

#no.4
def jwbNo4(npm):
    npm = str(npm)
    x = npm[-3]
    print("Halo, " + x + " Apa Kabar?")
jwbNo4(int(input("Masukkan NPM: ")))

#no5
def jwbNo5(npm):
    for i in npm:
        print (i)
    
jwbNo5(input("Masukkan NPM: "))

#no.6
def jwbNo6(npm):
    jumlah = 0
    for i in npm:
        jumlah += int(i)
    print ("Hasil Penjumlahan NPM adalah : " +str(jumlah))
jwbNo6(input("Masukkan NPM: "))

#No.7
def jwbNo7(npm):
    kalikan = 0
    for i in npm:
        kalikan *= int(i)
    print ("Hasil Perkalian NPM adalah : " +str(kalikan))
jwbNo7(input("Masukkan NPM: "))

#N0.8
def jwbNo8(npm):
    npm = list(map(int, npm))
    for n in npm:
        if(n % 2 == 0):
            if(n != 0):
                print(n, end ="")
jwbNo8(input("Masukkan NPM: "))

#No.9
def jwbNo9(npm):
    npm = list(map(int, npm))
    for n in npm:
        if(n % 2 !=0):
            print(n, end ="")
jwbNo9(input("Masukkan NPM: "))

#No.10
def jwbNo10(npm):
    npm = list(map(int, npm))
    prima = []
    for n in npm:
        bilPrima = True
        if n == 0 or n ==1:
            bilPrima = False
        for x in range(2, n):
            if n % x == 0:
                bilPrima = False
        if bilPrima:
            prima.append(n)
                
        for p in prima:
            print(p, end = "")
jwbNo10(input("Masukkan NPM: "))


