def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def generate_prime(n, m):
    primes = []
    for i in range(n, m + 1):
        if is_prime(i):
            primes.append(i)
    return primes

def count_prime_pairs(primes):
    count = 0
    for i in range(len(primes)):
        for j in range(len(primes)):
            if primes[i]-primes[j]==6:
                count += 1
    return count            
if __name__ == "__main__":
    n = int(input("Enter the starting number (n): "))
    m = int(input("Enter the ending number (m): "))
    
    prime_numbers = generate_prime(n, m)
    count = count_prime_pairs(prime_numbers)
    
    if count == 0:
        print("No Prime Pairs")
    else:
        print("Count of prime pairs with difference 6:", count)




















# def is_prime(num):
#     """Check if a number is prime."""
#     if num <= 1:
#         return False
#     if num == 2:
#         return True  # 2 is a prime number
#     if num % 2 == 0:
#         return False  # Even number greater than 2 is not a prime
#     for i in range(3, int(num ** 0.5) + 1, 2):
#         if num % i == 0:
#             return False
#     return True

# def generate_primes(n, m):
#     """Generate a list of prime numbers in the range [n, m]."""
#     primes = []
#     for num in range(n, m + 1):
#         if is_prime(num):
#             primes.append(num)
#     return primes

# def count_prime_pairs(primes):
#     """Count prime pairs with a difference of 6."""
#     count = 0
#     for i in range(len(primes) - 1):
#         if primes[i + 1] - primes[i] == 6:
#             count += 1
#     return count

# if __name__ == "__main__":
#     n = int(input("Enter the lower bound (n): "))
#     m = int(input("Enter the upper bound (m): "))
    
#     primes = generate_primes(n, m)
#     prime_pairs_count = count_prime_pairs(primes)
    
#     if prime_pairs_count > 0:
#         print(prime_pairs_count)
#     else:
#         print("No Prime Pairs")
