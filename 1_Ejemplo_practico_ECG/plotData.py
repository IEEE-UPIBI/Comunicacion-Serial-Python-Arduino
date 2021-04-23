import serial
import matplotlib.pyplot as plt
import numpy as np
DataSize = 2
ECG_np = []
with serial.Serial() as ser:
    ser.baudrate =  9600
    ser.port = 'COM5'
    ser.open()
    for j in range(0,DataSize):
        for i in range(0,200):
            data = ser.readline().decode('utf-8').strip()
            pos=data.index(":")
            label=data[:pos]
            value=data[pos+1:]
            if label == 'ECG':
                ECG_np.append(float(value))
                
    ser.close()

plt.plot(ECG_np)
plt.show()