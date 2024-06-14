def ispanagram(s):
    s=s.lower()
    alpha_set=set()
    for char in s:
        if 'a'<=char<='z':
            alpha_set.add(char)
    if len(alpha_set)==26:
        return 1
    else:
        return 0
# Example usage:
input_1 = "Pack mY box witH fIve dozen liquor jugs"
output_1 = ispanagram(input_1)
print(f"Input: {input_1}\nOutput: {output_1}")  # Output: 1

input_2 = "geeksFORgeeks"
output_2 = ispanagram(input_2)
print(f"Input: {input_2}\nOutput: {output_2}")  # Output: 0       