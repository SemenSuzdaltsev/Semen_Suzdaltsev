import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk, messagebox, filedialog

def mnk(x, y):
    x = np.array(x)
    y = np.array(y)
    k = np.sum((x - x.mean()) * (y - y.mean())) / np.sum((x - x.mean()) ** 2)
    b = y.mean() - k * x.mean()

    return k, b
def calculate(*args):
    file_name = name.get().strip()
    print(file_name)
    x_col = x.get().strip()
    y_col = y.get().strip()
    print(x_col,y_col)
    x_path = os.path.join(os.path.dirname(__file__), file_name)
    data = pd.read_csv(x_path, encoding='cp1251')  

    k,b = mnk(data[x_col].astype(float).values,data[y_col].astype(float).values)
    result.set(f"k = {k:.5f}\nb = {b:.5f}")
    save_plot(data[x_col].astype(float).values, data[y_col].astype(float).values, k, b)

def save_plot(x_data, y_data, k, b, default_name="grafic"):
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.scatter(x_data, y_data, color='steelblue', s=25,
               label='Данные', zorder=3)

    x_line = np.linspace(min(x_data), max(x_data), 100)
    ax.plot(x_line, k * x_line + b, 'r-', linewidth=2,
            label=f'МНК: y = {k:.4f}x + {b:.4f}')

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Аппроксимация МНК')
    ax.grid(alpha=0.3)
    ax.legend()

    answer = messagebox.askyesno(
        "Сохранить график?",
        "Хотите сохранить график в файл?"
    )

    if answer:
        path = filedialog.asksaveasfilename(
            title="Куда сохранить график?",
            defaultextension=".png",
            initialfile=f"{default_name}.png",
        )
        if path:
            fig.savefig(path, dpi=150, bbox_inches='tight')
            messagebox.showinfo("Готово", f"График сохранён:\n{path}")

    plt.show()

root = Tk()
root.title("Наша лаба")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

name = StringVar()
feet_entry1 = ttk.Entry(mainframe, width=20, textvariable=name)
feet_entry1.grid(column=2, row=1, sticky=(W, E))
x = StringVar()
feet_entry1 = ttk.Entry(mainframe, width=20, textvariable=x)
feet_entry1.grid(column=4, row=1, sticky=(W, E))
y = StringVar()
feet_entry = ttk.Entry(mainframe, width=20, textvariable=y)
feet_entry.grid(column=5, row=1, sticky=(W, E))


result = StringVar()
ttk.Label(mainframe, textvariable=result).grid(column=3, row=2, sticky= E)
ttk.Button(mainframe, text="Посчитать", command=calculate).grid(column=2, row=2, sticky=E)

ttk.Label(mainframe, text="Название файла, где лежат данные:").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Введите названия переменных по которым будем строить прямую (x,y):").grid(column=3, row=1, sticky=W)

feet_entry.focus()
root.bind("<Return>", calculate)
root.columnconfigure(0, weight=0)

root.mainloop()
