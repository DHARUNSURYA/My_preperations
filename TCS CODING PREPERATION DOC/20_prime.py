def prime(n):
    if n>1:
        for i in range(2,n):
            if n %i==0:
                print(n,"is not prime number")
                break
        else:
           print(n,"is prime number")
n=int(input("Enter a Number : "))
if n>0:
    prime(n)
else:
    print("Pleace Enter A Positive Number")                    
                