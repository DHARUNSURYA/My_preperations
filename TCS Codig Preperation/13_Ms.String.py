# def get_textual_representation(number):
#     # Define textual representations for numbers 0 to 9
#     textual_repr = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
#     return textual_repr[number]

# def count_vowels(text):
#     # Count the number of vowels (a, e, i, o, u) in the given text
#     vowels = "aeiou"
#     return sum(1 for char in text if char in vowels)

# def find_pairs_with_sum(numbers, target_sum):
#     pairs = set()
#     seen = set()
#     for num in numbers:
#         complement = target_sum - num
#         if complement in seen:
#             pairs.add((min(num, complement), max(num, complement)))
#         seen.add(num)
#     return pairs

# def main():
#     N = int(input())
#     numbers = list(map(int, input().split()))

#     # Calculate digit D
#     textual_repr_numbers = [get_textual_representation(num) for num in numbers]
#     vowels_count = sum(count_vowels(text) for text in textual_repr_numbers)
#     digit_D = vowels_count

#     # Find unordered pairs that sum up to digit D
#     pairs = find_pairs_with_sum(numbers, digit_D)

#     # Output
#     if len(pairs) > 100:
#         print("greater 100")
#     else:
#         print(get_textual_representation(len(pairs)))

# if __name__ == "__main__":
#     main()



def gettex(number):
    t=["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    return t[number]
def counttext(tet):
    v='aeiou'
    return sum(1 for t in tet if t in v)
    
def fin(num,target):
    pair=set()
    seen=set()
    for n in num:
        complements= target-n
        if complements in seen:
            pair.add((min(n,complements),max(n,complements)))
        seen.add(n)
    return pair    
def main():
    n=int(input())
    numbers=list(map(int,input().split()))
    
    text_re=[gettex(num) for num in numbers]
    vcount=sum(counttext(t) for t in text_re)
    print(vcount)
    digit_s=vcount
    
    pairs=fin(numbers,digit_s)
    
    if len(pairs) >100:
        print("Greater 100")
    else:
        print(gettex(len(pairs)))
    
    
if __name__ =="__main__":
    main()
    
       
