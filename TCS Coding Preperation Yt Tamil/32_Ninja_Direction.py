def cal(n):
    directions=[(1,0),(0,1),(-1,0),(0,-1)]
    distance=10
    x,y=0,0
    for i in range(n):
        direction=directions[i%4]
        x+=direction[0]*distance
        y+=direction[1]*distance
        distance+=10
    return(x,y)
print(cal(5))    