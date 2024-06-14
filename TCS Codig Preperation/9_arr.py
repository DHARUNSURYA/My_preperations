def pairs(k, arr):
    element_set = set(arr)
    count = 0
    
    for x in arr:
        if (x + k) in element_set:
            count += 1
        if (x - k) in element_set:
            count += 1
    
    # Each valid pair (x, y) and (y, x) will be counted twice
    return count // 2

# Read input values
n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Call the pairs function and print the result
print(pairs(k, arr))
