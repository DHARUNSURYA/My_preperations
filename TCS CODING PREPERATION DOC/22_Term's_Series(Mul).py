n=int(input("Enter The Number : "))
a=1
b=1
for i in range(1,n+1):
    if i%2!=0:
        a*=2
    else:
        b*=3
if n%2!=0:
    print(f'{n} term of series is {round(a/2)}')
else:
    print(f'{n} term of number is {round(n/3)} ')                