from random import randint
a = [randint(10,50) for i in range(randint(10,50))]
b = [randint(10,50) for i in range(randint(10,50))]

print(a)
print("\n", b)
print(f"уникальные в а {set(a)}")
print(f"уникальные в б {set(b)}")

print(f"Уникальные для обьединения {set(a)|set(b)}")
print(f"Уникальные для пересечния {set(a)&set(b)}")