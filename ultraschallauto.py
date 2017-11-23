from tkinter import *
import time
import os



class Ultraschallauto():
    def __init__(self):
        super().__init__(master = None)
        

    def draw(self): #canvas design
        global carpic, car, cvs, move, wand
        root = Tk() 
        root.title("Distanzmesser") # Titel des Programmes
        root.resizable(width=False, height=False) # Fenstergröße nicht veränderbar
        cvs = Canvas(bg='white', width = 1400, height = 300) #Canvas Fläche
        cvs.pack()
        carpic = PhotoImage(file=abs_file_path) #Funktion zum Importieren des Bildes
        car = cvs.create_image(1000, 160, image=carpic, anchor=NW)# Importiert das Bild
        wand = cvs.create_rectangle(0, 0, 50, 320, fill="grey")# Importiert die Wand
        cvs.bind("<1>", lambda event: Ultraschallauto.fahren(1)) #Mausklick Event




    def fahren(self): # 
        global cvs, move, car, coords, wand
        cvs.move(car, -5,0) # verschiebt das Auto nach links
        coords = cvs.coords(car)
            
        if coords == [700.0, 160.0]: #verändert die Farbe der Wand in Green
            wand = cvs.create_rectangle(0, 0, 50, 320, fill="green")

        elif coords == [350.0, 160.0]:#verändert die Farbe der Wand in Gelb
            wand = cvs.create_rectangle(0, 0, 50, 320, fill="yellow")

        elif coords == [100.0, 160.0]:#verändert die Farbe der Wand in Rot
            wand = cvs.create_rectangle(0, 0, 50, 320, fill="red")
    
        elif coords <= [15.0, 160.0]:
            print("AUTO KOMPLETT ZERSTÖRT LO WO HAST DU FAHREN GELERNT MORRUK")
            print("NEUSTART in...")
            time.sleep(1)
            print("3...")
            time.sleep(1)
            print("2...")
            time.sleep(1)
            print("1...")
            time.sleep(1)
            cvs.coords(car, 1000,160)
            wand = cvs.create_rectangle(0, 0, 50, 320, fill="grey")        
        
        

#----------------------------------

script_dir = os.path.dirname(__file__)
rel_path = "car.png"
abs_file_path = os.path.join(script_dir, rel_path)
Ultraschallauto.draw(1)
