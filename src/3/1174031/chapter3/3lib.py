# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 19:15:04 2019

@author: Tomy
"""
#Ketrampilan Pemrograman
#No.1
def jwbNo1(npm):
    
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

#no.2
def jwbNo2(npm):
    hitung = 0
    while(hitung <12):
        print("Halo, " + str(npm) + " Apa Kabar?")
        hitung = hitung +1
#no.3
def jwbNo3(npm):
    hitung = 0
    npm = str(npm)
    x = npm[4:7]
    while(hitung < 3):
        print("Halo, " + x + " Apa Kabar?")
        hitung = hitung +1

#no.4
def jwbNo4(npm):
    npm = str(npm)
    x = npm[-3]
    print("Halo, " + x + " Apa Kabar?")

#no5
def jwbNo5(npm):
    for i in npm:
        print (i)

#no.6
def jwbNo6(npm):
    jumlah = 0
    for i in npm:
        jumlah += int(i)
    print ("Hasil Penjumlahan NPM adalah : " +str(jumlah))
#No.7
def jwbNo7(npm):
    kalikan = 0
    for i in npm:
        kalikan *= int(i)
    print ("Hasil Perkalian NPM adalah : " +str(kalikan))

#N0.8
def jwbNo8(npm):
    npm = list(map(int, npm))
    for n in npm:
        if(n % 2 == 0):
            if(n != 0):
                print(n, end ="")

#No.9
def jwbNo9(npm):
    npm = list(map(int, npm))
    for n in npm:
        if(n % 2 !=0):
            print(n, end ="")

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


