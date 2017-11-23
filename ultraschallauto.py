from tkinter import *
from PIL import Image, ImageTk
import time


class Ultraschallauto():
    def __init__(self, auto, wand, abstand):
        super().__init__(master = None)
        

    def draw(self):
    
        root = Tk()
        cvs = Canvas(bg='black', width = 900, height = 800)
        cvs.pack()
        global carpic
        carpic = PhotoImage(file="D:\\GitHub\\Ultraschallauto\\car.png")
        car = cvs.create_image(5, 5, image=carpic, anchor=NW)
        
        
        
        
        
        

#----------------------------------

Ultraschallauto.draw(1)

