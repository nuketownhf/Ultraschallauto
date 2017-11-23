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
        
        im = Image.open("car.png")
        im.show()
        
        
        
        
        

#----------------------------------

Ultraschallauto.draw(1)

