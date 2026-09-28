import pandas as pd
import os
import matplotlib.pyplot as plt
x_path = os.path.join(os.path.dirname(__file__), "iris_data.csv")
df = pd.read_csv(x_path)
l = df["Species"].unique()
a = []
for i in l:
    a.append(list(df["Species"]).count(i))
plt.pie(a, labels = l, autopct = "%1.1f%%")
plt.show()

#иначе

counts = df["Species"].value_counts()


#2 part

x = sum(df["PetalLengthCm"] <= 1.2)
y = sum((df["PetalLengthCm"] > 1.2) & (df["PetalLengthCm"] <= 1.5))
z = sum(df["PetalLengthCm"] > 1.5)

plt.pie((x,y,z), labels = ["small", "medium", "big"])
plt.show()