print("\n #2 \n")

a = list(input().split(" "))
b = ""
for i in range(0, len(a[1])-1, int(a[0])):
    for j in range(i + int(a[0]), i, -1):
        b+=a[1][j-1]
print(b)