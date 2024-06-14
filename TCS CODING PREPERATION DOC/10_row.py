# r = int(input())  # Number of rows
# c = int(input())  # Number of columns

# sum = 0
# m = 0
# id = 0

# for i in range(r):
#     for j in range(c):
#         sum += int(input())  # Read the parking space status (0 or 1)
#     if sum > m:
#         m = sum
#         id = i + 1
#     sum = 0  # Reset sum for the next row

# print(id)
r=int(input('r: '))
c=int(input('c: '))

previous_check_or_to_find=0
sum=0
id=0
for i in range(r):
    for j in range(c):
        sum+=int(input('Enter: '))
    if sum>previous_check_or_to_find:
           previous_check_or_to_find=sum
           id=i+1
    sum=0
print(id)    