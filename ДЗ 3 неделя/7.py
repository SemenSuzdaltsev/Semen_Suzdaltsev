import numpy as np
N,M = map(int, input().split())
s = []
for i in range(N):
    s.append(input().split())
sn = np.array(s)
b = (sn.T[-1]).T
s = (np.array([[int(x) for x in row] for row in sn]).T[:N]).T
d = np.linalg.det(s)
di = [d]
def det(s):
    if N!=M-1:
        return print("Система имеет бесконечно много решений, либо не имеет вовсе")
    else:
        for i in range(M-1):
            sx= s.copy()
            sx[:, -(N-i)] = b
            di.append(np.linalg.det(sx))
    for i in range(N):
        print(f"x{i+1} = {round(((di[i+1])/(di[0])),2)}")

det(s)
