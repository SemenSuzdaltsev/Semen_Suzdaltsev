from random import randint

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
        return Vector(self.x+other.x,self.y+other.y,self.z+other.z)
    def __sub__(self, other):
        return Vector(self.x-other.x,self.y-other.y,self.z-other.z)
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

def area(vec1,vec2,vec3):
    z = vec3-vec1
    y = vec2-vec1
    return abs(y.vectornoe(z))/2

a = []
for i in range(10):
    a.append(Vector(randint(-10,10),randint(-10,10),randint(-10,10)))
def max_area(L):
    areas = []
    for i in L:
        for j in L:
            for k in L:
                areas.append(area(i,j,k))
    print(round(max(areas),2))
max_area(a)  