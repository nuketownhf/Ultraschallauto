from tkinter import *
import time
import os



class Ultraschallauto():
    def __init__(self, auto):
        self.auto = auto
        
        
    def draw(self): #canvas design
        global carpic, car, cvs, move, wand, root
        
        root = Tk() 
        root.title("Distanzmesser") # Titel des Programmes
        root.resizable(width=False, height=False) # Fenstergröße nicht veränderbar
        cvs = Canvas(bg='white', width = 1400, height = 300) #Canvas Fläche
        cvs.pack()
        Ultraschallauto.auto(1)
        wand = cvs.create_rectangle(0, 0, 50, 320, fill="grey")# Importiert die Wand
        cvs.bind("<1>", lambda event: Ultraschallauto.fahren(self, x1=1)) #Mausklick Event



    def auto(self):
        global carpic, car, autoabfrage, x1
        
        if abfrage == 1:
            carpic = PhotoImage(file=abs_file_path) #Funktion zum Importieren des Bildes
            car = cvs.create_image(1000, 160, image=carpic, anchor=NW)# Importiert das Bild
            
        elif abfrage == 2:
            carpic = PhotoImage(file=abs_file_path) #Funktion zum Importieren des Bildes
            car = cvs.create_image(1000, 162, image=carpic, anchor=NW)# Importiert das Bild
            x1 = 30.0
        elif abfrage == 3:
            carpic = PhotoImage(file=abs_file_path) #Funktion zum Importieren des Bildes
            car = cvs.create_image(1000, 115, image=carpic, anchor=NW)# Importiert das Bild
        else:
            print("error")
    
    def fahren(self, x1): # 
        global cvs, move, car, coords, wand
        cvs.move(car, -5,0) # verschiebt das Auto nach links
        coords = cvs.coords(car)
        car_collision = 0.0
        car_height = 0
        if abfrage == 1:
            car_collision = 20.0
            car_height = 160
        elif abfrage == 2:
            car_collision = 32.0
            car_height = 162
        elif abfrage == 3:
            car_collision = 20.0
            car_height = 115
        
        if coords == [700.0, car_height]: #verändert die Farbe der Wand in Green
            wand = cvs.create_rectangle(0, 0, 50, 320, fill="green")

        elif coords == [350.0, car_height]:#verändert die Farbe der Wand in Gelb
            wand = cvs.create_rectangle(0, 0, 50, 320, fill="yellow")

        elif coords == [100.0, car_height]:#verändert die Farbe der Wand in Rot
            wand = cvs.create_rectangle(0, 0, 50, 320, fill="red")
    
        elif coords <= [car_collision, 160.0]:
            print("Gute Fahrerskills nice nice")
            print("NEUSTART in...")
            time.sleep(1)
            print("3...")
            time.sleep(1)
            print("2...")
            time.sleep(1)
            print("1...")
            time.sleep(1)
            cvs.coords(car, 1000,car_height)
            wand = cvs.create_rectangle(0, 0, 50, 320, fill="grey")        
        
    def farbenwechsel(self):        
        return farbenwechsel()
#----------------------------------
autoabfrage = int(input("Welches Auto? (1 - 3) \n"))
abfrage = autoabfrage
if autoabfrage == 1:
    autoabfrage = "car.png"
elif autoabfrage == 2:
    autoabfrage = "car2.png"
elif autoabfrage == 3:
    autoabfrage = "car3.png"
    

script_dir = os.path.dirname(__file__)
rel_path = autoabfrage
abs_file_path = os.path.join(script_dir, rel_path)

Ultraschallauto.draw(1)
