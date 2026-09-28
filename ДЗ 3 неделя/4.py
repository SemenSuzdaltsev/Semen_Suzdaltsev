l,b = input().split()
l = int(l)
s = f"{b}"
for i in range(2, l//2+1):
    s+="\n"
    s+= f"{i*b}"
if l%2==1:
    s1 = f"\n{b*(l//2 + l%2)}"
else:
    s1 = ""
s = s + s1 + "\n"+s[::-1]
print(s)
