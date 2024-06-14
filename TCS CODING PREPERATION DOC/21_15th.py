n=int(input("Enter The Number : "))
a=0
b=0
for i in range(1,n+1):
    if i%2!=0:
        a+=7
    else:
        b+=6
if n%2!=0:
    print(f'{n} term of series is {a-7}')
else:
    print(f'{n} term of series is {b-6}')
                