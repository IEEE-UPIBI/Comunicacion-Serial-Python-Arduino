import serial
import time
import collections
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import  FigureCanvasTkAgg
from threading import Thread
from tkinter import Tk, Frame, StringVar, Label, Button, Entry
import utils

### FUNCTIONS ####
def getData(arduino):
    """ Recive Data from Arduino, This code will run in a SubThread"""
    time.sleep(2)                 # Give time to establish conection
    #arduino.reset_input_buffer() # Reset Buffer (In order to recive clean Data)


    while isRun:                                   # While isRune (Global Variable is True)
        global isReceiving                         # Set isRecevving to Global (for assigment)
        global value                               # Set value to Global (for assigment)

        #value = float(arduino.readline().strip())  # Get Value

        raw = arduino.readline()   # Read Value
        cad   = raw.decode()    # Decode to Ascii
        cad   = cad.strip()       # Remove \n and \r
        position = cad.index(":") # Get the index of lable/status separation
        label  = cad[:position]   # Get label
        status = float(cad[position+1:]) # Get Status
        
        if label  =="ECG":
            value = status



        isReceiving = True                         # Set is Rrecing to True 

def Begin():
    anim = animation.FuncAnimation(fig,plotData,fargs=(samples,lines),interval=sampleTime) # Animate Canvas
    plt.show()


def askQuit():
    """ Quit Protocol, this prevents pyton from crashing """
    global isRun                         # Reference Global Variable
    isRun = False                        # Set isRun to Flase (This stops GetData's while loop)
    thread.join()                        # Join Subtrhead (used for receving Data)
    arduino.write(('0\n').encode())      # Send a closing statement to arduino
    arduino.close()                      # Close connection
    root.quit()                          # Quit Tk
    root.destroy()                       # Destroy Tk

def plotData(self,Samples,lines):
    """ Function to Append data and plot in Tk """
    global value                         # Reference Global Variable
    data.append(value)                   # Append Value to data
    lines.set_data(range(Samples),data)  # plot Data


#### END OF FUCNTIONS ###

## Arduino Connetion  ##
arduino = utils.arduino_communication()  # Establish Communication with arduino 


samples = 100
data  = collections.deque([0]*samples,maxlen=samples)
data2  = collections.deque([0]*samples,maxlen=samples)
sampleTime = 100
xmin,xmax = (0,samples)
ymin,ymax = (0,280)
isReceiving = False
isRun = True
value = 0.0



if __name__ == "__main__":
    thread = Thread(target=getData,args=(arduino,))          # Create Thread for Communication with arduino
    thread.start()                                           # Start Thread 

    fig = plt.figure(facecolor='0.94')                       # Creat figure
    plt.title("ECG SIMULATOR")                                         # Add title to figure
    ax  = plt.axes(xlim=(xmin,xmax),ylim=(ymin,ymax))        # Create an axis    
    ax.set_xlabel("Tiempo")                                  # Xlabel
    ax.set_ylabel("Bits")                                    # Ylabel
    lines = ax.plot([],[],label="ECG")[0]                                # Create line (for ploting)
    ax.legend()

    ## GUI ##
    root = Tk()                                # Create Tk Object
    root.protocol("WM_DELETE_WINDOW",askQuit)  # Add exit portocol
    root.geometry("800x500")                 # Configure aspect ratio
    root.title("  \t\t\t\t ECG GUI")           # Add title 
    root.resizable(0,0)                        # Does not Enbale resize figure


    ### PLOTTING DATA ###
    canvas = FigureCanvasTkAgg(fig,master=root)                  # Create a canvas object with predermined fig
    canvas._tkcanvas.grid(row=0,column = 0, padx = 1,pady = 1)   # Set  canvas at specific position
    
    frame = Frame(root, width = 130,height = 200, bg = "#7003FC")
    frame.grid(row = 0,column = 1, padx = 1,pady = 2)
    frame.grid_propagate(False)
    frame.config(relief = "sunken")
    frame.config(cursor="circle")
   
    Begin = Button(frame,command= Begin, text= "Begin ",bg="blue",fg="white", font="Helvetica 14 bold",justify="center")
    Begin.pack
    Begin.grid(row=1,column=0, padx=30,pady=30) 
   
    
    Exit = Button(frame,command= askQuit, text= "Exit ",bg="red",fg="white", font="Helvetica 14 bold",justify="center")
    Exit.pack
    Exit.grid(row=2,column=0, padx=1,pady=5) 
    
    
    
    root.mainloop()