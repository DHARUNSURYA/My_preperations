def sumofminabsdiffrence(arr, n):
    if n < 2:
        return 0
    
    arr.sort()
    sum_diff = 0
    
    # Calculate absolute differences for each element
    for i in range(1, n - 1):
        diff1 = abs(arr[i] - arr[i - 1])  # Difference with previous element
        diff2 = abs(arr[i] - arr[i + 1])  # Difference with next element
        sum_diff += min(diff1, diff2)
    
    # Add differences for the first and last elements
    sum_diff += abs(arr[1] - arr[0])  # Difference for the first element
    sum_diff += abs(arr[n - 1] - arr[n - 2])  # Difference for the last element
    
    return sum_diff

# Example usage:
if __name__ == "__main__":
    # Example 1
    arr1 = [4, 1, 5]
    N1 = len(arr1)
    print("Friendliness of array:", sumofminabsdiffrence(arr1, N1))  # Output: 5
    
    # Example 2
    arr2 = [1, 1, 1]
    N2 = len(arr2)
    print("Friendliness of array:", sumofminabsdiffrence(arr2, N2))  # Output: 0
