def gcd(n1,n2):
    while n2!=0:
        n1,n2=n2,n1%n2
    return n1    
print(gcd(56,30))
        


# def gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a

# # Example usage:
# num1 = 3
# num2 = 6
# result = gcd(num1, num2)
# print(f"GCD({num1}, {num2}) = {result}")
