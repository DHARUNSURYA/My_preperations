 # base10_value=0
    # lenghth=len(base17_str)
    # for i in range(lenghth):
    #     char = base17_str[lenghth-1-i]
    #     value=char_to_value[char]
    #     base10_value+=value*(17**i)
    # return base10_value
def base17_to_base10(base17_str):
    # Mapping of characters to their respective values
    char_to_value = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16
    }    
    base10=0
    lenght=len(base17_str)
    for i in range(lenght):
        char=base17_str[lenght-1-i]
        value=char_to_value[char]
        base10+=value *(17**i)
    return base10     
print(base17_to_base10("1A"))