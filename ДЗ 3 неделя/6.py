import numpy as np

def mnk(x, y):
    x = np.array(x)
    y = np.array(y)
    k = np.sum((x - x.mean()) * (y - y.mean())) / np.sum((x - x.mean()) ** 2)
    b = y.mean() - k * x.mean()

    return k, b