print("\n #9 \n")
import os
x = os.path.join(os.path.dirname(__file__), "input.txt")
with open(x, "r", encoding="utf-8") as file:
    s = file.readlines()
    pred=0
    last=0
    for i in s:
        for j in i:
            if j=="." and last==0:
                pred+=1
                last+=1
            elif j=="!" and last==0:
                pred+=1
                last+=1
            elif j=="?" and last==0:
                pred+=1
                last+=1
            elif j!="." and j!="!" and j!="?":
                last=0
            
print(pred)