# # Read the size of the array
# N = int(input("Enter the size of the array: "))

# # Initialize a variable to keep track of the count
# count = 0

# # Initialize a variable to keep track of the maximum value seen so far
# max_so_far = float('-inf')

# # Iterate through the array
# for i in range(N):
#     # Read the value of the current element
#     value = int(input(f"Enter the value of Arr[{i}]: "))
    
#     # Check if the current element is greater than the maximum value seen so far
#     if value > max_so_far:
#         # Update the maximum value seen so far
#         max_so_far = value
#         # Increment the count
#         count += 1

# # Print the count of elements greater than all of their prior elements
# print("Output:", count)


# import sys
# n=int(input())
# c=0
# m=-sys.maxsize-1
# while n:
#     n-=1
#     a=int(input())
#     if a>m:
#         m=a
#         c+=1
# print(c)


n=int(input("Enter: "))

count=0
maxval=float('-inf')

for i in range(n):
    a=int(input(f"Enter Array {i}: "))
    
    if a>maxval:
        count+=1
        maxval=a
        
print(count)        