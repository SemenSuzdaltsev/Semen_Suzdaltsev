#скачать зарегестрироваться на гитхаб
import os
x_path = os.path.join(os.path.dirname(__file__), "text.txt")
x1_path = os.path.join(os.path.dirname(__file__), "text2.txt")

with open(x_path, "r") as file, open(x1_path, "w") as file2:
    s = file.readlines()
    z=0
    for i in list(s[0].split()):
        a = int(i,int(s[2]))
        if s[1] == "+":
            z+=a
        elif s[1] == "-":
            z-=a
        else:
            z*=a
        print(z)
        z+=a
        print(z)
    ans = "" 
    print(z)
    while z>0:
        ans += str(z%int(s[2]))
        z//=int(s[2])
    res = ans[::-1]
    print(res)

    file2.write(f"{res}")







import os
x_path = os.path.join(os.path.dirname(__file__), "text.txt")
x1_path = os.path.join(os.path.dirname(__file__), "text2.txt")

with open(x_path, "r") as file, open(x1_path, "w") as file2:
    s = file.readlines()
    z=0
    for i in list(s[0].split()):
        i = int(i,int(s[2]))
        if s[1] == "+":
            z+=int(i)
        elif s[1] == "-":
            z-=int(i)
        else:
            z*=int(i)
    ans = ""
    while z>0:
        ans += str(N%int(s[2]))
        N//=int(s[2])
    res = ans[::-1]
    print(res)

    file2.write(f"{res}")


import os

x_path = os.path.join(os.path.dirname(__file__), "text.txt")
x1_path = os.path.join(os.path.dirname(__file__), "text2.txt")

#4

with open(x_path, "r") as file, open(x1_path, "w") as file2:
    s = file.readlines()
    z=0
    for i in list(s[0].split()):
        if s[1] == "+":
            z+=int(i)
        elif s[1] == "-":
            z-=int(i)
        else:
            z*=int(i)
    file2.write(f"{z}")

#5

Nn = input()
b = int(input())
c = int(input())
ans = ""
N = 0
l = len(Nn)-1
for i in Nn:
    N+=int(i)*b**l
    l-=1
while N>0:
    ans += str(N%c)
    N//=c
print(ans[::-1])

#6
x_path = os.path.join(os.path.dirname(__file__), "text.txt")
x1_path = os.path.join(os.path.dirname(__file__), "text2.txt")

with open(x_path, "r") as file, open(x1_path, "w") as file2:
    s = file.readlines()
    z=0
    for i in list(s[0].split()):
        i = int(i,int(s[2]))
        if s[1] == "+":
            z+=int(i)
        elif s[1] == "-":
            z-=int(i)
        else:
            z*=int(i)
    ans = ""
    while z>0:
        ans += str(N%int(s[2]))
        N//=int(s[2])
    res = ans[::-1]
    print(res)

    file2.write(f"{res}")

