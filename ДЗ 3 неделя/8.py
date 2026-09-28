import numpy as np
n = int(input())
def mnk(x, y):
    x = np.array(x)
    y = np.array(y)
    k = np.sum((x - x.mean()) * (y - y.mean())) / np.sum((x - x.mean()) ** 2)
    b = y.mean() - k * x.mean()

    return k, b
a = np.random.randint(1,100, size=(n,1))
b = np.random.randint(1,100, size=(n,1))
print(a,b)


k,b = mnk(a, b)
print(k,b)
