def nth(n):
    a=1
    b=1
    for i in range(1,n+1):
        if (i%2!=0):
            a=a*2
        else:
            b=b*2
    if n%2!=0:
        print(a//2)
    else:
        print(b//3)                
nth(5)        


def nth(n):
    a=1
    b=1
    for i in range(1,n+1):
        if (i%2!=0):
            a=i**2
        else:
            b=i**2
    if n%2!=0:
        print(a)
    else:
        print(b)                
nth(6)        