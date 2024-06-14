# def final_position(n):
#     # Starting coordinates
#     x, y = 0, 0
    
#     # Define movements: right, up, left, down
#     directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
#     # Distance to be traveled in each step, starting from 10 units
#     distance = 10
    
#     # Iterate through each step
#     for i in range(n):
#         # Determine the direction for the current step
#         direction = directions[i % 4]
        
#         # Update the position based on the direction and distance
#         x += direction[0] * distance
#         y += direction[1] * distance
        
#         # Increase the distance for the next step
#         distance += 10
    
#     return (x, y)

# # Example usage
# n = 3
# print(final_position(n))  # Output for input 3

# # For the given input 3, the expected output should be the final position after 3 steps

def finalpo(n):
    x,y=0,0
    directions=[(1,0),(0,1),(-1,0),(0,-1)]
    distance=10
    
    for i in range(n):
        direction=directions[i%4]
        x+=direction[0]*distance
        y+=direction[1]*distance
        
        distance+=10
    return (x,y)    

print(finalpo(3))