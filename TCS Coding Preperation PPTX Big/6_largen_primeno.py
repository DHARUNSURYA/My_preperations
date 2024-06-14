def find_large_prime_no(n,p):
    result=0
    while n>=p:
        result+=n//p
        n=n//p
    return result    
    
if __name__=="__main__":
    n,p=map(int,input("Enter n,p : ").split(","))
    print(find_large_prime_no(n,p))
    



# def largest_power_of_prime(N, p):
#     # Initialize the result to 0
#     result = 0
    
#     # Calculate the exponent of p in N!
#     while N >= p:
#         result += N // p
#         N //= p
    
#     return result

# # Main function
# if __name__ == "__main__":
#     T = int(input("Enter the number of test cases: "))
#     for _ in range(T):
#         N, p = map(int, input("Enter N and p: ").split())
#         largest_power = largest_power_of_prime(N, p)
#         print("Largest power of prime p:", largest_power)
