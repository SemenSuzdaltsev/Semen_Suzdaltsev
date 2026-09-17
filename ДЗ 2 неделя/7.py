a = list(map(int, input().split()))
s = {}
for i in a:
    if i in s:
        s[i] += 1
    else:
        s[i] = 1
maxs = 0
maxn = 0
for i in s:
    if s[i] > maxn:
        maxs = i
        maxn = s[i]
print(maxs)