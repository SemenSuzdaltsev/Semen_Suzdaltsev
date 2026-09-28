import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


pos = 0
size1 = 1000
size2 = 10000
size3 = 1000000

values1 = np.random.normal(pos, 10, size1)
values2 = np.random.normal(pos, 10, size2)
values3 = np.random.normal(pos, 10, size3)

fig = plt.figure(figsize = (10,6))


ax1 = fig.add_subplot(311)
ax2 = fig.add_subplot(312)
ax3 = fig.add_subplot(313)

ax1.set_title("Все выше")
ax2.set_title("И выше")
ax3.set_title("И выше, и выше")

ax1.hist(values1, 100)
ax2.hist(values2, 100)
ax3.hist(values3, 100)
plt.tight_layout()
plt.show()