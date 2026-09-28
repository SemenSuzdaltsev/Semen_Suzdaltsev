a,b = map(int, input().split())
def nod(a, b):
    while b != 0:
        a, b = b, a % b
    return a
d = nod(a,b)
s1=11110
s_min=10000
s=""
for i in range(-max(a,b), max(a,b)+1):
    for j in range(-max(a,b), max(a,b)+1):
        if a*i + b*j == d:
            if abs(i)+abs(j)<s_min:
                s = f"{int(i)} {int(j)}"
                s_min = abs(i)+abs(j)
                s1 = i
            elif abs(i)+abs(j)==s_min:
                if i<s1:
                    s = f"{int(i)} {int(j)}"
                    s_min = abs(i)+abs(j)
                    s1 = i
print(s, d)

