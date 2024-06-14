def f(n,r):
    if r ==0:
        return 0
    
    ns=str(n)
    nl=list(ns)
    nl=list(map(int,nl))
    sn=sum(nl)
    
    mn=r*sn
    
    mns=str(mn)
    mnl=list(mns)
    mnl=list(map(int,mnl))
    
    
    
    print(sum(mnl))
f(1234,2)    
    