from tkinter import *
from tkinter import filedialog
import tkinter
from app import main

class Ap:
    def __init__(self):
        self.path = ""


window = tkinter.Tk()
ap = Ap()

window.geometry("500x300")
window.title("Descarga de archivo")

def selectRoute():
  
    global path
    global route
    window.route = filedialog.askopenfilename(title='Select Route')
    print(window.route)
    Button(window, text = "Ejecutar",height="2", width="30", command=lambda:main(window.route)).pack()     
    ap.path = window.route


Label(text="Eliga el archivo, y presiona ejecutar", bg="lightgreen", width="300", height="2", font=("Calibri", 13)).pack()
Label(text="").pack()

Button(window, text="Selecciona la ruta",height="2", width="30", command=selectRoute).pack()

Label(text="").pack()


window.mainloop()
