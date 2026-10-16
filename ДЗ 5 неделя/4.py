from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        hex_color = str(feet.get()) 
        r = int(hex_color[1:3], 16)
        g = int(hex_color[3:5], 16)
        b = int(hex_color[5:7], 16)

        new_r = 255 - r
        new_g = 255 - g  
        new_b = 255 - b 
        ans.set(f"#{hex(new_r)[2:]}{hex(new_g)[2:]}{hex(new_b)[2:]}") 
        
    except ValueError:
        pass

root = Tk()
root.title("Calculate")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=20, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

ans = StringVar()
ttk.Label(mainframe, textvariable=ans).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Расчет", command=calculate).grid(column=3, row=2, sticky=W)

ttk.Label(mainframe, text="Введите цвет в формате #XXXXXX:").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Комплементарный данному:").grid(column=1, row=2, sticky=W)

feet_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()