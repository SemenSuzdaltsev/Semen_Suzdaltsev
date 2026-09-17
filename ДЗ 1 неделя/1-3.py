#1

a, b = map(int, input().split())
print(a+b)
print(a-b)
print(a*b)


#2

a = int(input())
print(a%10)

#3

a = input().split()
p=1
for i in a:
    p*=int(i)
print(round(p**(1/len(a)),3))
