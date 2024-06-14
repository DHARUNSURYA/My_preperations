def f(n):
    ns=str(n)
    nl=list(ns)
    nl=list(map(int,nl))
    m=1
    for i in nl:
        m*=i
    return m
print(f(5244)) # Output: 6