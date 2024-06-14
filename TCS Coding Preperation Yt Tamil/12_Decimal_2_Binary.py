# def d2b(n):
#     if n==0:
#         return 0
#     b=''
#     while n>0:
#         r=n%2
#         b=str(r)+b
#         n=n//2
#     return b    
# print(d2b(25)) 

def dtob(n):
    return bin(n)[2:]
d=25
print(dtob(d))       