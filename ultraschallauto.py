from tkinter import *
from PIL import Image, ImageTk
import time


class Ultraschallauto():
    def __init__(self, root):
        super().__init__(master = None)
        

    def draw(self):
    
        root = Tk()
        root.title("Distanzmesser")
        root.resizable(width=False, height=False)
        cvs = Canvas(bg='white', width = 1400, height = 300)
        cvs.pack()
        global carpic, Ultraschallauto
        carpic = PhotoImage(file="D:\\GitHub\\Ultraschallauto\\car.png")
        car = cvs.create_image(500, 160, image=carpic, anchor=NW)
        wand = cvs.create_rectangle(0, 0, 50, 320, fill="grey")
        #--
        global ok
        ok = cvs.bind("<1>", lambda event: cvs.move(car, -2,0))
        
        
        
        
        

#----------------------------------

Ultraschallauto.draw(1)

