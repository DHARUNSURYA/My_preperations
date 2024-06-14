# def f(no,r):
#     nos=str(no)
#     nol=list(nos)
#     nol=list(map(int,nol))
#     nolsum=sum(nol)
#     rn=r*nolsum
    
#     rns=str(rn)
#     rnsl=list(rns)
#     rnsl=list(map(int,rnsl))
#     return sum(rnsl)
# print(f(1234,2))    
s=input()
n=int(input())
sum=0
for i in s:
    sum+=int(i)
sum*=n
s=str(sum)
sum1=0
for i in s:
    sum1+=int(i)
 

print(sum1)
