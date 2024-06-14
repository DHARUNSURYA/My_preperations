def halfsorted(arr):
    mid=len(arr)//2
    first_hald=sorted(arr[:mid])
    secoun_half=sorted(arr[mid:],reverse=True)
    return first_hald+secoun_half
input_str = "7 2 5 9 8"
arr = list(map(int, input_str.split()))
print(f"Unsorted input: {arr}")
sorted_result = halfsorted(arr)
print(f'Sorted output : {sorted_result}')
