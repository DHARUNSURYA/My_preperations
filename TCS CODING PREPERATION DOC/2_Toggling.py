#import math
#n=int(input())
#k=(1<<int(math.log2(n))+1)-1
#print(n^k)


#another code

# def toggle_bit(n):
#     num_bits=n.bit_length()
#     mask=(1<<num_bits)-1
#     result = n ^ mask
#     return result
# n=int(input("Enter an integer: "))
# print(toggle_bit(n))

def rool(n):
    bl=n.bit_length()
    mask=(1<<bl)-1
    result=n^mask
    return result
print(rool(5))

import math
n=5
k=(1<<int(math.log2(n))+1)-1
print(n^k)