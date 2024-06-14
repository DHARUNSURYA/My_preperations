def valy(steps,path):
    vally_count=0
    sea_level=0
    in_valley=False
    for step in path:
        if step=='U':
            sea_level+=1
            if sea_level==0 and in_valley:
                vally_count+=1
                in_valley=False
        elif step=='D':
            sea_level-=1
            if sea_level<0 and not in_valley:
                in_valley=True
    return vally_count
steps = 8
path = "UDDDUDUU"
print(valy(steps, path))             





# def countingValleys(steps, path):
#     sea_level = 0
#     valley_count = 0
#     in_valley = False
    
#     for step in path:
#         if step == 'U':
#             sea_level += 1
#             if sea_level == 0 and in_valley:
#                 valley_count += 1
#                 in_valley = False
#         elif step == 'D':
#             sea_level -= 1
#             if sea_level < 0 and not in_valley:
#                 in_valley = True
    
#     return valley_count

# # Example usage:
# steps = 8
# path = "UDDDUDUU"
# print(countingValleys(steps, path))  # Output: 1
