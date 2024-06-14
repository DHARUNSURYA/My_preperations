n=int(input("Enter The Number : "))
a=0
b=0
for i in range(1,n+1):
    if i%2!=0:
        a+=2
    else:
        b+=1
if n%2!=0:
    print(f'{n} term no is {a-2}')
else:
    print(f'{n} term no is {a-1}')        
                