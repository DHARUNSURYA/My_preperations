def trailing_zero(n):
    count=0
    pow=5
    while n>=pow:
        count+=n//pow
        pow*=5
    return count
print(trailing_zero(190))    