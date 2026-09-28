import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
x_path = os.path.join(os.path.dirname(__file__), "iris_data.csv")
df = pd.read_csv(x_path)

fig = plt.figure(figsize = (10,8))

def mnk(x, y):
    x = np.array(x)
    y = np.array(y)
    k = np.sum((x - x.mean()) * (y - y.mean())) / np.sum((x - x.mean()) ** 2)
    b = y.mean() - k * x.mean()

    return k, b

ax1 = fig.add_subplot(231)
ax2 = fig.add_subplot(232)
ax3 = fig.add_subplot(233)
ax4 = fig.add_subplot(234)
ax5 = fig.add_subplot(235)
ax6 = fig.add_subplot(236)

ax1.set_xlabel("SepalLengthCm")
ax1.set_ylabel("SepalWidthCm")

ax2.set_xlabel("SepalLengthCm")
ax2.set_ylabel("PetalLengthCm")

ax3.set_xlabel("SepalLengthCm")
ax3.set_ylabel("PetalWidthCm")

ax4.set_xlabel("SepalWidthCm")
ax4.set_ylabel("PetalLengthCm")

ax5.set_xlabel("SepalWidthCm")
ax5.set_ylabel("PetalWidthCm")

ax6.set_xlabel("PetalLengthCm")
ax6.set_ylabel("PetalWidthCm")



ax1.scatter(df["SepalLengthCm"],df["SepalWidthCm"], marker='x')
ax2.scatter(df["SepalLengthCm"],df["PetalLengthCm"], marker='x')
ax3.scatter(df["SepalLengthCm"],df["PetalWidthCm"], marker='x')
ax4.scatter(df["SepalWidthCm"],df["PetalLengthCm"], marker='x')
ax5.scatter(df["SepalWidthCm"],df["PetalWidthCm"], marker='x')
ax6.scatter(df["PetalLengthCm"],df["PetalWidthCm"], marker='x')

k1 = np.polyfit(df["SepalLengthCm"], df["SepalWidthCm"], 1)
k2= np.polyfit(df["SepalLengthCm"], df["PetalLengthCm"], 1)
k3 = np.polyfit(df["SepalLengthCm"], df["PetalWidthCm"], 1)
k4 = np.polyfit(df["SepalWidthCm"], df["PetalLengthCm"], 1)
k5 = np.polyfit(df["SepalWidthCm"], df["PetalWidthCm"], 1)
k6 = np.polyfit(df["PetalLengthCm"], df["PetalWidthCm"], 1)

x1 = np.linspace(df["SepalLengthCm"].min(), df["SepalLengthCm"].max(), 100)
ax1.plot(x1, k1[0] * x1 + k1[1], 'r')

x2 = np.linspace(df["SepalLengthCm"].min(), df["SepalLengthCm"].max(), 100)
ax2.plot(x2, k2[0] * x2 + k2[1], 'r')

x3 = np.linspace(df["SepalLengthCm"].min(), df["SepalLengthCm"].max(), 100)
ax3.plot(x3, k3[0] * x3 + k3[1], 'r')

x4 = np.linspace(df["SepalWidthCm"].min(), df["SepalWidthCm"].max(), 100)
ax4.plot(x4, k4[0] * x4 + k4[1], 'r')

x5 = np.linspace(df["SepalWidthCm"].min(), df["SepalWidthCm"].max(), 100)
ax5.plot(x5, k5[0] * x5 + k5[1], 'r')

x6 = np.linspace(df["PetalLengthCm"].min(), df["PetalLengthCm"].max(), 100)
ax6.plot(x6, k6[0] * x6 + k6[1], 'r')

plt.tight_layout()
plt.show()