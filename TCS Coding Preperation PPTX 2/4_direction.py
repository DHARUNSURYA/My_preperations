# def f(n):
#     x,y= 0, 0
#     directions=[(10,0),(0,10),(-10,0),(0,-10)]
    
#     for i in range(1,n+1):
#         direction=directions[(i-1)%4]
#         x+=direction[0]*(i//4+1)
#         y+=direction[1]*(i//4+1)
#     return(x,y)    

# print(f(1))

def f(n):   
    x,y =0,0
    directions=[(10,0),(0,10),(-10,0),(0,-10)]
    for i in range(n):
        direction=directions[i%4]
        x+=direction[0]*(i//4+1)
        y+=direction[1]*(i//4+1)
    return (x,y)   
print(f(3))    
