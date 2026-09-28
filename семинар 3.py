#рекурсия
#долго
def fib(N, cache = {0:0,1:1}):
    if N in cache:
        return cache[N]
    else:
        cache[N] = fib(N-1,cache) +fib(N-2, cache)
        return cache[N]

print(fib(100))

#быстро

def fast_f(N):
    if N<=1:
        return N
    a = 1
    b = 0
    for i in range(N-1):
        a,b = a + b, a
    return a

print(fast_f(100))

#увеличение длины допустимой рекурсии
a = 10000
#увеличенное допустмое число
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(a)

def f(x=[]):
    x.append(1)
    print(x)
for i in range(5):
    f()


print("\n #2 \n")

#без рекурсии

n = 30
def prost(n):
    p=set()
    for i in range(2,n+1):
        while n%i==0:
            p.add(i)
            n=n//i
    return p
print(*prost(n))

#с рекурсией

def prost1(n, i = 2):
    while(i*i <=n):
        if n%i:
            i+=1
        else:
            return [i]+prost1(n//i,i)
    return [n]
print(prost1(n))




#numpy

import numpy as np

a = np.array([1,2,3])
print(a)
b = np.array([1,2,3])
print(a+b)
print(a*b)
print(a@b) #матричное произведение
print(np.cos(a))
print(a<2)

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a.shape)
print(a.size)
print(a.reshape(1,-1))
print(np.zeros((5,5))) # аналогично ones из единиц eye единичная матрица
print(np.full((3,4),7))

print(np.empty((4,4))) #заливает чем угодно

print(np.diag([1,2,3], k = 2))

print(np.arange(10,30,5))
print(np.linspace(10,30,100))

# транспонирование a.T

a = np.array([1,2,3])
b = np.array([[1],[2],[3]])
print(a+b) #растягивает

a = np.arange(9).reshape(3,3)
print(a.max())
print(a.argmax()) #индекс в развернутом списке 
print(a.sum())
print(a.prod())
print(a.tolist()) #вернет питоновский список
print(a.sum(axis = 1)) #сумма по строкам в строку
print(a.sum(axis = 0)) #сумма по столбцам в строку
print(a.var()) #сигма квадрат
print(a.std()) #сигма
print(np.where(a<5, a, 0))
print(np.where(a<5, a*2, a*10))


a = np.array([30,10,20])
print(np.sort(a))
print(np.argsort(a))

print(np.random.randint(2,5, size=(2,4)))
print(np.random.randint([1,3,5,7], [[10],[20]])) #от 1 до 10 от 3 10 ... от 1 до 20 от 3 до 20 ...
rng = np.random.default_rng()
print(rng.random((3,3)))
print(rng.normal((1,2,(2,2)))) #параметры распределения среднее и отклонение и размер


a = np.arange(12).reshape(3,4)
i = np.array([[0,1],[1,2]]) #сетка выбора строки для элемента
j = np.array([[2,1],[3,3]]) #сетка выбора столбца для элемент
print(a[i,j]) # по данным матрицы а заполнит матрицу 2 на 2 элементами 0 2, 1 1 , если надо матрицу j забродкастим те растянем по строкам 

print(a[i,:]) #проходим по каждому
print(a[:,i]) # проходим по каждой строчки и пытаемся взять индекс i
print(a[i]) #на каркас i натягиваем данные с интересующих нас индексов строк


a = np.array([[1,0,1],[1,2,1],[3,1,1]])

print(np.linalg.det(a))
print(np.linalg.inv(a))

print(np.linalg.matrix_rank(a))

#задачи по numpy
a = np.zeros((8,8))
a[0::2,1::2] = 1
a[1::2,0::2] = 1
print(a)

print(np.nan == np.nan) #пустота не равна пустоте
print(np.inclose(0.3,3*0.1,1e-10)) # проверка на отдичеи больше чем на заданное

#задача отсортировать строки матрицы по значениями второго столбца
a = a[np.argsort(a[:,1])]
print(a)

#суммируем массив по двум последним осям

a = np.arange(2*3*4*5).reshape(3,4,5)
print(np.sum(a,axis=(-2,-1)))


#вычесть из элементов строки среднеарифметическое по этой строке
a = np.arange(12).reshape(3,4)
print(a - np.mean(a,axis=1).reshape(-1,1))



#5
n,m = list(map(int, input().split()))




#6
def least_squares(x, y):
    coeff = np.mean(x*y)/np.mean(x*x)
    err = 1 / np.sqrt(len(x)-1) * np.sqrt((y*y).mean() / (x*x).mean() - coeff ** 2)
    return coeff, err
