#4
import os
x = os.path.join(os.path.dirname(__file__), "input.txt")
x1 = os.path.join(os.path.dirname(__file__), "output.txt")

with open(x, "r") as file, open(x1, "w") as file2:
    s = file.readlines()
    numbers = list(map(int, s[0].split()))
    z = s[1].strip()
    if z == "+":
        z = sum(numbers)
    elif z == "-":
        z = numbers[0]
        for i in numbers[1:]:
            z -= i
    elif z == "*":
        z = 1
        for i in numbers:
            z *= i
    file2.write(str(z))

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

x = os.path.join(os.path.dirname(__file__), "input.txt")
x1 = os.path.join(os.path.dirname(__file__), "output.txt")

with open(x, "r") as file, open(x1, "w") as file2:
    s = file.readlines()
    numbers1 = list(map(int, s[0].split()))
    numbers = []
    z = s[1].strip()
    N = int(s[2].strip())
    for i in numbers1:
        N0 = 0
        l = len(str(i))-1
        for j in str(i):
            N0+=int(j)*N**l
            l-=1
        numbers.append(N0) 
    if z == "+":
        z = sum(numbers)
    elif z == "-":
        z = numbers[0]
        for i in numbers[1:]:
            z -= i
    elif z == "*":
        z = 1
        for i in numbers:
            z *= i
    ans = ""
    print(z)
    while z>0:
        ans += str(z%int(s[2]))
        z//=int(s[2])
    res = ans[::-1]
    print(res)
    file2.write(str(res))