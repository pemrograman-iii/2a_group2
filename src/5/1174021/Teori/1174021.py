import serial 

def bacaaja():
    ser = serial.Serial("COM5", 115200)
    print(ser.name)  

bacaaja()