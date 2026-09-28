import pandas as pd
import matplotlib.pyplot as plt
import os
x_path = os.path.join(os.path.dirname(__file__), "BTC_data.csv")
df = pd.read_csv(x_path)

df['time'] = (pd.to_datetime(df['time'])
                .dt.tz_localize(None)
                .dt.normalize())
print(df['time'])

plt.plot(df['time'],df["close"], "r")

a =[]
n=0
for i in df["time"]:
    n+=1
    if n%70==0:
        a.append(i)
plt.xticks(a, rotation=75)

plt.tight_layout()
plt.show()