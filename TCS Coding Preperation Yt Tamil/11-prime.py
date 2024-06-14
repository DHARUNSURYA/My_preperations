def isprime(n):
    count=0
    if n<=1:
        print('is not prime no')
    for i in range(2,n):
        if n%i==0:
            count+=1
    if count:
        print('no prime')
    else:
        print('prime')        
isprime(6)            