# # Read the number of elements
# n = int(input("Enter the number of elements: "))

# # Read the elements into a list
# a = list(map(int, input("Enter the elements separated by spaces: ").split()))

# # Sort the list using the sorted() function
# a = sorted(a)

# # Print the sorted array
# for num in a:
#     print(num, end=" ")

n = int(input("Enter the number of elements: "))
a = list(map(int, input("Enter the elements separated by spaces: ").split()))
sn=sorted(a)

n=len(a)

for i in range(n-1):
    for j in range(n-i-1):
        if a[j] > a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
            
for i in a:
    print(i, end=" ")
# for i in sn:
#     print(i,end=' ')    
