from tkinter import *
import time


class Ultraschallauto():
    def __init__(self):
        super().__init__(master = None)
        

    def draw(self):
        global carpic, car, cvs, move, wand
        root = Tk()
        root.title("Distanzmesser")
        root.resizable(width=False, height=False)
        cvs = Canvas(bg='white', width = 1400, height = 300)
        
        cvs.pack()
        
        carpic = PhotoImage(file="D:\\GitHub\\Ultraschallauto\\car.png")
        car = cvs.create_image(1000, 160, image=carpic, anchor=NW)
        
        wand = cvs.create_rectangle(0, 0, 50, 320, fill="grey")
        #--
        cvs.bind("<1>", lambda event: Ultraschallauto.drive(1))




    def drive(self):
        global cvs, move, car, coords
        cvs.move(car, -10,0)
        coords = cvs.coords(car)
        

        if coords <= [21.0, 160.0]:
            global wand
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
            
        elif coords == [700.0, 160.0]:
            wand = cvs.create_rectangle(0, 0, 50, 320, fill="green")

        elif coords == [350.0, 160.0]:
            wand = cvs.create_rectangle(0, 0, 50, 320, fill="yellow")

        elif coords == [100.0, 160.0]:
            wand = cvs.create_rectangle(0, 0, 50, 320, fill="red")
    
        
        
        

#----------------------------------

Ultraschallauto.draw(1)

