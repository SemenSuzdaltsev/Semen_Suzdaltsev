def fast_f(N):
    if N<=1:
        return N
    a = 1
    b = 0
    for i in range(N-1):
        a,b = a + b, a
    return a