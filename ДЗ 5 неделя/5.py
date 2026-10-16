from random import randint
from tkinter import *
from random import randint
from math import sqrt
WIDTH = 600
HEIGHT = 600

class Ball:
    def __init__(self):
        self.R = randint(10, 50) 
        self.x = randint(self.R, root.winfo_width() - self.R)
        self.y = randint(self.R, root.winfo_height() - self.R)
        self.dx, self.dy = (randint(5,20), randint(5,20))
        self.ball_id = canvas.create_oval(self.x - self.R,
                                     self.y - self.R,
                                     self.x + self.R,
                                     self.y + self.R, fill=f"#{randint(100000,999999)}") 

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x + self.R + 0.5 > root.winfo_width() or self.x - self.R -10 <= 0:
            self.dx = -self.dx
        if self.y + self.R + 0.5> root.winfo_height() or self.y - self.R -20<= 0: 
            self.dy = -self.dy

    def show(self):
        canvas.move(self.ball_id, self.dx, self.dy)

def click_handler(event):
    print('Hello World! x=', event.x, 'y=', event.y)

def resolve_collision(a, b):
    dx = b.x - a.x
    dy = b.y - a.y
    dist = sqrt(dx * dx + dy * dy)

    if dist == 0 or dist >= a.R + b.R:
        return

    nx = dx / dist
    ny = dy / dist

    dvx = b.dx - a.dx
    dvy = b.dy - a.dy
    vn = dvx * nx + dvy * ny

    if vn > 0:
        return

    a.dx += vn * nx
    a.dy += vn * ny
    b.dx -= vn * nx
    b.dy -= vn * ny

    overlap = a.R + b.R - dist
    a.x -= nx * overlap / 2
    a.y -= ny * overlap / 2
    b.x += nx * overlap / 2
    b.y += ny * overlap / 2


def tick():
    for i in range(len(balls)):
        for j in range(i + 1, len(balls)):
            resolve_collision(balls[i], balls[j])

    for ball in balls:
        ball.show()
        ball.move()

    root.after(50, tick)

root = Tk()
root.geometry(f'{WIDTH}x{HEIGHT}')
root.update()
canvas = Canvas(root)
balls = [Ball() for i in range(5)]
canvas.pack(fill = BOTH, expand = True)
def click(*args):
    balls.append(Ball())

canvas.bind('<Button-1>', click)

tick()
root.mainloop()