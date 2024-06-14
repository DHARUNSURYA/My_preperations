def ispalindrome(n):
    ns=str(n)
    if ns[::-1]==ns:
        return "Yes"
    else:
        return "No"
input_1 = 555
output_1 = ispalindrome(input_1)
print(f"Input: {input_1}\nOutput: {output_1}")  # Output: Yes

input_2 = 123
output_2 = ispalindrome(input_2)
print(f"Input: {input_2}\nOutput: {output_2}")  # Output: No    