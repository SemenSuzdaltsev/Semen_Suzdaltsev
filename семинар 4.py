import pandas as pd
import os
x_path = os.path.join(os.path.dirname(__file__), "iris_data.csv")
df = pd.read_csv(x_path)
print(df)
print(df.iloc[0:5]) #обзор строчек


#множестваa
a = set("Hello")
a.add(1)
print(a)
print(a.pop())
a.discard("H")
print(a)
b = {1,2,3,4}
a = {6,5,3,2}
print(a<=b) #является ли подмножеством
#a&b a|b a^b последнее XOR
#словари

a = frozenset("Hello") #неизменяемый

a = {1: "a", 2: "b", 3: "g"}
print(a.get(1))
#print(a.pop()) #удаляет и возвращает
for k,v in a.items():
    print(k,v)
print(a.keys(), a.values())


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x2 = np.linspace(0,4,100)
x = [0,1,2,3,4]
y = [0,2,4,6,8]

plt.figure(figsize = (10,6))
plt.plot(x,y, "rD:", markersize = 12, linewidth = 2, alpha = 0.5, markerfacecolor = "y", markeredgecolor = "b", label = "Test")

plt.plot(x2[:40], x2[:40]**2+1, "r", label = "$x^2$")
plt.plot(x2[40:], x2[40:]**2+1, "r--")
plt.title("GRAFIC", fontsize = 20, color = "m", loc = "right", fontweight = "bold", fontstyle = "italic", pad = 10)
plt.xlabel("X")
plt.ylabel("Y")
#сетка

#ручное построение сетки
plt.xticks([0,0.1,2.66,3.35])
plt.xticks([0,1,2])
plt.grid(color = (0,1,0))
plt.legend()
plt.show()


pos = 0
 
# параметр отвечающий за разброс
scale = 10
 
# размер массива случайных чисел (сколько их сгенерируем)
size = 10000
 
# используем функцию из подраздела random библиотеки numpy и передадим наши параметры
values = np.random.normal(pos, 10, size)
 
# строим гистограмму с 100 блоков
plt.hist(values, 100)

plt.show()



lables = ["A","B","C"]
a = [3,5,2]
values = [1,4,2]

plt.bar(lables,values,color = ["r","g","b"])
plt.show()

plt.barh(lables,values,color = ["r","g","b"])
plt.show()


x = [i for i in range(50)]
y = [j for j in range(50)]
s = [i+j for i in x for j in y]

plt.hist(s, bins = 20, density = True, histtype = "step")

plt.show()

plt.pie([0.5,0.5,0.2], labels = [1,2,3], autopct = "%1.1f%%", explode = [0.2,0.2,0.2], shadow = True, startangle= 90, wedgeprops = {"width": 0.4})
plt.show()

fig = plt.figure(figsize = (10,8))

ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

ax1.set_title("skfvs[fv]")
ax1.set_xlabel("X")
ax2.grid()
fig.suptitle("fsdkflv")

ax1.plot(np.arange(100),np.arange(100)**2)
ax2.plot(np.arange(100),np.arange(100)**0.5)
plt.tight_layout()
plt.show()



fig = plt.figure(figsize = (10,9)) # создали рисунок/Figure Fig пропорциями 16:9
ax1 = fig.add_subplot(111) # допустим, больше 1 графика нам не надо

x_measured = [1.01, 2.59, 3.03, 5.40, 7.33]
y_measured = [0.41, 0.84, 1.11, 3.22, 5.00]

x = [0.5, 9.0]
y = np.interp(x, x_measured, y_measured)

# ставим точки функцией scatter, точки будем ставить крестиком
ax1.scatter(x_measured, y_measured, marker='x')

# поставим кресты погрешностей, linestyle = None, чтобы кресты не соединялись прямыми
ax1.errorbar(x_measured, y_measured, yerr=0.2, xerr = 0.1, color = 'k', linestyle = 'None')

#построим красную прямую МНК
ax1.plot(x,y, 'r')

ax1.grid() # делаем сетку

mnk = np.polyfit(x_measured,y_measured,2)
z = np.poly1d(mnk)

x = np.linspace(0,9,100)

plt.plot(x,z(x))

plt.show()

