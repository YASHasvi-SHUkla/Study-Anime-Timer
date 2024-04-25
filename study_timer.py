import tkinter as tk
from PIL import Image, ImageTk
from tkinter import font


countdown_job = None

def countdown(count):
    global countdown_job
    label['text'] = f"{count // 60:02d}:{count % 60:02d}"

    if count > 0:
        countdown_job = dracule.after(1000, countdown, count - 1)

def start_30min():
    global countdown_job
    if countdown_job is not None:
        dracule.after_cancel(countdown_job)
    countdown(30 * 60)

def start_5min():
    global countdown_job
    if countdown_job is not None:
        dracule.after_cancel(countdown_job)
    countdown(5 * 60)

dracule = tk.Tk()
dracule.geometry('550x350')
dracule.title('UNLEASHED')
dracule.configure(background='#16141a')
dracule.resizable(False, False)

fontecust = font.Font(family="Merriweather", size=22)
fontecust2 = font.Font(family="Merriweather", size=16)
fontecust3 = font.Font(family="Merriweather", size=26)


path = '././perfect.png'

img = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(dracule, image=img)
panel.pack(side="bottom", fill="both", expand="yes")

texto = tk.Label(dracule, text="Study Timer", bg='#FED49A', fg='black', font=fontecust, highlightbackground='black',
                 highlightthickness=2)
texto.place(x=190, y=105)

label = tk.Label(dracule, text="", bg='#B836FF', fg='black', font=fontecust3, borderwidth=5, highlightbackground='black', highlightthickness=2)
label.place(x=230, y=155)


botao_iniciar = tk.Button(dracule, text='Study!', bg='#00BCD4', fg='black', font=fontecust2, borderwidth=5,
                          command=start_30min)
botao_iniciar.place(x=185, y=220)

botao_rest = tk.Button(dracule, text='Rest', bg='#FFFF00', fg='black', font=fontecust2, borderwidth=5,
                       command=start_5min)
botao_rest.place(x=300, y=220)


komthe = tk.Label(dracule, text='Coded by YASHasvi', font=fontecust2, bg='#569890', fg='black', highlightbackground='black', highlightthickness=2)
komthe.place(x=348, y=312)


dracule.mainloop()