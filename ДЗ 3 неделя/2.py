n = int(input())
def prost(n):
    p=set()
    for i in range(2,n+1):
        while n%i==0:
            p.add(i)
            n=n//i
    return p
print(*prost(n))
