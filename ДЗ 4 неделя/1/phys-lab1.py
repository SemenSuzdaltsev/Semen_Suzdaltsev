import pandas as pd
import os
import numpy as np
x = os.path.join(os.path.dirname(__file__), "phys.xlsx")
import matplotlib.pyplot as plt

data = pd.read_excel(x)
plt.title('Исследование сопротивления нихромовой проволоки', fontsize=17)
err_X = 0
err_Y = 2.5


def least_squares(x, y):
    coeff = np.mean(x*y)/np.mean(x*x)
    err = 1 / np.sqrt(len(x)-1) * np.sqrt((y*y).mean() / (x*x).mean() - coeff ** 2)
    return coeff, err




coeff1, err1 = least_squares(data['X'], data['Y'])
print(err1)
coeff2, err2 = least_squares(data['X1'], data['Y1'])
print(err2)
coeff3, err3 = least_squares(data['X2'], data['Y2'])
print(err3)
coeff4, err4 = least_squares(data['X3'], data['Y3'])
print(err4)

plt.errorbar(data['X'], data['Y'], err_Y, err_X, fmt='.')
plt.errorbar(data['X1'], data['Y1'], err_Y, err_X, fmt='.')

plt.errorbar(data['X2'], data['Y2'], err_Y, err_X, fmt='.')
plt.errorbar(data['X3'], data['Y3'], err_Y, err_X, fmt='.')

plt.plot(data['X'], coeff1 * data['X'], color='tab:red', label = "l = 10 cм")
plt.plot(data['X1'], coeff2 * data['X1'], color='tab:blue', label = "l = 20 cм")
plt.plot(data['X2'], coeff3 * data['X2'], color='tab:green', label = "l = 30 cм")
plt.plot(data['X3'], coeff4 * data['X3'], color='tab:purple', label = "l = 50 cм")

plt.text(200, 158, f'R10 = {round(coeff1,3)}')
plt.text(138, 218, f'R20 = {round(coeff2,3)}')
plt.text(192, 536, f"R30 = {round(coeff3,3)}")
plt.text(156, 714, f'R50 = {round(coeff4,3)}')



plt.xlabel('Ток, мА')
plt.ylabel('Напряжение, мВ')
plt.legend()
plt.grid() # Добавляет сетку
plt.show()