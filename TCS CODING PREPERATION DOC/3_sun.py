from collections import defaultdict

m=defaultdict(int)

m["mon"]=6
m["tue"]=5
m["wed"]=4
m["thu"]=3
m["fri"]=2
m["sat"]=1
m["sun"]=0


s=input()
a=int(input())

today=m[s[0:3]]
remaining=a-today
if remaining>=1:
    ans=1+(remaining-1)//7
else:
    ans=0    
print(ans)    

# from collections import defaultdict

# m = defaultdict(int)

# m["mon"] = 6
# m["tue"] = 5
# m["wed"] = 4
# m["thu"] = 3
# m["fri"] = 2
# m["sat"] = 1
# m["sun"] = 0

# # Function to test
# def calculate_weeks(start_day, days):
#     today = m[start_day[0:3]]
#     if days - today >= 1:
#         ans = 1 + (days - today - 1) // 7
#     else:
#         ans = 0
#     return ans

# # Test case
# print(calculate_weeks("mon", 13))  # Expected output should be 2
