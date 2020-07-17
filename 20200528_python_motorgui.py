
from Tkinter import *

from PIL import Image, ImageTk
import math
import time
import struct
#import matplotlib.pyplot as pltr
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from functools import partial # libreria para poder pasar argumentos (variable) a una funcion con un boton
import cv2

#comunicacion serial 
import serial





root = Tk() #Crear ventana

root.wm_title("INTERFAZ PLC IOT     HKM INDUSTRIES.") #Titulo en top
#root.attributes("-zoomed", True) # pantalla completa
root.geometry("1300x500") # set starting size of window
root.maxsize(1300, 500) # width x height
root.config(bg="lightgrey")
#root.config(background = "#FFFFFF") #fondo blanco





in1 = IntVar() # permite guardar el valor del textbox
in2 = IntVar()
in3 = IntVar() # permite guardar el valor del textbox
in4 = IntVar()



#frame 0 -  botones manual- read menu principal

frame_0 = Frame(root, width=200, height = 50)

frame_0.grid(row=7, column=1, padx=20, pady=3)

 

#frame 1 - puerto 1- botones

frame_1 = Frame(root, width=400, height = 1200)

frame_1.grid(row=0, column=0, padx=10, pady=2)

#frame2 - - puerto 2 - botones
frame_2 = Frame(root, width=400, height = 600)
frame_2.grid(row=1, column=0, padx=10, pady=2) 



#frame3 frame con los indicadores del puerto 1

frame_3 = Frame(root, width=200, height = 600)

frame_3.grid(row=0, column=1, padx=10, pady=2)

#frame4  frame con los indicadores del puerto 2
frame_4 = Frame(root, width=200, height = 300)

frame_4.grid(row=1, column=1, padx=10, pady=2)

 


#Canvas circulo 1

circleCanvas = Canvas(frame_3, width=50, height=50, bg='white')

circleCanvas.grid(row=1, column=0, padx=10, pady=2)
circleCanvas.create_oval(10, 10, 40, 40, width=0, fill='red')

#Canvas circulo 2

circleCanvas2 = Canvas(frame_4, width=50, height=50, bg='white')

circleCanvas2.grid(row=1, column=0, padx=10, pady=2)
circleCanvas2.create_oval(10, 10, 40, 40, width=0, fill='red')




#Logging LED on/off status

LEDLog = Text(frame_3, width = 10, height = 5, takefocus=0)

LEDLog.grid(row=3, column=0, padx=10, pady=2)

LEDLog2 = Text(frame_4, width = 10, height = 5, takefocus=0)

LEDLog2.grid(row=3, column=0, padx=10, pady=2)
 

#Labels

motor1_Label = Label(frame_1, text="MOTOR 1")

motor1_Label.grid(row=0, column=0, padx=10, pady=2)



motor2_Label = Label(frame_2, text="MOTOR 2")

motor2_Label.grid(row=6, column=0, padx=10, pady=2)

 

secondLabel = Label(frame_3, text="Historial del puerto")

secondLabel.grid(row=2, column=0, padx=10, pady=2)

 

thirdLabel = Label(frame_3, text= "DIGITAL OUT 1")

thirdLabel.grid(row=0, column=0, padx=10, pady=2)

def grnCircle(num):

    if (num == 1):
     circleCanvas.create_oval(10, 10, 40, 40, width=0, fill='green')
     LEDLog.insert(0.0, "Derecha\n")
    if (num == 2):
     circleCanvas.create_oval(10, 10, 40, 40, width=0, fill='green')
     LEDLog.insert(0.0, "Derecha\n")
    if (num == 3):
     circleCanvas.create_oval(10, 10, 40, 40, width=0, fill='white')
     LEDLog.insert(0.0, "Parar\n")

def redCircle(num):

   if (num == 1):
    circleCanvas.create_oval(10, 10, 40, 40, width=0, fill='red')
    LEDLog.insert(0.0, "Izquierda\n")
   if (num == 2):
     circleCanvas.create_oval(10, 10, 40, 40, width=0, fill='red')
     LEDLog.insert(0.0, "Izquierda\n")

   if (num == 3):
     circleCanvas.create_oval(10, 10, 40, 40, width=0, fill='white')
     LEDLog.insert(0.0, "Parar\n")

def circuloblanco(num):

   if (num == 1):
      circleCanvas.create_oval(10, 10, 40, 40, width=0, fill='white')
      LEDLog.insert(0.0, "Parar\n")
   if (num == 2):
     circleCanvas.create_oval(10, 10, 40, 40, width=0, fill='white')
     LEDLog.insert(0.0, "Parar\n")   
   
   if (num == 3):
     circleCanvas.create_oval(10, 10, 40, 40, width=0, fill='white')
     LEDLog.insert(0.0, "Parar\n")

def calculo():

    #circleCanvas.create_oval(20, 20, 80, 80, width=0, fill='red')
    c= in1.get() # permite obtener el valor de in1
  
    d= in2.get() # permite obtener el valor de ind
   
    labelc = Label(frame_maq, text= c)
    labelc.grid(row=0, column=2, padx=10, pady=2)
     
    labeld = Label(frame_maq, text= d)
    labeld.grid(row=1, column=2, padx=10, pady=2)
  
    labelcd = Label(frame_maq, text= c*d)
    labelcd.grid(row=2, column=1, padx=10, pady=2)

def calculo_acom():

   
    esp_prod= in3.get() # permite obtener el valor de in1
  
    esp_entre_tubos= in4.get() # permite obtener el valor de ind
   
    producto_por_metro = math.floor(1/(esp_prod*0.0254)) # math.floor sirve para redondear hacia abajo ( los productos deben ser enteros)
    tubos_por_metro =    math.floor( 1/(esp_entre_tubos*0.0254))


    labelesp_prod = Label(frame_acom, text= esp_prod)
    labelesp_prod.grid(row=0, column=2, padx=10, pady=2)
     
    labeld = Label(frame_acom, text= tubos_por_metro)
    labeld.grid(row=1, column=2, padx=10, pady=2)
  
    labelprod_metro = Label(frame_acom, text= producto_por_metro)  # imprimir resultado
    labelprod_metro.grid(row=2, column=1, padx=10, pady=2)
     
    labeltubo_metro = Label(frame_acom, text= tubos_por_metro) # imprimir resultado
    labeltubo_metro.grid(row=3, column=1, padx=10, pady=2)

    






def serial_1(num):
 ser = serial.Serial('/dev/ttyUSB0',9600)  # open serial port
    
 if (num == 1 ):
   ser.write(str(1).encode())
   time.sleep(0.1)
 if (num == 2 ):
   ser.write(str(2).encode())
   time.sleep(0.1)
 if (num == 3 ):
   ser.write(str(3).encode())
   time.sleep(0.1)
 

#Turning LED on

def Izquierda(num):

    print(num)   
    redCircle(num)
    serial_1(num)

#Turning LED off

def Derecha(num):
    print(num)
    grnCircle(num)
    serial_1(num)
   
def parar(num):
    print(num)
    circuloblanco(num)
    serial_1(num)
    