from tkinter import *

def saveposn(event):
    global lastx, lasty
    lastx,lasty = event.x, event.y

def add_line(event):
    global lastx, lasty
    canvas.create_line(lastx,lasty,event.x,event.y, fill = "red")
    lines.append((lastx, lasty, event.x, event.y))
    saveposn(event)

def redraw():
    canvas.delete("all")
    for line in lines:
        x1, y1, x2, y2 = line
        canvas.create_line(x1 * scale, y1 * scale, 
                           x2 * scale, y2 * scale, width=2, fill = "red")

def zoom(event):
    global scale
    if event.delta > 0:
        scale *= 1.1
    else:
        scale /= 1.1
    
    redraw()

prev_kx, prev_ky = 1.0, 1.0

def on_resize(event):
    global prev_kx, prev_ky
    w, h = canvas.winfo_width(), canvas.winfo_height()
    kx = w / 600
    ky = h / 600
    canvas.scale("all", 0, 0, kx / prev_kx, ky / prev_ky)
    prev_kx, prev_ky = kx, ky

def delete(*args):
    global lines
    lines.clear()
    canvas.delete("all")
    redraw()

root = Tk()
root.geometry("600x600")
lastx, lasty = 0,0
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)
scale = 1.0
lines = []
canvas = Canvas(root)
canvas.grid(column = 0, row = 0, sticky = (N,W,E,S))
canvas.bind("<Button-1>",saveposn)
canvas.bind("<B1-Motion>",add_line)
canvas.bind("<MouseWheel>", zoom)    
canvas.bind("<Configure>", on_resize)
canvas.bind("<Escape>", delete)
canvas.pack(fill = BOTH, expand = True) 

root.mainloop()