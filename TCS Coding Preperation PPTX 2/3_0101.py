# def decimal_to_binary(n):
    
#     if n==0:
#         return 0
#     binaryno=""
    
#     while n>0:
#         remainder=n%2
#         binaryno=str(remainder)+binaryno
#         n=n//2
#     return binaryno



# print(decimal_to_binary(10)) 

def dtob(n):
    if n==0:
        return 0
    
    b=""
    while n>0:
        r=n%2
        b=str(r)+b
        n=n//2
        
    return b
print(dtob(25))