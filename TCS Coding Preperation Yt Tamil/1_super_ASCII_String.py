def superasci(s):
    char_count=[0]*26
    for char in s:
        index=ord(char)-ord('a')
        char_count[index]+=1
    for i in range(26):
        if char_count[i]!=0:
            position=i+1
            if char_count[i]!=position:
                return "No"
    return "Yes"
i="bba"
print(superasci(i))        
                










# def is_super_ascii_string(s):
#     # Create a list to store the count of each character
#     char_count = [0] * 26

#     # Loop through each character in the string
#     for char in s:
#         # Calculate the position of the character in the alphabet (0-based index)
#         index = ord(char) - ord('a')
#         # Increment the count for this character
#         char_count[index] += 1

#     # Check the super ASCII condition
#     for i in range(26):
#         if char_count[i] != 0:
#             # Position in the alphabet (1-based index)
#             position = i + 1
#             if char_count[i] != position:
#                 return "No"

#     return "Yes"

# # Example 1
# input_string_1 = "bba"
# output_1 = is_super_ascii_string(input_string_1)
# print(f"Input: {input_string_1}")
# print(f"Output: {output_1}")

# # Example 2
# input_string_2 = "ssba"
# output_2 = is_super_ascii_string(input_string_2)
# print(f"Input: {input_string_2}")
# print(f"Output: {output_2}")
