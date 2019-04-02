import serial

def baca():
    ser = serial.Serial("COM5",9600)
    ikeh = ser.readline()
    print(ikeh)
    
baca()