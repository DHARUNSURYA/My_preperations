def f(n):
    ns=str(n)
    nl=len(ns)
    e=0
    o=0
    for i in range(nl):
        if i%2==0:
            e+=int(ns[i])
        else:
            o+=int(ns[i])
    return e-o

print(f(5179))        
        