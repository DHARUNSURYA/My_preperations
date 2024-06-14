# def get_total_mints(n, length):
#     if 2 < n < 10 and 1 < length < 20:
#         total_mints = n
#         previous_child_mints = n
#         for i in range(2, length + 1):
#             current_child_mints = previous_child_mints * 2 - 1
#             total_mints += current_child_mints
#             previous_child_mints = current_child_mints
#         return total_mints
#     else:
#         return "Invalid input"

# # Example usage:
# n = 4  # Number of mints with the first kid
# length = 2  # Length of the queue

# print(get_total_mints(n, length))

# def findmints(n,length):
#     if 2<n<100 and 1<length<20:
#         totalments=n
#         pments=n
#         for i in range(2,length+1):
#             cments=pments*2-1
#             totalments+=cments
#             pments=cments
#         return totalments
#     else:
#         return "INVALID INPUT"
    
# print(findmints(4,2))   

def cal(s,n):
    sum=s
    for _ in range(1,n):
        prev=sum-1
        sum+=prev
    return sum
print(cal(14,4))  # 7
        
        