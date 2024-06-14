n=int(input())
c=0
import sys
m=-sys.maxsize-1
maxval=float('-inf')
for i in range(n):
    a=int(input("Enater {i} Of Array: "))
    if a>maxval:
        maxval=a
        c+=1
print(c)        
         
    