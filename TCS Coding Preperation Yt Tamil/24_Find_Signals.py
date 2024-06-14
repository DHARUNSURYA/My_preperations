def max_count(nos):
    max_count=0
    current_count=0
    for char in nos:
        if char == '1':
            current_count += 1
            max_count=max(max_count,current_count)
        else:
            current_count=0
    return max_count
binary_number = "1010011"
print(max_count(binary_number))  # Output: 2









# def max_consecutive_ones(binary_str):
#     max_count = 0  # Variable to store the maximum count of consecutive '1's
#     current_count = 0  # Variable to store the current count of consecutive '1's
    
#     for char in binary_str:
#         if char == '1':
#             current_count += 1
#             max_count = max(max_count, current_count)
#         else:
#             current_count = 0  # Reset current count if we encounter '0'
    
#     return max_count

# # Example usage:
# binary_number = "101001"
# print(max_consecutive_ones(binary_number))  # Output: 4
