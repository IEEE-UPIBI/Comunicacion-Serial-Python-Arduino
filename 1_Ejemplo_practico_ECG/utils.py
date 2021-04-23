import serial
import time





### FUNCTIONS ####
#### SERIAL COMMUNICATION ####
def arduino_communication(COM="COM5",BAUDRATE=9600,TIMEOUT=1):
    """ Initalizes connection with Arduino Board """
    try:
        arduino = serial.Serial(COM, BAUDRATE , timeout=TIMEOUT)
        time.sleep(2)
          
    except:
        print("Error de coneccion con el puerto")

    return arduino 



