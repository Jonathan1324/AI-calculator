import tkinter as tk
import os

root = tk.Tk()

root.geometry('300x500+600+150')
root.title('AI calculates')
root.attributes('-fullscreen', False)
root.minsize(200,400)

def open_adderAI_window():
        root.destroy()
        os.system("python scripts/adder.py")

def open_multiplierAI_window():
        root.destroy()
        os.system("python scripts/multiplier.py")

def open_dividerAI_window():
        root.destroy()
        os.system("python scripts/divider.py")

def open_subtractorAI_window():
        root.destroy()
        os.system("python scripts/subtractor.py")

def open_settings():
        root.destroy()
        os.system("python scripts/settings/settings.py")

btnM = tk.Button(root, text="Multiply", font=('Times',20), command=open_multiplierAI_window)
btnA = tk.Button(root, text="Add", font=('Times',20), command=open_adderAI_window)
btnD = tk.Button(root, text="Divide", font=('Times',20), command=open_dividerAI_window)
btnS = tk.Button(root, text="Subtract", font=('Times',20), command=open_subtractorAI_window)

label = tk.Label(root, text="", font=('Times',20))

Settingsbtn = tk.Button(root, text="Settings", font=('Times',20), command=open_settings)
QuitBtn = tk.Button(root, text="Quit", font=('Times',20), command=root.destroy)

image = tk.PhotoImage(file = 'Textures/Logo/Python.png')

root.iconphoto(False, image)

btnA.pack()
btnS.pack()
btnM.pack()
btnD.pack()
label.pack()
Settingsbtn.pack()
QuitBtn.pack()

root.mainloop()