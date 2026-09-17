print("hello цщworld")


#git init
#git add
#git commit -m "comment"

#git push -u origin main

#генераторы

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


a = [i*j for i in range(1,10) for j in range(1,10)]

vec = [[1,2,3],[4,5,6],[7,8,9]]
print(*[num for elem in vec for num in elem])

b = "123"
f = a.extend(b)
print(f)

a = 1
b = 2
print("sum of {} and {} = {}".format(a,b,a+b)) #аналоговые ф строки
print(f"{b = }")
p = 1.34921384190283
print(f"{p:.2f}")
print(f"{17:o}")
print(f"{17:b}")
print(f"{17:#b}")

print("\n #2 \n")

a = list(input().split(" "))

print(a)

b = ""

for i in range(0, len(a[1])-1, int(a[0])):
    for j in range(i + int(a[0]), i, -1):
        b+=a[1][j-1]

print(b)


G,s = input().split()
G = int(G)
group_len = len(s)//G

print("".join(s[i:i+group_len][::-1] for i in range(0, len(s), group_len)))


print("\n #4 \n")

a = input().split()
a[0:-1:2], a[1::2] = a[1::2], a[0:-1:2]
print(*a)

print("\n #4 \n")

