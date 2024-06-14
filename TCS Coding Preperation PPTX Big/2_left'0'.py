# n=int(input("Enter n : "))
# l=[]
# for i in range(n):
#     a=int(input("Enter no : "))
#     l.append(a)
# print(sorted(l))    

n=int(input())
j=-1
L=[0 for i in range(n)]
for i in range(n):
    a=int(input())
    if a!=0:
        L[j]=a
        j-=1
for i in L:
    print(i,end=" ")
