from tkinter import *
import time


class Ultraschallauto:
    def __init__(self, auto, wand, abstand):
        super().__init__()
        self.auto = auto
        self.wand = wand
        self.abstand = abstand

#----------------------------------

main = Tk()
main.title("hi")
main.geometry("800x500")
main.mainloop()


