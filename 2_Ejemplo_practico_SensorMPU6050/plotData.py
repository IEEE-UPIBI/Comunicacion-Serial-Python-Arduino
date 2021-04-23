import serial
import matplotlib.pyplot as plt
import numpy as np
DataSize = 20
ax_np = []
ay_np = []
az_np = []
gx_np = []
gy_np = []
gz_np = []
with serial.Serial() as ser:
    ser.baudrate =  9600
    ser.port = 'COM5'
    ser.open()
    for j in range(0,DataSize):
        for i in range(0,6):
            data = ser.readline().decode('utf-8').strip()
            pos=data.index(":")
            label=data[:pos]
            value=data[pos+1:]
            if label == 'ax':
                ax_np.append(float(value))
                            
            elif label == 'ay':
                ay_np.append(float(value))
                
            elif label == 'az':
                az_np.append(float(value))
            
            elif label == 'gx':
                gx_np.append(float(value))
                            
            elif label == 'gy':
                gy_np.append(float(value))
                
            elif label == 'gz':
                gz_np.append(float(value))
                
    ser.close()

plt.plot(ax_np)
plt.plot(ay_np)
plt.plot(az_np)
plt.plot(gx_np)
plt.plot(gy_np)
plt.plot(gz_np)
plt.show()