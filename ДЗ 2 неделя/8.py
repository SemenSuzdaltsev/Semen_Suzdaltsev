n = int(input())
s = list(map(int, input().split()))
for i in s:
    men, bol = 0, 0
    for j in s:
        if i>j:
            bol+=1
        elif i<j:
            men+=1
    if men==bol:
        print(i)
        break
        