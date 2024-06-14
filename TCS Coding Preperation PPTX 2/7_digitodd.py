def f(n):
    sn=str(n)
    nl=len(sn)
    no=0
    ne=0
    for i in range(nl):
        if i%2==0:
            ne+=int(sn[i])
        else:
            no+=int(sn[i])
    return no-ne

print(f(4567))  # Correct usage and output
