class Vector():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __abs__(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x+other.x,self.y+other.y,self.z+other.z)
        elif isinstance(other, int) or isinstance(other, float):
            return Vector(self.x+other,self.y+other,self.z+other)
    def __radd__(self, other):
        return self + other
    def __sub__(self, other):
        return self - other
    def __str__(self):
        return f'x = {self.x} y = {self.y} z = {self.z}'

    def vectornoe(self,other):
        assert isinstance(other, Vector)
        a,b,c = other.x, other.y,other.z
        x1 = self.y*c-b*self.z
        y1 = self.z*a-c*self.x
        z1 = self.x*b-a*self.y
        return Vector(x1,y1,z1)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x*other.x+self.y*other.y+self.z*other.z
        else:
            self.x *=other
            self.y *=other
            self.z *=other

v = Vector(1,1,1)
print(v.vector_u(1,-1,1))
import numpy as np
from random import randint
a = []
for i in range(10):
    a.append([randint(-10,10),randint(-10,10),randint(-10,10)])
print(a)
print(f"Центр масс (x,y,z) {sum([i for i in a[0]])/10} {sum([i for i in a[1]])/10} {sum([i for i in a[2]])/10}")
