from tkinter import *
from tkinter import ttk


root = Tk()
root.title("ИМТ")
answers = {16:"Выраженный дефицит массы тела", 
           18.5:"Недостаточная (дефицит) масса тела",25:"Норма",
             30:"Избыточная масса тела (предожирение)",
             35:"Ожирение 1 степени",90:"Ожирение 2 степени и выше"}
result = StringVar()
def calculate(*args):
    try:
        ves = int(feet.get()) 
        rost = int(feet1.get())
        ans = ves*10000/rost**2
        last = 0
        for key in answers.keys():
            if last<=ans <= key:
                ans_slovo = answers[key]
            last = key
        result.set(f"ИМТ: {round(ans,2)} Итог: {ans_slovo}")
        
    except ValueError:
        pass




mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=20, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

feet1 = StringVar()
feet_entry1 = ttk.Entry(mainframe, width=20, textvariable=feet1)
feet_entry1.grid(column=4, row=1, sticky=(W, E))

ans = StringVar()
ttk.Label(mainframe, textvariable=result).grid(column=4, row=2, sticky= E)
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=2, row=2, sticky=E)

ttk.Label(mainframe, text="Введите ваш вес (кг):").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Введите ваш рост (см):").grid(column=3, row=1, sticky=W)

feet_entry.focus()
root.bind("<Return>", calculate)
root.columnconfigure(0, weight=0)

root.mainloop()