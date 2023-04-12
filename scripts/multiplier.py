import tkinter as tk
from AI.AI_simple_calculator import AImultiplier

root = tk.Tk()
e = tk.Entry(root, font=('Times',20))
e2 = tk.Entry(root, font=('Times',20))
e3 = tk.Entry(root, font=('Times',20))
    
def set_text(text):
    e2.delete(0,tk.END)
    e2.insert(0,text)
    return

def AIM():
    e1 = e.get()
    e_2 = e2.get()
    e_3 = e3.get()

    numberM = float(e1)
    epochsM = float(e_2)
    ysmM = float(e_3)

    prediction = AImultiplier(ysmM, numberM, epochsM)

    label2.config(text=("The result is " + str(round(prediction))))

def set_fullscreen():
    root.attributes('-fullscreen', True)

def set_window():
    root.attributes('-fullscreen', False)

set_text('2500')

root.geometry('400x500+600+150')
root.title('AI multiplies')
root.attributes('-fullscreen', False)
root.minsize(350,450)

label2 = tk.Label(root, text="", font=('Times',20))
label3 = tk.Label(root, text="Your epochs", font=('Times',20))
lable4 =tk.Label(root, text="x", font=('Times',20))
btn = tk.Button(root, text="Calculate",font=('Times',20), command=AIM)

image = tk.PhotoImage(file = 'Textures/Logo/Python.png')

root.iconphoto(False, image)

e.pack()

lable4.pack()
e3.pack()

label3.pack()
e2.pack()

btn.pack()

label2.pack()

root.mainloop()