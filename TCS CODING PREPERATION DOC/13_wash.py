n=int(input("Enter: "))
if n==0:
    print("0 Minutes")
elif n in range(1,2001):
    print("25 Minutes")
elif n in range(2001,4001):
    print("35 Minutes")
elif n in range(4001,7001):
    print("45 Minutes")
else:
    print("INVALID INPUT")    
            
            
            